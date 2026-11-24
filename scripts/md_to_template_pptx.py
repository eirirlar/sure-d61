"""Build a .pptx from a Markdown slide source by filling a copy of a reference deck.

Usage:
    python scripts/md_to_template_pptx.py <deck.md> [--template <reference.pptx>] [--date TEXT] [--pdf] [-o <out.pptx>]

The template and footer date can be set in the deck's YAML front matter
(`pptx_template:` as a repo-relative path, `footer_date:`), so a deck rebuilds
with no arguments. `--pdf` also renders a PDF next to the pptx via
scripts/render_docx_pdf.sh (sandboxed LibreOffice; optional).

Why: pandoc's --reference-doc path maps slides to layouts by fixed names
("Title Slide", "Section Header" ...) and drops a template's own footer
(date, slide number) and end slide. This script keeps the template's masters
and layouts and fills them directly.

Markdown conventions (a subset of pandoc's slide Markdown):
- YAML front matter between --- lines is skipped.
- `## Heading` starts a slide. `## Heading {layout="Title"}` picks a layout by name;
  default "Title and Content". The first non-empty body line on a "Title" or
  "Title Slide" layout becomes the subtitle; an "End slide" layout takes the heading only.
- `- item` and `  - sub-item` are bullets; other lines are paragraphs.
- Pipe tables become native tables (header row from the first row).
- `![caption](path){side=right}` places an image to the right of the text
  (text width shrinks); `{side=full}` fills the body area; the caption is set
  in small italics under the image.
- `::: notes` ... `:::` becomes the speaker notes of the slide.
- `<!-- ... -->` comments are ignored.

Footer: the date and slide-number placeholders are cloned from the template's
first content slide; `--date` sets the date text (default: keep the template's).

Requires: python-pptx, Pillow.
"""
import argparse
import copy
import re
import sys
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.util import Emu, Pt

BODY_PT = 22
SUB_PT = 19
TABLE_PT = 16
TITLE_PT = 32


def front_matter(md_text):
    lines = md_text.splitlines()
    out = {}
    if lines and lines[0].strip() == "---":
        for l in lines[1:]:
            if l.strip() == "---":
                break
            m = re.match(r"^(\w+):\s*(.*?)\s*$", l)
            if m:
                out[m.group(1)] = m.group(2).strip('"')
    return out


def parse(md_text):
    md_text = re.sub(r"<!--.*?-->", "", md_text, flags=re.S)
    lines = md_text.splitlines()
    if lines and lines[0].strip() == "---":
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
        lines = lines[end + 1:]
    slides, cur, in_notes = [], None, False
    for raw in lines:
        line = raw.rstrip()
        m = re.match(r"^## (.*?)(\s*\{layout=\"([^\"]+)\"\})?\s*$", line)
        if m and not in_notes:
            cur = {"title": m.group(1).strip(), "layout": m.group(3) or "Title and Content",
                   "body": [], "notes": []}
            slides.append(cur)
            continue
        if cur is None:
            continue
        if line.strip() == "::: notes":
            in_notes = True
            continue
        if line.strip() == ":::" and in_notes:
            in_notes = False
            continue
        (cur["notes"] if in_notes else cur["body"]).append(line)
    return slides


