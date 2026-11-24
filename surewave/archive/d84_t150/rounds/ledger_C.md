# Ledger C: D8.4 lines 395–617 (Sections 4.1–4.6.2)

Document: surewave/deliverables/2026-09-28_surewave_d8.4_exploitation_pathways_business_plan.md (paths below relative to C:\dev\src\sure-d61).
Script rerun: `PYTHONIOENCODING=utf-8 python scripts/breakwater_classes.py` (default) and `--site {50,300,1000,5000,30000} 45 light --host-share 0.5`. Plant-cost shares in 4.6.2 reproduced with the financial plan's kit-buyer capex €0.83/W held constant (financial plan §5.6).

## Claims ledger

| # | D8.4 line | Claim (short quote) | Source (file:line or URL) | Status | Fix |
|---|---|---|---|---|---|
| 1 | 399–405 | KER1 = internal array, external breakwater, transition element (PVC pipe, elasticated ropes), connections, mooring | docs/project_facts.md:89 (D3.4 §2.4); Clement report :244–257 | OK | – |
| 2 | 407 | Reference plant 10 MWp in ring, 346 m; 2 MWp 173 m | surewave/background/2025-02-03_surewave_clement_materials_and_resources.md:32–33 | CONFLICT | Owner decision is 10 MWp, but the coordinator's final technical report (surewave/background/2026-11-19_surewave_final_technical_report_working_copy.md:80) says "integrated 7.16 MW concept" and D8.3 (deliverables/2026-09-28_surewave_d8.3_technical_brochure.md:59) says 7 MWp on the same 346 m circle. Add one sentence: "D3.4 laid out 7 MWp on this circle; the materials report and D7.4 use 10 MWp", or align the final report and D8.3. |
| 3 | 407 | D7.4 assesses 2 MW, 5 × 2 MW, 10 MW | D7.4 :307 | OK | – |
| 4 | 409 | CONNECT: cast PU frame, flat bottom plate, one glass-glass panel, small fixed tilt just above water | docs/project_facts.md:31 | OK | – |
| 5 | 409 | Floats joined along full edge by flexible PU hinges | Sunlit Sea exploitation summary :39; D7.6 :689 (full width 1.88 m) | OK | – |
| 6 | 409 | Redesign "after SUREWAVE testing at SINTEF and MARIN" | D6.1 :75 (SINTEF lab tests of PU hinges); MARIN summary :25 (basin tests); webinar summary (SINTEF fatigue tests, MARIN 1:10 basin) | OK | – |
| 7 | 409 | "with fatigue and crack-propagation analysis by Ceit" | D5.5 :669–675 and D5.3 :1000 analyse breakwater rebar; D5.3 :1004 only announces hinge modelling "to be determined"; Ceit summary has no hinge work; D8.4's own KER6 row (line 362) says "crack-propagation and loading analysis of the breakwater" | UNSUPPORTED | Delete Ceit from the hinge sentence (and from Section 5, line 686), or cite the Ceit hinge analysis if it exists. |
| 8 | 409 | ULS break load 14 kN → 37 kN with third hinge generation (D7.6) | D7.6 :689, :761 | OK (incomplete) | Add D7.6's loads: 34 kN Baltic, 33 kN Mediterranean (below ULS), 40 kN North Sea (above ULS). See gap 1. |
| 9 | 409 | (implicit) the 37 kN figure describes the tested hinge | Final technical report :313: tested tensile capacity 3.69 → 8.36 kN (+127 %), compression 20.23 kN; D8.3 :169 calls 37 kN a result of "integrated finite-element analysis" | CONFLICT | State what each figure is: 37 kN = design ULS of hinge v3 (D7.6); 8.36 kN tensile / 20.23 kN compression = measured average capacities in SINTEF laboratory tests. Align D8.3. |
| 10 | 411, 433 | Site-planning tool built on SUREWAVE nearshore wave and wind models; estimates wave-induced energy loss | Sunlit Sea summary :3–29 | OK | – |
| 11 | 433 | "The tool computes the design waves for each direction from fetch and wind" | Sunlit Sea summary describes ERA5/GEBCO-based nearshore models along the perimeter; fetch-based sizing is in scripts/breakwater_classes.py and docs/project_facts.md:67 ("Eirik's SUREWAVE fetch-based wave estimate") | UNSUPPORTED (partly) | "The tool gives wave and wind conditions along the plant perimeter; from them, and from fetch-limited wave growth, the design waves per direction are set." |
| 12 | 417 | Platform: Prototype 4 in casting; TRL 4–5 | project_facts.md:33; Booster notes :54 | OK | – |
| 13 | 417 | First reference plants 2027–2028 | project_facts.md:45–46 (Skien mid-2027, Gunneklevfjorden 2028) | OK | – |
| 14 | 418 | Shielding tested in SUREWAVE basin campaigns | Final report :311 (breakwater reduced short-period wave energy and FPV motions by factors 2–3) | OK / UNDERSTATED | Give the factor 2–3. |
| 15 | 418 | Small wavebreakers at first reference plant, Norwegian port (2027) | project_facts.md:45 | OK | – |
| 16 | 418 | Field demonstrator of classes 2028–2030 | EIC proposal :294 (commissioned M22, TRL 6 at M36); project_facts.md:51 | OK | – |
| 17 | 419 | Full offshore plant: integrated concept TRL 5 (D7.6) | D7.6 :759; final report :331 | OK | But EIC proposal :40 says "laboratory-scale validation (TRL 4)"; see writing item 9. |
| 18 | 423 | SUREWAVE designed one breakwater, the heavy unit, full ring | D3.2; breakwater note §1 | OK | Minor: Clement report :120 has 19.4/20 m and 17 m units; "one cross-section" is exact. |
| 19 | 423 | Classes "scaled from the SUREWAVE design with its design and cost data (D3.2, D5.1, D7.4)" | breakwater note §4.1: adds fabrication (1.0 × material), couplings × 2.0, transport, supplier factor 1.25, mobilisation €40k, anchoring floor and open-arc factor, all "[to confirm]" | UNDERSTATED (method) | "... scaled from the SUREWAVE design and the D7.4 cost data, with Sunlit Sea's own estimates for fabrication, transport, fittings, supplier margin and mobilisation, which D7.4 does not contain." |
| 20 | 423 | Clement Germany owner of breakwater design (KER3) | D8.4 :362; Clement summary | OK | – |
| 21 | 427 | Light: up to 0.65 m; fetch up to about 2 km | note §2: 1.6 km | OK (rounded) | Write "about 1.6 km", and give fetch for medium (3.8 km) and rough (6.4 km) too. |
| 22 | 427 | Light cross-section 2.5 m wide, 1 m draft | note §3.2 | OK | – |
| 23 | 428 | Medium up to 1.0 m; 4 m wide, 1.5 m draft; CONNECT behind it | note §2, §3.2 (medium = sheltered-site platform) | OK | – |
| 24 | 429 | Heavy: 5 m wide, about 2 m draft, 20 m long | note §1 (2.03 m draft, 123 t) | OK | – |
| 25 | 429 | Heavy "Tested in CFD and wave basin in SUREWAVE" | D3.2 (CFD); final report :311; Gijón prototype final report :315 | OK / UNDERSTATED | Add "reduced-scale prototype exposed for about nine months at the Port of Gijón". |
| 26 | 431 | No breakwater if short waves (≤3 s) < 0.45 m and design Hs < 0.6 m | note §2, §3.1 (both "[to confirm]") | OK | – |
| 27 | 431 | At mild sites the short-wave limit governs | note §2 table (mild: short-wave 0.64 m of 0.65 m total) | OK | – |
| 28 | 431 | Above 1.3 m or with swell: open-sea design | note §2 | OK | – |
| 29 | 433 | Exposure sector 20°–180°; arc or straight line; end extensions | note §5.1 | OK | – |
| 30 | 437 | Cost per kWp halves 3 → 10 MWp, rises steeply below 1 MWp | script: 117 → 58 €/kWp (3.2 → 10 MWp); 547 at 350 kWp | OK | Write 3.2 MWp (the run's basis). |
| 31 | 438 | Dual use: berths, bathing/sauna platforms, boathouses, café; fits leisure lakes, marinas, harbours | note §5.1; Clement summary :13, :23 | OK | – |
| 32 | 439 | Natural roll/heave periods near design wave periods | script: 2.7/2.5, 3.4/3.2, 3.8/3.6 s vs Tp 2.3, 3.1, 3.7 s | OK | – |
| 33 | 443 | Founded 2019, Oslo | project_facts.md:10, :17 | OK | – |
| 34 | 443 | Gen 1 in Germany since 2023; Norway PPA 2024–2026 | project_facts.md:35–37 | OK | – |
| 35 | 443 | Subcontracted production from 2024 | project_facts.md:34 (Askim wound down autumn 2024) | OK | – |
| 36 | 443 | Partners for simulation (IFE), PV integration, sales in Germany, construction/permitting | project_facts.md:102–106, :109 | OK | – |
| 37 | 447 | 2027–2028 objectives (design freeze, TRL 6, DNV, series prep) | HRB business plan :28, :119–122 | OK | – |
| 38 | 448 | 2029–2032 kit sales Nordics, DE, Baltic, later Med; 10 MW-class contract by 2030 | HRB business plan :33–34 | OK | – |
| 39 | 452 | 8.7 GW end 2024 (IEA PVPS) | https://iea-pvps.org/wp-content/uploads/2025/12/Trends-2025-FS.pdf ("at least 8.7 GW") | OK | – |
| 40 | 452 | "almost 90 % of it in Asia" | IEA PVPS T13-31:2025 (https://iea-pvps.org/key-topics/t13-floating-pv-plants-review-2025/): almost 90 % of 7.7 GW at end 2023 | CONFLICT (date) | "almost 90 % of it in Asia at the end of 2023". |
| 41 | 452 | "nearly all of it on calm inland water" | HRB business plan :130 (no external source named) | UNSUPPORTED | Cite IEA PVPS T13-31:2025, which treats inland and nearshore FPV, or drop "nearly all". |
| 42 | 452 | Largest European marine units 0.5–1 MW | HRB business plan :145 (no source); BlueNewables 2 × 500 kW (business plan :207) | UNSUPPORTED | Name the units and sources, or write "the European marine pilots are below about 1 MW". |
| 43 | 452 | No supplier has a commercial multi-MW reference on European coastal water (2026) | HRB business plan :130 | UNSUPPORTED (negative claim) | "We found no ... in public sources (company announcements, trade press, 2024–2026)." |
| 44 | 452, 563 | "National studies indicate 4.5–6.5 GW ... Spain" | University of A Coruña, Journal of Cleaner Production 2026: 4.45–6.48 GW (https://www.pv-magazine.com/2026/06/15/spains-offshore-pv-potential-estimated-at-6-48-gw/) | OVERSTATED | One academic study, not "national studies": "a 2026 University of A Coruña study estimates 4.45–6.48 GW within Spain's maritime spatial plans". |
| 45 | 452 | Dutch scenarios 45 GWp solar at sea by 2050 | TNO (https://www.tno.nl/en/sustainable/energy-supply/solar-applications/floating-solar-panels/) | OK | Name TNO. |
| 46 | 454 | Niche 0.3–10 MWp at industry and ports | HRB business plan :130 | OK | – |
| 47 | 454 | NVE expects ground-mounted solar held back by grid scarcity and land use | HRB business plan :147 (NVE note Feb 2024) | OK / UNDERSTATED | Add: 1.4 GW applied, 14 MW licensed by early 2024, against about 10 GW needed for 2030 (NVE). |
| 48 | 458–461 | Segments and adjacent segment | HRB business plan :186–190 | OK | – |
| 49 | 463 | "Competitors are few and at pilot stage" | HRB business plan :203–210: Ocean Sun has plants in Asia, Maldives, Brazil and a BV type certificate; Swimsol >50 resort islands; Ciel & Terre large installed base | CONFLICT | "Competitors at sea are few and at pilot stage; inland and lagoon suppliers have installed bases but not for sea waves." |
| 50 | 465–468 | Competitor list | HRB business plan :201–210; project_facts.md:111 | OK | Oceans of Energy: business plan says North Sea pilot withdrawn 2026, no current project; BlueNewables units are at the Port of Valencia, not offshore. Saipem/Moss Maritime (project_facts) not listed. |
| 51 | 470 | Competition decided on references, independent review, price | HRB business plan :212 | OK | – |
| 52 | 480 | Hosts committed time; two Gen 1 plants from 2023 and 2024 | HRB business plan :196; project_facts | OK | – |
| 53 | 480 | First market southern Norway "where power prices are highest" | Statistics Norway prices 2025 (business plan :331), not checked | UNSUPPORTED in text | Name the source (SSB, price areas NO1, NO2, NO5). |
| 54 | 481 | Evidence: "Horizon Results Booster mentor review" shows references and independent review are required | Booster notes 2026-11-13: the expert rated the files and asked questions; the certification point came from Eirik (:50) | UNSUPPORTED | Evidence is the competitor benchmark and bankability literature (business plan :151); drop the mentor attribution. |
| 55 | 482 | Webinar 19 Nov 2024 with SAB; questions on cost, mismatch losses, monitoring, LCOE target | 2024-11-19 webinar summary Q&A | OK / UNDERSTATED | Add the figures given there: mismatch loss 0 to 12–13 % in the panels' range; estimate about 10 % unprotected, 2–3 % behind the breakwater; two attendees asked. |
| 56 | 482 | Wave-loss module as a consequence of the test | Sunlit Sea summary :25 (module in place by Sep 2026) | OK (sequence unclear) | "Wave-loss module, in the planning tool since 2026". |
| 57 | 483 | Developers and kits: "Not yet: one lead with confirmed interest" | project_facts.md:107 (Magdeburg, confirmed interest); Booster notes :49–50: kits of 4–6 panels sold; customers want Gen 2 in UK, Chile, Germany; Danish lead | UNDERSTATED | "Small kits of 4–6 panels sold; enquiries from the UK, Chile and Germany and a Danish lead; one lead in Germany with confirmed interest." |
| 58 | 484 | Support of about a quarter needed | financial plan :262–266 (27 %) | OK | – |
| 59 | 485 | D7.4: viable Med, break-even Baltic, not viable North Sea | D7.4 :334–349 | OK | – |
| 60 | 485 | Cross-reference "(Section 4.10)" | 4.10 is "Changes from the proposal" | WRONG (ref) | Point to Section 4.6.1. |
| 61 | 487 | Customer interviews early 2027 | HRB business plan :196 | OK | – |
| 62 | 495–500 | Value-innovation grid entries | HRB business plan :201–210; value chain :22 (assembly at local quay) | OK (method unstated) | See gap 8. "Generic per platform" for open-sea platforms has no source. |
| 63 | 504 | D7.6: lower GHG than coal reference, low land use, acceptable outcome per indicator in at least one scenario | D7.6 :1083–1101 | OK / UNDERSTATED | See gap 4 (omits higher impacts than land PV and wind, conditions). |
| 64 | 512 | Phase 1 2027–2029; owns one small reference plant; no contractor can build CONNECT | HRB business plan :251 | OK | Business plan also has a minority share of about €0.2M in a plant company; omitted (acceptable under the owner decision). |
| 65 | 513–514 | Phase 2 mainly 2030, first kits 2028; later stages after 2031 | HRB business plan :252–253 | OK | – |
| 66 | 518–522 | Revenue streams | financial plan :65 | OK | Development and engineering fees in phase 1 (financial plan :65) are missing; add. |
| 67 | 524 | Production subcontracted; designs parts, owns moulds, controls quality | HRB business plan :270 | OK | – |
| 68 | 524 | "Sunlit Sea seeks to buy the breakwater from Clement Germany" | Section 5 (line 694): three routes; Section 4.7 (line 633): bought by the plant owner, or by Sunlit Sea at cost; financial plan :124: "the plant owner buys it from Clement"; Booster notes :47 | CONFLICT | "For sites that need one, the breakwater is supplied by Clement Germany per project, bought by the plant owner or by Sunlit Sea at cost (Section 5)." |
| 69 | 528–532 | Channels and market order | HRB business plan :288–306 | OK | – |
| 70 | 536 | DNV-ST-C108, DNV-ST-E309 (2026), DNV-RP-0584 | https://www.dnv.com/news/2026/dnv-launches-coordinated-standards-to-improve-safety-and-reliability-of-floating-solar/ (editions 2026-04) | OK | Official title of C108: "Structural design of floats for floating photovoltaic systems". |
| 71 | 537–542 | Qualification programme incl. IEC TS 62788-7-2 | HRB business plan :115; project_facts.md:124 | OK | – |
| 72 | 546 | Design freeze with prototype 4 (Q2 2027) | business plan :119 (Q1–Q2 2027) | OK | – |
| 73 | 547–548 | First plant 2027; TRL 6 after first winter Q2 2028 | business plan :120 | OK | – |
| 74 | 549 | DNV design-basis assessment from Q4 2027 | roadmap :24, :72; business plan :121 says Q2 2027 – 2028 | OK (minor conflict) | Keep Q4 2027 (roadmap milestone M5); align business plan. |
| 75 | 550 | FTO review and design-registration decision Q3 2027 | roadmap :30, :71 | OK | – |
| 76 | 551 | Industrial moulds, kit packing 2027–2028 | business plan :122 | OK | – |
| 77 | 559 | Norway: <10 MW no national licence since July 2025, municipal approval | https://regjeringen.no/no/aktuelt/endringar-i-lover-og-forskrifter-fra-1.-juli-2025-fra-energidepartementet/id3111203 | OK | – |
| 78 | 559 | Harbour permit for plants at sea | business plan :154 | OK | Name the act (havne- og farvannsloven) without a paragraph unless verified. |
| 79 | 560 | Sweden: water operations under Environmental Code | project_facts.md:116 (Miljöbalken 11 kap.) | OK | – |
| 80 | 561 | Germany: federal rules on coverage and distance limit inland FPV | Wasserhaushaltsgesetz § 36 (public; not downloaded) | OK / UNDERSTATED | Give the rule: artificial and heavily modified waters only, at most 15 % coverage, at least 40 m from shore (verify text before citing). |
| 81 | 562 | Baltic states: "New permitting regimes for marine installations" | business plan :296 (no source) | UNSUPPORTED | Name the regime per country or generalise. |
| 82 | 563 | Spain, Italy: maritime concessions and EIA | none in repo | UNSUPPORTED | Cite Ley de Costas / Italian demanio marittimo concessions, or generalise. |
| 83 | 565 | DNV standards "give a clear path to a bankable design" | – | OVERSTATED | "give the basis for an independently reviewed design" (business plan :153). |
| 84 | 572 | Step to exposed sites "multiplies the number of usable sites" | – | UNSUPPORTED | Drop "multiplies" or quantify. |
| 85 | 576 | D7.4 v2.0: full life cycle, 50 years, PV replaced at 25, decommissioning; €0.12/kWh | D7.4 :91, :343 | OK | Add that €0.12/kWh is the target price from the application (D7.4 :343) and the 8.5 % base discount rate (D7.4 :795). |
| 86 | 580–582 | Med €7.3M / 15.6 % / €0.076 / 10 y; Baltic ≈€0 / 8.5 % / €0.120; North Sea −€5.8M / 3.4 % / €0.173 | D7.4 :334–340 | OK | – |
| 87 | 584 | Replace v1.0 values €0.062, 10.7 % quoted in D8.3 | D7.4 :496; D8.3 :32, :253, :315 | OK | D8.3 also states 7 MWp and TRL 4–5; see #2, writing item 9. |
| 88 | 584 | Baltic viable at lower cost of capital; North Sea needs lower cost, shared infrastructure or support | D7.4 :1126–1128, :1004 | OK | Give the thresholds: Baltic viable up to 8 %, North Sea only at 3 % or lower. |
| 89 | 584 | Non-panel costs at sea close to onshore PV | D7.4 :351 ("cable-exclusive non-panel costs") | OK (qualifier dropped) | "Excluding cables, ...". |
| 90 | 584 | Pontoons and breakwater €212/kWp, under a quarter of investment | D7.4 :817, :825 (212.16 of 940.07 = 22.6 %) | OK | D7.4 figure includes bridge pontoons, PVC pipes and ropes (D7.4 :828); say so. See gap 6 on known limits. |
| 91 | 588 | Mediterranean "whose sea states are milder than those of the North Sea and the Baltic Sea" | D5.1 :1011–1060: 50-year Hs up to 4.0 m Baltic, 6.5 m Mediterranean, 11 m North Sea; D7.4 :607 "Baltic and Mediterranean show similar wave occurrence profiles"; webinar: Baltic mild | WRONG | "in the Mediterranean, which has the highest solar yield and lower maintenance cost than the Baltic and North Sea; its sea states are milder than the North Sea's" (D7.4 :345, D7.6 :147). |
| 92 | 592 | First buyers coastal and island grids with dear supply and scarce land | D7.6 summary ("initial highly profitable niche applications at existing offshore installations"); D7.4 :349 (diesel, hybrid platforms) | UNSUPPORTED (partly) | Use D7.6's own wording: existing offshore installations and island grids. |
| 93 | 593 | €9.8M, €940/kWp, 300 m floating cable, no export cable | D7.4 :825, :480, :589 | OK | Add what is outside: substation, grid fees, development, permits, seabed lease (D7.4 :473). |
| 94 | 594 | €0.12/kWh, 8.5 %, NPV €7.3M, IRR 15.6 %, payback ten years | D7.4 :95–101 | OK | – |
| 95 | 595 | "Clement Germany engineers and supplies the breakwater, with ACCIONA's mixes (KER3, KER2)" | D7.4 :1146: the costed base case is the conventional breakwater; HPC raises LCOE €0.076 → €0.085/kWh | CONFLICT | "... with conventional concrete as costed in D7.4; ACCIONA's circular mixes (KER2) where the buyer values their lower footprint, at a higher cost (D7.4 Section 7.5.2)." |
| 96 | 595 | "MARIN and SINTEF provide mooring design and basin tests (KER5, KER4)" | D8.4 KER3 row (line 362): Clement holds "design methods for mooring and anchoring"; D3.2 mooring layout by Clement; KER5 = MARIN mooring optimisation | CONFLICT (role) | "Clement Germany designs mooring and anchoring with the breakwater; MARIN optimises the mooring and, with SINTEF, provides basin tests (KER3, KER5, KER4)". |
| 97 | 596 | First-of-a-kind sea plant cannot raise project debt without field record | HRB business plan :151 | OK | – |
| 98 | 597 | Open-sea pilot proposal about 2031; pilot after about 2033; commercial from about 2035 | No source in repo (roadmap, business plan, financial plan, value chain checked) | UNSUPPORTED | Owner's plan; acceptable as stated plan, but state it as Sunlit Sea's planning assumption. |
| 99 | 597 | Plant cost re-established incl. mooring, anchoring, fabrication labour | project_facts.md:90 (D7.4 known limits) | OK (reason not given) | See gap 6. |
| 100 | 600 | Section 4.7 figures end in 2031 | D8.4 :620 | OK | – |
| 101 | 604 | First breakwater at Norwegian port 2027, small wavebreakers | project_facts.md:45 | OK | – |
| 102 | 604 | "against local wind waves and vessel wakes" | No source mentions vessel wakes | UNSUPPORTED | Drop "and vessel wakes" or source it from the Skien havn site study. |
| 103 | 604 | Baseline EIC site is a lake; light breakwater over about 45°; dual use | EIC proposal :252, :300; project_facts.md:67; financial plan :314 | OK | – |
| 104 | 604 | EIC targets 1–5 MWp immediately after the project, about 2030 | EIC proposal :68, :198 | OK | Section 4.7 (line 637) models it in 2031; align the year (writing item 7). |
| 105 | 606 | Basis: light, 45°, arc at fixed distance, D7.4 v2.0 breakwater and anchoring costs | script: 30 MWp case picks the straight layout; costs include Sunlit Sea's added items (#19); PV plant cost €0.83/W not stated | UNDERSTATED (method) | See gap 7. |
| 106 | 610 | 50 kWp: about two thirds / about 80 % | script + €0.83/W: 64 % / 78 % | OK | – |
| 107 | 611 | 300 kWp: about 30 % / about 46 % | 30 % / 46 % | OK | Say 50–300 kWp is the demonstrator range in the EIC proposal (:369). |
| 108 | 612 | 1 MWp: about 15 % / 25 % | financial plan :320–322: 0.14/0.97 = 14 %, 0.28/1.11 = 25 % | OK | – |
| 109 | 613 | 5 MWp: about 6 % / 11 % | 0.05/0.88 = 6 %, 0.11/0.94 = 11 % | OK | – |
| 110 | 614 | 30 MWp: about 2 % / 4 % | script 19/38 €/kWp → 2.2 % / 4.4 % | OK | – |
| 111 | 616 | From 5 MWp breakwater about a tenth or less | #109 | OK | – |
| 112 | 616 | 1 MWp needs buyer behind the meter or support; grid sales do not cover cost | financial plan :321 (LCOE €0.099/kWh with breakwater) and :331 (German tender 4.84 ct/kWh, Bundesnetzagentur, July 2025) | OK / UNDERSTATED | Give the two figures. |

## Content gaps (requirements 4 and 5)

1. Hinge evidence is compressed to one figure (line 409). Sources: D7.6 :689, :719–721, :761; final technical report :119, :311–313; D6.1. Write: "SINTEF's laboratory tests and MARIN's first 1:10 basin campaign found compression buckling and snap loading in the second-generation hinge. The third generation spans the full float edge (1.88 m). In SINTEF's tests its average tensile capacity rose from 3.69 kN to 8.36 kN, with 20.23 kN in compression; the second basin campaign showed no buckling or snap loading. D7.6 gives the design ULS as 37 kN, against 14 kN before, with 50-year design loads of 34 kN (Baltic) and 33 kN (Mediterranean); in the North Sea the load is 40 kN, still above the ULS." This also explains why the exposed-site and North Sea steps need a further hinge generation (risk table line 646).

2. Breakwater test evidence not shown (lines 418, 429). Final report :311, :315: breakwater reduced short-period wave energy and array motions by factors of about 2–3 in the basin; reduced-scale prototype at the Port of Gijón for about nine months without significant deterioration. Add to the heavy-class status cell and the directional-breakwater row.

3. Why Clement's classes rest on Sunlit Sea's assumptions is not visible (lines 423, 431). The note's assumptions "[to confirm]" (allowable heights 0.45/0.6/0.8 m, design wind 22 m/s, SPM 1984 fetch-limited JONSWAP, Macagno transmission, width-to-draft 2–3, minimum width 2.5 m) should be named in one sentence: "Sizing method: fetch-limited JONSWAP spectra (SPM 1984) for a 22 m/s design wind, wave transmission by the Macagno formula used in D3.2 and D5.1, and cross-sections kept at a width-to-draft ratio of 2–3 as for the SUREWAVE unit." Add the main uncertainty in the same place: Macagno treats the breakwater as rigid, so transmission near resonance is probably higher (note §7).

4. Sustainability evidence (4.3.3) is compressed and one-sided. D7.6 :147, :151–155, :1083–1101. Add: substantially lower GHG and fossil-resource use than coal; lower social supply-chain risk; impacts higher than land-based PV or wind; local environmental impacts to be managed; conditions: target markets where FPV displaces fossil power, avoid sensitive shallow ecotopes and marine-mammal routes, socially beneficial procurement; Mediterranean most advantageous. Also say D7.6 assessed the open-sea 10 MW plant, so for sheltered sites the evidence is indicative.

5. Value-proposition testing (4.3.1) does not say how many interviews, stakeholders or hosts were involved, or when. Sources: webinar (about 23 participants, two attendees asked about mismatch losses, 31 sign-ups); Booster session 13 Nov 2026 (expert: Raluca Cibu-Buzac, META Group); Booster notes :49–50 for kit demand. Give counts and dates per row ("what, when, who, evidence").

6. D7.4's known limits are not stated (lines 584, 593, 597). project_facts.md:90 and breakwater note §4.2–4.3: anchoring counted per ring rather than per pile and chain (Clement report Tables 9, 11–13 give per-piece weights), pontoon maintenance once a year, no fabrication labour; built up with fabrication the ring costs about €443/kWp against D7.4's €201/kWp. Owner decision keeps D7.4 v2.0 figures, but line 597 asks the reader to accept that the cost is "re-established" without saying why. Write one sentence: "D7.4 prices the pontoons and anchoring from material quantities; fabrication labour and per-anchor weights are not costed, so the plant cost is to be re-established from engineering quotes before a pilot decision." (Error inside the accepted decision: the Clement report shows the per-anchor reading is correct, so the €212/kWp and the 4.6.2 shares are known to be low.)

7. Basis of the 4.6.2 table cannot be reconstructed. Missing: PV plant cost held at €0.83/W at every size (financial plan §5.6); a 50–300 kWp demonstrator costs much more per watt, so the breakwater shares in the demonstrator rows are overstated and should be marked as computed at commercial plant cost; stand-off 15 m; 10° directional spreading each side; 150 W/m² power density; €40,000 mobilisation; supplier factor 1.25; anchoring as modelled in D7.4. Also the 30 MWp case uses a straight layout, not an arc. Write the basis as: "PV plant at €0.83 per watt at every size, the cost of a plant built from the kit (Section 4.7); breakwater installed cost about €1,150 per metre for the light class, including Sunlit Sea's estimates for fabrication, transport, fittings and supplier margin, plus €40,000 mobilisation per site; arc or straight layout, whichever is shorter."

8. Value innovation (4.3.2) method not named. Name it: the eliminate–reduce–raise–create grid (Blue Ocean four actions) and say the competitor columns are from the competitor benchmark (company announcements and trade press 2024–2026).

9. Competitor evidence not shown item by item (line 463–468). The business plan table :201–210 holds status per competitor (Fred. Olsen DNV review to Hs 3.5 m; Ocean Sun BV type certificate 2025; Oceans of Energy pilot withdrawn 2026; BlueNewables 2 × 500 kW at Valencia). Add a short status per competitor.

10. Market sources not named (lines 452–454). Add source names inline: IEA PVPS Trends 2025 fact sheet; IEA PVPS T13-31:2025; University of A Coruña (J. Cleaner Production 2026); TNO; NVE note February 2024; Statnett half-year report 2026 (about 3,500 MW mature grid applications).

11. Regulatory table (4.5.1) is thin for Germany, Baltic, Spain/Italy. Germany: WHG § 36 limits (15 % coverage, 40 m from shore, artificial and heavily modified waters) after verifying the text; Baltic and Mediterranean: name the permitting route per country or reduce to "to be mapped per site".

12. Line 597 timeline (pilot proposal 2031, operation 2033, commercial 2035) has no derivation. State the basis: exposed-site record 2028–2030, two to three years for a pilot proposal, permits and build.

## Writing and consistency (requirements 6 and 7)

1. Line 588: "whose sea states are milder than those of the North Sea and the Baltic Sea" is wrong (see #91). Fix as in the ledger.
2. Line 485: "(Section 4.10)" points to the wrong section. Use "Section 4.6.1".
3. Lines 409 and 686 (Section 5): Ceit's role in the hinge redesign contradicts the KER6 row (line 362, breakwater analysis). Remove or source.
4. Line 524 vs lines 633, 694: three different statements of who buys the breakwater. Use the Section 5 wording everywhere.
5. Line 595: "ACCIONA's mixes" in a business case priced with the conventional breakwater. Fix as #95.
6. Line 595 vs line 362: mooring design attributed to MARIN and SINTEF, while KER3 holds Clement's mooring and anchoring design methods.
7. Line 604 "about 2030" vs line 637 "modelled in 2031": state both ("targeted about 2030; modelled in 2031, the first full year after the project").
8. Lines 452 and 563: "National studies indicate" repeated, and overstated (one study). Say it once, in 4.3, with the source; in the table write "about 4.5–6.5 GW potential (Section 4.3)".
9. TRL statements: line 419 and the KER table give the integrated concept TRL 5 (D7.6); Section 10 and the EIC proposal :40 say the exposed-site step starts at TRL 4; D8.3 :32 says TRL 4–5. Add one clause in 4.5 or Section 10: "TRL 5 for the integrated open-sea concept (D7.6); the exposed-site product with directional breakwater starts at TRL 4, since that configuration has been validated in the laboratory only."
10. Units: "10 MW plant" (lines 407, 578, 588) beside "10 MWp array" (407) and "2 MWp version". Use MWp for installed capacity throughout, or say once that D7.4's "MW" is peak capacity.
11. Line 580 "10 years" vs line 594 "ten years": pick one.
12. Line 437 "3 MWp" vs the note's 3.2 MWp basis: write 3.2 MWp.
13. Line 409: "ultimate limit state break load" is jargon for a non-specialist reader; write "design break load (ultimate limit state)".
14. Lines 411 and 433 describe the site-planning tool twice in near-identical words. Keep the description in 4.1.1 and shorten line 411 to a cross-reference.
15. Line 496: "None, so unusable at sea" is a non-sequitur in a "needed against waves" row. Write "None; not designed for sea waves".
16. Line 565: "give a clear path to a bankable design" claims more than a standard gives; use "give the basis for an independently reviewed design".
17. Line 572: "multiplies the number of usable sites" is an unquantified selling phrase; drop or quantify.
18. Line 463: "Competitors are few and at pilot stage" contradicts the listed Swimsol and Ciel & Terre; restrict to "at sea".
19. Line 423: "Most sites in Sunlit Sea's markets are nearshore or inland" and line 461 "An adjacent segment is large lakes" vs line 604 "they come first for the classes": the explanation at 604 is good; add a forward reference at 461 ("first for the breakwater classes, Section 4.6.2").
20. Line 418 table cell is a long run-on (three status items, four entry items in one cell). Split into separate rows or shorten: "Classes sized; directional layout to be demonstrated" / "Port wavebreakers 2027; demonstrator 2028–2030; commercial sites from about 2030".
21. No bold, no file paths, no task numbers found in lines 395–617. Tables: column counts consistent in all nine tables; no blank line after separator rows.
22. D8.3 companion consistency: D8.3 still states 7 MWp, LCOE €0.062/kWh, IRR 10.7 %, TRL 4–5 and "37 kN from integrated finite-element analysis". D8.4 line 584 names only the LCOE/IRR change. Either correct D8.3 or list all differences in one sentence.
