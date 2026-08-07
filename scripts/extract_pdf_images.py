# /// script
# requires-python = ">=3.10"
# dependencies = ["pypdf>=4", "Pillow"]
# ///
"""Extract embedded images from PDF files into a per-document folder.

Uses pypdf + Pillow to iterate each page's `.images` and save them under
`<output_dir>/<pdf_stem>/img-<page>-<idx>.<ext>`. Preserves original format
where possible (PNG for lossless, JPEG for lossy) via PIL's inferred format
from the `.image` attribute.

Usage:
    uv run scripts/extract_pdf_images.py <pdf_file> [<pdf_file> ...] --output-dir <dir>

Skips files with zero images. Prints a per-file summary of extracted images
with page and index. Safe by default — never overwrites existing images
without --force.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader


def extract(pdf_path: Path, output_root: Path, force: bool) -> int:
    """Extract images from one PDF. Returns count of images written."""
    reader = PdfReader(str(pdf_path))
    stem = pdf_path.stem
    out_dir = output_root / stem
    total = 0
    per_page: dict[int, int] = {}

    for page_idx, page in enumerate(reader.pages, start=1):
        for img_idx, img in enumerate(page.images):
            per_page[page_idx] = per_page.get(page_idx, 0) + 1
            ext = (Path(img.name).suffix or ".png").lstrip(".")
            # Normalize a few common odd extensions
            if ext.lower() in ("tif", "tiff"):
                ext = "png"
            filename = f"img-{page_idx:03d}-{img_idx:02d}.{ext.lower()}"
            out_path = out_dir / filename
            if out_path.exists() and not force:
                print(f"  skip existing: {out_path.relative_to(output_root)}")
                continue
            out_dir.mkdir(parents=True, exist_ok=True)
            try:
                out_path.write_bytes(img.data)
            except Exception as e:
                print(f"  ERROR writing {out_path.name}: {e}", file=sys.stderr)
                continue
            total += 1

    if total == 0 and not per_page:
        print(f"{pdf_path.name}: 0 embedded images")
    else:
        pages_str = ", ".join(f"p{p}={n}" for p, n in sorted(per_page.items()))
        print(f"{pdf_path.name}: {total} images extracted to {out_dir.relative_to(output_root.parent) if output_root.parent in out_dir.parents else out_dir}/  ({pages_str})")
    return total


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdfs", nargs="+", type=Path, help="PDF files to process")
    ap.add_argument("--output-dir", type=Path, required=True, help="Root output directory. Images go into <output-dir>/<pdf-stem>/")
    ap.add_argument("--force", action="store_true", help="Overwrite existing image files")
    args = ap.parse_args()

    grand_total = 0
    for pdf in args.pdfs:
        if not pdf.exists():
            print(f"skip missing: {pdf}", file=sys.stderr)
            continue
        grand_total += extract(pdf, args.output_dir, args.force)
    print(f"\nTotal images extracted: {grand_total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
