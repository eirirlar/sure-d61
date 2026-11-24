# D8.4 review, round 3: the coordinator (SINTEF), who submits D8.4 to CINEA

Scope: d84_merged.md (round-2 integrated and restructured draft, 1,541 lines, read end to end), checked against the SUREWAVE deliverables, the exploitable results report in the companions folder, the EIC Transition proposal (generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md), SINTEF's exploitation plan, and for statements the coordinator could not defend to CINEA or the partners. The final technical report working copy was not used (D22). Decisions D1–D45 and the round-1 and round-2 revisions were applied. Where a finding is an error inside a decision, it says so.

"D84:n" is the line in scratchpad_t150\d84_merged.md. Repo paths are relative to C:\dev\src\sure-d61. CORDIS was fetched again with curl on 24 November 2026 (https://cordis.europa.eu/project/id/101083342?format=xml).

## Status of my round-2 findings

| r2 # | Status in this draft |
|---|---|
| 1 duration and due month | Fixed (D84:5) |
| 2 D7.4 panels and layout | Fixed (D84:365) |
| 3 internal exploitation workshops | Fixed in 3.1 step 3 (D84:258); the Section 1 coverage table still reads as if the workshops were held (finding 12) |
| 4 "each with its status" | Fixed (D84:36, :173, reach table extended) |
| 5 CORDIS lists D7.6 | Fixed in A.23, but the date given is the project page's, not the D7.6 entry's (finding 6) |
| 6 D3.4 Sensitive | Withdrawn. My r2 finding read a misaligned row of the GA summary table. The GA's detailed entry for D3.4 says "PU - Public" (GA :4967), and D3.4's own cover says Public. Annex B is right. One naming point remains (finding 7) |
| 7 hinge inputs / D5.3 | Fixed (D84:264) |
| 8 further D8.3 differences | Fixed (D84:367–373) |
| 9 EDP role, second site | Fixed. My premise that "route to scale" is not the proposal's term was wrong: the consortium section of the proposal says "EDP (PT) -- End-user, adopter and route to scale" (proposal :274). Either wording is the proposal's |
| 10 "before 28 February" | Fixed |
| 11 SINTEF rows and EUPI-PV content | Fixed (D84:988, :1158); one conditional in Clement's row is off (finding 10) |
| 12 SINTEF lead roles | Fixed (D84:966) |
| 13 Zenodo v1.0 records | Fixed (D84:886, :1489) |
| 14 website 2024 visits | Fixed |
| 15 DNV 2022 statement | Fixed (D84:1112) |
| 16 40 % transmission | Fixed; D3.2 :1705 states it in the summary ("These waves are reduced by the FB to at least 40% of the incident wave height") |
| 17 breakwater-class date | Fixed |
| 18 PhD and R&D lines | Fixed (reach table, 3.5) |
| 19 CIRCWIND entity | Applied, but my premise no longer holds (finding 5) |
| 20 TRL source D7.2 | Fixed |
| 21 companion report | Not fixed (finding 3) |
| 22 15-day notice | Fixed |
| 23 €9.75M / €9.8M | Fixed |
| 24 access-rights timing | Fixed |

---

## Major

### 1. Major. D1.8's table of remaining IPR actions is not carried into the plan

- Where: Section 7 (D84:1076–1102), Section 9 (D84:1120–1142), Section 12 (D84:1177–1189), Section 13 roles (D84:1230–1234), Section 14 (D84:1251–1259).
- What is wrong: D1.8, the coordinator's IPR management plan at month 48, ends with "Table 3. Remaining IPR Actions, Responsible Partners, and Completion Points". It assigns seven actions that fall in the exploitation period. D8.4 takes over only one of them (freedom to operate, 7.3). The others are missing:
  - confirm ownership and inventor contributions for the final modified hinge designs (Sunlit Sea and documented contributors; before protection, licensing or commercial deployment);
  - confirm the final ownership status of commercially relevant breakwater results (Clement Germany and documented contributors; before a commercial or licensing agreement);
  - confirm the protection and licensing status of software-related results (SINTEF, Ceit, MARIN and relevant owners; before external release or licensing);
  - archive the dissemination-review and non-objection evidence (project management and output owners; at project closure);
  - identify access requirements for integrated post-project deployment (relevant result owners; before a demonstration or commercial agreement);
  - perform result-specific patentability or registered-design assessment (relevant owner; before public disclosure or filing).

  D8.4 is the exploitation plan that D1.8 hands these actions to ("The detailed exploitation of the Results remains the responsibility of the corresponding owners and is addressed under WP8", D1.8 :663). CINEA reads both deliverables, and the coordinator would have to explain why the WP8 plan drops the IPR plan's open actions. Several of them fall on dates that D8.4 already sets: the agreement with Clement Germany (2027), the design-registration decision (Q3 2027), the first reference plant (Q3 2027), the EIC Transition demonstrator (from 2027) and DIFFRAC and Surewave-ANN licensing.
- Source: surewave/background/2026-09-30_surewave_d1.8_ipr_management_plan_m36.md:663, :667–691 (Table 3), :291.
- Fix: add to Section 7, after 7.1, a subsection "7.4 Remaining IPR actions from D1.8", and give the dated ones a row in Section 14:

  "The IPR management plan D1.8 (SINTEF, September 2026) lists the IPR actions that remain after the project. This plan assigns them as follows.

  | Action (D1.8, Table 3) | Responsible | Completion point in D1.8 | Date in this plan |
  |---|---|---|---|
  | Confirm ownership and inventor contributions for the final hinge design | Sunlit Sea, with SINTEF, Ceit and MARIN as documented contributors | Before protection, licensing or commercial deployment | Q1 2027, with the access-rights requests, before the design freeze and the design-registration decision |
  | Confirm the final ownership status of the breakwater results used commercially | Clement Germany and documented contributors | Before a commercial or licensing agreement | Before the engineering and supply agreement with Sunlit Sea (2027) |
  | Confirm the protection and licensing status of software-related results | SINTEF (Surewave-ANN), Ceit (SHMS), MARIN (DIFFRAC scale-up) | Before external release or licensing | Reported at the first annual exploitation review (Q3 2027) |
  | Archive the dissemination-review and non-objection evidence | The coordinator and the owners of each output | At project closure | By 31 December 2026 |
  | Identify access requirements for integrated deployment | The owners of the results used | Before a demonstration or commercial agreement | Before the EIC Transition grant and consortium agreements, if the project is funded, and before the agreement with Clement Germany |
  | Patentability or registered-design assessment | Each result owner | Before public disclosure or filing | Before each publication; for KER1 by Q3 2027 (Section 7.2) |
  | Freedom-to-operate assessment | The commercialising partner | Before market deployment | KER1 by Q3 2027 (Section 7.3) |"

### 2. Major. D8.4 states the ownership of the hinge redesign and of the breakwater as settled; D1.8 says it is to be confirmed

- Where: Section 5, D84:850, "The redesign is Sunlit Sea's result; testing, modelling and technical feedback did not in themselves create joint ownership of it (D1.8)"; Section 7.1, D84:1082, "Applied to KER1, the WP8 lead proposes this split. Sunlit Sea's SUREWAVE results are the Generation 2 architecture with the redesigned full-edge hinge …"; Section 3.2 KER1 row and Section 4.1, "Integrating them transfers no ownership: they remain Clement Germany's (D1.8)"; Section 7.2 KER1, design-registration decision by Q3 2027.
- What is wrong: D1.8 does not settle the hinge ownership. Its section 4.5 says: "Before any patent, registered-design, licensing, or commercial deployment decision is taken, the relevant partners should confirm: the chronology of the design changes; the inventor or designer contributions; the distinction between pre-existing Background and new Results; the contribution of each testing and modelling activity; and whether any inseparable contribution requires a joint-ownership arrangement." Its Table 2 note says the ownership information "should be confirmed by the relevant Result owners before any patent filing, registered-design application, licence, assignment, joint-development agreement, or commercial deployment." For the breakwater, Table 2 gives "Partner-specific foreground, subject to confirmation of any documented inseparable contributions". D1.8 also names Ceit's finite element, fatigue and structural assessment among the inputs to the hinge refinement (:497, :511). D8.4 cites D1.8 for the rule that testing alone creates no joint ownership, which is correct, and leaves out the confirmation step that D1.8 attaches to it. The plan then schedules a design registration (Q3 2027) and a commercial plant (Q3 2027) with no confirmation step before them. SINTEF wrote D1.8 and cannot defend a plan that skips the step its own deliverable sets. The decision to name only SINTEF and MARIN as redesign inputs (D4) is not in question. The confirmation is a separate step, and it runs with the documented contributors that D1.8 names.
- Source: D1.8 :85, :291, :497–527 (section 4.5), :272 (breakwater row), :676 (Table 3).
- Fix: D84:850, after "(D1.8)": "D1.8 asks Sunlit Sea and the documented contributors (SINTEF, Ceit and MARIN) to confirm the chronology of the design changes, the designer contributions and the split between background and results before any registration, licence or commercial deployment. Sunlit Sea requests this confirmation together with the access rights, in writing in Q1 2027." D84:1082, replace "the WP8 lead proposes this split" with "the WP8 lead proposes this split, to be confirmed with the documented contributors before the design-registration decision (D1.8, section 4.5; Section 7.4)". 3.2 KER1 row and 4.1: "they remain Clement Germany's, subject to the confirmation of contributions that D1.8 asks for before a commercial agreement". Add to 4.5 milestones and 4.9 (2027): "ownership of the final hinge design confirmed with SINTEF, Ceit and MARIN (Q1 2027)".

---

## Minor

### 3. Minor. The exploitable results report still differs from D8.4 in four places, and the repo copy is still the old text

- Where: companions\2026-09-30_surewave_exploitable_results_report.md.
- What is wrong (round-2 finding 21, not fixed):
  - Line 11, distribution: "without written consent from the coordinator and from each contributing partner". D8.4 (D84:11) requires "the written consent of the beneficiaries whose information it contains". The two documents set different consent rules for the same SEN material.
  - Line 66: "the WP8 lead grouped them into seven KERs, one anchored in each beneficiary's main contribution". D8.4 3.1 steps 2 and 5 (D84:257, :266) say the WP8 lead proposed seven candidates in the template and mapped the results to them. Line 19 of the same report says the template listed the seven candidates.
  - Line 76: "modelling (MARIN ER1, ER2, SINTEF ER1, ER2, ER3, ER4)" as a route into KER1. D8.4 gives SINTEF no modelling role in KER1 for the concrete methods; its KER1 role is testing and qualification (Section 5 table, D84:864; KER4 relation "Test and qualification services", D84:291).
  - Line 171: "the SINTEF-to-Sunlit Sea hinge transfer". A reader takes "transfer" as a transfer of results under the Grant Agreement. It was a technical input.
  - The repo copy surewave/deliverables/2026-09-30_surewave_exploitable_results_report.md is still the old version: line 19 ("between 4 and 30 September 2026"), lines 32, 56, 107, 154, 159 ("Mikroflexishape", "Marisol", "planning platform"), 118 ("factor 2–3 reduction"), 179 ("revision 3").
- Fix: line 11, "… without the written consent of the beneficiaries whose information it contains"; line 66, "The WP8 lead proposed seven candidate KERs, one anchored in each beneficiary, and mapped the reported results to them; no partner proposed a KER of its own"; line 76, "modelling (MARIN ER1, ER2; SINTEF ER1, ER2)"; line 171, "SINTEF's test input to Sunlit Sea's hinge redesign". Replace the repo copy with the companion before submission.

### 4. Minor. The KER6 protection line attributes a Ceit patentability plan to D1.8; D1.8 does not contain it

- Where: Section 7.2, KER6 row, D84:1095, "Ceit assesses the patentability of new developments of the corrosion-monitoring function before their disclosure (D1.8)".
- What is wrong: D1.8 has no Ceit-specific patentability statement. Its Ceit rows (Table 2) give "Selected scientific findings disclosed; detailed implementation controlled". Its Table 3 gives a general action for every owner: "Perform Result-specific patentability or registered-design assessment — Relevant Result owner — Before public disclosure or filing". Ceit's own summary names no protection decision, and the companion report says so (line 132, open point 1). The sentence states a Ceit commitment that no source records.
- Source: D1.8 :282, :284, :686; surewave/background/2026-09-30_ceit_exploitation_summary.md (no protection statement); companion :132, :167.
- Fix: "… made available through contract R&D and co-development agreements with industrial partners. The sensor design is published (Sensors 24(13) 4211, 2024). Ceit's input sets out no protection decision for the sensor or the SHMS; D1.8 asks each owner to assess patentability before disclosure or filing (Section 7.4)."

### 5. Minor. The CIRCWIND parenthetical suggests a different SINTEF entity from SUREWAVE's; CORDIS shows the same entity in both

- Where: Section 10, CIRCWIND row, D84:1153, "SINTEF (in CIRCWIND through SINTEF Manufacturing AS)".
- What is wrong: this was added on my round-2 finding 19, which assumed that the SUREWAVE beneficiary is SINTEF AS. CORDIS now lists the SUREWAVE coordinator as "SINTEF MANUFACTURING AS" (fetched 24 November 2026), the same entity as in CIRCWIND. The parenthetical now suggests a distinction that the public record does not support. The coordinator's legal name is already an owner question (D1rr). The CORDIS record also lists ACCIONA as "ACCIONA CONSTRUCCION IBERIA SA" in both projects.
- Source: CORDIS 101083342 XML (coordinator SINTEF MANUFACTURING AS; participant ACCIONA CONSTRUCCION IBERIA SA); scratchpad_t150\web\cordis_101147517.html (SINTEF MANUFACTURING AS; ACCIONA CONSTRUCCION IBERIA SA).
- Fix: partner cell "SINTEF". Settle the entity once, on the cover, when the owner question on the coordinator's legal name is answered. Add to that owner question that CORDIS also shows ACCIONA under a new legal name.

### 6. Minor. The CORDIS date for D7.6 is the project page's update date

- Where: Annex A.23, D84:1491, "The CORDIS results page of SUREWAVE lists D7.6 (last update 5 November 2026)".
- What is wrong: 5 November 2026 is the update date of the project record. The D7.6 entry (101083342_32_DELIVHORIZON) has sourceUpdateDate 10 November and contentUpdateDate 12 November 2026. CORDIS also lists two publications and the periodic report for period 1 as results.
- Source: CORDIS 101083342 XML, fetched 24 November 2026.
- Fix: "The CORDIS results page of SUREWAVE lists D7.6 (entry added 12 November 2026), two of the publications and the periodic report for the first period."

### 7. Minor. A.23 names a Zenodo deliverable report by its record title instead of its deliverable number

- Where: Annex A.23, D84:1489, "Twelve are deliverable reports: D2.1, …, D7.6, and Sunlit Sea's report 'SUREWAVE FPV System Design' (May 2024)".
- What is wrong: the record is by Guillaume Kegelart (Sunlit Sea), who wrote revision 1.1 of D3.4 (D3.4 version table), and D3.4 is Public in the GA's detailed deliverable entry. A reader cannot tell which deliverable the twelfth report is, and OpenAIRE, in the next bullet, lists D3.4.
- Source: GA :4962–4967; surewave/background/2024-03-19_surewave_d3.4_summary_global_system_design.md (cover, version 1.1 Kegelart); Zenodo snapshot :18, :39.
- Fix: "… D7.5 and D7.6, and D3.4, the summary of the global system design (registered as "SUREWAVE FPV System Design", May 2024)." If Sunlit Sea cannot confirm that the record is D3.4, keep the current text. Do not change the dissemination level.

### 8. Minor. "Before SUREWAVE" for the Stadt Towing Tank tests is not supported; the public record places them in MariSol

- Where: Section 6.1, D84:886, "Before SUREWAVE, Sunlit Sea had tested strings of its floats at the Stadt Towing Tank in Norway, outside the project"; Section 10, MariSol row, D84:1152.
- What is wrong: D5.1 says only that the tests "were not part of the SUREWAVE project". It gives no date. D3.1 (June 2023) already uses them, which is consistent with tests either shortly before or shortly after 1 October 2022. The Research Council of Norway's record of MariSol says that Stadt Towing Tank carried out wave-tank tests in MariSol, to understand how the panels behave in waves. So the tests were most likely MariSol's. Naming MariSol gives the reader the record behind them, and the MariSol row then shows the link in both directions.
- Source: surewave/background/2024-04-16_surewave_d5.1.md:620; surewave/background/2023-06-26_surewave_d3.1_design_internal_floating_pv_components.md:397; Prosjektbanken 317808 (scratchpad_t150\web\pb_317808.html: "Stadt Towing Tank har gjennomført bølgetankforsøk").
- Fix: 6.1: "In the national project MariSol, outside SUREWAVE, Sunlit Sea had tested strings of its floats at the Stadt Towing Tank in Norway (Research Council of Norway project record)." MariSol row, last column, add: "In return, Sunlit Sea's MariSol float tests at the Stadt Towing Tank gave MARIN the data to validate DIFFRAC (D5.1)." Keep D5.1's "outside SUREWAVE" wording elsewhere.

### 9. Minor. "Starts the planned GEOPON project if it is funded" contradicts SINTEF's plan, which calls it nationally funded

- Where: Section 14, 2027 row, D84:1256, "SINTEF … starts the planned GEOPON project if it is funded".
- What is wrong: SINTEF's plan calls it "a nationally funded project involving the industrial partner GEOPON" and "the nationally funded collaboration with GEOPON", and counts it among the reuses that "provide concrete evidence that the project Results are already contributing". "Planned" follows D14, as there is no public record. "If it is funded" adds a condition that SINTEF does not state, and SINTEF would object to it.
- Source: surewave/background/2026-10-02_sintef_exploitation_plan.md:11, :54, :70.
- Fix: "SINTEF continues in CIRCWIND and SFI BLUES and starts the planned national project with GEOPON".

### 10. Minor. Clement Germany's EUPI-PV action is made conditional on Sunlit Sea joining

- Where: Section 6.3 action plan, D84:955, "Breakwater for the nearshore demonstration in the EUPI-PV proposal coordinated by SINTEF, if Sunlit Sea joins it and it is funded".
- What is wrong: Clement Germany's part in that proposal does not depend on Sunlit Sea. Section 10 lists Clement Germany as "proposed for the breakwater" and Sunlit Sea as "possibly" a participant. The project facts say that the breakwater is funded through and supplied by Clement Germany.
- Source: D84:1158; docs/project_facts.md:42.
- Fix: "Breakwater for the nearshore demonstration in the EUPI-PV proposal coordinated by SINTEF, if Clement Germany takes part and the proposal is funded (added by the WP8 lead, Section 10)". Also, after 1 December the EUPI-PV rows in 4.6.2, 4.7, 4.9, 6.3, 6.4, 10, 12 and 14 must be updated: submitted or not, and with or without Sunlit Sea. The deadline falls before any submission date of D8.4 (rejection r1disp_E #29 holds; the update is certain).

### 11. Minor. "The first site with a breakwater class" overlooks the EIC Transition demonstrator, which has a light breakwater about 2029

- Where: Section 5, D84:850, "From the first site that needs one of the breakwater classes, the breakwater is part of KER1. That site is targeted about 2030 …"; Section 5 table, D84:862, and Section 9 heads of terms, D84:1132, "in place before the first site with a breakwater class (targeted about 2030)"; Section 12, D84:1184.
- What is wrong: if the EIC Transition project is funded, its demonstrator has a light breakwater over the exposed side, commissioned at about month 22 (4.6.2, 4.9, D84:806), that is in 2028–2029. That is a site with a breakwater class before 2030. The sentences mean the first commercial site, which 4.6.2 and 4.9 call it. As written, they also suggest that the agreement with Clement Germany is needed only by 2030, whereas the access requirements for the demonstrator arise in 2027 (D1.8 Table 3, finding 1).
- Fix: in all four places, "the first commercial site with a breakwater class (targeted about 2030)". Add to Section 5 after the first sentence on the breakwater: "In the EIC Transition demonstrator, if funded, the breakwater is built within that project and its grant and consortium agreements (Section 10)."

### 12. Minor. The Section 1 coverage table lists the two internal exploitation workshops as covered

- Where: Section 1 table, D84:61, "Definition of the definitive KERs, with two internal exploitation workshops | Grant Agreement, Subtask 8.2.2 | 3.1".
- What is wrong: Section 3.1 step 3 says that the project record "holds no separate record of the two workshops" and that the KERs were set through the written input round and the WP8 lead's screening and mapping. The table row reads as if the workshops are part of what Section 3.1 covers.
- Fix: "Definition of the definitive KERs (the Grant Agreement foresaw two internal exploitation workshops; Section 3.1 states how the KERs were set) | Grant Agreement, Subtask 8.2.2 | 3.1". The owner question on whether the workshops were held stands.

### 13. Minor. The EIC Transition row gives Clement Germany's work-package lead but not the others'

- Where: Section 10, EIC row, D84:1157.
- What is wrong: the proposal's work-package table gives SINTEF WP1, WP3 and WP4; Sunlit Sea WP2 (site characterisation and demonstrator engineering) and WP5 (manufacturing, instrumentation and factory acceptance); Clement Germany WP6; EDP WP7 (market validation, exploitation and investment readiness). D8.4 names only Clement Germany's lead. Below the table, Sunlit Sea's lead of the requirements task (Task 2.1) is given, which is a task within its WP2. The partners of the EIC consortium read D8.4, and an uneven list reads as a ranking.
- Source: generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md:322–340 (Table 3.3a), :369.
- Fix: partner cell: "SINTEF, coordinator (project management; integrated design verification; performance, durability and model validation); Sunlit Sea, technology owner and main exploitation partner (site characterisation and demonstrator engineering; manufacturing, instrumentation and factory acceptance); Clement Germany (breakwater and mooring; deployment, operation and validation campaign); EDP (EDP R&D / CNET, Portugal), end user and commercialisation partner (market validation, exploitation and investment readiness)". Below the table: "The requirements task, led by Sunlit Sea within its site-characterisation work package, also evaluates …".

### 14. Minor. The public-emergency licence duty is stated without the GA's condition

- Where: Section 13, four-year list, D84:1203, "comply with any additional exploitation obligations that the call conditions impose, … and, on request of the granting authority, grant non-exclusive licences in a public emergency".
- What is wrong: GA Annex 5 makes this duty conditional: "Where the call conditions impose additional exploitation obligations in case of a public emergency, the beneficiaries must (if requested by the granting authority) grant for a limited period of time specified in the request, non-exclusive licences — under fair and reasonable conditions …". As written, the duty reads as unconditional, and D8.4 treats the standards duty and the objection right as conditional (owner decision). The open-science section of Annex 5 has a parallel public-emergency deposit duty, also conditional and also for four years, which Section 13 does not list.
- Source: GA :8895–8906, :9295–9304.
- Fix: "comply with any additional exploitation obligations that the call conditions impose, including those linked to strategic assets, interests, autonomy or security, and, where the call conditions provide for it and the granting authority requests it, grant non-exclusive licences for a limited period, under fair and reasonable conditions, to entities that need the results to address a public emergency; where the call conditions provide for it, also deposit research outputs with open access in such an emergency;".

### 15. Minor. D6.4 and D7.2 are cited as evidence but are not in the project records the plan was checked against

- Where: Exec D84:17; 3.2 KER2 row; 3.4 R3; 4.1 D84:381 ("reported in ACCIONA's deliverable D6.4"); 6.2 D84:915 ("It is the subject of ACCIONA's public deliverable D6.4"); Annex B rows D6.4 and D7.2 (date "–").
- What is wrong: neither deliverable is in the repo, in the Zenodo community (snapshot :38 lists both as public deliverables not deposited), or on CORDIS (only D7.6 is listed). D7.2 exists: D7.6 cites it as "Panjwani, B. (2025): Report on technological qualitative assessment". Its figures in D8.4 come from Preprints 202611.1173 and D7.6, which is stated. For D6.4 no date or submission is recorded. D8.4 takes the figures from Preprints 202611.1592, which it states, but it presents D6.4 as an existing report. If D6.4 is not yet submitted when D8.4 goes to CINEA, the coordinator would have to correct the statement.
- Source: Zenodo snapshot :38; D7.6 :631, reference list ("Panjwani, B. (2025)"); CORDIS XML; 2026-09-28_status.md (D7.1, D7.2 missing locally).
- Fix: Annex B, D7.2 "2025 (cited in D7.6)". For D6.4, the coordinator checks the submission in the portal before D8.4 is submitted and enters the date in Annex B. If D6.4 is not yet submitted, write in 4.1 and 6.2 "The exposure is Task 6.5, led by ACCIONA; its results are reported in Preprints 202611.1592 (November 2026) and in ACCIONA's deliverable D6.4, due at the end of the project", and drop "public deliverable … is the subject of".

---

## Wording

### 16. Wording. "Coordination of the EUPI-PV proposal, if it is funded"

- Where: Section 6.4 action plan, D84:988.
- Fix: "coordination of the EUPI-PV project, if the proposal is funded".

### 17. Wording. The Horizon Results Platform duty is phrased three ways

- Where: Exec D84:34 ("goes on the Horizon Results Platform from then on"); Section 6 intro D84:878 ("is offered on the Horizon Results Platform"); Section 11 D84:1171 ("goes on the platform").
- What is wrong: Sections 6.8 and 13 use the GA's wording ("use the Horizon Results Platform to find interested parties"). The short forms suggest an automatic listing.
- Fix: in all three places, "its owner uses the Horizon Results Platform from then on to find interested parties, for the rest of the four-year period (Section 6.8)".

### 18. Wording. The Gijón prototype is written out again in the heavy-class row

- Where: Section 4.1.1 table, heavy row, D84:425, "a reduced-scale prototype designed and cast by ACCIONA, with SINTEF and Clement Germany as contributing beneficiaries (D4.3), deployed by ACCIONA at its demonstration site in the Port of Gijón for nine months (Task 6.5; D6.4; Preprints 202611.1592) and monitored by Ceit (Section 6.2)".
- What is wrong: D40 gives each piece of evidence one home. The Gijón record is in 6.2 and summarised in 4.1.
- Fix: "Designed by Clement Germany with CFD (D3.2) and tested in the SUREWAVE wave-basin campaigns; a reduced-scale prototype exposed at Gijón for nine months (Section 6.2)".

---

## Rejections in my area: does each hold?

| Rejection | Holds? | Comment |
|---|---|---|
| disp_A A#3; D1rr (cover "Coordinator: SINTEF", legal name an owner question) | Yes | CORDIS (24 November 2026) shows SINTEF MANUFACTURING AS as coordinator; the owner question stands. It also bears on the CIRCWIND parenthetical (finding 5) |
| disp_A A-gap11 (no extension footnote) | Yes | Cover now gives the two extensions in one phrase (D1r) |
| disp_A A-w12, A-w13 (companion outside the part) | Yes for the parts; the companion itself still needs the four fixes and the repo copy replaced (finding 3) |
| disp_D writing 25 (CIRCWIND entity) | Moot | The parenthetical added on my r2 #19 should go (finding 5) |
| disp_E ledger_E #5, #108, W21 (end 31 December 2026; windows 2027 and 2030) | Yes | |
| r1disp_D r1_coord #12, r1_cinea #F24 (Ceit and the hinge redesign) | Yes for the redesign inputs | D5.3 concerns the breakwater (D5.3 :1004). D1.8 does name Ceit's assessments among the hinge inputs, which matters for the ownership confirmation (finding 2), not for the redesign credit |
| r1disp_A / r1disp_E / r1disp_B final-report figures (D22) | Yes | No D8.4 line cites the final technical report |
| r1disp_A r1_owner #19 (0.4 transmission) | Overtaken | D3.2's summary states it (D3.2 :1705); 6.3 now cites "the summary of D3.2" correctly |
| r1disp_A r1_owner #15 (450 kN) | Overturned by D44 | D6.1 figure now used (D84:974) |
| r1disp_B F2 (D8.5 goal KPIs) | Overtaken | Rows added |
| r1disp_B F32, 22; r1disp_C r1_cinea #F32, r1_owner #22 (no edit of D8.3) | Yes | 4.1 lists the differences (D31) |
| r1disp_B 61 (annex) | Overtaken by D40 | Annex A created |
| r1disp_C r1_cinea #F32 (D7.4 v2.0 submission date) | Yes | Annex B gives 20 November 2026 as the version date |
| r1disp_D r1_writing #6 (EDP named) | Yes | EDP is an applicant; the proposal uses both "commercialisation partner" and "route to scale" |
| r1disp_E r1_cinea #21 (strategic assets under the four-year limit) | Yes | GA :8896–8899 |
| r1disp_E r1_cinea #30, r1_coord #29, r1_owner #26; r2disp_D r2_owner #22 (EUPI-PV and December workshop at submission) | Yes | The EUPI-PV deadline of 1 December falls before submission, so the update is certain (finding 10) |
| r1disp_E r1_cinea #10 d (IP workshops) | Yes | 2.4 states they are not in the record |
| r2disp_A r2_cinea #F2 (submission field, "late") | Yes | D1r |
| r2disp_E r2_cold #5 (Section 13 as text) | Yes | Finding 14 asks for the exact Annex 5 condition, which a compact table would lose |
| disp_C C#14, disp_D D#71, D gap 5, C-gap #6 (no factor 2–3; anchoring limitation) | Yes | D3 and D7; "factor 2–3" remains only in the old repo copy of the companion report (finding 3) |

Findings: 2 major, 13 minor, 3 wording.
