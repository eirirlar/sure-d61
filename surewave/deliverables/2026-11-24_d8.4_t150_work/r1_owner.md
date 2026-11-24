# D8.4 review, round 1: owner persona

Persona: Sunlit Sea's technical lead, WP8 lead. The question is whether the draft shows the consortium's work and Sunlit Sea's work in full. It also checks credit, text that reads unfinished, and anything that would embarrass the owner in front of CINEA or the partners.

Document reviewed: scratchpad_t150/d84_merged.md (1,244 lines), read end to end. Line numbers refer to that file. Source paths are relative to C:\dev\src\sure-d61 unless stated. The decisions in decisions.md are treated as settled. Where a finding touches a decision, it reports an error inside the decision or a consequence of it, not the decision itself.

---

## A. Sunlit Sea's contribution not credited

### 1. Major. Sunlit Sea's technical work packages and deliverables are not named anywhere (Sections 2.5, 4.1, 6.1, 15)

Quote: line 188, "Sunlit Sea's own share. As WP8 lead, Sunlit Sea produced the roll-up, …". Line 921, "Sunlit Sea reported six results: …".

What is wrong: the only Sunlit Sea credit in the plan is for WP8 communication and the six results in its exploitation summary. The draft never says what Sunlit Sea did in the technical work. Some of the deliverables Sunlit Sea led are cited as sources without their lead (D3.4 at line 504, D7.4 throughout). A CINEA reader would conclude that Sunlit Sea was the communication partner that also owns the product. Sunlit Sea's roles in the project:

- Annex 1 Part B (surewave/background/2022-06-24_surewave_annex1_part_b_v2.md:1146): Sunlit Sea leads WP2 (global framework, general specifications, integration requirements) and the Stakeholder Advisory Board. It takes a "relevant role" in WP3 component and global design and in WP6 prototyping and validation. It leads the economic/LCOE analysis in WP7 and leads WP8.
- Lead beneficiary lines of the deliverables:
  - D2.3 General loads (2023-01-31_surewave_d2.3_general_loads.md:36);
  - D2.4 Stakeholder Advisory Board (2024-04-22_surewave_d2.4_stakeholder_advisory_board.md:36);
  - D3.1 Design of the internal floating PV components (2023-06-26_surewave_d3.1_design_internal_floating_pv_components.md:28);
  - D3.4 Global system design (2024-03-19_surewave_d3.4_summary_global_system_design.md:29);
  - D7.4 Economic assessment (2025-09-05_surewave_d7.4_economic_assessment.md:34);
  - D8.5 (2024-04-29_…d8.5…md);
  - D8.3 and D8.4.
- Final technical report working copy (surewave/background/2026-11-19_surewave_final_technical_report_working_copy.md):
  - Task 2.3, integration requirements (line 954), and Task 2.4, stakeholder engagement (line 956), are led by Sunlit Sea;
  - Task 3.1, design of the internal FPV components (lines 1115 and 1139), and Task 3.5, coupled breakwater and FPV design and global system design (lines 1123 and 1849), are led by Sunlit Sea;
  - Sunlit Sea provided the FPV geometry and interface requirements (line 1148) and the FPV array configuration and coupling requirements (line 1568).
- D8.3 (surewave/deliverables/2026-09-28_surewave_d8.3_technical_brochure.md:196): Sunlit Sea provided the Stadt Towing Tank campaign. Its results "calibrated the linear hydrodynamic methodology used subsequently across all three reference sites and gave the first physical evidence for the connector-force distribution".

Fix: open Section 6.1 with a paragraph headed "Sunlit Sea's work in SUREWAVE". Ready text:

"In SUREWAVE, Sunlit Sea led WP2, the design basis. Under WP2 it set the integration requirements between breakwater and array (Task 2.3), wrote the general loads (D2.3) and established and ran the Stakeholder Advisory Board (Task 2.4, D2.4). In WP3 it led the design of the internal floating PV components (Task 3.1, D3.1) and the coupled breakwater and floating PV global system design (Task 3.5, D3.4), with Clement Germany for the breakwater, mooring and transition elements. It supplied the Generation 1 floats and hinges for SINTEF's connection tests and MARIN's basin models. It provided the preliminary float-string campaign at the Stadt Towing Tank, which calibrated the linear hydrodynamic method used for all three reference sites (D8.3). It led the economic assessment D7.4 and published its cost model as open data. As WP8 lead it wrote the dissemination and exploitation plans D8.1 and D8.5, the technical brochure D8.3 with SINTEF, and this plan."

Before using it, check against Sunlit Sea's records that it supplied the Generation 1 test specimens for both SINTEF and MARIN. The Annex and D8.3 support the Stadt campaign and the Generation 1 floats tested, but I found no line that names the supplier of the specimens. If none is found, drop that sentence. Add one sentence to Section 15: "Sunlit Sea led the design basis, the floating PV and global system design, the economic assessment and WP8." Optionally, add the WP leads to the KER table in Section 3.2 or 3.4.

### 2. Major. D7.4 is cited about 30 times with no lead, and the change from version 1.0 to 2.0 is not explained (Sections 4.6 and 2.5.20; Executive summary line 32)

Quote: line 713, "The SUREWAVE economic assessment (D7.4, version 2.0) covers the full life cycle …". Line 721, "These figures are from D7.4 version 2.0 and replace the version 1.0 values (LCOE €0.062/kWh, IRR 10.7 %) quoted in the technical brochure D8.3."

What is wrong:

