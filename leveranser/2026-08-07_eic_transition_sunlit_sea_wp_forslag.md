---
title: "EIC Transition project structure — Sunlit Sea input"
from: Sunlit Sea AS (Eirik Larsen)
to: SINTEF (Balram Panjwani, coordinator), CLEMENT, EDP, WavEC
date: 2026-08-07
type: internal input note to consortium
basis: consortium meeting 30.07.2026 (see `background/eic/2026-07-31_MOM_EIC_SUREWAVE.txt`) and EDP's stated task interests (see `background/eic/edp_interests.txt`)
---

# EIC Transition project structure — Sunlit Sea input

Sunlit Sea's view of an optimal work-package structure, milestone set, and role split for the EIC Transition proposal that the consortium is preparing. Written as bullet points for Balram (SINTEF) and the other partners to react to. Not a substitute for the formal proposal text — a strategy note that flags what matters most from our side.

Framing from the 30.07.2026 meeting: 5-partner consortium (CLEMENT, Sunlit Sea, EDP, WavEC, SINTEF), €2.5M total + €50k Booster, 100% funding, TRL 6 target, 100-300 kWp pilot at Aguçadoura (Portugal). Assumed duration: 36 months (typical EIC Transition).

## 1. Sunlit Sea's strategic interests

- Advance Sunlit Sea CONNECT gen 2 from TRL 4 (per 2025 accounts) to TRL 6 through offshore validation — a bigger TRL jump than any of the Norwegian nearshore pilots in our pipeline can deliver on their own.
- Generate offshore performance data (structural response, energy production, environmental exposure) that validates the model chain we built in SuRE D6.1/D6.2 (SiSim, thermal CFD, LCA interface). This gives commercial weight to model-driven design.
- Establish an offshore reference installation that strengthens our Norwegian nearshore pipeline (Storavatnet, Gunneklevfjorden, Skien Havn) — offshore Portugal is harsher than our Norwegian sites, so passing there de-risks the commercial rollout at home.
- Position Sunlit Sea as offshore-capable in a market where our closest Norwegian competitors are Fred. Olsen 1848 and Saipem/Moss Maritime, and where Ocean Sun is in liquidity crisis.
- Align our design documentation with DNV FPV standards so that the pilot leaves us "certification-ready" without requiring DNV to be a project partner (see section 5).

## 2. Boundary conditions — what Sunlit Sea delivers and what is outside our domain

- **Sunlit Sea delivers:** the floating photovoltaic units themselves. Design, CAD, manufacturing, factory acceptance testing, electrical interface at the FPV terminal, transportation-ready packaging. Everything from the panel surface down to the aluminium bottom plate, including the CONNECT hinge halves cast into the frame.
- **Outside our domain, but we contribute knowledge and opinions:**
  - Mooring and anchoring — CLEMENT / WavEC / EDP lead.
  - Breakwater design — CLEMENT owns this from Surewave.
  - Site selection, permitting, offshore installation logistics — WavEC / EDP.
  - Grid interface, power management (batteries, load banks, dissipation) — EDP.
  - Offshore field operations (monitoring campaigns, inspections, maintenance visits) — WavEC / EDP. Field trips from Norway to offshore Portugal are prohibitively expensive; we cannot commit resources to on-site operations.
- **Sunlit Sea must receive:** raw and processed monitoring data from the deployed system, in a defined format, on a defined cadence, from day one of operations. Data access is essential — see section 6.

## 3. Work packages — Sunlit Sea's proposed structure

Nine WPs, consistent with EDP's task-numbering interests (T3.2, T4.1, T6.1, T6.2, T7.3, T8.2, T9.1). Sunlit Sea's role indicated per WP.

- **WP1 — Coordination and project management**
  - Lead: SINTEF (natural coordinator from Surewave continuity).
  - Sunlit Sea role: support — represented in the steering group; participate in reviews.

- **WP2 — System requirements, site assessment and permitting**
  - Lead: WavEC or EDP (Portuguese offshore expertise).
  - Sunlit Sea role: contribute FPV-specific requirements (panel dimensions, electrical interface, transport constraints, environmental limits from IEC and DNV-RP-0584).

