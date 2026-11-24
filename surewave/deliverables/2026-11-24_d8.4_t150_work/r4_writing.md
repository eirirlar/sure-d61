# T150 round 4: editor and confidentiality review of d84_merged.md

Persona: editor and confidentiality reviewer, sentence by sentence, annexes included. Confidentiality was checked against the financial plan (surewave/deliverables/2026-11-22_surewave_hrb_financial_plan_ker1.md, "FP"), docs/project_facts.md ("PF"), D7.4 (public, with its cost model on Zenodo), the breakwater-class note (surewave/deliverables/2026-11-23_surewave_breakwater_classes_nearshore.md, "BWN") and the EIC Transition proposal, which SINTEF, Clement Germany and EDP hold. Line numbers refer to d84_merged.md (1,595 lines, read end to end). Decisions D1–D59 and owner_questions.md are taken as given. Only errors inside them are reported.

## Mechanical and rendering checks

- `pandoc d84_merged.md -t html` runs with no warnings. The 84 lines that start with `#` become 1 h1 (the title) and 83 h2–h4 headings, in the right order (2.3, 4.5.1, 5, A.8, A.21 etc. render; their text only wraps across lines in the HTML). No heading is absorbed into a paragraph, and no "---" rules remain.
- There are 52 Markdown tables and 52 HTML `<table>` elements. Every table has the same column count in every row, a valid separator row, and a blank line before and after.
- No literal `**`, `|`, `##`, `](` or footnote marks are left in the rendered text. The nested lists in the executive summary (l.19–22) and in Section 3.1, steps 4 and 5, render as nested `<ul>`.
- No `**` in the source. None of "precisely", "crucially", "clearly", "therefore", "thus", "which is why", "it follows", "well beyond", "importantly" or "already" appears. "very" appears only in the expert's quoted rating (l.139). "key" appears only in names.
- Every "Section x.y" and "Annex A.n" reference resolves to a heading.
- No named Sunlit Sea customer, site, offtaker, contractor, vendor or price per watt appears in the text. Checked: Skien, Gunneklev, Storavatnet, Hainer/Leipzig, Gotland, Aaltvedt, Prosolar, Rixen/Mannheim, Metsolar, Tongge, Enova, Herøya, Haugaland, Nordkalk, Akershus, €/W and €/kWp of the kit.
- Counts re-checked and correct: 22 reach targets (3+1+3+5+7+1+2); A.4 by partner 4+4+3+2+1 = 14 and 7+2+2+3 = 14; A.5 15 rows; A.14 9; A.15 7; A.16 5; Zenodo 6+4+2+2+2+1+1 = 18 and 12 + 6; volume split 3.6 + 4.1 + 20 ≈ 28 MWp (13/15/72 %); 23 of 27 results in the 3.1 table; risk grades in 4.8; 9.75/10.375 = €940/kWp; 1.22/9.75 ≈ 13 %; 212/940 < 25 %; −40 % and −31 % in 4.10; Wood Mackenzie 4.4 GW / 10 years ≈ 0.44 GW, 16 MWp ≈ 3.6 %; cash deltas 0.70 and 0.86 against FP l.428–431; NOK conversions in 4.3.1; 1 March 2027 = 60 days after 31 December 2026.

## A. Major

