## 1. Cross-cutting additions we suggest

### 1.1 Milestones — propose a minimal set of four

The current draft does not yet include milestones. We would like to propose that the consortium adopts a deliberately minimal set — four milestones — before the structure hardens. Once milestones enter the grant agreement, CINEA does not accept date changes lightly, and every locked milestone becomes an area of schedule risk during execution. Fewer milestones means less exposure.

- **MS1 — Integrated system design frozen (approximately M12)**. Trigger for hardware procurement commitment.
- **MS2 — System delivered to site, ready for offshore installation (approximately M20)**.
- **MS3 — System commissioned and producing (approximately M24)**. Trigger for the operational phase.
- **MS4 — Final validation, exploitation plan and closeout (approximately M36)**.

If CINEA is expected to insist on more, we would prefer to add one at the M30 extended-operation checkpoint rather than adding early-phase milestones that constrain the technical iteration in WP2 and WP3.

### 1.2 DNV alignment as a strategic theme

DNV has recently expanded its floating PV standards landscape:

- **DNV-RP-0584** (Recommended Practice, offshore FPV design, development and operation) — updated 2026. Sunlit Sea's design methodology has been verified against this since 2022.
- **DNV-ST-C108** (Structural design of floating photovoltaic units) — new support standard released May 2026.
- **DNV-ST-E309** (Mooring of floating photovoltaic units) — new support standard released May 2026.

We suggest structuring the project so that its output leaves the technology "certification-ready" against these standards, without bringing DNV in as a project partner (which would add cost and slow review cycles). This is achievable by shaping design documentation, testing regime and monitoring plan so a future certification project can build directly on the EIC Transition outputs. Concretely, we suggest adding references to these three DNV documents inside T2.1 (Requirement Definition) and producing a certification-readiness documentation package as a deliverable under T9.3 (Dissemination and Communication).

### 1.3 Data delivery terms in the consortium agreement

The Data Acquisition Platform (T4.3) currently describes cloud storage and a dashboard, but does not specify how data flows to individual partners. We would like to propose that the consortium agreement includes:

- Raw operational data made available to all partners daily.
- Processed data made available weekly.
- No embargo on any partner's commercial or investor use of the data.
- Data-delivery obligations independent of on-site presence at Aguçadoura.

For Sunlit Sea this is essential. We cannot commit budget or personnel to regular field trips from Norway to offshore Portugal — the costs would erode our share of the €2.5M more than the value would justify. We depend on remote data delivery from day one of operations to validate our design and support commercial rollouts in our Northern European pipeline.

### 1.4 Explicit boundary between what Sunlit Sea delivers and what is outside our domain

To help balance the WP leads and reduce late confusion, we suggest formally documenting the following:

- **Sunlit Sea delivers**: the floating photovoltaic unit — from the panel surface down to the aluminium bottom plate, including the cast PU float-structure and integrated hinge halves. Design, CAD, manufacturing, factory acceptance testing, and electrical interface at the FPV terminal.
- **Sunlit Sea contributes knowledge and opinions on, but does not lead**: mooring and anchoring, breakwater design (CLEMENT owns this), site selection and permitting, grid interface and power management, offshore field operations (installation, monitoring campaigns, maintenance).

## 2. Per-WP suggestions

Where we do not comment, we agree with SINTEF's structure as drafted.

### WP1. Project Management and Innovation Management

- Content is fine as drafted. We agree with the addition of T1.3 Innovation and Commercialization Management as a dedicated task; this fits EIC Transition's business focus better than folding it into WP9.

### WP2. Design Optimization of the SUREWAVE FPV System

- **T2.1 Requirement Definition** — we suggest adding, as a sub-item: "Design against DNV-RP-0584 wave/wind exposure categories, DNV-ST-C108 structural design requirements and DNV-ST-E309 mooring requirements, with certification-readiness as an output". This makes the DNV alignment concrete at the requirements stage.
- **T2.3 FPV Platform Design** — Sunlit Sea would like to lead this task. This is our core deliverable and the domain where our expertise is most unique to the consortium.
- **T2.4 Mooring and Anchoring System Design** — outside Sunlit Sea's domain. We contribute FPV-load boundary conditions to whoever leads.

