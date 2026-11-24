---
internal_title: SUREWAVE Final Technical Report — Sunlit Sea paste-in instructions (redo on the 24 November working copy)
date: 2026-11-24
---

# SUREWAVE Final Technical Report — Sunlit Sea paste-in instructions

Instructions for editing the live Final Technical Report (Part B) on SINTEF's Teams site. Anchors quote the working copy downloaded on 24 November 2026 (history of changes at version 0.5, submission planned 25 November 2026). Each entry gives the location, an anchor (the first words of the passage, copied from the report), the action, and the text to paste. Entries follow document order within each part. Text in code blocks is ready to paste; tables are given as tables to copy cell by cell.

Sources behind the text: D8.4 version 1.0 (60-page version, November 2026), D7.4 version 2.0 (20 November 2026), the WP8 KPI record (status 23–24 November 2026).

Markers:

- `[CONFIRM: …]` — only Eirik can confirm. Resolve or delete before pasting.
- `[COORD]` — text in a section written by SINTEF. Paste it only if Balram agrees, or send it to him as a suggested change (mail in Part D).

Conventions kept:

- Late deliverables are not reported by Sunlit Sea (rule of 22 November 2026). The coordinator's own delay table in Section 5.1 is left as it is.
- The report defines reporting period 2 as 01.04.2024–30.09.2026 (M19–M48). Counts are given at 24 November 2026; items written and scheduled but not yet published are named as such, so that every figure is true on the submission day.
- Percentages are written without a space ("15.6%"), as in the report.

## Part A — the D7.4 figures (Sunlit Sea led Task 7.4)

The report quotes D7.4 version 1.0 in 21 places: Mediterranean LCOE €62/MWh (0.062 €/kWh), NPV €8.9 million, IRR 10.6% or 10.7%, payback 7–8 years, CAPEX about €900/kWp; Baltic €96/MWh; North Sea €139/MWh. D7.4 version 2.0 (20 November 2026), the reply to the Project Officer's request for revision of 16 October 2026, replaces them and states that it does. D8.4 uses version 2.0.

D7.4 version 2.0, 10 MW base cases (8.5% discount rate, 50-year life, PV replacement after 25 years, end-of-life clean-up included):

| Site | LCOE | NPV | IRR | Payback |
|---|---|---|---|---|
| Mediterranean | €76/MWh | €7.3 million | 15.6% | 10 years |
| Baltic Sea | €120/MWh | about €0 (break-even) | 8.5% | not reached |
| North Sea | €173/MWh | −€5.8 million | 3.4% | not reached |

Derived: €76/MWh is about 41% above the €54/MWh target (exact 40.7%), about 53% below the DoA's €161/MWh immature offshore-FPV reference (exact 52.8%), and within the €62–106/MWh SET Plan range for floating offshore wind. CAPEX €940/kWp. With a submarine export cable to shore, the Mediterranean LCOE rises from €76 to €89/MWh and the IRR falls from 15.6% to 12.6%; in the North Sea the LCOE exceeds €480/MWh (D7.4 version 2.0, Section 7.5.1). The IRR rises from version 1.0 although the NPV falls, because version 1.0 calculated it on discounted cash flows over 25 years and version 2.0 on undiscounted cash flows over 50 years; entry A2 says so once in the report.

With the gap to the target at 41% instead of 15%, the O7 status "Largely achieved" is still defensible on the SET Plan range and the 53% reduction, and the entries keep it; the wording "slightly higher" and "approximately 15% above" goes.

All Part A entries are in text SINTEF wrote; they correct Sunlit Sea's own results.

### A1. Section 1.1, Table 1 (objectives summary), row O7 `[COORD]`

Anchor: row "O7 | Economic impact | Mediterranean LCOE 0.062 €/kWh, positive NPV and IRR | ✅ Achieved But calculated LCoE is slightly higher than the DoA LCOE target".

Action: replace the third cell with

```
Mediterranean LCOE 0.076 €/kWh, positive NPV and IRR
```

and the fourth cell with

```
Largely achieved: positive Mediterranean business case; LCOE about 41% above the DoA target of 0.054 €/kWh and within the SET Plan range for floating offshore wind
```

### A2. WP7, Task 7.4 — add the version note `[COORD]`

Location: 1.2.7 Work Package 7, "Task 7.4: Economic Assessment", paragraph beginning "The assessment covered 27 cases, combining three deployment locations".

Action: insert after that paragraph.

```
The results below are from D7.4 version 2.0 (20 November 2026), revised in reply to the Project Officer's request of 16 October 2026. Version 2.0 adds end-of-life clean-up and the scope and system boundary, and corrects errors in version 1.0 with a rebuilt cost model, checked against a separate implementation with automated tests. For the Mediterranean 10 MW case the LCOE rises from €62 to €76/MWh and the NPV falls from €8.9 million to €7.3 million; the IRR rises from 10.7% to 15.6% because version 1.0 calculated it on discounted cash flows over 25 years and version 2.0 on undiscounted cash flows over the 50-year life.
```

### A3. WP7, Task 7.4 — results table `[COORD]`

Location: the table directly after "For the representative 10 MW base cases, the Mediterranean showed the strongest economic performance:" (columns Location, LCOE, NPV, IRR, Payback).

Action: replace the three data rows.

| Location | LCOE | NPV | IRR | Payback |
|---|---|---|---|---|
| Mediterranean Sea | €76/MWh | €7.3 million | 15.6% | 10 years |
| Baltic Sea | €120/MWh | About €0 (break-even) | 8.5% | Not reached |
| North Sea | €173/MWh | −€5.8 million | 3.4% | Not reached |

### A4. WP7, Task 7.4 — paragraph under the table `[COORD]`

Anchor: "The final Mediterranean LCOE of €62/MWh remained above the original project target of €54/MWh".

Action: replace the first sentence ("The final Mediterranean LCOE … in favourable locations.") with

```
The final Mediterranean LCOE of €76/MWh is above the original project target of €54/MWh and within the €62–106/MWh SET Plan range for floating offshore wind cited in the DoA, which gives a viable business case for the Mediterranean.
```

Keep the second sentence ("Further reductions will depend on …").

### A5. WP7, Task 7.6 — integrated assessment paragraph `[COORD]`

Anchor: "Across the assessed scenarios, offshore FPV achieved more than 90% lower greenhouse-gas emissions".

Action: in the second sentence, replace "with an estimated LCOE of €62/MWh and an IRR of approximately 10.7%" with

```
with an estimated LCOE of €76/MWh and an IRR of 15.6% (D7.4 version 2.0)
```

