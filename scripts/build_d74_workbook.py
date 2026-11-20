"""Build the SUREWAVE D7.4 cost workbook v3 (Excel) from the v2 workbook.

The v2 input sheets (in_gen, in_loc, inter_gen, freight, harbors, aggregates)
are carried over unchanged, except: an end-of-life input section is appended
to in_gen, and formula headers are replaced by literal text. All calculation
sheets are rebuilt with formulas that work in desktop Excel and LibreOffice
(no LAMBDA, MAP, SCAN, FILTER, SEQUENCE, UNIQUE, MINIFS):

- pontoons   pontoon sub-model: cost per design and pontoon type (SUMIFS),
             cheapest design per type (MIN), totals per installation size
- out_loc    one column per case (27 main cases + sensitivity cases)
- cf         year-by-year cash flows per case (years 0..55)
- summary    headline results for the 27 main cases
- sens_*     sensitivity tables, live from the sensitivity case columns
- README     version, conventions, system boundary, change log

Usage:
    python scripts/build_d74_workbook.py <v2.xlsx> <out.xlsx>      # ~2 min

Pipeline (no desktop applications needed): the workbook is assembled with
openpyxl, every formula is evaluated with the `formulas` library, and the file
is written with xlsxwriter with each formula's result stored next to it, so
Excel shows numbers even in Protected View. Excel recalculates on open
(xlsxwriter sets fullCalcOnLoad). scripts/test_d74_cost_model.py compares
every formula result with the independent Python model in d74_cost_model.py.

Python packages: openpyxl, xlsxwriter, formulas (pulls in numpy).
"""
from __future__ import annotations

import sys
from pathlib import Path

import openpyxl
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter as col

sys.path.insert(0, str(Path(__file__).resolve().parent))
from d74_cost_model import (LOCATIONS, CASES, IRR_GRID_TOP, IRR_GRID_BOTTOM,  # noqa: E402
                            IRR_GRID_STEP)

VERSION = "3.0"
N_GRID = int(round((IRR_GRID_TOP - IRR_GRID_BOTTOM) / IRR_GRID_STEP)) + 1
NY = 56                         # years 0..55 in the cash-flow sheet (max horizon 26 x 2 = 52)
SENS_LOCS = ["n_10", "b_10", "m_10"]
SENS_RATES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
DESIGNS = ["O0 Conv Ref", "O1 Conv LWAC", "O2 Hybrid", "O3 Sure LWAC", "O4 Sure HPC"]
PTYPES = ["Breakwater", "Bridge1968", "Bridge1830"]
INSTALLS = ["10MW", "2MW_5"]
# Dir values corrected relative to the v2 inputs: (input name, new Dir, note written to the comment column)
DIR_CORRECTIONS = [
    ("solar_energy_target_price", -1,
     "Sale price of the electricity (revenue). Dir -1: a higher price is favourable (v3 correction; v2 had +1, "
     "which gave the pessimistic case the higher price)."),
]

BOLD = Font(bold=True)
HEAD_FILL = PatternFill("solid", fgColor="DDEBF7")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")

EOL_INPUTS = [
    # name, unit, value, dir, comment
    ("decommissioning_pontoons_cost_factor", "factor", 1.0, 1,
     "Cost of removing breakwater, pontoons, anchors and moorings at end of life, as a multiple of the "
     "pontoon installation cost (installation_pontoons_* in in_loc). 1 = removal mirrors installation "
     "(marine crane handling, towing)."),
    ("decommissioning_pv_system_cost_factor", "factor", 1.0, 1,
     "Cost of removing the last PV layer at end of life, as a multiple of the PV installation cost "
     "(installation_pv_system_* in in_loc). Removal of the first PV layer at reinstallation is part of "
     "replacement_of_pv_system_*."),
    ("pv_module_disposal_cost_per_kw", "€ / kW", 0.0, 1,
     "Owner's cost for collection and treatment of removed PV modules, per kW removed, at each removal "
     "(reinstallation and end of life). 0 assumes producer take-back of end-of-life modules; set > 0 to "
     "test."),
    ("residual_value_fraction", "%", 0.0, -1,
     "Value recovered at end of life from structural materials (concrete, steel, mooring), as a share of "
     "their initial cost (pontoons + anchoring and mooring). 0 = no credit taken."),
]


# --------------------------------------------------------------- helpers ----
def name_rows(ws, first=2, col_idx=1) -> dict[str, int]:
    out = {}
    for r in range(first, ws.max_row + 1):
        v = ws.cell(r, col_idx).value
        if isinstance(v, str) and v.strip():
            out.setdefault(v.strip(), r)
    return out


def header(ws, row, values, start_col=1):
    for i, v in enumerate(values):
        c = ws.cell(row, start_col + i, v)
        c.font = BOLD
        c.fill = HEAD_FILL


