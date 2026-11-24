# T150 round 5 – fact-check of d84_merged.md (persona: fact-checker)

Checked 24 November 2026. d84_merged.md (1,592 lines) is byte-identical to d84_merged_r4.md. I read it end to end, and I made a word-level diff against d84_merged_r3int.md, which has 171 changed hunks: the round-4 fixes and the de-duplication pass. I checked every figure, date, name, DOI, period and attribution in the changed text against the primary sources. For each of the 23 items in dedup_log.md, I checked that the removed facts survive in their home section and that each new pointer leads to the statement it claims. Line numbers refer to d84_merged.md.

Sources:
- the repo files (paths relative to C:\dev\src\sure-d61);
- the live Zenodo API (communities/surewave/records, 18 records, including the owner and creation fields; records 8278574 and 10960431/10960432);
- Crossref (Energies 17(9) 2059 authors and affiliations; Sensors 25 s25196234 funder);
- CORDIS project 101084348 (NaturSea-PV, coordinator);
- the Prosjektbanken snapshot pb_317808.html.

I re-ran `PYTHONIOENCODING=utf-8 python scripts/hrb_financial_model.py --md` and `PYTHONIOENCODING=utf-8 python scripts/breakwater_classes.py`. Both exited 0, and their outputs are in the session scratchpad (r5\fm.md, r5\bw.txt). No repo file was written, and no git was run.

## Findings

### Major

1. Major. 3.1, step 4, LWAC bullet, L274: "ACCIONA's input gives its mix as 1,950 kg/m³ and 68 MPa, the values of D4.1's Sample 18, made with a CEM III cement ..."
   - What is wrong: WRONG attribution, introduced by the de-duplication pass (dedup item 11). D4.1 gives Sample 18 as 68 MPa "near 2000 kg/m³" (2024-01-18_surewave_d4.1_design_characterization_circular_materials.md l.1259; also l.1191, "a higher density compared to Sample 17"). 1,950 kg/m³ is ACCIONA's figure (2026-09-30_acciona_exploitation_summary.md), not D4.1's. The r3int text kept the two apart ("ACCIONA's input gives ... 1,950 kg/m³ and 68 MPa. ... Sample 18 ... reached 68 MPa at near 2,000 kg/m³").
   - The new sentence also contradicts Section 6.2, L918, which correctly says that D4.1 reports Sample 18 "reached 68 MPa at a density near 2,000 kg/m³". The bullet exists to record a source difference, so the error removes the very difference it records.
   - Fix: "LWAC: ACCIONA's input gives its mix as 1,950 kg/m³ and 68 MPa. D4.1 gives the same mix, Sample 18, made with a CEM III cement (blast-furnace cement, in which slag replaces part of the clinker), as 68 MPa at near 2,000 kg/m³; the prototype's top slab used it (D4.3), while D4.1 preferred Sample 17 (Section 6.2). D4.2 gives 1,850 kg/m³ and D8.3 about 1,800 kg/m³. This plan uses ACCIONA's figure for the mix used in the prototype."

### Minor

2. Minor. 2.5, L260: "It registered six of the 18 records in the SUREWAVE community on Zenodo: D2.4, D3.1, the global system design D3.4, the D7.4 report, the D7.4 cost model and the metocean design dataset". Also A.23, L1529: "Sunlit Sea registered six, IFEU four, Clement Germany, Ceit and SINTEF two each, and ACCIONA and MARIN one each."
   - What is wrong: UNSUPPORTED verb. The counts are by creator. The Zenodo snapshot (2026-11-19_surewave_zenodo_community_snapshot.md, "By type and partner") gives them as creator counts, and they are correct as such.
   - The live API's owner field tells a different story. One account (owner 520003) uploaded 13 of the 18 records: on 8 and 18 September 2026 it uploaded D2.1 (SINTEF), D3.3 and the anchoring dataset (Clement Germany), D4.3 (ACCIONA), D6.1 (SINTEF), D6.2 (MARIN) and D7.3 (IFEU), as well as Sunlit Sea's six. IFEU's accounts uploaded three records and Ceit's two.
   - The 520003 account also uploaded Sunlit Sea's D7.4 cost model on 6 November 2025. If it is Sunlit Sea's account, D8.4 understates Sunlit Sea's open-science work (decision D15: credit Sunlit Sea's WP8 output item by item) and wrongly credits the uploads to the partners.
   - Fix, 2.5: "Six of the 18 records in the SUREWAVE community on Zenodo are Sunlit Sea's: D2.4, D3.1, ... (Annex A.23)". If the owner confirms that the 520003 account is Sunlit Sea's, add: "Sunlit Sea also uploaded seven partner records, D2.1, D3.3, D4.3, D6.1, D6.2, D7.3 and Clement Germany's anchoring dataset, in September 2026."
   - Fix, A.23: "By creator, six records are Sunlit Sea's, four IFEU's, two each Clement Germany's, Ceit's and SINTEF's, and one each ACCIONA's and MARIN's." Add to the owner list: confirm whose account 520003 is.

