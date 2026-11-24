# /// script
# dependencies = ["python-docx"]
# ///
"""One-off (T146): apply Sunlit Sea's paste-in entries directly to the SUREWAVE
Final Technical Report docx. Usage: uv run apply_ftr_edits.py IN.docx OUT.docx
Never writes to IN. Every anchor must resolve exactly once or the script stops."""
import sys, re, copy
import docx
from docx.oxml.ns import qn

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M = 'http://schemas.openxmlformats.org/officeDocument/2006/math'

def N(s):
    s = s.replace(" ", " ").replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()

src, out = sys.argv[1], sys.argv[2]
assert src != out
d = docx.Document(src)
body = d.element.body
PS = list(body.iter(qn('w:p')))
log = []

def T(p):
    return "".join(x.text or "" for x in p.iter(qn('w:t')))

def one(sub, exact=False, nth=None):
    hits = [p for p in PS if (N(T(p)) == N(sub) if exact else N(sub) in N(T(p)))]
    if nth is not None:
        return hits[nth]
    if len(hits) != 1:
        raise SystemExit(f"ANCHOR {len(hits)} hits: {sub[:80]}")
    return hits[0]

def nxt(p):
    i = PS.index(p)
    return PS[i + 1]

AUTH = "Sunlit Sea (Eirik Larsen)"
DATE = "2026-11-24T14:00:00Z"
_rid = [9000]
def _rev(tag):
    _rid[0] += 1
    e = body.makeelement(qn(tag), {qn('w:id'): str(_rid[0]), qn('w:author'): AUTH, qn('w:date'): DATE})
    return e
XS = '{http://www.w3.org/XML/1998/namespace}space'

def _clean_rpr(rpr, keep_bold=False):
    rp = copy.deepcopy(rpr) if rpr is not None else None
    if rp is not None and not keep_bold:
        for tag in ('w:b', 'w:bCs'):
            e = rp.find(qn(tag))
            if e is not None: rp.remove(e)
    return rp

def _run(rpr, text, deleted=False):
    r = body.makeelement(qn('w:r'), {})
    if rpr is not None: r.append(copy.deepcopy(rpr))
    t = r.makeelement(qn('w:delText' if deleted else 'w:t'), {}); t.text = text; t.set(XS, 'preserve')
    r.append(t); return r

def _mark_para(p, kind):
    ppr = p.find(qn('w:pPr'))
    if ppr is None:
        ppr = p.makeelement(qn('w:pPr'), {}); p.insert(0, ppr)
    rpr = ppr.find(qn('w:rPr'))
    if rpr is None:
        rpr = ppr.makeelement(qn('w:rPr'), {}); ppr.append(rpr)
    rpr.insert(0, _rev(kind))

def _first_rpr(p):
    for r in p.iter(qn('w:r')):
        if r.find(qn('w:t')) is not None:
            return r.find(qn('w:rPr'))
    return None

def set_text(p, text, drop_math=True, keep_bold=False):
    """Tracked replacement of the paragraph's text: unchanged prefix/suffix stay plain."""
    old = N(T(p)); new = text
    rpr = _clean_rpr(_first_rpr(p), keep_bold)
    if drop_math:
        for m in list(p.iter('{%s}oMathPara' % M)) + list(p.iter('{%s}oMath' % M)):
            if m.getparent() is not None:
                m.getparent().remove(m)
    # common prefix/suffix at word level
    i = 0
    while i < min(len(old), len(new)) and old[i] == new[i]: i += 1
    while i > 0 and old[i - 1] != " " and i < len(old): i -= 1
    j = 0
    while j < min(len(old), len(new)) - i and old[-1 - j] == new[-1 - j]: j += 1
    while j > 0 and old[len(old) - j] != " " and j < len(old) - i: j -= 1
    pre, osub, nsub, suf = old[:i], old[i:len(old) - j], new[i:len(new) - j], old[len(old) - j:]
    for ch in list(p):
        if ch.tag in (qn('w:r'), qn('w:hyperlink'), qn('w:ins'), qn('w:del'), qn('w:smartTag')):
            p.remove(ch)
    if pre: p.append(_run(rpr, pre))
    if osub:
        dl = _rev('w:del'); dl.append(_run(rpr, osub, deleted=True)); p.append(dl)
    if nsub:
        ins = _rev('w:ins'); ins.append(_run(rpr, nsub)); p.append(ins)
    if suf: p.append(_run(rpr, suf))

def sub(p, old, new):
    full = N(T(p))
    assert N(old) in full, (old, full[:120])
    set_text(p, full.replace(N(old), new))

def rep(anchor, old, new):
    sub(one(anchor), old, new); log.append(f"sub: {old[:50]} -> {new[:50]}")

def clone_after(ref, tmpl, text, numbered=None, keep_bold=False):
    np_ = copy.deepcopy(tmpl)
    ppr = np_.find(qn('w:pPr'))
    if numbered is False and ppr is not None:
        n = ppr.find(qn('w:numPr'))
        if n is not None: ppr.remove(n)
        s = ppr.find(qn('w:pStyle'))
        if s is not None and s.get(qn('w:val')) in ('ListParagraph', 'ListBullet'):
            ppr.remove(s)
    rpr = _clean_rpr(_first_rpr(tmpl), keep_bold)
    for ch in list(np_):
        if ch.tag != qn('w:pPr'):
            np_.remove(ch)
    ppr = np_.find(qn('w:pPr'))
    if ppr is not None and ppr.find(qn('w:rPr')) is not None:
        for e in ppr.find(qn('w:rPr')).findall(qn('w:ins')) + ppr.find(qn('w:rPr')).findall(qn('w:del')):
            ppr.find(qn('w:rPr')).remove(e)
    ins = _rev('w:ins'); ins.append(_run(rpr, text)); np_.append(ins)
    _mark_para(np_, 'w:ins')
    ref.addnext(np_)
    return np_

def write_lines(first, lines, plain_tmpl, bullet_tmpl):
    """Tracked: first line replaces `first`'s text; the rest are inserted after it."""
    ln0 = lines[0][2:] if lines[0].startswith("- ") else lines[0]
    set_text(first, ln0)
    ref = first
    for ln in lines[1:]:
        isb = ln.startswith("- ")
        txt = ln[2:] if isb else ln
        tm = bullet_tmpl if isb else plain_tmpl
        ref = clone_after(ref, tm, txt, numbered=None if isb else False)
    return ref

def delete(p):
    """Tracked deletion of a whole paragraph (text and paragraph mark)."""
    if p.getparent() is None: return
    for r in list(p.iter(qn('w:r'))):
        if r.getparent().tag == qn('w:del'): continue
        for t in r.findall(qn('w:t')):
            t.tag = qn('w:delText')
        par = r.getparent(); idx = list(par).index(r)
        dl = _rev('w:del'); par.remove(r); dl.append(r); par.insert(idx, dl)
    _mark_para(p, 'w:del')

