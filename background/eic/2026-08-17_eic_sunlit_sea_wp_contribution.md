---
title: "EIC SUREWAVE — Sunlit Sea WP inputs for the proposal draft"
from: Sunlit Sea AS (Eirik Larsen)
to: SINTEF (Balram Panjwani, coordinator) and consortium partners
date: 2026-08-17
type: Contribution to proposal draft — WP-level inputs ready to insert into `EIC_SUREWAVE_Proposal.docx`
basis: >
  Balram's request 2026-08-14 (each partner to write their WP inputs, milestones and deliverables).
  WP structure per `background/eic/2026-08-10_contributing_tasks_wp_documents.md`.
  Sunlit Sea's earlier internal position paper: `background/eic/2026-08-07_eic_transition_sunlit_sea_wp_forslag.md`.
  Tech context from Sunlit Sea Gen 2 development (`gen2/norsmaterials_brief.md`) and SuRE D6.1/D6.2 model chain (`sure/deliverables/`).
---

# Sunlit Sea contribution — text for insertion into the proposal

This document holds Sunlit Sea's inputs to the WP structure Balram circulated, organised WP-by-WP so the coordinator can paste each block into the corresponding cell of the proposal template. Sections are structured to mirror `background/eic/2026-08-10_contributing_tasks_wp_documents.md`.

## About Sunlit Sea and what we bring to the consortium

Sunlit Sea AS is a Norwegian FPV company designing, manufacturing and deploying floating photovoltaic units engineered for a 25-year aquatic operating life. The company's first-generation product is deployed at commercial sites; the current focus is Sunlit Sea CONNECT gen. 2 — a full redesign that decouples the float from the PV module by cast-PU-frame around standard commercial 710–740 Wp panels on a 0.8 mm aluminium (5083-H111) bottom plate. Prototype 4 is next; pilot deployment is planned in H1 2026.

Sunlit Sea is a partner in Horizon Europe SuRE (WP6), where D6.1 (Model chain description) has been delivered and D6.2 (Multi-domain design screening) is in preparation. The D6.1 model chain covers pressing simulation, structural response (SiSim), thermal CFD and life-cycle assessment — the same numerical toolset that will be used to validate the demonstrator design in the present project.

Design methodology is verified against DNV-RP-0584 (Design, development and operation of floating solar photovoltaic systems) and will be extended in the present project to align with the new DNV-ST-C108 (structural) and DNV-ST-E309 (mooring) standards released in May 2026.

Sunlit Sea's role in this proposal is the FPV side of the integrated SUREWAVE system: the floating photovoltaic units themselves — design, CAD, manufacturing, factory acceptance, electrical interface at the FPV terminal, packaging for shipping. Everything from the panel surface down to the aluminium bottom plate, including the CONNECT hinge halves cast into the frame. Site engineering, mooring, offshore installation logistics, grid interface and offshore field operations are led by other consortium partners with Sunlit Sea in a supporting role.

---

## WP1 — Project Management and Innovation Management (L: SINTEF)

**Sunlit Sea role: participant, all tasks.**

Sunlit Sea will be represented in the Steering Committee and Technical Committee, participate in the monthly WP2 progress meetings, and contribute to all consortium-level deliverables. On the IPR/CA side (Task 1.4), Sunlit Sea will contribute the FPV-side IP register (background IP: Sunlit Sea CONNECT gen 2 design, CONNECT hinge geometry, the aluminium/PU float architecture; foreground IP: the site-adapted variant, offshore-load-adapted electrical routing) and the exploitation split that mirrors the Northern-European rollout pipeline.

---

## WP2 — Design Optimization of the SUREWAVE FPV System (L: Sunlit Sea)

### Objectives

WP2 defines the FPV + breakwater + mooring system configuration for the demonstrator. The specific demonstration site is being evaluated by the consortium (approximately seven candidate sites under review); site selection is completed under WP6 T6.1. WP2 works to a site-envelope specification that spans the candidate sites and freezes to the selected site as T6.1 concludes. Starting from the SUREWAVE breakwater concept and the Sunlit Sea CONNECT gen. 2 FPV platform, the WP will:

- Translate site-envelope metocean conditions and demonstration objectives into a complete system requirements specification (T2.1).
- Optimise the floating breakwater configuration for the demonstrator scale and selected site (T2.2, Clement lead).
- Deliver an installation-ready FPV platform design integrating standard commercial PV modules, dummy modules for load-representative fill, and the connection interface to the breakwater (T2.3).
- Deliver a site-specific mooring and anchoring design meeting DNV-ST-E309 principles and coordinated with the breakwater layout (T2.4, Clement/WavEC lead).

The WP outputs are frozen design documentation that unlocks procurement and manufacturing under WP5.

### Task 2.1 — Requirement Definition (L: Sunlit Sea; P: All)

Task 2.1 consolidates the demonstration objectives, site conditions, regulatory requirements and stakeholder constraints into a system-level requirements specification that all downstream tasks build on. Sunlit Sea leads the task and coordinates inputs from WavEC/EDP (site and grid), Clement (breakwater interface constraints) and SINTEF (numerical-model input requirements).