- D7.4 is Sunlit Sea's deliverable (D7.4:34, "Lead beneficiary: Sunlit Sea"). The draft credits this only inside the KER7 description (lines 442, 486, 1050), as an input to IFEU's work.
- A reader sees the LCOE rise from €0.062 to €0.076/kWh and the IRR rise from 10.7 % to 15.6 %, with no reason given. That reads as an error in Sunlit Sea's own model, and CINEA will ask. D7.4 explains it at lines 490–500: version 1.0 used a non-standard discount factor, counted operation from year 0, and calculated the IRR on discounted cash flows over 25 years only. Requirement 5 (method explained) applies.

Fix, line 713: "The SUREWAVE economic assessment D7.4, led by Sunlit Sea (version 2.0, November 2026), covers …".

Fix, line 721, replacing its first sentence: "These figures are from D7.4 version 2.0. Version 2.0 corrects the discounting of version 1.0 and calculates the IRR on undiscounted cash flows over the full 50-year life. The LCOE therefore rises, from €0.062 to €0.076/kWh in the Mediterranean, and the IRR, now on undiscounted cash flows, rises from 10.7 % to 15.6 % (D7.4, Section 1). The version 1.0 values appear in the technical brochure D8.3."

### 3. Major. The open-science section leaves out Sunlit Sea's six Zenodo records, among them the most used record in the community (Section 2.5.23)

Quote: line 392, "18 records in the SUREWAVE community on Zenodo;". Line 396, "IFEU's slides of the 91st LCA Discussion Forum (doi 10.5281/zenodo.22957101) and Ceit's dataset for the 41st GEF Congress paper (doi 10.17632/sdxwvmrk3t.1)."

What is wrong: the section names IFEU's and Ceit's records but none of Sunlit Sea's. The Zenodo snapshot (surewave/background/2026-11-19_surewave_zenodo_community_snapshot.md, records 5, 10, 13, 14, 15 and 17; summary lines 32–33) shows:

- Sunlit Sea registered 6 of the 18 records, more than any other partner: D2.4, D3.1, the FPV system design (D3.4), the D7.4 report, the D7.4 cost model and the metocean design dataset.
- The D7.4 cost model and financial analysis (10.5281/zenodo.17534609) is "the most-viewed and most-downloaded record in the community", with 223 views and 101 downloads.
- The metocean design dataset (10.5281/zenodo.22656463, 86 views and 50 downloads) is the second most used.
- Clement Germany's anchoring and connection design dataset (10.5281/zenodo.22658269, 84 views and 46 downloads) is also left out.

Fix: replace the first bullet (line 392) with:

"18 records in the SUREWAVE community on Zenodo, all under CC BY 4.0, registered by Sunlit Sea (6), IFEU (4), Clement Germany, Ceit and SINTEF (2 each), and ACCIONA and MARIN (1 each). They include four datasets:
- the D7.4 cost model and financial analysis (Sunlit Sea, doi 10.5281/zenodo.17534609), the most viewed and most downloaded record in the community (223 views and 101 downloads on 19 November 2026);
- the metocean design dataset for the three sea basins (Sunlit Sea, doi 10.5281/zenodo.22656463);
- the anchoring and connection design dataset (Clement Germany, doi 10.5281/zenodo.22658269);
- the crack-propagation dataset (Ceit)."

Then shorten line 396 to the IFEU slides only. The Ceit dataset is now in the first bullet.

### 4. Major. The sixth infographic exists, so the one "not met" target is a self-inflicted miss (Executive summary line 38; Sections 2.5, 2.5.16)

Quote: line 38, "SUREWAVE met or exceeded every dissemination and communication target in the table of Section 2.5 except one: five of the six infographics." Line 360, "The sixth, on the SUREWAVE modelling toolchain, is scheduled for 15 December 2026."

What is wrong:

- The modelling toolchain infographic was produced by Sunlit Sea on 22 November 2026 (surewave/deliverables/2026-11-22_surewave_modelling_toolchain_infographic.md and .pdf, plus the figure .svg and .tikz.tex).
- The KPI record applies a "written counts as delivered" rule to the newsletters and to D8.3 (2026-11-19_surewave_wp8_kpi_verification.md:349, Eirik, 22 Nov 2026). The draft applies that rule to newsletters III–V (line 303) but not to an infographic that is finished and only waiting for its scheduled post.
- The headline then reports a miss that does not exist. It is the only "not met" line in the target table, and it falls on WP8's own output.

Fix: count the infographic as the sixth, so 6 of 6. In the table at line 161, change Achieved to 6 and Contributors to "Ceit, SINTEF, Sunlit Sea; project website".

Line 360: "The sixth, a one-page infographic of the SUREWAVE modelling toolchain from site wind and waves to the condition of the concrete breakwater, was produced by Sunlit Sea in November 2026. Its publication on LinkedIn is scheduled for 15 December 2026."

Line 38: "SUREWAVE met or exceeded every target in the table of Section 2.5. Other targets in the proposal and in D8.5 are reported there with their status."

Line 142: drop "except infographics, with five of six". Update the KPI record line 32 to match. This needs the owner's confirmation that the rule extends to the infographic. If it does not, keep 5 of 6.

### 5. Minor. The Stadt Towing Tank campaign is written down to "not a separate result" and its credit is missing from the evidence column (Sections 3.1 and 3.4)

Quote: line 419, "The preliminary float-string campaign at the Stadt Towing Tank, provided by Sunlit Sea (D8.3), is not reported as a separate result; it is evidence for KER1 (Section 3.4)." Line 476 (R1 evidence), "Preliminary float-string campaign at the Stadt Towing Tank and two 1:10 campaigns …".

