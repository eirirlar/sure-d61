"""Tests for the SUREWAVE D7.4 cost workbook v3 (T157).

Run:  python -m pytest -p no:cacheprovider scripts/test_d74_cost_model.py     (~3-4 min)

No desktop applications needed: the workbook is built with
build_d74_workbook.py and every formula is evaluated with the `formulas`
library. Python packages: openpyxl, xlsxwriter, formulas (numpy), pytest.

What is tested:
1. The Python reference model reproduces every cached output of the v2
   workbook (27 cases x 31 rows), errors included -> it reads the inputs the
   way the sheet does.
2. EVERY formula cell of the v3 workbook (~62,000) has an independently
   computed expected value (test_every_formula_cell_has_an_expected_value),
   and every one of them matches (test_every_formula_result_matches_model).
3. The delivered file stores exactly these results next to the formulas.
4. Display: every number fits its column (no '###'), formulas are portable,
   no error values, no Google Sheets leftovers.
5. Every input is used by some formula or documented as unused.
6. Changing inputs changes the results, and the Python model agrees.
7. Unit tests of the financial helpers against hand-computed values.
8. Every Dir value moves NPV in the direction it claims (with a negative
   control on the v2 inputs), and the scenarios are ordered pes < base < opt.
"""
from __future__ import annotations

import copy
import re
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

import openpyxl
import pytest
from openpyxl.utils import get_column_letter

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))
import d74_cost_model as m  # noqa: E402
import build_d74_workbook as bw  # noqa: E402

V2 = REPO / "surewave/background/2025-09-05_surewave_d7.4_costs_v2.xlsx"
DOCUMENTED_UNUSED = {
    # in_gen: freight is priced from the freight table instead
    "container_transport_cost_road", "container_transport_cost_sea",
    # in_loc: layout counts/distances; costs use the weights instead
    "anchors_count", "pontoons_count", "solar_pipe_distance", "pipe_wavebreaker_distance",
}
NON_PORTABLE = re.compile(r"\b(LAMBDA|MAP|SCAN|FILTER|SEQUENCE|UNIQUE|MINIFS|MAXIFS|XLOOKUP|LET|SORT|TEXTJOIN)\s*\(|"
                          r"_xlfn|_xlws|UNSUPPORTED", re.I)


def close(a, b, rel=1e-9, abs_=1e-9):
    if isinstance(a, str) or isinstance(b, str):
        return str(a) == str(b)
    if a is None or b is None:
        return a == b
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))


# ---------------------------------------------------------------- fixture ----
@pytest.fixture(scope="session")
def built():
    with tempfile.TemporaryDirectory(prefix="d74_test_") as d:
        d = Path(d)
        wb = bw.build_openpyxl(V2)
        formula_file = d / "d74_v3.xlsx"
        wb.save(formula_file)
        results, model = bw.evaluate(formula_file)
        out = d / "out" / "d74_v3.xlsx"
        out.parent.mkdir()
        bw.write_with_results(wb, results, out)
        inp = m.load_inputs(formula_file)
        yield SimpleNamespace(wb=wb, formula_file=formula_file, results=results, model=model, out=out, inp=inp,
                              expected=expected_cells(wb, inp))


def formula_cells(wb):
    return {(ws.title.upper(), c.coordinate) for ws in wb for row in ws.iter_rows() for c in row
            if isinstance(c.value, str) and c.value.startswith("=")}