def cell_of(p):
    e = p
    while e is not None and e.tag != qn('w:tc'):
        e = e.getparent()
    return e

def set_cell(tc, text, fresh=False):
    ps = tc.findall(qn('w:p'))
    if fresh:  # cell in an inserted row: plain inserted text
        for p in ps[1:]: tc.remove(p)
        p = ps[0]; rpr = _clean_rpr(_first_rpr(p))
        for ch in list(p):
            if ch.tag != qn('w:pPr'): p.remove(ch)
        ins = _rev('w:ins'); ins.append(_run(rpr, text)); p.append(ins)
        return
    for p in ps[1:]:
        delete(p)
    set_text(ps[0], text)

def mark_row(tr, kind):
    trpr = tr.find(qn('w:trPr'))
    if trpr is None:
        trpr = tr.makeelement(qn('w:trPr'), {})
        tblpr = tr.find(qn('w:tblPrEx'))
        tr.insert(1 if tblpr is not None else 0, trpr)
    trpr.append(_rev(kind))

def rows_of(tbl):
    return tbl.findall(qn('w:tr'))

def cells(tr):
    return tr.findall(qn('w:tc'))

def ctext(tc):
    return N("".join(x.text or "" for x in tc.iter(qn('w:t'))))

def table_of(p):
    e = p
    while e is not None and e.tag != qn('w:tbl'):
        e = e.getparent()
    return e

def L(s):
    return [x for x in s.strip("\n").split("\n")]

# ---------------------------------------------------------------- resolve
R = {}
def res(key, anchor, **kw):
    R[key] = one(anchor, **kw)

res('t1_o7_c3', "Mediterranean LCOE 0.062 €/kWh, positive NPV and IRR")
res('t1_o7_c4', "slightly higher than the DoA LCOE target")
res('o5', "The representative 10 MW Mediterranean scenario achieved an estimated LCOE of approximately €62/MWh")
res('o7_l', "LCOE: approximately €62/MWh", exact=True)
res('o7_n', "NPV: approximately €8.9 million", exact=True)
res('o7_i', "IRR: approximately 10.6%", exact=True)
res('o7_p', "Payback period: approximately 8 years", exact=True)
res('o7_corr', "The corresponding LCOE values were approximately €96/MWh for the Baltic Sea and €139/MWh for the North Sea. The Mediterranean result was approximately 14.8%")
res('o7_diff', "The difference from the original target resulted mainly from")
res('o7_over', "Although the €54/MWh target was not fully reached, the final €62/MWh estimate")
res('o7_127', "approximately 127% improvement in average hinge tensile capacity;")
res('o8_bp', "Development of exploitation pathways and business planning")
res('o8_bm', "supported by a positive business case with an estimated LCOE of €62/MWh, NPV of €8.9 million and IRR of 10.6%")
res('d74_due', "Report on Economic Assessment")
# WP2
res('wp2_lead', "Guillaume Kegelart", exact=True)
res('wp2_sum', "The WP2 has completed most of the tasks except continue engagement with the advisory board.")
res('wp2_t24s', "Status: Completed:", exact=True, nth=0)  # first 'Status: Completed:' alone is Task 2.4 (line 758)
res('wp2_t24', "A technical stakeholder advisory board (SAB) was formed during the first reporting period")
res('wp2_o1', "In the subsequent period (M19–M36), discussions were held with SAB members")
res('wp2_dev', "Most of the technical tasks in WP2 have been completed, with no deviations observed")
# WP6 hinge
res('wp6_1998', "Increase in average FPV-connection tensile capacity from approximately 3.69 kN to 8.36 kN.")
res('wp6_2080', "Validation of the redesigned FPV connection, achieving an average tensile capacity of approximately 8.36 kN")
# WP7
res('wp7_note', "The assessment covered 27 cases, combining three deployment locations")
res('wp7_par', "The final Mediterranean LCOE of €62/MWh remained above the original project target")
res('wp7_ghg', "Across the assessed scenarios, offshore FPV achieved more than 90% lower greenhouse-gas emissions")
res('wp7_mmo', "Estimated Mediterranean LCOE of approximately €62/MWh, with an NPV of approximately €8.9 million")
res('wp7_sig', "The representative 10 MW Mediterranean case achieved the strongest economic performance, with an estimated LCOE of €62/MWh")
# WP8
res('wp8_from', "FROM:01.10.2022", exact=True)
res('wp8_s1', "The core focus of Work Package 8 (WP8) is to create effective strategies")
res('wp8_s2', "We are developing a master plan for dissemination, exploitation, and communication.")
res('wp8_s3', "To ensure broad and effective dissemination, we plan on producing")
res('wp8_s4', "Finally, we are working on exploitation pathways and a business plan")
res('wp8_s5', "In summary, WP8 is a comprehensive plan")
res('wp8_s6', "Since the start of the project, we have established a homepage")
res('wp8_s7', "Content has been produced for social media and the web at two-week intervals.")
res('wp8_p_first', "Objective 1 (O1): Raise Awareness and Inform about the Project")
res('wp8_p_last', "Maintained bi-weekly updates on LinkedIn and other platforms")
res('wp8_sig_first', "In the following the most relevant results which contribute to the project sub-objectives")
res('wp8_sig_last', "Stakeholder Workshops: Hosted a physical workshop in Oslo")
res('wp8_sig_b', "LinkedIn Engagement: Reached 500+ likes")
res('wp8_exp', "We are compiling all the exploitable results and update in M27")
res('wp8_devh', "Deviations", exact=True, nth=None) if False else None
devh = [p for p in PS if N(T(p)) == "Deviations"]
corh = [p for p in PS if N(T(p)) == "Corrective actions"]
wp8_start = one("Work Package 8 – DISSEMINATION, COMMUNICATION, EXPLOITATION & SOCIETAL ENGAGEMENT", nth=0) if False else one("1.2.2 Work Package 8 – DISSEMINATION")
i8 = PS.index(wp8_start)
R['wp8_devh'] = [p for p in devh if PS.index(p) > i8][0]
R['wp8_corh'] = [p for p in corh if PS.index(p) > i8][0]
R['wp8_dev'] = nxt(R['wp8_devh'])
R['wp8_cor'] = nxt(R['wp8_corh'])
res('pub_marine', "Date and place to be added")
res('pub_dcis', "DCIS 2023 Conference, Málaga, Spain, 2023. Exact dates to be added.")
res('pub_gef', "Revista de Mecánica de la Fractura (2024).")
res('pub_palwani', "Omar E. Godinez Brizuela, Balram Palwani")
res('pub_sensors', "Sensors, 24(13) (2024), 4211.")
res('etc', "Etc.", exact=True)
# 1.3
res('i_status', "Status: Largely achieved. SUREWAVE demonstrated a substantial reduction in the estimated LCOE")
res('i_148', "The Mediterranean result was approximately 14.8% above the original €54/MWh target:")
res('i_615', "However, compared with the original immature offshore-FPV reference of €161/MWh")
res('i_grid', "The Mediterranean LCOE of approximately €62/MWh assumes a short")
res('i_capex', "Mediterranean CAPEX was estimated at approximately €900/kWp")
res('i_fin', "The final techno-economic assessment estimated an LCOE of approximately €62/MWh")
res('i_b1', "is approximately 14.8% above the original target of €54/MWh;")
res('i_b2', "represents an indicative 61.5% reduction")
res('i_b3', "reaches the lower boundary of the €62–106/MWh range")
res('i_path', "The Mediterranean scenario demonstrated a credible commercial pathway, with an estimated NPV of €8.9 million")
res('i_diff', "The difference between the €62/MWh result and the €54/MWh target")
res('i_kl', "LCOE: approximately €62/MWh;", exact=True)
res('i_kn', "NPV: approximately €8.9 million;", exact=True)
res('i_ki', "IRR: approximately 10.6%; and", exact=True)
res('i_kp', "payback period: approximately 8 years.", exact=True)
res('i_kc', "The corresponding LCOE estimates were approximately €96/MWh for the Baltic Sea and €139/MWh for the North Sea. These results identify")
res('i_ach', "a Mediterranean 10 MW business case with an estimated LCOE of €62/MWh")
res('i_pub1', "at least six published journal articles and three peer-reviewed conference papers")
res('i_pub2', "Based on the currently confirmed publications, nine peer-reviewed papers")
res('i_pub3', "(10): MARIN (3); CEIT (5)")
res('i_h1', "The redesigned connection therefore achieved approximately 127% higher tensile capacity")
res('i_h2', "The redesigned hinge increased average tensile capacity from 3.69 kN to 8.36 kN")
res('i_h3', "a redesigned FPV hinge with approximately 127% higher tensile capacity")
res('i_h4', "an average tensile capacity of approximately 8.36 kN;", exact=True)
res('i_overall', "However, the project has established the technical design, economic calculations, priority market and exploitation framework required to pursue them.")
res('h14', "1.4 Update of the plan for exploitation and dissemination of results")
R['i_overall_h'] = [p for p in PS if N(T(p)) == "Overall Assessment" and PS.index(p) < PS.index(R['h14'])][-1]
# 1.4
res('x_first', "The initial exploitation strategy was refined from a broad system-level commercialisation concept")
res('x_cons', "For each result, the consortium is consolidating ownership")
res('x_med', "The final techno-economic assessment also refined the geographical commercialisation pathway.")
res('x_route', "The proposed route to market was consequently updated to:")
# 2, 4, 5
res('s2_act', "The consolidated record now includes six published peer-reviewed journal articles and three peer-reviewed conference papers")
res('s2_stat', "Largely addressed. Nine confirmed peer-reviewed publications")
res('s2_pre', "Five journal-style preprints were prepared from public project results: (1)")
res('s2_after1', "giving nine confirmed peer-reviewed publications")
res('s2_after2', "breakwater-layout and mooring design")
res('s4_item4', "Layout Selection and Mooring Design of a Floating Breakwater Sheltering", nth=1)
res('s4_count', "The project produced six published open-access peer-reviewed journal articles and three peer-reviewed conference papers")
res('s51_lcoe', "The final Mediterranean 10 MW base case reached approximately €62.2/MWh")
res('s51_pub', "Scientific-publication target", exact=True)

