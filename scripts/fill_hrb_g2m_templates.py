"""Fill Horizon Results Booster G2M templates from Markdown sources.

Fills the four G2M templates issued by META Group (characterisation table,
exploitation roadmap, risk assessment map, BOSAT questionnaire) from the
Markdown sources under surewave/deliverables/. Works directly on the OOXML
parts with lxml so form controls (BOSAT radio buttons), charts, comments and
hidden sheets in the templates survive untouched. Never modifies the
templates; always writes new output files.

Usage:
    python scripts/fill_hrb_g2m_templates.py characterisation <template.docx> <source.md> <out.docx>
    python scripts/fill_hrb_g2m_templates.py roadmap          <template.docx> <source.md> <out.docx>
    python scripts/fill_hrb_g2m_templates.py risk             <template.xlsx> <source.md> <out.xlsx>
    python scripts/fill_hrb_g2m_templates.py bosat            <template.xlsx> <source.md> <out.xlsx>
    python scripts/fill_hrb_g2m_templates.py lean             <template.pptx> <source.md> <out.pptx>
    python scripts/fill_hrb_g2m_templates.py bizplan          <template.docx> <source.md> <out.docx>
"""

import copy
import re
import sys
import zipfile
from pathlib import Path

from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
S = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
X14 = "http://schemas.microsoft.com/office/spreadsheetml/2009/9/main"
XDR = "http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PR = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"w": W, "s": S, "x14": X14, "xdr": XDR, "r": R, "pr": PR}


def q(ns, tag):
    return "{%s}%s" % (NS[ns], tag)


# --------------------------------------------------------------------------
# Markdown parsing
# --------------------------------------------------------------------------

def md_sections(path):
    """Return {heading: body_lines} for every '## heading' in the file."""
    sections, cur = {}, None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            cur = m.group(1).strip()
            sections[cur] = []
        elif cur is not None:
            sections[cur].append(line.rstrip())
    for k, v in sections.items():
        while v and not v[0].strip():
            v.pop(0)
        while v and not v[-1].strip():
            v.pop()
    return sections


def md_table(lines):
    rows = [l for l in lines if l.strip().startswith("|")]
    out = []
    for l in rows:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        out.append(cells)
    return out[0], out[1:]


def strip_md(text):
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return text.replace("`", "")


def body_to_paragraphs(lines):
    """Turn markdown body lines into a list of (text, is_bullet) paragraphs.
    Markdown tables are flattened to one line per row."""
    paras, buf = [], []
    table_lines = []

    def flush():
        if buf:
            paras.append((strip_md(" ".join(buf)), False))
            buf.clear()

    for line in lines + [""]:
        s = line.strip()
        if s.startswith("|"):
            flush()
            table_lines.append(s)
            continue
        if table_lines:
            header, rows = md_table(table_lines)
            for r in rows:
                parts = [r[0]] + ["%s: %s" % (h, c) for h, c in zip(header[1:], r[1:])]
                paras.append((strip_md(" — ".join(parts)), True))
            table_lines = []
        if not s:
            flush()
        elif s.startswith("- "):
            flush()
            paras.append((strip_md(s[2:]), True))
        else:
            buf.append(s)
    return paras


# --------------------------------------------------------------------------
# DOCX filling
# --------------------------------------------------------------------------

def text_of(el):
    return "".join(el.itertext()).strip()


def clean_rpr(rpr):
    rpr = copy.deepcopy(rpr) if rpr is not None else etree.Element(q("w", "rPr"))
    for tag in ("highlight", "i", "iCs", "b", "bCs", "shd"):
        for e in rpr.findall(q("w", tag)):
            rpr.remove(e)
    return rpr


def make_para(ppr, rpr, text, bullet):
    p = etree.Element(q("w", "p"))
    if ppr is not None:
        p.append(copy.deepcopy(ppr))
    r = etree.SubElement(p, q("w", "r"))
    r.append(copy.deepcopy(rpr))
    t = etree.SubElement(r, q("w", "t"))
    t.text = ("• " + text) if bullet else text
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    return p


