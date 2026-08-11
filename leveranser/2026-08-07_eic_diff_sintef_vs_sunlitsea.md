---
title: "EIC Transition WP structure — diff assessment: SINTEF proposal vs Sunlit Sea input"
from: Sunlit Sea AS (Eirik Larsen)
date: 2026-08-07
type: internal assessment note
compares:
  - SINTEF (Balram Panjwani): `background/eic/2026-08-07_sintef.md` (converted from `.docx`)
  - Sunlit Sea (Eirik Larsen): `leveranser/2026-08-07_eic_transition_sunlit_sea_wp_forslag.md`
---

# EIC Transition WP structure — diff assessment

Assessment of how SINTEF's preliminary WP/task structure (2026-08-07) compares with Sunlit Sea's input note (2026-08-07). Purpose: identify where the two documents agree, where they diverge, and what Sunlit Sea should push for in the next round of consortium discussion.

Both documents propose nine WPs, but the *content* of each WP differs. SINTEF's numbering aligns with the task interests EDP already stated (T3.2, T4.1, T6.1, T6.2, T7.3, T8.2, T9.1 — all fit SINTEF's structure). Sunlit Sea's numbering was invented independently and does not map cleanly to EDP's interests. This is the single most important observation from the diff.

## Structural comparison (per WP)

| WP | SINTEF proposal | Sunlit Sea proposal | Match |
|----|-----------------|---------------------|-------|
| WP1 | Project Management + Innovation Management | Coordination and project management | Partial — SINTEF adds Innovation/Commercialization management as a task, Sunlit Sea did not |
| WP2 | Design Optimization (requirements, breakwater, FPV platform, mooring) | System requirements, site assessment and permitting | Diverges — SINTEF puts *design* here, Sunlit Sea puts *requirements + permitting* here |
| WP3 | Design and Performance Assessment (numerical modelling, energy yield, model development) | Integrated system design (FPV + breakwater + interface) | Diverges — SINTEF puts *modelling* here, Sunlit Sea puts *design* here |
| WP4 | Instrumentation and Monitoring System Development | Numerical modelling and design validation | Diverges — SINTEF puts *instrumentation* here, Sunlit Sea puts *modelling* here |
| WP5 | Demonstrator Construction and Integration (manufacturing, integration, factory testing) | Manufacturing, prototyping and factory acceptance | Match — same content, minor phrasing differences |
| WP6 | Demonstration Site Preparation, Permitting and Deployment (site, permits, EIA, installation) | Site engineering, mooring and electrical infrastructure | Partial — SINTEF's WP6 is broader (also permits, EIA, deployment planning); Sunlit Sea's WP6 is narrower (site engineering + mooring + electrical only, deployment was in WP7) |
| WP7 | Operational Validation and Data Collection | Deployment and commissioning | Diverges — SINTEF puts *validation/data* here, Sunlit Sea puts *deployment* here |
| WP8 | Environmental, Economic and Replication Assessment (env, techno-economic) | Operation, monitoring and data collection | Diverges — SINTEF puts *assessment* here, Sunlit Sea puts *monitoring/ops* here |
| WP9 | Exploitation, Business Development and Dissemination | Exploitation, dissemination and commercialization | Match — same content and intent, SINTEF adds Booster Grant sub-task explicitly |

Both structures cover the same total scope, but the partitioning is different. Sunlit Sea's structure grouped by *project lifecycle phase* (requirements → design → modelling → build → deploy → operate → assess → exploit). SINTEF's structure grouped by *technical activity* (design → modelling → instrumentation → build → site → validation → assessment → exploit). SINTEF's approach is more typical for HE demonstrator projects.

## EDP alignment check

EDP has stated interest in: T9.1 (lead), T8.2 (lead), T7.3 (lead), T6.1/T6.2 (heavy support), T4.1 (support), T3.2 (support).

- Against SINTEF structure:
  - T9.1 Business Model Development — natural fit for EDP as utility ✓
  - T8.2 Techno-Economic Analysis (LCOE, CAPEX/OPEX) — perfect fit for EDP ✓
  - T7.3 Energy Performance Assessment — good fit for EDP (grid/production side) ✓
  - T6.1 Site Selection / T6.2 Permitting — Portuguese utility, natural fit ✓
  - T4.1 Monitoring Requirements — reasonable, EDP knows what grid ops need ✓
  - T3.2 Energy Yield Assessment — good fit for EDP ✓
