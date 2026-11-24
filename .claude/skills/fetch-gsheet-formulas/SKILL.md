---
name: fetch-gsheet-formulas
description: Snapshot a Google Sheet with every cell's formula and computed value through the Google Sheets API (scripts/fetch_gsheet.py), and compare it cell by cell with any .xlsx download of it (scripts/compare_gsheet_xlsx.py). Trigger before analysing, rebuilding, testing or quoting results from any model built in Google Sheets (for example the SUREWAVE D7.4 cost model), when the user gives a docs.google.com/spreadsheets link, or when work rests on a downloaded .xlsx of a Google Sheet. A Drive download to .xlsx is lossy and never counts as the source.
---

# fetch-gsheet-formulas

## Why

A Drive download of a Google Sheet to `.xlsx` drops or freezes formulas Excel does not support, and it cannot show what it lost. Precedent T157: the D7.4 cost model was rebuilt from the download, the API fetch was skipped, and later work rested on an unverified copy. The rule in `CLAUDE.md` makes the API snapshot the source.

## Steps

1. Get the sheet link from the user or the task notes. Do not guess links. Check what the link points to before relying on it (name, tabs, last-modified time). Precedent: the T157 link pointed to an unrelated budget sheet.
   - If the file is an xlsx stored on Drive and edited in Google Sheets (Office editing), the Sheets API cannot read it. Download it unchanged with `python scripts/fetch_drive_file.py <link> <out.xlsx>` and catalogue the formulas Google Sheets saved in its own form: `__xludf.DUMMYFUNCTION("…")` wrappers and new functions without the `_xlfn.` prefix. These break in Excel and LibreOffice. Example: `surewave/background/2025-07-03_surewave_d7.4_costs_original.md`.
2. Check prerequisites:
   - packages `google-api-python-client`, `google-auth`, `google-auth-oauthlib` (`python -c "import googleapiclient, google_auth_oauthlib"`);
   - `secrets/credentials.json`: OAuth client of type "Desktop app" from Google Cloud Console, with the Google Sheets API and the Google Drive API enabled in its project. Missing: ask the user to create it and save it there.
   - `secrets/token.json` (`secrets/token_drive.json` for `fetch_drive_file.py`): missing means the first sign-in has not been done. Run the script in the background; it prints the sign-in URL instead of opening a browser. Give the user the URL to approve with an account that can open the file; the script continues by itself. The user does not run Python.
3. Snapshot: `python scripts/fetch_gsheet.py <link> [--out <folder>] [--name <slug>]`. Default output `surewave/background/<date>_<slug>_gsheet_snapshot.json` and `.md`. The Drive last-modified time is recorded inside.
4. Compare with every download in use: `python scripts/compare_gsheet_xlsx.py <snapshot.json> <download.xlsx>`. Read the summary: lost formulas, wrapped (UNSUPPORTED) formulas, changed formula text, inputs and computed values that differ.
5. Report to the user: counts per category, what each lost or changed formula does, and which earlier conclusions or files depend on the affected cells. A finding stands only once checked against the snapshot.
6. Ask the user to check Extensions → Apps Script in the sheet; bound scripts are not in the snapshot.

## Do not

- Do not treat a download as the model, or mark a task done while the comparison is open (`[~]` instead).
- Do not commit `secrets/`.
- Do not write to the Google Sheet; the scopes are read-only.
