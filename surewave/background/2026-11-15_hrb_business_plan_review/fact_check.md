# Fact check — KER1 business plan draft (2026-11-14)

Reviewed file: `surewave/deliverables/2026-11-14_surewave_hrb_business_plan_ker1.md` (354 lines). Review date 15 November 2026.

Sources checked: `docs/project_facts.md` (canonical), `docs/surewave_configurations.md`, the five companion KER1 files (characterisation table, exploitation roadmap, risk assessment, BOSAT, lean canvas), SUREWAVE D7.4 economic assessment, D7.6 sustainability report (for the hinge figures), the EIC Transition proposal and BE2 budget, the five research notes in `surewave/background/2026-11-14_hrb_business_plan_research/`, the 2025-11-17 and 2026-07-16 løypemeldinger, and the 13 November meeting summary. Two web checks were made for claims the research notes did not cover (SolarPower Europe 2025 global figure; NZIA start date).

Status key: consistent / inconsistent / unsupported (no source in repo) / outdated. "Facts file" means `docs/project_facts.md`.

## 1. Summary

About 95 discrete claims checked. Roughly 70 consistent, 12 inconsistent, 8 unsupported, 5 outdated.

Most serious issues, in priority order:

1. D7.4 economics carried over to Sunlit Sea CONNECT (lines 167, 285). The SUREWAVE D7.4 10 MW reference plant uses prefabricated concrete pontoons with a perimeter breakwater (D7.4 lines 565–575; `docs/surewave_configurations.md`: full ring is the open-sea reference). The plan calls the €209/kWp line "floats and breakwater" and then uses it (as €0.21/W "at series production") to argue that CONNECT's €0.30–0.40/W kit price will fall with volume. D7.4 does not mention series production, and its "Pontoon + Breakwater" line covers a different architecture. The comparison is not like-for-like and a reviewer who knows D7.4 will spot it. The same issue appears in the characterisation table ("Proven economics", line 39).
2. Install dates conflict with the facts file. The plan (and roadmap) put Gunneklevfjorden in operation in 2028 and Storavatnet first supply in 2029, against facts-file targets of Q2–Q3 2027 and ~2028. Skien havn is "Q2 2027 – Q2 2028" (reference phase) and Q2–Q3 2027 in the roadmap, against Q1 2027 in the facts file and the 2026-07-16 løypemelding. Either the facts file is out of date (likely, given the 13 November discussions) or the plan is. The facts file wins until it is corrected, so the facts file needs a line update or the plan needs to revert.
3. Registered design presented as existing protection (lines 86, 127, 227). Companions say the design-registration decision is still to be made, for the hinge, by Q3 2027 (characterisation line 100, roadmap line 30, BOSAT IP5). The plan changes the object to the float and lists it among protections that "consist of". Research note `technology_standards_ip.md` line 21 adds that an EU design does not cover Norway and that function-dictated features are excluded (DOCERAM).
4. Bottom-plate material committed in external copy (lines 69, 76, 98, 113). Facts file line 35: do not commit externally to the bottom-plate material; state it as indicative. "Flat aluminium bottom plate" is stated as fact four times.
5. Skiftestjørna PPA (line 17) is outdated: the EV PowerCharge PPA ran to end October 2026 (facts file line 33 and line 74; løypemelding 2026-07-16 section 3).
6. "Concept validated in SUREWAVE wave-basin tests" for the directional-breakwater version (line 64) is not supported. SUREWAVE validated the protected concept at TRL 4 in lab and basin with the perimeter configuration (EIC proposal line 36); the directional strategy is a planning-tool rule, not a basin-tested configuration.
7. Facts file line 40 still says EIC Transition lifts CONNECT to TRL 6 "by end 2027". The submitted proposal is 36 months with TRL 6 at M36 (2030 if started 2027). The plan follows the proposal correctly; the facts file needs correcting.

## 2. Claim table

