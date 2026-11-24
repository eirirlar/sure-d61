# T150 round 1 – partner exploitation-manager review of D8.4

Persona: the exploitation manager of each non-lead partner in turn. Method: every passage of `d84_merged.md` that names the partner was read against that partner's exploitation summary, the deliverables it led, the final technical report working copy, D1.8 and the KPI record. Line numbers "D8.4 l.N" refer to `scratchpad_t150/d84_merged.md`. Repo paths are relative to `C:\dev\src\sure-d61`. Abbreviations: FTR = `surewave/background/2026-11-19_surewave_final_technical_report_working_copy.md`; KPI-V = `surewave/background/2026-11-19_surewave_wp8_kpi_verification.md`; KPI-R = `surewave/background/2026-10-06_surewave_wp8_kpi_partner_responses.md`.

Owner decisions were taken as given. Where a decision itself contains a factual error, this is said explicitly (items E1 and E3).

---

## ACCIONA (KER2)

### A1 – major – 4.6.1 Supply row (D8.4 l.732)
Quote: "in conventional concrete as costed in D7.4, or with ACCIONA's circular mixes (KER2) where the buyer values their lower footprint at a higher cost".
What is wrong: the claim of a lower footprint contradicts the project's own LCA. D7.3 (led by IFEU) finds that the circular mixes give no relevant greenhouse-gas saving over a conventional breakwater with an EPS core, because the cement content needed for the strength is similar. D7.3 also finds that the choice of breakwater material is not decisive for the plant's footprint. Both ACCIONA and IFEU would comment: ACCIONA because the result is mis-sold, IFEU because its finding is reversed.
Source: `surewave/background/2025-10-06_surewave_d7.3_environmental_report.md` l.1328, l.1340, l.1762; D7.4 l.1146–1148 (`2025-09-05_surewave_d7.4_economic_assessment.md`).
Fix: "...or with ACCIONA's circular mixes (KER2) where the buyer values their properties: a mineral core in place of expanded polystyrene, high resistance to chloride ingress, recycled aggregates and a thinner HPC shell. D7.3 finds no relevant difference in carbon footprint between the circular and the conventional breakwater, and D7.4 finds the circular options cost more." Apply the same correction anywhere else a footprint benefit is implied (see A8).

### A2 – major – Section 5 table, KER2 row (D8.4 l.899)
Quote: "Through the breakwater supplier, or directly where ACCIONA builds | Per project, within the breakwater supply; where Clement uses ACCIONA's mixes, under an agreement between the two".
What is wrong: ACCIONA would reject this on substance. ACCIONA is a construction contractor and does not sell concrete. Its stated routes are use in its own projects, further R&D and consultancy. D1.8 records the mix designs as confidential ACCIONA know-how. If Clement or another precaster casts units from ACCIONA's mixes, ACCIONA's return is a know-how licence with technical assistance, not a share "within the breakwater supply".
Source: `surewave/background/2026-09-30_acciona_exploitation_summary.md` l.36–42; `surewave/background/2026-09-30_surewave_d1.8_ipr_management_plan_m36.md` l.274, l.415–417.
Fix (Agreement type / Payment basis): "Licence of the mix designs with technical assistance, where Clement Germany or another precaster casts breakwater units from them; or ACCIONA as construction contractor where it builds | Licence fee or royalty per m³ cast, plus technical assistance per project; or contract price where ACCIONA builds". Change the matching sentence in 6.2 action 2028–2030 (l.952) to "...and as breakwater material under a licence where Clement Germany or another precaster casts SUREWAVE breakwater units".

### A3 – major – credit for the Gijón prototype (D8.4 l.437, l.478, l.942)
Quote (l.942): "The mixes were tested in the laboratory and in a reduced-scale concrete breakwater prototype exposed for about nine months in the Port of Gijón."
What is wrong: the text never says who built and ran the prototype. ACCIONA designed and cast it (D4.3), deployed it at ACCIONA's R&D maritime demo site in the Port of Gijón, coordinated the monitoring, recovered it and carried out the post-exposure assessment of concrete, chloride ingress, reinforcement and biofouling. This is ACCIONA's main field result, and the evidence is the kind requirement 4 asks to be shown item by item.
Source: FTR l.2878 ("R&D maritime environment demo site of ACC in Port of Gijón"), l.2960, l.2962 (installed September 2025 with a four-line catenary mooring to gravity anchors, exposed until June 2026), l.180–181; `surewave/background/2024-08-30_surewave_d4.3_breakwater_prototype.md` l.193, l.314.
Fix (6.2, replace l.942): "ACCIONA cast the reduced-scale prototype (3.40 × 1.70 × 1.05 m; about 1.5 m³ of HPC, 0.5 m³ of LWAC and 0.7 m³ of cellular concrete) with conventional reinforcement, moulds and curing (D4.3). It installed the prototype at its R&D maritime demonstration site in the Port of Gijón in September 2025 on a four-line catenary mooring with gravity anchors, coordinated its monitoring with Ceit, and recovered and inspected it in June 2026. The inspection found no significant structural deterioration, no measurable loss of reinforcement thickness, local chloride ingress only near the openings for monitoring equipment, and biofouling on more than about 85 % of the assessed surfaces without measurable structural effect (final technical report)." In the KER2 maturity cell (l.437), add "built, deployed and assessed by ACCIONA".

