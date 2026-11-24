---
internal_title: SUREWAVE Newsletter III — sources and figure provenance
internal_date: 2026-11-20
---

# SUREWAVE Newsletter III — sources and figure provenance

Companion to `2026-11-20_surewave_newsletter_iii.md`. Every figure and factual claim in the newsletter, with the deliverable section it comes from. All files are under `surewave/background/` unless the path says otherwise. Checked on 20 November 2026.

## Text

| Newsletter claim | Source |
|---|---|
| Preliminary tests on a string of six FPV floats at the Stadt Towing Tank, Norway | D8.3 §6 "Basin testing" (`deliverables/2026-09-28_surewave_d8.3_technical_brochure.md`) |
| Two system-level campaigns at the MARIN basin, Wageningen; 1:10-scale model with breakwater units, FPV modules, PU hinges, transition elements, mooring; quantities measured; operational and survival conditions | D8.3 §6 "Basin testing" |
| First campaign with and without breakwater; short-period wave energy attenuated | D8.3 §6 "Basin testing" |
| FPV motions reduced by factors of about 2–3 in the relevant frequency range; maximum local slamming pressure about 126 kPa; structural assessment found no threat to the breakwater's integrity | Final technical report working copy, WP6 Task 6.4, citing D6.2 (`surewave/archive/t146/2026-11-19_surewave_final_technical_report_working_copy.md`) |
| Original hinges buckled under compression and snapped back; consistent with component tests; led to the redesign | D8.3 §6 "Basin testing" |
| Second campaign with redesigned hinge: no measurable buckling or snap loading | D8.3 §6 "Basin testing" |
| Data from the first campaign on Zenodo, doi:10.5281/zenodo.10960432 | Bunnik et al. 2026, Data Availability Statement: "Basin test data from [27]", where [27] is the 2024 Energies paper on the first campaign (`2026-03-25_bunnik_hydrodynamic_simulations_2mw_offshore_solar_fpv.md`); DOI resolves (checked) |
| Corner hinges of the Generation 1 floats failed at a mean of 3.69 kN in tension; 8–10 kN operational loads expected; low compressive resistance | D6.1 Conclusions ("Relatively low ultimate strength (Average 3.5 kN)… a load of around 8-10kN are expected"); D8.3 §6 "Component-level" |
| Redesign by Sunlit Sea, second round of tests at SINTEF; the redesigned connection more than doubled the tensile capacity; buckling strength about 20 kN | Final technical report working copy, WP6 Task 6.2 ("from approximately 3.69 kN to 8.36 kN … more than twice the tensile capacity of the original hinge"); D6.3 Conclusions (buckling "around 20 kN"). D6.3 says "almost 3 times" on its 1/5 component scale and D8.3 "approximately three times"; "more than doubled" is consistent with all sources |
| Highest stress reached in the tests, about 11 MPa, used as a conservative value; extrapolated life 2.5 × 10^11^ cycles against 7.88 × 10^8^ for 25 years; "rough first estimate" | D6.3 fatigue section ("maximum calculated stress of 11.09 MPa … using this stress value as a conservative value"; "approx. 2.5e+11"; "7.88e+8 cycles"; "this is a very rough fatigue estimation"). D8.3 calls it the "design operational stress", which D6.3 does not support |
| Shrinkage during casting left gaps of 1–2 mm between the mating parts; strict quality control in series production | D6.3 ("significant shrinkage which induced significant gaps (around 1-2mm) between the male and female parts"); D8.3 §6 "Component-level" |
| Full-hinge ULS 37 kN under 50-year design storms; Baltic 34 kN, Mediterranean 33 kN, North Sea 40 kN; further iteration needed for the North Sea; loads computed for a 2 MWp farm | D8.3 §6 "Component-level" only; no primary SINTEF/MARIN report with these values is in the repo. Confirm in the partner check |
| Steel-wire connections between breakwater units failed at 402 kN on average, rated 450 kN | D6.1 (Table 10 and text: "average value of 402 kN … rated capacity of 450 kN"; failure either at the socket fixation or in the wire, hence "failed" rather than "broke") |
| Breakwater-to-FPV connection: mean 41 kN at failure, low scatter (standard deviation 2.2 kN), requirement 42 kN | D6.1 (Table 11 and text) |
| The rope always failed, as expected | D6.1 ("the connection always failed in the ropes, which are the weak point of the assembly, and which is expected") |
| DIFFRAC extended to run on a supercomputer; 2 MWp farm of 3,660 FPV modules inside a ring of 32 interconnected floating breakwaters; validated against basin tests | Bunnik et al. 2026, Abstract and §4 |
| Average axial loads reduced by up to 20 % in steep irregular seas; vertical loads and overturning moments reduced by up to 50 % for waves at an angle to the array; standing waves raise loads locally | Bunnik et al. 2026, §5.3 ("some increase in Fz and Mx loads for normal incident waves … clear reduction for 45 deg waves … reduce by 50%") and §7 |
| "It is not evident that these reductions outweigh the additional costs for material, mooring, installation and decommissioning"; damping estimates and validation data for larger farms as next steps | Bunnik et al. 2026, §7 |
| Paper citation: Bunnik, Baderiya, van der Zanden, Energies 19(7), 1609 (2026), doi:10.3390/en19071609 | Crossref record; KPI verification file §1 |
| D6.1 on Zenodo: doi:10.5281/zenodo.22830589; D6.2 basin test results: doi:10.5281/zenodo.22660916 | Zenodo community snapshot (`2026-11-19_surewave_zenodo_community_snapshot.md`); DOIs resolve (checked) |
| Energies 17(9) 2059 (2024), doi:10.3390/en17092059; MARINE 2025, doi:10.23967/marine.2025.163 | KPI verification file §1; DOIs resolve (checked) |
| Project end 31 December 2026 | `docs/project_facts.md` (SUREWAVE entry) |
| Coordinator Balram Panjwani, SINTEF, and contact address | Newsletters I and II (coordinator contact); surewave.eu (contact post@sunlitsea.no) |

## Figures

| Figure | File | Provenance | Notes |
|---|---|---|---|
| 1 | `surewave/images/2026-09-28_surewave_d8.3_technical_brochure_lowres/fig12.png` | Real wave-basin photograph; location not confirmed (figures companion, Fig 12 revision: "loads on individual breakwater units") | Caption describes only what is visible and does not name the basin. Ask MARIN in the partner check whether it is theirs. |
| 2 | `surewave/images/2026-11-18_clement_d8.3_figure_inputs/moored_ring_with_pv.png` | CAD graphic by Clement Germany | Shows the open-sea reference plant (larger ring). Caption states that the simulated 2 MWp farm uses a smaller ring of 32 breakwaters; no nearshore claim is made next to it. |

## Partner check before publication

- MARIN (Joep van der Zanden): basin-campaign item and the 2 MWp simulation item.
- SINTEF (Virgile Delhaye): hinge and connection test items.
- Request mail drafted in the T153 solution note; not sent.

## Removed after review

- Brochure fig14 (hinge geometry and force–displacement plot) was dropped. Its curves are AI-drawn from a prompt (figures companion, Fig 14) but the legend labels them "measured", and the drawn redesign peak (about 10 kN at 25 mm) is not stated in D6.3. The same figure is in D8.3 and should get a "schematic" label there.

## Issues found in D8.3 during this check

- Fig 14 legend says "measured" for AI-drawn curves (see above).
- §6 calls the 11 MPa fatigue stress the "design operational stress"; D6.3 uses it as a conservative peak.
- §6 says the breakwater-to-FPV connection "met its 41 kN requirement"; D6.1 measured 41 kN against a 42 kN requirement.