- Against Sunlit Sea structure: EDP interests do not match cleanly (numbering conflict).

**Conclusion:** SINTEF's numbering is what the consortium is converging on. Sunlit Sea should accept SINTEF's structure as the working baseline and re-express our input against it, rather than push our own numbering.

## What SINTEF got right that Sunlit Sea missed

- **T1.3 Innovation and Commercialization Management** — dedicated task for IP management, freedom-to-operate, exploitation roadmap. Important for EIC Transition (business focus). Sunlit Sea's WP1 did not have this.
- **T2.2 Circular material integration** in breakwater optimization — sustainability angle we didn't touch. Aligns with EU Green Deal narrative.
- **T3.3 Model Development** with real-time monitoring framework and model validation methodology as an explicit output — Sunlit Sea's SuRE model chain plugs cleanly in here.
- **T6.2 Permitting** with an explicit list of permits (maritime occupation, environmental, port authority, navigation safety, temporary offshore installation, electrical). Concrete and CINEA-friendly. Sunlit Sea lumped permitting into a broader WP2.
- **T6.3 Environmental and Social Impact Assessment** — separate task for EIA including fisheries consultation and visual impact. CINEA cares about this. Sunlit Sea did not call it out.
- **T6.4 Demonstrator Installation Planning** with HSE procedures and emergency response — necessary for offshore work. Sunlit Sea did not detail this.
- **T7.1 Fatigue assessment** as part of structural validation — we mentioned load and motion but not fatigue explicitly.
- **T9.4 Booster Grant Activities** as its own task — cleaner than absorbing €50k allocation into another WP.

## What Sunlit Sea has that SINTEF missed

- **DNV alignment (RP-0584, ST-C108, ST-E309)** — not called out anywhere in SINTEF's structure. Sunlit Sea's proposal makes "certification-ready" a strategic goal. Should be added as either:
  - Cross-cutting theme referenced in WP2 (design) and WP4 (instrumentation), or
  - Sub-task under T2.1 Requirement Definition (design against DNV standards), plus a documentation deliverable under T9.3 or T9.4.
- **Milestone structure** — SINTEF's document has no milestones at all. Sunlit Sea proposed four (MS1 design frozen ~M12, MS2 delivered ~M20, MS3 commissioned ~M24, MS4 closeout ~M36), with explicit rationale that CINEA does not accept date changes after signature so fewer is safer. Sunlit Sea should push its 4-milestone set into the working structure now while it is still soft.
- **Data delivery model to partners** — SINTEF's T4.3 Data Acquisition Platform specifies a dashboard and cloud storage, but nothing about who gets what data on what cadence, and whether embargo applies. Sunlit Sea should push: raw data daily, processed weekly, no embargo on commercial use by any partner. Sunlit Sea specifically needs this because we cannot field-visit and rely entirely on remote data.
- **Explicit boundary conditions** for Sunlit Sea — what we deliver (the FPV floating unit, panel surface down to bottom plate including hinges) vs. what is outside our domain (mooring, breakwater, site, grid, offshore field ops). Should be reflected in task-level lead assignments (see next section).
- **Booster Grant allocation guidance** — Sunlit Sea suggested using it for dissemination that supports commercial reach. SINTEF put it under T9.4 but did not specify direction.
- **IP and geographic exploitation split** — Sunlit Sea proposed Norway/Northern Europe first-user rights, EDP for Iberia, CLEMENT global for breakwater deployments. SINTEF's T1.3 covers IP management generically; the geographic split needs to be added at consortium agreement level.

## Task-level lead assignments Sunlit Sea should propose (in SINTEF's numbering)

SINTEF's document does not assign leads. Sunlit Sea should propose the following, consistent with our boundary conditions (we deliver the FPV unit, we contribute knowledge on mooring / breakwater / site but do not lead them):

- **WP1 Project Management** — SINTEF lead.
  - T1.1 Coordination: SINTEF.
  - T1.2 Risk and Quality: SINTEF.
  - T1.3 Innovation and Commercialization Management: CLEMENT or SINTEF; Sunlit Sea contribute.
