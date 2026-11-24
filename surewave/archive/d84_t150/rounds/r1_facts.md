# T150 round 1 — fact-check of d84_merged.md (persona: fact-checker)

Checked 23 November 2026 against the repo primary sources, the companion copies in scratchpad_t150\companions, live Crossref (citation counts re-fetched today), CORDIS and Prosjektbanken snapshots in scratchpad_t150\web, a live Prosjektbanken free-text search (FlexiShape), the live DNV news page of 23 June 2022 and the live EU PVSEC site. Both models were re-run: `scripts/hrb_financial_model.py --md` (PYTHONIOENCODING=utf-8) and `scripts/breakwater_classes.py`; the 45° lake table of 4.6.2 was recomputed with `breakwater_classes.coverage(kwp, 45, "light")`. Line numbers refer to d84_merged.md. Nearly every paragraph changed against d84_before_fix.md (627 of the non-blank lines), so the whole draft was treated as new text.

## Findings (numbered, with severity)

### Major

1. Major — 2.5 table row "Scientific publications | 10 | GA, D8.5 (peer-reviewed) | 10" (L146), 2.5.1 (L190–192), executive summary L38 "met or exceeded every ... target ... except one", 2.5 intro L142.
   What is wrong: the target is for peer-reviewed publications. GA Annex 1: "KPIs: >10 peer-reviewed publications" (GA L7389); D8.5: "Publish at least 10 peer-reviewed articles in scientific journals" (D8.5 L270) and "over 10 peer-reviewed research papers" (L561); proposal impact table: "10 peer-reviewed publications" (Annex 1 Part B L988). D8.4 itself says three of the ten are congress papers whose proceedings "do not state that the papers were peer reviewed" (L192). The final technical report counts "at least six published journal articles and three peer-reviewed conference papers" against the target of 10 (final report working copy L4462), i.e. 9. So the claim that the publications target is met, and the headline "except one: infographics", is OVERSTATED.
   Fix: in the table write Achieved "10 (6 journal papers, 1 peer-reviewed conference paper with DOI, 3 congress papers)" and add a status note; in L142 and L38 write: "SUREWAVE met or exceeded every target in the table of Section 2.5 except two: five of the six infographics, and peer-reviewed publications, where seven of the ten publications are peer reviewed (six journal papers and the MARINE 2025 paper) and the three congress papers do not state peer review. The two submitted SINTEF manuscripts would reach the target if accepted." If the owner keeps "10", the text must say the count relies on treating the three congress papers as peer reviewed, as the final technical report does.

2. Major — hinge test figures, 4.1 L516–520, 3.4 R1 L476, 6.1 L926 ("Between the second and third hinge generations, the ultimate-limit-state break load rose from 14 kN to 37 kN (design value, D7.6), and the tested average tensile capacity of the connection rose from 3.69 kN to 8.36 kN").
   What is wrong: (a) the two tensile values are not like for like. 3.69 kN is the mean ultimate tensile load of complete first-generation hinges (Preprints 202611.1612 abstract, crossref/10.20944_preprints202611.1612.v1.json). 8.36 kN is the mean for the new male–female connection tested as a 360 mm segment, "1/5th of the total real connection length", with a steel rod in place of the polypropylene rope (D6.3 L273, L447, L464); with the rope the same segment reached about 2 kN ("From 2kN to 8.36 kN", D6.3 L851). (b) Generation numbering conflicts: D6.3 calls the D6.1 hinge the "first generation" (D6.3 L261, L603, L673); D7.6 calls the corner hinge with 14 kN ULS "v2" and the full-edge hinge "v3" (D7.6 L687–689). 6.1 attaches the test values to the "second and third" generations, which no source does. (c) D7.6 states that "the robustness of these advanced hinges however could not be fully validated any more within the project" (D7.6 L1134), while the final technical report says the redesigned hinge was validated in the second basin campaign (final report L2953, L2998). The conflict is not flagged. (d) The 25-year fatigue result is conditional: with the steel rod the force in the polyurethane component must stay below 6.9 kN (D6.3 L841, L863).
   Fix (4.1 bullet 3): "In SINTEF's laboratory tests, complete first-generation hinges reached a mean tensile load of 3.69 kN and buckled at low compressive loads (Preprints 202611.1612). A 360 mm segment of the redesigned connection, one fifth of its full length, reached a mean tensile load of 8.36 kN with a steel rod in place of the rope (about 2 kN with the rope) and a mean compressive capacity of 20.23 kN (D6.3; final technical report). The fatigue assessment indicated compatibility with a 25-year service life if the force in the polyurethane component stays below about 6.9 kN (D6.3)." In 6.1 delete "between the second and third hinge generations ... and the tested average tensile capacity of the connection rose from 3.69 kN to 8.36 kN (final technical report)" and write "In D7.6, the design break load (ultimate limit state) rises from 14 kN for the corner hinge to 37 kN for the full-edge hinge; laboratory and basin results are in Section 4.1." In 3.4 R1 replace "raised from about 3.69 kN to 8.36 kN between hinge generations" with "3.69 kN for complete first-generation hinges and 8.36 kN for a one-fifth segment of the redesigned connection with a steel rod". Add one sentence in 4.1: "D7.6 notes that the redesigned hinges could not be fully validated within the project; the final technical report records no buckling or snap loading in the second basin campaign."

3. Major — 3.1 steps 2–3 (L411–412) and D11 wording "They were listed in a common input template sent to the partners on 29 September 2026 ... The partners described their results in written exploitation summaries in their own format rather than in the template fields".
   What is wrong: two of the seven summaries predate the template. ACCIONA uploaded its summary on 26 November 2025 (2025-11-26_acciona_exploitation_and_media_email.md L1–9) and Clement Germany's is dated 4 September 2026; the template is dated 30 September 2026 (deliverables/2026-09-30_surewave_partner_exploitation_input_template.md) and Ceit's reply refers to "Eirik Larsen's request of 2026-09-29" (Ceit summary L3). The text implies that every summary answered the template. A reader cannot reconstruct the sequence (requirement 5), and ACCIONA would object.
   Fix: "The WP8 lead listed seven candidate KERs in a common input template sent to the partners on 29 September 2026 (the template file is dated 30 September). ACCIONA had already submitted its summary on 26 November 2025 and Clement Germany on 4 September 2026; the other five replied between 30 September and 5 October 2026. None used the template fields; each described its results in its own format."

4. Major — Section 13, "Up to one year after the end of the action, to 31 December 2027: use the Horizon Results Platform to find interested parties for each result not exploited within that year" (L1180–1182).
   What is wrong: the one-year date is the trigger, not the end, of the Horizon Results Platform duty. GA Article 16: results "not exploited within one year after the end of the action" must be taken to the Platform (GA L8886–8888); the duty sits with the four-year exploitation obligation. Decision D17 lists "Horizon Results Platform rule per result" under four years. As written, the reader concludes the duty ends on 31 December 2027.
   Fix: move the bullet to the four-year list and word it: "from 1 January 2028, for each result not exploited within one year after the end of the action, use the Horizon Results Platform to find interested parties, unless otherwise agreed in writing with the granting authority (Section 6.8)". Keep only the access-rights requests under "up to one year".