1. Major (confidentiality; partly undoes D21). Section 4.6.2, l.709–724, with 4.1.1 l.426–432 and l.438. D21 removed the €0.83 per watt plant cost from 4.6.2. The share table still lets a reader rebuild it, because the plan gives everything needed to cost the breakwater:
   - the geometry: a 45° sector, widened by 10° on each side, at 15 m, in whole 20 m units, straight at 30 MWp (l.712, l.438);
   - the light unit: 2.5 × 1.0 m, about 30 t per 20 m against 123 t for the SUREWAVE unit (l.430–432);
   - the cost basis: "the breakwater and anchoring costs of D7.4 version 2.0 as modelled" (l.713). These are public: D7.4 and its cost model on Zenodo, about €1,091/m of material for the heavy unit and €8,770 per pontoon for installation (BWN l.94, 98).

   With the breakwater cost B per watt and the share s from the table, the plant cost is P = B(1 − s)/s. FP l.316–322 shows the actual values: at 1 MWp B = €0.28/W with no other uses, s = 25 %, so P = €0.83/W. A reader who uses D7.4's costs alone, without Sunlit Sea's markups (fabrication, fittings, transport, supplier factor 1.25, mobilisation; BWN l.103–104), gets a lower bound of roughly €0.5–0.6/W. Clement Germany, which designs and prices breakwaters and is asked to confirm these figures, can estimate B closely and so P closely. The two columns are also consistent with each other (B/P = 1/3 at 1 MWp gives 15 % and 25 %), which confirms the inversion.

   Fix (owner decision; recommend option b):
   - (a) Accept, and say so in Q36/Q74: the derivable figure is a plant cost including installation, not the kit price, and is accurate to about ±30 %.
   - (b) Replace the table and its "Basis" list with a statement that cannot be inverted: "The breakwater's share of the plant cost falls steeply with plant size. At a demonstrator of 50–300 kWp the breakwater costs as much as the PV plant or more. From about 5 MWp it is about a tenth of the plant cost or less, and at about 30 MWp a few per cent, with part of its cost carried by other uses. The figures are indicative and rest on the D7.4 version 2.0 breakwater and anchoring costs as modelled, plus Sunlit Sea's estimates for fabrication, fittings, transport, supplier margin and mobilisation; they are to be confirmed by Clement Germany." Also drop "45°" and "straight at 30 MWp" from l.712 (owner question Q74 already suggests dropping 45° in l.703).

2. Major (error inside an owner-question recommendation, Q36/Q74). The recommendation is to replace "about €0.10/kWh" (l.728) with "about twice the average award of €0.048/kWh". Twice €0.048 is €0.096/kWh, the same figure, so the change removes nothing. With the public PVGIS yield for a German lake (960 kWh/kWp at 2° tilt, FP l.316) and ordinary financing assumptions, the LCOE gives the plant capex: FP l.321 shows €0.099/kWh at €0.97/W. Combined with item 1, it gives P directly.

   Fix for l.728: "With the breakwater half carried by other uses, its cost of power is well above the average award of €0.048/kWh in Germany's solar tender of July 2025 (Bundesnetzagentur, August 2025). Selling to the grid does not cover its cost; it needs a buyer who values the power behind the meter, or investment support." Correct the recommendation in Q74 to match.

3. Major (confidentiality; the D41 route is reopened). Sections 4.7 and 4.6.2: the EIC scenario increment and the size of the first commercial plant.
   - l.761 gives EIC −€1.1M against base −€1.4M (FP l.428–430: −1,053 against −1,441, so +€0.39M).
   - l.765: "The EIC and EU-upside cases also include the first commercial plant at the demonstrator site after the project."
   - l.769: "The grants fund development work at close to cost."
   - l.705: the financial plan models that plant in 2031.
   - l.728: "A first plant of about 1 MWp serves as a reference and earns little margin."

   D41 dropped the 1 MWp from the EIC scenario so that no plant size meets an EBITDA or result effect. Section 4.6.2 restores the link. SINTEF, Clement Germany and EDP know the EIC budget: Sunlit Sea's €750k lump sum, with direct costs at 80 % (FP l.169). For them, (0.39 − 0.15)/1 MWp ≈ €0.24/W of kit and engineering gross profit. With the 40–50 % margin target (l.776), that gives a kit price of €0.48–0.60/W and a cost of €0.24–0.36/W. FP l.130–132 gives 2031 values of €0.45 and €0.23. The gross profit per watt alone is also sensitive: with D7.4's public €500/kWp for the modules, it gives the cost.

   The EU-upside increment (+€0.36M, l.762) works the same way for SINTEF, which coordinates EUPI-PV and knows the 1 MWp Gotland kit (PF l.42).

   Fix:
   - l.728: "The first commercial plant serves as a reference and earns little margin." Keep the 1–5 MWp range of l.705, so no size is attached to the scenario.
   - l.758–763: keep the Base and Grant downside rows. Replace the EIC and EU-upside rows with one sentence under the table: "The EIC and EU-upside cases improve the net result and the cash position against the base case; their lowest year-end cash is also in 2028."
   - l.769: "New EU project funding improves cash at the end of 2031 against the base case and the grant downside." Drop the €0.7M and €0.9M; their combination with two known kit deliveries gives the same route.