# ------------------------------------------------- independent expectations ----
def expected_cells(wb, inp: m.Inputs) -> dict:
    """Expected value of every formula cell, computed from the inputs by the
    Python model (not by reading the workbook's formulas)."""
    exp: dict = {}
    var_col = {"E": "pes", "F": "opt", "C": "base"}

    # in_gen: pessimistic (E) and optimistic (F) columns
    ws = wb["in_gen"]
    for r in range(2, ws.max_row + 1):
        name = ws.cell(r, 1).value
        for cl in ("E", "F"):
            if isinstance(ws[f"{cl}{r}"].value, str) and ws[f"{cl}{r}"].value.startswith("="):
                exp[("IN_GEN", f"{cl}{r}")] = inp.g(name, var_col[cl])

    # in_loc: pes/opt columns M..AD
    ws = wb["in_loc"]
    hdr = {c: ws.cell(1, c).value for c in range(4, 31)}
    for r in range(2, ws.max_row + 1):
        name = ws.cell(r, 1).value
        for c in range(4, 31):
            v = ws.cell(r, c).value
            if isinstance(v, str) and v.startswith("="):
                loc, var = m.split_case(hdr[c])
                exp[("IN_LOC", f"{get_column_letter(c)}{r}")] = inp.l(name, loc, var)

    # inter_gen: derived general inputs per variant column C/E/F, text column H
    ig = {
        "total_ac_cable_cost": (lambda v: inp.g("ac_cable_cost_per_m", v) * inp.g("ac_cable_length", v),
                                "ac_cable_cost_per_m * ac_cable_length"),
        "total_mv_floating_cable_cost": (lambda v: inp.g("mv_floating_cable_cost_per_m", v)
                                         * inp.g("mv_floating_cable_length", v),
                                         "mv_floating_cable_cost_per_m * mv_floating_cable_length"),
        "solar_panel_cost": (lambda v: inp.g("solar_panel_prod_workhours_per_kw", v)
                             * inp.g("solar_panel_prod_workhours_cost_per_hour", v)
                             + inp.g("solar_panel_prod_material_costs", v) + inp.g("solar_panel_prod_other_costs", v),
                             "solar_panel_prod_workhours_per_kw * solar_panel_prod_workhours_cost_per_hour + "
                             "solar_panel_prod_material_costs + solar_panel_prod_other_costs"),
        "scada_system": (lambda v: sum(inp.g(n, v) for n in m.SCADA_ITEMS), " + ".join(m.SCADA_ITEMS)),
    }
    ws = wb["inter_gen"]
    for r in range(2, ws.max_row + 1):
        name = ws.cell(r, 1).value
        if name in ig:
            for cl in ("C", "E", "F"):
                exp[("INTER_GEN", f"{cl}{r}")] = ig[name][0](var_col[cl])
            exp[("INTER_GEN", f"H{r}")] = ig[name][1]

    # pontoons
    ws = wb["pontoons"]
    costs = m.pontoon_type_costs(inp)
    for r in range(3, ws.max_row + 1):
        if isinstance(ws.cell(r, 6).value, str):        # F: weight x EUR/t
            exp[("PONTOONS", f"F{r}")] = ws.cell(r, 5).value * inp.material_cost[ws.cell(r, 4).value]
        if isinstance(ws.cell(r, 25).value, str):       # Y: extras weight x EUR/t
            exp[("PONTOONS", f"Y{r}")] = ws.cell(r, 23).value * ws.cell(r, 24).value
        design, inst = ws.cell(r, 13).value, ws.cell(r, 14).value
        if inst in bw.INSTALLS and design:
            extras = sum(w * c for (_, i, w, c) in inp.extras if i == inst)
            per_type = []
            for j, t in enumerate(bw.PTYPES):
                if design == "Cheapest per type":
                    val = min(costs.get((d, inst, t), 0.0) for d in bw.DESIGNS)
                else:
                    val = costs.get((design, inst, t), 0.0)
                per_type.append(val)
                exp[("PONTOONS", f"{get_column_letter(15 + j)}{r}")] = val
            exp[("PONTOONS", f"R{r}")] = sum(per_type) + extras
        key = ws.cell(r, 26).value
        if key in m.CASES and isinstance(ws.cell(r, 27).value, str):
            loc, var = m.split_case(key)
            pf = {"base": 1, "pes": 1 + inp.margin, "opt": 1 - inp.margin}[var]
            exp[("PONTOONS", f"AA{r}")] = m.pontoon_total(inp, m.INSTALL_SIZE[loc.split("_")[1]]) * pf

    # out_loc and cf: one column per case
    ol, cf = wb["out_loc"], wb["cf"]
    rows = {ol.cell(r, 1).value: r for r in range(2, ol.max_row + 1) if ol.cell(r, 1).value}
    loc_keys = [wb["in_loc"].cell(1, c).value for c in range(4, 31)]
    blocks = {cf.cell(r, 1).value: r for r in range(2, cf.max_row + 1) if isinstance(cf.cell(r, 1).value, str)}
    case_out: dict = {}
    for c in range(4, ol.max_column + 1):
        cid = ol.cell(1, c).value
        loc, var = ol.cell(rows["location"], c).value, ol.cell(rows["variant"], c).value
        case = loc if var == "base" else f"{loc}_{var}"
        ov = {}
        if ol.cell(rows["discount_rate_override"], c).value is not None:
            ov["discount_rate"] = ol.cell(rows["discount_rate_override"], c).value
        if ol.cell(rows["cable_alternative"], c).value == "long":
            ov["cable"] = "long"
        if ol.cell(rows["pontoon_design"], c).value != "cheapest":
            ov["pontoon_design"] = ol.cell(rows["pontoon_design"], c).value
        o = m.v3_outputs(inp, case, overrides=ov)
        case_out[cid] = o
        L = get_column_letter(c)
        o_def = {"in_loc_key": case, "in_loc_index": loc_keys.index(case) + 1,
                 "in_gen_index": {"base": 1, "pes": 3, "opt": 4}[var]}
        for name, r in rows.items():
            if isinstance(ol.cell(r, c).value, str) and ol.cell(r, c).value.startswith("="):
                if name in o_def:
                    exp[("OUT_LOC", f"{L}{r}")] = o_def[name]
                elif name in o and not isinstance(o[name], dict):
                    exp[("OUT_LOC", f"{L}{r}")] = o[name]
        for b, h in blocks.items():
            for i, val in enumerate(o["cf"][b]):
                exp[("CF", f"{L}{h + 1 + i}")] = val

    # summary: row label -> out_loc row, column header -> case
    s = wb["summary"]
    srow = {"CAPEX (€)": "total_capex_cost", "OPEX (€)": "total_maintenance_cost",
            "Reinstallation (€)": "total_solar_reinstall_cost", "End of life (€)": "total_end_of_life_cost",
            "Revenue (€)": "total_revenue", "LCOE (€/kWh)": "lcoe", "NPV (€)": "npv", "ROI (%)": "roi",
            "Payback (y)": "payback_period", "IRR (%)": "irr"}
    for r in range(2, s.max_row + 1):
        n = srow.get(s.cell(r, 1).value)
        if n:
            for c in range(2, s.max_column + 1):
                exp[("SUMMARY", f"{get_column_letter(c)}{r}")] = case_out[s.cell(1, c).value][n]

    # sensitivity sheets: (KPI label, parameter value) -> case id
    kpi = {"CAPEX (€)": "total_capex_cost", "OPEX (€)": "total_maintenance_cost", "Revenue (€)": "total_revenue",
           "LCOE (€/kWh)": "lcoe", "NPV (€)": "npv", "ROI (%)": "roi", "Payback (y)": "payback_period",
           "IRR (%)": "irr"}
    for name, case_of in (("sens_discounts", lambda loc, p: f"{loc}_r{p}"),
                          ("sens_subsea_cable", lambda loc, p: f"{loc}_subsea" if p == "Yes" else loc),
                          ("sens_pontoons", lambda loc, p: f"{loc}_{p.split()[0]}")):
        ws = wb[name]
        for r in range(2, ws.max_row + 1):
            n = kpi.get(ws.cell(r, 1).value)
            if n:
                for c in range(3, 3 + len(bw.SENS_LOCS)):
                    cid = case_of(ws.cell(1, c).value, ws.cell(r, 2).value)
                    exp[(name.upper(), f"{get_column_letter(c)}{r}")] = case_out[cid][n]
    return exp


