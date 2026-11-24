"""Tests for the Sunlit Sea KER1 financial plan model and workbook (T158).

Run:  python -m pytest -p no:cacheprovider scripts/test_hrb_financial_model.py     (~30 s)

No desktop applications needed: the workbook is built with
build_hrb_financial_workbook.py and every formula is evaluated with the
`formulas` library. Python packages: openpyxl, xlsxwriter, formulas, pytest.

What is tested:
1. The three statements tie in the Python model for every scenario: the
   balance sheet balances, cash in the balance sheet equals the cash-flow
   closing balance, and equity moves only by net result, equity raised and
   the shareholder-loan conversion.
2. Every model cell and every unit-economics result in the workbook matches
   the independent Python implementation, for all four scenarios (switches
   set through the inputs sheet).
3. The delivered file stores the base-case results next to the formulas, has
   no error values and uses only portable functions.
4. Direction checks: higher kit cost lowers the result, a higher kit price
   raises it, an extra EU project does not reduce cash, and removing a funding
   round makes cash negative (the funding need is real).
5. Unit-economics helpers against hand-computed values.
"""
from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

import openpyxl
import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import hrb_financial_model as m  # noqa: E402
import build_hrb_financial_workbook as bw  # noqa: E402
from build_d74_workbook import evaluate  # noqa: E402

NON_PORTABLE = re.compile(r"\b(LAMBDA|MAP|SCAN|FILTER|SEQUENCE|UNIQUE|MINIFS|MAXIFS|XLOOKUP|LET|SORT|TEXTJOIN)\s*\(|"
                          r"_xlfn|_xlws", re.I)


def close(a, b, tol=1e-6):
    return abs(a - b) <= max(tol, 1e-9 * max(abs(a), abs(b)))


@pytest.fixture(scope="module")
def built():
    wb, ctx = bw.build()
    d = Path(tempfile.mkdtemp())
    raw = d / "fp.xlsx"
    wb.save(raw)
    res, model = evaluate(raw)
    out = d / "fp_delivered.xlsx"
    bw.write_with_results(wb, res, out)
    return wb, ctx, raw, res, model, out


@pytest.mark.parametrize("sc", list(m.SCENARIOS))
def test_statements_tie(sc):
    r = m.compute(sc)
    for t in range(m.N):
        assert abs(r["balance_check"][t]) < 1e-6
    # cash in balance sheet = opening + cumulative net cash flow
    s, _, _ = m.inputs_for(sc)
    assert close(r["cash"][-1], s["open_cash"] + sum(r["net_cash_flow"]))
    # equity roll-forward
    eq0 = r["open_equity"][0]
    assert close(r["equity"][-1], eq0 + sum(r["net_income"]) + sum(r["equity_raise"]) + s["open_shareholder_loan"])


@pytest.mark.parametrize("sc", list(m.SCENARIOS))
def test_workbook_matches_python(built, sc):
    wb, ctx, raw, res, model, out = built
    ins = {("INPUTS", f"B{ctx.s_row[k]}"): v for k, v in m.SCENARIOS[sc].items()}
    vals, _ = evaluate(raw, ins, model)
    r = m.compute(sc)
    checked = 0
    for key, row in ctx.m_row.items():
        if key not in r:
            continue
        for t in range(m.N):
            got = vals[("MODEL", f"{bw.YC[t]}{row}")]
            assert close(got, r[key][t]), (sc, key, m.YEARS[t], got, r[key][t])
            checked += 1
    assert checked > 300
    for t in range(m.N):
        assert abs(vals[("MODEL", f"{bw.YC[t]}{ctx.m_row['balance_check']}")]) < 1e-6
    assert abs(vals[("MODEL", f"{bw.OPEN}{ctx.m_row['balance_check']}")]) < 1e-6


def test_every_model_line_is_checked(built):
    _, ctx, *_ = built
    r = m.compute("base")
    unchecked = set(ctx.m_row) - set(r)
    assert unchecked == {"shareholder_conversion"}, unchecked


def test_unit_economics_match(built):
    _, ctx, raw, res, model, out = built
    ue = m.unit_economics()
    for k, v in ue.items():
        got = res[("UNIT", f"B{ctx.u_row[k]}")]
        assert close(got, v), (k, got, v)