### A4 – minor – 6.2 HPC bullet against 3.1 (D8.4 l.940 against l.415)
Quote (l.940): "with 5 % of the cement replaced by industrial by-products". Quote (l.415): "This plan states the replacement without a percentage."
What is wrong: the text contradicts itself, and there is a fourth source. D7.3 gives a 20 % clinker reduction for the HPC, which matches the D4.1 figures of 400 kg instead of 500 kg.
Source: `2025-10-06_surewave_d7.3_environmental_report.md` l.935; D8.4 l.415.
Fix: 6.2: "with part of the cement replaced by industrial by-products (fly ash and ground granulated blast-furnace slag)". Add D7.3 to the list in 3.1: "D7.3 gives a 20 % lower clinker content".

### A5 – minor – evidence compressed (KER2 rows, D8.4 l.437, l.478–479, l.936–942)
What is wrong: the final technical report holds the full development record, and D8.4 does not give it:
- 18 LWAC, 2 HPC and 26 cellular-concrete formulations developed and tested;
- chloride-migration coefficients of about 0.4–0.9 × 10⁻¹² m²/s;
- no measurable water penetration for the selected HPC;
- cellular concrete with about 76 % less cement than the ≥150 kg/m³ reference;
- HPC at 380 kg/m³ against the proposal's 350 kg/m³ target (+8.6 %).
Source: FTR l.171, l.175, l.443–444, l.2193.
Fix: add to 6.2, after the three result bullets: "ACCIONA developed and tested 18 LWAC, 2 HPC and 26 cellular-concrete formulations for density, strength, bending, cyclic and impact response, water penetration, chloride migration and shell–core interaction. The selected HPC showed no measurable water penetration, and chloride-migration coefficients were about 0.4–0.9 × 10⁻¹² m²/s (final technical report)." In the R4 row (l.479), add "the final technical report gives about 76 % less cement than the project's non-structural reference of at least 150 kg/m³". In R3 (l.478), add "against a proposal target of 350 kg/m³".

### A6 – minor – KER2 relation to KER1 shown only at its worst (D8.4 l.437, l.731)
Quote: "at today's costs D7.4 finds the conventional-concrete breakwater cheapest"; "With ACCIONA's high-performance concrete ... the LCOE rises from €0.076 to €0.085/kWh".
What is wrong: only the costliest variant (HPC) is quantified. D7.4 also costs the SUREWAVE LWAC variant, which is much closer to conventional. D7.4 adds that durability assessments may requalify the result.
Source: D7.4 l.567–572 (10 MW breakwater: conventional €1.22M, SUREWAVE LWAC €1.51M, SUREWAVE HPC €2.15M), l.1148.
Fix (4.6.1 Revenue row): "...the LCOE rises from €0.076 to €0.085/kWh (D7.4). The SUREWAVE LWAC breakwater costs about 24 % more than the conventional one, the HPC breakwater about 76 % more; D7.4 notes that more detailed durability assessments may change this ranking."

### A7 – minor – LWAC description incomplete (D8.4 l.437, l.939)
What is wrong: D7.3 records that the LWAC also replaces 20 % of the natural coarse aggregate with recycled construction-and-demolition aggregate. ACCIONA's summary does not say this, and D8.4 omits it.
Source: D7.3 l.935.
Fix: add "and, according to D7.3, recycled construction-and-demolition aggregate for 20 % of the coarse aggregate".

### A8 – minor – CLC positioning stated without the LCA result (D8.4 l.938)
Quote: "in place of the expanded polystyrene of conventional pontoon breakwaters, which is costly and has a high carbon footprint."
What is wrong: this is ACCIONA's claim, written as fact, and D7.3 qualifies it (see A1).
Fix: "ACCIONA positions it as the inner core of floating breakwaters, in place of expanded polystyrene, which it describes as costly and carbon-intensive. At breakwater level, D7.3 finds no relevant difference in carbon footprint, depending on the end-of-life treatment of the polystyrene."

### A9 – minor – source of the Spanish articles misstated (D8.4 l.318, l.182)
Quote: "These four are found in search indexes and web archives but were not read in full".
What is wrong: ACCIONA itself reported these four items, with links, on 26 November 2025. The text credits search indexes and not the partner.
Source: `surewave/background/2025-11-26_acciona_exploitation_and_media_email.md`.
Fix: "ACCIONA reported four further articles on the prototype in Spanish regional and trade press: La Nueva España (27 October 2024 and 1 October 2025), pv magazine España (4 November 2024) and Tellkes (late 2024). They were not read in full and are not in the count."

### A10 – wording – "newsroom" (D8.4 l.322)
Quote: "on its newsroom on 11 October 2024".
What is wrong: the KPI record classes this as an acciona.com article and states that no separate press release was found in ACCIONA's newsroom.
Source: KPI-V l.244, l.294.
Fix: "on acciona.com on 11 October 2024".

### A11 – minor – ACCIONA interview record (D8.4 l.331, l.338)
Quote: "The links to the published 2024 interviews are not yet in the evidence record."
What is wrong: the KPI record has the owner's note of 22 November 2026 that the ACCIONA Wideangle interview is published on LinkedIn. The ACCIONA row also names no interviewee, while the other rows name theirs.
Source: KPI-V l.278, l.282.
Fix: "The ACCIONA interview is published on LinkedIn; the links to the other three 2024 interviews are not yet in the evidence record." Name the ACCIONA interviewee(s) from the recording.

### A12 – minor – timeline against action plan (D8.4 l.1229 against l.952)
Quote (timeline 2029): "ACCIONA uses the mixes in construction projects". The action plan gives 2028–2030.
Fix: move the entry to the 2028 row ("ACCIONA starts using the mixes in construction projects") or write "2028–2030" in both places.

---

## Clement Germany (KER3)