# sanity: Task 2.4 status line is the one right before the SAB paragraph
assert nxt(R['wp2_t24s']) is R['wp2_t24'], "Task 2.4 status anchor mismatch"
assert PS.index(R['i_overall_h']) < PS.index(R['h14'])

# ---------------------------------------------------------------- apply
def S(key, text): set_text(R[key], text); log.append(f"set {key}")

# Part A / 1.1
S('t1_o7_c3', "Mediterranean LCOE 0.076 €/kWh, positive NPV and IRR")
S('t1_o7_c4', "✅ Largely achieved: positive Mediterranean business case; LCOE about 41% above the DoA target of 0.054 €/kWh and within the SET Plan range for floating offshore wind")
sub(R['o5'], "€62/MWh", "€76/MWh")
S('o7_l', "LCOE: approximately €76/MWh")
S('o7_n', "NPV: approximately €7.3 million")
S('o7_i', "IRR: approximately 15.6%")
S('o7_p', "Payback period: approximately 10 years")
S('o7_corr', "The corresponding LCOE values were approximately €120/MWh for the Baltic Sea, at break-even, and €173/MWh for the North Sea, not viable at current costs. The Mediterranean result is about 41% above the original target of €54/MWh and within the €62–106/MWh SET Plan range cited in the Description of Action for floating offshore wind. Sites closer to shore in the Baltic and North Seas, with lower waves, lighter breakwaters and shorter export cables, may still be viable and are assessed site by site.")
set_text(R['o7_diff'], N(T(R['o7_diff'])) + " The final figures are from D7.4 version 2.0, which also includes end-of-life clean-up.")
sub(R['o7_over'], "the final €62/MWh estimate", "the final €76/MWh estimate")
S('o7_127', "redesign of the FPV hinge, with a design break load of 37 kN against 14 kN for the paired first-generation hinges;")
set_text(R['o8_bp'], N(T(R['o8_bp'])) + " D8.4 sets out a definitive business plan for the global solution, the integrated floating PV system with breakwater (KER1), prepared by Sunlit Sea with the Horizon Results Booster, and exploitation pathways and four-year action plans for the six other Key Exploitable Results.")
sub(R['o8_bm'], "an estimated LCOE of €62/MWh, NPV of €8.9 million and IRR of 10.6%", "an estimated LCOE of €76/MWh, NPV of €7.3 million and IRR of 15.6%")
# deliverables table D7.4 due date
tr = R['d74_due']
while tr.tag != qn('w:tr'): tr = tr.getparent()
cs = cells(tr)
for tc in cs:
    if ctext(tc) == "31 May 2026":
        set_cell(tc, "31 May 2025"); log.append("D7.4 due -> 31 May 2025")

