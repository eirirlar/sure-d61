# T150 round 4 – fact-check of d84_merged.md (persona: fact-checker)

Checked 24 November 2026. d84_merged.md (1,595 lines) is byte-identical to d84_merged_r3.md. I diffed it against d84_merged_r2final.md: 370 lines are new or changed. I read all of them, and checked every figure, date, name, DOI, period and attribution in them against the primary sources. Line numbers refer to d84_merged.md.

Sources:
- the repo files (paths relative to C:\dev\src\sure-d61);
- live Crossref (citation counts, licences, abstracts) and the NCBI PMC ID converter;
- the Zenodo community API (communities/surewave/records: 18 records);
- web searches for the RWE/SolarDuck release, the DNV/Sunlit Sea release and the EU PVSEC 2026 venue;
- the CORDIS and Prosjektbanken snapshots in scratchpad_t150\web.

I re-ran both models. `PYTHONIOENCODING=utf-8 python scripts/hrb_financial_model.py --md` and `python scripts/breakwater_classes.py` both exited 0. Their outputs are in the session scratchpad, r4\fm.md and r4\bw.txt. No repo file was written, and no git was run.

## Findings

### Major

1. Major. 4.6.2, L709: "from the demonstrator (50–300 kWp in the EIC Transition proposal)". Also in the share table rows "Demonstrator, 50 kWp" and "Demonstrator, 300 kWp" (L720–721), and in Section 10, L1205: "with a demonstrator of 50–300 kWp".
   What is wrong: UNSUPPORTED attribution. The submitted proposal (generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md) gives no demonstrator size. It only says "an integrated pilot-scale demonstrator" (l.72), and a grep for kWp finds only the 105 kWp Skiftestjørna reference (l.163). The 50–300 kWp band is in Sunlit Sea's own work-package contribution of 17 August 2026 (generic/background/eic/2026-08-17_eic_sunlit_sea_wp_contribution.md l.55, l.146, l.358). It is a planning band for its Task 5.2 budget, with "final size determined by site selection and consortium decisions". The coordinator, SINTEF, will read the attribution against the proposal it submitted.
   Fix, L709: "as the plant grows from a pilot-scale demonstrator (50–300 kWp in Sunlit Sea's planning for the EIC Transition proposal; the proposal sets the size at site selection) to commercial size".
   Fix, L1205: "with a pilot-scale demonstrator (Sunlit Sea plans 50–300 kWp)".

### Minor

2. Minor. 6.5 (MARIN), L1031: "the heave and pitch motions were generally similar to the measured ones, and D5.1 concludes that measured and simulated motions agree well."
   What is wrong: OVERSTATED. D5.1 contains no "agree well" (grep). Its conclusion reads: "DIFFRAC can reproduce the general motion behaviour, including shielding by the fore floaters". It also notes that "some differences are notable": the surge RAOs are shifted, heave is over-predicted in short waves, and pitch in long waves. It adds that "the computed hinge loads and the motions in large fields come with high uncertainty" and that the motions are validated only up to a 1×6 array (2024-04-16_surewave_d5.1.md l.644–660).
   Fix: "the heave and pitch motions were generally similar to the measured ones, with differences in surge and in short-wave heave, and D5.1 concludes that DIFFRAC reproduces the general motion behaviour, including the shielding by the forward floats, for arrays of up to 1×6 modules."

3. Minor. Annex B, L1561: D2.2 "Version 1.2, 31 January 2023".
   What is wrong: WRONG version. The D2.2 version table runs 1.0 (30.01.2023) to 1.4, and ends with "2.0 | 01.02.2023 | Thomas Pehlke | Final version". The delivery-date field is blank, and the file is dated 2023-02-01 (2023-02-01_surewave_d2.2_requirements_surface_mooring_system.md l.42–55).
   Fix: "Version 2.0, 1 February 2023 (due 31 January 2023)".