### C1 – major – transition element and connection system credited to KER1 (D8.4 l.436, l.476, l.500, l.438)
Quote (l.500): "the transition element, a floating PVC pipe between breakwater and array attached with elasticated ropes". KER1 result (l.436): "...with full-edge polyurethane hinges, mooring, transition element and, for exposed sites, a floating breakwater". KER3 result (l.438) does not mention them.
What is wrong: Clement led Task 3.4 (connection system between breakwater and solar modules) and Task 3.3 (mooring and anchoring). D3.3 (Clement) designs the transition element. In SINTEF's connection tests, Clement supplied the steel-wire breakwater connections and the breakwater-to-FPV transition components. In the KER table these Clement results appear as Sunlit Sea components without credit.
Source: `surewave/background/2026-09-29_surewave_wp_task_deliverable_index.md` l.64–67; `surewave/background/2023-12-08_surewave_d3.3_final.md` l.144, l.1108–1156; FTR l.1568, l.2923.
Fix: KER3 result: "...design approaches for large floating concrete structures; the breakwater mooring and anchoring, the breakwater-to-breakwater connections and the transition element between breakwater and array (D3.3)". In 4.1 (l.500): "the transition element designed by Clement Germany (D3.3), a floating PVC pipe ...". In the KER1 result cell: "...integrated with Clement Germany's breakwater, mooring and transition element (KER3)".

### C2 – major – KER3 maturity understated (D8.4 l.438, l.454, l.477)
Quote: "Breakwater unit designed (D3.2, D3.3); wave transmission computed with CFD; shielding of the array measured in MARIN's 1:10 basin campaigns".
What is wrong: three facts are missing:
- Clement selected the circular ring layout (D3.3) and led the geometry, structural arrangement, buoyancy, stability and modular configuration.
- The CFD study is Clement's own FLOW-3D Hydro study of the cross-section variants (D3.2).
- The Gijón prototype was built from Clement's breakwater geometry, structural requirements and buoyancy and stability inputs.
4.1.1 (l.547) lists the prototype under the heavy class, but KER3 does not, so the text is also inconsistent.
Source: `surewave/background/2023-08-08_surewave_d3.2_floating_breakwater_design.md` l.38, l.504; FTR l.1148, l.1568, l.2096; `2025-02-03_surewave_clement_materials_and_resources.md` l.23 ("The circular layout was determined in Deliverable D3.3").
Fix (KER3 maturity): "Breakwater unit and ring layout designed by Clement Germany (D3.2, D3.3); wave transmission of the cross-section variants computed with CFD (FLOW-3D Hydro, D3.2); mooring and anchoring designed (D3.3) and optimised by MARIN (D5.1); shielding of the array measured in MARIN's two 1:10 basin campaigns; a reduced-scale prototype to Clement's geometry exposed for nine months at the Port of Gijón." Mirror this in the R2 row and in 3.3 Market readiness (l.454).

### C3 – minor – Clement's quantities behind D7.4 and D7.6 uncredited; internal report cited (D8.4 l.504)
Quote: "the materials report of Clement Germany and the economic assessment D7.4 use 10 MWp".
What is wrong: two problems.
- Stand-alone: the materials report is an internal, non-deliverable report that the reader does not have.
- Missing credit: its anchoring, transition-element and connection quantities are inputs to the D7.4 cost model and to the D7.6 mass and energy balances (D7.6 thanks Thomas Pehlke for the data).
Source: `surewave/background/2025-02-03_surewave_clement_materials_and_resources.md` l.2–15; D7.6 l.1412.
Fix: "D7.4 uses 10 MWp, with anchoring, mooring, transition-element and connection quantities supplied by Clement Germany, and a 2 MWp version 173 m across." Drop the reference to the report.

### C4 – minor – EIC site access through Clement not stated (D8.4 l.1138, l.741)
Quote: "an inland lake in Germany, whose owner signed a letter of intent on 8 September 2026".
What is wrong: the proposal states that Clement provides access to Hainer See through its relationship with the site owner. The repo facts file says the site access is via Clement's letter of intent and lapses without a collaboration agreement by 28 February 2027. Neither the credit nor the deadline appears. The deadline also bears on the 2027 agreement dates in 4.9, 6.3 and 9.
Source: `generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md` l.274; `docs/project_facts.md` l.67.
Fix: "...at an inland lake in Germany, reached through Clement Germany's relationship with the site owner, who signed a letter of intent on 8 September 2026; the letter lapses unless a collaboration agreement is signed by 28 February 2027." In 6.3, add the action "Q1 2027: collaboration agreement with the Hainer See site owner, if the EIC Transition project is funded".

### C5 – minor – Clement's role differs between sections (D8.4 l.732 against l.898; EIC l.156)
What is wrong: 4.6.1 says Clement "engineers and supplies the breakwater and designs its mooring and anchoring". Section 5 says "engineering, supply and installation". The EIC proposal says Clement "will supply and install the breakwater and mooring solution, priced by configuration".
Fix (4.6.1): "Clement Germany engineers, supplies and installs the breakwater with its mooring and anchoring (KER3)...".

### C6 – minor – standardisation status overstated (D8.4 l.1103)
Quote: "Clement is an active participant in national and international committees and brings in SUREWAVE experience".
What is wrong: Clement writes that the knowledge "will contribute to the advancement of industry best practices and future standardisation activities", which is future tense.
Source: `surewave/background/2026-09-04_clement_germany_exploitation_summary.md` l.65.
Fix: "Clement reports that it is an active participant in national and international technical committees, and that the SUREWAVE knowledge will contribute to future best practice and standardisation in floating infrastructure and mooring design."