3. Minor. Credit for D8.5.
   - 2.5, L258: "As WP8 lead it wrote the dissemination, exploitation and communication master plan D8.1 and its update D8.5".
   - 4.2, L455: "the technical lead, author of Sunlit Sea's deliverables D2.4 ..., D7.4 ... and D8.5 (WP8 master plan)".
   - What is wrong: UNDERSTATED for SINTEF. D8.5's version table lists "Eirik Larsen/ Balram Panjwani" for the final version 2.0 (29.04.2024) and the revised version 3.0 (15/08/2024). Version 1.0 was drafted by Christoffer Isdahl (2024-04-29_surewave_d8.5_dissemination_exploitation_communication_master_plan.md l.38–50). D2.4 (l.44–48) and D7.4 (l.48, l.58) list Eirik Larsen alone. D8.1's Zenodo record (concept doi 10.5281/zenodo.8278574) names Christoffer Isdahl as creator.
   - Fix, 2.5: "wrote the master plan D8.1 and its update D8.5, the latter with SINTEF".
   - Fix, 4.2: "author of Sunlit Sea's deliverables D2.4 (Stakeholder Advisory Board) and D7.4 (economic assessment) and, with SINTEF, of D8.5 (WP8 master plan)".

4. Minor. A.17, L1502: the BRIDGE entry is "written by Sunlit Sea". The de-duplication pass took "Christoffer Isdahl of Sunlit Sea designed the roll-up, wrote the BRIDGE entry and set up the website's visitor monitoring" out of 2.5. The roll-up credit (A.19) and the monitoring credit (A.22) were moved to the annex, but the BRIDGE credit was not, so a named credit was lost. The KPI record holds it: "written by Christoffer Isdahl (Sunlit Sea)" (2026-11-19_surewave_wp8_kpi_verification.md l.199).
   Fix, A.17: "(15 August 2023, pages 149–150, written by Christoffer Isdahl of Sunlit Sea)".

5. Minor. 6.6, L1061: "D5.7 (Ceit) ... calibrated the concrete model on the WP4 and WP6 test data".
   - What is wrong: CONFLICT with D5.7 and with 3.4 R8 (L348, "calibrated on the WP4 test data"). D5.7 says: "Finite element models were benchmarked ... and calibrated using WP4 concrete test data. Crack propagation simulations incorporated real-time corrosion data from WP6 sensors" (2025-09-05_surewave_d5.7_modelling_tools_validation.md l.91).
   - Fix: "calibrated the concrete model on the WP4 test data, used the WP6 corrosion-sensor data in the crack-propagation simulations, and used the second basin campaign to confirm that the effect of slamming loads on the breakwater is negligible."

6. Minor. 4.10, CAPEX row, L843: "the fairlead and anchor loads rise in the optimised designs (Section 6.5)".
   - What is wrong: UNSUPPORTED in part. D5.1 reports the trade-off as "a mooring mass reduction comes with the cost of increased maximum tensions at the fairlead" (2024-04-16_surewave_d5.1.md l.1538). Table 9's Tmax is the maximum line tension (l.1480–1487). A grep finds no statement on anchor loads. Section 6.5, the pointer's target, gives only the fairlead tensions (L1030).
   - The text was in r3int too; the de-duplication pass kept it as the remaining clause of this row (dedup item 10).
   - Fix: "lighter after optimisation at the Mediterranean and North Sea sites, with fairlead tensions up to about 2.5 times higher; heavier at the Baltic site (Section 6.5)".

