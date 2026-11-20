---
internal_title: SUREWAVE Newsletter IV — sources and figure provenance
internal_date: 2026-11-20
---

# SUREWAVE Newsletter IV — sources and figure provenance

Companion to `2026-11-20_surewave_newsletter_iv.md`. Every figure and factual claim, with the deliverable section it comes from. Files are under `surewave/background/` unless the path says otherwise. Checked 20 November 2026.

## Text

| Newsletter claim | Source |
|---|---|
| ACCIONA developed three mixes with recycled and by-product materials | D4.1 Conclusions (`2024-01-18_surewave_d4.1_design_characterization_circular_materials.md`) |
| HPC 128 MPa against 120 MPa target; 18 % of cement replaced by GGBFS and fly ash | D4.1 Conclusions, HPC ("Sample 2 … 128MPa … 18% by weight of cement was replaced by by-products GGBFS and FA") |
| LWAC: recycled-glass lightweight aggregate replaces all natural lightweight aggregate; recycled concrete replaces 20 % of natural coarse aggregate; the mix that met all requirements reached 49 MPa; the low-carbon-cement version, used for the prototype top slab, reached 68 MPa at a higher density | D4.1 Conclusions, LWAC ("100% of natural lightweight aggregates … replaced by Minolite recycled lightweight aggregate"; "20% by volume of natural coarse aggregate was replaced by recycled concrete aggregate"; Sample 17 "49MPa … 1898 kg/m3 … comply with the requirements"; Sample 18 "green cement … 68 MPa", density "near 2000 kg/m3"; Sample 18 used in the prototype top slab per D8.3/D4.3). Density deliberately not stated: D4.1 gives "near 2000 kg/m³" for Sample 18, D8.3 "approximately 1800 kg/m³" |
| Cellular core 365 kg/m³ against about 300 kg/m³ target; recycled-glass aggregate; 80 % less cement than ordinary non-structural concrete | D4.1 Conclusions, cellular concrete ("Sample 26 … 365 kg/m3"; "80% less cement than non-structural normal concrete (25kg/m3 vs minimum 150kg/m3)") |
| All shell mixes high water and chloride resistance after 28 days; no water penetrated HPC | D4.2 Conclusions (`2024-07-31_surewave_d4.2_lab_testing_breakwater_prototype.md`) |
| Waterproofing admixture: LWAC water penetration 8.2 mm → 0.6 mm; chloride diffusion coefficient halved | D4.2 Conclusions ("LWAC-CEM III+KRY was 0.6mm compared with 8.2mm for LWAC-CEM III, and a reduction of 50% of the chloride diffusion coefficient"). Product name omitted, as in D8.3 |
| Sandwich beams tested in static and cyclic bending, pull-out, drop-tower; HPC more than 55 % stronger, about 50 % better strength-to-weight, best under impact; thermal cycling negligible; pull-out weak because the cellular core is a filler; HPC chosen for the shell | D4.2 Conclusions |
| Prototype 3.40 × 1.70 × 1.05 m; HPC bottom slab and walls, LWAC top slab, cellular core, buoyancy blocks; built at ACCIONA's workshop | Final technical report working copy, WP6 Task 6.5 (dimensions); D8.3 §6 "Reduced-scale prototype" (composition, workshop) |
| Installed September 2025 at ACCIONA's maritime demonstration site in El Musel port, Gijón; four-line catenary mooring with gravity anchors; in the water until June 2026 | Final technical report working copy, WP6 Task 6.5 ("installed in September 2025 … remained exposed until June 2026"); D8.3 §6 |
| Inspection findings (operation throughout; fouling > 85 %, up to 35 mm, 6.3–9.7 kg/m², within 0.06 m allowance; chloride < 0.6 % by mass of cement at rebar depth; HPC wall rebar sound; corrosion potentials = saturated concrete; elevated chloride and possible pitting only near openings in the LWAC top slab, no measurable rebar loss; deck openings the critical detail) | D8.3 §6 "Reduced-scale prototype", nine-month conclusions; final technical report working copy, WP6 Task 6.5. D6.4 is not in the repo — confirm with ACCIONA and Ceit |
| SHMS combines FE stress fields, crack growth and degradation data; compares materials, relates degradation to remaining capacity, identifies critical crack orientations, recommends inspection intervals (four-year cycle plus event checks); runs on model-generated degradation data, built for real sensor data | D5.6 Conclusions (`2025-06-13_surewave_d5.6_shms_demo.md`); D8.3 §7 |
| Eddy-current sensor resolves about 0.17 mm material loss in the laboratory | D5.4 Conclusions (`2024-09-30_surewave_d5.4_monitoring_strategy.md`: "resolution of approximately 0.17mm") |
| At Gijón: signal affected by temperature, moisture, wetting–drying; within ±135 Ω after compensation; field detection remains to be demonstrated; accelerometers reliable, 0.35–0.45 Hz matched natural frequencies; sealing the main weakness | D8.3 §6 nine-month conclusions; final technical report working copy, WP6 |
| DOIs: D4.3 10.5281/zenodo.22830370; Sensors 24(13) 4211; Electronics 13(22) 4485; FFEMS 10.1111/ffe.70435; dataset 10.17632/sdxwvmrk3t.1 | Zenodo snapshot; KPI verification file §1; all five resolve (checked 20 Nov 2026) |

## Figures

| Figure | File | Provenance | Notes |
|---|---|---|---|
| 1 | `surewave/images/2026-11-18_clement_d8.3_figure_inputs/breakwater_sections.png` | CAD graphic by Clement Germany | Same figure and caption basis as D8.3 §4; no material labels (Clement decision) |
| 2 | `surewave/images/2026-09-28_surewave_d8.3_technical_brochure_lowres/fig15.png` | Real photograph (ACCIONA footage, low resolution) | Shows the prototype at El Musel |

Not used: fig17 (SHMS screenshot) — its "hinge force" axis shows about ±1,500 kN, which readers would compare with the 37 kN FPV hinge in Newsletter III; fig18 (AI illustration of the sensor).

## Partner check before publication

- ACCIONA (Aurora María Casado Barrasa): materials, laboratory tests, prototype and Gijón results.
- Ceit (Ainhoa Cortés, Aritz Dorronsoro): SHMS, corrosion sensor and accelerometer results.

## Changes after review (2026-11-20)

Two review agents (layout; fact and label check). Applied: LWAC strength stated as 49 MPa for the compliant mix and 68 MPa for the low-carbon version (D4.1); pull-out weakness attributed to the core material, not the bond (D4.2: "attributed to the inherently low mechanical properties of the core cellular concrete rather than the interfaces"); harbour caveat added and title changed from "at sea" to "the water" (final technical report working copy: "the exposure site did not continuously reproduce the most extreme design conditions"); Figure 1 caption states the full-scale design and the enlarged transverse section; Figure 2 credited "Photo: ACCIONA"; chloride bullet starts "Elsewhere in the structure", corrosion readings located in the tidal and submerged zones and explained in plain words; deck-opening finding softened to "points to … the detail that most needs attention"; 0.17 mm qualified as laboratory tests with simulated material loss; biomass located on the side surfaces; ±135 Ω number replaced by "stayed stable"; growth allowance in mm; "at all" removed; shell types named in the beam tests; heading "Monitoring the structure over its life"; system name in lower case; lead line under "Open results"; forced page break removed (issue stays at 3 pages).