# ------------------------------------------------------------------ 1 ----
def test_v2_replica_matches_cached_values():
    inp = m.load_inputs(V2)
    cached = m.read_cached_outputs(V2)
    bad = []
    for case in m.CASES:
        o = m.v2_outputs(inp, case)
        for k in m.OUTPUT_ROWS_V2:
            if not close(o[k], cached[case][k], 1e-9):
                bad.append((case, k, o[k], cached[case][k]))
    assert not bad, bad[:10]


# ------------------------------------------------------------------ 2 ----
def test_every_formula_cell_has_an_expected_value(built):
    formulas_in_wb = formula_cells(built.wb)
    uncovered = sorted(formulas_in_wb - set(built.expected))
    assert len(formulas_in_wb) > 60000
    assert not uncovered, f"{len(uncovered)} formula cells without an expected value, e.g. {uncovered[:10]}"


def test_every_formula_result_matches_model(built):
    bad = []
    for key, want in built.expected.items():
        got = built.results.get(key)
        if not close(got, want, rel=1e-7, abs_=1e-7):
            bad.append((key, got, want))
    assert not bad, f"{len(bad)} of {len(built.expected)} formula results differ, e.g. {bad[:10]}"


# ------------------------------------------------------------------ 3 ----
def test_delivered_file_stores_the_results(built):
    wb_v = openpyxl.load_workbook(built.out, data_only=True)
    wb_f = openpyxl.load_workbook(built.out)
    assert formula_cells(wb_f) == formula_cells(built.wb), "formulas lost or added when writing the file"
    names = {n.upper(): n for n in wb_v.sheetnames}
    bad = []
    for sheet, coord in formula_cells(built.wb):
        stored = wb_v[names[sheet]][coord].value
        if not close(stored, built.results[(sheet, coord)]):
            bad.append((sheet, coord, stored, built.results[(sheet, coord)]))
    assert not bad, bad[:10]


