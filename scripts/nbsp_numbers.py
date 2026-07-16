"""Bind thousands-separated number groups with non-breaking space (NBSP, U+00A0).

Problem: When Markdown documents with Norwegian-style thousands separators
(e.g. "18 570 858 kr") are converted to PDF via pandoc + xelatex, LaTeX
treats the regular space between digit groups as a valid line-break point,
producing ugly breaks like "18<newline>570 858" in narrow table columns.

Fix: replace the regular space (U+0020) between digit groups with NBSP
(U+00A0). Pandoc translates NBSP directly to LaTeX's non-breaking-space
mechanism, and Word treats NBSP as unbreakable too. Visually identical to
a regular space in every renderer (PDF, DOCX, VS Code preview, GitHub).

The substitution is idempotent — running twice produces no additional
change. Character count is unchanged (one char in, one char out); only the
character type changes.

Safe by default: writes to <name>.cleaned.md sibling and prints stats
(word/line/char counts before and after, NBSP substitution count, first few
changed lines). Use --promote to overwrite in place, only after inspecting
the dry-run output. Convention exists because of the T73 investor-update
incident where two files silently lost ~90% of content to an over-broad
regex.

Usage:
    python scripts/nbsp_numbers.py <file.md> ...                 # dry-run (default)
    python scripts/nbsp_numbers.py --promote <file.md> ...       # overwrite in place
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NBSP = " "

# Match a single regular space that sits between a digit and a 3-digit group
# terminated by a non-digit (or end of string / end of line). This matches
# Norwegian thousands-separators like "18 570 858" while leaving unrelated
# digit-space-digit patterns (like "1 måned" or "M18 May 2024") alone.
NBSP_PATTERN = re.compile(r"(\d) (\d{3})(?=\D|$)", re.MULTILINE)


def bind_numbers(text: str) -> tuple[str, int]:
    """Replace regular spaces inside thousands-separated numbers with NBSP.

    Applied repeatedly until stable — a single pass may miss overlapping
    matches like "1 234 567" where the second space is "captured" as part
    of the lookahead terminator for the first match.

    Returns (transformed_text, total_substitutions).
    """
    total = 0
    prev = None
    result = text
    replacement = "\\1" + NBSP + "\\2"
    while prev != result:
        prev = result
        result, n = NBSP_PATTERN.subn(replacement, result)
        total += n
    return result, total


def find_changed_lines(original: str, cleaned: str, limit: int = 5) -> list[tuple[int, str, str]]:
    """Return the first `limit` lines that differ, as (lineno, before, after)."""
    changes: list[tuple[int, str, str]] = []
    for i, (o, c) in enumerate(zip(original.splitlines(), cleaned.splitlines()), start=1):
        if o != c:
            changes.append((i, o, c))
            if len(changes) >= limit:
                break
    return changes


def process(path: Path, promote: bool) -> bool:
    """Process one file. Returns True on success, False on error."""
    if not path.exists():
        print(f"skip: {path} does not exist", file=sys.stderr)
        return False

    original = path.read_text(encoding="utf-8")
    cleaned, substitutions = bind_numbers(original)

    orig_words = len(original.split())
    orig_lines = original.count("\n") + (0 if original.endswith("\n") else 1)
    orig_chars = len(original)
    new_words = len(cleaned.split())
    new_lines = cleaned.count("\n") + (0 if cleaned.endswith("\n") else 1)
    new_chars = len(cleaned)

    print(f"{path}")
    print(f"  words:  {orig_words} -> {new_words}  (delta {new_words - orig_words:+d})")
    print(f"  lines:  {orig_lines} -> {new_lines}  (delta {new_lines - orig_lines:+d})")
    print(f"  chars:  {orig_chars} -> {new_chars}  (delta {new_chars - orig_chars:+d})")
    print(f"  NBSP substitutions: {substitutions}")

    if substitutions > 0:
        changed = find_changed_lines(original, cleaned, limit=5)
        print(f"  sample changed lines (NBSP shown as [_]):")
        for lineno, before, after in changed:
            after_disp = after.replace(NBSP, "[_]")
            print(f"    L{lineno} before: {before[:140]}")
            print(f"    L{lineno} after:  {after_disp[:140]}")

    if promote:
        path.write_text(cleaned, encoding="utf-8")
        print(f"  -> overwritten in place")
    else:
        out = path.with_name(path.stem + ".cleaned" + path.suffix)
        out.write_text(cleaned, encoding="utf-8")
        print(f"  -> wrote {out.name} (dry-run; re-run with --promote to overwrite)")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Bind thousands-separated number groups with NBSP for pandoc/LaTeX-safe PDF output."
    )
    ap.add_argument("files", nargs="+", type=Path, help="Markdown file(s) to process")
    ap.add_argument(
        "--promote",
        action="store_true",
        help="Overwrite in place instead of writing .cleaned sibling. Only use after inspecting dry-run output.",
    )
    args = ap.parse_args()

    ok = True
    for path in args.files:
        if not process(path, args.promote):
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