| Line | Claim (quoted) | Status | Source / conflict | Suggested correction |
|---|---|---|---|---|
| 13 | "founded in 2019 and based in Oslo" | consistent | Facts file lines 11, 19 | — |
| 13 | "in Norway it also develops, operates and sells its own floating solar plants" | consistent | Facts file lines 33, 41 | — |
| 17 | Gen 1 "produced in Sunlit Sea's own factory in Askim, Norway, until autumn 2024" | consistent | Facts file lines 12, 30 | — |
| 17 | "Mannheim Cablepark in Germany (60 kWp, since 2023, customer Rixen Cableway)" | consistent | Facts file line 32 | — |
| 17 | "Skiftestjørna ... (105 kWp, since autumn 2024, operated by Sunlit Sea with a power purchase agreement)" | outdated | PPA to EV PowerCharge ran to end October 2026 (facts file lines 33, 74; løypemelding 2026-07-16 §3: plant sells at normal price after expiry) | "operated by Sunlit Sea, which sold its power under a power purchase agreement until October 2026" or name current arrangement |
| 17 | "factory was wound down because it cost more to run than the volumes of the time could carry" | consistent | Meeting summary line 45 ("too costly to run") | — |
| 18 | "SUREWAVE (Grant Agreement 101083342, 2022–2026) and SuRE (Grant Agreement 101135567, 2024–2027), with testing at SINTEF and MARIN" | consistent | Facts file lines 48–49 (SUREWAVE extended to 2026-12-31) | — |
| 20 | "The company is led by its founders" / line 41 "much depends on the two founders" | unsupported | Facts file line 19 names Per Lindberg as co-founder; no repo source records Eirik Larsen as founder (he appears in 2020 investor updates as part-time team member via KodeWorks) | Verify with user; otherwise "led by its co-founder and CEO Per Lindberg and technical lead Eirik Larsen" and "the two key people" |
| 20 | "CEO and board chair Per Lindberg invented the Generation 1 system and leads research and development on Generation 2" | consistent | Facts file line 19 (corrected 2026-11-15) | Consider disclosing that the CEO is part-time (employed by Akershus Energi since 2026-01-01); an evaluator will ask about team capacity |
| 20 | "Eirik Larsen, technical lead, is responsible for product development, sales and administration" | consistent | Facts file line 18 | — |
| 20 | partners "IFE (structural simulation), Metsolar in Lithuania (photovoltaic module integration) and Rixen Cableway (sales in Germany)" | consistent | Facts file lines 84–86 | — |
| 20 | "financed by EU and Norwegian public funding and by private equity from Norwegian investors" | consistent | BOSAT F2, Tm10 | — |
| 26 | "reach ... TRL 6 for sheltered sites through the first reference plant" (2027–2028) | consistent | Roadmap M7 (Q2 2028) | — |
| 27 | "Skien havn (350 kWp, 2027) and Gunneklevfjorden ... (3.2 MWp, 2028)" | inconsistent | Facts file line 43: Gunneklevfjorden target install Q2–Q3 2027; løypemelding 2026-07-16 same. Plan matches roadmap M8 (Q3 2028) | Update facts file if 2028 is the new target, or revert plan to 2027 |
| 28 | "Start a DNV design-basis assessment and set up European series production" | consistent | Roadmap lines 24, 39 | — |
| 34 | "first 10 MW-class supply contract by 2030" | consistent | Roadmap M10 | — |
| 35 | "Extend the product to exposed sites ... building on the EIC Transition demonstrator if it is funded" | consistent | EIC proposal lines 72, 93 | — |
| 41 | "hinge and float tested at SINTEF and MARIN over four years of EU projects" | consistent | SUREWAVE Oct 2022 – Dec 2026 | — |
| 42 | "Generation 1 plants in commercial operation since 2023" | consistent | Facts file line 32 | — |
| 43 | "Own Norwegian pipeline of 6.75 MWp at named industrial and harbour sites" | consistent | 0.35 + 3.2 + 3.2 = 6.75 (facts file lines 42–44) | — |
| 43 | "No series production yet; prototypes still in casting" | consistent | Facts file line 34 | — |
| 60 | Gen 1 "Marketed 2022–2024" | unsupported | First commercial plant 2023; no repo source for 2022 market start | Use "2023–2024" or "until 2024" |
| 60 | "On the market; no longer produced" | inconsistent (internal) | Same row says "line discontinued"; facts file line 30 | "Discontinued; existing plants in operation" |
| 61 | "Prototype 4 in casting; TRL 4–5" | consistent | Facts file line 34; meeting summary line 53 | — |
| 61 | "kit sales from 2028" | unsupported | Characterisation and roadmap give no kit-sales start date; no Gen 2 kit order in pipeline | Keep as target, mark "planned" |
| 63 | "Skien havn and Gunneklevfjorden in development" listed under own plants | inconsistent (internal) | Løypemelding 2026-07-16 table lists Skien havn as "Direct sales / PPA"; sales forecast line 326 books Skien as supply-plus-engineering revenue | Decide whether Skien is own plant or third-party sale; revenue from an own plant is not supply revenue |
| 64 | Directional breakwater "Concept validated in SUREWAVE wave-basin tests" | unsupported | EIC proposal line 36: SUREWAVE validated protected concept at TRL 4; basin tests used the perimeter configuration (`docs/surewave_configurations.md`). Directional placement is a planning-tool rule | "Protection concept validated in SUREWAVE laboratory and basin tests; directional placement set by the planning tool" |
| 64 | "TRL 6 at the end of the EIC Transition project, if funded" | consistent | EIC proposal O7, M36. Facts file line 40 ("TRL 6 by end 2027") is outdated | Correct facts file line 40 |
| 65 | Reinforced edge system, "can also serve rivers" | consistent | Meeting summary line 22 | — |
| 69 | "flat aluminium bottom plate" | inconsistent with facts-file rule | Facts file line 35: do not commit externally to bottom-plate material; aluminium 5083 flat is internal base case | "a flat metal bottom plate (aluminium in the current design, to be confirmed at design freeze)" or "bottom plate" |
| 69 | "standard 710–740 Wp glass-glass solar panel at a small, fixed tilt just above the water" | consistent | Facts file line 35 (no values committed) | — |
| 69 | "fitted at deployment" | consistent | Characterisation line 11 | — |
| 75 | "raised the ultimate load capacity of the critical connection from 14 kN to 37 kN with the third-generation hinge" | consistent | D7.6 lines 689, 761; status 2026-09-28 line 79 | Optional: add that 37 kN covers Baltic and Mediterranean loads (34/33 kN) but not North Sea extremes (40 kN), which supports the nearshore focus |
| 76 | "flat aluminium plate. No custom panels or specialist steelwork" | inconsistent with facts-file rule | As line 69 | As line 69 |
| 77 | "Installation from ordinary quays ... A damaged hinge can be replaced without recovering the array" | consistent | Characterisation line 38 | — |
| 82 | "Patenting was assessed with a patent attorney and not pursued, because the field ... is crowded with prior art" | consistent | Meeting summary line 24; research `technology_standards_ip.md` line 20 | — |
| 84 | Trade secrets in casting recipes and planning-tool rules | consistent | Characterisation line 100; research IP line 22 | — |
| 86 | "registered design for the float, in the EU and Norway" (listed as part of current protection) | inconsistent | Characterisation line 100, roadmap line 30, BOSAT IP5: decision on design registration for the hinge by Q3 2027. Research IP line 21: EU design does not cover Norway (separate Patentstyret filing) | "a design registration, decided in 2027 after the freedom-to-operate review (EU design plus a Norwegian filing)"; align float vs hinge across documents |
| 87 | FTO review in 2027 with Booster IAM support | consistent | Roadmap line 30; meeting summary line 14 | — |
| 90 | "An earlier Sunlit Sea patent covered the Generation 1 float construction" | consistent | Meeting summary line 24 (UK granted, extended to EP; status to confirm) | Confirm whether still in force before external use |
| 94 | "Generation 2 is qualified against the 2026 DNV floating solar standards before series production" | inconsistent (tense) | Qualification not started; roadmap M5 Q4 2027 | "will be qualified" |
| 97 | UV ageing to IEC TS 62788-7-2 followed by mechanical testing | consistent | Facts file line 120; research IP line 16 | — |
| 98 | "corrosion protection of the aluminium bottom plate" | inconsistent with facts-file rule | As line 69 | "of the bottom plate" |
| 102 | "Storm failures ... have started at moorings and float-to-float connections" | consistent | Research IP line 12 (Yamakura, Shintaku) | — |
| 102 | "a North Sea pilot withdrawn in 2026, was caused by an electrical connector" | consistent | Research competitors line 160 (CrossWind 1 May 2026, manufacturing defect in a connector) | — |
| 106 | "€0.30–0.40 per watt for early projects" | consistent | Roadmap line 82; lean canvas line 85 | — |
| 106 | "Site engineering is priced at 8–12 % of project capital cost" | consistent | Roadmap line 83 | — |
| 108 | Rixen leads "Germany (Magdeburg), Türkiye and Italy" | consistent | Facts file line 75 | — |
| 108 | Aaltvedt Betong offtaker candidate; HIP host; HNP host of Skiftestjørna and Storavatnet | consistent | Facts file lines 76–79 | — |
| 113 / 280 | "prototypes in Asia today; series production planned in Europe" / "in-house moulds in Norway for pilot volumes" (future) | outdated | Facts file line 34 and løypemelding 2026-07-16 §2: P4 casting already running in parallel in Norway with 3D-printed moulds | "prototypes cast in Asia and, for prototype 4, also in Norway" |
| 114 / 280 | Packing kits in Lithuania / Metsolar candidate | consistent | Meeting summary lines 27, 45 | — |
| 116 / 272–274 | Three breakwater supply routes with Clement Germany | consistent | Meeting summary line 46 | — |
| 123 | Design freeze Q1–Q2 2027, "About €0.5 million, largely within SuRE", TRL 5 | consistent | Roadmap lines 17, 75 | — |
| 124 | Skien havn reference phase "Q2 2027 – Q2 2028" | inconsistent | Facts file line 42: target install Q1 2027. Roadmap Q2–Q3 2027 | Align facts file and plan |
| 125 | DNV assessment "About €0.15 million" against ST-C108, ST-E309, RP-0584 | consistent | Roadmap lines 24, 75 | Research IP line 33 flags that €0.15 m may be low against the polymer test scope |
| 126 | Industrialisation "About €0.3–0.5 million" | consistent | Roadmap line 75 | — |
| 127 | IP "About €0.05 million" | consistent | Roadmap line 75 | — |
| 128 | "EIC Transition, Sunlit Sea share about €0.75 million" | consistent | BE2 budget line 5 (€750,000) | — |
| 128 | "€0.5–1.0 million plus the EIC share" | consistent | Roadmap line 76 (fourth-generation hinge €0.5–1.0 m) | — |
| 136 | "Global installations reached a record 664 GW in 2025 and the global fleet passed 3 TW (SolarPower Europe)" | consistent (web check) | SolarPower Europe press release, June 2026; not in research notes | Add to research notes |
| 136 | "EU installed 65.1 GW in 2025, its first annual decline since 2016 ... 718 GW by 2030, short of the 750 GW target" | consistent | Research `market.md` line 17 | Note: SPE's global outlook reports EU-27 at 67.2 GW and IEA PVPS 65.7 GW; keep one source per figure |
| 136 | "Value is shifting to solar that supplies a local load directly" | consistent (inference) | Research `market.md` line 17 implication | — |
| 138 | IEA PVPS 8.7 GW end-2024, 7.7 GW end-2023, just over 1.6 GW end-2018; ~90 % Asia, ~half China; NL and FR largest outside Asia | consistent | Research `market.md` lines 11–12 (primary) | — |
| 138 | Wood Mackenzie 77 GW by 2033; DE 2.2, FR 1.2, NL 1 GW | consistent (secondary) | Research `market.md` line 3, 124 | — |
| 138 | "with European growth held back by coverage and distance limits on inland water" (attributed to Wood Mackenzie) | inconsistent (attribution) | Wood Mackenzie names permitting and environmental concerns; the 15 %/40 m limits come from Solarplaza / WHG (`market.md` line 16) | Split the sentence or attribute to Solarplaza |
| 140 | Ember 25 GW behind hydropower connections, seven countries | consistent | `market.md` line 24 (primary) | — |
| 140 | Spain 4.5–6.5 GW floating offshore solar; Dutch 45 GWp at sea by 2050 | consistent (secondary) | `market.md` line 15 | — |
| 142 | NVE: ~1.4 GW applications, 14 MW licensed; 8 TWh by 2030 needs ~10 GW | consistent | `market.md` line 21 (primary) | — |
| 142 | "Norway passed 1 GW ... in September 2026"; Denmark 6.3–6.5 GW; Sweden 5.4 GW | consistent (secondary) | `market.md` line 22 | — |
| 142 | Statnett "about 3,500 MW of mature applications in the first half of 2026 alone", tightened requirements | consistent | `customers_regulation.md` lines 9, 60 | — |
| 142 | Q4 2025 NO1/NO2/NO5 74–82 øre/kWh; "about 24 øre/kWh in northern Norway" | consistent | `market.md` line 23 (NO4 24.1, primary) | — |
| 146 | Inland "rated above TRL 8"; offshore TRL 3–5; nearshore its own category | consistent | `market.md` line 13 (primary) | — |
| 148 | Two 500 kW platforms at Valencia; SolarDuck 0.5 MWp Merganser; Fred. Olsen 1848 pilots in Norway and Portugal | consistent | `competitors.md` lines 159–166 | — |
| 148 | HKN pilot "withdrawn in 2026 after thermal incidents" | consistent | `competitors.md` line 160 | — |
| 149 | CHN Energy 1 GW pile-mounted, 8 km off Shandong, ~end 2025, ~USD 1.16 billion incl. storage | consistent (secondary) | `competitors.md` line 166 | — |
| 149 | ~7.5 MW floating at Qingdao refinery; Changhua 373 MWac on leased coastal water | consistent (secondary) | `competitors.md` line 167 | Qingdao 7.5 MW is search-summary only |
| 150 | "No supplier has a commercial multi-megawatt floating reference on European coastal water, and no competitor publishes a price per watt" | consistent | `competitors.md` lines 159, 173 | — |
| 154 | "6.75 MWp at three named Norwegian sites, plus 30–50 MW of long-term potential at Storavatnet" | consistent | Facts file line 44 | — |
| 154 | "inbound requests without marketing, for example from Germany, Türkiye, Italy and Denmark" | inconsistent (cross-doc) | Türkiye and Italy came via Rixen (facts file line 75), not unsolicited; meeting summary line 50 names UK, Chile (unclear) and Germany; characterisation line 58 names Norway, Germany and Denmark; løypemelding 2026-07-16 names Mexico and Peru | Pick one list, verified with the user, and use it in all files |
| 158 | Lender, insurer concerns; insurers reassessing exposure | consistent | `market.md` line 25; `customers_regulation.md` line 19 | — |
| 159 | DNV-ST-C108, DNV-ST-E309 published May 2026, with DNV-RP-0584 | consistent | Facts file lines 117–119; research IP line 7 (edition 2026-04, announced 14 May 2026) | — |
| 159 | "IEC standards for floating PV are still in draft" | consistent | Research IP line 10 | — |
| 159 | "Bureau Veritas issued a first type certificate for a floating solar structure in November 2025" | consistent (secondary) | Research IP line 11 (28 Nov 2025) | — |
| 159 | "DNV reviewed Fred. Olsen 1848's design in 2026" | consistent | `competitors.md` line 215 (DNV news July 2026) | — |
| 160 | Norway <10 MW no NVE licence since 1 July 2025; Harbour and Fairways Act permit; zoning first | consistent | `customers_regulation.md` lines 7–8 | — |
| 160 | Sweden: water operations, notification or court permit | consistent | `customers_regulation.md` line 18 | — |
| 160 | Germany WHG ban on natural waters, 15 % and 40 m on artificial waters; coastal status unclear | consistent | `customers_regulation.md` line 16 | — |
| 167 | "imported TOPCon modules cost about €0.11–0.12 per watt ... European-assembled modules about €0.25 per watt" (October 2026) | consistent (secondary) | `market.md` line 18 | Note: meeting summary line 109 says the European-vs-Chinese price paradox "will not be emphasised in the business plan"; this sentence brings it in through market data. Also løypemelding 2026-07-16 §4 expected 20–25 % module price rise through 2026 |
| 167 | NREL: FPV ~25 % more expensive, "structural costs about three times higher", floats 75–85 % of structural cost | inconsistent (minor) | `business_model_finance.md` line 7: "about 300 % higher" structural cost, which is about four times, not three | "structural costs about four times those of ground-mount" or "about 300 % higher" |
| 167 | Offshore FPV installation ~30 % above ground-mount | consistent (secondary) | `market.md` line 19 | — |
| 167 | D7.4: "floats and breakwater together made up about €209/kWp of about €900/kWp total investment, and installation another €156/kWp" | inconsistent | D7.4 lines 843–858: line item is "Pontoon + Breakwater" for concrete pontoons with perimeter breakwater (D7.4 lines 567–575); total €899.83/kWp excludes MV cable | "In the SUREWAVE assessment of a 10 MW open-sea reference plant with concrete pontoons and a perimeter breakwater, pontoons and breakwater made up about €209/kWp of about €900/kWp (excluding export cable)" |
| 171 | NZIA non-price criteria on "at least 30 % of auctioned renewable volume (or 6 GW per year), from 2026" | inconsistent (minor) | Web check: obligation applies from 30 December 2025 (implementing act adopted 2025). Research notes did not re-check | "from 30 December 2025" or "from the end of 2025" |
| 172 | AFIR / FuelEU: shore power for most container and passenger calls from 2030 | consistent (secondary) | `customers_regulation.md` line 15 (90 % of calls, TEN-T ports) | — |
| 173 | EUPI-PV call with nearshore branch, deadline 1 December 2026; Innovation Fund small-scale | consistent | Facts file line 56; `customers_regulation.md` line 21 | — |
| 174 | "the 10 MW licensing threshold covers Sunlit Sea's whole plant range" | inconsistent (minor) | Threshold is below 10 MW (`customers_regulation.md` line 7); plan targets 10 MW-class contracts (line 34) and Storavatnet 30–50 MW long term (line 154) | "covers the first plants (below 10 MW)" |
| 174 | "Enova has granted pre-project support to Sunlit Sea's Gunneklevfjorden plant" | consistent | Facts file lines 43, 80 (1 MNOK) | — |
| 199 | EIC Transition targets wave-exposed inland water "with a utility partner, through a demonstrator on a German lake" | consistent | EIC proposal lines 26, 72, 165–167 (EDP, Hainer See) | — |
| 201 | Power-intensive industry >half of Nordic PPA volume; developers want ≥10 years | consistent | `customers_regulation.md` line 11 (primary) | — |
| 201 | "corporate buyers kept the PPA market going in 2025 while utility deals fell, and solar deals held up" | consistent (secondary) | `customers_regulation.md` line 13 | — |
| 201 | Norwegian state guarantee only for offtakers of ≥10 GWh/yr | consistent | `customers_regulation.md` line 12 (also ≥35 GWh total, specific industries) | — |
| 203 | Early adopters incl. "the quarry and port operator at Storugns on Gotland" | consistent | Facts file line 72 | — |
| 205 | "No published survey of industrial buyers' decision criteria for floating solar was found"; interviews early 2027 | consistent | `customers_regulation.md` line C-28 (section 2.5) | — |
| 211 | Fred. Olsen 1848 BRIZO: 124 kW Risør 2024, EDP reservoir lab Portugal, DNV review to RP-0584 for Hs up to 3.5 m | consistent | `competitors.md` lines 161, 215–216 | Add that it targets qualification in H1 2027 |
| 212 | Ocean Sun: Norway, Asia, Maldives, Brazil (300 kWp, first power 2026), 270 kWp Canary Islands, BV type certificate 2025, licensing in Asia | consistent | `competitors.md` lines 163, 179, 205–209; research IP line 11 | — |
| 213 | SolarDuck: Merganser, Tokyo Bay, shift to power hubs (2026), €15 million (2023) | consistent | `competitors.md` lines 165, 181 | — |
| 214 | Oceans of Energy: pilots since 2019, HKN installed 2025, faulty connector, closed May 2026 | consistent | `competitors.md` line 234 | — |
| 215 | BlueNewables two 500 kW at Valencia with Naturgy (2026), testing | consistent | `competitors.md` line 241 | — |
| 216 | Saipem / Moss XolarSurf prototype in Trondheim fjord; subsea and aquaculture | consistent | `competitors.md` line 261 | — |
| 217 | Swimsol "Over 50 resort islands in the Maldives; 2.4 MW plant (2026)" | inconsistent (minor) | `competitors.md` line 266: over 50 islands use Swimsol solar "roof and sea combined" | "over 50 resort islands supplied (roof and sea)" |
| 218 | Ciel & Terre certifying a heavy-duty version | consistent | `competitors.md` line 273 | — |
| 219 | New entrants Landatu, HelioRec, Reverlast; "Port pilots of up to 25 kW or no pilot yet" | consistent | `competitors.md` lines 169, 289–290 | — |
| 220 | 1 GW Shandong; 1.8 GW under construction in Hebei; ~7.5 MW floating | consistent (secondary) | `competitors.md` lines 166–167 | — |
| 222 | "Ciel & Terre is a partner in SuRE" | consistent | Facts file line 90 | — |
| 227 | "Registered design for the float" | inconsistent | As line 86 | As line 86 |
| 228 | "first nearshore reference plants in the Nordics in 2027–2028" | consistent with roadmap; inconsistent with facts file dates | See line 27 | — |
| 253 | Prosolar in Norway; Ceit for structural health monitoring | consistent | Facts file line 77; roadmap line 51 | — |
| 254 | SolarDuck €15 million 2023; CorPower €53 million plus EIC Accelerator; impact lenders financed small sea-based solar portfolios | consistent (secondary) | `business_model_finance.md` lines 17–18 | — |
| 255 | DNV for design-basis assessment; SINTEF and MARIN for testing | consistent | Roadmap lines 44, 49, 54 | — |
| 261–264 | Scale stages; EPC around 100 MW; sell plants after 5–7 years | consistent | Meeting summary line 110 | Meeting says technology supplier "at 1–2 MW projects"; plan says from 2028 at 1–10 MW. Acceptable |
| 266 | Swimsol debt-financed; inland FPV developers sell plants; EPC lesson | consistent | `business_model_finance.md` lines 15, 18–19 | — |
| 276 | "first Norwegian sites are sheltered enough to need little or no breakwater" | consistent | Risk assessment line 10 | — |
| 280 | "Production is fully subcontracted. Sunlit Sea designs the parts, owns the moulds" | consistent / partly outdated | Meeting summary line 45; but P4 in-house casting in Norway (facts file line 34) | See line 113 |
| 284 | Gross margin 30–40 %; trackers "about 32–34 %" | consistent, needs caveat | `business_model_finance.md` lines 14, 41: tracker margins inflated by US 45X credits, roughly 26–27 % without | Add "(partly supported by US manufacturing tax credits)" or drop the comparison |
| 285 | NREL float cost USD 0.40/W at 2 MW, 0.30 at 10 MW, 0.20 at 50 MW | consistent | `business_model_finance.md` line 8 (primary) | Plan compares € and USD directly ("sits in that range"); state the currencies |
| 285 | "At 10 MW and series production, the SUREWAVE economic assessment assumes about €0.21 per watt for floats and breakwater together, so the price falls with volume" | inconsistent | D7.4 lines 567–575, 843–858: concrete pontoons plus perimeter breakwater, no series-production assumption; different architecture from CONNECT kit (which excludes breakwater) | Drop or rewrite: "the SUREWAVE open-sea reference design costs about €0.21/W for pontoons and breakwater at 10 MW, which indicates the price level larger buyers will benchmark against" |
| 286 | "European solar power purchase agreements averaged about €34/MWh in the third quarter of 2025" | consistent (secondary) | `business_model_finance.md` line 20 (LevelTen €34.25) | Name LevelTen |
| 287 | "SUREWAVE assessment gives €0.062/kWh for a 10 MW plant in the Mediterranean" | consistent | D7.4 lines 99, 404, 1076 | Add "open-sea reference plant" to avoid reading it as CONNECT |
| 287 | Open-sea FPV in Northern Europe "several times higher" | consistent | `business_model_finance.md` line 12 (€250–650/MWh) | — |
| 297 | Nordic sites sheltered, product works without costly breakwater | consistent | Risk assessment line 10 | — |
| 299 | "Enova and municipal support lower the risk" | consistent | Facts file lines 42, 80 (Telemark Utviklingsfond, Enova) | "regional development fund" is more precise than "municipal" |
| 309 | Baltic "2029 onwards, Gotland demonstrator subject to EU funding" | consistent | Facts file line 39 (installation May–September 2029) | — |
| 310 | Mediterranean "From 2030" | consistent | Characterisation line 92 (pilot discussions 2029) | — |
| 320 | Business development budget about €0.3 million in 2027 | consistent | Roadmap line 75 | — |
| 326 | 2027: 0.35 MWp, €0.2–0.4 million | consistent | Roadmap line 82 | — |
| 327 | 2028: Gunneklevfjorden, "about 3.5" MWp cumulative; "first kit sales in Germany" | consistent (MWp); unsupported (kit sales) | 0.35 + 3.2 = 3.55. No Gen 2 kit order in Germany in repo; only Magdeburg 60 kWp interest | Mark as target |
| 328 | 2029: Storavatnet engineering and first supply, 4–5 MWp, €1–2 million | inconsistent with facts file; consistent with roadmap | Facts file line 44: Storavatnet install ~2028. 4–5 MWp only reached if Gotland (~1 MWp) is installed in 2029 | State that 4–5 MWp includes Gotland |
| 335 | Reputation via DNV design-basis assessment, SUREWAVE and SuRE results | consistent | — | Consider citing the 2022 DNV RP-0584 verification of Gen 1 (facts file line 117; research IP line 32), which is a real credential the plan does not mention |
| 339–353 | Source list | consistent | Matches research notes; "Soltec" is named in sources but only alluded to in body (line 266) | — |

