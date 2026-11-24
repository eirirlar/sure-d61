# T150 round 3 – fact-check of d84_merged.md (persona: fact-checker)

Checked 24 November 2026. I read d84_merged.md in full (1,541 lines; identical to d84_merged_r2.md) and compared it with d84_merged_r1.md. Since round 2 the text was restructured: Annex A and Annex B were added, and evidence was moved to one home per item (r2_integration_log.md). Most sentences changed, so I re-checked every figure I could find in the body. I gave most weight to figures that moved, and checked that each one still carries its source at its new home and at every pointer.

Sources:
- the repo primary files (paths relative to C:\dev\src\sure-d61);
- the Grant Agreement work-package, task and deliverable descriptions (GA l.3862–5480);
- Crossref records for the four preprints and the journal papers (cached JSON in the session scratchpad; the ILCSA reference was fetched live from api.crossref.org today);
- the CORDIS and Prosjektbanken snapshots in scratchpad_t150\web;
- a web search for the SolarDuck certificate (pv-magazine.com/2024/03/28/bureau-veritas-certifies-solarducks-offshore-pv-platform and marine-offshore.bureauveritas.com newsroom).

I re-ran both models. `PYTHONIOENCODING=utf-8 python scripts/hrb_financial_model.py --md` wrote its output to the session scratchpad, r3facts\fm.md. `python scripts/breakwater_classes.py` overwrote the existing scratchpad file bw.txt, which can be regenerated from the script. Line numbers refer to d84_merged.md.

## Findings

### Major

None found. All figures that depend on the two models match a fresh run. The Annex B lead beneficiaries and dissemination levels match the Grant Agreement deliverable descriptions (see the ledger).

### Minor

1. Minor. 4.4.1 single-point-of-failure table, L602: "One local contractor on both larger Norwegian projects".
   What is wrong: WRONG. The value chain analysis names Prosolar on the first reference plant (Skien havn, a few hundred kWp) and on the first multi-megawatt plant. The two larger sites are the multi-megawatt plant and the third reference plant (surewave/deliverables/2026-11-23_surewave_hrb_value_chain_ker1.md L35, L70; risk assessment 2026-11-11_surewave_hrb_risk_assessment_ker1.md, row "One local contractor on both Norwegian projects": "Skien havn and Gunneklevfjorden"). The intervention "a second contractor ... for the later plants" refers to the third plant, which shows that the third plant is not one of the two.
   Fix: "One local contractor on the first two Norwegian reference plants (the port plant and the first multi-megawatt plant)".

2. Minor. Clement Germany's work-package lead is not credited anywhere. Sections 3.2, 6.3 and 15 list Clement Germany's design work, and 6.1 says "In WP3 it [Sunlit Sea] led the design of the internal floating PV components (Task 3.1, D3.1) and ... (Task 3.5, D3.4)".
   What is wrong: UNDERSTATED (requirement 4, credit). The Grant Agreement makes Clement Germany the lead of WP3, Development of the floating PV system (GA l.3998, and the WP list at l.3736). D8.4 credits every other WP lead: SINTEF WP1 and WP6, Sunlit Sea WP2 and WP8, ACCIONA WP4, Ceit WP5, IFEU WP7. Only Clement Germany's is missing. 6.1, read alone, can suggest that Sunlit Sea led WP3.
   Fix, 6.3 first paragraph: "Clement Germany led WP3, the development of the floating PV system with its breakwater, mooring and connections, and within it Tasks 3.2–3.4 (D3.2, D3.3)."
   Fix, 6.1: "In WP3, led by Clement Germany, Sunlit Sea led the design of ...".

3. Minor. 6.4, L974: "The first two specimens failed at the interface between rope and bracket at about 38 kN; with that interface protected, the next three reached 41.1, 43.7 and 42.9 kN (D6.1; Preprints 202611.1612)."
   What is wrong: CONFLICT between the two cited sources, not flagged.
   - D6.1 puts the fabric band in place from test 4, which gives the three values 41.1, 43.7 and 42.9 kN (2024-09-12_surewave_d6.1_ultimate_strength_capacity.md L744–748, L763).
   - The newer preprint says "Protection of the bracket-rope interface reduced local abrasion, and the final two specimens reached 43.7 and 42.9 kN" (Crossref abstract, 10.20944/preprints202611.1612.v1).
   - The preprint also states the mean as "approximately 2.7% below the 42 kN design requirement", while D8.4 gives D6.1's reading, "aligned with the requirement".
   Fix: "... the first two specimens failed at the rope–bracket interface at about 38 kN (D6.1). D6.1 places a protective band at the interface from the third valid test (41.1 kN); the preprint reports the last two, 43.7 and 42.9 kN, as the protected ones. The mean of 40.88 kN is about 2.7 % below the 42 kN requirement (Preprints 202611.1612), which D6.1 finds aligned with the requirement."

