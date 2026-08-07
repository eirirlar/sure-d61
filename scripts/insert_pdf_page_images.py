# /// script
# requires-python = ">=3.10"
# ///
"""Insert markdown image references per PDF page into an .md file.

Expects the .md file to be a pdftotext-derived conversion where each PDF page
is separated by the form-feed character `\f`. For each page, inserts image
references for all matching image files in `<images_dir>/<stem>/`, named
`img-<page:03d>-*.*` (as produced by `extract_pdf_images.py`).

Image references are inserted at the end of each page's text, so that readers
see the original text first, then the visuals.

Safe by default — writes to `<name>.imgref.md` sibling. Use `--promote` to
overwrite in place after verifying.

Assumption: the .md file has an optional header block (title + metadata)
prepended before the first `\f`, which is treated as part of PDF page 1's
chunk. Trailing empty chunk (from trailing `\f` in pdftotext output) is
preserved but no images are added.

Usage:
    python scripts/insert_pdf_page_images.py <mdfile> --images-dir <dir> [--promote]

Example:
    python scripts/insert_pdf_page_images.py \\
      sure/background/2025-03-12_uv_minipatch_preliminary_results.md \\
      --images-dir sure/background/images/ --promote
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def find_page_images(images_dir: Path, pdf_page: int) -> list[str]:
    """Return sorted list of image filenames for a given PDF page."""
    pattern = re.compile(rf"^img-{pdf_page:03d}-\d+\.\w+$", re.IGNORECASE)
    if not images_dir.is_dir():
        return []
    return sorted(
        f.name for f in images_dir.iterdir()
        if f.is_file() and pattern.match(f.name)
    )


def build_image_block(images: list[str], relative_dir: str) -> str:
    """Build a markdown block of image references."""
    if not images:
        return ""
    lines = [""]  # blank line before
    for img in images:
        lines.append(f"![]({relative_dir}/{img})")
        lines.append("")  # blank line after each for pandoc-friendly rendering
    return "\n".join(lines)


def process(md_path: Path, images_root: Path, promote: bool) -> bool:
    stem = md_path.stem
    images_dir = images_root / stem
    if not images_dir.is_dir():
        print(f"skip: no image directory {images_dir}")
        return False

    content = md_path.read_bytes().decode("utf-8", errors="replace")
    chunks = content.split("\f")

    # Chunks 0..N-2 correspond to PDF pages 1..N-1 (chunk 0 includes any
    # prepended header). Trailing empty chunk (last) preserved without images.
    num_pages = len(chunks) - 1 if chunks and not chunks[-1].strip() else len(chunks)

    relative_dir = f"images/{stem}"
    inserted_pages = []
    for i in range(num_pages):
        pdf_page = i + 1
        images = find_page_images(images_dir, pdf_page)
        if not images:
            continue
        block = build_image_block(images, relative_dir)
        # Ensure the chunk ends with a newline before appending
        if not chunks[i].endswith("\n"):
            chunks[i] += "\n"
        chunks[i] += block + "\n"
        inserted_pages.append((pdf_page, len(images)))

    new_content = "\f".join(chunks)

    if promote:
        out_path = md_path
        note = "overwritten in place"
    else:
        out_path = md_path.with_name(md_path.stem + ".imgref" + md_path.suffix)
        note = f"wrote {out_path.name} (dry-run)"

    out_path.write_bytes(new_content.encode("utf-8"))

    total_imgs = sum(n for _, n in inserted_pages)
    print(f"{md_path.name}: {total_imgs} image refs on {len(inserted_pages)} pages -> {note}")
    for page, count in inserted_pages:
        print(f"  page {page:2d}: {count} images")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mdfiles", nargs="+", type=Path)
    ap.add_argument("--images-dir", type=Path, required=True, help="Root images dir (contains per-stem subfolders)")
    ap.add_argument("--promote", action="store_true", help="Overwrite in place instead of writing .imgref sibling")
    args = ap.parse_args()
    ok = True
    for md in args.mdfiles:
        if not md.exists():
            print(f"skip missing: {md}", file=sys.stderr)
            ok = False
            continue
        if not process(md, args.images_dir, args.promote):
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