def test_delivered_file(built):
    wb, ctx, raw, res, model, out = built
    wb2 = openpyxl.load_workbook(out, data_only=True)
    wbf = openpyxl.load_workbook(out)
    r = m.compute("base")
    ws = wb2["model"]
    for key in ("revenue", "ebitda", "cash", "equity"):
        for t in range(m.N):
            assert close(ws[f"{bw.YC[t]}{ctx.m_row[key]}"].value, r[key][t])
    for sh in wbf.worksheets:
        for row in sh.iter_rows():
            for cell in row:
                v = cell.value
                if isinstance(v, str) and v.startswith("="):
                    assert not NON_PORTABLE.search(v), (sh.title, cell.coordinate, v)
    for sh in wb2.worksheets:
        for row in sh.iter_rows():
            for cell in row:
                assert not (isinstance(cell.value, str) and cell.value.startswith("#")), (sh.title, cell.coordinate)


def test_directions():
    base = m.compute("base")
    hi_cost = m.compute("base", {"kit_cost": [c + 0.02 for c in m.YEARLY["kit_cost"][0]]})
    hi_price = m.compute("base", {"kit_price": [p + 0.02 for p in m.YEARLY["kit_price"][0]]})
    assert sum(hi_cost["net_income"]) < sum(base["net_income"])
    assert sum(hi_price["net_income"]) > sum(base["net_income"])
    eic = m.compute("eic")
    assert all(eic["cash"][t] >= base["cash"][t] - 1e-9 for t in range(m.N))
    er = m.YEARLY["equity_raise"][0]
    no_round2 = m.compute("base", {"equity_raise": [er[0], 0, 0, 0, 0]})
    assert min(no_round2["cash"]) < 200  # below the buffer without round 2
    no_round1 = m.compute("base", {"equity_raise": [0] + er[1:]})
    assert min(no_round1["cash"]) < 0
    # capitalisation is cash-neutral
    nocap = m.compute("base", {"capitalise": [0, 0, 0, 0, 0]})
    assert all(close(nocap["cash"][t], base["cash"][t]) for t in range(m.N))


def test_minimum_cash_buffer():
    for sc in m.SCENARIOS:
        assert min(m.compute(sc)["cash"]) > 200, sc


def test_unit_economics_hand_values():
    ue = m.unit_economics()
    assert close(ue["epc_cost"], 0.64)
    assert close(ue["epc_price"], 0.64 / 0.88)
    # annuity check: flat energy, no degradation
    flat = m.unit_economics({"ue_degradation": 0.0, "ue_opex_escalation": 0.0, "ue_inverter": 0.0})
    ann = sum(1 / 1.06 ** k for k in range(1, 26))
    assert close(flat["pv_energy"], 900 * ann)
    assert close(flat["pv_opex"], 12 * ann)
    assert close(ue["kit_margin_050"], 0.22 / 0.50)
    # support needed makes the supported LCOE equal the host's value
    sup = m.unit_economics({"ue_support": ue["support_needed"]})
    assert close(sup["lcoe_supported"], ue["host_value"])


def test_breakeven_volume_is_consistent():
    r = m.compute("base")
    mw = m.breakeven_kit_mw(r)
    y = list(m.YEARLY["kit_mw"][0])
    eng = list(m.YEARLY["eng_revenue"][0])
    ue = m.unit_economics()
    y[-1] = mw
    eng[-1] = ue["p2_eng_rev_per_w"] * 1000 * mw
    r2 = m.compute("base", {"kit_mw": y, "eng_revenue": eng})
    assert abs(r2["ebt"][-1]) < 1e-6
    # scenario-aware: a cost override changes the break-even volume consistently
    ov = {"kit_cost": [c + 0.03 for c in m.YEARLY["kit_cost"][0]]}
    r3 = m.compute("base", ov)
    mw3 = m.breakeven_kit_mw(r3, overrides=ov)
    y3 = list(ov["kit_cost"]) and list(m.YEARLY["kit_mw"][0])
    y3[-1] = mw3
    ov2 = dict(ov, kit_mw=y3, eng_revenue=eng[:-1] + [ue["p2_eng_rev_per_w"] * 1000 * mw3])
    assert abs(m.compute("base", ov2)["ebt"][-1]) < 1e-6
    assert mw3 > mw


def test_quarterly_cash_adds_up():
    q = m.quarterly_cash()
    r = m.compute("base")
    assert close(sum(f for _, f, _ in q[:4]), r["net_cash_flow"][0])
    assert close(sum(f for _, f, _ in q[4:]), r["net_cash_flow"][1])
    assert close(q[3][2], r["cash"][0]) and close(q[7][2], r["cash"][1])
    assert min(c for _, _, c in q) > 200


def test_cap_table_sums_to_one():
    for col in (1, 2, 3):
        assert close(sum(row[col] for row in m.cap_table()), 1.0)
