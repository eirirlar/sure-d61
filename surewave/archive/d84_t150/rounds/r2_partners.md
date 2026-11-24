# T150 round 2: review of D8.4 by each non-lead partner's exploitation manager

Persona: the exploitation manager of ACCIONA, Clement Germany, SINTEF, MARIN, Ceit and IFEU, one at a time. Method: I grepped every mention of each partner in `scratchpad_t150/d84_merged.md` (read end to end) and checked it against that partner's exploitation summary, the deliverables it led, the publication records (Crossref abstracts in `scratchpad_t150/crossref/`) and the KPI record. The final technical report working copy was not used as a source (D22). Line numbers "l.N" refer to `d84_merged.md`. Repo paths are relative to `C:\dev\src\sure-d61`.

Round 1 fixes I checked and found in place: the ACCIONA licence route (Section 5), the CLC wording, acciona.com, the ACCIONA interviewee, the Spanish articles credited to ACCIONA, Clement's transition element and mooring in KER1, the Clement role in 4.6.1, the template sequence, the SINTEF validation wording, the CIRCWIND tense, GEOPON "if funded", the hydrodynamic split, ReFRESCO in R5, the MARIN presenters, the Dakota note, the D5.1 Baltic increase, the SHMS inputs (D13r), D5.7 in KER6, the Ceit tense, the Ceit contract wording, IFEU's background, IFEU's deliverables, the D7.6 recommendation in 4.3.3, the IFEU and MARIN KER1 rows, and the D1.8 "major dispute" wording.

---

## Assessment of the rejections in rejected_so_far.md (partner area only)

| Rejection | Holds? | Reason |
|---|---|---|
| r1disp_A / r1disp_E, r1_partners#A5: the 18 LWAC, 2 HPC and 26 cellular formulations rejected as "final technical report only" | Does not hold for the counts | D4.1 gives them. Eight reference LWAC trial mixes plus ten circular ones are samples 1–18 (`surewave/background/2024-01-18_surewave_d4.1_design_characterization_circular_materials.md` l.241, l.271). There are two HPC trial mixes (l.554) and 26 cellular-concrete samples (l.1079). The draft already uses the 26 (l.1075). The rejection holds for the 76 % figure and for 380 against 350 kg/m³: those are in the final report only. See A9. |
| r1disp_A, r1_owner#17: chloride coefficients rejected as FTR-only | Superseded; no longer holds | D4.2 Table 6 gives D_Cl 0.4–0.9 (`2024-07-31_surewave_d4.2_lab_testing_breakwater_prototype.md` l.470, l.477). r1disp_E then put the figure into 6.2 (l.1079). The two dispositions contradict each other. The text is now correct. |
| r1disp_A, r1_owner#19: "0.4 transmission in 1–3 s not found in D3.2 text" (OWNER QUESTION 7) | Does not hold | The D3.2 summary says: "Critical wave periods for the PV-system are between 1 and 3 seconds. These waves are reduced by the FB to at least 40% of the incident wave height" (`2023-08-08_surewave_d3.2_floating_breakwater_design.md` l.1709). 6.3 now uses it (l.1102), so owner question 7 can be closed. |
| r1disp_E, r1_partners#S2: "19 risk indicators" rejected as final-report only | Does not hold, and is now resolved | The abstract of Preprints 202611.1173 says "Nineteen technological risks were evaluated" (crossref JSON). R11 now cites it (l.534). |
| r1disp_E, r1_partners#C2: "prototype built to Clement's geometry" rejected (FTR only) | Holds for "geometry" | Other sourced credit exists and is still missing. Clement is a contributing beneficiary of D4.3, and the mixes were developed "according to production requirements established by Clement" (D4.3 l.27, l.413). Clement also set the requirements for the core concrete (D4.1 l.597). See C4. |
| r1disp_A, r1_partners#S3: 1,030 mixtures | Holds | Found only in the final report working copy; D5.2 is not in the repo. |
| r1disp_A / r1disp_E, r1_partners#S4: 87 % / 97 % | Holds | Not in the Energies 17(19) 4873 abstract or any deliverable in the repo. |
| r1disp_A, r1_partners#E3; r1disp_D cinea#F24, coord#12; r1disp_E ledger_E#79: Ceit left out of the hinge redesign | Holds (D4/D4r) | The 3.1 conflict bullet now names D1.8's attribution to Ceit (l.459). The wording of that bullet needs a fix: see E3. |
| r1disp_E, r1_partners#M3: final-report sentence on installed cost | Holds (D22) | |
| r1disp_C, C#14, and decision D3: no "factor 2–3" | Holds as a rule | The rule has produced a wrong statement about MARIN's input: see M2. |
| r1disp_B 9 (ACCIONA articles), B#88 (BayWa), 24 (EERA year), F5 / 36 (ISNRE record) | Hold | These follow decisions D10, D16 and D22. |
| r1disp_D writing#6 (EDP not anonymised) | Holds | EDP is an applicant in the EIC proposal (proposal l.26). |
| r1disp_E cinea#10 (IP workshops), coord#29 / owner#26 (EUPI-PV status) | Hold for now | These are owner questions to settle at submission. |

