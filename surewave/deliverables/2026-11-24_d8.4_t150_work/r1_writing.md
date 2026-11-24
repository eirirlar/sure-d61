# T150 round 1: editor and confidentiality review of d84_merged.md

Reviewer persona: editor and confidentiality reviewer. Scope: requirement 7 and CLAUDE.md "Language and tone", read sentence by sentence; terminology, units, number format, heading levels, repetition, sentences a non-native reader would stumble on, tables; confidentiality against the financial plan (surewave/deliverables/2026-11-22_surewave_hrb_financial_plan_ker1.md, "FP" below) and docs/project_facts.md ("PF" below). Line numbers refer to d84_merged.md.

Mechanical checks run: no `**` in the file (0 hits). No banned emphasis words or conclusion connectives found by grep ("already", "clearly", "therefore", "thus", "crucially", "precisely", "well beyond", "which is why", "it follows"; "key" only in "Key Exploitable Results" and "key people"). Every table has the same column count in every row and no blank line after the separator row. Counts were checked against their tables: conferences 14 (Ceit 4, IFEU 4, MARIN 3, Sunlit Sea 2, SINTEF 1), presentations 15, posters 3, web events 4, articles 8 (5 independent + 3 partner), interviews 9, videos 7, infographics 5, factsheets 3, publications 10 (6 + 1 + 3), volume split 3.6 + 4.1 + 20 = 27.7 MWp (13 + 15 + 72 %), CAPEX −40 %, OPEX −31 %, €606 + €175 = €781/kWp, 2031 volume 16 MWp ≈ 3–4 % of 0.4–0.5 GW. Final periodic report date (60 days after 31 December 2026 = 1 March 2027) is correct.

## A. Confidentiality

1. Major. Section 4.6.2, line 745: "PV plant at €0.83 per watt at every size, the cost of a plant built from the kit (Section 4.7)". This is a Sunlit Sea cost per watt: FP line 275 ("A developer that buys kits at €0.47 per watt (2030) builds a plant for about €0.83 per watt") and FP line 316 ("phase 2 capex €0.83 per watt"). The accepted owner decision in the brief says costs per watt are not shown; decision D7 writes the figure into 4.6.2, so the error sits inside D7. Section 2.3 (line 127) gives the reason in the draft itself: several partners are potential suppliers. Clement Germany, as the breakwater supplier, would see Sunlit Sea's plant cost per watt. Fix: replace the bullet with "PV plant at the cost of a plant built from the kit (Section 4.7), taken as the same per watt at every size. A demonstrator costs more per watt, so the shares in the demonstrator rows are upper values." In D7's own wording, "at a plant cost of €0.83 per watt" should be cut as well.

2. Major. Section 4.6.2, lines 747 and 752–758: "about €1,150 per metre installed for the light class, plus about €40,000 mobilisation per site", together with the breakwater lengths and the shares in the table. With these three, any reader can work out the PV plant cost per watt even if item 1 is fixed. Example for 1 MWp: 190 m × €1,150 + €40,000 ≈ €0.26M. A 25 % share then gives a PV plant of about €0.78M, or about €0.8 per watt. Clement Germany can do the same with its own cost per metre. Fix: keep the shares and drop both the cost per metre and the lengths ("Breakwater and anchoring costs of D7.4 version 2.0 as modelled, plus Sunlit Sea's estimates for fabrication, fittings, transport, supplier margin and mobilisation"). Or keep the lengths and give the shares as bands only ("about a quarter", "about a tenth"). Either way, delete the "Breakwater length" column, or the €/m figure, but not just one of the three inputs.

3. Minor. Sections 4.7 and the executive summary: kit price and kit cost per watt can be estimated closely. The base-case 2031 revenue is €8.2M (line 791) for about 16 MWp delivered (lines 34, 774), "as kit sales dominate" (line 771). That gives about €0.51 per watt, against FP's kit price of €0.47 per watt plus engineering at 4 % of a €0.83 per watt plant (FP lines 283–286). Line 805 ("At today's production cost the margin is about 44 %, provided the kit price holds close to today's level") then gives a kit cost of about €0.28 per watt, which is FP line 292's "today's delivered cost of €0.28 per watt". The estimate is not exact, but it lands within about 10 % of the true figures. Decision D9 requires the 7 and 16 MWp volumes, so the lever is the revenue side. Fix: in the scenario table (lines 789–794), replace "Revenue 2031" with "Revenue 2030–2031" (as in the table at line 770). In line 805, delete "At today's production cost the margin is about 44 %, provided the kit price holds close to today's level" and write "The plan's kit gross margin target is 40–50 %; the plan meets it at today's kit price and production cost."

