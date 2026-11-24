# T150 round 2 – fact-check of d84_merged.md (persona: fact-checker)

Checked 23 November 2026, late evening. I read d84_merged.md in full (1,420 lines) and compared it with d84_merged_r0.md. Almost every paragraph changed (difflib: 739 output lines of changes), so I checked all the text again, with most attention on figures and attributions that are new or reworded. Sources: the repo primary files (paths below are relative to C:\dev\src\sure-d61); live Crossref, fetched today for all 11 DOIs (citation counts summed again); the live CORDIS results page and the CORDIS XML export for 101083342, fetched today; the live OpenAIRE API (relProjectCode=101083342, 37 results); and the CORDIS, Prosjektbanken and SINTEF snapshots in scratchpad_t150\web. I re-ran both models: `scripts/hrb_financial_model.py --md` (PYTHONIOENCODING=utf-8) and `scripts/breakwater_classes.py`. I also recomputed the 45° lake table of 4.6.2 with `breakwater_classes.coverage(kwp, 45, "light", host_share)` against the €0.83/W kit-plant capex in the model's unit-economics table.

Line numbers refer to d84_merged.md.

## Findings

### Major

1. Major. Cover line L5 says "Coordinator: SINTEF AS · Project duration: 1 October 2022 to 31 December 2026 (51 months, including a three-month extension) · Due in the Grant Agreement: month 36". The same coordinator is named in Sections 13 and 10.
   What is wrong: CONFLICT with the public record. The CORDIS project page and its XML export (CORDA data, fetched 23 Nov 2026, page last updated 5 Nov 2026) give these values:
   - coordinator: SINTEF MANUFACTURING AS;
   - duration: 48 months, end date 30 September 2026;
   - ACCIONA's legal name: ACCIONA CONSTRUCCION IBERIA SA.

   The Grant Agreement in the repo is the signed 2022 version, which gives a different set:
   - coordinator: "SINTEF AS (SINTEF), PIC 910945140" (surewave/background/2022-09-20_surewave_grant_agreement_101083342.md L25–26);
   - "Project duration: 36 months" (GA L330 and L3613);
   - ACCIONA as "ACCIONA CONSTRUCCION SA" (GA L35);
   - D8.4 at month 36 (GA L5358–5366).

   So the GA has since been amended at least once: the duration went from 36 to 48 months, before the three-month extension to 51. CORDIS suggests the coordinator entity changed as well. The deliverables confirm the amendment. D1.8 ("IPR management plan M36") and D8.3 both have a due date of 30 September 2026, which is month 48 (2026-09-30_surewave_d1.8_ipr_management_plan_m36.md L26; deliverables/2026-09-28_surewave_d8.3_technical_brochure.meta.yaml due_date). Under the 2022 GA, month 36 is September 2025, so a reader who sees "month 36" will think D8.4 is more than a year late.
   Fix: check the current GA in the Funding & Tenders Portal before submission, then do three things.
   - Use the coordinator's legal name as the amended GA gives it. Keep "SINTEF AS" only if the Portal shows it. CORDIS may be wrong, but its data is the public record the reviewers see.
   - Write the due date as a date, for example "Due in the Grant Agreement: 30 September 2026", if the amended GA gives it.
   - Keep "51 months" and write "as extended" rather than spelling out the extension history (that respects D1).

   No source in the repo resolves which entity is correct. This is an owner check, not a text guess.

### Minor

2. Minor. 2.5.10 L326: "D2.4 names six member organisations, most with several roles: a chair …, two project developers …, a floating PV technology provider, a regulatory authority (the Norwegian Coastal Administration) and an environmental research institute (Wageningen University and Research)."
   What is wrong: D2.4 names seven organisations, and the text says so: "most of the 7 representatives fulfil multiple roles". The seventh is Solenergiklyngen (Katja Kerschke), listed under "Policy-makers" (2024-04-22_surewave_d2.4_stakeholder_advisory_board.md L209, L259–261). This corrects my own round 1 finding 7, which missed the Policy-makers entry and so caused the error.
   Fix: "D2.4 names seven member organisations, most with several roles: a chair who also covers finance and insurance, two project developers (one of them also covering finance, insurance and end users), a floating PV technology provider, a regulatory authority (the Norwegian Coastal Administration), an environmental research institute (Wageningen University and Research) and a Norwegian solar energy cluster (Solenergiklyngen) for policy." Under D16, BayWa stays unnamed, and naming the cluster does not conflict with that.

