"""Tests for fetch_gsheet.py (cell walk, Markdown dump) and compare_gsheet_xlsx.py, without the Google API.

A fake snapshot is built from the D7.4 download itself (formulas as entered, cached values as computed).
Compared with the same file it must come out clean apart from the UNSUPPORTED-wrapped cells; planted
differences must each land in the right category.

Run: python -m pytest -p no:cacheprovider scripts/test_compare_gsheet_xlsx.py
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

import openpyxl
import pytest

sys.path.insert(0, str(Path(__file__).parent))
import compare_gsheet_xlsx as cmp  # noqa: E402
import fetch_gsheet as fg  # noqa: E402

XLSX = Path(__file__).resolve().parents[1] / "surewave/background/2025-09-05_surewave_d7.4_costs_v2.xlsx"


def ev(v):
    if v is None:
        return None
    if isinstance(v, bool):
        return {"boolValue": v}
    if isinstance(v, (int, float)):
        return {"numberValue": v}
    if isinstance(v, str) and v.startswith("="):
        return {"formulaValue": v}
    return {"stringValue": str(v)}


@pytest.fixture(scope="module")
def snap():
    wf = openpyxl.load_workbook(XLSX)
    wv = openpyxl.load_workbook(XLSX, data_only=True)
    sheets = []
    for i, t in enumerate(wf.sheetnames):
        rows = []
        for r in range(1, wf[t].max_row + 1):
            vals = []
            for c in range(1, wf[t].max_column + 1):
                f = wf[t].cell(r, c).value
                f = cmp.xlsx_formula(f) or f
                inner, _ = cmp.unwrap(f) if isinstance(f, str) else (f, False)
                vals.append({"userEnteredValue": ev(inner), "effectiveValue": ev(wv[t].cell(r, c).value)})
            rows.append({"values": vals})
        sheets.append({"properties": {"title": t, "index": i}, "data": [{"startRow": 0, "startColumn": 0, "rowData": rows}]})
    return {"properties": {"title": "test"}, "sheets": sheets,
            "_meta": {"spreadsheet_id": "x", "fetched": "now", "modified_time": "then", "version": "1"}}


def test_self_comparison_is_clean(snap):
    res = cmp.compare(snap, XLSX)
    for k in ("lost", "changed", "added", "input", "computed", "only_gsheet", "only_xlsx"):
        assert res[k] == [], (k, res[k][:3])
    assert {c for _, c, *_ in res["wrapped"]} >= {"AA4", "AA5"}


def cell(snap, sheet, addr):
    sh = next(s for s in snap["sheets"] if s["properties"]["title"] == sheet)
    col, row = openpyxl.utils.cell.coordinate_from_string(addr)
    return sh["data"][0]["rowData"][row - 1]["values"][openpyxl.utils.column_index_from_string(col) - 1]


def test_planted_differences(snap):
    s = copy.deepcopy(snap)
    cell(s, "sens_discounts", "C2")["userEnteredValue"] = {"formulaValue": "=out_loc!F23"}       # lost
    cell(s, "out_loc", "L20")["userEnteredValue"] = {"formulaValue": "=in_loc!L19*in_loc!L25"}   # changed
    cell(s, "in_gen", "C24")["userEnteredValue"] = {"numberValue": 2500}                         # input
    cell(s, "in_loc", "D25")["userEnteredValue"] = {"formulaValue": "=1+1"}                       # gsheet formula over typed value
    res = cmp.compare(s, XLSX)
    assert sorted((t, c) for t, c, *_ in res["lost"]) == [("in_loc", "D25"), ("sens_discounts", "C2")]
    assert [c for _, c, *_ in res["changed"]] == ["L20"]
    assert [c for _, c, *_ in res["input"]] == ["C24"]


def test_normalisation():
    assert cmp.norm("=_xlfn.SEQUENCE(1, 3)") == cmp.norm("=sequence(1,3)")
    assert cmp.norm('=A1&" x "') != cmp.norm('=A1&"x"')
    assert cmp.norm("=ARRAYFORMULA(A1:A3*2)") == cmp.norm("=A1:A3*2")
    f, w = cmp.unwrap('=IFERROR(__xludf.UNSUPPORTED("FILTER(A:A, B:B=""x"")"),42)')
    assert w and f == '=FILTER(A:A, B:B="x")'


def test_markdown_dump(snap, tmp_path):
    p = tmp_path / "snap.md"
    fg.write_md(snap, p)
    text = p.read_text(encoding="utf-8")
    assert "## Sheet `out_loc`" in text and "| L20 | `=in_loc!L$22*" in text
    assert fg.col_letter(0) == "A" and fg.col_letter(26) == "AA" and fg.col_letter(29) == "AD"