# WP2
S('wp2_lead', "Eirik Larsen")
S('wp2_sum', "Tasks 2.1–2.3 were completed in the first reporting period, and their design basis was used throughout the second period in system design, modelling, testing and the sustainability and economic assessments. In the reporting period (M19–M48), Task 2.4 continued the engagement with the Stakeholder Advisory Board (SAB): an online SAB workshop on 19 November 2024 and a follow-up SAB meeting in March 2025 (M30). All WP2 tasks are completed.")
S('wp2_t24s', "Status: Completed.")
S('wp2_t24', "The technical Stakeholder Advisory Board (SAB) was established in the first reporting period (D2.4), with seven members from industry, finance, regulation and research; four of the seven member organisations are companies. In the first period, SAB input was gathered through questionnaires and interviews (D2.4). In the reporting period, the SAB workshop was held online on 19 November 2024 as an open lunch webinar, where project results were presented and the audience asked about cost, mismatch losses, environmental monitoring, the LCOE target and equipment on the breakwater; a follow-up SAB meeting was held in March 2025 (M30). SAB members also reviewed and extended the list of potential social impacts in D8.2. Their points on grid access, permitting, certification and insurability were used in the exploitation plan (D8.4).")
sub(R['wp2_o1'], "In the subsequent period (M19–M36), discussions were held with SAB members regarding the organization of a workshop aimed at disseminating project results. A follow-up meeting took place in M30, and preparations for a joint workshop are ongoing.",
    "In the reporting period (M19–M48), the SAB workshop was held online on 19 November 2024, a follow-up meeting in M30 (March 2025), and SAB members reviewed the social-impact list of D8.2. Their feedback was used in the societal, exploitation and dissemination work of WP8. Status: Fully achieved.")
# Objectives 2-4 status lines in WP2 Progress: the three 'Status: Completed:' after wp2_o1 and before WP3
i0 = PS.index(R['wp2_o1']); iw3 = PS.index(one("1.2.3 Work Package 3 – Development of the floating PV solution"))
for p in PS[i0:iw3]:
    if N(T(p)) == "Status: Completed:":
        set_text(p, "Status: Fully achieved (completed in the first reporting period)."); log.append("WP2 obj status")
S('wp2_dev', "All WP2 tasks were completed. No deviations occurred in the reporting period (M19–M48).")

# WP6 hinge
S('wp6_1998', "Redesign of the FPV connection as a full-edge hinge: a one-fifth segment reached 8.36 kN with a steel rod and 2.04 kN with the rope, which D6.3 scales to about 10 kN for the full connection with the rope.")
sub(R['wp6_2080'], "achieving an average tensile capacity of approximately 8.36 kN", "achieving an average tensile capacity of approximately 8.36 kN for a one-fifth segment with a steel rod (2.04 kN with the rope; about 10 kN scaled to the full connection with the rope)")

# WP7
clone_after(R['wp7_note'], R['wp7_note'], "The results below are from D7.4 version 2.0 (20 November 2026), revised in reply to the Project Officer's request of 16 October 2026. Version 2.0 adds end-of-life clean-up and the scope and system boundary, and corrects errors in version 1.0 with a rebuilt cost model, checked against a separate implementation with automated tests. For the Mediterranean 10 MW case the LCOE rises from €62 to €76/MWh and the NPV falls from €8.9 million to €7.3 million; the IRR rises from 10.7% to 15.6% because version 1.0 calculated it on discounted cash flows over 25 years and version 2.0 on undiscounted cash flows over the 50-year life.", numbered=False)
sub(R['wp7_par'], N("The final Mediterranean LCOE of €62/MWh remained above the original project target of €54/MWh, but demonstrated a credible route towards competitive offshore FPV in favourable locations."),
    "The final Mediterranean LCOE of €76/MWh is above the original project target of €54/MWh and within the €62–106/MWh SET Plan range for floating offshore wind cited in the DoA, which gives a viable business case for the Mediterranean.")
sub(R['wp7_ghg'], "with an estimated LCOE of €62/MWh and an IRR of approximately 10.7%", "with an estimated LCOE of €76/MWh and an IRR of 15.6% (D7.4 version 2.0)")
S('wp7_mmo', "Estimated Mediterranean LCOE of approximately €76/MWh, with an NPV of approximately €7.3 million and an IRR of 15.6% for the representative 10 MW base case (D7.4 version 2.0).")
S('wp7_sig', "The representative 10 MW Mediterranean case achieved the strongest economic performance, with an estimated LCOE of €76/MWh, NPV of €7.3 million, IRR of 15.6% and a 10-year payback period.")

# result tables (WP7 5-col, 1.3 6-col)
newrows = {
    "Mediterranean Sea": ["€76/MWh", "€7.3 million", "15.6%", "10 years", "Economically attractive"],
    "Baltic Sea": ["€120/MWh", "About €0 (break-even)", "8.5%", "Not reached", "At break-even; viable with favourable financing or at nearshore sites"],
    "North Sea": ["€173/MWh", "−€5.8 million", "3.4%", "Not reached", "Not viable as a stand-alone base case; viable only at discount rates of 3% or lower"],
}
ntab = 0
for tbl in body.iter(qn('w:tbl')):
    rs = rows_of(tbl)
    if not any("€96/MWh" in ctext(c) for r in rs for c in cells(r)):
        continue
    hit = False
    for r in rs:
        cs = cells(r)
        k = ctext(cs[0]) if cs else ""
        if k in newrows and any("€" in ctext(c) for c in cs[1:2]):
            hit = True
            vals = newrows[k]
            for j, tc in enumerate(cs[1:]):
                set_cell(tc, vals[j])
    ntab += hit
assert ntab == 2, ntab
log.append("result tables: 2")

# WP8
S('wp8_from', "FROM:01.04.2024")
summary = L("""Work Package 8 (WP8), led by Sunlit Sea, covers dissemination, communication, exploitation and societal engagement.
Work carried out in the reporting period (M19–M48):
- Dissemination: the publications grew to ten, six journal articles and four conference papers, on breakwater aerodynamics, wave-basin testing, farm-scale hydrodynamics, corrosion sensing, wireless monitoring and fatigue-crack modelling.
- Events: the CINEA Solar PV clustering event (April 2024), the online Stakeholder Advisory Board workshop (November 2024), the joint SUREWAVE/NaturSea-PV webinar (February 2026) and the final workshop on sustainable concrete for marine applications (30 September 2026).
- Communication: the website, the LinkedIn page, videos and webinar recordings, interviews, articles in specialist and regional media, and the press release on the Port of Gijón prototype (October 2024).
- Societal engagement (Task 8.1, led by IFEU): societal needs and a SWOT analysis with the SAB and the partners, reported in D8.2.
- Technical brochure (D8.3), written by Sunlit Sea and SINTEF.
- Exploitation (Task 8.4): seven Key Exploitable Results (KERs), one anchored in each beneficiary, with owners, protection, exploitation routes and four-year action plans, and a definitive business plan for the integrated system (KER1), prepared by Sunlit Sea with the Horizon Results Booster (D8.4).
At 24 November 2026, 21 of the 21 output targets for dissemination and communication are met, counting the newsletters, the infographic and the LinkedIn posts that are written and scheduled for publication by the end of 2026.""")
btmpl = copy.deepcopy(R['wp8_sig_b'])
ptmpl = copy.deepcopy(R['wp8_s1'])
for k in ('wp8_s2', 'wp8_s3', 'wp8_s4', 'wp8_s5'):
    delete(R[k])