What is wrong: this is listed as a "difference between sources", which frames Sunlit Sea's test campaign as a gap. D8.3:196 gives its outcome: six floats in a string under regular and irregular waves, the calibration of the linear hydrodynamic method used for all three sites, and the first physical evidence for the connector-force distribution.

Fix: remove the bullet at line 419; it is not a source conflict. In the R1 evidence cell write: "Preliminary float-string campaign at the Stadt Towing Tank, provided by Sunlit Sea: six floats under regular and irregular waves, which calibrated the linear hydrodynamic method used for the three sites (D8.3); two 1:10 campaigns …".

### 6. Minor. The Stakeholder Advisory Board is described without saying that Sunlit Sea established and ran it (Section 2.5.10)

Quote: line 290, "Its seven members, set out in D2.4, are …".

What is wrong: Task 2.4 and D2.4 are Sunlit Sea's (Annex line 1146; D2.4:36; final report working copy line 956). The section credits Sunlit Sea only for organising the November 2024 webinar. The follow-up meeting at line 293, "Follow-up meeting in March 2025 (month 30).", gives no organiser, format or topics and reads as a stub.

Fix, line 290: "Sunlit Sea established the Stakeholder Advisory Board under Task 2.4 and reported it in D2.4 (April 2024). It brings …".

Line 293: add the organiser, format and the topics discussed from Sunlit Sea's records. If none are found, write "Follow-up meeting with board members in March 2025 (month 30), on the organisation of a joint results workshop (final technical report)". The working copy, line 972, says the discussions were about organising a workshop.

### 7. Minor. The November 2026 interview series lacks its producer, and the 2024 set may be incomplete (Section 2.5.14)

Quote: lines 332–336, rows with no producer. Line 338, "The links to the published 2024 interviews are not yet in the evidence record."

What is wrong:

- surewave/deliverables/2026-09-30_surewave_wp8_final_interviews.md:3–5 shows that Sunlit Sea scripted the closing round and that Wideangle filmed it.
- Line 5 of the same file says "Earlier Wideangle rounds captured Maria, Aritz, Thomas and Virgile". That points to a Wideangle interview with Aritz Dorronsoro (Ceit), which is not in the count. It also points to María as the ACCIONA interviewee, who is unnamed at line 331.
- The KPI record (line 282) says the ACCIONA Wideangle interview is published on LinkedIn. The sentence at line 338 therefore understates what is shown and reads as unfinished.

Fix:

- Add after the table: "The November 2026 interviews were scripted by Sunlit Sea and filmed with Wideangle."
- Check Sunlit Sea's Wideangle records for an Aritz Dorronsoro (Ceit) interview. If one was held, add it, which makes 10 against a target of 9.
- Name the ACCIONA interviewee.
- Replace line 338 with the LinkedIn publication dates of the 2024 interviews. If they are not found before submission, write "The 2024 interviews were published on the SUREWAVE and Sunlit Sea LinkedIn pages" for those that Eirik confirms.

### 8. Minor. The draft does not name the people at Sunlit Sea who did the WP8 work, and omits several WP8 outputs (Section 2.5, own-share paragraph)

Quote: line 188.

What is wrong:

- The paragraph leaves out D8.1 and D8.5 (the plans), the KPI verification behind every figure in Section 2.5, the written newsletters III–V, the sixth infographic, the Zenodo uploads (finding 3) and D2.4.
- Christoffer Isdahl of Sunlit Sea designed the roll-up, wrote the BRIDGE entry, set up the Matomo tracking and authored D3.1 (KPI record lines 172, 199 and 300; Zenodo record 13). The draft names Eirik Larsen and Guillaume Kegelart but not him.

Fix: extend the paragraph with "It wrote the dissemination plans D8.1 and D8.5 and this plan, and verified every figure in this section against public and project records in November 2026." Then add "Christoffer Isdahl (Sunlit Sea) designed the roll-up and wrote the BRIDGE entry". Add the infographic and the newsletters as in finding 4.

### 9. Minor. Sunlit Sea's role in the EIC Transition proposal is not stated (Section 10)

Quote: line 1138, "SINTEF (coordinator), Sunlit Sea, Clement Germany, and EDP as end user and commercialisation partner".

What is wrong: EDP gets a role in this cell and Sunlit Sea does not. The proposal (generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md:264 and 272) makes Sunlit Sea "technology owner and main exploitation partner", "responsible for the path to market beyond the project". Sunlit Sea also leads requirements (Task 2.1), FPV detailed design (Task 2.3), FPV manufacturing (Task 5.1) and system integration (Task 5.4). Clement Germany supplies the breakwater and mooring.

Fix: "SINTEF (coordinator); Sunlit Sea, technology owner, leading FPV design, manufacture, system integration and commercialisation; Clement Germany, breakwater and mooring; EDP, end user and commercialisation partner".

### 10. Minor. Sunlit Sea's own techno-economic manuscript is missing (Sections 2.5.3, 4.9, 6.1)

What is wrong: Eirik Larsen (Sunlit Sea) and Balram Panjwani (SINTEF) have a draft journal article, "Techno-Economic Assessment of Breakwater-Protected Offshore Floating Photovoltaics Across Three European Sea Basins", built on D7.4 (surewave/background/2026-11-19_surewave_techno_economic_assessment_article_draft.md:1–10). Section 2.5.3 lists only SINTEF's manuscripts. Sunlit Sea's action plan (4.9) has no publication action, while every other partner's plan has one.

Fix: in 2.5.3 add "A third, on the techno-economic assessment of D7.4 by Sunlit Sea and SINTEF, is in preparation for an MDPI journal; it is not counted." In 4.9, 2027, add "Journal article on the SUREWAVE techno-economic assessment submitted, with SINTEF." Add the same in Section 13, KER1 indicators ("publications").

