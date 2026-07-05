"""Convert Markdown image references between Pandoc-native and raw-HTML form.

Two modes:

--to-html (default): rewrite Pandoc-native image syntax
    ![CAPTION](PATH){width=Npx}
to HTML <figure>/<img>/<figcaption>:
    <figure>
    <img src="PATH" alt="CAPTION" width="N" />
    <figcaption>CAPTION</figcaption>
    </figure>

Use this to make captions visible in renderers that don't understand Pandoc's
`{width=Npx}` attribute syntax (VS Code preview, GitHub Flavored Markdown,
most non-Pandoc renderers).

--to-markdown: reverse — rewrite the HTML <figure> block back to Pandoc-native
image syntax. Use this before running Pandoc to build PDF/DOCX — Pandoc's
LaTeX writer does not reliably map raw HTML <img> to \\includegraphics, so
PDFs come out without images.

The two modes are inverses. Round-tripping a file through --to-html then
--to-markdown returns it to the original form (indentation preserved).

Safe by default — writes to <name>.htmlimg.md / <name>.pandoc.md sibling;
use --in-place to overwrite. Prints per-file word-count delta.

Usage:
    python scripts/md_image_to_html.py <file.md>                       # to HTML
    python scripts/md_image_to_html.py --to-markdown <file.md>         # to Pandoc syntax
    python scripts/md_image_to_html.py --in-place <file.md>            # overwrite
    python scripts/md_image_to_html.py --dry-run <file.md>             # count only
    python scripts/md_image_to_html.py --width N <file.md>             # override default width (only used for --to-html when input has no width)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

IMG_RE = re.compile(
    r"^(?P<indent>\s*)!\[(?P<caption>.*?)\]\((?P<path>[^)]+)\)(?:\{width=(?P<w>\d+)px\})?\s*$"
)

# Multi-line HTML <figure>/<img>/<figcaption> block produced by --to-html.
# Captures indent, src, alt/caption, width — same shape on every line.
FIGURE_RE = re.compile(
    r"^(?P<indent>\s*)<figure>\s*\n"
    r"(?P=indent)<img src=\"(?P<path>[^\"]+)\" alt=\"(?P<alt>[^\"]*)\" width=\"(?P<w>\d+)\" ?/>\s*\n"
    r"(?P=indent)<figcaption>(?P<caption>[^<]*)</figcaption>\s*\n"
    r"(?P=indent)</figure>",
    re.MULTILINE,
)


def to_pandoc(text: str) -> tuple[str, int]:
    """HTML <figure> block → Pandoc-native ![caption](path){width=Npx}."""
    count = 0

    def repl(m: re.Match) -> str:
        nonlocal count
        count += 1
        indent = m.group("indent")
        # Prefer the visible caption over the alt attribute (they should match,
        # but if they differ, figcaption is the human-visible text).
        caption = m.group("caption") or m.group("alt")
        # Un-escape the &quot; we injected on the way in.
        caption = caption.replace("&quot;", '"')
        path = m.group("path")
        width = m.group("w")
        return f"{indent}![{caption}]({path}){{width={width}px}}"

    out = FIGURE_RE.sub(repl, text)
    return out, count


def rewrite(text: str, default_width: int) -> tuple[str, int]:
    lines_in = text.splitlines(keepends=False)
    lines_out: list[str] = []
    count = 0
    for line in lines_in:
        m = IMG_RE.match(line)
        if not m:
            lines_out.append(line)
            continue
        indent = m.group("indent")
        caption = m.group("caption")
        path = m.group("path")
        width = m.group("w") or str(default_width)
        # Escape a couple of HTML special chars in the alt/caption. Deliberately
        # NOT escaping < > because captions here are plain text.
        alt = caption.replace('"', "&quot;")
        lines_out.append(f"{indent}<figure>")
        lines_out.append(f'{indent}<img src="{path}" alt="{alt}" width="{width}" />')
        lines_out.append(f"{indent}<figcaption>{caption}</figcaption>")
        lines_out.append(f"{indent}</figure>")
        count += 1
    return "\n".join(lines_out) + ("\n" if text.endswith("\n") else ""), count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--in-place", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    direction = parser.add_mutually_exclusive_group()
    direction.add_argument("--to-html", action="store_true", help="Markdown -> HTML <figure> (default)")
    direction.add_argument("--to-markdown", action="store_true", help="HTML <figure> -> Pandoc-native Markdown")
    parser.add_argument("--width", type=int, default=451, help="default width in px when the input has no explicit width (only used for --to-html)")
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    reverse = args.to_markdown  # to-html is default

    for path_str in args.files:
        path = Path(path_str)
        original = path.read_text(encoding="utf-8")
        if reverse:
            cleaned, n = to_pandoc(original)
            sibling_suffix = ".pandoc.md"
        else:
            cleaned, n = rewrite(original, args.width)
            sibling_suffix = ".htmlimg.md"
        words_before = len(original.split())
        words_after = len(cleaned.split())
        print(f"  {n} images rewritten. words {words_before} -> {words_after}  {path.name}")
        if args.dry_run:
            continue
        if args.in_place:
            path.write_text(cleaned, encoding="utf-8", newline="\n")
        else:
            out = path.with_suffix(sibling_suffix)
            out.write_text(cleaned, encoding="utf-8", newline="\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
