"""Reference implementation of the SUREWAVE D7.4 techno-economic cost model.

Purpose: an independent test oracle for the D7.4 cost workbook. It reads the
*input* sheets of a workbook (v2 Google Sheets export or the v3 Excel rebuild;
both share the input layout) and computes every output per case.

Two calculation modes:

- ``v2_outputs``  reproduces the v2 workbook exactly, errors included. Used to
  prove that the inputs are read correctly (tests compare against the values
  cached in the v2 file).
- ``v3_outputs``  the corrected model. Each correction is a switch in
  ``V3_FIXES`` so its effect can be quantified one at a time for the changelog.

The Python code is not the deliverable; the Excel workbook is. See
docs/scripts.md (d74_cost_model.py) and T157 in TASKS.md.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path

import openpyxl

LOCATIONS = ["n_2", "n_25", "n_10", "b_2", "b_25", "b_10", "m_2", "m_25", "m_10"]
VARIANTS = ["base", "pes", "opt"]
CASES = [loc if v == "base" else f"{loc}_{v}" for v in VARIANTS for loc in LOCATIONS]
# Installation size key in the pontoon sub-model for each location size suffix
INSTALL_SIZE = {"2": "2MW", "25": "2MW_5", "10": "10MW"}


def split_case(case: str) -> tuple[str, str]:
    parts = case.split("_")
    if len(parts) == 3:
        return f"{parts[0]}_{parts[1]}", parts[2]
    return case, "base"


# ---------------------------------------------------------------- inputs ----
@dataclass
class Inputs:
    gen: dict[str, float]                 # in_gen base values (column C)
    gen_dir: dict[str, float]             # in_gen Dir (column D)
    loc: dict[str, dict[str, float]]      # in_loc base values, per location key
    loc_dir: dict[str, float]             # in_loc Dir (column C)
    freight: list[tuple[float, float]]    # (containers, EUR per km per container)
    pontoon_rows: list[tuple[str, str, str, str, float]]  # design, install, type, material, weight t
    material_cost: dict[str, float]       # EUR/t per pontoon material
    pontoon_counts: dict[tuple[str, str], float]  # (install, type) -> count
    extras: list[tuple[str, str, float, float]]   # component, install, weight t, EUR/t
    extra_gen: dict[str, float] = field(default_factory=dict)  # v3-only inputs

    @property
    def margin(self) -> float:
        return self.gen["sensitivity_margin"]

    # value of a general input for a variant, as in in_gen columns C/E/F
    def g(self, name: str, variant: str = "base") -> float:
        base = self.gen[name] if name in self.gen else self.extra_gen[name]
        d = self.gen_dir.get(name, 0)
        s = {"base": 0, "pes": 1, "opt": -1}[variant]
        return base * (1 + self.margin * d * s)

    # value of a location input for a variant, as in in_loc columns D..AD
    def l(self, name: str, loc: str, variant: str = "base") -> float:
        base = self.loc[name][loc]
        d = self.loc_dir.get(name, 0)
        s = {"base": 0, "pes": 1, "opt": -1}[variant]
        return base * (1 + self.margin * d * s)


def _num(v):
    return v if isinstance(v, (int, float)) else None


def load_inputs(path: str | Path) -> Inputs:
    wb = openpyxl.load_workbook(path, data_only=True)

    ws = wb["in_gen"]
    gen, gen_dir = {}, {}
    for r in range(2, ws.max_row + 1):
        name, val = ws.cell(r, 1).value, _num(ws.cell(r, 3).value)
        if isinstance(name, str) and val is not None:
            gen[name] = val
            gen_dir[name] = _num(ws.cell(r, 4).value) or 0

    ws = wb["in_loc"]
    header = [ws.cell(1, c).value for c in range(1, ws.max_column + 1)]
    cols = {k: header.index(k) + 1 for k in LOCATIONS}
    loc, loc_dir = {}, {}
    for r in range(2, ws.max_row + 1):
        name = ws.cell(r, 1).value
        if not isinstance(name, str):
            continue
        vals = {k: _num(ws.cell(r, c).value) for k, c in cols.items()}
        if all(v is None for v in vals.values()):
            continue
        loc[name] = {k: (v if v is not None else 0.0) for k, v in vals.items()}
        loc_dir[name] = _num(ws.cell(r, 3).value) or 0

    ws = wb["freight"]
    freight = [(ws.cell(r, 1).value, ws.cell(r, 2).value) for r in range(2, ws.max_row + 1)
               if _num(ws.cell(r, 1).value) is not None]

    ws = wb["pontoons"]
    rows, mat, counts, extras = [], {}, {}, []
    for r in range(3, ws.max_row + 1):
        a, b, c, d, e = (ws.cell(r, k).value for k in range(1, 6))
        if a and b and c and d and _num(e) is not None:
            rows.append((a, b, c, d, float(e)))
        if ws.cell(r, 7).value and _num(ws.cell(r, 8).value) is not None:
            mat[ws.cell(r, 7).value] = ws.cell(r, 8).value
        if ws.cell(r, 9).value and ws.cell(r, 10).value and _num(ws.cell(r, 11).value) is not None:
            counts[(ws.cell(r, 9).value, ws.cell(r, 10).value)] = ws.cell(r, 11).value
        if ws.cell(r, 21).value and ws.cell(r, 22).value and _num(ws.cell(r, 23).value) is not None:
            extras.append((ws.cell(r, 21).value, ws.cell(r, 22).value,
                           float(ws.cell(r, 23).value), float(ws.cell(r, 24).value)))

    extra_gen = {}
    if "in_gen_eol" in wb.sheetnames:  # v3-only inputs
        ws = wb["in_gen_eol"]
        for r in range(2, ws.max_row + 1):
            name, val = ws.cell(r, 1).value, _num(ws.cell(r, 3).value)
            if isinstance(name, str) and val is not None:
                extra_gen[name] = val

    return Inputs(gen, gen_dir, loc, loc_dir, freight, rows, mat, counts, extras, extra_gen)


# ------------------------------------------------------- shared helpers ----
def vlookup_approx(key: float, table: list[tuple[float, float]]) -> float:
    """Excel VLOOKUP(..., TRUE): last row whose first column is <= key."""
    best = None
    for k, v in table:
        if k <= key:
            best = v
        else:
            break
    if best is None:
        raise ValueError(f"VLOOKUP key {key} below first table row")
    return best


def pontoon_type_costs(inp: Inputs) -> dict[tuple[str, str, str], float]:
    """(design, install, type) -> cost: sum over materials of weight x EUR/t (pontoons!O)."""
    out: dict[tuple[str, str, str], float] = {}
    for design, inst, ptype, material, weight in inp.pontoon_rows:
        key = (design, inst, ptype)
        out[key] = out.get(key, 0.0) + weight * inp.material_cost[material]
    return out


def pontoon_total(inp: Inputs, install: str, design: str | None = None,
                  v2_count_bug: bool = False) -> float:
    """Total pontoon cost for one installation size.

    design=None: cheapest design per pontoon type (pontoons!S, MINIFS per type).
    v2_count_bug: reproduce v2 pontoons!AA4/AA5, which add the pontoon counts
    (pontoons!T) to the euro total via SUMPRODUCT({FILTER(S),FILTER(T)}).
    """
    if install == "2MW":
        return pontoon_total(inp, "2MW_5", design, v2_count_bug) / 5
    costs = pontoon_type_costs(inp)
    types = sorted({t for (_, i, t) in costs if i == install})
    total = 0.0
    for t in types:
        cands = {d: c for (d, i, tt), c in costs.items() if i == install and tt == t}
        total += cands[design] if design else min(cands.values())
        if v2_count_bug:
            total += inp.pontoon_counts[(install, t)]
    total += sum(w * c for (_, i, w, c) in inp.extras if i == install)
    return total


IRR_GRID_TOP, IRR_GRID_BOTTOM, IRR_GRID_STEP = 0.50, -0.10, 0.01
N_GRID = int(round((IRR_GRID_TOP - IRR_GRID_BOTTOM) / IRR_GRID_STEP)) + 1


def irr(cashflows: list[float]) -> float | None:
    """Internal rate of return, defined as the highest rate in [-10 %, 50 %]
    at which NPV = 0. Cash flows with late outflows (reinstallation,
    decommissioning) can have several roots; the workbook uses the same
    definition (NPV on a 1 % rate grid, then IRR() with a guess at the grid
    point just below the highest root). Scans down the grid for the first
    sign change of NPV and bisects it. Returns None if there is no root."""
    def npv(rate):
        return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))
    hi, f_hi = IRR_GRID_TOP, npv(IRR_GRID_TOP)
    lo = None
    rate = IRR_GRID_TOP
    while rate > IRR_GRID_BOTTOM + 1e-9:
        rate_next = round(rate - IRR_GRID_STEP, 6)
        f_next = npv(rate_next)
        if f_next * f_hi <= 0:
            lo, f_lo = rate_next, f_next
            break
        hi, f_hi, rate = rate_next, f_next, rate_next
    if lo is None:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = npv(mid)
        if f_lo * f_mid <= 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


# ------------------------------------------------------------ v2 model ----
def v2_outputs(inp: Inputs, case: str) -> dict[str, float]:
    """Reproduce v2 out_loc for one case column, including its errors.

    The v2 workbook mixes in_gen columns between variants in several rows;
    each such quirk is reproduced and commented.
    """
    loc, v = split_case(case)
    g = lambda n: inp.g(n, v)          # in_gen column of this variant
    gb = lambda n: inp.g(n, "base")    # in_gen column C
    L = lambda n: inp.l(n, loc, v)     # in_loc column of this case
    o: dict[str, float] = {}

    hinge_num = gb("solar_panel_hinge_length") if v in ("base", "pes") else g("solar_panel_hinge_length")
    o["solar_panels_per_matrix_width"] = math.floor(
        (L("matrix_side_length") * 1000 + hinge_num) / (g("solar_panel_width") + g("solar_panel_hinge_length")))
    o["solar_panels_per_matrix_length"] = math.floor(
        (L("matrix_side_length") * 1000 + g("solar_panel_hinge_length"))
        / (g("solar_panel_length") + g("solar_panel_hinge_length")))
    o["solar_panels_per_matrix"] = o["solar_panels_per_matrix_width"] * o["solar_panels_per_matrix_length"]
    o["solar_matrices_along_radii"] = math.ceil(math.sqrt(L("matrices_per_quadrant")))
    o["solar_radius"] = math.ceil(math.sqrt(1 + o["solar_matrices_along_radii"] ** 2) * L("matrix_side_length")) \
        + g("pontoon_width") / 2
    o["total_solar_panels"] = o["solar_panels_per_matrix"] * L("matrices_per_quadrant") * 4
    o["total_dc_cable_cost"] = g("dc_cable_cost_per_m") * g("dc_cable_per_panel") * o["total_solar_panels"]
    o["total_solar_power"] = o["total_solar_panels"] * g("solar_panel_power") / 1000
    o["solar_container_count"] = math.ceil(o["total_solar_panels"] / g("panels_per_container"))
    o["total_mv_submarine_cable_cost"] = (g("mv_submarine_cable_cost_per_m") + g("cable_installation_cost_per_m")) \
        * L("distance_to_shore")
    o["total_pvc_cost"] = g("pvc_cost") * L("pvc_pipe_weight")
    o["total_rope_cost"] = g("polypropylene_cost") * L("polypropylene_rope_weight")
    rings = L("rings_count")
    # v2 error: freight rate looked up with total_pvc_cost (row 13) instead of the container count
    o["solar_freight_cost"] = rings * L("panel_transport_km") * o["solar_container_count"] \
        * vlookup_approx(o["total_pvc_cost"], inp.freight)
    pf = {"base": 1, "pes": 1 + inp.margin, "opt": 1 - inp.margin}[v]
    o["total_pontoon_cost"] = pontoon_total(inp, INSTALL_SIZE[loc.split("_")[1]], v2_count_bug=True) * pf
    # v2 quirk: pes columns use the *optimistic* inter_gen column F
    ig = lambda n: inp.g(n, "base" if v == "base" else "opt")
    panel_cost_kw = ig("solar_panel_prod_workhours_per_kw") * ig("solar_panel_prod_workhours_cost_per_hour") \
        + ig("solar_panel_prod_material_costs") + ig("solar_panel_prod_other_costs")
    ac = ig("ac_cable_cost_per_m") * ig("ac_cable_length")
    mvf = ig("mv_floating_cable_cost_per_m") * ig("mv_floating_cable_length")
    o["total_cost_solar_panels"] = rings * panel_cost_kw * o["total_solar_power"]
    o["total_cost_cabling_short_alternative"] = rings * (o["total_dc_cable_cost"] + ac + mvf)
    o["total_cost_cabling_long_alternative"] = rings * (o["total_dc_cable_cost"] + ac) + o["total_mv_submarine_cable_cost"]
    o["total_cost_anchoring_mooring"] = rings * (L("anchor_weight") * g("anchor_cost_per_t")
                                                 + L("chain_weight") * g("anchor_chain_cost_per_t"))
    o["total_cost_installation"] = rings * sum(L(f"installation_{p}_{c}_cost")
                                               for p in ("pontoons", "pv_system")
                                               for c in ("equipment", "fuel", "personnel"))
    o["total_capex_cost"] = (o["total_pvc_cost"] + o["total_rope_cost"] + o["solar_freight_cost"]
                             + o["total_pontoon_cost"] + o["total_cost_solar_panels"]
                             + o["total_cost_cabling_short_alternative"] + o["total_cost_anchoring_mooring"]
                             + o["total_cost_installation"])

    r, n = g("discount_rate"), int(round(g("solar_lifetime")))
    cool = gb("solar_extra_production_from_cooling") if v in ("base", "pes") else g("solar_extra_production_from_cooling")
    y, wl, dg = L("solar_production_yearly"), L("solar_wave_loss"), L("solar_degradation_yearly")
    kw = o["total_solar_power"]
    # v2 error: discount factor (1 - r)^t instead of 1/(1 + r)^t; first year at t = 0
    o["total_solar_production"] = rings * kw * sum(
        y * (1 - wl) * (1 + cool) * (1 - dg * t) * (1 - r) ** t for t in range(n))
    o["total_solar_maintenance_cost"] = rings * kw * sum(L("solar_maintenance_cost_per_kw_per_year") * (1 - r) ** t
                                                         for t in range(n))
    k = int(round(g("solar_lifetimes_per_wavebreaker_lifetime")))
    # v2 error: extra (1 - r) factor; replacement inputs not multiplied by rings_count
    def reinst(value, rr, nn):
        return sum(value * (1 - rr) * (1 - rr) ** (nn * j) for j in range(1, k)) if k > 1 else 0.0
    repl = o["total_cost_solar_panels"] + sum(L(f"replacement_of_pv_system_{c}_cost")
                                              for c in ("equipment", "fuel", "personnel"))
    o["total_solar_reinstall_cost"] = reinst(repl, r, n)
    # v2 quirk: opt column uses base discount rate and base lifetime for reinstall production
    r28, n28 = (inp.g("discount_rate", "pes"), int(round(inp.g("solar_lifetime", "pes")))) if v == "pes" \
        else (gb("discount_rate"), int(round(gb("solar_lifetime"))))
    o["total_solar_reinstall_production"] = reinst(o["total_solar_production"], r28, n28)
    o["total_solar_reinstall_maintenance_cost"] = reinst(o["total_solar_maintenance_cost"], r, n)
    # v2 error: LCOE omits total_solar_reinstall_cost
    o["lcoe"] = (o["total_capex_cost"] + o["total_solar_maintenance_cost"] + o["total_solar_reinstall_maintenance_cost"]) \
        / (o["total_solar_production"] + o["total_solar_reinstall_production"])
    price = g("solar_energy_target_price")
    o["total_revenue"] = price * (o["total_solar_production"] + o["total_solar_reinstall_production"])
    o["npv"] = o["total_revenue"] - (o["total_capex_cost"] + o["total_solar_maintenance_cost"]
                                     + o["total_solar_reinstall_cost"] + o["total_solar_reinstall_maintenance_cost"])
    o["roi"] = o["npv"] / o["total_capex_cost"]
    cool_pb = g("solar_extra_production_from_cooling")
    net = [rings * kw * (price * y * (1 - wl) * (1 + cool_pb) - L("solar_maintenance_cost_per_kw_per_year"))
           * (1 - dg * t) * (1 - r) ** t for t in range(n)]
    cum, pb = 0.0, None
    for t, x in enumerate(net):
        cum += x
        if o["total_capex_cost"] <= cum:
            pb = t + 1
            break
    o["payback_period"] = pb if pb is not None else "-"
    # v2 error: IRR on (1 - r)^t-discounted flows, years 0..n-1, capex in the first year
    o["irr"] = irr([x - (o["total_capex_cost"] if t == 0 else 0) for t, x in enumerate(net)])
    return o


# ------------------------------------------------------------ v3 model ----
V3_FIXES = {
    "reinstall_in_lcoe": "LCOE includes the year-25 reinstallation capital cost",
    "discounting": "Discount factor 1/(1+r)^t; CAPEX in year 0, operation in years 1..H",
    "irr_undiscounted_full_life": "IRR on undiscounted net cash flows over the full life",
    "unused_cost_inputs": "Pontoon maintenance, inverters/transformers and SCADA included",
    "replacement_rings": "Replacement inputs multiplied by rings_count, like installation inputs",
    "end_of_life": "Decommissioning of structure and PV at end of life; PV disposal at each removal",
    "freight_key": "Freight rate looked up by container count",
    "pontoon_count_bug": "Pontoon counts no longer added to the euro total",
    "variant_columns": "Pessimistic/optimistic columns use their own inputs throughout",
}


def v3_outputs(inp: Inputs, case: str, fixes: set[str] | None = None,
               overrides: dict | None = None) -> dict[str, float]:
    """Corrected model. ``fixes`` = subset of V3_FIXES to apply (default: all).

    overrides (for sensitivity cases): ``discount_rate``, ``cable`` ('short' |
    'long'), ``pontoon_design`` (design code or None for cheapest per type).
    """
    fx = set(V3_FIXES) if fixes is None else set(fixes)
    ov = overrides or {}
    loc, v = split_case(case)
    vv = v if "variant_columns" in fx else None
    g = lambda n: inp.g(n, v)
    L = lambda n: inp.l(n, loc, v)
    eol = lambda n: inp.g(n, v) if n in inp.gen else EOL_DEFAULTS[n]
    o: dict[str, float] = {}

    hinge = g("solar_panel_hinge_length")
    o["solar_panels_per_matrix_width"] = math.floor((L("matrix_side_length") * 1000 + hinge)
                                                    / (g("solar_panel_width") + hinge))
    o["solar_panels_per_matrix_length"] = math.floor((L("matrix_side_length") * 1000 + hinge)
                                                     / (g("solar_panel_length") + hinge))
    o["solar_panels_per_matrix"] = o["solar_panels_per_matrix_width"] * o["solar_panels_per_matrix_length"]
    o["total_solar_panels"] = o["solar_panels_per_matrix"] * L("matrices_per_quadrant") * 4
    o["total_dc_cable_cost"] = g("dc_cable_cost_per_m") * g("dc_cable_per_panel") * o["total_solar_panels"]
    o["total_solar_power"] = o["total_solar_panels"] * g("solar_panel_power") / 1000
    o["solar_container_count"] = math.ceil(o["total_solar_panels"] / g("panels_per_container"))
    o["total_mv_submarine_cable_cost"] = (g("mv_submarine_cable_cost_per_m") + g("cable_installation_cost_per_m")) \
        * L("distance_to_shore")
    o["total_pvc_cost"] = g("pvc_cost") * L("pvc_pipe_weight")
    o["total_rope_cost"] = g("polypropylene_cost") * L("polypropylene_rope_weight")
    rings = L("rings_count")
    key = o["solar_container_count"] if "freight_key" in fx else o["total_pvc_cost"]
    o["solar_freight_cost"] = rings * L("panel_transport_km") * o["solar_container_count"] \
        * vlookup_approx(key, inp.freight)
    pf = {"base": 1, "pes": 1 + inp.margin, "opt": 1 - inp.margin}[v]
    o["total_pontoon_cost"] = pontoon_total(inp, INSTALL_SIZE[loc.split("_")[1]], ov.get("pontoon_design"),
                                            v2_count_bug="pontoon_count_bug" not in fx) * pf
    ig = (lambda n: inp.g(n, v)) if "variant_columns" in fx else (lambda n: inp.g(n, "base" if v == "base" else "opt"))
    panel_cost_kw = ig("solar_panel_prod_workhours_per_kw") * ig("solar_panel_prod_workhours_cost_per_hour") \
        + ig("solar_panel_prod_material_costs") + ig("solar_panel_prod_other_costs")
    ac = ig("ac_cable_cost_per_m") * ig("ac_cable_length")
    mvf = ig("mv_floating_cable_cost_per_m") * ig("mv_floating_cable_length")
    o["total_cost_solar_panels"] = rings * panel_cost_kw * o["total_solar_power"]
    o["total_cost_cabling_short_alternative"] = rings * (o["total_dc_cable_cost"] + ac + mvf)
    o["total_cost_cabling_long_alternative"] = rings * (o["total_dc_cable_cost"] + ac) + o["total_mv_submarine_cable_cost"]
    o["total_cost_anchoring_mooring"] = rings * (L("anchor_weight") * g("anchor_cost_per_t")
                                                 + L("chain_weight") * g("anchor_chain_cost_per_t"))
    inst_pont = sum(L(f"installation_pontoons_{c}_cost") for c in ("equipment", "fuel", "personnel"))
    inst_pv = sum(L(f"installation_pv_system_{c}_cost") for c in ("equipment", "fuel", "personnel"))
    o["total_cost_installation"] = rings * (inst_pont + inst_pv)
    use_inputs = "unused_cost_inputs" in fx
    o["total_inverters_transformers_cost"] = rings * L("inverters_transformers_cost") if use_inputs else 0.0
    scada = sum(g(n) for n in SCADA_ITEMS)
    o["total_scada_cost"] = rings * scada if use_inputs else 0.0
    cabling = o["total_cost_cabling_long_alternative"] if ov.get("cable") == "long" \
        else o["total_cost_cabling_short_alternative"]
    o["total_capex_cost"] = (o["total_pvc_cost"] + o["total_rope_cost"] + o["solar_freight_cost"]
                             + o["total_pontoon_cost"] + o["total_cost_solar_panels"] + cabling
                             + o["total_cost_anchoring_mooring"] + o["total_cost_installation"]
                             + o["total_inverters_transformers_cost"] + o["total_scada_cost"])

    # ---- yearly cash flows
    r = ov.get("discount_rate", g("discount_rate"))
    life = int(round(g("solar_lifetime")))
    k = int(round(g("solar_lifetimes_per_wavebreaker_lifetime")))
    horizon = life * k
    cool = g("solar_extra_production_from_cooling")
    y, wl, dg = L("solar_production_yearly"), L("solar_wave_loss"), L("solar_degradation_yearly")
    kw = o["total_solar_power"]
    om_solar = rings * kw * L("solar_maintenance_cost_per_kw_per_year")
    om_pont = rings * sum(L(f"maintenance_pontoons_{c}_cost") for c in ("equipment", "fuel", "personnel")) \
        if use_inputs else 0.0
    repl_inputs = sum(L(f"replacement_of_pv_system_{c}_cost") for c in ("equipment", "fuel", "personnel"))
    # inverter replacements are covered by inverters_transformers_cost in CAPEX (D7.4 §4.3.1)
    repl = o["total_cost_solar_panels"] + (rings if "replacement_rings" in fx else 1) * repl_inputs
    do_eol = "end_of_life" in fx
    disposal = eol("pv_module_disposal_cost_per_kw") * rings * kw if do_eol else 0.0
    decom = (eol("decommissioning_pontoons_cost_factor") * rings * inst_pont
             + eol("decommissioning_pv_system_cost_factor") * rings * inst_pv + disposal
             - eol("residual_value_fraction") * (o["total_pontoon_cost"] + o["total_cost_anchoring_mooring"])) \
        if do_eol else 0.0
    price = g("solar_energy_target_price")

    if "discounting" in fx:
        years = range(0, horizon + 1)
        df = lambda t: 1 / (1 + r) ** t
        age = lambda t: (t - 1) % life
        operating = lambda t: 1 <= t <= horizon
    else:  # v2 convention: operation from t = 0, factor (1 - r)^t
        years = range(0, horizon)
        df = lambda t: (1 - r) ** t
        age = lambda t: t % life
        operating = lambda t: True
    reinstall_years = {life * j - (0 if "discounting" in fx else 0) for j in range(1, k)}
    prod, cost_om, cost_capex, cost_reinst, cost_eol = [], [], [], [], []
    for t in years:
        e = rings * kw * y * (1 - wl) * (1 + cool) * (1 - dg * age(t)) if operating(t) else 0.0
        prod.append(e)
        cost_om.append(om_solar + om_pont if operating(t) else 0.0)
        cost_capex.append(o["total_capex_cost"] if t == 0 else 0.0)
        cost_reinst.append(repl + disposal if t in reinstall_years else 0.0)
        cost_eol.append(decom if t == (horizon if "discounting" in fx else horizon - 1) else 0.0)
    D = [df(t) for t in years]
    pv = lambda xs: sum(x * d for x, d in zip(xs, D))
    o["horizon_years"] = horizon
    o["total_solar_production"] = pv(prod)
    o["total_maintenance_cost"] = pv(cost_om)
    o["total_solar_reinstall_cost"] = pv(cost_reinst)
    o["total_end_of_life_cost"] = pv(cost_eol)
    lcoe_costs = o["total_capex_cost"] + o["total_maintenance_cost"] + o["total_end_of_life_cost"] \
        + (o["total_solar_reinstall_cost"] if "reinstall_in_lcoe" in fx else 0.0)
    o["lcoe"] = lcoe_costs / o["total_solar_production"]
    o["total_revenue"] = price * o["total_solar_production"]
    o["npv"] = o["total_revenue"] - (o["total_capex_cost"] + o["total_maintenance_cost"]
                                     + o["total_solar_reinstall_cost"] + o["total_end_of_life_cost"])
    o["roi"] = o["npv"] / o["total_capex_cost"]
    net = [price * e - om - c - ri - de for e, om, c, ri, de in zip(prod, cost_om, cost_capex, cost_reinst, cost_eol)]
    cum, pb = 0.0, None
    for t, (x, d) in enumerate(zip(net, D)):
        cum += x * d
        if cum >= 0 and t > 0:
            pb = t
            break
    o["payback_period"] = pb if pb is not None else "-"
    o["irr"] = irr(net) if "irr_undiscounted_full_life" in fx else irr([x * d for x, d in zip(net, D)][:life])
    if o["irr"] is None:
        o["irr"] = "-"          # no root: shown as "-" in the workbook, like payback

    # every remaining out_loc row, and the cf sheet year by year (full v3 only),
    # so the tests can check every formula cell of the workbook
    o["solar_matrices_along_radii"] = math.ceil(math.sqrt(L("matrices_per_quadrant")))
    o["solar_radius"] = math.ceil(math.sqrt(1 + o["solar_matrices_along_radii"] ** 2) * L("matrix_side_length")) \
        + g("pontoon_width") / 2
    o["total_cost_cabling"] = cabling
    o["total_cost_installation_pontoons"] = rings * inst_pont
    o["total_cost_installation_pv_system"] = rings * inst_pv
    o["solar_lifetime_years"] = life
    o["solar_lifetimes"] = k
    o["yearly_production_new_modules"] = rings * kw * y * (1 - wl) * (1 + cool)
    o["yearly_om_cost"] = om_solar + om_pont
    o["pv_disposal_cost"] = disposal
    o["reinstallation_cost"] = repl + disposal
    o["end_of_life_cost"] = decom
    o["energy_price"] = price
    o["discount_rate"] = r
    o["total_lifetime_cost"] = (o["total_capex_cost"] + o["total_maintenance_cost"]
                                + o["total_solar_reinstall_cost"] + o["total_end_of_life_cost"])
    if "discounting" in fx:
        o["cf"] = cash_flow_table(o, life, horizon, dg, r)
        grid = [round(IRR_GRID_TOP - i * IRR_GRID_STEP, 6) for i in range(N_GRID)]
        npvs = [sum(x / (1 + rate) ** t for t, x in enumerate(o["cf"]["net_cash_flow"])) for rate in grid]
        o["cf"]["npv_at_rate"] = npvs
        o["cf"]["npv_nonnegative"] = [1 if x >= 0 else 0 for x in npvs]
        o["irr_guess"] = next((rate for rate, x in zip(grid, npvs) if x >= 0), "-")
    return o


CF_YEARS = 56   # years 0..55 in the workbook's cf sheet


def cash_flow_table(o: dict, life: int, horizon: int, dg: float, r: float) -> dict[str, list[float]]:
    """The workbook's cf blocks for one case, years 0..CF_YEARS-1."""
    t_all = range(CF_YEARS)
    cf: dict[str, list] = {}
    cf["operating"] = [1 if 1 <= t <= horizon else 0 for t in t_all]
    cf["module_age"] = [(t - 1) % life if op else 0 for t, op in zip(t_all, cf["operating"])]
    cf["production"] = [op * o["yearly_production_new_modules"] * (1 - dg * a)
                        for op, a in zip(cf["operating"], cf["module_age"])]
    cf["om_cost"] = [op * o["yearly_om_cost"] for op in cf["operating"]]
    cf["capex"] = [o["total_capex_cost"] if t == 0 else 0 for t in t_all]
    cf["reinstallation"] = [o["reinstallation_cost"] if 0 < t < horizon and t % life == 0 else 0 for t in t_all]
    cf["end_of_life"] = [o["end_of_life_cost"] if t == horizon else 0 for t in t_all]
    cf["revenue"] = [o["energy_price"] * e for e in cf["production"]]
    cf["net_cash_flow"] = [rv - om - c - ri - de for rv, om, c, ri, de in
                           zip(cf["revenue"], cf["om_cost"], cf["capex"], cf["reinstallation"], cf["end_of_life"])]
    cf["discount_factor"] = [1 / (1 + r) ** t for t in t_all]
    cum, cums = 0.0, []
    for x, d in zip(cf["net_cash_flow"], cf["discount_factor"]):
        cum += x * d
        cums.append(cum)
    cf["cumulative_discounted_net"] = cums
    cf["payback_flag"] = [1 if t > 0 and c >= 0 else 0 for t, c in zip(t_all, cums)]
    return cf


