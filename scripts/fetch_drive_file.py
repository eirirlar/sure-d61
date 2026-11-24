"""Download a file from Google Drive exactly as stored (no conversion), with its Drive metadata.

Usage:
    python scripts/fetch_drive_file.py <Drive link or file ID> <output path>

For an uploaded file (xlsx, pdf, docx, ...) the bytes are saved unchanged (Drive API files.get alt=media);
this is the file itself, not a Google export. The output's modification time is set to the Drive
"last modified" time, and the metadata (name, MIME type, size, MD5, modified time, version) is printed
as JSON. Native Google files (Docs, Sheets) cannot be downloaded unchanged; use fetch_gsheet.py for Sheets.

Sign-in: secrets/credentials.json (Desktop-app OAuth client). Own token secrets/token_drive.json with the
read-only scope drive.readonly; the first run prints a URL to approve (the browser redirects to localhost).

Packages: google-api-python-client, google-auth, google-auth-oauthlib.
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import os
import re
import sys
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def file_id(link: str) -> str:
    for pat in (r"/d/([A-Za-z0-9_-]+)", r"[?&]id=([A-Za-z0-9_-]+)"):
        m = re.search(pat, link)
        if m:
            return m.group(1)
    return link


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


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("link")
    ap.add_argument("out", type=Path)
    ap.add_argument("--credentials", type=Path, default=Path("secrets/credentials.json"))
    ap.add_argument("--token", type=Path, default=Path("secrets/token_drive.json"))
    a = ap.parse_args()
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseDownload
    drive = build("drive", "v3", credentials=load_credentials(a.credentials, a.token))
    fid = file_id(a.link)
    meta = drive.files().get(fileId=fid, supportsAllDrives=True,
                             fields="id,name,mimeType,size,md5Checksum,modifiedTime,createdTime,version").execute()
    if meta["mimeType"].startswith("application/vnd.google-apps."):
        sys.exit(f"{meta['name']} is a native Google file ({meta['mimeType']}); use fetch_gsheet.py for Sheets.")
    buf = io.BytesIO()
    dl = MediaIoBaseDownload(buf, drive.files().get_media(fileId=fid, supportsAllDrives=True))
    done = False
    while not done:
        _, done = dl.next_chunk()
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_bytes(buf.getvalue())
    t = dt.datetime.fromisoformat(meta["modifiedTime"].replace("Z", "+00:00")).timestamp()
    os.utime(a.out, (t, t))
    print(json.dumps(meta, ensure_ascii=False, indent=1))
    print(f"OK {len(buf.getvalue())} bytes -> {a.out}")


if __name__ == "__main__":
    main()