### C7 – wording – "background" placement (D8.4 l.438)
Quote: "SUREWAVE development of Clement Germany's floating concrete breakwater (background) for exposed conditions".
What is wrong: the sentence reads as if the KER3 result were background. D1.8 keeps the two apart: Clement's pre-existing engineering knowledge is background, while the SUREWAVE breakwater geometry, configuration and design integration are Clement's project result.
Source: D1.8 l.367, l.443–447.
Fix: "Clement Germany's SUREWAVE floating breakwater design for exposed conditions, built on its pre-existing floating concrete breakwater know-how (background); ...".

### C8 – minor – web events contributors (D8.4 l.152)
What is wrong: the contributors are given as "SINTEF, Sunlit Sea, ACCIONA, MARIN". Clement presented in the SAB webinar (2.5.7) and reported it as a web event. IFEU answered questions in the same webinar.
Source: KPI-R (Clement, web events); `2024-11-19_surewave_lunch_webinar_summary.md` l.8–9.
Fix: "SINTEF, Sunlit Sea, Clement Germany, ACCIONA, MARIN; answers from IFEU".

### C9 – minor – D8.3 contributors (D8.4 l.165, l.378)
Quote: "Technical brochure ... Sunlit Sea, SINTEF"; "led by Sunlit Sea with SINTEF".
What is wrong: Clement reviewed D8.3 on 18 November 2026 with eleven comments and sent seven CAD graphics as input for four figures. IFEU (Guido Reinhardt) reviewed version 0.3.
Source: `surewave/background/2026-11-18_clement_d8.3_brochure_review_comments.md` l.3–12; `surewave/deliverables/2026-09-28_surewave_d8.3_technical_brochure.meta.yaml`.
Fix: "led by Sunlit Sea with SINTEF; Clement Germany provided the breakwater drawings and review, and IFEU reviewed the draft".

### C10 – minor – Clement's deliverables not all named
What is wrong: Clement lists D2.2 (requirements for the surface mooring system between array and breakwater), D3.2 and D3.3 as its outputs. D8.4 never cites D2.2.
Source: KPI-R (Clement, publications).
Fix: add D2.2 to the R2 evidence cell (l.477): "D2.2, D3.2, D3.3; D5.1 (mooring)...".

### C11 – minor – partner input versus template (D8.4 l.412)
Quote: "The partners described their results ... in their own format rather than in the template fields".
What is wrong: the template went out on 29 September 2026. ACCIONA's summary (26 November 2025) and Clement's (4 September 2026) predate it, so the sentence wrongly suggests these two partners ignored it.
Fix: "ACCIONA's and Clement Germany's summaries predate the template; the other partners also answered in their own format rather than in the template fields."

---

## SINTEF (KER4, KER5)

### S1 – major – validation status (D8.4 l.982, l.439, l.480)
Quote (l.982): "modelling, testing and qualification methods ... checked against the SUREWAVE laboratory and basin tests". Quote (l.439, l.480): "validation against field data is further work".
What is wrong: SINTEF's own plan says "Further work will focus on validation against experimental and field data", so experimental validation is also further work. The value proposition claims what SINTEF does not claim. The final technical report speaks of "validated aerodynamic simulations"; this conflict is not flagged.
Source: `surewave/background/2026-10-02_sintef_exploitation_plan.md` l.13; FTR l.3908.
Fix (l.982): "Value proposition: modelling, testing and qualification methods for floating structures, flexible connections and circular concrete, developed and applied on the SUREWAVE designs and test campaigns." (l.439 and l.480): "validation against experimental and field data is further work (SINTEF)". In 3.1, list the conflict with the final technical report.

### S2 – major – SINTEF's sustainability work uncredited (D8.4 l.442, l.486, l.1050)
Quote: "combining its environmental and social life-cycle assessment with the economic results of D7.4 (Sunlit Sea) and the technology-risk results (SINTEF)".
What is wrong: SINTEF led Task 7.1 (sustainability framework definition and mass and energy balances) and coordinated the technical data for the LCA. It also led Task 7.2 (technological risk assessment, 19 risk indicators, which support the TRL 5 rating). R11 is the "integrated sustainability assessment framework". The framework and the mass and energy balances are SINTEF's, and D7.6 thanks SINTEF for the coordination.
Source: FTR l.3270, l.3276, l.3285, l.3407; `surewave/background/2026-09-29_surewave_wp_task_deliverable_index.md` l.149–150; D7.6 l.1412.
Fix (KER7 result, R11 row, 6.7): "...led by IFEU, combining its environmental (D7.3) and social (D7.5) life-cycle assessments with the economic results of D7.4 (Sunlit Sea) and the technological risk assessment (SINTEF, 19 risk indicators), on the sustainability framework and the mass and energy balances established by SINTEF (Task 7.1)".

### S3 – minor – Surewave-ANN evidence understated (D8.4 l.482)
Quote: "Used to support the characterisation of the SUREWAVE mixes ... | D8.3 (mix characterisation); D8.5".
What is wrong: the record is fuller than the cell. SINTEF's own deliverable D5.2 was delivered on 26 November 2024. The model is trained on a database of 1,030 concrete mixtures that combines the WP4 tests with published data. Its predictions were validated against the experimental mixing and testing results, and SINTEF delivered a database interface and the Surewave-ANN web application.
Source: FTR l.254, l.583, l.2301.
Fix: "Model trained on 1,030 concrete mixtures (WP4 tests and published data), predictions validated against the WP4 mixing and testing results; database interface and web application delivered (D5.2) | D5.2 (2024); final technical report".