The requirements specification covers: (i) demonstrator size and configuration targets (50–300 kWp band, matrix layout options — final size determined by site selection and consortium decisions on operational testing depth, not by the Sunlit Sea budget envelope); (ii) FPV module dimensions and electrical interface constraints (standard commercial 710–740 Wp panels, 2384 × 1303 mm footprint); (iii) environmental design envelopes spanning the candidate demonstration sites (waves, wind, current, temperature, salinity, UV) mapped to DNV-RP-0584 exposure categories, tightened to the selected site as T6.1 concludes; (iv) mechanical interface to the breakwater and mooring system; (v) transport and installation constraints from Sunlit Sea's Norwegian manufacturing base to the selected site; (vi) monitoring and instrumentation requirements feeding WP4; (vii) certification-alignment requirements against DNV-ST-C108 and DNV-ST-E309 for a "certification-ready" documentation set at project end.

The task delivers the system requirements document (D2.1) at M6.

### Task 2.2 — Floating Breakwater Optimization (L: Clement)

Clement leads the breakwater design refinement. Sunlit Sea contributes the FPV-side interface requirements: the mechanical connection geometry (CONNECT hinge halves cast into the FPV frame edge), the acceptable relative-motion envelope between FPV and breakwater under the design sea states, and the electrical routing constraints that the breakwater-to-shore path must accommodate.

### Task 2.3 — FPV Platform Design (L: Sunlit Sea; P: SINTEF, EDP)

Task 2.3 delivers the detailed design of the demonstrator's floating photovoltaic platform, ready for procurement and manufacturing under WP5.

The design starts from the Sunlit Sea CONNECT gen. 2 architecture: a modular unit with a 0.8 mm aluminium (5083-H111) bottom plate, a cast polyurethane frame around each standard commercial PV panel (710–740 Wp, 2384 × 1303 mm), interior PU-foam infill, and PU-foam CONNECT connector rods that join neighbouring units on all four sides. The panel sits at a 2° tilt with the lowest edge 6 cm above the water surface.

For the demonstrator the design will be site-specifically adapted along four dimensions (site frozen at T6.1 completion):

- **Array layout.** Sunlit Sea will produce parametric FreeCAD models of alternative matrix configurations (rectangular, circular, staggered), export STEP geometries to SINTEF for coupled hydrodynamic/structural simulation in Task 3.1, and iterate the layout to balance hydrodynamic performance (behind the breakwater), installation feasibility, maintenance accessibility, and mooring-load distribution. The chosen layout is frozen at M12.
- **Mixed operational/dummy modules.** Per the consortium decision (MoM 30.07.2026), the demonstrator will include both operational PV modules for energy-generation testing and dummy modules matched in mass and aero/hydrodynamic characteristics. Sunlit Sea will specify the dummy-module design so that it presents equivalent mechanical loads to the float and connection system, while allowing water-ingress and reliability sensors to be embedded at defined locations.
- **Electrical interface and offshore routing.** Sunlit Sea delivers the FPV-side electrical bill of materials — string configuration, module-to-module connectors, terminal box, cable exit — engineered for the offshore-load-adapted electrical routing agreed with EDP under WP3 T3.2 and WP6.
- **Instrumentation carriers.** The FPV design incorporates mounting and cable-routing provisions for the sensor set defined in T4.1, so that instruments are installed at manufacturing time rather than retrofitted at deployment.

The design methodology reuses the model chain developed and validated in the Horizon Europe SuRE D6.1 deliverable: parametric FreeCAD → STEP export → SINTEF-side coupled hydrodynamic-structural FEM (Task 3.1) → Sunlit Sea thermal CFD and structural (SiSim) analyses → LCA update. The multi-domain screening approach developed in D6.2 will be applied to compare alternative FPV geometries against site-specific load cases.

Design documentation is structured to comply with DNV-ST-C108 for the FPV structural side, so that a future full DNV certification project can build directly on the T2.3 output.

Deliverables: D2.3 FPV platform detailed design report (M12, includes STEP models, structural drawings, electrical BoM, instrumentation mounting spec).

### Task 2.4 — Mooring and Anchoring System Design (L: Clement/WavEC)

Clement and WavEC lead this task. Sunlit Sea contributes the FPV-side load cases (motions, mooring-attachment-point loads) derived from Task 2.3 and Task 3.1, and reviews the mooring design against the FPV structural envelope. Sunlit Sea recommends the mooring documentation follow DNV-ST-E309 principles to support the project-end certification-ready documentation package.

---

## WP3 — Design and Performance Assessment (L: SINTEF/EDP)

**Sunlit Sea role: participant in T3.2 (Energy Yield); model-chain contribution to T3.1.**

### Task 3.1 — Numerical Modelling (L: SINTEF/WavEC)