## B. Minor

4. Minor (error inside owner question Q68). Q68 recommends replacing "40–50 %" (l.776) with a qualitative target. l.740 still gives "41–44 %, as kit sales dominate" for 2030–2031, the same margin, so it opens the same derivation from D7.4's public €500/kWp. Fix, if the owner picks the Q68 option: l.740 2030–2031 cell becomes "Higher than in 2027–2029, as kit sales dominate". The executive summary and Section 13 give no margin, so no other change is needed. Correct the Q68 text to name both lines.

5. Minor (consistency; the text runs ahead of owner question Q28/Q70).
   - l.395 is careful: "The SUREWAVE reference design uses floats of pressed marine-grade aluminium sheets", with no generation named.
   - l.912 states that "Laboratory and wave-basin tests in SUREWAVE showed that the Generation 1 platform, square aluminium floats joined by polyurethane hinges, took excessive hinge loads."
   - l.20 says CONNECT "replaces the Generation 1 aluminium float".

   Until Q28 is answered, fix:
   - l.912: "Laboratory and wave-basin tests in SUREWAVE showed that the tested platform, aluminium floats joined by polyurethane hinges, took excessive hinge loads, …"
   - l.20: "It replaces Sunlit Sea's aluminium floats and is developed in parallel in SuRE, …"

6. Minor (consistency). Two readings of how long a result stays on the Horizon Results Platform.
   - l.30, l.1217 and l.1231: "keep a result on the platform for the rest of the four-year period".
   - l.1103 and l.1245: "until it is exploited or the four-year exploitation period ends on 31 December 2030".

   Fix l.30, l.1217 and l.1231: "and to keep a result on the platform until it is exploited or the four-year period ends on 31 December 2030".

7. Minor (fact, tense). l.254: "Guillaume Kegelart of Sunlit Sea co-authored the wave-basin paper". PF l.22 lists him as a former engineer, no longer employed. Fix: "Guillaume Kegelart, then at Sunlit Sea, co-authored …". The A.1 author column, "Kegelart (Sunlit Sea)", gives the affiliation at publication and can stay. Check whether Christoffer Isdahl (l.254) is still at Sunlit Sea; if not, write "then of Sunlit Sea" as well.

8. Minor (self-contradiction). A.11, l.1433: "Sunlit Sea wrote and issued all five newsletters." l.1441 and 2.5 (l.186, l.200) say that III–V are written and scheduled for 24 November – 8 December 2026. Fix: "Sunlit Sea wrote all five newsletters and issued the first two; III–V are scheduled (below)."

9. Minor (Annex B against A.23). Annex B, l.1588 gives D8.1 as "–", meaning "the project records checked hold no copy". A.23 (l.1533) gives D8.1 a public Zenodo record (doi 10.5281/zenodo.8278574), and OpenAIRE lists it (l.1534). Fix: "– (public on Zenodo, doi 10.5281/zenodo.8278574)", or the date of that record.

10. Minor (two statements read as a contradiction). The KER4 cell (l.298) and R5 (l.339) say: "Validation of the aerodynamic and hydrodynamic models against experimental and field data is further work (SINTEF)". The same rows, KER5 (l.299) and 6.4 (l.998), say that SINTEF's breakwater model "was assessed against wave-basin experiments". The wording is SINTEF's, but a reader takes it as "not validated against experiments". Fix l.298 and l.339: "Validation against field data, and further validation against experiments, is future work (SINTEF)". The 6.4 action row (l.1017) can keep SINTEF's own wording.