write_lines(R['wp8_s1'], summary, ptmpl, btmpl)
set_text(R['wp8_s6'], "")
delete(R['wp8_s7'])

progress = L("""Objective 1 (O1): Raise awareness and inform about the project, its results and potential benefits to industry and society
Over the project, partners presented SUREWAVE at 14 conferences and in 15 presentations, and at web events and joint events with other EU projects. The website passed 50,000 visits, the LinkedIn page has 694 followers, and the project appeared in seven journalistic articles, two press releases, nine interviews and seven videos and webinar recordings. The awareness targets are met (table of targets and actuals below).
Status: Fully achieved.
Objective 2 (O2): Disseminate project results in appropriate and impactful channels
The Dissemination, Exploitation and Communication Master Plan (D8.1, revised as D8.5 at M18) set the channels and targets. In the reporting period, dissemination moved from awareness to validated results: ten publications against a target of ten, of which seven state peer review, five preprints, public deliverables and datasets in the SUREWAVE Zenodo community, and the technical brochure (D8.3). Five of the seven peer-reviewed papers were deposited in an open repository after publication rather than at publication (see Deviations).
Status: Achieved.
Objective 3 (O3): Identify and engage with critical stakeholders from industry, research, certification bodies, media
The Stakeholder Advisory Board (WP2, Task 2.4) took part in the online workshop of 19 November 2024 and a follow-up meeting in March 2025. Societal stakeholders were engaged through the Task 8.1 needs assessment and SWOT analysis (D8.2); industry, research and media audiences through conferences, the final workshop of 30 September 2026, the joint webinar with NaturSea-PV, the CINEA clustering event and interviews.
Status: Fully achieved.
Objective 4 (O4): Develop exploitation strategies to ensure that the project will have a long-lasting impact
D8.4 maps the 27 results reported by the partners: 23 fall under seven Key Exploitable Results (KERs), one anchored in each beneficiary, and four are reported as impact. The KERs are KER1 integrated floating PV system with breakwater (Sunlit Sea), KER2 circular concrete formulations (ACCIONA), KER3 floating breakwater design (Clement Germany), KER4 modelling and testing methods (SINTEF), KER5 hydrodynamic models and basin testing (MARIN and SINTEF), KER6 structural health monitoring and eddy-current sensing (Ceit) and KER7 integrated sustainability assessment (IFEU). KER1 has a definitive business plan; KERs 2–7 have exploitation pathways, dated four-year action plans with indicators, their roles in KER1 and their protection positions. Results are carried forward in SuRE and MariSol (Sunlit Sea), in CIRCWIND and SFI BLUES (SINTEF), and in an EIC Transition proposal submitted on 16 September 2026 by SINTEF, Sunlit Sea, Clement Germany and EDP.
Status: Fully achieved.
Task 8.1: Societal Engagement (L: IFEU; Participants: All)
IFEU identified the societal stakeholders and led the needs assessment and SWOT analysis with the SAB and the project partners, covering compatibility with other sea uses and spatial planning. The results are reported in D8.2 and were used in the social and integrated sustainability assessments (D7.5, D7.6) and in the exploitation plan.
Task 8.2: Dissemination, Exploitation and Communication Strategy, and Monitoring of its Implementation (L: SIS; Participants: All)
The M18 revision of the master plan (D8.5) reviewed progress against the key performance indicators and set the plan for the second period. Website traffic was monitored with Matomo and the LinkedIn page through its own statistics. The definitive KERs were set through a written input round: the WP8 lead proposed seven candidate KERs in a template sent to the partners on 29 September 2026, all seven beneficiaries replied with written exploitation summaries, and the WP8 lead screened and mapped the results. In September–November 2026, the WP8 lead collected the partners' dissemination records and checked each indicator against publisher records, Crossref, OpenAIRE, Zenodo, the website and the LinkedIn page.
Task 8.3: Dissemination Activities (L: SIS; P: All)
Subtask 8.3.1: ten publications (six journal articles and four conference papers; table below), five preprints and two submitted journal manuscripts. Partners presented at 14 conferences, among them Floating Solar in Europe, MARINE 2025, the congresses of the Spanish Fracture Group (GEF) in 2024 and 2025 and the LCA Discussion Forums in Wädenswil.
Subtask 8.3.2: the technical brochure (D8.3) for industry stakeholders presents the system concept, materials, modelling, testing, monitoring, sustainability and economic results, the Key Exploitable Results and the remaining development needs. It was written by Sunlit Sea and SINTEF and reviewed by Clement Germany and MARIN.
Task 8.4: Exploitation Pathways and Business Plan (L: SIS; P: All)
D8.4 applies the proposal's five-step method: identification of results and IPR management under the IPR management plans (D1.4, D1.8); evaluation of business potential; business models; IPR analysis; and business and exploitation plans. It gives a definitive business plan for the integrated system (KER1), the roles, agreement types and fair-price logic for the results that feed into KER1, and each partner's exploitation pathway and four-year action plan. Sunlit Sea prepared the KER1 plan in the Horizon Results Booster Go-to-Market service from October 2026, with canvases, a risk map, the Business Opportunity Self-Assessment Tool (BOSAT), a business plan and a financial plan; at the Booster review of 13 November 2026 the expert asked for no major changes.
Task 8.5: Communication Activities (L: SIS; Participants: All)
Communication followed the master plan: the website, the LinkedIn page (694 followers; 34 posts by 18 November 2026 and six more scheduled to 29 December 2026), seven videos and webinar recordings, nine interviews, seven journalistic articles, two press releases (project start, 1 November 2022; Port of Gijón prototype, 11 October 2024), five newsletters (two published in 2023, three written and scheduled for November–December 2026), six infographics (five published, one scheduled for 15 December 2026), three factsheets, a flyer and a roll-up.""")
i_a, i_b = PS.index(R['wp8_p_first']), PS.index(R['wp8_p_last'])
ptm = copy.deepcopy(R['wp8_p_first'])
for p in PS[i_a + 1:i_b + 1]:
    if cell_of(p) is cell_of(R['wp8_p_first']):
        delete(p)
write_lines(R['wp8_p_first'], progress, ptm, btmpl)

sig = L("""- Ten publications against a target of ten: six journal articles and four conference papers, of which seven state peer review, on breakwater aerodynamics, wave-basin validation, farm-scale hydrodynamics, corrosion sensing, wireless monitoring and fatigue-crack modelling; plus five preprints.
- The output targets for dissemination and communication met, among them 694 LinkedIn followers (target more than 500) and more than 50,000 website visits (target more than 36,000).
- The technical brochure (D8.3) for industry stakeholders.
- Seven Key Exploitable Results with owners, protection positions, exploitation routes and four-year action plans, and a definitive business plan for the integrated system (D8.4), prepared with the Horizon Results Booster.
- SUREWAVE results carried into SuRE, MariSol, CIRCWIND, SFI BLUES and an EIC Transition proposal.""")
sig_intro = N(T(R['wp8_sig_first']))
i_a, i_b = PS.index(R['wp8_sig_first']), PS.index(R['wp8_sig_last'])
stm = copy.deepcopy(R['wp8_sig_first'])
for p in PS[i_a + 1:i_b + 1]:
    delete(p)
