"""Generate the SUREWAVE modelling-toolchain diagram as SVG and as TikZ.

One definition of boxes and arrows (below) produces two text-based vector
files, so the web/LinkedIn figure (SVG) and the PDF figure (TikZ, rendered
natively by xelatex without an SVG converter) can never drift apart.

Usage:
    python scripts/toolchain_figure.py <out_stem>

Writes <out_stem>.svg and <out_stem>.tikz.tex. Standard library only.
Built for T159 (SUREWAVE WP8 modelling toolchain infographic); box contents
verified against D2.1, D2.3, D5.1, D5.3-D5.7 and the Annex 1 results R6-R10.
"""
import sys
from xml.sax.saxutils import escape

W, H = 1000, 640          # canvas units; 1 unit = 0.182 mm on the A4 page
BW, BH = 180, 165         # standard box
COLS = [10, 210, 410, 610, 810]
ROWS = [20, 240, 460]

GAPS = {"use": 7, "valid": 46}   # gap between items in left-aligned panels

TITLE_FS, BODY_FS, FOOT_FS = 15.5, 13, 12
TITLE_LH, BODY_LH, FOOT_LH = 17.5, 15.5, 13.5

STYLES = {
    #        fill       stroke     title      body       foot
    "input": ("#E6EEF4", "#1F5373", "#1F5373", "#333333", "#1F5373"),
    "hydro": ("#DFF1F3", "#2E8F9C", "#1B545C", "#333333", "#1B545C"),
    "struct": ("#EAF2DF", "#7E9F4C", "#3F5A1E", "#333333", "#3F5A1E"),
    "monit": ("#FBF1D6", "#C89207", "#7A5600", "#333333", "#7A5600"),
    "shms": ("#DDEDE6", "#4F8A73", "#24543F", "#333333", "#24543F"),
    "use": ("#1F5373", "#1F5373", "#FFFFFF", "#FFFFFF", "#FFFFFF"),
    "valid": ("#F3F5F7", "#808080", "#1F5373", "#333333", "#1F5373"),
}

# id: (x, y, w, h, style, title lines, body lines, footer lines, align)
# Footers carry the developing partner only; deliverable numbers are in the
# tool list on the page.
BOXES = {
    "A": (COLS[0], ROWS[0], BW, BH, "input",
          ["Site conditions", "and load cases"],
          ["Three sea sites;", "25 years of ERA5 wind", "and wave hindcast;", "design load cases"],
          ["SINTEF · Sunlit Sea"], "c"),
    "C": (COLS[1], ROWS[0], BW, BH, "hydro",
          ["Coupled aero-", "hydrodynamics"],
          ["Diffraction and time-", "domain models; CFD for", "damping and wind loads"],
          ["MARIN · SINTEF"], "c"),
    "D": (COLS[2], ROWS[0], BW, BH, "hydro",
          ["Mooring", "optimisation"],
          ["Surrogate models and", "genetic algorithm; up to", "56 % less mooring mass", "in selected cases"],
          ["MARIN"], "c"),
    "U": (COLS[3], ROWS[0], 2 * BW + 20, BH, "use",
          ["What the chain can be used for"],
          ["• System design and mooring layout", "  for a given site", "",
           "• Remaining-life prediction of the", "  critical reinforcement", "",
           "• Inspection and maintenance planning"],
          [], "l"),
    "E": (COLS[2], ROWS[1], BW, BH, "struct",
          ["Structural finite-", "element assessment"],
          ["Global model and sub-", "models of the reinforced-", "concrete breakwater;", "critical locations"],
          ["Ceit"], "c"),
    "G": (COLS[3], ROWS[1], BW, BH, "struct",
          ["Fatigue crack", "propagation"],
          ["New stress-intensity", "solutions for cracks in", "rebar; crack growth and", "remaining life"],
          ["Ceit"], "c"),
    "Hs": (COLS[4], ROWS[1], BW, BH, "shms",
           ["Structural Health", "Management System"],
           ["MATLAB application;", "four-year inspection", "cycle plus event-", "triggered checks"],
           ["Ceit"], "c"),
    "B": (COLS[2], ROWS[2], BW, BH, "struct",
          ["Concrete property", "prediction"],
          ["Machine learning predicts", "compressive strength", "from the concrete mix;", "stand-alone screening"],
          ["SINTEF"], "c"),
    "F": (COLS[3], ROWS[2], BW, BH, "monit",
          ["Corrosion", "monitoring"],
          ["Eddy-current sensor", "designed to track section", "loss of embedded rebar"],
          ["Ceit"], "c"),
    "V": (COLS[0], ROWS[1], 2 * BW + 20, ROWS[2] + BH - ROWS[1], "valid",
          ["Validation of the chain"],
          ["Finite-element models against ABS and",
           "DNV guidance and concrete tests (Ceit)",
           "",
           "Hydrodynamic models against towing-tank",
           "and wave-basin tests (MARIN)",
           "",
           "Crack growth against published",
           "fracture-mechanics results (Ceit)",
           "",
           "Corrosion sensor operated on the breakwater",
           "prototype at sea; detection of corrosion",
           "in the field still to be shown"],
          [], "l"),
}