---

## ACCIONA (KER2)

### A1 – major – ACCIONA's deliverable D6.4 on the Gijón exposure is never named
Sections 3.2 (l.485), 3.4 R3/R4 (l.526–527), 4.1 (l.570), 6.2 (l.1081) and 15 (l.1412) cite the nine-month Gijón exposure only to Preprints 202611.1592.
What is wrong: the exposure is the subject of Task 6.5, "Long-term degradation of the concrete component exposed in harbor". ACCIONA leads that task, with Ceit, SINTEF and Clement as partners. It is also the subject of deliverable D6.4, "Marine long-term degradation of concrete breakwater", led by ACCIONA. D8.4 names neither. The text also never says that ACCIONA led WP4. An ACCIONA reader sees the main field result of its own work package and deliverable credited only to a preprint.
Sources: `surewave/background/2026-09-29_surewave_wp_task_deliverable_index.md` l.81, l.132, l.140; the GA list of deliverables (`2022-09-20_surewave_grant_agreement_101083342.md` l.4655, l.5202: "D6.4 … Lead Beneficiary 5. ACCIONA"); D1.7 l.622; the Zenodo snapshot l.38 (D6.4 listed as a public deliverable not yet in the community).
Fix: in 6.2, after "ACCIONA designed and cast…", add: "The exposure is Task 6.5 of the technical validation work package, led by ACCIONA with Ceit, SINTEF and Clement Germany, and is reported in ACCIONA's public deliverable D6.4, Marine long-term degradation of concrete breakwater, and in the joint preprint." Give D6.4's status (submitted, or due by 31 December 2026); this is an OWNER QUESTION, because D6.4 is not in the repo. Add "D6.4" to the evidence cells of R3 and R4 and to the KER2 maturity cell. In 6.2, before the three results, add: "ACCIONA led WP4, New circular material solutions (D4.1–D4.3)."

### A2 – minor – the LWAC conflict in 3.1 is stated incompletely (l.455)
Quote: "LWAC density: 1,950 kg/m³ (68 MPa) in ACCIONA's input, near 2,000 kg/m³ for the same 68 MPa mix in D4.1, and about 1,800 kg/m³ in D8.3."
What is wrong: D4.1 sets the LWAC requirement as at least 45 MPa at no more than 1,900 kg/m³. It selects Sample 17 (49 MPa, 1,898 kg/m³) as "the optimized circular LWAC solution". Sample 18 (68 MPa, near 2,000 kg/m³, with the lower-carbon CEM III cement) is described as having "a higher density" (D4.1 l.1191, l.1255–1259). The prototype used Sample 18 (D4.3 Table 3, l.413–424). D4.2 gives 1,850 kg/m³ for the LWAC "selected" in D4.1 (D4.2 l.659). The reader cannot tell which mix ACCIONA's 1,950 kg/m³ / 68 MPa describes, or that it sits above D4.1's density requirement.
Fix: "LWAC: ACCIONA's input gives its optimal mix as 1,950 kg/m³ and 68 MPa. D4.1 selected Sample 17 (49 MPa, 1,898 kg/m³) against its requirement of at least 45 MPa and at most 1,900 kg/m³. D4.1 gives Sample 18, with a lower-carbon CEM III cement, 68 MPa at near 2,000 kg/m³, and the prototype's top slab used Sample 18 (D4.3). D4.2 gives 1,850 kg/m³ and D8.3 about 1,800 kg/m³. This plan uses ACCIONA's figure for the mix used in the prototype."

### A3 – wording – R3 implies an unexplained deviation (l.526)
Quote: "D4.1 develops these two mixes for the shell and gives no reason for leaving UHPFRC."
What is wrong: the statement is accurate, but it reads as a finding against ACCIONA. D4.1 sets requirements for the two shell concretes it develops: HPC at 120 MPa and 2,350–2,500 kg/m³, and LWAC at 45 MPa or more and 1,900 kg/m³ or less (D4.1 l.221–235, l.1255, l.1271).
Fix: "D4.1 sets requirements for an HPC (120 MPa) and an LWAC (at least 45 MPa, at most 1,900 kg/m³) shell and develops both. Neither D4.1 nor ACCIONA's summary discusses UHPFRC."