4. Minor. Annex A.8, L1412: "Joint webinar with NaturSea-PV, coordinated by Tecnalia, 2 February 2026, with speakers from SINTEF, Ceit, TU Darmstadt and Tecnalia".
   What is wrong: CONFLICT between sources, not flagged.
   - The webinar summary lists the presenters as Virgile Delhaye (SINTEF), Neven Ukrainczyk and Max (TU Darmstadt) and Aritz (Ceit). Its co-host is "Adriana (NaturSea-PV)", with no organisation given (2026-02-02_surewave_natursea_pv_joint_webinar_summary.md l.5–10).
   - The KPI record says "with TU Darmstadt and TECNALIA speakers" (2026-11-19_surewave_wp8_kpi_verification.md l.130).

   The summary was written from the recording and is the more specific source.
   Fix: "with speakers from SINTEF, Ceit and TU Darmstadt, co-hosted by NaturSea-PV". Alternatively, name the co-host's organisation if the recording shows it. Align the KPI record.

5. Minor. 4.10 impacts row, L855: "D7.6 ... gives no per-farm figure comparable with the proposal's."
   What is wrong: CONFLICT with the technical brochure D8.3 and incomplete.
   - D8.3, led by Sunlit Sea, states "of the order of 170,000 tonnes CO2-equivalent saved per reference plant over 25 years against a coal-fired marginal reference" and attributes it to IFEU's assessment (2026-09-28_surewave_d8.3_technical_brochure.md l.31, l.226).
   - D7.3 gives the climate impacts "per plant and operating period of 25 years" (2025-10-06_surewave_d7.3_environmental_report.md l.1278–1286, Figure 17).
   - 170,000 t over 25 years is about 7,000 t a year, a tenth of the proposal's 70,000 t a year per farm. The 4.1 list of D8.3 differences does not mention it, and the KPI record notes that D8.3's rounded Fig. 19 values were "not yet checked".

   Fix, L855: "D7.3 gives the climate impact per plant over 25 years (Figure 17), and D7.6 finds that offshore floating PV can replace fossil-based electricity ... The technical brochure D8.3 derives from these about 170,000 t CO2-eq avoided per D7.4 reference plant over 25 years against coal power, about 7,000 t a year, a tenth of the proposal's per-farm target, for a 10 MWp plant against the proposal's farm size". Add a seventh point to the 4.1 list of D8.3 differences if the 170,000 t is not confirmed against D7.3.

6. Minor. 4.7 / 4.9 against the financial plan (requirement 6). D8.4 places the first Norwegian reference plant "in operation from Q3 2027" (L753; M3 Q3 2027, L834; 4.9 L820, L1299).
   What is wrong: CONFLICT. The financial plan says "Skien havn, commissioned mid-2027" twice (surewave/deliverables/2026-11-22_surewave_hrb_financial_plan_ker1.md l.102, l.175; the same in the companion copy). project_facts.md l.45 also has "target commissioning mid-2027". The roadmap M3 says Q3 2027 (2026-11-11_surewave_hrb_exploitation_roadmap_ker1.md l.70).
   Fix: align the financial plan to "commissioned in Q3 2027", or write "mid-2027 (Q3)" in both.

7. Minor. 4.7 table, L739: "Three and a half to four times the 2027–2029 total" (2030–2031 revenue against 2027–2029).
   What is wrong: the model run gives 3.82 (base and grant downside), 3.98 (EIC) and 3.44 (EU upside: 12,553 / 3,647 kEUR). The text says the table "holds in all four funding scenarios", so the EU upside falls just outside the stated range.
   Fix: "About three and a half to four times".

8. Minor. Conclusions, L1312: "The plan depends on three conditions: the kit price holds; ...; and the Norwegian reference plants come on time and perform as designed, and kit volume, including a first 10 MW-class supply contract by 2030, comes as planned."
   What is wrong: inconsistent with 4.7 (L780–782) and the model run.
   - Losing the 10 MW-class contract leaves 2031 EBITDA at +685 kEUR and the lowest cash at 620 kEUR.
   - A kit price 6–7 % lower leaves 2031 EBITDA at +1,462 kEUR.
   - A 30 % lower kit volume leaves 2031 EBITDA at +973 kEUR.
   - Only the one-year delay (−105 kEUR) and the combined downside (−619 kEUR) turn 2031 EBITDA negative.

   "Depends on" overstates the price and contract conditions, and the financial plan has no such three-condition sentence.
   Fix: "The plan is most sensitive to the timing of the Norwegian reference plants: a one-year delay makes 2031 EBITDA slightly negative and needs about €0.5M more equity. A lower kit price or volume, or the loss of the first 10 MW-class contract, lowers the result but keeps 2031 EBITDA positive. The first plants need investment support of about a quarter of their cost (Section 4.7)."

