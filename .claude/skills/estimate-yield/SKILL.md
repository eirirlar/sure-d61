---
name: estimate-yield
description: Produce a six-section Mulighetsstudie-style annual-production report for a floating-PV site, matching the Sunlit Sea Simuleringsrapport format. Trigger when the user asks to "estimate yield for X", "mulighetsstudie for lat,lng med N MWp", "add a yield report for this RFP", "give me the annual production number for Z", "lag en produksjonssimulering for N m² ved …", or similar. Minimum input is site lat/lng and either installed capacity or available water area; everything else defaults, and every default appears in the output. Uses `scripts/estimate_yield.py` (PVGIS 5.2 for POA + GHI, user-supplied PR decomposition, scenario sensitivity, FPV cooling bonus). YAML frontmatter `sunlit_template: report` dispatches to `md_to_sunlit_report.py` for PDF rendering in the Sunlit Sea visual profile.
---

# estimate-yield

## When to use

- User asks for an annual-production number for an FPV site at a specific lat/lng and capacity (or available water area).
- User says: "estimate yield for Risø", "mulighetsstudie for Gunneklevfjorden med 3.2 MWp", "yield for Blekinge med 30 000 m²", "add a yield report for this RFP", "give me the production number for <lat>,<lng>".
- A deliverable (RFP response, mulighetsstudie, investor material, commercial pipeline sizing) needs a plausible yield figure with its loss decomposition and scenario range visible.

## Target format

The reference artefact for what the output should look like is `generic/background/2026-09-17_simuleringsrapport_blekinge_mulighetsstudie.pdf`. The estimator reproduces that structure: headline KPI row, six numbered sections (Panelkonfigurasjon og areal, Solinnstråling og POA-analyse, Tapsbudsjett / PR-dekomponering, Energiproduksjon, Sensitivitetsanalyse, Nøkkelantakelser og begrensninger), rendered through the Sunlit Sea report template with Everett headlines, Arial body and blue+yellow accents.

## Not for

- Bankable P50/P75/P90 yields for financing. Use PVsyst with site-measured solar resource.
- LCOE, NPV, cashflow or revenue modelling.
- Design optimisation (optimal tilt, string sizing, DC/AC ratio).

## Procedure

1. **Collect the minimum inputs:**
    - site lat (WGS84 decimal degrees)
    - site lng (WGS84 decimal degrees)
    - **either** installed DC capacity in kWp (`--kwp`) **or** available water surface area in m² (`--area`)

    If any is missing, ask the user. For an RFP site, look in the RFP background `.md` for coordinates; for a Sunlit Sea commercial site, check `docs/project_facts.md` for the canonical site entry.

2. **Decide where the report goes.** Default: a new file next to the invoking deliverable, named `<deliverable_stem>.feasibility_study.md (English) / .simuleringsrapport.md (Norwegian)`, with the chart written as `<deliverable_stem>.feasibility_study.png (English) / .simuleringsrapport.png (Norwegian)` alongside. The caller then renders via `python scripts/md_to_pdf.py <path>` (dispatcher picks up `sunlit_template: report` from the YAML frontmatter).

3. **Run the estimator:**

    ```bash
    # Area-based (preferred when available water surface is the fixed quantity)
    uv run scripts/estimate_yield.py \
      --lat <lat> --lng <lng> --area <m2> \
      --location-name "<Site name>" \
      --md-out <path>.feasibility_study.md (English) / .simuleringsrapport.md (Norwegian)

    # Capacity-based (when kWp is the fixed quantity)
    uv run scripts/estimate_yield.py \
      --lat <lat> --lng <lng> --kwp <kwp> \
      --location-name "<Site name>" \
      --md-out <path>.feasibility_study.md (English) / .simuleringsrapport.md (Norwegian)
    ```

    Chart PNG is written automatically next to the `.md`. Full JSON goes to stdout; a short human summary (annual MWh, specific yield, CF, PR) goes to stderr.

4. **Optional overrides.** The script accepts per-component loss flags (`--loss-temperature-coefficient`, `--loss-inverter`, `--loss-dc-cable`, `--loss-ac-cable`, `--loss-mismatch`, `--loss-soiling`, `--loss-lid`, `--loss-availability`, `--loss-transformer`), plus `--tilt`, `--azimuth`, `--fpv-cooling-bonus`, `--panel-width`, `--panel-height`, `--panel-wp`, `--gap-mm`, `--year`, `--yaml`. Use when the user has specific site data that beats the defaults.

5. **Render to PDF.**

    ```bash
    python scripts/md_to_pdf.py <path>.feasibility_study.md (English) / .simuleringsrapport.md (Norwegian)
    ```

    The dispatcher reads `sunlit_template: report` from the YAML frontmatter and routes to `md_to_sunlit_report.py`. Output is a PDF matching the Sunlit Sea visual profile.