SINTEF leads coupled hydrodynamic and structural simulation. Sunlit Sea contributes the FPV-side model chain established in SuRE D6.1: SiSim structural-response model for the aluminium/PU float unit, thermal CFD for surface-to-water heat transfer, and LCA update. These models complement the SINTEF/WavEC OpenFOAM+SPH+MoorDyn framework by providing the FPV-side response characteristics needed as inputs (mass distribution, stiffness, hydrodynamic added-mass estimates for the unit and matrix) and by consuming the SINTEF outputs (loads at the mooring attachment and inter-unit connectors, motion time histories) as boundary conditions for Sunlit Sea's own structural and thermal analyses.

The site-specific load cases (extreme sea state, fatigue-driving operational sea state, thermal peak day) are agreed with SINTEF and executed in parallel: SINTEF for the system-level coupled analysis, Sunlit Sea for the unit-level structural and thermal analysis. The results feed WP2 T2.3 design iteration. Load cases are initially evaluated across the candidate-site envelope and tightened to the selected site as T6.1 concludes.

### Task 3.2 — Energy Yield Modelling and Assessment (L: EDP; P: Sunlit Sea)

EDP leads energy yield modelling. Sunlit Sea contributes:

- Panel-level electrical performance model for the standard commercial 710–740 Wp modules used in the demonstrator (temperature coefficients, low-light behaviour, spectral response).
- Thermal boundary conditions from the SuRE D6.1 thermal CFD chain: cell-temperature distributions under representative site conditions, quantifying the wind-cooling advantage of the offshore location and the effect of the 6 cm PV-to-water distance and 2° tilt.
- Salt-deposition and soiling assumptions calibrated against Sunlit Sea's Norwegian nearshore operational data.
- The comparison basis: energy yield of the demonstrator against the Sunlit Sea Norwegian pipeline projects (Skien Havn, Storavatnet, Gunnekleivfjorden), so the demonstrator data has a direct commercial reference.

### Task 3.3 — Model Development (L: SINTEF/EDP)

Sunlit Sea's contribution is limited: providing the physical baseline for the FPV-side machine-learning features (which sensor signals correspond to which failure modes) based on Gen 1 field-return data and Gen 2 lab-test data.

---

## WP4 — Instrumentation and Monitoring System Development (L: WavEC)

### Task 4.1 — Monitoring Requirements (L: Sunlit Sea; P: EDP, WavEC, SINTEF)

Sunlit Sea leads Task 4.1: defining the instrumentation specification for the demonstrator so that instruments are installed at manufacturing time (WP5) and the data collected during operation (WP7) directly validates the design assumptions from WP2/WP3 and supports the reliability assessment in T7.2.

The instrumentation specification covers:

- **Structural monitoring.** Strain gauges at critical points of the PU frame and aluminium bottom, load cells at the CONNECT hinge attachments (FPV-to-FPV and FPV-to-breakwater), IMUs on selected units to capture 6-DoF motion, mooring-line load cells (coordinated with WP2 T2.4).
- **Environmental monitoring.** Wave, wind, current and irradiance sensors coordinated with the site campaign of WavEC/EDP. Panel-surface and water-side temperature sensors on selected units to close the thermal loop against the D6.1 CFD chain.
- **Reliability monitoring.** Water-ingress sensors embedded in the dummy modules and at defined risk points in the operational modules; corrosion coupons at representative locations; junction-box humidity monitoring. Rationale: our Gen 2 water-ingress test on Prototype 3 identified specific interface regions to instrument.
- **Energy performance monitoring.** DC-side per-string current/voltage; module-level monitoring on a defined subset for spatial performance mapping; AC-side power quality at the inverter output (coordinated with EDP).

Sensor selection prioritises rugged, salt-water-tolerant instruments with proven track records in offshore or marine service, and standard interfaces (Modbus RTU, IEC 61850, 4-20 mA) compatible with the WavEC data-acquisition platform in T4.3. Sampling rates and data-retention policies are specified so that the data volume is manageable while preserving the frequency content needed for fatigue analysis (T7.1) and reliability assessment (T7.2).

The instrumentation specification is frozen at M9 to feed procurement in WP5.

Deliverable: D4.1 Instrumentation specification report (M9).

### Tasks 4.2, 4.3 — WavEC / SINTEF lead

Sunlit Sea contributes the FPV-side interface documentation (sensor mounting drawings, cable-routing, terminal-box specifications) so WavEC's sensor integration in T4.2 is drop-in during manufacturing. On T4.3, Sunlit Sea contributes data-format requirements for the Sunlit Sea-side ingestion of processed data (see WP7 data-delivery obligation).

---

## WP5 — Demonstrator Construction and Integration (L: Clement)

### Task 5.1 — Prototype Manufacturing Breakwater (L: Clement)

Not Sunlit Sea's scope.

### Task 5.2 — Prototype Manufacturing PV module (L: Sunlit Sea; P: Clement, WavEC, EDP)

Sunlit Sea leads the manufacturing of the FPV units for the demonstrator: 50–300 kWp of Sunlit Sea CONNECT gen. 2 modules, factory-verified, packed for shipping to the demonstration-site staging area. The final size within the 50–300 kWp band is not fixed at this point in the application — it is settled during WP6 T6.1 site selection and consortium agreement on operational testing depth. The Sunlit Sea T5.2 budget is set on the basis of raising the FPV unit from TRL 4/5 to TRL 6, not on the number of kWp built (see the cost estimate section).

