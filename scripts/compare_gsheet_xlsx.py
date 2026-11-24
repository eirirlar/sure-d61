"""Compare a Google Sheet snapshot (from fetch_gsheet.py) with an .xlsx download of the same sheet, cell by cell.

Usage:
    python scripts/compare_gsheet_xlsx.py <snapshot.json> <download.xlsx> [--out report.md]

Report categories (one table each):
    lost          formula in the Google Sheet, plain value in the download (the formula is gone)
    wrapped       formula kept only inside __xludf.UNSUPPORTED(...) with a frozen fallback value
    changed       formula in both, different text after normalisation
    added         formula in the download, none in the Google Sheet (the sheet was changed after the download)
    input         typed value differs (an input changed after the download)
    computed      both have the same formula or input, but the computed values differ
    only_gsheet / only_xlsx   cell or sheet present on one side only
Spill cells (filled by an array formula elsewhere) are compared on value only.

Normalisation before formula comparison: Excel prefixes (_xlfn., _xlws., _xlpm.) removed, an outer
ARRAYFORMULA(...) removed, whitespace outside string literals removed, case ignored outside strings.

Packages: openpyxl.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).parent))
from fetch_gsheet import cells  # noqa: E402

UNSUP = re.compile(r'^=IFERROR\(__xludf\.UNSUPPORTED\("((?:[^"]|"")*)"\),(.*)\)$', re.S)


def norm(f: str) -> str:
    f = f.strip()
    f = re.sub(r"_xl(fn|ws|pm)\.", "", f)
    parts = re.split(r'("(?:[^"]|"")*")', f)  # keep string literals intact
    s = "".join(p if p.startswith('"') else re.sub(r"\s+", "", p).upper() for p in parts)
    if s.startswith("=ARRAYFORMULA(") and s.endswith(")"):
        s = "=" + s[len("=ARRAYFORMULA("):-1]
    return s


def unwrap(f: str) -> tuple[str, bool]:
    m = UNSUP.match(f.strip())
    if not m:
        return f, False
    return "=" + m.group(1).replace('""', '"').lstrip("="), True


def xlsx_formula(v) -> str | None:
    if type(v).__name__ == "ArrayFormula":
        return v.text
    if isinstance(v, str) and v.startswith("="):
        return v
    return None


def same_value(a, b, tol=1e-9) -> bool:
    if a is None and b in (None, ""):
        return True
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(a, b, rel_tol=tol, abs_tol=tol)
    return str(a).strip() == str(b).strip()


def compare(snap: dict, xlsx: Path) -> dict[str, list]:
    wf = openpyxl.load_workbook(xlsx)
    wv = openpyxl.load_workbook(xlsx, data_only=True)
    res = {k: [] for k in ("lost", "wrapped", "changed", "added", "input", "computed", "only_gsheet", "only_xlsx")}
    gs_titles = [s["properties"]["title"] for s in snap["sheets"]]
    for t in wf.sheetnames:
        if t not in gs_titles:
            res["only_xlsx"].append((t, "(whole sheet)", "", ""))
    for sh in snap["sheets"]:
        t = sh["properties"]["title"]
        if t not in wf.sheetnames:
            res["only_gsheet"].append((t, "(whole sheet)", "", ""))
            continue
        fs, vs = wf[t], wv[t]
        seen = set()
        for addr, entered, effective, _ in cells(sh):
            seen.add(addr)
            xf = xlsx_formula(fs[addr].value)
            xv = vs[addr].value
            g_is_f = isinstance(entered, str) and entered.startswith("=")
            if g_is_f:
                if xf is None:
                    (res["lost"] if xv is not None else res["only_gsheet"]).append((t, addr, entered, xv))
                    continue
                inner, wrapped = unwrap(xf)
                if wrapped:
                    res["wrapped"].append((t, addr, entered, xf))
                if norm(inner) != norm(entered):
                    res["changed"].append((t, addr, entered, xf))
                elif not same_value(effective, xv, 1e-6):
                    res["computed"].append((t, addr, effective, xv))
            elif entered is None:  # spill cell
                if not same_value(effective, xv, 1e-6):
                    res["computed"].append((t, addr, effective, xv))
            else:
                if xf is not None:
                    res["added"].append((t, addr, entered, xf))
                elif xv is None:
                    res["only_gsheet"].append((t, addr, entered, ""))
                elif not same_value(entered, xv):
                    res["input"].append((t, addr, entered, xv))
        for row in fs.iter_rows():
            for c in row:
                if c.value is not None and c.coordinate not in seen:
                    res["only_xlsx"].append((t, c.coordinate, "", xlsx_formula(c.value) or c.value))
    return res


TITLES = {
    "lost": ("Formulas lost in the download", "Google Sheet formula", "Download value"),
    "wrapped": ("Formulas wrapped as UNSUPPORTED in the download", "Google Sheet formula", "Download cell"),
    "changed": ("Formulas with different text", "Google Sheet formula", "Download formula"),
    "added": ("Formulas only in the download", "Google Sheet value", "Download formula"),
    "input": ("Typed values that differ", "Google Sheet", "Download"),
    "computed": ("Same formula or input, different computed value", "Google Sheet", "Download"),
    "only_gsheet": ("Only in the Google Sheet", "Google Sheet", "Download"),
    "only_xlsx": ("Only in the download", "Google Sheet", "Download"),
}


def esc(x) -> str:
    return ("" if x is None else str(x)).replace("|", "\\|").replace("\n", " ")


def report(res: dict, snap: dict, xlsx: Path) -> str:
    m = snap["_meta"]
    out = [f"# Google Sheet vs xlsx download: {esc(snap['properties']['title'])}", "",
           f"- Google Sheet snapshot: fetched {m['fetched']}, last modified on Drive {m.get('modified_time')}",
           f"- Download compared: `{xlsx.as_posix()}`", "", "## Summary", "", "| Category | Cells |", "|---|---:|"]
    out += [f"| {TITLES[k][0]} | {len(v)} |" for k, v in res.items()]
    for k, rows in res.items():
        if not rows:
            continue
        title, a, b = TITLES[k]
        out += ["", f"## {title}", "", f"| Sheet | Cell | {a} | {b} |", "|---|---|---|---|"]
        out += [f"| {esc(t)} | {c} | `{esc(x)}` | `{esc(y)}` |" for t, c, x, y in rows]
    return "\n".join(out) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("snapshot", type=Path)
    ap.add_argument("xlsx", type=Path)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    snap = json.loads(a.snapshot.read_text(encoding="utf-8"))
    res = compare(snap, a.xlsx)
    out = a.out or a.snapshot.with_name(a.snapshot.name.removesuffix(".json").replace("_snapshot", "_vs_download") + ".md")
    out.write_text(report(res, snap, a.xlsx), encoding="utf-8")
    print(" ".join(f"{k}={len(v)}" for k, v in res.items()), "->", out)


if __name__ == "__main__":
    main()