### A4 – minor – "low-carbon cement" stated as fact in the KER2 cell (l.485)
Quote: "LWAC: 1,950 kg/m³, 68 MPa, recycled glass aggregate, low-carbon cement".
What is wrong: 6.2 correctly says "a cement that ACCIONA describes as low-carbon" (l.1076), and D24 bars footprint claims. The KER2 cell states it as fact.
Fix: "a CEM III cement with a lower clinker content than CEM I (D4.1)". D4.1 l.548 names it as Holcim's ECOPlanet CEM IIIA.

### A5 – minor – D4.3 cited for something it cannot show (l.485, l.526, l.610)
Quote: "a reduced-scale breakwater prototype built and deployed by ACCIONA (D4.3)"; "designed, cast and deployed by ACCIONA (D4.3)".
What is wrong: D4.3 is dated 29 August 2024. It documents design and manufacture, says the prototype "will be installed at the R&D maritime environment demo site of ACCIONA" (l.235), and names SINTEF and Clement as contributing beneficiaries (l.27). The deployment and mooring are documented in Preprints 202611.1592 ("four-line catenary mooring system connected to gravity anchors", abstract).
Fix: "designed and cast by ACCIONA, with SINTEF and Clement Germany as contributing beneficiaries (D4.3), and deployed by ACCIONA at its R&D maritime demonstration site in the Port of Gijón (Preprints 202611.1592)". Apply the same change in 4.1.1 (l.610) and R3 (l.526).

### A6 – minor – the KER2 relation to KER1 is shown only at its worst (l.485)
Quote: "Material option for the breakwater; at today's costs D7.4 finds the conventional-concrete breakwater cheapest".
What is wrong: 4.6.1 (l.851) gives the full picture: LWAC +24 %, HPC +76 %, and D7.4's caveat that more detailed durability assessments may change the ranking. The KER2 cell, which partners and CINEA read first, gives only the negative half.
Fix: "Material option for the breakwater; at today's costs D7.4 finds the conventional-concrete breakwater cheapest, and notes that more detailed durability assessments may change this ranking (Section 4.6.1)".

### A7 – minor – the Gijón prototype is anonymous where the other partners' tests are named (l.17, l.998, l.1412)
Quotes: "on the wave-basin tests of the integrated system at MARIN and the component tests. A reduced-scale concrete breakwater prototype…" (exec); "two 1:10-scale wave-basin campaigns … at MARIN, the component and connection tests at SINTEF, and nine months of sea exposure of a reduced-scale concrete breakwater prototype in the Port of Gijón" (Section 15).
Fix: Section 15: "…and nine months of sea exposure of ACCIONA's reduced-scale concrete breakwater prototype in the Port of Gijón, monitored by Ceit, without the PV array." Executive summary: "…on the wave-basin tests of the integrated system at MARIN and the component tests at SINTEF. ACCIONA's reduced-scale concrete breakwater prototype, without the PV array, was exposed…". Do the same in the 4.10 status cell (l.998).

### A8 – wording – ACCIONA's research topic is attributed without a source (l.1090)
Quote: "long-term marine durability, building on the Gijón exposure, is one topic".
What is wrong: ACCIONA's summary names further R&D in general (l.40). The durability topic comes from the preprint's conclusion.
Fix: "…; long-term marine durability, which the Gijón preprint names as the next step, is one candidate topic".

### A9 – minor – evidence compressed: the development record in D4.1 is not given (requirement 4; l.1075–1077)
What is wrong: 6.2 gives the 26 cellular trial mixes but not the other counts, and they are in D4.1: eight reference and ten circular LWAC trial mixes, with recycled construction and demolition aggregate, steel slag and recycled glass (Minolite) (l.241, l.271), and two HPC trial mixes, a reference mix and a circular one (l.554).
Fix: add to 6.2 after the HPC bullet: "D4.1 records the development: eight reference and ten circular LWAC trial mixes, with recycled concrete aggregate, steel slag and recycled glass aggregate in place of natural aggregates; a reference and a circular HPC mix; and 26 cellular-concrete trial mixes."

---

## Clement Germany (KER3)