# arrows: (points of the polyline, optional label (text, x, y, anchor), dashed)
ARROWS = [
    ([(190, 102), (210, 102)], None, False),                # A -> C
    ([(390, 102), (410, 102)], None, False),                # C -> D
    ([(590, 102), (610, 102)], None, False),                # D -> uses (design)
    ([(380, 185), (430, 240)], ("connector and mooring loads", 396, 224, "end"), False),  # C -> E
    ([(590, 322), (610, 322)], None, False),                # E -> G
    ([(790, 322), (810, 322)], None, False),                # G -> SHMS
    ([(790, 542), (900, 542), (900, 405)], ("sensor-data interface", 892, 440, "end"), True),  # F -> SHMS
    ([(900, 240), (900, 185)], None, False),                # SHMS -> uses
]
ARROW_COLOUR = "#1F5373"


def _lines(box):
    x, y, w, h, style, title, body, foot, align = box
    out = []  # (text, x, baseline_y, size, colour, bold, anchor)
    fill, stroke, ct, cb, cf = STYLES[style]
    pad = 12
    ax = x + w / 2 if align == "c" else x + pad + 4
    anchor = "middle" if align == "c" else "start"
    cy = y + pad + TITLE_FS
    for t in title:
        out.append((t, ax, cy, TITLE_FS, ct, True, anchor))
        cy += TITLE_LH
    cy += 4
    # Left-aligned panels (uses, validation) get a larger body font and
    # wider gaps between items; "•" starts a bullet item, "  " continues it.
    bfs, blh, gap = (BODY_FS, BODY_LH, BODY_LH * 0.5) if align == "c" else (14, 18, GAPS[style])
    if align != "c":
        cy += 6
    for t in body:
        if not t:
            cy += gap
            continue
        if t.startswith("•"):
            out.append(("•", ax, cy, bfs, cb, False, anchor))
            out.append((t[1:].strip(), ax + 14, cy, bfs, cb, False, anchor))
        elif t.startswith("  "):
            out.append((t.strip(), ax + 14, cy, bfs, cb, False, anchor))
        else:
            out.append((t, ax, cy, bfs, cb, False, anchor))
        cy += blh
    fy = y + h - pad - (len(foot) - 1) * FOOT_LH
    for i, t in enumerate(foot):
        out.append((t, ax, fy + i * FOOT_LH, FOOT_FS, cf, i == 0, anchor))
    return out