11. Minor (ambiguous comparison). l.404: "With the rope, the full connection stays far below the simulated extreme loads of 33–34 kN at the Baltic and Mediterranean sites; with a steel rod it is above them". "Stays below" reads as "safe". Fix: "With the rope, the capacity of the full connection, about 10 kN, is far below the simulated extreme loads of 33–34 kN at the Baltic and Mediterranean sites; with a steel rod, about 42 kN, it is above them".

12. Minor (repetition; D54 "one home"). The description of the second campaign (second-generation connectors, longer and thicker, fitted in pairs; the full-edge hinge only as a one-fifth segment at SINTEF) is written out at l.275, 335, 378, 390, 397, 402, 912, 1037 and 1122. Within 4.1 alone it appears at l.390, 397 and 402. Home: l.402. Fix:
    - l.390: "Sunlit Sea rates its CONNECT platform at TRL 4–5. Its full-edge third-generation hinge has been tested as a one-fifth segment at SINTEF (D6.3) and not yet in a basin (below). Prototype 3 …"
    - l.912: "… MARIN's second basin campaign tested the second hinge generation and SINTEF a segment of the third (Section 4.1)."
    - l.1037 and l.1122: shorten in the same way, with "(Section 4.1)".

13. Minor (repetition). The timing of the EIC first commercial installation ("immediately after completion in its summary, about 2030, and within 12–24 months after completion in its exploitation plan") appears almost word for word at l.705 and l.1208. Fix l.1208: delete the sentence "A first commercial installation of 1–5 MWp is targeted after the project: …" and end the previous sentence with "(first commercial installation: Section 4.6.2)".

14. Minor (repetition in one bullet). l.20: "The first Norwegian reference plant, in a port in 2027, uses small wavebreakers (…) on its exposed side. It gives the first field record of the platform with protection on its exposed side." Fix: "The first Norwegian reference plant, in a port in 2027, uses small wavebreakers (light floating barriers against wind waves and vessel wakes) on its exposed side and gives the first field record of the platform behind protection."