### 11. Minor. The Booster outputs are presented as submissions with no author, and the expert's ratings are understated (Sections 2.3, 4.3.1)

Quote: lines 116–121, "… submitted". Line 125, "the expert returned the files with notes and no major changes".

What is wrong:

- Every output in the table was prepared by Sunlit Sea, but the table does not say so.
- The kick-off was on 2 October 2026 (surewave/deliverables/2026-10-01_hrb_kickoff_meeting_prep.md:7), not "Early October".
- On 15 November only sections 2–5 of the business plan were sent (2026-11-15_hrb_final_files_and_business_plan_cover_email_to_raluca.md:1 and 21).
- The expert rated the work in writing: "Excellent" on 8 of the characterisation-table fields and "Very good" on the use model (2026-11-13_hrb_expert_feedback_characterisation_table_ker1.md:34–108). The roadmap was rated "Very good" (…exploitation_roadmap_ker1.md:36). The files overall were judged "of very high quality, with no major changes needed" (meeting summary line 13). The balanced BOSAT profile was "uncommon" (line 107). Stating ratings is a fact, not selling.

Fix:

- Table header "Step (all outputs prepared by Sunlit Sea)".
- "2 October: kick-off call with META Group."
- "15 November: final exploitation files, Lean Canvas and business plan sections 2–5 (organisation, product, market, business model) submitted."
- Line 125: "The expert judged the files of very high quality and asked for no major changes. She rated target market, adopters' problems, value proposition, competitors, end-user needs, competitive advantages and early adopters as excellent, and the use model and the roadmap as very good. …"

### 12. Minor. The Generation 1 record is undersold (Section 4.2)

Quote: line 563, "It has built two Generation 1 plants: one in commercial operation in Germany since 2023, and one in Norway that operated under a power purchase agreement from 2024 to 2026."

What is wrong: the business plan (2026-11-14_surewave_hrb_business_plan_ker1.md:15–18) gives the sizes, 60 kWp and 105 kWp. It also says Generation 1 was built in Sunlit Sea's own factory and that Sunlit Sea owned and operated the Norwegian plant. Sizes are not commercially sensitive. The decision protects customers and sites, which stay unnamed here.

Fix: "It has built two Generation 1 plants in its own factory: a 60 kWp plant in commercial operation in Germany since 2023, and its own 105 kWp plant in Norway, which sold its power under a power purchase agreement from 2024 to 2026. Sunlit Sea's CEO invented Generation 1 and leads the Generation 2 development; the technical lead is responsible for product development, sales and administration."

---

## B. Consortium work undersold or compressed

### 13. Major. Section 3.4 says no ReFRESCO result was reported, while Section 4.10 and D5.1 show that MARIN used ReFRESCO (Section 3.4, R5)

Quote: line 480, "No ReFRESCO result is reported at project end; D8.5 reported progress on it at mid-term." Line 878, "ReFRESCO used for CFD of the modules in high waves and for breakwater damping (D5.1)".

What is wrong: the two sections contradict each other, and 3.4 undersells MARIN. D5.1 (2024-04-16_surewave_d5.1.md:664 and 910) reports ReFRESCO CFD of the coupled modules in high waves and 2D forced-motion simulations for the breakwater's viscous damping in sway, heave and roll. Those damping values feed the breakwater model. The R5 row also names MARIN as an owner in the proposal but credits only SINTEF in the delivered column.

Fix, R5 delivered cell: "KER4 and KER5. MARIN applied its CFD code ReFRESCO in D5.1 to the coupled modules in high waves and to the viscous damping of the breakwater. No further development of ReFRESCO's combined current-wave-wind modelling is reported at project end (D8.5 reported progress at mid-term). The combined-effects work was delivered as SINTEF's aerodynamic wind-load method … (KER4) and SINTEF's high-fidelity hydrodynamic modelling … (KER5)."

Evidence cell: add "D5.1 (ReFRESCO CFD)".

### 14. Major. Parts of KER1 are presented without crediting Clement Germany's design (Sections 3.2, 4.1, 4.1.1)

Quote: line 436, "Generation 2 floating PV platform (Sunlit Sea CONNECT) with full-edge polyurethane hinges, mooring, transition element and, for exposed sites, a floating breakwater". Lines 500–502, "the transition element, a floating PVC pipe …; the electrical and mechanical connections; anchoring and mooring." Line 547, "The SUREWAVE breakwater unit: … Designed with CFD (D3.2)".

What is wrong: Clement Germany led the system layout and the preliminary design of the mooring lines, the anchoring and the breakwater-to-FPV transition elements (final report working copy line 1568; D3.3 lead, 2023-12-08_surewave_d3.3_final.md). Clement also led the breakwater design and its CFD (D3.2 lead). KER3 lists none of these, and KER1 lists them as its own components. Clement will comment in the review round.

Fix:

- Line 436: "… with full-edge polyurethane hinges; integrated in the plant with the mooring, anchoring, transition element and breakwater designed by Clement Germany (KER3) …".
- Line 496: "It consists of the following components, with their designers: …". Add to the list "(Sunlit Sea)" for the array, "(Clement Germany, D3.2)" for the breakwater, "(Clement Germany, D3.3)" for the transition element and for anchoring and mooring, and "with MARIN's mooring optimisation (D5.1)".
- Line 547: "Designed by Clement Germany with CFD (D3.2) …".
- KER3 row (line 438), Result: add "transition elements between breakwater and array (D3.3)".

### 15. Minor. The evidence for KER4 omits SINTEF's measured connection results (Sections 3.2, 3.4)