### A6. WP7, Progress, O7.1 "Main Measurable Outcomes", bullet `[COORD]`

Anchor: "- Estimated Mediterranean LCOE of approximately €62/MWh, with an NPV of approximately €8.9 million and an IRR of approximately 10.7%".

Action: replace the bullet with

```
- Estimated Mediterranean LCOE of approximately €76/MWh, with an NPV of approximately €7.3 million and an IRR of 15.6% for the representative 10 MW base case (D7.4 version 2.0).
```

### A7. WP7, "Significant Results", bullet `[COORD]`

Anchor: "- The representative 10 MW Mediterranean case achieved the strongest economic performance, with an estimated LCOE of €62/MWh, NPV of €8.9 million, IRR of 10.7% and a 7–8-year payback period."

Action: replace with

```
- The representative 10 MW Mediterranean case achieved the strongest economic performance, with an estimated LCOE of €76/MWh, NPV of €7.3 million, IRR of 15.6% and a 10-year payback period.
```

### A8. Section 1.1, Objective O5 summary `[COORD]`

Anchor: "The representative 10 MW Mediterranean scenario achieved an estimated LCOE of approximately €62/MWh, supporting a credible pathway".

Action: replace "€62/MWh" with "€76/MWh".

### A9. Section 1.1, Objective O7, "Reduction of LCOE" `[COORD]`

Anchor: the four bullets "- LCOE: approximately €62/MWh", "- NPV: approximately €8.9 million", "- IRR: approximately 10.6%", "- Payback period: approximately 8 years", and the paragraph after them beginning "The corresponding LCOE values were approximately €96/MWh".

Action: replace the four bullets and that paragraph with

```
- LCOE: approximately €76/MWh
- NPV: approximately €7.3 million
- IRR: approximately 15.6%
- Payback period: approximately 10 years

The corresponding LCOE values were approximately €120/MWh for the Baltic Sea, at break-even, and €173/MWh for the North Sea, not viable at current costs. The Mediterranean result is about 41% above the original target of €54/MWh and within the €62–106/MWh SET Plan range cited in the Description of Action for floating offshore wind. Sites closer to shore in the Baltic and North Seas, with lower waves, lighter breakwaters and shorter export cables, may still be viable and are assessed site by site.
```

Keep the next paragraph ("The difference from the original target resulted mainly from …") and add at its end:

```
The final figures are from D7.4 version 2.0, which also includes end-of-life clean-up.
```

### A10. Section 1.1, Objective O7, "Overall Achievement of Objective O7" `[COORD]`

Anchor: "Although the €54/MWh target was not fully reached, the final €62/MWh estimate confirmed a competitive pathway".

Action: replace "the final €62/MWh estimate" with "the final €76/MWh estimate".

### A11. Section 1.1, Objective O8, "Business and market assessment" bullet `[COORD]`

Anchor: "supported by a positive business case with an estimated LCOE of €62/MWh, NPV of €8.9 million and IRR of 10.6%."

Action: replace with

```
supported by a positive business case with an estimated LCOE of €76/MWh, NPV of €7.3 million and IRR of 15.6%.
```

### A12. Section 1.3 Impact, LCOE outcome status `[COORD]`

Anchor: "Status: Largely achieved. SUREWAVE demonstrated a substantial reduction in the estimated LCOE compared with the immature offshore-FPV reference case".

Action: replace the last sentence ("The original project target of €54/MWh was not fully reached, but the final Mediterranean estimate of €62/MWh is within …") with

```
The original project target of €54/MWh was not reached; the final Mediterranean estimate of €76/MWh is within the €62–106/MWh SET Plan range for floating offshore wind cited in the DoA.
```

### A13. Section 1.3 Impact, "Final LCOE results" table `[COORD]`

Location: the table after "For the representative 10 MW base-case configurations, the final results were:" (columns Location, LCOE, NPV, IRR, Payback, Assessment).

Action: replace the three data rows.

| Location | LCOE | NPV | IRR | Payback | Assessment |
|---|---|---|---|---|---|
| Mediterranean Sea | €76/MWh | €7.3 million | 15.6% | 10 years | Economically attractive |
| Baltic Sea | €120/MWh | About €0 | 8.5% | Not reached | At break-even; viable with favourable financing or at nearshore sites |
| North Sea | €173/MWh | −€5.8 million | 3.4% | Not reached | Not viable as a stand-alone base case; viable only at discount rates of 3% or lower |

### A14. Section 1.3 Impact, the two percentage paragraphs and formulas under that table `[COORD]`

Anchor: "The Mediterranean result was approximately 14.8% above the original €54/MWh target:", its equation "(62 − 54)/54 × 100 = 14.8%", then "However, compared with the original immature offshore-FPV reference of €161/MWh, it represents an indicative reduction of approximately 61.5%:" and its equation "(161 − 62)/161 × 100 = 61.5%".

Action: replace the two sentences with the sentences below. Edit the two Word equations to the new values (double-click each equation), or delete them and keep the sentences.

```
The Mediterranean result was approximately 41% above the original €54/MWh target: (76 − 54)/54 × 100 ≈ 41%
However, compared with the original immature offshore-FPV reference of €161/MWh, it represents an indicative reduction of approximately 53%: (161 − 76)/161 × 100 ≈ 53%
```

### A15. Section 1.3 Impact, "Grid-Connection Sensitivity" `[COORD]`

Anchor: "The Mediterranean LCOE of approximately €62/MWh assumes a short, approximately 300 m floating-cable connection".

Action: replace the paragraph with

```
The Mediterranean LCOE of approximately €76/MWh assumes a short, approximately 300 m floating-cable connection to nearby offshore infrastructure. A dedicated submarine export cable to shore (11 km) increases the Mediterranean LCOE to approximately €89/MWh and reduces the IRR from 15.6% to 12.6%. For the assessed North Sea case, 170 km from shore, the export cable increases the LCOE to more than €480/MWh.
```

### A16. Section 1.3 Impact, CAPEX bullet `[COORD]`

Anchor: "Mediterranean CAPEX was estimated at approximately €900/kWp, compared with €781/kWp in the DoA;"

Action: replace "approximately €900/kWp" with "approximately €940/kWp".

### A17. Section 1.3 Impact, "Overall achievement of Topic Outcome 3" `[COORD]`

Anchor: "The final techno-economic assessment estimated an LCOE of approximately €62/MWh for the representative Mediterranean case. This result:", the three bullets, and the paragraph beginning "The Mediterranean scenario demonstrated a credible commercial pathway, with an estimated NPV of €8.9 million".

