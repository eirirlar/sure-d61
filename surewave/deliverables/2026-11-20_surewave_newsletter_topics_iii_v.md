---
internal_title: SUREWAVE Newsletters III–V — topic proposal
date: 2026-11-20
---

# SUREWAVE Newsletters III–V — topic proposal

Three issues to complete the D8.5 target of five newsletters before the project ends on 31 December 2026. Same format as Newsletters I and II (about three pages, PDF on surewave.eu, sent to the mailing list and announced on LinkedIn). None of the items repeats the first two issues, which covered requirements, metocean criteria, the MARIN partner profile, breakwater CFD basics, Zenodo, Intersolar/Seagriculture 2023 and the early consortium meetings.

Method: four parallel agents, each reading the deliverables as one reader type — an offshore energy developer, a cleantech investor, a CINEA policy officer and a research engineer at a marine institute — proposed and critiqued topics. Their proposals converged on the same three themes. Every figure below was checked against the deliverable named in the source column on 20 November 2026.

What all four readers asked for: one measured number per item with its limits, honest statements of what did not work (the North Sea hinge margin, the unproven field corrosion detection, the cost case for the ring), DOIs and datasets that can be used today, and a named contact. What would make them stop reading: "revolutionary/groundbreaking" wording, AI concept renders presented as hardware, and unsourced numbers.

## Newsletter III — "Tested at scale" (publish about 3 December 2026)

Theme: what the physical tests and the validated models showed, including the redesigns they forced.

| # | Item | Content | Source | Image |
|---|---|---|---|---|
| 1 | Two basin campaigns at MARIN | 1:10 model of the coupled breakwater and FPV system, tested with and without the breakwater. The first campaign revealed buckling and snap loading in the original hinges; the second, with redesigned hinges, did not. | D8.3 §6 "Basin testing"; final technical report working copy, WP6 Task 6.4 | fig12 (real MARIN photo; caption as loads on individual breakwater units, which is what it shows) |
| 2 | A hinge that failed, and the one that replaced it | The redesigned polyurethane connection has about three times the tensile strength of the first generation and about 20 kN buckling strength; calculated fatigue life is 2.5×10¹¹ cycles against 7.88×10⁸ needed for 25 years. The full-hinge ultimate limit state of 37 kN clears the Baltic (34 kN) and Mediterranean (33 kN) design loads; the North Sea load (40 kN) needs one more design iteration. | D6.3 Conclusions; D8.3 §6 "Component-level" | fig14 (Gen-1 drawing plus measured test data; the redesigned geometry is not shown) |
| 3 | Connections between breakwaters and to the array | The wire connection between breakwater units reached an average of 402 kN (rated 450 kN). The breakwater-to-FPV connection failed at a mean 41 kN, in line with the 42 kN requirement. | D6.1 Conclusions | Clement CAD, breakwater_unit_exterior_interior.png |
| 4 | A 2 MWp farm on a supercomputer | MARIN's DIFFRAC simulation of 3,660 FPV modules inside a ring of 32 breakwaters, validated against the basin tests. Vertical connector loads fall by up to 50 % in steep irregular seas, but standing waves inside the ring raise loads locally; the authors note it is not evident that the load reductions outweigh the cost of the ring. Basin dataset: 10.5281/zenodo.10960431; paper: Energies 19(7) 1609. | Bunnik et al. 2026 (Energies), abstract and §7 | Clement CAD moored_ring_with_pv.png (open-sea ring; no nearshore claims next to it) |

## Newsletter IV — "From recycled concrete to nine months at sea" (publish about 15 December 2026)

Theme: the circular concrete breakwater, from lab mix to field exposure, and how its condition is monitored.

