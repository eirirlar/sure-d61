"""Fill the HRB G2M Market Definition Canvas (PDF) and Value Proposition Canvas (pptx)
with Sunlit Sea KER1 content.

One-off for T140 (2026-11-05); content strings are hard-coded and match the
companion markdown canvases in surewave/deliverables/.
"""

from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pptx import Presentation
from pptx.util import Pt
from pptx.enum.text import MSO_AUTO_SIZE

ROOT = Path(__file__).resolve().parent.parent
BG = ROOT / "surewave" / "background"
OUT = ROOT / "surewave" / "deliverables"

# --------------------------------------------------------------------------
# Market Definition Canvas (PDF, AcroForm fields Testo1..Testo8)
# --------------------------------------------------------------------------

MDC_FIELDS = {
    "Testo1": (
        "Sunlit Sea CONNECT offshore floating photovoltaic platform "
        "(Generation 2). Aluminium bottom plate plus cast polyurethane "
        "frame carrying a standard commercial 710-740 Wp glass-glass "
        "panel; panels are decoupled from float manufacture and dropped "
        "in at deployment. Floats connect along the full edge through "
        "Generation-3 polyurethane hinges validated under SUREWAVE "
        "(Grant Agreement 101083342). Deployed standalone or behind a "
        "floating breakwater."
    ),
    "Testo2": (
        "- Project development managers at utility-scale renewable "
        "developers and IPPs (1-10 MW offshore photovoltaic).\n"
        "- Asset managers at offshore wind farms evaluating in-lease "
        "solar co-location.\n"
        "- Energy and sustainability directors at coastal industrial "
        "off-takers.\n"
        "- EPC technical leads at marine contractors.\n"
        "- Investment committees and lender technical due diligence."
    ),
    "Testo3": "Offshore renewable energy project developer.",
    "Testo4": (
        "Primary (verb / object / contextual clarifier):\n"
        "Generate utility-scale electricity from solar irradiance on "
        "European coastal water surfaces (1-10 MW first generation, "
        "scaling to 50+ MW by 2033).\n\n"
        "Secondary:\n"
        "- Co-locate with offshore wind leases, sharing substation, grid "
        "connection and mooring corridors.\n"
        "- Provide platform-integrated structural health monitoring "
        "data for condition-based maintenance."
    ),
    "Testo5": (
        "- Offshore wind turbines: offshore wind electricity "
        "(complementary).\n"
        "- Onshore utility photovoltaic: land-based solar (substitute "
        "when land is available).\n"
        "- Grid connection infrastructure: transmit offshore electricity "
        "to shore.\n"
        "- Mooring and anchoring: hold floating structures in position.\n"
        "- Floating breakwaters (SUREWAVE KER3, Clement Germany): "
        "attenuate waves at exposed sites.\n"
        "- Structural health monitoring platforms (SUREWAVE KER6, Ceit): "
        "condition data for maintenance.\n"
        "- Power purchase agreements and offtake contracts: monetise the "
        "generated electricity."
    ),
    "Testo6": (
        "\"Grow renewable capacity in a coastal market where onshore "
        "solar is blocked by land scarcity and permit friction, using "
        "offshore lease or nearshore water that no other technology in "
        "my portfolio can currently use productively.\""
    ),
    "Testo7": "offshore renewable energy project developers",
    "Testo8": "grow offshore renewable capacity where onshore solar is blocked",
}

mdc_src = BG / "2024-12-17_hrb_g2m_market_definition_canvas_template.pdf"
mdc_dst = OUT / "2026-11-05_surewave_hrb_market_definition_canvas_ker1_filled.pdf"

reader = PdfReader(str(mdc_src))
writer = PdfWriter(clone_from=reader)
for page in writer.pages:
    writer.update_page_form_field_values(page, MDC_FIELDS, auto_regenerate=True)
with open(mdc_dst, "wb") as f:
    writer.write(f)
print(f"Wrote {mdc_dst.relative_to(ROOT)}")

