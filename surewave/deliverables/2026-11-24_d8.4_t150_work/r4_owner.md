# D8.4 review, round 4: owner persona

Persona: Sunlit Sea's technical lead and WP8 leader. I looked for anything undersold, uncredited, unfinished or embarrassing in front of CINEA and the partners, and checked whether any evidence was lost since d84_merged_r1.md.

Document reviewed: scratchpad_t150/d84_merged.md (1,595 lines, the draft after the round-3 integration), read end to end. Line numbers refer to that file. Source paths are relative to C:\dev\src\sure-d61 unless stated. Decisions D1–D59 and owner_questions.md are treated as settled; I report errors inside them only.

## Part 1. Earlier rejections in my area: do they hold?

| Rejection | Holds? | Comment |
|---|---|---|
| rejected_r3: r3disp_C r3_cold#10 ("no source states that the SUREWAVE array's pressed-aluminium float is the Generation 1 float") | Does not hold | Sunlit Sea's own input states it: "During the first phase of SUREWAVE, Sunlit Sea focused on the development and testing of its Generation 1 floating PV platform, consisting of square aluminium floaters connected by polyurethane hinges. Laboratory and scale model wave tank tests revealed..." (surewave/background/2026-09-30_sunlit_sea_exploitation_summary.md:37). D3.1 describes the same float, pressed thin sheets of 5083-H111 marine aluminium (2023-06-26_surewave_d3.1_design_internal_floating_pv_components.md:248–252), and D3.3 sized the ring for 537 Wp panels, the Gen 1 panel (docs/project_facts.md, Products, Gen 1). D8.4 6.1 (line 912) already uses the input; 4.1 and 7.1 do not. See finding 2. Q28/Q70 can be reduced to the patent question. |
| rejected_r3: r3disp_C r3_owner#14 (stages of the hosts) | Holds | Owner decision, Q76. |
| rejected_r3: r3disp_F r3_owner#11 (final summary video) | Holds | Owner action, Q9. |
| rejected_r3: r3disp_F r3_owner#17 (Pehlke interview topic) | Holds | Owner fact, Q81. A.14 line 1467 still has no topic. |
| rejected_r3: r3disp_A 11 (owner action) and 4(g) (own-share paragraph keeps WP2/SAB) | Holds | |
| rejected_r3: r3disp_C r3_cinea#F10 (D7.4 v2.0 resubmission date) | Holds | Q39 / action 6. |
| rejected_r2: r2_owner#16, #22; r2disp_B r2_cold#15 (campaign channel) | Holds as a source rule | The text gaps remain (A.10, A.22); they are owner facts Q10, Q13. |
| rejected_so_far: r1disp_B 36 (D8.5 "April 2024") | Holds for the first delivery date, but incomplete | The repo copy of D8.5 is version 3.0 of 15 August 2024, "Revised version after PO comments" (2024-04-29_surewave_d8.5_...md:50). See finding 6. |
| rejected_so_far: r1disp_B 21 (own-event talks not counted) | Holds | It leaves Sunlit Sea with no counted presentation (2.5 table line 180), which is correct under the stated rule (line 200). |
| rejected_so_far: r1disp_A r1_owner#4, r1disp_B 4, 23, 24 | Holds | Q5, Q7, Q9. |

## Part 2. Round-3 owner findings: status in this draft