### Minor

5. Minor — 4.6.2 L741, 4.9 L848, Section 14 L1230, Section 10 L1138: "The EIC Transition proposal targets a first commercial installation of 1–5 MWp immediately after the project, about 2030".
   CONFLICT inside the source: the EIC proposal says "immediately after project completion" (generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md L68) and "within 12–24 months after completion" (same file L254). Requirement 2: flag. Fix in 4.6.2: "The EIC Transition proposal targets a first commercial installation of 1–5 MWp after the project: immediately after completion in its summary, within 12–24 months in its exploitation plan. The financial plan models it in 2031, the first full year after the project."

6. Minor — 2.3 L111 "The coordinator applied ... on 1 October 2026" and table row "Early October | Kick-off call".
   WRONG date: the meeting-prep note dated 1 October 2026 says "Balram applied yesterday on the SUREWAVE Project Officer's recommendation from the midterm review" and schedules the kick-off for "2026-10-02 14:00 CEST" with Mikaela Tsakalidou and Rosellina Di Santo (META Group) (deliverables/2026-10-01_hrb_kickoff_meeting_prep.md L7–11). Fix: "applied on 30 September 2026"; table row "2 October | Kick-off call with META Group (scheduled; no minutes on file)". The integration log's "actual date not recorded" is too weak: the scheduled date is recorded.

7. Minor — 2.5.10 L290 "Its seven members, set out in D2.4, are a chair ..., two project developers, a floating PV technology provider, a regulatory authority (the Norwegian Coastal Administration), an environmental research institute (Wageningen University and Research) and a Norwegian solar industry cluster."
   UNSUPPORTED: D2.4 lists six organisations (Greenlight as chair, Scandinavian Solar Parks, Innovex, a floating PV technology provider, the Norwegian Coastal Administration, Wageningen University and Research) while saying "most of the 7 representatives fulfil multiple roles"; no solar industry cluster is named, and finance and insurance are covered by the chair and by one project developer (D2.4 L209–242). Fix: "D2.4 names a chair who also covers finance and insurance, two project developers (one also covering finance and insurance), a floating PV technology provider, a regulatory authority (the Norwegian Coastal Administration) and an environmental research institute (Wageningen University and Research)." Add the cluster only with a source.

8. Minor — 4.3 competitor list L593 "Oceans of Energy (offshore platforms): a 0.5 MW array at an offshore wind farm in the Dutch North Sea, contracted in 2023".
   OUTDATED (newest source wins): the system at Hollandse Kust Noord was installed in August 2025, suffered thermal incidents traced to a connector defect, was returned to port and the project concluded (CrossWind, 1 May 2026; surewave/background/2026-11-14_hrb_business_plan_research/competitors.md L8, L82); the business plan says "withdrawn in 2026 after a connector fault" (business plan L208). Fix: "Oceans of Energy (offshore platforms): an array of about 1,400 panels at an offshore wind farm in the Dutch North Sea, installed in August 2025 and withdrawn in 2026 after a connector fault (CrossWind, May 2026); partner in the EU project BAMBOO."

9. Minor — 4.3 L596 "Ciel & Terre has installed 650 MW worldwide ... (CORDIS, 2024)".
   CONFLICT/outdated: the 650 MW is from the SuRE objective text on CORDIS (proposal-stage figure); a 2023 source in the repo gives 820 MW in 280 projects by mid-2023 (business_model_finance.md L43, TaiyangNews). Fix: "Ciel & Terre had completed about 820 MW in 280 projects by mid-2023 (TaiyangNews, 2023) and is a partner in the EU project SuRE (CORDIS)."

10. Minor — 4.3 L595 "Swimsol ...: floating systems at sea at ten locations, mostly in the Maldives, the largest 2.4 MW (Swimsol, April 2026)".
    UNSUPPORTED: no repo source for "ten locations". The research notes give 2.4 MW at Cheval Blanc Randheli (April 2026), 1,037 kWp at Fari Islands and 1,080 kWp at Taj Exotica, and "over 50 Maldives resort islands" using Swimsol solar, roof and sea combined (competitors.md L18, L114). Fix: "Swimsol (rigid platforms for tropical lagoons): sea-based plants in the Maldives, the largest 2.4 MW (April 2026)", or give the source for ten.

11. Minor — 4.3.1 hypothesis 4 L611 "buyers in the United Kingdom, Chile and Germany ask for Generation 2".
    UNSUPPORTED in part: the meeting summary marks Chile "(unclear)" (2026-11-13 meeting summary L50). Fix: "buyers in the United Kingdom and Germany ask for Generation 2", or confirm Chile with the owner.

12. Minor — 4.3.1 hypothesis 1 L608 "against 24–47 øre/kWh in NO3 and NO4 (NVE, Kraftsituasjonen fjerde kvartal 2025)".
    UNSUPPORTED in part: the repo notes from that NVE report give NO1, NO2, NO5 at 74–82 øre/kWh and NO4 at 24.1 øre/kWh, but no NO3 value (market.md L13 of key findings). Fix: add the NO3 figure to the research notes from the NVE PDF, or write "against 24 øre/kWh in NO4".

13. Minor — Section 8 KER1 L1101 "DNV verified the design basis of the Generation 1 float to DNV-RP-0584 in a statement of conformity (June 2022)".
    OVERSTATED in scope: DNV's news item of 23 June 2022 says DNV "issued a Statement of Conformity verifying that Sunlit Sea Design Basis complies with the RP" and that the design basis "aims to provide a general methodology, without being project nor site-specific" (dnv.com/news/2022/dnv-verifies-sunlit-sea-s-design-basis-for-floating-solar-pv-to-rp-0584-227297, fetched 23 Nov 2026). Fix: "DNV issued a Statement of Conformity in June 2022 verifying that Sunlit Sea's design basis, a general design methodology developed for Generation 1, complies with DNV-RP-0584."

14. Minor — 4.3.2 table, "Open-sea platforms | References and independent review | Pilots; first certificates and reviews from 2025".
    WRONG against D8.4's own competitor list: SolarDuck's Bureau Veritas prototype certificate is dated March 2024 (L592) and hypothesis 2 cites "2024–2026" (L609). Fix: "from 2024".

15. Minor — 4.1 L520 "The simulated 50-year maximum hinge loads are 34 kN in the Baltic Sea and 33 kN in the Mediterranean ... (D7.6)".
    UNSUPPORTED attribution: D7.6 gives the loads "under extreme conditions" without a return period (D7.6 L689, L763–767); "50-year design storms" appears in D8.3 (D8.3 L169). Fix: "The maximum hinge loads simulated for extreme conditions are ... (D7.6)", or cite D8.3 for the return period.

16. Minor — 4.1 L516 "The earlier hinge generations were shorter and placed at the float corners (D7.6)."
    D7.6 says this of the v2 hinge only ("shorter hinges (v2) installed at panel corners", D7.6 L687). Fix: "The second-generation hinges were shorter and placed at the float corners (D7.6)."