# ------------------------------------------------------------------ 4 ----
def displayed_text(value: float, fmt: str) -> str:
    """Text Excel shows for a number in the formats the workbook uses."""
    f = (fmt or "General").replace("\\", "")
    if f == "#,##0":
        return f"{round(value):,}"
    if f == "#,##0.0":
        return f"{value:,.1f}"
    if f == "0.0%":
        return f"{value * 100:.1f}%"
    if f == "0%":
        return f"{value * 100:.0f}%"
    if f == "0.0000":
        return f"{value:.4f}"
    if f == "0":
        return f"{value:.0f}"
    if f in ("0.0", "0.00"):
        return f"{value:.{len(f) - 2}f}"
    # General: Excel drops decimals to fit, so only the integer part can overflow
    if float(value).is_integer():
        return str(int(value))
    return f"{int(value)}.0" if abs(value) >= 1 else "0.0"


def test_displayed_values_fit_their_columns(built):
    """No '###': every number, in its cell's number format, fits its column with one
    character of margin (width is in units of the '0' character)."""
    wb = openpyxl.load_workbook(built.out, data_only=True)
    bad = []
    for ws in wb:
        widths = {}
        for dim in ws.column_dimensions.values():
            if dim.width and dim.min and dim.max:
                for ci in range(dim.min, dim.max + 1):
                    widths[ci] = dim.width
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, (int, float)) and not isinstance(c.value, bool):
                    w = widths.get(c.column, 8.43)
                    text = displayed_text(c.value, c.number_format)
                    if len(text) + 1 > w:
                        bad.append((ws.title, c.coordinate, text, c.number_format, w))
    assert not bad, f"{len(bad)} cells would show ###, e.g. {bad[:8]}"


def test_width_check_catches_a_narrow_column():
    """Negative control for the check above."""
    assert len(displayed_text(13714799, "#,##0")) + 1 > 6
    assert not len(displayed_text(0.0764, "0.0000")) + 1 > 12


def test_portable_formulas_and_no_errors(built):
    bad = [(ws.title, c.coordinate, c.value[:80]) for ws in built.wb for row in ws.iter_rows() for c in row
           if isinstance(c.value, str) and c.value.startswith("=") and NON_PORTABLE.search(c.value)]
    assert not bad, bad[:10]
    errs = [(k, v) for k, v in built.results.items()
            if (isinstance(v, str) and v.startswith("#")) or type(v).__name__ == "XlError"]
    assert not errs, errs[:10]
    assert not openpyxl.load_workbook(built.out).defined_names


# ------------------------------------------------------------------ 5 ----
def test_every_input_is_used_or_documented(built):
    text = "\n".join(c.value for ws in built.wb for row in ws.iter_rows() for c in row
                     if isinstance(c.value, str) and c.value.startswith("="))
    unused = []
    for sheet in ("in_gen", "in_loc"):
        ws = built.wb[sheet]
        for r in range(2, ws.max_row + 1):
            name = ws.cell(r, 1).value
            val = ws.cell(r, 3 if sheet == "in_gen" else 4).value
            if not isinstance(name, str) or not isinstance(val, (int, float)):
                continue
            if not re.search(rf"{sheet}!\$?[A-Z]+\$?{r}(?!\d)", text) and name not in DOCUMENTED_UNUSED:
                unused.append((sheet, r, name))
    assert not unused, unused