### C1 – minor – Clement's figures in D8.3 are not credited (l.191, l.420)
Quotes: KPI table "Technical brochure | 1 (GA) | 1 | Met | Sunlit Sea, SINTEF"; 2.5.20 "On 18 November 2026 Clement Germany sent review comments, mostly on the breakwater section, and seven CAD drawings as input for four figures."
What is wrong: the comments and graphics were used. D8.3's AI-generated breakwater figures were withdrawn and replaced by Clement's CAD graphics, which carry the credit "Graphics: Clement Germany" (`surewave/deliverables/2026-09-28_surewave_d8.3_figures.md` l.904–922; D8.3 l.95). The breakwater text was revised to Clement's four points: keels, catenary mooring, transverse walls, deep draft (D8.3 l.77, l.91). The contributors column also leaves out IFEU, which reviewed version 0.3 (meta.yaml).
Fix: 2.5.20: "Clement Germany reviewed the breakwater section on 18 November 2026 and supplied the CAD graphics that replaced four breakwater and mooring figures, credited to Clement Germany in the brochure." KPI table contributors: "Sunlit Sea, SINTEF; graphics and review by Clement Germany; review by IFEU".

### C2 – minor – unit weight inconsistent between 6.3 and 4.1.1 (l.1102 against l.610)
Quote (6.3): "The design analysis limited the unit weight to about 120 t, which mobile cranes can still handle (D3.2)." Quote (4.1.1): "about 123 t".
What is wrong: D3.2 sets an upper limit of about 120 t for crane handling (l.428). The chosen unit weighs 123.39 t (l.1715). As written, 6.3 says the unit was kept within a limit that it slightly exceeds.
Fix: "The design analysis set an upper unit weight of about 120 t, which mobile cranes can still handle; the selected unit weighs about 123 t (D3.2)."

### C3 – minor – the 10 MWp sizing and the 346 m ring are credited to an internal report instead of D3.3 (l.562)
Quote: "Clement Germany compiled the material quantities of the plant for 10 MWp, about 18,600 panels of 537 Wp, and for a 2 MWp version with a ring 173 m across."
What is wrong: the 10 MWp minimum size, the 18,600 panels of 537 Wp and the 346 m circular layout are in Clement's public deliverable D3.3 (l.383, l.857). The 2 MWp ring is in the internal materials report. That report also supplies D7.4's anchoring, transition-element and connection quantities (materials report l.12–16), which the text does not say.
Fix: "Clement Germany's D3.3 sized the circular layout for 10 MWp: about 18,600 panels of 537 Wp in a ring 346 m across. Clement Germany later compiled the material quantities for that plant and for a 2 MWp version with a ring 173 m across; D7.4 takes its anchoring, mooring, transition-element and connection quantities from them."

### C4 – minor – Clement's requirements behind the concrete and the prototype are not credited (KER3 l.486, 6.3)
What is wrong: Clement provided the requirements for the core concrete (D4.1 l.597: "provided by the industrial partner Clement"). The mixes for the prototype were developed "according to production requirements established by Clement" (D4.3 l.413).
Fix: add to the KER3 maturity cell and to 6.3: "Clement Germany set the requirements for the core concrete (D4.1) and the production requirements for the prototype mixes (D4.3)."

### C5 – minor – Clement's role in the EIC proposal is understated (l.1111, l.1120, l.1308)
Quote: "Clement supplies and installs the breakwater and mooring and provides access to the baseline site".
What is wrong: the proposal gives Clement more than that. It "leads the development, manufacturing, deployment, and operation of the floating breakwater and mooring systems" (proposal l.274). It leads WP6, Deployment, Operation and Validation Campaign, M15–M34 (l.337). It "will confirm [the Water Resources Act restrictions] … with the competent authority" (l.252).
Fix: 6.3: "…Clement Germany leads the development, manufacture, deployment and operation of the breakwater and mooring, leads the deployment, operation and validation work package, confirms the permitting route with the competent authority, and provides access to the baseline site…". In the action row 2027–2029, add "operation and validation campaign".

### C6 – minor – Clement's role in EUPI-PV is missing (l.1309, 6.3)
What is wrong: Section 10 puts Clement Germany only in the text column, as "proposed supplier". The Partner column says "SINTEF-coordinated consortium, possibly including Sunlit Sea". The project facts say the breakwater is "funded through and supplied by Clement Germany" (`docs/project_facts.md` l.42). Clement's action plan has no EUPI-PV row.
Fix: Partner column: "SINTEF-coordinated consortium, with Clement Germany for the breakwater; Sunlit Sea possibly". Add to 6.3: "2027–2029 | Breakwater for the EUPI-PV nearshore demonstration, if the proposal is funded | Breakwater installed".