- **WP3 — Integrated system design (FPV + breakwater + interface)**
  - Co-lead: CLEMENT (breakwater side) and Sunlit Sea (FPV side).
  - Sub-tasks:
    - T3.1: FPV unit design (Sunlit Sea lead) — parametric FreeCAD model, STEP output for FEM, electrical bill of materials.
    - T3.2: Site-specific adaptation of the design (EDP support per stated interest) — grid interface, offshore-load-adapted electrical routing.
    - T3.3: Breakwater design and integration geometry (CLEMENT lead).
    - T3.4: FPV-to-breakwater mechanical interface (co-authored, CLEMENT + Sunlit Sea).

- **WP4 — Numerical modelling and design validation**
  - Lead: SINTEF (hydrodynamic and structural modelling continuity from Surewave).
  - Sub-tasks:
    - T4.1: Grid and operational simulation (EDP support per stated interest).
    - T4.x: FPV-side model chain from SuRE D6.1/D6.2 applied to Aguçadoura load cases (Sunlit Sea heavy contribute) — SiSim structural response, thermal CFD, LCA update.

- **WP5 — Manufacturing, prototyping and factory acceptance**
  - Split lead: Sunlit Sea for the FPV units, CLEMENT for the breakwater. Norwegian casting collaboration (Norsmaterials, from gen 2 development track) plugged in if pricing works.
  - Sunlit Sea deliverable: 100-300 kWp of FPV modules, factory-accepted, packed for shipping to Aguçadoura.

