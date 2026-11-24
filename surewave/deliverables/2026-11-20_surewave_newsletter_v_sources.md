---
internal_title: SUREWAVE Newsletter V — sources and figure provenance
internal_date: 2026-11-20
---

# SUREWAVE Newsletter V — sources and figure provenance

Companion to `2026-11-20_surewave_newsletter_v.md`. Files are under `surewave/background/` unless the path says otherwise. Checked 20 November 2026.

## Text

| Newsletter claim | Source |
|---|---|
| Project ends 31 December 2026 | `docs/project_facts.md` |
| Sunlit Sea led the economic assessment; plant sizes, layouts and financial scenarios at three sites | D7.4 (`2025-09-05_surewave_d7.4_economic_assessment.md`), scope; task 7.4 leader Sunlit Sea (WP index) |
| Base case: electricity sold at €0.12/kWh; discount rate 8.5 %; short floating cable to a nearby offshore substation (submarine cable excluded from the base case) | D7.4 §5.1 (base-case discount rate 8.50 %); results text ("reference electricity sale price of €0.12/kWh"); §7.5.1 ("exclude submarine cable costs from the base-case financial analysis") |
| 10 MW: Mediterranean €0.062/kWh, NPV about €8.9 M, viable, recommended for pilot and scale-up; Baltic €0.096/kWh, viable under favourable conditions; North Sea €0.139/kWh, not viable stand-alone, hybrid/demonstration only | D7.4 "Key Financial Findings" (recommendations quoted there). IRR and payback deliberately omitted: D7.4 gives 10.7 % and 7–8 years in its summary but 10.6 % and 8 years in its results table |
| 2 MW and 5 × 2 MW modular less viable than single 10 MW | D7.4 ("2 MW and 10 MW modular are significantly less economically viable") |
| Floating cable about 300 m; full submarine cable raises Mediterranean LCOE from €0.062 to €0.076/kWh; North Sea above €0.45/kWh; prioritise nearby offshore substations, hybrid platforms or shorelines within 15 km | D7.4 §7.5.1. D8.3 §9's "€0.09–0.11/kWh for a 20 km connection" is not used |
| Sharing infrastructure with offshore wind is the most promising route | D7.4 §7.5.1 (hybrid energy platforms); D7.3 Key results ("connection to existing offshore facilities such as an offshore wind farm can significantly reduce the environmental impacts"); D8.3 §11 |
| Conventional breakwater gave the best economic result; HPC raised investment cost without improving the economics | D7.4 §7.5.2 ("the conventional design consistently yields the most favourable results. HPC designs … significantly higher CAPEX, with marginal or no improvement") |
| 9 MWp plant, North Sea: 160,000–180,000 t CO₂-eq saved over 25 years vs coal depending on layout; sunnier sites save more | D7.3 Key results ("saving of around 170,000 tonnes of CO2 compared to electricity generation from coal over a 25-year operating period"). D7.3 also gives > 180,000 t (North Sea, uniform) and > 160,000 t (North Sea, split) |
| Quantities of vessel fuel dominate; then panels, breakwaters, anchoring; cable relevant beyond about 50 km | D7.3 Key results (LCA) ("dominated in particular by the quantities of vessel fuel") |
| Circular concrete gives no relevant GHG saving vs conventional; minor next to the saving vs fossil power | D7.3 Key results ("Innovative breakwaters") |
| Higher impacts than land PV and wind; complements rather than replaces | D7.3 Key results ("Comparison with other renewable energy sources"); Conclusions ("can complement the portfolio") |
| Local concerns: piling noise, shading, anchor chains and migratory species, cable routes through coastal habitats; artificial-reef effect; case-by-case | D7.3 Key results (local environmental impacts) |
| Purchased inputs carry most social risk; solar-panel supply chain almost half, mainly solar cells; risk can more than triple from higher-risk countries; offshore work safety and labour rights | D7.6 "Summary of social assessment" (`2025-11-05_surewave_d7.6_integrated_sustainability_report.md`) |
| TRL 2–3 to 4–5; next steps (open-sea pilot kW–low MW, North Sea hinge iteration, field data into SHMS, shared infrastructure, permits and stakeholder agreements, independent technology qualification required by lenders) | D8.3 §11 "Path to market" (`deliverables/2026-09-28_surewave_d8.3_technical_brochure.md`) |
| DOIs: D7.3 22831061; D7.4 22831172; cost-model dataset 17534609; D7.5 22955900; D7.6 22956130; 91st LCA Forum 22957101 | Zenodo snapshot; all six resolve (checked 20 Nov 2026) |

## Figures

| Figure | File | Provenance | Notes |
|---|---|---|---|
| 1 | `surewave/images/2026-09-28_surewave_d8.3_technical_brochure_lowres/fig20.png` | Chart generated for D8.3 from D7.4 figures (AI-drawn) | Values match D7.4's summary (LCOE, NPV; in-chart IRR 10.7 % and payback 7–8 years are D7.4 summary values). Caption says "Chart drawn from the figures in the economic assessment (D7.4)" |

Not used: fig19 (CO₂ chart shows the same 170,000 t for all three sites and labels the site classes inconsistently with D2.1/D7.3); fig21 (cable infographic based on D8.3's €0.09–0.11/kWh, which D7.4 does not support).

## Partner check before publication

- IFEU (Heiko Keller, Maximilian Breyer): climate, environment and social items.
- SINTEF (Balram Panjwani): overall check of the final issue.

## Changes after review (2026-11-20)

Two review agents (layout; fact and label check). Applied: base case adds the 50-year asset life with mid-life PV module reinstallation (D7.4 "Asset lifetime: 50 years (including mid-life PV module reinstallation)"), which also explains the chart subtitle; climate figure restated for the 9 MWp LCA plant as 160,000–180,000 t in the North Sea depending on layout, with sunnier sites saving more (D7.3: "> 180,000 t" uniform, "> 160,000 t" split, Figure 8 "9 MWp"; electricity yield the largest single factor between sites) — replaces "around 170,000 t for the reference layout"; D7.3 durability caveat added ("include a durability, which is not yet achieved in practise … hinges"); co-location stated as D7.4's recommendation, not as "most promising"; breakwater economics names the four options and says "marginal or no improvement" (D7.4 §7.5.2), and no longer calls HPC "circular"; "can have higher impacts" than land PV and wind (D7.3 "can perform significantly worse"); lenders "typically" require qualification (D8.3); IFEU credited for the social LCA; hinge and monitoring system explained in plain words; figure caption states it was prepared for the brochure; Zenodo community URL added. Layout: forced page break removed, chart 60 %, two redundant lines removed from "In numbers"; the issue is two pages.

Known and accepted: the chart (fig20) prints D7.4's summary values, including Baltic "IRR 2.2 % · NPV +€2.1 M", which are mutually inconsistent at an 8.5 % discount rate — an inconsistency inside D7.4 itself. The newsletter text does not repeat IRR or payback. Replace the chart with an LCOE-only version if a cleaner figure is wanted.

D7.4's repo copy carries "Dissemination level: SEN", while the Grant Agreement lists D7.4 as PU (WP index); the Zenodo record is public. Confirm with the coordinator if in doubt.

Partner review (IFEU, Heiko Keller, comments in the PDF, 2026-11-23). Applied: IFEU written out in full in the project box; "it saves" changed to "it can save more than", in line with D7.3 "> 160,000 t" (split) and "> 180,000 t" (uniform); vessel-fuel sentence changed to the plural "dominate", with "quantities of vessel fuel" as the subject, following D7.3; "to achieve a faster decarbonisation" added to the closing sentence of the climate section.
