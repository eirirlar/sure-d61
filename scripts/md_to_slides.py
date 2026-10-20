"""Convert a Markdown file to a Sunlit Sea-styled PDF slide deck.

Pandoc + XeLaTeX renders Beamer slides in 16:9 using Everett (headings)
and Arial (body), per the Sunlit Sea Visual Profile Overview under
visual_profile/. The styling header lives in
scripts/sunlit_sea_slides_header.tex and defines color palette, frame
title, footer and the `\\bignum` helper.

Usage::

    python scripts/md_to_slides.py path/to/input.md
    python scripts/md_to_slides.py path/to/input.md -o custom/out.pdf

Pandoc runs with --slide-level=2 — each `## Heading` begins a frame. Use
`## {.plain}` for custom chrome-free slides (title, section dividers,
closing) and inline a tikzpicture overlay for the visuals.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HEADER_TEX = Path(__file__).with_name("sunlit_sea_slides_header.tex")
FONTS_DIR = REPO_ROOT / "visual_profile" / "fonts"


def _font_prelude(path: Path, md_dir: Path) -> Path:
    """Write a prelude that loads Everett and sets \\graphicspath to md_dir.

    Relative image paths in raw \\includegraphics inside the markdown resolve
    from the markdown's directory, matching pandoc's --resource-path for
    markdown-syntax images.
    """
    fonts_abs = path.resolve().as_posix() + "/"
    md_abs = md_dir.resolve().as_posix() + "/"
    content = (
        "\\usepackage{fontspec}\n"
        f"\\newfontfamily\\everett[Path={fonts_abs}, Extension=.ttf, "
        "UprightFont=Everett-Regular-web, "
        "BoldFont=Everett-Bold-web]{Everett}\n"
        f"\\newfontfamily\\everettMedium[Path={fonts_abs}, "
        "Extension=.ttf]{Everett-Medium-web}\n"
        "\\usepackage{graphicx}\n"
        f"\\graphicspath{{{{{md_abs}}}}}\n"
    )
    tmp = Path(tempfile.mkstemp(suffix=".tex", prefix="sunlitfonts_")[1])
    tmp.write_text(content, encoding="utf-8")
    return tmp


def build(input_md: Path, output_pdf: Path) -> None:
    if not input_md.is_file():
        sys.exit(f"input not found: {input_md}")
    if not HEADER_TEX.is_file():
        sys.exit(f"header include not found: {HEADER_TEX}")
    if shutil.which("pandoc") is None:
        sys.exit("pandoc not on PATH")
    if shutil.which("xelatex") is None:
        sys.exit("xelatex not on PATH (needed as pandoc --pdf-engine)")

    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    prelude = _font_prelude(FONTS_DIR, input_md.parent) if FONTS_DIR.is_dir() else None
    try:
        cmd = ["pandoc", str(input_md), "-t", "beamer",
               "--pdf-engine=xelatex",
               "--slide-level=2",
               f"--resource-path={input_md.parent}",
               "-V", "aspectratio=169",
               "-V", "lang=nb-NO",
               "-V", "classoption=aspectratio=169"]
        if prelude:
            cmd += ["-H", str(prelude)]
        cmd += ["-H", str(HEADER_TEX),
                "-o", str(output_pdf)]
        print(" ".join(cmd))
        subprocess.check_call(cmd)
    finally:
        if prelude and prelude.exists():
            try:
                prelude.unlink()
            except OSError:
                pass  # xelatex may still have an open handle on Windows
    print(f"wrote {output_pdf}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="input markdown file")
    p.add_argument("-o", "--output", type=Path, default=None,
                   help="output PDF (default: input with .pdf extension)")
    args = p.parse_args()
    out = args.output or args.input.with_suffix(".pdf")
    build(args.input.resolve(), out.resolve())


if __name__ == "__main__":
    main()