6. **Report back to the user.** Headline MWh/y, specific yield, PR, location of the written `.md`, `.png` and `.pdf`. Flag loud if the estimator nudged the lookup point off the input coordinates (PVGIS refuses over-sea sites; the script picks the nearest land grid cell within 5 km; the nudge appears in the assumption audit).

## Output shape

The generated Markdown report contains, in order:

- **Title and meta line** — title ("Flytende solkraftverk — Mulighetsstudie"), location subtitle, date + author + status strap, irradiasjonsdata source.
- **Nøkkeltall (headline row)** — two rows of three cells each: antall paneler, installert effekt, POA-innstråling, PR, estimert produksjon, spesifikk yield.
- **Section 1 — Panelkonfigurasjon og areal** — panel dimensions, slot area, packing factor, available area, panel count, installed kWp.
- **Section 2 — Solinnstråling og POA-analyse** — GHI (horizontal), POA (tilted), tilt and azimuth, gain vs horizontal.
- **Section 3 — Tapsbudsjett / PR-dekomponering** — nine loss components summing to Σ, computed PR, plus a PVGIS cross-check line noting whether the component list is optimistic, conservative or consistent with PVGIS's internal crystSi model.
- **Section 4 — Energiproduksjon** — P_peak, POA, PR, estimated production with the explicit formula (`E = P × H × PR × (1 + FPV bonus)`), specific yield, equivalent operating hours, DC-nameplate capacity factor.
- **Section 5 — Sensitivitetsanalyse** — Low / Base / High scenarios with GHI ±5 % and PR ±3/+2 pp. Monthly chart embedded below.
- **Section 6 — Nøkkelantakelser og begrensninger** — three-column table: tema, antakelse / begrensning, anbefalt neste steg. Covers irradiation, POA / tilt, area, panel spec, PR, FPV cooling bonus, albedo, grid / inverter, regulatory.
- **Footer** — beregningsmetode, irradiasjonsgrunnlag, preliminary-use disclaimer, link to methodology doc.

Bold in table cells is used for key values (per the project's no-bold-in-body rule, which permits bold inside data-display tables; the rule targets emphasis-in-prose).

## Applicable rules

- CLAUDE.md "**File changes require confirmation**" — running the estimator and writing the output `.md` is a lookup. Inlining the report into a target deliverable is a separate edit; wait for an "add it to the RFP" instruction.
- CLAUDE.md "**External deliverables stand alone**" — the generated report references the methodology doc by path, which is correct because an external reader can be told that a methodology document exists without needing its contents. Do not add any other repo-internal paths when customising the report for a deliverable.
- CLAUDE.md "**Do not convert to docx automatically**" — the estimator outputs `.md`. PDF conversion through `md_to_pdf.py` is a separate, explicit instruction.
- CLAUDE.md "**Follow conventions written this session**" — once a deliverable uses one of the baseline loss values, keep it consistent across sibling deliverables for the same site. Document the component values in the deliverable's working notes if they differ from the defaults.

## Historical references

- First estimator run: COWI/DTU Risø RFP response (§2.8 Energi-yield). Site 55.6915 N, 12.0809 E; 35 kWp; result ~34 MWh/y (specific yield ~976 kWh/kWp, PR 90 %). The Risø site is over water; the estimator auto-nudged to the nearest PVGIS land grid cell for the irradiation lookup.
- Reference format: Blekinge/Kronoberg Simuleringsrapport (September 2026, 56.63 N / 14.65 E, 30 000 m² → 8 608 panels × 750 Wp → 6.456 MWp DC). Running the estimator on the same inputs produces 5 863 MWh/y vs the reference's 6 320 MWh/y (−7 %); the difference is entirely in POA (PVGIS gives 989 kWh/m²/år at those exact coordinates vs the reference's 1 088), and PR matches at 90 %.

## Known pitfalls

- **Supplying azimuth in PVGIS convention** (0 = S) instead of compass convention (180 = S). The script's `--azimuth` is compass; it converts internally.
- **Forgetting that the FPV cooling bonus default is a preliminary assumption**, not a site measurement. The output flags it as such; do not strip that flag.
- **Treating the estimate as bankable.** It is not. The methodology doc explains why.
- **Adjusting the loss decomposition without rationale.** Each override should have a basis — a vendor datasheet value for inverter efficiency, a measured soiling study, a site-specific availability number. Random tweaks to hit a target yield number undermine the auditability the loss decomposition is there to provide.
- **Rendering the PDF before reviewing the Markdown.** The Markdown is the authoritative source; eyeball it for weirdness before conversion. The dispatcher is deterministic — once the `.md` looks right, the PDF will too.
