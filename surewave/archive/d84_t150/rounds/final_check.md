# Final check of round 5 changes (d84_merged.md, 2026-11-24)

Scope: every passage listed in r5_changed_passages.md, checked against its source, the D66–D72 decisions, the rest of the draft (grep on the same topic), confidentiality against the financial plan (surewave/deliverables/2026-11-22_surewave_hrb_financial_plan_ker1.md), and the pointers each passage contains. The companion ERR changes were read too.

Render check: `pandoc d84_merged.md -o d84.html` exits with rc 0 and no warnings. There is no `<p>|`, there are 51 tables, and there is no `**` in the source or the HTML.

Confidentiality: no Sunlit Sea price or cost per watt can be derived from the changed passages. Section 4.7 gives volumes (28, 7 and 16 MWp) and margins (41–44 %, target 40–50 %), but no absolute revenue or cost. The kit sensitivity (l.771) no longer gives the €0.03/W. The breakwater share in 4.6.2 (l.717: "around a tenth" at 5 MWp) cannot be turned into a plant cost per watt, because D8.4 gives no cost for the light class. The only unit mass left is 123 t (l.959). That is Clement Germany's public D3.2 unit, not a Sunlit Sea figure.

Checked and correct, with no finding: the TRL source for CONNECT in the Booster business plan l.63; D7.6 l.759; the small wavebreakers bought from a supplier (value chain l.22, D8.4 l.620); the financial-plan figures in the executive summary, 4.7 and Section 15 (financial plan l.25–32, 100–118, 427–476); the posters counting rule (KPI record l.205–218, l.361); EU PVSEC (KPI record l.72); D8.5's one workshop and one joint event (D8.5 l.1039–1043); WP2 lead (GA l.3910); D8.5 co-authors (D8.5 l.38–50); BRIDGE author (KPI record l.199); the Zenodo creators and counts (Zenodo snapshot l.7–34); LWAC Sample 18 and ACCIONA's 1,950 kg/m³ (D4.1 l.1259, ACCIONA l.17, D4.3 l.233); Stadt tests made outside SUREWAVE (D5.1 l.620); the D5.1 Table 9 masses and the 10 MWp North Sea tension (D5.1 l.1484–1534); the D6.3 scaling (D6.3 l.447, 841, 849); the second-generation connectors and their pairing (Energies 19(7) 1609, l.70–71, 122); the breakwater-class margins (breakwater note l.38, 59–63); the D5.7 calibration and future work (D5.7 l.89–91, 651, 663); the Gijón preprint conclusions (Crossref abstract, 10.20944/preprints202611.1592.v1); the EIC rights statement (EIC proposal l.26, 216); the EIC 36-month duration (l.312); the TRL 6 and 7 definitions of the General Annexes; the DNV editions (project_facts l.122–124); SuRE and MariSol (project_facts l.53, 131; Prosjektbanken 317808); D8.1 (DataCite 10.5281/zenodo.8278574: issued 2023-03-31); NPV at 4 % (D7.4 v3 changelog l.115); and the Sunlit Sea input on SuRE and the SAB (l.53). The pointers checked in the changed passages all lead to the statement they claim: 4.1, 4.3.1, 4.4, 4.6.2, 4.7, 4.8, 6.8, 6.9, 7.2, 7.4, 9, 10 and 2.5 for the SAB follow-up.

## Major