Quote: line 439, "Methods applied in SUREWAVE. …".

What is wrong: the strongest SINTEF evidence is not in the maturity cell:

- D6.1 (2024-09-12_surewave_d6.1_ultimate_strength_capacity.md:685 and 702): the breakwater-to-breakwater wire connection reached a mean of 402 kN against a 450 kN rating, and the breakwater-to-FPV connection failed at a mean of 41 kN against a 42 kN requirement (from the D6.1 Conclusions, as quoted in 2026-11-20_surewave_newsletter_topics_iii_v.md item III-3).
- D6.3 (2025-02-12_surewave_d6.3.md:861): the fatigue life of the redesigned polyurethane connection is about 2.5×10¹¹ cycles against 7.88×10⁸ needed for 25 years, with ageing not yet included.

Fix, KER4 maturity: "Methods applied in SUREWAVE: ultimate-strength tests of the breakwater wire connection (mean 402 kN, rating 450 kN) and of the breakwater-to-array connection (mean 41 kN, requirement 42 kN) (D6.1); fatigue tests of the redesigned hinge material, giving about 2.5×10¹¹ cycles against 7.88×10⁸ for 25 years, ageing not included (D6.3). …".

In Section 4.1, line 518, replace "indicated compatibility with a 25-year service life" with the same numbers.

### 16. Minor. The KER5 evidence omits what the 2 MWp simulation showed (Sections 3.2, 3.4 R6, 6.5)

What is wrong: Energies 19(7) 1609 (surewave/background/2026-03-25_bunnik_hydrodynamic_simulations_2mw_offshore_solar_fpv.md:11 and 275) simulated 3,660 FPV modules inside a ring of 32 breakwaters. The breakwater ring reduced vertical connector loads and overturning moments by up to 50 % in steep irregular seas. Standing waves inside the ring raised them locally. The draft gives the size of the scale-up (100 to 4,000 bodies) but not the result. MARIN's interview topic ("sloshing inside the breakwater ring", line 333) depends on that result.

Fix, KER5 maturity and R6: add "DIFFRAC simulation of a 2 MWp farm (3,660 modules in a ring of 32 breakwaters): the ring cuts vertical connector loads and overturning moments by up to 50 % in steep irregular seas, with local increases from standing waves inside the ring (Energies 19(7) 1609, 2026)".

### 17. Minor. The KER2 durability evidence is given only in words (Sections 3.2, 6.2)

Quote: line 940, "Water porosity, air permeability, chloride diffusion and damage from freeze–thaw cycles are much lower than for standard concrete."

What is wrong: D4.2 (2024-07-31_surewave_d4.2_lab_testing_breakwater_prototype.md:442 and 449) and the final report give the figures:

- the HPC showed no measurable water penetration;
- a crystalline admixture cut the mean water penetration of the LWAC from 8.2 mm to 0.6 mm;
- chloride-migration coefficients were about 0.4–0.9 × 10⁻¹² m²/s (final report working copy line 175);
- the HPC reached 128 MPa against a 120 MPa target (newsletter topics IV-1, citing D4.1).

Requirement 4 asks for the evidence in full.

Fix: add after line 940: "In the laboratory tests of D4.2, the HPC showed no measurable water penetration, and a crystalline admixture cut the mean water penetration of the LWAC from 8.2 mm to 0.6 mm. Chloride-migration coefficients of the selected mixes were about 0.4–0.9 × 10⁻¹² m²/s (final technical report)."

### 18. Minor. The KER6 evidence omits the sensor's measured resolution (Sections 3.2, 6.6)

What is wrong: D5.4 (2024-09-30_surewave_d5.4_monitoring_strategy.md:517) gives a laboratory resolution of about 0.17 mm of material loss. This is Ceit's headline figure, the "target-number quote" in its interview script. It is the right counterpart to the field caveat already in the text.

Fix, line 1032, after "through about 5–6 cm of concrete cover": "In the laboratory, the sensor quantified uniform material loss with a resolution of about 0.17 mm (D5.4)."

### 19. Minor. The KER3 performance figure is missing (Sections 3.2, 6.3)

What is wrong: Clement's results are described only qualitatively. D3.2 and the SAB webinar presentation (2024-11-19_surewave_lunch_webinar_summary.md, Section 3) give a maximum wave transmission of 0.4 in the 1–3 s band critical for the array. They also give the unit's dimensions and its design for production on land with conventional lifting equipment, without dry docks. Section 6.3 is the only partner pathway without a single number.

Fix: in KER3 maturity (line 438) and in 6.3 after the first bullet, add "In the 1–3 s wave band critical for the array, the breakwater lets through at most 40 % of the wave height (D3.2). Units are sized to be cast on land, lifted, transported and launched with conventional equipment."

Verify the 0.4 figure in D3.2 itself before inserting it. The webinar summary is a record of a presentation.

### 20. Minor. Clement's review of D8.3 is not credited (Section 2.5.20)

Quote: line 378, "led by Sunlit Sea with SINTEF".

What is wrong: Clement reviewed the breakwater and mooring sections (surewave/background/2026-11-18_clement_d8.3_brochure_review_comments.md; final report paste-in, item 12).

Fix: "led by Sunlit Sea with SINTEF, with Clement Germany's review of the breakwater and mooring sections".

### 21. Minor. Public talks at the SAB webinar and at the final workshop are not counted as presentations, while comparable webinar talks are (Sections 2.5, 2.5.5)

Quote: line 261, "Talks given in the project's own Stakeholder Advisory Board meetings and consortium meetings are not counted here."

What is wrong:

- The SAB workshop was held as a public webinar, a LinkedIn event with 31 registrations (line 273).
- Three partners presented there: SINTEF, Sunlit Sea and Clement Germany.
- The final workshop of 30 September 2026 was public and hybrid, and had talks by ACCIONA (the Gijón demonstrator) and SINTEF (line 286).
- MARIN's own webinar (line 256) and the SFI BLUES webinar are counted.

The rule undercounts Sunlit Sea, SINTEF, Clement and ACCIONA, and the reader cannot see why one public webinar counts and the other does not.

Fix, owner decision: either count the three webinar talks and the two workshop talks as presentations (15 → 20) and change line 261 to "Talks in internal consortium meetings are not counted", or keep the rule and give the reason: "The talks at the project's own public SAB webinar and final workshop are counted under web events and conference workshops, not as presentations."

---

## C. Text that reads unfinished, or would embarrass the owner in front of CINEA or the partners

### 22. Major. The published brochure D8.3, Sunlit Sea's own deliverable, will contradict D8.4 when it is posted on 22 December (Sections 2.5.20, 2.5.21, 4.6)

Quote: line 378, "Its economic figures are from D7.4 version 1.0; this plan uses version 2.0 (Section 4.6)." Line 382, "the technical brochure D8.3 on 22 December 2026".

What is wrong: D8.3 carries LCOE €0.062/kWh, NPV €8.9M and IRR 10.7 % (D8.3:32, 253, 315). It also says the concept advanced "from TRL 2–3 to TRL 4–5" (D8.3:32). D8.4 states TRL 5 for the integrated concept (decision D2) and the version 2.0 figures. The public post on 22 December will put superseded numbers and a different TRL in front of the market, nine days before D8.4 is submitted. D7.4 version 2.0 itself says its figures "replace the version 1.0 figures, including where those are quoted in other SUREWAVE deliverables" (D7.4:500).

Fix (action before 22 December): issue D8.3 version 1.1 with the version 2.0 figures and the D2 TRL wording, and post that version.

Then line 378: "D8.3 version 1.1 (December 2026) uses the D7.4 version 2.0 figures and the readiness levels of Section 4.1." If no revision is made, keep the current sentence. Also drop "quoted in the technical brochure D8.3" from line 721, or keep it only if D8.3 is not revised.

### 23. Major. The GA's final summary video is reported as "not produced" for WP8, which Sunlit Sea leads (Section 2.5, reach table)

Quote: line 186, "A final summary video has not been produced; the November 2026 interview series presents the results by topic".

What is wrong: the Grant Agreement names two videos, an introduction and a final summary. This is the only GA communication output that the WP8 lead reports as not done, and there are still five weeks of project time. The material exists: five interview clips, the explainer, the MARIN basin video and the Gijón caisson video. A project summary post is already scheduled for 29 December (line 382).

Fix (action): cut a two- to three-minute final summary video from the existing clips, with Wideangle or in-house, and publish it as the 29 December project summary. Then change the row to "Introduction: the explainer of April 2024. Final summary: the project summary video of 29 December 2026, edited from the November 2026 interview series | Met". If it is not made, keep the honest status, but say who is responsible: "planned by Sunlit Sea for …".

### 24. Major. "Year not given" for a counted conference and poster (Sections 2.5.4, 2.5.6)

Quote: line 237, "| year not given | EERA DeepWind, Trondheim | SINTEF | …". Line 267, "EERA DeepWind, Trondheim, year not given (SINTEF)".

What is wrong: a counted item with no date in a final deliverable reads as unchecked. The KPI record (line 216) also notes that it is unknown whether the poster acknowledges SUREWAVE. If it does not, CINEA can strike it.