17. Minor — 4.6.1 table row "Buyer and owner": "D7.6 names existing offshore installations and small islands that rely on diesel-based power as first applications".
    OVERSTATED: D7.6 calls them "further fields of application" (D7.6 L1216) and, separately, recommends benchmarking first installations against offshore diesel at €0.36–0.42/kWh (D7.6 L1288). Fix: "D7.6 names offshore sites such as industrial platforms and small islands that rely on diesel power as further applications, and recommends benchmarking first installations against offshore diesel generation at €0.36–0.42/kWh."

18. Minor — 2.5.2 L209 "All four follow the end of the second reporting period (30 September 2026)" against Section 13 L1169 "The final periodic report is due within 60 days after the end of the project, by 1 March 2027".
    CONFLICT inside D8.4: if the project ends on 31 December 2026 (D1), the last reporting period ends on that date and its report is due 1 March 2027; the GA's original RP2 was M19–M36 (GA L458) and the final report working copy uses M19–M48. Fix: "All four were posted after 30 September 2026, the end of the reporting period covered by the partners' KPI replies", or state the amended reporting-period end.

19. Minor — 2.5 table "Conference workshops | 3 | GA, D8.5 | 3".
    GA Annex 1 sets ">3 conference workshops" (GA L7403); D8.5 sets 3 (D8.5 L310, L691). Fix: Target source "D8.5 (GA: more than 3)"; the headline then reads met against D8.5.

20. Minor — 2.5 table "Roll-ups | 1 | GA".
    The GA says "1 flyer, rollups" and "various posters and roll-ups" without a number (GA L4508, L7619); the 1 is the tracker's. Fix: Target source "WP8 (GA: roll-ups, no number)" and change "for four indicators" in L142 to five.

21. Minor — 3.4 R1 evidence L476 "two 1:10 campaigns of the integrated system at MARIN (D8.3; Energies 17(9) 2059, 2024 ...)" and 6.5 L1016 "The method and results were published in Energies 17(9) 2059 (2024)".
    The paper (April 2024) reports the first campaign: a 5 × 3 matrix with and without the breakwater, ending in hinge buckling (abstract, crossref/10.3390_en17092059.json). The second campaign with the redesigned hinge is reported in D5.7 (Sept 2025) and the final technical report. Fix: "(first campaign: Energies 17(9) 2059, 2024; second campaign: D5.7 and the final technical report)"; 6.5: "The method and the first-campaign results were published in Energies 17(9) 2059 (2024)".

22. Minor — 3.4 R4 L479 "The prototype core combines CLC with EPS blocks, kept as a manufacturing safety margin".
    D4.3 gives a different reason: EPS was added because the stability and buoyancy checks made an all-CLC prototype "almost equivalent to a full-size unit", and to keep it afloat if the cellular concrete absorbed water; an HPC layer on the bottom keeps EPS out of contact with the sea (D4.3 L267–271). Fix: "The prototype core combines CLC with EPS blocks, added to keep the reduced-scale prototype buildable and afloat if the cellular concrete absorbed water (D4.3); D4.3 expects a full-scale unit in circular mixes to float without EPS."

23. Minor — 7.3 L1091 "polyurethane floats with an aluminium bottom" and 4.5 "corrosion protection of the bottom plate".
    docs/project_facts.md L36: do not commit externally to "the bottom-plate material or alloy (aluminium 5083-H111 flat is current internal base case, likely but not certain)". D8.4 goes to CINEA and all partners. Fix: "polyurethane floats on a flat bottom plate".

24. Minor — 4.7 L799 Wood Mackenzie: "Averaged by Sunlit Sea over the forecast period, that is roughly 0.4–0.5 GW of new capacity a year".
    The forecast is cumulative capacity by 2033 (2.2 + 1.2 + 1.0 GW) and includes capacity already installed (the Netherlands and France were already the largest markets outside Asia at end-2023, L572). Dividing the total by the years overstates new capacity. Fix: "Spread over 2024–2033, that is at most about 0.4–0.5 GW a year in the three markets, less the capacity already installed".

25. Minor — Section 10 EUPI-PV row L1139 "The breakwater is funded within the project".
    The call FAQ states that demonstrator construction costs cannot be funded in full; only depreciation of equipment and other assets is eligible (funding/background/eupi_pv/2026-08-04_horizon_cl5_2026_11_d3_14_call_text.md L177–178). Fix: "The breakwater is planned within the project budget, with Clement Germany as the proposed supplier, subject to the call's rules on eligible equipment costs."

26. Minor — 4.8 row "Industrialisation" L833 "framework agreement with Metsolar (Lithuania) for module integration and kit packing".
    Stated as settled; the value chain analysis says "Kit packing partner not yet contracted" and "Packing with Metsolar or another partner in Lithuania under a framework agreement in 2027–2028" (2026-11-23_surewave_hrb_value_chain_ker1.md L39). Fix: "a framework agreement, planned for 2027–2028, with a module-integration and packing partner in Lithuania".

27. Minor — Section 10 CIRCWIND row L1133 "SINTEF's hydrodynamic modelling and its finite element methods ... reused and developed further".
    SINTEF states reuse for the finite element methods ("are being reused") but future reuse for the hydrodynamic model ("will be reused and further developed in ... CIRWIND") (SINTEF plan L11, L19). 6.4 L1000 has it right. Fix: "SINTEF's finite element methods for cracking and damage in concrete, reused and developed further; its hydrodynamic modelling, planned for reuse; potential use of Surewave-ANN".

28. Minor — 6.1 L924 and Section 10 L1132 "used in MariSol's final phase".
    UNSUPPORTED: Sunlit Sea's input says the models were "key input to a subsequent project" (Sunlit Sea summary L17); "final phase" is an inference from the dates. Fix: "used in MariSol (2020–2025)". The conflict itself is already noted in 3.1.

29. Minor — FlexiShape identification (exec summary L40, 3.1 L418, 6.4 L992, Section 10 L1135; decision D14).
    The Prosjektbanken record 321508 ("FlexiShape – Flexible patches for safe ship salvage", MIKO Marine AS, 2021–2025) names neither SINTEF nor aramid; it is the only FlexiShape project in the database (live free-text search, 23 Nov 2026). The match to SINTEF's "Mikroflexishape" is an inference and the reader is not told so. Fix in Section 10 note column: "identified from the Research Council of Norway record; SINTEF's role is from its own input". Ask SINTEF in the review round.

30. Minor — 2.5.8 and reach table "(60 participants)" and "(35 participants)".
    These counts come from the partners' KPI replies and the tracker (2026-10-06 partner responses L85; 2026-09-29 tracker L15–16), not from the MARIN news page or the NaturSea-PV page. Add "partner-reported" once, or name the source in the reach table.

31. Minor — 4.1.1 L540 "since D3.2 and D5.1 find the array's hinge loads peaking in that band".
    The breakwater note attributes these separately: D3.2 names the band as critical for the PV array, D5.1 finds the hinge-load response peaking there (breakwater note L46). Fix: "the band D3.2 names as critical for the array and where D5.1 finds the hinge loads peaking".