write_lines(R['wp8_sig_first'], [sig_intro] + sig, stm, btmpl)

write_lines(R['wp8_exp'], ["The exploitation of all project results is set out in D8.4. Sunlit Sea exploits the integrated system (KER1) through CONNECT, its second-generation floating platform, at sheltered coastal sites first, with breakwater protection on the exposed side of sites that need it, and with the open-sea ring-breakwater plant as the long-term configuration. The other partners exploit their results (KER2–KER7) through their own products, services and research. The technical brochure, the public deliverables and the SUREWAVE Zenodo community serve as reference material after the project. Sunlit Sea enters KER1 on the Horizon Results Platform in Q1 2027."], copy.deepcopy(R['wp8_exp']), btmpl)

dev = L("""- Open access: the Grant Agreement asks for deposit of peer-reviewed publications in a trusted repository at publication. Of the seven papers with stated peer review, one met this (Sensors 24(13) 4211, PubMed Central); five are deposited on Zenodo after publication (one done, four in progress); the MARINE 2025 paper is open under CC BY-NC-SA 3.0, which does not meet the licence requirement.
- Reach and impact targets: of 22 targets in the Grant Agreement and D8.5, 18 are met, two partly met (more than 140 citations: 41 in Crossref; final conference with more than 100 stakeholders: 27 guests invited to the final workshop, open to a wider audience) and two not met (a new PhD completed within the project; a separate sustainability and replication guide, whose content is covered by D7.6, D8.3 and D8.4).""")
cor = L("""- Open access: the partners deposit the four MDPI papers (CC BY 4.0) in the SUREWAVE Zenodo community; MARIN deposits the accepted manuscript of the MARINE 2025 paper under CC BY if its publishing agreement with CIMNE allows it.
- Reach: communication continues after the project through the LinkedIn page, the website and partner channels.""")
write_lines(R['wp8_dev'], dev, copy.deepcopy(R['wp8_dev']), btmpl)
cor_tbl = table_of(R['wp8_cor'])
write_lines(R['wp8_cor'], cor, copy.deepcopy(R['wp8_cor']), btmpl)

# publications table
pub_tbl = table_of(R['pub_sensors'])
sub(R['pub_palwani'], "Palwani", "Panjwani")
sub(R['pub_marine'], "Date and place to be added.", "23 June 2025, Edinburgh, United Kingdom. DOI: 10.23967/marine.2025.163.")
S('pub_dcis', "DCIS 2023 Conference, Málaga, Spain, November 2023 (poster).")
sub(R['pub_gef'], "Revista de Mecánica de la Fractura (2024).", "Revista Española de Mecánica de la Fractura 8 (2024), 87–92.")
tmpl_row = R['pub_sensors']
while tmpl_row.tag != qn('w:tr'): tmpl_row = tmpl_row.getparent()
anchor_row = R['pub_palwani']
while anchor_row.tag != qn('w:tr'): anchor_row = anchor_row.getparent()
new_pubs = [
    ["AJ", "U. Eibar; A. Dorronsoro; J.M. Martínez-Esnaola (CEIT)", "Fatigue & Fracture of Engineering Materials & Structures, 49(11) (2026), 5081–5098. DOI: 10.1111/ffe.70435.", "Numerical Generation of Mode I Stress Intensity Factors for Narrow Elliptical Cracks in Round Bars"],
    ["AJ", "M. Losada et al. (CEIT, MARIN)", "Electronics, 13(22) (2024), 4485. DOI: 10.3390/electronics13224485.", "UWB-Based Accelerometer Sensor Nodes for Low-Power Applications in Offshore Platforms"],
    ["COC", "U. Eibar; A. Dorronsoro; D. González; J. Alkorta; J.M. Martínez-Esnaola (CEIT)", "Revista Española de Mecánica de la Fractura 9 (2025), p. 15. 41 Congreso del Grupo Español de Fractura, 26–28 March 2025, Vitoria-Gasteiz, Spain.", "Generation of Mode I Stress Intensity Factor Solutions for Narrow Elliptical-Shaped Cracks in Round Bars: A Finite Element Approach"],
]
for vals in new_pubs:
    nr = copy.deepcopy(tmpl_row)
    for tc, v in zip(cells(nr), vals):
        set_cell(tc, v, fresh=True)
    mark_row(nr, 'w:ins')
    anchor_row.addprevious(nr)
log.append("3 publication rows")
delete(R['etc'])

# targets-and-actuals table: copy of publications table with header + rows
kt = copy.deepcopy(pub_tbl)
krs = rows_of(kt)
hdr, body_row = krs[0], krs[1]
for r in krs[2:]:
    kt.remove(r)
kt.remove(body_row)
for tc, v in zip(cells(hdr), ["Indicator", "Target", "Source of target", "Achieved (24 November 2026)"]):
    set_cell(tc, v, fresh=True)
mark_row(hdr, 'w:ins')
kpi = [
    ("Scientific publications", "10", "GA", "10 (6 journal articles, 4 conference papers; 7 state peer review)"),
    ("Conferences", "5", "WP8", "14"),
    ("Presentations", "More than 10", "GA", "15"),
    ("Posters", "1", "WP8", "3"),
    ("Web events", "2", "WP8", "4"),
    ("Joint events with other EU projects", "More than 2", "GA", "3"),
    ("Conference workshops", "3", "GA, D8.5", "3"),
    ("Stakeholder Advisory Board workshops and meetings", "2", "D8.5", "2"),
    ("Newsletters", "5", "D8.5", "5 (2 published; 3 written, scheduled 24 Nov – 8 Dec 2026)"),
    ("Journalistic articles", "6", "GA", "7"),
    ("Press releases", "At the start and at milestones", "GA", "2"),
    ("Interviews", "9", "GA", "9"),
    ("Videos", "An introduction and a final summary", "GA", "7"),
    ("Infographics", "6", "GA", "6 (5 published; 1 scheduled 15 Dec 2026)"),
    ("Factsheets", "3", "GA", "3"),
    ("Flyers", "1", "GA", "1"),
    ("Roll-ups", "1", "WP8", "1"),
    ("Technical brochure", "1", "GA", "1 (D8.3)"),
    ("LinkedIn followers", "More than 500", "GA", "694"),
    ("LinkedIn posts", "25", "WP8", "34 (6 more scheduled to 29 Dec 2026)"),
    ("Website visits", "More than 36,000", "GA", "More than 50,000"),
]
for row in kpi:
    nr = copy.deepcopy(body_row)
    for tc, v in zip(cells(nr), row):
        set_cell(tc, v, fresh=True)
    mark_row(nr, 'w:ins')
    kt.append(nr)