Action: replace the sentence, the three bullets and that paragraph with

```
The final techno-economic assessment estimated an LCOE of approximately €76/MWh for the representative Mediterranean case. This result:
- is approximately 41% above the original target of €54/MWh;
- represents an indicative 53% reduction from the DoA's immature offshore-FPV reference of €161/MWh; and
- is within the €62–106/MWh range for floating offshore wind cited in the DoA.

The Mediterranean scenario demonstrated a credible commercial pathway, with an estimated NPV of €7.3 million, IRR of 15.6% and payback period of ten years. The corresponding LCOE estimates were approximately €120/MWh for the Baltic Sea and €173/MWh for the North Sea. The Baltic case is at break-even at the 8.5% discount rate, while stand-alone North Sea deployment is not economically viable under the base assumptions.
```

### A18. Section 1.3 Impact, paragraph after A17 `[COORD]`

Anchor: "The difference between the €62/MWh result and the €54/MWh target reflects the use of more detailed and conservative assumptions".

Action: replace "The difference between the €62/MWh result and the €54/MWh target reflects the use of more detailed and conservative assumptions for CAPEX, O&M, component replacement, decommissioning and financing." with

```
The difference between the €76/MWh result and the €54/MWh target reflects more detailed assumptions for CAPEX, O&M, component replacement, decommissioning, end-of-life clean-up and financing.
```

### A19. Section 1.3 Impact, economic KPI list `[COORD]`

Anchor: "- LCOE: approximately €62/MWh;" with "- NPV: approximately €8.9 million;", "- IRR: approximately 10.6%; and", "- payback period: approximately 8 years." and the paragraph after them beginning "The corresponding LCOE estimates were approximately €96/MWh".

Action: replace the four bullets and the first sentence of that paragraph with

```
- LCOE: approximately €76/MWh;
- NPV: approximately €7.3 million;
- IRR: approximately 15.6%; and
- payback period: approximately 10 years.

The corresponding LCOE estimates were approximately €120/MWh for the Baltic Sea and €173/MWh for the North Sea.
```

Keep the rest of that paragraph from "These results identify the Mediterranean as the preferred market …".

### A20. Section 1.3 Impact, achievements list `[COORD]`

Anchor: "- a Mediterranean 10 MW business case with an estimated LCOE of €62/MWh, NPV of €8.9 million, IRR of approximately 10.6% and an eight-year payback period;"

Action: replace with

```
- a Mediterranean 10 MW business case with an estimated LCOE of €76/MWh, NPV of €7.3 million, IRR of approximately 15.6% and a ten-year payback period;
```

### A21. Section 1.4, "Exploitation updates" `[COORD]`

Anchor: "The final techno-economic assessment also refined the geographical commercialisation pathway. The Mediterranean was identified as the preferred market for initial demonstration and deployment, with an estimated LCOE of approximately €62/MWh, NPV of €8.9 million, IRR of 10.6%, and payback period of approximately eight years".

Action: replace the second sentence up to "for the representative 10 MW case." with

```
For the open-sea plant, the Mediterranean was identified as the preferred market, with an estimated LCOE of approximately €76/MWh, NPV of €7.3 million, IRR of 15.6%, and payback period of approximately ten years for the representative 10 MW case.
```

Keep the last sentence ("The Baltic Sea represents a possible second-stage market …").

### A22. Section 5.1, row "Objective O7: LCOE target" `[COORD]`

Anchor: "The final Mediterranean 10 MW base case reached approximately €62.2/MWh, around 15% above the target".

Action: replace "approximately €62.2/MWh, around 15% above the target, based on more detailed and conservative cost and financing assumptions." with

```
approximately €76/MWh, around 41% above the target, based on more detailed cost and financing assumptions, end-of-life clean-up and the corrected cost model of D7.4 version 2.0.
```

## Part B — WP2 (Sunlit Sea is WP leader)

### B1. WP2 header — WP leader

Location: WP2 header table, cell under "WP LEADER": "Guillaume Kegelart".

Action: replace with

```
Eirik Larsen
```

### B2. WP2 — Publishable summary, last sentence

Anchor: "The WP2 has completed most of the tasks except continue engagement with the advisory board."

Action: replace with

```
Tasks 2.1–2.3 were completed in the first reporting period, and their design basis was used throughout the second period in system design, modelling, testing and the sustainability and economic assessments. In the reporting period (M19–M48), Task 2.4 continued the engagement with the Stakeholder Advisory Board (SAB): an online SAB workshop on 19 November 2024 and a follow-up SAB meeting in March 2025 (M30). All WP2 tasks are completed.
```

### B3. WP2 — Task 2.4 status and paragraph

Location: "Work planned for this reporting period (M19-M48)", Task 2.4. The line "Status: Completed:" and, below it, the paragraph beginning "A technical stakeholder advisory board (SAB) was formed during the first reporting period and it mainly consists of:" (it ends "…to understand the market scenario", without a full stop).

Action: replace "Status: Completed:" with "Status: Completed." and replace the paragraph with

```
The technical Stakeholder Advisory Board (SAB) was established in the first reporting period (D2.4), with seven members from industry, finance, regulation and research; four of the seven member organisations are companies. In the first period, SAB input was gathered through questionnaires and interviews (D2.4). In the reporting period, the SAB workshop was held online on 19 November 2024 as an open lunch webinar, where project results were presented and the audience asked about cost, mismatch losses, environmental monitoring, the LCOE target and equipment on the breakwater; a follow-up SAB meeting was held in March 2025 (M30). SAB members also reviewed and extended the list of potential social impacts in D8.2. Their points on grid access, permitting, certification and insurability were used in the exploitation plan (D8.4).
```

### B4. WP2 — Progress, Objective 1

Anchor: "In the subsequent period (M19–M36), discussions were held with SAB members regarding the organization of a workshop aimed at disseminating project results. A follow-up meeting took place in M30, and preparations for a joint workshop are ongoing."

Action: replace those two sentences with

```
In the reporting period (M19–M48), the SAB workshop was held online on 19 November 2024, a follow-up meeting in M30 (March 2025), and SAB members reviewed the social-impact list of D8.2. Their feedback was used in the societal, exploitation and dissemination work of WP8.

Status: Fully achieved.
```

### B5. WP2 — Progress cell, Objectives 2–4

Location: in the WP2 "Progress" cell, the three lines "Status: Completed:" under Objectives 2, 3 and 4. (The same line occurs four more times in "Work planned"; change only the three in "Progress".)