def build_openpyxl(v2_path: Path) -> openpyxl.Workbook:
    """Build the v3 workbook (formulas, no results) in memory."""
    wb = openpyxl.load_workbook(v2_path)
    for name in ["summary", "out_loc", "pontoons", "sens_discounts", "sens_subsea_cable", "sens_pontoons"]:
        del wb[name]
    # v2 defined name V is a Google Sheets LAMBDA helper not used by any formula
    for n in list(wb.defined_names.keys()):
        del wb.defined_names[n]

    # ------------------------------------------------------------ in_gen ----
    g = wb["in_gen"]
    r0 = 53
    g.cell(r0, 1, "End of life").font = BOLD
    for i, (n, unit, val, d, comment) in enumerate(EOL_INPUTS):
        r = r0 + 1 + i
        g.cell(r, 1, n); g.cell(r, 2, unit); g.cell(r, 3, val).fill = INPUT_FILL
        g.cell(r, 4, d)
        g.cell(r, 5, f"=$C{r}*(1+$C$44*D{r})")
        g.cell(r, 6, f"=$C{r}*(1+$C$44*-D{r})")
        g.cell(r, 7, comment)
    G = name_rows(g)
    # Input corrections relative to v2 (Dir = direction in which a higher value is worse)
    for name, d, why in DIR_CORRECTIONS:
        g.cell(G[name], 4, d)
        old = g.cell(G[name], 7).value
        g.cell(G[name], 7, (f"{old} " if old else "") + why)

    # ------------------------------------------------------------ in_loc ----
    lw = wb["in_loc"]
    loc_cols = []
    for i, k in enumerate(LOCATIONS + [f"{l}_pes" for l in LOCATIONS] + [f"{l}_opt" for l in LOCATIONS]):
        lw.cell(1, 4 + i, k)                    # literal header (v2: formula =D1&"_pes")
        loc_cols.append(k)
    Lr = name_rows(lw)
    ig = wb["inter_gen"]
    IGr = name_rows(ig)

    # ---------------------------------------------------------- pontoons ----
    v2 = openpyxl.load_workbook(v2_path, data_only=True)
    pv2 = v2["pontoons"]
    p = wb.create_sheet("pontoons")
    header(p, 1, ["Pontoon data (weights per design, installation size, pontoon type and material)"])
    header(p, 2, ["Design", "Installation", "Pontoon", "Material", "Total Weight (t)", "Total Cost (€)",
                  "Material", "Cost (€/t)", "Installation", "Pontoon", "Count"])
    rr = 3
    for r in range(3, pv2.max_row + 1):
        a = [pv2.cell(r, k).value for k in range(1, 6)]
        if all(x is not None for x in a):
            for k, x in enumerate(a):
                p.cell(rr, 1 + k, x)
            p.cell(rr, 6, f"=VLOOKUP($D{rr},$G$3:$H$8,2,0)*$E{rr}")
            rr += 1
    last_data = rr - 1
    for r in range(3, 9):
        p.cell(r, 7, pv2.cell(r, 7).value); p.cell(r, 8, pv2.cell(r, 8).value)
        if pv2.cell(r, 8).value is not None:
            p.cell(r, 8).fill = INPUT_FILL
    for r in range(3, 7):
        for k in (9, 10, 11):
            p.cell(r, k, pv2.cell(r, k).value)
    # extras (steel, rubber) as in v2 columns U..Y
    header(p, 2, ["Component", "Installation", "Weight (t)", "Cost/ton (€)", "Total cost (€)"], start_col=21)
    xr = 3
    for r in range(3, pv2.max_row + 1):
        if pv2.cell(r, 21).value and pv2.cell(r, 22).value:
            for k in range(21, 25):
                p.cell(xr, k, pv2.cell(r, k).value)
            p.cell(xr, 23).fill = INPUT_FILL; p.cell(xr, 24).fill = INPUT_FILL
            p.cell(xr, 25, f"=W{xr}*X{xr}")
            xr += 1
    last_x = xr - 1
    # cost grid per installation size: rows = designs, cols = pontoon types
    p.cell(1, 13, "Cost per design and pontoon type (€), cheapest per type, totals").font = BOLD
    rng = lambda c: f"${c}$3:${c}${last_data}"
    grid_rows = {}
    row = 2
    for inst in INSTALLS:
        header(p, row, ["Design", "Installation"] + PTYPES + ["Design total (€)"], start_col=13)
        for d in DESIGNS:
            row += 1
            grid_rows[(inst, d)] = row
            p.cell(row, 13, d); p.cell(row, 14, inst)
            for j, t in enumerate(PTYPES):
                p.cell(row, 15 + j, f'=SUMIFS({rng("F")},{rng("A")},$M{row},{rng("B")},$N{row},{rng("C")},"{t}")')
            p.cell(row, 18, f'=SUM(O{row}:Q{row})+SUMIFS($Y$3:$Y${last_x},$V$3:$V${last_x},$N{row})')
        row += 1
        grid_rows[(inst, "cheapest")] = row
        first = grid_rows[(inst, DESIGNS[0])]; last = grid_rows[(inst, DESIGNS[-1])]
        p.cell(row, 13, "Cheapest per type").font = BOLD; p.cell(row, 14, inst)
        for j in range(3):
            c = col(15 + j)
            p.cell(row, 15 + j, f"=MIN({c}{first}:{c}{last})")
        p.cell(row, 18, f'=SUM(O{row}:Q{row})+SUMIFS($Y$3:$Y${last_x},$V$3:$V${last_x},$N{row})').font = BOLD
        row += 2
    # location totals (Z/AA as in v2)
    header(p, 2, ["Location", "Total Costs (€)"], start_col=26)
    tot = {inst: f"$R${grid_rows[(inst, 'cheapest')]}" for inst in INSTALLS}
    for i, k in enumerate(CASES):
        r = 3 + i
        loc = k.split("_")[0] + "_" + k.split("_")[1]
        size = k.split("_")[1]
        base = {"2": f"{tot['2MW_5']}/5", "25": tot["2MW_5"], "10": tot["10MW"]}[size]
        factor = "" if k == loc else ("*(1+in_gen!$C$44)" if k.endswith("_pes") else "*(1-in_gen!$C$44)")
        p.cell(r, 26, k)
        p.cell(r, 27, f"=({base}){factor}")
    P_LOC = (3, 3 + len(CASES) - 1)
    d10 = (grid_rows[("10MW", DESIGNS[0])], grid_rows[("10MW", DESIGNS[-1])])

    # ------------------------------------------------------------ cases ----
    cases = []  # (id, location, variant, discount_override, cable, design, label)
    for k in CASES:
        loc = "_".join(k.split("_")[:2]); var = k.split("_")[2] if k.count("_") == 2 else "base"
        cases.append((k, loc, var, None, "short", "cheapest"))
    for loc in SENS_LOCS:
        for rate in SENS_RATES:
            cases.append((f"{loc}_r{rate}", loc, "base", rate / 100, "short", "cheapest"))
    for loc in SENS_LOCS:
        cases.append((f"{loc}_subsea", loc, "base", None, "long", "cheapest"))
    for loc in SENS_LOCS:
        for d in DESIGNS:
            cases.append((f"{loc}_{d.split()[0]}", loc, "base", None, "short", d))
    ncase = len(cases)
    C0 = 4  # first case column (D)
    ccol = lambda i: col(C0 + i)
    last_case_col = ccol(ncase - 1)

    o = wb.create_sheet("out_loc")
    cf = wb.create_sheet("cf")
    header(o, 1, ["Parameter", "Unit", "Comment"] + [c[0] for c in cases])

    rows: dict[str, int] = {}
    spec: list[tuple[str, str, str, object]] = []   # name, unit, comment, formula-template or list

    def Gx(n):   # in_gen value for this column's variant
        return f"INDEX(in_gen!$C${G[n]}:$F${G[n]},{{c}}$6)"

    def Lx(n):   # in_loc value for this column
        return f"INDEX(in_loc!$D${Lr[n]}:$AD${Lr[n]},{{c}}$5)"

    def IGx(n):
        return f"INDEX(inter_gen!$C${IGr[n]}:$F${IGr[n]},{{c}}$6)"

    def R(n):    # reference to another out_loc row in the same column
        return f"{{c}}${rows[n]}"

    def add(name, unit, comment, formula):
        rows[name] = 2 + len(spec)
        spec.append((name, unit, comment, formula))

    # case definition rows (2..10): literal per column, written below
    for n, unit, cm in [
        ("location", "", "Location and size key (n/b/m = North Sea/Baltic/Mediterranean; 2 = 2 MW, 25 = 5 × 2 MW, 10 = 10 MW)"),
        ("variant", "", "base / pes (pessimistic) / opt (optimistic): selects in_gen column C/E/F and the in_loc column"),
        ("in_loc_key", "", "in_loc column used by this case"),
        ("in_loc_index", "", "Position of in_loc_key in in_loc!D1:AD1"),
        ("in_gen_index", "", "1 = in_gen!C (base), 3 = E (pes), 4 = F (opt)"),
        ("discount_rate_override", "%", "Sensitivity cases only: discount rate replacing in_gen discount_rate"),
        ("discount_rate", "%", "Discount rate used"),
        ("cable_alternative", "", "short = 300 m floating MV cable to an offshore substation (base case); long = submarine cable to shore (sensitivity)"),
        ("pontoon_design", "", "cheapest = cheapest design per pontoon type (base case); otherwise the design code (sensitivity, 10 MW only)"),
    ]:
        add(n, unit, cm, None)
    rows_def_end = 2 + len(spec)

    add("solar_panels_per_matrix_width", "unit", "",
        f"=FLOOR(({Lx('matrix_side_length')}*1000+{Gx('solar_panel_hinge_length')})/({Gx('solar_panel_width')}+{Gx('solar_panel_hinge_length')}),1)")
    add("solar_panels_per_matrix_length", "unit", "",
        f"=FLOOR(({Lx('matrix_side_length')}*1000+{Gx('solar_panel_hinge_length')})/({Gx('solar_panel_length')}+{Gx('solar_panel_hinge_length')}),1)")
    add("solar_panels_per_matrix", "unit", "", f"={R('solar_panels_per_matrix_width')}*{R('solar_panels_per_matrix_length')}")
    add("solar_matrices_along_radii", "unit", "", f"=CEILING(SQRT({Lx('matrices_per_quadrant')}),1)")
    add("solar_radius", "m", "", f"=CEILING(SQRT(1+{R('solar_matrices_along_radii')}^2)*{Lx('matrix_side_length')},1)+{Gx('pontoon_width')}/2")
    add("total_solar_panels", "unit", "Per ring", f"={R('solar_panels_per_matrix')}*{Lx('matrices_per_quadrant')}*4")
    add("total_dc_cable_cost", "€", "Per ring", f"={Gx('dc_cable_cost_per_m')}*{Gx('dc_cable_per_panel')}*{R('total_solar_panels')}")
    add("total_solar_power", "kW", "Per ring", f"={R('total_solar_panels')}*{Gx('solar_panel_power')}/1000")
    add("solar_container_count", "unit", "Per ring", f"=CEILING({R('total_solar_panels')}/{Gx('panels_per_container')},1)")
    add("total_mv_submarine_cable_cost", "€", "Submarine MV cable to shore incl. installation (used only when cable_alternative = long)",
        f"=({Gx('mv_submarine_cable_cost_per_m')}+{Gx('cable_installation_cost_per_m')})*{Lx('distance_to_shore')}")
    add("total_pvc_cost", "€", "", f"={Gx('pvc_cost')}*{Lx('pvc_pipe_weight')}")
    add("total_rope_cost", "€", "", f"={Gx('polypropylene_cost')}*{Lx('polypropylene_rope_weight')}")
    add("solar_freight_cost", "€", "Rate per container-km from the freight table, by container count (v2 looked up total_pvc_cost)",
        f"={Lx('rings_count')}*{Lx('panel_transport_km')}*{R('solar_container_count')}*VLOOKUP({R('solar_container_count')},freight!$A$2:$B$999,2,1)")
    add("total_pontoon_cost", "€", "From pontoons: cheapest design per pontoon type, or the design named in pontoon_design",
        f'=IF({R("pontoon_design")}="cheapest",INDEX(pontoons!$AA${P_LOC[0]}:$AA${P_LOC[1]},MATCH({R("in_loc_key")},pontoons!$Z${P_LOC[0]}:$Z${P_LOC[1]},0)),'
        f'INDEX(pontoons!$R${d10[0]}:$R${d10[1]},MATCH({R("pontoon_design")},pontoons!$M${d10[0]}:$M${d10[1]},0)))')
    add("total_cost_solar_panels", "€", "", f"={Lx('rings_count')}*{IGx('solar_panel_cost')}*{R('total_solar_power')}")
    add("total_cost_cabling_short_alternative", "€", "DC + AC + 300 m floating MV cable",
        f"={Lx('rings_count')}*({R('total_dc_cable_cost')}+{IGx('total_ac_cable_cost')}+{IGx('total_mv_floating_cable_cost')})")
    add("total_cost_cabling_long_alternative", "€", "DC + AC + submarine MV cable to shore",
        f"={Lx('rings_count')}*({R('total_dc_cable_cost')}+{IGx('total_ac_cable_cost')})+{R('total_mv_submarine_cable_cost')}")
    add("total_cost_cabling", "€", "Cabling alternative used by this case",
        f'=IF({R("cable_alternative")}="long",{R("total_cost_cabling_long_alternative")},{R("total_cost_cabling_short_alternative")})')
    add("total_cost_anchoring_mooring", "€", "",
        f"={Lx('rings_count')}*({Lx('anchor_weight')}*{Gx('anchor_cost_per_t')}+{Lx('chain_weight')}*{Gx('anchor_chain_cost_per_t')})")
    add("total_cost_installation_pontoons", "€", "",
        f"={Lx('rings_count')}*({Lx('installation_pontoons_equipment_cost')}+{Lx('installation_pontoons_fuel_cost')}+{Lx('installation_pontoons_personnel_cost')})")
    add("total_cost_installation_pv_system", "€", "",
        f"={Lx('rings_count')}*({Lx('installation_pv_system_equipment_cost')}+{Lx('installation_pv_system_fuel_cost')}+{Lx('installation_pv_system_personnel_cost')})")
    add("total_cost_installation", "€", "", f"={R('total_cost_installation_pontoons')}+{R('total_cost_installation_pv_system')}")
    add("total_inverters_transformers_cost", "€", "New in v3 (input existed in v2 but was not used)",
        f"={Lx('rings_count')}*{Lx('inverters_transformers_cost')}")
    add("total_scada_cost", "€", "New in v3 (input existed in v2 but was not used)", f"={Lx('rings_count')}*{IGx('scada_system')}")
    add("total_capex_cost", "€", "Excludes the substation and, in the base case, the export cable to shore",
        "=" + "+".join(R(n) for n in ["total_pvc_cost", "total_rope_cost", "solar_freight_cost", "total_pontoon_cost",
                                       "total_cost_solar_panels", "total_cost_cabling", "total_cost_anchoring_mooring",
                                       "total_cost_installation", "total_inverters_transformers_cost", "total_scada_cost"]))
    add("solar_lifetime_years", "y", "PV layer lifetime", f"=ROUND({Gx('solar_lifetime')},0)")
    add("solar_lifetimes", "unit", "PV lifetimes per structure lifetime", f"=ROUND({Gx('solar_lifetimes_per_wavebreaker_lifetime')},0)")
    add("horizon_years", "y", "Operating life of the structure = PV lifetime × PV lifetimes", f"={R('solar_lifetime_years')}*{R('solar_lifetimes')}")
    add("yearly_production_new_modules", "kWh", "Production in a year with new modules (age 0)",
        f"={Lx('rings_count')}*{R('total_solar_power')}*{Lx('solar_production_yearly')}*(1-{Lx('solar_wave_loss')})*(1+{Gx('solar_extra_production_from_cooling')})")
    add("yearly_om_cost", "€", "PV O&M per kW + pontoon maintenance (v2 left out the pontoon maintenance inputs)",
        f"={Lx('rings_count')}*{R('total_solar_power')}*{Lx('solar_maintenance_cost_per_kw_per_year')}"
        f"+{Lx('rings_count')}*({Lx('maintenance_pontoons_equipment_cost')}+{Lx('maintenance_pontoons_fuel_cost')}+{Lx('maintenance_pontoons_personnel_cost')})")
    add("pv_disposal_cost", "€", "Disposal of one removed PV layer", f"={Gx('pv_module_disposal_cost_per_kw')}*{Lx('rings_count')}*{R('total_solar_power')}")
    add("reinstallation_cost", "€", "Nominal cost at each PV reinstallation: new modules, replacement work, disposal of removed modules. "
        "Inverter replacements are covered by inverters_transformers_cost in CAPEX (D7.4 §4.3.1)",
        f"={R('total_cost_solar_panels')}+{Lx('rings_count')}*({Lx('replacement_of_pv_system_equipment_cost')}+{Lx('replacement_of_pv_system_fuel_cost')}+{Lx('replacement_of_pv_system_personnel_cost')})"
        f"+{R('pv_disposal_cost')}")
    add("end_of_life_cost", "€", "Nominal cost in the last year: removal of structure and PV, disposal, minus residual value",
        f"={Gx('decommissioning_pontoons_cost_factor')}*{R('total_cost_installation_pontoons')}"
        f"+{Gx('decommissioning_pv_system_cost_factor')}*{R('total_cost_installation_pv_system')}+{R('pv_disposal_cost')}"
        f"-{Gx('residual_value_fraction')}*({R('total_pontoon_cost')}+{R('total_cost_anchoring_mooring')})")
    add("energy_price", "€/kWh", "", f"={Gx('solar_energy_target_price')}")

    # cash flow blocks (sheet cf): rows per block = header + NY years
    blocks = ["operating", "module_age", "production", "om_cost", "capex", "reinstallation", "end_of_life",
              "revenue", "net_cash_flow", "discount_factor", "cumulative_discounted_net", "payback_flag"]
    B = {b: 2 + i * (NY + 1) for i, b in enumerate(blocks)}   # header row of each block
    B["npv_at_rate"] = 2 + len(blocks) * (NY + 1)
    B["npv_nonnegative"] = B["npv_at_rate"] + N_GRID + 1
    yr = lambda b: (B[b] + 1, B[b] + NY)                       # first/last year row
    cfr = lambda b: f"cf!{{c}}${yr(b)[0]}:{{c}}${yr(b)[1]}"
    add("total_solar_production", "kWh", "Discounted lifetime production", f"=SUMPRODUCT({cfr('production')},{cfr('discount_factor')})")
    add("total_maintenance_cost", "€", "Discounted lifetime O&M", f"=SUMPRODUCT({cfr('om_cost')},{cfr('discount_factor')})")
    add("total_solar_reinstall_cost", "€", "Discounted reinstallation cost", f"=SUMPRODUCT({cfr('reinstallation')},{cfr('discount_factor')})")
    add("total_end_of_life_cost", "€", "Discounted end-of-life cost", f"=SUMPRODUCT({cfr('end_of_life')},{cfr('discount_factor')})")
    add("total_lifetime_cost", "€", "CAPEX + discounted O&M, reinstallation and end of life",
        f"={R('total_capex_cost')}+{R('total_maintenance_cost')}+{R('total_solar_reinstall_cost')}+{R('total_end_of_life_cost')}")
    add("lcoe", "€/kWh", "Discounted lifetime cost / discounted lifetime production", f"={R('total_lifetime_cost')}/{R('total_solar_production')}")
    add("total_revenue", "€", "Discounted revenue", f"=SUMPRODUCT({cfr('revenue')},{cfr('discount_factor')})")
    add("npv", "€", "Net present value", f"={R('total_revenue')}-{R('total_lifetime_cost')}")
    add("roi", "%", "NPV / CAPEX", f"={R('npv')}/{R('total_capex_cost')}")
    add("payback_period", "y", "First year in which cumulative discounted net cash flow is ≥ 0",
        f'=IFERROR(INDEX(cf!$B${yr("payback_flag")[0]}:$B${yr("payback_flag")[1]},MATCH(1,{cfr("payback_flag")},0)),"-")')
    gr = (B["npv_at_rate"] + 1, B["npv_at_rate"] + N_GRID)
    add("irr_guess", "%", "Highest grid rate (1 % steps, 50 % to -10 %) with NPV ≥ 0 (see cf, block npv_at_rate)",
        f'=IFERROR(INDEX(cf!$B${gr[0]}:$B${gr[1]},MATCH(1,cf!{{c}}${B["npv_nonnegative"] + 1}:{{c}}${B["npv_nonnegative"] + N_GRID},0)),"-")')
    add("irr", "%", "Internal rate of return on undiscounted net cash flows, year 0 to end of life: the highest rate at "
        "which NPV = 0 (late outflows can give several roots)",
        f'=IF({R("irr_guess")}="-","-",IFERROR(IRR({cfr("net_cash_flow")},{R("irr_guess")}),"-"))')

    # write out_loc
    for i, (n, unit, cm, f) in enumerate(spec):
        r = 2 + i
        o.cell(r, 1, n); o.cell(r, 2, unit); o.cell(r, 3, cm)
        if r < rows_def_end:
            o.cell(r, 1).font = Font(italic=True)
    for j, (cid, loc, var, drate, cable, design) in enumerate(cases):
        c = ccol(j)
        o[f"{c}{rows['location']}"] = loc
        o[f"{c}{rows['variant']}"] = var
        o[f"{c}{rows['in_loc_key']}"] = f'=IF({c}{rows["variant"]}="base",{c}{rows["location"]},{c}{rows["location"]}&"_"&{c}{rows["variant"]})'
        o[f"{c}{rows['in_loc_index']}"] = f"=MATCH({c}{rows['in_loc_key']},in_loc!$D$1:$AD$1,0)"
        o[f"{c}{rows['in_gen_index']}"] = f'=IF({c}{rows["variant"]}="pes",3,IF({c}{rows["variant"]}="opt",4,1))'
        if drate is not None:
            o[f"{c}{rows['discount_rate_override']}"] = drate
            o[f"{c}{rows['discount_rate_override']}"].fill = INPUT_FILL
        o[f"{c}{rows['discount_rate']}"] = (f"=IF(ISNUMBER({c}{rows['discount_rate_override']}),{c}{rows['discount_rate_override']},"
                                             f"INDEX(in_gen!$C${G['discount_rate']}:$F${G['discount_rate']},{c}$6))")
        o[f"{c}{rows['cable_alternative']}"] = cable
        o[f"{c}{rows['pontoon_design']}"] = design
        for i, (n, unit, cm, f) in enumerate(spec):
            if f is not None:
                o.cell(2 + i, C0 + j, f.replace("{c}", c))
    assert rows["in_loc_index"] == 5 and rows["in_gen_index"] == 6, rows

    # write cf
    cf.cell(1, 1, "Year-by-year cash flows per case (columns as in out_loc). Year 0 = construction; "
                  "operation in years 1..horizon_years.").font = BOLD
    for j, cs in enumerate(cases):
        cf.cell(1, C0 + j, cs[0]).font = BOLD
    OL = lambda n, c: f"out_loc!{c}${rows[n]}"
    for b in blocks:
        h = B[b]
        cf.cell(h, 1, b).font = BOLD; cf.cell(h, 1).fill = HEAD_FILL
        for t in range(NY):
            r = h + 1 + t
            cf.cell(r, 2, t)
            for j in range(ncase):
                c = ccol(j)
                op = f"{c}{yr('operating')[0] + t}"
                if b == "operating":
                    f = f"=IF(AND($B{r}>=1,$B{r}<={OL('horizon_years', c)}),1,0)"
                elif b == "module_age":
                    f = f"=IF({op}=1,MOD($B{r}-1,{OL('solar_lifetime_years', c)}),0)"
                elif b == "production":
                    age = f"{c}{yr('module_age')[0] + t}"
                    f = (f"={op}*{OL('yearly_production_new_modules', c)}*(1-INDEX(in_loc!$D${Lr['solar_degradation_yearly']}:"
                         f"$AD${Lr['solar_degradation_yearly']},out_loc!{c}$5)*{age})")
                elif b == "om_cost":
                    f = f"={op}*{OL('yearly_om_cost', c)}"
                elif b == "capex":
                    f = f"=IF($B{r}=0,{OL('total_capex_cost', c)},0)"
                elif b == "reinstallation":
                    f = (f"=IF(AND($B{r}>0,$B{r}<{OL('horizon_years', c)},MOD($B{r},{OL('solar_lifetime_years', c)})=0),"
                         f"{OL('reinstallation_cost', c)},0)")
                elif b == "end_of_life":
                    f = f"=IF($B{r}={OL('horizon_years', c)},{OL('end_of_life_cost', c)},0)"
                elif b == "revenue":
                    f = f"={OL('energy_price', c)}*{c}{yr('production')[0] + t}"
                elif b == "net_cash_flow":
                    f = (f"={c}{yr('revenue')[0] + t}-{c}{yr('om_cost')[0] + t}-{c}{yr('capex')[0] + t}"
                         f"-{c}{yr('reinstallation')[0] + t}-{c}{yr('end_of_life')[0] + t}")
                elif b == "discount_factor":
                    f = f"=1/(1+{OL('discount_rate', c)})^$B{r}"
                elif b == "cumulative_discounted_net":
                    prev = "0" if t == 0 else f"{c}{r - 1}"
                    f = f"={prev}+{c}{yr('net_cash_flow')[0] + t}*{c}{yr('discount_factor')[0] + t}"
                elif b == "payback_flag":
                    f = f"=IF(AND($B{r}>0,{c}{yr('cumulative_discounted_net')[0] + t}>=0),1,0)"
                cf.cell(r, C0 + j, f)
    # IRR helper: NPV of the net cash flows on a rate grid (descending), and a >= 0 flag
    yrs = f"$B${yr('net_cash_flow')[0]}:$B${yr('net_cash_flow')[1]}"
    for b in ("npv_at_rate", "npv_nonnegative"):
        h = B[b]
        cf.cell(h, 1, b).font = BOLD; cf.cell(h, 1).fill = HEAD_FILL
        cf.cell(h, 2, "rate").font = BOLD
        for i in range(N_GRID):
            r = h + 1 + i
            cf.cell(r, 2, round(IRR_GRID_TOP - i * IRR_GRID_STEP, 6))
            for j in range(ncase):
                c = ccol(j)
                if b == "npv_at_rate":
                    net = f"{c}${yr('net_cash_flow')[0]}:{c}${yr('net_cash_flow')[1]}"
                    f = f"=SUMPRODUCT({net}/(1+$B{r})^{yrs})"
                else:
                    f = f"=IF({c}{B['npv_at_rate'] + 1 + i}>=0,1,0)"
                cf.cell(r, C0 + j, f)
    cf.freeze_panes = "D2"

    # ----------------------------------------------------------- summary ----
    s = wb.create_sheet("summary")
    header(s, 1, [None] + CASES)
    srows = [("CAPEX (€)", "total_capex_cost"), ("OPEX (€)", "total_maintenance_cost"),
             ("Reinstallation (€)", "total_solar_reinstall_cost"), ("End of life (€)", "total_end_of_life_cost"),
             ("Revenue (€)", "total_revenue"), ("LCOE (€/kWh)", "lcoe"), ("NPV (€)", "npv"), ("ROI (%)", "roi"),
             ("Payback (y)", "payback_period"), ("IRR (%)", "irr")]
    for i, (label, n) in enumerate(srows):
        s.cell(2 + i, 1, label).font = BOLD
        for j, k in enumerate(CASES):
            s.cell(2 + i, 2 + j, f"=out_loc!{ccol(j)}{rows[n]}")
    s.cell(13, 1, "Discounted values at the case discount rate. OPEX, reinstallation and end of life are present values; "
                  "CAPEX is in year 0.")

    # ------------------------------------------------------ sensitivities ----
    idx = {cs[0]: j for j, cs in enumerate(cases)}
    kpis = [("CAPEX (€)", "total_capex_cost"), ("OPEX (€)", "total_maintenance_cost"), ("Revenue (€)", "total_revenue"),
            ("LCOE (€/kWh)", "lcoe"), ("NPV (€)", "npv"), ("ROI (%)", "roi"), ("Payback (y)", "payback_period"),
            ("IRR (%)", "irr")]

    def sens_sheet(name, label, values):  # values: list of (display, {loc: case id})
        ws = wb.create_sheet(name)
        header(ws, 1, ["Parameter", label] + SENS_LOCS)
        r = 2
        for disp, m in values:
            for klabel, n in kpis:
                ws.cell(r, 1, klabel); ws.cell(r, 2, disp)
                for j, loc in enumerate(SENS_LOCS):
                    ws.cell(r, 3 + j, f"=out_loc!{ccol(idx[m[loc]])}{rows[n]}")
                r += 1
        return ws

    sens_sheet("sens_discounts", "Discount rate (%)",
               [(rate, {l: f"{l}_r{rate}" for l in SENS_LOCS}) for rate in SENS_RATES])
    sens_sheet("sens_subsea_cable", "Subsea cable",
               [("Yes", {l: f"{l}_subsea" for l in SENS_LOCS}), ("No", {l: l for l in SENS_LOCS})])
    sens_sheet("sens_pontoons", "Pontoon design",
               [(d, {l: f"{l}_{d.split()[0]}" for l in SENS_LOCS}) for d in DESIGNS])

    # ------------------------------------------------------------ README ----
    rd = wb.create_sheet("README", 0)
    lines = README_LINES
    for i, line in enumerate(lines):
        rd.cell(1 + i, 1, line)
        if i == 0 or (line and not line.startswith((" ", "-", "•")) and line.endswith(":")):
            rd.cell(1 + i, 1).font = BOLD
    rd.column_dimensions["A"].width = 140

    # ------------------------------------------------------------ format ----
    order = ["README", "summary", "in_gen", "in_loc", "inter_gen", "out_loc", "cf", "pontoons", "freight", "harbors",
             "aggregates", "sens_discounts", "sens_subsea_cable", "sens_pontoons"]
    wb._sheets = [wb[n] for n in order]
    # number formats by unit, and column widths wide enough for every displayed value
    # (checked by test_displayed_values_fit_their_columns)
    unit_fmt = {"€": "#,##0", "kWh": "#,##0", "unit": "#,##0", "kW": "#,##0.0", "m": "#,##0.0", "y": "0",
                "%": "0.0%", "€/kWh": "0.0000"}
    kpi_fmt = {"lcoe": "0.0000", "roi": "0.0%", "irr": "0.0%", "payback_period": "0"}
    o.freeze_panes = "D2"
    o.column_dimensions["A"].width = 38; o.column_dimensions["B"].width = 7; o.column_dimensions["C"].width = 60
    for i, (n, unit, cm, f) in enumerate(spec):
        fmt = kpi_fmt.get(n) or unit_fmt.get(unit, "General")
        for j in range(ncase):
            o.cell(2 + i, C0 + j).number_format = fmt
    for j in range(ncase):
        o.column_dimensions[ccol(j)].width = 16
    s.column_dimensions["A"].width = 20
    for i, (label, n) in enumerate(srows):
        fmt = kpi_fmt.get(n, "#,##0")
        for j in range(len(CASES)):
            s.cell(2 + i, 2 + j).number_format = fmt
    for j in range(len(CASES)):
        s.column_dimensions[col(2 + j)].width = 14
    cf_fmt = {"operating": "0", "module_age": "0", "payback_flag": "0", "discount_factor": "0.0000",
              "npv_nonnegative": "0"}
    cf.column_dimensions["A"].width = 26; cf.column_dimensions["B"].width = 8
    for b, h in B.items():
        n_rows = N_GRID if b in ("npv_at_rate", "npv_nonnegative") else NY
        fmt = cf_fmt.get(b, "#,##0")
        for r in range(h + 1, h + 1 + n_rows):
            if b in ("npv_at_rate", "npv_nonnegative"):
                cf.cell(r, 2).number_format = "0%"
            for j in range(ncase):
                cf.cell(r, C0 + j).number_format = fmt
    for j in range(ncase):
        cf.column_dimensions[ccol(j)].width = 15
    for name in ("sens_discounts", "sens_subsea_cable", "sens_pontoons"):
        ws = wb[name]
        ws.column_dimensions["A"].width = 16; ws.column_dimensions["B"].width = 18
        for r in range(2, ws.max_row + 1):
            n = dict(kpis).get(ws.cell(r, 1).value)
            for c in range(3, 3 + len(SENS_LOCS)):
                ws.cell(r, c).number_format = kpi_fmt.get(n, "#,##0")
        for c in range(3, 3 + len(SENS_LOCS)):
            ws.column_dimensions[col(c)].width = 15
    for c, w in {"A": 16, "B": 12, "C": 12, "D": 14, "E": 16, "F": 15, "G": 14, "H": 11, "I": 12, "J": 12, "K": 8,
                 "M": 16, "N": 12, "O": 14, "P": 14, "Q": 14, "R": 16, "U": 18, "V": 12, "W": 12, "X": 13,
                 "Y": 14, "Z": 12, "AA": 16}.items():
        p.column_dimensions[c].width = w
    # input sheets carried over from the Google Sheets export had 2-5 character columns
    for name, ws_widths in {
        "in_gen": {"A": 42, "B": 18, "C": 12, "D": 6, "E": 12, "F": 12, "G": 90},
        "in_loc": dict({"A": 42, "B": 40, "C": 6}, **{col(c): 12 for c in range(4, 31)}),
        "inter_gen": {"A": 32, "B": 10, "C": 14, "D": 4, "E": 14, "F": 14, "G": 10, "H": 90},
        "freight": {"A": 22, "B": 34},
        "harbors": {"A": 20, "B": 22, "C": 22, "D": 30, "E": 22, "F": 30, "G": 14},
        "aggregates": {"A": 26, "B": 40, "C": 14, "D": 14},
    }.items():
        for c, w in ws_widths.items():
            wb[name].column_dimensions[c].width = w
    for row in p.iter_rows(min_row=3):
        for c in row:
            if c.column in (5,):
                c.number_format = "#,##0.0"
            elif c.column in (6, 15, 16, 17, 18, 25, 27):
                c.number_format = "#,##0"
    return wb