| r3_owner | Subject | Status now |
|---|---|---|
| #1 | Full-edge hinge said to be tested in the basin | Fixed (3.1 line 275, 4.1 lines 378, 390, 402, 6.1 line 912, 6.5 line 1037, 7.1 line 1122). |
| #2 | D8.3 changed after its delivery date | Not fixed in substance; owner action 5 (Q48). A.20 (line 1518), the reach table (line 241) and Annex B (line 1590) still say delivered 18 November and revised after the reviews of 18 and 19 November. |
| #3 | Zenodo records hold D7.4 v1.0 and the old cost model | Not fixed; owner action 2 (Q45). Lines 238 ("D7.4 version 2.0 still to be added") and 1532. |
| #4 | SUREWAVE/SuRE line for Generation 2 | Partly fixed: R1 (line 335), 4.1 (393–395), 7.1 (1122), Section 10 (1199). Still open in the 3.2 KER1 cell (finding 1) and on the origin of Generation 2 (finding 3; Q71). |
| #5 | Interviews filed as partner reports | Fixed (line 219). |
| #6 | Yearly web visits | Status cell fixed (line 243); 6.9 adds measurement from 2027 (line 1109). A.22 still says tracking ended "once the total target had been reached" (finding 9). |
| #7 | Infographic cards without a credited maker | Partly fixed ("published by Sunlit Sea ... whose designer is not recorded", lines 191, 1494). Q49. |
| #8 | Panel-frame finding | Reworded (line 98), still a non-answer. Q20. |
| #9 | SAB follow-up meeting stub | Partly fixed (organiser named, line 1427); date, format and participants still missing. Q13. |
| #10 | D8.3 errors listed twice | Fixed (3.1 step 4, line 270, is now a short source-conflict bullet; Stadt bullet only in 4.1). |
| #11 | Final summary video | Owner action Q9. |
| #12 | DeepWind year; D3.4 on Zenodo; D8.1/D8.3/D8.5 on Zenodo | D3.4 fixed (line 1532). "Year not reported by SINTEF" still at lines 1367 and 1397 (Q7/Q80). D8.x on Zenodo: action 3. |
| #13 | "Behind a breakwater" in the executive summary | Fixed (line 20). |
| #14 | Host stages in 4.3.1 | Q76. |
| #15–#16 | Interview and joint-event contributors | Fixed (lines 183, 189). |
| #17 | Pehlke interview topic | Q81. |
| #18 | "SINTEF reviewed version 0.2" | Fixed (line 1518). |

## Part 3. Evidence lost since d84_merged_r1.md