7. Minor. 7.4, L1155: "The Q1 2027 confirmation with Ceit and MARIN, proposed below, documents this position".
   - What is wrong: inconsistent with every other statement of the step. L1157, the table row L1145, and 4.5, 4.9, 6.3 and Section 14 all say "with SINTEF, Ceit and MARIN". The sentence reads as if SINTEF were left out. SINTEF is in the EIC consortium (EIC proposal l.26), which may be why it was dropped, but the reader cannot tell.
   - Fix: "The Q1 2027 confirmation with SINTEF, Ceit and MARIN, proposed below, documents this position for the hinge and the breakwater, and identifies any SUREWAVE model or test result of Ceit or MARIN, partners outside the EIC consortium, that the demonstrator would use, ..."

8. Minor. 4.5, milestone, L643: "one winter at a single plant of a few hundred kWp counts as demonstration in a relevant environment; a system prototype demonstrated in an operational environment (TRL 7) needs a longer record at plant scale".
   - What is wrong: the TRL 6/7 boundary is stated as a fact with no source. The first Norwegian reference plant is a grid-connected plant selling power at a real port. Under the Horizon Europe TRL definitions (General Annexes, Annex B: TRL 6, "technology demonstrated in relevant environment"; TRL 7, "system prototype demonstration in operational environment"), a reviewer may read such a plant as an operational environment for the sheltered-site product.
   - Fix: mark the reasoning as the WP8 lead's, and name the scale: "the WP8 lead rates one winter at a single plant of a few hundred kWp as TRL 6, technology demonstrated in a relevant environment (Horizon Europe General Annexes); TRL 7, a system prototype demonstrated in an operational environment, needs a longer record at plant scale".

### Wording

9. Wording. A.8, L1409: "Joint webinar with NaturSea-PV, coordinated by Tecnalia, 2 February 2026, co-hosted by NaturSea-PV". "Co-hosted by NaturSea-PV" repeats "joint webinar with NaturSea-PV". CORDIS confirms Tecnalia as NaturSea-PV's coordinator (project 101084348, FUNDACION TECNALIA RESEARCH & INNOVATION).
   Fix: "Joint webinar of SUREWAVE and NaturSea-PV (an EU project coordinated by Tecnalia), 2 February 2026, with speakers ...".

10. Wording. A.23, L1546: "The other five were not deposited at publication, as the Grant Agreement requires". A reader can take this to mean that the Grant Agreement requires them not to be deposited.
    Fix: "The Grant Agreement requires deposit at the latest at publication; the other five were not deposited then."

11. Wording. 3.4 R1 maturity, L341: "the laboratory tests and the basin validation were delivered, the basin validation on a module array behind one breakwater section (Section 4.1)". The clause repeats "the basin validation".
    Fix: "the laboratory tests and the basin validation were delivered, the latter on a module array behind one breakwater section (Section 4.1)".

12. Wording. 4.7, L754: "The EIC and EU-upside cases also include the first commercial plant at the demonstrator site after the project." This repeats the EIC bullet (L745), and the EU-upside bullet builds on it (L746). Delete the sentence.
    The model run confirms the rest of the paragraph. EIC: net result −1,053 kEUR, lowest cash 923 kEUR (2028). EU upside: −694 kEUR, 932 kEUR (2028). Base: −1,441 kEUR, 894 kEUR (2028).

13. Wording. Annex B, D8.1, L1585: "Due month 6 (March 2023); Zenodo record, doi 10.5281/zenodo.8278574". The column is for the delivery date or version. The Zenodo record (concept doi …8278574, version doi …8278575) gives the publication date 31 March 2023.
    Fix: "31 March 2023 (Zenodo record, doi 10.5281/zenodo.8278574)".

14. Wording (source note, no text change needed). 4.1, first-generation bullet, L406: "a mean tensile load of 3.69 kN ... D6.1 compares this with the 8–10 kN". D6.1 gives the mean as 3.69 kN in its results (l.467, l.478), but writes "Average 3.5 kN" in the conclusion where it makes the 8–10 kN comparison (l.773). The draft's figure is the measured mean, which is correct; the note is for anyone who checks the quote.