### C7 – wording – the site agreement row is not marked as conditional (l.1118)
Quote: "Q1 2027 | Collaboration agreement with the owner of the EIC Transition demonstrator site; the site owner's letter of intent lapses without one on 28 February 2027".
Fix: "Q1 2027 | Collaboration agreement with the owner of the EIC Transition demonstrator site, if the project is funded (decision expected December 2026 – January 2027); the letter of intent lapses without one on 28 February 2027".

### C8 – minor – Clement's connections tested at SINTEF are not credited (KER3 l.486, KER4 l.487, 6.4 l.1139)
What is wrong: the 402 kN steel-wire-rope assemblies between breakwater units and the breakwater-to-module connections (40.88 kN) are Clement's connection designs from D3.3, tested by SINTEF (Preprints 202611.1612 abstract). KER4 and 6.4 report the figures without saying whose designs were tested, and KER3 does not mention the tests.
Fix: in KER3 maturity add "breakwater connections and breakwater-to-array connections tested at SINTEF: 402 kN and 40.9 kN mean ultimate load (D6.1; Preprints 202611.1612)". In 6.4, write "The steel-wire-rope assemblies between breakwater units, designed by Clement Germany (D3.3), reached…".

### C9 – wording – the open datasets are listed without owners (l.542)
Quote: "among them the D7.4 cost model, the metocean design dataset, the anchoring and connection design dataset and the basin-test dataset".
Fix: "…the D7.4 cost model and the metocean design dataset (Sunlit Sea), the anchoring and connection design dataset (Clement Germany) and the basin-test dataset (MARIN)".

---

## SINTEF (KER4, KER5)

### S1 – major – SINTEF's technological risk assessment is presented as D7.6's (l.17, l.568, l.583, l.750, l.956, l.1412)
Quotes: "D7.6 (November 2025) assessed the integrated SUREWAVE concept at TRL 5. It rests on D7.6's technical risk assessment of the system with the redesigned hinge"; "Design values (D7.6). The design break load … is 37 kN, against 14 kN"; Lean Canvas: "design break load of the full-width hinge 37 kN, against 14 kN …, D7.6".
What is wrong: the TRL 5 rating, the 14 → 37 kN capacities and the simulated hinge loads (45/43/54 kN to 34/33/40 kN) are results of SINTEF's technological risk assessment. That is D7.2, "Panjwani, B. (2025): Report on technological qualitative assessment", which D7.6 summarises. D7.6 thanks SINTEF for "the provision of the summary of the technical risk assessment" (D7.6 l.1412, l.1526). Preprints 202611.1173 (Panjwani, SINTEF) gives the same figures and says "The results support the current TRL 5 assessment" (abstract). D8.4 credits SINTEF with D7.2 in KER7 (l.490), but in 4.1 calls the same work "D7.6's technical risk assessment", so the terms are also inconsistent. This is an error inside decisions D2r and D4r ("in D7.6"); the error is the attribution only.
Fix (4.1): "D7.6 (November 2025) assessed the integrated SUREWAVE concept at TRL 5. The rating comes from SINTEF's technological risk assessment (D7.2; Preprints 202611.1173, 2026), made after the two 1:10-scale wave-basin campaigns at MARIN and the component tests, and is adopted in D7.6." Design values: "Design values (SINTEF's technological risk assessment, D7.2 and Preprints 202611.1173, as summarised in D7.6)…". Lean Canvas and 4.8: "…37 kN … (SINTEF's risk assessment, D7.2 and D7.6)". Use "technological risk assessment" everywhere (KER7, R11 and 4.1).

### S2 – minor – SINTEF's shell–core test programme is missing (6.4 l.1131; R3/R4 l.526–527; 6.2 l.1079)
What is wrong: SINTEF led Task 4.3, durability of the interface between shell and core (index l.87). In D4.2, ACCIONA cast 25 HPC and 23 LWAC shell–core beams, and SINTEF tested them in three-point bending, cyclic bending, pull-out of the shell–core interface and impact (wave slamming) (D4.2 l.519–541). These are also the tests that calibrated Ceit's model. 6.4 mentions only "three-point bending tests"; 6.2 and R3/R4 omit the programme.
Fix: 6.4: "It led the durability assessment of the shell–core interface (Task 4.3). It tested 25 HPC and 23 LWAC shell–core beams cast by ACCIONA in three-point and cyclic bending, pull-out of the interface and impact (D4.2); the bending tests calibrated Ceit's concrete model." Add to the R3 and R4 evidence: "shell–core beam tests at SINTEF (D4.2)".