README_LINES = [
    f"SUREWAVE D7.4 techno-economic cost model, version {VERSION}",
    "",
    "Purpose:",
    "Bottom-up CAPEX, OPEX, reinstallation and end-of-life costs, lifetime production, LCOE, NPV, ROI, payback and IRR "
    "for the SUREWAVE floating PV system with integrated breakwater, for nine site/size cases (North Sea, Baltic, "
    "Mediterranean; 2 MW, 5 × 2 MW, 10 MW), each with base, pessimistic and optimistic inputs.",
    "",
    "How to use:",
    "- Inputs are on in_gen (general), in_loc (per site and size), pontoons (pontoon weights and material prices) and freight. "
    "Pessimistic and optimistic values are derived from the base value with sensitivity_margin and the Dir column "
    "(+1: higher is worse, -1: higher is better, 0: not varied).",
    "- Results per case are on out_loc and summarised on summary. Year-by-year cash flows are on cf.",
    "- Sensitivity cases (discount rate, subsea cable, pontoon design) are extra columns on out_loc and feed the sens_* sheets.",
    "",
    "Conventions:",
    "- Year 0: construction and all initial CAPEX. Operation in years 1 to horizon_years (PV lifetime × PV lifetimes per "
    "structure lifetime = 25 × 2 = 50 years in the base case).",
    "- PV reinstallation at the end of each PV lifetime except the last (year 25): new modules, replacement work, disposal "
    "of the removed modules. Module degradation restarts after reinstallation.",
    "- Inverters and transformers: inverters_transformers_cost is CAPEX in year 0 and covers the inverter replacements over "
    "the life (12-15 year cycles), as D7.4 §4.3.1 describes; no separate replacement cash flow.",
    "- End of life in the last operating year: removal of breakwater, pontoons, anchors and moorings, and of the last PV "
    "layer; disposal; minus any residual value (inputs in in_gen, section End of life).",
    "- Discount factor 1/(1+r)^t. LCOE = discounted lifetime cost / discounted lifetime production. NPV = discounted revenue "
    "- discounted lifetime cost. IRR on undiscounted net cash flows over the full life; because reinstallation and "
    "decommissioning are late outflows, the cash flows can have more than one IRR, and the model reports the highest "
    "rate between -10 % and 50 % at which NPV = 0. Payback = first year in which cumulative discounted net cash flow "
    "is ≥ 0.",
    "",
    "System boundary:",
    "- Included: PV modules and their production, DC/AC cabling, 300 m floating MV cable to the grid connection point, "
    "inverters and transformers, SCADA, breakwater and bridge pontoons, anchors and moorings, PVC pipes and ropes, freight "
    "of the PV containers, marine installation, O&M of PV and pontoons, PV reinstallation, decommissioning.",
    "- Grid connection point: an existing offshore substation within ~300 m. The substation itself is not included.",
    "- Export cable to shore: not in the base case; covered by the subsea cable sensitivity (cable cost per metre × distance "
    "to shore, without cable losses, cable landing or onshore substation).",
    "- Not included: substation, development and permitting, seabed lease, grid connection fees, insurance, financing "
    "costs, contingency, environmental monitoring, curtailment.",
    "",
    "Changes from version 2 (see the D7.4 revision note for the effect of each change on the results):",
    "- LCOE includes the reinstallation capital cost (v2 counted second-life production but not its cost).",
    "- Discounting with 1/(1+r)^t (v2: (1-r)^t), CAPEX in year 0 and operation from year 1.",
    "- IRR on undiscounted cash flows over the full life (v2: discounted flows, first 25 years only).",
    "- Pontoon maintenance, inverters/transformers and SCADA included (inputs existed in v2 but were not used).",
    "- Replacement costs multiplied by the number of rings, like installation costs.",
    "- End-of-life costs added (decommissioning, disposal, residual value).",
    "- Freight rate looked up by container count (v2 looked it up by the PVC cost).",
    "- Pontoon totals recalculate in Excel (v2 used Google Sheets formulas that Excel could not evaluate, and added the "
    "pontoon counts to the euro total).",
    "- Pessimistic and optimistic cases use their own inputs throughout (v2 mixed columns in some rows).",
    "- Sensitivity sheets are calculated live (v2: pasted values from an earlier run).",
    "- Dir for the electricity sale price (in_gen, solar_energy_target_price) corrected from +1 to -1: a higher sale "
    "price is favourable, so the pessimistic case now uses the lower price (EUR 0.1152/kWh) and the optimistic case the "
    "higher (EUR 0.1248/kWh).",
    "- Formulas use only functions available in desktop Excel and LibreOffice.",
]