### WP3. Design and Performance Assessment

- **T3.3 Model Development** — Sunlit Sea would like to heavy-contribute here. Our SuRE D6.1/D6.2 model chain (SiSim structural response coupled to thermal CFD, with LCA interface) is directly applicable and adds a formal modelling layer that would otherwise need to be built from scratch. Happy to co-author with SINTEF as lead.

### WP4. Instrumentation and Monitoring System Development

- **T4.1 Monitoring Requirements** — we suggest adding a sub-item: "FPV-side instrumentation specification (sensors on frame, hinges, PU-glass interface, panel back)" so that Sunlit Sea provides this input at project start, allowing sensors to be embedded at manufacturing time.
- **T4.3 Data Acquisition Platform** — please add data-delivery terms as discussed in section 1.3 above. This is the concrete place where remote data-access rights are codified.

### WP5. Demonstrator Construction and Integration

- **T5.1 Prototype Manufacturing** — we suggest splitting the current three-item breakdown ("Floating structures", "Breakwater components", "Mooring components") into three lead assignments: Sunlit Sea leads the Floating structures deliverable, CLEMENT leads the Breakwater components, WavEC or CLEMENT leads the Mooring components. This clarifies scope and budget allocation at the manufacturing stage.
- **T5.2 PV and Dummy Module Integration** — Sunlit Sea would like to lead. Integration of PV modules into our float units is our factory-side responsibility.
- **T5.3 System Assembly and Factory Testing** — split lead: Sunlit Sea for FPV factory acceptance, CLEMENT for breakwater factory acceptance. Combined final integration should be co-authored with WavEC involved for pre-shipping check.

### WP6. Demonstration Site Preparation, Permitting and Deployment

- Content is well-structured, particularly the explicit list of permits under T6.2 and the addition of T6.3 Environmental and Social Impact Assessment. These are important for a CINEA-reviewer audience and we support keeping them.
- Sunlit Sea sits outside the domain for this whole WP. We propose that WavEC or EDP lead throughout, with Sunlit Sea contributing FPV-specific input where asked (transport constraints, electrical interface pre-check, one commissioning visit under T6.5).

### WP7. Operational Validation and Data Collection

- **T7.1 Structural Validation** — we suggest adding, as a sub-item: "Comparison of measured loads against DNV-ST-C108 load matrix as a validation criterion". This ties the structural work back to the DNV alignment theme without extra effort.
- **T7.3 Energy Performance Assessment** — good fit for EDP lead as per their stated interest.
- **T7.4 Model Validation** — Sunlit Sea heavy-contribute for the FPV-side validation (comparing SuRE model chain predictions against real drift, temperature and structural data).

### WP8. Environmental, Economic and Replication Assessment

- **T8.1 Environmental Assessment** — where possible, we suggest the LCA methodology aligns with the SuRE D6.1/D6.2 LCA interface approach (developed with TNO). This avoids parallel work and lets the two projects reinforce each other in exploitation.
- **T8.2 Techno-Economic Analysis** — natural fit for EDP lead as per their stated interest.

### WP9. Exploitation, Business Development and Dissemination

- **T9.3 Dissemination and Communication** — we suggest adding: "Certification-readiness documentation package (mapping project outputs to DNV-RP-0584, DNV-ST-C108, DNV-ST-E309)" as a specific deliverable. This is useful for CINEA reporting and directly supports each partner's commercial exploitation.
- **T9.4 Booster Grant Activities** — we suggest the €50k Booster is directed at dissemination that supports commercial reach across Portugal, Norway and Germany (industry conferences, customer demonstration events at Aguçadoura, communications materials in three languages). Balances the geographic exploitation split.
- We would also like to propose that the consortium agreement documents a geographic exploitation split so it does not have to be renegotiated at the end: Sunlit Sea → Northern Europe / Norway; EDP → Iberia; CLEMENT → global for breakwater-related deployments; the integrated FPV-plus-breakwater concept jointly owned by CLEMENT and Sunlit Sea.