9. Minor. r3 finding 8(b) is still not fixed (companion). The Booster business plan, in both the repo copy and the scratchpad companion copy, still says "Technical lead Eirik Larsen is responsible for product development, sales and administration" (2026-11-14_surewave_hrb_business_plan_ker1.md l.20). D8.4 4.2, L448, says "the technical lead is responsible for the site-planning tool, sales, projects and administration", from the value chain analysis.
   Fix: correct the companion.

10. Minor. r3 findings 9 and 13 are still not fixed (companion; the risk assessment is not in the companions folder). Row "Breakwater cost makes exposed sites uneconomic" in 2026-11-11_surewave_hrb_risk_assessment_ker1.md l.15 still says "breakwater €1.3–1.5 million, about 15 % of total investment" and "first breakwater site". The row of l.30 still says "IFE for structural design".
    - D8.4 4.6, L683, now says "about €1.2M in conventional concrete, about 13 %". D7.4 l.568–572 gives €1,221,594 for conventional concrete; €1.34–1.51M are the LWAC, hybrid and SUREWAVE LWAC variants.
    - "First breakwater site" is a term that decision D6 bans.
    - D8.4 uses "IFE for structural simulation" throughout (L600, L798).

    The risk assessment is cited in D8.4 4.8 as "revised on 23 November 2026 to match the financial plan". Its sensitivity figures do match the model run: −€3.6M, −€2.4M, −€0.94M, −€0.4M per €0.03/W.
    Fix the row: "breakwater about €1.2M in conventional concrete, about 13 % of the investment (€1.3–1.5M with LWAC or hybrid shells)"; "at the first site with a breakwater class"; "IFE for structural simulation".

### Wording

11. Wording. 4.3, L459: "whose first unit has been in testing since July 2026 (pv magazine, July 2026)". The research note gives: first unit "Paiporta" "arrived 13 July 2026 for testing outside the southern breakwater" (Valenciaport), and pv magazine 14 July 2026, "Port of Valencia activates first 500 kW floating offshore PV unit" (surewave/background/2026-11-14_hrb_business_plan_research/competitors.md l.89, l.180–181). The text is supported. "Activated and in testing since mid-July 2026" would match the cited headline more closely. The list of the largest European marine units omits Oceans of Energy's Hollandse Kust Noord array, which the research note ranks with them (l.7). It is covered two paragraphs later, so this is acceptable.

12. Wording. 3.4 R4, L338: "365 kg/m³ was the best density result of D4.1's 26 cellular-concrete trial mixes". D4.1 states "The best density result achieved from Sample 10 to Sample 26 was 365 kg/m³" (the circular mixes with Minolite; Samples 1–9 used expanded clay), and Sample 26 was "selected ... due to its lowest density and highest sustainability" (2024-01-18_surewave_d4.1_design_characterization_circular_materials.md l.1233–1235). Write "the best density result of D4.1's 17 circular cellular-concrete mixes (Samples 10–26), out of 26 trial mixes".

13. Wording (source hygiene, no text change). Two external facts in 4.3 and Section 12 are correct but rest on no repo note:
    - SolarDuck's Merganser pilot was installed in July 2024 (RWE press release of 4 July 2024, rwe.com/en/press/rwe-offshore-wind-gmbh/2024-07-04-solarduck-and-rwe-successfully-install-offshore-floating-solar-pilot-meganser; pv magazine 4 July 2024). The research note's S15 is an undated ALCircle reprint.
    - "In 2022 DNV verified Sunlit Sea's design basis ... (DNV news release, 2022)": dnv.com/news/2022/dnv-verifies-sunlit-sea-s-design-basis-for-floating-solar-pv-to-rp-0584-227297 (June 2022). The release states the design basis is general, not site-specific, which matches "a general design methodology". In the repo, only project_facts.md l.122 and the auditor pack mention the verification.

    Add both URLs to competitors.md and technology_standards_ip.md.