The manufacturing scope covers:

- **Aluminium bottom plates** (0.8 mm 5083-H111, flat as the confirmed base case; the pressed-cup alternative from the D6.1 hydroforming pipeline is retained as a fall-back option to be resolved by D6.2 output before manufacturing starts).
- **Cast polyurethane frames** produced either at Sunlit Sea's Norwegian in-house casting facility (using 3D-printed moulds; currently ramping through the Norsmaterials collaboration) or at the Tongge (Weihai, China) subcontractor already qualified for Prototype 3. Sourcing decision is made at M12 based on lead-time and cost.
- **Interior PU-foam infill** cast in place with the geometry defined in T2.3.
- **Standard commercial PV panels** (710–740 Wp, 2384 × 1303 mm) procured from qualified suppliers and integrated into the cast PU frames at Sunlit Sea's assembly facility.
- **Dummy modules** with matched mass and aero/hydrodynamic characteristics, produced through the same aluminium/PU cycle without the operational PV lamination.
- **CONNECT hinge halves** cast into the frame edges during PU casting, matching the revised Surewave-derived geometry.
- **PU-foam connector rods** for inter-module connection.
- **Instrumentation** installed at manufacturing time per the T4.1 specification.

Manufacturing quality is assured by the T5.5 factory-acceptance protocol. All FPV units are delivered to the demonstration site at MS2 (approximately M20), ready for offshore installation.

### Task 5.3 — System Integration (L: EDP; P: Sunlit Sea, WavEC)

Sunlit Sea contributes the FPV-side integration documentation: installation drawings for the FPV-to-breakwater mechanical interface, electrical integration procedures at the FPV terminal, and safety-critical procedures for handling the FPV units on-site. Sunlit Sea's on-site presence during integration is minimised — one commissioning visit is planned (see T5.5 and MS2/MS3).

### Task 5.5 — Acceptance and Factory Testing (L: Sunlit Sea; P: All)

Sunlit Sea leads factory acceptance testing (FAT) of the FPV units before shipping to the demonstration site. FAT protocol covers:

- **Structural inspection** — dimensional check against T2.3 drawings, PU-frame integrity, aluminium bottom flatness and edge quality, CONNECT hinge geometry.
- **Electrical acceptance** — DC insulation, string continuity, panel electroluminescence for micro-crack screening, terminal-box IP-rating verification.
- **Water-ingress test** — an accelerated version of the Prototype 3 water-ingress protocol on a sample of production units.
- **Instrumentation acceptance** — verify each installed sensor reads within calibration on a defined stimulus.
- **Documentation package** — each unit ships with a serialised acceptance record.

Deliverable: D5.5 Factory acceptance test report (M20).

---

## WP6 — Demonstration Site Preparation, Permitting and Deployment (L: WavEC)

**Sunlit Sea role: minimal, per the offshore-Portugal-from-Norway logistics constraint.**

### Tasks 6.1, 6.2 (Regulatory Compliance) — WavEC lead

Not Sunlit Sea's scope. Sunlit Sea will review permit-application documentation touching the FPV design (structural safety, electrical safety, environmental performance) and respond to authority queries in that domain.

### Task 6.2 (Installation Planning) — WavEC/EDP/Sunlit Sea

Sunlit Sea contributes the FPV-side installation methodology: handling procedures at the staging area, lifting and floating-launch procedures, on-water assembly sequence for the CONNECT inter-module connections, electrical hook-up procedure at the string terminals. Sunlit Sea coordinates with WavEC/EDP on vessel and equipment requirements so the FPV design's transport and installation constraints (from T2.3) are respected in the installation plan.

### Task 6.3 — Offshore Installation and Commissioning (L: Clement; P: All)

Sunlit Sea provides one on-site technical presence during the FPV-installation window and remote support throughout. Post-installation commissioning of the FPV strings is coordinated with EDP (grid/power-management side).

---

## WP7 — Operational Validation and Data Collection (L: SINTEF; T7.3 L: EDP)

### Task 7.1 — Structural Validation (L: SINTEF; P: All)

Sunlit Sea contributes analysis of the structural sensor data specific to the FPV units: comparison of measured strains, hinge loads and 6-DoF motions against the T2.3 design assumptions and the T3.1 numerical predictions; fatigue-life reassessment based on measured operational load spectra; failure-mode diagnosis for any structural anomalies observed during operation.

### Task 7.2 — Reliability Assessment (L: Sunlit Sea; P: WavEC, EDP)

Sunlit Sea leads the reliability assessment of the FPV units. The task processes the reliability-monitoring data stream from T4 and correlates it with visual inspection reports from WavEC's field campaigns to characterise:

- **Water ingress.** Longitudinal analysis of the water-ingress sensor readings and any observed intrusion at defined interface regions (PV-glass-to-PU seal, junction-box entry, terminal-box entry). This directly extends the Prototype 3 water-ingress test into a real-marine-service dataset.
- **Corrosion.** Analysis of corrosion coupons and inspection reports on the aluminium bottom plate, CONNECT hinge metalwork, and exposed electrical connections. The 5083-H111 aluminium is expected to perform, but the operational data will characterise the actual corrosion rate under real service.
- **PU degradation.** UV-induced degradation of the topside PU (still an open Norsmaterials-collaboration question, per `gen2/norsmaterials_brief.md`); salt-water fatigue of the PU-foam CONNECT connector rods; interior PU-foam moisture uptake if any.
- **Electrical reliability.** Analysis of junction-box humidity trends, string-level performance drift, hot-spot detection from IR inspection.
- **Overall availability.** Time-in-service / time-in-fault ratios for the FPV subsystem.

The reliability data is captured in a structured way that supports both a Sunlit Sea commercial reliability model (feeding warranty and O&M costing for the Norwegian pipeline) and a general-audience reliability report for the consortium.

Deliverables: D7.2a Interim reliability assessment (M30), D7.2b Final reliability assessment (M42).

### Task 7.3 — Energy Performance Assessment (L: EDP)

Sunlit Sea provides the per-module baseline performance (factory-flash data), the temperature coefficient set, and the thermal boundary conditions from the D6.1 CFD chain so EDP's performance model has a validated FPV-side input. Sunlit Sea will independently compare measured yield against the T3.2 pre-project model to close the loop on the model-chain validation from WP3.

### Task 7.4 — Model Validation (L: EDP)

Sunlit Sea contributes the T3.1/T3.2 model outputs and comparison analyses for the FPV side.

### Data delivery to Sunlit Sea

As a WP7 obligation on the operating partners (WavEC, EDP, SINTEF), Sunlit Sea receives raw and processed monitoring data for the FPV side of the system on a defined cadence (proposed: raw daily, processed weekly), in a defined format, from day one of operations. No embargo on Sunlit Sea's use of the data in commercial presentations, investor communications and marketing. Data access is essential for the Sunlit Sea-side reliability work (T7.2) and for the commercial rollout under WP8. This obligation should be reflected in the consortium agreement.

---

## WP8 — Exploitation, Business Development and Dissemination (L: EDP)

### Task 8.1 — Techno-Economic Analysis (L: EDP; P: All)

Sunlit Sea provides:

- Manufacturing cost breakdown for the Sunlit Sea CONNECT gen. 2 FPV module at demonstrator scale (50–300 kWp) and at commercial scale (multi-MW pipeline).
- Target cost benchmark: Sunlit Sea's Gen 2 float production cost target is ≤ €70/kWp on top of the standard PV panel cost (~€130/kWp for large glass/glass panels from China today), so that total EPC delivery can compete across the €300–€1800/kWp range.
- Operational cost model calibrated against the T7.2 reliability data.

### Task 8.1(bis) — Business Model Development (L: Sunlit Sea/EDP)

Sunlit Sea co-leads business model development with EDP. Sunlit Sea's contribution focuses on the Northern-European / Norwegian nearshore market, where the company has a live pipeline:

- **Skien Havn** — approximately 300 kWp, near-term.
- **Storavatnet in Haugaland Næringspark** — 3.2 MWp Phase 1 with 30–50 MW long-term capacity, in partnership with Endra, Fagne and Haugaland Næringspark. Positioned as Gen 2's flagship reference at commercial scale.
- **Gunneklevfjorden inside Hærøya Industripark** — 3.2 MWp.

The demonstrator functions as offshore de-risking for these Norwegian nearshore projects — the candidate demonstration sites are more exposed than Sunlit Sea's Norwegian pipeline sites, so passing there strengthens bankability for the home market. EDP's contribution complements this with the Iberian offshore-utility market.

The business-model deliverable will articulate the market segmentation, route-to-market, revenue model (sale of FPV units, licensing, O&M service), and the exploitation split between partners.

### Task 8.2 — Investor and Stakeholder Engagement (L: EDP/Sunlit Sea)

Sunlit Sea contributes:

- Sunlit Sea's existing investor network in Northern Europe.
- Industry-workshop content on Sunlit Sea CONNECT gen. 2 architecture, demonstrator progress, and reliability data as it becomes available.
- Customer engagement in the Norwegian pipeline: bringing prospective customers (Endra, Fagne, Haugaland Næringspark and others) into contact with the demonstrator data.

### Task 8.3 — Dissemination and Communication (L: SINTEF)

Sunlit Sea supports with FPV-side content for scientific publications (in particular the reliability findings from T7.2 and the model-chain validation results comparing T3.1 predictions against T7.1 measurements) and conference presentations.

### Task 8.4 — Booster Grant Activities (L: Sunlit Sea)

Sunlit Sea leads the €50k Booster Grant activities, focused on commercialisation reach:

- Industry-conference presence at key floating-solar and marine-renewables events with the demonstrator data.
- Customer demonstrations at the demonstration site for European utility, port-authority and industrial-user prospects.
- Communications materials (video, technical briefs, case studies) positioning the SUREWAVE-protected FPV concept in the market.
- Investor matchmaking events building on the T8.2 engagement stream.

