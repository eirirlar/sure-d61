# D8.4 review, round 5: the coordinator (SINTEF), who submits D8.4

Scope: d84_merged.md (1,592 lines, after the round-4 fixes and the one-home de-duplication pass; identical to d84_merged_r4.md), read end to end. It was checked against D1.8 (surewave/background/2026-09-30_surewave_d1.8_ipr_management_plan_m36.md), the corrected exploitable results report (scratchpad_t150\companions\2026-09-30_surewave_exploitable_results_report.md, "ERR"), the EIC Transition proposal (generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md, "EIC"), SINTEF's exploitation plan (surewave/background/2026-10-02_sintef_exploitation_plan.md), the GA, D8.5 and Energies 19(7) 1609 (surewave/background/2026-03-25_bunnik_hydrodynamic_simulations_2mw_offshore_solar_fpv.md). The final technical report working copy was not used (D22). "D84:n" is a line in d84_merged.md. Decisions D1–D65, the rejections of rounds 1–4 and owner_questions.md were applied.

Round-5 loss check: I compared d84_merged.pre_dedup.md with d84_merged.md hunk by hunk with a script. It lists every figure, name, DOI and deliverable number that was removed from a changed paragraph and checks whether it still appears somewhere in the document. All removed figures and sources survive elsewhere, except the bare string "Preprints 202611.1612, 2026", which survives as "Preprints 202611.1612 (2026)". Every "Section x.y" reference resolves to an existing heading, and every deliverable cited in the body is in Annex B. No figure, source or credit was lost. The de-duplication pass did reintroduce two round-4 coordinator findings (findings 1 and 2), and four pointers now lead to a statement that is incomplete or does not hold (findings 3, 4, 10, 11).

Checked and found consistent (no finding): D1.8 Table 2 and Table 3, its §4.1, §4.3 and §4.5 lists and its conclusions (D1.8 :265–291, :306–320, :371, :395–401, :485–527, :661–691), as used in 2.4, 3.1 step 4, 5, 7.1, 7.2 (KER2, KER5) and 7.4; the EIC rights statement (EIC :26) and the 7.4 paragraph about it (D84:1155); the EIC topic, applicants, work-package leads, months M6, M12, M22 and M34, and the 50–300 kWp demonstrator capacity in the requirements task (EIC :4, :26, :72, :294, :312, :369, :373, WP4–WP6 tables :395–450); "1–5 MWp immediately after project completion" and "within 12–24 months after completion" (EIC :68, :254), as used in 4.6.2; the EIC "TRL 4" basis and its evidence date, the Interim Progress Report to 31 October 2024 (EIC :36, :44), as used in 4.1; SINTEF's six results, its routes, CIRCWIND, SFI BLUES, FlexiShape and GEOPON as used in 6.4, 10 and 14 (SINTEF plan :7–70); the KPI counts in the executive summary and in 2.5 (16 targets, 11 met; 22 reach targets: 3 met, 1 met for 2024 only, 3 partly, 5 not met, 7 not measured, 1 not shown, 2 open); the 60-day final report date (1 March 2027); Annex B against the body.

## Status of my round-4 findings

| r4 # | Status in this draft |
|---|---|
| 1 ERR five differences | Fixed in the companion (ERR:9, :58, :68, :137, :159). Repo copy: owner question Q90 |
| 2 DIFFRAC already released (7.4 row 3) | Fixed (D84:1147) |
| 3 EIC rights statement against the Q1 2027 confirmation | Fixed (D84:1155) |
| 4 "principal generating partner" | Fixed (D84:855, :1115) |
| 5 2.4 "identified" stated as done | Fixed (D84:153) |
| 6 "is covered by access rights" | Fixed (D84:855) |
| 7 Q1 2027 confirmation stated as a fact | Fixed in round 4, then reverted in 4.5, 4.9 and 14 by the de-duplication pass (finding 1) |
| 8 D6.4 presented as a report that holds the results | Fixed in 6.2, R3 and R4. Reintroduced in the 3.2 KER2 cell by the de-duplication pass (finding 2); still open in the ERR (finding 8) |
| 9 Annex B D8.1 | Fixed (D84:1585) |
| 10 FTO wording | Fixed (D84:1153) |
| 11 WP2 named three ways | Fixed (D84:15, :890, :1305) |
| 12 "review" added to the D1.8 list | Fixed (D84:1113) |
| 13 ERR rules and "draft" | Fixed (ERR has no "---"; ERR:165 "version 1.0") |