14. Wording. 6.5 Result 3, L1037: "the test data in a Zenodo dataset (doi 10.5281/zenodo.10960431, April 2024)". The Energies 19(7) 1609 data statement cites "https://zenodo.org/doi/10.5281/zenodo.10960432" as the basin data used for validation (2026-03-25_bunnik_hydrodynamic_simulations_2mw_offshore_solar_fpv.md l.282). This is probably the concept DOI of the same record. No change is needed if …431 resolves to the version cited in Energies 17(9). Check that both resolve to the same record before submission.

## Claims ledger (changed text; OK items briefly)

| # | D8.4 line | Claim (short) | Source | Status |
|---|---|---|---|---|
| 1 | 13 | Start TRL 2–3; D7.2 TRL 5; D7.6 IFEU Nov 2025; Gijón results Nov 2026; EIC TRL 4 | GA l.5730; Preprints 202611.1173 abstract (Crossref); D7.6 cover 05.11.2025; Preprints 202611.1592 posted 16 Nov 2026 | OK |
| 2 | 32, 168 | 11 of 16 met; 22 further targets: 3 met, 1 met 2024 only, 3 partly, 5 not met, 7 not measured, 1 not shown, 2 open | Recount of both tables, L176–247 | OK |
| 3 | 32, 227 | 41 citations of 7 DOI papers | Crossref today: 23 + 11 + 5 + 2 + 0 + 0 + 0 = 41 | OK |
| 4 | 189, 1476 | 9 interviews: 2 Rostock, 7 Wideangle | KPI record l.262–282 (5 Nov 2026 clips + Delhaye + ACCIONA = 7; Breyer, Pehlke) | OK |
| 5 | 191, 1494 | Infographics 5: three cards, Ceit gif, CINEA poster | KPI record l.180–190 | OK |
| 6 | 1532 | 18 Zenodo records; 12 deliverables; 6 others; cost model 223 views / 101 downloads on 19 Nov | Zenodo API today: 18 records; same 12 deliverables; cost model now 228 / 102 (consistent); cost model pub. 2025-11-05 | OK |
| 7 | 1540 | Sensors in PMC11244420 | NCBI idconv: PMC11244420 | OK |
| 8 | 1539–1545 | Licences CC BY 4.0 (MDPI, FFE 49(11)) | Crossref licence fields; FFE published 27 Aug 2026 | OK |
| 9 | 403 | Hinge 14 → 37 kN; 34 / 33 / 40 kN vs 45 / 43 / 54 kN; North Sea about 8 % above | Preprints 202611.1173 abstract | OK |
| 10 | 940, 1062 | Prototype 3.40 × 1.70 × 1.05 m; > 85 % fouling; 35 mm; 0.6 % chloride; ±135 Ω; 0.35–0.45 Hz; authors ACCIONA / SINTEF / Ceit | Preprints 202611.1592 abstract and authors | OK |
| 11 | 1029 | 3,660 modules; 32 breakwaters; axial up to 20 %, vertical up to 50 % | Energies 19(7) 1609 conclusions (bunnik md l.274–276) | OK |
| 12 | 386, 402, 1037 | 1:10, 3 × 5 array, breakwater across the basin; second campaign longer, thicker paired connectors; second-campaign motions used for validation | bunnik md l.70–72, l.122 | OK |
| 13 | 664, 672–681 | D7.4 v2.0 20.11.2026; request of 16 Oct 2026; six correction bullets; v1 → v2 figures | D7.4 version table; l.486–500 | OK |
| 14 | 683, 693 | Breakwater €1.22M ≈ 13 %; €212/kWp; +24 % LWAC, +76 % HPC; LCOE 0.076 → 0.085 | D7.4 l.568–572, l.817–828, l.1146 | OK |
| 15 | 854, 860 | €940/kWp, 40 % below €1,560; OPEX €17.4 (31 % below €25.4); NPV €20.8M at 4 % | D7.4 l.825, l.857, l.1105–1111 | OK |
| 16 | 371, 848 | D3.3 10 MWp, about 18,600 panels of 537 Wp, ring 346 m; D3.4 7.16 MWp; 2 MWp ring 173 m; 10,375 kWp, about 730 Wp | D3.3 l.383, l.394; D3.4 Table 7 (7,157,13x Wp); Clement report l.33; D7.4 l.576, l.810 | OK |
| 17 | 735–782 | Financial plan: break-even 2030 in all four scenarios; 28 MWp; equity 3.5 + 2.0; uses about €0.1–0.3M of round 2; GM 14 % (2028), 41–44 %; EU funding +€0.7M / +€0.9M; delay −€0.3M lowest cash, +€0.5M equity; 10 MW loss EBITDA and cash positive; combined downside +€1.0M; wavebreakers −€0.1M cash / −€0.05M result; minority share €0.2M; SuRE about €0.4M | Model run fm.md (347/2,515 = 13.8 %; 3,537/8,181 = 43.2 %; 3,493 − 2,796 = 697; 3,493 − 2,633 = 860; −314, 514, 685/620, 1,006, 794, −1,486); fin. plan l.31, l.70, l.168 | OK (except finding 7) |
| 18 | 743 | 28 % at permitted, named or lead sites; 7 / 16 MWp in 2030 / 2031 | Fin. plan l.112–116 (13 % + 15 %), l.599 (7.2 MWp), table (2 + 14) | OK |
| 19 | 711–724 | Shares 1 MWp 15 % / 25 %; 5 MWp 6 % / 11 %; LCOE about €0.10 | bw run: 0.142/0.97, 0.283/1.11, 0.054/0.88, 0.107/0.94; LCOE 0.099 | OK |
| 20 | 418–436 | Classes: fetch 1.6 / 3.8 / 6.4 km; 30 / 73 / 123 t; 2.5 × 1.0, 4.0 × 1.5, 5.0 × 2.03; lightest sections | bw run | OK |
| 21 | 793–814 | 26 risks; ratings 56, 56, 54, 54, 45, 42, 42, 42, 40, 40, 36, 35, 32, 28, 24, 24, 21, 20, 15; zones | Risk assessment l.9–34 (26 rows) | OK |
| 22 | 497 | SAB webinar 19 Nov 2024: 31 sign-ups, about 23; two mismatch questions; 12–13 %, 10 %, 2–3 % | Lunch webinar summary l.10, l.50 | OK |
| 23 | 448 | Founded 2019, Oslo; 60 kWp Germany 2023; 105 kWp PPA 2024 – Oct 2026; factory wound down 2024 | project_facts l.11, l.19, l.31–34 | OK |
| 24 | 30, 1130 | Patent attorney: no patentable technology in Gen 2 (prior art); old patent on sandwich float | Booster meeting summary l.24 | OK |
| 25 | 733 | Annex chosen 13 Nov; next workshop Dec 2026 | Booster summary l.13–15, l.114 | OK |
| 26 | 1146–1160 | D1.8 Table 3, seven actions and responsibilities; §4.5 roles; FTO sentence | D1.8 l.483–500, l.663, l.671–691 | OK |
| 27 | 1199–1205 | SuRE 1 Sep 2024 – 31 Aug 2027, IFE; MariSol 317808, 2020–2025, partners, Stadt; SFI BLUES 2020–2028, SINTEF Ocean; EIC submitted 16 Sep 2026, LoI 8 Sep 2026, lapse 28 Feb 2027, M22, M34 DNV SoC, about €2.5M, 12–24 months | CORDIS snapshot; Prosjektbanken 317808 and BLUES; LoI md l.48, l.73; EIC v1 l.81–93, l.254, l.318 | OK (except 50–300 kWp, finding 1) |
| 28 | 1260–1261, 1250 | GA transfer: 45 days, 30 days, waiting rule; objection 60 days, stand-still | GA l.8919–8992 | OK |
| 29 | 1281 | Impact evaluation up to 5 years after final payment | GA Data Sheet l.540 | OK |
| 30 | 1299 | Final periodic report by 1 March 2027 | 60 days after 31 Dec 2026 = 1 Mar 2027 | OK |
| 31 | 1366 | EU PVSEC 2026 Rotterdam, 17 Sept | eupvsec.org: 14–18 Sept 2026, WTC Rotterdam | OK |
| 32 | 1369 | 14 conferences by partner (4 / 4 / 3 / 2 / 1); 7 + 2 + 2 + 3 | A.4 table L1355–1367 | OK |
| 33 | 932, 934 | 8.2 → 0.6 mm; 0.4–0.9 × 10⁻¹² m²/s; > 55 % stronger, 50 % strength-to-weight | D4.2 l.442, l.964–968 | OK |
| 34 | 296, 338 | CLC 365 kg/m³, 25 kg cement, 26 mixes, 300–400 kg/m³ aim | D4.1 l.607, l.1233, l.1287 | OK (finding 12) |
| 35 | 1002 | Fabric band from specimen 4; preprint "final two"; mean 40.88 kN, 2.7 % below | D6.1; Preprints 202611.1612 (r3) | OK |
| 36 | 903 | Injection-moulded segments delivered by Sunlit Sea to SINTEF | D6.3 l.273 | OK |
| 37 | 808 | 1–2 mm gaps from shrinkage | D6.3 l.285 | OK |
| 38 | 1168 | DNV-ST-C108 / ST-E309 2026; RP-0584; IEC TS 62548-3, TS 63496 in draft; DNV 2022 verification | project_facts l.122–124; technology_standards_ip.md l.10, l.37–38; dnv.com 2022 news | OK |
| 39 | 1031 | D5.1 "agree well" | D5.1 l.644–660 | OVERSTATED (finding 2) |
| 40 | 1561 | D2.2 version 1.2 | D2.2 version table | WRONG (finding 3) |
| 41 | 1412 | Tecnalia speakers | Webinar summary vs KPI record | CONFLICT (finding 4) |
| 42 | 855 | No per-farm CO2 figure | D8.3 l.31, l.226; D7.3 Fig. 17 | CONFLICT (finding 5) |
| 43 | 266 | Five partners replied 30 Sep – 5 Oct 2026 | Ceit header (parts 30 Sep and 5 Oct); SINTEF 2 Oct | OK |
| 44 | 1553–1592 | Annex B dates: D1.7 30 Sep 2026; D3.4 v3.0 31/05/24; D7.3 v4; D7.5 v3; D8.2 v2.0 24 Sep 2025; D6.2 Zenodo 10 Mar 2025; D8.3 18 Nov 2026 (meta); D7.4 v1.0 30 May 2025 | Covers and version tables; Zenodo API; D8.3 meta.yaml | OK (except D2.2) |
| 45 | 1518 | D8.3 v0.2 SINTEF 5 Nov, v0.3 IFEU 16 Nov, v1 17 Nov | D8.3 meta.yaml version history ("Guido") | OK |
| 46 | 459 | SolarDuck 0.5 MWp installed July 2024 | RWE release 4 July 2024 | OK |

## Earlier rejections in my area

- rejected_r3 r3_facts#12 (Ciel & Terre 820 MW against CORDIS 650 MW): holds.
- rejected_r3 r3_facts#13 (structural simulation): holds for D8.4. The companion is still unaligned (finding 10).
- rejected_r3 r3_facts#14 (A.10 board list): holds.
- rejected_r3 r3disp_A #20 (ACCIONA date, from the covering e-mail of 26 Nov 2025): holds.
- rejected_r2 r2_facts#15 (D6.3 conclusions quote): holds.

## Earlier facts findings: status

r3_facts findings 1–7 are fixed in the text:
- 1: L609;
- 2: WP3 credit at L15, L297, L901 and L959;
- 3: L1002;
- 4: L672–679;
- 5: L438 and L712 now name "D7.4's cost model" (L712 only by pointer to 4.1.1);
- 6: L1553;
- 7: L1559.

Finding 8(a), 27 guests, is fixed in the companion KPI record. Findings 8(b), 9 and 13 are still open in the companions (findings 9 and 10 above). Finding 10, the canvas review, was rejected with a source, and the rejection holds. Findings 11 and 13 above repeat r3 finding 11 for SolarDuck and DNV.

Findings: 1 major, 9 minor, 4 wording.