### S4 – minor – aerodynamic result not quantified (D8.4 l.439, l.986)
What is wrong: the final technical report states that the breakwater reduced the calculated aerodynamic lift and drag loads on the array by about 87 % and 97 %. This is SINTEF's headline result, and D8.4 does not give it.
Source: FTR l.3908.
Fix (6.4 first bullet): "...shielding effect of floating breakwaters (Energies 17(19) 4873, 2024): for the evaluated configuration the breakwater reduced the calculated lift and drag loads by about 87 % and 97 % (final technical report)."

### S5 – minor – SINTEF's roles in WP6 and at Gijón uncredited
What is wrong: SINTEF led WP6 and the connection test programme, which also covered Clement's steel-wire breakwater connections and the transition components. It contributed the marine-deployment requirements, the instrumentation support and the structural assessment for the Gijón prototype, and it tested ACCIONA's beams used to calibrate Ceit's concrete model. None of this is in 6.4.
Source: FTR l.2096, l.2923, l.2931, l.2960; `2026-02-02_surewave_natursea_pv_joint_webinar_summary.md` l.54.
Fix: add to 6.4, after the result bullets: "SINTEF led the technical validation work package: ultimate-strength and fatigue tests of the critical connections (hinges, breakwater connections and transition components; D6.1, D6.3), the bending tests of ACCIONA's mixes used to calibrate Ceit's concrete model, and support for the instrumentation and assessment of the Gijón prototype."

### S6 – minor – follow-on proposals missing from SINTEF's action plan (D8.4 l.998–1006)
What is wrong: SINTEF coordinates the EIC Transition proposal (modelling, design verification, reliability and validation) and the EUPI-PV application, both listed in Section 10, but neither appears in its action plan. SINTEF's plan names "future research proposals" as a route.
Source: EIC proposal l.270; `docs/project_facts.md` l.42, l.93.
Fix: add the row "2027–2030 | Coordination, modelling and validation in the EIC Transition project for the exposed-site version of KER1 if funded, and in the EUPI-PV nearshore demonstration if funded | Projects started".

### S7 – minor – tense of reuse in CIRCWIND (D8.4 l.1133)
Quote: "SINTEF's hydrodynamic modelling and its finite element methods ..., reused and developed further".
What is wrong: SINTEF writes that the finite element methods "are being reused" but that the hydrodynamic knowledge "will be reused".
Source: SINTEF plan l.11, l.19.
Fix: "SINTEF's finite element methods for cracking and damage in concrete, being reused and developed further; its hydrodynamic modelling, planned for reuse; potential use of Surewave-ANN".

### S8 – minor – GEOPON start date asserted (D8.4 l.1227)
Quote (timeline 2027): "SINTEF ... starts the planned GEOPON project".
What is wrong: SINTEF gives no date, and Section 10 says no programme or number is public yet.
Fix: "SINTEF ... starts the planned GEOPON project if it is funded".

### S9 – minor – SINTEF's modelling split across two KERs without explanation (D8.4 l.420, l.984)
What is wrong: SINTEF reported aerodynamic and hydrodynamic modelling as one route (Section 1 of its plan). D8.4 puts the aerodynamic part in KER4 and the hydrodynamic part in KER5 with MARIN, and the reader cannot reconstruct why the result is split (requirement 5).
Fix (3.1 step 5): "SINTEF reported its aerodynamic and hydrodynamic modelling together; this plan places the aerodynamic method with SINTEF's other methods in KER4 and the hydrodynamic modelling with MARIN's in KER5, because the customers for hydrodynamic services are the same, while ownership stays separate (Section 7.1)."

### S10 – minor – source conflict on SINTEF's hydrodynamic result not flagged
What is wrong: D1.8 lists "Mechanical testing and aerodynamic assessment methods" and Surewave-ANN as SINTEF's results, and "Hydrodynamic models and basin-testing methods" as MARIN's. SINTEF's own plan claims high-fidelity hydrodynamic modelling, supported by Preprint 1. Requirement 2 asks that conflicts are flagged.
Source: D1.8 l.278–286, l.403–405, l.475–479.
Fix: add a bullet in 3.1 step 4: "Hydrodynamic modelling: D1.8 attributes the hydrodynamic models to MARIN; SINTEF's input and Preprint 1 document SINTEF's own high-fidelity breakwater-dynamics modelling. This plan lists both, each owned by its developer."

---

## MARIN (KER5)

### M1 – major – ReFRESCO and MARIN's part of R5 (D8.4 l.480 against l.878)
Quote (l.480): "No ReFRESCO result is reported at project end ... The combined-effects work was delivered as SINTEF's aerodynamic wind-load method ... and SINTEF's high-fidelity hydrodynamic modelling". Quote (l.878): "ReFRESCO used for CFD of the modules in high waves and for breakwater damping (D5.1)".
What is wrong: the two sections contradict each other. D5.1, led by MARIN, reports ReFRESCO CFD of the PV modules in high waves and 2D CFD of the breakwater's viscous damping. D5.1 itself is the "coupled aero-hydrodynamic analyses" deliverable. R5's owners were MARIN and SINTEF, yet the delivered column credits only SINTEF.
Source: `surewave/background/2024-04-16_surewave_d5.1.md` l.34, l.664, l.688–690, l.910; Annex 1 Part B Table 2-5 (R5 owners MARIN & SINTEF); FTR l.2404.
Fix (R5 delivered): "KER4 and KER5. MARIN used ReFRESCO in D5.1 for CFD of the PV modules in high waves (replaced by low-fidelity models with safety factors because CFD lacked robustness in breaking waves and was costly in 3D) and for the viscous damping of the breakwater; no further ReFRESCO development is reported, against the progress D8.5 reported at mid-term. The combined wind–wave work was delivered as MARIN's coupled hydrodynamic analyses with breakwater damping (D5.1, KER5), SINTEF's aerodynamic wind-load method with breakwater shielding (KER4) and SINTEF's high-fidelity hydrodynamic modelling of floating breakwaters (KER5)."