3. Minor. 2.5.23 L436: "The public deliverables on CORDIS: D2.1, D2.4, D3.1, D3.3, D3.4, D4.3, D6.1, D6.2, D7.3, D7.5, D8.1, D8.2 and D8.5."
   What is wrong: the live CORDIS results page (https://cordis.europa.eu/project/id/101083342/results, last update 5 November 2026) lists one deliverable under "Documents, reports (1)": D7.6, the report on integrated sustainability assessment. The XML export has the same single entry. The 13 deliverables in D8.4's list are the undated deliverable records in OpenAIRE (live API, 37 results: D2.1, D3.1, D2.4, D3.3, D8.2, D6.1, D8.1, D7.3, D6.2, D7.5, D3.4, D8.5, D4.3). D7.6, which is on CORDIS, is not in D8.4's list.
   Fix: "OpenAIRE lists 13 public deliverables from the EU project records (D2.1, D2.4, D3.1, D3.3, D3.4, D4.3, D6.1, D6.2, D7.3, D7.5, D8.1, D8.2 and D8.5); the CORDIS results page itself shows D7.6 (November 2026)."

4. Minor. 3.4 R3 L526 says "biofouling on more than 85 % of the evaluated surfaces", and 6.2 L1081 says "Biofouling covered more than 85 % of the evaluated surfaces."
   What is wrong: the preprint says "Biofouling coverage exceeded 85% on all evaluated surfaces, with mussel-dominated layers up to 35 mm thick" (Preprints 202611.1592 abstract, Crossref). Every surface was more than 85 % covered. D8.4's wording reads as if 85 % of the surfaces had any fouling.
   Fix: "biofouling covered more than 85 % of every evaluated surface, with mussel layers up to 35 mm thick".

5. Minor. 4.3 L637 and L657: "BlueNewables' 1 MW demonstrator of two 500 kW platforms at the Port of Valencia, in testing since October 2026 (pv magazine, 2026)".
   What is wrong: the research notes give a different timeline. The first 500 kW unit arrived on 13 July 2026 and was activated (Valenciaport; pv magazine, 14 July 2026). An October 2026 report, from CruiseMapper and not pv magazine, describes the full 1 MW as installed and in testing (surewave/background/2026-11-14_hrb_business_plan_research/competitors.md L12, L89, S12–S14). So testing did not start in October, and the October claim is not pv magazine's.
   Fix: "BlueNewables' 1 MW demonstrator of two 500 kW platforms at the Port of Valencia: the first unit in testing since July 2026 (pv magazine, July 2026), the full 1 MW reported in testing in October 2026".

6. Minor. 4.6 L831: "The electricity sale price is €0.12/kWh, the target price set in the SUREWAVE application".
   What is wrong: UNSUPPORTED as phrased. Neither Annex 1 Part B, nor the proposal file, nor the GA contains a €0.12/kWh price. The proposal sets an LCOE target of €54/MWh against a reference of €161/MWh (Annex 1 L135, L654). D7.4 itself says "the target price indicated in the Surewave planning and application process" (2025-09-05_surewave_d7.4_economic_assessment.md L343).
   Fix: "The electricity sale price is €0.12/kWh, which D7.4 takes as the project's target price".

7. Minor. Reach table L214: "more than 12,000 in 2024, within the more than 50,000 recorded by the end of that year".
   What is wrong: UNDERSTATED. Tracking began in late August 2023, and the site had about 800 visits by March 2024 (L428). So almost all of the more than 50,000 visits fell in 2024: at least about 49,000 (2.5.22; KPI record §17).
   Fix: "about 800 visits from late August 2023 to March 2024; about 49,000 or more in 2024, of the more than 50,000 recorded by the end of that year".

8. Minor. 2.3 L141: "She rated the roadmap as very good and asked for a timeline per activity."
   What is wrong: the rating was given row by row, not for the roadmap as a whole. The expert rated Actions "Very good. Please also include the timeline per each activity", Milestones "Excellent", and Costs, Revenues and Other sources of coverage "Fair enough" (2026-11-13_hrb_expert_feedback_exploitation_roadmap_ker1.md L36, L67, L74, L81, L92).
   Fix: "She rated the roadmap's actions as very good, asking for a timeline per activity, its milestones as excellent, and its costs, revenues and other funding sources as fair."

9. Minor. 2.5.9 L320: "The draft agenda has Thomas Pehlke (Clement Germany) as moderator of eight sessions" and "invited 27 guests".
   What is wrong: (a) the agenda makes Pehlke moderator of the workshop as a whole. Its nine rows are a welcome, seven talks and a Q&A (2026-09-09_surewave_final_workshop_invitation_and_agenda.md L15–27). (b) The sources disagree on the invitee count. The invitation file says "27 guests invited" (L10), while the KPI record says the invitation went "to 26 recipients" (2026-11-19_surewave_wp8_kpi_verification.md L154). That conflict is not flagged.
   Fix: "The draft agenda has Thomas Pehlke (Clement Germany) as moderator, with seven talks by speakers from …". Keep 27, the organiser's own figure, and correct the KPI record.

10. Minor. Section 3.4 R3 and R4, and 3.2 KER2 (L485, L526–527): the delivered densities are not compared with the targets.
    What is wrong: UNDERSTATED under requirement 4, because the text leaves out two targets that were missed.
    - D4.1's requirement for the LWAC shell was 45 MPa and a dry density of at most 1,900 kg/m³ (2024-01-18_surewave_d4.1_design_characterization_circular_materials.md L223–227). ACCIONA's LWAC exceeds the strength (68 MPa) but, at 1,950 kg/m³, also exceeds the density limit.
    - The CLC reached 365 kg/m³, against the proposal's 200–300 kg/m³ (Annex 1 L204) and D4.1's requirement of "around 300 kg/m³" (D4.1 L599). R4 gives the proposal figure in the left column and 365 in the middle column without saying the target was not met.

    Fix, R3: "LWAC (68 MPa against the required 45 MPa; 1,950 kg/m³, above D4.1's limit of 1,900 kg/m³)".
    Fix, R4: "CLC at 365 kg/m³, above the proposal's 200–300 kg/m³ and D4.1's requirement of about 300 kg/m³".

11. Minor. 4.1 L556: "the transition element, a floating PVC pipe between breakwater and array attached with elasticated ropes, designed by Clement Germany (D3.3)".
    What is wrong: D3.3 specifies a floating round pipe of Ø219 mm, with polypropylene multifilament ropes of Ø30 mm to the breakwater and Ø16 mm to the PV array, pre-tensioned at about 3 kN (2023-12-08_surewave_d3.3_final.md L1108–1130). "Elasticated" suggests elastic cords, which D3.3 does not specify.
    Fix: "a floating pipe (Ø219 mm) between breakwater and array, connected with pre-tensioned polypropylene ropes, designed by Clement Germany (D3.3)".

12. Minor. 4.4 L716 dates phase 1 to "2027–2029", and 4.7 L888 says "From 2030 it sells mainly kits with site engineering."
    What is wrong: the model has EPC revenue of €852k in 2030 and €1,400k in 2031 (base case income statement, `hrb_financial_model.py --md`). The value chain analysis has "Phase 1 (2027–2029, deliveries to 2031)" (deliverables/2026-11-23_surewave_hrb_value_chain_ker1.md L9). The 4.4 table hides those later EPC deliveries.
    Fix: in the 4.4 table, "2027–2029 (EPC deliveries to 2031)". 4.7's "mainly" is correct and can stay.

13. Minor. 4.2 L626: "the technical lead is responsible for product development, sales and administration."
    What is wrong: the companion documents disagree. The business plan says exactly this (deliverables/2026-11-14_surewave_hrb_business_plan_ker1.md L20). The value chain analysis, written later, says "The CEO holds the design and casting knowledge; the technical lead holds the planning tool, sales, projects and administration" (value chain L32).
    Fix: align with the newer value chain: "the CEO invented Generation 1 and holds the design and casting work for Generation 2; the technical lead is responsible for the site-planning tool, sales, projects and administration". Update the business plan the same way.

14. Minor. 3.1 L457, 3.4 R6 L529 and 4.10 L1005: "D5.1 cut mooring-line mass by 34–59 %".
    What is wrong: the range is correct from D5.1 Table 9, where the optimised-to-reference mass ratio for the 2 MW North Sea case is 0.41 (2024-04-16_surewave_d5.1.md L1490–1530). But D5.1's own summary says "34-56%" (L1774) and "nearly 60%" for that case (L1472), so a reviewer comparing summaries will see a mismatch.
    Fix: at the first use (3.1), add "(D5.1, Table 9)".

15. Minor. 4.1 L581: "Its mean compressive capacity was 20.23 kN, which D6.3 expects to avoid the early buckling of the first generation."
    What is wrong: OVERSTATED attribution. D6.3 says the new connection "was designed by SUNLIT Sea, in order to avoid early buckling of the first generation" (D6.3 L261). D6.3 states a design intent; it does not conclude that the measured 20.23 kN avoids buckling. The basin evidence comes separately from D8.3.
    Fix: "Its mean compressive capacity was 20.23 kN (D6.3); the redesign was made to avoid the early buckling of the first generation."

16. Minor. 4.3 L653: "Fred. Olsen 1848 (pretensioned rope mesh): pilot stage; DNV completed a technical review against DNV-RP-0584 for significant wave heights up to 3.5 m (DNV, 2026)."
    What is wrong: UNDERSTATED. The research notes record a DNV Statement of Conformity to DNV-RP-0584 for a 3 MW BRIZO island at Hs up to 3.5 m (pv magazine, 3 September 2026), and separately a DNV technical review of the design methodology (DNV news, July 2026) (competitors.md L9, L63, S4, S5). The certification-type evidence is what hypothesis 2 in 4.3.1 relies on.
    Fix: "pilot stage; DNV Statement of Conformity to DNV-RP-0584 for a 3 MW island at significant wave heights up to 3.5 m, and a DNV technical review of its design methodology (DNV, July 2026; pv magazine, September 2026)".

### Wording

17. Wording. 2.3 L141: "the alternative solutions, timing and IP strategy as fair." The expert wrote "Fair enough." (2026-11-13_hrb_expert_feedback_characterisation_table_ker1.md, three rows), which in English means acceptable. That is not quite a rating step below "good". Write "as acceptable ('fair enough')", or keep "fair" consistently with finding 8.

18. Wording. 2.5.1 table L234: "*Revista Española de Mecánica de la Fractura* 9, 15". Write "9 (2025), p. 15" (KPI record L66).

19. Wording. 4.6.1 L851: "about 24 % more with the lightweight-aggregate shell and about 76 % more with the high-performance-concrete shell". Both percentages are correct against the conventional breakwater (€1,513,384 and €2,146,102 against €1,221,594; D7.4 L563–572), and both SUREWAVE variants have a cellular-concrete core. Add "(both with a cellular-concrete core)", so the reader does not confuse the first figure with D7.4's "LWAC shell, EPS core" variant, which is only about 10 % more.

## Rejections in my area: do they hold?

- disp_A A#3 (coordinator stays SINTEF AS, D1). Holds against the 2022 GA in the repo. CORDIS/CORDA now names SINTEF MANUFACTURING AS, and the GA has been amended (duration 36 → 48 months). It therefore holds only if the current Portal GA still names SINTEF AS. See finding 1; owner check needed.
- disp_A A-gap11, disp_E ledger_E#5, #108, W21 (no extension history; end 31 December 2026). These hold as decision D1, but the "month 36" due date that goes with them needs the amended GA (finding 1).
- disp_B B#78 (spelling NaturSea-PV; evidence-file URL). Holds.
- disp_B B#88 (BayWa not named, D16). Holds. Naming Solenergiklyngen (finding 2) is a separate matter and does not conflict with D16.
- disp_C C#14 (no "factor 2–3", D3). Holds. 6.5's "a factor of 3 around a peak period of 4 s" is D5.1's hinge-load statement (D5.1 L846), not the banned mooring figure.
- disp_C C#64, C-gap#6; disp_D D#71, D gap 5 (D7). Hold as owner decisions.
- disp_E ledger_E#79; r1disp_D r1_cinea#F24 and r1_coord#12 (no Ceit in the hinge redesign). Hold. D5.3 L1004 says Ceit identified the hinges as most failure-prone and that their modelling would come with the new hinge report, and 3.1 now explains this.
- r1disp_A r1_partners#A5 and r1_owner#17, and r1disp_E r1_partners#A5 (figures rejected as "final technical report only"). These hold only in part:
  - the chloride-migration coefficients 0.4–0.9 × 10⁻¹² m²/s are in D4.2 Table 5 (2024-07-31_surewave_d4.2_lab_testing_breakwater_prototype.md, Table 5 after L455; "extremely highly resistant", L477), so the rejection for R3 does not hold. 6.2 already uses them; R3 can cite them too;
  - the 18 LWAC trial mixes (samples 1–18, D4.1 Tables 1–2) and the 2 HPC trial mixes ("Two trial mixes of HPC were cast", D4.1 L554) are in D4.1, so those rejections do not hold either;
  - the 76 % and the 380 vs 350 kg/m³ comparison: not found in any deliverable, so those rejections hold.
- r1disp_A r1_owner#15 ("450 kN rating" rejected as newsletter-only). Does not hold. D6.1 L783 says: "The ultimate strength was found to be 402kN, in agreement with the rated strength of 450kN". The KER4 cell can add "against a rated strength of 450 kN (D6.1)".
- r1disp_A r1_owner#19 (0.4 transmission not in D3.2 text). Does not hold. D3.2 L1705: "Critical wave periods for the PV-system are between 1 and 3 seconds. These waves are reduced by the FB to at least 40% of the incident wave height." It is already used in 6.3 (r1disp_E). KER3 in 3.2 and R2 in 3.4 may use the same wording.
- r1disp_E r1_partners#S2 ("19 risk indicators" rejected as final-report only). Superseded. The preprint 202611.1173 abstract (Crossref) says "Nineteen technological risks were evaluated", and R11 already cites it. The rejection no longer applies. 6.7 can add it with the preprint as source.
- r1disp_A r1_partners#S3 (1,030 mixtures) and r1_partners#S4 / r1disp_E S4 (87 % / 97 %). Hold. These figures appear only in the final technical report working copy, not in D5.1, D5.2 or the Energies 17(19) abstract.
- r1disp_E r1_partners#C2 (Gijón prototype built to Clement's geometry). Holds. D4.3 says only that the mixes followed Clement's production requirements (D4.3 L413).
- r1disp_E r1_partners#M3 (installed-cost sentence). Holds.
- r1disp_C r1_facts#12 (NVE NO3 and NO4). Holds; the dispatcher's curl fetch of the NVE Q4 2025 report gives NO3 47.1 and NO4 24.1 øre/kWh.
- r1disp_C r1_facts#23 and r1_cold#65 (no bottom-plate material). Hold (docs/project_facts.md L36).
- r1disp_C r1_cold#3 (no float generation for the basin model). Holds.
- r1disp_D r1_cold#66 (IFE as deputy). Holds; the risk assessment and 4.8 say "IFE for structural simulation".
- r1disp_D r1_writing#6 (EDP named). Holds; EDP R&D / CNET is an applicant in the EIC proposal (proposal L26).
- r1disp_E r1_cinea#21 (strategic assets under the four-year limit). Holds (GA Annex 5).
- r1disp_B 36 (D8.5 "April 2024"). Holds (D8.5 actual delivery 29/04/2024).
- r1disp_B 24 and F5 (EERA DeepWind "Year not reported", partner report). Hold (KPI record L111, L216).
- r1disp_B 4 and r1disp_A r1_owner#4 (infographics 5 of 6). Hold as D10r.

## Claims checked and found correct (ledger, brief)

| # | D8.4 line | Claim | Source | Status |
|---|---|---|---|---|
| 1 | 17, 451 | Project started at TRL 2–3 | Annex 1 L149 | OK |
| 2 | 17, 568 | D7.6 (Nov 2025): integrated concept at TRL 5 | D7.6 L759 | OK |
| 3 | 569, 1308 | EIC: TRL 4 starting point; interim report 1 Apr–31 Oct 2024; long-term grid-connected operation not demonstrated | EIC proposal L36–38, L134 | OK |
| 4 | 1308 | EIC: 50–300 kWp; commissioning month 22; ≥12 months of operation; DNV statement of conformity by month 34; lump sum about €2.5M; letter of intent 8 Sept 2026 | EIC L72, L369, L318, K1, K8, L167 | OK (K8 gives month 34; milestone MS6 gives month 36: an inconsistency inside the proposal) |
| 5 | 861, 1308 | 1–5 MWp "immediately after completion" (summary) and "within 12–24 months" (exploitation plan) | EIC L68, L254 | OK |
| 6 | 30, 833–839 | D7.4 v2.0 (20.11.2026): Med €7.3M / 15.6 % / €0.076 / 10 years; Baltic ≈€0 / 8.5 % / €0.120; North Sea −€5.8M / 3.4 % / €0.173; v1.0→v2.0 changes; request for revision 16 Oct 2026 | D7.4 L58, L336–340, L486–500 | OK |
| 7 | 841, 850, 1005, 1011 | €212/kWp breakwater and pontoons; €9.75M / €940/kWp for 10,375 kWp; OPEX €17.4/kWp; NPV €20.8M at 4 %; HPC LCOE €0.085; exclusions | D7.4 L810–828, L857, L1100–1120, L1146, L466–480 | OK |
| 8 | 457, 488, 1167 | Mooring −34 %/−42 % (10 MWp), −56 %/−59 % (2 MWp); Baltic ×3.16 and ×2.05 | D5.1 Table 9 | OK (see finding 14) |
| 9 | 1166 | Horizontal hinge loads cut by about a factor of 3 around Tp 4 s, less than 50 % for the largest farm; 3D CFD too demanding | D5.1 L846, L84 | OK |
| 10 | 603 | Array hinge loads peak in the ≤3 s band | D5.1 L538, L558 (peak at 1.6 s in regular waves) | OK |
| 11 | 579–583, 956 | 3.69 kN; 2.04/8.36 kN; 20.23 kN; 2.5×10¹¹ vs 7.88×10⁸ cycles; 6.9 kN; 1–2 mm gaps; 1.88 m; 37 vs 14 kN; 34/33/40/54 kN; "could not be fully validated" | Preprint 1612 abstract; D6.3 L285, L435, L464, Table 4, L739, L841, L849–863; D7.6 L689, L721, L761–767, L1134; preprint 1173 abstract | OK (see finding 15) |
| 12 | 582 | Second campaign used to validate the 2 MWp model | Energies 19(7) full text, 2026-03-25_bunnik… L122 | OK |
| 13 | 206 | 41 citations of the seven DOI papers | Crossref, 23 Nov 2026: 23+5+11+2+0+0+0 | OK |
| 14 | 229–246 | Bibliographic data, authors, dates of the 10 papers and 4 preprints; preprint 1 v1 → v2 on 14 Oct 2026 | Crossref (11 records) | OK |
| 15 | 349, 362 | SINTEF news article 1 November 2022 | SINTEF page datePublished 2022-11-01 (web/sintef_news.html) | OK. The KPI record L241 gives 27 Mar 2023, which is the page's dateModified; correct the KPI record, not D8.4 |
| 16 | 892–935 | All 4.7 figures (revenue ranges, margins, EBITDA, scenario table, volume split 13/15/72 %, sensitivities −€3.6M / −€2.4M / €0.9M / €0.4M / −€5.6M, equity €0.5M / €1.0M, wavebreaker €0.1M / €0.05M, breakwater €0.9M, cash +€0.7M / +€0.9M, 7 and 9 MWp break-even, 27 % support) | Model run | OK |
| 17 | 604–622 | Breakwater classes: Hs, fetch, sections, 30/73/123 t, natural periods; cost halves from 3.2 to 10 MWp; about 10× at 350 kWp | breakwater_classes.py | OK |
| 18 | 872–878 | Lake table 80 %/⅔, 46/30, 25/15, 11/6, 4/2 % | coverage(…,45,"light") with €0.83/W | OK |
| 19 | 882 | €0.10/kWh at 1 MWp half carried; German tender €0.048 (4.84 ct) | model table; financial plan L332 | OK |
| 20 | 946–968 | 26 risks; every grade and zone | risk assessment L9–34 | OK |
| 21 | 983–992 | M1–M10 and dates | roadmap L68–77 | OK |
| 22 | 754–781 | Nine steps; 8–10 parties; single points of failure | value chain L16–39, L26 | OK |
| 23 | 125–137 | Booster: applied 30 Sept, kick-off 2 Oct, 18 Oct, 23 Oct written feedback, 11–12 Nov, 13 Nov, 15 Nov (sections 2–5), IA service from January 2027, BOSAT >3 in all dimensions | kickoff prep L7, L11; pillars training L3; cover e-mails; meeting summary L11–14, L97 | OK (see finding 8) |
| 24 | 113–121 | Partner input dates and result counts (27); template request of 29 Sept | partner files; Ceit L3 | OK |
| 25 | 46, 524–534, 998–1011 | Proposal figures: 850→350 kg/m³, 200–300 kg/m³, TRL targets, 25 MW pilot 2025–2027, 2030–2032 and 2035, 1,240 MW, 25 plants, €50M, €967.2M, 1,335,608, 3,460, 70,000 t, 1,736,000 t, €0.054/€0.161, 1,645 kWh/m², 4 %/8 %, 20/15 years, €1,560/€781, €25.4/€12.7 | Annex 1 L149–242, L583–762, L887–895 | OK |
| 26 | 1054 | Sunlit Sea task leads (2.3, 2.4, 3.1, 3.5, 7.4), D2.3/D3.1/D3.4 led by Sunlit Sea; Clement Tasks 3.2–3.4; MARIN 5.2, 6.4; Ceit 6.1; SINTEF 7.1, 7.2; IFEU 7.6 | GA L3935–4430; deliverable covers | OK |
| 27 | 1302–1306 | SuRE 1 Sep 2024 – 31 Aug 2027 (IFE); CIRCWIND 1 Oct 2024 – 30 Sep 2028; MariSol 317808 2020–2025 (IFE, UiO, Stadt Towing Tank, Kodeworks); SFI BLUES 2020–2028; FlexiShape 321508 2021–2025 (MIKO Marine) | CORDIS snapshots; Prosjektbanken snapshots | OK |
| 28 | 1309 | EUPI-PV call: title, ID, deadline 1 Dec 2026, minimum 5 MW over several zones | call text L2–58 | OK |
| 29 | 1370–1375 | Data Sheet point 6: 5/5/2/2/2/5 years | GA L535–540 | OK |
| 30 | 1289–1291, 1364 | 45/30/60 days; 15/15 days | GA L8858, L8931–8935, L8982, L9193–9200 | OK |
| 31 | 562, 999 | Ring 346 m; D3.4 7.16 MWp; 18,600 × 537 Wp; 2 MWp ring 173 m | D3.4 L518–542; Clement materials L28, L33 | OK |
| 32 | 1102 | At most about 40 % transmission in the 1–3 s band; 120 t unit limit | D3.2 L1705, L428 | OK |
| 33 | 1076–1081 | HPC 400 vs 500 kg/m³ cement with GGBFS and fly ash, 128 vs 120 MPa; 26 CLC trial mixes; D4.2 8.2→0.6 mm; chloride 0.4–0.9; D7.3 20 % clinker, 20 % coarse aggregate | D4.1 L233, L554–588, L607; D4.2 Tables 3, 5; D7.3 L935 | OK |
| 34 | 489, 1187 | 0.17 mm at 5–6 cm; ±135 Ω; 0.35–0.45 Hz; 3.40 × 1.70 × 1.05 m; four-line catenary | Sensors 24(13) abstract; preprint 1592 abstract | OK (see finding 4) |
| 35 | 532 | 598 finite element simulations | D5.5 L527 | OK |
| 36 | 1243 | D1.8: no major ownership or access-right dispute | D1.8 L91 | OK |
| 37 | 434–435 | Zenodo: 18 records, split by partner, 223/101 for the cost model; DOIs | Zenodo snapshot L3–26; KPI record L355 | OK |
| 38 | 305, 675 | SAB webinar: 31 sign-ups, about 23 at the start, 64 min; losses 12–13 %, about 10 % and 2–3 % | webinar summary L10, L50 | OK |
| 39 | 313, 306 | MARIN webinar 28 Oct 2025, 60 participants, Bunnik and van der Zanden | KPI partner responses L72, L85 | OK |
| 40 | 635–642 | IEA PVPS 8.7 GW and 7.7 GW, 90 % in Asia, NL/FR; inland TRL 8+, offshore TRL 3–5; Spain 4.45–6.48 GW; NVE 1.4 GW / 3 plants / 14 MW / 10 GW / 8 TWh; NO1/NO2/NO5 74–82 øre | market.md L11–23 | OK |
| 41 | 654–659 | Ocean Sun BV type certificate Nov 2025; Oceans of Energy about 1,400 panels Aug 2025, withdrawn; Swimsol 2.4 MW; Ciel & Terre 820 MW / 280 projects | technology_standards_ip.md L11, L129; competitors.md L8, L18; business_model_finance.md L43 | OK |
| 42 | 923 | Wood Mackenzie 2.2/1.2/1 GW by 2033; 16 MWp ≈ 3–4 % of 0.4–0.5 GW | financial plan L521 | OK |
| 43 | 697–706 | D7.6 conclusions and conditions; diesel €0.36–0.42/kWh; intermediate-scale demonstration | D7.6 L147–159, L1216, L1288 | OK |
| 44 | 99–105 | D8.5's six findings, further opportunities, Clement/Sunlit Sea demonstrator at TRL 6–7 in Germany or Norway | D8.5 L1184, L1277–1319 | OK |
| 45 | 420 | D8.3 delivered 18 Nov 2026; Clement's comments and seven CAD graphics for four figures | D8.3 meta; Clement comments L3, L14 | OK |
| 46 | 337–343, 402, 424 | Newsletter dates; posting schedule 24 Nov – 29 Dec 2026 (Tuesdays) | KPI record L342–347 | OK |
| 47 | 368–376 | Interview dates and interviewees | KPI record L262–276 | OK |
| 48 | 384–390 | Videos: 20 Nov 2023 (99 s), 29 Feb 2024 (13 s), 10 Apr 2024 (52 s), May 2024, recordings of 64 min and 1 h 36 min, May 2026 caisson reshared 6 Oct 2026 | KPI record L222–230 | OK |
| 49 | 406–416 | Factsheets, BRIDGE pp. 149–150 on 15 Aug 2023, roll-up 85 × 200 cm printed June 2023 | KPI record L172–199 | OK |
| 50 | 358 | Four Spanish articles reported by ACCIONA; dates and outlets | ACCIONA e-mail of 26 Nov 2025 L12–22; KPI record L250–258 | OK |

Findings: 1 major, 15 minor, 3 wording.