### S3 – minor – D2.1, the use-case basis led by SINTEF, is not credited (6.4 l.1131)
What is wrong: SINTEF led Task 2.1 and D2.1, the use-case scenario basis (index l.44, l.51; Zenodo record 16). D2.1 defines the three reference sites and the 50-year conditions that D3.3 and D5.1 use (D3.3 l.225; D5.1 l.862).
Fix: add to "SINTEF's work in SUREWAVE": "It led the use-case definition (D2.1) that set the three reference sites and their design conditions."

### S4 – minor – SINTEF omitted as a contributor to the prototype (KER3 l.486)
Quote: "reduced-scale prototype exposed for nine months at Gijón, with Clement Germany as a contributing beneficiary (D4.3)".
What is wrong: D4.3 names "SINTEF, CLEMENT" (l.27), and SINTEF revised D4.3 (l.44).
Fix: "…with SINTEF and Clement Germany as contributing beneficiaries (D4.3)". See also A5.

### S5 – minor – "validation … is further work" sits on testing methods in the KER4 cell (l.487)
Quote: "…Surewave-ANN kept as an internal research tool. Validation against experimental and field data is further work (SINTEF)".
What is wrong: SINTEF's sentence refers to its modelling methods (plan Section 1, l.13). In the KER4 cell it follows the test results and reads as if the test methods were unvalidated.
Fix: "Validation of the aerodynamic and hydrodynamic models against experimental and field data is further work (SINTEF)."

### S6 – wording – the open-source solver is not mentioned in the protection position (7.2 KER5, l.1253)
Quote: "SINTEF's hydrodynamic modelling as for KER4".
What is wrong: SINTEF's SPH model runs on the open-source solver DualSPHysics (Preprints 202610.0011 abstract). For MARIN the text separates Dakota from MARIN's own software; the same distinction applies to SINTEF.
Fix: "SINTEF's hydrodynamic modelling, a model set-up and workflow on the open-source solver DualSPHysics, as for KER4."

### S7 – minor – SINTEF's EIC role is incomplete (l.1308)
Quote: "SINTEF, coordinator, for modelling, design verification and validation".
What is wrong: the proposal adds "monitoring systems, reliability assessment" (proposal l.270, l.318).
Fix: "SINTEF, coordinator, for modelling, design verification, monitoring systems, reliability assessment and validation". Use the same wording in the 6.4 action row (l.1153).

### S8 – minor – the aerodynamic correlations are omitted (6.4 l.1135; KER4 l.487)
What is wrong: the reusable output of Energies 17(19) 4873 is a set of correlations for lift and drag forces as a function of the number of panels, for designing mooring lines and connections (abstract). D8.4 gives only the shielding result.
Fix: add to 6.4: "From CFD simulations of panel configurations, SINTEF derived correlations for lift and drag forces as a function of the number of panels, for the design of mooring lines and connections (Energies 17(19) 4873)."

---

## MARIN (KER5)

### M1 – major – the Stadt Towing Tank tests are shown as a SUREWAVE campaign, and MARIN's validation is uncredited (R1 l.524; 6.1 l.1054; 6.5 l.1166)
Quotes (R1): "Basin tests: preliminary float-string campaign at the Stadt Towing Tank, provided by Sunlit Sea, with six floats in regular and irregular waves, which calibrated the linear hydrodynamic method used for the three reference sites (D8.3)". (6.1): "Sunlit Sea provided the first wave-tank campaign, a string of six floats at the Stadt Towing Tank". (6.5): "In D5.1, DIFFRAC's heave and pitch motions were generally similar to the basin-test results."
What is wrong: D5.1, led by MARIN, says: "Wave basin tests of Sunlit Sea's floating PV system were performed in the Stadt Towing Tank, Norway. These tests were not part of the SUREWAVE project, but the results were made available by Sunlit Sea for the numerical model validation presented herein" (D5.1 l.620). The arrays were 1×3, 1×6 and 1×9 modules, not six floats (l.622). MARIN compared DIFFRAC with them, which is a validation, not a calibration (l.626–646, l.652). D8.4 therefore presents Sunlit Sea background as a SUREWAVE campaign and gives MARIN's validation to the tests. 6.5 does not say which basin tests DIFFRAC was compared with, and 3.1 does not list the conflict between D8.3 (l.135, l.196) and D5.1.
Fix (R1): "Basin tests: two 1:10 campaigns of the integrated system at MARIN (…). Before them, MARIN validated DIFFRAC against Sunlit Sea's earlier tests of 1×3, 1×6 and 1×9 module arrays at the Stadt Towing Tank, which were made available to the project (D5.1)." (6.1): "Sunlit Sea made the results of its earlier Stadt Towing Tank tests of module arrays available to the project, and MARIN used them to validate its diffraction model (D5.1)." (6.5): "…generally similar to Sunlit Sea's Stadt Towing Tank tests of 1×3 and 1×6 arrays (D5.1)." Add to the 3.1 conflict list: "Stadt Towing Tank tests: D8.3 describes them as a SUREWAVE campaign that calibrated the linear method; D5.1 states that they were not part of SUREWAVE and were used to validate DIFFRAC. This plan follows D5.1."