head = clone_after(cor_tbl, R['wp8_corh'], "Dissemination and communication: targets and actuals", numbered=False, keep_bold=True)
head.getparent().remove(head)
note_p = clone_after(cor_tbl, ptmpl, "GA = Grant Agreement, Annex 1; D8.5 = master plan at M18; WP8 = the WP8 lead's monitoring targets for indicators that the GA and D8.5 name without a number. Items are counted over the whole project. Preprints (5) and submitted journal manuscripts (2) are reported separately from the publications. The reach and impact targets are listed under Deviations.", numbered=False)
note_p.getparent().remove(note_p)
cor_tbl.addnext(head)
head.addnext(kt)
kt.addnext(note_p)
log.append("KPI table inserted")

# 1.3 Impact
sub(R['i_status'], N("The original project target of €54/MWh was not fully reached, but the final Mediterranean estimate of €62/MWh is within the €62–106/MWh SET Plan range for floating offshore wind cited in the DoA."),
    "The original project target of €54/MWh was not reached; the final Mediterranean estimate of €76/MWh is within the €62–106/MWh SET Plan range for floating offshore wind cited in the DoA.")
S('i_148', "The Mediterranean result was approximately 41% above the original €54/MWh target: (76 − 54)/54 × 100 ≈ 41%.")
S('i_615', "However, compared with the original immature offshore-FPV reference of €161/MWh, it represents an indicative reduction of approximately 53%: (161 − 76)/161 × 100 ≈ 53%.")
for key in ('i_148', 'i_615'):  # remove the equation paragraphs that follow
    q = nxt(R[key])
    ms = list(q.iter('{%s}oMathPara' % M)) + list(q.iter('{%s}oMath' % M))
    if N(T(q)) == "" and ms:
        for m in ms:
            if m.getparent() is not None: m.getparent().remove(m)
        delete(q); log.append("equation removed")
S('i_grid', "The Mediterranean LCOE of approximately €76/MWh assumes a short, approximately 300 m floating-cable connection to nearby offshore infrastructure. A dedicated submarine export cable to shore (11 km) increases the Mediterranean LCOE to approximately €89/MWh and reduces the IRR from 15.6% to 12.6%. For the assessed North Sea case, 170 km from shore, the export cable increases the LCOE to more than €480/MWh.")
sub(R['i_capex'], "approximately €900/kWp", "approximately €940/kWp")
sub(R['i_fin'], "€62/MWh", "€76/MWh")
S('i_b1', "is approximately 41% above the original target of €54/MWh;")
S('i_b2', "represents an indicative 53% reduction from the DoA's immature offshore-FPV reference of €161/MWh; and")
S('i_b3', "is within the €62–106/MWh range for floating offshore wind cited in the DoA.")
S('i_path', "The Mediterranean scenario demonstrated a credible commercial pathway, with an estimated NPV of €7.3 million, IRR of 15.6% and payback period of ten years. The corresponding LCOE estimates were approximately €120/MWh for the Baltic Sea and €173/MWh for the North Sea. The Baltic case is at break-even at the 8.5% discount rate, while stand-alone North Sea deployment is not economically viable under the base assumptions.")
sub(R['i_diff'], N("The difference between the €62/MWh result and the €54/MWh target reflects the use of more detailed and conservative assumptions for CAPEX, O&M, component replacement, decommissioning and financing."),
    "The difference between the €76/MWh result and the €54/MWh target reflects more detailed assumptions for CAPEX, O&M, component replacement, decommissioning, end-of-life clean-up and financing.")
S('i_kl', "LCOE: approximately €76/MWh;")
S('i_kn', "NPV: approximately €7.3 million;")
S('i_ki', "IRR: approximately 15.6%; and")
S('i_kp', "payback period: approximately 10 years.")
sub(R['i_kc'], "€96/MWh for the Baltic Sea and €139/MWh", "€120/MWh for the Baltic Sea and €173/MWh")
S('i_ach', "a Mediterranean 10 MW business case with an estimated LCOE of €76/MWh, NPV of €7.3 million, IRR of approximately 15.6% and a ten-year payback period;")
S('i_pub1', "The DoA target was 10 peer-reviewed publications or papers. By the end of the project, the consortium had published six journal articles and four conference papers, ten publications against the target of ten, seven of them with stated peer review, together with further conference contributions, five preprints and two submitted journal manuscripts.")
S('i_pub2', "Ten publications count towards the DoA target of ten, which is achieved.")
S('i_pub3', "(10): MARIN (3); CEIT (6); SINTEF (1), by lead partner")
S('i_h1', "The redesigned full-edge connection was tested as a one-fifth segment: 8.36 kN with a steel rod and 2.04 kN with the rope, which D6.3 scales to about 10 kN for the full connection with the rope. Its design break load is 37 kN, against 14 kN for the paired first-generation hinges (D7.2). In the second wave-basin campaign, the longer and thicker paired hinges showed no measurable buckling or snap loading under the tested conditions.")
S('i_h2', "The redesigned full-edge hinge has a design break load of 37 kN, against 14 kN for the paired first-generation hinges (D7.2).")
S('i_h3', "a redesigned FPV hinge with a design break load of 37 kN against 14 kN for the paired first-generation hinges, improved compression resistance, and no measurable buckling or snap loading of the paired hinges in the second wave-basin campaign;")
S('i_h4', "an average tensile capacity of approximately 8.36 kN for a one-fifth segment with a steel rod (about 10 kN scaled to the full connection with the rope);")

# SME subsection before 1.4 heading
sme = L("""Impact on SMEs
Three of the seven beneficiaries are SMEs: Sunlit Sea, Clement Germany and IFEU.
- Sunlit Sea, the floating PV company in the consortium, designed the floating PV array and the global system in SUREWAVE and led the economic assessment (D7.4). The connection tests showed that its first-generation hinge was too weak; Sunlit Sea redesigned it as a hinge along the full edge of the float, with a design break load of 37 kN against 14 kN for the earlier paired hinges (D7.2), and started the redesign of its float into CONNECT, its second-generation platform, which it continues in the parallel Horizon Europe project SuRE. CONNECT goes into Sunlit Sea's first Norwegian reference plants from 2027 and is sold as a kit from 2028; the integrated system with breakwater (KER1) is Sunlit Sea's main commercial result.
- Clement Germany extended its floating breakwater, mooring and anchoring design to the protection of floating PV arrays (KER3), which adds floating PV to its markets for floating concrete structures.
- IFEU applied its integrated life-cycle sustainability assessment to offshore floating PV (KER7) and reuses the method in grant-funded and commissioned studies.
For SMEs outside the consortium, the public deliverables, the design basis and the economic assessment and its cost model are open on Zenodo, so a small developer or supplier can screen sites and test a business case from them. The modular 2 MW architecture divides assembly, installation and maintenance into work packages of a size that regional marine contractors can take on.""")
ref = R['i_overall']
bul13 = R['i_b1']
for k, ln in enumerate(sme):
    if k == 0:
        ref = clone_after(ref, R['i_overall_h'], ln, numbered=False, keep_bold=True)
        continue
    isb = ln.startswith("- ")
    ref = clone_after(ref, bul13 if isb else R['i_overall'], ln[2:] if isb else ln, numbered=None if isb else False)
