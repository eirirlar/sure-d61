# T150 round 3: check of D8.4 by each non-lead partner's exploitation manager

Persona: the exploitation manager of ACCIONA, Clement Germany, SINTEF, MARIN, Ceit and IFEU, one at a time. Method: I read `scratchpad_t150/d84_merged.md` end to end and checked every mention of each partner, the annexes included, against that partner's exploitation summary, the KPI partner responses, the deliverables it led, the Crossref abstracts in `scratchpad_t150/crossref/` and the Energies 19(7) full text in the repo. I did not use the final technical report working copy as a source (D22). "l.N" means a line in `d84_merged.md`. Repo paths are relative to `C:\dev\src\sure-d61`.

## Round 2 partner findings: status

All round 2 partner findings are in the text except these two:

- E1 (Ceit's WP5 deliverables) is only partly fixed. r2disp_E dropped D5.5 on the grounds that "D5.5 is SINTEF's". That premise is wrong (finding 2).
- M3 was rejected in round 2. The rejection holds: Energies 19(7) 1609, Section 4 (`surewave/background/2026-03-25_bunnik_hydrodynamic_simulations_2mw_offshore_solar_fpv.md` l.122), says the motions measured in the second campaign were used for validation.

Fixes I checked and found correct:

- ACCIONA: A1–A9 (D6.4, Task 6.5, the LWAC bullet, the CEM III wording, the contributing beneficiaries, the D7.4 caveat, the prototype named in the executive summary, 4.10 and 15, the D4.1 trial-mix record).
- Clement Germany: C1–C9.
- SINTEF: S1–S8.
- MARIN: M1, M2, M4, M5.
- Ceit: E2–E5.
- IFEU: F1–F4.

## Do the earlier rejections still hold? (partner area)

| Rejection | Holds? | Reason |
|---|---|---|
| rejected_so_far, r1disp_C on r1_cold#3: "FIXED – 4.1: basin campaigns tested the full ring". r2_coord l.223 accepted it: "Energies 17(9) 2059 and 19(7) 1609 support the wording" | No. The fix is factually wrong | Both papers describe a 1:10 model of a 3 × 5 (5 × 3) module array with one floating breakwater across the width of the basin. The full ring was only simulated. See finding 1 |
| r2disp_C on r2_partners#M3 (validation against the second campaign) | Yes | Energies 19(7) l.122 |
| r2disp_E on r2_partners#E1: "D5.5 is SINTEF's, so 'D5.3–D5.7' was not used" | No | GA l.5099: "D5.5 … Lead Beneficiary 3. Ceit". Annex B (l.1520) and R9 (l.336) of the draft say the same. See finding 2 |
| rejected_so_far: 1,030 mixtures (S3), 87 %/97 % (S4), final-report installed cost (M3), "prototype built to Clement's geometry" (C2) | Yes | Still found only in the final technical report working copy (D22) |
| Ceit left out of the hinge redesign (D4/D4r; several dispositions) | Yes | D1.8 l.85, l.465 and l.497 credit Ceit's finite element work in the hinge development. D5.3 l.1004 shows that this work concerned the breakwater and only announced the new-hinge modelling. The 3.1 bullet (l.264) now states this fairly |
| r1disp_C C#14 and D3: no "factor 2–3" | Yes | 6.5 gives MARIN's chain-mass ratio fairly (l.1002) |
| r1disp_D writing#6 (EDP not anonymised) | Yes | |
| r1disp_B 9, B#88, 24 and F5/36 (ACCIONA articles, BayWa, EERA year, ISNRE) | Yes | These follow D10, D16 and D22 |
| r1disp_E cinea#10 and coord#29 (IP workshops; EUPI-PV status) | Yes, for now | Submission-day items |

---

## Findings

### 1 – major – MARIN and Clement Germany – the basin campaigns did not test a full ring (4.1 l.407; also l.384 and l.328)

Quotes:
- l.407, configurations table: "Breakwater shielding of the array tested in the SUREWAVE basin campaigns, in a full ring; … directional layout not yet tested".
- l.384: "The breakwater classes … and a directional layout, with a breakwater only on the exposed side, have not been tested."
- R1 evidence, l.328: "two 1:10 campaigns of the integrated system at MARIN".

What is wrong: MARIN's two campaigns used a down-sized model. It was a 3 × 5 array of modules, tested with and without one floating breakwater that spans the width of the rectangular basin, in normal and oblique waves. The ring of 32 or 56 breakwaters was only analysed numerically (D5.1; Energies 19(7) 1609). A MARIN reader would reject "in a full ring". A Clement Germany reader would point out that the tested arrangement, a straight breakwater on the wave side of the array, is closer to a one-sided layout than to the ring. The draft says that the one-sided arrangement is untested, and this misreports MARIN's work.

Sources:
- Energies 17(9) 2059, abstract (`crossref/10.3390_en17092059.json`): "Tests of a 5 × 3 FPV matrix are performed, with and without shelter, by external floating breakwater … for oblique incidence".
- Energies 19(7) 1609, l.122: "wave basin tests at geometric scale 1:10 of a simplified, down-sized version of the FPV farm, comprising a 3 × 5 array of FPV modules with an FBW that covers the width of the rectangular basin … The FBW and FPV model, basin setup, environmental conditions and data analysis were the same in both test series".
- D5.1 l.862 and l.1174: the 56- and 32-breakwater rings were simulated.

Fix:
- l.407 Status cell: "Breakwater shielding tested at 1:10 in MARIN's two basin campaigns: a 3 × 5 module array behind a straight breakwater section spanning the basin, in normal and oblique waves (Energies 17(9) 2059; Energies 19(7) 1609). The ring was analysed numerically (D5.1; Energies 19(7) 1609). Breakwater classes sized on the desk (Section 4.1.1). Directional layout at plant scale not yet tested. Integrated system at TRL 4–5 (above)".
- l.384: "The breakwater classes for nearshore sites (Section 4.1.1) have not been tested. Neither has a directional layout at plant scale, with a breakwater placed across the exposed sector of a full array. The basin campaigns tested a small array behind a straight breakwater section."
- R1 evidence (l.328): "two 1:10 campaigns at MARIN of a down-sized integrated system, a 3 × 5 module array behind a breakwater section (D6.2, MARIN; …)".

The same correction belongs in the companion exploitable-results report wherever it says the ring was tested.

### 2 – minor – Ceit – D5.5 is left out of Ceit's WP5 deliverables (6.6, l.1022)

Quote: "Ceit led WP5 … with its deliverables D5.3, D5.4, D5.6 and D5.7".

What is wrong: D5.5, Fatigue crack propagation algorithms, is Ceit's. The GA (l.5099) and the WP index (l.116) say so. The draft itself agrees in Annex B (l.1520) and in R9 (l.336, "D5.5 (2025), D5.7 (2025), both Ceit"). r2disp_E dropped it in error. D5.5 holds the 598 simulations that the draft cites (D5.5 l.527). Ceit's crack-propagation tool is one of its two exploitation routes.

Fix: "Ceit led WP5, the predictive modelling and simulation tools for material properties and structural integrity management, with its deliverables D5.3 to D5.7 (the structural integrity assessment, the monitoring strategy, the fatigue crack propagation algorithms, the SHMS demonstrator and the validation report), and the sensing and monitoring task of the technical validation work package (Task 6.1). Within WP5, D5.1 is MARIN's and D5.2 SINTEF's."

### 3 – minor – Ceit – Ceit's sensing in MARIN's basin tests is not credited (6.6, KER6 l.293, R10 l.337)

What is wrong: Ceit leads Task 6.1, "Advanced sensing & monitoring solutions for basin tests and concrete component" (WP index l.128). The draft names the task but describes only the work at Gijón. The Electronics paper, which the draft lists only as evidence for R10, reports Ceit's UWB wireless accelerometer nodes. They were compared with a wired reference system and assessed in the SUREWAVE wave-basin tests at MARIN ("These tests have provided a valuable opportunity to assess the effectiveness of the proposed Sensor Node", abstract, `crossref/10.3390_electronics13224485.json`, co-authored with MARIN). Ceit also co-authored the first basin-campaign paper (Cortés, Energies 17(9) 2059). R10 of the proposal asks for validation "against basin-model tests". This is the closest the record comes to that, and the draft does not say so.

Fix, in 6.6 after the Gijón paragraph: "Ceit's wireless UWB accelerometer nodes were checked against a wired reference system in the laboratory and assessed in MARIN's SUREWAVE wave-basin tests (Electronics 13(22) 4485, 2024, with MARIN)." KER6 maturity cell: add "accelerometer nodes assessed in MARIN's basin tests (Electronics 13(22) 4485)". R10 maturity cell: "accelerometer nodes assessed in the basin tests; sensor and accelerometers operated about nine months at Gijón; …".

### 4 – minor – Clement Germany – the risk assessment's rating of Clement's components is not reported (KER3 l.290, 6.3, 3.3)

What is wrong: SINTEF's technological risk assessment, as summarised in D7.6, rates Clement's mooring lines, the surface mooring and the breakwater connections as high-TRL components. It finds reliable performance at all three sites (D7.6 l.685: "high-TRL components such as mooring lines, surface mooring systems, and breakwater connections showing reliable performance across all sites"; l.759). The preprint abstract adds: "Most remaining risks were assessed as manageable through proven mooring technology" (`crossref/10.20944_preprints202611.1173.v1.json`). This is the main independent assessment of KER3 in the project, and the draft quotes the same assessment only for the hinge.

Fix, KER3 maturity cell and 6.3, second bullet: "SINTEF's technological risk assessment rates the mooring lines, the surface mooring and the breakwater connections as high-TRL components with reliable performance at all three sites (D7.2, SINTEF, as summarised in D7.6)."

### 5 – minor – Clement Germany – Clement's EUPI-PV role is made to depend on Sunlit Sea (6.3 action plan, l.955)

Quote: "Breakwater for the nearshore demonstration in the EUPI-PV proposal coordinated by SINTEF, if Sunlit Sea joins it and it is funded".

What is wrong: In this SINTEF-coordinated proposal, the breakwater is "funded through and supplied by Clement Germany" (docs/project_facts.md l.42). Sunlit Sea's decision affects the floating PV kit, not Clement's breakwater. Section 10 (l.1158) lists Clement Germany for the breakwater without that condition.

Fix: "…coordinated by SINTEF, if the proposal is funded (added by the WP8 lead, Section 10)".

### 6 – wording – Clement Germany – the D1.8 qualifier on ownership is dropped (3.2 KER1 l.288, 4.1 l.363, 7.1 l.1082)

Quote: "Integrating them transfers no ownership: they remain Clement Germany's (D1.8)".

What is wrong: D1.8 rates the floating breakwater design as "Partner-specific foreground, subject to confirmation of any documented inseparable contributions" (l.270; also l.453). Clement Germany would accept the sentence, but the qualifier belongs with a citation of D1.8.

Fix (once, in 7.1): "D1.8 records the breakwater design as Clement Germany's foreground, subject to confirmation of any documented inseparable contributions; no such contribution has been documented."

### 7 – minor – MARIN – in its home section, DIFFRAC's validation is shown against the Stadt tests only (6.5 l.1001; KER5 l.292)

What is wrong: 6.5, the single home of the MARIN record under D40, says that MARIN validated DIFFRAC against Sunlit Sea's Stadt Towing Tank tests (D5.1). It leaves out MARIN's later validation against SUREWAVE's own second basin campaign: "Results of this second campaign (measured motions of FPV modules and breakwater) are used for numerical model validation" (Energies 19(7) l.122). 4.1 (l.395) mentions that validation, so the home section has less than the pointer section. The KER5 maturity cell also names only the Stadt validation. For MARIN this is the stronger evidence, because it uses the project's own test, with the breakwater.

Fix (6.5, after the Stadt sentences): "Before simulating the 2 MWp farm, MARIN validated the model against the motions of the modules and the breakwater measured in the second SUREWAVE basin campaign (Energies 19(7) 1609)." KER5 cell: "DIFFRAC's motions validated against Sunlit Sea's earlier Stadt Towing Tank tests (D5.1) and against the second SUREWAVE basin campaign (Energies 19(7) 1609)."

### 8 – minor – MARIN and SINTEF – who simulated the 50-year hinge loads is unclear (4.1 l.396, 4.1.1 l.429)

Quotes:
- l.396: "The maximum hinge loads simulated in the 50-year sea states are 34 kN …".
- l.429: "MARIN's coupled analysis (D5.1) and SINTEF's risk assessment (D7.2) simulate the hinge loads of the array in each site's 50-year sea states".

What is wrong: D5.1, dated April 2024, reports most probable maximum hinge loads for given sea states (for example Hs 2.5 m, D5.1 l.342–352). Its 50-year appendices cover mooring and breakwater-connector forces (l.242–248). The 45/43/54 → 34/33/40 kN values come from "updated simulations" in D7.2 and D7.6 (D7.6 l.159, l.689). Sunlit Sea's D8.3 (l.169) says "MARIN computed these connector loads for a 2 MWp farm". The draft gives the attribution in two different forms, and neither form is shown by MARIN's or SINTEF's own text.

Fix: l.429: "The hinge loads of the array in each site's 50-year sea states, reported in SINTEF's risk assessment (D7.2), are compared with the hinge's design break load (Section 4.1)". l.396: "…simulated in the 50-year sea states (D7.2) …". If MARIN ran the simulations, credit MARIN once in 4.1, with the record that shows it.

### 9 – wording – MARIN – the reason for not counting MARIN's reported talk is vague (2.5 l.216)

Quote: "One reported item is not counted because the organiser's record contradicts it: a SUREWAVE talk at the NaturSea-PV kick-off of 15 March 2023."

What is wrong: MARIN reported this talk (partner responses: "NaturSea-PV public kick-off … Joep van der Zanden … Oral presentation"). The draft does not say whose item it is or what the record shows. A MARIN reader cannot check it.

Fix: "One item reported by MARIN is not counted: a SUREWAVE talk at the NaturSea-PV public kick-off of 15 March 2023. The organiser's programme lists a MARIN talk by another speaker on NaturSea-PV's own design work and does not name SUREWAVE (KPI check)." Source: `surewave/background/2026-11-19_surewave_wp8_kpi_verification.md` l.138.

### 10 – wording – MARIN – the axial-load result has no figure (6.5 l.1001)

Quote: "the ring reduced the axial connector loads on average and the vertical loads and overturning moments … by up to 50 %".

Fix: "the ring reduced the spatially averaged axial connector loads by up to 20 % and the vertical loads and overturning moments … by up to 50 % in steep irregular seas" (Energies 19(7) l.274–275).

### 11 – wording – MARIN – MARIN's observation is sourced to Sunlit Sea's brochure (4.1 l.395)

Quote: "MARIN observed no measurable hinge buckling or snap loading (D8.3)."

What is wrong: this is MARIN's finding, cited to the brochure that Sunlit Sea led. MARIN's paper says that the second campaign used "an improved connector design with higher compressive stiffness" after the first campaign's "frequent buckling" (Energies 19(7) l.122).

Fix: cite MARIN's D6.2 if it states the observation; otherwise: "The first campaign had shown frequent connector buckling; the second used a connector with higher compressive stiffness (Energies 19(7) 1609), and no measurable hinge buckling or snap loading was observed (D8.3)."

### 12 – minor – SINTEF – SINTEF's role in CIRCWIND and SFI BLUES is understated (Section 10, l.1153–1154)

Quote: "SINTEF (in CIRCWIND through SINTEF Manufacturing AS)"; SFI BLUES: "SINTEF".

What is wrong: CORDIS gives "Coordinated by SINTEF MANUFACTURING AS" for CIRCWIND (`scratchpad_t150/web/cordis_101147517.html`). The Research Council's project record gives SINTEF Ocean AS as the organisation of SFI BLUES (`web/pb_blues.html`).

Fix: CIRCWIND: "SINTEF Manufacturing AS, coordinator". SFI BLUES: "SINTEF (SINTEF Ocean, host of the centre)".

### 13 – minor – SINTEF – the SFI BLUES action is marked "Continuing" although SINTEF reports the reuse as done (6.4 l.986)

Quote: "Continuing, 2027–2028 | Use of the connection-testing methods in SFI BLUES".

What is wrong: SINTEF writes "The connection-testing methods have already been reused in research activities, including SFI BLUES" (SINTEF plan l.43), in the past tense. Section 6 sets the rule: "Actions that a partner reports as under way at the end of the project are marked 'continuing'" (l.876). SINTEF does not report this reuse as under way. 6.4 itself lists it under "Reuse during the project" (l.976).

Fix: "2027–2028 | Further use of the connection-testing methods in SFI BLUES, to the centre's end in 2028, and discussions with Norwegian industrial partners on applications of the aerodynamic and hydrodynamic models (added by the WP8 lead for SFI BLUES)".

### 14 – minor – SINTEF – GEOPON: "if it is funded" conflicts with SINTEF's own words (Section 14 l.1256, Section 10 l.1156)

Quotes: Section 14: "starts the planned GEOPON project if it is funded"; Section 10: "Follow-on: planned; programme and project number not yet public".

What is wrong: SINTEF calls it "a nationally funded project involving the industrial partner GEOPON" and "nationally funded collaboration with GEOPON" (SINTEF plan l.11, l.54, l.70). The condition was proposed in round 1 (r1_partners S8). Against SINTEF's text the condition reads as a doubt that SINTEF has not expressed. Section 10 also uses different wording. Requirement 6 asks for consistency.

Fix: Section 14: "starts the planned national project with GEOPON". Section 10 status: "Follow-on: planned; SINTEF describes it as nationally funded; programme and project number not yet public".

### 15 – minor – SINTEF – D2.1 is set against D5.1, although D5.1 takes its design sea states from D2.1 (4.1 l.371)

Quote: "It gives the 50-year significant wave heights of the use-case basis D2.1 (4.4, 7.0 and 12.3 m); this plan uses the design sea states of MARIN's D5.1."

What is wrong: D5.1 builds its design sea states from the 50-year Hs–Tp contours of SINTEF's D2.1. D5.1 Table 3 is "Adopted from Table 14 in D2.1" (D5.1 l.260), and D5.1 l.862 refers to "the 50-year return period conditions described in D2.1". As written, a SINTEF reader would think that D2.1 was superseded.

Fix: "It gives the 50-year significant wave heights of the use-case basis D2.1, led by SINTEF (4.4, 7.0 and 12.3 m). This plan uses the design sea states that MARIN's D5.1 takes from the 50-year contours of D2.1."

### 16 – minor – ACCIONA – D7.3's greenhouse-gas finding on the mixes is given only in part (6.2 l.913)

Quote: "…finds no relevant greenhouse-gas saving from the circular mixes against a conventional breakwater …, because the cement content needed for the strength is similar (D7.3, IFEU)."

What is wrong: D7.3 gives two reasons (l.1328). For the shell, the cement content needed for the strength is similar, and the steel reinforcement is about half of the shell's footprint, which limits what any mix can change. For the core, the emissions of the recycled-glass aggregate, lime and aluminium powder happen to balance those of the polystyrene. D7.3 also says that the mixes "contain substantial amounts of by-products from other industrial processes" and that circularity was assessed in the technological assessment (l.1336). The draft keeps only the reason that reflects on ACCIONA's mixes. D24 bars a footprint claim but does not bar a full and fair statement of D7.3.

Fix: "At breakwater level, the environmental assessment finds no relevant greenhouse-gas saving from the circular mixes against a conventional breakwater with a concrete shell and an expanded polystyrene core. In the shell, the cement content needed for the strength is similar, and the steel reinforcement makes up about half of the shell's footprint. In the core, the emissions of the recycled-glass aggregate, lime and aluminium powder balance those of the polystyrene. D7.3 notes that the mixes contain substantial amounts of by-products from other industrial processes (D7.3, IFEU)."

### 17 – minor – ACCIONA – D4.2's mechanical conclusions are missing (6.2 l.913; R3 l.330; requirement 4)

What is wrong: 6.2 gives D4.2's durability results but none of its mechanical conclusions (D4.2 l.966–986):

- In static three-point bending, HPC is more than 55 % stronger than LWAC and about 50 % better in strength-to-weight ratio.
- Thermal cycling has a negligible effect.
- In the drop-tower tests both mixes dissipate impact energy through cracking.
- The low pull-out values come from the cellular core, not from the interface.
- D4.2 concludes that "HPC is the most suitable material for the shell".

These conclusions are why the prototype has HPC walls and an HPC bottom slab. D4.2 also says that a crystalline waterproofing admixture is part of all the optimal shell mixes (l.960).

Fix, 6.2 after the durability sentence: "In SINTEF's mechanical tests of the shell–core beams, HPC was more than 55 % stronger than LWAC in static bending and about 50 % better in strength-to-weight ratio. Both dissipated impact energy through cracking, and the low pull-out values came from the cellular core, which carries no structural load. D4.2 concludes that HPC is the most suitable shell material (D4.2, ACCIONA, with the tests by SINTEF; Section 6.4)."

### 18 – minor – ACCIONA – R4 misstates D4.1's aim for the cellular concrete (3.4 R4 l.331, against 6.2 l.907)

Quote (R4): "365 kg/m³ was the best density result of D4.1's 26 cellular-concrete trial mixes, above the proposal's 200–300 kg/m³ and D4.1's aim of about 300 kg/m³, a requirement set by Clement Germany."

What is wrong: D4.1 has two figures. Clement's requirement is "around 300 kg/m³" (l.599). D4.1's trial programme aimed at "a density between 300 and 400 kg/m³" (l.607), and 6.2 says exactly that. R4 merges the two into "D4.1's aim of about 300", which makes ACCIONA's result look like a miss against its own aim.

Fix: "365 kg/m³ was the best density result of D4.1's 26 cellular-concrete trial mixes, which aimed at 300–400 kg/m³. It is above Clement Germany's requirement of about 300 kg/m³ and the proposal's 200–300 kg/m³."

### 19 – wording – ACCIONA – D7.4's caveat is worded in two ways (KER2 l.289 against 4.6.1 l.683)

Quotes: KER2: "more detailed environmental and durability assessments may change this conclusion"; 4.6.1: "more detailed durability assessments may change this ranking".

What is wrong: D7.4 says "conventional breakwater solutions remain preferable unless structural or regulatory constraints demand alternatives. In future phases, more detailed environmental and durability assessments may help requalify this conclusion" (D7.4 l.1148). 4.6.1 drops "environmental", and neither place gives the "unless" condition. ACCIONA reads both.

Fix (both places): "D7.4 finds the conventional breakwater preferable unless structural or regulatory constraints demand alternatives, and notes that more detailed environmental and durability assessments may change this conclusion."

### 20 – minor – ACCIONA – the date of ACCIONA's summary has no source in the record (2.2 l.117, 3.1 l.258, executive summary l.28)

Quote: "ACCIONA | Exploitation summary | 26 November 2025".

What is wrong: the ACCIONA summary in the repo has no date line, and its file name carries 2026-09-30 (`surewave/background/2026-09-30_acciona_exploitation_summary.md`). No file in surewave/ or docs/ contains the 26 November 2025 date. Decision D11 asks for "each file's own date line", and this file has none. ACCIONA's exploitation manager would ask where the date comes from. The sequence argument of 3.1 rests on the date: "written before the template was sent".

Fix: cite the record that dates it, for example the covering e-mail, in the evidence for 2.2. If no record exists, ask ACCIONA to confirm the date in the review round. This is an owner question; the draft text stays.

### 21 – minor – ACCIONA – the last extension is not linked to ACCIONA's exposure work (cover l.5; 6.2)

What is wrong: the three-month extension to 31 December 2026 was granted for ACCIONA's breakwater demonstrator in Spain (docs/project_facts.md l.51: "extended three months to 2026-12-31 … for ACCIONA breakwater demonstrator in Spain"). The draft gives the extension (l.5) but never says what it served. That fact explains why D6.4 and the Gijón results come at the end of the project and after D7.6 (l.381).

Fix, 6.2 after the D6.4 sentence: "The last extension of the project, by three months to 31 December 2026, gives time to complete this exposure and its reporting."

### 22 – wording – ACCIONA – R3 leaves out that D8.5 still named UHPFRC (l.330)

Quote: "neither D4.1 nor ACCIONA's summary discusses UHPFRC".

What is wrong: ACCIONA's mid-term text in D8.5 (April 2024) still refers to "the UHPFRC and other materials mixes" (D8.5 l.1202), three months after D4.1 had set the HPC and LWAC requirements. A reader comparing D8.5 with D8.4 sees an unexplained shift.

Fix: "…neither D4.1 nor ACCIONA's final summary discusses UHPFRC; ACCIONA's mid-term entry in D8.5 still named it."

### 23 – wording – ACCIONA – ACCIONA's part in the NaturSea-PV webinar is not recorded (2.5 joint-events row l.184; Annex A.8)

What is wrong: ACCIONA reports taking part in the joint NaturSea-PV webinar (Valle Chozas) and in the final workshop (partner responses, ACCIONA, "Web events"). The joint-events contributors are "SINTEF, MARIN, Ceit". The final workshop is credited, but the webinar is not. The web-events row sets the pattern for non-speaking contributors ("IFEU answering questions").

Fix: joint-events row: "SINTEF, MARIN, Ceit; ACCIONA attending". If attendance is not counted as a contribution, say so in the counting paragraph.

### 24 – minor – IFEU – an offer is attributed to IFEU without a source (4.1 l.388)

Quote: "Its life-cycle assessment has not been made; IFEU offers one for the first multi-megawatt plant (Section 6.7)."

What is wrong: IFEU's input contains no such offer (`2026-09-30_ifeu_exploitation_summary.md`). The 6.7 row is marked "added by the WP8 lead from the KER1 plan" (l.1058). Requirement 3 applies.

Fix: "Its life-cycle assessment has not been made. The WP8 lead proposes one, as a study commissioned from IFEU for the first multi-megawatt plant (Section 6.7)."

### 25 – minor – IFEU – IFEU's lead of the societal-engagement task is not credited (6.7 l.1047; 3.5 l.347)

What is wrong: IFEU leads Task 8.1, Societal Engagement (WP index l.173), of which D8.2 is the output. 6.7 lists D8.2 only as a report. 3.5's social bullet names D8.2 and D7.5 "both led by IFEU" but does not mention the task. The Stakeholder Advisory Board's review of the social-impact list in D8.2 (A.10, l.1386) is part of IFEU's task.

Fix (6.7): "…and the societal engagement task of WP8 (Task 8.1), reported in D8.2, Report on societal needs and engagement, for which Stakeholder Advisory Board members reviewed and extended the list of potential social impacts."

---

Findings: 1 major, 17 minor, 7 wording.
