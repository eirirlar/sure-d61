# T150 round 5: cold-reader review of D8.4 (d84_merged.md)

Persona: an evaluator at another agency who has never seen the project. Questions throughout: why this choice, is this term defined yet, does this follow, have I read this before, does the pointer lead to the statement it claims. Line numbers refer to d84_merged.md (1,592 lines). Decisions D1–D65 and the owner questions (owner_questions.md) are taken as given; only text errors inside them are reported.

Checks run: the whole draft read end to end; every "Section x.y" and "Annex A.x" pointer followed to its target (about 120 pointers); a token comparison with d84_merged_r3int.md (figures, DOIs, preprint numbers, deliverable numbers, capitalised names and content words that disappeared); repo sources opened only to settle a doubt (D5.1 for the anchor-load claim, the final technical report working copy for the Gijón dates, which D22 does not allow as a citation).

## A. Round-5 comparison with d84_merged_r3int.md (lost figures, sources, credits)

Nothing was lost by accident. Every DOI, preprint number, deliverable number and Energies reference in r3int is still in the draft. The figures that disappeared were removed on purpose:
- 4.6.2 breakwater-share table (50 kWp 67/80 %, 300 kWp 30/46 %, 1 MWp 15/25 %, 5 MWp 6/11 %, 30 MWp 2/4 %), the 15 m / 20 m-unit / "straight at 30 MWp" geometry sentence and the €0.10/kWh cost of power: D60a and D60c.
- 4.7 EIC (−€1.1M; €0.92M) and EU-upside (−€0.7M; €0.93M) rows, and the €0.7M / €0.9M cash deltas: D60b.
- Executive summary "41 against more than 140" and "13 against more than 25": moved to 2.5 (lines 231, 243–244), not lost.
- D2.2 "Version 1.2, 31 January 2023": corrected to version 2.0 (r4_facts 3).
- 4.10 "it gives no per-farm figure comparable with the proposal's": replaced by D8.3's 170,000 t figure (r4_facts 5).
- "No measurable hinge buckling or snap loading was observed (D8.3)": now attributed ("D8.3 reports ...; MARIN's papers do not state it", line 409).

Credits checked one by one: MARIN (basin tests, DIFFRAC, mooring, Energies papers), SINTEF (D6.1, D6.3, D7.2, Task 4.3, Task 7.1, coordination), Clement Germany (WP3, D3.2, D3.3, D2.2, drawings in D8.3, Gijón contribution), ACCIONA (WP4, D4.1–D4.3, Task 6.5, D6.4), Ceit (WP5, D5.3–D5.7, Gijón monitoring), IFEU (WP7, D7.1, D7.3, D7.5, D7.6, D8.2, Task 8.1), Sunlit Sea (WP2, WP8, D3.1, D3.4, D7.4, Zenodo records, item-by-item WP8 output). All are present after the dedup pass. Two pointers lost their target in the removals: findings 1 and 2.

## B. Findings

1. Major. "After the project" means two different projects, and one pointer now leads nowhere (sections: executive summary, 4.1, 4.6.2, 4.7, 4.9, 14, 15).
   In this plan "the project" is SUREWAVE, which ends on 31 December 2026 (lines 5, 13). In the passages on the first commercial site with a breakwater class, "after the project" means after the EIC Transition project (2027–2030):
   - line 25: "The EIC Transition proposal targets the first commercial site with a breakwater class after the project, from about 2030";
   - line 711: "targets a first commercial installation of 1–5 MWp after the project ... The financial plan models it in 2031, the first full year after the project (Section 4.7)";
   - lines 421, 745, 754, 815, 1299 ("a first commercial site with a breakwater class, targeted after the project" in the 2030 row), 1307.
   A reader takes "the first full year after the project" as 2027 and finds 2031 instead. Second fault: since D60b removed the EIC rows from 4.7, Section 4.7 nowhere says 2031 for this plant (line 745 says only "a first commercial plant from the kit at the demonstrator site after the project"), so the pointer in line 711 leads to no such statement. In r3int, 4.7 and 4.9 (r3int lines 826, 1302) carried the 2031 link.
   Fix: write "after the EIC Transition project" (or "after the EIC Transition project, which would run 2027–2030") at each of these lines. Line 711: "The financial plan models it in 2031, the first full year after the EIC Transition project; Section 4.7 gives no figures for it." Line 745: "... and a first commercial plant from the kit at the demonstrator site in 2031, after the EIC Transition project." (No size and no euro amount, so D60b is respected.)