### M2 – minor – mooring reduction stated without the site limit (D8.4 l.440, l.481, l.877)
Quote: "mooring optimisation of the SUREWAVE ring cut mooring mass by 34–56 % without exceeding proof loads".
What is wrong: the reduction holds for the Mediterranean and North Sea sites only. At the Baltic site the reference design exceeded proof loads, and the optimised mooring is 2–3 times heavier. 6.5 says this, but 3.2, 3.4 and 4.10 do not.
Source: D5.1 l.1294, l.1454, l.1482.
Fix: "...cut mooring mass by 34–56 % at the Mediterranean and North Sea sites without exceeding proof loads (nearly 60 % for the 2 MW North Sea farm); at the Baltic site, where the reference design exceeded proof loads, the optimised mooring is heavier (D5.1)."

### M3 – minor – mass versus cost (D8.4 l.1015, l.877)
Quote (l.1015): "D5.1 reports 34–56 % lower mooring-line mass and cost". Quote (l.877): "D5.1 gives the reduction for the weight, and with it the cost, of the mooring lines".
What is wrong: D5.1 optimises mass and assumes that cost "correlates strongly" with steel weight. The final technical report states that the mass reduction "cannot be interpreted directly as an equivalent reduction in installed cost".
Source: D5.1 l.1296; FTR l.4297.
Fix: "D5.1 reports 34–56 % lower mooring-line mass, taken in D5.1 as the measure of mooring cost; anchors, vessels, labour and weather delays are outside it (final technical report)."

### M4 – minor – conflict with MARIN's own figure not flagged (D8.4 l.414–419)
What is wrong: MARIN's summary says "up to a factor 2-3 reduction in mooring chains". D5.1 gives 34–56 % (about 60 % at most), and "factor 2–3" appears in D5.1 only as the Baltic increase. The text uses D5.1 (owner decision D3) but does not list the difference among the conflicts in 3.1, so MARIN will see its own statement silently replaced.
Source: `surewave/background/2026-09-30_surewave_marin_exploitation_summary.md` l.15; D5.1 l.1482.
Fix: add a bullet in 3.1 step 4: "Mooring reduction: MARIN's input gives up to a factor 2–3 reduction in mooring chains; D5.1 gives 34–56 % lower mooring mass at the Mediterranean and North Sea sites (nearly 60 % for the 2 MW North Sea farm) and a 2–3 times heavier mooring at the Baltic site. This plan uses D5.1."

### M5 – minor – MARIN's public deliverable and dataset not cited (D8.4 l.476–477, l.393)
What is wrong: D6.2 (MARIN, public report on the basin tests) and the Zenodo dataset "Wave basin tests of multi-body floating photovoltaics system and an external floating breakwater" (April 2024) are the primary evidence for the basin campaigns. The evidence cells cite D8.3 and the journal paper instead, and 2.5.23 lists the dataset without its producer.
Source: `surewave/background/2026-09-29_surewave_wp_task_deliverable_index.md` l.137; D8.4 l.393–394.
Fix: in the R1 and R2 evidence cells: "D6.2 (MARIN); dataset doi 10.5281/zenodo.10960431; Energies 17(9) 2059". In 2.5.23: "...the MARIN dataset 'Wave basin tests ...'".

### M6 – minor – KER5 evidence compressed (D8.4 l.440, l.1014–1016)
What is wrong: two D5.1 results are omitted.
- DIFFRAC heave and pitch motions were compared with the basin tests and were "generally similar".
- The breakwater was shown to strongly reduce vertical hinge loads, and horizontal hinge loads by about a factor of 3 around Tp = 4 s (less than 50 % for the largest farm in the highest sea states).
Both support MARIN's service offer.
Source: D5.1 l.652, l.846.
Fix: add to 6.5 first bullet: "In D5.1, DIFFRAC's motion predictions were compared with the basin tests and found generally similar, and the simulations showed the breakwater reducing vertical hinge loads strongly and horizontal hinge loads by about a factor of 3 around a 4 s peak period, less in the highest sea states of the largest farm."

### M7 – minor – no KER1 action in MARIN's plan (D8.4 l.1022–1026 against l.901, l.559)
What is wrong: Section 5 gives MARIN roles (basin testing of new configurations, mooring assessment), and 4.1.1 says the breakwater classes are "to be checked ... in basin tests" near their natural periods. MARIN's action plan has no such action, although Section 6 says that "Actions that concern KER1 follow the roles proposed in Section 5".
Fix: add the row "2028–2030 | Basin tests and mooring assessment for KER1: breakwater classes near their natural periods and the exposed-site configuration, if commissioned by Sunlit Sea or a demonstration project | Campaigns for KER1".