4. Minor. 4.6, L664–669: "Its rebuilt cost model ... also corrects these errors of version 1.0:" followed by four bullets.
   What is wrong: UNDERSTATED. D7.4 version 2.0 Section 2.5 lists two more corrections (2025-09-05_surewave_d7.4_economic_assessment.md L490–493):
   - the electricity prices of the pessimistic and optimistic scenarios were reversed, and some rows used inputs from the wrong scenario;
   - smaller errors in freight, pontoon cost totals, the PV replacement cost of the 5 × 2 MW cases and the sensitivity tables.

   "These errors" reads as the full list.
   Fix: add the bullet "the electricity prices of the pessimistic and optimistic scenarios were swapped, and smaller errors in freight, pontoon totals, the PV replacement of the 5 × 2 MWp cases and the sensitivity tables were corrected". Or write "among them these errors".

5. Minor. 4.1.1, L431: "It stands 15 m from the array, the distance D7.4 uses for its 2 MWp ring."
   What is wrong: UNSUPPORTED as phrased. The D7.4 report text contains no 15 m stand-off (grep of 2025-09-05_surewave_d7.4_economic_assessment.md). The figure comes from the D7.4 cost model, version 3: 7.5 m + 7.5 m in the 2 MW cases. scripts/breakwater_classes.py L67 still marks it "[CONFIRM]".
   Fix: "the distance in D7.4's cost model for its 2 MWp ring". The same applies to 4.6.2, L698 ("at 15 m from the array").

6. Minor. Annex B note, L1498: "The amended Grant Agreement sets the due date of D1.8, D8.3 and D8.4 at month 48, 30 September 2026."
   What is wrong: the amended Grant Agreement is not in the repo. The dates come from the deliverable records: the D1.8 cover ("Due delivery date 30.09.2026", 2026-09-30_surewave_d1.8_ipr_management_plan_m36.md L26) and the D8.3 and D8.4 meta files (due_date 2026-09-30). The cover line L5 makes the same claim. The 2022 GA in the repo gives month 36 (GA l.5356–5366). This is the open owner question on the amended GA (r2 finding 1), not a contradiction.
   Fix: keep the date, and confirm it against the Portal GA before submission. Until then, "The due date of D1.8, D8.3 and D8.4 is month 48, 30 September 2026, after the amendment of the Grant Agreement" is safer than naming a document no one has checked.

7. Minor. Annex B, L1504: the D1.8 title "IPR Management Plan (M36 revision)".
   What is wrong: the GA title is "IPR- Management plan (M36 revision)" (GA l.4822). Annex B claims to give titles "as set in the list of deliverables of the Grant Agreement".
   Fix: "IPR Management plan (M36 revision)", or note that the titles are normalised. All other 35 titles, lead beneficiaries and levels match the GA descriptions. The D3.4 PU / summary-table SEN row shift is handled correctly.

8. Minor. Companion consistency (requirement 6). Two round-2 fixes were made in D8.4 but not in the companions:
   - (a) The KPI record still says the final-workshop invitation went "to 26 recipients" (2026-11-19_surewave_wp8_kpi_verification.md L154). D8.4 Annex A.9 and the reach table say 27 guests, from the organiser's invitation (r2 finding 9).
   - (b) The Booster business plan still says "Technical lead Eirik Larsen is responsible for product development, sales and administration" (2026-11-14_surewave_hrb_business_plan_ker1.md L20). D8.4 4.2 now follows the value chain analysis (site-planning tool, sales, projects and administration) (r2 finding 13).

   Fix: correct both companions.

