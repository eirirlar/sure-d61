# T150 round 5: D8.4 checked by each non-lead partner's exploitation manager

Persona: the exploitation manager of ACCIONA, Clement Germany, SINTEF, MARIN, Ceit and IFEU, one at a time. Method: I read `scratchpad_t150/d84_merged.md` (1,592 lines, after the round-4 fixes and the de-duplication pass) end to end, annexes included. I checked every passage that names a partner against that partner's exploitation summary, the deliverables it led (D1.8, D4.1, D4.3, D5.1, D5.4, D6.1, D7.3, D7.5), the Grant Agreement task and work-package tables, the Crossref records in `scratchpad_t150/crossref/` and the WP8 KPI record. For round 5 I compared `d84_merged.md` with `d84_merged_r3int.md` and `d84_merged.pre_dedup.md`, sentence by sentence, for every sentence that names a partner, a deliverable or a publication. I also followed every section pointer in the partner passages to its target. "l.N" means a line in `d84_merged.md`. Repo paths are relative to `C:\dev\src\sure-d61`.

## Round 4 partner findings: status

Fixed and checked: 1 (l.978), 2 (l.409), 3 (l.1030, l.843), 4 (l.225), 5 (l.526), 6 (l.967, l.1202, l.1205), 7 (A.3 l.1345, l.809, l.1282), 8 (l.925), 9 (l.406), 10 (l.1129), 11 (l.306, l.1061), 12 (l.1049), 14 (l.409; 6.5 now points to 4.1).

Regressed: 13 (GEOPON wording in the KER4 cell). r4disp records it as fixed. The de-duplication pass then rewrote the KER4 maturity cell and restored the old wording. See finding 1.

## Earlier rejections in the partner area