### M8 – wording – presenters and dates as MARIN reports them (D8.4 l.252, l.256)
What is wrong: two details differ from MARIN's own report.
- MARIN webinar of 28 October 2025: MARIN lists Tim Bunnik and Joep van der Zanden as presenters, and the text names Bunnik and William Otto.
- Floating Solar in Europe 2025: MARIN reports 13 February 2025, an oral presentation by Joep van der Zanden and Naman Baderiya. The organiser's agenda gives 14 February with van der Zanden only.
Source: KPI-R (MARIN tables); KPI-V l.98, l.128.
Fix: webinar: "Tim Bunnik and Joep van der Zanden (SUREWAVE), William Otto (BAMBOO), MARIN". Floating Solar in Europe: keep the organiser's date and add "MARIN reports the talk as given with Naman Baderiya".

### M9 – wording – partner column (D8.4 l.311)
Quote: "| MARIN tests |".
Fix: "| MARIN |".

### M10 – minor – protection of the mooring workflow (D8.4 l.1083)
Quote: "the mooring-optimisation workflow is MARIN know-how".
What is wrong: the workflow couples Dakota, third-party open-source software, to MARIN's own time-domain software, which is background. Without saying so, the text implies that MARIN owns the optimiser.
Source: MARIN summary l.15; Annex 1 Part B Challenge 4 (DAKOTA).
Fix: "the mooring-optimisation workflow, which couples the open-source toolkit Dakota to MARIN's time-domain software, is MARIN know-how".

---

## Ceit (KER6)

### E1 – major – inputs to the SHMS misattributed (D8.4 l.420, l.1034); this is an error inside decision D13
Quote: "Ceit's structural health management system uses Ceit's own finite element stress fields, MARIN's hydrodynamic load histories and SINTEF's material-property predictions."
What is wrong: Ceit's model used the following inputs:
- Clement's breakwater geometry;
- MARIN's load histories;
- ACCIONA's mixes, with the concrete model calibrated on SINTEF's three-point bending tests of ACCIONA beams;
- SINTEF's initial finite element models.
SINTEF supplied test data, not predictions, and the credit to ACCIONA and Clement is missing.
Source: `surewave/background/2026-02-02_surewave_natursea_pv_joint_webinar_summary.md` l.53–54; FTR l.2432, l.2457.
Fix: "Ceit's structural health management system combines Ceit's own finite element stress fields, calibrated on SINTEF's bending tests of ACCIONA's concrete mixes, with Clement Germany's breakwater geometry and MARIN's hydrodynamic load histories." Use the same wording in 6.6.

### E2 – major – Ceit's validation deliverable not used (D8.4 l.441, l.483–485, l.1034)
What is wrong: D5.7, led by Ceit, validates the WP5 tools against the ABS fatigue and fracture guides and DNV guidance. It calibrates the concrete model on WP4/WP6 test data and uses the second basin campaign to confirm that the slamming loads on the breakwater are negligible. This is the "validated" evidence the proposal asked for in R10, and D8.4 omits it. D5.7 also names the open item: validation with long-term field data from the prototype.
Source: `surewave/background/2025-09-05_surewave_d5.7_modelling_tools_validation.md` l.57 (lead CEIT), l.89–91, l.303, l.651, l.663.
Fix: KER6 maturity: add "finite element, crack-propagation and SHMS methods validated against ABS and DNV guidance, with the concrete model calibrated on WP4 and WP6 test data (D5.7); validation with long-term field data from the prototype is further work". Add D5.7 to the evidence of R8, R9 and R10. In the R10 maturity cell, add "basin-test data used to confirm the load assumptions (D5.7)".

### E3 – minor – Ceit's contribution to the connection work erased; error inside decision D4
What is wrong: D4 removes Ceit from all hinge statements. The final technical report credits Ceit with fatigue and crack-propagation methods in SINTEF's fatigue assessment of the connections (Task 6.3) and with a contribution to the assessment of hinge behaviour in MARIN's basin tests (Task 6.4). D1.8, written by the coordinator, lists "finite element, fatigue, and structural assessment by CEIT" in the hinge development. D5.3 says hinge modelling "will be done", with no later record. The decision is right that Ceit was not an input to the redesign; it is wrong to leave Ceit out entirely.
Source: FTR l.2923, l.2931, l.2993; D1.8 l.85, l.496–500; `2024-11-07_surewave_d5.3_structural_integrity_assessment.md` l.1004.
Fix: keep the redesign inputs as SINTEF and MARIN. Add to the R1 evidence cell (l.476): "Ceit contributed fatigue and crack-propagation methods to SINTEF's fatigue assessment of the connections (final technical report)."

### E4 – minor – Ceit's role at Gijón passive (D8.4 l.441, l.1032)
Quote: "In SUREWAVE the corrosion sensor operated for about nine months on the breakwater prototype".
What is wrong: Ceit led the development and data analysis of the corrosion and vibration monitoring and provided the systems on the prototype. The text describes the sensor as if it ran by itself.
Source: FTR l.2898, l.2960.
Fix: "In SUREWAVE, Ceit developed the corrosion and vibration monitoring, installed it on the breakwater prototype in the Port of Gijón with ACCIONA and analysed its data over about nine months of exposure; the corrosion sensor measured through about 5–6 cm of concrete cover."

### E5 – wording – tense of the transfer (D8.4 l.1032)
Quote: "Ceit transfers the eddy-current technology to two industrial applications."
What is wrong: Ceit writes "Exploitation activities ... will focus on transferring".
Fix: "Ceit plans to transfer the eddy-current technology to two industrial applications."

### E6 – minor – Ceit's hardware result classed as a method (D8.4 l.413)
Quote: "...and methods and service lines that the partners add to their existing portfolios."
What is wrong: D1.8 records "Corrosion monitoring hardware, methodology and data processing" and "FEM, structural integrity, fatigue, and SHMS tools" as Ceit software and hardware results. Ceit's sensor is a hardware result.
Source: D1.8 l.282–284.
Fix: "...one hardware platform on a defined path to market (Sunlit Sea's Generation 2 platform), one sensor technology at demonstrator stage (Ceit's eddy-current corrosion sensor), and methods, software and service lines that the partners add to their existing portfolios."