15. Minor (r3 #12 still partly open). A.20 (l.1518) and Annex B (l.1590) say that D8.3 was delivered on 18 November and "revised after both reviews" (Clement Germany 18 November, MARIN 19 November). They do not say whether the revised version is the one with the granting authority, or give its date. This is owner action 5. When the portal check is done, add: "The revised version, dated […], replaced the delivered file on […]", or "The delivered file is version 1; the revision is submitted with this plan."

## C. Wording

16. Wording. l.13: "an offshore floating photovoltaic (PV) system, abbreviated FPV". Fix: "an offshore floating photovoltaic (FPV) system". Section 4.6.1 and later use "PV" alone only inside "floating PV", which stays clear.

17. Wording. l.252: "The partners deposit the other five before this plan is submitted, MARIN's paper at MARINE 2025, the conference on computational methods in marine engineering, as its accepted manuscript under CC BY, since its published licence (CC BY-NC-SA 3.0) excludes commercial use." The appended clause is hard to parse. Fix: "The partners deposit the other five before this plan is submitted. For its paper at MARINE 2025, the conference on computational methods in marine engineering, MARIN deposits the accepted manuscript under CC BY, since the published licence (CC BY-NC-SA 3.0) excludes commercial use."

18. Wording. l.607 (value-chain table, casting row) says "moulds owned by Sunlit Sea" twice in one cell. Fix: "Sunlit Sea's own pilot moulds for pilot volumes; a series source qualified before the first megawatt-scale order, in Europe where it is cost-competitive; since Sunlit Sea owns the moulds, production can move".

19. Wording. l.1200: "Kodeworks". The company writes its name KodeWorks (PF l.18, "KodeWorks AS"). Fix: "KodeWorks".

20. Wording. l.1312: "The plan depends on three conditions: the kit price holds; the first plants receive investment support of about a quarter of their cost; and the Norwegian reference plants come on time and perform as designed, and kit volume, including a first 10 MW-class supply contract by 2030, comes as planned." The third item holds two conditions. Fix: "four conditions: …; the Norwegian reference plants come on time and perform as designed; and kit volume, including a first 10 MW-class supply contract by 2030, comes as planned."

21. Wording (requirement 3, tense). l.733: "The Booster mentor reviews the plan at the second business-planning workshop in December 2026". The workshop is planned (l.133). Fix: "The Booster mentor is to review the plan at the second business-planning workshop, planned for December 2026".

22. Wording. l.1532: "18 records in the SUREWAVE community on the open repository Zenodo". Fix: "18 records in the SUREWAVE community on Zenodo, the open repository run by CERN". The first use of Zenodo is l.238; define it there or here, once.

23. Wording (r3 #34 still partly open). Paragraphs and table rows over 1,500 characters remain: l.15 (1,601), l.254 (1,555), l.297 (KER3 row, 1,653), l.335 (R1 row, 2,458, with the evidence cell at 1,007), l.912 (1,592) and l.940 (1,621). Fix:
    - split l.15 after "(D3.1, D3.4)." and after "(Section 7.1).";
    - split l.254 after "set up the website's visitor monitoring.";
    - in l.335 move the Stadt Towing Tank sentence of the evidence cell to the text below the table, or replace it with "(Section 6.5)";
    - split l.912 after "cast in polyurethane." and after "(Section 3.1).";
    - split l.940 after "(Section 6.2… D6.4, Marine long-term degradation of concrete breakwater." and after "which the buoyancy of the reduced scale required."

## D. Earlier rejections in my area: does each rejection hold?

- r3disp_C, r3_writing #4 (site-type column, 4.4): holds as owner question Q75. The table still gives "Port / Industrial basin / Lake" (l.546–548) with roles, quarters and the minority share. For the EIC proposal's holders these are the named sites, so the recommendation in Q75 still stands.
- r3disp_C, r3_writing #5 (45° sector, scale-up path, €0.10/kWh): holds as owner question Q74, but the recommendation inside Q74 is wrong (item 2), and the share table is a separate route (item 1).
- r3disp_C, r3_writing #30 and #31: hold. "19 risks" (l.345, 1085) and Q-notation are used. The one spelled-out quarter (l.495) is the period of the NVE report, and l.30 introduces "Q3" once.
- r2disp_D, r2_writing #2 (2030–2031 revenue): superseded. D47 removed the euro revenue; the remaining routes are items 3 and 4.
- r2disp_D, r2_writing #3, and r2_writing #7 (EDP R&D / CNET): hold.
- r2disp_A, r2_cold #6, and r2disp_E, r2_cold #5: hold.
- r1disp_A, r1_cold #59 (glossary): holds. Every abbreviation checked is expanded at first use (FPV, TRL, LCOE, IRR, NPV, EBITDA, EPC, HPC, LWAC, CLC, CFD, DIC, SHMS, ABS, UWB, ILCSA, GEF, ISNRE, EU PVSEC, EERA, BOSAT, SCADA, PVC, NVE, IEA PVPS, CEM III).
- r1disp_D, r1_writing #3 and #6; disp_D writing 22, 24, 25: hold.

## E. Earlier findings in my area still not fixed

- r3 #1–3: fixed. Headings render. The euro amounts of the sensitivities are gone (l.779–782). The basin-campaign text follows Energies 19(7) 1609 throughout.
- r3 #4, #5: owner questions Q75 and Q74 (see D and items 1–2).
- r3 #6–11, #13, #15, #16, #18–33, #35, #36: fixed in the current text.
- r3 #12: partly fixed (item 15).
- r3 #14 (repetition): mostly fixed under D54. The second-campaign description remains (item 12). The Q1 2027 access-rights request is still written out in several sections (l.631, 814, 820, 1150, 1178, 1185, 1229, 1254, 1299); owner question Q67 accepts this as completed, so it is not reported again.
- r3 #17: owner question Q20.
- r3 #34: partly fixed (item 23).

Findings: 3 major, 12 minor, 8 wording.
