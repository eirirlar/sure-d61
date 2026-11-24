# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "python-docx>=1.1",
#   "docxcompose>=1.4",
#   "pyyaml>=6.0",
#   "lxml>=4.9",
# ]
# ///
"""
Build a SUREWAVE deliverable .docx from Markdown, starting from a copy of a
SUREWAVE deliverable that has already been accepted on the portal (default:
D7.4 version 2.0), instead of from the stock template.

The shell keeps the delivered document's cover page, styles, headers, footers,
page setup, Deliverable Review table and table-of-contents field. Everything
that belongs to the shell's own deliverable is removed or overwritten:

  - cover text boxes (deliverable number) and title cell;
  - Deliverable details table (WP, task, document name, lead, dissemination
    level, type, due date, delivery date);
  - version table (rows from meta.version_history, the rest blanked);
  - executive summary (replaced by the Markdown's front sections);
  - Deliverable Review table (reviewer names and comments cleared);
  - table of contents (cached entries removed; Word rebuilds it on open);
  - the whole body after the table of contents (replaced by the Markdown body).

Markdown layout expected: a title block, then front sections as `## <Heading>`
(e.g. Confidentiality notice, Executive summary), then numbered body sections
starting at `## 1. `. Front sections go before the Deliverable Review table in
the shell's executive-summary heading style; body headings are shifted one
level up (## -> Heading 1, ### -> Heading 2, #### -> Heading 3).

Usage:
    uv run scripts/md_to_surewave_docx_from_delivered.py <input.md> [--meta <meta.yaml>] [-o <out.docx>] [--shell <delivered.docx>]

Default meta: <input>.meta.yaml. Default output: <input>.docx.
Default shell: surewave/deliverables/2026-11-20_surewave_d7.4_economic_assessment_rev2.docx

Meta fields: deliverable_number, title, work_package, task, document_name,
lead_beneficiary, dissemination_level, deliverable_type, due_date,
delivery_date, version_history (list of [version, date, author, comments]).

Checks printed at the end: any text left from the shell's deliverable
(SHELL_MARKERS) is reported, so the output can be confirmed free of it.
"""

import argparse
import copy
import importlib.util
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from docx import Document
from docxcompose.composer import Composer
from lxml import etree

REPO = Path(__file__).resolve().parent.parent
DEFAULT_SHELL = REPO / "surewave/deliverables/2026-11-20_surewave_d7.4_economic_assessment_rev2.docx"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_NS}}}"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

# Text that would show that content from the shell deliverable survived.
SHELL_MARKERS = ("D7.4", "Economic Assessment", "Economic_Assessment", "LCOE", "Baltic Sea 10 MW",
                 "Mediterranean 10 MW Configuration", "Not applicable for this deliverable", "Balram")

PANDOC_TO_SHELL_STYLE = {"BodyText": "Normal0", "FirstParagraph": "Normal0", "Compact": "Normal0"}


