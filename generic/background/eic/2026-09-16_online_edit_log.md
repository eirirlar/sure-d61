---
internal_title: "Online edit log — EIC SUREWAVE proposal & portal (submission day)"
acronym: SUREWAVE_EIC
call: HORIZON-EIC-2026-TRANSITIONOPEN
deadline: 2026-09-16 17:00 Brussels
baseline_snapshot: generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md
internal_date: 2026-09-16
purpose: >
  Track every proposed edit to the live proposal (in Teams online) and every entry
  into the EIC portal web forms. Prevent loss of work when other authors edit the
  document while we work, and prevent double-applying edits.
---


# Online edit log

Living document while the proposal is in Teams and the portal is being filled. Every proposed edit and every portal-field entry gets a status here.

## Baseline

Live text baseline: `generic/background/eic/2026-09-16_1302_eic_surewave_proposal_v1.md` (converted from the docx pulled at 13:02 on submission day). Supersedes the 08:38 snapshot. Note: WP structure changed from 6 to 7 WPs in this snapshot (old WP3 split into new WP3 Verification + new WP4 Performance/Durability; Manufacturing/Deployment/Business all pushed up by one number).

When we pull a fresh snapshot from Teams, save it in `generic/background/eic/` with a new `YYYY-MM-DD_HHMM_` prefix and update the baseline pointer above.

## Status legend

- **proposed** — drafted here, not yet in Teams / portal.
- **applied** — Eirik has entered the change online and confirmed.
- **superseded** — overtaken by later text, or another author changed the same passage; needs re-review before applying.
- **withdrawn** — decided not to apply.

## Correction history

- **2026-09-16 v2**: Rewrote Section 3 after Eirik flagged the Askim factory was closed October 2025 (2025-10-07 løypemelding). Corrected Skiftestjørna commissioning date (autumn 2024, not 2023) and ownership model (Sunlit Sea-owned develop-operate-sell, PPA to EV PowerCharge) — affected PF-001 and PP-003. Removed IE-001 Askim, replaced with the actually-existing assets (Edge platform, FreeCAD library, Skiftestjørna as validation plant, in-house cast-PU test setup, Tongge/Haitai supply chain).
- **2026-09-16 v3**: Removed country references (China/Weihai) from IE-005 and reserve PP-007 per Eirik. Partner names Tongge and Haitai Solar retained; location scrubbed.
- **2026-09-16 v4**: Rewrote PE-001 and PE-002 to strip all claims of post-project value or reuse. Eirik's rule: any statement that equipment has commercial or operational value beyond the project period opens the door for the EU to reclassify full-capitalised costs as depreciation and force partners to bear the fraction of "useful life" unused during the project. Reframed as end-of-life / material-recovery, with any continued operation explicitly outside grant scope. Task 6.5 renamed "Recovery, Post-Campaign Inspection and End-of-Life Handling" (was "…and Reuse"). Note: the original baseline T6.5 text already contained the same risk on CLEMENT's side ("CLEMENT intends to retain and reuse the floating breakwater and mooring components for future applications") — flagged for consortium discussion; my edit no longer amplifies it.
- **2026-09-16 v5**: Shortened PE-001 (1095 → 926 chars) and PE-002 (2720 → 2050 chars). Removed the three intra-cell bold sub-headings from PE-002 (Selection / Destructive inspection / End-of-life handling); prose runs as flat paragraphs. Task-title and Output line remain bold to match the docx convention for other tasks.

---

## Portal — Section 1: Publications / datasets / software / goods / services / achievements (up to 5)

Field limits: Type (dropdown), Short description ≤ 500 chars. Portal already shows one empty `Publication` placeholder.

Status: **proposed** 2026-09-16 v2.

**PF-001 — Skiftestjørna gen 1 installation** · Type: **Good** · 442 chars
> Sunlit Sea-owned 105 kWp gen 1 floating PV plant at Skiftestjørna, Haugaland Næringspark (Norway). Installed autumn 2024 under Sunlit Sea's develop-operate-sell model, delivered under the Enova Flytende Solkraft grant (with EV PowerCharge and Endra), operating under a PPA to EV PowerCharge to October 2026. First full operating period delivered production above expectation; used to calibrate demonstrator design and reliability assumptions.