Booster Grant activities are timed to the operational phase (M24 onwards) so demonstration data is available to support the outreach.

---

## Deliverables Sunlit Sea leads or co-leads

| ID | Title | WP | Type | Delivery month | Lead |
|---|---|---|---|---|---|
| D2.1 | System requirements specification | WP2 | R | M6 | Sunlit Sea |
| D2.3 | FPV platform detailed design report (incl. STEP models, drawings, electrical BoM, instrumentation mounting spec) | WP2 | R + DATA | M12 | Sunlit Sea |
| D4.1 | Instrumentation specification report | WP4 | R | M9 | Sunlit Sea |
| D5.2 | FPV manufacturing completion report | WP5 | R + DEM | M20 | Sunlit Sea |
| D5.5 | Factory acceptance test report | WP5 | R | M20 | Sunlit Sea |
| D7.2a | Interim reliability assessment | WP7 | R | M30 | Sunlit Sea |
| D7.2b | Final reliability assessment | WP7 | R | M42 | Sunlit Sea |
| D8.1b | Business model report (co-led with EDP) | WP8 | R | M30 | Sunlit Sea / EDP |
| D8.4 | Booster Grant activities report | WP8 | R + DEC | M42 | Sunlit Sea |

## Milestones Sunlit Sea contributes to

Aligned with the four-milestone set proposed in `background/eic/2026-08-07_eic_transition_sunlit_sea_wp_forslag.md`; if the consortium prefers a larger milestone set, our next preferred addition is an extended-operation checkpoint at approximately M30, not an early-phase one.

| MS | Title | Month | Trigger for | Sunlit Sea contribution to MS |
|---|---|---|---|---|
| MS1 | Integrated system design frozen | M12 | Hardware procurement and manufacturing commitment | FPV detailed design frozen; full CAD released (D2.3) |
| MS2 | System delivered to site, ready for offshore installation | M20 | Offshore installation activities | FPV modules factory-accepted (D5.5) and physically at the demonstration-site staging area (D5.2) |
| MS3 | System commissioned and producing | M24 | Operational phase; FPV energy production and monitoring streams online | FPV commissioning support on-site (single visit); FPV monitoring streams verified |
| MS4 | Final validation, exploitation plan and closeout | M42 | Grant closeout | Final reliability assessment (D7.2b); DNV-alignment audit output; Booster Grant closeout (D8.4) |

## Person-months indication (Sunlit Sea, draft for allocation table)

For the coordinator's Table 3.3f. These numbers are Sunlit Sea's estimate for our WP participation; final numbers agreed with the coordinator against the €2.5M budget envelope. Bold indicates WP leadership.

| WP | Sunlit Sea PM | Role |
|---|---|---|
| WP1 | 3 | Participant |
| WP2 | **24** | Lead |
| WP3 | 4 | T3.2 participant, model-chain contribution to T3.1 |
| WP4 | 6 | T4.1 lead |
| WP5 | 18 | T5.2 lead, T5.5 lead, T5.3 participant |
| WP6 | 2 | T6.2 participant, one commissioning visit |
| WP7 | 12 | T7.2 lead, T7.1 participant, T7.3/7.4 support |
| WP8 | 8 | T8.1b co-lead, T8.4 lead, T8.2 participant |
| **Total** | **77 PM** | |

## Cost estimate — Sunlit Sea share of the €2.5M project budget

The consortium budget is €2.5M lump-sum + €50k Booster Grant. Sunlit Sea's requested share is **€715k of the main envelope** (28.6%) **plus the €50k Booster Grant** which Sunlit Sea leads — **€765k total**.

Rationale for the ~29% share: Sunlit Sea leads one WP (WP2), leads four task-level activities including the hardware-heavy manufacturing task (T5.2), and delivers the physical FPV units for the demonstrator. The share sits above equal-split (€500k per partner for a 5-partner consortium) with a hardware-delivery premium; T5.2 alone represents €310k of tangible hardware plus dedicated manufacturing labour, which is proper concentration of budget on the physical deliverable. The remaining ~€1.785M is available to the four other partners (average €446k each), consistent with their expected scopes (SINTEF as coordinator + WP3/WP7 lead, WavEC as WP4/WP6 lead, EDP as WP7.3/WP8 lead, Clement as WP5 breakwater + WP2.2/T5.1).

Estimating basis: personnel cost at €8k per person-month (Norwegian tech-company fully-loaded average, mid-range for a small company); materials priced at 2026 market rates from live Sunlit Sea supply chain (PV panels at €130/kWp for large glass/glass modules; 5083-H111 aluminium, cast PU raw materials, standard marine-instrumentation hardware); subcontracting priced from current Norsmaterials and Tongge quotes for cast PU work at the P4 scale.

**Per-task cost allocation (Sunlit Sea share)**