1. A.23, l.1551, and the table above it (l.1546): "Two of the seven papers with stated peer review meet this requirement. The Grant Agreement requires deposit at the latest at publication; the other five were not deposited then."
   - Source: Crossref gives the FFEMS article 10.1111/ffe.70435 as published online on 27 August 2026, with a CC BY licence from that date. The Zenodo snapshot (surewave/background/2026-11-19_surewave_zenodo_community_snapshot.md, record 4) shows it uploaded on 30 September 2026. Europe PMC has no record of it. Only *Sensors* 24(13) 4211 is in PubMed Central (PMC11244420, from 28 June 2024).
   - Problem: under the rule the paragraph itself states, one paper meets the requirement, not two. FFEMS was deposited about five weeks after publication. CINEA will check this against Annex 5.
   - Fix (l.1551): "Annex 5 of the Grant Agreement requires, for each peer-reviewed publication, a copy of the published version or the accepted manuscript in a trusted repository at the latest at publication, with open access under CC BY or a licence with equivalent rights. One of the seven papers with stated peer review, *Sensors* 24(13) 4211, met this requirement through PubMed Central. Ceit deposited the *Fatigue & Fracture of Engineering Materials & Structures* article in the SUREWAVE community on Zenodo on 30 September 2026, five weeks after its publication on 27 August 2026. The other five were not deposited. Four of them were published in 2024–2026 under CC BY 4.0, and the partners are depositing them on Zenodo after publication; Sunlit Sea, a co-author of *Energies* 17(9) 2059, deposits that paper. For the MARINE 2025 paper, …" (rest unchanged)
   - Fix (table, FFEMS row, last cell): "Yes, Zenodo (deposited 30 September 2026, after publication)".
   - Also check: wherever the final periodic report or Section 13 repeats the count, change it to one.

## Minor

2. 4.10 table, l.844: "the maximum fairlead tensions rise in most of the optimised designs, up to about 2.5 times (Section 6.5)".
   - Source: D5.1 Table 9 (l.1484–1530). Tmax opt/ref is 1.01 (Baltic 10 MWp), 1.40 (Mediterranean 10 MWp), 1.00 (North Sea 10 MWp), 0.83 (Baltic 2 MWp), 2.46 (Mediterranean 2 MWp) and 2.15 (North Sea 2 MWp). The tension rises in 3 of the 6 optimised designs, not in most. Section 6.5 (l.1031) and the ERR say it correctly: "most of the lighter moorings" (3 of 4).
   - Problem: the error sits inside D68 itself ("they rise in most optimised designs, not all").
   - Fix: "the lighter moorings mostly carry higher maximum fairlead tensions, up to about 2.5 times the reference (Section 6.5)".

3. Executive summary l.25, 4.6.2 l.713, Section 14 l.1304 and Section 15 l.1312: "The EIC Transition proposal targets the first commercial site … from about 2030" / "immediately after its completion in the proposal's summary, about 2030".
   - Source: EIC proposal l.68 ("a first 1–5 MWp commercial installation immediately after project completion") is in section 1.1, not a summary. The proposal names no year. Its plan is 36 months (l.312). "About 2030" is the WP8 lead's derivation (project_facts l.43: "about 2030 if started 2027").
   - Problem: D66 itself attributes "about 2030" to the proposal, and that is an error inside the decision.
   - Fix (l.713): "The EIC Transition proposal targets a first commercial installation of 1–5 MWp after the EIC Transition project: immediately after its completion in its description of the commercial potential, and within 12–24 months after completion in its exploitation plan, subject to the site owner, permits and finance. With a start in 2027, the 36-month project ends about 2030."
   - Fix (l.25, l.1312): "after the EIC Transition project, which would end about 2030".

4. KER4 cell, l.306: "connection-testing methods reused in SFI BLUES and FlexiShape".
   - Source: SINTEF plan l.43 says the connection-testing methods were reused in SFI BLUES, and "the fatigue-testing setup … applied in the nationally funded Mikroflexishape project for testing aramid membrane materials". D8.4 6.4 (l.1000) says it correctly.
   - Fix: "connection-testing methods reused in SFI BLUES, and the fatigue-testing setup in FlexiShape".

5. 7.4, l.1156: "The Q1 2027 confirmation with SINTEF, Ceit and MARIN, proposed below, documents this position for the hinge and the breakwater".
   - Problem: the sentence presumes the outcome of a confirmation that has not taken place (requirement 3). D1.8 asks the partners to check whether any inseparable contribution needs joint ownership (l.1160).
   - Fix: "The Q1 2027 confirmation with SINTEF, Ceit and MARIN, proposed below, would test this position for the hinge and the breakwater and identify any SUREWAVE model or test result of Ceit or MARIN, partners outside the EIC consortium, that the demonstrator would use, before the EIC grant and consortium agreements are signed."