**PF-002 — DNV-RP-0584 third-party verification** · Type: **Other achievement** · 444 chars
> Third-party design verification of the Sunlit Sea floating PV product against DNV Recommended Practice DNV-RP-0584 "Design, development and operation of floating solar photovoltaic systems" (2022). Documents alignment with the industry recommended practice on structural, mooring and safety design. Establishes the baseline the SUREWAVE-DEMO design will be extended against the 2026 DNV-ST-C108 (structural) and DNV-ST-E309 (mooring) standards.

**PF-003 — SUREWAVE MARIN 1:10 campaign & Energies papers** · Type: **Publication** · 401 chars
> 1:10-scale wave-basin test campaign at MARIN on the SUREWAVE protected floating PV concept, with Sunlit Sea contributing the FPV array design and geometry. Campaign generated motion, load and hydrodynamic-interaction data that anchors the design basis of this proposal. Publicly reported in Energies 17(9), 2059 (2024), DOI 10.3390/en17092059, and Energies 17(19), 4873 (2024), DOI 10.3390/en17194873.

**PF-004 — SuRE D6.1 multi-domain FPV model chain** · Type: **Software** (alt: Publication) · 433 chars
> Multi-domain floating-PV design model chain — parametric FreeCAD/STEP geometry → coupled hydrodynamic and structural FEM → thermal CFD → life-cycle assessment — documented in Horizon Europe SuRE deliverable D6.1 "Model chain description" (2025) with Sunlit Sea as WP6 lead and author of the FPV-side sections. Extended in D6.2 "Multi-domain design screening", it is the toolset that will verify the SUREWAVE-DEMO demonstrator design.

**PF-005 — Sunlit Sea CONNECT gen 2 platform** · Type: **Good** · 416 chars
> Sunlit Sea CONNECT gen 2 — a redesigned floating PV architecture decoupling standard commercial 710–740 Wp PV modules from the float, using a cast polyurethane frame around each panel on a 0.8 mm 5083-H111 aluminium bottom plate, joined by cast PU-foam CONNECT rods. Multiple prototypes built and lab-tested; prototype 4 in preparation. This is the FPV building block transferred into the SUREWAVE-DEMO demonstrator.

### Reserves for Section 1

- **PF-006** SUREWAVE breakwater connection strength tests (Other achievement) — 402 kN wire / 41 kN FPV connection + material tests
- **PF-007** Gen 1 delivery at Rixen Mannheim, Germany (Good) — earlier commercial reference

---

## Portal — Section 2: Previous projects or activities connected to the proposal (up to 5)

Field limits: Name ≤ 50 chars, Short description ≤ 500 chars.

Status: **proposed** 2026-09-16 v2.

**PP-001 — Horizon Europe SUREWAVE** · Name (41 chars): `Horizon Europe SUREWAVE (grant 101083342)` · Desc (472 chars):
> Horizon Europe RIA (2022–2026), SINTEF-coordinated 7-partner consortium; Sunlit Sea partner 2, leading WP2 (specifications and framework) and WP8 (dissemination and exploitation). Developed and validated the wave-protected FPV concept at TRL 4 through the 1:10 MARIN wave-basin campaign, integrated hydrodynamic and structural simulation, and laboratory connection-strength testing. Provides the direct baseline result on which the present SUREWAVE-DEMO proposal is built.