SCADA_ITEMS = ["scada_ppc", "scada_sems", "scada_weather_station", "scada_smart_energy_meter",
               "scada_gateway_rtu", "scada_switch_fiber", "scada_local_hmi", "scada_license_config",
               "scada_cabling_racks_power_backup"]

# End-of-life inputs added in v3 (sheet in_gen_eol). Defaults used when the
# workbook does not carry them (v2).
EOL_DEFAULTS = {
    "decommissioning_pontoons_cost_factor": 1.0,
    "decommissioning_pv_system_cost_factor": 1.0,
    "pv_module_disposal_cost_per_kw": 0.0,
    "residual_value_fraction": 0.0,
}

OUTPUT_ROWS_V2 = [
    "solar_panels_per_matrix_width", "solar_panels_per_matrix_length", "solar_panels_per_matrix",
    "solar_radius", "total_solar_panels", "solar_matrices_along_radii", "total_dc_cable_cost",
    "total_solar_power", "solar_container_count", "total_mv_submarine_cable_cost", "total_pvc_cost",
    "total_rope_cost", "solar_freight_cost", "total_pontoon_cost", "total_cost_solar_panels",
    "total_cost_cabling_short_alternative", "total_cost_cabling_long_alternative",
    "total_cost_anchoring_mooring", "total_cost_installation", "total_capex_cost",
    "total_solar_production", "total_solar_maintenance_cost", "lcoe", "total_solar_reinstall_cost",
    "total_solar_reinstall_production", "total_solar_reinstall_maintenance_cost", "total_revenue",
    "npv", "roi", "payback_period", "irr",
]


def read_cached_outputs(path: str | Path) -> dict[str, dict[str, object]]:
    """Cached out_loc values of a workbook: {case: {row name: value}}."""
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb["out_loc"]
    header = [ws.cell(1, c).value for c in range(1, ws.max_column + 1)]
    out: dict[str, dict[str, object]] = {}
    for case in CASES:
        c = header.index(case) + 1
        out[case] = {}
        for r in range(2, ws.max_row + 1):
            name = ws.cell(r, 1).value
            if isinstance(name, str):
                out[case][name] = ws.cell(r, c).value
    return out


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("workbook")
    p.add_argument("--mode", choices=["v2", "v3"], default="v3")
    p.add_argument("--cases", nargs="*", default=["n_10", "b_10", "m_10"])
    a = p.parse_args()
    inp = load_inputs(a.workbook)
    for c in a.cases:
        o = v2_outputs(inp, c) if a.mode == "v2" else v3_outputs(inp, c)
        print(c, {k: (round(o[k], 4) if isinstance(o[k], float) else o[k])
                  for k in ("total_capex_cost", "lcoe", "npv", "irr", "payback_period")})