2. Minor. Pointer without target, 4.10 CAPEX row (line 843): "the fairlead and anchor loads rise in the optimised designs (Section 6.5)". Section 6.5 (line 1030) and D5.1 give only the maximum fairlead tensions (D5.1 l.1396–1424, "Maximum line tension at fairlead"; Table 9); neither gives anchor loads. Fix: "the maximum fairlead tensions rise, up to about 2.5 times the reference value (Section 6.5)".

3. Minor. Pointer without target, 4.6.1 "Path and gates" (line 702): "the exposed-site field record 2028–2030 (Section 4.6.2)". Section 4.6.2 gives no years for the demonstrator. The years are in 4.1 (configuration table, line 421) and 4.10 (line 836). Fix: "(Sections 4.1 and 4.6.2)", or add to 4.6.2 line 717: "The demonstrator would run 2028–2030, if the proposal is funded."

4. Minor. Pointer without target, 2.1 table, fifth D8.5 finding (line 102): "this plan does not assess what the panel frame adds to the float's robustness (Section 4.1)". Section 4.1 says nothing about panel frames. Fix: drop "(Section 4.1)".

5. Minor. Pointer that does not support the claim, 6.1 Network bullet (line 904): "Sunlit Sea initiated SuRE (Section 10)." Section 10 (line 1196) says that SuRE, coordinated by IFE, "grew out of contacts made through the SUREWAVE Stakeholder Advisory Board". It does not say who initiated it, and a reader asks how Sunlit Sea initiated a project that IFE coordinates. Fix: "SuRE, coordinated by IFE, grew out of contacts made through the Stakeholder Advisory Board that Sunlit Sea ran (Section 10)."