4. Minor. Section 4.6.2, line 760: "it produces power at about €0.10/kWh (financial plan)" for a 1 MWp plant with the breakwater half carried by other uses. With D7.4's opex and a public PVGIS yield, a reader can back out the plant capex roughly. The risk is low. If item 1 is applied, keep the LCOE and do not add the yield (FP line 316: 960 kWh/kWp).

5. Minor. Pipeline detail lets partners identify the sites. Each item is generic, but together they point to Skien havn (350 kWp, two-year permit by dispensation, harbour; PF lines 45, 72) and Gunneklevfjorden (3.2 MWp, Enova pre-project grant; PF line 85). Both are also named in the EIC proposal (generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md line 64). Occurrences:
   - line 557: "from a 3.2 MWp to a 10 MWp plant", "€547 per kWp at 350 kWp" (the exact sizes of the reference sites);
   - line 608: "a harbour (two-year permit by dispensation), an industrial basin (state pre-project grant; grid capacity confirmed by the local grid company; seabed mooring accepted by the environment agency) and a lake (rezoning under way)";
   - line 611: "buyers in the United Kingdom, Chile and Germany ask for Generation 2 …; inbound leads from Germany, Türkiye, Italy and Denmark; one lead in Germany with confirmed interest";
   - line 766: "three Norwegian reference sites (a harbour, an industrial basin and a lake), kit leads in Germany, Denmark and the Baltic states";
   - lines 857, 862, 863: M3 "350 kWp commissioned", M8 "3.2 MWp commissioned", M9 "Investment decision for 3.2 MWp after rezoning".

   Fix: in line 557, use round sizes ("from about 3 MWp to 10 MWp", "below 0.5 MWp"). In line 608, write "Three Norwegian hosts have committed time to permits and site studies; one site holds a temporary permit, one has a state pre-project grant and confirmed grid capacity, and one is being rezoned". In line 611, write "inbound requests from several European countries and outside Europe; no kit order for a plant yet". In M3, M8 and M9, write "First reference plant commissioned", "First multi-megawatt plant commissioned" and "Investment decision after rezoning". The owner may choose to keep the site types; the sizes are the identifying element.

6. Minor. Section 10, line 1138 (EIC row): "EDP as end user and commercialisation partner" and "an inland lake in Germany, whose owner signed a letter of intent on 8 September 2026". EDP is a named prospective customer, and the letter of intent is a host commitment. Four SUREWAVE beneficiaries (ACCIONA, MARIN, Ceit, IFEU) are not in the EIC consortium. PF line 43 also says only "possible EDP (Portugal) involvement", while the proposal (line 26) lists EDP as an applicant. Fix: "SINTEF (coordinator), Sunlit Sea, Clement Germany and an energy utility as end user and commercialisation partner" and "a demonstrator of 50–300 kWp at an inland lake in Germany, with a signed letter of intent from the site owner".

7. Wording. Section 4.8, line 833: "framework agreement with Metsolar (Lithuania) for module integration and kit packing". This names a supplier, and it reads as if the agreement exists. The roadmap (surewave/deliverables/2026-11-11_surewave_hrb_exploitation_roadmap_ker1.md line 41) has it as a plan for Q2 2027–2028. Fix: "a planned framework agreement with a module integrator in Lithuania for module integration and kit packing".

8. Wording. Section 4.8, line 837: "30 % advance and staged payments; … liability capped at 20–30 % of the contract value". This is Sunlit Sea's contract strategy, shown to partners that may become its subcontractors. Optional fix: "advance and staged payments; back-to-back terms with subcontractors; capped liability".

## B. Consistency inside D8.4

9. Major. Section 6.2, line 940: "with 5 % of the cement replaced by industrial by-products". This contradicts Section 3.1, line 415: "This plan states the replacement without a percentage". Section 3.2 (line 437) follows the rule. Fix: "with part of the cement replaced by industrial by-products (fly ash and ground granulated blast-furnace slag)".