- **WP6 — Site engineering, mooring and electrical infrastructure**
  - Lead: EDP (per T6.1 and T6.2 heavy support interest — EDP's core utility expertise).
  - Sunlit Sea role: support — provide FPV electrical interface spec, review mooring design against FPV load cases.

- **WP7 — Deployment and commissioning**
  - Lead: WavEC (offshore ops).
  - T7.3: EDP lead (per stated interest — likely grid connection or power-management commissioning).
  - Sunlit Sea role: minimal on-site presence (one commissioning visit maximum, budget permitting) — deliver factory-verified units that plug into the offshore work.

- **WP8 — Operation, monitoring and data collection**
  - Lead: WavEC (offshore ops) — WavEC handles physical monitoring campaigns; SINTEF supports on data processing.
  - T8.2: EDP lead (per stated interest — grid-side power measurement).
  - Sunlit Sea role: **receive processed data** on a defined cadence and format, do not run field operations. Contribute the FPV-instrumentation specification (which sensors on which parts) at project start so instruments are installed at manufacturing time. See section 4 for data delivery structure.

- **WP9 — Exploitation, dissemination and commercialization**
  - Lead: CLEMENT or EDP (T9.1 EDP lead per stated interest).
  - Sunlit Sea sub-task: commercial rollout of gen 2 in Northern European / Norwegian market, feeding Aguçadoura performance data into our nearshore pipeline sales.

## 4. Milestones — as few as CINEA will accept

Deliberately minimalist. Every milestone locked into the grant agreement is hard to move after signature (CINEA does not accept date changes lightly), so fewer milestones means less exposure to schedule risk. Proposed set: **four milestones**.

- **MS1 — Integrated system design frozen (approximately M12)**
  - Trigger for hardware procurement and manufacturing commitment.
  - Sunlit Sea deliverable inside MS1: FPV detailed design frozen; full CAD released.

- **MS2 — System delivered to site, ready for offshore installation (approximately M20)**
  - Trigger for offshore installation activities.
  - Sunlit Sea deliverable inside MS2: FPV modules factory-accepted and physically at the Aguçadoura staging area.

- **MS3 — System commissioned and producing (approximately M24)**
  - Trigger for the operational phase. FPV energy production and monitoring streams online.

- **MS4 — Final validation, exploitation plan and closeout (approximately M36)**
  - Trigger for grant closeout. Includes DNV-alignment audit output (see section 5).

Four is our best estimate of the CINEA minimum for a €2.5M, TRL 4 → 6, 36-month project. If Balram believes CINEA will insist on more, we would rather add one at MS3.5 (extended-operation checkpoint, e.g. M30) than at M6 or M9 — early milestones in a demonstration project are the ones that get in the way when technical iteration is needed.

## 5. DNV alignment — aim for "certification-ready", not certification

- Relevant DNV documents:
  - **DNV-RP-0584** — Recommended Practice: Design, development and operation of floating solar photovoltaic systems. Sunlit Sea's design methodology has been verified against this since 2022.
  - **DNV-ST-C108** — Structural design of floating photovoltaic units. New support standard released May 2026.
  - **DNV-ST-E309** — Mooring of floating photovoltaic units. New support standard released May 2026.
- Rationale for "certification-ready" and not full certification:
  - Full certification requires DNV to be involved as an accredited party throughout design and testing. That would add a partner, dilute the €2.5M budget, and lengthen review cycles.
  - "Certification-ready" is much cheaper: we structure our documentation, testing regime and data collection so that a future DNV certification project can be built directly on top of the EIC Transition outputs, without re-doing work.
- Concrete mapping to project WPs:
  - WP3 (design) documentation follows the format DNV-ST-C108 expects for structural documentation. Design load cases explicitly cite DNV-RP-0584 wave/wind exposure categories.
  - WP4 (modelling) validation report demonstrates that the numerical predictions cover the DNV-ST-C108 load matrix.
  - WP6 (mooring) design follows DNV-ST-E309 principles — good hygiene regardless of certification aim, and if EDP/WavEC lead here they already work to these norms.
  - WP8 (monitoring) instrumentation plan captures the parameters DNV-ST-C108 requires for in-service verification (mooring loads, structural strains, motion, environmental exposure).
  - WP9 (exploitation) sub-task: prepare a "certification-readiness" package as a deliverable to CINEA and to third-party marketing use. Investor-relevant.
- What this is not:
  - DNV is not a project partner. We do not spend budget on DNV review cycles during the project.
  - The pilot does not receive a DNV certificate at the end. It receives DNV-alignment documentation.

## 6. Data access, IP and exploitation

- Data delivery to Sunlit Sea (must be in the consortium agreement):
  - Sunlit Sea receives raw and processed monitoring data for the FPV side of the system, on a defined cadence (proposed: raw daily, processed weekly), in a defined format, from day one of operations.
  - No embargo on Sunlit Sea's use of the data in commercial presentations, investor communications and marketing.
  - Data delivery is a WP8 obligation on WavEC/SINTEF/EDP, not conditional on visits.
- IP:
  - Sunlit Sea retains full ownership of the FPV design (gen 2 CONNECT and its improvements). Consortium receives usage rights inside the project only.
  - CLEMENT retains ownership of the breakwater.
  - The integrated FPV+breakwater interface is jointly owned by Sunlit Sea and CLEMENT.
- Exploitation split:
  - Sunlit Sea: Northern Europe / Norway first-user rights on the integrated concept.
  - EDP: Portugal / Iberia.
  - CLEMENT: global for breakwater-related deployments.
  - Booster Grant (€50k) allocation: propose it goes to dissemination activities that support commercial reach (industry conferences, customer demonstrations at Aguçadoura, communications materials).

## 7. Open questions to raise with Balram / consortium

- WP3 lead structure: single-lead with CLEMENT or explicit co-lead with Sunlit Sea for the FPV side? Sunlit Sea prefers co-lead or a split into WP3a (FPV) and WP3b (breakwater).
- Milestone count: comfortable with four? Or does Balram expect CINEA to want more? If more, the M30 extended-operation checkpoint is our next preferred addition, not an early-phase one.
- Scale: 100 vs 200 vs 300 kWp. Sunlit Sea's view: 200 kWp is a good balance between TRL 6 credibility (multi-module matrix effects, realistic power generation) and budget headroom.
- Sunlit Sea on-site presence: one FPV commissioning visit in WP7 budgeted, no others. Any additional visits would need to be justified by unexpected issues and covered from contingency, not baseline budget.
- Norwegian nearshore knowledge transfer: how do we formalise the flow of Aguçadoura pilot data into Sunlit Sea's Norwegian projects, within the consortium IP framework? A short annex to the consortium agreement is probably enough.
- DNV-alignment scope: is any partner already working towards DNV-ST-C108 / DNV-ST-E309 alignment in ongoing work? If so, we can piggyback on the format. If not, we propose Sunlit Sea leads the documentation-alignment sub-task in WP3.