## Major

None.

## Minor

### 1. Minor. The de-duplication pass reverted the round-4 fix: 4.5, 4.9 and Section 14 again state as a fact the Q1 2027 confirmation by SINTEF, Ceit and MARIN

- Where:
  - 4.5 milestones, D84:638: "access-rights requests to SINTEF and MARIN, before the design freeze, and the confirmation of contributions to the hinge redesign (Q1 2027; Sections 7.4 and 9)".
  - 4.9, D84:809: "Access-rights requests to SINTEF and MARIN ..., and the confirmation of contributions to the hinge redesign and the breakwater design, both in Q1 (Sections 7.4 and 9)".
  - Section 14, 2027 row, D84:1296: "access-rights requests and confirmation of contributions to the hinge redesign and the breakwater design (Sections 7.4 and 9)".
  - Executive summary, D84:34: "after the partners have confirmed their contributions to the hinge redesign".
- What is wrong: round 4 (r4_coord #7, r4disp "FIXED – 4.5, 4.8, 4.9, Section 5, 9, 14 now 'ask ... to confirm, as proposed in Section 7.4'") changed these passages to Sunlit Sea's request and the WP8 lead's proposal. d84_merged.pre_dedup.md still has that wording at :810, :1176 and :1297. The current file no longer has it in 4.5, 4.9 or 14. Section 9 (D84:1175, "Sunlit Sea and Clement Germany ask for the confirmation") and Section 5 (D84:855, "the WP8 lead proposes this confirmation") keep the correct framing. In 4.5, 4.9 and 14 the text again commits SINTEF, Ceit and MARIN to a Q1 2027 confirmation that none of their inputs contains (D18). The coordinator would be submitting a date on behalf of three beneficiaries.
- Source: decisions.md D18; r4disp.md (r4_coord 7); d84_merged.pre_dedup.md :810, :1176, :1297; D84:1157 (7.4, "The WP8 lead proposes ...").
- Fix:
  - 4.5: "access-rights requests to SINTEF and MARIN, before the design freeze, and Sunlit Sea's request to SINTEF, Ceit and MARIN to confirm the contributions to the hinge redesign, as proposed in Section 7.4 (Q1 2027; Sections 7.4 and 9);".
  - 4.9: "... and, as proposed in Section 7.4, the request by Sunlit Sea and Clement Germany to SINTEF, Ceit and MARIN to confirm the contributions to the hinge redesign and the breakwater design, both in Q1 (Sections 7.4 and 9);".
  - Section 14: "access-rights requests; confirmation of the contributions to the hinge redesign and the breakwater design requested from SINTEF, Ceit and MARIN, as proposed in Section 7.4 (Sections 7.4 and 9);".
  - Executive summary: "after the contributions to the hinge redesign have been confirmed with the partners concerned, as proposed in Section 7.4 (Sections 7.2 and 7.4)".

### 2. Minor. The 3.2 KER2 cell cites D6.4 as evidence again; the record holds no copy of it

- Where: 3.2, KER2, maturity cell, D84:302: "Validated in the laboratory and in the reduced-scale breakwater prototype exposed at Gijón (D4.1, D4.2, D4.3, D6.4, all ACCIONA; Preprints 202611.1592; Section 6.2)".
- What is wrong: round 4 changed every D6.4 citation to "the subject of D6.4" (r4_coord #8), since Annex B gives D6.4 as "– (results cited from Preprints 202611.1592)" (D84:1578) and its submission status is owner action 7. The pre-dedup cell had "Task 6.5, ACCIONA, the subject of D6.4" (pre_dedup :302). The shortened cell lists D6.4 with D4.1–D4.3 as evidence of validation. If D6.4 is not in the portal when D8.4 is submitted, the coordinator submits a deliverable that cites a missing deliverable as evidence.
- Source: D84:1578; owner_questions.md action 7; d84_merged.pre_dedup.md :302; D84:343–344 (R3 and R4 keep "the subject of D6.4").
- Fix: "(D4.1, D4.2, D4.3, all ACCIONA; Task 6.5, ACCIONA, the subject of D6.4; Preprints 202611.1592; Section 6.2)".

### 3. Minor. The 3.2 KER4 cell now attaches "validation against field data is future work" to Surewave-ANN, and its pointer leads to a statement about the other models

- Where: 3.2, KER4, maturity cell, D84:304: "Surewave-ANN kept as an internal research tool; validation against field data is future work (Section 3.4, R5)".
- What is wrong: the pre-dedup cell said "Validation of the aerodynamic and hydrodynamic models against field data, and further validation against experiments, is future work (SINTEF)" (pre_dedup :304). In the shortened cell the clause follows Surewave-ANN and has no subject of its own, so it reads as a statement about the ANN tool. R5 (D84:345), the target of the pointer, concerns the aerodynamic method and the breakwater model. SINTEF's plan gives that future work for the aerodynamic and hydrodynamic modelling (SINTEF plan :13). For Surewave-ANN it gives "validation against data from other circular and marine concrete applications" (:27).
- Source: SINTEF plan :13, :27; D84:345; pre_dedup :304.
- Fix: "... Surewave-ANN kept as an internal research tool. Validation of the aerodynamic and hydrodynamic models against field data is future work (Section 3.4, R5)."

### 4. Minor. 3.4 R1 now says that Sunlit Sea's D3.1 and D3.4 designed the D7.4 reference plant

- Where: 3.4, R1, delivered cell, D84:341: "the design of the floating PV array and of the global system (D3.1, D3.4) for the open-sea reference design, the D7.4 reference plant and a 2 MWp version (Section 4.1)".
- What is wrong: the pointer leads to 4.1, which says something different (D84:377). D3.4 placed 7.16 MWp in Clement Germany's ring with the panels of the time. The 2 MWp version comes from Clement Germany's later material quantities. The D7.4 reference plant (10.4 MWp, about 730 Wp modules) is D7.4's own change of panels. The pre-dedup cell kept these apart ("a 10 MWp-class array (10.4 MWp installed in the D7.4 reference plant; Section 4.1)", pre_dedup :341). Read alone, the shortened cell credits D3.4 with a layout it did not make, and leaves out Clement Germany's 2 MWp quantities.
- Source: D84:377; pre_dedup :341.
- Fix: "the design of the floating PV array and of the global system (D3.1, D3.4) for the open-sea reference design, which D7.4 develops into the D7.4 reference plant and a 2 MWp version (Section 4.1)".

### 5. Minor. D8.4 credits D8.5 to Sunlit Sea alone; D8.5's version table lists a SINTEF co-author on its final versions

- Where: 2.5, D84:258, "As WP8 lead it wrote the dissemination, exploitation and communication master plan D8.1 and its update D8.5"; 4.2, D84:455, "the technical lead, author of Sunlit Sea's deliverables D2.4 (Stakeholder Advisory Board), D7.4 (economic assessment) and D8.5 (WP8 master plan)"; 6.1, D84:894, "Sunlit Sea wrote the dissemination and exploitation plans D8.1 and D8.5".
- What is wrong: D8.5's version table gives "Eirik Larsen/ Balram Panjwani" as the authors of version 2.0 (29 April 2024, final version) and version 3.0 (15 August 2024, revised after the project officer's comments). Version 3.0 is the version Annex B cites. Decision D36 asks D8.4 to credit SINTEF where it contributed, and the brochure line in the same paragraphs already does so ("D8.3 with SINTEF"). Sunlit Sea's lead of D8.5 stands; the sole authorship does not. D2.4 lists Balram Panjwani as the reviser of version 1.1 and as reviewer, and Eirik Larsen as author of the final version, so "author of D2.4" holds.
- Source: surewave/background/2024-04-29_surewave_d8.5_dissemination_exploitation_communication_master_plan.md :38–50; surewave/background/2024-04-22_surewave_d2.4_stakeholder_advisory_board.md :42–48, :86.
- Fix: 2.5 "As WP8 lead it wrote the master plan D8.1 and led its update D8.5, with SINTEF as co-author of D8.5's final versions, and checked each figure ..."; 4.2 "author of Sunlit Sea's deliverables D2.4 and D7.4 and lead author of D8.5, with SINTEF"; 6.1 "Sunlit Sea wrote D8.1, led D8.5 with SINTEF, led the technical brochure D8.3 with SINTEF, and wrote this plan".

### 6. Minor. The ERR still calls Generation 2 the "product core" of KER1; D8.4 names Sunlit Sea's SUREWAVE results first and CONNECT as their commercial carrier

- Where: ERR:62, "Sunlit Sea ER4 is its product core: the Generation 2 floating platform"; ERR:25 (summary bullet). D8.4: 3.2 KER1 (D84:301), 3.4 R1 (D84:341), 6.1 (D84:907), 7.1 (D84:1117).
- What is wrong: decision D63 asks D8.4 to name Sunlit Sea's SUREWAVE results first (D3.1, D3.4, the hinge redesign, the D7.4 cost model) and CONNECT, developed in SuRE, as their commercial carrier. D8.4 does this in all four places. The companion, which ships with D8.4 and states that it is "aligned with D8.4 Section 3" (ERR:5), still makes the SuRE-developed platform the core of the SUREWAVE KER. A reviewer comparing the two documents finds two answers to the question of what KER1 is. ERR:62 also writes "The SUREWAVE reference design kept aluminium floats" without "Generation 1", which D8.4 uses throughout (D63).
- Source: decisions.md D63; D84:301, :1117; ERR:5, :25, :62.
- Fix: ERR:62 "KER1 is the global solution of the Grant Agreement, marketed by Sunlit Sea. Its SUREWAVE results are Sunlit Sea's design of the floating PV array and the global system (D3.1, D3.4), the hinge redesign, the nearshore models with the wave-loss module (ER1–ER3) and the economic assessment and cost model (D7.4). Its commercial carrier is Sunlit Sea CONNECT (ER4), the Generation 2 platform with cast polyurethane floats, developed in the parallel project SuRE on the results of the Generation 1 aluminium-float SUREWAVE array. ..." Then continue from "The tests showed ...". Change "kept aluminium floats" to "used Sunlit Sea's Generation 1 aluminium floats". ERR:25 "... Sunlit Sea's Generation 2 float, the commercial carrier of KER1, developed in the parallel project SuRE and commercialised as Sunlit Sea CONNECT."

### 7. Minor. The ERR's open point 5 still gives one completion point for all software results; D8.4 7.4 now treats the DIFFRAC scale-up separately

- Where: ERR:158, "protection and licensing status of the software results before their first external release".
- What is wrong: round 4 split the row in D8.4 (D84:1147). Surewave-ANN and the SHMS tools are confirmed before their first external release. The DIFFRAC scale-up is already available to licence subscribers, so MARIN confirms its status at the first annual review, by the end of Q3 2027. The companion repeats the old single date, which for MARIN has already passed. ERR:5 says the companion's IPR actions are aligned with D8.4 Section 7.4.
- Source: D84:1147; ERR:5, :158.
- Fix: ERR:158 "... protection and licensing status of Surewave-ANN and the SHMS tools before their first external release, and of the DIFFRAC scale-up, which MARIN already provides to licence subscribers, at the first annual exploitation review (by the end of Q3 2027); ..."

### 8. Minor. The ERR still cites D6.4 as a source for the Gijón exposure

- Where: ERR:82, "exposed for nine months (Task 6.5, led by ACCIONA; D6.4; Preprints 202611.1592)".
- What is wrong: this is the same point as r4_coord #8, which was fixed in D8.4 and not in the companion. The record holds no copy of D6.4 (D84:1578; owner action 7).
- Fix: "(Task 6.5, led by ACCIONA, the subject of ACCIONA's deliverable D6.4; results in Preprints 202611.1592)".

## Wording

### 9. Wording. 3.2 KER4 puts the completed FlexiShape project in the present tense

- Where: D84:304, "Finite element methods being reused in CIRCWIND and connection-testing methods in SFI BLUES and FlexiShape".
- What is wrong: "being reused" now governs FlexiShape, which ended in 2025 (Section 10, D84:1200; 6.4, D84:999, "Reuse during the project"). The pre-dedup cell had "connection-testing methods reused in SFI BLUES and FlexiShape".
- Fix: "Finite element methods being reused in CIRCWIND; connection-testing methods reused in SFI BLUES and, for the fatigue setup, in FlexiShape;".

### 10. Wording. 3.4 R1 lists D5.7 (Ceit) as basin-test evidence without saying why

- Where: D84:341, evidence cell, "Basin tests: D6.2 (MARIN); Energies 17(9) 2059 (2024) and Energies 19(7) 1609 (2026), both led by MARIN; D5.7 (Ceit)."
- What is wrong: the reason was cut ("its results are also used in D5.7 (Ceit)", pre_dedup :341). Without it, a reader takes Ceit's validation report for a basin-test report. 6.6 says D5.7 used the second campaign to confirm that slamming loads on the breakwater are negligible (D84:1061).
- Fix: "...; D5.7 (Ceit), which uses the second campaign's results (Section 6.6)."

### 11. Wording. The 2.1 outcome row on panel frames points to a section that does not mention them

- Where: D84:102, "this plan does not assess what the panel frame adds to the float's robustness (Section 4.1)".
- What is wrong: 4.1 does not mention the panel frame. The pointer supports only the first half of the cell.
- Fix: "The cast polyurethane structure of the Generation 2 float (Section 4.1) carries the standard panel; this plan does not assess what the panel frame adds to the float's robustness."

### 12. Wording. The hinge record cites only D7.2 for the paired connectors; MARIN's own paper states it

- Where: 4.1, D84:409, "fitted in pairs between adjacent floats (D7.2, Preprints 202611.1173)".
- What is wrong: Energies 19(7) 1609 states "adjacent FPV modules are connected through a pair of connectors" and gives the stiffness of the pair (bunnik file :71, :73). The D8.3-difference bullet (D84:384) attributes the pairing to MARIN's papers, so the two passages cite different sources for the same fact. Both are right. Citing both credits MARIN's own record of its campaign (D36).
- Fix: "fitted in pairs between adjacent floats (Energies 19(7) 1609; D7.2, Preprints 202611.1173)".

### 13. Wording. The ERR's mooring entry lacks the trade-off that D8.4 now gives

- Where: ERR:110 (MARIN ER2).
- What is wrong: D8.4 6.5 (D84:1030) gives D5.1's trade-off under decision D64: fairlead tensions up to about 2.5 times higher, and the weighting between mass and tension left open with Clement Germany. The companion gives the mass reductions only. A reader of the companion alone sees lighter moorings without their cost.
- Fix: add to ERR:110: "The lighter moorings carry fairlead tensions up to about 2.5 times the reference; D5.1 presents the optima on the Pareto front of mooring mass and fairlead tension, with the weighting left open after consultation with Clement Germany."

## Observation for the owner (not a D8.4 finding)

- The EIC Transition proposal, which SINTEF coordinates and submitted, says "The company is led by Eirik Larsen (CEO)" (EIC :272). docs/project_facts.md :18–19 gives Per Lindberg as CEO and Eirik Larsen as technical lead, and D8.4 4.2 follows the facts file without names. D8.4 names no person in 4.2, so it is not wrong. If the EIC proposal reaches the interview stage, the team description there needs correcting. This could go on the owner list next to Q88/Q91.

## Rejections in my area: does each hold?

| Rejection | Holds? | Comment |
|---|---|---|
| disp_A A#3; D1rr; D58 (cover "Coordinator: SINTEF", no parenthetical) | Yes | D84:5, :1202 |
| disp_A A-gap11; r2disp_A r2_cinea#F2; r3disp_A #6 (extension wording, due month) | Yes | D84:5 |
| disp_E ledger_E #5, #108, W21 (end 31 December 2026; 2027 and 2030 windows) | Yes | |
| r1disp_D r1_coord#12, r1_cinea#F24; D4 (Ceit not a hinge-redesign input) | Yes | 3.1 step 4 (D84:278) and 7.4 (D84:1157) keep Ceit in the D1.8 confirmation and out of the redesign credit |
| r1disp_E r1_cinea#21 (strategic assets) | Yes | D84:1258 |
| r1disp_E r1_cinea#10 d; Q29 (IP and exploitation workshops) | Yes | D84:153, :272 |
| r1disp_E r1_coord#29, r1_cinea#30; r2disp_D r2_owner#22 (EUPI-PV deadline before submission) | Yes | Owner actions 9 and 11. The 1 December deadline falls before submission, so the 6.3, 10 and 4.6.2 statements must be updated then |
| r2disp_E r2_cold#5 (Section 13 as text) | Yes | |
| r3disp_E r3_partners#6, r3_cold#7 | Yes | |
| r3disp_A #20 (ACCIONA summary date) | Yes | |
| r1disp_D r1_writing#6, r2disp_D r2_writing#7 (EDP named) | Yes | EIC :26 |
| r4disp F8 (D6.4, D7.6 amended due dates: owner action 4) | Yes | The draft text itself must still not present D6.4 as delivered (findings 2 and 8) |
| r4disp r4_facts 6 (Q3 2027 against mid-2027) | Yes | Owner action 8b |
| r4disp r4_cold #1 (one home per item) | Overtaken | The de-duplication pass has done it; findings 1–4 and 9–10 are its side effects |

Findings: 0 major, 8 minor, 5 wording.