| # | Item | Content | Source | Image |
|---|---|---|---|---|
| 1 | Circular concrete that meets marine specifications | High-performance concrete reached 128 MPa (target 120 MPa) and lightweight aggregate concrete 68 MPa, with recycled and secondary materials replacing part of the cement and aggregate. | D8.3 §4; D4.1 Conclusions | breakwater_sections.png (Clement CAD) |
| 2 | Lab durability | A crystalline admixture cut mean water penetration in the lightweight concrete from 8.2 mm to 0.6 mm. | D4.2, water-penetration results | None catalogued — request a lab photo from ACCIONA |
| 3 | Nine months at El Musel, Gijón | A reduced-scale prototype (3.40 × 1.70 m) was exposed for about nine months. Post-exposure inspection found no significant structural deterioration; fouling covered more than 85 % of surfaces but stayed within the 0.06 m design allowance; openings cut for monitoring equipment were the critical durability detail. | D8.3 §6 "Reduced-scale prototype"; final technical report working copy, WP6 Task 6.5 | fig15 (real ACCIONA photo) |
| 4 | Watching the structure age | Ceit's structural health management system combines material data, loads, degradation and crack growth to recommend inspection intervals. The eddy-current sensor resolves about 0.17 mm of material loss in the lab; detection of corrosion in the field remains to be demonstrated. | D5.4 Conclusions; D5.6 Conclusions; D8.3 §6–7 | fig17 (real Ceit software screenshot) |

## Newsletter V — "Cost, carbon and what comes next" (publish about 29 December 2026)

Theme: where offshore FPV makes sense, its climate and social footprint, the open results, and how to engage after the project.

| # | Item | Content | Source | Image |
|---|---|---|---|---|
| 1 | Cost of energy by sea basin | For a 10 MW plant: €0.062/kWh in the Mediterranean (NPV about €8.9 M), €0.096/kWh in the Baltic, €0.139/kWh in the North Sea (not viable on its own). | D7.4 Summary of Key Financial Results | fig20 (bar chart) |
| 2 | The grid connection decides | In the Mediterranean, replacing the short floating cable to a nearby offshore connection point with a full submarine cable to shore raises the cost from €0.062 to €0.076/kWh; in the North Sea it goes above €0.45/kWh. Sharing infrastructure with offshore wind is the main lever. | D7.4 §7.5.1 | fig21 (infographic) |
| 3 | Carbon and social footprint | Around 170,000 t CO₂-eq saved per plant over 25 years compared with coal-fired electricity; vessel fuel and cable length dominate the impacts. Social risk sits mainly in the solar-cell supply chain. | D7.3 Key results; D7.6 §4.2 and §4.4 | fig19 (chart; fix the CO₂ subscript first) |
| 4 | Open results and how to engage | Ten peer-reviewed publications, datasets and public deliverables in the SUREWAVE Zenodo community (with DOIs), webinar recordings, the technical brochure (D8.3), the remaining development steps (open-sea pilot, North Sea hinge iteration, qualification) and the partner contact list. | KPI verification file §1, §5, §12; Zenodo snapshot; D8.3 §11 and "Talk to us" | asset-solar-floating.jpg (real Sunlit Sea photo, no breakwater) |

## Fix before publishing

1. Cable cost. D8.3 §9 says a dedicated 20 km connection gives €0.09–0.11/kWh; D7.4 §7.5.1 gives €0.076/kWh for a full submarine cable in the Mediterranean. Newsletter V uses D7.4; D8.3 should be aligned or the difference explained.
2. Circular concrete economics. D8.3 says the circular formulations work "without penalising the economics"; D7.4 finds that switching to an HPC-based breakwater increases the LCOE and that conventional breakwaters remain preferable on cost. Newsletter IV makes no economic claim for the circular concrete.
3. Mediterranean IRR. D7.4 states 10.7 % in its summary and 10.6 % in its results table; the final technical report uses 10.6 %. The newsletter omits IRR; if added, use one figure consistently with the final report.
4. Gijón figures. The field-exposure results come from D8.3 and the final technical report working copy; D6.4 is not yet available. Confirm with ACCIONA and Ceit before Newsletter IV goes out.
5. Carbon figure. D7.3 gives around 170,000 t for the reference plant, more than 180,000 t for the North Sea ring layout and more than 160,000 t for the North Sea split layout. Use "around 170,000 t" with "reference plant".

## Images and material to request

- Lab photos of the concrete tests (ACCIONA, SINTEF) and a close-up of fouling on the prototype (ACCIONA).
- A photo of the SINTEF hinge test rig.
- Do not use fig01 or fig03 (AI renders of the full-ring open-sea plant) in any issue. Label AI-generated figures (fig14, fig18, fig23, fig24) as illustrations.

## Not included

- The nearshore and Gotland strategy and the KER1 business details (not public; D8.4 is Sensitive).
- Ceit's 2022 ultrasound sensor paper (funded by WATEREYE, not SUREWAVE).
- Consortium-meeting news and general EU policy summaries (low value to all four readers).