def fill_cell(tc, paragraphs):
    ps = tc.findall(q("w", "p"))
    ppr = ps[0].find(q("w", "pPr")) if ps else None
    first_r = tc.find(".//" + q("w", "r"))
    rpr = clean_rpr(first_r.find(q("w", "rPr")) if first_r is not None else None)
    if ppr is not None:
        ppr = copy.deepcopy(ppr)
        rp = ppr.find(q("w", "rPr"))
        if rp is not None:
            ppr.remove(rp)
    for p in ps:
        tc.remove(p)
    for text, bullet in paragraphs:
        tc.append(make_para(ppr, rpr, text, bullet))


def norm(s):
    return re.sub(r"[^a-z]", "", s.lower())


def replace_marked_runs(par, new_text):
    """Replace highlighted placeholder runs in a paragraph with new_text."""
    runs = par.findall(".//" + q("w", "r"))
    marked = [r for r in runs if r.find(q("w", "rPr") + "/" + q("w", "highlight")) is not None]
    if not marked:
        return False
    first = marked[0]
    rpr = first.find(q("w", "rPr"))
    for e in rpr.findall(q("w", "highlight")):
        rpr.remove(e)
    for t in first.findall(q("w", "t")):
        first.remove(t)
    t = etree.SubElement(first, q("w", "t"))
    t.text = new_text
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    for r in marked[1:]:
        r.getparent().remove(r)
    return True


def fill_docx(template, md, out, title_section, title_label_regex):
    sections = md_sections(md)
    keymap = {norm(k): k for k in sections}
    with zipfile.ZipFile(template) as zin:
        doc = etree.fromstring(zin.read("word/document.xml"))
        body = doc.find(q("w", "body"))
        # Drop instruction paragraphs that are pure highlighted placeholders outside tables.
        for p in list(body.findall(q("w", "p"))):
            txt = text_of(p)
            if txt.startswith("[") and "prepare a characterisation table" in txt:
                body.remove(p)
        filled = []
        for tr in doc.iter(q("w", "tr")):
            tcs = tr.findall(q("w", "tc"))
            label = text_of(tcs[0]) if tcs else ""
            if re.search(title_label_regex, label, re.I):
                title = strip_md(" ".join(sections[title_section]).strip())
                par = tcs[0].findall(q("w", "p"))[-1]
                if not replace_marked_runs(par, title):
                    r = etree.SubElement(par, q("w", "r"))
                    t = etree.SubElement(r, q("w", "t"))
                    t.text = " " + title
                    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
                filled.append(title_section)
                continue
            if len(tcs) < 2:
                continue
            key = keymap.get(norm(label.rstrip(":")))
            if key:
                fill_cell(tcs[1], body_to_paragraphs(sections[key]))
                filled.append(key)
        write_zip(zin, out, {"word/document.xml": doc})
    return filled


# --------------------------------------------------------------------------
# XLSX helpers
# --------------------------------------------------------------------------

def col_to_num(col):
    n = 0
    for ch in col:
        n = n * 26 + ord(ch) - 64
    return n


def split_ref(ref):
    m = re.match(r"([A-Z]+)(\d+)", ref)
    return m.group(1), int(m.group(2))


def get_cell(sheet, ref):
    col, row = split_ref(ref)
    sd = sheet.find(q("s", "sheetData"))
    rows = sd.findall(q("s", "row"))
    row_el = next((r for r in rows if int(r.get("r")) == row), None)
    if row_el is None:
        row_el = etree.Element(q("s", "row"), r=str(row))
        after = [r for r in rows if int(r.get("r")) < row]
        if after:
            after[-1].addnext(row_el)
        else:
            sd.insert(0, row_el)
    cells = row_el.findall(q("s", "c"))
    c = next((x for x in cells if x.get("r") == ref), None)
    if c is None:
        c = etree.Element(q("s", "c"), r=ref)
        before = [x for x in cells if col_to_num(split_ref(x.get("r"))[0]) < col_to_num(col)]
        if before:
            before[-1].addnext(c)
        else:
            row_el.insert(0, c)
    return c


def set_value(sheet, ref, value):
    c = get_cell(sheet, ref)
    for ch in list(c):
        c.remove(ch)
    if isinstance(value, (int, float)):
        c.attrib.pop("t", None)
        etree.SubElement(c, q("s", "v")).text = str(value)
    else:
        c.set("t", "inlineStr")
        is_ = etree.SubElement(c, q("s", "is"))
        t = etree.SubElement(is_, q("s", "t"))
        t.text = value
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")