# ------------------------------------------------------------------ 6 ----
def _ol(built, results, cid, key):
    ol = built.wb["out_loc"]
    col = next(c for c in range(4, ol.max_column + 1) if ol.cell(1, c).value == cid)
    row = next(r for r in range(2, ol.max_row + 1) if ol.cell(r, 1).value == key)
    return results[("OUT_LOC", f"{get_column_letter(col)}{row}")]


def test_pontoon_material_price_moves_results(built):
    p = built.wb["pontoons"]
    r = next(r for r in range(3, 10) if p.cell(r, 7).value == "CC")
    new_price = p.cell(r, 8).value * 2
    res, _ = bw.evaluate(built.formula_file, inputs={("pontoons", f"H{r}"): new_price}, model=built.model)
    assert _ol(built, res, "m_10", "total_pontoon_cost") > _ol(built, built.results, "m_10", "total_pontoon_cost") + 100_000
    inp = copy.deepcopy(built.inp)
    inp.material_cost["CC"] = new_price
    want = m.v3_outputs(inp, "m_10")
    assert close(_ol(built, res, "m_10", "npv"), want["npv"], 1e-7)
    assert want["npv"] < m.v3_outputs(built.inp, "m_10")["npv"]


def test_discount_rate_and_end_of_life_inputs_move_results(built):
    rows = bw.name_rows(built.wb["in_gen"])
    res, _ = bw.evaluate(built.formula_file, model=built.model, inputs={
        ("in_gen", f"C{rows['discount_rate']}"): 0.06,
        ("in_gen", f"C{rows['decommissioning_pontoons_cost_factor']}"): 3.0})
    assert _ol(built, res, "m_10", "discount_rate") == pytest.approx(0.06)
    assert _ol(built, res, "m_10_r8", "discount_rate") == pytest.approx(0.08)   # sensitivity case keeps its rate
    inp = copy.deepcopy(built.inp)
    inp.gen["discount_rate"] = 0.06
    inp.gen["decommissioning_pontoons_cost_factor"] = 3.0
    for cid in ("m_10", "b_10_pes", "n_25_opt"):
        assert close(_ol(built, res, cid, "lcoe"), m.v3_outputs(inp, cid)["lcoe"], 1e-7)
        assert close(_ol(built, res, cid, "total_end_of_life_cost"),
                     m.v3_outputs(inp, cid)["total_end_of_life_cost"], 1e-7)


# ------------------------------------------------------------------ 7 ----
def test_irr_hand_example():
    # -100 now, +60 in years 1 and 2: 100 = 60/(1+r) + 60/(1+r)^2 -> r = 13.0662 %
    assert m.irr([-100, 60, 60]) == pytest.approx(0.130662, abs=1e-6)


def test_irr_takes_highest_root_with_late_outflow():
    # roots at 10 % and 20 %: (1.1)(1.2) = 1.32 -> -100, 230, -132
    assert m.irr([-100, 230, -132]) == pytest.approx(0.20, abs=1e-9)


def test_vlookup_bands():
    table = [(1, 1.5), (2, 1.3995), (34, 1.0371), (55, 0.9967)]
    assert m.vlookup_approx(36, table) == 1.0371
    assert m.vlookup_approx(34, table) == 1.0371
    assert m.vlookup_approx(1, table) == 1.5
    with pytest.raises(ValueError):
        m.vlookup_approx(0.5, table)


def test_pontoon_cheapest_per_type_and_v2_count_bug():
    inp = m.load_inputs(V2)
    costs = m.pontoon_type_costs(inp)
    types = ["Breakwater", "Bridge1968", "Bridge1830"]
    cheapest = sum(min(c for (d, i, t), c in costs.items() if i == "10MW" and t == tt) for tt in types)
    extras = sum(w * c for (_, i, w, c) in inp.extras if i == "10MW")
    assert m.pontoon_total(inp, "10MW") == pytest.approx(cheapest + extras)
    counts = sum(inp.pontoon_counts[("10MW", t)] for t in types)
    assert m.pontoon_total(inp, "10MW", v2_count_bug=True) == pytest.approx(cheapest + extras + counts)
    assert m.pontoon_total(inp, "10MW", v2_count_bug=True) == pytest.approx(2118899)  # v2 frozen value