6. 4.7, l.771: "Kit volume 30 % lower in 2030–2031, a kit price a few per cent lower, or a kit cost higher by the same amount, each lowers 2031 EBITDA".
   - Source: financial plan l.458–459 and 476. The case is €0.03/W on both price and cost. That is about 6–7 % of the 2030–2031 kit price (l.132), but about 13 % of the 2031 kit cost of €0.23/W (l.294). A reader takes "by the same amount" after "a few per cent" to mean a few per cent of cost, which understates the cost case.
   - Fix (reveals nothing): "Kit volume 30 % lower in 2030–2031, or a kit price lower or a kit cost higher by the same small amount per watt, each lowers 2031 EBITDA, which stays positive in every case; cash stays positive."

7. Section 2.5 l.260, A.17 l.1507 and A.22 l.1528: "Christoffer Isdahl of Sunlit Sea".
   - Source: KPI record l.172 and 199 give "(Sunlit Sea)" as of 2023. docs/project_facts.md (People, l.17–25) does not list him among current staff and describes a two-person core team. The same draft writes "Guillaume Kegelart, then at Sunlit Sea" (l.262).
   - Fix: if he has left, write "then at Sunlit Sea" in all three places. Add an owner question if this is not known.

8. 6.1 l.905, Section 10 SuRE row l.1201 and A.10 l.1431: "SuRE … grew out of contacts made through the Stakeholder Advisory Board" is stated as fact.
   - Source: the only source is Sunlit Sea's input (l.53: "Sunlit Sea has initiated a new EU project (SuRE) in partnership with one member of the SUREWAVE Stakeholder Advisory Board").
   - Problem: l.1431 attributes the second sentence to Sunlit Sea but not the first. l.905 attributes it after the claim.
   - Fix (l.1431): "Sunlit Sea's exploitation input states that SuRE, a Horizon Europe project in which Sunlit Sea develops its Generation 2 floating PV system (September 2024 – August 2027), grew out of contacts made through the Stakeholder Advisory Board, initiated with one board member, and that another board member works with Sunlit Sea in several joint initiatives."
   - Fix (l.1201): end the cell with "; Sunlit Sea reports that SuRE grew out of contacts made through the SUREWAVE Stakeholder Advisory Board".

9. Companion ERR, open point 5: "ownership and contributions for the final hinge designs and for the breakwater results, whose confirmation Sunlit Sea and Clement Germany request from SINTEF, Ceit and MARIN in Q1 2027".
   - Problem: the confirmation is stated as a fixed action. D8.4 (l.810, 1162, 1180, 1301) and D67 present it as the WP8 lead's proposal.
   - Fix: "…whose confirmation by SINTEF, Ceit and MARIN the WP8 lead proposes that Sunlit Sea and Clement Germany request in Q1 2027".

10. 3.4 R1 evidence cell, l.343: "D5.7 (Ceit), which uses the second campaign to confirm that slamming loads on the breakwater are negligible".
    - Source: D5.7 l.303 says the slamming stresses were "orders of magnitude smaller than those resulting from the hinge and mooring analysis", so "the effect of not including these forces in the initial FE model was negligible". 6.6 (l.1062) says this correctly ("the effect of slamming loads … is negligible").
    - Fix: "D5.7 (Ceit), which uses the second campaign to confirm that the effect of slamming loads on the breakwater is negligible (Section 6.6)".

11. Executive summary, l.13: "This plan uses TRL 4–5 for the integrated system and for Sunlit Sea's CONNECT platform: SINTEF's technological risk assessment (D7.2) … rates the integrated concept at TRL 5".
    - Problem: the colon presents a TRL 5 rating as the evidence for TRL 4–5, so the reader cannot reconstruct the choice (requirement 5).
    - Fix: "This plan rates the integrated system and Sunlit Sea's CONNECT platform at TRL 4–5. SINTEF's technological risk assessment (D7.2), summarised in the integrated sustainability assessment D7.6 (IFEU), rates the integrated concept at TRL 5 on MARIN's wave-basin tests and SINTEF's component tests; the proposal of September 2026 to EIC Transition … starts from TRL 4; and Sunlit Sea rates CONNECT at TRL 4–5 in its Horizon Results Booster business plan (Section 4.1)."