15. Wording. 4.3, competitor list, L486: "BlueNewables ... (pv magazine, July 2026)". The paragraph above, L466, now cites "pv magazine, 14 July 2026". Use the same date in both.

16. Wording. Executive summary, L13: the sentence after "This plan uses TRL 4–5 for the integrated system and for Sunlit Sea's CONNECT platform:" runs to about 60 words, across two sources and the definition of EIC Transition.
    Fix: split after "component tests": "... rates the integrated concept at TRL 5 on MARIN's wave-basin tests and SINTEF's component tests. The proposal of September 2026 to EIC Transition, the European Innovation Council's scheme for taking research results towards the market, starts from TRL 4 (Section 4.1)."

## Check of the de-duplication pass (dedup_log.md)

For each item: the home section still holds the removed facts, the pointer resolves, and no source or credit was lost, except where a finding is named.

| # | Item | Home holds the facts | Pointers checked | Lost source or credit |
|---|---|---|---|---|
| 1 | Q1 2027 package | 7.4 L1145–1157; 9 L1175, L1182 | 4.5 L638, 4.8 L803, 4.9 L809, 5 L855, 12 L1226, 14 L1296 | None; wording conflict in 7.4 (finding 7) |
| 2 | First commercial site with a breakwater class | 4.6.2 L711 (1–5 MWp, about 2030, 12–24 months, 2031) | 3.2 KER3, 4.1 table, 4.4.1, 4.9, 4.10, 5, 9, 12, 14, 15 | None |
| 3 | Horizon Results Platform | 6.8 L1096–1098 | Exec L34, 11 L1214, 12 L1228, 13 L1242 | None |
| 4 | Aluminium floats and CONNECT | 4.1 L400–402 | 3.2 KER1, 3.4 R1, 6.1 L907, 7.1 L1117 (identical clause, as D63 asks) | None |
| 5 | TRL basis | 4.1 L392–397 | Exec L13, 3.4 R1, 4.10 | None; proposal TRL 4–5 (GA l.5736) and R1 TRL 5 (GA l.7660) confirmed |
| 6 | Nine-month Gijón exposure | 6.2 L931 | 3.2, 3.3, 3.4, 4.1, 4.1.1, 4.10 | None |
| 7 | 123 t and the 120 t limit | 6.3 L958 | 4.1.1 L439 | None |
| 8 | SuRE extension | 4.7 L744 | Section 10 L1196 "(Section 4.7)" | None |
| 9 | Hinge record | 4.1 L404–412 (numbering sentence MOVED, L404) | 3.1 L281, 6.1 L903, 6.5 L1032, 7.1 | None |
| 10 | Mooring | 6.5 L1030 | 3.1 L276, 4.10 L843 | 4.10 keeps "anchor loads" (finding 6) |
| 11 | HPC and LWAC | 6.2 L917–919 | 3.1 L274–275, 3.2 KER2, 3.4 R3 | LWAC bullet wrong (finding 1) |
| 12 | Stadt tests and DIFFRAC | 6.5 L1026; Council record moved to 10, L1197 (Prosjektbanken 317808: "Stadt Towing Tank har gjennomført bølgetankforsøk") | 3.2 KER5, 4.1 L412 | None; float-load use kept in 6.1 L892 (D3.1) |
| 13 | ReFRESCO | 6.5 L1028 (MOVED clauses present; D5.1 l.690, l.850) | 3.4 R5 | None |
| 14 | Ceit D5.7 record | 6.6 L1055, L1061 (ABS inspection-planning MOVED) | 3.2 KER6 | WP4/WP6 wording (finding 5) |
| 15 | Clement Germany's record | 6.3 L954–961 (FLOW-3D Hydro, D4.1/D4.3 requirements, D7.2 rating) | 3.2 KER3, 3.3, 3.4 R2 | None |
| 16 | SINTEF methods | 6.4 L993 (lift/drag correlations kept) | 3.2 KER4 | None |
| 17 | KER7 | 6.7 L1080 (Task 7.1/D7.1, data suppliers, WP7, 19 risks) | 3.2 KER7, 3.4 R11 | None |
| 18 | D7.4 on ACCIONA-mix breakwaters | 4.6.1 L699 | 3.2 KER2, 6.2 L929 | None |
| 19 | Sunlit Sea's own work | 6.1 L890–894 | 2.5 L258 | BRIDGE author lost (finding 4) |
| 20 | KPI figures | 2.5 L172 | Exec L36 | None; counts recounted, 11/16 and 3+1+3+5+7+1+2 = 22 |
| 21 | Funding scenarios | 4.7 L742–758 | Section 15 L1309 | None; model run matches |
| 22 | EUPI-PV 2029 | 4.6.2 L713; 10 L1203 | Section 5 | None |
| 23 | Small wavebreakers | 4.7 L761 | Section 5 L853 | None |