Action: replace each with

```
Status: Fully achieved (completed in the first reporting period).
```

### B6. WP2 — Deviations

Anchor: "Most of the technical tasks in WP2 have been completed, with no deviations observed over the last six months (M19-M48)".

Action: replace with

```
All WP2 tasks were completed. No deviations occurred in the reporting period (M19–M48).
```

### B7. WP2 — Resources table `[CONFIRM]`

Location: WP2 "Resources (M19-36)". Reported PM: SINTEF 0,52, Sunlit Sea 1,90, MARIN 0,13, ACCIONA 1,16, Clement 0,90, sum 4,61; Ceit and IFEU empty. Sunlit Sea's budget is 11,00 PM.

Action: check Sunlit Sea's 1,90 PM against the portal and fill Ceit's cell (or 0,00) with the coordinator. If the figures cover M19–M48, change the heading to "Resources (M19-M48)". The PM deviation itself is explained in Section 5.2. `[CONFIRM: Sunlit Sea WP2 PM in RP2]`

## Part C — WP8 (Sunlit Sea is WP leader) and the sections that report WP8 results

### C1. WP8 header — reporting period

Location: WP8 header table, cell "FROM: 01.10.2022".

Action: replace the date with

```
01.04.2024
```

### C2. WP8 — Publishable summary

Location: WP8 "Publishable summary", both cells: the first beginning "The core focus of Work Package 8 (WP8) is to create effective strategies", the second beginning "Since the start of the project, we have established a homepage on surewave.eu".

Action: replace the text of the first cell with the text below and empty the second cell.

```
Work Package 8 (WP8), led by Sunlit Sea, covers dissemination, communication, exploitation and societal engagement.

Work carried out in the reporting period (M19–M48):
- Dissemination: the publications grew to ten, six journal articles and four conference papers, on breakwater aerodynamics, wave-basin testing, farm-scale hydrodynamics, corrosion sensing, wireless monitoring and fatigue-crack modelling.
- Events: the CINEA Solar PV clustering event (April 2024), the online Stakeholder Advisory Board workshop (November 2024), the joint SUREWAVE/NaturSea-PV webinar (February 2026) and the final workshop on sustainable concrete for marine applications (30 September 2026).
- Communication: the website, the LinkedIn page, videos and webinar recordings, interviews, articles in specialist and regional media, and the press release on the Port of Gijón prototype (October 2024).
- Societal engagement (Task 8.1, led by IFEU): societal needs and a SWOT analysis with the SAB and the partners, reported in D8.2.
- Technical brochure (D8.3), written by Sunlit Sea and SINTEF.
- Exploitation (Task 8.4): seven Key Exploitable Results (KERs), one anchored in each beneficiary, with owners, protection, exploitation routes and four-year action plans, and a definitive business plan for the integrated system (KER1), prepared by Sunlit Sea with the Horizon Results Booster (D8.4).

At 24 November 2026, 21 of the 21 output targets for dissemination and communication are met, counting the newsletters, the infographic and the LinkedIn posts that are written and scheduled for publication by the end of 2026.
```

### C3. WP8 — Progress

Location: WP8 "Progress", from "Objective 1 (O1): Raise Awareness and Inform about the Project" to the end of the Task 8.5 paragraph ("…a robust foundation for future communication and public outreach.").

Action: replace the whole block with

```
Objective 1 (O1): Raise awareness and inform about the project, its results and potential benefits to industry and society
Over the project, partners presented SUREWAVE at 14 conferences and in 15 presentations, and at web events and joint events with other EU projects. The website passed 50,000 visits, the LinkedIn page has 694 followers, and the project appeared in seven journalistic articles, two press releases, nine interviews and seven videos and webinar recordings. The awareness targets are met (table of targets and actuals below).
Status: Fully achieved.

Objective 2 (O2): Disseminate project results in appropriate and impactful channels
The Dissemination, Exploitation and Communication Master Plan (D8.1, revised as D8.5 at M18) set the channels and targets. In the reporting period, dissemination moved from awareness to validated results: ten publications against a target of ten, of which seven state peer review, five preprints, public deliverables and datasets in the SUREWAVE Zenodo community, and the technical brochure (D8.3). Five of the seven peer-reviewed papers were deposited in an open repository after publication rather than at publication (see Deviations).
Status: Achieved.

Objective 3 (O3): Identify and engage with critical stakeholders from industry, research, certification bodies, media
The Stakeholder Advisory Board (WP2, Task 2.4) took part in the online workshop of 19 November 2024 and a follow-up meeting in March 2025. Societal stakeholders were engaged through the Task 8.1 needs assessment and SWOT analysis (D8.2); industry, research and media audiences through conferences, the final workshop of 30 September 2026, the joint webinar with NaturSea-PV, the CINEA clustering event and interviews.
Status: Fully achieved.

Objective 4 (O4): Develop exploitation strategies to ensure that the project will have a long-lasting impact
D8.4 maps the 27 results reported by the partners: 23 fall under seven Key Exploitable Results (KERs), one anchored in each beneficiary, and four are reported as impact. The KERs are KER1 integrated floating PV system with breakwater (Sunlit Sea), KER2 circular concrete formulations (ACCIONA), KER3 floating breakwater design (Clement Germany), KER4 modelling and testing methods (SINTEF), KER5 hydrodynamic models and basin testing (MARIN and SINTEF), KER6 structural health monitoring and eddy-current sensing (Ceit) and KER7 integrated sustainability assessment (IFEU). KER1 has a definitive business plan; KERs 2–7 have exploitation pathways, dated four-year action plans with indicators, their roles in KER1 and their protection positions. Results are carried forward in SuRE and MariSol (Sunlit Sea), in CIRCWIND and SFI BLUES (SINTEF), and in an EIC Transition proposal submitted on 16 September 2026 by SINTEF, Sunlit Sea, Clement Germany and EDP.
Status: Fully achieved.

Task 8.1: Societal Engagement (L: IFEU; Participants: All)
IFEU identified the societal stakeholders and led the needs assessment and SWOT analysis with the SAB and the project partners, covering compatibility with other sea uses and spatial planning. The results are reported in D8.2 and were used in the social and integrated sustainability assessments (D7.5, D7.6) and in the exploitation plan.

Task 8.2: Dissemination, Exploitation and Communication Strategy, and Monitoring of its Implementation (L: SIS; Participants: All)
The M18 revision of the master plan (D8.5) reviewed progress against the key performance indicators and set the plan for the second period. Website traffic was monitored with Matomo and the LinkedIn page through its own statistics. The definitive KERs were set through a written input round: the WP8 lead proposed seven candidate KERs in a template sent to the partners on 29 September 2026, all seven beneficiaries replied with written exploitation summaries, and the WP8 lead screened and mapped the results. In September–November 2026, the WP8 lead collected the partners' dissemination records and checked each indicator against publisher records, Crossref, OpenAIRE, Zenodo, the website and the LinkedIn page.

Task 8.3: Dissemination Activities (L: SIS; P: All)
Subtask 8.3.1: ten publications (six journal articles and four conference papers; table below), five preprints and two submitted journal manuscripts. Partners presented at 14 conferences, among them Floating Solar in Europe, MARINE 2025, the congresses of the Spanish Fracture Group (GEF) in 2024 and 2025 and the LCA Discussion Forums in Wädenswil.
Subtask 8.3.2: the technical brochure (D8.3) for industry stakeholders presents the system concept, materials, modelling, testing, monitoring, sustainability and economic results, the Key Exploitable Results and the remaining development needs. It was written by Sunlit Sea and SINTEF and reviewed by Clement Germany and MARIN.

Task 8.4: Exploitation Pathways and Business Plan (L: SIS; P: All)
D8.4 applies the proposal's five-step method: identification of results and IPR management under the IPR management plans (D1.4, D1.8); evaluation of business potential; business models; IPR analysis; and business and exploitation plans. It gives a definitive business plan for the integrated system (KER1), the roles, agreement types and fair-price logic for the results that feed into KER1, and each partner's exploitation pathway and four-year action plan. Sunlit Sea prepared the KER1 plan in the Horizon Results Booster Go-to-Market service from October 2026, with canvases, a risk map, the Business Opportunity Self-Assessment Tool (BOSAT), a business plan and a financial plan; at the Booster review of 13 November 2026 the expert asked for no major changes.

Task 8.5: Communication Activities (L: SIS; Participants: All)
Communication followed the master plan: the website, the LinkedIn page (694 followers; 34 posts by 18 November 2026 and six more scheduled to 29 December 2026), seven videos and webinar recordings, nine interviews, seven journalistic articles, two press releases (project start, 1 November 2022; Port of Gijón prototype, 11 October 2024), five newsletters (two published in 2023, three written and scheduled for November–December 2026), six infographics (five published, one scheduled for 15 December 2026), three factsheets, a flyer and a roll-up.
```