def blocks(body):
    """Group body lines into ('bullets', [(level, text)]), ('table', rows), ('image', ...), ('para', text)."""
    out, i = [], 0
    while i < len(body):
        line = body[i]
        if not line.strip():
            i += 1
            continue
        if line.lstrip().startswith("|"):
            rows = []
            while i < len(body) and body[i].lstrip().startswith("|"):
                cells = [c.strip() for c in body[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            out.append(("table", rows))
            continue
        m = re.match(r"^!\[(.*?)\]\((.*?)\)(\{side=(\w+)\})?", line.strip())
        if m:
            out.append(("image", (m.group(1), m.group(2), m.group(4) or "right")))
            i += 1
            continue
        if re.match(r"^\s*- ", line):
            items = []
            while i < len(body) and re.match(r"^\s*- ", body[i]):
                lvl = 1 if body[i].startswith("  ") else 0
                items.append((lvl, re.sub(r"^\s*- ", "", body[i]).strip()))
                i += 1
            out.append(("bullets", items))
            continue
        out.append(("para", line.strip()))
        i += 1
    return out


def layout_by_name(prs, name):
    for lay in prs.slide_layouts:
        if lay.name == name:
            return lay
    sys.exit(f"Layout {name!r} not in template")


def set_runs(par, text, size, italic=False):
    par.text = ""
    run = par.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.italic = italic


def fill_text(tf, items, first=True):
    for kind, payload in items:
        entries = payload if kind == "bullets" else [(None, payload)]
        for lvl, text in entries:
            par = tf.paragraphs[0] if first else tf.add_paragraph()
            first = False
            if lvl is None:
                set_runs(par, text, BODY_PT)
                pPr = par._p.get_or_add_pPr()
                pPr.set("marL", "0")
                pPr.set("indent", "0")
                buNone = pPr.makeelement("{http://schemas.openxmlformats.org/drawingml/2006/main}buNone", {})
                pPr.append(buNone)
            else:
                par.level = lvl
                set_runs(par, text, SUB_PT if lvl else BODY_PT)


def add_table(slide, rows, left, top, width, max_height):
    nrows, ncols = len(rows), max(len(r) for r in rows)
    row_h = min(Emu(int(max_height / nrows)), Emu(Pt(TABLE_PT * 2.3)))
    shape = slide.shapes.add_table(nrows, ncols, left, top, width, Emu(row_h * nrows))
    table = shape.table
    # column widths proportional to the longest cell text, with a floor
    lens = [max(len(r[c]) if c < len(r) else 0 for r in rows) for c in range(ncols)]
    lens = [max(l, 11) for l in lens]
    total = sum(lens)
    for c in range(ncols):
        table.columns[c].width = Emu(int(width * lens[c] / total))
    for r, row in enumerate(rows):
        table.rows[r].height = row_h
        for c in range(ncols):
            cell = table.cell(r, c)
            cell.margin_top = cell.margin_bottom = Emu(Pt(2))
            text = row[c] if c < len(row) else ""
            set_runs(cell.text_frame.paragraphs[0], text, TABLE_PT)
            cell.text_frame.word_wrap = True
    return shape


def add_image(slide, path, caption, left, top, width, height):
    with Image.open(path) as im:
        w, h = im.size
    scale = min(width / w, (height - Emu(Pt(22))) / h)
    pw, ph = int(w * scale), int(h * scale)
    px = left + int((width - pw) / 2)
    slide.shapes.add_picture(str(path), px, top, pw, ph)
    if caption:
        tb = slide.shapes.add_textbox(left, top + ph + Emu(Pt(2)), width, Emu(Pt(20)))
        tb.text_frame.word_wrap = True
        set_runs(tb.text_frame.paragraphs[0], caption, 11, italic=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("--template", help="reference deck; default: `pptx_template:` in the YAML front matter")
    ap.add_argument("-o", "--out")
    ap.add_argument("--date", help="footer date text; default: `footer_date:` in the YAML front matter")
    ap.add_argument("--pdf", action="store_true",
                    help="also render a PDF next to the pptx with scripts/render_docx_pdf.sh (LibreOffice)")
    a = ap.parse_args()
    md = Path(a.md)
    front = front_matter(md.read_text(encoding="utf-8"))
    a.template = a.template or front.get("pptx_template")
    a.date = a.date or front.get("footer_date")
    if not a.template:
        sys.exit("No template: pass --template or set pptx_template: in the front matter")
    repo = Path(__file__).resolve().parent.parent
    if not Path(a.template).is_absolute() and not Path(a.template).exists():
        a.template = str(repo / a.template)
    out = Path(a.out) if a.out else md.with_suffix(".pptx")
    slides = parse(md.read_text(encoding="utf-8"))

    prs = Presentation(a.template)
    # footer placeholders and body geometry from the template's first content slide
    footer_xml, body_geo = [], None
    for s in prs.slides:
        if s.slide_layout.name == "Title and Content":
            for sh in s.shapes:
                if sh.is_placeholder and sh.placeholder_format.idx in (10, 11):
                    footer_xml.append(copy.deepcopy(sh._element))
                elif sh.is_placeholder and sh.placeholder_format.idx == 0 and body_geo is None:
                    # content area: aligned with the title, from below the title to above the footer
                    foot_top = min((f.top for f in s.shapes if f.is_placeholder
                                    and f.placeholder_format.idx in (10, 11)), default=prs.slide_height)
                    top = sh.top + sh.height + Emu(Pt(6))
                    body_geo = (sh.left, top, prs.slide_width - sh.left - Emu(Pt(40)),
                                foot_top - top - Emu(Pt(14)))
            break
    # drop all template slides
    sldIdLst = prs.slides._sldIdLst
    for sldId in list(sldIdLst):
        prs.part.drop_rel(sldId.rId)
        sldIdLst.remove(sldId)

    for spec in slides:
        lay = layout_by_name(prs, spec["layout"])
        slide = prs.slides.add_slide(lay)
        title = spec["title"]
        bl = blocks(spec["body"])
        if spec["layout"] in ("Title", "Title Slide"):
            slide.shapes.title.text = title
            for p in slide.shapes.title.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(28)
            paras = [p for k, p in bl if k == "para"]
            for ph in slide.placeholders:
                if ph.placeholder_format.idx == 1:
                    ph.text_frame.text = "\n".join(paras)
        elif spec["layout"] == "End slide":
            slide.shapes.title.text = title
        else:
            slide.shapes.title.text = title
            for p in slide.shapes.title.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(TITLE_PT)
            body_ph = next(ph for ph in slide.placeholders if ph.placeholder_format.idx == 1)
            left, top, width, height = body_geo or (body_ph.left, body_ph.top, body_ph.width, body_ph.height)
            images = [p for k, p in bl if k == "image"]
            tables = [p for k, p in bl if k == "table"]
            texts = [(k, p) for k, p in bl if k in ("bullets", "para")]
            text_w = width
            if images and images[0][2] == "right":
                text_w = int(width * 0.56)
                cap, path, _ = images[0]
                add_image(slide, md.parent / path if not Path(path).is_absolute() else path, cap,
                          left + text_w + Emu(Pt(12)), top, width - text_w - Emu(Pt(12)), height)
            elif images:
                cap, path, _ = images[0]
                txt_h = Emu(Pt(26)) * len(texts)
                add_image(slide, md.parent / path, cap, left, top + txt_h, width, height - txt_h)
            if tables:
                # text above the table, table fills the rest
                cpl = max(1, int((text_w / 12700 - 30) / (BODY_PT * 0.5)))
                n_lines = sum(-(-len(t) // cpl) for k, p in texts
                              for t in ([x[1] for x in p] if k == "bullets" else [p]))
                txt_h = Emu(int(Pt(BODY_PT * 1.25) * n_lines + Pt(12)))
                body_ph.left, body_ph.top, body_ph.width, body_ph.height = left, top, text_w, txt_h
                if texts:
                    fill_text(body_ph.text_frame, texts)
                else:
                    body_ph._element.getparent().remove(body_ph._element)
                tb_top = top + txt_h + Emu(Pt(6))
                add_table(slide, tables[0], left, tb_top, text_w, height - txt_h - Emu(Pt(6)))
            else:
                body_ph.left, body_ph.top, body_ph.width, body_ph.height = left, top, text_w, height
                if texts:
                    fill_text(body_ph.text_frame, texts)
                    body_ph.text_frame.word_wrap = True
                else:
                    body_ph._element.getparent().remove(body_ph._element)
            for el in footer_xml:
                el2 = copy.deepcopy(el)
                A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
                if a.date:
                    for fld in list(el2.iter(A + "fld")):
                        if fld.get("type", "").startswith("datetime"):
                            fld.tag = A + "r"  # a static run keeps the text when the deck is opened
                            for k in ("id", "type"):
                                fld.attrib.pop(k, None)
                            for t in fld.iter(A + "t"):
                                t.text = a.date
                slide.shapes._spTree.append(el2)
        notes = "\n".join(spec["notes"]).strip()
        if notes:
            notes = re.sub(r"\n(?!\n)", " ", notes)  # unwrap soft line breaks, keep paragraphs
            slide.notes_slide.notes_text_frame.text = notes
    prs.save(out)
    if a.pdf:
        import os, shutil, subprocess, tempfile
        tmp = Path(tempfile.mkdtemp(dir=repo / "temp")) if (repo / "temp").is_dir() else Path(tempfile.mkdtemp())
        env = dict(os.environ, OUTDIR=str(tmp))
        subprocess.run(["bash", str(repo / "scripts" / "render_docx_pdf.sh"), str(out)], check=True, env=env)
        shutil.move(str(tmp / (out.stem + ".pdf")), str(out.with_suffix(".pdf")))
        shutil.rmtree(tmp, ignore_errors=True)
        print(f"{out.with_suffix('.pdf')}")
    print(f"{out}: {len(slides)} slides, notes on {sum(1 for s in slides if any(l.strip() for l in s['notes']))}")


if __name__ == "__main__":
    main()