def test_cash_flow_timing():
    """Reinstallation in year 25, end of life in year 50, CAPEX in year 0, degradation reset (m_10)."""
    cf = m.v3_outputs(m.load_inputs(V2), "m_10")["cf"]
    assert [t for t, v in enumerate(cf["reinstallation"]) if v] == [25]
    assert [t for t, v in enumerate(cf["end_of_life"]) if v] == [50]
    assert [t for t, v in enumerate(cf["capex"]) if v] == [0]
    assert cf["production"][0] == 0 and cf["production"][51] == 0
    assert cf["production"][26] == pytest.approx(cf["production"][1])
    assert cf["production"][25] < cf["production"][1]
    assert cf["discount_factor"][25] == pytest.approx(0.130094, abs=1e-6)   # 1/1.085^25


# ------------------------------------------------------------------ 8 ----
def dir_violations(inp: m.Inputs, locations) -> list:
    """Inputs whose Dir contradicts their effect: applying only the pessimistic
    value of one input (all others at base) must lower NPV, and only the
    optimistic value must raise it. Inputs that do not affect a case are skipped."""
    def with_one(kind, name, loc, variant):
        i = copy.deepcopy(inp)
        if kind == "gen":
            i.gen[name] = inp.g(name, variant)
        else:
            i.loc[name][loc] = inp.l(name, loc, variant)
        return i
    items = [("gen", n) for n, d in inp.gen_dir.items() if d] + [("loc", n) for n, d in inp.loc_dir.items() if d]
    bad, checked = [], 0
    for loc in locations:
        base = m.v3_outputs(inp, loc)["npv"]
        for kind, name in items:
            pes = m.v3_outputs(with_one(kind, name, loc, "pes"), loc)["npv"]
            opt = m.v3_outputs(with_one(kind, name, loc, "opt"), loc)["npv"]
            if abs(pes - base) < 1e-6 and abs(opt - base) < 1e-6:
                continue
            checked += 1
            if not pes < base < opt:
                bad.append((loc, name, round(pes - base), round(opt - base)))
    return bad, checked


def test_dir_values_move_npv_the_documented_way(built):
    bad, checked = dir_violations(built.inp, m.LOCATIONS)
    assert checked > 300, checked
    assert not bad, bad


def test_dir_check_flags_the_v2_price_direction():
    """Negative control: on the original v2 inputs the check above must flag
    exactly the electricity sale price, whose Dir was +1."""
    bad, _ = dir_violations(m.load_inputs(V2), ["n_10", "b_10", "m_10"])
    assert {name for _, name, _, _ in bad} == {"solar_energy_target_price"}


def test_sale_price_varies_in_the_right_direction(built):
    rows = bw.name_rows(built.wb["in_gen"])
    r = rows["solar_energy_target_price"]
    assert built.wb["in_gen"].cell(r, 4).value == -1
    base, pes, opt = 0.12, built.results[("IN_GEN", f"E{r}")], built.results[("IN_GEN", f"F{r}")]
    assert pes == pytest.approx(0.1152) and opt == pytest.approx(0.1248)
    for loc in ("n_10", "b_10", "m_10"):
        assert _ol(built, built.results, f"{loc}_pes", "energy_price") == pytest.approx(0.1152)
        assert _ol(built, built.results, f"{loc}_opt", "energy_price") == pytest.approx(0.1248)
        assert _ol(built, built.results, loc, "energy_price") == pytest.approx(base)


def test_scenarios_are_ordered_in_the_workbook(built):
    """In the workbook's own formula results, every site and size has
    NPV(pessimistic) < NPV(base) < NPV(optimistic) and the reverse order for LCOE."""
    for loc in m.LOCATIONS:
        npv = [_ol(built, built.results, c, "npv") for c in (f"{loc}_pes", loc, f"{loc}_opt")]
        lcoe = [_ol(built, built.results, c, "lcoe") for c in (f"{loc}_pes", loc, f"{loc}_opt")]
        assert npv[0] < npv[1] < npv[2], (loc, npv)
        assert lcoe[0] > lcoe[1] > lcoe[2], (loc, lcoe)
