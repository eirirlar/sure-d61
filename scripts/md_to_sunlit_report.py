"""Convert a Markdown file to a Sunlit Sea-styled PDF report (long-form).

Pandoc + XeLaTeX renders an A4 article in Arial body + Everett headings,
with the Sunlit Sea colour palette. Companion to md_to_slides.py (which
is for slide decks) and md_to_letter.py (which is for letterhead letters).

Usage::

    python scripts/md_to_sunlit_report.py path/to/input.md
    python scripts/md_to_sunlit_report.py path/to/input.md -o custom/out.pdf

Title / author / date come from YAML frontmatter if present:
    title: "Work instruction — ..."
    author: "Sunlit Sea AS"
    date: "2026-10-19"

The styling header lives in scripts/sunlit_sea_report_header.tex.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HEADER_TEX = Path(__file__).with_name("sunlit_sea_report_header.tex")
FONTS_DIR = REPO_ROOT / "visual_profile" / "fonts"


def _font_prelude(path: Path, md_dir: Path) -> Path:
    """Write a prelude that loads Everett and sets \\graphicspath to md_dir."""
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
        cmd = ["pandoc", str(input_md),
               "--pdf-engine=xelatex",
               f"--resource-path={input_md.parent}",
               "-V", "lang=en",
               "-V", "documentclass=article",
               "--number-sections=false",
               "--toc",
               "--toc-depth=2"]
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
                pass
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
