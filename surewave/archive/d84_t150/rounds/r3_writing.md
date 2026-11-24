# T150 round 3: editor and confidentiality review of d84_merged.md

Persona: editor and confidentiality reviewer. Scope: requirement 7 and CLAUDE.md "Language and tone", read sentence by sentence, annexes included; terminology, units, numbers, headings, repetition, readability for non-native readers, tables; consistency where it is a matter of terms or of the text contradicting itself. Confidentiality checked against the financial plan (surewave/deliverables/2026-11-22_surewave_hrb_financial_plan_ker1.md, "FP"), docs/project_facts.md ("PF"), D7.4 (public) and the EIC Transition proposal (generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md, "EIC"), which SINTEF, Clement Germany and EDP hold. Line numbers refer to d84_merged.md (1,541 lines, read end to end). Decisions D1–D45 and the round 1 and round 2 revisions are taken as given; only errors inside them are reported.

Mechanical checks run:
- No `**` in the file.
- Emphasis words and conclusion connectives: no "precisely", "crucially", "clearly", "therefore", "thus", "which is why", "it follows", "well beyond", "importantly". "already" once (l.754, literal). "very" once (l.147, the expert's rating). "substantially" (l.970) and "significantly" (l.1217) are the source's and the GA's wording. "key" occurs only in names (Key Exploitable Results, key people, key performance indicators). All "not" constructions put the positive claim first ("Y, not X").
- All tables: same column count in every row, valid separator row, blank line before and after. Longest cell now 886 characters (l.328).
- Every "Section x.y" and "Annex A.n" reference resolves to an existing heading.
- Counts re-checked: D2.4 Advisory Board, seven organisations, three with several roles, four companies (D2.4 l.209–261); conferences 14 (7 + 2 + 2 + 3); presentations 15; web events 4; joint events 3; workshops 3; articles 8 (5 + 3); media mentions 8 + 1 + 4 = 13; Zenodo 6+4+2+2+2+1+1 = 18 and 12 + 6; OpenAIRE 13 deliverables; publications 6 journals + 1 proceedings + 3 congress papers; volumes 13/15/72 %; scenario differences (−0.7 vs −1.4 and −1.6); 5 × 2.04 = 10.2 kN, 5 × 8.36 = 41.8 kN; 40/37 = 1.08; 7.89 × 10⁸ cycles; 2.27–2.44 mass ratios; 0.44–0.49 GW a year. All correct.
- Pandoc behaviour checked on a test file (pandoc -t native): a heading directly after a paragraph line is read as paragraph text; a heading directly after `---` is read as a heading.

## A. Major

1. Major (rendering). Section 2.5, l.170–171, and Section 4.7, l.714–715. The headings "### 2.5 Dissemination and communication results" and "### 4.7 Financial plan" follow a paragraph line with no blank line between. Pandoc (default markdown, `blank_before_header`) reads them as part of the paragraph: the docx will show "… Section 3.3 gives the assessment for each KER. ### 2.5 Dissemination and communication results" as running text, and Sections 2.5 and 4.7 disappear from the heading structure and the table of contents. Verified with pandoc on a test file (output: `Para [… SoftBreak, Str "###", Str "2.5" …]`). Fix: insert a blank line before l.171 and before l.715. For uniformity also add a blank line between `---` and the heading at l.250, 351, 872, 1145 and 1177 (these render correctly today, but the restructure scripts produced the pattern, so a later edit can turn them into the same fault).

2. Major (confidentiality; error inside the owner decision on generalised figures). Section 4.7, l.719, 760, 764, 765. The owner decision allows volumes and a margin level but not Sunlit Sea's prices or costs per watt. Two sensitivities, combined with the stated contract size and the margin target, give both:
   - l.719 "a first 10 MW-class kit supply contract of about 10 MWp"; l.764 "If the 10 MW-class contract is not won, the net result over the period falls by about €2.4M and 2031 EBITDA is about €0.7M". €2.4M over 10 MWp is a gross profit of €0.24 per watt (FP l.120: "a gross profit of about €2.4 million" on €4.9M of revenue). l.760: "the plan's kit gross margin target is 40–50 %, and the plan meets it at today's kit price and production cost". A gross profit of €0.24/W at a 40–50 % margin is a kit price of €0.48–0.60/W and a production cost of €0.24–0.36/W. FP l.130–132: €0.25/W cost, €0.50/W price; PF l.37: "Never in external copy".
   - l.765 "Kit volume 30 % lower in 2030–2031 moves 2031 EBITDA by about €0.9M": 30 % of the 2031 volume (about 16 MWp, l.727) is 4.8 MWp, so about €0.19/W of gross profit, and with the 40–50 % margin a price of about €0.38–0.47/W (FP l.460).
   - D7.4 (public, surewave/background/2025-09-05_surewave_d7.4_economic_assessment.md l.828) prices the PV modules at €500/kWp; a partner who assumes the kit is priced at D7.4's figure gets the production cost straight from the margin target.
   This route is independent of the 2030–2031 revenue line that owner question D41 covers: removing that revenue would not close it. Fix (keeps the volumes and the margin level the owner allows; removes the euro effects that turn them into a per-watt figure):
   - l.764: "If the 10 MW-class contract is not won, the net result over the period falls, 2031 EBITDA stays positive and cash stays positive."
   - l.765: "Kit volume 30 % lower in 2030–2031, or a lower kit price or a higher kit cost within the range tested, lowers 2031 EBITDA but keeps it positive."
   - l.766 (combined downside, −€5.6M and −€0.6M) mixes delay, volume and cost and gives no per-watt figure; it can stay.
   If the owner prefers to keep the euro amounts, drop the margin figures instead (l.724 "41–44 %", l.760 "40–50 %") and the contract size "of about 10 MWp" (l.719, l.446); say in the owner question that one of the two sets must go.

3. Major (consistency, requirement 6; it touches the main KER1 evidence). What MARIN's second basin campaign tested. l.383: "The hinge redesign has been tested at SINTEF (D6.3) and in MARIN's second basin campaign (D8.3)"; l.1082: "the Generation 2 architecture with the redesigned full-edge hinge, tested by SINTEF (D6.3) and in MARIN's second basin campaign (D8.3)"; l.893: "tested mechanically at SINTEF and in MARIN's wave basin. Hinges distributed along the full edge of the floats improved load capacity and durability." The same plan says at l.395–396 that the second campaign "used an improved connector, longer and thicker than the first generation and fitted in pairs between adjacent floats", which is the second generation ("the paired second-generation corner hinges", l.396), and that the full-edge third generation was tested only as a one-fifth segment at SINTEF (l.394). Sources: Energies 19(7) 1609 (surewave/background/2026-03-25_bunnik_hydrodynamic_simulations_2mw_offshore_solar_fpv.md l.70–71, 122: "a new design of the polyurethane connector, longer and thicker than the first generation", "adjacent FPV modules are connected through a pair of connectors"); D7.6 l.687–689 (v2 = shorter hinges at the corners, v3 = full width, 1.88 m). D8.3 l.200 ("The second campaign evaluated the redesigned hinge") is the older and less specific source; MARIN's 2026 paper wins (requirement 2). Fix:
   - l.383: "Sunlit Sea rates its CONNECT platform at TRL 4–5. A one-fifth segment of the full-edge third-generation hinge has been tested at SINTEF (D6.3); MARIN's second basin campaign used the improved second-generation corner hinges and observed no measurable buckling or snap loading (Energies 19(7) 1609; D8.3). Prototype 3 of the Generation 2 float has been cast and prototype 4 is in casting; no Generation 2 plant has operated yet."
   - l.1082: "Sunlit Sea's SUREWAVE results are the Generation 2 architecture with the redesigned full-edge hinge (Section 4.1), the nearshore wave and wind models, …"
   - l.893: "Several prototypes were CAD-modelled, 3D-printed and cast in polyurethane. The improved second-generation hinges were tested in MARIN's second basin campaign, and a segment of the full-edge third generation at SINTEF (Section 4.1). Sunlit Sea expects the full-edge hinge to raise load capacity and durability."
   - l.367: "differs from this plan on six points", with a sixth bullet: "It states that the second basin campaign evaluated the redesigned hinge. MARIN's paper on the campaign (Energies 19(7) 1609) shows that it used the improved second-generation corner hinges; the full-edge hinge was tested as a segment at SINTEF (D6.3)."
   - l.395, for the reader who follows the numbering of l.390: "MARIN's second campaign used an improved connector of the second generation, longer and thicker than the first and fitted in pairs between adjacent floats".

## B. Minor

4. Minor (confidentiality, pipeline; owner question). Section 4.4 table l.537–541 and l.719 "three Norwegian reference sites (a harbour, an industrial basin and a lake)". The EIC proposal, which SINTEF, Clement Germany and EDP hold, names the pipeline: "Skien Havn, Gunneklevfjorden, and Haugaland Næringspark" (EIC l.64, also l.163, 169). For these partners the site types are named sites, and the 4.4 table then gives each named project's commercial structure: Sunlit Sea's role, the minority share in the industrial-basin plant company (about €0.2M, l.752), the quarter of each investment decision and of commissioning, the rezoning at the lake. l.602 ("One local contractor on both larger Norwegian projects") adds the shared contractor. The owner decision allows site types, so this is an owner question, not a fix I can make on my own. Recommendation: drop the "Site type" column of the 4.4 table and the parenthesis in l.719 ("three Norwegian reference sites at sheltered coastal and inland sites"); keep "a Norwegian port" for the first plant, which appears throughout and is the field record of the small wavebreakers. Rejection r2disp_D/r2_writing#3 holds for 4.7 alone, not for this combination.

5. Minor (confidentiality, low; owner question). Section 4.6.2, l.693, 698, 704–714. The table rows (demonstrator 50 kWp, then about 1, 5 and 30 MWp), the 45° sector, half the cost carried by dual use, and "The baseline site of the EIC Transition demonstrator … is such a lake" reproduce the internal scale-up path of the EIC host lake (PF l.67: "Base case: light breakwater over about 45° of exposure, half of its cost carried by dual use. Scale-up after the demonstrator: 1 MWp, then 5 MWp, then about 30 MWp"). The proposal names the lake and its owner (EIC l.72, 167). With l.714 ("it produces power at about €0.10/kWh") the table reads, for those partners, as the host's business case. No price per watt follows from it (D21 is applied), so the risk is low. Fix if the owner wants it: present the table as a generic site ("The table shows a generic lake site with one exposed side of about 45°") and cut "There a light breakwater covers the exposed side, a sector of about 45°, and the site owner's other uses, such as berths or bathing platforms, can carry part of its cost" from the lake sentence in l.693. Rejection r2disp_C/r2_writing#4 (€0.10/kWh, owner question 7) holds.

6. Minor (consistency). l.24 "First product: Sunlit Sea sells Sunlit Sea CONNECT" and l.19 "the product P1 Offshore FPV plant …, which Sunlit Sea AS markets". l.491: "Generation 2, which is not yet for sale"; l.532: first kit sales from 2028; l.383 and l.406: prototype 4 in casting. Fix l.24: "First product: Sunlit Sea CONNECT, Sunlit Sea's Generation 2 floating platform and the core of KER1, for sheltered coastal sites: first in Sunlit Sea's reference plants from 2027, then as a kit from 2028." Fix l.19: "the product P1 Offshore FPV plant (FPV: floating photovoltaic), to be marketed by Sunlit Sea AS".

7. Minor (consistency). Section 5, l.850: "That site is targeted about 2030 … ; it comes in 2029 if the EUPI-PV nearshore demonstration goes ahead (Section 10)." It states as a fact what l.693 states as a possibility ("could come earlier, in 2029") and what depends on two open decisions (Sunlit Sea joining; funding). Fix: "… ; a nearshore demonstration with a breakwater could come earlier, in 2029, if Sunlit Sea joins the EUPI-PV application and it is funded (Section 10)."

8. Minor (requirement 3). l.712: "The demonstrator's breakwater is funded by the demonstration grant." The EIC Transition proposal is under evaluation. Fix: "The demonstrator's breakwater would be funded by the EIC Transition grant, if the proposal is funded."

9. Minor (broken pointer). l.697: "PV plant: the cost of a plant built from the kit (Section 4.7)". Section 4.7 gives no plant cost (removed under D21). Fix: "PV plant: the cost of a plant built from the kit in Sunlit Sea's financial plan, taken as the same per watt at every size."

10. Minor (counting text incomplete). Section 2.5, l.203–212: the list "Items counted under more than one indicator" omits two items that Annex A counts twice: the SFI BLUES webinar of 27 October 2023 (presentation, A.5; web event, A.7) and ACCIONA's talk at the PTEC online event of 7 November 2024 (presentation, A.5; web event, A.7). The general rule in l.201 covers conferences, not webinars. Add: "- the SFI BLUES webinar of October 2023: presentation and web event;" and "- ACCIONA's talk at the PTEC online event: presentation and web event;". l.214 "Three targets rest in part on items counted elsewhere" omits the SAB workshops (2 of 2; the SAB webinar is also a web event and a video recording). Fix: "Four targets rest in part on items counted elsewhere: …, infographics (the CINEA poster) and SAB workshops (the SAB webinar is also a web event)."

11. Minor (status date). l.258: "the Horizon Results Booster sessions of October to December 2026". The December workshop is planned (l.141); the status date is 23 November 2026. Fix: "the Horizon Results Booster sessions of October and November 2026, which concerned KER1 and Sunlit Sea (Section 2.3), with a further workshop planned for December".

12. Minor (r2#34 partly fixed). Annex A.20, l.1475: "was issued on 18 November 2026 … Clement Germany reviewed the issued brochure on 18 November 2026: its comments corrected …, and its own drawings replaced the earlier illustrations … MARIN reviewed the brochure on 19 November 2026; following its review, the brochure states …". The reader cannot tell whether the issued D8.3 contains these changes, since two reviews post-date the issue. The D8.3 cover itself says "September 2026" (surewave/deliverables/2026-09-28_surewave_d8.3_technical_brochure.md l.14). Fix: "The technical brochure D8.3 … was first issued on 18 November 2026. SINTEF reviewed version 0.2 …, IFEU version 0.3 …. Clement Germany (18 November) and MARIN (19 November) reviewed the issued brochure, and it was revised after their reviews: Clement Germany's comments corrected …; following MARIN's review, it states …". Give the date of the revised version in the same sentence.

13. Minor (r2#19 partly fixed). Gate 3, l.772: "(Q1–Q2 2028)" against M7 "Q2 2028" (l.822), l.629 "(Q2 2028)", l.805 "in Q2" and l.1257 "Q2". Fix: "(Q2 2028)".

14. Minor (repetition; r1#32 and r2#20 still open; D40 "one home per evidence item"). Each statement below is written out in full in several places:
   - Integration transfers no ownership of Clement Germany's components: l.19, 288, 290, 328, 363, 869, 1082. Home: 7.1 (l.1082). Elsewhere keep the clause of D29 ("designed by Clement Germany (KER3)") and point to Section 7.1; delete l.363 and the second sentence of l.869.
   - The plant owner buys the breakwater; Sunlit Sea buys it as EPC contractor: l.25, 553, 756, 854, 862. Home: Section 5 (l.854) and the 5 table (l.862). In l.553 and l.756 write "Breakwater classes are bought as set out in Section 5."
   - Access rights to SINTEF's and MARIN's test results, Q1 2027, "before the design freeze": 10 occurrences (l.397, 624, 798, 804, 850, 1124, 1131, 1184, 1209, 1256). Home: Section 9 (l.1124, 1131). Keep it in the 4.5 milestones (l.624) and the 4.9 action plan (l.804); elsewhere "(Section 9)".
   - SuRE "grew out of contacts made through the Stakeholder Advisory Board": l.38, 894, 1151, 1386. Home: Annex A.10 and the Section 10 table; delete it in l.894 ("Sunlit Sea initiated SuRE (Section 10).").
   - "SuRE and SUREWAVE fund different work" and "pending at CINEA": l.32, 599, 737, 782, 1151. Home: 4.7 (l.737). In l.599 and l.782 write "(SuRE extension, Section 4.7)".
   - The Gijón prototype credit ("designed and cast by ACCIONA, with SINTEF and Clement Germany as contributing beneficiaries (D4.3) … deployed by ACCIONA at its … demonstration site in the Port of Gijón …"): l.289, 330, 425, 915. Home: 6.2 (l.915). In the 4.1.1 heavy-class row (l.425) write "reduced-scale prototype exposed nine months at Gijón (Section 6.2)".
   - "about 123 t, slightly above the upper weight of about 120 t that D3.2 set for handling with mobile cranes": l.329, 425, 936. Home: 6.3 (l.936); in l.329 and l.425 "about 123 t (Section 6.3)".
   - "could not be fully validated within the project": l.396, 787, 893. Home: 4.1; in l.893 delete the clause after "(D7.2)".
   - The Horizon Results Platform rule: l.34, 878, 1063, 1171, 1186, 1202. Home: 6.8 and 13; l.878 and l.1171 can point to 6.8.
   - "The value propositions for KERs 2–7 are those stated by their owners": l.495 and l.874. Delete l.495's sentence; l.874 is the home.
   - The Zenodo cost-model record holding the version 1.0 cost model: l.886 and l.1489. Keep it in A.23 only (see item 26).
   - Re-expanded terms: FPV (l.19, 46), IFE (l.38, 441, 891, 1151), ERA5 and GEBCO (l.431, 890), HPC/LWAC/CLC (l.259, 840, 1475), BRIDGE (l.245, 1462). Expand once; use the short form afterwards.

15. Minor (title mismatch). D7.2 is called "SINTEF's technological risk assessment" throughout (l.17, 294, 379, 396, 1047), while Annex B (l.1528) gives its Grant Agreement title, "Report on technological qualitative assessment". A reader who looks up D7.2 in Annex B finds a different name. Fix at first use (l.17): "SINTEF's technological risk assessment (D7.2, Report on technological qualitative assessment; Preprints 202611.1173)".

16. Minor (wording that changes the meaning). l.683: "The SUREWAVE breakwater variants in ACCIONA's circular mixes, both with a cellular-concrete core, cost more than the conventional one: about 24 % more with the lightweight-aggregate shell and about 76 % more with the high-performance-concrete shell, which raises the LCOE from €0.076 to €0.085/kWh." "which" can be read as both variants raising the LCOE to €0.085; D8 assigns the €0.085 to the HPC variant. The abbreviations defined in l.259 are not used. Fix: "The breakwater variants in ACCIONA's circular mixes, both with a CLC core, cost more than the conventional breakwater: about 24 % more with an LWAC shell and about 76 % more with an HPC shell. The HPC variant raises the LCOE from €0.076 to €0.085/kWh (D7.4)."

17. Minor (D8.5 finding not answered). Section 2.1 table, l.105–106: the rows "Off-the-shelf solar panels in place of custom panels" and "Use of the panels' aluminium frames for robustness" have almost the same outcome text, and the second does not say whether the panel frame contributes to robustness in Generation 2. Fix: state the outcome for the frame finding, e.g. "Not taken up: in Generation 2 the cast polyurethane structure carries the loads and holds a standard glass-glass panel (Section 4.1)", if that is the design; otherwise state how the frame is used.

18. Minor (abbreviations used before or without expansion; the r1_cold#59 glossary rejection holds only if every term is defined at first use):
   - "GEOPON (SINTEF)" (l.38): reads as part of a name. Fix: "a national project of SINTEF with the industrial partner GEOPON".
   - "Surewave-ANN" (l.225) before ANN is expanded (l.334). Fix l.225: "Surewave-ANN, SINTEF's artificial-neural-network model, within KER4".
   - "CEM III" (l.260, 289, 908, 913) and "CEM I" (l.908) are never explained. Fix l.260: "the same recipe with a CEM III cement (blast-furnace cement, in which slag replaces part of the clinker)".
   - "GEF" first at l.1279 ("The 41st GEF Congress paper"), expanded at l.1283. Fix l.1279: "The 41st congress paper of the Spanish Fracture Group (GEF)".
   - "IEC TC 82" (l.1112). Fix: "IEC technical committee TC 82 (solar photovoltaic energy systems)".
   - "CO2-eq" (l.839). Fix: "CO₂-eq".

19. Minor (unsourced items in a sourced list). Section 4.3, l.452: "with the full 1 MW reported in testing in October 2026" names no source, while every other figure in the paragraph does; l.473: "Swimsol … the largest 2.4 MW (April 2026)" gives a date without an outlet. Fix: add the outlet in each, as in the other bullets.

20. Minor (stand-alone; r2#29 partly fixed). l.173: "the values the WP8 lead recorded in its KPI tracker; the earliest version of the tracker in the project records is that of 29 September 2026". The reader does not have the tracker. Fix: "For these the table gives reference values that the WP8 lead set in its internal KPI record; the earliest version of that record is of 29 September 2026, after most of the activities."

21. Minor (confusing record note). l.886: "On 19 November 2026 the cost-model record held the earlier version of November 2025, which belongs to D7.4 version 1.0; D7.4 version 2.0 states that cost model version 3 is published as a new version of the same record." The reader cannot tell whether version 3 is public. Fix in A.23 (l.1489), and delete the sentence in l.886: "D7.4 version 2.0 refers to cost model version 3 as a new version of the cost-model record. On 19 November 2026 the D7.4 report and cost-model records still held the version 1.0 report and the cost model of November 2025."

## C. Wording

22. Wording. l.157: "Each result-generating partner identified its results and informed the work package leader (D1.8)". "work package leader" is undefined and differs from "WP8 lead" everywhere else. Fix: "informed the leader of its work package (D1.8)", or "informed the WP8 lead", whichever D1.8 says.

23. Wording. l.365: "a change it links to the change of hinge system, and this changes the number of panels, the array layout and the installed power". Fix: "D7.4 links this to the new hinge system. The larger panels change the number of panels, the array layout and the installed power."

24. Wording. l.593: "… at three steps: design and qualification (IFE …, SINTEF and MARIN for tests, DNV for the design basis), assembly, where the breakwater classes come from Clement Germany from the first site that needs one, targeted about 2030, and operation, with Ceit's monitoring as an option for larger plants." The list items have different shapes and the second runs on. Fix: "… at three steps: in design and qualification, IFE for structural simulation, SINTEF and MARIN for tests and DNV for the design basis; in assembly, Clement Germany with the breakwater classes, from the first site that needs one (targeted about 2030); and in operation, Ceit with monitoring as an option for larger plants."

25. Wording. l.601: "cast with pilot moulds in the months after the first winter inspection". The inspection is not introduced. Fix: "cast with pilot moulds after the first reference plant's first winter inspection (decision gate 3, Section 4.7)".

26. Wording. "in-house moulds" (l.600), "in-house 3D-printed moulds" (l.789), "Parallel casting routes (in-house moulds and a vendor)" (l.792). After l.441 ("wound down the factory and moved to subcontracted production") and l.553 ("Production is subcontracted: Sunlit Sea … owns the moulds"), "in-house" reads as Sunlit Sea casting itself. Fix: "moulds owned by Sunlit Sea" / "Sunlit Sea's own 3D-printed pilot moulds" / "Parallel casting routes (Sunlit Sea's pilot moulds at a casting partner, and a vendor's tooling)".

27. Wording. l.1090: "Sunlit Sea's earlier patent concerns the sandwich construction of the Generation 1 float, the square aluminium float joined by polyurethane hinges (Section 4.1), which Generation 2 does not use." "which" can refer to the float, the hinges or the construction. Fix: "… concerns the sandwich construction of the Generation 1 float (Section 4.1). Generation 2 does not use that construction."

28. Wording. l.1267: "The breakwater classes follow at inland and inner waters". Fix: "at inland lakes and inner waters" (as l.693).

29. Wording. l.371: "It gives the 50-year significant wave heights of the use-case basis D2.1 (4.4, 7.0 and 12.3 m); this plan uses the design sea states of MARIN's D5.1." The reader cannot compare. Fix: "…; this plan uses the design sea states of MARIN's D5.1 (4.0, 6.5 and 11 m; D5)."

30. Wording. Number style. "the project has 10 papers" (l.36) against "ten publications" (l.173, 346, 1279); "nineteen risks" (l.338, 1047) against "26 risks" (l.777) and "27 results". Fix: numerals from 10 up, words for one to nine: "10 publications", "19 risks".

31. Wording. Quarters written two ways: "Q1 2027" (most places) against "the first quarter of 2027" (l.752, 1063, 1184, 1185, 1186, 1209) and "by the end of the third quarter of 2027" (l.1063, 1185). Fix: "Q1 2027", "by the end of Q3 2027" throughout.

32. Wording. l.233: "are open on the open repository Zenodo". Fix: "are openly available on Zenodo".

33. Wording. l.294 and l.338: "Integrated life-cycle sustainability assessment of the SUREWAVE system (D7.6), led by IFEU with its integrated life-cycle sustainability assessment (ILCSA) method". The term appears twice in one phrase. Fix: "Integrated life-cycle sustainability assessment of the SUREWAVE system (D7.6), led by IFEU with its ILCSA method (integrated life-cycle sustainability assessment; IFEU background)".

34. Wording. Paragraphs and cells still too long for a non-native reader or a portrait Word page (r2#30 and r2#42 partly fixed): l.1001 (MARIN's DIFFRAC bullet, 1,916 characters), l.173 (1,763), l.1267 (conclusions, 1,760), l.216 (1,707), l.693 (1,626), l.1024 (1,591), l.886 (1,533); cells l.328 (886) and l.242 (877). Fix: split l.1001 into three paragraphs (scale-up and the 2 MWp paper; validation against the Stadt Towing Tank tests; ReFRESCO and the linear methods); split l.173 after "(none; SINTEF's news article of 1 November 2022 announced the start)." and after "the status is that of 23 November 2026."; split l.1267 after "as the field record and the cost base allow." and after "(Section 4.6)."; in l.242 move the EIC sentence to the text below the table.

35. Wording. l.36 and l.173 state the publications exception in two forms ("more than 10 in the Grant Agreement; the project has 10 papers, 7 of them with stated peer review" against "ten publications against the Grant Agreement's more than ten, seven of them with stated peer review"). Fix: one wording in both: "10 publications against the Grant Agreement's more than 10, 7 of them with stated peer review".

36. Wording. l.1318: the Floating Solar in Europe 2025 row gives "14 February 2025" and "MARIN reports an oral presentation on 13 February"; A.5 (l.1339) gives 14 February. Fix: in A.4 write "13–14 February 2025" if the event ran over two days (check the organiser's agenda), or say in one clause which date the organiser's agenda gives for the talk.

## D. Earlier rejections in my area: does the rejection hold?

- r2disp_D, r2_writing#2 (2030–2031 revenue gives a price per watt; D41 keeps it): holds as an owner decision, but it is not sufficient. Item 2 shows a second, independent route (10 MW-class sensitivity and kit-volume sensitivity with the 40–50 % margin target), so the owner question must cover the sensitivities as well.
- r2disp_D, r2_writing#3 (site types in 4.7): holds for 4.7 under the owner decision; the 4.4 table combined with the EIC proposal's site names is item 4.
- r2disp_C, r2_writing#4 (€0.10/kWh in 4.6.2): holds (low risk); see item 5 for the scale-up path that the table repeats.
- r2disp_D, r2_writing#7 (EDP R&D / CNET): holds; the proposal uses that name (EIC l.26).
- r2disp_A, r2_cold#6 (move criteria between 2.4 and 3.3): holds; 2.4 states the criteria and 3.3 applies them, which reads correctly now.
- r2disp_E, r2_cold#5 (Section 13 lists as text): holds.
- r1disp_A, r1_cold#59 (glossary): holds, provided the terms in item 18 are defined at first use.
- r1disp_D, r1_writing#3 and #6: hold (see the first bullet; EDP is a co-applicant, not a customer).
- disp_D, writing 22 ("a site that would otherwise be closed to floating PV"): holds; one occurrence (l.756).
- disp_D, writing 24 and 25: hold (EBITDA and EPC expanded at first use, l.25 and l.32; cover "Coordinator: SINTEF", D1rr).
- r1disp_B, #61 (annex move): superseded by D40; done (Annex A).

## E. Earlier findings in my area still not fixed

- r2#2 (2030–2031 revenue and margin give a price and cost per watt): open, owner question; widened by item 2.
- r2#3 (pipeline detail): fixed in 4.3.1 (l.488); open in 4.4, 4.4.1 and 4.7 (item 4).
- r2#4 (€0.10/kWh): open, owner question (item 5).
- r2#19 (gate 3 date): partly fixed (item 13).
- r2#20 and r1#32 (repetition): open (item 14).
- r2#29 (KPI tracker): partly fixed (item 20).
- r2#30 and r2#42 (long cells and sentences): partly fixed (item 34).
- r2#34 (D8.3 reviews after issue): partly fixed (item 12).
- All other round 2 writing items (1, 5, 7–18, 21–28, 31–33, 35–41, 43–58) are fixed in the current text.

Findings: 3 major, 18 minor, 15 wording.