| Task | Cost (€) | Basis |
|---|---|---|
| WP1 participation | 15,000 | 2 PM |
| **T2.1** Requirement Definition (lead) | 35,000 | 4 PM + coordination |
| **T2.3** FPV Platform Design (lead) | 95,000 | 10 PM design engineering + FreeCAD/STEP tooling |
| WP2 subtotal | **130,000** | WP lead |
| T3.2 Energy Yield (participant) | 15,000 | 2 PM + thermal-CFD input from D6.1 chain |
| T3.1 model-chain support to SINTEF | 7,000 | 1 PM |
| WP3 subtotal | 22,000 | |
| **T4.1** Monitoring Requirements (lead) | 40,000 | 5 PM + external sensor-vendor spec work |
| **T5.2 Prototype Manufacturing PV module (lead)** | **310,000** | **See T5.2 breakdown below — by far the largest single Sunlit Sea line. Cost is driven by the TRL 4/5 → 6 step (design realisation, tooling, subcontractor qualification, instrumentation, QA), largely independent of the kWp scale within the 50–300 kWp band** |
| T5.3 System Integration (participant) | 20,000 | 2 PM + installation-docs |
| **T5.5** Factory Acceptance Testing (lead) | 45,000 | 4 PM + FAT rig time + test consumables — scaled up to match the fuller instrumentation set from T5.2 |
| WP5 subtotal | 375,000 | Hardware-heavy WP; ~52% of Sunlit Sea's main envelope |
| T6.2 Installation Planning (participant) + one commissioning visit | 12,000 | 1 PM + travel Norway↔Portugal |
| **T7.2** Reliability Assessment (lead, M24–M42) | 55,000 | 7 PM spread across operational phase |
| T7.1 Structural Validation (participant) | 25,000 | 3 PM data analysis on FPV structural sensors |
| WP7 subtotal | 80,000 | Long-duration operational-phase work |
| T8.1b Business Model (co-lead with EDP) | 20,000 | 2.5 PM |
| T8.2 Investor/Stakeholder Engagement (participant) | 10,000 | 1 PM |
| T8.3 Dissemination support | 6,000 | ~0.5 PM |
| T8.4 Booster Grant (lead) — see note | 5,000 | 0.6 PM coordination charged to main envelope; €50k of activities funded from Booster |
| WP8 subtotal (excl. Booster) | 41,000 | |
| **Sunlit Sea main envelope total** | **€715,000** | 28.6% of €2.5M |
| **T8.4 Booster Grant activities** | **€50,000** | Separate Booster Grant envelope, Sunlit Sea leads |
| **Sunlit Sea grand total** | **€765,000** | |