Other round-4 edits checked against sources:
- the D4.1 shell reason, R3 and 4.10 (D4.1 l.215);
- D6.1's 8–10 kN (l.773–779);
- the D5.1 trade-off and Pareto front (l.1538, Table 9, Tmax/Tproof 2.46);
- the breakwater "especially effective" below Tp 5 s (l.846);
- the D5.1 DIFFRAC conclusion (l.656, l.660);
- the D5.3 hinge note (l.1004);
- the D7.6 split layout, North Sea only (l.483);
- the D4.2 thermal cycling (l.691);
- the EIC proposal's rights statement (l.26) and tasks 2.1 and 2.2, M1–M6 (l.369, l.373);
- D2.2 version 2.0;
- D8.5 version 3.0 of 15 August 2024 (l.50);
- the Sensors s25196234 funder (Crossref: EU award 1011122184, WILLOW);
- the Energies 17(9) 2059 authors (Crossref: MARIN, Ceit, SINTEF, Sunlit Sea, Clement);
- Zenodo 10960431 as the concept DOI of 10960432 (same record, CC BY 4.0, 11 April 2024).

All are OK.

## Claims ledger (changed text; OK items briefly)

| # | D8.4 line | Claim (short) | Source | Status |
|---|---|---|---|---|
| 1 | 13, 392 | Start TRL 2–3, aim TRL 4–5; R1 TRL 5 in a relevant environment | GA l.5730, l.5736, l.7660 | OK |
| 2 | 337–351 | Target TRLs: R2 4, R3 5, R4 5, R5 5, R7 4–5, R8–R10 5 | GA l.5833, 5892, 5924, 5981, 6065, 6121 | OK |
| 3 | 274 | Sample 18 = 1,950 kg/m³ | D4.1 l.1259 (near 2,000) | WRONG (finding 1) |
| 4 | 343, 845 | Shell must be the waterproof layer, as light or thin as possible | D4.1 l.215 | OK |
| 5 | 278, 1157 | D5.3 notes the hinges as most prone to failure; further modelling announced | D5.3 l.1004 | OK |
| 6 | 406 | D6.1: 8–10 kN expected from WP5; redesign recommended | D6.1 l.773–779 | OK (note 14) |
| 7 | 409–410 | Paired v2 corner hinges; 14 → 37 kN; 34/33/40 vs 45/43/54 kN | D7.6 l.687–689, l.719–721; Preprints 202611.1173 | OK |
| 8 | 411 | Rope about 10 kN, under a third of 33–34 kN; rod about 42 kN | D6.3 (5 × 2.04; 5 × 8.36) | OK |
| 9 | 455 | Technical lead authored D2.4, D7.4, D8.5 | Version tables | UNDERSTATED for SINTEF (finding 3) |
| 10 | 503, 522, 589, 1165 | DNV verified the Generation 1 design basis to RP-0584 in 2022 | project_facts l.122; DNV news 2022 | OK |
| 11 | 526 | Split layout assessed for the North Sea only | D7.6 l.483 | OK |
| 12 | 715 | Shares: demonstrator about 1× to several times the PV plant; about a tenth at 5 MWp; a few per cent at tens of MWp | r4 share run (46–80 % → 0.85–4×; 11 %; 2–4 %) | OK |
| 13 | 730–771 | Ratio 3.44–3.98; GM 14 %; scenario table; sensitivities | fm.md | OK |
| 14 | 754 | EIC and EU-upside cases better than base; lowest cash 2028 | fm.md (923, 932) | OK |
| 15 | 843 | Fairlead and anchor loads rise | D5.1 l.1538 | UNSUPPORTED in part (finding 6) |
| 16 | 844 | D8.3 170,000 t per plant over 25 years; 7,000 t a year; 70,000 t per 50 MWp farm (1,240 MW / 25) | D8.3 l.31; GA l.7660 area | OK |
| 17 | 925 | Thermal cycles −15 to +60 °C, one month, ACCIONA chamber | D4.2 l.691 | OK |
| 18 | 1026 | DIFFRAC reproduces general motion; hinge loads and large-field motions uncertain | D5.1 l.656, l.660 | OK |
| 19 | 1028 | Most effective below Tp 5 s; highly effective on vertical loads; CFD robustness; safety factors | D5.1 l.690, l.846, l.850 | OK |
| 20 | 1030 | Up to about 2.5 × fairlead tension; weighting left open after consultation with Clement | D5.1 Table 9, l.1538 | OK |
| 21 | 1032, 1536 | Energies 17(9) 2059 led by MARIN with SINTEF, Clement, Ceit, Sunlit Sea | Crossref | OK |
| 22 | 1032, 1530 | Dataset doi 10.5281/zenodo.10960431, April 2024 | Zenodo API (concept of 10960432, 11 April 2024) | OK |
| 23 | 1061 | Calibrated on WP4 and WP6 data | D5.7 l.91 | CONFLICT (finding 5) |
| 24 | 1155 | EIC: SINTEF, Sunlit Sea, Clement hold the rights | EIC v1 l.26 | OK (wording, finding 7) |
| 25 | 1197 | Council's MariSol record lists Stadt wave-tank tests | pb_317808.html | OK |
| 26 | 1205 | Both sites assessed M1–M6; Clement site characterisation, Sunlit Sea requirements | EIC v1 l.369, l.373 | OK |
| 27 | 225 | Sensors 2025 s25196234 funded by WILLOW only | Crossref funder award 1011122184; KPI record l.71 | OK |
| 28 | 260, 1529 | "Registered" six (Sunlit Sea) etc. | Zenodo owners (520003 owns 13) | UNSUPPORTED verb (finding 2) |
| 29 | 1529 | Metocean 86 views / 50 downloads, second among datasets | Zenodo snapshot 19 Nov (86/50; cost model 223/101; Clement 84/46) | OK |
| 30 | 1409 | NaturSea-PV coordinated by Tecnalia | CORDIS 101084348 | OK |
| 31 | 1502 | BRIDGE entry "written by Sunlit Sea" | KPI record l.199 (Isdahl) | UNDERSTATED (finding 4) |
| 32 | 1558 | D2.2 version 2.0, 1 Feb 2023 | D2.2 version table | OK |
| 33 | 1585 | D8.1 due month 6; Zenodo 8278574 | Zenodo API (31 March 2023; creator Isdahl) | OK (wording, note 13) |
| 34 | 1589 | D8.5 version 3.0, 15 August 2024 | D8.5 l.50 | OK |

## Earlier rejections in my area

- rejected_r4, r4_facts #6 (mid-2027 against Q3 2027): holds for D8.4, as an owner action.
- rejected_r4, #9 (Booster team line): holds. project_facts l.18 gives the technical lead "product development, sales"; D8.4's "product development of the site-planning tool" is narrower but does not conflict, since the CEO holds the Generation 2 work (project_facts l.19).
- rejected_r4, #10 (risk-assessment row): holds as an owner question (Q91); the repo file is unchanged.
- rejected_r4, #13 (research-note URLs): holds.
- rejected_r4, #14 (Zenodo …431 against …432): holds. The API shows that …431 is the concept DOI of …432, so it is the same record.
- rejected_r3, r3_facts #12, #13, #14 and r3disp_A #20: hold.

## Earlier facts findings: status

r4_facts findings 1, 2, 3, 4, 5, 7, 8, 11 and 12 are fixed, at L715 and L1202, L1026, L1558, L1409, L844, L730, L1309, L466 and L344. Findings 6, 9, 10, 13 and 14 were rejected, and the rejections hold (above).

Findings: 1 major, 7 minor, 8 wording.