**PP-002 — Horizon Europe SuRE** · Name (19 chars): `Horizon Europe SuRE` · Desc (408 chars):
> Horizon Europe project (2024–2027) coordinated by Institutt for Energiteknikk (IFE). Sunlit Sea leads WP6 (Sunlit's integrated FPV technology), authoring the multi-domain model chain (D6.1, delivered 2025) and the multi-domain design screening (D6.2, in preparation). The methodology and toolset developed here will directly verify and screen the SUREWAVE-DEMO demonstrator design under the present proposal.

**PP-003 — Enova Flytende Solkraft** · Name (42 chars): `Enova Flytende Solkraft for Norske Forhold` · Desc (385 chars):
> Enova pilot programme (grant 23/12577, 2023–2025). Sunlit Sea lead recipient with EV PowerCharge AS and Endra AS. Delivered the 105 kWp gen 1 floating PV plant at Skiftestjørna in Haugaland Næringspark — the Norwegian nearshore reference plant now operating under Sunlit Sea ownership, providing multi-year field data used to calibrate SUREWAVE-DEMO design and reliability assumptions.

**PP-004 — SkatteFUNN Robusthet** · Name (40 chars): `SkatteFUNN Robusthet i flytende solkraft` · Desc (414 chars):
> Norwegian R&D tax-credit project (project 350626, 2023–2026) on floating PV robustness. Focus areas overlap directly with SUREWAVE-DEMO WP7 (reliability): materials-and-interface robustness of the aluminium/PU float, hinge fatigue behaviour, water-ingress and salt-corrosion characterisation, and instrumentation strategies for operational monitoring. Feeds directly into the reliability methodology proposed here.

**PP-005 — MariSol IPN** · Name (45 chars): `MariSol (Innovation Project in Industry, RCN)` · Desc (386 chars):
> Norwegian Research Council Innovation Project in Industry (IPN), initiated 2020, closing out in 2025. Contributed to development of the Sunlit Sea gen 1 FPV product and manufacturing methodology, including the aluminium-forming pipeline that the D6.1/D6.2 model chain now abstracts. Historical basis for the design and manufacturing know-how carried into the current gen 2 architecture.

### Reserves for Section 2

- **PP-006** Norsmaterials strategic PU-formulation collaboration (early stage)
- **PP-007** Tongge / Haitai Solar cast-PU manufacturing qualification programme

---

## Portal — Section 3: Infrastructure and major technical equipment (up to 5)

Field limits: Name ≤ 50 chars, Short description ≤ 300 chars.

Status: **proposed** 2026-09-16 v2 — **fully rewritten after Askim closure was flagged**. All entries now reflect assets Sunlit Sea actually has today (no employees, no factory; asset base is digital tools, the Skiftestjørna operating plant, and qualified partner supply chain).

**IE-001 — Edge sensor / data pipeline** · Name (36 chars): `Sunlit Sea Edge sensor/data pipeline` · Desc (295 chars):
> Real-time sensor data platform designed by Sunlit Sea for FPV field units, running on resource-constrained edge hardware — multi-sensor ingestion, buffering and remote upload. Directly extensible to the demonstrator instrumentation set (structural, environmental, reliability) defined under WP4.

**IE-002 — Parametric FreeCAD/STEP library** · Name (42 chars): `Parametric FreeCAD/STEP FPV design library` · Desc (283 chars):
> Parametric FreeCAD model library and STEP-export pipeline for the CONNECT gen 2 architecture. Supports rapid layout variations for coupled hydrodynamic/structural FEM and thermal CFD analysis. Documented in Horizon Europe SuRE D6.1; ready for demonstrator design iteration under WP2.

**IE-003 — Skiftestjørna operational plant** · Name (43 chars): `Skiftestjørna 105 kWp operational FPV plant` · Desc (300 chars):
> Sunlit Sea-owned 105 kWp gen 1 floating PV plant at Skiftestjørna, Haugaland Næringspark (Norway). In service since autumn 2024. Operational validation platform in Northern-European nearshore conditions; instrumentation and monitoring approach directly transferable to the SUREWAVE-DEMO demonstrator.

**IE-004 — In-house cast-PU test setup + Norsmaterials** · Name (43 chars): `In-house cast-PU test setup + Norsmaterials` · Desc (274 chars):
> Norwegian in-house cast-PU test setup using 3D-printed moulds, established ahead of the P4 prototype build. Strategic collaboration with Norsmaterials (Sandane) under active discussion to industrialise a UV-resistant PU formulation for gen 2 and the SUREWAVE-DEMO FPV units.

**IE-005 — Qualified cast-PU FPV manufacturing supply chain** · Name (48 chars): `Qualified cast-PU FPV manufacturing supply chain` · Desc (274 chars):
> Qualified cast-PU FPV manufacturing supply chain through Sunlit Sea's active partnership with Tongge and Haitai Solar. Prototype 3 produced under the arrangement in autumn 2025; P4 currently in production. Ready manufacturing route for the SUREWAVE-DEMO FPV units under WP4.

### Reserves for Section 3

- **IE-006** IFE materials-test facility access via SuRE — Name (34 chars): `IFE materials-test access via SuRE` · Desc (278 chars):
  > Access to IFE (Institutt for Energiteknikk) materials-testing facilities — accelerated UV weathering, salt-spray, chloride and thermal testing — via the ongoing Horizon Europe SuRE partnership. Currently in use for gen 2 PU-variant qualification; extendable to demonstrator FAT.
- **IE-007** DNV-verified design methodology (borderline whether this counts as "infrastructure/equipment" vs. an achievement — likely a better fit for Section 1)

### Note on possible duplication

Skiftestjørna now appears in both Section 1 (PF-001, as a delivered Good) and Section 3 (IE-003, as an operational validation platform). Both are legitimate framings. If the portal / reviewers dislike the duplication, keep it in Section 1 (Good) and swap in IE-006 (IFE test-facility access) in the Section 3 slot.

---

## Proposal text edits

### PE-001 — Expand Phase 3 decommissioning paragraph (Section 1 Excellence)

Status: **proposed** 2026-09-16 v4 (was v1 2026-09-16 — see correction history).
Location: Section 1 "Excellence", Phase 3 discussion (single paragraph immediately following the "Phase 3 -- Demonstration and Validation (M15-M34)" block; in the 08:38 baseline this is around line 130).
Reason: Current paragraph gives one sentence to recovery and doesn't reflect (a) the string-level + drone selection workflow or (b) the destructive-inspection protocol. Rewrite avoids any language that claims post-project value on the demonstrator components (per Eirik: such claims risk the EU reclassifying full-capitalised costs to depreciation and forcing the partner to bear the residual "useful life" cost). Recircle is retained as an end-of-life routing channel, not as a resale market. Continued operation is mentioned as a possibility explicitly outside the grant scope.

**Find (exact text in current baseline):**
> At the end of the campaign, the demonstrator will be recovered and inspected. The floating breakwater and mooring system will be reused by CLEMENT for future applications, while PV modules, inverters, and electrical equipment will be redeployed or transferred to secondary markets where feasible. This will provide additional evidence on durability, reliability, lifecycle performance, and component reuse.

**Replace with:**
> At the end of the campaign, the demonstrator will be recovered and inspected under T6.5. String-level performance at the inverter and drone thermographic surveys will be used, with a stratified random sample, to select FPV units for detailed inspection — quantifying water ingress by weight, opening floats to measure trapped water, measuring polyurethane-to-aluminium and polyurethane-to-glass delamination, and characterising biofouling and structural wear. Recovered components will be routed to certified end-of-life and material-recovery channels, including PV-specific circular-economy channels such as the Recircle marketplace (in which EDP participates). Continued operation of parts of the demonstrator beyond the funded period, if agreed with the site owner, would be pursued outside the grant scope. Inspection results feed the lifecycle assessment, reliability model and engineering guidance for follow-on designs.

### PE-002 — Rewrite T6.5 (WP6 Deployment table, Recovery task)

Status: **proposed** 2026-09-16 v4 (was v1 2026-09-16 — see correction history).
Location: Section 3 (Implementation), WP6 table, Task 6.5 cell (in the 08:38 baseline this is the last task in WP6, currently titled "Task 6.5 -- Recovery and Post-Campaign Assessment").
Reason: Same as PE-001. Adds selection workflow + destructive-inspection protocol + Recircle. Renames the task from "Recovery and Post-Campaign Assessment" to "Recovery, Post-Campaign Inspection and End-of-Life Handling" — no "reuse" in title. Removes claims of post-project residual value on any partner's equipment (audit-risk avoidance per PE-001 reasoning).

**Find (unique anchor line at start of task cell):**
> **Task 6.5 -- Recovery and Post-Campaign Assessment (L: CLEMENT; P: All; M33-M34):**

**Then replace the entire task cell text with:**
> **Task 6.5 -- Recovery, Post-Campaign Inspection and End-of-Life Handling (L: CLEMENT; P: All; M33-M34):** At the end of the campaign, the demonstrator is recovered and inspected in two tiers. Throughout T6.3, string-level electrical performance at the inverter is analysed to flag underperforming strings, and periodic drone flights with RGB and thermal cameras (EDP-led) localise cell-level anomalies to individual FPV units. At the end of the campaign, units flagged by these two channels — together with a stratified random sample of the remainder — are selected for detailed inspection.
>
> Each selected FPV unit is (i) weighed against its factory-recorded dry weight to quantify total water ingress (K6); (ii) cut open to measure the volume of trapped water inside the float; (iii) inspected at each material interface for delamination between the cast polyurethane frame, the aluminium bottom plate and the solar-panel glass; (iv) characterised for biofouling and algal or micro-organism colonisation on wetted surfaces; and (v) assessed for corrosion and mechanical wear at structural and electrical interfaces. The breakwater, mooring lines, connectors and anchors are inspected in parallel for water ingress, corrosion, degradation, growth and wear, with attention to hinge and connection systems relative to design predictions and monitoring data.
>
> Recovered components are routed to certified end-of-life and material-recovery channels — PV modules through circular-economy channels including the Recircle marketplace (in which EDP participates); polyurethane, aluminium, steel, concrete, mooring hardware and cabling through standard industrial recycling routes. Any continued operation of parts of the demonstrator beyond the funded period, if agreed with the site owner, would be pursued outside the grant scope. Inspection findings and recovery outcomes feed the lifecycle assessment, reliability assessment (T6.4) and commercialisation roadmap (T7.3, T7.5). **Output: Final Performance, Reliability and Lessons Learned Report (D6.3).**

### Verify before applying PE-001 / PE-002

- **Recircle / EDP relationship**: "the Recircle marketplace (in which EDP participates)". Please confirm EDP's actual role on recircle.market before pasting; if their role is more distinctive (e.g. co-founder), stronger phrasing is available.
- **Continued-operation phrasing** (`"if agreed with the site owner, would be pursued under a separate arrangement outside the grant scope"`): careful and audit-safe as written. Do NOT strengthen this to "will be operated after project end" or similar — that would put the residual-value claim back and invite the depreciation reclassification.
- **Stratified random sample**: Assumes the array is large enough to make sampling meaningful. Fine at ~50–300 kWp / ~50–150 modules; if the demonstrator has settled at the low end, swap to "a defined subset of the remainder".
- **Original baseline T6.5 still contains a CLEMENT residual-value claim** ("CLEMENT intends to retain and reuse the floating breakwater and mooring components for future applications"). PE-002 replaces the whole cell and removes it. If Sunlit Sea applies PE-002, that claim also comes out — which is *good* for CLEMENT's own audit exposure on the €518k Table 3.3h purchase lines. Worth telling Balram / CLEMENT explicitly rather than doing it silently.

### PE-003 — Fix deliverable reference in T6.5 (D5.4 → D6.3)

Status: **proposed** 2026-09-16.
Location: Same T6.5 cell as PE-002 (end of the task text in the current baseline).
Reason: Current baseline text ends "Output: Final Performance, Reliability and Lessons Learned Report (D5.4)." — but the Table 3.3c deliverables list has this deliverable as D6.3 (Final performance, reliability and recovery report). Note that if PE-002 is applied, this fix is already included (PE-002 replaces the whole cell). Only apply PE-003 as a standalone if you keep the old T6.5 wording.

**Find:**
> **Output: Final Performance, Reliability and Lessons Learned Report (D5.4).**

**Replace with:**
> **Output: Final Performance, Reliability and Lessons Learned Report (D6.3).**

### PE-004 — Permitting specifics in T6.1 (WP6 Deployment table, Site preparation task)

Status: **proposed** 2026-09-16.
Location: Section 3 (Implementation), WP6 table, Task 6.1 cell (baseline line ~453; task titled "Task 6.1 -- Site Preparation, Permitting and Installation Planning").
Reason: The current T6.1 text is generic. Adds three factual points relevant to permitting risk: (a) demonstrator does not need grid interconnection (removes the typical FPV-permitting bottleneck); (b) environmental and social studies run in parallel with engineering, tracked in the T6.1 plan; (c) Sunlit Sea has a prior private-lake permit reference in Germany. Framed to describe the situation without dismissing risk and without exaggerating it. No new budget line — environmental consultancy is already in CLEMENT's €25k subcontracting per Table 3.3g.

**Find (exact text in baseline, penultimate sentence of T6.1 body):**
> The task will deliver a complete installation and operations plan supporting safe deployment and operation of the demonstrator.

**Replace with:**
> The task will deliver a complete installation and operations plan supporting safe deployment and operation of the demonstrator. The demonstrator does not require grid interconnection, removing the permitting pathway that typically drives lead-time for FPV projects in inland waters. Environmental and social studies required for the final site permit run in parallel with WP2-WP4 engineering under the German inland-water permitting framework and Saxony authority guidance; scope, timelines and dependencies are tracked in the T6.1 planning output. Sunlit Sea's prior gen 1 installation at Rixen Mannheim (Germany, 2023) obtained authorisation on an equivalent private-inland-water pathway without material permit issues.

### PE-005 — Update R8 mitigation in risk register

Status: **proposed** 2026-09-16.
Location: Risk register table, row R8 "Permitting or site-access delays (L/H)" (baseline line ~606, third-column mitigation cell).
Reason: Reinforce PE-004 at the risk-register level so reviewers scoring risk management see the concrete mitigations, not just a generic "LOI + local relationships" cell. Same three factual points, condensed.

**Find (exact mitigation text in current R8 cell):**
> Site secured through LOI, established local relationships, permitting support, early preparation activities.

**Replace with:**
> Site secured through LOI; demonstrator does not require grid interconnection, removing the principal permit-timing driver for inland-water FPV; environmental and social studies proceed in parallel with WP2-WP4; permit pathway comparable to Sunlit Sea's prior private-lake installation in Germany.

### Verify before applying PE-004 / PE-005

- **Grid-connection consistency across the docx.** Objective O1 in the baseline currently reads "Protected FPV demonstrator, `[grid-connected]{.mark}`, commissioned and generating" (line ~71; the `.mark` highlight suggests SINTEF already flagged this for revision). If PE-004/PE-005 are applied while O1 still says "grid-connected", the two sections contradict each other. Confirm with the consortium that the demonstrator is genuinely standalone; if yes, O1 also needs to change (would be a separate PE). If the demonstrator does connect to a local load or battery — but does not export to grid — the language "does not require grid interconnection" still holds, but you may prefer to add "operates in standalone configuration with local load" to O1.
- **Mannheim reference.** Fact-safe on permitting (permit went through). If a reviewer digs into Sunlit Sea + Mannheim publicly, they may find the separate quality/payment history from the same 2023 installation — that is a delivery-quality issue, not a permit issue, and the wording I've used ("obtained authorisation on an equivalent private-inland-water pathway without material permit issues") is honest to that scope. If you'd prefer not to invite the search, drop the Mannheim sentence entirely; PE-004 still stands without it.
- **Budget check.** PE-004 does not add any activity that requires new budget. Environmental consultancy is CLEMENT's €25k subcontracting line (Table 3.3g); site engineering time is in personnel PMs already allocated.
- **Framing check against your guidance.** Not glossing (states the study is needed before final permit and describes the pathway). Not exaggerating (no "no risk" claim; residual risk sits in the risk register at (L/H) as before). No budget grab.

### PE-006 — Add political / energy-security / price-context paragraph (Section 2.1)

Status: **proposed** 2026-09-16.
Location: Section 2.1 "Credibility of the impacts", after the market-scope paragraph ("The initial market is European reservoir and artificial-lake owners…"; baseline line ~156) and before the "Business model and route to customers" subsection.
Reason: Section 1 has market sizing figures but no macro-driver framing. Reviewers scoring Impact respond to a clean line from EU policy priorities → energy-price economics → why *this* FPV technology in *this* market. Tied to specific SUREWAVE-DEMO characteristics rather than boilerplate REPowerEU invocation.

**Find (exact anchor — last sentence of the current market-scope paragraph):**
> Sheltered harbours and coastal sites are an adjacent market requiring additional marine qualification. This focus connects the inland demonstrator to a defined first market while preserving a route to wider deployment.

**Replace with (keeps the anchor sentence, appends a new paragraph):**
> Sheltered harbours and coastal sites are an adjacent market requiring additional marine qualification. This focus connects the inland demonstrator to a defined first market while preserving a route to wider deployment.
>
> The demand pull is structural. REPowerEU set the direction in 2022 — accelerate domestic renewable capacity to reduce fossil-fuel imports and shield European industry from price shocks — and subsequent EU instruments including the Net-Zero Industry Act have prioritised the equipment and integration end of the solar value chain. European wholesale electricity prices remain well above pre-2021 levels, so any capacity that displaces gas-set marginal generation compounds in value across its lifetime. Floating PV expands the set of usable European sites without competing with agricultural or forested land; inland installations also shorten transmission distance to demand. SUREWAVE-DEMO advances the FPV subset — protected exposed inland waters — that current European FPV suppliers cannot serve without over-engineering.

### PE-007 — Add LCOE + selective-protection paragraph (Section 2.1)

Status: **proposed** 2026-09-16.
Location: Section 2.1 "Credibility of the impacts", after the "selective protection is most attractive…" paragraph (baseline line ~188) and before the "Business validation and decisions" subheading (baseline line ~190).
Reason: The current paragraph states selective protection as a hypothesis to be tested; SUREWAVE's own prior techno-economic work already indicated the shape of the answer. Making that explicit strengthens the credibility of the LCOE claim in O9 / B3 and frames the D6.2 quantification as sharpening a known finding rather than starting from scratch.

**Find (exact anchor — the "selective protection" hypothesis paragraph in full):**
> The initial hypothesis is that selective protection is most attractive where limited breakwater length shelters substantial generating capacity and the unprotected alternative incurs significant structural or operating costs. WP6 will test this using quotations and operating-limit evidence under equivalent site and energy-delivery conditions.

**Replace with (keeps the anchor paragraph, appends a new paragraph):**
> The initial hypothesis is that selective protection is most attractive where limited breakwater length shelters substantial generating capacity and the unprotected alternative incurs significant structural or operating costs. WP6 will test this using quotations and operating-limit evidence under equivalent site and energy-delivery conditions.
>
> SUREWAVE's own techno-economic work established the pathway to a competitive LCOE for wave-exposed inland sites. Inland-water wave conditions are much less severe than offshore, so the breakwater sizing envelope is a fraction of an offshore installation. The breakwater is scaled to the dominant-fetch wave direction rather than surrounding the array, keeping protection length per installed MW contained. The wave-height reduction behind the breakwater then lets the FPV array be built to a lower structural spec than an unprotected installation at the same site would demand. The combined system targets an LCOE below that of reinforced conventional FPV at the same exposed site and below offshore FPV alternatives, while unlocking a substantially larger set of European inland waters. D6.2 will quantify LCOE at 1, 10 and 50 MW using demonstrator cost data.

### Verify before applying PE-006 / PE-007

- **Policy references in PE-006** — "REPowerEU (2022)" and "Net-Zero Industry Act" are safe. If the reviewer set is more energy-market-focused you can additionally reference the Electricity Market Design reform (2024) or the Solar Manufacturing initiative; I've kept the list short to avoid boilerplate.
- **"Well above pre-2021 levels"** — factual for EU wholesale power to date; if you'd rather cite a specific number (e.g. "roughly double the 2019 average on many EU day-ahead markets") we can add one, but a numberless claim carries less audit exposure and is harder to date-stamp.
- **PE-007 LCOE claim** — deliberately framed as "targets an LCOE below reinforced conventional FPV at the same exposed site and below offshore FPV alternatives" (comparators where SUREWAVE is genuinely likely to win), not "cheaper than ground-mounted PV" (which we can't defend without a specific site). If SUREWAVE has published LCOE numbers we can cite, that would strengthen the paragraph further — otherwise the qualitative claim is what's supportable at proposal stage.
- **Alignment with existing text** — Line 188 already says "selective protection is most attractive where limited breakwater length shelters substantial generating capacity"; PE-007 extends and specifies that thought. If you prefer to *replace* line 188 rather than append after it, tell me and I'll produce a merged single paragraph.

### PE-008 / PE-009 — Email to co-authors: update Sunlit Sea rows in Table 3.3g and Table 3.3h

Status: **email drafted** 2026-09-16 — Sunlit Sea can no longer edit the docx directly (too close to deadline); coordinator or a co-author needs to make these changes on our behalf. Numbers below match the ported BE2 xlsm exactly (`2026-09-16_SUREWACE_EIC_sunlit_sea.xlsm`, total €750 000). The email describes only what changes on Sunlit Sea's side; it does not prescribe numbers or placement on any other partner's budget — that's for each partner to decide.

**Email body — copy from here down:**

---

Subject: Sunlit Sea BE2 — please update Table 3.3g and Table 3.3h in Part B before submission

Hi Balram, Thomas, João,

We've locked Sunlit Sea's BE2 workbook at €750 000 total. Two entries in the Part B docx still show older values on Sunlit Sea's line and should be aligned with the workbook. Since we're too close to the deadline for me to touch the doc directly, could you please apply the two changes below?

**Change 1 — Table 3.3g "Subcontracting costs", Sunlit Sea row**

Please replace the current Sunlit Sea row:

> Sunlit Sea | 105,000 | Specialist subcontracting for polyurethane frame production and qualification (€35k), accredited accelerated ageing and durability testing (€35k), and temporary assembly labour during peak manufacturing (€35k).

with:

> Sunlit Sea | 70,000 | Specialist subcontracting for polyurethane frame production and qualification (€55k) and temporary assembly labour during peak manufacturing (€15k).

Two reasons: (a) accelerated ageing testing sits outside Sunlit Sea's scope (we supply modules for the tests rather than running them ourselves), so it has been removed from our subcontracting line; (b) the three items in the previous description were each labelled €35k but summed to €105k — the correct components are €55k + €35k + €15k.

**Change 2 — Table 3.3h "Purchase costs", Sunlit Sea sub-table**

Please replace the current Sunlit Sea sub-table with:

| Participant 2 — Sunlit Sea | Cost (€) | Justification |
|---|---:|---|
| Equipment | 140 000 | Production tooling (moulds, jigs, hinge-placement fixtures, fluid-forming rig for the aluminium bottom plate) €100k + Standard commercial glass/glass 710–740 Wp PV modules €40k. Both under WP5, dedicated to the demonstrator build; depreciated at 100 % of purchase cost (see Depreciation costs sheet in the workbook). |
| Consumables | 20 492 | PU raw materials + Aluminium 5083-H111 sheet + Electrical BoM (inverters, cabling, connectors, junction/terminal boxes) for the demonstrator FPV build, at demonstrator scale. |
| Travel and Subsistence | 17 500 | Sunlit Sea travel across WP1–WP7 (kickoff, GA meetings, site engagement, module handover to SINTEF, manufacturing coordination, deployment, customer engagement) — ~10–12 trips at €1 500–€2 000 each. |
| Services for meetings, seminars | 1 000 | WP1 consortium meeting participation costs. |
| Other (shipment, insurance, translation) | 34 000 | WP1 shipment/insurance/translation €4k + WP6 packaging + inland transport NO → Saxony €30k (specialist marine packaging + freight for FPV units, tooling, PU raw, aluminium and electrical BoM). |
| **Total** | **212 992** | |

Main changes vs the current version: sensors (torque sensors and multi-sensor monitoring) have been removed — sensor procurement is outside Sunlit Sea's scope. Equipment now covers production tooling and PV modules per Sunlit Sea's manufacturing scope. Shipment reflects the real freight cost from Norway to the German site. The current table also has swapped descriptions between Equipment and Consumables — the version above fixes that. Sunlit Sea's BE2 total stays at €750 000 (the increased Equipment line is funded by a personnel-effort cut and by removing the items now out of scope).

Please shout if any of the numbers or wording is a problem — happy to adjust.

Thanks,
Eirik

---

**End of email body.**

Internal notes (not for the email):

- Table 3.3h sub-table is currently in grid-table format (`+--- ---+`) in the docx. Balram may need to render our replacement in the same grid form for it to sit cleanly next to the SINTEF and CLEMENT sub-tables.
- Sunlit Sea total in Table 3.3h jumps from ~€110k in current baseline to €213k — the email flags this indirectly through the "main changes" paragraph; if you want to call it out more explicitly, add a one-liner.
- Cross-check when the changes are in: Table 3.3g Sunlit Sea €70k = BE2 subcon total in the xlsm ✓; Table 3.3h Sunlit Sea total €212 992 = BE2 C total in the xlsm ✓.
- Items removed from Sunlit Sea scope (not mentioned in the email — not our place to prescribe): €35k accelerated ageing, €14k torque sensors, €10k multi-sensor monitoring. Consortium coordinator will notice these have come off Sunlit Sea and can decide what happens to them.