`[CONFIRM: the task headings in "Work planned" keep the DoA durations (M1–M36, M13–M36). The progress headings above leave the duration out; add the amended durations if the coordinator wants them.]`

### C4. WP8 — Significant results, Exploitation of results, Deviations, Corrective actions

Location: WP8 "Significant Results" cell (beginning "In the following the most relevant results which contribute to the project sub-objectives"), "Exploitation of results" cell ("- We are compiling all the exploitable results and update in M27"), and the "Deviations" and "Corrective actions" cells (each holds one empty bullet).

Action: replace the content of the four cells.

Significant Results:

```
- Ten publications against a target of ten: six journal articles and four conference papers, of which seven state peer review, on breakwater aerodynamics, wave-basin validation, farm-scale hydrodynamics, corrosion sensing, wireless monitoring and fatigue-crack modelling; plus five preprints.
- The output targets for dissemination and communication met, among them 694 LinkedIn followers (target more than 500) and more than 50,000 website visits (target more than 36,000).
- The technical brochure (D8.3) for industry stakeholders.
- Seven Key Exploitable Results with owners, protection positions, exploitation routes and four-year action plans, and a definitive business plan for the integrated system (D8.4), prepared with the Horizon Results Booster.
- SUREWAVE results carried into SuRE, MariSol, CIRCWIND, SFI BLUES and an EIC Transition proposal.
```

Exploitation of results:

```
The exploitation of all project results is set out in D8.4. Sunlit Sea exploits the integrated system (KER1) through CONNECT, its second-generation floating platform, at sheltered coastal sites first, with breakwater protection on the exposed side of sites that need it, and with the open-sea ring-breakwater plant as the long-term configuration. The other partners exploit their results (KER2–KER7) through their own products, services and research. The technical brochure, the public deliverables and the SUREWAVE Zenodo community serve as reference material after the project. Sunlit Sea enters KER1 on the Horizon Results Platform in Q1 2027.
```

Deviations:

```
- Open access: the Grant Agreement asks for deposit of peer-reviewed publications in a trusted repository at publication. Of the seven papers with stated peer review, one met this (Sensors 24(13) 4211, PubMed Central); five are deposited on Zenodo after publication (one done, four in progress); the MARINE 2025 paper is open under CC BY-NC-SA 3.0, which does not meet the licence requirement.
- Reach and impact targets: of 22 targets in the Grant Agreement and D8.5, 18 are met, two partly met (more than 140 citations: 41 in Crossref; final conference with more than 100 stakeholders: 27 guests invited to the final workshop, open to a wider audience) and two not met (a new PhD completed within the project; a separate sustainability and replication guide, whose content is covered by D7.6, D8.3 and D8.4).
```

Corrective actions:

```
- Open access: the partners deposit the four MDPI papers (CC BY 4.0) in the SUREWAVE Zenodo community; MARIN deposits the accepted manuscript of the MARINE 2025 paper under CC BY if its publishing agreement with CIMNE allows it.
- Reach: communication continues after the project through the LinkedIn page, the website and partner channels.
```

`[CONFIRM: citation count and final-workshop figures as in D8.4 §2.5.2; deposit status on submission day]`

### C5. WP8 — new table of targets and actuals

Location: directly after the WP8 "Corrective actions" cell, before the publications table.

Action: insert the heading, the table and the note.

```
Dissemination and communication: targets and actuals (status 24 November 2026)
```

| Indicator | Target (source) | Achieved |
|---|---|---|
| Scientific publications | 10 (GA) | 10 (6 journal articles, 4 conference papers; 7 state peer review) |
| Conferences | 5 (WP8) | 14 |
| Presentations | More than 10 (GA) | 15 |
| Posters | 1 (WP8) | 3 |
| Web events | 2 (WP8) | 4 |
| Joint events with other EU projects | More than 2 (GA) | 3 |
| Conference workshops | 3 (GA, D8.5) | 3 |
| Stakeholder Advisory Board workshops and meetings | 2 (D8.5) | 2 |
| Newsletters | 5 (D8.5) | 5 (2 published; 3 written, scheduled 24 Nov – 8 Dec 2026) |
| Journalistic articles | 6 (GA) | 7 |
| Press releases | At the start and at milestones (GA) | 2 |
| Interviews | 9 (GA) | 9 |
| Videos | An introduction and a final summary (GA) | 7 |
| Infographics | 6 (GA) | 6 (5 published; 1 scheduled 15 Dec 2026) |
| Factsheets | 3 (GA) | 3 |
| Flyers | 1 (GA) | 1 |
| Roll-ups | 1 (WP8) | 1 |
| Technical brochure | 1 (GA) | 1 (D8.3) |
| LinkedIn followers | More than 500 (GA) | 694 |
| LinkedIn posts | 25 (WP8) | 34 (6 more scheduled to 29 Dec 2026) |
| Website visits | More than 36,000 (GA) | More than 50,000 |