## Wording

12. 6.1, l.908: "and the economic assessment and its cost model (D7.4); Their commercial carrier is". The capital letter follows a semicolon. Fix: "(D7.4). Their commercial carrier is".

13. 2.5, l.260: "the 2023 brochure of BRIDGE, the European Commission's initiative of EU-funded energy projects (Christoffer Isdahl)". The name reads as if it glossed BRIDGE. Fix: "wrote, through Christoffer Isdahl, the project's entry in the 2023 brochure of BRIDGE, the European Commission's initiative of EU-funded energy projects". Apply item 7 if he has left.

14. A.23, l.1551: "Sunlit Sea, one of its co-authors, deposits Energies 17(9) 2059". The pronoun comes before its antecedent, and the GA requirement is stated twice in the paragraph. Covered by the fix in item 1.

15. 4.1, l.411: "(Energies 19(7) 1609, 2026), fitted in pairs between adjacent floats (Energies 19(7) 1609; D7.2, Preprints 202611.1173)". The same source is cited twice in one sentence. Fix: "MARIN's second campaign used second-generation connectors, longer and thicker than the first generation, with higher compressive stiffness, fitted in pairs between adjacent floats (Energies 19(7) 1609, 2026; D7.2, Preprints 202611.1173)."

16. 4.6.2, l.713: "Section 4.7 gives no figures for it." This pointer leads to an absence and is a negation (writing rule). 4.7 l.747 and l.756 do cover the plant qualitatively. Fix: delete the sentence.

17. 6.1, l.895: "Sunlit Sea wrote the dissemination and exploitation plan D8.1". D8.1's title is "Dissemination, Exploitation and Communication Master Plan" (Annex B l.1590; l.260). Fix: "wrote the dissemination, exploitation and communication master plan D8.1".

18. A.10, l.1429: "counted on Sunlit Sea's confirmation (Section 2.5)". Section 2.5 (l.225) says "(Sunlit Sea's records)". Fix: "counted on Sunlit Sea's records (Section 2.5)".

19. 4.9, l.810: "test-service agreements with both sought". After four partners have been named, "both" is ambiguous. Fix: "test-service agreements with SINTEF and MARIN sought" (as in Section 14, l.1301).

20. 4.7, l.728: "Sunlit Sea builds and owns the first and smallest of them (2027)". "Them" could also refer to the kit leads or the contract named in the sentence before. Fix: "Sunlit Sea builds and owns the first and smallest Norwegian reference plant (2027) and delivers the other two …".

21. KER5 cell, l.307: "applied to a 2 MWp farm (Energies 19(7) 1609); its motions validated against …". "Its motions" has no clear owner. Fix: "its computed motions validated against Sunlit Sea's earlier Stadt Towing Tank tests, made outside SUREWAVE (D5.1), and against the second SUREWAVE basin campaign (Energies 19(7) 1609)".

22. 6.2, l.936: "Ceit monitored the prototype. Biofouling covered …". The findings come from the joint preprint of ACCIONA, SINTEF and Ceit (Crossref authors: Ruiz Maestre, Chozas, Casado, Panjwani, Chathurani Thibbotuwa, Irizar, Olaizola, Cortes), not from Ceit alone. Fix: "Ceit monitored the prototype. The joint preprint reports that biofouling covered …".

23. 7.1, l.1118: the paragraph says twice that the SUREWAVE reference design or array used Generation 1 floats: "Its background is the Generation 1 float and hinge, used in the SUREWAVE reference design, and its earlier patent" and "the SUREWAVE array, which used Sunlit Sea's Generation 1 aluminium floats". Fix, second instance: "Sunlit Sea started its redesign in SUREWAVE, from the hinge tests and models of the SUREWAVE array, and continues it in the parallel project SuRE (Section 4.1)."

Findings: 1 major, 10 minor, 12 wording.
