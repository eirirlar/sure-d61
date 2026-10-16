#!/usr/bin/env python
"""Convert a Markdown file to a .docx or .pdf on the Sunlit Sea letterhead.

Default: produces .docx via pandoc's ``--reference-doc`` option. The letterhead
docx contributes the SUNLIT SEA wordmark (first-page header), the cream "A"
watermark (every-page header), the Letter page size and margins, and the style
definitions. The Markdown becomes the body.

With ``--pdf``: produces .pdf via pandoc + xelatex. The wordmark and watermark
images are extracted on the fly from the letterhead .docx (so the .docx stays
the single source of truth); an ``eso-pic`` LaTeX header-include renders them
behind/over the pandoc-generated body at the same page positions as in Word.

Usage:
    python scripts/md_to_letter.py path/to/brev.md                 # .docx
    python scripts/md_to_letter.py --pdf path/to/brev.md           # .pdf
    python scripts/md_to_letter.py path/to/brev.md -o out.docx
    python scripts/md_to_letter.py --pdf path/to/brev.md -o out.pdf
    python scripts/md_to_letter.py path/to/brev.md --letterhead other.docx
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LETTERHEAD = (
    REPO_ROOT / "generic" / "background" / "2026-10-10_sunlit_sea_letterhead.docx"
)

# Positions extracted from the letterhead docx's header2.xml:
#   wordmark anchored with positionV = 691325 EMU = 0.756 in from page top,
#   width = 1810512 EMU = 1.98 in, height = 165383 EMU = 0.181 in.
# Image centre is therefore (0.5 * paperwidth, 0.756 + 0.0905) = ~0.847 in
# from the top of the page.
WORDMARK_WIDTH_IN = 1.98
WORDMARK_CENTER_FROM_TOP_IN = 0.847

# The wordmark bottom sits at ~1.03 in from the top of the page. 1.1 in gives a
# small gap before body text starts; 0.8 in bottom gives a few more lines than
# the standard 1 in and avoids orphaned signature lines on short letters. Side
# margins match the docx template (1 in).
PAGE_MARGINS = "top=1.1in,bottom=0.8in,left=1in,right=1in"

LATEX_LETTERHEAD = r"""
\usepackage{eso-pic}
\usepackage{graphicx}

% Full-page watermark behind every page.
\AddToShipoutPictureBG{%
  \AtPageCenter{%
    \makebox(0,0){\includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio]{__WATERMARK__}}%
  }%
}

% Wordmark on the first page only, centred horizontally at ~0.85 in from top.
% Guard with a boolean flag rather than \value{page} because pandoc's titling
% can reset the page counter mid-shipout; the flag is global and one-shot.
\newif\iffirstpageletterhead
\firstpageletterheadtrue
\AddToShipoutPictureFG*{%
  \iffirstpageletterhead
    \AtPageUpperLeft{%
      \put(\LenToUnit{0.5\paperwidth},\LenToUnit{-__WORDMARK_Y__ in}){%
        \makebox(0,0){\includegraphics[width=__WORDMARK_W__ in]{__WORDMARK__}}%
      }%
    }%
    \global\firstpageletterheadfalse
  \fi
}
"""


def extract_letterhead_assets(letterhead_docx: Path, out_dir: Path):
    """Extract wordmark + watermark PNGs from the letterhead docx into out_dir."""
    with zipfile.ZipFile(letterhead_docx) as zf:
        names = set(zf.namelist())
        if "word/media/image1.png" not in names or "word/media/image2.png" not in names:
            sys.exit(
                f"error: letterhead {letterhead_docx} does not contain the expected "
                "image1.png (wordmark) and image2.png (watermark)"
            )
        wordmark = out_dir / "wordmark.png"
        watermark = out_dir / "watermark.png"
        wordmark.write_bytes(zf.read("word/media/image1.png"))
        watermark.write_bytes(zf.read("word/media/image2.png"))
    return wordmark, watermark


def build_docx(input_md: Path, output_docx: Path, letterhead: Path):
    cmd = [
        "pandoc", str(input_md),
        "--reference-doc", str(letterhead),
        "-o", str(output_docx),
    ]
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)


def build_pdf(input_md: Path, output_pdf: Path, letterhead: Path):
    if shutil.which("xelatex") is None:
        sys.exit("error: xelatex not on PATH (install TeX Live; see README)")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        wordmark, watermark = extract_letterhead_assets(letterhead, tmp)
        header_tex = tmp / "letterhead.tex"
        header_tex.write_text(
            LATEX_LETTERHEAD
            .replace("__WATERMARK__", watermark.as_posix())
            .replace("__WORDMARK__", wordmark.as_posix())
            .replace("__WORDMARK_Y__", f"{WORDMARK_CENTER_FROM_TOP_IN}")
            .replace("__WORDMARK_W__", f"{WORDMARK_WIDTH_IN}"),
            encoding="utf-8",
        )
        cmd = [
            "pandoc", str(input_md),
            "-o", str(output_pdf),
            "--pdf-engine=xelatex",
            "-H", str(header_tex),
            "-V", f"geometry:paper=letterpaper,{PAGE_MARGINS}",
        ]
        print("+", " ".join(cmd))
        subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("input", type=Path, help="Input Markdown file")
    parser.add_argument(
        "-o", "--output", type=Path, default=None,
        help="Output path (default: sibling of input with .docx or .pdf extension)",
    )
    parser.add_argument(
        "--letterhead", type=Path, default=DEFAULT_LETTERHEAD,
        help=f"Reference letterhead .docx (default: {DEFAULT_LETTERHEAD.relative_to(REPO_ROOT)})",
    )
    parser.add_argument(
        "--pdf", action="store_true",
        help="Produce .pdf instead of .docx (uses xelatex + eso-pic to render the letterhead)",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        sys.exit(f"error: input not found: {args.input}")
    if not args.letterhead.is_file():
        sys.exit(f"error: letterhead not found: {args.letterhead}")
    if shutil.which("pandoc") is None:
        sys.exit("error: pandoc not on PATH (see README 'Document conversion')")

    ext = ".pdf" if args.pdf else ".docx"
    output = args.output or args.input.with_suffix(ext)
    output.parent.mkdir(parents=True, exist_ok=True)

    if args.pdf:
        build_pdf(args.input, output, args.letterhead)
    else:
        build_docx(args.input, output, args.letterhead)
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