32. Minor — Section 14 2028 row "Start of the exposed-site demonstrator if the EIC Transition project is funded".
    The financial plan has EIC grant income from 2027 (model, EIC scenario, 2027 grants 591 vs 491 kEUR) and the EIC project runs 36 months with commissioning at M22 (EIC proposal O1). Fix: "Exposed-site demonstrator built (design released at month 12) if the EIC Transition project is funded".

33. Minor — companion consistency, D8.3 date.
    D8.4 gives D8.3 as issued on 18 November 2026 (L183, L378) in line with the KPI record; D8.3's own title page says September 2026 and it still carries 7 MWp, LCOE €0.062/kWh, IRR 10.7 % and "37 kN from integrated finite-element analysis" (integration log, items not applied). D8.4 states the version difference for the economics (L378, L721) but not for the plant size and hinge source. Fix: add to 2.5.20 "and its plant size, 7 MWp, is the D3.4 layout (Section 4.1)", or update D8.3.

### Wording

34. Wording — 4.7 L808 "cash falls below zero (lowest year-end cash about −€0.3M) unless about €0.5M more equity is raised".
    The model's €0.5M (514 kEUR) is the extra equity for a €0.2M cash buffer; staying above zero needs about €0.3M. Fix: "unless about €0.5M more equity is raised, which keeps a €0.2M cash buffer".

35. Wording — 4.7 L797 "The base case alone would need only about €0.1–0.3M of the second round". "only" is emphasis. Fix: "The base case alone would need about €0.1–0.3M of the second round".

36. Wording — 2.5.10 L292 and 4.3.1 L610 "The questions covered cost, wave-induced mismatch losses, environmental monitoring and the cost-of-energy target".
    The webinar also took questions on wave attenuation, a wind turbine on the breakwater, lighter concrete and 2D/3D models (2024-11-19 lunch webinar summary L49–56). Fix: "The questions included cost, ..." (positive claim, not a complete list).

37. Wording — 7.1 L1073 "D1.8 reports that no ownership or access-right dispute requiring formal escalation arose".
    D1.8: "No major ownership or access-right dispute requiring formal escalation was reported to project management" (D1.8 L91). Fix: quote that.

38. Wording — 4.7 L784, 4.8 L827 "the extension of the SuRE project for Sunlit Sea", "Staff funded by the SuRE extension".
    The source is an IFE-recommended scope expansion of about €0.4M for Sunlit Sea pending CINEA (project_facts L56; risk assessment "about €435,000"). "Extension" reads as a time extension. Fix at first use: "the extension of Sunlit Sea's scope in SuRE (about €0.4M; CINEA decision pending)".

39. Wording — 7.2 KER1 L1079 "Sunlit Sea's earlier patent covers the sandwich construction of the Generation 1 float".
    The meeting summary notes "the transcript suggests it has been written off; to confirm" (2026-11-13 summary L24). Fix: "Sunlit Sea's earlier patent, granted in the UK and extended to Europe, covered the sandwich construction ..." (past tense) until the status is confirmed.

40. Wording — Section 10 L1127 and decision D1: CORDIS lists the coordinator as "SINTEF MANUFACTURING AS" (web/cordis_101083342.html); the GA names "SINTEF AS" (GA L26). Decision D1 keeps the GA name; no change asked, recorded so the reviewer is not surprised. Not counted.

## Claims ledger

