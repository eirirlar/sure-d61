# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10"]
# ///
"""
Render every page of a PDF to a small image and combine the pages into contact
sheets, for a fast page-by-page visual check of a rendered deliverable (tables,
column widths, page breaks, empty pages).

Usage:
    uv run scripts/pdf_contact_sheets.py <input.pdf> [-o <out_dir>] [--per 8] [--dpi 45]

Output: <out_dir>/sheet_NN.png, each holding --per pages (default 8, in two
rows). Default out_dir: temp/<pdf stem>_sheets/. Needs `pdftoppm` (poppler) on
PATH. Typical chain for a SUREWAVE docx:

    OUTDIR="$(pwd)/temp/render" bash scripts/render_docx_pdf.sh <file.docx>
    uv run scripts/pdf_contact_sheets.py temp/render/<file>.pdf

Reads only the given PDF; writes only into out_dir.
"""
import argparse
import glob
import os
import subprocess
import sys
import tempfile

from PIL import Image


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("-o", "--out")
    ap.add_argument("--per", type=int, default=8)
    ap.add_argument("--dpi", type=int, default=45)
    a = ap.parse_args()
    stem = os.path.splitext(os.path.basename(a.pdf))[0]
    out = a.out or os.path.join("temp", f"{stem}_sheets")
    os.makedirs(out, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=out) as td:
        subprocess.run(["pdftoppm", "-r", str(a.dpi), "-png", a.pdf, os.path.join(td, "p")], check=True)
        files = sorted(glob.glob(os.path.join(td, "p-*.png")))
        cols = a.per // 2 if a.per > 3 else a.per
        for k in range(0, len(files), a.per):
            imgs = [Image.open(f) for f in files[k:k + a.per]]
            w, h = imgs[0].size
            rows = (len(imgs) + cols - 1) // cols
            sheet = Image.new("RGB", (cols * w, rows * h), "white")
            for i, im in enumerate(imgs):
                sheet.paste(im, ((i % cols) * w, (i // cols) * h))
                im.close()
            sheet.save(os.path.join(out, f"sheet_{k // a.per + 1:02d}.png"))
    print(f"{len(files)} pages -> {(len(files) + a.per - 1) // a.per} sheets in {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