```
Sources of the targets: GA = Grant Agreement, Annex 1; D8.5 = master plan at M18; WP8 = the WP8 lead's monitoring targets for indicators that the GA and D8.5 name without a number. Items are counted over the whole project. Preprints (5) and submitted journal manuscripts (2) are reported separately from the publications. The reach and impact targets are listed under Deviations.
```

### C6. WP8 — publications table: corrections and additions

Location: the publications table at the end of WP8 (columns Type, Author et al. (Partners involved), Journal…, Title).

Actions:

1. Row beginning "Omar E. Godinez Brizuela, Balram Palwani": replace "Palwani" with "Panjwani".
2. Row MARINE 2025: replace "Date and place to be added." with "23 June 2025, Edinburgh, United Kingdom. DOI: 10.23967/marine.2025.163."
3. Row DCIS 2023: replace the whole venue cell text "DCIS 2023 Conference, Málaga, Spain, 2023. Exact dates to be added." with "DCIS 2023 Conference, Málaga, Spain, November 2023 (poster)." `[CONFIRM with Ceit: exact dates]`
4. Row "Revista de Mecánica de la Fractura (2024). 40 Congreso del Grupo Español de Fractura": replace "Revista de Mecánica de la Fractura (2024)." with "Revista Española de Mecánica de la Fractura 8 (2024), 87–92."
5. Insert three rows directly above the row "Omar E. Godinez Brizuela, Balram Panjwani, Kseniia Koseniuk" (the published items come before the submitted ones). All three acknowledge grant 101083342.

| Type | Author et al. (Partners involved) | Journal, Volume (Year), Article/Pages / DOI; or Conference, Date, Place | Title |
|---|---|---|---|
| AJ | U. Eibar; A. Dorronsoro; J.M. Martínez-Esnaola (CEIT) | Fatigue & Fracture of Engineering Materials & Structures, 49(11) (2026), 5081–5098. DOI: 10.1111/ffe.70435. | Numerical Generation of Mode I Stress Intensity Factors for Narrow Elliptical Cracks in Round Bars |
| AJ | M. Losada et al. (CEIT, MARIN) | Electronics, 13(22) (2024), 4485. DOI: 10.3390/electronics13224485. | UWB-Based Accelerometer Sensor Nodes for Low-Power Applications in Offshore Platforms |
| COC | U. Eibar; A. Dorronsoro; D. González; J. Alkorta; J.M. Martínez-Esnaola (CEIT) | Revista Española de Mecánica de la Fractura 9 (2025), p. 15. 41 Congreso del Grupo Español de Fractura, 26–28 March 2025, Vitoria-Gasteiz, Spain. | Generation of Mode I Stress Intensity Factor Solutions for Narrow Elliptical-Shaped Cracks in Round Bars: A Finite Element Approach |

6. Delete the heading line "Etc." after the table.

### C7. WP8 — Resources table `[CONFIRM]`

Location: WP8 "Resources (M19-36)". Reported PM: SINTEF 1,50, Sunlit Sea 2,25, MARIN 1,19, ACCIONA 2,70, Clement 1,80, IFEU 2,18, sum 11,62; Ceit empty. Sunlit Sea's budget is 10,00 PM.

Action: check Sunlit Sea's 2,25 PM against the portal and fill Ceit's cell with the coordinator. If the figures cover M19–M48, change the heading to "Resources (M19-M48)". `[CONFIRM: Sunlit Sea WP8 PM in RP2]`

### C8. Section 1.1 — deliverables table: D7.4 and D8.4

Location: "SUREWAVE List of deliverables (M19-M48)".

Actions:

1. Row D7.4: the due date reads "31 May 2026"; D7.4's own cover gives 30 May 2025, and the other WP7 reports read "31 May 2025". Replace with "31 May 2025" and fill Delivery Date with the portal date of version 1.0 `[CONFIRM: portal date]`.
2. Row D8.4: fill Delivery Date with the portal submission date `[CONFIRM: date]`.

No remarks on lateness.

### C9. Section 1.1, Objective O8 — name the business plan `[COORD]`

Anchor: "- Development of exploitation pathways and business planning: The project identified and assessed the exploitation potential of the key technologies developed within SUREWAVE".

Action: add at the end of that bullet

```
D8.4 sets out a definitive business plan for the global solution, the integrated floating PV system with breakwater (KER1), prepared by Sunlit Sea with the Horizon Results Booster, and exploitation pathways and four-year action plans for the six other Key Exploitable Results.
```

### C10. Section 1.3 Impact — new subsection on SMEs

Location: end of Section 1.3, after the last "Overall Assessment" paragraph (ending "…the exploitation framework required to pursue them."), before "1.4 Update of the plan for exploitation and dissemination of results".

Action: insert

```
Impact on SMEs

Three of the seven beneficiaries are SMEs: Sunlit Sea, Clement Germany and IFEU.

- Sunlit Sea, the floating PV company in the consortium, designed the floating PV array and the global system in SUREWAVE and led the economic assessment (D7.4). The connection tests showed that the corner hinges of its Generation 1 floats were too weak; Sunlit Sea redesigned it as a hinge along the full edge of the float, with a design break load of 37 kN against 14 kN for the earlier paired hinges (D7.2), and started the redesign of its float into CONNECT, its second-generation platform, which it continues in the parallel Horizon Europe project SuRE. CONNECT goes into Sunlit Sea's first Norwegian reference plants from 2027 and is sold as a kit from 2028; the integrated system with breakwater (KER1) is Sunlit Sea's main commercial result.
- Clement Germany extended its floating breakwater, mooring and anchoring design to the protection of floating PV arrays (KER3), which adds floating PV to its markets for floating concrete structures.
- IFEU applied its integrated life-cycle sustainability assessment to offshore floating PV (KER7) and reuses the method in grant-funded and commissioned studies.

For SMEs outside the consortium, the public deliverables, the design basis and the economic assessment and its cost model are open on Zenodo, so a small developer or supplier can screen sites and test a business case from them. The modular 2 MW architecture divides assembly, installation and maintenance into work packages of a size that regional marine contractors can take on.
```