9. Minor. Companion consistency with 4.6 and 4.8. The KER1 risk assessment row "Breakwater cost makes exposed sites uneconomic" still says "breakwater €1.3–1.5 million, about 15 % of total investment" and "at the first breakwater site, about 1 MWp" (2026-11-11_surewave_hrb_risk_assessment_ker1.md L15). D8.4 4.6 gives "breakwater and bridge pontoons, with PVC pipes and ropes, about €212/kWp, under a quarter of the reference plant's investment".
   What is wrong: both statements can be right, but they measure different things. The breakwater alone is €1.22M (conventional) to €1.51M (LWAC shell) (D7.4 L563–572), about 12.5–15.5 % of €9.75M. The €212/kWp (about €2.2M, 22.6 %) also includes the bridge pontoons, pipes and ropes. A reader comparing D8.4 with the risk map sees 15 % against "under a quarter". "First breakwater site" is also a term decision D6 bans.
   Fix, D8.4 4.6: "The breakwater itself is about €1.2M, about 13 % of the investment; with the bridge pontoons, PVC pipes and ropes it is about €212/kWp, under a quarter (D7.4)".
   Fix, risk assessment: write "first site with a breakwater class".

10. Minor. Section 2.3 / 4.3.1. "The Horizon Results Booster expert (META Group) reviewed ... on 13 November 2026" (L495) is correct. But 2.3 gives "5–6 November: market definition and value proposition canvases submitted and reviewed in the value-proposition workshop" (L136).
    What is wrong: the cover e-mail is dated 5 November (deliverables/2026-11-05_hrb_canvases_cover_email_to_raluca.md) and the UVP workshop 6 November (background/2026-11-06_hrb_g2m_uvp_workshop.md). No source shows that the canvases were reviewed in the workshop, only that it took place.
    Status: OK if the workshop transcript or slides show the review. Otherwise write "submitted (5 November); value-proposition workshop (6 November)".

### Wording

11. Wording. 4.3, L470: "SolarDuck (elevated platforms): the 0.5 MWp North Sea pilot above (RWE, 2024), with a Bureau Veritas prototype certificate (pv magazine, March 2024)." This is correct in public sources: pv magazine, 28 March 2024; Bureau Veritas news, 27 March 2024, which calls it the first prototype certification, for the 520 kWp Merganser pilot. But it is not in the repo's research notes (competitors.md has no Bureau Veritas entry for SolarDuck). Add the source to surewave/background/2026-11-14_hrb_business_plan_research/competitors.md. Optionally write "a Bureau Veritas prototype certificate for the pilot design (March 2024, before installation)".

12. Wording. 4.3, L474: "Ciel & Terre had completed about 820 MW in 280 projects by mid-2023 (TaiyangNews, 2023)". The SuRE CORDIS description says Ciel et Terre "have installed 650 MW globally" (scratchpad_t150\web\cordis_101135567.html). The TaiyangNews figure is the newer one and is correct to use. No change, but be aware of the difference if a reviewer reads CORDIS.

13. Wording. 4.2, 4.4.1 and 4.8 use "IFE for structural simulation". The risk assessment row says "IFE for structural design" (risk assessment L30). Use one term; "structural simulation" matches project_facts and the value chain analysis. Align the risk assessment.

14. Wording. Annex A.10, L1381: "D2.4 names seven member organisations, three of them with several roles". This is supported by D2.4's member list: Greenlight, Scandinavian Solar Parks and Innovex hold several roles (2024-04-22_surewave_d2.4_stakeholder_advisory_board.md L215–261). D2.4's own sentence says "most of the 7 representatives fulfil multiple roles". D8.4 follows the list, which is the more specific source. No change needed; this is noted in case a partner quotes D2.4's sentence.

## Earlier findings in my area: status