10. Major. Section 2.5, table row at line 146: the target source is "GA, D8.5 (peer-reviewed)" and 10 is achieved. Section 2.5.1 (line 192) says three of the ten "are papers in the proceedings of Spanish and Basque scientific congresses, which do not state that the papers were peer reviewed". On the document's own record, the peer-reviewed count is 7, and the headline claims (lines 38, 142: "met or exceeded every … target except one") rest on counting the three. A CINEA reviewer will compare the two lines. Fix, if the GA target is peer-reviewed: Achieved "7 peer-reviewed with DOI; 3 congress papers", count the target as not met, and change line 38 to "except two: peer-reviewed publications (seven of ten, with three further congress papers) and infographics (five of six)". If the GA target is not limited to peer review, delete "(peer-reviewed)" from the source cell instead.

11. Minor. Press releases, line 158: the target is "start and milestones" (GA) and 1 is achieved. Line 322 says the start was announced by SINTEF and "that news item is counted under journalistic articles". The headline counts the target as met, but the table shows one release against a two-part target. Fix: in the Achieved cell, write "1 (milestone); the start was announced in SINTEF's news item of 1 November 2022, counted under journalistic articles". Alternatively, count the target as not met.

12. Minor. The counting rule in line 170, "an event attended counts as a conference", does not match the tables. The CINEA clustering event of 25 April 2024 (in person, Brussels) is not in the conference table (2.5.4). The joint NaturSea-PV webinar is not counted as a web event (2.5.7), although it is a webinar. Fix: state the rule as applied: "a conference is an external scientific or industry conference or fair; EU clustering events and joint project webinars are counted as joint events and workshops, not as conferences or web events".

13. Minor. ACCIONA announcement. Line 170 says it "is counted once, as the press release". However, its reprint in Global Renewable News (line 313) is one of the eight journalistic articles, and line 182 counts both the eight articles and "the ACCIONA announcement" among the 13 media mentions. Fix for line 170: "ACCIONA's own announcement of October 2024 is counted once, as the press release; reprints and reports on it in other outlets are counted as journalistic articles."

14. Minor. Line 318 says the four Spanish articles "are not in the count", but line 182 counts them among the 13 media mentions. Fix for line 318: "… and they are not counted as journalistic articles; they are counted as media mentions (reach table above)."

