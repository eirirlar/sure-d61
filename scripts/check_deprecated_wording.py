"""
Report deprecated wording in current documents.

Reads the pattern table in docs/deprecated_wording.md (first column, a Python
regular expression in backticks, matched case-insensitively) and searches the
Markdown files under surewave/deliverables/ and docs/, skipping background/,
archive/, work folders (*_work/), delivered documents (D8.3, D7.4), lines
quoting a rule ("Do not use") and docs/deprecated_wording.md itself. In
surewave/deliverables/linkedin_posts.md the archive of published posts
(section 3) is skipped.

Usage:
    python scripts/check_deprecated_wording.py [path ...]

Exit code 1 if any hit is found, 0 otherwise. Standard library only. Reads
only Markdown files under the given paths (default: surewave/deliverables and
docs); writes nothing.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABLE = ROOT / "docs" / "deprecated_wording.md"
SKIP_PARTS = {"background", "archive"}
SKIP_NAMES = ("d8.3_technical_brochure", "d7.4")  # delivered documents keep their wording


def load_patterns() -> list[tuple[re.Pattern, str]]:
    pats = []
    for line in TABLE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*`(.+?)`\s*\|\s*(.*?)\s*\|", line)
        if m:
            pats.append((re.compile(m.group(1).replace("\\|", "|"), re.I), m.group(2)))
    return pats


def files(paths: list[Path]):
    for p in paths:
        for f in sorted(p.rglob("*.md")) if p.is_dir() else [p]:
            rel = f.relative_to(ROOT)
            if (f == TABLE or SKIP_PARTS & set(rel.parts) or any(x.endswith("_work") for x in rel.parts)
                    or any(s in f.name for s in SKIP_NAMES)):
                continue
            yield f


def main() -> int:
    paths = [ROOT / a for a in sys.argv[1:]] or [ROOT / "surewave" / "deliverables", ROOT / "docs"]
    pats = load_patterns()
    hits = 0
    for f in files(paths):
        text = f.read_text(encoding="utf-8", errors="replace")
        if f.name == "linkedin_posts.md":
            text = re.split(r"^## 3\. ", text, flags=re.M)[0]
        for n, line in enumerate(text.splitlines(), 1):
            if "Do not use" in line:  # a line quoting the rule itself
                continue
            for pat, repl in pats:
                m = pat.search(line)
                if m:
                    hits += 1
                    s = max(0, m.start() - 60)
                    print(f"{f.relative_to(ROOT)}:{n}: '{m.group(0)}' -> {repl}\n    ...{line[s:m.end() + 60]}...")
    print(f"{hits} hit(s)")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