### M2 – minor – the draft says MARIN reported "a larger reduction" (l.457, l.1167)
Quotes: "MARIN's input reports a larger reduction in mooring chains than D5.1 gives"; "MARIN's summary reports a larger reduction in mooring chains; this plan uses the figures of D5.1."
What is wrong: MARIN's "up to a factor 2–3" is a ratio of chain mass. D5.1 Table 9 gives mass ratios of 0.44 and 0.41 for the 2 MWp ring at the Mediterranean and North Sea sites (D5.1 l.1500–1520), which is a factor of about 2.3–2.4. MARIN's figure therefore agrees with D5.1 for the 2 MWp ring and exceeds it only at the top of its range. Read against D5.1, the sentence says MARIN overstated its result. Decision D3 bars the words "factor 2–3 reduction"; the fix below does not use them.
Fix: "MARIN's summary expresses the reduction as a ratio of mooring-chain mass; the largest reductions in D5.1, 56 % and 59 % for the 2 MWp ring, correspond to a ratio of about 2.3–2.4 (D5.1, Table 9). This plan gives the reductions in per cent."

### M3 – minor – the second campaign is said to validate Energies 19(7) 1609 without a source (l.582)
Quote: "The measured motions were used to validate the hydrodynamic model of the 2 MWp farm (Energies 19(7) 1609, 2026)."
What is wrong: the paper's abstract describes simulations of the 2 MWp farm with and without the breakwater ring and does not mention validation against the second campaign. D8.3 says only that the two campaigns provided the data "required to validate the hydrodynamic models" (D8.3 l.200).
Fix: "The two campaigns provided the motion and load data for validating MARIN's hydrodynamic models (D8.3); MARIN's 2 MWp farm simulations are published in Energies 19(7) 1609 (2026)."

### M4 – wording – the source of 34–59 % is not stated (l.457, l.529, l.1005)
What is wrong: D5.1's abstract and conclusion say "up to 56 %" and "34-56 %" (D5.1 l.86, l.1774). The 59 % comes from Table 9 (0.41 for the 2 MWp North Sea ring). MARIN will see a figure that differs from its own summary text.
Fix: write "34–59 % (D5.1, Table 9)" at first use in 3.1, and keep the per-site figures of 6.5.

### M5 – minor – the conclusion of Energies 19(7) 1609 is omitted (KER5 l.488; 6.5 l.1166)
What is wrong: the paper also finds an average reduction of axial connector loads, local increases from horizontal module motions, and "recommendations for improving the farm configuration to further reduce fatigue and survival loads" (abstract). The last point is the service MARIN offers.
Fix: add to 6.5: "The paper gives recommendations for the farm layout to reduce fatigue and survival loads on modules and connectors."

---

## Ceit (KER6)

### E1 – minor – Ceit's WP5 leadership is not stated (6.6, KER6)
What is wrong: Ceit led WP5, Predictive modelling and simulation tools for material properties and structural integrity management (index l.98–100; NaturSea webinar summary l.52), and its deliverables D5.3–D5.7. 6.6 mentions only Task 6.1.
Fix: in 6.6, before Result 1: "Ceit led WP5, the predictive modelling and structural integrity management tools (D5.3–D5.7), and the sensing and monitoring task of the validation work package (Task 6.1)."

### E2 – wording – "resolution" and "accuracy" are used for the same figure (l.489 against l.1187)
Quotes: KER6 "Sensor resolution of about 0.17 mm of material loss in the laboratory (D5.4)"; 6.6 "detected material loss around a rebar with an accuracy of about 0.17 mm".
What is wrong: D5.4 says "resolution of approximately 0.17mm" (l.517); the Sensors paper says "accuracy of approximately 0.17 mm" (abstract).
Fix: use "about 0.17 mm" with the source's own term, for example "material loss quantified to about 0.17 mm in the laboratory (D5.4; Sensors 24(13) 4211)", in both places.