15. Minor. Section 3.4, line 488: "Four groups of results have no counterpart among R1–R11", but only three groups are listed (Sunlit Sea's three results; SINTEF's three methods; Clement Germany's hydrodynamic knowledge). Fix: "Three groups of results …", or add the missing group.

16. Minor. Section 4.6.2, line 747: the basis omits the end anchor sets. The breakwater note (surewave/deliverables/2026-11-23_surewave_breakwater_classes_nearshore.md line 163) gives "Cost = units × 20 m × installed €/m + end anchor sets + mobilisation". With only the stated basis, the demonstrator rows cannot be reproduced. For 50 kWp, 70 m × €1,150 + €40,000 = €0.12M against a €0.04M PV plant gives about 74 % without other uses, but the table says "about 80 %". If item 2 is not applied, add "and end anchor sets" to the bullet. If item 2 is applied, this finding falls away.

17. Minor. Section 8 vs Section 13. Section 8 (line 1097) places the request to include the EU funding statement in a standard under the same four-year, call-conditional duty. Section 13 (line 1188) lists it under "Without a time limit in the Grant Agreement". Fix: pick one, following the GA text (decision D17 puts the standards duty in the four-year group), and make Section 8 match Section 13 word for word.

18. Minor. Timing of the Clement Germany agreement. Line 898 says the engineering and supply agreement comes "before the first site with a breakwater class (about 2030)". Lines 845, 975, 1113 and 1159 say it is sought in 2027, and line 975's indicator is "Agreement concluded" in 2027. Fix for line 898: "Engineering and supply agreement, including the access rights needed, sought in 2027 and in place before the first site with a breakwater class (about 2030)".

19. Minor. Project relation labels in Section 10. SFI BLUES (2020–2028) is "Parallel: started before SUREWAVE". FlexiShape (2021–2025) and MariSol (2020–2025) are "Earlier: started before SUREWAVE; completed in 2025". Line 992, however, says FlexiShape's reuse happened "during the project", so FlexiShape overlapped SUREWAVE. The reader cannot reconstruct the rule. Fix: add to line 1127 "Earlier: started before SUREWAVE and ended before it; parallel: running at the same time and continuing after it; follow-on: starting after it".

20. Minor. Section 3.1, line 420: "and the input confirmed the seven KERs" claims a confirmation that no source shows (requirement 3; line 412 says only that no partner proposed a KER of its own). Fix: "No partner input called for a change to the seven KERs."

21. Minor. Section 4.1, line 518: "the average tensile capacity of the redesigned hinge rose from 3.69 kN to 8.36 kN". The 3.69 kN belongs to the earlier generation, so it is not the redesigned hinge that "rose". Fix: "the average tensile capacity rose from 3.69 kN for the second-generation hinge to 8.36 kN for the redesigned, third-generation hinge, and its average compression capacity was 20.23 kN." Line 926 already has the correct form.

22. Minor. Section 4.1.1, line 534: "SUREWAVE designed one breakwater cross-section, the heavy unit for the open sea". In the class table (line 547), the same unit is the heavy class for "rough nearshore" sites up to about 1.3 m. Fix: "SUREWAVE designed one breakwater cross-section, for the open sea, in a full ring around the plant. In the classes below it is the heavy class."

23. Wording. Section 4.1.1, line 541: "plus a margin" does not say what margin. Fix: give the margin used in scripts/breakwater_classes.py (for example "plus 10 % on width"), or delete the phrase.

24. Minor. Units: MW vs MWp. Line 504 says "this plan writes MWp for the plants it assesses". The text nevertheless has "the 2 MW North Sea farm" (lines 440, 481, 877, 1015), "at least 5 MW" and "about 4 MW at a nearshore site in Germany" (line 1139) and "Mediterranean 10 MW" in places. Fix: use MWp for plant sizes everywhere except in quoted titles and in "10 MW-class" (a contract class, defined once).

25. Minor. Currency units in a euro document. Line 608 gives "74–82 øre/kWh … against 24–47 øre/kWh", and line 760 gives "4.84 ct/kWh". Fix, at the plan's rate (FP line 135: 0.70 NOK = €0.060): "about €0.063–0.070/kWh in price areas NO1, NO2 and NO5 …, against about €0.021–0.040/kWh in NO3 and NO4 (NVE, …; converted at about 11.7 NOK per euro)". For line 760: "above the average award of €0.0484/kWh".

26. Wording. Number format. The document uses "€5.5 million" (lines 34, 464, 1238), "€7.3 million" (line 32) and "€5.5M", "€7.3M", "€0.75M" (lines 717, 797 and elsewhere). Line 32 writes "a payback of ten years", while the table at line 717 has "10 years". Fix: use one form (for example €5.5M in tables and "€5.5 million" in prose, applied everywhere) and "10 years".

27. Wording. Range notation: "R8, R9, R10" (lines 429, 441) vs "R8–R10" (line 457). Fix: "R8–R10" throughout, or the full list throughout.

28. Minor. One name for the planning tool. The draft uses "site-planning tool" (lines 436, 476, 522, 553), "planning tool" (lines 923, 1079), "web planning tool" (line 923), "planning platform" (lines 413, 835, 930, 1132), "commercial web platform" (line 925) and "planning software" (line 892). A non-native reader will take these to be different products. Fix: "site-planning tool" everywhere; describe it once as "web-based" in 6.1.

29. Wording. Partner names: "Clement" and "Clement Germany" alternate within sections (lines 890, 898, 961–978, 1081, 1103, 1214, 1227). Fix: write "Clement Germany" at the first mention in each section and in tables. The short form "Clement" is fine in running text once it has been introduced.

30. Wording. Workshop name: "Second business-planning workshop" (line 123) vs "the second business-plan workshop" (lines 764, 1226). Fix: "second business-planning workshop" throughout.

31. Wording. EPC is spelled out and defined three times: line 27, line 649 (table) and line 766. Fix: define it once, in the executive summary, and repeat the definition once in Section 4.4 for readers who start there. Delete it at line 766.

32. Wording. Repetition between sections. Each statement below repeats with no new information:
   - "SuRE grew out of contacts made through the Stakeholder Advisory Board": lines 40, 295, 927, 1131.
   - "another board member … joint initiatives": lines 295, 927.
   - "Guillaume Kegelart … co-authored the wave-basin paper": lines 188, 930, plus the author lists at lines 197, 476, 1016.
   - Access-rights deadline 31 December 2027: lines 886, 905, 1114, 1160, 1183.
   - The full TRL and validation sentence: lines 19, 508–510, 870, 1236. Per D2 the wording is identical, which is fine, but line 870 repeats the whole validation sentence inside a table cell.

   Fix: keep each statement in its home section (SuRE and the Board: 2.5.10 and Section 10; Kegelart: 2.5 "own share"; access rights: Section 9; TRL: 4.1). Elsewhere, refer to it ("(Section 9)"). In line 870, shorten the cell to "No pilot funding; TRL as in Section 4.1; the integrated system has had no long-term exposure at sea".

33. Wording. Section 4.9, 2027 bullet (line 845) runs Q1, Q2, Q3, Q4, Q4, and then "KER1 profile on the Horizon Results Platform in Q1". Fix: move "KER1 profile on the Horizon Results Platform in Q1" to directly after "first equity round closed in Q1".

## C. Sentences a non-native reader will stumble on

34. Wording. Line 27: "A field demonstrator follows in 2028–2030 if the EIC Transition proposal is funded, and the first commercial site with a breakwater class about 2030, expected at an inland lake or inner water exposed to wind waves." The second clause has no verb. Fix: "If the EIC Transition proposal is funded, a field demonstrator follows in 2028–2030. The first commercial site with a breakwater class is expected about 2030, at an inland lake or inner water exposed to wind waves."

35. Wording. Line 38: "SUREWAVE met or exceeded every dissemination and communication target in the table of Section 2.5 except one: five of the six infographics." Here the exception is named by its result, not by the target. Fix (subject to item 10): "SUREWAVE met or exceeded every dissemination and communication target in the table of Section 2.5 except infographics, where five of six were produced."

36. Wording. Line 56: "Sections 7–13 cover intellectual property, standardisation, exploitation agreements, earlier, parallel and follow-on projects, the use of Horizon Europe support, …". The embedded "earlier, parallel and" breaks the list. Fix: use semicolons: "Sections 7–13 cover intellectual property; standardisation; exploitation agreements; earlier, parallel and follow-on projects; the use of Horizon Europe support; consortium-level risks; and reporting and post-project obligations under the Grant Agreement." This also removes "Articles 16 and 17", since Section 13 also covers Article 21 and the Data Sheet.

37. Wording. Line 142: "for four indicators that neither document quantifies, the WP8 lead set them (WP8)". Fix: "The WP8 lead set the targets of four indicators that neither document quantifies; these are marked WP8."

38. Wording. Line 286: "According to the draft agenda, Thomas Pehlke (Clement Germany) moderated eight sessions". The past tense states as fact something that only a draft agenda shows. Fix: "The draft agenda has Thomas Pehlke (Clement Germany) as moderator of eight sessions, …".

39. Minor. Line 386, website. The paragraph mixes page views and visits ("about 3,000 page views … up by about 27,000 %"), does not say when the target was passed, and "were then stopped" is ambiguous. Fix: "Sunlit Sea measured visits to surewave.eu with the web analytics service Matomo from late August 2023 to the end of 2024. Until March 2024 the site had up to about 35 visits a week, about 800 in total at month 18. After a promotion campaign started around 29 May 2024, page views rose to about 3,000 in the first reporting period of the campaign. By the end of 2024 more than 50,000 visits were recorded. Sunlit Sea then ended the analytics subscription, so the figure rests on its own record." Delete the 27,000 % figure: it reads as a misprint.

40. Minor. Line 390: "OpenAIRE lists 37 SUREWAVE results". The bullets that follow (18 + 3 + 13 deliverables + 14 publications and preprints + 2) add up to more than 37, so a reader takes them for a breakdown that does not add up. Fix: "OpenAIRE lists 37 SUREWAVE results (November 2026). The open results are held in these places:".

41. Wording. Line 504: "the materials report of Clement Germany and the economic assessment D7.4 use 10 MWp, and a 2 MWp version 173 m across". Fix: "the materials report of Clement Germany and the economic assessment D7.4 use 10 MWp, and they also define a 2 MWp version with a ring 173 m across."

42. Wording. Line 510: "The EIC Transition proposal (Section 10) starts from TRL 4 for this reason." This is close to the banned conclusion connectives. Fix: "The EIC Transition proposal (Section 10) starts from this TRL 4."

43. Wording. Line 632: "uses much less fossil resources". This is ungrammatical ("resources" is countable). Fix: "uses far fewer fossil resources".

44. Wording. Line 741: "The baseline site proposed for the EIC Transition demonstrator, the exposed-site step, is such a lake". The apposition is hard to parse. Fix: "The baseline site of the EIC Transition demonstrator, the step to exposed sites, is such a lake (Section 10)."

45. Wording. Line 760: "A first plant of about 1 MWp is a reference rather than a margin case." Fix: "A first plant of about 1 MWp serves as a reference and earns little margin."

46. Wording. Line 610: "losses of 0 to 12–13 %". Fix: "losses of up to 12–13 %".

47. Wording. Line 886: "The small wavebreakers at the first reference plant, a Norwegian port, in 2027 are bought for that plant …". Fix: "The small wavebreakers at the first reference plant (a Norwegian port, 2027) are bought for that plant and are part of its cost, which Sunlit Sea carries as owner."

48. Wording. Line 894: "Each owner is paid once, when and where its result is used". "Once" can be read as a single payment over the whole partnership. Fix: "Each owner is paid where its result is used, for that use; the kit price carries no partner charge …".

49. Wording. Line 1127: "SUREWAVE ran from 1 October 2022 to 31 December 2026." The document is dated November 2026, so the project has not yet ended. Fix: "SUREWAVE runs from 1 October 2022 to 31 December 2026."

50. Wording. Line 1103: "Clement is an active participant in national and international committees". "Active" is a selling word. Fix: "Clement Germany takes part in national and international committees and brings in its SUREWAVE experience."

51. Wording. Line 237 and line 267: "year not given" for EERA DeepWind. Fix: "year not reported by the partner".

## D. Tables, headings and layout

52. Wording. Line 99 and lines 104–105: the partner-input table names individuals for three partners only, and the ACCIONA cell includes the internal detail "uploaded by Aurora María Casado Barrasa to the consortium's shared folder". Fix: give every row the same content ("Exploitation summary"; Ceit "Exploitation summary, in two parts"; SINTEF "Exploitation plan") and drop the names and the folder.

53. Wording. Line 311: the Partner cell reads "MARIN tests". Fix: "MARIN".

54. Wording. Lines 253 and 259: in a column where every other row names a person, the presenter is only "Ceit" or "IFEU". Fix: name the presenters, or write "Ceit (presenter not recorded)".

55. Wording. Line 768: the first header cell of the table is empty ("| | 2027–2029 | 2030–2031 |"). Fix: "| Figure | 2027–2029 | 2030–2031 |".

56. Wording. Lines 718–719: Payback "–" for the Baltic Sea and the North Sea. Fix: "not reached (NPV ≤ 0)", or a footnote line under the table.

57. Wording. Lines 752–754: the share column header is 13 words long, and the 50 kWp cell mixes a share with a funding note ("about two thirds; funded by the demonstration grant"). Fix: in the lead-in, define "share = breakwater cost / (PV plant + breakwater)". Use the headers "Share, half carried by other uses" and "Share, no other uses", and put "The demonstrator breakwater is funded by the demonstration grant" under the table.

58. Minor. Section 3.2 table (line 434): eight columns with very long cells. It will be unreadable in a portrait Word page. "Proposal results" and "Treatment" repeat the tables in 3.1 and 3.3. Fix: delete those two columns (they are in 3.1 and 3.3), or split the table into "Owner, result, maturity" and "Route, relation to KER1". The 3.4 table (line 474) and the 4.10 table (line 868) have the same problem in their long cells. Check the rendered docx.

59. Wording. Heading levels: "# SUREWAVE Deliverable D8.4" is followed by "## Exploitation Pathways and Definitive Business Plan" (line 3). The subtitle thus sits at the same level as "## 1. Purpose and scope" and the unnumbered "## Confidentiality notice" and "## Executive summary". In a Word navigation pane the subtitle shows as a section. Fix: make the title one H1, "SUREWAVE D8.4 Exploitation Pathways and Definitive Business Plan", or render the subtitle as a plain line (it goes on the template cover page anyway).

60. Wording. Lines 718 and 735: the self-reference "(Section 4.6)" appears inside Section 4.6.1, pointing to its own parent section. Fix: "(table above in Section 4.6)" or delete it.

Findings: 4 major, 22 minor, 34 wording.