def _load_helpers():
    spec = importlib.util.spec_from_file_location("mtsd", REPO / "scripts/md_to_surewave_docx.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def text_of(el) -> str:
    return "".join(t.text or "" for t in el.iter(f"{W}t"))


def set_text(container, new: str) -> None:
    """Put `new` in the first w:t of the first paragraph of `container` and blank the rest."""
    ts = list(container.iter(f"{W}t"))
    if not ts:
        p = container.find(f".//{W}p")
        r = etree.SubElement(p, f"{W}r")
        ts = [etree.SubElement(r, f"{W}t")]
    ts[0].text = new
    ts[0].set(XML_SPACE, "preserve")
    for t in ts[1:]:
        t.text = ""


def split_md(md: str) -> tuple[list[tuple[str, str]], str]:
    """Return ([(heading, text)] front sections, body text from '## 1. ')."""
    m = re.search(r"^## 1\. ", md, flags=re.M)
    if not m:
        raise SystemExit("no '## 1. ' section found")
    front_md, body_md = md[:m.start()], md[m.start():]
    parts = re.split(r"^## (.+)$", front_md, flags=re.M)
    front = []
    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        text = re.sub(r"^\s*---\s*$", "", parts[i + 1], flags=re.M).strip()
        if heading.lower().startswith("exploitation pathways") or not text:
            continue  # title block subtitle
        front.append((heading, text))
    # the title block (# ..., ## subtitle, italic line, metadata line) is dropped: it is on the cover
    front = [(h, t) for h, t in front if not t.startswith("*Structural")]
    return front, body_md


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def size_pipe_tables(md: str) -> str:
    """Rewrite each pipe table's separator row so pandoc gives columns widths
    in proportion to their content, instead of equal widths.

    Pandoc derives relative column widths from the dash counts of the separator
    row. Widths are allocated in characters of an assumed text width
    (TEXT_CHARS): every column first gets its longest word plus padding, so no
    word is broken, and the remaining width is shared in proportion to each
    column's mean cell length beyond its longest word, so text-heavy columns get most of
    it. Alignment colons are kept. The Markdown source file is not changed.
    """
    TEXT_CHARS = 85
    lines = md.split("\n")
    sep_re = re.compile(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
    i = 0
    while i < len(lines):
        if i > 0 and lines[i - 1].lstrip().startswith("|") and sep_re.match(lines[i]):
            head = _cells(lines[i - 1])
            seps = _cells(lines[i])
            j = i + 1
            rows = []
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append(_cells(lines[j]))
                j += 1
            n = len(seps)
            mins, wants = [], []
            for k in range(n):
                col = [r[k] for r in [head] + rows if k < len(r)]
                # words can break at hyphens and slashes, so measure the parts
                longest_word = max((len(w) + 0.4 * sum(ch.isupper() for ch in w) for c in col for w in re.split(r"[\s/\-–]+", c) if w), default=3)  # capitals are wider
                mean_len = sum(len(c) for c in col) / max(len(col), 1)
                mins.append(min(longest_word, 12) + 5)
                wants.append(max(mean_len - longest_word, 0))
            # at least 40 % of the width goes to text-heavy columns, even when
            # the minimum widths alone would fill the page
            extra = max(TEXT_CHARS - sum(mins), 0.4 * TEXT_CHARS)
            wsum = sum(wants) or 1
            weights = [m + extra * w / wsum for m, w in zip(mins, wants)]
            total = sum(weights)
            new = []
            for k, s in enumerate(seps):
                dashes = "-" * max(3, round(100 * weights[k] / total))
                left = ":" if s.startswith(":") else ""
                right = ":" if s.endswith(":") else ""
                new.append(left + dashes + right)
            lines[i] = "|" + "|".join(new) + "|"
            i = j
        else:
            i += 1
    return "\n".join(lines)


def pandoc(md_text: str, out: Path, shell: Path, tmp: Path, shift: int) -> None:
    src = tmp / (out.stem + ".md")
    src.write_text(size_pipe_tables(md_text), encoding="utf-8")
    # --columns=20: every pipe table wider than 20 characters gets relative
    # column widths from its separator row (see size_pipe_tables).
    cmd = ["pandoc", str(src), "-o", str(out), "--reference-doc", str(shell), "--wrap=none",
           "--columns=20", f"--shift-heading-level-by={shift}"]
    subprocess.run(cmd, check=True)
    doc = Document(str(out))
    for ps in doc.element.body.iter(f"{W}pStyle"):
        v = ps.get(f"{W}val")
        if v in PANDOC_TO_SHELL_STYLE:
            ps.set(f"{W}val", PANDOC_TO_SHELL_STYLE[v])
    doc.save(str(out))


def add_table_borders(doc_path: Path) -> None:
    doc = Document(str(doc_path))
    for tbl in doc.element.body.iter(f"{W}tbl"):
        tblPr = tbl.find(f"{W}tblPr")
        for old in tblPr.findall(f"{W}tblBorders"):
            tblPr.remove(old)
        b = etree.SubElement(tblPr, f"{W}tblBorders")
        for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
            e = etree.SubElement(b, f"{W}{side}")
            e.set(f"{W}val", "single"); e.set(f"{W}sz", "4"); e.set(f"{W}space", "0"); e.set(f"{W}color", "BFBFBF")
        # cell text left-aligned: the shell's body style is justified, which
        # opens wide gaps between words in narrow columns
        for p in tbl.iter(f"{W}p"):
            pPr = p.find(f"{W}pPr")
            if pPr is None:
                pPr = etree.Element(f"{W}pPr"); p.insert(0, pPr)
            for old in pPr.findall(f"{W}jc"):
                pPr.remove(old)
            jc = etree.SubElement(pPr, f"{W}jc"); jc.set(f"{W}val", "left")
        # header row: light shading (no bold, per the repo's typography rule)
        tr = tbl.find(f"{W}tr")
        if tr is not None:
            for tc in tr.findall(f"{W}tc"):
                tcPr = tc.find(f"{W}tcPr")
                if tcPr is None:
                    tcPr = etree.SubElement(tc, f"{W}tcPr"); tc.insert(0, tcPr)
                shd = etree.SubElement(tcPr, f"{W}shd")
                shd.set(f"{W}val", "clear"); shd.set(f"{W}color", "auto"); shd.set(f"{W}fill", "E7EEF7")
    doc.save(str(doc_path))


def page_break_paragraph():
    p = etree.Element(f"{W}p")
    r = etree.SubElement(p, f"{W}r")
    br = etree.SubElement(r, f"{W}br"); br.set(f"{W}type", "page")
    return p


def build_shell(shell: Path, meta: dict, front_headings: list[str], out: Path) -> dict:
    doc = Document(str(shell))
    body = doc.element.body
    els = list(body.iterchildren())

    def find_idx(pred, start=0):
        for i in range(start, len(els)):
            if pred(els[i]):
                return i
        raise SystemExit("shell structure not recognised")

    i_exec = find_idx(lambda e: e.tag == f"{W}p" and text_of(e).strip().lower() == "executive summary")
    i_review = find_idx(lambda e: e.tag == f"{W}p" and text_of(e).strip() == "Deliverable Review", i_exec)
    i_toc = find_idx(lambda e: e.tag == f"{W}sdt", i_review)

    # cover: deliverable number text boxes
    for tb in body.iter(f"{W}txbxContent"):
        if "Deliverable number:" in text_of(tb):
            set_text(tb, f"Deliverable number: {meta['deliverable_number']}")
    for p in els[:i_exec]:
        if p.tag == f"{W}p" and text_of(p).startswith("Deliverable number:"):
            # fallback text of the text-box (mc:Fallback) is covered by the loop above
            pass
    # cover tables
    labels = {"Work package:": "work_package", "Task:": "task", "Document name:": "document_name",
              "Lead beneficiary:": "lead_beneficiary", "Dissemination level:": "dissemination_level",
              "Deliverable type:": "deliverable_type", "Due date:": "due_date", "Delivery date:": "delivery_date"}
    shell_title = None
    for tbl in [e for e in els[:i_exec] if e.tag == f"{W}tbl"]:
        rows = tbl.findall(f"{W}tr")
        for tr in rows:
            tcs = tr.findall(f"{W}tc")
            if len(tcs) == 2 and text_of(tcs[0]).strip() in labels:
                set_text(tcs[1], str(meta.get(labels[text_of(tcs[0]).strip()], "") or ""))
        texts = [text_of(tr).strip() for tr in rows]
        if any(t.startswith("SUREWAVE") for t in texts) and any(t.startswith("Disclaimer") for t in texts):
            i_proj = next(i for i, t in enumerate(texts) if t.startswith("SUREWAVE"))
            shell_title = texts[i_proj + 1]
            set_text(rows[i_proj + 1], meta["title"])
        if texts and texts[0].lower().replace(" ", "").startswith("versiondate"):
            hist = meta.get("version_history") or []
            for k, tr in enumerate(rows[1:]):
                vals = hist[k] if k < len(hist) else []
                for j, tc in enumerate(tr.findall(f"{W}tc")):
                    set_text(tc, str(vals[j]) if j < len(vals) else "")
    # executive summary: drop the shell's text, keep its heading paragraph as the style source
    heading_proto = els[i_exec]
    for e in els[i_exec + 1:i_review]:
        body.remove(e)
    # front headings: first reuses the shell heading, the others are copies
    heads = []
    for n, h in enumerate(front_headings):
        hp = heading_proto if n == 0 else copy.deepcopy(heading_proto)
        set_text(hp, h)
        heads.append(hp)
    anchor = heading_proto
    for hp in heads[1:]:
        anchor.addnext(hp)
        anchor = hp
    pb = page_break_paragraph()
    anchor.addnext(pb)
    # review table: clear reviewer names and comments, keep the questions and tick boxes
    review = els[i_review + 1]
    rows = review.findall(f"{W}tr")
    for tc in rows[0].findall(f"{W}tc"):
        t = text_of(tc)
        if t.startswith("Reviewer #"):
            set_text(tc, t.split(":")[0] + ":")
    for tr in rows[2:]:
        tcs = tr.findall(f"{W}tc")
        for j in (2, 5):
            if j < len(tcs):
                set_text(tcs[j], "")
    # table of contents: keep field code, drop cached entries
    sdt = els[i_toc]
    content = sdt.find(f"{W}sdtContent")
    ps = content.findall(f"{W}p")
    first, last = ps[0], ps[-1]
    for p in ps[1:-1]:
        content.remove(p)
    # first paragraph: keep runs up to and including 'separate'; then a hint; last paragraph: only the end run
    keep, seen_sep = [], False
    for r in list(first.findall(f"{W}r")):
        if seen_sep:
            first.remove(r); continue
        fc = r.find(f"{W}fldChar")
        if fc is not None and fc.get(f"{W}fldCharType") == "separate":
            seen_sep = True
    for h in first.findall(f"{W}hyperlink"):
        first.remove(h)
    hint = etree.SubElement(first, f"{W}r")
    ht = etree.SubElement(hint, f"{W}t"); ht.text = "Update the table of contents (right-click, Update Field)."
    for child in list(last):
        if child.tag in (f"{W}r", f"{W}hyperlink"):
            fc = child.find(f".//{W}fldChar")
            if not (fc is not None and fc.get(f"{W}fldCharType") == "end"):
                last.remove(child)
    # body after the TOC
    sect = body.find(f"{W}sectPr")
    for e in els[i_toc + 1:]:
        if e is not sect and e.getparent() is body:
            body.remove(e)
    body.insert(list(body).index(sect), page_break_paragraph())
    doc.save(str(out))
    # index positions of the front headings for inserting content after each
    d2 = Document(str(out))
    kids = list(d2.element.body.iterchildren())
    pos = [next(i for i, e in enumerate(kids) if e.tag == f"{W}p" and text_of(e).strip() == h) for h in front_headings]
    return {"positions": pos, "shell_title": shell_title}


def clean_package(path: Path, author: str) -> list[str]:
    """Remove what the shell leaves in the package outside the body: image
    relationships no longer referenced by document.xml (the shell's figures) and
    their media files, the shell's comment authors (people.xml), and the shell's
    document properties (creator, last modified by, dates, revision)."""
    import datetime
    import io
    import zipfile
    with zipfile.ZipFile(path) as z:
        parts = {n: z.read(n) for n in z.namelist()}
    removed = []
    doc_xml = parts["word/document.xml"].decode("utf-8")
    used = set(re.findall(r'r:(?:embed|id|link)="(rId\d+)"', doc_xml))
    rels_name = "word/_rels/document.xml.rels"
    rels = etree.fromstring(parts[rels_name])
    for rel in list(rels):
        if rel.get("Type", "").endswith("/image") and rel.get("Id") not in used:
            rels.remove(rel)
    parts[rels_name] = etree.tostring(rels, xml_declaration=True, encoding="UTF-8", standalone=True)
    referenced = set()
    for n, data in parts.items():
        if n.endswith(".rels"):
            referenced |= {"word/" + t for t in re.findall(r'Target="(media/[^"]+)"', data.decode("utf-8"))}
    for n in [n for n in parts if n.startswith("word/media/") and n not in referenced]:
        del parts[n]
        removed.append(n)
    if "word/people.xml" in parts:
        root = etree.fromstring(parts["word/people.xml"])
        for child in list(root):
            root.remove(child)
        parts["word/people.xml"] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    core = parts["docProps/core.xml"].decode("utf-8")
    core = re.sub(r"<dc:creator>.*?</dc:creator>", f"<dc:creator>{author}</dc:creator>", core)
    core = re.sub(r"<cp:lastModifiedBy>.*?</cp:lastModifiedBy>", f"<cp:lastModifiedBy>{author}</cp:lastModifiedBy>", core)
    core = re.sub(r"<cp:revision>.*?</cp:revision>", "<cp:revision>1</cp:revision>", core)
    core = re.sub(r'(<dcterms:(?:created|modified)[^>]*>).*?(</dcterms:)', rf"\g<1>{now}\g<2>", core)
    parts["docProps/core.xml"] = core.encode("utf-8")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for n, data in parts.items():
            z.writestr(n, data)
    path.write_bytes(buf.getvalue())
    return removed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", type=Path)
    ap.add_argument("--meta", type=Path)
    ap.add_argument("-o", "--output", type=Path)
    ap.add_argument("--shell", type=Path, default=DEFAULT_SHELL)
    a = ap.parse_args()
    meta_path = a.meta or a.input.with_suffix(".meta.yaml")
    meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
    out = a.output or a.input.with_suffix(".docx")
    md = a.input.read_text(encoding="utf-8")
    md = re.sub(r"^---\n.*?\n---\n", "", md, count=1, flags=re.S) if md.startswith("---\n") else md
    front, body_md = split_md(md)
    helpers = _load_helpers()

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        shell_out = tmp / "shell.docx"
        info = build_shell(a.shell, meta, [h for h, _ in front], shell_out)
        front_docs = []
        for n, (h, t) in enumerate(front):
            fd = tmp / f"front{n}.docx"
            pandoc(t, fd, a.shell, tmp, 0)
            add_table_borders(fd)
            front_docs.append(fd)
        body_docx = tmp / "body.docx"
        pandoc(body_md, body_docx, a.shell, tmp, -1)
        add_table_borders(body_docx)

        comp = Composer(Document(str(shell_out)))
        comp.append(Document(str(body_docx)))
        for pos, fd in sorted(zip(info["positions"], front_docs), key=lambda x: -x[0]):
            comp.insert(pos + 1, Document(str(fd)))
        comp.save(str(out))

    helpers.inject_update_fields(out)
    removed = clean_package(out, meta.get("author", "Eirik Larsen"))
    print("shell media removed:", removed or "none")

    # leftover check
    d = Document(str(out))
    norm = lambda x: re.sub(r"[\W_]+", "", x).lower()
    md_norm = norm(md)
    markers = SHELL_MARKERS + ((info["shell_title"],) if info["shell_title"] else ())
    found = []
    for p in d.element.body.iter(f"{W}p"):
        t = text_of(p)
        if any(m in t for m in markers) and norm(t)[:60] not in md_norm:
            found.append(t[:80])
    print(f"shell: {a.shell.name}; cover title replaced: {info['shell_title']!r} -> {meta['title']!r}")
    print("shell text left:", found or "none")
    print(f"wrote {out} ({out.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