### C11. Section 1.4 — list of exploitable results and route to market `[COORD]`

Location: Section 1.4, "Exploitation updates".

Action 1: replace the paragraph "The initial exploitation strategy was refined from a broad system-level commercialisation concept into a portfolio of identifiable Key Exploitable Results, including:", the nine bullets after it, and the paragraph beginning "For each result, the consortium is consolidating ownership" with

```
The initial exploitation strategy was refined from a broad system-level commercialisation concept into seven Key Exploitable Results (KERs), one anchored in each beneficiary (D8.4):
- KER1 integrated floating PV system with breakwater (Sunlit Sea), the proposal's global solution, including the redesigned FPV hinge;
- KER2 circular concrete formulations: HPC, LWAC and cellular lightweight concrete (ACCIONA);
- KER3 floating breakwater design, with mooring, anchoring, connections and transition element (Clement Germany);
- KER4 modelling and testing methods, including the aerodynamic wind-load method, connection testing and the Surewave-ANN concrete-property tool (SINTEF);
- KER5 hydrodynamic models and basin testing (MARIN and SINTEF);
- KER6 structural health monitoring and eddy-current sensing, including the Structural Health Management System (Ceit); and
- KER7 integrated sustainability assessment (IFEU).

For each KER, D8.4 gives the owner, maturity, exploitation route, protection, role in the integrated system and a four-year action plan with indicators. The principal exploitation routes are product sales and project delivery (KER1), use in the owners' projects and services, engineering and consultancy, software licences and testing services, contract research and follow-on projects.
```

Action 2: keep the economic paragraph between them (corrected in A21). Replace the paragraph "The proposed route to market was consequently updated to:" and its six numbered items with

```
The route to market for the integrated system was updated in the definitive business plan (D8.4):
1. Sunlit Sea's second-generation floating platform, CONNECT, goes into its first Norwegian reference plants at sheltered coastal sites from 2027, to build the operating record that buyers and lenders ask for, and is sold as a kit from 2028;
2. at exposed nearshore sites, a breakwater on the exposed side only, in classes sized from the SUREWAVE breakwater, with a field demonstrator in 2028–2030 if the EIC Transition proposal is funded, and the first commercial site with a breakwater after it;
3. further qualification and certification of the critical components, in particular the FPV hinge for harsh conditions;
4. partnerships with project developers, utilities and offshore-infrastructure owners;
5. a kW- to low-MW open-sea demonstrator, with a pilot proposal about 2031; and
6. commercial open-sea plants with ring breakwater from about 2035, first in favourable Mediterranean locations.
```

Keep the paragraph "This staged pathway is considered more realistic …".

## Part D — mail to Balram (send with the `[COORD]` entries)

Plain text, ready to send:

```
Subject: SUREWAVE final technical report - corrections from Sunlit Sea before submission

Hi Balram,

Before submission, these are the points from Sunlit Sea on the sections you wrote. I have each change anchored passage by passage and can paste them myself, or you can make them.

1. D7.4 figures. The report quotes D7.4 version 1.0 in 21 places (1.1 incl. Table 1, 1.3, 1.4, WP7, 5.1): Mediterranean LCOE 62 EUR/MWh, NPV 8.9 MEUR, IRR 10.6/10.7 %, payback 8 years, CAPEX 900 EUR/kWp; Baltic 96 and North Sea 139 EUR/MWh. Version 2.0 of 20 November, our reply to the Project Officer's request for revision, replaces them: Mediterranean 76 EUR/MWh, 7.3 MEUR, 15.6 %, 10 years, 940 EUR/kWp; Baltic 120 EUR/MWh at break-even; North Sea 173 EUR/MWh, -5.8 MEUR. The IRR rises although the NPV falls because version 1.0 took the IRR of discounted cash flows over 25 years. The gap to the 54 EUR/MWh target becomes about 41 %, so "slightly higher" in Table 1 and "around 15 %" in 5.1 go; "largely achieved" can stay on the SET Plan range (62-106) and the 53 % reduction from the 161 EUR/MWh reference. D8.4 uses version 2.0.

2. Publications. The record holds ten publications: six journal articles (Energies 17(9) 2059 and 17(19) 4873, Sensors 24(13) 4211, Electronics 13(22) 4485, Energies 19(7) 1609, Fatigue & Fracture of Engineering Materials & Structures 49(11)) and four conference papers (MARINE 2025, GEF 2024, MZT 2024, GEF 2025). Seven state peer review; the three Ceit congress papers are in proceedings that do not state it. Sections 2, 4 and 5.1 have six journal and three conference papers, nine of ten. D8.4 reports the GA target "10 publications" as met with ten, seven of them peer-reviewed. If you agree, the 5.1 row on the publication target can go; if you read the target as ten peer-reviewed, it is seven of ten, not nine. The 1.3 table also splits the ten as MARIN 3, CEIT 5, SINTEF 2; by lead partner it is MARIN 3, CEIT 6, SINTEF 1.

3. Preprints. Section 2 (recommendation 5 and the paragraph after the table) and Section 4.1 name a preprint "Layout Selection and Mooring Design ..." that has no DOI. The five preprints with DOIs are: Technological Risk Assessment ... (202611.1173), Experimental Characterization of Critical Connections ... (202611.1612), Marine Exposure Performance of a Circular-Concrete Floating Breakwater Prototype ... (202611.1592), Economic Assessment ... (202611.2292), and SINTEF's Numerical Simulation of the Dynamics of Modular Moored Keeled Breakwater Structures ... (202610.0011.v2). Recommendation 5 also gives older titles for the first three.

4. Hinge figure. 1.1 (O7) and WP6 say the redesigned hinge raised the average tensile capacity from 3.69 to 8.36 kN, 127 %. The 3.69 kN is a complete corner hinge of the Generation 1 float; the 8.36 kN is a one-fifth segment of the new full-edge hinge with a steel rod instead of the rope (2.04 kN with the rope; D6.3 scales to about 10 kN for the full connection with the rope). A like-for-like comparison is the design break load in D7.2: 37 kN for the new hinge against 14 kN for the paired corner hinges.

5. Route to market. 1.4 and the 1.3 "Commercialisation Pathway" start with pilot-scale Mediterranean deployment. D8.4 starts with sheltered coastal sites (CONNECT reference plants from 2027), then exposed nearshore sites with a breakwater, then the open-sea plant, first in the Mediterranean, from about 2035. I have a replacement for 1.4; the 1.3 list could follow the same order.

6. PhD. 1.3 gives one PhD (Thibbotuwa and Eibar). D8.4 records no doctoral thesis completed within the project. If a thesis has been defended, I will correct D8.4; otherwise the 1.3 row should say in progress.

7. Open science. Section 4 says the project substantially complied. On the deposit rule, one of the seven peer-reviewed papers was in a trusted repository at publication; five are deposited after publication and the MARINE 2025 licence is CC BY-NC-SA. I have put this in the WP8 deviations with the corrective action.

8. Reporting period and project end. The cover and all WP tables give 30.09.2026 as the end; D8.4 gives the project end as 31 December 2026 after the three-month extension. In the WP8 text I count items at 24 November and name the scheduled ones, so it holds either way.

9. 5.1, row "1.4 sensitivity-status change and short delay to D7.6": its last sentence says the mail subject refers to MADE4WIND. Please check whether the row belongs here.

10. Gender dimension. 1.3 has no gender subsection. The DoA places the gender actions in dissemination and communication (WP8). I will send a short paragraph for WP8 if you want one.

I have also added a Sunlit Sea SME subsection at the end of 1.3 and rewritten the WP2 and WP8 sections.

Best regards,
Eirik
```