## 3. Cross-document inconsistencies

| Topic | Plan | Companion / other source | Note |
|---|---|---|---|
| Skien havn timing | Reference phase Q2 2027 – Q2 2028; "2027" | Roadmap: build Q2–Q3 2027, M3 Q3 2027. Characterisation: in operation H2 2027. Facts file and løypemelding 2026-07-16: install Q1 2027 | Facts file is outdated or plan set is; resolve and update facts file |
| Gunneklevfjorden timing | Operation 2028 | Roadmap M6 financed Q4 2027, M8 Q3 2028; facts file Q2–Q3 2027 | Same |
| Storavatnet timing | First supply 2029 | Roadmap M9 investment decision 2029; facts file install ~2028 (rezoning ~2 years from mid-2026 implies ~2028) | Same |
| EIC Transition TRL 6 | End of project (36 months) | Roadmap: TRL 6 at month 36; characterisation: 2030; facts file line 40: "by end 2027" | Facts file line 40 is outdated |
| Design registration object | Float (lines 86, 227) | Characterisation line 100, roadmap line 30, BOSAT IP5: hinge | Align; IP research suggests a hinge is weakly protectable (function-dictated) |
| Design registration status | Presented as existing protection | All companions: decision by Q3 2027 | Use future tense |
| Inbound demand countries | Germany, Türkiye, Italy, Denmark | Characterisation: Norway, Germany, Denmark. Meeting: UK, Chile (unclear), Germany. Løypemelding: Mexico, Peru | Pick one verified list |
| D7.4 economics attributed to CONNECT | €209/kWp "floats and breakwater"; €0.21/W at series production | Characterisation line 39 "Proven economics" with €0.062/kWh, 10.7 % IRR, 8-year payback; D7.4 is concrete pontoon open-sea reference | Label every D7.4 figure as the open-sea reference plant |
| D7.4 IRR | Not used in plan | Characterisation 10.7 %; D7.4 gives 10.6 % (line 404) and 10.7 % (line 1076); payback 7–8 years (line 101) and 8 (line 404) | Minor; D7.4 is itself inconsistent |
| Cumulative MWp 2029 | 4–5 MWp incl. Gotland | Roadmap line 83: "Cumulative 4–5 MWp in operation (Skien havn and Gunneklevfjorden)" — those two give only 3.55 MWp | Roadmap arithmetic error; add Gotland there |
| CEO role | Leads Gen 2 R&D | BOSAT Tm4: "CEO and board chair on project development" (follows løypemelding 2026-07-16) | BOSAT outdated per facts file correction 2026-11-15 |
| TRL | 4–5 | BOSAT T3 option "TRL3-4" selected (note says 4–5); løypemelding 2026-07-16 says TRL 4; løypemelding 2025-11-17 says TRL 5–6 | Plan and facts file agree; BOSAT option is the closest available, fine |
| Prototype casting location | Asia today; Norway moulds planned | Roadmap line 17: in-house 3D-printed moulds in Norway in parallel (now); facts file line 34 same | Plan understates the Norwegian casting already running |
| Bottom plate | "flat aluminium" stated as fact | Characterisation lines 11, 37; lean canvas line 27 also state aluminium | All companions breach the facts-file hedge; the plan is the most external-facing |
| Prices, margins, engineering fee, costs per phase, EIC share | €0.30–0.40/W; 30–40 %; 8–12 %; €0.5 m / €0.15 m / €0.3–0.5 m / €0.05 m; €0.75 m | Roadmap and lean canvas identical; BE2 budget €750,011 | Consistent |
| Year-1 cost total | Not totalled in plan | Roadmap: €1.5–2.0 million in 2027 | Plan could carry the total for consistency |
| Revenue 2027 and 2029 | €0.2–0.4 m; €1–2 m | Roadmap identical | Consistent |
| Skien business model | Listed under own plants (line 63) and as supply-plus-engineering revenue (line 326) | Løypemelding 2026-07-16: "Direct sales / PPA" | Clarify before the financial annex |
| Storugns early adopter | Line 203 includes; line 301 "chosen" list omits | Lean canvas and characterisation include Storugns | Minor |

