"""One-off: replace [[FIGURE-N ...]] placeholders in the D8.3 brochure with real
image references, remove Fig 25 and Fig 26 lines, and write back in-place.

Kept as a script rather than an inline sed because the placeholder text is unique
per figure and the replacement includes a proper caption for each.
"""

import re
from pathlib import Path

BROCHURE = Path("surewave/deliverables/2026-09-28_surewave_d8.3_technical_brochure.md")
IMG_DIR = "../images/2026-09-28_surewave_d8.3_technical_brochure"

# Captions written for the printed brochure — short, informative, PDF-friendly.
CAPTIONS = {
    1:  "Cover — the SUREWAVE offshore floating PV concept in operation.",
    2:  "Offshore floating PV market opportunity — installed capacity by segment with the addressable-market ribbon.",
    3:  "The integrated SUREWAVE system — isometric cutaway showing the four subsystems and their connections.",
    4:  "Reference plant layout — 346 m diameter circular footprint with 68 matrices, perimeter and internal breakwater lines.",
    5:  "Three reference site classes — Baltic (mild), Western Mediterranean (mid) and Greater North Sea (harsh), with wave height and water depth to scale.",
    6:  "Floating breakwater unit — dimensioned three-view engineering drawing (20 m x 5 m x 2.5 m, 123.4 t).",
    7:  "FPV module and hinge architecture — exploded isometric with aluminium float, PV surface, sealant, hinge and sensor node.",
    8:  "Catenary mooring — three configurations across the Baltic, Mediterranean and North Sea site classes.",
    9:  "Circular concrete composition — recycled and secondary content across the HPC, LWAC and cellular formulations.",
    10: "Breakwater unit cross-section — three-material sandwich of HPC shell, LWAC top slab and cellular concrete core.",
    11: "SUREWAVE integrated modelling toolchain — from metocean data through coupled aero-hydro, structural FE, fatigue and corrosion-sensor inputs to the SHMS platform.",
    12: "MARIN wave-basin test — scaled floating breakwater and FPV array segment under coupled wave and wind loading.",
    13: "FE stress field on the breakwater under an extreme wave-loading event — peaks at mooring and connector attachment points.",
    14: "Gen-1 polyurethane hinge geometry (top) with the measured Gen-1 vs redesigned-hinge force-displacement test results (bottom).",
    15: "Reduced-scale breakwater prototype in field monitoring at El Musel Port, Gijón.",
    16: "Connection component test at SINTEF — hinge under tensile loading with digital-image-correlation setup.",
    17: "Structural Health Management System — degradation-tracking view with sensor data, filtered corrosion curve and residual-life estimates.",
    18: "Eddy-current corrosion sensor mounted on the concrete surface, detection field reaching the embedded rebar.",
    19: "25-year cumulative CO2 emissions per plant — SUREWAVE offshore FPV against a coal-fired reference, across the three sites.",
    20: "SUREWAVE 10 MW LCoE by region — base scenario, 50-year project lifetime.",
    21: "Mediterranean 10 MW CAPEX composition — cable connection is the most sensitivity-driving segment.",
    22: "SUREWAVE material-supply risk map — hotspots and consortium partner locations.",
    23: "SUREWAVE technology-readiness trajectory — 2022 project start through indicative commercial roll-out.",
    24: "The SUREWAVE consortium — seven partners across four countries.",
}

WIDTH_DEFAULT = "90%"
WIDTH_OVERRIDES = {
    17: "80%",  # SHMS UI screenshot — smaller so it doesn't dominate the page
    21: "70%",  # Cost stack — portrait orientation, narrower is better
}

text = BROCHURE.read_text(encoding="utf-8")

# Pattern for each placeholder line
placeholder_re = re.compile(r"^\[\[FIGURE-(\d+)[^\]]*\]\]\s*$", re.MULTILINE)


def replace(match):
    n = int(match.group(1))
    if n in (25, 26):
        # Removed at user request — signal deletion
        return "\x00DELETE\x00"
    if n not in CAPTIONS:
        return match.group(0)  # leave alone if unknown
    width = WIDTH_OVERRIDES.get(n, WIDTH_DEFAULT)
    filename = f"fig{n:02d}.png"
    return f"![Figure {n}. {CAPTIONS[n]}]({IMG_DIR}/{filename}){{width={width}}}"


new_text = placeholder_re.sub(replace, text)

# Collapse "\x00DELETE\x00" lines and the blank line immediately before them if present
new_text = re.sub(r"\n\n\x00DELETE\x00\n", "\n", new_text)
new_text = new_text.replace("\x00DELETE\x00\n", "").replace("\x00DELETE\x00", "")

BROCHURE.write_text(new_text, encoding="utf-8")

# Report
remaining = placeholder_re.findall(new_text)
inserted = new_text.count(f"]({IMG_DIR}/")
print(f"Placeholders remaining: {len(remaining)} (should be 0)")
print(f"Image links inserted: {inserted} (should be 24)")
