"""Snapshot a Google Sheet with every cell's formula and computed value, through the Google Sheets API.

Why: a Drive download to .xlsx is lossy. Formulas Excel does not support are wrapped or frozen, and the
download cannot show what was lost. This script reads the sheet as Google stores it: for each cell the
text as entered (the formula, or the typed value) and the value Google computed.

Usage:
    python scripts/fetch_gsheet.py <sheet link or ID> [--out DIR] [--name SLUG]

Writes, in --out (default surewave/background):
    <date>_<slug>_gsheet_snapshot.json   full API response (sheets, cells, named ranges) plus Drive metadata
    <date>_<slug>_gsheet_snapshot.md     readable dump: per sheet, every formula cell and every constant
<date> is the fetch date; the sheet's last-modified time on Drive is recorded inside both files.

Sign-in: OAuth client of type "Desktop app" in secrets/credentials.json (git-ignored, per machine).
The first run opens the browser for consent and stores secrets/token.json. Read-only scopes only.
Claude must not start the first sign-in; the user runs it: ! python scripts/fetch_gsheet.py <link>

Not covered: Apps Script bound to the sheet (needs the Apps Script API); check Extensions -> Apps Script
by hand.

Packages: google-api-python-client, google-auth, google-auth-oauthlib.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly",
          "https://www.googleapis.com/auth/drive.metadata.readonly"]
CELL_FIELDS = "userEnteredValue,effectiveValue,formattedValue"
FIELDS = ("properties(title,locale,timeZone),namedRanges,"
          "sheets(properties(sheetId,title,index,hidden,gridProperties),"
          f"data(startRow,startColumn,rowData(values({CELL_FIELDS}))))")


def sheet_id(link: str) -> str:
    m = re.search(r"/spreadsheets/d/([A-Za-z0-9_-]+)", link)
    return m.group(1) if m else link


def load_credentials(credentials_file: Path, token_file: Path):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    creds = Credentials.from_authorized_user_file(str(token_file), SCOPES) if token_file.exists() else None
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    if not creds or not creds.valid:
        if not credentials_file.exists():
            sys.exit(f"Missing OAuth client file: {credentials_file}")
        flow = InstalledAppFlow.from_client_secrets_file(str(credentials_file), SCOPES)
        creds = flow.run_local_server(port=0, open_browser=False,
                                      authorization_prompt_message="Open this URL to approve access:\n{url}\n")
        token_file.parent.mkdir(parents=True, exist_ok=True)
        token_file.write_text(creds.to_json(), encoding="utf-8")
    return creds


def col_letter(n: int) -> str:  # 0-based
    s = ""
    n += 1
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def scalar(v: dict | None):
    """Value of an ExtendedValue: formula text, number, string, bool or error."""
    if not v:
        return None
    for k in ("formulaValue", "numberValue", "stringValue", "boolValue"):
        if k in v:
            return v[k]
    if "errorValue" in v:
        e = v["errorValue"]
        return f"#ERROR {e.get('type', '')}: {e.get('message', '')}".strip()
    return None


def cells(sheet: dict):
    """Yield (A1 address, entered, effective, formatted) for every non-empty cell of a sheet."""
    for block in sheet.get("data", []):
        r0, c0 = block.get("startRow", 0), block.get("startColumn", 0)
        for i, row in enumerate(block.get("rowData", [])):
            for j, cell in enumerate(row.get("values", []) or []):
                entered = scalar(cell.get("userEnteredValue"))
                effective = scalar(cell.get("effectiveValue"))
                if entered is None and effective is None:
                    continue
                yield f"{col_letter(c0 + j)}{r0 + i + 1}", entered, effective, cell.get("formattedValue")


def md_escape(x) -> str:
    s = "" if x is None else str(x)
    return s.replace("|", "\\|").replace("\n", " ")


def write_md(snap: dict, path: Path) -> None:
    meta = snap["_meta"]
    out = [f"# Google Sheet snapshot: {md_escape(snap['properties']['title'])}", "",
           f"- Spreadsheet ID: `{meta['spreadsheet_id']}`",
           f"- Last modified on Drive: {meta.get('modified_time', 'unknown')} (Drive version {meta.get('version', '?')})",
           f"- Fetched: {meta['fetched']} with the Google Sheets API (`spreadsheets.get`, includeGridData)",
           "- Entered = the cell as written in Google Sheets (formula or typed value). "
           "Computed = the value Google Sheets calculated. A cell with a computed value and no entered value "
           "is filled by an array formula in another cell (spill).", ""]
    if snap.get("namedRanges"):
        out += ["## Named ranges", "", "| Name | Range |", "|---|---|"]
        for nr in snap["namedRanges"]:
            out.append(f"| {md_escape(nr.get('name'))} | {md_escape(json.dumps(nr.get('range')))} |")
        out.append("")
    out += ["## Sheets", "", "| # | Sheet | Hidden | Formulas | Constants | Spill cells |", "|---:|---|---|---:|---:|---:|"]
    for sh in snap["sheets"]:
        cs = list(cells(sh))
        nf = sum(isinstance(e, str) and e.startswith("=") for _, e, _, _ in cs)
        ns = sum(e is None for _, e, _, _ in cs)
        p = sh["properties"]
        out.append(f"| {p['index']} | {md_escape(p['title'])} | {'yes' if p.get('hidden') else ''} | {nf} | {len(cs) - nf - ns} | {ns} |")
    for sh in snap["sheets"]:
        p = sh["properties"]
        cs = list(cells(sh))
        out += ["", f"## Sheet `{p['title']}`", "", "### Formulas", "", "| Cell | Formula | Computed |", "|---|---|---|"]
        out += [f"| {a} | `{md_escape(e)}` | {md_escape(f if f is not None else v)} |"
                for a, e, v, f in cs if isinstance(e, str) and e.startswith("=")]
        out += ["", "### Constants and spill cells", "", "| Cell | Entered | Computed |", "|---|---|---|"]
        out += [f"| {a} | {md_escape(e) if e is not None else '(spill)'} | {md_escape(f if f is not None else v)} |"
                for a, e, v, f in cs if not (isinstance(e, str) and e.startswith("="))]
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("link")
    ap.add_argument("--out", type=Path, default=Path("surewave/background"))
    ap.add_argument("--name", default="surewave_d7.4_costs")
    ap.add_argument("--credentials", type=Path, default=Path("secrets/credentials.json"))
    ap.add_argument("--token", type=Path, default=Path("secrets/token.json"))
    a = ap.parse_args()
    from googleapiclient.discovery import build
    creds = load_credentials(a.credentials, a.token)
    sid = sheet_id(a.link)
    snap = build("sheets", "v4", credentials=creds).spreadsheets().get(
        spreadsheetId=sid, includeGridData=True, fields=FIELDS).execute()
    drive = build("drive", "v3", credentials=creds).files().get(
        fileId=sid, fields="name,modifiedTime,version", supportsAllDrives=True).execute()
    today = dt.date.today().isoformat()
    snap["_meta"] = {"spreadsheet_id": sid, "fetched": dt.datetime.now().isoformat(timespec="seconds"),
                     "modified_time": drive.get("modifiedTime"), "version": drive.get("version"),
                     "drive_name": drive.get("name")}
    a.out.mkdir(parents=True, exist_ok=True)
    base = a.out / f"{today}_{a.name}_gsheet_snapshot"  # names may contain dots (d7.4): no with_suffix
    Path(f"{base}.json").write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
    write_md(snap, Path(f"{base}.md"))
    n = sum(1 for sh in snap["sheets"] for _ in cells(sh))
    print(f"OK {len(snap['sheets'])} sheets, {n} non-empty cells -> {base}.json / .md")


if __name__ == "__main__":
    main()