Method: every figure and every sentence of d84_merged_r1.md checked by script against the current draft (figures by exact match, sentences by word coverage below 80 %), and the same for d84_merged_r2final.md. Result:
- No figure or evidence item is lost except the deliberate, recorded cuts: the EUPI-PV site sizes (about 1 MWp in Sweden, about 4 MWp in Germany; Q61), the per-scenario euro revenue and EBITDA (D41, D47), the per-site host stages in 4.3.1 (Q76), "China" for the casting vendor (r2_writing#5), the 360 mm segment length (Q58), and the DNV Statement of Conformity month (Q63).
- The 3.2 table lost its headline figures (D54); each is in full in its home section: 40.9 kN is now 40.88 kN in 6.4 (line 1002), the 0.6 mm water penetration in 6.2 (line 932), the 3.69 kN in 4.1 (line 399).
- Round 3 removed nothing of substance; the only sentences without a match are the D47 EBITDA figures and rephrasings.

Conclusion: no evidence was lost. The weak points are the owner facts still open (Part 2) and the items below.

## Part 4. Findings

### 1. Major. The KER1 cell of the KER table names a SuRE product as the result and leaves out Sunlit Sea's SUREWAVE results (Section 3.2, line 295)

Quote: "Generation 2 floating PV platform (Sunlit Sea CONNECT) with full-edge polyurethane hinges and its mooring, developed in parallel in SuRE on the SUREWAVE hinge tests and models; site-planning tool with nearshore wave and wind models and a wave-loss module."

What is wrong:
- The table is titled "The seven KERs" and its "Result" column defines what each KER is. For KER1 it names a platform that the same cell says is developed in SuRE. CINEA manages both grants and is deciding the SuRE extension (line 753). A reader looking for double funding finds a SuRE product presented as the SUREWAVE result.
- 7.1 (line 1122) defines Sunlit Sea's SUREWAVE results differently: the hinge redesign, the nearshore models, the wave-corrected performance ratio and the wave-loss module. 3.4 R1 (line 335) gives yet another set: the open-sea reference design with the aluminium floats, the redesigned hinge, the site-planning tool, and the D7.4 economics.
- Sunlit Sea's own design deliverables are missing from the cell: the internal floating PV components (D3.1) and the global system design (D3.4), both led by Sunlit Sea (lines 15, 363, 901), and the economic assessment and cost model D7.4 (line 903). They are the SUREWAVE work the GA funded.
- "and its mooring": no section describes a CONNECT mooring as a SUREWAVE result; the mooring in SUREWAVE is Clement Germany's (D3.3) and MARIN's optimisation (D5.1).

Fix (3.2, KER1 "Result" cell): "Sunlit Sea's SUREWAVE results: the design of the floating PV array and of the global system (D3.1, D3.4, both Sunlit Sea), the hinge redesign from the paired connector to the full-edge connection (Section 4.1), the nearshore wave and wind models with the wave-corrected performance ratio and the wave-loss module of the site-planning tool, and the economic assessment and cost model (D7.4, Sunlit Sea). Commercial carrier: Sunlit Sea CONNECT, the Generation 2 platform, which Sunlit Sea develops further in SuRE on these results (Section 4.1). Sunlit Sea's background (the Generation 1 float and hinge) and its SUREWAVE results are distinguished by design version (D1.8). For exposed sites, the plant integrates the floating breakwater, ... (unchanged)". Use the same list in 7.1 (line 1122) by adding "the design of the floating PV array and of the global system (D3.1, D3.4)" before "the hinge redesign".

### 2. Minor. 4.1 and 7.1 avoid saying that the SUREWAVE array used the Generation 1 float, which 6.1 and Sunlit Sea's input state (lines 393, 395, 1122)

Quotes:
- Line 395: "The SUREWAVE reference design uses floats of pressed marine-grade aluminium sheets".
- Line 393: "Generation 1, Sunlit Sea's earlier product, uses square aluminium floats joined by polyurethane hinges."
- Line 912 (6.1): "Laboratory and wave-basin tests in SUREWAVE showed that the Generation 1 platform, square aluminium floats joined by polyurethane hinges, took excessive hinge loads".

What is wrong: the three passages describe the same float in two ways, and only 6.1 says what it is. The reader of 4.1 cannot tell whether the background float was tested, which matters for the background/result split of 7.1. The source exists (Part 1: Sunlit Sea input line 37; D3.1 lines 248–252).

Fix:
- Line 395: "The SUREWAVE reference design uses Sunlit Sea's Generation 1 float, made of pressed marine-grade aluminium sheets (D3.1), and D7.4 and D7.6 assessed the array with these floats (D7.6)."
- Line 1122: "Its background is the Generation 1 float and hinge, used in the SUREWAVE reference design, and its earlier patent."
- Q28/Q70 then keeps only the patent question (sandwich construction, patent in force).

### 3. Minor. "Sunlit Sea develops CONNECT in the parallel project SuRE" compresses Sunlit Sea's own account of where Generation 2 began (exec summary line 20; 4.1 line 393; 7.1 line 1122; Section 10 line 1199)

What is wrong: Sunlit Sea's input says that the SUREWAVE tests "led to a complete redesign of the product architecture, resulting in Generation 2", that several prototypes were produced and tested at SINTEF and MARIN, and that "This redesign process continues in the follow-up EU project SuRE, where prototype 4 and 5 of generation 2 will be developed" (sunlit_sea_exploitation_summary.md:41, 43). The draft says CONNECT is developed in SuRE, which drops the SUREWAVE start of the redesign that Sunlit Sea reported, while 6.1 (line 912) keeps it ("Sunlit Sea redesigned the hinge and the product architecture"). D13 asks partner statements to follow the partner's own input. The prototype boundary itself is Q71; the wording below is true on either answer.

Fix (in 4.1 line 393; same words in 7.1 and the Section 10 SuRE row): "Sunlit Sea started the Generation 2 redesign from the SUREWAVE hinge tests and models and continues it in the parallel project SuRE, where prototypes 4 and 5 are developed and prepared for pilot-scale deployment (Section 10)." Exec summary line 20: "... It replaces the Generation 1 aluminium float; the redesign started from the SUREWAVE hinge tests and models and continues in SuRE (Section 4.1)."

### 4. Minor. Broken pointer for the Generation 1 patent (Section 7.2, line 1130)

Quote: "Sunlit Sea's earlier patent concerns the sandwich construction of the Generation 1 float (Section 4.1)."

What is wrong: Section 4.1 does not mention a sandwich construction (checked: "sandwich" occurs only at line 1130). The pointer sends the reader to text that is not there.

Fix: "Sunlit Sea's earlier patent concerns the sandwich construction of the Generation 1 float, the float described in Section 4.1." If Q28 shows that the pressed-sheet float of D3.1 is not the patented sandwich, drop the pointer.

### 5. Minor. Annex B shows the WP8 lead's own first deliverable D8.1 as missing from the records (line 1588)

Quote: "D8.1 | Dissemination, Exploitation & Communication Master Plan | Sunlit Sea | PU | –", with the annex rule "A dash means that the project records checked hold no copy of the deliverable" (line 1553).

What is wrong: Sunlit Sea wrote D8.1 (line 254) and it is openly on Zenodo, as A.23 states (line 1533, doi 10.5281/zenodo.8278574; zenodo snapshot line 38). The dash tells CINEA that the WP8 lead does not hold its own deliverable.

Fix: "Month 6 (March 2023); Zenodo record 10.5281/zenodo.8278574". If the owner has the cover page, give its actual delivery date instead of the month.

### 6. Minor. D8.5's revision after the project officer's comments is not shown, and its cover gives another dissemination level (Annex B line 1592; Section 2.1 line 79; Section 2.5 line 221)

What is wrong:
- The D8.5 in the repo is version 3.0 of 15 August 2024, "Revised version after PO comments", by Eirik Larsen and Balram Panjwani (2024-04-29_surewave_d8.5_...md:50). Annex B gives only 29 April 2024. For D3.4, Annex B shows the revision after the project officer's feedback ("Version 3.0, 31 May 2024 (first delivered 19 March 2024)", line 1567); D8.5 is treated differently, and Sunlit Sea's response to the project officer goes uncredited.
- D8.5's cover gives "Dissemination level SEN" (same file, line 26); Annex B gives PU from the Grant Agreement, and OpenAIRE lists D8.5 among the public deliverables (line 1534). Annex B follows the GA, which is right, but the conflict is not stated.

Fix: Annex B: "Version 3.0, 15 August 2024, revised after the project officer's comments (first delivered 29 April 2024)". Add to the Annex B introduction: "Where a cover page gives another level, this table follows the Grant Agreement (D8.5's cover gives SEN)."

### 7. Minor. The only surviving web-traffic evidence is in page views, while the met target is in visits (2.5 table line 198; A.22 line 1526)

What is wrong:
- The Matomo account no longer exists (KPI record 2026-11-19_surewave_wp8_kpi_verification.md:298). The supporting e-mail of 29 May 2024 quotes "3 022 sidevisninger" (page views) and "The 33K views will be reached for sure!" (same file:300). D8.5 lists page views among the Matomo indicators (D8.5:533).
- The target is visits (GA: "12,000/year web visits, >36.000 in total", grant agreement:7611). If a reviewer reads the e-mail, the 50,000 can look like page views, and the "Met" on the website row has no other check.

Fix (owner fact, then text): confirm that the 50,000+ in the KPI tracker (2026-09-29_surewave_wp8_kpis.md:58) is Matomo's "visits" metric. Then write in A.22: "By the end of 2024 Matomo recorded more than 50,000 visits (its visits metric, not page views), more than 49,000 of them in 2024." If it was page views, change the row to "Not measured" and the count of met targets to 10 of 16.

### 8. Minor. D8.5 states the 36,000 target in two ways (2.5 table line 198)

Quote: "More than 36,000 in total (GA); 36,000 (D8.5)".

What is wrong: D8.5 gives "Goal of 36,000 visits" (D8.5:298, 1003) and also "Aim to attract over 36,000 visits annually" (D8.5:523). The second reading is a yearly target that only 2024 met. The draft takes the first reading without saying so (requirement 2: flag every conflict).

Fix: "36,000 (D8.5, which also states it once as a yearly aim)" in the target cell. The status stays "Met" against the GA total; the yearly GA row (line 243) already covers the yearly reading.

### 9. Minor. A.22 still says the WP8 lead stopped measuring once the target was reached (line 1526)

Quote: "Sunlit Sea ended tracking and the Matomo subscription at the end of 2024, once the total target had been reached and recorded."

What is wrong: the GA also sets 12,000 visits a year (line 243), so the reason reads as stopping the measurement of a running target. This is the remainder of r3_owner#6. The KPI tracker gives the same reason (2026-09-29_surewave_wp8_kpis.md:58), so the fact stays; the framing can change.

Fix: "Sunlit Sea ended the Matomo subscription at the end of 2024, after recording the total. The yearly visits of 2025 and 2026 were therefore not measured; measurement resumes from January 2027 (Section 6.9)."

### 10. Minor. Sunlit Sea's own DNV verification is left out of the value-proposition evidence (Sections 4.3.1 line 496, 4.3.2 line 515, Lean Canvas line 582)

What is wrong: 4.3.1 tests the hypothesis that buyers accept a new system "on test results alone" and cites only competitors' certificates. 4.3.2 rates KER1's "References and independent review" as "To be raised". Section 8 (line 1168) records that DNV verified Sunlit Sea's Generation 1 design basis against DNV-RP-0584 in 2022 (DNV news release; project_facts line 122). The plan undersells the one independent review Sunlit Sea already has.

Fix:
- 4.3.1, evidence cell, add: "Sunlit Sea's own Generation 1 design basis was verified by DNV against DNV-RP-0584 in 2022 (Section 8)."
- 4.3.2, KER1 cell: "To be raised: DNV verification of the Generation 1 design basis (2022); Norwegian reference plants and DNV assessment of Generation 2 in 2027–2028".
- Lean Canvas, unfair advantage: "... Generation 1 in commercial operation since 2023, with a DNV-verified design basis (2022); ...".

### 11. Minor. The team description leaves out who did Sunlit Sea's SUREWAVE work (Section 4.2, line 448)

Quote: "The chief executive officer (CEO) invented Generation 1 and holds the design and casting work for Generation 2; the technical lead is responsible for the site-planning tool, sales, projects and administration."

What is wrong: the BOSAT rated team as one of six dimensions (line 139), and key-person dependency is an action-zone risk (line 798). The technical lead authored D2.4, D7.4 (versions 1.0 and 2.0) and D8.5 (version tables: d2.4 lines 44–48, d7.4 lines 48–58, d8.5 lines 42–50) and moderated the SAB webinar (line 1403). The description reduces the person who carried Sunlit Sea's SUREWAVE deliverables to "administration".

Fix: "... the technical lead, who led Sunlit Sea's SUREWAVE work on the Stakeholder Advisory Board (D2.4), the economic assessment (D7.4) and WP8, is responsible for the site-planning tool, sales, projects and administration."

### 12. Minor. Sunlit Sea's open records are given in part (2.5 own-share paragraph line 254; A.23 line 1532)

What is wrong: the own-share paragraph names three of Sunlit Sea's six community records (D3.4, the cost model, the metocean dataset). The other three are D2.4, D3.1 and the D7.4 report (zenodo snapshot, records 5, 13, 14). A.23 gives use figures for the cost model (223 views, 101 downloads) but not for the metocean dataset, which has the second-highest use of the community's datasets (86 views, 50 downloads; snapshot record 15).

Fix: own-share paragraph: "It registered six of the 18 records in the SUREWAVE community on Zenodo: D2.4, D3.1, D3.4, the D7.4 report, the D7.4 cost model and the metocean design dataset (Annex A.23)." A.23, after the metocean doi: "with 86 views and 50 downloads".

### 13. Wording. The open-access sentence in 2.5 does not parse, and it repeats A.23 (line 252)

Quote: "The partners deposit the other five before this plan is submitted, MARIN's paper at MARINE 2025, the conference on computational methods in marine engineering, as its accepted manuscript under CC BY, since its published licence (CC BY-NC-SA 3.0) excludes commercial use."

Fix: "The partners deposit the other five in the SUREWAVE community on Zenodo before this plan is submitted. For MARIN's paper at MARINE 2025, the conference on computational methods in marine engineering, MARIN deposits the accepted manuscript under CC BY, since the published licence (CC BY-NC-SA 3.0) excludes commercial use. Annex A.23 gives the status of each paper." Then delete the last three sentences of A.23 (line 1549), which say the same, keeping the GA rule there. Sunlit Sea, as co-author of Energies 17(9) and administrator of the community, can make that deposit itself (owner action 1).

### 14. Wording. "far below" where the numbers are at hand (line 404)

Quote: "With the rope, the full connection stays far below the simulated extreme loads of 33–34 kN".

Fix: "With the rope, the full connection, at about 10 kN, carries less than a third of the simulated extreme loads of 33–34 kN".

### 15. Wording. "strongly reduced" (6.5, line 1033)

Quote: "In the D5.1 simulations the breakwater strongly reduced the vertical hinge loads."

Fix: give D5.1's figure, as the next sentence does for the horizontal loads, or write "reduced the vertical hinge loads more than the horizontal ones".

### 16. Wording. "far fewer fossil resources" (4.3.3, line 519)

Fix: "uses less fossil resources" or D7.6's own figure.

### 17. Wording. "a new PhD is not shown" (exec summary line 32; 2.5 line 168)

Fix: "no new PhD is recorded".

### 18. Wording. The SAB follow-up bullet repeats the paragraph above it and calls Sunlit Sea's confirmation a record (A.10, line 1427)

Quote: "Follow-up meeting with board members in March 2025 (month 30), organised by Sunlit Sea, which set up the board in WP2; the record of the meeting is Sunlit Sea's confirmation. Its date, format and participants are not in the project records checked."

Fix (until Q13 gives the details): "Follow-up meeting with board members in March 2025 (month 30), organised by Sunlit Sea; its date, format and participants are to be taken from Sunlit Sea's calendar and e-mail." Better, with Q13 answered: "[date] March 2025, [online], with [n] board members, on [topic] (Sunlit Sea's calendar)".

Findings: 1 major, 11 minor, 6 wording.
