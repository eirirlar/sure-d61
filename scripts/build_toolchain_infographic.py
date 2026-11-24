"""Rebuild the SUREWAVE modelling-toolchain infographic PDF (T159) in one step.

Usage (from the repo root or anywhere):
    python scripts/build_toolchain_infographic.py

Steps:
1. scripts/toolchain_figure.py regenerates the diagram
   (surewave/deliverables/2026-11-22_surewave_modelling_toolchain_figure.svg and .tikz.tex).
2. pandoc + xelatex renders the page source
   surewave/deliverables/2026-11-22_surewave_modelling_toolchain_infographic.md with
   scripts/infographic_pandoc_header.tex into
   surewave/deliverables/2026-11-22_surewave_modelling_toolchain_infographic.pdf.
3. If pdfinfo (poppler) is on PATH, checks that the PDF is exactly one page.

Requirements: Python 3 (standard library only), pandoc, TeX Live with xelatex
and TeX Gyre Heros. No desktop applications. The script only writes the three
generated files listed above.
"""
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DELIV = ROOT / "surewave" / "deliverables"
STEM = "2026-11-22_surewave_modelling_toolchain"
SRC = f"{STEM}_infographic.md"
PDF = f"{STEM}_infographic.pdf"


def run(cmd):
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=DELIV, check=True)


def main():
    for tool in ("pandoc", "xelatex"):
        if not shutil.which(tool):
            sys.exit(f"error: {tool} not found on PATH")
    run([sys.executable, str(ROOT / "scripts" / "toolchain_figure.py"), f"{STEM}_figure"])
    run(["pandoc", SRC, "-o", PDF, "--pdf-engine=xelatex",
         f"--include-in-header={ROOT / 'scripts' / 'infographic_pandoc_header.tex'}",
         "--resource-path=."])
    if shutil.which("pdfinfo"):
        info = subprocess.run(["pdfinfo", PDF], cwd=DELIV, capture_output=True, text=True).stdout
        pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
        if pages != 1:
            sys.exit(f"error: {PDF} has {pages} pages, expected 1 — shorten the page source")
        print(f"ok: {DELIV / PDF} (1 page)")
    else:
        print(f"wrote {DELIV / PDF} (pdfinfo not found, page count not checked)")


if __name__ == "__main__":
    main()