# --------------------------------------------------------------------------
# Value Proposition Canvas (pptx, 7 text boxes on slide 1)
# --------------------------------------------------------------------------
# Compressed to fit the actual box dimensions (inches):
#   [0] Gain creators     2.95 x 1.29
#   [1] Products & svcs   1.70 x 1.87  (narrow!)
#   [2] Pain relievers    2.95 x 1.19
#   [3] Gains             2.63 x 1.41
#   [4] Customer jobs     1.70 x 1.76  (narrow!)
#   [5] Pains             2.63 x 1.58
#   [6] Customer segment  7.34 x 0.77  (header strap)

BULLET = "• "  # • Unicode bullet

VPC_FILLS = {
    6: [  # Customer segment (header strap, max 2 lines)
        "Utility-scale renewable energy developers and independent "
        "power producers — 1–10 MW offshore photovoltaic in European "
        "coastal waters, 2027–2030 commercial window.",
    ],
    4: [  # Customer jobs (narrow)
        BULLET + "Grow renewables where onshore land is blocked",
        BULLET + "Add solar to offshore wind portfolios",
        BULLET + "Clear investment-grade due diligence",
        BULLET + "Meet offtake-price benchmarks",
        BULLET + "Operate 20+ years at predictable OPEX",
        BULLET + "Position as offshore-renewables technology leader",
    ],
    5: [  # Pains
        BULLET + "No credible offshore floating-PV product at commercial scale",
        BULLET + "No bankable design basis; underwriters price risk conservatively",
        BULLET + "CAPEX per watt high; economics close only in specific sea basins",
        BULLET + "Site development slow: marine spatial planning, EIA, grid, permits",
        BULLET + "OPEX uncertain; no condition-based-maintenance track record",
        BULLET + "Supply chain immature; single-vendor dependency is a procurement flag",
    ],
    3: [  # Gains
        BULLET + "Design basis the TDD team can accept, independently tested",
        BULLET + "Cost case below €70/MWh LCOE at Mediterranean 10 MW scale",
        BULLET + "Portfolio diversification: solar complements wind, lifts firm capacity",
        BULLET + "Reference sites + demonstrator evidence for investment committee",
        BULLET + "Maintenance model fits existing offshore-asset operations",
        BULLET + "Supplier scales to multiple projects per year",
    ],
    1: [  # Products & services (narrow)
        BULLET + "Sunlit Sea CONNECT platform",
        BULLET + "Site engineering and system integration",
        BULLET + "SUREWAVE-validated model chain",
        BULLET + "Ceit SHMS integrated subsystem",
        BULLET + "Gen 1 reference fleet (Mannheim, Skiftestjørna)",
    ],
    2: [  # Pain relievers
        BULLET + "SUREWAVE-validated model chain at TRL 4–5; DNV-aligned",
        BULLET + "Gen-3 hinge load capacity 14 → 37 kN (SINTEF-tested)",
        BULLET + "Mediterranean 10 MW: LCOE €0.062/kWh, 8-year payback (D7.4)",
        BULLET + "Standard glass-glass panels; mainstream supply chain",
        BULLET + "SHMS data product for condition-based maintenance",
        BULLET + "SuRE follow-on scaling Gen 2 prototypes 4 and 5",
    ],
    0: [  # Gain creators
        BULLET + "Cast-PU + aluminium scales 3D-printed moulds → industrial casting",
        BULLET + "Decoupled standard panels ride mainstream PV price reduction",
        BULLET + "Floating-wind co-location ready (shared substation, mooring)",
        BULLET + "Serviceable Gen-3 hinge replacement without array recovery",
        BULLET + "Commissioning from standard quays; no specialist offshore vessel",
        BULLET + "European strategic-autonomy case on heavy components",
    ],
}

vpc_src = BG / "2024-12-17_hrb_g2m_value_proposition_canvas_template.pptx"
vpc_dst = OUT / "2026-11-05_surewave_hrb_value_proposition_canvas_ker1_filled.pptx"

prs = Presentation(str(vpc_src))
slide = prs.slides[0]
shapes = list(slide.shapes)

for idx, lines in VPC_FILLS.items():
    tf = shapes[idx].text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    tf.clear()
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        # Compact font so default rendering stays in-box; auto_size can still shrink.
        for run in p.runs:
            run.font.size = Pt(9)

prs.save(str(vpc_dst))
print(f"Wrote {vpc_dst.relative_to(ROOT)}")