## 3. Task-lead assignments — a compact proposal

To help the discussion converge, here is a first-cut proposal for task leads. All lead assignments are open to negotiation; please treat this as our opening position, not a demand.

| Task | Proposed lead | Support | Notes |
|------|---------------|---------|-------|
| T1.1 Coordination | SINTEF | all | continuity from Surewave |
| T1.2 Risk and Quality | SINTEF | all | |
| T1.3 Innovation and Commercialization Management | CLEMENT or SINTEF | Sunlit Sea | |
| T2.1 Requirement Definition | SINTEF (convener) | all | add DNV-alignment sub-item |
| T2.2 Floating Breakwater Optimization | CLEMENT | | their design |
| T2.3 FPV Platform Design | **Sunlit Sea** | | our core deliverable |
| T2.4 Mooring and Anchoring System Design | WavEC or EDP | Sunlit Sea (loads only) | |
| T3.1 Numerical Modelling | SINTEF | | hydrodynamic and structural |
| T3.2 Energy Yield Assessment | EDP (per stated interest) | Sunlit Sea (thermal CFD) | |
| T3.3 Model Development | SINTEF | **Sunlit Sea heavy** | SuRE model chain plugs in |
| T4.1 Monitoring Requirements | EDP (per stated interest) | Sunlit Sea (FPV spec) | |
| T4.2 Sensor System Development | SINTEF or WavEC | | |
| T4.3 Data Acquisition Platform | SINTEF | Sunlit Sea (FPV data schema) | add data-delivery terms |
| T5.1 Prototype Manufacturing (floating) | **Sunlit Sea** | | |
| T5.1 Prototype Manufacturing (breakwater) | CLEMENT | | |
| T5.1 Prototype Manufacturing (mooring) | WavEC or CLEMENT | | |
| T5.2 PV and Dummy Module Integration | **Sunlit Sea** | | our factory scope |
| T5.3 System Assembly and Factory Testing | Sunlit Sea (FPV) + CLEMENT (breakwater) | WavEC | co-authored |
| T6.1 Site Selection | EDP or WavEC | | |
| T6.2 Permitting | EDP or WavEC | | |
| T6.3 EIA | WavEC | | |
| T6.4 Installation Planning | WavEC | | |
| T6.5 Offshore Installation | WavEC | Sunlit Sea (one commissioning visit) | |
| T7.1 Structural Validation | SINTEF or WavEC | Sunlit Sea | add DNV-ST-C108 validation sub-item |
| T7.2 Reliability Assessment | WavEC | | |
| T7.3 Energy Performance | EDP (per stated interest) | Sunlit Sea | |
| T7.4 Model Validation | SINTEF | **Sunlit Sea heavy** | SuRE model chain validation |
| T8.1 Environmental Assessment | SINTEF or WavEC | Sunlit Sea (SuRE LCA continuity) | |
| T8.2 Techno-Economic Analysis | EDP (per stated interest) | | |
| T9.1 Business Model Development | EDP (per stated interest) | Sunlit Sea (Northern Europe) | |
| T9.2 Investor and Stakeholder Engagement | shared | | |
| T9.3 Dissemination and Communication | CLEMENT or SINTEF | Sunlit Sea | add certification-readiness deliverable |
| T9.4 Booster Grant Activities | CLEMENT | all | dissemination across PT / NO / DE |

## 4. Two items we did not have but would like to reserve for later discussion

- **Scale of the demonstrator** — the 30.07 meeting left 100-300 kWp open. From a TRL 6 credibility standpoint, we would prefer around 200 kWp as a balance between matrix-effect testing (which needs multiple modules) and budget headroom for the DNV-alignment and remote-data work.
- **Sunlit Sea on-site presence** — we have budgeted for one FPV commissioning visit in T6.5 / T7 handover. Additional visits would need to be justified separately and covered from contingency rather than baseline budget. We would like this to be reflected in the resource planning early.
