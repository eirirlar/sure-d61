# T150 round 2: editor and confidentiality review of d84_merged.md

Persona: editor and confidentiality reviewer. Scope: requirement 7 and CLAUDE.md "Language and tone", read sentence by sentence; terminology, units, numbers, headings and numbering, repetition, non-native readability, tables; confidentiality checked against the financial plan (surewave/deliverables/2026-11-22_surewave_hrb_financial_plan_ker1.md, "FP") and docs/project_facts.md ("PF"). Line numbers refer to d84_merged.md (1,420 lines, read end to end). Decisions D1–D34 and the Round 1 revisions are applied; only errors inside them are reported.

Mechanical checks run:
- No `**` in the file (0 hits).
- Emphasis words and connectives: no "precisely", "crucially", "clearly", "therefore", "thus", "which is why", "it follows", "well beyond". "already" occurs once (l.923, "capacity already installed", literal, fine). "very" occurs only in the expert's quoted ratings (l.141) and in "a very low land-use footprint" (l.697, see item 40).
- All 47 tables have the same column count in every row, a valid separator row and a blank line after the table.
- Counts checked against their own lists: partner results 3+6+1+3+6+2+6 = 27; 23 in KERs + 4 impact; KER table rows 4+3+4+5+4+2+1 = 23; conferences 14 (Ceit 4, IFEU 4, MARIN 3, Sunlit Sea 2, SINTEF 1; 7 + 2 + 2 + 3); presentations 15; posters 3; web events 4; joint events 3; workshops 3; articles 8 (5 + 3); interviews 9; videos 7; infographics 5; factsheets 3; Zenodo 6+4+2+2+2+1+1 = 18 and 12 + 1 + 1 + 4 = 18; WP8-set targets 5; reach "8 distinct events" 4+3+1; media mentions 8+1+4 = 13; volume split 3.6 + 4.1 + 20 = 27.7 MWp (13/15/72 %); €9.75M / 10,375 kWp = €940/kWp; CAPEX −40 %, OPEX −31 %; €212/kWp ≈ 23 % of €940; 16 MWp ≈ 3–4 % of 0.44–0.5 GW; 25 years at one wave a second = 7.89 × 10⁸; NOK conversions at 11.7 (74–82 øre → €0.063–0.070; 24–47 øre → €0.021–0.040); 51 months; final periodic report 1 March 2027. All correct.
- Round 1 writing findings now fixed in the text: 1, 2 (4.6.2 basis and lengths), 7, 8, 9, 10, 11, 13, 14, 15, 17, 20, 21, 25, 27, 28, 30, 33–46, 49, 50, 51, 52, 53, 55, 56, 57, 59, 60. Still open or only partly fixed: 3 (see items 1–2), 5 (item 3), 24 (item 15), 26 (item 16), 29 (item 18), 31/32 (item 20), 54 (item 27), 58 (item 30).

## A. Confidentiality

1. Major. Section 4.7, EIC scenario, lines 907, 913–914, 918, 922: "a first commercial plant of 1 MWp from the kit at the demonstrator site in 2031"; table: Base revenue 2031 €8.2M, EBITDA €1.9M; EIC €8.7M, €2.1M; "The EIC and EU-upside cases have a higher 2031 revenue and EBITDA because of the first commercial plant at the demonstrator site"; "adds about €0.2M to 2031 EBITDA". The difference between the two rows is one named-size kit delivery: €0.5M of revenue and €0.2M of EBITDA for 1 MWp. Any reader gets about €0.50 per watt for kit plus engineering and about €0.25–0.30 per watt for the kit cost. FP lines 283–286 give €0.47/W kit and 4 % engineering of a €0.83/W plant (€0.033/W), so €0.50/W; PF line 37 gives the production cost €0.25/W and the kit price €500/kWp and says "Never in external copy". This is the clearest price-per-watt leak left in the draft, and Clement Germany, ACCIONA and the other partners are potential suppliers (Section 2.3, l.143). Fix:
   - l.907: "EIC: the base case plus the EIC Transition project for the exposed-site version of KER1 (Section 10), with a Sunlit Sea share of about €0.75M over 2027–2030, and a first commercial plant from the kit at the demonstrator site after the project."
   - Scenario table: delete the columns "Revenue 2031" and "EBITDA 2031"; keep "Net result, total 2027–2031" and "Lowest year-end cash (year)".
   - l.918: "Grant income is not counted as revenue. The EIC and EU-upside cases also include the first commercial plant at the demonstrator site."
   - l.922: delete "In the EIC case, the first commercial plant at the demonstrator site, modelled in 2031 as the first full year after the project, adds about €0.2M to 2031 EBITDA."
   The EU-upside "1 MWp kit delivery in 2029" (l.908) has the same effect on 2029 if a 2029 figure is ever added; keep 2029 out of any per-scenario table.