### E7 – wording – Ceit contract asserted (D8.4 l.1113)
Quote: "A contract with Ceit follows at the first site with a breakwater class that is monitored."
What is wrong: the sentence states the contract as settled, while it is the lead's proposal (requirement 3).
Fix: "Sunlit Sea proposes a contract with Ceit for the first site with a breakwater class where the owner wants monitoring."

---

## IFEU (KER7)

### F1 – major – background shown as a project result (D8.4 l.1085)
Quote: "Published methodology: the integrated assessment method is public through the SUREWAVE deliverables (D7.6 is public)".
What is wrong: the method is IFEU background. D7.6 states that the assessment "is based on the integrated life cycle sustainability assessment (ILCSA) methodology [Keller et al. 2015]", IFEU's pre-existing method. The SUREWAVE result is its application to the system, which D7.3, D7.5 and D7.6 publish.
Source: D7.6 l.405–417 (`2025-11-05_surewave_d7.6_integrated_sustainability_report.md`).
Fix: "Background and published application: the ILCSA methodology is IFEU's (Keller et al. 2015); its SUREWAVE application (scenarios, inventories, indicator results and recommendations) is public in D7.3, D7.5 and D7.6. IFEU's models, inventories and know-how stay with IFEU and are exploited in commissioned studies." Align 3.1 step 4 (l.413): "KER7 describes IFEU's application of its ILCSA method in D7.6".

### F2 – minor – IFEU's deliverables not credited (D8.4 l.1050–1052)
What is wrong: 6.7 names only D7.6. IFEU led D7.3 (including the local marine environmental impacts, with IUS Team Ness), D7.5 and D7.6, and it led Task 8.1 and D8.2 (societal needs and engagement).
Source: `2026-09-29_surewave_wp_task_deliverable_index.md` l.151–165, l.172; D7.6 l.1414; FTR l.3285, l.3345.
Fix: "Its basis in SUREWAVE is the work IFEU led: the environmental assessment with the local marine impacts (D7.3), the social life-cycle assessment (D7.5), the integrated assessment (D7.6) and the report on societal needs and engagement (D8.2)."

### F3 – minor – D7.6 recommendations that bear on the KER1 route are omitted (D8.4 l.632–641)
What is wrong: D7.6 recommends that offshore FPV "should be demonstrated offshore at a relevant intermediate scale as quickly as remaining technological de-risking allows". It also prefers large uniform units over five 2 MW units for lower material intensity, and finds that more profitable technical choices tend to be more sustainable. The KER1 plan puts the open-sea pilot after about 2033, and the text does not state this tension with IFEU's finding.
Source: D7.6 l.148, l.159.
Fix: add to 4.3.3: "D7.6 recommends demonstrating offshore floating PV at an intermediate scale as soon as technological de-risking allows, and prefers large uniform units over several 2 MW units for their lower material intensity. The KER1 plan takes the de-risking step at sheltered and exposed nearshore sites first, and proposes the open-sea pilot about 2031 (Section 4.6.1)."

### F4 – minor – no KER1 action in IFEU's plan (D8.4 l.1058–1061 against l.641, l.903)
What is wrong: 4.3.3 says the evidence for sheltered and nearshore sites "is indicative until it is assessed for those plants", and Section 5 gives IFEU a role in commissioned studies. IFEU's action plan has no matching action.
Fix: add the row "2027–2028 | Life-cycle assessment of the CONNECT configuration for sheltered and nearshore sites, if commissioned by Sunlit Sea, for the first multi-megawatt plant and its lenders | Study commissioned".

### F5 – minor – ISNRE record weaker than available (D8.4 l.234, l.172)
What is wrong: ISNRE 2025 is recorded as "Partner report" only. The consortium's final technical report also lists the talk (speaker, title, date and place). That record is internal, so the item stays in the "not yet found in a public record" note, but the Record column can name it.
Source: FTR l.3491, l.3721.
Fix: Record column: "Partner report; final technical report".

---

## All partners

### G1 – minor – D1.8 quoted more strongly than written (D8.4 l.1073)
Quote: "D1.8 reports that no ownership or access-right dispute requiring formal escalation arose during the project."
What is wrong: D1.8 says "No major ownership or access-right dispute requiring formal escalation was reported to project management."
Source: D1.8 l.91.
Fix: "D1.8 reports that no major ownership or access-right dispute requiring formal escalation was reported to project management."

### G2 – minor – "confirmed" without a source (D8.4 l.420)
Quote: "and the input confirmed the seven KERs".
What is wrong: no partner confirmed the KER set; partners described their results (requirement 3).
Fix: "Every reported result could be placed under one of the seven candidates."

### G3 – minor – KER1 roles missing from four action plans (Section 6)
What is wrong: Section 6 says "Actions that concern KER1 follow the roles proposed in Section 5". SINTEF's and Clement's plans have such actions, but ACCIONA's has only a breakwater mention (see A2), and MARIN's, Ceit's and IFEU's have none (see M7, F4). Ceit needs, for example, "2028–2030 | Monitoring offer for breakwater-class sites with Sunlit Sea, where the owner wants it | Offers made".
Fix: add one KER1 row to each of these plans, as in A2, M7 and F4 and the Ceit row above.

---

Findings: 11 major, 41 minor, 6 wording.
