# T150 round 4: D8.4 checked by each non-lead partner's exploitation manager

Persona: the exploitation manager of ACCIONA, Clement Germany, SINTEF, MARIN, Ceit and IFEU, one at a time. Method: I read `scratchpad_t150/d84_merged.md` (1,595 lines, after the round-3 integration) end to end, annexes included. I checked every passage that names a partner against that partner's exploitation summary, the deliverables it led, the Grant Agreement task and deliverable tables, the Crossref abstracts in `scratchpad_t150/crossref/`, the Energies 19(7) full text, D1.8, the EIC Transition proposal, Clement's D8.3 review and the WP8 KPI record. I did not use the final technical report working copy as a source (D22). "l.N" means a line in `d84_merged.md`. Repo paths are relative to `C:\dev\src\sure-d61`.

## Round 3 partner findings: status

Fixed in the text and checked:

- 1 (no full ring in the basin), at l.335, l.378, l.386, l.391, l.414, l.847, l.1037 and l.1306.
- 2 (D5.5 is Ceit's), at l.1056.
- 3 (Ceit's nodes in MARIN's basin tests), at l.300, l.344 and l.1060.
- 4 (D7.2 rating of Clement's components), at l.297, l.336 and l.959.
- 6 (D1.8 qualifier), at l.1120.
- 7 (DIFFRAC validated against the second campaign), at l.299, l.402 and l.1031.
- 8 (hinge loads attributed to D7.2), at l.403 and l.436.
- 9 (MARIN's NaturSea-PV kick-off talk), at l.221.
- 10 (axial loads up to 20 %), at l.1029.
- 12 (CIRCWIND and SFI BLUES roles), at l.1201–1202.
- 13 (SFI BLUES action no longer "continuing"), at l.1014.
- 14 (GEOPON condition), at l.1204 and l.1299.
- 15 (D5.1 takes its sea states from D2.1), at l.377.
- 16 (full D7.3 finding), at l.936.
- 17 (D4.2 mechanical conclusions), at l.934.
- 18 (D4.1 density aim), at l.338 and l.926.
- 19 (D7.4 caveat), at l.296, l.693 and l.938.
- 21 (extension linked to the Gijón exposure), at l.940. The wording waits for owner question Q82.
- 22 (UHPFRC in D8.5), at l.337.
- 23 (ACCIONA at the NaturSea-PV webinar), at l.183 and l.1412.
- 24 (IFEU offer), at l.395 and l.1096.
- 25 (IFEU Task 8.1), at l.354, l.1085 and l.1429.

Only partly fixed:

- 5 (Clement's EUPI-PV role). The condition on Sunlit Sea is gone, but a new condition on Clement's own participation has taken its place, and it conflicts with the facts file. See finding 1.
- 11 (MARIN's observation cited to D8.3). The first-campaign context was added. The claim of no buckling in the second campaign still rests on D8.3 alone. See finding 2.

## Do the earlier rejections in the partner area still hold?

| Rejection | Holds? | Reason |
|---|---|---|
| rejected_r3, r3disp_A #20: ACCIONA's summary dated 26 November 2025 | Yes | `surewave/background/2025-11-26_acciona_exploitation_and_media_email.md` l.10: "I have just uploaded ACCIONA's expected exploitation summary" |
| rejected_r3, r3disp_E on r3_partners#6: "no such contribution has been documented" | Yes | D1.8 asks for a confirmation and does not record that no contribution exists. 7.4 now has the confirmation step |
| rejected_r2, r2disp_C on r2_partners#M3 (validation against the second campaign) | Yes | Energies 19(7) l.122 |
| rejected_so_far: 1,030 mixtures (S3), 87 %/97 % (S4), installed cost (M3), prototype built to Clement's geometry (C2), 19 risk indicators | Yes, in part | The first four figures still appear only in the final technical report working copy (D22). "19 risks" is now sourced to the Preprints 202611.1173 abstract ("Nineteen technological risks were evaluated"), as D44 allows |
| D4/D4r: Ceit not named among the inputs to the hinge redesign | Yes | D5.3 l.1004 shows that Ceit's assessment concerned the breakwater. 7.4 l.1160 gives D1.8's wording and adds that fact |
| D3: no "factor 2–3" | Yes | 6.5 gives D5.1 Table 9 in per cent. The figures match Table 9: −34 %, −42 %, −56 %, −59 %; Baltic ×3.16 and ×2.05 |
| r1disp_D writing#6 (EDP not anonymised), r1disp_B 9 / B#88 / 24 / F5 | Yes | These follow D10, D16 and D22 |

## Findings

### 1 – minor – Clement Germany – the EUPI-PV row makes Clement's breakwater role conditional on Clement taking part (6.3 action plan, l.983)

Quote: "Breakwater for the nearshore demonstration in the EUPI-PV proposal coordinated by SINTEF, if Clement Germany takes part and the proposal is funded".

What is wrong: The facts file records that the breakwater "is funded through and supplied by Clement Germany" in this SINTEF-coordinated application. Section 10 (l.1206) lists "Clement Germany proposed for the breakwater" without a condition. Only Sunlit Sea's participation is undecided. The round-3 fix moved the condition from Sunlit Sea onto Clement. A Clement reader would read this as doubt about its own commitment, which no source expresses. The row is also inconsistent with Section 10 (requirement 6).

Source: `scratchpad_t150/companions/project_facts.md` l.42 ("the breakwater is funded through and supplied by Clement Germany (Eirik 2026-11-23)"); D8.4 l.1206.

Fix: "2027–2029 | Breakwater for the nearshore demonstration in the EUPI-PV proposal coordinated by SINTEF, in which Clement Germany is proposed for the breakwater, if the proposal is funded (added by the WP8 lead, Section 10) | Breakwater installed". Owner question Q66 can then be closed, or kept only for whether the breakwater work goes ahead if Sunlit Sea does not join.

### 2 – minor – MARIN – "no measurable hinge buckling or snap loading" in the second campaign is still sourced only to Sunlit Sea's brochure (4.1 l.402)

Quote: "No measurable hinge buckling or snap loading was observed (D8.3)."

What is wrong: This is a basin-test observation, and MARIN ran the tests. Its two papers do not state it. Energies 19(7) says only that the second series used "an improved connector design with higher compressive stiffness" (l.122) and "longer and thicker than the first generation" (l.70). The D8.3 paragraph that holds the claim (D8.3 l.200) also says that "the second campaign evaluated the redesigned hinge". Four lines earlier (l.378), D8.4 itself rejects that statement as wrong. A MARIN reader will not accept a finding about its own campaign that cites only a brochure, when the plan has corrected the same paragraph of that brochure.

Source: `surewave/background/2026-03-25_bunnik_hydrodynamic_simulations_2mw_offshore_solar_fpv.md` l.70, l.122; `surewave/deliverables/2026-09-28_surewave_d8.3_technical_brochure.md` l.200; D8.4 l.378.

Fix: If MARIN's D6.2 (public on Zenodo) states the observation, cite D6.2 (MARIN). Otherwise: "Sunlit Sea's brochure D8.3 reports no measurable hinge buckling or snap loading in the second campaign; MARIN's paper states that the connector had higher compressive stiffness (Energies 19(7) 1609)." Also send it to MARIN as an explicit check in the review round.

### 3 – minor – MARIN and Clement Germany – the trade-offs of the mooring optimisation are left out (6.5 l.1035; 3.4 R6 l.340; 4.10 l.854)

Quote: "Without exceeding proof loads, the optimised moorings have 34 % (Mediterranean) and 42 % (North Sea) less mooring-line mass …".

What is wrong: D5.1 states the cost of the mass reduction, and D8.4 omits it:

- The maximum fairlead tensions rise, by up to 2.46 times in Table 9 (Mediterranean 2 MW). D5.1 notes that "for most designs on the Pareto front, a mooring mass reduction comes with the cost of increased maximum tensions at the fairlead".
- D5.1 calls the tabulated optima "possible and somewhat subjective". It notes that, "following consultation with CLEMENT, it is not evident what weighting factors or cost function should be applied to these two design objectives".
- The 2 MW optimum exceeds the proof load by 1 kN (0.1 %), accepted within the uncertainty.

MARIN would want its result reported with the caveats it gave. Clement, which designs the mooring and anchoring (KER3), carries the higher fairlead and anchor loads. This bears on requirement 4 (evidence in full, nothing overstated) and on 4.10, where the mass reduction is the evidence against the proposal's −40 % mooring-cost target.

Source: `surewave/background/2024-04-16_surewave_d5.1.md` l.1484–1532 (Table 9, Tmax/Tproof and Opt/Ref rows), l.1536, l.1538.

Fix (6.5, after the D5.1 percentages): "The lighter moorings carry higher maximum tensions at the fairlead, up to about 2.5 times the reference value. D5.1 presents its optima as possible solutions on the Pareto front: after consultation with Clement Germany, the weighting between mooring mass and fairlead tension was left open." In 4.10, add after "D5.1 takes mooring-line mass as the measure of mooring cost": "; the fairlead and anchor loads rise in the optimised designs (Section 6.5)".

### 4 – minor – Ceit – a publication Ceit reported is excluded without being named (2.5 evidence paragraph, l.221; Annex A.1)

What is wrong: The WP8 tracker of 29 September 2026 lists a Ceit journal article, *Sensors* 25 (2025), doi 10.3390/s25196234, "Coating Thickness Estimation Using a CNN-Enhanced Ultrasound Echo-Based Deconvolution" (Perez-Diego, Thibbotuwa, Cortés, Irizar). The KPI check removed it because its funding statement names only the project WILLOW. D8.4 names the one MARIN item it does not count (the NaturSea-PV kick-off) but is silent on this one. Ceit's exploitation manager will count 11 publications in its own records and will not find out why D8.4 has 10. The same rule of disclosure should apply to every partner.

Source: `surewave/background/2026-09-29_surewave_wp8_kpis.md` l.35; `scratchpad_t150/companions/2026-11-19_surewave_wp8_kpi_verification.md` l.71.

Fix (2.5, after the NaturSea-PV sentence): "One publication reported by Ceit is not counted: the *Sensors* article of 2025 on coating-thickness estimation with ultrasound (doi 10.3390/s25196234), whose funding statement names only the EU project WILLOW."

### 5 – minor – IFEU – D7.6's preference for one large plant is given without its conditions (4.3.3 l.519)

Quote: "large uniform plants are preferred over five units of about 2 MWp for their lower material intensity."

What is wrong: D7.6 attaches two conditions to the preference: "if durability is supported by offshore experience and if shading of sensitive ecosystems is not an issue at the given location". It also assessed the split concept "for harsh conditions (i.e. North Sea) only". D8.4 makes IFEU's conditional finding unconditional and general. IFEU will correct this in review.

Source: `surewave/background/2025-11-05_surewave_d7.6_integrated_sustainability_report.md` l.159, l.483.

Fix: "…and one large uniform plant is preferred over five units of about 2 MWp for its lower material intensity, if offshore experience supports its durability and shading of sensitive ecosystems is not an issue at the site; D7.6 assessed the split layout for the North Sea only."

### 6 – minor – Clement Germany – Clement's leading roles in the EIC Transition proposal are understated (6.3 l.972; Section 10 l.1205 and l.1208)

Quotes:
- 6.3: "Clement leads the development, manufacture, deployment and operation of the breakwater and mooring, leads the work package for deployment, operation and validation (project months 15–34), confirms the permitting route …".
- l.1208: "The requirements task, led by Sunlit Sea within its site-characterisation work package, also evaluates a floating PV site of EDP in Portugal."

What is wrong: In the proposal, Clement also leads three tasks that D8.4 leaves out:

- Task 2.2, Site Characterisation and Metocean Design Basis: "CLEMENT will lead the assessment of Hainer See and the Portuguese site".
- Task 2.4, Breakwater and Mooring System Design.
- Task 5.2, Breakwater and Mooring Manufacturing, including the transition elements.

l.1208 names only Sunlit Sea's requirements task for the Portuguese site. Clement's assessment of both candidate sites is missing. This understates the evidence (requirement 4). Section 10's role cell for Clement is narrower than the proposal, while the cells for Sunlit Sea and SINTEF list their work packages in full.

Source: `generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md` l.337 (WP6 lead), l.373 (Task 2.2), l.383 (Task 2.4), l.431 (Task 5.2), l.252 (permitting).

Fix:
- 6.3: "In it, Clement leads the site characterisation and metocean design basis of the German baseline site and the Portuguese alternative, the design and manufacture of the breakwater and mooring (with the transition elements), and the work package for deployment, operation and validation (project months 15–34); it confirms the permitting route with the competent authority and provides access to the baseline site …".
- Section 10, Clement cell: "Clement Germany, leading site characterisation, breakwater and mooring design and manufacture, and deployment, operation and validation".
- l.1208: "Both candidate sites, the German lake and a floating PV site of EDP in Portugal, are assessed in the first six months: their site characterisation is led by Clement Germany and their requirements by Sunlit Sea."

### 7 – minor – SINTEF – the techno-economic article that D8.4 plans with SINTEF currently uses the superseded D7.4 figures (4.9 l.820; Section 13 KER1 target l.1285; Annex A.3 l.1348)

Quote (A.3): "A third manuscript, on the techno-economic assessment of the three SUREWAVE sea basins, by Sunlit Sea and SINTEF, is in preparation for an MDPI journal".

What is wrong: The manuscript draft of 19 November 2026 was last edited by SINTEF (B. Panjwani). Its abstract gives the D7.4 version 1.0 results: LCOE €62.2/MWh, NPV €8.98M, IRR 10.8 %. D8.4 states the version 2.0 results (€0.076/kWh, €7.3M, 15.6 %, l.668) and says why version 1.0 was corrected (l.672–681). A SINTEF co-author reading D8.4's plan to submit the article in 2027 should see that the article is to carry the version 2.0 figures. Otherwise a third public set of SUREWAVE economics would follow D8.3 and D7.6 (requirement 6).

Source: `surewave/background/2026-11-19_surewave_techno_economic_assessment_article_draft.md` l.1 and the abstract; D8.4 l.668, l.681.

Fix (A.3): "… is in preparation for an MDPI journal, to be based on D7.4 version 2.0, and is not counted." 4.9 2027 bullet: "The journal article on the SUREWAVE techno-economic assessment, by Sunlit Sea and SINTEF and based on D7.4 version 2.0, is submitted."

### 8 – minor – ACCIONA – ACCIONA's thermal-cycling tests are credited to SINTEF (6.2 l.934; 6.4 l.994)

Quotes:
- 6.2: "SINTEF tested shell–core beams cast by ACCIONA … Thermal cycling had a negligible effect on the beams … (D4.2, ACCIONA, with the tests by SINTEF)".
- 6.4: "it tested 25 HPC and 23 LWAC shell–core beams cast by ACCIONA in static and cyclic three-point bending, pull-out of the interface and impact".

What is wrong: D4.2 shows that the one-month thermal cycling, from −15 °C to +60 °C, was done in the climate test chamber at ACCIONA's R&D facilities. SINTEF then bend-tested the cycled beams. Read together, the 6.2 sentences credit the whole beam programme to SINTEF. ACCIONA will ask for its share of the work. 6.4 is correct as written, since it does not list the thermal cycling.

Source: `surewave/background/2024-07-31_surewave_d4.2_lab_testing_breakwater_prototype.md` l.541 (25 HPC and 23 LWAC beams sent to SINTEF), l.691 and l.700 (climate chamber at ACCIONA).

Fix (6.2): "SINTEF tested shell–core beams cast by ACCIONA from the HPC and LWAC (Section 6.4), among them beams that ACCIONA had first subjected to a month of thermal cycles between −15 °C and +60 °C in its climate chamber. … Thermal cycling had a negligible effect …".

### 9 – minor – SINTEF – the requirement that the first-generation hinge failed to meet is missing (4.1 l.399; requirement 4)

Quote: "In SINTEF's laboratory tests, complete hinges reached a mean tensile load of 3.69 kN and buckled at low compressive loads (D6.1; Preprints 202611.1612)."

What is wrong: D6.1 sets the result against a requirement: "Relatively low ultimate strength (Average 3.5 kN), while a load of around 8–10 kN are expected from the work carried out in WP5". It "highly recommended to redesign these hinges, to at least meet the requirements in terms of ultimate strength". This is the basis for the redesign. Without it the reader cannot judge 3.69 kN, nor the later 8.36 kN segment and the 37 kN design value. SINTEF's own recommendation is the trigger of the KER1 hinge story, and it is missing.

Source: `surewave/background/2024-09-12_surewave_d6.1_ultimate_strength_capacity.md` l.467, l.773, l.777.

Fix (append to the first-generation bullet): "D6.1 compares this with the 8–10 kN expected from the WP5 simulations and recommends a redesign that at least meets that requirement and avoids the collisions that the low compressive strength can cause."

### 10 – wording – MARIN – "the basin-test method … is published" without D1.8's know-how position (7.2 KER5 l.1134)

Quote: "The basin-test method with elastically scaled hinges is published."

What is wrong: MARIN's input confirms that the method was "communicated publicly through a journal paper". D1.8 Table 2, however, records MARIN's "hydrodynamic models and basin-testing methods" as "partner-specific models, experimental methods, and know-how". As written, the cell can be read as saying that the method is free for anyone to use.

Source: `surewave/background/2026-09-30_surewave_d1.8_ipr_management_plan_m36.md` l.280; MARIN summary l.29.

Fix: "The basin-test method with elastically scaled hinges is published (Energies 17(9) 2059); the experimental know-how for applying it stays with MARIN (D1.8)."

### 11 – wording – Ceit – the KER6 maturity cell claims more validation against ABS and DNV than D5.7 gives (3.2 KER6 l.300, against R9 l.343)

Quote: "Finite element, crack-propagation and SHMS methods validated against the guidance of the classification societies ABS … and DNV (D5.7, Ceit)."

What is wrong: In D5.7, the finite element models were benchmarked against the ABS and DNV guidance. The crack-propagation simulations "were validated using established fracture mechanics laws and external experimental studies". The SHMS procedure was compared step by step with the ABS structural-health-management procedure. R9 (l.343) states the crack-propagation validation correctly, so the two cells disagree.

Source: `surewave/background/2025-09-05_surewave_d5.7_modelling_tools_validation.md` l.91, l.261, l.651.

Fix: "Finite element models benchmarked against ABS and DNV guidance, crack-propagation algorithms validated against established fracture-mechanics laws and external experimental studies, and the SHMS procedure checked against the ABS procedure (D5.7, Ceit)."

### 12 – wording – Ceit – the market line adds a customer group Ceit did not name (6.6 l.1054)

Quote: "Ceit names the aeronautics sector, owners of civil and marine reinforced-concrete structures, and end users and technology integrators."

What is wrong: Ceit names applications (aeronautics, "civil / marine reinforced concrete") and partners ("potential end users and technology integrators", "industrial partners"). It does not name owners of structures as customers. Section 6's own rule is that the market line gives "the customers the partner names now" (l.889).

Fix: "Ceit names industrial end users and technology integrators in aeronautics and in civil and marine reinforced-concrete monitoring, and industrial partners for co-developed SHMS tools."

### 13 – wording – SINTEF – GEOPON: "planned" where SINTEF writes "continued use" (KER4 cell l.298; 6.4 l.1013)

Quotes: KER4: "DIC planned for a national project with GEOPON"; 6.4: "a planned national project with GEOPON".

What is wrong: For the testing and DIC methods, SINTEF's summary table reads "Continued use in projects involving GEOPON and other industrial partners". Its text reads "will support collaboration with GEOPON" (SINTEF plan l.36, l.62). SINTEF's own wording mixes the present and the future, and D8.4 picks one reading. This is a minor difference, but SINTEF will see it.

Fix (KER4 cell): "DIC to be used in SINTEF's collaboration with GEOPON (a nationally funded project, planned)". Keep 6.4 as is and point to Section 10.

### 14 – wording – MARIN and SINTEF – "fitted in pairs" is cited to MARIN's paper, which does not say it (4.1 l.402; 6.5 l.1037)

Quote (4.1): "MARIN's second campaign used second-generation connectors, longer and thicker than the first generation, with higher compressive stiffness, fitted in pairs between adjacent floats (Energies 19(7) 1609, 2026)."

What is wrong: Energies 19(7) gives "longer and thicker" and "higher stiffness" (l.70, l.122). The pairing comes from SINTEF's risk assessment ("the paired generation-v2 configuration", Preprints 202611.1173 abstract) and from decision D46.

Fix: "(Energies 19(7) 1609; the pairing as in D7.2, Preprints 202611.1173)". Make the same change in 6.5.

---

Findings: 0 major, 9 minor, 5 wording.