**T5.2 breakdown (the largest single line — €310k, 43% of Sunlit Sea's main envelope)**

T5.2 delivers the physical FPV units for the demonstrator, in the 50–300 kWp band. The T5.2 budget is set by the work required to raise the Sunlit Sea CONNECT gen. 2 FPV unit from TRL 4/5 to TRL 6, not by the number of kWp built. The TRL step is what the project is paid to deliver, and it is what carries the cost:

- **Design realisation** — turning the WP2 T2.3 detailed design into a manufacturable article, resolving the last open architectural choices (flat vs. hydroformed aluminium bottom, cast-on-frame vs. separate-and-mount PU, UV-resistant PU formulation) at production quality rather than 3D-printed-prototype quality.
- **Tooling** — one set of production-run moulds, jigs and fixtures, cost largely independent of run length.
- **Cast-PU subcontracting setup** — supplier qualification, tool-set adjustment, first-article inspection, quality gates. Fixed component dominates over per-unit component at demonstrator scale.
- **Instrumentation set** — sensor selection, integration into the manufacturing process, wiring, terminal-box qualification. Cost is per instrumented unit and per instrument type, not per kWp of the overall array.
- **Manufacturing engineering and QA** — a demonstrator build requires a full quality regime (inline inspection, dimensional checks, electrical acceptance, water-ingress test, documentation package per unit). This effort is essentially fixed for the build campaign.
- **Materials** — the only line that scales linearly with kWp is PV panels + aluminium + PU raw materials. This is a minority of T5.2.

The line-item breakdown below reflects an internal nominal split at ~200 kWp (mid of the 50–300 kWp band). The T5.2 total (€310k) is fixed; if the final scale settles below or above the nominal, the fixed-cost lines (personnel, tooling, subcontracting setup, instrumentation) absorb the difference against the variable-cost lines (PV panels, aluminium, PU raw). At the low end (50 kWp) the freed capacity supports denser per-unit instrumentation, more iteration cycles and more design-margin; at the high end (300 kWp) more of the envelope shifts to raw materials at the expense of per-unit instrumentation density.

| Item | Cost (€) | Scaling | Note |
|---|---|---|---|
| Personnel — manufacturing engineering, QA, assembly supervision | 95,000 | Fixed | ~12 PM through the build window (M13–M20) |
| Cast-PU subcontracting (Norsmaterials or Tongge, per M12 sourcing decision) | 55,000 | Mostly fixed | Supplier qualification, tool-set adjustment, first-article, ongoing QA — includes Norsmaterials development share for the UV-resistant PU variant. Per-unit variable component is small at demonstrator run length |
| Instrumentation hardware installed at manufacturing time | 50,000 | Fixed per instrumented-unit set | Denser sensor coverage than a minimum spec — build time is the cheapest place to add sensors, highest-value input to WP7 reliability and energy-performance analyses |
| PU raw materials (cast frame + interior foam + connector rods) | 32,000 | Semi-variable | Includes formulation-trial budget for UV-resistant Norsmaterials variant (open item per `gen2/norsmaterials_brief.md`); scales moderately with unit count |
| Standard commercial PV panels (nominal 200 kWp × €130/kWp) | 26,000 | Fully variable with kWp | Large glass/glass, 710–740 Wp panels. Only fully-linear scaling line |
| Tooling — moulds, jigs, fixtures | 18,000 | Fixed | Production-run tooling above the 3D-printed prototype level; jigs for consistent hinge-half placement |
| Assembly labour subcontracting | 15,000 | Semi-variable | Extended peak-load capacity to hold the M20 delivery date without QA compromise |
| Aluminium 5083-H111 sheet, 0.8 mm | 15,000 | Semi-variable | Bottom plates for all units + QA-reject buffer |
| Packaging + inland transport to shipping port | 4,000 | Variable | Sea-freight-ready packaging |
| **T5.2 total** | **€310,000** | Fixed | |

Roughly two-thirds of T5.2 is scale-independent — the TRL-step cost — and roughly one-third scales with kWp. This is why the total is stable across the 50–300 kWp band.

Note on the T5.2 emphasis: this line is by design the largest single Sunlit Sea allocation. The physical FPV units are Sunlit Sea's core deliverable, and the reliability / energy-yield data the whole project ultimately produces depends on what is actually built here. Concentrating budget on T5.2 — better tooling, more instrumentation at build time, more manufacturing engineering, more QA margin, more subcontractor development for the UV-resistant PU — converts directly into higher-quality operational data downstream (T7.2, T7.3) and into a manufacturable article that survives beyond the demonstrator.

**Booster Grant (€50k, Sunlit Sea leads T8.4)**

The €50k Booster Grant is not part of the €2.5M main envelope and is allocated separately by the EIC. Sunlit Sea proposes to lead the Booster activities focused on commercialisation reach (industry conferences, customer demonstrations at the demonstration site, communications materials, investor matchmaking). Timing: activities front-loaded from M24 onwards, once operational data is available.

**Sensitivity — demonstrator scale within 50–300 kWp**

The T5.2 budget is fixed at €310k across the 50–300 kWp band, and Sunlit Sea's total main envelope (€715k) is fixed independent of scale. The reason is that the TRL-raising work — design realisation, tooling, subcontractor qualification, instrumentation set, manufacturing engineering, QA regime — is essentially scale-independent, and the only strictly-variable line inside T5.2 (PV panels + aluminium + PU raw materials) is a minority of the total.

Practical implication for the consortium:

- **At the low end (50 kWp)** the freed variable-cost capacity supports denser per-unit instrumentation, more design-iteration cycles during the build, and more thorough factory acceptance testing per unit. TRL-6 evidence per unit is stronger; system-level matrix evidence is weaker.
- **At the high end (300 kWp)** more of the fixed T5.2 envelope is consumed by PV panels and PU/aluminium raw materials, reducing per-unit instrumentation density and design-iteration margin. TRL-6 evidence at system-matrix level is stronger; per-unit resolution is lower.

Sunlit Sea does not require a fixed scale commitment at proposal stage. The choice sits with the consortium and follows from WP6 T6.1 site selection.

## Open items to raise with Balram and the consortium

- **T2.2 lead structure** — confirm co-lead with Clement for WP2 (Sunlit Sea FPV-side, Clement breakwater-side), or split into WP2a (FPV, Sunlit Sea) and WP2b (breakwater, Clement). Our preference is co-lead; the current draft has SiS as sole WP2 lead.
- **T5.3 lead** — the preliminary WP document has EDP leading system integration, but the practical work is FPV-installation-heavy. Sunlit Sea can co-lead T5.3 with EDP if that helps clarify the offshore work split.
- **Milestone count** — confirm four milestones is acceptable to CINEA in a €2.5M / TRL 5→6 / 36-month project. If more are needed, next preferred is an M30 extended-operation checkpoint.
- **Site selection and demonstration scale** — approximately seven candidate demonstration sites are under evaluation (WP6 T6.1); Sunlit Sea takes no position on the specific site at proposal stage. Similarly, Sunlit Sea does not require a fixed scale commitment in the 50–300 kWp band — the Sunlit Sea T5.2 budget (€310k) is fixed across this range because the TRL-raising work is largely scale-independent. Scale selection is a consortium/site call, not a budget call.
- **Data delivery to Sunlit Sea in the consortium agreement** — see WP7 data-delivery paragraph; needs explicit CA article.
- **DNV-ST-C108 / DNV-ST-E309 alignment scope** — Sunlit Sea proposes to lead the certification-alignment documentation sub-task in WP2 and WP7. If another partner is already working to these standards in ongoing work, we can piggyback on their format.
