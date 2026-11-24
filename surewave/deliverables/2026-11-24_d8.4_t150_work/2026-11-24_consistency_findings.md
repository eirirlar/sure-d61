# D8.4 internal consistency findings (2026-11-24)

Document: surewave/deliverables/2026-09-28_surewave_d8.4_exploitation_pathways_business_plan.md. Each (a) string occurs exactly once in the document (checked with grep -F). Ordered roughly by importance.

## 1. KER table rates the integrated system at TRL 4–5 (Section 3.2, KER1 row)

(a) `Integrated system and CONNECT platform TRL 4–5 (Section 4.1)`

(b) `Integrated system TRL 5; CONNECT platform TRL 4–5 (Section 4.1)`

(c) This conflicts with the executive summary ("This plan uses TRL 5 for the integrated system ... CONNECT, is at TRL 4–5"), with Section 4.1 ("This plan uses TRL 5 for the integrated system"), with Section 15 ("The integrated system is at TRL 5") and with project_facts line 50.

## 2. R1 row gives CONNECT TRL 5 (Section 3.4)

(a) `hinge redesign; CONNECT platform | TRL 5 |`

(b) `hinge redesign; CONNECT platform (TRL 4–5) | TRL 5 for the integrated system |`

(c) This conflicts with the paragraph under the same table ("Sunlit Sea rates its CONNECT platform at TRL 4–5"), with Section 4.1 and with project_facts line 50 ("Generation 2 (CONNECT) is a step back, at TRL 4–5").

## 3. R1 evidence leaves out the basis this plan gives for TRL 5 (Section 3.4)

(a) `| D6.1, D6.3, D7.2 (SINTEF); D6.2 (MARIN); D7.4 (Sunlit Sea) |`

(b) `| D6.1, D6.3, D7.2 (SINTEF); D6.2 (MARIN); D7.4 (Sunlit Sea); Generation 1 operation in Germany and Norway and the Gijón exposure (Section 4.1) |`

(c) Section 4.1 bases the plan's TRL 5 on "Generation 1 plants have been in long-term, grid-connected operation ... the breakwater prototype was exposed at sea at Gijón". The R1 evidence cell cites only the tests and assessments.

## 4. "Them" has no antecedent (Section 3.4, closing paragraph)

(a) `rates the integrated concept that contains them at TRL 5`

(b) `rates the integrated concept that contains it at TRL 5`

(c) The preceding sentence names only "its CONNECT platform", so "them" refers to nothing. This looks like a remnant of an earlier version that named the hinge and platform together. (Strictly, D7.2 rated the concept with the SUREWAVE array, so "the integrated concept" without the clause is the safer wording.)

## 5. Executive summary calls the one-year delay the largest single risk

(a) `The largest single risk is a one-year delay of those plants (Section 4.8).`

(b) `In the financial plan the largest single effect comes from a one-year delay of those plants (Section 4.8).`

(c) In the Section 4.8 risk table that risk is graded 54, below two risks graded 56 ("Buyers and lenders wait for a track record | 8 × 7 = 56" and "Key-person dependency ... 8 × 7 = 56"). Section 4.7 says "the largest single effect", and the 4.8 row says "the largest risk in the financial plan".

## 6. A stray sentence sits inside the financial table (Section 4.7)

(a) `| Cash at year end (€M) | 2.91 | 0.89 | 2.48 | 2.12 | 2.80 | Sunlit Sea updates it after the Booster mentor's review and the first equity round, for adoption by its board in Q2 2027 (M2).`

(b) `| Cash at year end (€M) | 2.91 | 0.89 | 2.48 | 2.12 | 2.80 |` followed by a blank line and then the sentence as its own paragraph: `Sunlit Sea updates the plan after the Booster mentor's review and the first equity round, for adoption by its board in Q2 2027 (milestone M2, Section 4.9).`

(c) The sentence ends up in a seventh cell of a six-column table, and it uses "M2" before the milestones are defined in Section 4.9 ("M2 Business plan adopted by the board | Q2 2027").

## 7. The gross-margin range does not match the table (Section 4.7)

(a) `The gross margin is lowest in 2028 and 41–44 % in 2030–2031.`

