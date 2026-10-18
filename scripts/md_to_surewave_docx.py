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
Produce a SUREWAVE-branded .docx from a Markdown source:

  1. Open the SUREWAVE consortium template as the starting document (preserves
     the cover page body content, headers, footers, section properties).
  2. Replace placeholders on the cover (deliverable number, title, work package,
     task, document name, lead beneficiary, dissemination level, deliverable
     type, due date, delivery date) using metadata from YAML frontmatter in the
     .md or a sidecar <input>.meta.yaml.
  3. Convert the Markdown body (minus YAML frontmatter, if present) to docx via
     pandoc using --reference-doc on the same template, so pandoc's output
     styling matches the template.
  4. Append the body to the template using docxcompose, which handles image
     re-embedding and style merging correctly.
  5. Inject <w:updateFields w:val="true"/> into settings.xml so Word evaluates
     PAGE and NUMPAGES fields on open, giving dynamic page numbers.

Usage:
    uv run scripts/md_to_surewave_docx.py <input.md>
    uv run scripts/md_to_surewave_docx.py <input.md> -o <output.docx>
    uv run scripts/md_to_surewave_docx.py <input.md> --template <alt_template.docx>
    uv run scripts/md_to_surewave_docx.py <input.md> --meta <sidecar.yaml>

Default template: surewave/background/2026-10-16_surewave_docx_template.docx
Default output: <input>.docx next to the .md.
Default meta: YAML frontmatter in .md, falling back to <input>.meta.yaml sidecar.

Metadata fields (all optional; unknown keys are tolerated):
    deliverable_number    e.g. "D8.3"
    title                 e.g. "Technical Brochure"
    work_package          e.g. "WP8"
    task                  e.g. "8.3"
    document_name         full deliverable name
    lead_beneficiary      e.g. "Sunlit Sea AS"
    dissemination_level   PU | SEN | EU classified
    deliverable_type      R | DEM | DEC | OTHER
    due_date              e.g. "2026-09-30"
    delivery_date         e.g. "2026-09-28"
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import yaml
from docx import Document
from docxcompose.composer import Composer
from lxml import etree

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_NS}}}"

DEFAULT_TEMPLATE = Path("surewave/background/2026-10-16_surewave_docx_template.docx")


# -------------------- metadata loading --------------------

