# D8.4 review, round 2: the coordinator (SINTEF), who submits D8.4 to CINEA

Scope: consistency of d84_merged.md (round-1 integrated draft) with the SUREWAVE deliverables in surewave/background and surewave/deliverables, the exploitable results report (companion version), the EIC Transition proposal and SINTEF's exploitation plan, plus statements the coordinator could not defend to CINEA or the partners. The final technical report working copy was not used as a source (D22). Decisions D1–D34 and the round-1 revisions were applied; errors inside them are reported as such.

"D84:n" is the line in scratchpad_t150\d84_merged.md. Repo paths are relative to C:\dev\src\sure-d61. CORDIS was fetched with curl (https://cordis.europa.eu/project/id/<id>?format=xml) on 23 November 2026.

All round-1 coordinator findings were checked in the new draft. Fixed: 1, 2, 3, 4, 5 (in part, see 6 below), 6, 7, 9 (option B), 10, 11, 13, 14, 15, 16, 17, 18 (wording), 19, 20, 21, 23, 24, 25, 26, 29 (owner question), 31 (companion), 32 (in part, see 9 below), 33, 34, 35 (owner question). Still open or reopened with new evidence: 8 (finding 4), 12 (finding 7), 22 (finding 14), 27 (finding 5), 30 (finding 15).

---

## Major

### 1. Major. The title block gives the project as 51 months "including a three-month extension"; the signed Grant Agreement has 36 months

- Where: title block, D84:5, "Project duration: 1 October 2022 to 31 December 2026 (51 months, including a three-month extension) · … Due in the Grant Agreement: month 36".
- What is wrong: this is an error inside decision D1. The signed Grant Agreement gives "Project end date: 30 September 2025" and "Project duration: 36 months", with periodic reports for M1–M18 and M19–M36. CORDIS today gives 1 October 2022 to 30 September 2026, 48 months. So the project was first extended by 12 months by amendment, then by three more months. "51 months, including a three-month extension" tells CINEA that the project was 48 months to begin with, and the project officer will know it was not. The due month has the same problem. In the signed Grant Agreement, month 36 is September 2025, so D8.4 looks 15 months late. The D8.3 metadata gives D8.3's due date (also month 36 in the signed Grant Agreement) as 30 September 2026, so the amendment appears to have moved the month-36 deliverables to month 48. Owner question 1 asks about the due date but assumes a single extension.
- Sources: surewave/background/2022-09-20_surewave_grant_agreement_101083342.md:328–330 and Data Sheet lines 3612–3613 ("Project duration: 36 months"), line in the Data Sheet "Project end date: 30 September 2025", lines 452–458 (periodic reports M1–18, M19–36), D8.4 deliverable entry line 5358 ff. (due month 36); CORDIS 101083342 XML (startDate 2022-10-01, endDate 2026-09-30, duration 48); surewave/deliverables/2026-09-28_surewave_d8.3_technical_brochure.meta.yaml (due_date 2026-09-30); surewave/background/2026-09-28_status.md:25–41 (amendment inferred, not in the repo).
- Fix (no footnote, as D1 asks): "Project duration: 1 October 2022 to 31 December 2026 (51 months: 36 months in the signed Grant Agreement, extended by amendment to 30 September 2026 and by a further three months) · Due date: [month 48, 30 September 2026, as amended / the amended due date]". The coordinator holds the amendment and can give the amended due month. Correct project_facts.md the same way ("Nominal duration 2022-10-01 to 2026-09-30" is the amended duration, not the signed one).

### 2. Major. Section 4.1 says D7.4 uses Clement Germany's 10 MWp layout; D7.4 says it replaced the panels and changed the layout

- Where: Section 4.1, D84:562, "Clement Germany compiled the material quantities of the plant for 10 MWp, about 18,600 panels of 537 Wp, and for a 2 MWp version with a ring 173 m across. The economic assessment D7.4 uses these layouts …"; D84:564, "This plan uses the 10 MWp layout of Clement Germany's material quantities and the economics of D7.4 version 2.0".
- What is wrong: this is an error inside decision D31. D7.4 states that it departs from the system description: "Panels are replaced due to the change of hinge systems. This affects the number of panels, the layout, the DC cable length, and the total power of the system." D7.4 uses panels of about 730 Wp. Its 10,375 kWp corresponds to about 14,200 panels of 730 Wp. Clement Germany's quantities give 18,624 panels of 537 Wp, which is 10.0 MWp. D7.4 is public, and a reviewer who checks it will find that the plant D8.4 calls Clement Germany's layout is not the one D7.4 costed. This also explains the 10.4 MWp that D32 asks D8.4 to state: the panel change gives it, not the Clement layout.
- Sources: surewave/background/2025-09-05_surewave_d7.4_economic_assessment.md:503–506 (exceptions to the system description), :576 and :1678 (730 Wp), :810 (10,375 kWp); surewave/background/2025-02-03_surewave_clement_materials_and_resources.md:28, :40 (537 Wp, 18,624 panels), :33 (346 m and 173 m rings).
- Fix (Section 4.1, D84:562): "Clement Germany compiled the material quantities for a 10 MWp plant, 18,624 panels of 537 Wp in the 346 m ring, and for a 2 MWp version with a ring 173 m across. The economic assessment D7.4 keeps these rings and breakwaters but uses panels of about 730 Wp, which changes the number of panels, the array layout and the installed power: its 10 MWp plant has 10.4 MWp installed (10,375 kWp), and its investment figures refer to that capacity." D84:564: "This plan uses the 10 MWp-class plant of Clement Germany's ring and of D7.4 version 2.0 (November 2026), the newest assessment of the plant." Also check the R1 row of Section 3.4 (D84:524, "a 10 MWp-class array (10.4 MWp installed in D7.4)"), which is correct as it stands.

### 3. Major. The Grant Agreement's two internal exploitation workshops for defining the definitive KERs are not mentioned

- Where: Section 3.1 (D84:449–466), the five steps by which the KERs were set; Section 2.4 table (D84:151).
- What is wrong: Task 8.2 of the Grant Agreement includes "Subtask 8.2.2 Internal Exploitation Workshops: As part of the exploitation strategy, two internal exploitation workshops will be conducted by all partners to accurately define the definitive Key Exploitable Results (KER)." D8.4 describes the KERs as set by a template, written summaries and screening by the WP8 lead, and says nothing about the workshops. CINEA checks the Grant Agreement method against the deliverable, and the coordinator will be asked whether the workshops took place. Owner question 29 covers the IP workshops and identification sheets of Annex 1 Section 2.2.3, which are a separate commitment, and rejection r1disp_E (r1_cinea #10 d) concerns those only.
- Sources: surewave/background/2022-09-20_surewave_grant_agreement_101083342.md:4478–4479; also the proposal, surewave/background/2022-02-23_surewave_proposal_sep_210808360.md:5042.
- Fix: if the workshops were held, add to Section 3.1 step 2 or 3: "The candidate KERs were discussed with all partners at the internal exploitation workshops of [date] and [date] (Grant Agreement, Subtask 8.2.2)". If they were not held, add after step 3: "The Grant Agreement foresaw two internal exploitation workshops with all partners to define the definitive KERs (Subtask 8.2.2). The definitive KERs were set instead from the partners' written input and checked against the deliverables, because [reason, e.g. the extension compressed the last months and the Booster sessions covered KER1]; the partners confirm the KER list in the review round of this plan." Add the item to owner questions (Sunlit Sea and the coordinator know whether they took place).

### 4. Major. The executive summary and Section 2.5 say the reach targets of the GA and D8.5 are reported "each with its status"; several are not in the table

- Where: executive summary, D84:36, "Section 2.5 also reports, each with its status, the reach targets of the Grant Agreement and of the dissemination plan D8.5"; Section 2.5, D84:168, "The Grant Agreement and the dissemination plan D8.5 also set reach targets … the second table gives the status of each."
- What is wrong: the reach table (D84:204–218) does not include the Grant Agreement's two internal communication trainings (Subtask 8.2.1; Annex 1 KPI "2 trainings"), nor six D8.5 goal KPIs: over 500 stakeholders reached through digital campaigns; bi-annual stakeholder forums and roundtables; a feedback loop with at least three industry partnerships; quarterly training sessions; published impact assessments; and a sustainability and replication guide. The rejection in r1disp_B F2 leaves adding these rows to the owner (owner question 15). That rejection holds as far as adding the rows goes. But until the owner answers, the word "each" is a claim to CINEA that the text does not meet.
- Sources: surewave/background/2022-06-24_surewave_annex1_part_b_v2.md:946–950; GA :4476–4477 (Subtask 8.2.1); surewave/background/2024-04-29_surewave_d8.5_dissemination_exploitation_communication_master_plan.md:248–290.
- Fix: either add the rows (statuses as in round-1 coordinator finding 8), or narrow both sentences now: executive summary "Section 2.5 also reports, each with its status, the quantified reach targets of the Grant Agreement and D8.5's targets for webinars and workshops, media mentions and new commercial agreements"; Section 2.5 "… the second table gives the status of each of these."

---

## Minor

### 5. Minor. The CORDIS list omits D7.6, which CORDIS lists as a project deliverable

- Where: Section 2.5.23, D84:436, "The public deliverables on CORDIS: D2.1, D2.4, D3.1, D3.3, D3.4, D4.3, D6.1, D6.2, D7.3, D7.5, D8.1, D8.2 and D8.5."
- What is wrong: the CORDIS record of SUREWAVE lists "Report on integrated sustainability assessment" (D7.6) as a project deliverable, content updated 12 November 2026. The list in D8.4 comes from OpenAIRE's harvest (KPI record :355), which is older. Section 7.2 calls D7.6 public, and the CORDIS list should match it.
- Source: CORDIS 101083342 XML, result id 101083342_32_DELIVHORIZON, contentUpdateDate 2026-11-12; surewave/background/2026-11-19_surewave_wp8_kpi_verification.md:355.
- Fix: "The public deliverables on CORDIS (checked 23 November 2026): D2.1, D2.4, D3.1, D3.3, D3.4, D4.3, D6.1, D6.2, D7.3, D7.5, D7.6, D8.1, D8.2 and D8.5." Recheck the full list on the CORDIS results tab on submission day.

### 6. Minor. D3.4 is Sensitive in the Grant Agreement, but D8.4 lists it as a public deliverable, and the Zenodo "floating PV system design report" is probably D3.4

- Where: Section 2.5.23, D84:434 ("the floating PV system design report" among the Zenodo deliverable reports) and D84:436 (D3.4 among "the public deliverables on CORDIS").
- What is wrong: the Grant Agreement's deliverable table gives D3.4 "Summary of global system design" as SEN. The Zenodo snapshot notes that record 10, "SUREWAVE FPV System Design" (Sunlit Sea, 31 May 2024), is most likely D3.4, and that its open publication should be confirmed with the coordinator. D8.4 states the publication as a fact and does not name the deliverable. A reader cannot tell which deliverable "the floating PV system design report" is. If it is D3.4, CINEA will see a Sensitive deliverable published openly, and D3.4 includes Clement Germany's breakwater design data (D3.2 is also SEN).
- Sources: surewave/background/2022-09-20_surewave_grant_agreement_101083342.md:4609 ("D3.4 Summary of global system design … SEN - Sensitive"); surewave/background/2026-11-19_surewave_zenodo_community_snapshot.md:18, :39.
- Fix: the coordinator confirms the dissemination level of D3.4 (amendment, or a change agreed with the partners). If D3.4 is public, write "D3.4 (summary of the global system design)" in place of "the floating PV system design report". If it is still Sensitive, remove it from both lists, and Sunlit Sea restricts the Zenodo record after Clement Germany's and the coordinator's review.

### 7. Minor. The hinge-inputs bullet in Section 3.1 misreports D5.3

- Where: Section 3.1, step 4, D84:459, "Ceit's structural integrity assessment (D5.3) concerns the breakwater; it identified the hinges as the most failure-prone part of the system and left their modelling to the hinge redesign."
- What is wrong: D5.3 says that "additional modelling of the mechanical behaviour of the new hinge solution will be done to support this process. This analysis will be included in the reporting of the new hinge concept". So D5.3 announced hinge modelling, not left it to others. The finite element analysis of the new connection that was reported is SINTEF's, in D6.3, which does not mention Ceit. The plan's choice (SINTEF and MARIN as the redesign inputs) holds. The rejections r1disp_D (r1_coord #12, r1_cinea #F24) hold for Section 5. But the 3.1 note now paraphrases D5.3 inaccurately, and Ceit would object to it.
- Sources: surewave/background/2024-11-07_surewave_d5.3_structural_integrity_assessment.md:1004; surewave/background/2025-02-12_surewave_d6.3.md:223–231, :841 (SINTEF's FEA of the new connection); D1.8 :85.
- Fix: "Hinge inputs: D1.8 names SINTEF, Ceit and MARIN as the partners whose assessments informed the hinge design. Ceit's structural integrity assessment (D5.3) concerns the breakwater; it identified the hinges as the most failure-prone part of the system and announced further modelling of the new hinge. The modelling of the new connection reported in the project is SINTEF's finite element analysis in D6.3. This plan names SINTEF's connection tests and analysis and MARIN's basin tests as the inputs to the redesign."

### 8. Minor. Section 4.1 lists four differences from D8.3 but misses three more that CINEA can compare

- Where: Section 4.1, D84:564.
- What is wrong: D8.3 also differs from the sources D8.4 uses on three points:
  - 50-year design waves. D8.3 gives 4.4, 7.0 and 12.3 m (from D2.1). D8.4 uses D5.1's design sea states, for example 6.5 m in the Mediterranean (D84:614).
  - Mooring optimisation. D8.3 says "up to 56 % chain-weight reduction". D8.4 gives 34–59 % and a 2–3 times heavier mooring at the Baltic site.
  - Breakwater wave transmission. D8.3 gives about 40 % transmission in the 1–3 s band. D8.4 Section 6.3 gives the same, so this one is consistent.

  Decision D31 asks D8.4 to say once how it differs from D8.3.
- Sources: surewave/deliverables/2026-09-28_surewave_d8.3_technical_brochure.md:65–67, :141; surewave/background/2023-01-31_surewave_d2.1_use_case_scenario.md:96; surewave/background/2024-04-16_surewave_d5.1.md, Table 5 (around :1060) and Table 9.
- Fix (append to D84:564): "D8.3 also gives the 50-year significant wave heights of the use-case basis D2.1 (4.4, 7.0 and 12.3 m), where this plan uses the design sea states of D5.1, and summarises the mooring optimisation as up to 56 % lighter chains, where this plan gives D5.1's figures per site, including the heavier mooring at the Baltic site (Section 6.5)."

### 9. Minor. The EIC Transition row describes EDP's role in other words than the proposal and omits the second candidate site

- Where: Section 10, EIC row, D84:1308, "EDP (EDP R&D / CNET, Portugal), end user and route to scale"; "Demonstrator of 50–300 kWp at an inland lake in Germany".
- What is wrong:
  - The proposal names EDP's role as "end user and commercialisation partner". "Route to scale" is not the proposal's term, and SINTEF wrote the proposal.
  - Task 2.1 of the proposal evaluates both the Hainer See baseline site and EDP's Alto Rabagão floating PV site. D8.4 gives only the German lake. The partner column also omits that Sunlit Sea leads Task 2.1 (requirements).
- Source: generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md:26, :369.
- Fix: "EDP (EDP R&D / CNET, Portugal), end user and commercialisation partner", and "Demonstrator of 50–300 kWp at a baseline site on an inland lake in Germany, reached through Clement Germany's relationship with the site owner …; Task 2.1 also evaluates EDP's floating PV site at Alto Rabagão (Portugal)." Alto Rabagão is an EDP site named in the proposal, and the proposal's partners read D8.4, so naming it matches the treatment of EDP (rejection r1disp_D, r1_writing #6). If the owner prefers no site names, write "and an EDP floating PV site in Portugal".

### 10. Minor. The letter-of-intent deadline is worded three ways; the letter says "before"

- Where: Section 10, D84:1308, "the letter lapses unless a collaboration agreement is signed by 28 February 2027"; Section 6.3, D84:1118, "lapses without one on 28 February 2027"; Section 14, D84:1403, "By 28 February".
- What is wrong: the letter says it "is automatically cancelled if no collaboration agreements are signed before [28th Feb 2027]". "By" and "on" both suggest that 28 February itself is in time.
- Source: generic/background/eic/2026-09-08_loi_leipzigseen_hainer_see.md:48.
- Fix: "unless a collaboration agreement is signed before 28 February 2027" in Section 10; in 6.3, "the site owner's letter of intent lapses if no agreement is signed before 28 February 2027"; in Section 14, "Before 28 February: …". This does not decide owner question 31 on whether to keep the clause.

### 11. Minor. SINTEF's action plan contains two rows that are not in SINTEF's input, and the EUPI-PV row discloses SINTEF's unsubmitted proposal

- Where: Section 6.4 action plan, D84:1153, "Coordination, modelling, design verification and validation in the EIC Transition project for the exposed-site version of KER1, and in the EUPI-PV nearshore demonstration, if each is funded (Section 10)"; Section 10, EUPI-PV row, D84:1309 (sites, capacities, start, installation window May–September 2029, breakwater supplier).
- What is wrong:
  - The Section 6 introduction says that each pathway "sets out what the partner reported in its own exploitation summary" and that added facts carry their source (D84:1042). SINTEF's plan names neither proposal. The EIC row can rest on the proposal (Section 10). The EUPI-PV row rests only on Sunlit Sea's notes (project_facts.md; funding/deliverables/eupi_pv/).
  - SINTEF coordinates the EUPI-PV application, due 1 December 2026, and the agency that runs that call reads D8.4. The coordinator would not want an unsubmitted proposal's sites, capacities and installation dates in another project's deliverable without its consortium's agreement.
- Sources: surewave/background/2026-10-02_sintef_exploitation_plan.md (no EIC or EUPI-PV); docs/project_facts.md:42, :93.
- Fix: in 6.4, mark the row as the WP8 lead's addition: "2027–2030 | (Added by the WP8 lead from the proposals, Section 10.) Coordination …". In Section 10, shorten the EUPI-PV row to the call, the requirement ("a demonstration of at least 5 MW over more than one sea zone"), SINTEF as coordinator and Sunlit Sea's possible role. Give the Swedish and German sites, capacities and the 2029 installation window only with SINTEF's consent, or after submission.

### 12. Minor. SINTEF's own work in SUREWAVE is listed without three of its lead roles

- Where: Section 6.4, D84:1131, "SINTEF's work in SUREWAVE. Besides coordinating the project, SINTEF led WP6 … It led the concrete-property modelling … (D5.2), the definition of the sustainability framework … (Task 7.1) and the technological risk assessment (D7.2)."
- What is wrong: the Grant Agreement also has SINTEF leading three tasks that D8.4 relies on elsewhere:
  - the use-case scenario definition (Task 2.1, D2.1), which set the three reference sites and their metocean basis used in D5.1, D7.4 and this plan;
  - the IPR management (Task 1.4, D1.4, D1.8), on which Sections 2.4 and 7.1 rest;
  - the synergy-building and clustering activities (Task 1.5), under which SINTEF presented at the CINEA clustering event that Section 2.5 counts four times.

  Section 2.5 credits Sunlit Sea's own share item by item (D15), and the coordinator will expect the same for SINTEF.
- Sources: surewave/background/2022-09-20_surewave_grant_agreement_101083342.md:3896, :3901, :3935, :4843 (D2.1 lead SINTEF), :4824 (D1.8 lead SINTEF).
- Fix: "SINTEF's work in SUREWAVE. Besides coordinating the project (WP1), with the IPR management plan D1.8 and the clustering with other EU projects, SINTEF defined the use-case scenarios and the three reference sites (D2.1) and led WP6 …".

### 13. Minor. Several Zenodo citations point to the version 1.0 records of D7.4, while D8.4 uses version 2.0

- Where: Section 2.5 own share (D84:220, "the D7.4 cost model"); 2.5.23 (D84:434, "the D7.4 cost model and financial analysis (Sunlit Sea, doi 10.5281/zenodo.17534609)" and D7.4 among the twelve deliverable reports); 3.5 (D84:542); 6.1 (D84:1054).
- What is wrong: the Zenodo records are the version 1.0 report (doi 10.5281/zenodo.22831172, 2025) and the version 1.0 cost model (doi 10.5281/zenodo.17534609, November 2025). D7.4 version 2.0 replaces the version 1.0 figures "including where those are quoted in other SUREWAVE deliverables". The coordinator's upload plan includes new versions of both Zenodo records. As written, D8.4 sends readers to the model with the errors that Section 4.6 lists.
- Sources: surewave/background/2026-11-19_surewave_zenodo_community_snapshot.md:13, :25; surewave/background/2025-09-05_surewave_d7.4_economic_assessment.md:500; surewave/deliverables/2026-11-22_followup_panjwani_d7.4_revision.md ("New versions of the two D7.4 Zenodo records").
- Fix: when the new versions are uploaded, cite their DOIs, or the concept DOIs, which resolve to the latest version. Until then, in 2.5.23 add "(version 1.0; the version 2.0 report and cost model are added as new versions of these records)".

### 14. Minor. The website reach row understates 2024 visits

- Where: reach table, D84:214, "more than 12,000 in 2024, within the more than 50,000 recorded by the end of that year"; Section 2.5.22.
- What is wrong: the site had about 800 visits in total by March 2024 and more than 50,000 by the end of 2024. So 2024 alone had more than 49,000. "More than 12,000" is true but understates the record by a factor of four (requirement 4).
- Source: Section 2.5.22 of D8.4 itself; KPI record (website line).
- Fix: "More than 49,000 in 2024 (more than 50,000 recorded from late August 2023 to the end of 2024, of which about 800 by March 2024); 2025 and 2026 not measured after tracking stopped | Met in 2024; not measured for the other years". Owner question 10 on the campaign still applies.

### 15. Minor. The June 2022 DNV "Statement of Conformity" for Generation 1 is still not supported

- Where: Section 8, KER1 row, D84:1271, "In June 2022 DNV issued a Statement of Conformity verifying that Sunlit Sea's design basis, a general design methodology developed for Generation 1, complies with DNV-RP-0584."
- What is wrong: round-1 coordinator finding 30 is not in the rejected list and not fixed. The repo sources give only "DNV RP-0584 verifisering fra 2022" and a 2022 DNV press release on design-basis verification. The month and the document type are not in them. CINEA can ask for the statement.
- Sources: generic/background/2026-07-08_market_intel.md:104, :138; surewave/background/2026-11-14_hrb_business_plan_research/technology_standards_ip.md:32.
- Fix: "In 2022 DNV verified Sunlit Sea's design basis for Generation 1, a general design methodology, against DNV-RP-0584 (DNV news release, 2022)." Restore "June" and "Statement of Conformity" only if Sunlit Sea holds the document; then add it to the owner questions.

### 16. Minor. The 40 % wave transmission is cited to D3.2, which round 1 found holds it only in figures

- Where: Section 6.3, D84:1102, "In Clement's CFD study of the cross-section variants (FLOW-3D Hydro, D3.2), the selected breakwater lets through at most about 40 % of the incident wave height at the wave periods of 1–3 s that are critical for the array."
- What is wrong: rejection r1disp_A (r1_owner #19) found the 0.4 transmission in D3.2's figures and the webinar summary, not in D3.2's text (owner question 21). The figure is now in D8.4 with D3.2 as its only source. Clement Germany's own review of D8.3 (18 November 2026) states it in writing: "The transmission coefficient is about 40 % in that range, so the wave attenuation is about 60 %." The rejection was right that D3.2's text alone does not carry the figure. With Clement's statement the figure holds, and it should be cited.
- Sources: surewave/background/2026-11-18_clement_d8.3_brochure_review_comments.md, comment 5; surewave/background/2023-08-08_surewave_d3.2_floating_breakwater_design.md (figures).
- Fix: "… lets through about 40 % of the incident wave height at the wave periods of 1–3 s that are critical for the array (D3.2, figures; confirmed by Clement Germany in its review of D8.3, November 2026)." This closes owner question 21.

### 17. Minor. "Expected about 2030" for the first breakwater-class site does not match the plan's own model

- Where: executive summary, D84:25, "The first commercial site with a breakwater class is expected about 2030"; Section 3.2 KER3 row (D84:486, "first commercial site about 2030"); Section 15 (D84:1414, "The breakwater classes follow from about 2030").
- What is wrong: Section 4.6.2 and Section 4.9 say the EIC proposal targets it "immediately after completion … about 2030" and the financial plan models it in 2031. "Expected" states Sunlit Sea's own expectation, but the plan models 2031.
- Fix: executive summary "The first commercial site with a breakwater class is targeted about 2030 in the EIC Transition proposal and modelled in 2031 in the financial plan"; KER3 row "first commercial site targeted about 2030"; Section 15 "The breakwater classes follow from about 2030–2031".

### 18. Minor. GA scientific-impact targets for a PhD and four R&D lines are not reported

- Where: Section 3.5 (non-commercial pathways) and Section 4.10 (changes from the proposal).
- What is wrong: the proposal's impact canvas, part of the Grant Agreement, sets "10 peer-reviewed publications with more than 140 citations, and 1 new PhD. 4 new R&D lines on: Coupled aero & Hydrodynamic simulation; Structural Health Management; Concrete circular mixes; Material properties modelling." D8.4 reports the publications and citations but not the PhD or the R&D lines. A reviewer comparing the impact canvas with the final plan will ask. The four R&D lines exist in the KERs: KER4/KER5, KER6, KER2 and Surewave-ANN.
- Source: surewave/background/2022-09-20_surewave_grant_agreement_101083342.md, impact canvas (around :7700, "SCIENTIFIC IMPACT").
- Fix (3.5, Scientific bullet): "The four research lines named in the proposal continue in the partners' KERs: coupled aero- and hydrodynamic simulation (KER4, KER5), structural health management (KER6), circular concrete mixes (KER2) and material-property modelling (Surewave-ANN, KER4). [The proposal's target of one new PhD: state the thesis (for example Ceit's PhD work on corrosion monitoring, shown at DCIS 2023) or 'no PhD thesis was completed within the project'.]" Add to owner questions for Ceit and SINTEF.

### 19. Minor. CIRCWIND's SINTEF participant is SINTEF Manufacturing AS, not the SUREWAVE beneficiary SINTEF AS

- Where: Section 10, CIRCWIND row, D84:1304, partner "SINTEF"; executive summary D84:38; Section 6.4.
- What is wrong: CORDIS lists SINTEF Manufacturing AS as CIRCWIND's SINTEF participant. Results of SINTEF AS reused by another legal entity fall under the Grant Agreement's rules for affiliated entities and the Consortium Agreement. The coordinator would want the entity named correctly where Section 10 says its periods and data come from CORDIS. The rejection disp_D writing 25 relies on D1, but D1 concerns the coordinator's name, not CIRCWIND. That rejection holds for the SUREWAVE coordinator. It does not settle this row.
- Source: CORDIS 101147517 XML (participants: … SINTEF MANUFACTURING AS …; ACCIONA CONSTRUCCION IBERIA SA is also a partner).
- Fix: Section 10 partner cell "SINTEF (in CIRCWIND through SINTEF Manufacturing AS)". No change in the executive summary.

### 20. Minor. The source of the TRL 5 in Section 4.1 is described as D7.6's own risk assessment; it builds on SINTEF's D7.2

- Where: Section 4.1, D84:568, "It rests on D7.6's technical risk assessment of the system with the redesigned hinge".
- What is wrong: the TRL 5 statement sits in D7.6's technological-sustainability section, which integrates the technological risk assessment of SINTEF (D7.2, Task 7.2, a survey of the consortium experts). D7.6 also states elsewhere that its scenarios "go beyond the TRL 5 pursued with the technical work done within the project". The coordinator would want its D7.2 credited for the rating that D8.4 uses throughout.
- Sources: surewave/background/2025-11-05_surewave_d7.6_integrated_sustainability_report.md:391, :643, :759.
- Fix: "It rests on the technological risk assessment in D7.6, which builds on SINTEF's assessment D7.2 and rates the system with the redesigned hinge after the two 1:10-scale wave-basin campaigns of the integrated system at MARIN and the component tests."

### 21. Minor. The exploitable results report (companion) still differs from D8.4 in four places, and the repo copy is the old version

- What is wrong:
  - Companion line 66: "the WP8 lead grouped them into seven KERs, one anchored in each beneficiary's main contribution". D8.4 says the WP8 lead proposed the seven candidates first and mapped the results to them (D84:452, :462). Line 19 of the same report says the template listed the seven candidates.
  - Companion line 11: distribution "without written consent from the coordinator and from each contributing partner". D8.4's notice (D84:11): "the written consent of the beneficiaries whose information it contains". The two documents set different consent rules for the same SEN material.
  - Companion line 76: SINTEF ER3 and ER4 (concrete cracking and Surewave-ANN) are listed as modelling that reaches KER1. D8.4 Section 5 has no such role (SINTEF's KER1 role there is testing and qualification).
  - Companion line 171: "the SINTEF-to-Sunlit Sea hinge transfer" can be read as a transfer of results under Article 16. It is a technical input. Write "SINTEF's test input to Sunlit Sea's hinge redesign".
  - The repo copy surewave/deliverables/2026-09-30_surewave_exploitable_results_report.md is still the old text: lines 19 ("between 4 and 30 September 2026"), 56 and 154 ("Marisol", "planning platform"), 118 (factor 2–3), 159 ("Mikroflexishape"), 179 ("revision 3"). It must be replaced by the companion before anything goes to CINEA.
- Sources: scratchpad_t150\companions\2026-09-30_surewave_exploitable_results_report.md:11, :19, :66, :76, :171; repo copy lines as given.
- Fix: companion line 66 "The WP8 lead proposed seven candidate KERs, one anchored in each beneficiary, and mapped the reported results to them; no partner proposed a KER of its own." Line 11: use D8.4's wording. Line 76: "modelling (MARIN ER1, ER2, SINTEF ER1, ER2)". Line 171: as above.

---

## Wording

### 22. Wording. The dissemination-notice rule in Section 13 drops "unless agreed otherwise"

- Where: Section 13, D84:1364, "give the other beneficiaries at least 15 days' notice before disseminating results; another beneficiary may object within 15 days if its legitimate interests would be significantly harmed".
- Source: GA Annex 5 :9193–9201 ("at least 15 days advance notice … (unless agreed otherwise)"; "may object within (unless agreed otherwise) 15 days").
- Fix: "give the other beneficiaries at least 15 days' notice before disseminating results, unless agreed otherwise; another beneficiary may object within 15 days, unless agreed otherwise, if its legitimate interests in the results or background would be significantly harmed".

### 23. Wording. The open-sea investment is €9.75M in 4.10 and €9.8M in 4.6.1

- Where: Section 4.10, CAPEX row, D84:1005, "about €9.75M"; Section 4.6.1, D84:850, "About €9.8M".
- Fix: use "about €9.8M (€9.75M)" once in 4.6.1 and "about €9.8M" in 4.10, or the reverse. D32 uses €9.8M.

### 24. Wording. "Hinge decision point" and access-rights timing appear with slightly different conditions

- Where: Section 4.5 milestones (D84:799, "written requests … (Q1 2027, before the design freeze)"); Section 5 (D84:1017, "before the design freeze and the first reference plant"); Section 9 (D84:1283, same); Section 12 (D84:1331, "before the design freeze").
- Fix: use one form everywhere: "in writing in Q1 2027, before the design freeze (D23)". The first reference plant (Q3 2027) follows the freeze anyway.

---

## Rejections in my area: does each hold?

| Rejection | Holds? | Comment |
|---|---|---|
| disp_A A#3 (coordinator "SINTEF AS") | Yes | GA Data Sheet names SINTEF AS as coordinator |
| disp_A A-gap11 (no extension history or footnote) | In part | No footnote is needed, but "51 months, including a three-month extension" is wrong against the signed GA (36 months) and CORDIS (48 months); one corrected phrase in the title block is enough (finding 1) |
| disp_A A-w12, A-w13 (ERR outside the part) | Yes | The companion is revised; the repo copy must still be replaced (finding 21) |
| disp_E ledger_E #5, #108, W21 (end 31 December 2026; windows to 2027 and 2030) | Yes | The dates follow from the extended end date; finding 1 concerns the duration and due month only |
| disp_D writing 25 (CIRCWIND entity) | For the coordinator, yes; for CIRCWIND, no | D1 concerns SUREWAVE's coordinator; CORDIS shows SINTEF Manufacturing AS in CIRCWIND (finding 19) |
| r1disp_D r1_coord #12, r1_cinea #F24 (Ceit and the hinge) | Yes for Section 5 | The 3.1 note now exists, but its paraphrase of D5.3 is inaccurate (finding 7) |
| r1disp_A r1_partners #S1, #S3, #S4, #E3, #A5; r1disp_E #A5, #C2, #S2, #S4, #M3; r1disp_B 6, 36, F5 (final technical report figures) | Yes | D22; no D8.4 line cites the final technical report (checked: zero occurrences) |
| r1disp_A r1_owner #19 (0.4 transmission not in D3.2 text) | The premise holds; the outcome changed | D8.4 6.3 now gives the figure with D3.2 as its only source; Clement's written review of D8.3 supports it and should be cited (finding 16) |
| r1disp_A r1_owner #4; r1disp_B 4 (infographics 5 of 6) | Yes | D10r; counting rule stated |
| r1disp_A r1_owner #15 (450 kN) | Yes | Not in D6.1 |
| r1disp_B F2 (D8.5 goal KPIs and GA trainings left to the owner) | Yes for the rows | The claim "each with its status" must be narrowed until the rows are added (finding 4) |
| r1disp_B F32, 22; r1disp_C r1_cinea #F32, r1_owner #22 (no edit of D8.3) | Yes | D31; but 4.1 should name the further differences (finding 8) |
| r1disp_B 9 (option B for the Spanish articles) | Yes | The rule and its reason are stated in 2.5.12 |
| r1disp_B 21, 23, 24 | Yes | Owner decisions and D10/D10r |
| r1disp_B 61 (annex) | Yes | Section numbers kept |
| r1disp_C r1_cinea #F32 (D7.4 v2.0 submission date unknown) | Yes | Owner question 39; the coordinator holds the upload plan. Related: the Zenodo records are still v1.0 (finding 13) |
| r1disp_C r1_cold #3 (basin campaigns tested the full ring) | Yes | Energies 17(9) 2059 and 19(7) 1609 support the wording |
| r1disp_D r1_writing #6 (EDP not anonymised) | Yes | EDP is an applicant in the EIC consortium; finding 9 asks for the proposal's own role wording |
| r1disp_E r1_cinea #21 (strategic assets under the four-year limit) | Yes | GA Annex 5 :8896–8899 |
| r1disp_E r1_cinea #30, r1_coord #29, r1_owner #26 (EUPI-PV and December workshop updated at submission) | Yes | The 1 December deadline falls before any submission, so the update is certain to be needed; see finding 11 on the EUPI-PV row's content |
| r1disp_E r1_cinea #10 d (IP workshops) | Yes for the IP workshops | The GA's two internal exploitation workshops (Subtask 8.2.2) are a separate, unaddressed commitment (finding 3) |
| disp_C C#14, disp_D D#71, D gap 5, disp_C C-gap #6 (no factor 2–3; anchoring limitation per D7) | Yes | D3 and D7 |
| disp_D writing 22, 24 | Yes | Checked in the draft |
| disp_B B#78, B#88 | Yes | D16 applied; no BayWa |

Findings: 4 major, 17 minor, 3 wording.
