# D8.4 round-2 integration and restructure log (24 November 2026)

Input: d84_merged.md (the joined r2part1–8), backed up first as d84_merged.pre_restructure.md. Script: r2int_edit.py (exact one-occurrence replacements, then the Annex A move and the Annex B insert); Annex B source table: annexB.md. A follow-up edit moved the Zenodo definition to its first use. Nothing in C:\dev\src\sure-d61 was edited; no git. CRLF kept.

## Word counts

- Before: 46645 words in total.
- After: body (title block to Section 15) 40767 words; Annexes A and B 5922 words (Annex A 5220, Annex B 702); total 46731 words.

## 1. CROSS-PART items (r2disp_A–E)

Already in the merged draft (applied by the part fixers in their own sections; verified here, no change): A1 (executive summary), A2, A6, A7, A8, A9, A10, A12; B2; C2, C3, C5; D1, D3, D4 (executive summary, 3.2, 4.1, 5, 10, 15), D5, D8, D9, D10, D11; E1, E2 (CFD, ERA5/GEBCO, ABS, IFE), E10, E11, E12, E13, E14, E15, E16.

Applied in this pass:
- A1: 2.5 intro "the second table gives the status of each" → "the second table lists them with their status"; D8.5 row reads "Met for partnerships; no commercial agreement yet".
- A3 / C4 / E7: Gijón wording in the 4.1.1 heavy row and the 4.10 status cell (designed and cast by ACCIONA with SINTEF and Clement Germany as contributing beneficiaries, deployed by ACCIONA, Task 6.5, D6.4, monitored by Ceit).
- A4 / C9 / E5: Stadt Towing Tank wording per D35, with the full statement in its single home, 6.5 (section 2).
- A5: 6.2 biofouling and LWAC wording verified; "(D4.2, Table 5)" added to the chloride coefficients.
- A11: Section 15 verified (breakwater classes, equity).
- B1: Section 11 "the public deliverables on CORDIS (Section 2.5.23)" → "the public deliverables in the EU project records (CORDIS and OpenAIRE, the European open-science infrastructure) (Annex A.23)".
- B3: 3.5 scientific bullet ends "(Section 2.5, second table)"; its record pointer is now "(Annex A.23)".
- B4: done as the D40 restructure; reach-table references to 2.5.10, 2.5.12, 2.5.22 and 2.5.23 replaced.
- B5: no "submitted on 18 November" outside the dissemination record (grep).
- C1: 4.8 hinge row keeps the attribution (D7.2, summarised in D7.6); the figures are in 4.1 (D40).
- C6: 4.6 drops the repeated definitions of NPV, IRR and LCOE (defined in the executive summary).
- C7 / D12: "(Section 4.4)" pointers to the reference-plant table in 4.7 (second paragraph), 4.9 (2029) and Section 14 (2029).
- C8: 7.2 describes Generation 1 as "the square aluminium float joined by polyurethane hinges (Section 4.1)".
- C10: unit weight "about 123 t, slightly above the upper weight of about 120 t that D3.2 set for handling with mobile cranes" in 3.4 R2 and 6.3, as in 4.1.1.
- C11 / D2: 4.6.2, first use of EUPI-PV: the call "Improved system design for innovative PV applications" (HORIZON-CL5-2026-11-D3-14) of the co-programmed European Partnership for Innovation in Photovoltaics (EUPI-PV).
- D4: 4.4.1 "from about 2030" → "from the first site that needs one, targeted about 2030"; Sections 9 and 12 "(about 2030)" → "(targeted about 2030)".
- D6: Sections 13 and 14 access-rights wording "in writing ... before the design freeze".
- D7 / E6: 3.1 mooring bullet names the three forms (MARIN's chain-mass ratio, D5.1 in per cent, D8.3's summary figure) and points to 6.5, where the per-site figures and the 2.3–2.4 ratio stay (D40). "A larger reduction" not used.
- E3: "digital image correlation (DIC)" at first use (3.1 table), then "DIC" in 3.2, the 3.4 note and Section 10.
- E4: 3.2 KER3 relation cell adds "integrating them in KER1 transfers no ownership (D1.8; Section 7.1)".
- E8 / E9: the connection-test and 0.17 mm figures stay in their homes (6.4, 6.6); the 3.2 cells point there (D40 wins over the cell texts proposed in E8 and E9).

## 2. Restructure (D40)