## 4. Not checkable

- Whether Eirik Larsen is a co-founder (affects "led by its founders", "two founders").
- Status of the earlier Gen 1 patent (in force, lapsed or written off; meeting summary flags "to confirm").
- "Each host has committed time to permits and studies" (line 205): plausible from løypemelding narrative, no written commitment in repo.
- Swimsol 2.4 MW, Qingdao 7.5 MW, Hebei 1.8 GW, Landatu, Reverlast details: research notes have them only as secondary or search-summary sources.
- Enova support for Skien havn: "indicated", not granted; plan does not overstate it, but no written confirmation in repo.
- The €0.2–0.4 million 2027 revenue range: no calculation in repo; a rough check (350 kWp at €0.30–0.40/W ≈ €0.1–0.14 m, plus engineering fees on Skien and Gunneklevfjorden) makes it plausible only if Gunneklevfjorden engineering is billed to the HIP-SPV in 2027.
- Facts-file rule on how to describe Chinese suppliers: no such rule exists in `docs/project_facts.md`. The plan's "Asia" phrasing matches the companions; the meeting summary (line 109) records the decision not to emphasise the European-vs-Chinese price gap, which line 167 partly reintroduces through module prices.
- "Marketed 2022–2024" start year for Gen 1.

Web checks used (market claims not in research notes): SolarPower Europe press release "Global Solar Market hits new record of 664 GW installation in 2025" (June 2026, solarpowereurope.org); NZIA non-price-criteria implementing act summaries (globalpolicywatch.com, hsfkramer.com, 2025).