(b) `The gross margin is lowest in 2028 and 41–43 % in 2030–2031.`

(c) The base-case table gives "Gross margin | 69 % | 14 % | 54 % | 41 % | 43 %".

## 8. Citation count uses "seven papers with a DOI", but the preprints also have DOIs (Section 2.5.2)

(a) `41 in Crossref for the seven papers with a DOI`

(b) `41 in Crossref for the seven peer-reviewed papers`

(c) Section 2.5.3 says "Seven of the ten publications state peer review". The preprints cited in the document (for example Preprints 202611.2292, which has a Crossref DOI per project_facts line 49) also carry DOIs, so "seven papers with a DOI" undercounts.

## 9. Ten publications against seven peer-reviewed papers and five cited preprints (Section 2.5.3)

(a) `Seven of the ten publications state peer review`

(b) It is unclear which version is right. The document cites five preprints (Preprints 202610.0011, 202611.1173, 202611.1592, 202611.1612, 202611.2292), and with the seven peer-reviewed papers that makes 12, not 10. Either the newest November preprints are not in the count of 10, or some preprints are versions of the peer-reviewed papers. The most likely fix keeps the 10 (the owner's decision in project_facts line 46) and adds a clause, such as `Seven of the ten publications state peer review (the count of ten includes the preprints deposited by 23 November 2026 that are not versions of these papers)`, once the list has been checked.

(c) This conflicts with the "Scientific publications | 10 (GA) | 10 | Met" row and with the five preprint citations in Sections 3.4, 4.1, 4.6, 6.2 and 6.4.

## 10. "SAB" is used before it is defined (Section 2.5.2, Events row)

(a) `4 web events, 3 conference workshops, 3 joint events and 2 SAB workshops`

(b) `4 web events, 3 conference workshops, 3 joint events and 2 Stakeholder Advisory Board (SAB) workshops`. Then change the next row's "Stakeholder Advisory Board (SAB), four of its" to "SAB, four of its".

(c) The abbreviation is defined only in the following row: "Stakeholder Advisory Board (SAB), four of its seven member organisations".

## 11. EDP is listed as a confirmed EIC Transition partner (Section 10)

(a) `SINTEF (coordinator), Sunlit Sea, Clement Germany, EDP`

(b) `SINTEF (coordinator), Sunlit Sea, Clement Germany; possible involvement of EDP`

(c) project_facts line 57 says "SINTEF-coordinated, with Clement and possible EDP (Portugal) involvement". Nowhere else in the document is EDP named as a partner.

## 12. Cross-reference points to a section without the 28 February date (Section 10)

(a) `needs a collaboration agreement with the site owner before 28 February 2027 (Section 4.6.2)`

(b) `needs a collaboration agreement with the site owner before 28 February 2027 (Section 6.3)`

(c) Section 4.6.2 does not mention the agreement or the date. Section 6.3 does: "the site owner's letter of intent lapses if no agreement is signed before 28 February 2027".

## 13. EUPI-PV row points to the financial plan rather than the section that describes the demonstration (Section 10)

(a) `Nearshore demonstration with breakwater (Section 4.7)`

(b) `Nearshore demonstration with breakwater (Sections 4.6.2 and 4.7)`

(c) The nearshore demonstration ("a nearshore demonstration with a breakwater could come in 2029") is described in Section 4.6.2. Section 4.7 gives only the EU upside scenario.

## 14. Breakwater sizing makes SINTEF conditional (Section 4.6.2)

(a) `the breakwater cost of each project is calculated by Clement Germany in the project's feasibility study, with SINTEF where it takes part`

(b) `the breakwater size and cost of each project are calculated by Clement Germany and SINTEF in the project's feasibility study, with the SUREWAVE tools`

(c) The executive summary says "for each project, Clement Germany and SINTEF size the breakwater with the SUREWAVE tools", and Section 4.1.1 says "Clement Germany and SINTEF size the breakwater from site-based calculations". project_facts line 56 says the same.

## 15. A per-project figure is given despite the disclosure rule (Section 4.7)

(a) `the small wavebreakers of the first plant are included at an estimated €0.1M`

(b) `the small wavebreakers of the first plant are included in its plant cost`

(c) The opening of Section 4.7 says "figures per project and per customer are not given", and project_facts line 53 agrees. This is a cost figure for one named project (the first Norwegian reference plant). Low priority if Eirik considers a wavebreaker estimate harmless.

## 16. The breakwater share of the investment does not match the figures (Section 4.6)

(a) `about 13 % of the investment`

(b) `about 12 % of the investment` (if D7.4 v2.0 gives €1.2M against the €9.75M investment of Section 4.6.1). Keep 13 % only if D7.4 states it for an unrounded breakwater cost of about €1.27M. In that case write "about €1.3M".

(c) Section 4.6.1 gives "The investment is about €9.75M", and 1.2 / 9.75 = 12.3 %. I could not check this against D7.4 from inside the document.

## 17. The timeline leaves out the 2028 annual review (Section 14)

(a) `| Unexploited results on the Platform (Q1); CIRCWIND and SFI BLUES end |`

(b) `| Unexploited results on the Platform (Q1); review Q3; CIRCWIND and SFI BLUES end |`

(c) Section 13 proposes "four annual reviews (Q3 2027, 2028, 2029; Q4 2030)". The timeline lists reviews for 2027, 2029 and 2030 but not 2028.

## 18. The conclusions leave out the breakwater as a supplied component (Section 15)

(a) `Partners' results reach KER1 as services or licences under the agreements set out in Section 9`

(b) `Partners' results reach KER1 as a supplied component (the breakwater), services or licences under the agreements set out in Sections 5 and 9`

(c) Section 5 says "The partner results reach KER1 in three ways", and the first of them is "The breakwater (KER3, with KER2 materials) is a component of KER1". Section 9 includes the "Engineering and supply" agreement.

## 19. The scope sentence does not cover all of Sections 7–15 (Section 1)

(a) `Sections 7–15 cover IPR, agreements, projects, risks, obligations and conclusions`

(b) `Sections 7–15 cover IPR, standardisation, agreements, projects, Horizon Europe support, risks, obligations, the timeline and conclusions`

(c) The list leaves out Section 8 "Standardisation", Section 11 "Horizon Europe support used and to use" and Section 14 "Timeline".

## 20. SuRE row cites prototype 5, which Section 4.1 does not mention (Section 10)

(a) `CONNECT prototypes 4 and 5 (Section 4.1)`

(b) `CONNECT prototypes 4 and 5 (prototype 4 in casting, Section 4.1)`. Alternatively, keep the row and add prototype 5 to Section 4.1.

(c) Section 4.1 mentions only "prototype 4 is in casting". Low priority.

## Checked and found consistent (no finding)

- Output targets: 21 rows, 16 sourced from the GA or D8.5 and 5 from WP8. They match the executive summary and Section 2.5.1.
- Reach and impact targets: they add up to 22, with 18 met, 2 partly met and 2 not met.
- Six hypotheses are listed with six claims. The 27 results minus 4 reported as impact leaves 23. R1–R11 has 11 rows. Five projects use SUREWAVE results (SuRE, MariSol, CIRCWIND, SFI BLUES, FlexiShape).
- Journalistic articles 7 and press releases 2 are consistent in every place.
- Open access: 1 + 5 + 1 = 7 papers, consistent with the executive summary.
- Hinge figures are consistent: 3.69, 2.04/8.36 scaled to 10/42, 37 kN design, 34/33/40 kN, 8 % above.
- D7.4 figures (€0.076, 15.6 %, €7.3M, €940/kWp, the CAPEX and OPEX percentages) match project_facts and each other.
- Revenue and EBITDA sums are consistent: the base-case net result total is −€1.45M against the −€1.44M stated, a rounding difference. The volume total is about 28 MWp. The revenue ratio is 3.8.
- Milestones M1–M10 match the text and the timeline. The equity figures (€5.5M = 3.5 + 2.0) are consistent.
- The SuRE extension status, the polyurethane float LCA, Generation 1 operation and the Stadt tests (described as made outside SUREWAVE) agree with project_facts. There is no "not tested / not validated / undemonstrated" remnant.
- Annex A lists every deliverable cited in the body (D1.4 to D8.5), and every Annex A entry is cited. All "Section x.y" references resolve to existing sections, apart from findings 12, 13 and 20.
