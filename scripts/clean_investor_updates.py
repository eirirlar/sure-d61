"""Clean investor-update .md files under `background/`.

The pandoc/pdftotext conversions in `background/new/` leave three kinds of noise
in the resulting Markdown:

1. **Top mail-header block** (PDF-derived files only) — Gmail print headers,
   From/To lines, subject line, timestamp, `1 message` etc.
2. **Mid-body page-print repeats** — every page break in a Gmail-printed PDF
   inserts a `Kodeworks AS Mail - <subject>` line and a
   `https://mail.google.com/…` URL.
3. **Trailing signature block** — `Mvh`, name, contact line
   (`sunlitsea.no | +47 …`), Google Groups unsubscribe boilerplate, final URL.

The cleaner strips all three, preserves the YAML frontmatter, and never touches
document body content in between.

## Safety

**Default mode writes a sibling file `<name>.cleaned.md`.** It does not modify
the original. Compare the original vs. `.cleaned.md`, confirm the diff is what
you expected, then either rename manually or re-run with `--in-place`.

Never use `--in-place` on a batch without first doing a `--dry-run` word-count
comparison. Two files in an earlier run were catastrophically truncated
(~90% loss) because a regex pattern (`^-{2,}$`) intended to match email
`-- ` separators also matched pandoc-generated `---` markdown horizontal
rules. That pattern has been removed; the current signature-start set is
`Mvh` / `Med vennlig hilsen` / `-- ` (dash-dash-space, exact) / Google Groups
unsubscribe / trailing contact-info lines.

## Usage

    # Safe default — write <name>.cleaned.md sibling files
    python scripts/clean_investor_updates.py background/*.md

    # Dry-run — print per-file word-count before/after, no writes
    python scripts/clean_investor_updates.py --dry-run background/*.md

    # In-place — overwrites originals; only use after a dry-run looks safe
    python scripts/clean_investor_updates.py --in-place background/*.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MID_BODY_DROP = [
    re.compile(r"^\s*\d+/\d+/\d+,\s+\d+:\d+\s*(?:AM|PM)?\s+Kodeworks AS Mail"),
    re.compile(r"^https://mail\.google\.com/mail/"),
]

HEADER_LINE_PATTERNS = [
    re.compile(r"^\s*Eirik Larsen\s*<"),
    re.compile(r"^\s*Per Lindberg\s*<"),
    re.compile(r"^\s*per@sunlitsea\.no"),
    re.compile(r"^\s*eirik\.larsen@kodeworks\.no"),
    re.compile(r"^\s*(?:To|Cc|Bcc|From|Subject|Reply-To):\s"),
    re.compile(r"^\s*Sunlit Sea l[øo]ypemelding\s*$", re.IGNORECASE),
    re.compile(r"^\s*L[øo]ypemelding( fra Sunlit Sea)?\s*$", re.IGNORECASE),
    re.compile(r"^\s*RE:\s", re.IGNORECASE),
    re.compile(r"^\s*FW:\s", re.IGNORECASE),
    re.compile(r"^\s*\d+ messages?\s*$"),
    re.compile(r"^\s*(?:Sun|Mon|Tue|Wed|Thu|Fri|Sat), .*\d{4}"),
]

# Signature-start patterns. Deliberately narrow — anything that could match a
# legitimate body line has been removed. The bad `^-{2,}$` pattern (matches
# markdown horizontal rules) is NOT in this list.
SIG_START_PATTERNS = [
    re.compile(r"^Mvh\s*$", re.IGNORECASE),
    re.compile(r"^Med vennlig hilsen", re.IGNORECASE),
    re.compile(r"^-- $"),  # email separator: exactly dash-dash-space, no more
    re.compile(r"^You received this message", re.IGNORECASE),
]

# Contact-info tail patterns. Stripped only when they appear in the last 20%
# of the body — never mid-document (that would risk hitting a body sentence
# mentioning a phone number or URL).
CONTACT_TAIL_PATTERNS = [
    re.compile(r"^\s*sunlitsea\.no\s*\|\s*\+47"),
    re.compile(r"^\s*kodeworks\.no\s*\|\s*\+47"),
    re.compile(r"^\s*\+47[\s\d]+$"),
    re.compile(r"^\s*Eirik Larsen,\s*(Daglig leder|CEO|CFO)", re.IGNORECASE),
    re.compile(r"^\s*Per Lindberg,\s*(Daglig leder|CEO|CFO)", re.IGNORECASE),
    re.compile(r"^\s*per@sunlitsea\.no\s*$"),
    re.compile(r"^\s*eirik@sunlitsea\.no\s*$"),
]

BLANK = re.compile(r"^\s*$")


def is_header(line: str) -> bool:
    return any(p.match(line) for p in HEADER_LINE_PATTERNS)


def is_sig_start(line: str) -> bool:
    stripped = line.rstrip("\r\n")
    return any(p.match(stripped) for p in SIG_START_PATTERNS)


def is_mid_drop(line: str) -> bool:
    return any(p.match(line) for p in MID_BODY_DROP)


def is_contact_tail(line: str) -> bool:
    return any(p.match(line) for p in CONTACT_TAIL_PATTERNS)


def clean(text: str) -> str:
    # Split off YAML frontmatter (kept verbatim).
    yaml = ""
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            yaml = text[: end + 5]
            body = text[end + 5 :]

    lines = body.splitlines()

    # Pass 1: drop mid-body page-print repeats.
    lines = [l for l in lines if not is_mid_drop(l)]

    # Pass 2: strip top mail-header block if present. Trigger only if at least
    # 2 clear header-line matches appear in the first 15 non-blank lines
    # (avoids false positives on DOCX files that already start with real
    # content).
    top_nonblank = [l for l in lines[:15] if l.strip()]
    header_hits = sum(1 for l in top_nonblank if is_header(l))
    if header_hits >= 2:
        i = 0
        while i < len(lines):
            l = lines[i]
            if BLANK.match(l) or is_header(l):
                i += 1
                continue
            break
        lines = lines[i:]

    # Pass 3: signature-start markers strip only forward from top. Because the
    # patterns are narrow (Mvh / Med vennlig hilsen / -- / Google Groups) it is
    # safe to strip everything from the first match to end.
    end = len(lines)
    for i, l in enumerate(lines):
        if is_sig_start(l):
            end = i
            break
    lines = lines[:end]

    # Pass 4: strip contact-info tail lines from the last 20% of the file. This
    # catches signature blocks that had no `Mvh` header — just name + phone.
    if lines:
        tail_start = max(0, int(len(lines) * 0.80))
        # Walk backward from end; drop contact-info and blank lines.
        while len(lines) > tail_start:
            last = lines[-1]
            if BLANK.match(last) or is_contact_tail(last):
                lines.pop()
                continue
            break

    # Trim leading/trailing blank lines.
    while lines and BLANK.match(lines[0]):
        lines.pop(0)
    while lines and BLANK.match(lines[-1]):
        lines.pop()

    return yaml + "\n" + "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite the original file. Only use after --dry-run looks safe.",
    )
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Report per-file word count before/after, do not write anything.",
    )
    parser.add_argument("files", nargs="+", help="Markdown files to clean.")
    args = parser.parse_args()

    for path_str in args.files:
        path = Path(path_str)
        if not path.is_file():
            print(f"SKIP  not a file: {path}", file=sys.stderr)
            continue
        original = path.read_text(encoding="utf-8")
        cleaned = clean(original)

        words_before = len(original.split())
        words_after = len(cleaned.split())
        pct = 100 * words_after / words_before if words_before else 0
        marker = "  " if pct >= 70 else " !"  # flag suspicious shrinkage
        print(f"{marker}  {words_before:5d} -> {words_after:5d} ({pct:5.1f}%)  {path.name}")

        if args.dry_run:
            continue
        if args.in_place:
            path.write_text(cleaned, encoding="utf-8", newline="\n")
        else:
            out = path.with_suffix(".cleaned.md")
            out.write_text(cleaned, encoding="utf-8", newline="\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