log.append("SME subsection")

# 1.4
kers = L("""The initial exploitation strategy was refined from a broad system-level commercialisation concept into seven Key Exploitable Results (KERs), one anchored in each beneficiary (D8.4):
- KER1 integrated floating PV system with breakwater (Sunlit Sea), the proposal's global solution, including the redesigned FPV hinge;
- KER2 circular concrete formulations: HPC, LWAC and cellular lightweight concrete (ACCIONA);
- KER3 floating breakwater design, with mooring, anchoring, connections and transition element (Clement Germany);
- KER4 modelling and testing methods, including the aerodynamic wind-load method, connection testing and the Surewave-ANN concrete-property tool (SINTEF);
- KER5 hydrodynamic models and basin testing (MARIN and SINTEF);
- KER6 structural health monitoring and eddy-current sensing, including the Structural Health Management System (Ceit); and
- KER7 integrated sustainability assessment (IFEU).
For each KER, D8.4 gives the owner, maturity, exploitation route, protection, role in the integrated system and a four-year action plan with indicators. The principal exploitation routes are product sales and project delivery (KER1), use in the owners' projects and services, engineering and consultancy, software licences and testing services, contract research and follow-on projects.""")
i_a, i_b = PS.index(R['x_first']), PS.index(R['x_cons'])
xb = copy.deepcopy(PS[i_a + 1])
xp = copy.deepcopy(R['x_first'])
for p in PS[i_a + 1:i_b + 1]:
    delete(p)
write_lines(R['x_first'], kers, xp, xb)
sub(R['x_med'], N("The Mediterranean was identified as the preferred market for initial demonstration and deployment, with an estimated LCOE of approximately €62/MWh, NPV of €8.9 million, IRR of 10.6%, and payback period of approximately eight years for the representative 10 MW case."),
    "For the open-sea plant, the Mediterranean was identified as the preferred market, with an estimated LCOE of approximately €76/MWh, NPV of €7.3 million, IRR of 15.6%, and payback period of approximately ten years for the representative 10 MW case.")
route = [
    "Sunlit Sea's second-generation floating platform, CONNECT, goes into its first Norwegian reference plants at sheltered coastal sites from 2027, to build the operating record that buyers and lenders ask for, and is sold as a kit from 2028;",
    "at exposed nearshore sites, a breakwater on the exposed side only, in classes sized from the SUREWAVE breakwater, with a field demonstrator in 2028–2030 if the EIC Transition proposal is funded, and the first commercial site with a breakwater after it;",
    "further qualification and certification of the critical components, in particular the FPV hinge for harsh conditions;",
    "partnerships with project developers, utilities and offshore-infrastructure owners;",
    "a kW- to low-MW open-sea demonstrator, with a pilot proposal about 2031; and",
    "commercial open-sea plants with ring breakwater from about 2035, first in favourable Mediterranean locations.",
]
set_text(R['x_route'], "The route to market for the integrated system was updated in the definitive business plan (D8.4):")
items = PS[PS.index(R['x_route']) + 1: PS.index(R['x_route']) + 7]
for p, t in zip(items, route):
    set_text(p, t)
log.append("1.4 route")

# Section 2
sub(R['s2_act'], "six published peer-reviewed journal articles and three peer-reviewed conference papers", "six published peer-reviewed journal articles and four conference papers")
S('s2_stat', "Addressed. Ten publications count towards the DoA target of 10: six journal articles and four conference papers, seven of them with stated peer review. The two submitted manuscripts and five preprints are reported separately.")
full = N(T(R['s2_pre']))
a = full.index("(1) Technological Risk Assessment"); b = full.index("economic assessment.") + len("economic assessment.")
set_text(R['s2_pre'], full[:a] + "(1) Technological Risk Assessment of a Breakwater-Protected Offshore Floating Photovoltaic System Across Three European Sea Basins (doi.org/10.20944/preprints202611.1173.v1); (2) Experimental Characterization of Critical Connections in an Offshore Floating Photovoltaic System (doi.org/10.20944/preprints202611.1612.v1); (3) Marine Exposure Performance of a Circular-Concrete Floating Breakwater Prototype: Biofouling, Chloride Ingress and Structural Monitoring (doi.org/10.20944/preprints202611.1592.v1); (4) Numerical Simulation of the Dynamics of Modular Moored Keeled Breakwater Structures for the Shielding of Floating Photovoltaic Installations (doi.org/10.20944/preprints202610.0011.v2); and (5) Economic Assessment of Breakwater-Protected Offshore Floating Photovoltaics Across Three European Sea Basins (doi.org/10.20944/preprints202611.2292.v1)." + full[b:])
sub(R['s2_after1'], N("six peer-reviewed journal articles and three peer-reviewed conference papers had been published, giving nine confirmed peer-reviewed publications against the DoA target of ten."),
    "six peer-reviewed journal articles and four conference papers had been published, giving ten publications against the DoA target of ten.")
sub(R['s2_after2'], "breakwater-layout and mooring design", "the dynamics of modular moored breakwater structures")
# Section 4
S('s4_item4', "Numerical Simulation of the Dynamics of Modular Moored Keeled Breakwater Structures for the Shielding of Floating Photovoltaic Installations: https://doi.org/10.20944/preprints202610.0011.v2")
sub(R['s4_count'], "and three peer-reviewed conference papers", "and four conference papers")
# Section 5.1
sub(R['s51_lcoe'], N("approximately €62.2/MWh, around 15% above the target, based on more detailed and conservative cost and financing assumptions."),
    "approximately €76/MWh, around 41% above the target, based on more detailed cost and financing assumptions, end-of-life clean-up and the corrected cost model of D7.4 version 2.0.")
row = R['s51_pub']
while row.tag != qn('w:tr'): row = row.getparent()
for p in list(row.iter(qn('w:p'))):
    delete(p)
mark_row(row, 'w:del')
log.append("5.1 publication row deleted")

W14 = "http://schemas.microsoft.com/office/word/2010/wordml"
seen = set()
for e in body.iter(qn('w:p'), qn('w:tr')):
    for at in ("{%s}paraId" % W14, "{%s}textId" % W14):
        v = e.get(at)
        if v is None: continue
        if (at, v) in seen: del e.attrib[at]
        else: seen.add((at, v))
d.save(out)
print("\n".join(log))
print("OK", len(log))