def svg():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         'font-family="TeX Gyre Heros, Helvetica, Arial, sans-serif">',
         '<title>SUREWAVE integrated modelling toolchain (schematic)</title>',
         '<rect width="100%" height="100%" fill="#FFFFFF"/>',
         f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
         f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{ARROW_COLOUR}"/></marker></defs>']
    for bid, b in BOXES.items():
        x, y, w, h, style = b[:5]
        fill, stroke = STYLES[style][:2]
        dash = ' stroke-dasharray="6 4"' if style == "valid" else ""
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="1.6"{dash}/>')
        for t, tx, ty, fs, col, bold, anc in _lines(b):
            wgt = ' font-weight="bold"' if bold else ""
            s.append(f'<text x="{tx:.1f}" y="{ty:.1f}" font-size="{fs}" fill="{col}" '
                     f'text-anchor="{anc}"{wgt}>{escape(t)}</text>')
    for pts, label, dashed in ARROWS:
        p = " ".join(f"{x},{y}" for x, y in pts)
        da = ' stroke-dasharray="7 5"' if dashed else ""
        s.append(f'<polyline points="{p}" fill="none" stroke="{ARROW_COLOUR}" stroke-width="2.2"{da} '
                 'marker-end="url(#ah)"/>')
        if label:
            t, lx, ly, anc = label
            s.append(f'<text x="{lx}" y="{ly}" font-size="{FOOT_FS}" font-style="italic" '
                     f'fill="{ARROW_COLOUR}" text-anchor="{anc}">{escape(t)}</text>')
    s.append("</svg>")
    return "\n".join(s) + "\n"


def _tex(t):
    rep = {"&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "•": r"\textbullet"}
    return "".join(rep.get(c, c) for c in t)


def _col(hexc):
    return "{rgb,255:red,%d;green,%d;blue,%d}" % tuple(int(hexc[i:i + 2], 16) for i in (1, 3, 5))


def tikz():
    pt = 0.5159  # 1 unit = 0.182 mm = 0.5159 pt
    s = ["% Generated by scripts/toolchain_figure.py -- do not edit by hand.",
         r"\begin{tikzpicture}[x=0.182mm,y=-0.182mm,line join=round]"]
    for bid, b in BOXES.items():
        x, y, w, h, style = b[:5]
        fill, stroke = STYLES[style][:2]
        dash = ",dash pattern=on 3pt off 2pt" if style == "valid" else ""
        s.append(rf"\draw[fill={_col(fill)},draw={_col(stroke)},line width=0.8pt,rounded corners=1.8mm{dash}] "
                 rf"({x},{y}) rectangle ({x + w},{y + h});")
        for t, tx, ty, fs, col, bold, anc in _lines(b):
            a = {"middle": "base", "start": "base west"}[anc]
            f = rf"\fontsize{{{fs * pt:.2f}}}{{{fs * pt * 1.15:.2f}}}\selectfont"
            if bold:
                f += r"\bfseries"
            s.append(rf"\node[anchor={a},inner sep=0,text={_col(col)},font={f}] at ({tx:.1f},{ty:.1f}) {{{_tex(t)}}};")
    for pts, label, dashed in ARROWS:
        p = " -- ".join(f"({x},{y})" for x, y in pts)
        da = ",dash pattern=on 3pt off 2pt" if dashed else ""
        s.append(rf"\draw[-{{Stealth[length=2.2mm,width=1.8mm]}},draw={_col(ARROW_COLOUR)},line width=1.1pt{da}] {p};")
        if label:
            t, lx, ly, anc = label
            a = {"end": "base east", "start": "base west"}[anc]
            f = rf"\fontsize{{{FOOT_FS * pt:.2f}}}{{{FOOT_FS * pt * 1.15:.2f}}}\selectfont\itshape"
            s.append(rf"\node[anchor={a},inner sep=0,text={_col(ARROW_COLOUR)},font={f}] at ({lx},{ly}) {{{_tex(t)}}};")
    s.append(r"\end{tikzpicture}")
    return "\n".join(s) + "\n"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    stem = sys.argv[1]
    with open(stem + ".svg", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(svg())
    with open(stem + ".tikz.tex", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(tikz())
    print(f"wrote {stem}.svg and {stem}.tikz.tex")


if __name__ == "__main__":
    main()