r2_facts.md:
- 1, coordinator and due date: cover fixed per D1r/D1rr. The coordinator's legal entity (CORDIS: SINTEF Manufacturing AS) remains an owner question. See finding 6.
- 2, seven member organisations: fixed (A.10).
- 3, CORDIS against OpenAIRE: fixed (A.23, Section 11).
- 4, biofouling on every surface: fixed (6.2).
- 5, BlueNewables timeline: fixed (4.3).
- 6, €0.12/kWh source: fixed (4.6, "which D7.4 takes as the target price").
- 7, website visits: fixed (reach table and A.22).
- 8, roadmap ratings row by row: fixed (2.3).
- 9, Pehlke moderator: fixed in D8.4. The 26 against 27 invitees is still open in the KPI record (finding 8a).
- 10, density targets: fixed (3.4 R3, R4; 3.1).
- 11, transition pipe: fixed (4.1).
- 12, EPC deliveries to 2031: fixed (4.4).
- 13, technical lead: fixed in D8.4, not in the business plan (finding 8b).
- 14, D5.1 Table 9: fixed (6.5).
- 15, D6.3 conclusion: rejected in r2disp_C with D6.3 L857 ("will avoid earlier buckling and snapping loads"). The rejection holds; 4.1 now quotes that conclusion.
- 16, Fred. Olsen 1848: fixed (4.3).
- 17–19, wording: fixed.

Rejections in my area:
- rejected_r2: r2_cinea F7 (D4.1 cement wording, final report conflict) holds under D22 and D34. D8.4 uses the D4.1 recipe consistently (3.1, 3.2, 3.4, 6.2).
- rejected_r2: r2disp_C r2_partners#M3 holds (Energies 19(7) full text; 4.1 L395).
- rejected_so_far, disp_A A#3 and D1 (coordinator): superseded by D1rr ("Coordinator: SINTEF"). This holds, pending the owner question.
- rejected_so_far: the other entries in my area hold as stated in r2_facts. These are the D3 "factor 2–3" ban, the FTR-only figures (1,030 mixtures, 87 %/97 %, 76 %, 380/350 kg/m³), NVE NO3/NO4, the bottom-plate material, EDP named, IFE as deputy, strategic assets, and D8.5 "April 2024".
- The rejections that r2_facts said did not hold (450 kN, chloride coefficients, 40 % transmission, trial-mix counts, "19 risks") were overturned by D44. All five are now in the text with primary sources: 6.4 L974 (D6.1), 6.2 L913 (D4.2 Table 5), 6.3 L936 (D3.2 summary), 6.2 L911 and 3.4 R4 (D4.1), 3.4 R11 and 6.7 (preprint 1173).

## Moved figures: do they keep their sources? (D40 check)

Each evidence item has one home, and I checked the source cited there. I also checked every pointer to it. Every pointer either names the source deliverable or points to a home that names it.
- Hinge: home 4.1, D6.1, D6.3, preprints 1612 and 1173, D7.6, Energies 17(9) and 19(7). Pointers: 3.2 KER4, 3.4 R1, 4.4 Lean Canvas, 4.8, 6.1, 6.4.
- Mooring: home 6.5, D5.1 Table 9 and summary. Pointers: 3.1, 3.2 KER5, 3.4 R6, 4.1, 4.10.
- Wave transmission: home 6.3, D3.2. Pointers: 3.2 KER3, 3.4 R2, 4.1.1.
- Connection tests and beam tests: home 6.4, D6.1, D4.2 and preprint 1612.
- Gijón materials results: home 6.2, D4.1–D4.3, D6.4 and preprint 1592.
- Sensors: home 6.6, D5.4, Sensors 24(13) and preprint 1592.
- D7.4 economics: home 4.6 and 4.6.1, D7.4 version 2.0 with sections 2.5 and 7.4.
- Stadt Towing Tank: home 6.5, D5.1 and D3.1.
- TRL: home 4.1, D7.2 and preprint 1173, D7.6, EIC proposal.

The executive summary and Section 15 keep summary figures with section pointers. No figure lost its source in the move.

## Claims ledger (checked this round; OK unless a finding above says otherwise)