2. Major (error inside an owner decision; rejection r1_writing#3 holds only narrowly). Section 4.7 first table (l.890–894) and lines 896, 893, 913: revenue 2030–2031 €12.1–12.6M for about 7 + 16 = 23 MWp delivered gives €0.53–0.55 per watt; 2031 revenue €8.2M for about 16 MWp gives €0.51 per watt; the 2030–2031 gross margin of 41–44 % "as kit sales dominate" then gives a cost of about €0.29–0.31 per watt. FP: kit plus engineering €0.50/W (l.283–286), delivered cost €0.24–0.28/W (l.284, 292). The estimate lands within about 10 % of both confidential figures. The r1 disposition rejected the column change because the first table gives the same information; that is correct, and it shows the leak sits in the combination the owner decision allows (period revenue + period volumes + period margin). Owner question with a recommendation: keep the volumes (D9), the margin level and EBITDA; remove the per-period revenue for 2030–2031. Ready text for the first table: "| Revenue | €3.2–3.6M in total, mainly the first EPC delivery in 2028 | Grows with kit volume; mainly kit sales and site engineering |". With item 1 applied, the 2031 revenue column goes as well. Kit-volume sensitivity (l.934, "Kit volume 30 % lower in 2030–2031 moves 2031 EBITDA by about €0.9M") gives a gross profit near €0.2M per MWp; with the revenue removed it no longer gives a price. If the owner keeps the revenue figures, the plan accepts that partners can estimate the kit price per watt; say so in the owner question.

3. Minor. Pipeline detail still lets SINTEF and Clement Germany (who have the EIC proposal, generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md l.64) and anyone with Norwegian press access identify the three Norwegian sites (PF l.45–47, 83–85): l.888 "three Norwegian reference sites (a harbour, an industrial basin and a lake)"; l.673 "one site holds a temporary permit, one has a state pre-project grant, grid capacity confirmed by the local grid company and its seabed mooring accepted by the environment agency, and one is being rezoned"; l.975 and M9 (l.991) "investment decision for the third reference plant, the second multi-megawatt plant, after rezoning"; l.777 "One local contractor on both larger Norwegian projects". The round-sized plant figures were removed (good). The owner may keep site types; the combination "industrial basin + state pre-project grant + seabed mooring accepted by the environment agency" is the identifying element (Gunneklevfjorden, PF l.46, 83, 85). Fix for l.673: "Three Norwegian hosts have committed time to permits and site studies; their permits, grid capacity and investment support are at different stages." Keep l.888 as is or write "three Norwegian reference sites of different types".

4. Minor. Section 4.6.2, l.882: "With the breakwater half carried by other uses, it produces power at about €0.10/kWh (financial plan)", next to the table share "about 15 %" for 1 MWp. With a public PVGIS yield and D7.4's opex and financing assumptions, a reader can back out a plant capex of roughly €0.9–1.0 per watt and from the 15 % share a PV plant of about €0.8 per watt (FP l.316–321: €0.83/W, €0.97/W with breakwater, LCOE 0.099). The financing terms are not in D8.4, so the estimate is loose. Low risk; acceptable if the owner accepts it. Do not add the yield or the discount rate of the worked example.

5. Wording. Supplier locations: l.775 "prototypes are cast by one supplier in China", l.958 "prototypes are cast in China", l.781 and l.958 "a module-integration and kit-packing partner in Lithuania". The supplier is not named, but in a document read by potential competing suppliers the sourcing country plus "one supplier" is commercial detail (PF l.37, 87, 89). Optional fix: "prototypes are cast by a single vendor outside Europe" and "a module-integration and kit-packing partner in the Baltic region".

6. No finding (record of what was checked). Checked and acceptable under the owner decision: the EIC host (an inland lake in Germany, letter of intent of 8 September 2026, lapsing on 28 February 2027; l.861, 1111, 1118, 1308, 1403) is not named; the Gen 1 references (60 kWp in Germany, 105 kWp in Norway, l.626) carry no customer names; the EUPI-PV sites are given by country only (l.1309); the wavebreaker sensitivity (€0.1M) and the breakwater sensitivity (€0.9M at the two larger sites) cannot be turned into a per-watt figure because the site sizes are no longer given. The €0.83 per watt, the cost per metre, the mobilisation sum and the breakwater lengths are gone from 4.6.2 (D21 applied).

7. Wording. Rejection r1_writing#6 (EDP, l.218, 1308) holds. EDP is a co-applicant in the EIC proposal (proposal l.26), D14 asks for the proposal's partners, and EDP is not a Sunlit Sea customer. One addition: "EDP R&D / CNET" is unexplained for a reader; write "EDP (its research centre EDP NEW R&D, Portugal)" if that is the proposal's name for the entity, or "EDP (Portugal)".

## B. Consistency inside D8.4 and with the sources

8. Minor. Section 6.3, l.1102: "the selected breakwater lets through at most about 40 % of the incident wave height at the wave periods of 1–3 s that are critical for the array" (D3.2). The r1 disposition of r1_owner#19 rejected this figure because it is not in the D3.2 text, only in its figures (OWNER QUESTION 7); the r1disp_E disposition of r1_partners#C2 then added it. The two dispositions conflict. A grep of surewave/background/2023-08-08_surewave_d3.2_floating_breakwater_design.md finds the transmission coefficients only in Figures 37–42 (l.713–745). Fix: either cite "D3.2, Figures 37–42" so a reader can check it, or cut the clause until owner question 7 is answered.

9. Minor. Section 6.3, l.1102: "The design analysis limited the unit weight to about 120 t", against l.610 "about 123 t" for the same unit. D3.2 l.428 sets "approx. 120 tons" as the upper limit for the analysis; the unit itself is 123.39 t (D3.2 l.1715). Fix: "The design analysis set an upper unit weight of about 120 t, which mobile cranes can still handle; the selected unit weighs about 123 t (D3.2)."

10. Minor. Rejection r1_partners#A5 in r1disp_A ("0.4–0.9 × 10⁻¹² ... REJECTED – D22", "26 formulations" FTR only) does not hold. D4.2 Table 5 and Table 7 give D_Cl 0.4–0.9 × 10⁻¹² m²/s (surewave/background/2024-07-31_surewave_d4.2_lab_testing_breakwater_prototype.md l.470–495, 978: "extremely high water and chloride resistance"), and D4.1 l.607 gives "Twenty-six different trial mixes". The text (l.1075, 1079) follows the correct r1disp_E disposition; only the rejection record is wrong. No change to D8.4.

11. Minor. Section 3.4 R3 evidence, l.526: "a crystalline admixture cut the mean water penetration of the LWAC from 8.2 mm to 0.6 mm". D4.2 Table 7 has four LWAC variants; the 8.2 → 0.6 mm is LWAC-CEM III, and for LWAC-CEM I the admixture raised it from 1.1 to 1.3 mm. Section 6.2 (l.1079) says "of one LWAC". Fix in 3.4: "of one LWAC variant (CEM III cement) from 8.2 mm to 0.6 mm (D4.2)".

12. Minor. Section 3.2 KER2 result, l.485: "low-carbon cement" stated as a property, while 6.2 (l.1076) writes "a cement that ACCIONA describes as low-carbon", and D24 bars a greenhouse-gas or "lower footprint" claim. Fix in 3.2: "a cement that ACCIONA describes as low-carbon".

13. Minor. Hinge numbering, l.577: "D7.6 numbers the short hinge at the float corners as the second generation and the full-edge hinge as the third; SINTEF's test reports call the hinge tested before the redesign the first generation." The reader cannot tell whether SINTEF's "first generation" (3.69 kN, l.579) is the same hinge as D7.6's "second generation" (14 kN, l.583) or an earlier one. D7.6 l.159 and l.689 call the earlier design "v2" and the new one "v3"; D6.3 l.261 calls the hinge before the redesign "the first generation of the connections". Fix: state the mapping in one sentence, e.g. "SINTEF's 'first generation' is the hinge that D7.6 calls the second generation (v2)", if Sunlit Sea confirms it; otherwise "The two numberings are independent: SINTEF counts from the hinge it first tested, D7.6 from the first design of the project." Without this, the three figures in the list below cannot be compared.

14. Minor. l.583, definition: "The design break load (ultimate limit state, the load at which the part is designed to break)". The ultimate limit state is the limit state, not a load, and a part is not designed to break. Fix: "The design break load at the ultimate limit state (the highest load the part is designed to carry) of the full-width third-generation hinge is 37 kN".

15. Minor. Units MW vs MWp. l.562 says "this plan writes MWp for the plants it assesses", but l.265 ("Paper on the hydrodynamics of a 2 MW offshore floating solar farm") and l.286 ("Hydrodynamics of a 2 MW offshore floating solar farm") describe the same 2 MWp farm that l.488, 529 and 1166 call "2 MWp". These are descriptions, not quoted titles. Fix: "2 MWp" in both cells. Quoted headlines and titles (l.235, 236, 355, 356) stay as published; legal and call thresholds (l.813 "below 10 MW", l.1309 "at least 5 MW") and other companies' plants (l.637, 657, 658) can stay as reported.

16. Wording. Number format. Prose uses "€7.3 million" (l.30), "€5.5 million" (l.32, 512, 1414) and also "€5.5M" (l.921, prose), "€0.75M" (l.907, prose), "€2.5M" (l.1308). Fix: one form throughout. Recommended: "€5.5M" everywhere, tables and prose, since 4.7 uses that form in about 30 places.

17. Wording. Same figure, two roundings: "About €9.8M for the 10.4 MWp installed" (l.850) and "about €9.75M for the 10 MWp-class Mediterranean plant" (l.1005). Fix: "about €9.75M" in both (it reproduces €940/kWp), or "about €9.8M" in both.

18. Wording. "Clement" in tables: l.1117 "Clement's engineering processes" (table cell). Running text in 6.3 is fine after "Clement Germany" is introduced. Fix in the table: "Clement Germany's engineering processes".

19. Wording. Terminology drift:
   - "WP8 leader" (l.1062) against "WP8 lead" everywhere else. Fix: "WP8 lead".
   - "10 degrees" (l.1135) against "10°" (l.487). Fix: "10°".
   - "digital image correlation" (l.387) against "Digital Image Correlation" (8 places). Fix: one form; lower case is the usual form for a method ("digital image correlation (DIC)").
   - "integrated life cycle sustainability assessment" (l.1210) against "life-cycle" elsewhere. Fix: "integrated life-cycle sustainability assessment (ILCSA)".
   - "ring breakwater 346 m across" (l.524) against "346 m diameter" (l.562, 999). Fix: "346 m across" in all three, matching "173 m across".
   - "technical risk assessment" (l.568, "D7.6's technical risk assessment") against "technological risk assessment (D7.2, SINTEF)" (l.490, 534, 1131, 1210). Fix: "the technological risk assessment of the system with the redesigned hinge (D7.2, used in D7.6)", if that is what D7.6 rests on.
   - "the customer buys it directly" (l.1029) against D6's "the plant owner buys the breakwater" (l.25, 728, 925, 1021); the order of the three routes also differs from l.1021. Fix: "Per project, by one of three routes: the plant owner buys the breakwater; Sunlit Sea buys it and delivers the full system as EPC contractor; or Clement Germany leads with Sunlit Sea as floating PV subcontractor".
   - "first half of 2028" (gate 3, l.941) against "Q2 2028" (l.804, M7 l.989, 974). Fix: "Q2 2028".
   - "the DNV floating solar documents (DNV, May 2026)" (l.787) and "the DNV floating solar standards of 2026" (l.820); DNV-RP-0584 is a recommended practice. Fix l.820: "The DNV floating solar standards and recommended practice of 2026".

20. Wording. Repetition with no new information (r1 item 32 not applied). Each statement below is repeated in full:
   - "SuRE grew out of contacts made through the Stakeholder Advisory Board": l.38, 331, 1062, 1302.
   - "The plant owner buys the breakwater. Where Sunlit Sea delivers the full system as EPC contractor, it buys the breakwater and includes it in the EPC price": l.25, 728, 925, 1021, plus 1029.
   - The Q1 2027 access-rights request to SINTEF and MARIN "before the design freeze": l.799, 967, 973, 1017, 1025, 1283, 1331, 1332, 1356, 1387, 1403.
   - "KER1 integrates Clement Germany's breakwater, transition element, mooring and anchoring (KER3) with Sunlit Sea's array" (l.560) directly after the bullet list that says the same (l.552–558). D29 asks for the statement where KER1 is described, not twice in a row.
   - "The value propositions for KERs 2–7 are those stated by their owners" (l.680, 1042).
   Fix: keep the full statement in its home section (SuRE: 2.5.10 and Section 10; breakwater buyer: 4.4 and Section 5; access rights: Section 9; value propositions: Section 6) and replace the others by a short reference, e.g. "(Section 9)". Delete l.560.

21. Wording. l.17 and l.1412 state the TRL position differently: "This plan uses TRL 4–5 for the integrated system and TRL 4–5 for Sunlit Sea's CONNECT platform" against "This plan uses TRL 4–5 for the integrated system and for the CONNECT platform". D20 asks for the same wording. Fix l.17: "This plan uses TRL 4–5 for the integrated system and for Sunlit Sea's CONNECT platform (Section 4.1)."

22. Minor. Section 4.1 table, l.592 (directional breakwater row, Status): "TRL 4 as the starting point of the EIC Transition proposal". In a row about the directional configuration alone this reads as the EIC TRL 4 applying only to that configuration, which D2r forbids, and it differs from the TRL 4–5 used for the integrated system. Fix: "directional layout not yet tested; integrated system at TRL 4–5 (Section 4.1)".

23. Minor. Reach table, l.214: "more than 12,000 in 2024, within the more than 50,000 recorded by the end of that year". With about 800 visits recorded up to March 2024 and tracking from late August 2023, at least about 49,000 of the more than 50,000 fall in 2024. "More than 12,000" is true but understates the record (requirement 4) and reads as a contradiction. Fix: "About 800 visits from late August 2023, when tracking started, to March 2024; more than 49,000 in 2024, of the more than 50,000 recorded by the end of that year; 2025 and 2026 not measured after tracking stopped".

24. Minor. Section 2.5.10, l.326: "D2.4 names six member organisations, most with several roles". The list that follows gives several roles to two of the six (the chair and one developer). Fix: "D2.4 names six member organisations, two of them with several roles:".

25. Minor. Section 3.2 KER4, l.487: "breakwater-to-array connections 40.9 kN against a 42 kN design requirement" does not say that the mean fell short; 6.4 (l.1139) gives 40.88 kN and that the last two specimens exceeded the requirement. Fix: "breakwater-to-array connections 40.9 kN mean, below the 42 kN design requirement; the two specimens with a protected bracket–rope interface exceeded it". Use 40.9 kN in both places.

26. Minor. Section 4.8, l.946: the zone rule covers feasibility above 5 and exactly 5, but not below 5. The reader cannot place a risk with low feasibility (requirement 5). Fix: add "; a feasibility below 5 places a risk in the [name the Booster zone, e.g. 'monitor'] zone. No KER1 risk has a feasibility below 5." (check the risk map, surewave/deliverables/2026-11-11_surewave_hrb_risk_assessment_ker1.md, for the zone name and the last claim).

27. Wording. Presentations table, l.285 and l.291: the presenter cell is "Ceit" and "IFEU" where every other row names a person (r1 item 54). Fix: name the presenters (2.5.1 lists the Ceit authors of the 41st GEF paper; IFEU's EU PVSEC presenter is in IFEU's input), or write "Ceit (presenter not recorded)".

28. Wording. Table cells that do not match their column:
   - Videos, l.388–389, column "Producer": "Published by Sunlit Sea". Fix: "SUREWAVE (recorded and published by Sunlit Sea)", or rename the column "Producer or publisher".
   - Overview table, l.187, column "Contributors": "Ceit, SINTEF; project website". The website is a channel, not a contributor. Fix: name who made the three cards, or "Ceit, SINTEF, and the authors of the website cards".
   - l.180, Status: "Met for D8.5; not met for the GA", while the other rows state the GA result first and the headline counts it as an exception. Fix: "Not met (GA); met (D8.5)".
   - l.193–194, Achieved: "more than 25", "more than 50,000" against "More than …" in the Target column. Fix: capitalise, "More than 25", "More than 50,000".

29. Wording. Stand-alone references to records the reader does not have: "project tracker" (l.209, 215, 314), "MARIN's report" (l.215, 288, 306, 313), "the project's interim report for April to October 2024" (l.569). The reader has neither the KPI tracker nor MARIN's internal reply. Fix: "(project records)" for the tracker; "(as reported by MARIN)" for MARIN's report; for l.569, "Its evidence is the project's progress up to October 2024: the first MARIN campaign, …" (the list of evidence stays).

30. Minor. Very long table cells that will not read in a portrait Word page: 3.4 R1 Evidence (l.524, about 1,690 characters), 3.2 KER2/KER5/KER6 rows (l.485, 488, 489, up to 1,450), Section 10 EIC row (l.1308, about 1,450), Timeline 2027 row (l.1403, about 1,270). Fix: in 3.4 R1, move the basin-test and hinge evidence into a short paragraph under the table and leave "Basin tests (D6.2, D8.3; Energies 17(9) 2059); hinge tests (D6.1, D6.3; Section 4.1); D7.4 version 2.0" in the cell; in Section 10, move the EIC demonstrator details (letter of intent, month 22, DNV statement, lump sum) into a paragraph below the table. Check the rendered docx.

31. Wording. Section 6 intro, l.1044: "proposes a target for each indicator in Section 13". The Section 13 table gives one set of targets per KER, not a target per indicator. Fix: "and proposes targets for each KER in Section 13".

32. Wording. Section 3.3 KER5, l.504: "Part of R5, and R6, exploited by MARIN and SINTEF" reads as if SINTEF also exploits R6. Fix: "Part of R5 (MARIN and SINTEF) and R6 (MARIN)".

33. Wording. Section 4.9, 2030 bullet (l.976) ends with a 2031 event: "modelled in the financial plan in 2031". Fix: move the sentence to a line after the bullets, "A first commercial installation with a breakwater class, of 1–5 MWp, is targeted in the EIC Transition proposal after the project; the financial plan models it in 2031 (Section 4.6.2)."

34. Wording. Section 2.5.20, l.420: "submitted on 18 November 2026 … On 18 November 2026 Clement Germany sent review comments … and seven CAD drawings as input for four figures." The reader cannot tell whether the comments and drawings are in the submitted D8.3. Fix: add "which were [included in / not included in] the submitted version".

35. Wording. Abbreviations used before or without expansion (the r1_cold#59 rejection of a glossary holds only if every term is defined at first use; these are not):
   - HPC, LWAC, CLC: first used l.454 ("ACCIONA's HPC, LWAC and CLC"), expanded only at l.485. Fix l.454: "(ACCIONA's high-performance concrete (HPC), lightweight aggregate concrete (LWAC) and cellular lightweight concrete (CLC))".
   - CFD: first use l.486, never expanded. Fix: "computational fluid dynamics (CFD)".
   - NPV, IRR: spelled out in l.30 without the abbreviation, then used as NPV/IRR from l.833. Fix l.30: "an internal rate of return (IRR) of 15.6 % and a net present value (NPV) of €7.3M".
   - CAPEX, OPEX: l.1005, not expanded. Fix: "Investment (CAPEX)", "operating cost (OPEX)" at first use.
   - EERA, EU PVSEC: l.200, 268, not expanded. Fix at first use: "EERA DeepWind (the European Energy Research Alliance's offshore wind conference)", "EU PVSEC (the European Photovoltaic Solar Energy Conference)".
   - "Keller et al. 2015" (l.1210, 1255): a short citation with no reference list. Fix: give the full reference once (authors, title, journal, year) or write "IFEU's published ILCSA method (2015)".

36. Wording. Section 2.5.24, l.441: "The floating solar and offshore communities at Intersolar, Floating Solar in Europe, MARINE and DeepWind are the buyers and partners for KER1 …". The audiences contain potential buyers; the sentence states them as buyers. Fix: "include the potential buyers and partners of KER1 …".

37. Wording. l.139: "In the November files the first market became sheltered coastal sites, and the product the Generation 2 CONNECT platform described in Section 4.1." "the November files" is internal shorthand, and PF l.29 keeps the generation label out of the product name. Fix: "In the November outputs the first market became sheltered coastal sites, and the product the CONNECT platform (Generation 2) described in Section 4.1."

## C. Sentences a non-native reader will stumble on

38. Wording. l.17: "The EIC Transition proposal of September 2026, which takes the protected floating PV system to a demonstrator (EIC Transition is the European Innovation Council's scheme for taking research results towards market), sets TRL 4 as its starting point." Two insertions break the sentence. Fix: "EIC Transition is the European Innovation Council's scheme for taking research results towards the market. The EIC Transition proposal of September 2026 takes the protected floating PV system to a demonstrator and sets TRL 4 as its starting point." Also in the same paragraph: "on the wave-basin tests" → "based on the wave-basin tests".

39. Wording. l.141: "the expert judged the files of very high quality". Fix: "the expert judged the files to be of very high quality".

40. Wording. l.697: "Its impacts are higher than those of land-based PV or wind power." "Its" has no clear antecedent after "every scenario". "a very low land-use footprint" is D7.6's wording only if D7.6 says "very". Fix: "The plant's impacts are higher than those of land-based PV or wind power." and "has a low land-use footprint" unless D7.6 says "very low".

41. Wording. l.196: "Webinars count as web events, except the two workshops hosted by SUREWAVE, the joint NaturSea-PV webinar and the final workshop, which count as conference workshops." It reads as four items. Fix: "Webinars count as web events, except two that SUREWAVE hosted as workshops, the joint NaturSea-PV webinar and the final workshop; these count as conference workshops."

42. Wording. l.198 (93 words), l.434 (106 words), l.839 (86 words), l.1212 (91 words): one sentence each. Fix: turn l.198 into a list ("Items counted under more than one indicator:" followed by one bullet per item); split l.434 after the counts ("They are twelve deliverable reports (…). The others are …"); split l.839 into "Version 2.0 answers the request for revision of 16 October 2026. It adds the clean-up of the site at the end of life. Its rebuilt cost model, checked against a separate implementation with automated tests, corrects these errors of version 1.0: …"; split l.1212 at each semicolon into short sentences.

43. Wording. l.462: "because both serve the same customers for hydrodynamic design services". "Both" can mean the two SINTEF models or SINTEF and MARIN. Fix: "because SINTEF's and MARIN's hydrodynamic modelling serve the same customers for hydrodynamic design services".

44. Wording. l.573: "Neither the breakwater classes … nor a directional layout … have been tested." Fix: "has been tested", or "The breakwater classes … and a directional layout … have not been tested."

45. Wording. l.603: "All waves at most 0.6 m for the platform for sheltered sites and 0.8 m for the exposed-site version under development." The sentence has no verb. Fix: "All waves together are limited to 0.6 m significant height for the platform for sheltered sites and to 0.8 m for the exposed-site version under development."

46. Wording. l.626: "It has built two Generation 1 plants in its own factory" (plants are not built in a factory) and "which has sold its power under a power purchase agreement since 2024, to October 2026". Fix: "It has built two Generation 1 plants, with floats from its own factory: … and its own 105 kWp plant in Norway, which sold its power under a power purchase agreement from 2024 to October 2026."

47. Wording. l.783: "Delivery earns a thin margin for the most risk, so the EPC role is limited …". Fix (without a conclusion connective): "Delivery earns a thin margin and carries the most risk. Sunlit Sea limits the EPC role to the three Norwegian reference plants and passes it to developers in phase 2."

48. Wording. l.845: "Its business case rests on D7.4 and is held until the exposed-site field record exists." "is held" is unclear. Fix: "Its business case rests on D7.4. Sunlit Sea pursues it once the exposed-site field record exists."

49. Wording. l.861: "The first breakwater protection in operation will be the small wavebreakers at the first reference plant, a Norwegian port, in 2027, on the side exposed to local wind waves." Fix (as applied in Section 5): "The first breakwater protection in operation will be the small wavebreakers at the first reference plant (a Norwegian port, 2027), on the side exposed to local wind waves."

50. Wording. l.868: "'Half carried by other uses' is an assumption." Fix: "The column 'half carried by other uses' assumes that the site owner's other uses of the breakwater carry half of its cost." And in the table (l.874) "about two thirds" sits among percentages; fix: "about 67 %".

51. Wording. l.886: "Sunlit Sea prepared the financial plan for KER1 as the annex of its Horizon Results Booster business plan; the financial plan was the annex Sunlit Sea chose at the Booster business-planning workshop of 13 November 2026." Fix: "Sunlit Sea prepared the financial plan for KER1 as the annex to its Horizon Results Booster business plan, the annex it chose at the business-planning workshop of 13 November 2026."

52. Wording. l.934: "a lower kit price or a higher kit cost of the size tested moves it by about €0.4M". The size is not given, so the clause does not help the reader; giving it would re-open item 1. Fix: "a lower kit price or a higher kit cost, within the range tested, moves it by about €0.4M".

53. Wording. l.1166: "and reducing the horizontal hinge loads by about a factor of 3 around a peak period of 4 s, by less than 50 % for the largest farm in the highest sea states." Fix: "… around a peak period of 4 s, and by less than 50 % for the largest farm in the highest sea states."

54. Wording. l.1170: "mooring assessment and improvement, a MARIN service for existing and new markets, to which the SUREWAVE results show that optimisation adds value". Fix: "mooring assessment and improvement, a MARIN service for existing and new markets; the SUREWAVE results show that optimisation adds value to it".

55. Wording. l.1187: "from up to 5–6 cm outside the concrete". The phrase is unclear (distance from the concrete surface, or concrete cover). Fix: use the wording of Sensors 24(13) 4211, e.g. "through a concrete cover of up to 5–6 cm" if that is what the paper reports.

56. Wording. l.1414: "and the reference plants come on time and perform as designed, with kit volume, including a first 10 MW-class supply contract by 2030, as planned." The last clause has no verb. Fix: "… the reference plants come on time and perform as designed, and kit volume, including a first 10 MW-class supply contract by 2030, comes as planned."

57. Wording. l.121: "The 27 results are the basis for Sections 3, 5, 6 and 7." The number appears without having been stated. Fix: "The 27 results in the table are the basis …".

58. Wording. l.38: "Projects that started before SUREWAVE or run alongside it use its results." MariSol and FlexiShape ended in 2025. Fix: "Projects that started before SUREWAVE or run alongside it have used or use its results."

## D. Rejected findings in my area: does the rejection hold?

- r1disp_D, r1_writing#3 (2031 revenue column): holds as to the proposed column change, which would not have closed the leak; the leak itself remains and is items 1–2 above.
- r1disp_D, r1_writing#6 (anonymise EDP): holds (item 7).
- r1disp_A, r1_cold#59 (glossary): holds, provided every term is defined at first use; item 35 lists the terms that are not.
- r1disp_B, #61 (move 2.5.1–2.5.24 to an annex): holds; section numbers are kept.
- r1disp_B, #9 (journalistic articles rule, option B): holds; the rule and its reason are stated in 2.5.12.
- r1disp_B, #F32 and #22; r1disp_C, r1_cinea#F32 and r1_owner#22 (correct D8.3): hold under D31; 4.1 (l.564) and 2.5.20 state the difference once each.
- r1disp_C, r1_facts#12 (NVE prices): holds; the euro conversion is correct at 11.7 NOK per euro.
- r1disp_C, r1_cold#65 and r1_facts#23 (bottom-plate material): hold; PF l.36 keeps the material out of external copy.
- disp_D, writing 22 ("otherwise be closed to floating PV"): holds; the phrase occurs once (l.925).
- disp_D, writing 24 (EBITDA, EPC expansion): holds; both are expanded in the executive summary (l.25, 32), and EPC again in the 4.4 table for readers who start there.
- disp_D, writing 25 (SINTEF AS): holds (D1).
- disp_A, A-w12 and A-w13: hold; they concern the companion exploitable results report, not D8.4.
- disp_B, B#78: holds; the URL issue is in the evidence file, not D8.4.
- r1disp_A, r1_owner#19 (0.4 transmission): the rejection and the current text disagree (item 8).
- r1disp_A, r1_partners#A5 (chloride coefficients, 26 mixes as FTR-only): does not hold; both are in D4.2 and D4.1 (item 10). The text is right.

Findings: 2 major, 16 minor, 39 wording.