Annex A. Sections 2.5.1–2.5.23 moved unchanged to "Annex A. Dissemination and communication record" as A.1–A.23, after Section 15 and before the EU funding statement, with a two-sentence introduction. All items and tables kept. Internal references updated (2.5.1, 2.5.2, 2.5.3, 2.5.7, 2.5.9, 2.5.13, 2.5.14 → Annex A.n; "(Section 2.5.24)" → "(Section 2.5)"); A.2 "technology risk assessment" → "technological risk assessment". Section 2.5 keeps the intro, the KPI table with status, the counting paragraph and multi-count list, the "Three targets" paragraph, the Evidence paragraph, the reach-target table, the Sunlit Sea credit paragraph and "How the reach serves exploitation" (former 2.5.24, now a lead-in paragraph like "Counting."). The 2.5 intro points to Annex A; Section 1 (text and map) points to Annexes A and B. Main-text references to 2.5.x replaced by Annex A.x (reach table, own-share paragraph, 3.5, 6.1, 11, 13). Definitions that lived only in the moved text were added at first main-text use: Zenodo (reach table), BRIDGE (own share), MARINE, LCA and BAMBOO (2.5 exploitation paragraph); Crossref introduced in the reach table; CORDIS (4.3) and OpenAIRE (Section 11) defined.