| # | D8.4 line | Claim | Source | Status |
|---|---|---|---|---|
| 1 | 5 | Topic HORIZON-CL5-2021-D3-03-10; 51 months; due 30 Sept 2026 | CORDIS snapshot (topic-details/HORIZON-CL5-2021-D3-03-10); D1r; D8.4 meta due_date | OK (see 6) |
| 2 | 17, 379, 396 | D7.2 rates TRL 5; v3 ULS 37 against 14 kN; 50-year maxima 45→34, 43→33, 54→40 kN; North Sea about 8 % above | Preprint 202611.1173 abstract (Crossref); D7.6 L689, L719–767 (gives only 54) | OK |
| 3 | 129 | Coordinator applied 30 Sept 2026 on the PO's mid-term recommendation | 2026-10-01_hrb_kickoff_meeting_prep.md L11 ("applied yesterday") | OK |
| 4 | 147 | Characterisation and roadmap ratings; BOSAT above 3 in six dimensions, IP and finance lowest | expert feedback files (rows parsed); meeting summary L12 | OK |
| 5 | 157 | D1.4, D1.8 led by SINTEF | GA l.4763, 4824 | OK |
| 6 | 226 | D8.5 training "digital literacy and social media engagement", video calls | D8.5 L439, L481 | OK |
| 7 | 231 | Four of the seven SAB organisations are companies | D2.4 L215–261 | OK |
| 8 | 245 | Isdahl: roll-up, BRIDGE entry, Matomo set-up | KPI record L172, L199, L300 | OK |
| 9 | 260, 908 | Sample 17 (49 MPa, 1,898 kg/m³); Sample 18, CEM IIIA, 68 MPa, near 2,000; top slab Sample 18; D4.2 1,850; D8.3 about 1,800 | D4.1 L548, L1257–1259; D4.3 L233, L422; D4.2 L659; D8.3 L109 | OK |
| 10 | 331 | All-CLC core almost as large as a full-size unit; EPS; HPC bottom layer | D4.3 L267–271 | OK |
| 11 | 289, 330, 915 | Prototype by ACCIONA, contributing SINTEF and Clement (D4.3); production requirements set by Clement; Task 6.5 led by ACCIONA with Ceit, SINTEF, Clement; D6.4 PU | D4.3 L28, L413; GA l.4360, l.5202 | OK |
| 12 | 915, 1024 | 3.40 × 1.70 × 1.05 m; four-line catenary; >85 % on every surface; 35 mm; 0.6 % chloride only in LWAC top slab; ±135 Ω; 0.35–0.45 Hz | Preprint 202611.1592 abstract | OK |
| 13 | 966 | SINTEF Task 1.4, 1.5, 4.3, 7.1, WP6; 25 HPC and 23 LWAC beams | GA l.3896, 3901, 4137, 4391, 4273; D4.2 L541 | OK |
| 14 | 974 | 402 kN, rated 450 kN, D6.1 "in agreement"; 4 of 5 at terminations; 40.88 against 42 kN | D6.1 L685, L702, L750, L783; preprint 1612 | OK (see 3) |
| 15 | 1001 | 3,660 modules, 32 breakwaters, up to 50 % | Energies 19(7) abstract | OK |
| 16 | 1002 | 56 and 32 breakwater rings; Task 5.2 MARIN | D5.1 L362, L392, L862; GA l.4191 | OK |
| 17 | 970 | Breakwater cuts lift and drag up to 10°, less for a 2 m breakwater | Energies 17(19) abstract | OK |
| 18 | 1022 | Ceit led WP5 and Task 6.1 | GA l.4157, l.4293 | OK |
| 19 | 1047 | Keller, Rettenmaier, Reinhardt, Applied Energy 154, 2015 | Crossref 10.1016/j.apenergy.2015.01.095 | OK |
| 20 | 656–671 | v2.0 responds to the 16 Oct 2026 request; LCOE 0.062→0.076, NPV 8.9→7.3, IRR 10.7→15.6; section 2.5; North Sea ≤3 %; 300 m cable; 730 Wp modules linked to the hinge change | D7.4 L484–500, L506, L576, L589, L1126 | OK (see 4) |
| 21 | 683 | +24 % LWAC, +76 % HPC, LCOE 0.085 | D7.4 L563–572 | OK |
| 22 | 371–372 | D8.3: 4.4/7.0/12.3 m from D2.1; "up to 56 % chain-weight reduction" | D8.3 L65–67, L141; D2.1 L96 | OK |
| 23 | 441 | Founded 2019, Oslo; 60 kWp DE 2023; 105 kWp NO, PPA 2024 to Oct 2026; factory wound down 2024 | project_facts L11–34 | OK |
| 24 | 383 | Prototype 3 cast; prototype 4 in casting | project_facts L35 | OK |
| 25 | 452, 470 | SolarDuck 0.5 MWp July 2024 (RWE); BV prototype certificate March 2024 | generic/background/2026-07-08_market_intel.md L162 (RWE press 4 Jul 2024); pv magazine 28 Mar 2024 | OK (see 11) |
| 26 | 471 | Oceans of Energy, about 1,400 panels, Aug 2025, withdrawn, connector defect (CrossWind, May 2026) | competitors.md L8, L82 | OK |
| 27 | 474 | Ciel & Terre a partner in SuRE | CORDIS 101135567 participants | OK |
| 28 | 638, 640 | Norway <10 MW municipal since 1 July 2025; WHG § 36(3) 15 % and 40 m; Swedish vattenverksamhet | customers_regulation.md L7, L16, L18 | OK |
| 29 | 1112 | IEC TS 62548-3, IEC TS 63496 (design guidelines) at draft stage | technology_standards_ip.md L37–38 | OK |
| 30 | 1090 | Earlier patent on the Gen 1 sandwich construction; Gen 2 patenting not pursued | meeting summary L24; business plan L85 | OK |
| 31 | 945, 1157, 1160 | EIC: TRANSITIONOPEN; Clement leads WP6 (M15–M34); Task 2.1 led by Sunlit Sea, evaluates EDP Alto Rabagão; LOI lapses before 28 Feb 2027; decision Dec 2026 – Jan 2027 | EIC proposal L4, L337, L369; LOI L73; financial plan L169 | OK |
| 32 | 1152–1155 | MariSol lead Sunlit Sea, 2020–2025; FlexiShape MIKO Marine, 2021–2025; SFI BLUES 309281, 2020–2028 (host SINTEF Ocean); CIRCWIND via SINTEF Manufacturing AS | Prosjektbanken snapshots; CORDIS 101147517 | OK |
| 33 | 831, 834 | Proposal: 25 MW pilot 2025–2027; contracts from 2026; first products 2028–2030; first phase 2030–2032; Mediterranean and harshest by 2035 | Annex 1 L887, L891 | OK |
| 34 | 838 | CAPEX 40 % below reference (940/1,560); OPEX 31 % below (17.4/25.4) | arithmetic | OK |
| 35 | 1195 | RP2 from month 19 (April 2024); final report due 1 March 2027 | GA l.436–460; 31 Dec + 60 days | OK |
| 36 | 1500–1537 | Annex B: 36 deliverables, lead beneficiaries and levels | GA deliverable descriptions l.4716–5480 | OK (see 7) |
| 37 | 723–766 | All 4.7 figures (revenue €3.2–3.6M / €12.1–12.6M; GM 14 % / 41–44 %; EBITDA €0.2M / €1.9–2.1M; scenario net results and lowest cash; +€0.7M / +€0.9M; 7 and 9 MWp; sensitivities −€3.6M, −€0.1M EBITDA, −€0.3M cash, +€0.5M; −€2.4M / €0.7M; €0.9M; €0.4M; −€5.6M / −€0.6M / €1.0M; wavebreakers −€0.1M cash / −€0.05M result; breakwater −€0.9M; 27 % support; outlook 18 and 25–45 MWp; kit margin 40–50 %) | fresh model run | OK |
| 38 | 737–739 | SuRE about €0.4M (€435k) in 2027; EIC €0.75M; EU upside €0.9M; minority share about €0.2M; €0.1–0.3M of round 2 | financial plan L31, L70, L169–170 | OK |
| 39 | 714 | €0.10/kWh at 1 MWp, half carried | model table (0.099) | OK |
| 40 | 416–437 | Classes 0.65/1.0/1.3 m, 1.6/3.8/6.4 km; 2.5×0.9, 3.0×1.2, 4.5×1.5; 30/73/123 t; periods; cost halves from 3.2 to 10 MWp (117→58 €/kWp); about 10× at 350 kWp (547/58) | breakwater_classes.py run | OK |
| 41 | 777–799 | Risk-map rules; four action risks 56/56/54/54; other grades | risk assessment L5, L12–38 | OK |
| 42 | A.4, A.5, A.23 | Partner counts (4/4/3/2/1 = 14); 15 presentations; Zenodo split 6/4/2/2/2/1/1 = 18 | Annex rows; KPI record | OK |

Findings: 0 major, 10 minor, 4 wording.