### E3 – minor – the 3.1 hinge bullet makes Ceit appear to have declined the hinge work (l.459)
Quote: "Ceit's structural integrity assessment (D5.3) concerns the breakwater; it identified the hinges as the most failure-prone part of the system and left their modelling to the hinge redesign."
What is wrong: D5.3 says that "additional modelling of the mechanical behaviour of the new hinge solution will be done to support this process" and will be reported with the new hinge concept (D5.3 l.1004). D1.8 also says Ceit "performed finite element and structural integrity assessments of … FPV components, and critical structural connections" (D1.8 l.465).
Fix: "Ceit's structural integrity assessment (D5.3) concerns the breakwater. It identified the hinges as the most failure-prone part of the system and foresaw further modelling of the new hinge, to be reported with the new hinge concept; no such report is in the project record. This plan therefore names SINTEF's connection tests and MARIN's basin tests as the inputs to the redesign."

### E4 – minor – a protection decision is attributed to Ceit without a source (7.2 KER6, l.1254)
Quote: "Ceit decides on patenting new developments of the corrosion-monitoring function as they reach field validation".
What is wrong: Ceit's input says nothing about patents. D1.8 gives the owner the task of assessing patentability "before public disclosure or filing" (l.686), not at field validation.
Fix: "Ceit assesses the patentability of new developments of the corrosion-monitoring function before their disclosure (D1.8)."

### E5 – wording – presenters are left unnamed (2.5.5 l.285, l.291)
Quotes: "26–28 March 2025 | 41st Congress … | Ceit"; "17 September 2026 | EU PVSEC 2026 | IFEU".
What is wrong: every other row names the presenter. The 41st GEF paper lists Eibar first (l.234).
Fix: name the presenters from the partner records (KPI partner responses), or write "Unai Eibar (Ceit), first author" if the record does not say who presented. Ask IFEU for the EU PVSEC presenter.

---

## IFEU (KER7)

### F1 – major – the sustainability framework is credited to SINTEF alone; IFEU's D7.1 is missing (l.490, l.534, l.1131, l.1210)
Quotes: "on the sustainability framework of Task 7.1 (led by SINTEF)"; "on the framework of Task 7.1 (SINTEF)"; "the definition of the sustainability framework with the mass and energy balances (Task 7.1)"; "within the sustainability framework of the task led by SINTEF (Task 7.1)".
What is wrong: SINTEF leads Task 7.1. The task's deliverable, D7.1 "Interim report on sustainability definitions and settings", is IFEU's (GA l.3812, l.4657, l.5215–5217; index l.158). The common definitions and settings for all the assessments are set out by IFEU in D7.6 §2.1 (l.303–357). D8.4 names the framework four times and credits it only to SINTEF.
Fix: KER7 and R11: "…on the common definitions and settings of the sustainability framework (Task 7.1, led by SINTEF; D7.1, IFEU) and with data for the mass and energy balances from Clement Germany, Sunlit Sea and ACCIONA". 6.4: "the sustainability framework task with the mass and energy balances (Task 7.1), with IFEU writing the definitions and settings report D7.1". 6.7: "…within the sustainability framework of Task 7.1, led by SINTEF, whose definitions and settings IFEU reported in D7.1".

### F2 – minor – the KER7 protection cell contradicts itself (l.1255)
Quote: "its SUREWAVE application, with scenarios, inventories, indicator results and recommendations, is public in D7.3, D7.5 and D7.6. IFEU's models, inventories and know-how stay with IFEU".
Fix: "…is public in D7.3, D7.5 and D7.6. IFEU's underlying assessment models, databases and know-how stay with IFEU and are exploited as expertise in commissioned studies."

### F3 – minor – IFEU's part in the SAB webinar is missing from the contributors (l.178, l.181)
What is wrong: Heiko Keller (IFEU) answered the environmental questions in the SAB webinar (`2024-11-19_surewave_lunch_webinar_summary.md` l.9, l.51). 2.5.7 says so (l.305), but the "Web events" and "Stakeholder Advisory Board workshops" rows leave IFEU out, and the SAB row also leaves out ACCIONA.
Fix: Web events: "SINTEF, Sunlit Sea, Clement Germany, ACCIONA, MARIN; IFEU answering questions". SAB workshops: "Sunlit Sea, SINTEF, Clement Germany; IFEU and ACCIONA answering questions".

### F4 – minor – IFEU's WP7 leadership is not stated (6.7, l.1210)
What is wrong: IFEU led WP7, Integrated sustainability assessment, which also contains Sunlit Sea's D7.4 and SINTEF's D7.2 (index l.143–163). 6.7 lists only the deliverables IFEU wrote.
Fix: "Its basis in SUREWAVE is the work IFEU led: the integrated sustainability assessment work package (WP7), with the definitions and settings (D7.1), the environmental assessment … (D7.3), … and the report on societal needs and engagement (D8.2)."

---

Findings: 4 major, 28 minor, 8 wording.