| # | D8.4 line | Claim (short quote) | Source (file:line or URL) | Status | Fix |
|---|---|---|---|---|---|
| 1 | 7 | Project 101083342, HORIZON-CL5-2021-D3-03-10, coordinator SINTEF AS, D8.4 SEN | CORDIS topic HORIZON-CL5-2021-D3-03-10 (web/cordis_101083342.html); GA L26, deliverable table D8.4 "SEN - Sensitive" | OK | – |
| 2 | 13 | Confidentiality per GA Article 13 | GA L1487–1508 | OK | – |
| 3 | 19 | TRL 2–3 to TRL 5; MARIN basin tests; nine months at Gijón without PV | Final report L735, L148, L2962; D7.6 L759 | OK | – |
| 4 | 19 | CONNECT TRL 4–5; directional configuration TRL 4 | project_facts L35; EIC proposal L38, L134 | OK | – |
| 5 | 19 | Project ends 31 December 2026 | project_facts L51 (CORDIS still 30 Sep 2026); decision D1 | OK (D1) | – |
| 6 | 21 | 27 results, seven KERs, KER names | Partner files: ACCIONA 3, Clement 6, IFEU 1, MARIN 3, Sunlit Sea 6, Ceit 2, SINTEF 6 | OK | – |
| 7 | 26 | First reference plant, Norwegian port, 2027, small wavebreakers | project_facts L45 (Skien havn, mid-2027) | OK | – |
| 8 | 30, 99–105 | Partner input dates and authors (ACCIONA 26 Nov 2025, uploaded by Aurora María Casado Barrasa; Clement 4 Sep; Ceit 30 Sep and 5 Oct; SINTEF 2 Oct, Panjwani) | 2025-11-26 ACCIONA email; Ceit summary L3; SINTEF plan L3 | OK | – |
| 9 | 32, 715–721 | D7.4 v2.0: Med LCOE €0.076, IRR 15.6 %, NPV €7.3M, payback 10 y; Baltic €0.120, −€0.03M, 8.5 %; North Sea €0.173, −€5.8M, 3.4 % | D7.4 L97–123, L334–340, L496–498 | OK | – |
| 10 | 32, 612, 806 | Investment support about a quarter (27 %) | Model unit economics support_needed 0.2731; financial plan L33, L266 | OK | – |
| 11 | 34, 774–778 | 28 MWp 2027–2031; 7 MWp 2030; 16 MWp 2031; 3.6 (13 %), 4.1 (15 %), 20 (72 %) | Model KPIs cum_mw_2031 28; financial plan L112–116, L519, L598 | OK | – |
| 12 | 34, 797 | €5.5M in two rounds: €3.5M Q1 2027, €2.0M H2 2029 | Model equity_raised 5500; financial plan L30, L55 | OK | – |
| 13 | 34 | Proposal 25 MW pilot 2025–2027; 1,240 MW by 2032 | Annex 1 Part B L887, L698 | OK | – |
| 14 | 36, 1079 | Gen 2 patenting assessed with patent attorney, not pursued (prior art) | 2026-11-13 meeting summary L24 | OK | – |
| 15 | 38, 142, 146 | Publications target met (10 of 10) | GA L7389; D8.5 L270; final report L4462 | OVERSTATED | Finding 1 |
| 16 | 40 | MariSol RCN 2020–2025 with IFE; SuRE coordinated by IFE, Sep 2024 – Aug 2027 | web/pb_317808.html; web/cordis_101135567.html | OK | – |
| 17 | 46 | GA description of D8.4; Task 8.4 wording; O8 | GA L5363–5371, L4491–4497; Annex 1 Part B L141 | OK | – |
| 18 | 48 | P1 marketed by Sunlit Sea; R11 has no owner in the preliminary KER table | Annex 1 Part B Table 2-5 L860–882 | OK | – |
| 19 | 82–83 | D8.1 month 6; D8.5 month 18 | GA D8.1 and D8.5 detail (due 6 and 18) | OK | – |
| 20 | 111 | Booster application 1 October 2026 | 2026-10-01 kickoff prep L11 ("applied yesterday") | WRONG | Finding 6 |
| 21 | 115 | Kick-off "early October" | kickoff prep L7 (2 Oct 2026, 14:00) | UNDERSTATED | Finding 6 |
| 22 | 116–123 | Booster steps 18 Oct, 23 Oct, 5–6 Nov, 11–12 Nov, 13 Nov, 15 Nov, 22–23 Nov, December | File dates in surewave/deliverables and background; meeting summary L15, L128 | OK | – |
| 23 | 125 | No major changes; BOSAT above 3 in six dimensions; IA service from Jan 2027 | Meeting summary L11–14, L96–97, L122 | OK | – |
| 24 | 142, 144–168 | Target sources GA / D8.5 / WP8 | GA L4507–4510, L7389–7633; D8.5 L252–316 | OK except rows 25–26 | Findings 19, 20 |
| 25 | 154 | Conference workshops target 3 (GA, D8.5) | GA L7403 ">3"; D8.5 L310 | CONFLICT | Finding 19 |
| 26 | 164 | Roll-ups target 1 (GA) | GA L4508 "rollups" (no number) | UNSUPPORTED | Finding 20 |
| 27 | 170 | Counting rule and items counted under several indicators | KPI record (companion) L357–362 | OK | – |
| 28 | 172 | Partner-reported items named; NaturSea-PV kick-off contradicted | KPI record L111, L139, L138, L216, L362 | OK | – |
| 29 | 178 | 41 Crossref citations of seven DOI papers, two from 2026 | Live Crossref 23 Nov 2026: 23 + 5 + 11 + 2 + 0 + 0 + 0 | OK | – |
| 30 | 180 | 8 distinct webinar/workshop events vs D8.5 "at least 10" | D8.5 L252; D8.4 lists | OK | – |
| 31 | 181, 184 | 35 and 60 participants | Tracker L15–16; partner responses L85 | OK (partner-reported) | Finding 30 |
| 32 | 182 | Media mentions 13 vs >20 (D8.5) | D8.5 L280; KPI record L250–260 | OK | – |
| 33 | 183 | D8.3 issued 18 Nov 2026; LinkedIn 22 Dec 2026 | KPI record L304, L347 | OK (see 33) | Finding 33 |
| 34 | 185 | Final workshop 30 Sep 2026, 27 guests | KPI record L154; invitation file | OK | – |
| 35 | 188 | Sunlit Sea's own WP8 output; Kegelart co-author | KPI record L172, L199, L224–229; Crossref en17092059 authors | OK | – |
| 36 | 196–205 | Ten publications: venues, volumes, pages, dates, authors, DOIs | crossref/*.json; KPI record L56–65 | OK | – |
| 37 | 211–214 | Four preprints: titles, authors, dates, DOIs (v2 14 Oct for preprint 1) | crossref preprint JSON files | OK | – |
| 38 | 209 | "follow the end of the second reporting period (30 September 2026)" | GA L452–458; final report L756; D8.4 L1169 | CONFLICT | Finding 18 |
| 39 | 218 | Two submitted manuscripts: keeled-breakwater dynamics; machine-learning concrete model | Final report L3724–3725 | OK | – |
| 40 | 224–237 | 14 conferences, dates, places, contributions, records | KPI record L91–111; tracker L13, L31; final report L3503, L3721; eupvsec.org (14–18 Sep 2026, Rotterdam) | OK | – |
| 41 | 239 | By partner: Ceit 4, IFEU 4, MARIN 3, Sunlit Sea 2, SINTEF 1 | Count of the table | OK | – |
| 42 | 245–259 | 15 presentations, presenters | KPI record L117–141; poster md L3 (Panjwani presented) | OK | – |
| 43 | 265–267 | Three posters | KPI record L205–216 | OK | – |
| 44 | 271–274 | Four web events; SAB webinar 31 sign-ups, about 23 at start, 64 min | Lunch webinar summary L7–10; KPI record L152 | OK | – |
| 45 | 278–280 | Three joint events; 15 projects incl. NaturSea-PV and BAMBOO | KPI record L306–312 | OK | – |
| 46 | 284–286 | Three conference workshops; final workshop details | KPI record L316–322 | OK | – |
| 47 | 290 | SAB seven members incl. a Norwegian solar cluster (D2.4) | D2.4 L209–242 | UNSUPPORTED | Finding 7 |
| 48 | 292–295 | SAB 19 Nov 2024 and March 2025 meetings; questionnaires (D2.4), D8.2 review | KPI record L328–336 | OK | – |
| 49 | 301–303 | Newsletters I (6 Jul 2023), II (14 Sep 2023) and contents; III–V scheduled | Newsletter I and II files; KPI record L340–347 | OK | – |
| 50 | 309–318 | Eight journalistic articles; five independent; four Spanish items not counted | KPI record L236–260; ACCIONA email of 26 Nov 2025 | OK | – |
| 51 | 322 | ACCIONA announcement 11 Oct 2024; SINTEF start news 1 Nov 2022 | KPI record L240, L244, L292–294 | OK | – |
| 52 | 328–338 | Nine interviews, dates, interviewees | KPI record L262–282 | OK | – |
| 53 | 344–350 | Seven videos, dates, lengths, producers | KPI record L220–230 | OK | – |
| 54 | 354–360 | Five infographics; sixth scheduled 15 Dec 2026 | KPI record L178–190, L347 | OK | – |
| 55 | 364–374 | Factsheets, flyer, roll-up 85 × 200 cm, June 2023 | KPI record L168–200 | OK | – |
| 56 | 378 | D8.3 led by Sunlit Sea with SINTEF; economics from D7.4 v1.0 | GA L4486–4487; D8.3 | OK | – |
| 57 | 382 | LinkedIn 371 at M18, 694 in Nov 2026 | KPI record L160–162 | OK | – |
| 58 | 386 | Matomo from late Aug 2023; ≤35 visits/week; 800 at M18; campaign 29 May 2024; ~27,000 %; stopped end 2024 | KPI record L296–300 | OK | – |
| 59 | 390–396 | OpenAIRE 37 results; 18 Zenodo community; three outside; CORDIS public deliverables incl. D3.4 and D7.5; CC BY 4.0 | KPI record L355; crossref licence fields; GA deliverable detail: D3.4 "PU - Public", D7.5 "Report on social assessment ... PU - Public" | OK | The integration log's open item (D7.5 listed as Sensitive in the GA) rests on the misaligned summary table; the GA detail table lists D7.5 as Public. No change needed |
| 60 | 410 | D8.5 six findings (snapping loads, lighter floats, off-the-shelf panels, aluminium frames, sustainable concrete, partial protection) | D8.5 L1277–1309 | OK | – |
| 61 | 411 | Template sent 29 Sep 2026 with the listed fields | Template L51, L414; Ceit summary L3 | OK (date) | – |
| 62 | 412 | Partners wrote "in their own format rather than in the template fields" | ACCIONA 26 Nov 2025; Clement 4 Sep 2026 predate the template | OVERSTATED | Finding 3 |
| 63 | 414–416 | LWAC 1,950 / about 2,000 / about 1,800 kg/m³; HPC 5 % / 400 vs 500 / 380; CLC 25 vs 36 | ACCIONA summary L7, L17, L28; Clement materials report L126 (2,560 m³ = 5,119 t); D4.1 L1259; final report L193, L443 | OK | – |
| 64 | 417 | MariSol record 2020–2025 | web/pb_317808.html | OK | – |
| 65 | 418 | CIRWIND and Mikroflexishape spellings | SINTEF plan L11, L43 | OK | Finding 29 on identification |
| 66 | 420 | SHMS uses Ceit stress fields, MARIN loads, SINTEF material predictions | Decision D13; final report | OK | – |
| 67 | 436–442 | KER table facts (CLC 365 kg/m³, LWAC 68 MPa, HPC 128 MPa; Gijón results; DIFFRAC 100 → nearly 4,000; mooring 34–56 %, nearly 60 %; ±448 → ±135 Ω; 0.35–0.45 Hz) | ACCIONA summary; final report L269, L2962–2965; MARIN summary L7; D5.1 L1774, L1472 | OK | – |
| 68 | 476 | R1 50 MWp future plant; TRL 5 target | Annex 1 Part B L960 | OK | – |
| 69 | 476, 518, 926 | Hinge 3.69 → 8.36 kN as capacity of the redesigned hinge / between generations | D6.3 L273, L447, L851; preprint 1612 abstract; D7.6 L687, L1134 | CONFLICT | Finding 2 |
| 70 | 476, 520 | ULS 14 → 37 kN; 34 / 33 / 40 kN | D7.6 L689, L763–767; final report L3278 | OK | – |
| 71 | 520 | "simulated 50-year maximum hinge loads" (D7.6) | D7.6 gives no return period; D8.3 L169 | UNSUPPORTED | Finding 15 |
| 72 | 477 | R2 target TRL 4; Clement direct sales to FPV builders and port protection | Annex 1 Part B L180, L862 | OK | – |
| 73 | 478 | R3 UHPFRC 850 → 350 kg/m³ ("up to 60 %"); achieved 380, about 55 %; prototype 3.40 × 1.70 × 1.05 m, Sept 2025 – June 2026; biofouling >85 % | Annex 1 Part B L192, L196; final report L193, L2961–2965 | OK | – |
| 74 | 478 | D7.4: HPC raises Med LCOE 0.076 → 0.085 | D7.4 L1146 | OK | – |
| 75 | 479 | EPS "kept as a manufacturing safety margin" | D4.3 L267–271 | CONFLICT | Finding 22 |
| 76 | 480–486 | R5–R11 target TRLs and types; 598 FE simulations; D5.3 infinite-life; D7.5 Oct 2025, D7.6 Nov 2025 | Annex 1 Part B L216, L232, L242; D5.5 L527; D5.3 L97, L992; D7.5 file date 2025-10-06; D7.6 file date | OK (153 points and D7.3 date not checked) | – |
| 77 | 476 | Two MARIN campaigns evidenced by Energies 17(9) | Energies 17(9) abstract (first campaign only) | OVERSTATED | Finding 21 |
| 78 | 504 | 346 m ring; 7.16 MWp in D3.4; 173 m for 2 MWp; D7.4 1 × 2, 5 × 2, 10 MWp | D3.4 L518–527; Clement materials report L33 | OK | – |
| 79 | 516 | "earlier hinge generations ... at the float corners (D7.6)" | D7.6 L687 (v2 only) | OVERSTATED | Finding 16 |
| 80 | 517–519 | 1.88 m full-edge hinge; 20.23 kN; 25-year fatigue; second campaign no buckling | D7.6 L689; final report L313, L2998 | OK (with Finding 2) | – |
| 81 | 538–559 | Breakwater classes: JONSWAP/SPM 1984, 22 m/s, Macagno, 0.45 / 0.6 / 0.8 m, 2.5 m min width; light 2.5 × 1.0 m, 30 t; medium 4 × 1.5 m, 73 t; heavy 5 × 2.03 m, 123 t; Hs 0.65 / 1.0 / 1.3 m, fetch 1.6 / 3.8 / 6.4 km; €117 → €58 per kWp; €547 at 350 kWp; natural periods 2.7/2.5, 3.4/3.2, 3.8/3.6 s against 2.3, 3.1, 3.7 s | Re-run of scripts/breakwater_classes.py; breakwater note L30–76 | OK | – |
| 82 | 540 | "D3.2 and D5.1 find the array's hinge loads peaking in that band" | Breakwater note L46 | OVERSTATED (attribution) | Finding 31 |
| 83 | 563 | Sunlit Sea founded 2019, Oslo; Gen 1 plants Germany 2023, Norway PPA 2024–2026; subcontracted production 2024 | project_facts L10–12, L22, L31–33 | OK | – |
| 84 | 572 | IEA PVPS 8.7 GW end-2024; 7.7 GW end-2023, ~90 % Asia; NL and France; TRL >8 inland, 3–5 offshore | market.md key findings 1–3 | OK | – |
| 85 | 574 | SolarDuck 0.5 MWp July 2024; BlueNewables 1 MW Valencia | competitors.md L7, L12, L29, L73 | OK (dates not re-fetched) | – |
| 86 | 576–577 | Spain 4.45–6.48 GW (U. A Coruña, JCP, pv magazine June 2026); TNO 200 GWp / 45 GWp | market.md finding 5 | OK | – |
| 87 | 579 | NVE: 1.4 GW applications, three plants 14 MW, 10 GW for 8 TWh, 5 Feb 2024 | market.md finding 11 | OK | – |
| 88 | 590–592 | Fred. Olsen DNV review Hs 3.5 m; Ocean Sun BV type certificate Nov 2025; SolarDuck BV prototype certificate | competitors.md L9, L63; business plan L204 | OK | – |
| 89 | 593 | Oceans of Energy 0.5 MW contracted 2023 | competitors.md L8, L82; business plan L208 | CONFLICT (outdated) | Finding 8 |
| 90 | 595 | Swimsol ten locations | no repo source | UNSUPPORTED | Finding 10 |
| 91 | 596 | Ciel & Terre 650 MW; SuRE partner | CORDIS SuRE text; business_model_finance.md L43 | CONFLICT (outdated) | Finding 9 |
| 92 | 608 | NO1/NO2/NO5 74–82 øre; NO3/NO4 24–47 øre | market.md finding 13 (NO4 24.1; no NO3) | UNSUPPORTED (NO3) | Finding 12 |
| 93 | 608 | Hosts: harbour two-year permit; industrial basin pre-project grant, grid, mooring accepted; lake rezoning | project_facts L45–47 | OK | – |
| 94 | 610 | Webinar: two attendees asked; 0 to 12–13 %; about 10 % and 2–3 % | Lunch webinar summary L50 | OK | – |
| 95 | 611 | Kits of 4–6 panels; UK, Chile, Germany | Meeting summary L49–50 (Chile "unclear") | UNSUPPORTED (Chile) | Finding 11 |
| 96 | 628 | "first certificates and reviews from 2025" | D8.4 L592 (SolarDuck certificate March 2024) | WRONG | Finding 14 |
| 97 | 632–639 | D7.6 coal comparison and deployment conditions | D7.6 L147, L1204, L1210 | OK | – |
| 98 | 673–676 | DNV-ST-C108, DNV-ST-E309 (May 2026), DNV-RP-0584; IEC TS 62788-7-2 | customers_regulation.md L20; technology_standards_ip.md L7; risk assessment | OK | – |
| 99 | 683–688 | Milestones Q2 2027 to Q2 2028 | Roadmap M1–M7 (L68–74) | OK | – |
| 100 | 696–698 | Norway 10 MW licence threshold from 1 July 2025; Sweden vattenverksamhet; WHG 15 % and 40 m | customers_regulation.md L7, L16, L18 | OK | – |
| 101 | 713 | 50 years, PV replacement at 25, decommissioning; €0.12/kWh target price; 8.5 % | D7.4 L91, L343, L982 | OK | – |
| 102 | 721 | Baltic viable up to 8 %; North Sea at 3 % or lower; non-panel costs close to onshore; €212/kWp under a quarter | D7.4 L1128, L500, L351, L817–828 (212/940 = 23 %) | OK | – |
| 103 | 725 | Mediterranean leads on yield and lower maintenance | D7.4 L345, L733 | OK | – |
| 104 | 729 | D7.6 diesel-powered islands as "first applications" | D7.6 L1216, L1288 | OVERSTATED | Finding 17 |
| 105 | 730 | €9.8M, €940/kWp, 300 m floating cable; exclusions | D7.4 L825, L464–475 | OK | – |
| 106 | 741, 848, 1138, 1230 | EIC: first commercial 1–5 MWp "immediately after" | EIC proposal L68 vs L254 | CONFLICT | Finding 5 |
| 107 | 741, 746 | Lake site, 45° sector | Financial plan L314; model BW_EXAMPLE sector_deg 45 | OK | – |
| 108 | 745–758 | €0.83/W; €1,150/m; €40,000 mobilisation; lengths 70 / 120 / 190 / 400 / 960 m; shares 64/78, 30/46, 15/25, 6/11, 2/4 % | Model; recomputed with coverage(kwp, 45, "light"): 69.9 / 120.2 / 193.7 / 404.3 / 958.9 m and the same shares; breakwater note L104, L221 | OK | – |
| 109 | 760 | About €0.10/kWh; German tender July 2025 average 4.84 ct/kWh (BNetzA, Aug 2025) | Model 1 MWp half-shared LCOE 0.099; model BW_EXAMPLE grid_award note (press release 14 Aug 2025) | OK (tender not re-fetched) | – |
| 110 | 770–772 | Revenue €3.2–3.6M and €12.1–12.6M; margin 14 % 2028, 41–44 %; EBITDA ~€0.2M 2030, €1.9–2.1M 2031 | Model: 3,157 / 3,647; 12,070 / 12,553; 347/2,515 = 13.8 %; 41.5–43.6 %; 164–214; 1,878–2,117 kEUR | OK | – |
| 111 | 784–787 | Four scenarios; EIC €0.75M and 1 MWp in 2031; EU upside €0.9M and 1 MWp in 2029 | Financial plan L169–170 | OK | Finding 38 (wording) |
| 112 | 791–794 | Scenario table (8.2/1.9/−1.4/0.89; 8.7/2.1/−1.1/0.92; 8.7/2.1/−0.7/0.93; 8.2/1.9/−1.6/0.73) | Model summary table | OK | – |
| 113 | 796 | Kit break-even 7 MWp (EBITDA), 9 MWp (all costs) | Model KPIs; financial plan L53, L486 | OK | – |
| 114 | 797 | €0.1–0.3M of round 2; minority share €0.2M | Financial plan L31, L70 | OK | Finding 35 (wording) |
| 115 | 798 | Cash +€0.7M vs base, +€0.9M vs grant downside; EIC +€0.2M EBITDA 2031 | Model: 3,493 − 2,796 = 697; 3,493 − 2,633 = 860; 2,117 − 1,878 = 239 | OK | – |
| 116 | 799 | Outlook 18 MWp 2032, 25–45 MWp; Wood Mackenzie 2.2 / 1.2 / 1 GW; 3–4 % | Model indicative table; financial plan L519–521 | OK (arithmetic), OVERSTATED (new capacity) | Finding 24 |
| 117 | 801 | Wavebreakers ~€0.1M → −€0.05M; light breakwater at two sites → −€0.9M | Model sensitivities −1,486 and −2,382 vs −1,441 | OK | – |
| 118 | 805 | Kit margin target 40–50 %; about 44 % today | Financial plan L24, L292–300 | OK | – |
| 119 | 808–811 | Delay −€3.6M, EBITDA −€0.1M, cash −€0.3M, €0.5M; 10 MW lost −€2.4M, €0.7M; volume −30 % €0.9M; price/cost €0.4M; combined −€5.6M, −€0.6M, €1.0M | Model sensitivity table | OK | Finding 34 (wording) |
| 120 | 815–818 | Four decision gates | Financial plan L583–586 | OK | – |
| 121 | 822 | 26 risks; rating rules; four in action zone | Risk assessment L3–5 and summary (26 rows) | OK | – |
| 122 | 826–840 | Each rating (8×7, 8×7, 9×6, 9×6, 9×5, 7×6, 7×6 feas 5, 8×5, 8×5, 6×6, 8×4, 7×4, 6×4, 6×4, 7×3) and mitigations | Risk assessment rows L9–34 | OK | Finding 26 (Metsolar) |
| 123 | 855–864 | Roadmap M1–M10 | Roadmap L68–77 | OK | – |
| 124 | 870–877 | Proposal targets: 2026 contracts, 2028–2030 plants, 2030–2032 phase, 2035; 25 facilities, 5–10 utilities, €50M, 1,335,608, 3,460, €967.2M; LCOE 54 from 161; CAPEX 1,560 → 781; OPEX 25.4 → 12.7; mooring −40 % | Annex 1 Part B L585, L631, L650–654, L698–762, L887–891; GA L6972 | OK | – |
| 125 | 877 | 940/1,560 = 40 % below; 17.4/25.4 = 31 % below | D7.4 L825, L857 | OK | – |
| 126 | 880 | €606 + €175; reference twice calm-water cost | Annex 1 Part B L585, L618, L621 | OK | – |
| 127 | 886, 905, 1114 | Access rights within one year, by 31 December 2027 | GA Article 16 (Annex 5) | OK | – |
| 128 | 924 | MariSol "final phase" | Sunlit Sea summary L17 | UNSUPPORTED | Finding 28 |
| 129 | 938–940 | ACCIONA mix properties and positioning | ACCIONA summary L7–33 | OK | – |
| 130 | 944 | D8.5 named certification | D8.5 L1309 | OK | – |
| 131 | 961–968 | Clement results and routes | Clement summary L3–65 | OK | – |
| 132 | 986–992 | SINTEF results; reuse in SFI BLUES, FlexiShape (2021–2025, aramid), CIRCWIND (2024–2028) | SINTEF plan L11–45; web/pb_321508.html; web/cordis_101147517.html | OK | Finding 29 |
| 133 | 1014–1016 | MARIN results; Task 5.2, Dakota; Baltic heavier | MARIN summary L7–25; D5.1 L1416–1430, L1449–1452, L1774 | OK | Finding 21 (paper scope) |
| 134 | 1032–1034 | Ceit routes, 5–6 cm cover | Ceit summary; final report L268 | OK | – |
| 135 | 1050–1052 | IFEU result and talks | IFEU summary L15; KPI record | OK | – |
| 136 | 1073 | D1.8 joint ownership rule; "no ... dispute" | D1.8 L91, L305–307 | OK | Finding 37 (wording) |
| 137 | 1079 | Trade secrets, design registration, earlier patent | Meeting summary L24 | OK | Finding 39 (wording) |
| 138 | 1080 | KER2: recipes not published (D1.8) | D1.8 Table 2 ("detailed formulations restricted") | OK | – |
| 139 | 1091 | FTO scope incl. "aluminium bottom" | project_facts L36 | CONFLICT (facts file) | Finding 23 |
| 140 | 1097, 1119–1121 | Standards duty; 45 / 30 / 60 days; exclusive licences | GA L8840–8910, L8935, L8982 | OK | – |
| 141 | 1101 | DNV statement of conformity on the Gen 1 float design basis, June 2022 | DNV news 23 June 2022 (live) | OVERSTATED (scope) | Finding 13 |
| 142 | 1127 | SUREWAVE 1 Oct 2022 – 31 Dec 2026 | CORDIS start 1 Oct 2022; D1 | OK | – |
| 143 | 1131–1135 | SuRE 101135567; MariSol 317808 partners; CIRCWIND 101147517; SFI BLUES 309281, 2020–2028; FlexiShape 321508, MIKO Marine, 2021–2025 | CORDIS and Prosjektbanken snapshots | OK | – |
| 144 | 1133 | CIRCWIND: hydrodynamic modelling "reused and developed further" | SINTEF plan L11 (future) | OVERSTATED | Finding 27 |
| 145 | 1138 | EIC topic, submitted 16 Sep 2026, decision Dec 2026 – Jan 2027; applicants; 50–300 kWp; LOI 8 Sep 2026; M22, 12 months, DNV SoC by M34; €2.5M | EIC proposal L4, L26, L81–93, L167, L318, L369; project_facts L43 | OK | – |
| 146 | 1139 | EUPI-PV title, ID, deadline 1 Dec 2026; ≥5 MW multi-zone; 1 MWp Sweden + 4 MW Germany; start H2 2027; install May–Sep 2029 | Call text L2–31, L58; project_facts L42 | OK | – |
| 147 | 1139 | "breakwater is funded within the project" | Call FAQ L177–178 | OVERSTATED | Finding 25 |
| 148 | 1169 | Article 21 continuous reporting; final report 60 days, 1 March 2027 | GA L432–458 | OK | Finding 18 |
| 149 | 1180–1183 | HRP duty "up to one year" | GA L8886–8888; D17 | WRONG (framing) | Finding 4 |
| 150 | 1190 | 15 days' notice and objection | GA L9193–9202 | OK | – |
| 151 | 1195–1200 | Data Sheet point 6: 5 / 5 / 2 / 2 / 5 years | GA L530–539 | OK | – |
| 152 | 1238 | Conclusions: Med €0.076, 15.6 %; €5.5M; break-even 2030 | as rows 9, 12, 112 | OK | – |

## Content gaps (requirements 4 and 5)

1. Peer-review status of the three congress papers (2.5.1). The record can be completed: the GEF proceedings (Revista Española de Mecánica de la Fractura) and the MZT congress state their review procedure on gef.es and mzt.mondragon.edu (KPI record L63–65 give the PDFs). Write one sentence per venue on whether papers were reviewed, so the target count in finding 1 rests on evidence rather than on the final report's label.

2. Hinge evidence chain (4.1). The repo holds the full chain: D6.1 (first-generation hinge tests), D6.3 (new connection, segment tests, rope vs steel rod, fatigue S–N curves, 6.9 kN limit, production shrinkage of 1–2 mm), D5.7 and the final report (second basin campaign), D7.6 (ULS 14 → 37 kN, 54 kN earlier peak load, North Sea 40 kN about 8 % above). Present it item by item: what was tested, specimen, configuration, result, source. The production-quality finding (D6.3 L285, L485: shrinkage gaps and early cracks, "very critical to control the production process") is relevant to the KER1 durability risk in 4.8 and is missing.

3. Booster record (2.3). Add the scheduled kick-off (2 October 2026, mentors from META Group) and the actual application date (30 September 2026) from the meeting-prep note; say the timeline was set as a sprint pending the project extension (kickoff prep L13).

4. EIC timing (4.6.2, 4.9, 10, 14). State both timings in the proposal and why the financial plan uses 2031 (finding 5).

5. Competitors (4.3). Bring the Oceans of Energy withdrawal and its cause (connector fault, not structural) into the list; the research notes call electrical and balance-of-system reliability "the recurring failure mode in 2025–2026" (competitors.md L20). This supports the qualification programme in 4.5 and is missing.

6. SAB composition (2.5.10). Either give the D2.4 list as it stands (six organisations, seven representatives) or name the source for the seventh member.

## Writing and consistency (requirements 6 and 7)

1. KER names, section references, table column counts and blank lines after separator rows: all checked by script; no faults found.
2. No `**` in the body; no "therefore", "thus", "which is why", "it follows", "precisely", "crucially", "clearly", "already", "well above" or "well beyond". One emphatic "only" (finding 35).
3. Hinge generation numbering: D8.4 uses "third hinge generation" (3.1 L420, 3.4 R1, 4.1, 4.8) following D7.6's v3, while D6.3 counts the D6.1 hinge as the first generation and the tested connection as "a new generation". 3.1 says hinge generations are numbered separately from platform generations; add once, in 4.1: "hinge generations follow D7.6: the corner hinge is the second, the full-edge hinge the third".
4. "50-year" (4.1) vs "under extreme conditions" (D7.6) — finding 15.
5. "extension of the SuRE project" (4.7, 4.8, Section 12 rows) — finding 38; use one term throughout.
6. Section 14 2028 "Start of the exposed-site demonstrator" vs 4.9 2029 commissioning and the 2027 EIC start in the financial plan — finding 32.
7. "about 7 MWp in 2030" (exec, 4.7) vs financial plan "7.2 MWp" — consistent within rounding.
8. Integration-log item on D7.5 (left for the owner): the GA's detailed deliverable table lists D7.5 "Report on social assessment" as PU - Public (GA deliverable detail, the D7.5 block before D7.6); the "SEN" reading came from the misaligned summary table. D8.4 2.5.23 is correct as written.

Findings: 4 major, 29 minor, 6 wording.