- **WP2 Design Optimization**
  - T2.1 Requirement Definition: co-authored by all partners; convener SINTEF. Sunlit Sea explicitly contributes DNV-alignment requirements (RP-0584 / ST-C108 / ST-E309) here.
  - T2.2 Floating Breakwater Optimization: **CLEMENT lead** (their design).
  - T2.3 FPV Platform Design: **Sunlit Sea lead** — this is our core deliverable.
  - T2.4 Mooring and Anchoring System Design: **WavEC or EDP lead**; Sunlit Sea contribute FPV-load boundary conditions only.
- **WP3 Design and Performance Assessment**
  - T3.1 Numerical Modelling: **SINTEF lead** (hydrodynamic and structural, continuity from Surewave).
  - T3.2 Energy Yield Assessment: **EDP support** (per stated interest); Sunlit Sea contribute FPV thermal-CFD outputs from SuRE model chain.
  - T3.3 Model Development: **SINTEF lead**; Sunlit Sea heavy contribute (SuRE D6.1/D6.2 model chain plugs in here).
- **WP4 Instrumentation and Monitoring System Development**
  - T4.1 Monitoring Requirements: **EDP support**; Sunlit Sea contribute FPV instrumentation spec (which sensors on which FPV parts).
  - T4.2 Sensor System Development: **SINTEF or WavEC lead**.
  - T4.3 Data Acquisition Platform: **SINTEF lead**; Sunlit Sea contribute FPV data schema and require data delivery terms in consortium agreement.
- **WP5 Demonstrator Construction and Integration**
  - T5.1 Prototype Manufacturing: split — **Sunlit Sea lead for Floating structures** (FPV units), **CLEMENT lead for Breakwater components**, **WavEC or CLEMENT lead for Mooring components**.
  - T5.2 PV and Dummy Module Integration: **Sunlit Sea lead** (integration of PV modules into our float units).
  - T5.3 System Assembly and Factory Testing: **Sunlit Sea lead for FPV factory acceptance**; CLEMENT for breakwater factory acceptance.
- **WP6 Site, Permitting, Deployment** — **WavEC or EDP lead throughout**. Sunlit Sea outside domain, supports on FPV-specific input where asked.
  - T6.5 Offshore Installation: WavEC / EDP lead. Sunlit Sea presence limited to one commissioning visit maximum, budget permitting.
- **WP7 Operational Validation and Data Collection** — **WavEC lead**; SINTEF supports on data analysis; Sunlit Sea receives data.
  - T7.3 Energy Performance Assessment: **EDP lead** (per stated interest).
  - T7.4 Model Validation: **SINTEF lead**; Sunlit Sea heavy contribute (validating SuRE model chain predictions against real data).
- **WP8 Environmental, Economic and Replication Assessment**
  - T8.1 Environmental Assessment: **SINTEF or WavEC lead**.
  - T8.2 Techno-Economic Analysis: **EDP lead** (per stated interest).
- **WP9 Exploitation, Business Development and Dissemination**
  - T9.1 Business Model Development: **EDP lead** (per stated interest); Sunlit Sea contribute for Northern European / Norwegian market.
  - T9.2 Investor and Stakeholder Engagement: **shared**.
  - T9.3 Dissemination and Communication: **CLEMENT or SINTEF lead**; add DNV-alignment documentation as a specific deliverable here.
  - T9.4 Booster Grant Activities: **CLEMENT lead**; use budget for dissemination that supports commercial reach across Portugal, Norway, Germany.

## Recommended next steps for Sunlit Sea

- Send an update note to Balram accepting SINTEF's WP numbering as the working baseline, and expressing our input against it (the four items below).
- Push our four proposals hard while the structure is still soft:
  1. DNV alignment as strategic theme (add as sub-tasks in T2.1 and T9.3).
  2. Milestone set reduced to four (MS1 design M12, MS2 delivered M20, MS3 commissioned M24, MS4 closeout M36).
  3. Data delivery terms specified in T4.3 (raw daily, processed weekly, no embargo).
  4. Boundary conditions and task-level leads assigned as in the section above.
- Escalate our on-site presence constraint: budget for one commissioning visit, not multiple field campaigns. Sunlit Sea depends on remote data delivery.
- Confirm geographic IP/exploitation split at consortium agreement level (Sunlit Sea → Northern Europe / Norway; EDP → Iberia; CLEMENT → breakwater global).