Fix: ask SINTEF for the year, the authors and the acknowledgement before submission (it is in the record's "evidence still needed", line 382), and fill them in. If SINTEF cannot confirm by then, drop it from the count. The conference target is still met (13 against 5) and so is the poster target (2 against 1). Decision D10 keeps it counted, so the minimum fix is the year. Leaving "year not given" in the text is the embarrassing part.

### 25. Major. The "peer-reviewed" headline rests on three papers the draft itself says are not shown to be peer reviewed (Sections 2.5, 2.5.1)

Quote: line 146, "Scientific publications | 10 | GA, D8.5 (peer-reviewed) | 10". Line 192, "Three are papers in the proceedings of Spanish and Basque scientific congresses, which do not state that the papers were peer reviewed."

What is wrong: the table claims the peer-reviewed target as met, and the next section undercuts that claim. A CINEA reviewer will count seven. The final report paste-in (item 20) asks the coordinator to check this point, and it is still open.

Fix (action): ask Ceit for the GEF and MZT review procedure. GEF congress papers go through the scientific committee before they appear in the Revista; if Ceit confirms this, write "reviewed by the congress scientific committee (Ceit)". If it cannot be confirmed, change the target-source cell to "GA, D8.5" and the indicator to "Scientific publications (seven peer-reviewed with DOI, three congress papers)". In that case keep "met" on the GA wording ("10 scientific publications"), if the GA text does not say "peer-reviewed". Check the GA wording before choosing.

### 26. Major. Statements that will be out of date on the submission date (Sections 2.3, 2.5.11, 2.5.21, 10, 12, 14)

Quotes:

- line 1139, "Follow-on; application in preparation; Sunlit Sea's participation under consideration" (deadline 1 December 2026);
- line 303, "scheduled for 24 November, 1 December and 8 December 2026";
- line 1138, "decision expected December 2026 – January 2027";
- line 123, "December | Second business-planning workshop";
- line 382, LinkedIn schedule.

What is wrong: the document is dated November 2026, but it goes to the review meeting in the first week of December and is submitted by 31 December (meeting summary lines 18 and 128). By then the EUPI-PV deadline has passed and Sunlit Sea's participation is decided, newsletters III and IV are published, and the December workshop may have taken place. A final plan that calls a closed call "in preparation" reads as unmaintained.

Fix: at submission, update each item to its actual state: newsletters "published on …", EUPI-PV "submitted on 1 December 2026 with / without Sunlit Sea", workshop held or not. Add one line under the title block: "Status of dated items: [submission date]". The EUPI-PV choice also changes the scenario wording in 4.7 (line 786) and 4.9 (line 847).

### 27. Minor. The companion "Report on Exploitable Results", circulated with D8.4, now contradicts it

Source: surewave/deliverables/2026-09-30_surewave_exploitable_results_report.md.

What is wrong:

- line 19 says ACCIONA submitted in September 2026; D8.4 line 99 says 26 November 2025 (decision D11);
- line 118 says MARIN reports "up to a factor 2–3 reduction in mooring chains", which decision D3 forbids;
- lines 32, 107 and 159 use "Mikroflexishape" and "Marisol";
- line 32 says the results are "carried on" in GEOPON and line 111 says "reused in the national project with GEOPON", while D8.4 calls that project planned;
- line 179 cites "D8.4 … revision 3".

A partner reading both documents sees two versions of the same facts from the WP8 lead.

Fix: align the companion with D8.4. ACCIONA 26 November 2025; mooring "34–56 % lower mooring mass without exceeding proof loads, nearly 60 % for the 2 MW North Sea farm (D5.1)"; "FlexiShape", "MariSol"; GEOPON "planned"; cite "D8.4 version 1.0". Also align the risk assessment companion (2026-11-11_surewave_hrb_risk_assessment_ker1.md, breakwater-cost row): "breakwater €1.3–1.5 million, about 15 % of total investment". D8.4 line 721 gives €212/kWp "under a quarter". Check which D7.4 v2.0 figure each refers to (breakwater alone, or breakwater plus bridge pontoons) and state the basis in both.

### 28. Major. The value chain analysis is listed as a Booster output but never summarised (Sections 2.3, 4.4)

Quote: line 122, "22–23 November | Financial plan and value chain analysis". Section 4 contains no value chain.

What is wrong:

- Line 127 says Section 4 summarises the outputs, but the value chain analysis (2026-11-23_surewave_hrb_value_chain_ker1.md) is used only indirectly, through the key-person risk.
- It is the answer to the mentor's request on the key-person risk (meeting summary line 76) and the basis for who does what across the partners. The GA's business-model item and Task 8.4's "basis for the exploitation agreements" are where it belongs.
- Leaving out a finished analysis that the plan itself lists undersells the Booster work.

Fix: add Section 4.4.1, "Value chain", written without names, prices or sites. Ready text:

"A CONNECT plant passes through nine steps:
1. site screening and design basis;
2. permits and grid;
3. offtake and financing;
4. product design and qualification;
5. components;
6. kit packing and logistics;
7. assembly, launch and mooring;
8. operation and maintenance;
9. sale or exit.

In phase 1 Sunlit Sea, as EPC contractor, carries the interfaces between eight to ten parties: host and offtaker, plant company, investment-support agency, bank, local contractor, marine contractor, casting vendor, module supplier, DNV and Sunlit Sea. In phase 2 the developer carries most of them, and Sunlit Sea keeps site engineering, design and qualification, components and kit packing, with support in assembly and operation.

The SUREWAVE partners enter at three steps: design and qualification (IFE for structural simulation, SINTEF and MARIN for tests), assembly, where the breakwater classes come from Clement Germany from about 2030, and operation, with Ceit monitoring as an option for larger plants.

The analysis finds four single points of failure, with their interventions in Section 4.8: the two key people, the lack of a casting source qualified for series production, float production capacity for the first multi-megawatt plant, and one local contractor on both larger Norwegian projects.

Most of the margin sits in design, the moulds and the kit, which Sunlit Sea keeps in both phases. Delivery earns a thin margin for the most risk, so the EPC role is limited to the three Norwegian reference plants."

Add a row "Value chain | GA item 4 | 4.4.1" to the coverage table at line 67.

### 29. Minor. The Exploitation Intentions Table sent to the Booster on 18 October contradicts the plan, and the pivot it shows is not reported (Sections 2.3, 4.3.1)

Quote: line 116, "18 October | Exploitation Intentions Table for KER1 submitted".

What is wrong: that table (2026-10-18_surewave_exploitation_intentions_table.md:17–29) describes "pressed marine-grade aluminium floats carrying thin-film photovoltaic modules", gives the "Mediterranean offshore" market as the first, and uses the version 1.0 figures (LCOE €0.062, IRR 10.7 %). D8.4 describes cast polyurethane floats, glass-glass panels and sheltered Norwegian coastal sites first. The change from Mediterranean offshore to sheltered coastal sites between October and November is the most visible result of the value-proposition work. The draft hides it, and META Group holds a file that contradicts the plan.

Fix, line 116: "Exploitation Intentions Table for KER1 submitted: open-sea Mediterranean plants as the first market." Add after the table: "Between the October table and the November files, the first market moved from open-sea plants in the Mediterranean to sheltered coastal sites in Norway, and the product description from the SUREWAVE test platform to the Generation 2 cast-polyurethane platform. The value-proposition tests of Section 4.3.1 set out the reasons." Optionally add a row to 4.3.1 recording that change.

### 30. Minor. The draft points out a partner's spelling mistakes and Sunlit Sea's own error in a document CINEA reads (Section 3.1, step 4)

Quote: line 417, "MariSol: Sunlit Sea's input calls it a subsequent project." Line 418, "SINTEF's input spells CIRCWIND as 'CIRWIND' and calls FlexiShape 'Mikroflexishape'".

What is wrong: the density, cement and project-date conflicts belong in the deliverable (requirement 2). Spelling corrections of the coordinator's input do not, and they read as petty to SINTEF.

Fix: delete line 418; the text already uses the public names. Shorten line 417 to "MariSol started in 2020, before SUREWAVE (Research Council of Norway record); this plan treats it as an earlier project." Move both notes to the companion report.

### 31. Minor. The website figure invites scrutiny (Section 2.5.22)

Quote: line 386, "the statistics showed about 3,000 page views for the current period, up by about 27,000 % on the period before."

What is wrong: the indicator counts visits, but the quoted figure is page views. A 27,000 % jump caused by a paid campaign leads a reviewer to ask what was bought. The sentence before says the account no longer exists, so the reviewer cannot check either figure.

Fix: "Sunlit Sea started a promotion campaign around 29 May 2024 [state the channel, for example LinkedIn and Google ads, from Sunlit Sea's records]. Page views rose to about 3,000 in its first reporting period. The recorded visits passed the 36,000 target and reached more than 50,000 by the end of 2024, when tracking stopped." Drop the percentage.

### 32. Minor. Reach figures marked "not recorded" that could still be recorded (Section 2.5, reach table)

Quotes: line 185, "attendance not recorded". Line 183, "distribution not yet measured".

What is wrong: the project's final workshop ran on Teams, which keeps an attendance report for the organiser (SINTEF). Brochure distribution can be counted from the newsletter mailing list and Zenodo downloads.

Fix: ask SINTEF for the Teams attendance report of 30 September 2026 and report the number of participants. Send D8.3 with newsletter IV or V and report the number of recipients, plus Zenodo views and downloads at submission.

### 33. Minor. The status of Sunlit Sea's earlier patent may be wrong (Section 7.2)

Quote: line 1079, "Sunlit Sea's earlier patent covers the sandwich construction of the Generation 1 float".

What is wrong: the Booster meeting summary (2026-11-13_hrb_exploitation_strategy_business_planning_meeting_summary.md:24) says that the transcript suggests the patent "has been written off (to confirm)".

Fix: check the patent's status (EPO register). If it has lapsed, write "covered" in place of "covers"; if it is still in force, keep the text.

### 34. Minor. The date of the WP8 lead's own input is vague (Section 2.2)

Quote: line 103, "Sunlit Sea | Exploitation summary | by 30 September 2026".

What is wrong: the file is dated 30 September 2026 (surewave/background/2026-09-30_sunlit_sea_exploitation_summary.md). "By" looks as if the WP8 lead does not know when its own input arrived. Names of contributors are given for ACCIONA, Ceit and SINTEF but not for the other four, which is inconsistent.

Fix: give the file date of each summary (decision D11 asks for each file's own date line). Either name a contact for every partner or for none.

### 35. Minor. Newsletters III–V are counted without their content (Section 2.5.11)

Quote: line 303, "Newsletters III, IV and V: written, and scheduled …".

What is wrong: Newsletters I and II are described item by item; III–V, which carry the count to 5, get one line. The written issues exist (2026-11-20_surewave_newsletter_iii.md, _iv.md, _v.md; topics in 2026-11-20_surewave_newsletter_topics_iii_v.md).

Fix:

- "Newsletter III, 'Tested at scale': the two MARIN basin campaigns, the hinge redesign, the connection tests and the 2 MWp DIFFRAC simulation."
- "Newsletter IV, 'From recycled concrete to nine months at sea': the circular concrete mixes, laboratory durability, the Gijón exposure and the structural health management system."
- "Newsletter V, 'Cost, carbon and what comes next': where offshore floating PV makes sense, its climate and social footprint, the open results and engagement after the project."

Check these titles and contents against the final issue files, which may have changed since the topic proposal.

### 36. Minor. The D8.5 date conflicts with the final technical report (Section 2.5, evidence paragraph)

Quote: line 172, "D8.5, issued in April 2024".

What is wrong: the final report paste-in (item 15 table; Task 8.2 text) gives the D8.5 submission as 20 August 2024 ("D8.5, August 2024"). The repo file is dated 29 April 2024.

Fix: use the portal submission date in both documents. If April is the issue date and August the resubmission, write "issued in April 2024 (submitted in August 2024)".

---

## D. Wording

### 37. Wording. Executive summary, line 38

Quote: "except one: five of the six infographics".

What is wrong: the phrase is ungrammatical.

Fix: as in finding 4. If 5 of 6 stays: "except infographics, with five of six".

### 38. Wording. Section 4.9, 2027 item order

Quote: line 845, "… Hinge decision point in Q4, on the first reference-plant data. KER1 profile on the Horizon Results Platform in Q1."

What is wrong: a Q1 item follows the Q4 items.

Fix: move the Horizon Results Platform item after "first equity round closed in Q1".

### 39. Wording. Section 2.2 table, "Results reported" column

Quote: line 99, "3 concrete formulations"; the other rows give numbers only.

Fix: "3".

### 40. Wording. Section 4.3.3, line 632

Quote: "every scenario is substantially more climate-friendly".

What is wrong: this is borderline emphasis.

Fix: if D7.6 states a figure, give it ("emits about X % less CO2-eq per kWh than coal"). Otherwise write "every scenario is more climate-friendly".

---

Findings: 12 major, 24 minor, 4 wording.