def set_cached(sheet, ref, value):
    """Update the cached result of an existing formula cell."""
    c = get_cell(sheet, ref)
    v = c.find(q("s", "v"))
    if v is None:
        v = etree.SubElement(c, q("s", "v"))
    if isinstance(value, str):
        c.set("t", "str")
    else:
        c.attrib.pop("t", None)
    v.text = str(value)


def shared_strings(zin):
    try:
        sst = etree.fromstring(zin.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    return ["".join(si.itertext()) for si in sst.findall(q("s", "si"))]


def cell_text(sheet, ref, sst):
    c = get_cell(sheet, ref)
    v = c.find(q("s", "v"))
    if c.get("t") == "s" and v is not None:
        return sst[int(v.text)]
    if c.get("t") == "inlineStr":
        return "".join(c.itertext())
    return v.text if v is not None else None


def force_recalc(wb):
    calc = wb.find(q("s", "calcPr"))
    if calc is None:
        calc = etree.SubElement(wb, q("s", "calcPr"))
    calc.set("fullCalcOnLoad", "1")


def write_zip(zin, out, replaced, drop=()):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename in drop:
                continue
            if item.filename in replaced:
                data = replaced[item.filename]
                if not isinstance(data, bytes):
                    data = etree.tostring(data, xml_declaration=True, encoding="UTF-8", standalone=True)
                zout.writestr(item, data)
            else:
                zout.writestr(item, zin.read(item.filename))


# --------------------------------------------------------------------------
# Risk assessment map
# --------------------------------------------------------------------------

RISK_BLOCKS = {
    "partnership": range(5, 10),
    "technological": range(11, 16),
    "market": range(17, 22),
    "ipr/legal": range(23, 28),
    "financial/management": range(29, 34),
    "environmental/regulation/safety": range(35, 40),
}


def risk_conclusion(f, h):
    if f == 0:
        return "Not Filled"
    if f == 50 and h == 5:
        return "In the Middle of Everything"
    if h == 5 and f < 50:
        return "Between Control & No Action"
    if h == 5 and f > 50:
        return "Between Action & Warning"
    if f == 50 and h < 5:
        return "Between No Action & Warning"
    if f == 50 and h > 5:
        return "Between Control & Action"
    if f > 50 and h < 5:
        return "Warning;"
    if f > 50 and h > 5:
        return "Action!"
    if h < 5:
        return "No Action'"
    return "Control."


def fill_risk(template, md, out):
    sections = md_sections(md)
    first = next(iter(sections.values()))
    title_line = Path(md).read_text(encoding="utf-8").splitlines()[0]
    ker = title_line.split("—", 1)[1].strip()
    table_lines = []
    for line in Path(md).read_text(encoding="utf-8").splitlines():
        if line.startswith("|"):
            table_lines.append(line)
    header, rows = md_table(table_lines)
    with zipfile.ZipFile(template) as zin:
        sheet = etree.fromstring(zin.read("xl/worksheets/sheet3.xml"))
        wb = etree.fromstring(zin.read("xl/workbook.xml"))
        set_value(sheet, "B2", "Risk Assessment Map - " + ker)
        slots = {k: list(v) for k, v in RISK_BLOCKS.items()}
        counts = {}
        for cat, risk, crit, prob, interv, feas in rows:
            r = slots[cat.lower()].pop(0)
            d, e, h = int(crit), int(prob), int(feas)
            set_value(sheet, "C%d" % r, risk)
            set_value(sheet, "D%d" % r, d)
            set_value(sheet, "E%d" % r, e)
            set_value(sheet, "G%d" % r, interv)
            set_value(sheet, "H%d" % r, h)
            set_cached(sheet, "F%d" % r, d * e)
            # Grow the row when the text needs more than the template's fixed height
            # (about 50 characters per line in C, 75 in G, 12 pt per line).
            lines = max(-(-len(risk) // 50), -(-len(interv) // 75))
            row_el = next(x for x in sheet.iter(q("s", "row")) if int(x.get("r")) == r)
            need = lines * 12 + 6
            if need > float(row_el.get("ht", "0")):
                row_el.set("ht", str(need))
                row_el.set("customHeight", "1")
            concl = risk_conclusion(d * e, h)
            set_cached(sheet, "I%d" % r, concl)
            counts[concl] = counts.get(concl, 0) + 1
        force_recalc(wb)
        write_zip(zin, out, {"xl/worksheets/sheet3.xml": sheet, "xl/workbook.xml": wb})
    return counts


# --------------------------------------------------------------------------
# BOSAT questionnaire
# --------------------------------------------------------------------------

def fill_bosat(template, md, out):
    text = Path(md).read_text(encoding="utf-8").splitlines()
    ker = text[0].split("—", 1)[1].strip()
    _, rows = md_table([l for l in text if l.startswith("|")])
    answers = {code.replace("IP", "I"): ans for code, ans, _ in rows}
    with zipfile.ZipFile(template) as zin:
        sst = shared_strings(zin)
        sheet = etree.fromstring(zin.read("xl/worksheets/sheet1.xml"))
        wb = etree.fromstring(zin.read("xl/workbook.xml"))
        rels = etree.fromstring(zin.read("xl/worksheets/_rels/sheet1.xml.rels"))
        rid_target = {r.get("Id"): r.get("Target") for r in rels}
        set_value(sheet, "D2", ker)
        # Walk question blocks: D cell starting with code, options in F from next row.
        sd = sheet.find(q("s", "sheetData"))
        qrows = []
        for row in sd.findall(q("s", "row")):
            r = int(row.get("r"))
            t = cell_text(sheet, "D%d" % r, sst)
            if t:
                m = re.match(r"^(T|Tm|M|U|I|F)(\d+)\.", t)
                if m:
                    qrows.append((m.group(1) + m.group(2), r))
        done = []
        for code, r in qrows:
            if code not in answers:
                raise SystemExit("No answer for %s" % code)
            want = answers[code].strip()
            k, opt_row, score = 0, None, None
            rr = r + 1
            idx = 0
            while True:
                opt = cell_text(sheet, "F%d" % rr, sst)
                if not opt:
                    break
                idx += 1
                if opt.strip() == want:
                    k, opt_row = idx, rr
                    score = cell_text(sheet, "G%d" % rr, sst)
                rr += 1
            if not k:
                raise SystemExit("Answer for %s not found among options: %r" % (code, want))
            set_value(sheet, "H%d" % r, k)
            set_cached(sheet, "G%d" % r, float(score))
            # Mark the options as text in column E (which holds a "." in the template):
            # "[x]" for the chosen option, "[ ]" for the others.
            for i in range(1, idx + 1):
                set_value(sheet, "E%d" % (r + i), "[x]" if i == k else "[ ]")
            done.append((code, k, score))
        force_recalc(wb)
        # Remove the radio buttons. They are replaced by the text marks, and they
        # render unreliably (LibreOffice resets cell-linked option groups on load).
        # Each control lives in three places: <controls> in the sheet, a ctrlProp
        # part (via the sheet rels) and a shape in the legacy VML drawing.
        radio_rids, radio_sids = set(), set()
        for ctl in list(sheet.iter(q("s", "control"))):
            part = "xl/" + rid_target.get(ctl.get(q("r", "id")), "").replace("../", "")
            try:
                props = etree.fromstring(zin.read(part))
            except KeyError:
                continue
            if props.get("objectType") != "Radio":
                continue
            radio_rids.add(ctl.get(q("r", "id")))
            radio_sids.add(ctl.get("shapeId"))
            node = ctl
            while node.getparent().tag != q("s", "controls"):
                node = node.getparent()
            node.getparent().remove(node)
        controls = sheet.find(".//" + q("s", "controls"))
        if controls is not None and len(controls) == 0:
            node = controls
            while node.getparent() is not sheet:
                node = node.getparent()
            sheet.remove(node)
        drop = set()
        for rel in list(rels):
            if rel.get("Id") in radio_rids:
                drop.add("xl/" + rel.get("Target").replace("../", ""))
                rels.remove(rel)
        ct = etree.fromstring(zin.read("[Content_Types].xml"))
        for o in list(ct):
            if o.get("PartName", "").lstrip("/") in drop:
                ct.remove(o)
        vml_name = "xl/drawings/vmlDrawing1.vml"
        vml = zin.read(vml_name).decode("utf-8")
        vml, _ = re.subn(r'<v:shape id="_x0000_s(\d+)"(?:(?!</v:shape>).)*?</v:shape>',
                         lambda m: "" if m.group(1) in radio_sids else m.group(0), vml, flags=re.S)
        replaced = {
            "xl/worksheets/sheet1.xml": sheet,
            "xl/workbook.xml": wb,
            "xl/worksheets/_rels/sheet1.xml.rels": rels,
            "[Content_Types].xml": ct,
            vml_name: vml.encode("utf-8"),
        }
        done.append(("radio buttons removed", len(radio_sids), ""))
        write_zip(zin, out, replaced, drop=drop)
    return done


# --------------------------------------------------------------------------
# Lean Canvas (pptx, one slide)
# --------------------------------------------------------------------------

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"

# shape name -> list of (template heading text, markdown section, subsection or None)
LEAN_BOXES = {
    "Rounded Rectangle 3": [("Problem", "Problem", None),
                            ("Alternative Solutions", "Problem", "Alternative solutions")],
    "Rounded Rectangle 11": [("Solution", "Solution", None)],
    "Rounded Rectangle 12": [("Key Metrics", "Key metrics", None)],
    "Rounded Rectangle 13": [("Unique Value Proposition", "Unique Value Proposition", None)],
    "Rounded Rectangle 14": [("Unfair Advantage", "Unfair advantage", None)],
    "Rounded Rectangle 15": [("Channels", "Channels", None)],
    "Rounded Rectangle 16": [("Customer Segments", "Customer segments", None),
                             ("Early adopters", "Customer segments", "Early adopters")],
    "Rounded Rectangle 17": [("Cost Structure", "Cost structure", None)],
    "Rounded Rectangle 18": [("Revenue Streams", "Revenue streams", None)],
}


def split_subsections(lines):
    """Split a '## ' section body into {None: main_lines, '### name': lines}."""
    out, cur = {None: []}, None
    for line in lines:
        m = re.match(r"^###\s+(.*)$", line)
        if m:
            cur = m.group(1).strip()
            out[cur] = []
        else:
            out[cur].append(line)
    return out


def lean_para(text, size, bullet):
    p = etree.Element("{%s}p" % A)
    ppr = etree.SubElement(p, "{%s}pPr" % A)
    if bullet:
        ppr.set("marL", "114300")
        ppr.set("indent", "-114300")
        etree.SubElement(ppr, "{%s}buFont" % A, typeface="Arial")
        etree.SubElement(ppr, "{%s}buChar" % A, char="•")
    else:
        etree.SubElement(ppr, "{%s}spcAft" % A).append(
            etree.Element("{%s}spcPts" % A, val="300"))
    r = etree.SubElement(p, "{%s}r" % A)
    rpr = etree.SubElement(r, "{%s}rPr" % A, lang="en-US", sz=str(size), dirty="0")
    fill = etree.SubElement(rpr, "{%s}solidFill" % A)
    clr = etree.SubElement(fill, "{%s}schemeClr" % A, val="tx1")
    etree.SubElement(clr, "{%s}lumMod" % A, val="75000")
    etree.SubElement(clr, "{%s}lumOff" % A, val="25000")
    etree.SubElement(rpr, "{%s}latin" % A, typeface="Arial")
    etree.SubElement(rpr, "{%s}cs" % A, typeface="Arial")
    t = etree.SubElement(r, "{%s}t" % A)
    t.text = text
    return p


def set_textbox(sp, text, size=None):
    runs = sp.findall(".//{%s}r" % A)
    runs[0].find("{%s}t" % A).text = text
    if size:
        runs[0].find("{%s}rPr" % A).set("sz", str(size))
    for r in runs[1:]:
        r.getparent().remove(r)


def fill_lean(template, md, out, size=800):
    sections = md_sections(md)
    header = Path(md).read_text(encoding="utf-8").splitlines()[2]
    date = re.search(r"(\d{1,2}) (\w+) (\d{4})", header)
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    date_txt = "%02d-%02d-%s" % (int(date.group(1)), months.index(date.group(2)) + 1, date.group(3))
    iteration = re.search(r"Iteration #\d+", header).group(0)
    filled = []
    with zipfile.ZipFile(template) as zin:
        slide = etree.fromstring(zin.read("ppt/slides/slide1.xml"))
        for sp in slide.iter("{%s}sp" % P):
            name = sp.find(".//{%s}cNvPr" % P).get("name")
            if name == "TextBox 6":
                set_textbox(sp, strip_md(" ".join(sections["KER name"]).strip()), 1100)
            elif name == "TextBox 7":
                set_textbox(sp, date_txt)
            elif name == "TextBox 10":
                set_textbox(sp, iteration)
            if name not in LEAN_BOXES:
                continue
            body = sp.find("{%s}txBody" % P)
            paras = body.findall("{%s}p" % A)
            heads = {}
            for p in paras:
                heads.setdefault(text_of(p), p)
                body.remove(p)
            for head, sec, sub in LEAN_BOXES[name]:
                body.append(heads[head])
                lines = split_subsections(sections[sec])[sub]
                for text, bullet in body_to_paragraphs(lines):
                    body.append(lean_para(text, size, bullet))
                filled.append(head)
        write_zip(zin, out, {"ppt/slides/slide1.xml": slide})
    return filled


# --------------------------------------------------------------------------
# Business Plan template (docx, free-text chapters)
# --------------------------------------------------------------------------

def md_blocks(lines):
    """Turn section body lines into blocks: ('h', text), ('p', text), ('li', text), ('table', rows)."""
    blocks, buf, table = [], [], []

    def flush():
        if buf:
            blocks.append(("p", strip_md(" ".join(buf))))
            buf.clear()

    for line in lines + [""]:
        s = line.strip()
        if s.startswith("|"):
            flush()
            table.append(s)
            continue
        if table:
            header, rows = md_table(table)
            blocks.append(("table", [header] + rows))
            table = []
        if not s:
            flush()
        elif s.startswith("### "):
            flush()
            blocks.append(("h", strip_md(s[4:])))
        elif s.startswith("- "):
            flush()
            blocks.append(("li", strip_md(s[2:])))
        elif re.match(r"^\d+\. ", s):
            # Numbered items stay separate paragraphs, keeping their number.
            flush()
            blocks.append(("p", strip_md(s)))
        else:
            buf.append(s)
    return blocks


def bp_run(text, size=22):
    r = etree.Element(q("w", "r"))
    rpr = etree.SubElement(r, q("w", "rPr"))
    etree.SubElement(rpr, q("w", "rFonts"), {q("w", "ascii"): "Calibri", q("w", "hAnsi"): "Calibri", q("w", "cs"): "Calibri"})
    etree.SubElement(rpr, q("w", "sz"), {q("w", "val"): str(size)})
    etree.SubElement(rpr, q("w", "lang"), {q("w", "val"): "en-GB"})
    t = etree.SubElement(r, q("w", "t"))
    t.text = text
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    return r


def bp_para(text, style=None, num=None, size=22, after=120, jc=None):
    p = etree.Element(q("w", "p"))
    ppr = etree.SubElement(p, q("w", "pPr"))
    if style:
        etree.SubElement(ppr, q("w", "pStyle"), {q("w", "val"): style})
    if num is not None:
        ppr.append(copy.deepcopy(num))
    if after is not None:
        etree.SubElement(ppr, q("w", "spacing"), {q("w", "after"): str(after)})
    if jc:
        etree.SubElement(ppr, q("w", "jc"), {q("w", "val"): jc})
    p.append(bp_run(text, size))
    return p


def bp_table(rows):
    tbl = etree.Element(q("w", "tbl"))
    tblpr = etree.SubElement(tbl, q("w", "tblPr"))
    etree.SubElement(tblpr, q("w", "tblStyle"), {q("w", "val"): "Grigliatabella"})
    etree.SubElement(tblpr, q("w", "tblW"), {q("w", "w"): "5000", q("w", "type"): "pct"})
    etree.SubElement(tblpr, q("w", "tblLook"), {q("w", "val"): "04A0", q("w", "firstRow"): "1"})
    grid = etree.SubElement(tbl, q("w", "tblGrid"))
    ncol = len(rows[0])
    for _ in range(ncol):
        etree.SubElement(grid, q("w", "gridCol"), {q("w", "w"): str(9000 // ncol)})
    for i, row in enumerate(rows):
        tr = etree.SubElement(tbl, q("w", "tr"))
        if i == 0:
            trpr = etree.SubElement(tr, q("w", "trPr"))
            etree.SubElement(trpr, q("w", "tblHeader"))
        for cell in row:
            tc = etree.SubElement(tr, q("w", "tc"))
            tcpr = etree.SubElement(tc, q("w", "tcPr"))
            etree.SubElement(tcpr, q("w", "tcW"), {q("w", "w"): str(5000 // ncol), q("w", "type"): "pct"})
            if i == 0:
                etree.SubElement(tcpr, q("w", "shd"), {q("w", "val"): "clear", q("w", "color"): "auto", q("w", "fill"): "D9E2F3"})
            tc.append(bp_para(strip_md(cell), size=18, after=0, jc="left"))
    return tbl


def fill_bizplan(template, md, out):
    """Fill the chapters of the Business Plan template that have a matching '## ' section.
    Chapters without a section keep the template's guidance text."""
    sections = md_sections(md)
    keymap = {norm(k): k for k in sections}
    title = Path(md).read_text(encoding="utf-8").splitlines()[0]
    ker = title.split("—", 1)[1].strip()
    filled = []
    with zipfile.ZipFile(template) as zin:
        doc = etree.fromstring(zin.read("word/document.xml"))
        body = doc.find(q("w", "body"))
        children = list(body)
        # Title: "Business Plan for [name of the KER]"
        for p in children:
            if p.tag == q("w", "p") and "name of the KER" in text_of(p):
                for r in p.findall(q("w", "r")):
                    t = r.find(q("w", "t"))
                    if t is None:
                        continue
                    if t.text == "name of the KER":
                        t.text = ker
                        hl = r.find(q("w", "rPr") + "/" + q("w", "highlight"))
                        if hl is not None:
                            hl.getparent().remove(hl)
                    elif t.text.endswith("["):
                        t.text = t.text[:-1]
                    elif t.text == "]":
                        t.text = ""
                break
        # Bullet numbering from the template's own list paragraphs.
        num = next(p.find(".//" + q("w", "numPr")) for p in children
                   if p.tag == q("w", "p") and p.find(".//" + q("w", "numPr")) is not None)
        heads = [p for p in children if p.tag == q("w", "p")
                 and p.find(".//" + q("w", "pStyle")) is not None
                 and p.find(".//" + q("w", "pStyle")).get(q("w", "val")) == "Titolo1"]
        for h in heads:
            key = keymap.get(norm(text_of(h)))
            if not key:
                continue
            # Remove the guidance paragraphs up to the next chapter heading.
            idx = list(body).index(h)
            removed_marks = []
            nxt = h.getnext()
            while nxt is not None and nxt not in heads and nxt.tag == q("w", "p") \
                    and nxt.find(".//" + q("w", "sectPr")) is None:
                if text_of(nxt) == "" and nxt.find(".//" + q("w", "highlight")) is None:
                    break
                removed_marks += nxt.findall(".//" + q("w", "bookmarkStart")) + nxt.findall(".//" + q("w", "bookmarkEnd"))
                after = nxt.getnext()
                body.remove(nxt)
                nxt = after
            new = []
            for kind, val in md_blocks(sections[key]):
                if kind == "h":
                    new.append(bp_para(val, style="Titolo2", after=None))
                elif kind == "p":
                    new.append(bp_para(val))
                elif kind == "li":
                    new.append(bp_para(val, style="Paragrafoelenco", num=num, after=None))
                elif kind == "table":
                    new.append(bp_table(val))
                    new.append(bp_para("", after=0))
            if removed_marks:
                first_p = next(e for e in new if e.tag == q("w", "p"))
                ppr = first_p.find(q("w", "pPr"))
                for m in removed_marks:
                    ppr.addnext(m)
            for k, e in enumerate(new):
                body.insert(idx + 1 + k, e)
            filled.append(key)
        write_zip(zin, out, {"word/document.xml": doc})
    return filled


def main():
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(1)
    kind, template, md, out = sys.argv[1:]
    if kind == "characterisation":
        print(fill_docx(template, md, out, "KER name", r"^KER name"))
    elif kind == "roadmap":
        print(fill_docx(template, md, out, "KER title", r"^Exploitation roadmap for KER"))
    elif kind == "risk":
        print(fill_risk(template, md, out))
    elif kind == "bosat":
        for row in fill_bosat(template, md, out):
            print(*row)
    elif kind == "lean":
        print(fill_lean(template, md, out))
    elif kind == "bizplan":
        print(fill_bizplan(template, md, out))
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