def evaluate(xlsx_path: Path, inputs: dict | None = None, model=None):
    """Evaluate every formula of a workbook with the `formulas` library.

    Returns ({(sheet, 'A1'): value}, model). Pass the returned model back with
    `inputs` ({(sheet, 'A1'): value}) to recalculate after changing input cells
    without reloading the file (~20 s instead of ~95 s for the full workbook).
    """
    import formulas
    import numpy as np
    name = Path(xlsx_path).name
    if model is None:
        model = formulas.ExcelModel().loads(str(xlsx_path)).finish()
    ins = {f"'[{name}]{s.upper()}'!{c}": v for (s, c), v in (inputs or {}).items()}
    sol = model.calculate(inputs=ins) if ins else model.calculate()
    out = {}
    for key, ranges in sol.items():
        if "!" not in key or ":" in key.split("!")[1]:
            continue
        sheet = key.split("]")[1].split("'")[0]
        v = np.array(ranges.value).flatten()[0]
        if isinstance(v, np.generic):
            v = v.item()
        out[(sheet.upper(), key.split("!")[1])] = v
    return out, model


def write_with_results(wb: openpyxl.Workbook, results: dict, out_path: Path) -> None:
    """Write an openpyxl workbook with xlsxwriter, storing each formula's result
    next to the formula, so Excel (also in Protected View) and other readers
    show numbers without recalculating. Copies values, formulas, number formats,
    bold/italic, solid fills, column widths and freeze panes."""
    import xlsxwriter
    xw = xlsxwriter.Workbook(str(out_path), {"strings_to_numbers": False, "strings_to_formulas": False,
                                             "strings_to_urls": False})
    fmt_cache: dict = {}

    def fmt(cell):
        f = cell.font
        fill = cell.fill.fgColor.rgb if cell.fill and cell.fill.fill_type == "solid" else None
        key = (cell.number_format, bool(f.bold), bool(f.italic), fill if isinstance(fill, str) else None)
        if key == ("General", False, False, None):
            return None
        if key not in fmt_cache:
            props = {}
            if key[0] != "General":
                props["num_format"] = key[0]
            if key[1]:
                props["bold"] = True
            if key[2]:
                props["italic"] = True
            if key[3]:
                props["bg_color"] = "#" + key[3][-6:]
            fmt_cache[key] = xw.add_format(props)
        return fmt_cache[key]

    missing = []
    for ws in wb.worksheets:
        xs = xw.add_worksheet(ws.title)
        for dim in ws.column_dimensions.values():
            if dim.width and dim.min and dim.max:
                xs.set_column(dim.min - 1, dim.max - 1, dim.width)
        if ws.freeze_panes:
            fc = ws[ws.freeze_panes]
            xs.freeze_panes(fc.row - 1, fc.column - 1)
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                r0, c0, f = c.row - 1, c.column - 1, fmt(c)
                if isinstance(v, str) and v.startswith("="):
                    key = (ws.title.upper(), c.coordinate)
                    if key not in results:
                        missing.append(key)
                    res = results.get(key, 0)
                    if isinstance(res, bool):
                        res = int(res)
                    if not isinstance(res, (int, float, str)):
                        res = str(res)
                    xs.write_formula(r0, c0, v, f, res)
                elif isinstance(v, bool):
                    xs.write_boolean(r0, c0, v, f)
                elif isinstance(v, (int, float)):
                    xs.write_number(r0, c0, v, f)
                elif isinstance(v, str):
                    xs.write_string(r0, c0, v, f)
                elif v is not None:
                    xs.write(r0, c0, v, f)
                elif f is not None:
                    xs.write_blank(r0, c0, None, f)
    xw.close()
    if missing:
        raise RuntimeError(f"{len(missing)} formula cells have no evaluated result, e.g. {missing[:5]}")


def build(v2_path: Path, out_path: Path, tmp_dir: Path | None = None) -> dict:
    """Build v3: formulas (openpyxl) -> evaluate (formulas library) -> write with
    stored results (xlsxwriter). Returns the evaluated results."""
    import tempfile
    wb = build_openpyxl(v2_path)
    with tempfile.TemporaryDirectory(prefix="d74_build_", dir=tmp_dir) as d:
        tmp = Path(d) / Path(out_path).name
        wb.save(tmp)
        results, _ = evaluate(tmp)
    write_with_results(wb, results, Path(out_path))
    return results


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: python scripts/build_d74_workbook.py <v2.xlsx> <out.xlsx>")
    build(Path(sys.argv[1]), Path(sys.argv[2]))
    print("wrote", sys.argv[2])