`[CONFIRM: point 6 (PhD) and point 10 (gender) — whether to raise them; point 10 needs facts on gender monitoring in WP8 that the repo does not hold]`

## Part E — publication and preprint counts in SINTEF's sections `[COORD]`

### E1. Section 2, recommendation 1 and the paragraph after the table

Anchor (row 1, status column): "Largely addressed. Nine confirmed peer-reviewed publications can currently be counted towards the DoA target of 10."

Action: replace the whole status cell with

```
Addressed. Ten publications count towards the DoA target of 10: six journal articles and four conference papers, seven of them with stated peer review. The two submitted manuscripts and five preprints are reported separately.
```

In the action column of the same row, replace "six published peer-reviewed journal articles and three peer-reviewed conference papers" with "six published peer-reviewed journal articles and four conference papers".

Anchor (paragraph after the table): "By the end of the project, six peer-reviewed journal articles and three peer-reviewed conference papers had been published, giving nine confirmed peer-reviewed publications against the DoA target of ten."

Action: replace with

```
By the end of the project, six peer-reviewed journal articles and four conference papers had been published, giving ten publications against the DoA target of ten.
```

In the next paragraph, replace "breakwater-layout and mooring design" with "the dynamics of modular moored breakwater structures".

### E2. Section 2, recommendation 5, action column

Anchor: "Five journal-style preprints were prepared from public project results: (1) Technological Risk Assessment".

Action: replace the list of five titles (from "(1)" to the end of "(5) a preprint based on the project's economic assessment.") with

```
(1) Technological Risk Assessment of a Breakwater-Protected Offshore Floating Photovoltaic System Across Three European Sea Basins (doi.org/10.20944/preprints202611.1173.v1); (2) Experimental Characterization of Critical Connections in an Offshore Floating Photovoltaic System (doi.org/10.20944/preprints202611.1612.v1); (3) Marine Exposure Performance of a Circular-Concrete Floating Breakwater Prototype: Biofouling, Chloride Ingress and Structural Monitoring (doi.org/10.20944/preprints202611.1592.v1); (4) Numerical Simulation of the Dynamics of Modular Moored Keeled Breakwater Structures for the Shielding of Floating Photovoltaic Installations (doi.org/10.20944/preprints202610.0011.v2); and (5) Economic Assessment of Breakwater-Protected Offshore Floating Photovoltaics Across Three European Sea Basins (doi.org/10.20944/preprints202611.2292.v1).
```

### E3. Section 1.3, publication outcome

Anchor: "By the end of the project, the consortium had produced at least six published journal articles and three peer-reviewed conference papers, together with additional conference contributions, preprints and 2 journal manuscripts are submitted."

Action: replace with

```
By the end of the project, the consortium had published six journal articles and four conference papers, ten publications against the target of ten, seven of them with stated peer review, together with further conference contributions, five preprints and two submitted journal manuscripts.
```

Anchor (same cell, two paragraphs later): "Based on the currently confirmed publications, nine peer-reviewed papers can be counted towards the DoA target."

Action: replace that paragraph with

```
Ten publications count towards the DoA target of ten, which is achieved.
```

In the table above this text, row "Peer-reviewed publications or papers", replace "(10): MARIN (3); CEIT (5): SINTEF (2)" with "(10): MARIN (3); CEIT (6); SINTEF (1), by lead partner".

### E4. Section 4.1 — preprint list and publication count

Action 1: replace the text of list item 4 ("Layout Selection and Mooring Design of a Floating Breakwater Sheltering an Offshore Floating Photovoltaic Array: A Design Study for Mild, Moderate and Harsh European Seas;") with the text below. The list numbers itself; paste without a number.

```
Numerical Simulation of the Dynamics of Modular Moored Keeled Breakwater Structures for the Shielding of Floating Photovoltaic Installations: https://doi.org/10.20944/preprints202610.0011.v2
```

Action 2: anchor "The project produced six published open-access peer-reviewed journal articles and three peer-reviewed conference papers": replace "and three peer-reviewed conference papers" with "and four conference papers".

### E5. Section 5.1 — row "Scientific-publication target"

Action: delete the row if Balram accepts point 2 of the mail. If he keeps it, replace the status cell with "Achieved: ten publications against the target of ten, seven of them with stated peer review."

## Part F — checked, no change

- WP3 Tasks 3.1 and 3.5 (Sunlit Sea leads): filled by the coordinator; consistent with D8.4.
- Section 1.1, O7, "A detailed 7.16 MWp commercial configuration": the D3.4 design. D7.4 and D8.4 use a 10 MWp plant (10.4 MWp installed); the sentence describes D3.4 and can stay.
- Section 5.1 delay table, rows D8.3 and D8.4: the coordinator's text; Sunlit Sea adds nothing (rule of 22 November 2026).
- Section 5.2, Sunlit Sea (2SIS) entries: already in the report; not touched here.
- Deliverables table, D8.3 delivery date "17 Nov 2026": `[CONFIRM: portal date]`.
- Section 1.3 "Commercialisation Pathway" (pathway to the 2032 indicators): raised in point 5 of the mail; no replacement given.
