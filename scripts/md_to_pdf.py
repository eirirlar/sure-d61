"""Dispatch a Markdown file to the correct Sunlit Sea PDF wrapper.

Reads ``sunlit_template:`` from the Markdown YAML frontmatter and runs
one of:

    slides → scripts/md_to_slides.py
    report → scripts/md_to_sunlit_report.py
    letter → scripts/md_to_letter.py --pdf

If the YAML field is missing, infers the template from the markdown
shape (slide-chrome blocks, numbered sections, signature block). If
inference is ambiguous, exits with a prompt to add the YAML field.

Usage::

    python scripts/md_to_pdf.py path/to/input.md
    python scripts/md_to_pdf.py path/to/input.md -o custom/out.pdf
    python scripts/md_to_pdf.py path/to/input.md --template report
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = {
    "slides": REPO_ROOT / "scripts" / "md_to_slides.py",
    "report": REPO_ROOT / "scripts" / "md_to_sunlit_report.py",
    "letter": REPO_ROOT / "scripts" / "md_to_letter.py",
}


def read_yaml_frontmatter(path: Path) -> dict[str, str]:
    """Return a dict of top-level YAML scalar fields from the frontmatter."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end]
    out: dict[str, str] = {}
    for line in block.splitlines():
        m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"\'')
    return out


def infer_template(path: Path) -> str | None:
    """Guess the template from markdown shape; return None if ambiguous."""
    body = path.read_text(encoding="utf-8")
    # slides: `## {.plain}` chrome blocks + a tikzpicture overlay is diagnostic.
    if "## {.plain}" in body and "tikzpicture" in body:
        return "slides"
    # report: three or more numbered `## N.` sections in the body.
    if len(re.findall(r"^## \d+\.", body, flags=re.MULTILINE)) >= 3:
        return "report"
    # letter: Norwegian signoff patterns.
    if re.search(r"\n(Med )?[Vv]ennlig hilsen\b", body) or re.search(r"\nMvh\b", body):
        return "letter"
    return None


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="input markdown file")
    p.add_argument("-o", "--output", type=Path, default=None,
                   help="output PDF path (default: sibling .pdf of input)")
    p.add_argument("--template", choices=sorted(SCRIPTS), default=None,
                   help="override template detection")
    args = p.parse_args()

    md = args.input.resolve()
    if not md.is_file():
        sys.exit(f"input not found: {md}")

    # Priority: CLI --template > YAML frontmatter > inference.
    template = args.template
    source = "--template"
    if not template:
        yaml = read_yaml_frontmatter(md)
        template = yaml.get("sunlit_template")
        source = "YAML frontmatter"
    if not template:
        template = infer_template(md)
        source = "shape inference"
    if not template:
        sys.exit(
            f"cannot determine template for {md.name}.\n"
            "Add `sunlit_template: slides|report|letter` to the YAML "
            "frontmatter, or pass --template on the CLI."
        )
    if template not in SCRIPTS:
        sys.exit(
            f"unknown template: {template!r}. "
            f"Valid: {sorted(SCRIPTS)}"
        )

    script = SCRIPTS[template]
    if not script.is_file():
        sys.exit(f"wrapper not found: {script}")

    cmd = [sys.executable, str(script)]
    if template == "letter":
        cmd.append("--pdf")  # letter wrapper defaults to .docx; force PDF
    cmd.append(str(md))
    if args.output:
        cmd += ["-o", str(args.output.resolve())]
    print(f"template={template} (via {source})")
    print(" ".join(cmd))
    subprocess.check_call(cmd)


if __name__ == "__main__":
    main()