6. Minor. Wrong as written, 2.5 (line 225): "The CINEA clustering event of 25 April 2024, four days before D8.5 was issued, is the earliest item counted here." Earlier items are counted: Intersolar Europe and Seagriculture EU (June 2023), the SFI BLUES webinar (27 October 2023), DCIS 2023 (November 2023) (Annex A.4, A.5, A.7). The sentence means the earliest conference workshop or joint event. The sentence still sets two facts side by side and leaves the reader to draw the conclusion (r4_cold#16). Fix: "D8.5 ... reported one conference workshop and one joint event without naming them, and this plan cannot identify them. The earliest conference workshop and joint event counted here is the CINEA clustering event of 25 April 2024, four days before D8.5 was issued."

7. Minor. Logic jump, Section 10 MariSol row (line 1197): "In the other direction, the Council's record of MariSol lists wave-tank tests at Stadt Towing Tank, and Sunlit Sea's float tests at Stadt Towing Tank, made outside SUREWAVE, gave MARIN the data to validate DIFFRAC (D5.1)". The sentence suggests that the MariSol tests and the float tests MARIN used are the same tests, but does not say so. It also places a MariSol-to-SUREWAVE flow in the column "SUREWAVE results carried forward". Fix, if they are the same tests: "MariSol also gave SUREWAVE data: Sunlit Sea's float tests at Stadt Towing Tank, listed in the Council's record of MariSol and made outside SUREWAVE, gave MARIN the measured motions to validate DIFFRAC (D5.1)." If this is not established, cut the clause on the Council's record. 6.5 (line 1026) points here for "outside SUREWAVE" and stays valid either way.

8. Minor. Inconsistent evidence statement, Ceit's model calibration. 3.4 R8 (line 348): "calibrated on the WP4 test data (D5.7)"; 6.6 (line 1061): "calibrated the concrete model on the WP4 and WP6 test data". Fix: use the D5.7 wording in both places (6.6 is the home; R8: "calibrated on the WP4 and WP6 test data (D5.7; Section 6.6)", if D5.7 says WP6).

9. Minor. Statement of fact ahead of the step it depends on, executive summary (line 34): "a decision on design registration follows by ... Q3 2027, after the partners have confirmed their contributions to the hinge redesign". Elsewhere the confirmation is the WP8 lead's proposal (lines 855, 1157; r4_coord#7). Fix: "after the confirmation of contributions to the hinge redesign that the WP8 lead proposes for Q1 2027 (Sections 7.2 and 7.4)".

10. Minor. Term used before definition, 4.3.1 table, fourth row (line 505): "Phase 1 with Sunlit Sea as developer and EPC contractor before phase 2 kit sales". The phases are defined in 4.4 (line 545). Fix: "Phase 1 (Section 4.4), with Sunlit Sea as developer and EPC contractor, before the kit sales of phase 2".

11. Minor. Two measures mixed in one passage, 4.6.2 (line 715). The share is defined as breakwater cost over the cost of PV plant and breakwater together. The next sentence then gives a ratio to the PV plant ("from about as much as the PV plant to several times as much"), and the one after goes back to the share ("around a tenth of the plant cost"). The reader has to convert. Fix: "At a pilot-scale demonstrator ... the breakwater makes up half or more of the plant cost, since it costs from about as much as the PV plant to several times as much. At about 5 MWp its share is around a tenth, and at a few tens of MWp a few per cent; ..."

12. Minor. Unexplained choice, 4.1.1 cross-sections (line 433): "the chosen classes are somewhat larger, as a margin: 2.5 × 1.0 m against 2.5 × 0.9 m (light), 4.0 × 1.5 m against 3.0 × 1.2 m (medium)". The light class has a margin of 0.1 m of draft. The medium class is a third wider and a quarter deeper than the lightest section found. "Somewhat" understates this, and the reason is not given. Fix: state the reason, for example "the medium class is rounded up to 4.0 × 1.5 m so that it shares the keel geometry and draft-to-width steps of the heavy unit" (the owner should confirm the real reason), or "the margins differ: about 10 % in draft for the light class, about 30 % in width for the medium class, because ...".

13. Minor. DNV edition dates disagree. 4.5 (line 626): "the DNV floating solar documents (DNV, May 2026): DNV-ST-C108 ...; DNV-ST-E309 ...; and ... DNV-RP-0584". Section 8 (line 1165): "DNV-ST-C108 ... and DNV-ST-E309 ..., both 2026, and DNV-RP-0584", with the 2022 verification against DNV-RP-0584. 4.5.1 (line 659): "The 2026 editions of the DNV floating solar standards and recommended practice". The reader cannot tell whether DNV-RP-0584 has a 2026 edition or only the edition used in 2022. Fix: give each document's edition once, in 4.5 (for example "DNV-ST-C108 and DNV-ST-E309, May 2026; DNV-RP-0584, edition of [year]"), and use the same wording in Section 8 and 4.5.1.

14. Minor. Executive summary length and one overloaded paragraph (r4_cold#2, partly fixed). The summary is 1,616 words (1,733 in round 4). The paragraph at line 32 runs to about 260 words and covers EBITDA, the SuRE extension, volumes by status, equity, plant financing, the largest risk, four action-zone risks and the changes from the proposal. Fix: split it after "...beyond the plan." (finance) and start a new paragraph at "The largest single risk..." (risk and proposal changes). Optionally drop the plant-financing sentence (line 32, "Plant investments are financed at plant level, ..."), which is in 4.7.

15. Minor. "Small wavebreakers" against the light class, executive summary (line 24): "small wavebreakers (light floating barriers against wind waves and vessel wakes)". 4.6.2 (line 709) now says that they are bought from a wavebreaker supplier and are not built from the SUREWAVE classes (r4_cold#9), but the executive summary still calls them "light", the name of a class. Fix: "small wavebreakers (floating barriers bought from a wavebreaker supplier, against wind waves and vessel wakes)". The type is owner question Q86.

16. Minor. WP8 reference value equal to the count, 2.5 (line 176) and A.21 (line 1519). The LinkedIn-posts reference value of 25 equals the 25 posts that the WP8 record counts on 29 September 2026, the date of the record's earliest version. A reader sees a reference value set at the value already achieved. Fix, line 176, add: "For LinkedIn posts the reference value equals the count in that record on 29 September 2026."

17. Minor. Unsourced and vague, A.10 (line 1426): "Another board member works with Sunlit Sea in several joint initiatives." This gives no member, initiative or date, and is not used anywhere. Fix: cut it, or name the type of initiative and the year from Sunlit Sea's records.

18. Minor. Label in the R1 evidence cell, 3.4 (line 341): "Basin tests: D6.2 (MARIN); Energies 17(9) 2059 ...; D5.7 (Ceit)". A reader expects only MARIN under basin tests. D5.7 used the second campaign for the slamming check (line 1061). Fix: "D5.7 (Ceit; slamming check on the second campaign)".

19. Wording. Inside a paragraph, 4.1 "Comparison on the full edge" (line 411): "five segments with the rope carry about 10 kN ... With the rope, the full connection carries about 10 kN". The same figure is given twice in successive sentences. Fix: second sentence: "That is less than a third of the simulated extreme loads of 33–34 kN at the Baltic and Mediterranean sites; the steel-rod value, about 42 kN, is above them, and D6.3 then requires ..."

20. Wording. Second D8.3 difference, 4.1 (line 382): "about three times as strong in tension as the first-generation hinge on the same test scale. The factor is SINTEF's scaling ... of a one-fifth segment". "On the same test scale" (D8.3's phrase) and "scaling of a one-fifth segment" have to be read twice. Fix: "It gives the redesigned hinge as about three times as strong in tension as the first-generation hinge. The factor compares a complete first-generation hinge with five one-fifth segments held by a rope, SINTEF's scaling in D6.3; D8.3 does not say this. This plan gives the measured segment values and the scaling below."

21. Wording. References to sections of another deliverable look like this plan's sections: line 678 "(section 2.5 of D7.4)" (this plan has a Section 2.5 on dissemination) and line 849 "(section 7.4 of D7.4)" (this plan's Section 7.4 is on IPR actions). Fix: "(D7.4, its section 2.5)" and "(D7.4, its section 7.4)".

22. Wording. Repeated within 4.7: line 754 "The EIC and EU-upside cases improve the net result and the cash position against the base case" and line 758 "New EU project funding improves cash at the end of 2031 against the base case and the grant downside (scenarios above)". Fix: delete the bullet at line 758 and add "and the grant downside" to line 754.

23. Wording. The cost of the small wavebreakers being part of Sunlit Sea's first plant is stated four times: lines 567, 761 (home), 853 and 1226. Fix: keep line 761; elsewhere "(Section 4.7)". Lines 853 and 1226 can be cut to a clause with that pointer.

24. Wording. Section 1 (line 42): "This plan replicates at sheltered and nearshore coastal sites first and in the open sea later". "Replicates" has no object. Fix: "This plan starts replication at sheltered and nearshore coastal sites and moves to the open sea later; Section 4.10 gives the reasons."

25. Wording. 4.6.2 (line 719): "With the breakwater half carried by other uses, its cost of power is well above ...". "Its" could be the breakwater or the plant. Fix: "the plant's cost of power".

## C. Round-4 cold findings: status in this draft

Fixed: 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 17, 18, 19, 22 (pointer now "the float described in Section 4.1"; content is Q28), 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36.
Fixed in the dedup pass: 1. The Q1 2027 package now appears in full only in 7.4 and Section 9, the Horizon Results Platform proposal only in 6.8, the HPC sentence three times as D34 and the dedup log specify, and "nine months" only in the executive summary, 6.2 and a newsletter description. Remaining repetition is minor (finding 23).
Partly fixed: 2 (summary shorter, still long; finding 14); 9 (fixed in 4.6.2, not in the executive summary; finding 15); 16 (dates stated, but the sentence now reads as a wrong claim; finding 6); 20 (owner question Q87).
Rejected: 13 and 21 (see D).

## D. Rejections in my area: do they hold?

- rejected_r4: r4_cold#13 (counting-rule reason). Holds. D8.5 l.316 does not give the reason I proposed, and Q69 is open. The rule at line 204 still has no stated reason, so the owner's answer to Q69 should add one sentence.
- rejected_r4: r4_cold#21 (Generation 1 in 6.1). Holds now. D63 and Sunlit Sea's input make it a fact, and 4.1 (line 402), 7.1 and 6.1 now agree.
- rejected_r4: r4_cold#1 (one home per item, reserved for the separate pass). Overtaken: the dedup pass did it (dedup_log.md), and the result is acceptable.
- rejected_r3 (r3disp_C on r3_cold#10, #14). Overtaken (#10, by D63) and holds (#14, Q59).
- rejected_r2: r2_cold#5 (Section 13 lists stay as text). Holds; Section 9 points to Section 13 with no duplicate. r2_cold#6 (criteria between 2.4 and 3.3). Holds; 3.3 now applies the 2.4 rule without restating it. r2_cold#15 (campaign channel). Holds; A.22 states that the records do not show it.
- rejected_so_far: r1_cold#59 (glossary). Holds; every abbreviation met in this read is defined at first use (FPV, TRL, KER, WP8, EPC, LCOE, IRR, NPV, EBITDA, HPC, LWAC, CLC, CFD, DIC, SHMS, ILCSA, EERA, ISNRE, EU PVSEC, PTEC, SAB, BOSAT, UV, SCADA, PVC, CAPEX, OPEX, GEF). r1_cold#3, #60, #65, #66: hold.
- Owner questions that also cover reader problems found in this round, so not reported as findings: Q19 (Gijón exposure start and end dates; a reader of 6.2 asks "when?"), Q82 (the extension "gives time to complete this exposure", while the exposure itself has ended), Q28 (sandwich construction behind the pointer in 7.2), Q86 (wavebreaker type), Q87 (SAB set-up year), Q88 (Isdahl).

Findings: 1 major, 17 minor, 7 wording.