| Rejection | Holds? | Reason |
|---|---|---|
| rejected_r4 (all items) | Yes | None of them concerns a partner passage. Q66 (Clement's EUPI-PV role) is narrowed, and the D8.4 text no longer depends on it |
| rejected_r3: ACCIONA's summary dated 26 November 2025; "no such contribution has been documented" | Yes | `surewave/background/2025-11-26_acciona_exploitation_and_media_email.md` l.10; 7.4 has D1.8's confirmation step |
| rejected_r2: DIFFRAC validated against the second campaign | Yes | Energies 19(7) l.122 |
| rejected_so_far: 1,030 mixtures, 87 %/97 %, installed cost, prototype built to Clement's geometry | Yes | These still rest only on the final technical report working copy (D22) |
| D4/D4r: Ceit not named among the inputs to the hinge redesign | Yes | D5.3 analyses the breakwater (3.1 step 4, l.278; 7.4 l.1157) |
| D3: no "factor 2–3" | Yes | MARIN's summary says "factor 2-3". D8.4 l.1030 gives D5.1's percentages and only the ratio that follows from them (2.3–2.4) |

## Round 5 check: lost figures, sources and credits; pointers

I compared every partner-related sentence removed between r3int and now with the current text. These facts now each have one home: Energies 17(9) co-authors (6.5 l.1032, A.1, A.23); Clement's D4.1 and D4.3 requirements (6.3 l.961); Clement as a contributing beneficiary of the prototype (KER3 cell, 6.2); the wired-reference check of Ceit's nodes (6.6 l.1055); the ReFRESCO robustness and safety-factor remarks (6.5 l.1028); the KER7 framework and data credits to SINTEF, Clement, Sunlit Sea and ACCIONA (6.7 l.1080); Sunlit Sea's use of the Stadt tests for float loads (6.1 l.892); D7.4's view on the ACCIONA-mix breakwaters (4.6.1 l.699). No figure or partner credit was lost, with two exceptions: finding 1 (a regression) and finding 6 (a credit cut to a bare reference).

Every section pointer in the partner passages leads to the statement it claims. I checked those in 3.1 steps 4–5, the KER2, KER3, KER4, KER5 and KER6 cells, 3.4 R2, R3, R6 and R10, 4.1.1, 6.2–6.7, 7.2 KER6 and KER7, 7.4 and Section 10.

## Findings

### 1 – minor – SINTEF – the GEOPON fix of round 4 was undone by the de-duplication pass (3.2 KER4 cell, l.304)

Quote: "DIC planned for the national project with GEOPON".

What is wrong: Round 4 (finding 13) replaced this with SINTEF's own framing. `d84_merged.pre_dedup.md` holds the fixed text: "DIC to be used in SINTEF's collaboration with GEOPON (a nationally funded project, planned)". The de-duplication rewrite of the KER4 cell brought back the old clause. SINTEF's plan uses future tense for the GEOPON collaboration ("will support collaboration with GEOPON", l.35). It also lists the "nationally funded collaboration with GEOPON" among the reuses that already provide "concrete evidence" (l.70). Its summary table reads "Continued use in projects involving GEOPON" (l.57). "Planned" alone gives only one reading of a mixed source.

Source: `surewave/background/2026-10-02_sintef_exploitation_plan.md` l.35, l.57, l.70; `scratchpad_t150/d84_merged.pre_dedup.md` (KER4 cell); r4disp "13 … FIXED in KER4 cell".

Fix (KER4 maturity cell): "… connection-testing methods in SFI BLUES and FlexiShape; DIC to be used in SINTEF's collaboration with GEOPON (a nationally funded project, planned; Section 10); …". Keep 6.4 and Section 10 as they are (D14).

### 2 – minor – ACCIONA – 3.1 step 4 attributes ACCIONA's density figure to D4.1's Sample 18 (l.274)

Quote: "ACCIONA's input gives its mix as 1,950 kg/m³ and 68 MPa, the values of D4.1's Sample 18".

What is wrong: For Sample 18, D4.1 gives 68 MPa and a density "near 2000 kg/m³" (D4.1 l.1259). The 1,950 kg/m³ figure appears only in ACCIONA's summary. 6.2 (l.918) states D4.1's wording correctly ("68 MPa at a density near 2,000 kg/m³"), so 3.1 and 6.2 now disagree. The de-duplication cut the earlier sentence that kept the two sources apart.

Source: `surewave/background/2024-01-18_surewave_d4.1_design_characterization_circular_materials.md` l.1259; `surewave/background/2026-09-30_acciona_exploitation_summary.md` (Result 2); D8.4 l.918.

Fix: "LWAC: ACCIONA's input gives its mix as 1,950 kg/m³ and 68 MPa. This is D4.1's Sample 18, made with a CEM III cement (…), for which D4.1 gives 68 MPa at a density near 2,000 kg/m³; the prototype's top slab used it (D4.3) …".

### 3 – minor – ACCIONA, SINTEF and Ceit – the Gijón conclusions leave out two of the authors' findings (6.2, l.935)

Quote: "The authors judge the short-term marine performance satisfactory and call for longer exposure to assess durability over the life cycle."

What is wrong: The preprint abstract calls for longer exposure "under open-sea conditions". The exposure was in a port. It also identifies "instrumentation openings as the most critical durability details". 6.2 mentions the openings only as the place where chloride exceeded the limit. Both points bear on ACCIONA's next step (the 2027–2028 action row, "long-term marine durability, which the Gijón preprint names as the next step") and on Ceit's sensor installation. The three co-authoring partners will want their conclusions quoted in full (requirement 4).

Source: `scratchpad_t150/crossref/10.20944_preprints202611.1592.v1.json` (abstract).

Fix: "The authors judge the short-term marine performance satisfactory and identify the openings made for instrumentation as the most critical durability details. They call for longer exposure under open-sea conditions to assess durability over the life cycle, corrosion development and the long-term effect of biofouling on the hydrodynamic response and mooring loads."

### 4 – minor – IFEU – 7.2 KER7 states that the databases stay with IFEU (l.1131)

Quote: "IFEU's underlying assessment models, databases and know-how stay with IFEU and are exploited as expertise in commissioned studies".

What is wrong: IFEU's assessments rest on third-party databases. D7.3 uses ecoinvent and D7.5 uses the Social Hotspots Database, both licensed from their providers. D1.8 records no IPR position for IFEU, and IFEU's summary sets out none. IFEU will not accept a sentence that places licensed third-party databases among its own results or background.

Source: `surewave/background/2025-10-06_surewave_d7.3_environmental_report.md` (ecoinvent); `surewave/background/2025-10-06_surewave_d7.5_social_report.md` (SHDB); `surewave/background/2026-09-30_surewave_d1.8_ipr_management_plan_m36.md` (no IFEU entry in Table 2).

Fix: "IFEU's own assessment models, inventories and know-how stay with IFEU and are exploited as expertise in commissioned studies; the third-party life-cycle and social-risk databases used (ecoinvent, Social Hotspots Database) remain under their providers' licences."

### 5 – minor – IFEU – the EU PVSEC 2026 contribution appears in the KPI record as a reported publication, but D8.4 counts it only as a talk, without saying so (2.5 evidence paragraph, l.221; A.1)

What is wrong: The KPI record's publication row lists one partner-reported item, EU PVSEC, and A.5 gives the contribution a paper-style title ("… Is It Worth the Effort"). The KPI record notes that the paper is not found in Crossref and that the proceedings archive can only be searched in a browser. D8.4 counts the item as a conference and a talk. It does not say whether a proceedings paper exists or why it is not among the 10 publications. D8.4 names its other non-counted publications (Ceit's *Sensors* 25 and MARIN's kick-off talk) with the reason, so IFEU's exploitation manager will expect the same here.

Source: `scratchpad_t150/companions/2026-11-19_surewave_wp8_kpi_verification.md` l.25, l.72.

Fix (2.5, after the Ceit *Sensors* sentence): "IFEU's EU PVSEC 2026 contribution is counted as a talk; a proceedings paper has not been found in Crossref and is not counted as a publication."

### 6 – wording – Ceit – the R1 evidence cell lists D5.7 without its role (3.4 R1, l.341)

Quote: "Basin tests: D6.2 (MARIN); Energies 17(9) 2059 (2024) and Energies 19(7) 1609 (2026), both led by MARIN; D5.7 (Ceit)."

What is wrong: The de-duplication cut the clause "its results are also used in D5.7 (Ceit)". The cell now cites Ceit's validation report as evidence for the basin tests without saying how it relates to them.

Fix: "… both led by MARIN; D5.7 (Ceit), which used the second campaign to confirm that slamming loads on the breakwater are negligible (Section 6.6)."

### 7 – wording – MARIN – the KER5 maturity cell merges two validations against different data (3.2 KER5, l.305)

Quote: "applied to a 2 MWp farm and validated against measured motions (D5.1; Energies 19(7) 1609)".

What is wrong: The cell gives no hint that one of the two data sets comes from tests outside SUREWAVE. A reader of the table alone can take both as SUREWAVE basin measurements (D35). The pre-dedup cell named both.

Fix: "… validated against the motions measured in Sunlit Sea's earlier Stadt Towing Tank tests (D5.1) and in the second SUREWAVE basin campaign (Energies 19(7) 1609)".

### 8 – wording – all publishing partners (MARIN in particular) – the deposit sentence in A.23 is in a tense that will be wrong once the plan is submitted (l.1546)

Quote: "The partners deposit these five in the SUREWAVE community on Zenodo before this plan is submitted, so they are deposited after publication. For the MARINE 2025 paper … MARIN deposits the accepted manuscript under CC BY if its publishing agreement with CIMNE allows it; otherwise … MARIN reports this in the final periodic report."

What is wrong: The submitted document will describe as future an action that should then be complete. The open-access paragraph in 2.5 (l.256) still says the five "were not deposited at publication", which is correct, but gives no deposit state at submission. This follows D48 and D62 and owner question Q (D48). The text itself should not say "before this plan is submitted".

Fix: before submission, replace with the outcome: "The five were deposited in the SUREWAVE community on Zenodo in [month] 2026, after publication." For MARINE 2025, state the result of MARIN's check with CIMNE. Until then: "The partners are depositing these five …".

---

Findings: 0 major, 5 minor, 3 wording.
