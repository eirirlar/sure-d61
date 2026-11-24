# D8.4 review, round 2: owner persona

Persona: Sunlit Sea's technical lead and WP8 leader. The question is whether the draft shows the consortium's work and Sunlit Sea's work in full, credits it correctly, and contains nothing unfinished or embarrassing in front of CINEA or the partners.

Document reviewed: scratchpad_t150/d84_merged.md (1,420 lines), read end to end. Line numbers refer to that file. Source paths are relative to C:\dev\src\sure-d61 unless stated. Decisions D1–D34 and the round-1 revisions are treated as settled. Most round-1 owner findings have been integrated (Sunlit Sea's technical work in 6.1, the D7.4 changes in 4.6, the Zenodo records, the Booster ratings, the value chain in 4.4.1, Clement credit, the D6.3/D6.1 hinge record, and others). The findings below are what remains or what is new.

---

## Part 1. Rejections in my area: do they hold?

| Rejection (file#item) | Rejected because | Holds? | Reason |
|---|---|---|---|
| r1disp_A: r1_owner#4; r1disp_B: 4 (sixth infographic, 5 of 6) | D10r keeps 5 of 6, sixth scheduled | Holds | D10r is an owner decision. Two consequences remain, see findings 9 and 10: the reason the counting paragraph gives for the written-counts rule is wrong, and the infographic is scheduled for 15 December. It will therefore be 6 of 6 on the submission date (owner Q5), so it belongs on the list of submission-day updates. |
| r1disp_A: r1_owner#15 ("450 kN rating" only in newsletter topics, not verified in D6.1) | Not found in D6.1 | Does not hold | D6.1 states the rating twice: line 685, "An average value of 402 kN is calculated which is slightly lower than the rated capacity of 450 kN", and line 783 (Conclusions), "The ultimate strength was found to be 402kN, in agreement with the rated strength of 450kN". Add the rating to KER4 maturity (line 487) and to 6.4 (line 1139). See finding 5. |
| r1disp_A: r1_owner#17 (chloride coefficients, FTR only) | D22 | Does not hold | D4.2 Table 5 (2024-07-31_surewave_d4.2_lab_testing_breakwater_prototype.md:463–477) gives D_Cl 0.4–0.9 × 10⁻¹² m²/s and classes all mixes as "extremely highly resistant to chloride penetration" (Gjørv). r1disp_E then added the figures to 6.2 (line 1079) with D4.2 as the source, so the two dispositions contradict each other. Make 3.4 R3 (line 526) and KER2 maturity (line 485) agree with 6.2. See finding 6. |
| r1disp_A: r1_owner#19 (0.4 transmission not in D3.2 text; owner Q21) | Not found in D3.2 | Does not hold | D3.2 Summary, 2023-08-08_surewave_d3.2_floating_breakwater_design.md:1705: "Critical wave periods for the PV-system are between 1 and 3 seconds. These waves are reduced by the FB to at least 40% of the incident wave height." Clement's D8.3 review comment 5 (2026-11-18_clement_d8.3_brochure_review_comments.md) gives the reading: "The transmission coefficient is about 40 % in that range, so the wave attenuation is about 60 %." 6.3 already carries it (line 1102); KER3 in 3.2 and R2 in 3.4 do not. Owner Q21 can be closed. See finding 4. |
| r1disp_B: 6 (SAB follow-up topics) | D22 | Holds for the final report as a source | The stub "Follow-up meeting with board members in March 2025 (month 30)." (line 329) still reads unfinished. Sunlit Sea's own records (it established and ran the board) can be cited instead of the final report. See finding 16. |
| r1disp_B: 21 (SAB webinar and workshop talks as presentations) | Owner decision | Holds | The rule and its reason are stated at line 293. |
| r1disp_B: 22, r1disp_C: r1_owner#22 (reissue D8.3) | D31 | Holds | D8.4 4.1 states the differences once. See finding 7 on the D8.3 entry itself. |
| r1disp_B: 23 (final summary video) | D10r | Holds as a status | Producing it from the November 2026 clips for the 29 December post is still the cheapest way to close a named Grant Agreement exception (owner Q9). |
| r1disp_B: 24 (DeepWind "year not given") | D10 keeps it counted | Holds as a count | "Year not reported by SINTEF" (lines 269, 299) still shows an unchecked item in a final deliverable. A web search for the poster title found no public record. Ask SINTEF before submission. |
| r1disp_B: 36 (D8.5 date) | D22; D8.5 cover gives 29/04/2024 | Holds | |
| r1disp_E: r1_owner#26 (statuses that age before submission) | Updated at submission | Holds | Keep it on the submission checklist; finding 22 lists the items. |
| r1_owner#30 (3.1 step 4 lists partners' naming slips) | Not dispositioned in rejected_so_far.md | Still open | Lines 460–461 still tell CINEA that Sunlit Sea's own input called MariSol "a subsequent project" and that SINTEF's input calls FlexiShape "Mikroflexishape". See finding 15. |

---

## Part 2. Findings

### 1. Major. The Stadt Towing Tank campaign is presented as a SUREWAVE campaign; D5.1 says it was not (Sections 3.4 R1, 6.1)

Quotes. Line 524 (R1 evidence): "Basin tests: preliminary float-string campaign at the Stadt Towing Tank, provided by Sunlit Sea, with six floats in regular and irregular waves, which calibrated the linear hydrodynamic method used for the three reference sites (D8.3)". Line 1054: "Sunlit Sea provided the first wave-tank campaign, a string of six floats at the Stadt Towing Tank in Norway, whose results calibrated the linear hydrodynamic method used for all three reference sites (D8.3)."

What is wrong:
- The primary source is MARIN's D5.1, chapter 3 (2024-04-16_surewave_d5.1.md:620): "These tests were not part of the SUREWAVE project, but the results were made available by Sunlit Sea for the numerical model validation presented herein."
- D5.1:1748 states that only the motions were validated, with good agreement: "Since hinge loads were not measured these could not be validated."
- D8.3 is Sunlit Sea's own brochure, and its "first physical evidence for the connector-force distribution" goes beyond D5.1.
- MARIN will see D8.4 present a test outside the project as SUREWAVE work under Sunlit Sea's name. That overclaims, and the overclaim falls on the owner.
- The real contribution is still worth stating. Sunlit Sea brought its own test data into the project as background. MARIN validated its linear diffraction model on that data. D3.1 used the same campaigns to estimate float loads (D3.1:397).
- Minor conflict: the D5.1 text says "5 coupled PV modules" and "an array of five PV panels" (lines 442, 1740), while its Figure 14 caption says "six PV floats".

Fix, R1 evidence: "Model tests of a string of Sunlit Sea floats at the Stadt Towing Tank, carried out before and outside SUREWAVE. Sunlit Sea made the results available to the project, and MARIN used the measured motions to validate its linear diffraction model, with good agreement; hinge loads were not measured (D5.1, chapter 3). Two 1:10 campaigns of the integrated system at MARIN …".

Fix, 6.1: "Sunlit Sea made the results of its earlier float-string tests at the Stadt Towing Tank in Norway available to the project. MARIN validated its linear diffraction model against them (D5.1), and Sunlit Sea used them to estimate float loads in D3.1."

### 2. Major. The most-viewed open record, Sunlit Sea's D7.4 cost model, carries the version that D8.4 says was corrected (Sections 2.5.23, 3.5, 6.1)

Quotes. Line 434: "the D7.4 cost model and financial analysis (Sunlit Sea, doi 10.5281/zenodo.17534609), the most viewed and most downloaded record in the community". Line 839: version 2.0 "corrected errors of version 1.0".

What is wrong:
- The Zenodo snapshot of 19 November 2026 (2026-11-19_surewave_zenodo_community_snapshot.md, records 5 and 17) shows the D7.4 report published 2025-09-05 and the cost model published 2025-11-05. Both predate version 2.0 of 20 November 2026.
- D7.4 version 2.0 states that cost model version 3 is "published on Zenodo as a new version of https://doi.org/10.5281/zenodo.17534609" (2025-09-05_surewave_d7.4_economic_assessment.md:87, 1472). The snapshot does not show that version.
- As the draft stands, D8.4 points CINEA to Sunlit Sea's most-used record and, in Section 4.6, says that record's figures were wrong. A reviewer who opens it finds LCOE €0.062/kWh.

Fix (owner action before submission): upload cost model version 3 and the D7.4 version 2.0 report as new versions of records 17 and 5.

Then, line 434: "the D7.4 cost model and financial analysis (Sunlit Sea, doi 10.5281/zenodo.17534609; version 3, matching D7.4 version 2.0, uploaded [date]), the most viewed and most downloaded record in the community, with 223 views and 101 downloads on 19 November 2026". Also add "on 19 November 2026" to the counts, which are undated now.

### 3. Major. D8.5's "two new commercial agreements or partnerships" is reported as not met, although SuRE is such a partnership (Section 2.5, reach table, line 218)

Quote: "No commercial agreement for adopting a SUREWAVE result had been concluded by 23 November 2026. One partnership for further development: the EIC Transition proposal … | Not met".

What is wrong:
- D8.5:290 reads "Establish at least 2 new commercial agreements or partnerships for adopting the developed solutions."
- SuRE (Horizon Europe 101135567, running since 1 September 2024) is a signed consortium partnership. In it, Sunlit Sea takes the Generation 2 redesign that followed the SUREWAVE hinge tests to prototypes 4 and 5 (lines 302, 1302).
- Sunlit Sea's input says it "initiated a new EU project (SuRE) in partnership with one member of the SUREWAVE Stakeholder Advisory Board" (2026-09-30_sunlit_sea_exploitation_summary.md, Result 5).
- CIRCWIND (101147517) is a running partnership in which SINTEF reuses its SUREWAVE finite element methods (line 1304).
- Both are public on CORDIS. Counting only an unfunded proposal understates the result on a target the WP8 lead set.

Fix: "Two partnerships that adopt SUREWAVE results are running: SuRE (Horizon Europe 101135567, from September 2024), in which Sunlit Sea develops the Generation 2 platform that followed the SUREWAVE hinge tests, with partners met through the Stakeholder Advisory Board; and CIRCWIND (Horizon Europe 101147517, from October 2024), in which SINTEF reuses its SUREWAVE finite element methods. A third, the EIC Transition proposal of SINTEF, Sunlit Sea, Clement Germany and EDP, is under evaluation. No commercial supply or licence agreement for a SUREWAVE result had been concluded by 23 November 2026. | Met for partnerships; no commercial agreement yet".

If the owner reads "commercial" as applying to partnerships too, keep "Not met" but name SuRE and CIRCWIND in the status cell. Leaving them out is the understatement either way.

### 4. Minor. The breakwater's measured performance is given only in 6.3, not in the KER table or the proposal-result table (Sections 3.2 KER3, 3.4 R2)

Quotes. Line 486 (KER3 maturity): "wave transmission of the cross-section variants computed with CFD (FLOW-3D Hydro, D3.2)". Line 525: "Design completed; wave transmission computed with CFD".

What is wrong: these are the only partner rows without the headline result. D3.2:1705 gives it: in the 1–3 s band critical for the array, the transmitted wave height is at most about 40 % of the incident height. Clement's review comment 5 confirms the reading (about 60 % attenuation). D3.2:428 adds the weight limit of about 120 t, so mobile cranes can handle the units.

Fix: in both cells, after "computed with CFD", add "; in the 1–3 s wave band critical for the array, at most about 40 % of the incident wave height passes the breakwater (D3.2)". In 6.3, line 1102, keep the current sentence.

### 5. Minor. The D6.1 connection results omit the rating and the requirement context D6.1 gives (Sections 3.2 KER4, 6.4)

Quotes. Line 487: "breakwater steel-wire-rope connections 402 kN". Line 1139: "The breakwater-to-array connections reached a mean of 40.88 kN against a design requirement of 42 kN; the last two specimens, with the bracket–rope interface protected, exceeded it".

What is wrong:
- D6.1:685 and 783 give the 450 kN rated capacity, and the conclusion calls 402 kN "in agreement with the rated strength".
- D6.1:740–763 shows that five specimens were tested (1, 2, 4, 5, 6). The fabric protection was added from test 4 on, so three specimens were protected: 41.1, 43.7 and 42.9 kN. "The last two specimens, with the … interface protected" implies only two were protected.
- D6.1:735 calls the result "aligned with the requirements".

Fix, line 487: "breakwater steel-wire-rope connections 402 kN mean against a rated 450 kN, which D6.1 finds in agreement". Line 1139: "… a mean of 40.88 kN against a design requirement of 42 kN, which D6.1 finds aligned with the requirement. The first two failed at the rope–bracket interface at about 38 kN; with that interface protected, the next three reached 41.1–43.7 kN (D6.1; Preprints 202611.1612)."

### 6. Minor. The chloride and water-penetration results appear in 6.2 but not in 3.4 R3 or KER2 (Sections 3.2, 3.4)

Line 526 gives the D4.2 water penetration but not the chloride migration. Line 1079 gives both. Fix, line 526, after the water-penetration clause: "; chloride-migration coefficients of 0.4–0.9 × 10⁻¹² m²/s, which D4.2 classes as extremely high resistance to chloride penetration (D4.2, Table 5)". One clause in KER2 maturity, line 485, would do the same: "laboratory: no water penetration in the HPC, extremely high chloride resistance in all shell mixes (D4.2)".

### 7. Major. The D8.3 entry suggests the partners' corrections arrived after submission and were not applied (Section 2.5.20, line 420)

Quote: "was submitted on 18 November 2026. SINTEF reviewed the draft, and IFEU a later version. … On 18 November 2026 Clement Germany sent review comments, mostly on the breakwater section, and seven CAD drawings as input for four figures."

What is wrong:
- A partner reading this concludes that Clement's corrections came in on the submission day and may be missing from the submitted brochure.
- The record (TASKS.md T145, solution passes 1–5, 18 November 2026) shows the comments were applied the same day. Clement's own drawings replaced the AI figures of the breakwater, the plant layout and mooring, and the sections. Thomas Pehlke's final reply was "No further comments", and he sent an improved moored-ring figure that is in the brochure.
- MARIN (Joep van der Zanden) reviewed on 19 November. Its correction was applied: the connector loads were computed for a 2 MWp farm (T145, sixth pass). That is one day after the stated submission date. Either the submitted file lacks MARIN's correction, or the submission date is wrong. CINEA can check the portal date.
- Version 0.3 (16 November) is by Guido Reinhardt (IFEU), per the meta sidecar.
- Clement's drawings are now in a Sunlit Sea-led public deliverable, and the text does not credit them.

Fix: "The technical brochure D8.3, led by Sunlit Sea with SINTEF, was reviewed by SINTEF (5 November 2026), IFEU (16 November), Clement Germany (18 November) and MARIN (19 November). Clement Germany's review corrected the breakwater and mooring description, and its own drawings replaced the earlier illustrations of the plant layout, the breakwater unit, its sections and the moored ring. MARIN's review set out that the connector loads were computed for a 2 MWp farm. The brochure was submitted on [portal date]." Check the portal date first. If it is 18 November, D8.3 needs a resubmission with the MARIN change, or the MARIN sentence goes.

### 8. Minor. D3.4 is listed as public, but the Grant Agreement makes it Sensitive (Section 2.5.23, lines 434, 436)

Quotes: "the floating PV system design report" among the Zenodo records; "The public deliverables on CORDIS: … D3.4 …".

What is wrong:
- The GA deliverable table gives "D3.4 Summary of global system design … SEN - Sensitive" (2022-09-20_surewave_grant_agreement_101083342.md:4609).
- The D3.4 cover says Public (2024-03-19_surewave_d3.4_summary_global_system_design.md:25), and CORDIS lists it as public.
- The Zenodo record "SUREWAVE FPV System Design" (record 10, Kegelart, Sunlit Sea) is most likely D3.4. The snapshot itself flags this: "if this is D3.4, its open publication should be confirmed with the coordinator".
- D8.4, a Sunlit Sea document, would advertise to CINEA that Sunlit Sea openly published a deliverable the GA classes as Sensitive. CINEA can check this.

Fix (owner action): confirm with SINTEF whether D3.4 was reclassified as public. If it was, add "(reclassified as public; the Grant Agreement lists it as Sensitive)". If not, ask SINTEF to withdraw it from CORDIS, restrict the Zenodo record, and remove D3.4 from both lists in 2.5.23 (11 deliverable reports, 17 records).

### 9. Minor. The stated reason for the written-counts rule is wrong (Section 2.5, counting paragraph, line 196)

Quote: "Newsletters and the technical brochure count when written, since their publication continues after the project".

What is wrong: every scheduled publication falls inside the project. Newsletters III–V are due 24 November, 1 December and 8 December, and D8.3's post 22 December, all before 31 December 2026 (line 343, line 424; KPI record line 347). The real reason is the status date of 23 November. A reviewer who compares the two sentences sees a rule justified by a fact that is not true.

Fix: "Newsletters and the technical brochure count when written: they are finished, and their publication is scheduled for the last weeks of the project, after the status date of this section. The other items count when published."

### 10. Minor. The executive summary still says only "scheduled" for the sixth infographic (lines 36, 168)

What is wrong: 2.5.16 says it "was produced by Sunlit Sea in November 2026". The summary and 2.5 say "the sixth is scheduled", so the WP8 lead's own output reads as not yet made.

Fix, both places: "infographics (5 of 6 published; the sixth was produced in November 2026 and is published on 15 December 2026)". Update to 6 of 6 at submission (owner Q5).

### 11. Minor. Sunlit Sea's production of the project-website infographics is not credited (Section 2.5 table, line 187; 2.5.16)

Quote: "Infographics | … | Ceit, SINTEF; project website".

What is wrong: four of the five counted infographics were posted as surewave.eu news (KPI record, section 8, lines 184–187). Sunlit Sea runs the website and the LinkedIn page (lines 424, 428). "Project website" credits nobody. The sixth, made by Sunlit Sea, has no credit in the table at all.

Fix: "Sunlit Sea (website cards, the sixth infographic), Ceit (crack-propagation animation), SINTEF (CINEA poster)". Check with Christoffer Isdahl who designed the three carousel cards before writing "Sunlit Sea" for them.

### 12. Minor. "Sunlit Sea issued the newsletters and wrote newsletters III–V" implies someone else wrote I and II (Section 2.5.11, line 335)

Source: Newsletters I and II carry Sunlit Sea's contact (Christoffer@sunlitsea.no; 2023-07-06_surewave_newsletter_i.md:172, 2023-09-14_surewave_newsletter_ii.md:200), and the own-share paragraph says Sunlit Sea produced "the five newsletters" (line 220).

Fix: "Sunlit Sea wrote and issued all five newsletters."

### 13. Minor. Sunlit Sea's technical role is missing from the executive summary (line 19)

What is wrong: the summary credits Clement Germany's design inside KER1 but says nothing of Sunlit Sea's technical work. It mentions only "D7.4, led by Sunlit Sea" at line 30. Section 15 has the sentence (line 1414); a reader of the summary alone sees Sunlit Sea as the seller of a system others designed.

Fix, line 19, after "which Sunlit Sea AS markets.": "Sunlit Sea led the design basis (WP2), the floating PV and global system design (D3.1, D3.4), the hinge redesign and the economic assessment (D7.4)."

### 14. Minor. The conclusions' technical record leaves out the design and modelling work of four partners (Section 15, line 1412)

Quote: "They rest on the project's technical record: two 1:10-scale wave-basin campaigns of the integrated system at MARIN, the component and connection tests at SINTEF, and nine months of sea exposure …".

What is wrong: this omits:
- Clement Germany's breakwater design and CFD;
- ACCIONA's laboratory-validated mixes and the prototype it built;
- Ceit's SHMS demonstrator;
- MARIN's DIFFRAC scale-up and mooring optimisation;
- Sunlit Sea's hinge redesign;
- IFEU's integrated assessment.

The partners will read this paragraph first.

Fix: "… They rest on the project's technical record: the breakwater design and CFD of Clement Germany, the circular concrete mixes and the reduced-scale prototype of ACCIONA, the hinge redesign of Sunlit Sea, the component and connection tests at SINTEF, two 1:10-scale wave-basin campaigns and the DIFFRAC and mooring-optimisation work of MARIN, the structural health management demonstrator of Ceit, the economic assessment of Sunlit Sea and the integrated sustainability assessment of IFEU, and nine months of sea exposure of the reduced-scale concrete breakwater prototype in the Port of Gijón, without the PV array."

### 15. Minor. 3.1 still reports partners' naming slips to CINEA, including Sunlit Sea's own (lines 460–461)

Quotes: "MariSol: Sunlit Sea's input calls it a subsequent project." "… FlexiShape (… the national project SINTEF's input calls Mikroflexishape)."

What is wrong: these are corrections of wording, not conflicts of fact under requirement 2. They make the coordinator and the WP8 lead look careless in a document CINEA reads. Section 10 already uses the public names and records.

Fix: delete both bullets. If a note is wanted, put one sentence under the Section 10 table: "Periods and numbers are from the public project records, which this plan follows where partner inputs differ." This also covers D14.

### 16. Minor. The SAB follow-up meeting is still a one-line stub (Section 2.5.10, line 329)

Quote: "Follow-up meeting with board members in March 2025 (month 30)."

What is wrong: the meeting is counted as one of the two SAB workshops on Sunlit Sea's records alone, and it has no organiser, format, participants or topic. Sunlit Sea established and ran the board, so the record is its own.

Fix (owner action): "Follow-up meeting with board members, organised by Sunlit Sea, [online/in person], [date] March 2025 (month 30): [topic, e.g. organisation of a joint results workshop]." Give these from Sunlit Sea's calendar or minutes. Without them, CINEA has reason to strike the item, and the target (2) falls to 1.

### 17. Minor. "Sunlit Sea has not yet traced the publication links …" reads as unfinished WP8 work (Section 2.5.14, line 378)

What is wrong: the WP8 lead's own interviews are the only items described as "not yet traced". The KPI record (line 282) already says the ACCIONA Wideangle interview is published on LinkedIn. The closing-round script (deliverables/2026-09-30_surewave_wp8_final_interviews.md:5) says "Earlier Wideangle rounds captured Maria, Aritz, Thomas and Virgile". If a Dorronsoro (Ceit) Wideangle clip exists, the count is 10.

Fix (owner action): look up the LinkedIn posts and give dates in the table. If they cannot be found by submission, write "The 2024 interviews were posted on LinkedIn by Sunlit Sea; the record of their publication dates is held by Sunlit Sea." Check for the Dorronsoro clip (owner Q12).

### 18. Minor. The Norwegian Generation 1 plant sentence is self-contradictory (Section 4.2, line 626)

Quote: "its own 105 kWp plant in Norway, which has sold its power under a power purchase agreement since 2024, to October 2026."

Source: business plan (deliverables/2026-11-14_surewave_hrb_business_plan_ker1.md:17), "under a PPA from 2024 to October 2026; its future use is open".

Fix: "its own 105 kWp plant in Norway, which sold its power under a power purchase agreement from 2024 to October 2026."

### 19. Minor. SuRE credit is weaker than Sunlit Sea's input (Sections 2.5.10, 6.1, 10)

Quote, line 331 and others: "SuRE … grew out of contacts made through the Stakeholder Advisory Board."

What is wrong:
- Sunlit Sea's input states that it "initiated a new EU project (SuRE) in partnership with one member of the SUREWAVE Stakeholder Advisory Board".
- D16 sets the phrase "grew out of contacts" and forbids naming BayWa. It does not forbid saying who acted.
- As written, SuRE reads as something that happened to the project rather than an outcome of Sunlit Sea's WP8 work.

Fix, 6.1 Network bullet only: "Sunlit Sea initiated SuRE, which grew out of contacts made through the Stakeholder Advisory Board (Section 2.5.10)." The SuRE coordinator stays IFE, as in Section 10.

### 20. Minor. The D7.4 version history sentence reads as a rejected deliverable without context (Section 4.6, line 839)

Quote: "Version 2.0 answers the request for revision of 16 October 2026."

What is wrong: the sentence is accurate. Read by partners alone, it says Sunlit Sea's deliverable was sent back, before saying what improved. Requirement 7 asks for the positive claim first.

Fix: "Version 2.0 adds the clean-up of the site at the end of life and corrects errors found in version 1.0, in reply to the project officer's request for revision of 16 October 2026: …" Move the rest of the sentence after the colon.

### 21. Minor. The unfinished state of the panel-frame finding (Section 2.1, line 102)

Quote: "Use of the panels' aluminium frames for robustness | Covered by the Generation 2 design with a standard commercial panel".

What is wrong: "Covered" does not say whether the finding was taken up or dropped (owner Q20). docs/project_facts.md:88 says a partner works on "solar panel frame design for Gen 2", so a framed panel may be part of the design. The answer is Sunlit Sea's to give, and the row is its own finding in D8.5.

Fix (owner): either "Taken up: the Generation 2 float carries the panel by its frame, which adds stiffness to the float" or "Not taken up: the Generation 2 float carries the panel in its own cast polyurethane structure". Choose according to the design-freeze state.

### 22. Major. Statements that change before submission need a single dated checklist (Sections 2.3, 2.5, 4.7, 10, 12, 14)

What is wrong: the round-1 rejection (r1_owner#26) holds, but the list keeps growing and is spread across sections:
- newsletters III–V (lines 182, 343);
- the sixth infographic (lines 36, 168, 187, 402);
- D8.3 publication (lines 212, 424);
- final summary video (lines 186, 392);
- the December Booster workshop (lines 137, 886, 1402);
- the EUPI-PV row and the EU-upside scenario (lines 908, 922, 975, 1309, 1335);
- the EIC decision (line 1308);
- the SuRE extension decision (lines 774, 906);
- the D8.3 submission date (finding 7);
- the Zenodo uploads (finding 2).

If one is missed, a final plan submitted on 31 December calls a closed call "in preparation".

Fix: keep "the status is that of 23 November 2026" in 2.5 and add it once in the title block: "Status of dated items: [submission date]". Work through the list above on submission day. This is a process fix, not a text change now.

### 23. Wording. "Sunlit Sea's own share" omits two of its WP8 outputs named elsewhere (line 220)

What is wrong: the paragraph credits Sunlit Sea with the five newsletters, the sixth infographic and the explainer. It leaves out:
- the KPI verification of every figure, which it names only as "checked each figure";
- the website cards (finding 11);
- the D8.3 coordination with four partners' reviews (finding 7);
- the business card (KPI record line 203; not counted).

Fix: after "led the technical brochure D8.3, with SINTEF", add "and coordinated its review by SINTEF, IFEU, Clement Germany and MARIN".

### 24. Wording. Table "Technical brochure" contributors (line 191)

Quote: "Sunlit Sea, SINTEF". Fix: "Sunlit Sea, SINTEF; reviewed by IFEU, Clement Germany and MARIN".

### 25. Wording. Interview count note (line 185)

Quote: "recorded or published by Sunlit Sea". Fix: "arranged and recorded by Sunlit Sea, with Wideangle for five of the nine". This matches line 378 and the 2024 rows.

---

Findings: 5 major, 17 minor, 3 wording.