One home per evidence item. Each removed figure was checked present in its home; sources stay cited at each pointer.
- TRL: home 4.1. 3.2 KER1 cell and 3.4 R1 maturity → "Integrated system and CONNECT platform TRL 4–5 (Section 4.1)"; Section 15 shortened to one sentence with pointer. The executive summary keeps its summary.
- Hinge tests and loads: home 4.1. 3.2 KER4 (3.69 kN, D6.3 fatigue), 4.4 Lean Canvas (37/14 kN), 4.8 hinge row (40/37 kN) and 6.4 (3.69 kN, D6.3 fatigue, cracks) → pointers. D6.3's "rough estimate that does not cover mixed-mode loading" moved from 6.4 into 4.1.
- Connection tests (D6.1) and shell–core beam tests (D4.2): home 6.4. 3.2 KER3 and KER4 cells and 6.2 → pointers.
- Breakwater wave transmission (about 40 %, D3.2): home 6.3. 3.2 KER3, 3.4 R2 and 4.1.1 → pointers.
- Mooring reductions: home 6.5. 3.1 bullet, 3.2 KER5, 3.4 R6 and 4.10 → pointers (the 4.10 cell keeps the direction of change per site for the comparison with the proposal's −40 % target).
- Stadt Towing Tank: home 6.5, now the full statement from D5.1 (l.620–652, l.1748): tests of 1×3, 1×6 and 1×9 arrays outside SUREWAVE, results made available by Sunlit Sea, DIFFRAC computed for the 1×3 and 1×6 arrays, motions generally similar, good agreement in the conclusions, hinge loads not measured, nonlinear hinges. 3.1 conflict bullet, 3.2 KER5, 3.4 R1, 4.1 (D8.3 list and uncertainty bullet) and 6.1 → short form with pointer; 6.1 keeps Sunlit Sea's D3.1 load estimate.
- Gijón exposure results (materials): home 6.2. 3.2 KER2 and 3.4 R3 → pointers; the 3.4 R3 trial-mix list and prototype dimensions → pointer to 6.2.
- Sensor results: home 6.6. 3.2 KER6 and 3.4 R10 → pointers; the second ABS expansion (6.6) dropped.
- D7.4 economics: home 4.6 (site table, changes from version 1.0, breakwater share) and 4.6.1 (investment €9.75M, ACCIONA-mix variants). 4.6.1 revenue row → table of 4.6; 4.6.1 breakwater share → 4.6; 4.10 LCOE row → Mediterranean value with pointer; 4.10 CAPEX row keeps €940/kWp for the comparison with the proposal's targets and drops €9.75M; 3.4 R3 HPC LCOE → 4.6.1; installed-power repeats in 3.4 R1 and 4.10 → 4.1. Executive summary and Section 15 keep their summary figures and gain "(Section 4.6)".

Annex B. "Annex B. SUREWAVE deliverables cited": all 36 deliverables cited (D1.4, D1.7, D1.8, D2.1–D2.4, D3.1–D3.4, D4.1–D4.3, D5.1–D5.7, D6.1–D6.4, D7.1–D7.6, D8.1–D8.5), with title, lead beneficiary and dissemination level from the deliverable descriptions of the Grant Agreement (surewave GA l.4716–5340), and the version or date this plan uses where its text states one; a note gives the amended due date of D1.8, D8.3 and D8.4 (month 48, decision D1rr). D3.4 is PU in its deliverable description; the SEN on the D3.4 line of the summary table (l.4609) is a row shift of the text extraction and belongs to D4.1 (owner question 47 marked answered).

Checks (script): every "Section x.y", "Sections x and y" and "Annex A.n" resolves to an existing heading; no table row has a different column count; no blank line after a separator row; no "**".

## 3. Consistency pass

Checked against D1–D45 and the round-1 and round-2 revisions. Grep for bold, "therefore", "thus", "which is why", "it follows", "precisely", "crucially", "clearly", "already" (one non-emphatic use, 4.7 "already installed"), "well beyond", "milder", "factor 2", "first breakwater site", "Lithuania", "China", "Skien", file paths, task numbers, "submitted on 18 November", "No request", "consortium plans/will", and "agreed/approved/confirmed/decided" (remaining uses are Grant Agreement rules, plan conditions or "to be confirmed"). First uses checked for LCA, CFD, DIC, HPC, LWAC, CLC, EPS, SHMS, ABS, ERA5, GEBCO, ILCSA, EUPI-PV, CORDIS, OpenAIRE, Zenodo, BAMBOO, SAB, DOI, CAPEX, OPEX, NPV, IRR, EERA, EU PVSEC, ISNRE, IFE, BRIDGE, Crossref, R&D, UV, SCADA. The 2.5 D8.5-agreements row and the closing sentence of Section 10 match (D42). No confidential prices, costs per watt, customers or site names were added; the €0.10/kWh and the 2030–2031 revenue stay as owner questions (Q36, Q60).

## 4. Companions (companions\)

- 2026-11-22_surewave_d8.4_ker1_financial_section.md: body replaced by D8.4 Section 4.7 verbatim. It still carried the round-1 text (a 1 MWp EIC plant, the old scenario definitions, revenue and EBITDA columns per scenario). internal_title date → 24 November 2026. Backup *.pre_r2int.md.
- 2026-09-30_surewave_exploitable_results_report.md: aligned with Section 3: KER1 TRL attributed to SINTEF's D7.2, summarised in D7.6, with the no-ownership-transfer and design-version sentences; KER2 LWAC sources (D4.1 Sample 18, D4.2, D8.3) and the CEM III wording, prototype credit (ACCIONA with SINTEF and Clement Germany; Task 6.5; D6.4); DIC; KER5 Stadt validation and the chain-mass-ratio wording in place of "a larger reduction"; KER6 0.17 mm laboratory result; KER7 D7.2, D7.3, D7.5, Task 7.1 and D7.1; open point 5 and the sources list. LF kept. Backup *.pre_r2int.md.
- 2026-11-19_surewave_wp8_kpi_verification.md: LinkedIn posts "at least 34" (row 7 and the §7 heading); ACCIONA interview published on LinkedIn (row 15); D8.3 "issued 18 Nov 2026" (row 18); "§2.5.3" → "Annex A.3"; the further-targets sentence names the PhD, R&D lines, trainings, D8.5 goal-level targets and the partnership KPI met with SuRE and CIRCWIND, with a pointer to Annex A. CRLF kept. Backup *.pre_r2int.md.
- Not changed: Booster business plan, full financial plan, project_facts (nothing they state was changed by this pass).

## 5. Owner questions

owner_questions.md rewritten (backup owner_questions.pre_r2int.md). Q1–Q41 kept and updated to the current text and Annex numbering; round-2 duplicates merged into them (Q1, Q4, Q8, Q10–Q13, Q16, Q20, Q26, Q28, Q29, Q33, Q36, Q39). Answered or partly answered from sources: Q1 (due date, D1rr), Q11 (public post count), Q14, Q15 (reach rows added in round 2), Q16 (open-access locations), Q21 (D3.2 summary, D44), Q22 (D5.2 in the Grant Agreement), Q40 (Annex B), Q47 (D3.4 level, Grant Agreement deliverable description). New: Q42–Q67.

## 6. Edit list (r2int_edit.py, in order)

- S1: pointer to Annex A
- S1: pointer to Annex B
- S1 map: 2.5, Annex A
- 2.5 intro: drop 'status of each' (A1)
- 2.5 intro: pointer to Annex A (D40)
- 2.5 reach: Crossref introduced
- 2.5 reach: ref A.23
- 2.5 reach: ref A.12
- 2.5 reach: ref A.22
- 2.5 reach: SuRE ref to Section 10
- 2.5 own share: ref A.10
- 2.5 own share: BRIDGE defined (first main-text use)
- 2.5 own share: Zenodo defined, ref A.23
- 2.5.24 kept in 2.5 as a paragraph
- 2.5 reach-exploitation: MARINE defined
- 2.5: LCA defined at first main-text use
- 2.5: BAMBOO defined at first main-text use
- 3.1 mooring bullet: figures moved to their home in 6.5 (D40)
- 3.1 Stadt bullet: details moved to 6.5 (D35, D40)
- 3.1 table: DIC defined at first use (E3)
- 3.2 KER1: TRL pointer to 4.1 (D40)
- 3.2 KER2: results moved to home 6.2 (D40)
- 3.2 KER3: transmission, mooring, connection figures to homes 6.3/6.5/6.4 (D40)
- 3.2 KER3 relation: no ownership transfer (E4)
- 3.2 KER4: DIC
- 3.2 KER4: test figures to homes 4.1/6.4 (D40)
- 3.2 KER5: load, mooring and Stadt figures to home 6.5 (D40)
- 3.2 KER6: sensor results to home 6.6 (D40)
- 3.4 R1: installed power pointer
- 3.4 R1: TRL pointer
- 3.4 R1: Stadt pointer to 6.5
- 3.4 R2: unit weight wording as 4.1.1 (C10)
- 3.4 R2: transmission pointer to 6.3
- 3.4 R3: trial mixes pointer to 6.2
- 3.4 R3: prototype size in 6.2
- 3.4 R3: evidence to homes 6.2/4.6.1
- 3.4 R6: mooring pointer to 6.5; proof load defined here
- 3.4 R10: pointer to 6.6
- 3.4 note: DIC
- 3.5: pointer to reach table (B3)
- 3.5: ref A.23
- 4.1 D8.3 list: Stadt pointer to 6.5
- 4.1: D6.3 qualifier moved here from 6.4
- 4.1 uncertainty: Stadt pointer
- 4.1.1: transmission pointer to 6.3
- 4.1.1 heavy row: Gijón wording (A3)
- 4.3: CORDIS defined at first use
- 4.4 Lean Canvas: hinge pointer to 4.1
- 4.4.1: 'targeted about 2030' (D4 cross-part)
- 4.6: abbreviations defined in the executive summary (C6)
- 4.6.1: breakwater share pointer
- 4.6.1: return pointer to 4.6 table
- 4.6.1: ref fixed
- 4.6.2: EUPI-PV defined at first use (C11, D2)
- 4.7: pointer to reference-plant table (D12, C7)
- 4.8: hinge figures in 4.1
- 4.9: pointer to 4.4 (C7)
- 4.10 status: Gijón wording (A3, C4)
- 4.10: installed power pointer
- 4.10 LCOE: pointer to 4.6
- 4.10 CAPEX/mooring: pointers to 4.6.1 and 6.5
- 6.1: Stadt pointer to 6.5
- 6.1: Zenodo wording as Annex A.23 (no unsourced claim)
- 6.1: ref A.10
- 6.2: beam tests pointer to 6.4; Table 5 kept
- 6.3: unit-weight wording (C10)
- 6.4: hinge figures to home 4.1
- 6.4: D6.3 hinge results to home 4.1
- 6.5: Stadt home, full statement (D35)
- 6.6: ABS defined in 3.2
- 7.2: Generation 1 description (C8)
- 9: 'targeted about 2030'
- 10: DIC
- 11: open-science wording (B1)
- 12: 'targeted about 2030'
- 13: access-rights wording (D6 cross-part)
- 13: refs to Annex A
- 14: access-rights wording
- 14: pointer to 4.4 (C7)
- 15: TRL short form, pointer
- 15: D7.4 pointer
- Exec: D7.4 pointer
- D40: 2.5.1–2.5.23 moved to Annex A as A.1–A.23, internal references updated
- D40: Annex B added
- Follow-up: Zenodo defined at first use in the reach table ("the open repository Zenodo"); own-share paragraph changed back to "on Zenodo".