def read_md(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    meta: dict = {}
    body = text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if m:
        try:
            parsed = yaml.safe_load(m.group(1)) or {}
            if isinstance(parsed, dict):
                meta = parsed
                body = m.group(2)
        except yaml.YAMLError:
            pass
    return meta, body


def load_meta(md_path: Path, cli_meta: Path | None) -> dict:
    frontmatter, _ = read_md(md_path)
    sidecar: dict = {}
    sidecar_path = cli_meta or md_path.with_suffix(".meta.yaml")
    if sidecar_path.exists():
        sidecar = yaml.safe_load(sidecar_path.read_text(encoding="utf-8")) or {}
        if not isinstance(sidecar, dict):
            sidecar = {}
    merged = {**sidecar, **frontmatter}  # frontmatter wins on conflict
    return merged


# -------------------- placeholder substitution --------------------

PARAGRAPH_SUBS = [
    # Each (pattern, meta_key) rewrites the full paragraph text, preserving the
    # first run's formatting. Patterns are regexes anchored on the full joined
    # paragraph text.
    (re.compile(r"^Deliverable number:\s*D[\sX]*\.?[\sX]*$"), "deliverable_number",
     lambda v: f"Deliverable number: {v}"),
    (re.compile(r"^Title:\s*X+\s*$"), "title",
     lambda v: f"Title: {v}"),
    # Also handle paragraphs that are just the X placeholder on their own
    (re.compile(r"^X{4,}$"), "title", lambda v: v),
]

# Cell-level substitutions on the first (cover) table only. Looks for a label
# in column 0 (approximately), replaces the next-column text with the metadata
# value. Operates on tables[0] in the document.
CELL_LABEL_TO_KEY = {
    "WP": "work_package",
    "Task": "task",
    "Work package:": "work_package",
    "Task:": "task",
    "Document name:": "document_name",
    "Title": "title",
    "Lead beneficiary": "lead_beneficiary",
    "Lead beneficiary:": "lead_beneficiary",
    "Dissemination level": "dissemination_level",
    "Dissemination level:": "dissemination_level",
    "Deliverable type": "deliverable_type",
    "Deliverable type:": "deliverable_type",
    "Due date": "due_date",
    "Due date:": "due_date",
    "Due delivery date": "due_date",
    "Delivery date": "delivery_date",
    "Delivery date:": "delivery_date",
    "Actual delivery date": "delivery_date",
}

# Default placeholder values in template cells that should be scrubbed to empty
# unless overridden by meta. These are the "example" values Carvo-Thalia et al
# used when drafting the template.
TEMPLATE_DEFAULT_VALUES = {"SEN", "SINTEF", "28.11.2022", "DXX", "XX", "XXXXXXX", "R"}


def cell_text(cell) -> str:
    return "".join(p.text for p in cell.paragraphs).strip()


def set_cell_text(cell, new_text: str) -> None:
    # Replace all paragraphs in the cell with a single paragraph containing new_text,
    # preserving the first paragraph's style and formatting.
    if not cell.paragraphs:
        p = cell.add_paragraph(new_text)
        return
    first = cell.paragraphs[0]
    style = first.style
    # Remove extra paragraphs
    for extra in cell.paragraphs[1:]:
        extra._element.getparent().remove(extra._element)
    # Clear runs in the first paragraph, keep the first run's formatting if any
    runs = first.runs
    if runs:
        first_run = runs[0]
        first_run.text = new_text
        for r in runs[1:]:
            r._element.getparent().remove(r._element)
    else:
        first.add_run(new_text)
    first.style = style


def _cell_runs_text(tc) -> str:
    texts = tc.findall(f".//{W}t")
    return "".join((t.text or "") for t in texts).strip()


def _set_tc_text(tc, new_text: str) -> None:
    """Replace all text content of a tc element with new_text, keeping the first
    paragraph/run intact for style, zeroing subsequent runs."""
    paragraphs = tc.findall(f"{W}p")
    if not paragraphs:
        return
    # Operate on first paragraph only; blank out any additional paragraphs' text
    first_p = paragraphs[0]
    texts = first_p.findall(f".//{W}t")
    if texts:
        texts[0].text = new_text
        texts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        for t in texts[1:]:
            t.text = ""
    else:
        # Create a new text element inside a new run
        r = etree.SubElement(first_p, f"{W}r")
        t = etree.SubElement(r, f"{W}t")
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        t.text = new_text
    for extra_p in paragraphs[1:]:
        for t in extra_p.findall(f".//{W}t"):
            t.text = ""


# Standalone placeholder cells — the cell text IS the placeholder (not a label
# for the next cell). First occurrence per key wins; later cells with the same
# literal text (unlikely but possible) are left alone.
STANDALONE_CELL_PLACEHOLDERS: dict[str, str] = {
    "Title": "document_name",       # highlighted "Title" in WP/Task table 3rd col
    "XXXXXXX": "title",             # text-box fallback (also handled by fill_textboxes)
}


def fill_cover_table(doc, meta: dict) -> None:
    """Iterate every <w:tc> across every table in document order. Two kinds of
    substitutions:

      1. Label-value pairs: when cell[i]'s text matches CELL_LABEL_TO_KEY, set
         cell[i+1] to the meta value.
      2. Standalone placeholders: when a cell's text matches STANDALONE_CELL_PLACEHOLDERS,
         replace that cell's own text with the meta value.

    Each key is used at most once (first occurrence wins), so reference tables
    further down the document (e.g. Dissemination level definitions, Deliverable
    type definitions) that reuse the same labels are left alone."""
    used_keys: set[str] = set()
    for table in doc.tables:
        all_tcs = list(table._tbl.iter(f"{W}tc"))
        i = 0
        while i < len(all_tcs):
            text = _cell_runs_text(all_tcs[i])

            # Standalone placeholder in this cell?
            standalone_key = STANDALONE_CELL_PLACEHOLDERS.get(text)
            if standalone_key and standalone_key not in used_keys and standalone_key in meta and meta[standalone_key] is not None:
                _set_tc_text(all_tcs[i], str(meta[standalone_key]))
                used_keys.add(standalone_key)
                i += 1
                continue

            # Label-value pair with the next cell?
            if i + 1 < len(all_tcs):
                key = CELL_LABEL_TO_KEY.get(text)
                if key and key not in used_keys and key in meta and meta[key] is not None:
                    _set_tc_text(all_tcs[i + 1], str(meta[key]))
                    used_keys.add(key)
                    i += 2
                    continue

            i += 1


def fill_paragraph_placeholders(doc, meta: dict) -> None:
    for para in doc.paragraphs:
        text = para.text
        for pattern, key, builder in PARAGRAPH_SUBS:
            if key in meta and meta[key] is not None and pattern.match(text.strip()):
                new_text = builder(str(meta[key]))
                # Replace paragraph text preserving first run formatting
                runs = para.runs
                if runs:
                    runs[0].text = new_text
                    for r in runs[1:]:
                        r._element.getparent().remove(r._element)
                else:
                    para.add_run(new_text)
                break


def fill_textboxes(doc, meta: dict) -> None:
    """Replace placeholder text inside text-boxes (Deliverable number box, Title box).
    Text boxes use w:txbxContent and are embedded in w:drawing/mc:AlternateContent."""
    body_xml = doc.element.body
    nsmap = {"w": W_NS}
    txbx_contents = body_xml.findall(f".//{W}txbxContent")
    for tbx in txbx_contents:
        texts = tbx.findall(f".//{W}t")
        joined = "".join((t.text or "") for t in texts)
        new_joined = None

        # Deliverable number pattern: "Deliverable number: DX.X" (letters X split across runs)
        if "Deliverable number:" in joined and ("deliverable_number" in meta):
            new_joined = f"Deliverable number: {meta['deliverable_number']}"
        # Title pattern: "Title: XXXXXXX"
        elif joined.strip().startswith("Title:") and "title" in meta:
            new_joined = f"Title: {meta['title']}"

        if new_joined is not None:
            if texts:
                texts[0].text = new_joined
                for t in texts[1:]:
                    t.text = ""
                # Make sure the first run preserves spaces
                texts[0].set(f"{{{'http://www.w3.org/XML/1998/namespace'}}}space", "preserve")


# -------------------- strip reference/QA tables after cover --------------------

CUT_MARKERS = (
    # First occurrence of any of these text snippets in a body element triggers
    # deletion of that element and everything after it (up to sectPr). All are
    # taken from the trailing "reference and QA" block in the stock SUREWAVE
    # template; chosen so none of them collide with the earlier cover content.
    "Public- fullly open",     # Dissemination level definitions table
    "SEN = Sensitive",          # Dissemination level definitions table alt
    "Reviewer #1",              # QA review table header
    "EXECUTIVE SUMMARY",        # placeholder heading
    "Deliverable Review",       # placeholder heading
    "No table of contents entries found",   # pandoc-style TOC placeholder
    "* Type of comments:",      # footnote under QA table
)


def _element_text(el) -> str:
    return "".join((t.text or "") for t in el.iter(f"{W}t"))


def strip_reference_tail(doc) -> int:
    """Remove reference-definition tables, QA review table, and placeholder
    headings that follow the cover + deliverable-details tables in the stock
    SUREWAVE template. Returns number of elements removed."""
    body = doc.element.body
    children = list(body)
    cut_idx = None
    for i, el in enumerate(children):
        if el.tag == f"{W}sectPr":
            break
        text = _element_text(el)
        if any(marker in text for marker in CUT_MARKERS):
            cut_idx = i
            break
    if cut_idx is None:
        return 0
    removed = 0
    for el in children[cut_idx:]:
        if el.tag == f"{W}sectPr":
            break
        body.remove(el)
        removed += 1
    return removed


# -------------------- settings.xml updateFields fix --------------------

def replace_shape_page_number_with_inline(docx_path: Path) -> int:
    """Remove any anchored <w:drawing> in word/footer*.xml that contains a PAGE
    field (the template's blue box) and append a right-aligned paragraph with
    an inline PAGE field styled with white text + blue character shading.

    Word 365 does not reliably update fields inside anchored shapes, so the
    "pretty blue box" page number in the template renders as a stale "1" on
    every page. Replacing it with an inline field makes Word evaluate it on
    open. Visual approximation of the original (blue background + white text
    at bottom right), not an exact pixel match.

    Returns the number of footer files modified."""
    import io

    with zipfile.ZipFile(docx_path, "r") as zin:
        contents = {name: zin.read(name) for name in zin.namelist()}

    SUREWAVE_BLUE = "1D76BB"
    modified_count = 0
    footer_names = [n for n in contents if n.startswith("word/footer") and n.endswith(".xml")]

    for name in footer_names:
        tree = etree.fromstring(contents[name])
        # Find drawings whose text content includes a PAGE instrText
        drawings_to_remove = []
        for drawing in tree.iter(f"{W}drawing"):
            instr_texts = [el.text or "" for el in drawing.iter(f"{W}instrText")]
            if any("PAGE" in t for t in instr_texts):
                drawings_to_remove.append(drawing)
        if not drawings_to_remove:
            continue

        # Remove each drawing (and the enclosing w:r / mc:AlternateContent wrapper that holds it)
        for d in drawings_to_remove:
            # Walk up to a removable ancestor: w:r is the right level because the drawing is
            # embedded via <w:r><mc:AlternateContent>...<w:drawing/>...</mc:AlternateContent></w:r>.
            ancestor = d
            while ancestor is not None and ancestor.tag != f"{W}r":
                ancestor = ancestor.getparent()
            if ancestor is not None and ancestor.getparent() is not None:
                ancestor.getparent().remove(ancestor)

        # Build and append a right-aligned paragraph with inline PAGE field.
        # Styling strategy: single-row single-cell table at the right side of the
        # footer, cell shaded SUREWAVE blue, cell text white + bold. A table cell
        # is the one place in OOXML where Word 365 reliably honours fill + text
        # colour (character-level <w:shd> inside <w:rPr> is ignored by Word in
        # some setups, and paragraph-level <w:shd> extends across the entire line).
        # Full-width 2-column table: wide empty spacer on the left, narrow blue
        # cell on the right with the PAGE field. Using full-width instead of a
        # right-aligned narrow table because Word 365 ignores <w:jc> in <w:tblPr>
        # for footer tables (LibreOffice does respect it).
        SPACER_W = 8640  # twips: pushes the box to the right side of a Letter-page footer
        BOX_W = 720
        BOX_H = 360
        tbl = etree.SubElement(tree, f"{W}tbl")
        tblPr = etree.SubElement(tbl, f"{W}tblPr")
        tblW = etree.SubElement(tblPr, f"{W}tblW")
        tblW.set(f"{W}w", str(SPACER_W + BOX_W))
        tblW.set(f"{W}type", "dxa")
        tblLayout = etree.SubElement(tblPr, f"{W}tblLayout")
        tblLayout.set(f"{W}type", "fixed")
        tblGrid = etree.SubElement(tbl, f"{W}tblGrid")
        for w in (SPACER_W, BOX_W):
            gc = etree.SubElement(tblGrid, f"{W}gridCol")
            gc.set(f"{W}w", str(w))
        tr = etree.SubElement(tbl, f"{W}tr")
        trPr = etree.SubElement(tr, f"{W}trPr")
        trHeight = etree.SubElement(trPr, f"{W}trHeight")
        trHeight.set(f"{W}val", str(BOX_H))
        trHeight.set(f"{W}hRule", "exact")

        # Left spacer cell — transparent, empty
        spacer_tc = etree.SubElement(tr, f"{W}tc")
        spacer_tcPr = etree.SubElement(spacer_tc, f"{W}tcPr")
        spacer_tcW = etree.SubElement(spacer_tcPr, f"{W}tcW")
        spacer_tcW.set(f"{W}w", str(SPACER_W))
        spacer_tcW.set(f"{W}type", "dxa")
        # Zero padding on all sides, else the row grows
        spacer_tcMar = etree.SubElement(spacer_tcPr, f"{W}tcMar")
        for edge in ("top", "left", "bottom", "right"):
            m = etree.SubElement(spacer_tcMar, f"{W}{edge}")
            m.set(f"{W}w", "0")
            m.set(f"{W}type", "dxa")
        etree.SubElement(spacer_tc, f"{W}p")

        # Right page-number cell — SUREWAVE blue fill, white bold PAGE field, centred.
        # OOXML CT_TcPrInner schema requires children in order:
        #   tcW → tcBorders → shd → noWrap → tcMar → textDirection → tcFitText → vAlign → hideMark
        # Word 365 silently ignores <w:shd> if placed after <w:tcMar>, which is why the
        # earlier version showed white background in Word (LibreOffice is more forgiving).
        tc = etree.SubElement(tr, f"{W}tc")
        tcPr = etree.SubElement(tc, f"{W}tcPr")
        tcW = etree.SubElement(tcPr, f"{W}tcW")
        tcW.set(f"{W}w", str(BOX_W))
        tcW.set(f"{W}type", "dxa")
        tcShd = etree.SubElement(tcPr, f"{W}shd")
        tcShd.set(f"{W}val", "clear")
        tcShd.set(f"{W}color", "auto")
        tcShd.set(f"{W}fill", SUREWAVE_BLUE)
        tcMar = etree.SubElement(tcPr, f"{W}tcMar")
        for edge, w in (("top", "20"), ("left", "0"), ("bottom", "20"), ("right", "0")):
            m = etree.SubElement(tcMar, f"{W}{edge}")
            m.set(f"{W}w", w)
            m.set(f"{W}type", "dxa")
        tcVAlign = etree.SubElement(tcPr, f"{W}vAlign")
        tcVAlign.set(f"{W}val", "center")
        cell_p = etree.SubElement(tc, f"{W}p")
        cell_pPr = etree.SubElement(cell_p, f"{W}pPr")
        cell_jc = etree.SubElement(cell_pPr, f"{W}jc")
        cell_jc.set(f"{W}val", "center")
        cell_r = etree.SubElement(cell_p, f"{W}r")
        cell_rPr = etree.SubElement(cell_r, f"{W}rPr")
        etree.SubElement(cell_rPr, f"{W}b")
        color = etree.SubElement(cell_rPr, f"{W}color")
        color.set(f"{W}val", "FFFFFF")
        sz = etree.SubElement(cell_rPr, f"{W}sz")
        sz.set(f"{W}val", "22")
        begin = etree.SubElement(cell_r, f"{W}fldChar")
        begin.set(f"{W}fldCharType", "begin")
        begin.set(f"{W}dirty", "true")
        instr = etree.SubElement(cell_r, f"{W}instrText")
        instr.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        instr.text = " PAGE   \\* MERGEFORMAT "
        sep = etree.SubElement(cell_r, f"{W}fldChar")
        sep.set(f"{W}fldCharType", "separate")
        t = etree.SubElement(cell_r, f"{W}t")
        t.text = "1"
        end = etree.SubElement(cell_r, f"{W}fldChar")
        end.set(f"{W}fldCharType", "end")

        # OOXML requires any <w:tbl> to be followed by a <w:p> as final body element
        etree.SubElement(tree, f"{W}p")

        contents[name] = etree.tostring(tree, xml_declaration=True, encoding="UTF-8", standalone=True)
        modified_count += 1

    if modified_count:
        print(f"replaced shape page number with inline PAGE field in {modified_count} footer(s)")

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in contents.items():
            zout.writestr(name, data)
    docx_path.write_bytes(buf.getvalue())
    return modified_count


def inject_update_fields(docx_path: Path) -> None:
    """Add <w:updateFields w:val="true"/> to word/settings.xml so Word evaluates
    PAGE/NUMPAGES fields on open. Modifies docx in-place by rewriting the zip.

    Also marks every <w:fldChar w:fldCharType="begin"> in headers and footers
    with w:dirty="true" — this is the more forceful mechanism, honoured by Word
    even for fields inside anchored shapes/text boxes (e.g. the SUREWAVE template
    puts its PAGE field inside a floating blue box, where plain updateFields
    does not reach)."""
    import io

    with zipfile.ZipFile(docx_path, "r") as zin:
        contents = {name: zin.read(name) for name in zin.namelist()}

    # settings.xml: add updateFields
    settings_name = "word/settings.xml"
    if settings_name in contents:
        tree = etree.fromstring(contents[settings_name])
        if tree.find(f"{W}updateFields") is None:
            new = etree.SubElement(tree, f"{W}updateFields")
            new.set(f"{W}val", "true")
        contents[settings_name] = etree.tostring(tree, xml_declaration=True, encoding="UTF-8", standalone=True)

    # headers + footers: mark field-begin markers as dirty
    dirty_targets = [
        n for n in contents.keys()
        if n.startswith("word/footer") and n.endswith(".xml")
        or n.startswith("word/header") and n.endswith(".xml")
    ]
    dirty_count = 0
    for name in dirty_targets:
        tree = etree.fromstring(contents[name])
        for fldChar in tree.iter(f"{W}fldChar"):
            if fldChar.get(f"{W}fldCharType") == "begin":
                fldChar.set(f"{W}dirty", "true")
                dirty_count += 1
        contents[name] = etree.tostring(tree, xml_declaration=True, encoding="UTF-8", standalone=True)
    if dirty_count:
        print(f"marked {dirty_count} header/footer field(s) dirty for re-evaluation")

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in contents.items():
            zout.writestr(name, data)
    docx_path.write_bytes(buf.getvalue())


# -------------------- main --------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", type=Path, help="Markdown input .md")
    ap.add_argument("-o", "--output", type=Path, help="Output .docx (default: next to input)")
    ap.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE,
                    help=f"SUREWAVE docx template (default: {DEFAULT_TEMPLATE})")
    ap.add_argument("--meta", type=Path, help="Sidecar YAML with metadata (default: <input>.meta.yaml)")
    args = ap.parse_args()

    md_path: Path = args.input
    if not md_path.exists():
        print(f"error: input not found: {md_path}", file=sys.stderr)
        return 2
    template_path: Path = args.template
    if not template_path.exists():
        print(f"error: template not found: {template_path}", file=sys.stderr)
        return 2
    output_path: Path = args.output or md_path.with_suffix(".docx")

    meta = load_meta(md_path, args.meta)
    print(f"metadata: {len(meta)} fields loaded")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        body_md = tmp / "body.md"
        _, body_text = read_md(md_path)
        body_md.write_text(body_text, encoding="utf-8")

        body_docx = tmp / "body.docx"
        cmd = [
            "pandoc", str(body_md),
            "-o", str(body_docx),
            "--reference-doc", str(template_path),
            "--resource-path", str(md_path.parent.resolve()),
            "--wrap=none",
        ]
        print(f"pandoc: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)

        # Open the template fresh for each run (so repeated runs don't accumulate changes)
        tmp_template = tmp / "template.docx"
        shutil.copyfile(template_path, tmp_template)
        template_doc = Document(str(tmp_template))

        fill_paragraph_placeholders(template_doc, meta)
        fill_cover_table(template_doc, meta)
        fill_textboxes(template_doc, meta)
        removed = strip_reference_tail(template_doc)
        print(f"stripped {removed} reference/placeholder elements from template tail")

        tmp_filled = tmp / "template_filled.docx"
        template_doc.save(str(tmp_filled))

        # Append body to filled template
        composer = Composer(Document(str(tmp_filled)))
        body_doc = Document(str(body_docx))
        composer.append(body_doc)
        composer.save(str(output_path))

    replace_shape_page_number_with_inline(output_path)
    inject_update_fields(output_path)

    print(f"wrote {output_path} ({output_path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
