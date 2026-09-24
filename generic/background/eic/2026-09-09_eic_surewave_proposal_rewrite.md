---
internal_title: "SUREWAVE_EIC — EIC Transition proposal, Part B (working draft)"
acronym: SUREWAVE_EIC
call: HORIZON-EIC-2026-TRANSITIONOPEN
deadline: 2026-09-16 17:00 Brussels
internal_author: Sunlit Sea AS (Eirik Larsen) — draft offered to SINTEF as coordinator
internal_date: 2026-09-09
duration: 36 months
requested_lump_sum: EUR 2 480 000
basis: >
  Complete rewrite of the SINTEF draft of 2026-09-09, addressing the findings in
  generic/background/eic/2026-09-09_eic_proposal_revision_strategy.md and verified against the
  EIC Work Programme 2026 (Annex C(2026) 4080).
note: >
  Chapter and subchapter structure and all #@…@# / #§…§# processing tags are reproduced
  exactly from the EU Part B template. The template's grey guidance text has been removed,
  as it is at submission. Page-limit notes and the open-decisions appendix live in task T104.
---


# Cover page

This page must be completed and maintained in the submitted proposal. It contains important information, if missing, the proposal could be considered incomplete and therefore inadmissible.

I confirm that this proposal builds on results achieved (achieved and completed minimum TRL 3) within eligible project(s), indicated in Part A.  ☒ Yes  ☐ No

I confirm that the applicant(s) are the owner or have any necessary agreements with owners or right holders of those results, as described in the proposal.  ☒ Yes  ☐ No

Eligible project on which this proposal is built:
Grant agreement 101083342 — SUREWAVE, *"Structural Reliable Offshore Floating PV Solution Integrating Circular Concrete Floating Breakwater"*, HORIZON-RIA under Horizon Europe Pillar II (HORIZON.2.5.2 Energy Supply), 1 October 2022 – 30 September 2026, coordinated by SINTEF AS.

Three of the four applicants — SINTEF AS, Sunlit Sea AS and CLEMENT Germany GmbH — are beneficiaries of SUREWAVE and are the owners or holders of the intellectual property rights in the results developed further here, with the necessary rights to commercialise them for the whole duration of this project. EDP joins as end user and commercialisation partner and requires no access to SUREWAVE background beyond what the Consortium Agreement will grant; a commitment letter is therefore not required.

Where the result is reported:
CORDIS project page <https://cordis.europa.eu/project/id/101083342> · CORDIS reporting <https://cordis.europa.eu/project/id/101083342/reporting> · project website <https://surewave.eu/>

*Other linked projects relevant to the proposal*

| Funding scheme/call | Project ID | Project Acronym | Project Acronym and weblink (e.g. Cordis) |
|:---|:---|:---|:---|
| Horizon Europe (HORIZON-CL5-2021-D3-03) | 101083342 | SUREWAVE | SUREWAVE — https://cordis.europa.eu/project/id/101083342 |

\[This document is tagged. Do not delete the tags; they are needed for processing.\] \#@APP-FORM-HEEICTRA@#

---

# 1. Excellence \#@REL-EVA-RE@#

SUREWAVE developed and validated a floating photovoltaic (FPV) system protected by a purpose-designed floating breakwater built from circular concrete. The breakwater absorbs and reflects wave energy before it reaches the solar array, so the array itself does not have to be engineered to survive the wave climate.

By the end of SUREWAVE the following elements are complete: the integrated breakwater-plus-FPV concept design; circular concrete formulations (lightweight aggregate, high-performance and cellular) characterised for marine and freshwater service; coupled aero-hydrodynamic models (CFD, SPH, MoorDyn) and non-linear structural FEM; a redesigned inter-module hinge developed after the first wave-basin campaign exposed a load path that the original connector could not carry; mooring and anchoring concepts for both modular and large-array configurations; structural-health-monitoring methodology; and two wave-basin campaigns at MARIN covering mild and harsh irregular sea states. The result is validated in a laboratory environment: all elements of TRL 4 are complete. What has never been done is to build the integrated system at production scale, put it in open water, and operate it. That is the gap this project closes, and it is the reason the technology cannot yet be sold.

The consortium partners' own products — Sunlit Sea's floating solar arrays (sold without mooring) and CLEMENT's floating concrete breakwaters — have never been fielded together at production scale. This project combines them into the protected-array configuration validated in SUREWAVE, deploys the result at Hainer See, and produces the six things a customer, an insurer and a lender ask for before signing: measured wave attenuation, measured structural loads, measured energy yield, a demonstrated installation and maintenance method, an independent conformity statement against the applicable DNV standards, and a cost model built on real invoices rather than estimates. EDP is a potential adopter and commercialisation partner for the combined offering, contingent on what the demonstrator shows.

## 1.1 Technological breakthrough \#@PRJ-OBJ-PO@#

Floating solar is a fast-growing industry that is almost entirely confined to calm water. The reason is structural: on an open reservoir, wind blowing along several kilometres of fetch generates short, steep waves, and those fetch-driven waves are one of the dominant destroyers of conventional FPV — alongside wind uplift, storm loads and corrosion, all of which the sector engineers against and each of which has caused known field failures. On windy inland water bodies specifically, fatigue and impact loading from short steep waves is the failure mode that most sharply limits deployment: a small floating solar installation on a lake near Hainer See was destroyed by wave loading within two years, on a lake with smaller waves than our demonstration site. Wave loading fatigues the connectors between modules, drives mooring loads that scale faster than array size, and forces inspection and repair cycles that ruin the operating cost case.

The industry's answer so far has been to make the float stronger: thicker HDPE, more steel, heavier moorings, stiffer inter-module connections. Every one of those answers raises capital cost per watt and none of them removes the load. Above roughly 0.5 m significant wave height, conventional reservoir FPV becomes uneconomic, and the developers who need the area most — hydropower operators with large, windy reservoirs — are exactly the ones who cannot use it.

SUREWAVE inverts the problem. Instead of designing the solar array to resist the incident wave field, we filter it. A modular floating breakwater, engineered specifically for solar protection rather than borrowed from marina practice, is moored around the array and attenuates the wave frequencies that damage FPV, leaving a residual field the array can operate in at calm-water specification. The array then runs in the regime it was designed for, at calm-water cost, on water that is not calm.

This changes the economics rather than the physics of the panel. The breakwater is concrete — cheap, durable, locally produced — and doubles as usable real estate on the water: the pontoons can host inverters, transformers or charging stations, or integrate into marinas and other waterside structures, so their cost is spread across more than one function. The concrete mix itself is a live design decision, weighed during the project against service performance, cost and CO₂ footprint rather than fixed to a single formulation up front. The saving is on the other side of the ledger: a lighter float, a simpler connector, a smaller mooring spread, longer inspection intervals, and a design life that is not consumed by fatigue.

The integrated system combines seven elements developed and validated in SUREWAVE: a breakwater geometry optimised for solar protection rather than for berth shelter, dimensioned to the directional wave exposure of the specific site rather than to a full 360° envelope; concrete formulations characterised for the required durability and buoyancy, with the mix selected per site against cost, service performance and CO₂ footprint; coupling and transition elements between breakwater and array; a hinge redesigned to survive the load path that basin testing revealed; mooring and anchoring for both moderate and harsh states; a coupled aero-hydro-structural model chain; and structural health monitoring for predictive maintenance.

The strongest evidence that the concept will work is that its failure modes have already been found. The first MARIN campaign broke the connector, which is what a basin campaign is for. The redesigned hinge was then tested and characterised against the load cases that broke its predecessor. A technology whose weakest element has been located, redesigned and re-tested is in a materially different position from one that has only ever succeeded.

The addressable market has two anchor segments that open up together the moment the wave constraint is removed. First, the world's existing reservoirs, where the grid connection, the access road and the permitting precedent already exist: 1 % of global reservoir surface would support roughly 404 GW of solar — about twice the world's total solar additions in 2024 — and 25 % coverage would support approximately 4 400 GW.¹ Second, harbours and sheltered coastal water in and around the world's coastal cities. Many of the world's largest cities sit on coastlines, and shoreline expansion — reclaimed land, new marinas, port extensions, waterfront redevelopment — is a live construction activity in most of the fastest-growing urban regions, particularly near the equator. Harbours already provide partial wave shelter from the sectors where the shore is close; completing that shelter with a directional concrete breakwater produces usable water surface in places where new land is not on offer at any price. The floating solar market as a whole stands at about USD 7.9 bn in 2026 and is forecast to grow at roughly 12 % annually,² while the nearshore and coastal segment grows about three times faster — around 35 % CAGR to 2030 — from a small base.

The commercial sweet spot inside both segments is the same physical case: partially sheltered water where the dominant wave direction is set by fetch through one or a small number of sectors, with the remaining sectors sheltered by geography or existing infrastructure. SUREWAVE's site studies identified this as the single largest cost lever: a breakwater arranged to intercept a 30–90° arc, rather than a full 360° ring, uses a fraction of the breakwater metres and mooring spread per protected megawatt. Directional selectivity is what makes the protected-array architecture affordable on the sites that need it most, and it lets one architecture serve both windy reservoirs and urban harbours, since the design load in each case is fetch-driven short steep seas.

In the harbour and waterfront context, the concrete breakwater doubles as urban infrastructure. Port Hercule in Monaco is the precedent, and it predates any floating solar consideration: a 352 m semi-floating concrete caisson, cast in Algeciras and towed across the Mediterranean in 2002, which extends the harbour while housing a four-level 360-car garage and some 25 000 m² of technical space inside its hull.³ The same pontoon can carry inverters, transformers and cabling for the array, and beyond that walkways, ferry berths, EV or boat charging, or public space, shaped to sit inside a cityscape rather than at the edge of it. Where waterfront real estate carries the very high land value it does in almost every coastal city, a shared-function breakwater turns from a cost line into a value line.

What puts water beyond reach for conventional FPV is the wave climate, and the two segments build their waves by different routes. On a reservoir the energy is wind-driven: fetch across open water raises short, steep seas whose severity follows the distance the wind crosses. In a harbour that fetch-driven component is joined by swell refracting in through the entrance, generated far offshore and arriving from a narrow, predictable sector. Both mechanisms load a solar array cyclically in ways it was not built for, and both are strongly directional, so a partial breakwater arc does the work of a full ring. Above the economic threshold described earlier, the water stays unbuilt on either kind of site. SUREWAVE's competitive position is that it moves that threshold, using a component whose supply chain is local, mature and European, and whose secondary use as harbour infrastructure is an established building type.

Two lines of customer evidence sit inside the consortium and its immediate commercial pipeline. On the reservoir side, EDP operates the largest floating solar plant on a dam reservoir in Europe (Alqueva, 5 MWp, ~7.5 GWh/yr, hybridised with hydro and a 1 MW battery), holds a 70 MW floating-solar award at Alqueva from the 2022 Portuguese auction, and runs an open-access Floating PV Lab at Alto Rabagão whose published purpose is to reduce technology risk and industrialise new floating solar solutions — a site EDP itself characterises as having strong winds, significant wave action, and temperatures from below 0 °C to above 30 °C with ice and snow. EDP has stated a target of supporting the commercialisation of at least five new floating solar technologies by the end of 2027. On the harbour and nearshore side, Sunlit Sea's active Northern European commercial pipeline is dominated by harbour and sheltered-coastal sites: Skien Havn (~300 kWp, near-term), Vollsfjorden inside the same Grenland port district, Gunneklevfjorden inside Hærøya Industripark (3.2 MWp), and Storavatnet at Haugaland Næringspark (3.2 MWp phase 1, 30–50 MW long-term).

Competitors are pursuing either the harder fully-exposed offshore segment (SolarDuck, Oceans of Energy) or a stronger float without a breakwater (Ocean Sun, Saipem/Moss Maritime XolarSurf, Fred. Olsen 1848 Brizo, Sungrow FPV). None is selling a protected-array architecture that serves both windy reservoirs and urban harbours using the same protected-water principle. That is the gap.

¹ ~404 GW from 1 % of global reservoir surface: *J. Marine Science and Engineering* 13(8), 2025. Global FPV–hydropower potential 3.0–7.6 TW: *Renewable Energy*, 2020. ² Market size and segment growth: Global Market Insights, *Floating Solar PV Market 2026–2035*. ³ Port Hercule semi-floating dyke, Monaco: FDN Group; technical description, AFGC.

## 1.2 Objectives

Everything below is defined against a single physical object: a protected floating solar demonstrator at Hainer See, Saxony, Germany — the baseline site, confirmed at M6 against the alternatives assessed in T6.4 — operated for at least twelve months. The demonstrator is sized by what it has to prove rather than by nameplate capacity. TRL 6 evidence comes from an instrumented array of production units operating behind a representative run of breakwater through a full seasonal cycle, and that evidence is complete anywhere in the 50–300 kWp band. The figure inside that band follows from the site layout settled in WP2 — directional wave exposure at the deployment area sets the breakwater arrangement, and the breakwater arrangement sets how much protected water there is to fill — and is fixed at the M12 design freeze.

The work-package scope and the requested lump sum hold across the whole band, because the cost of this demonstrator is dominated by the step from laboratory result to manufactured article: production tooling, subcontractor qualification, the instrumentation set, manufacturing engineering and the quality regime. Each of those is a one-time cost of standing up the build campaign, paid in full whether it produces fifty kilowatts or three hundred. Only the PV modules, the aluminium and the polyurethane raw materials scale with installed capacity, and together they are a minority of the manufacturing budget. Sizing at the lower end of the band buys denser per-unit instrumentation and more design-iteration margin; sizing at the upper end buys more array-level behaviour. Both deliver the evidence the project exists to produce, and both leave the work-package boundaries and the amount requested exactly where they stand.

### Technology objectives

| | Objective | Target | By |
|:--|:--|:--|:--|
| O1 | Build and commission the integrated demonstrator | Protected FPV demonstrator, grid-connected, commissioned and generating | M22 |
| O2 | Quantify the wave attenuation the breakwater delivers | Attenuation measured across the encountered sea states, against a design target of ≥ 50 % reduction in significant wave height at the array | M30 |
| O3 | Quantify the structural benefit to the array | Mooring and anchoring loads measured and set against the unprotected prediction, design target ≤ 50 % | M30 |
| O4 | Operate the demonstrator and record what it produces | ≥ 12 months continuous operation, with availability and performance ratio measured and reported; design targets ≥ 95 % and ≥ 0.80 | M34 |
| O5 | Establish the accuracy of the model chain | Prediction error quantified for motions, loads and yield across the measured envelope, design target ≤ 20 % | M34 |
| O6 | Demonstrate and cost the installation and O&M method | Installation, maintenance and recovery executed and costed from actual invoices | M34 |
| O7 | Reach TRL 6 with independent confirmation | Integrated system demonstrated in a relevant environment; DNV statement of conformity issued | M34 |

### Business objectives

| | Objective | Target | By |
|:--|:--|:--|:--|
| O8 | Validate the customer requirement against real sites and an operating installation | Requirements drawn from the partners' live commercial engagements in year one; ≥ 15 organisations hosted at the demonstrator across the operating campaign | M34 |
| O9 | Validate the economics | Techno-economic model with LCOE at 1 MW, 10 MW and 50 MW, built on demonstrator invoices | M30 |
| O10 | Secure the commercial defensibility of the result | Freedom to operate confirmed for the demonstrator configuration; trade-secret regime and data-access rules in force; demonstrator dataset governed as consortium foreground | M12 |
| O11 | Convert interest into commitment | ≥ 3 Letters of Intent for post-project installations, ≥ 1 from a consortium partner | M34 |
| O12 | Be investment ready | Investment-ready business plan; ≥ 10 investor meetings; EIC Accelerator Fast Track application prepared | M36 |

The technology objectives are written as measurements, because measurement is what the project controls. The values in the target column are what the system is engineered to reach and what the business case assumes. Where a measured result lands below one of them, the project's output is the quantified shortfall and its cause. That is what the next design iteration and the commercial model both run on, and it can only come from water. O2 and O3 carry the most weight: they establish whether the protected-array architecture delivers the effect the whole product rests on, and the instrumentation is arranged so that the answer arrives by M30. O5 matters because a customer buying a 50 MW array will not buy from a demonstrator — they buy from a validated model, and the model is only worth what its measured error says it is worth. O7 exists because "we think it is TRL 6" is worth less than a DNV statement. The business objectives run in parallel from M1, so that customer requirements shape the design before the M12 freeze rather than arriving in the final year when the design is fixed.

The timing argument is specific. DNV released ST-C108 (structural) and ST-E309 (mooring) in May 2026, and RP-0584 already covers FPV design. For the first time there is a certification path for floating solar, which means for the first time a floating solar asset can be financed conventionally. A technology that arrives with a conformity statement against those standards in 2029 arrives at the right moment. One that arrives in 2033 arrives to a market that has already chosen.

## 1.3 Methodology \#@CON-MET-CM@# \#@COM-PLE-CP@#

The methodology is four phases, each producing what the next one needs, with the business track running in parallel from M1 rather than being appended at the end.

Phase 1 — Engineering (M1–M12). Hainer See is the baseline site and the engineering works to it from M1, while a comparative assessment against the Portuguese candidates EDP brings runs alongside in WP6 and closes at M6, before the design basis freezes. The site is therefore characterised rather than searched for. Hainer See is surveyed: bathymetry, wind and wave hindcast validated against local measurement, water level, ice, access and grid interface. That produces the design basis. From it, Sunlit Sea details the FPV platform (CONNECT gen. 2 architecture: 0.8 mm aluminium 5083-H111 bottom plate, cast polyurethane frame around standard commercial 710–740 Wp modules, PU-foam infill and connector rods), CLEMENT optimises the breakwater geometry and the mooring spread, and SINTEF runs the coupled models over the site load cases to verify the configuration before anything is built. The array layout is decided in this phase — a rectangular matrix behind a shore-parallel breakwater run — not left open. SINTEF governs conformity throughout: it holds the requirement set derived from DNV-RP-0584, ST-C108 and ST-E309, reviews each partner's design output against it, and returns findings to the designer while there is still time to act on them. Documentation is structured to those standards from the first drawing, so that certification becomes a review rather than a retrofit.

Phase 2 — Build (M7–M20). CLEMENT casts the breakwater modules and fabricates the mooring hardware; Sunlit Sea manufactures the FPV units. The floating units are built sealed and unmodified, exactly as they would be sold. Measurement sits outside them: two moored wave buoys, load cells in the mooring and anchoring system, a pyranometer with its thermal sensor at the array, and a site camera, all commissioned with the system. Keeping instrumentation off the product is deliberate. A module with a sensor cable through its seal is no longer the article a customer buys, and a reliability result taken from it would not transfer. What comes out of the water after twelve months is the commercial unit. Both partners run factory acceptance testing against written protocols before anything ships.

Phase 3 — Deploy and operate (M15–M34). Mooring is pre-laid, the breakwater is towed and connected, the array is assembled and moored inside it, electrical and monitoring systems are commissioned. Then the system runs for at least twelve months while the monitoring platform collects environment, structure, mooring and energy data continuously. Mid-campaign the array is inspected and a subset of units is opened for condition assessment. At the end the system is recovered and taken apart, and the units are examined for growth, ingress, corrosion and hinge condition — a forensic step that answers questions no sensor placed at the outset could have anticipated.

Phase 4 — Validate and commercialise (M1–M36). Running throughout. Market and requirement input starts at M1, drawn from the commercial engagements the partners already have running, and feeds the requirements specification. The techno-economic model is built early on estimates and progressively replaced with actual invoices and actual production. IP is filed during the project, not after. The demonstrator itself becomes the sales instrument: EDP, Sunlit Sea's Norwegian pipeline and invited European developers visit an operating installation rather than a slide.

What remains uncertain is how the parts behave together, and how they behave over time. Basin tests cannot tell you what a hinge does after ten million cycles, what a PU frame does after two winters of UV and ice, or what it actually costs to moor a breakwater with a local contractor. Only time in water answers those, which is why the operational campaign is the longest single activity and why the budget concentrates on building something worth measuring.

Alternative pathways exist if a risk materialises. The breakwater is modular, so its spacing and draft can be adjusted in the water if attenuation underperforms. The array is modular, so a failed unit can be removed and replaced without disturbing the rest. The validated model chain lets us test a mitigation numerically before committing to it physically. The demonstrator is instrumented redundantly on the critical channels, so a sensor failure does not cost a measurement. And the Letter of Intent with the site owner keeps the end of the campaign open: the parties may either recover the installation or move to a commercial agreement covering price targets and supply terms, so an extension of the operating period is a conversation the site agreement already anticipates.

The result of SUREWAVE is at TRL 4 — technology validated in laboratory. All elements of TRL 4 are complete: the integrated concept has been modelled, the materials characterised, the components tested, and the system validated in two wave-basin campaigns at MARIN under both mild and harsh irregular seas. It is not beyond TRL 4: no version of the integrated system has been built at production scale or operated outside a laboratory, and the connector design that will be manufactured has been characterised in test rigs but never fielded. Assessed on its lowest core subsystem, as required, the result is TRL 4.

The intended end-user application is grid-connected electricity generation on wave-exposed inland water bodies — principally hydropower and water-supply reservoirs — with sheltered coastal water as the adjacent segment. By the end of the project the complete integrated system will have been demonstrated in exactly that environment and will be at TRL 6.

Milestones already achieved: integrated protected-FPV concept developed and optimised · circular concrete formulations developed and characterised · coupled aero-hydrodynamic and non-linear structural models built and validated · two MARIN wave-basin campaigns completed · connector failure mode identified, hinge redesigned and re-tested · mooring and anchoring solutions validated for modular and large-array cases · structural-health-monitoring methodology developed · full technical risk assessment completed.

The milestones that carry the technology to TRL 6, and the evidence that closes each one, are set out in table 3.3d.

The unique selling point — *we make windy water usable for solar, using concrete* — is the protected-array architecture, and this project develops it in three directions: from a basin model to a fielded product; from an engineering claim to a certified one; and from a component into a system whose cost at 10 MW and 50 MW is known rather than assumed.

On gender dimension: the research and innovation content — hydrodynamics, structural response of floating bodies, concrete durability, photovoltaic yield — concerns physical systems with no sex or gender dimension in the analysis. No sex- or gender-based analysis is therefore built into the technical content. Gender is addressed at the level of team composition and project governance: the consortium applies each partner's equality plan, and dissemination and stakeholder-engagement activities will monitor and report the gender balance of participants.

On open science: the project applies openness proportionately to a project whose value is commercial. A Data Management Plan is delivered at M6. Open by default: the metocean characterisation of the site, the wave-attenuation performance dataset, the validated model-error statistics and the peer-reviewed publications arising from them will be deposited in Zenodo under FAIR principles with persistent identifiers, because these are the results that let others build on the science and that regulators and researchers need. Closed by exception: detailed manufacturing drawings, the PU formulation, the hinge geometry, per-unit cost data and the commercial models are withheld under Article 17 of the Model Grant Agreement, as their disclosure would destroy the exploitation the project exists to create. Publications will be open access. The consortium will engage end users directly in defining the requirements specification, which is the co-creation practice most relevant to this project's objectives.

\#§PRJ-OBJ-PO§# \#§REL-EVA-RE§# \#@CON-MET-CM@# \#@COM-PLE-CP@#

---

# 2. Impact \#@IMP-ACT-IA@#

## 2.1 Credibility of the impacts

The business model is simple and is already partly operating: Sunlit Sea sells integrated protected-FPV systems; CLEMENT supplies and installs the breakwater; the customer owns and operates the plant. Revenue accrues to Sunlit Sea per watt-peak of FPV supplied and to CLEMENT per breakwater metre supplied and installed. Secondary streams are engineering services during project development, and licensing of the breakwater design into geographies neither partner will serve directly.

Validation is empirical, not assertive, and follows a defined sequence:

1. Problem/solution fit (M1–M9). The consortium already carries live commercial engagements on wave-limited sites: Sunlit Sea's Northern European pipeline of harbour and sheltered-coastal projects, and EDP's own reservoir portfolio together with the applicant flow into its Floating PV Lab. Those engagements are worked as the primary evidence base, documenting for each site the wave climate at which it becomes unbuildable today and what removing that constraint is worth to its owner. Using deals already in motion keeps the requirement grounded in sites with real budgets and real timelines. Findings feed directly into the requirements specification (D2.1), so the design responds to them rather than preceding them.
2. Value quantification (M9–M30). The techno-economic model converts the measured performance into the only number a customer acts on: delivered LCOE at their site, versus their alternative. Built first on estimates, then rebuilt on the demonstrator's real invoices and real production.
3. Willingness to pay (M24–M34). Site visits to an operating installation, with a costed offer. The test of validation is not enthusiasm but Letters of Intent: ≥ 3 by M34.
4. Business model iteration (M30–M36). The model canvas is revised against what the site engagements and the LOIs actually showed, and the revised version is what the final business plan is built on.

Certification is where the project buys something the consortium cannot buy any other way. Until 2026 floating solar had no certification framework, and that absence has been the single largest obstacle to financing floating solar assets. DNV-RP-0584 covers FPV design, and DNV-ST-C108 (structural) and DNV-ST-E309 (mooring) were released in May 2026. This project is designed to those standards from the first drawing, and DNV is engaged as a subcontractor to perform an independent design-basis review and issue a statement of conformity on the demonstrated system. That artefact is what converts the demonstrator from an interesting result into a bankable one, and it is the reason lenders and insurers will price the first commercial project differently.

The project also generates the operating evidence that insurers require — availability, failure modes, inspection intervals, recovery method — and contributes measured data back to the standards process through SINTEF's and DNV's participation in the relevant technical committees.

The exploitable IP splits into three layers and each is protected differently, deliberately.

Floating solar is a densely patented field, and sheltering a marine structure behind a breakwater is long-established art. Sunlit Sea has searched this landscape for its first-generation product and again for the CONNECT gen. 2 float connection, and the position is settled: the consortium has freedom to operate, and the patentable surface in the protected-array architecture is thin. The exploitation strategy is built accordingly, on three assets that a crowded patent landscape leaves untouched.

*Manufacturing know-how, held as trade secrets.* The polyurethane formulation and its UV-resistant variant, the casting process parameters, the aluminium forming route and the hinge manufacturing tolerances are the difference between a float that survives twenty-five years in water and one that does not. They are difficult to recover from a finished unit, and a patent would publish them. A formal trade-secret register, access control and an employee and subcontractor NDA regime is established under Task 1.4 by M6.

*The validated model chain and the operational dataset.* A competitor can copy a geometry from a photograph; twelve months of instrumented performance across a full seasonal cycle takes twelve months and a demonstrator to reproduce. This is the asset the project creates and the one that compounds, because every subsequent installation extends it. Ownership and access are fixed in the Consortium Agreement before the grant starts, with a specific article guaranteeing each partner the demonstrator data relevant to its exploitation.

*A certification lead.* Sunlit Sea has been verified against DNV-RP-0584 since 2022, and this project carries the design through the standards DNV released in May 2026. Being early to a conformity statement in a field that has only just acquired one is a time-based advantage that a competitor closes by doing the work rather than by designing around a claim.

Freedom to operate for the demonstrator configuration is confirmed at M12 (D1.2) before manufacturing commits, covering Europe, the United States and the principal Asian FPV markets. Filings remain open where the project generates something genuinely novel and defensible — the instrumented hinge and the integrated monitoring arrangement are the candidates most likely to qualify — and the register is reviewed at each Steering Committee rather than at project end.

*Background.* SINTEF, Sunlit Sea and CLEMENT own or hold the SUREWAVE results and bring them as background with the rights needed to commercialise. Foreground arising from the FPV side accrues to Sunlit Sea, from the breakwater and mooring side to CLEMENT, from modelling and monitoring to SINTEF, and from yield and techno-economic methods to EDP, with cross-licences for exploitation defined in the CA.

Patent families

| Patent Applicant | Number | Title of patent | Date of filing/Priority date |
|:---|:---|:---|:---|
| Sunlit Sea AS | — | No granted patents or pending applications. Defensibility is held as manufacturing trade secrets, proprietary performance data and a certification lead, as set out above. | — |

The market has been explored from three independent directions and the answers agree. From the customer side, EDP built its Floating PV Lab because it could not find qualified technology for its harder sites, and EDP has published a target of commercialising at least five new floating solar technologies by end-2027. From the supplier side, Sunlit Sea maintains an active Northern European pipeline including named prospects (Endra, Fagne, Haugaland Næringspark and others) whose sites are wave-limited today. From the competitive side, no supplier currently offers a protected-array architecture for exposed reservoirs; competitors are either strengthening floats for calm water or targeting the far harder offshore segment.

For Sunlit Sea, the reachable segment is European exposed-reservoir and sheltered-coastal FPV. A conservative post-project trajectory is a first commercial installation of 1–5 MWp in 2029–2030 and a cumulative 50–100 MWp supplied by 2033, which at demonstrated system prices represents a business of the order of €40–80 M cumulative revenue and roughly 30–50 direct jobs at Sunlit Sea and comparable numbers at CLEMENT. For EDP, the relevant number is different in kind: unlocking wave-exposed area across a reservoir portfolio that already includes a 70 MW floating-solar award and a 50 GW-by-2030 renewables target.

## 2.2 Economic and/or societal benefits

If this works, the change is specific: wave-limited water surface that is currently unbuildable becomes buildable — inland reservoirs on the one hand, harbours and sheltered coastal water on the other. Reservoir potential at 1 % coverage is on the order of 404 GW, and at 25 % coverage approximately 4 400 GW; a large share of the biggest reservoirs are windy, which is why realised floating solar remains a small fraction of that potential. In coastal cities the constraint is different but the answer is the same: harbours already provide partial wave shelter, and shoreline expansion is a live activity in most of the world's fastest-growing urban regions. Removing the wave constraint does not create either market; it releases two markets that already exist and are already blocked.

The customer-side scale-up is anchored in EDP's own numbers: 32.7 GW of installed capacity, 21.2 GW of it wind and solar as of Q1 2026, targeting more than 50 GW of renewables by 2030 and 100 % renewable production, planning more than €12 bn of investment through 2028 with around 70 % on renewables and storage, and intending to grow its solar presence tenfold. A partner of that size adopting a protected-FPV architecture is a market-making event, not a pilot.

The concrete benefits accrue at several levels.

*Land, not consumed.* Every gigawatt built on water is roughly 1 000–1 500 hectares of land not converted from agriculture or nature. In densely populated Member States, land competition is now the binding constraint on solar deployment, and it is a political constraint as much as a physical one.

*Water, retained.* Reservoir surface coverage reduces evaporation — material in Southern Europe, where the same reservoirs serve irrigation and drinking supply and where drought is a recurring emergency.

*Infrastructure, reused.* Hydropower reservoirs already have grid connection, substation capacity, access roads and an operating licence. Hybridising solar onto them avoids new transmission and new permitting, the two slowest steps in European renewables deployment. EDP's Alqueva installation already demonstrates this pattern, battery included.

*Urban waterfront, activated.* In coastal cities the addressable water is inside or next to harbours, where waterfront land is at its highest value. A concrete breakwater that both attenuates waves and carries inverters, transformers, walkways or public space is a single asset serving two purposes — a cost-basis shift that does not apply to reservoir installations and that turns the wave problem into a piece of city-making.

*Strategic autonomy, concretely.* The value chain here is European end to end: aluminium and float manufacture in Norway, polyurethane and casting in Norway, concrete breakwater in Germany from locally sourced circular mixes, engineering in Norway and Portugal, deployment by a German contractor. Concrete and aluminium floats are heavy and low-value-density — they are not economically importable from Asia. Unlike the PV cell itself, this part of the floating solar value chain can be structurally European, and this project builds exactly that part.

*Circularity and emissions.* The breakwater draws on the concrete formulations developed and characterised in SUREWAVE — lightweight-aggregate, high-performance and cellular variants that reduce clinker content where the service life and cost case allow. The mix used at Hainer See is selected during the project against service performance, cost and CO₂ footprint rather than committed up front. The demonstrator is designed for recovery, and its components are examined after recovery to build the end-of-life evidence base. The Letter of Intent with the site owner provides for the installation to continue in service under a commercial agreement once the research phase ends, as an alternative to recovery. Where that route is taken the avoided decommissioning is both an emissions saving and a cost saving, and the project quantifies it either way.

*Employment.* Manufacturing, casting, marine works and installation are regionally anchored jobs in Norway and in Mecklenburg-Vorpommern and Saxony, in a sector where most component manufacturing has left Europe.

## 2.3 Investment readiness

The go-to-market pathway is direct exploitation by the beneficiaries. Sunlit Sea exploits the FPV system directly as manufacturer and supplier; CLEMENT exploits the breakwater directly as supplier and installer; EDP exploits as adopter and project developer. No spin-off is created — Sunlit Sea already has the manufacturing capability, the product, the certification route and a commercial pipeline. Licensing is a secondary route, used only for geographies neither partner will serve directly.

Investment readiness is built across four dimensions.

*Technology readiness as an investment argument.* An operating, instrumented, independently reviewed installation at TRL 6 changes the diligence conversation from "does it work" to "at what price". This is the largest single item of investment readiness the project delivers, and it is why the budget concentrates on building and instrumenting the demonstrator rather than on further analysis.

*IP readiness.* Confirmed freedom to operate, a formal trade-secret regime, and contractual control of the demonstrator dataset — see §2.1. Investors diligence this layer hardest, and a clear-eyed account of where defensibility actually sits in a crowded field stands up better under that scrutiny than a claim portfolio assembled for the purpose.

*Commercial readiness.* Validated business model, LCOE at three scales built on real costs, at least three Letters of Intent, and a defined first commercial project.

*Team readiness.* The consortium will undertake the EIC Investor Readiness training in year one, and Transition coaching through Business Acceleration Services, including the Tech2Market Business Validation Programme. Once funded, the project also intends to pursue an EIC Booster grant for portfolio activities with other EIC projects and for commercialisation work lying outside this work plan; everything described in this proposal is costed and delivered within the requested lump sum, independently of that. Sunlit Sea will apply through the EIC Accelerator Fast Track route at project end, for which reaching TRL 6 is the qualifying condition.

Validation with users and customers runs through the partners' live site engagements in year one and through visits to the operating demonstrator thereafter — see §2.1. The distinguishing feature is that from M22 the conversation happens *at* a working installation rather than over a specification.

Deployment permits are site-by-site and national. At Hainer See the site is privately held and access is secured: LeipzigSeen GmbH, the lake's owner, and CLEMENT signed a Letter of Intent on 8 September 2026, at CEO level on both sides, covering a floating solar project at the lake as part of this research project and running for the duration of the campaign. Permitting for a floating structure on a private inland lake is a known and short process, and that combination — a willing owner and a short regulatory path — is a principal reason the site was chosen. For the wider market, the binding constraint is not permitting but certification and insurability, which is why the DNV conformity work is treated as a commercial activity rather than a technical one.

First commercial installation is targeted for 2029–2030, immediately following project close, sized 1–5 MWp. Revenue model: equipment supply at a price per watt-peak (Sunlit Sea) and per breakwater metre supplied and installed (CLEMENT), with engineering services during development and O&M support contracts thereafter.

Sunlit Sea intends to raise a growth round of private capital during or immediately after the project, sized to fund manufacturing scale-up from demonstrator volume to multi-megawatt annual output. Preparation is deliberate and is scheduled inside the project: an investment-ready business plan (M36), demonstrator performance data as the core diligence asset, the IP position secured, and at least ten investor meetings held during the project so that the round opens with a warm book rather than a cold one. The EIC Accelerator Fast Track application is prepared in parallel as a non-dilutive complement.

\#§IMP-ACT-IA§#

---

# 3. Quality and efficiency of the implementation \#@QUA-LIT-QL@# \#@CON-SOR-CS@# \#@PRJ-MGT-PM@#

Sunlit Sea AS is the entity responsible for the path to market beyond the project and owns exploitation of the integrated system, supported by CLEMENT Germany GmbH for the breakwater and by EDP as adopter and route to scale.

## 3.1 Quality and motivation of the team

Four partners. Each one is present because it owns a piece of the value chain that cannot be bought in, and the consortium is sized to concentrate budget on the physical demonstrator rather than on coordination.

SINTEF AS (NO) — coordinator, research and validation. One of Europe's largest independent research organisations. Coordinated SUREWAVE. Owns the coupled aero-hydrodynamic and non-linear structural model chain the design depends on, and the monitoring methodology. SINTEF also holds conformity governance for the project, checking each partner's design and documentation against the applicable DNV standards and feeding findings back, and it specifies and operates the instrumentation and telemetry. Coordinates because it has the track record and because the modelling work spans every technical work package.

Sunlit Sea AS (NO) — technology owner and main exploitation partner. Norwegian FPV manufacturer, founded 2019, designing and building floating solar engineered for a 25-year aquatic life. First-generation product deployed at commercial sites; CONNECT gen. 2 is the architecture this project fields. SUREWAVE beneficiary and, separately, partner in Horizon Europe SuRE WP6, where the delivered D6.1 model chain (parametric CAD → structural FEM → thermal CFD → LCA) is the same toolset used here. Design practice has been verified against DNV-RP-0584 since 2022, and in this project SINTEF checks that practice against ST-C108 and ST-E309 and reports back. Sunlit Sea's scope is the floating photovoltaic units themselves — design, manufacture and factory acceptance — together with the reliability knowledge that reads the physical evidence at recovery. Mooring and anchoring, instrumentation and data processing sit with other partners. Sunlit Sea is the company that will sell the product, which is why it holds the largest budget share alongside CLEMENT.

CLEMENT Germany GmbH (DE) — breakwater, mooring and marine works. Rostock-based specialist in floating concrete structures, breakwaters and marinas, with its own production and installation capability. SUREWAVE beneficiary and originator of the circular concrete breakwater. CLEMENT has built two marinas at Hainer See, knows the lake, its logistics and its owner, and has secured the demonstration site under a Letter of Intent signed with LeipzigSeen GmbH on 8 September 2026. That combination — the technology, the manufacturing, and the site relationship in one partner — is why the project can commit to a named site at proposal stage.

EDP (PT) — end user, adopter and route to scale. One of the world's largest renewable energy producers: 32.7 GW installed, 21.2 GW wind and solar, ~12 000 employees across Europe, North and South America and Asia Pacific, targeting >50 GW renewables and 100 % renewable production by 2030 with >€12 bn of investment through 2028. EDP built and operates Alqueva, Europe's largest floating solar plant on a dam reservoir, holds a 70 MW floating-solar award, and runs the open-access Floating PV Lab at Alto Rabagão whose stated purpose is to de-risk and industrialise new floating solar technologies, targeting five commercialised technologies by end-2027. EDP is not a letterhead partner: it brings the requirement, the yield-modelling capability, the techno-economic discipline of an asset owner, and a credible next site.

For Sunlit Sea and CLEMENT this project is the commercial article, not a research exercise — both are SMEs whose product line depends on the outcome. For EDP it addresses a constraint on a portfolio it is actively building. For SINTEF it converts a decade of floating-structure research into a deployed system. All four worked together in SUREWAVE and know each other's delivery.

Interview team. Balram Panjwani (SINTEF, coordinator) · Eirik Larsen (Sunlit Sea) · Thomas Pehlke (CLEMENT) · João Formiga (EDP).

Women-led consortium. ☐ Yes ☒ No.

International participation. All four participants are established in EU Member States or Horizon Europe Associated Countries — Norway (×2), Germany, Portugal — satisfying the requirement for at least one Member State entity and at least two further independent entities in different countries. No third-country participation.

## 3.2 KPIs, milestones and risks

Progress is tracked on nine technology KPIs and six business KPIs, all measurable, all timed, all owned (table 3.3d). Two of them decide the project and are worth calling out.

K2 (wave attenuation) and K3 (load reduction) are the falsifiable core, and the instrumentation is arranged so that both are answered by M30 rather than at project end. K2 in particular is measured rather than inferred: two buoys in the same sea state, one in the incident field and one behind the breakwater, produce the attenuation ratio directly. The 50 % threshold comes from engineering rather than from the basin result: it is the level at which the array can be built to calm-water structural specification, which is where the cost advantage comes from. A measured value below the threshold remains a usable outcome — it sizes the residual load the array has to carry and re-prices the architecture on real data, which is the evidence a customer and an insurer need either way.

The remaining technology KPIs cover production, durability, predictive accuracy and independent confirmation; the business KPIs track the market and investment maturation the EIC requires to run in parallel with the technology. Both sets are defined with target, verification method and month in table 3.3d.

Six milestones (table 3.3d) gate the project at the points where money is committed: design frozen (M6), design verified and released to manufacture (M12), components accepted (M20), system commissioned (M22), performance thesis proven (M30), and validation plus commercial readiness complete (M36). Under lump-sum funding each work package is declared complete or not complete, so the milestones are placed to align with work-package closure.

Ten critical risks are carried in table 3.3e. Three deserve narrative treatment because they are the ones a reviewer should press us on.

*The site is a lake, and the ambition includes coastal water.* Hainer See reproduces the wave and wind load envelope of the target market — fetch-driven short steep seas on a large inland water body — which is the load case that defines the product. It does not reproduce salinity, biofouling, tidal range, or the longer-period swell that reaches a coastal harbour from offshore. We treat that explicitly rather than glossing it: the project runs a parallel accelerated salt-spray, immersion and UV programme at an accredited laboratory on production-representative assemblies (K9), Sunlit Sea's existing Gen 1 units already operate in Norwegian salt water, and the validated model chain is exercised across the full marine load envelope — swell periods included — even where the demonstrator does not reach it. Swell is the more tractable of the two wave mechanisms for this architecture, since it arrives from a narrow sector that a directional breakwater is built to intercept; the demonstrator measures the harder case, which is the short, steep, multi-directional fetch sea. TRL 6 is claimed for the exposed-inland-water application, which is the primary market and the one EDP buys in; coastal deployment is stated as the adjacent segment, not as a claim of this project.

*Environmental conditions may be milder than design during the campaign.* Twelve months may not contain a design-level event. Mitigation: the monitoring set is dimensioned to extract fatigue-relevant statistics from ordinary conditions rather than relying on extremes; measured response is extrapolated using models validated against the conditions that did occur, with the extrapolation error quantified; and an extension of the operating period is available by agreement with the site owner, whose Letter of Intent already contemplates continuing beyond the research phase.

*Budget concentration on manufacturing.* Roughly 47 % of the grant sits in WP4, because both hardware beneficiaries manufacture in it. This is deliberate — the data the project exists to produce cannot be better than the object that produces it — but it means a manufacturing overrun has no slack behind it. Mitigation: fixed-price subcontracts for the cast-PU work and the breakwater materials, factory acceptance gates before shipment, and a design frozen at M12 with formal change control thereafter.

## 3.3 Work plan and resources \#@WRK-PLA-WP@#

The work plan is six work packages over 36 months, in two reporting periods (RP1 M1–M12, RP2 M13–M36), consistent with the template's reporting-period table for a 36-month project. The structure follows the physical logic of the project: engineer it (WP2), verify it (WP3), build it (WP4), operate it (WP5), sell it (WP6), with management and IP throughout (WP1).

WP2 delivers the design basis and detailed design in the first year, verified in parallel by WP3, which continues to project end as the model-validation stream. WP4 begins at M7 on long-lead procurement, overlapping the last of WP2, and closes at M20 with factory acceptance. WP5 starts at M15 with installation planning and site preparation, deploys at M21–M22, and runs the operational campaign to M34. WP6 runs M1–M36 in parallel; its early customer work feeds WP2's requirements, and its later work consumes WP5's operational data. The critical path runs WP2 → WP4 → WP5, and the two points where it can slip are the design freeze at M12 and the installation weather window at M21–M22, both of which are milestone-gated.

*A Gantt chart and a PERT diagram are to be inserted here at layout stage.*

Total effort is 160 person-months and the requested lump sum is €2 480 000. Budget follows the physical deliverable rather than the org chart: Sunlit Sea and CLEMENT hold equal and largest shares because between them they design, manufacture, deliver and install everything that goes in the water; SINTEF holds half of one of those shares, sufficient for coordination plus a focused modelling and validation programme; EDP holds a third of one, sufficient for yield modelling, techno-economics and the business track it leads. Subcontracting totals €262 000 (10.6 %) and covers only work no beneficiary should perform on itself — independent certification review — or specialist capability none holds in house.

\#§CON-SOR-CS§# \#§PRJ-MGT-PM§#

---

## Tables for section 3.3

### Table 3.3a: List of work packages

| WP No | Work Package Title | Lead | PMs | Start | End |
|:--|:--|:--|:--|:--|:--|
| WP1 | Management, IP and innovation management | SINTEF | 16 | M1 | M36 |
| WP2 | Site characterisation and demonstrator engineering | Sunlit Sea | 31 | M1 | M12 |
| WP3 | Design verification and model validation | SINTEF | 25 | M1 | M34 |
| WP4 | Manufacturing, instrumentation and factory acceptance | Sunlit Sea | 36 | M7 | M20 |
| WP5 | Deployment, operation and validation campaign | CLEMENT | 27 | M15 | M34 |
| WP6 | Business validation, exploitation and dissemination | EDP | 25 | M1 | M36 |
| | Total PMs | | 160 | | |

### Table 3.3b: Work package description

---

Work package number: 1 · Work package title: Management, IP and innovation management (SINTEF) · M1–M36

Objectives. Deliver the project on time, on budget and in compliance; manage the intellectual property that is the project's principal output; and run the risk process.

*Task 1.1 — Administrative, financial and legal coordination (L: SINTEF; P: all; M1–M36).* Consortium Agreement in force before the grant starts, including the data-access article guaranteeing each partner the demonstrator data relevant to its exploitation. Quality Management Plan at M2. Liaison with the Agency, two periodic reports (M12, M36). Lump-sum work-package completion evidence maintained continuously rather than assembled at reporting time.

*Task 1.2 — Technical coordination and risk management (L: SINTEF; P: all; M1–M36).* Kick-off at M1; Steering Committee twice yearly; Technical Committee monthly during WP2 and WP4, monthly during the deployment window, quarterly otherwise. Risk register reviewed at every Steering Committee against table 3.3e. Formal design-change control after the M12 freeze.

*Task 1.3 — Data management (L: SINTEF; P: all; M1–M36).* Data Management Plan at M6 implementing the open-by-default / closed-by-exception split in §1.3. Repository, metadata schema and retention policy established before the first demonstrator data arrives.

*Task 1.4 — IP and innovation management (L: Sunlit Sea; P: all; M1–M36).* IP register and trade-secret regime by M6. Freedom-to-operate confirmation for the demonstrator configuration at M12, before manufacturing commits. Novelty reviewed at each Steering Committee, with filings made where a defensible claim emerges. Ongoing coordination with the EIC Programme Manager and Business Acceleration Services, including Investor Readiness training in year one.


---

Work package number: 2 · Work package title: Site characterisation and demonstrator engineering (Sunlit Sea, with CLEMENT co-leading the breakwater and mooring scope) · M1–M12

Objectives. Turn the SUREWAVE laboratory result into a manufacturable, installable, site-specific demonstrator design, frozen at M12 and documented to DNV-ST-C108 and DNV-ST-E309 under SINTEF's conformity governance.

*Task 2.1 — Requirements specification (L: Sunlit Sea; P: all; M1–M6).* Consolidates demonstration objectives, the Hainer See design basis, regulatory constraints and — importantly — the first WP6 market input into one system requirements document. Covers array size and layout, module and electrical interface constraints (standard commercial 710–740 Wp, 2384 × 1303 mm), environmental design envelope mapped to DNV-RP-0584 exposure categories, the mechanical interface between array and breakwater, transport and installation constraints from Norway to Saxony, instrumentation requirements, and the certification-alignment requirements that govern all downstream documentation, which SINTEF specifies and maintains. D2.1 at M6, and MS1.

*Task 2.2 — Site characterisation and metocean design basis (L: CLEMENT; P: SINTEF, EDP; M1–M6).* Bathymetric and geotechnical survey of the deployment area. Long-term wind and wave climate from hindcast, validated against local measurement, expressed as directional scatter diagrams, joint probability tables and seasonal occurrence statistics. Water-level variation, ice statistics, access routes, grid interface point. Feeds T2.3, T2.4 and WP3.

*Task 2.3 — FPV platform detailed design (L: Sunlit Sea; P: SINTEF; M4–M12).* Detailed design of the array from the CONNECT gen. 2 architecture: 0.8 mm aluminium 5083-H111 bottom plate, cast polyurethane frame, PU-foam infill and connector rods, 2° tilt with the lowest edge 60 mm above water. Site-specific adaptation along four dimensions — array layout (parametric CAD models exported to SINTEF for coupled simulation in T3.1 and iterated to balance hydrodynamic behaviour, installation, maintenance access and mooring load distribution); mixed operational and dummy modules, the dummies matched in mass and hydrodynamic character so that load-representative fill is achieved while carrying the units that are opened and measured at recovery; the electrical interface and array routing agreed with EDP; and the mechanical interface at which the array attaches to the mooring arrangement CLEMENT designs under T2.4. D2.2 at M12.

*Task 2.4 — Breakwater and mooring design (L: CLEMENT; P: SINTEF; M4–M12).* Optimisation of the breakwater geometry, module arrangement, buoyancy and ballast for the Hainer See wave climate and the demonstrator's scale, evaluated against the WP3 models for attenuation, transmitted load and survivability. Site-specific mooring and anchoring design for both operating and extreme conditions, with dynamic analysis of line tensions, anchor loads and excursions, and an installation and inspection method. Design loads, manufacturing specifications and installation requirements released to WP4. D2.3 at M12.


---

Work package number: 3 · Work package title: Design verification and model validation (SINTEF) · M1–M34

Objectives. Verify the demonstrator design numerically before it is built, and afterwards establish — with a number — how accurately the model chain predicts the real system. Scope is deliberately confined to these two purposes; the models themselves were developed and validated in SUREWAVE and are not redeveloped here.

*Task 3.1 — Integrated design verification (L: SINTEF; P: Sunlit Sea, CLEMENT; M3–M12).* Coupled aero-hydrodynamic analysis (CFD, SPH, MoorDyn) and non-linear structural FEM of the complete breakwater-array-mooring system over the Hainer See load cases, plus the marine load envelope for the adjacent-market claim. Quantifies attenuation, array motions, connector and mooring loads, and survivability. Iterates with T2.3 and T2.4 until the configuration meets the design targets, then issues the verification that releases manufacture at MS2. D3.1 at M12.

*Task 3.2 — Energy yield modelling (L: EDP; P: Sunlit Sea, SINTEF; M4–M18).* Site-specific yield methodology for FPV on exposed inland water, combining irradiance, electrical, optical and thermal models with the effects specific to this application: platform motion, water-surface cooling, humidity, soiling, albedo and reflection. Establishes the pre-operational production baseline and the parameters that dominate yield uncertainty and hence bankability. Benchmarked by EDP against its own operating floating solar assets. D3.2 at M18.

*Task 3.3 — Model validation against operational data (L: SINTEF; P: all; M24–M34).* Compares measured environment, motions, structural loads, mooring tension and energy production against the predictions from T3.1 and T3.2. Calibrates the models, quantifies prediction error, sensitivity and confidence intervals, and issues the validated model chain with a stated accuracy — the artefact that lets a customer dimension a 50 MW array without building one. D3.3 at M34.


---

Work package number: 4 · Work package title: Manufacturing, instrumentation and factory acceptance (Sunlit Sea leads FPV manufacture; CLEMENT leads breakwater and mooring manufacture; SINTEF leads instrumentation and telemetry) · M7–M20

Objectives. Build the demonstrator to industrial standard, procure and prepare the measurement system, and prove every component before it ships. This work package carries the largest share of the budget because the quality of every result in WP5 is set here.

*Task 4.1 — Instrumentation specification (L: SINTEF; P: CLEMENT, Sunlit Sea, EDP; M7–M9).* Specifies the monitoring set so procurement can start. Two instrumented buoys carry inertial measurement units, one moored outside the breakwater and one inside, so attenuation is read directly as a ratio between two measurements in the same sea state. They deploy early, in the T2.2 site characterisation, so the design basis rests on measured wave data rather than hindcast. Load cells in the mooring and anchoring measure structural loading where the environmental load is reacted. Energy performance is read at the inverter — per-string DC and AC-side output — against a pyranometer with integrated thermal sensor at the array. Wind data comes from a site sensor or a nearby meteorological station. A camera serves security and gives a dated visual record between inspections. Reliability evidence comes from recovering and examining the units, not from sensors inside them. Instruments are chosen for proven service life, standard interfaces and a power and service profile suited to an installation reached by boat. Sampling rates and retention preserve the frequency content fatigue analysis needs within the site uplink. The specification carries the telemetry requirement T4.4 implements: what streams continuously, what records at high rate, what must be time-synchronised. Frozen at M9.

*Task 4.2 — FPV manufacturing (L: Sunlit Sea; M9–M18).* Manufacture of the demonstrator array to the T2.3 design: aluminium bottom plates, cast PU frames (subcontracted to a qualified specialist), PU-foam infill and connector rods, standard commercial modules, dummy modules, and integrated connection systems, built sealed and to production specification. Industrial production methods, inline dimensional and electrical inspection, and a serialised documentation package per unit for traceability into certification. D4.2 at M18.

*Task 4.3 — Breakwater and mooring manufacturing (L: CLEMENT; M9–M18).* Casting of the breakwater modules in the concrete formulation selected under T2.4, fabrication of connectors, transition elements and hinges, and procurement of mooring lines and anchors. Dimensional tolerance, cover, curing and durability control to the standards CLEMENT applies to its commercial marine structures, with records maintained for certification. D4.3 at M18.

*Task 4.4 — Telemetry and monitoring platform (L: SINTEF; P: all; M9–M18).* Builds the path from instrument to analyst and keeps it open for the whole campaign.

Getting the data off the water. The two wave buoys run standalone on battery with a small solar panel, each carrying a cellular modem; where coverage at the water surface proves marginal they fall back to a short-range radio link to a gateway on the breakwater. The mooring and anchoring load cells, the pyranometer and the camera draw power from the installation and report to the same gateway. Every node buffers locally, so a dropped connection costs latency rather than data and back-fills when the link returns.

Rates and time base. Ten-minute summary statistics stream continuously on every channel. The wave and load channels additionally record high-rate bursts, triggered both on schedule and on threshold, and the two buoys share a common time base so that inside and outside records can be paired within the same sea state — the condition K2 rests on. The camera delivers scheduled stills continuously and a live feed on demand, keeping video inside the site uplink budget while leaving full-motion viewing available when someone needs it.

Access. Everything lands in one store with a documented schema, reachable two ways. A web dashboard gives every partner live values, time series, alarm state and the camera feed from any browser. A programmatic interface serves the same data directly, so that the model validation in T3.3, the yield work in T3.2 and the reliability analysis in T5.4 all query the source rather than passing exports between partners. Alarm thresholds are set on mooring load, array motion, power loss, sensor dropout and camera motion, with notification to the on-call partner.

The dashboard carries a second job on the commercial side: visitors hosted at the demonstrator under T6.1 see the installation and its live behaviour together, which is a more convincing artefact than either on its own.

The platform is exercised end to end on synthetic and laboratory data before it is connected to anything real, and is commissioned with the system at MS4, with acceptance recorded in D5.2.

*Task 4.5 — Factory acceptance testing (L: Sunlit Sea; P: CLEMENT; M16–M20).* Written FAT protocols executed before shipment. FPV side: dimensional check against released drawings, PU-frame and hinge geometry, aluminium flatness and edge quality, DC insulation and string continuity, module electroluminescence for micro-crack screening, terminal-box IP verification, and an accelerated water-ingress test on a sample of production units. SINTEF calibration-checks and function-tests the measurement system — buoys, mooring load cells, pyranometer and camera — separately before deployment. Breakwater side: dimensional and mass verification, buoyancy and freeboard check, connector fit-up. Nothing ships without a signed acceptance record. D4.4 at M20, and MS3.

*Task 4.6 — Accelerated ageing of the gen 2 materials (L: Sunlit Sea; M12–M30).* The campaign puts the units in water for twelve months; the product is sold on a twenty-five year design life, and accelerated ageing is the bridge between the two. Production-representative assemblies — cast PU frame in its UV-resistant formulation, aluminium bottom plate and edge treatment, and the hinge bond line — are aged at an accredited laboratory under UV, thermal and freeze-thaw cycling and prolonged immersion, with mechanical and bond-strength testing before and after. Freeze-thaw and UV are the dominant ageing mechanisms at Hainer See itself, where winters freeze, so these results read directly onto the demonstrator's own service life and onto the warranty terms in T5.4. One strand of the programme runs saline immersion and salt-spray, extending the durability evidence to the sheltered-coastal segment without waiting for a second demonstrator; Sunlit Sea's first-generation units already operating in Norwegian salt water give the field reference against which that strand is read.


---

Work package number: 5 · Work package title: Deployment, operation and validation campaign (CLEMENT) · M15–M34

Objectives. Install the demonstrator at Hainer See, operate it for at least twelve months, recover it, and produce the measured evidence that the whole project rests on.

*Task 5.1 — Site preparation, permitting and installation planning (L: CLEMENT; P: all; M15–M20).* Secures the permits and agreements for installation and operation at Hainer See, building on the site owner's confirmation and CLEMENT's existing relationship with the lake. Site-specific HSE and risk assessment. Installation and operations plan: assembly sequence, transport logistics from Norway and Rostock, lifting and towing method, mooring pre-lay, weather-window criteria, commissioning procedure, maintenance and inspection schedule, and emergency response. D5.1 at M20.

*Task 5.2 — Installation and commissioning (L: CLEMENT; P: all; M21–M22).* Mooring pre-laid, breakwater modules towed and connected, array assembled and moored inside the protected zone, electrical integration and grid connection, monitoring system connected and verified. Full commissioning and functional test of structural, electrical and monitoring systems. D5.2 at M22, and MS4.

*Task 5.3 — Operational campaign (L: CLEMENT; P: all; M22–M34).* At least twelve months of continuous operation with continuous monitoring. Planned inspections at M26 and M30, including opening a subset of units for internal condition assessment. Maintenance and interventions logged with time and cost so that the O&M model is built from record rather than estimate. Delivers the wave-attenuation and structural-load evidence for K2 and K3 at M30. D5.3 at M30.

*Task 5.4 — Reliability and durability assessment (L: SINTEF; P: all; M24–M34).* Analyses the reliability streams: water ingress, biological growth, corrosion, PU degradation, connector and hinge condition, electrical reliability and availability, drawing on the operational record during the campaign and on the recovery forensics in T5.5. SINTEF performs the data analysis on the platform it built in T4.4. Sunlit Sea contributes the product and manufacturing knowledge needed to read the physical evidence — what a given degradation pattern says about formulation, forming route or bond line — and CLEMENT does the same for the breakwater and mooring hardware. Failure modes and degradation mechanisms identified and quantified into a reliability database supporting warranty terms and the O&M cost model. Includes the T4.6 accelerated-exposure results.

*Task 5.5 — Recovery and post-campaign forensics (L: CLEMENT; P: all; M33–M34).* The array is recovered, disassembled and examined unit by unit. Biological growth is recorded and sampled. Water ingress is measured by weighing each unit against its factory-recorded dry mass, giving a quantity for every unit rather than presence-or-absence from a sampled few. PU frames and aluminium bottoms are inspected for degradation. The hinge bond line receives particular attention: SURE testing established that delamination occurs only where wave forces exceed what the absorption arrangement can take, so its presence or absence after a full seasonal cycle is a direct verdict on the protected-array configuration. Read with the mooring load record, the buoy pair, the validated models and the SURE laboratory characterisation, this carries the hinge assessment without instrumenting the hinge in the field. Recovery is planned and costed on the assumption the installation is removed; where the parties instead take the commercial route the Letter of Intent provides for, it stays in service. Either outcome is quantified for the LCA and cost model. Results feed T5.4 and T3.3.


---

Work package number: 6 · Work package title: Business validation, exploitation and dissemination (EDP) · M1–M36

Objectives. Mature the business case in parallel with the technology, and finish the project investment ready.

*Task 6.1 — Market and customer validation (L: EDP; P: Sunlit Sea, all; M1–M34).* Validation is built on engagements the partners are already running rather than on a separate research exercise. In year one, Sunlit Sea's Northern European harbour and sheltered-coastal pipeline and EDP's reservoir portfolio and Floating PV Lab applicant flow are documented site by site: wave climate, the threshold at which the site becomes unbuildable with conventional FPV, grid and permitting context, and what removing the wave constraint is worth to the owner. This establishes the requirement base for T2.1 and the segment map for T6.2. From M22 the demonstrator becomes the validation instrument: qualified prospects, developers, utilities and port authorities are hosted on site, each visit closing with a short structured debrief that is logged against the segment map. D6.1 at M9, updated at M34.

*Task 6.2 — Techno-economic analysis and scale-up (L: EDP; P: all; M6–M30).* CAPEX and OPEX collected from every partner and, from M22, replaced with the demonstrator's actual invoices and actual production. Cost models and scale-up scenarios for 1 MW, 10 MW and 50 MW plants. LCOE, NPV, IRR and payback under alternative market conditions, with sensitivity on wave exposure, depth, yield, grid connection, lifetime, electricity price, financing and O&M. Benchmarked against EDP's operating floating solar assets and published data. D6.2 at M30.

*Task 6.3 — Business model and commercialisation roadmap (L: Sunlit Sea; P: EDP, all; M6–M36).* Business model canvas at M12, iterated at M30 against site-engagement and LOI evidence. Segment prioritisation, value proposition, pricing, channel strategy, partnership structure, certification pathway, market-entry barriers and manufacturing scale-up plan. Concludes in the investment-ready business plan. D6.3 at M12, D6.5 at M36.

*Task 6.4 — Site comparison and replication study (L: EDP; P: all; M1–M30).* Runs in two stages.

The first stage, M1–M6, compares the German baseline with the Portuguese candidate sites EDP brings, against criteria fixed at the outset: technical suitability against the design load envelope, deployment and logistics cost, permitting requirements and timeline, grid interface, and exploitation potential after the project. Hainer See enters as the baseline, with site access already secured under a signed Letter of Intent and a short permitting route on a privately held lake. The comparison puts on the record what an alternative would cost in time and money, and closes before the design basis freezes at M6. WP2 works to the Hainer See design basis throughout, so the assessment runs alongside the engineering rather than ahead of it and consumes no schedule.

The second stage, M6–M30, takes the demonstrated system and assesses its transfer to EDP's own portfolio and to Southern European reservoir conditions, using the Portuguese sites and the Alto Rabagão Floating PV Lab as reference cases. It covers metocean differences, permitting regimes, grid interface, logistics, cost deltas and the modifications required, and produces a costed site-transfer assessment, a European replication map, and the definition of the first post-project commercial installation. This is the bridge from a German demonstrator to an EDP deployment.


*Task 6.5 — Investor and stakeholder engagement (L: Sunlit Sea; P: EDP; M12–M36).* At least ten investor meetings drawing on Sunlit Sea's Northern European network. Customer engagement with the named Norwegian pipeline and with EDP-introduced developers, structured around site visits to the operating demonstrator from M22. Target: three Letters of Intent by M34. Preparation of the EIC Accelerator Fast Track application.

*Task 6.6 — Dissemination and communication (L: SINTEF; P: all; M1–M36).* Project website and visual identity by M3. Peer-reviewed publications on wave attenuation, model validation and yield, open access. Conference presence at floating-solar and marine-renewables events. Demonstration events at the site. Engagement with DNV technical committees and relevant industry associations to feed measured data into the standards process. Plan for dissemination and exploitation at M6. D6.6 at M6.


---

### Table 3.3c: List of deliverables

| Number | Deliverable name | WP | Lead | Type | Diss. | Month |
|:--|:--|:--|:--|:--|:--|:--|
| D1.1 | Data Management Plan | WP1 | SINTEF | DMP | PU | 6 |
| D1.2 | IP strategy and freedom-to-operate report | WP1 | Sunlit Sea | R | SEN | 12 |
| D2.1 | System requirements specification | WP2 | Sunlit Sea | R | SEN | 6 |
| D2.2 | FPV platform detailed design | WP2 | Sunlit Sea | R+DATA | SEN | 12 |
| D2.3 | Breakwater and mooring design package | WP2 | CLEMENT | R | SEN | 12 |
| D3.1 | Design verification report | WP3 | SINTEF | R | SEN | 12 |
| D3.2 | Energy yield assessment | WP3 | EDP | R | SEN | 18 |
| D3.3 | Model validation report | WP3 | SINTEF | R | PU | 34 |
| D4.1 | Instrumentation specification | WP4 | SINTEF | R | SEN | 9 |
| D4.2 | FPV manufacturing completion report | WP4 | Sunlit Sea | DEM | SEN | 18 |
| D4.3 | Breakwater manufacturing completion report | WP4 | CLEMENT | DEM | SEN | 18 |
| D4.4 | Factory acceptance test report | WP4 | Sunlit Sea | R | SEN | 20 |
| D5.1 | Installation and operations plan | WP5 | CLEMENT | R | SEN | 20 |
| D5.2 | Deployment and commissioning report | WP5 | CLEMENT | DEM | PU | 22 |
| D5.3 | Interim performance and structural validation report | WP5 | SINTEF | R | SEN | 30 |
| D5.4 | Final performance, reliability and lessons-learned report | WP5 | SINTEF | R | PU | 34 |
| D6.1 | Market and customer validation report | WP6 | EDP | R | SEN | 9 |
| D6.2 | Techno-economic and scale-up assessment | WP6 | EDP | R | PU | 30 |
| D6.3 | Business model canvas | WP6 | Sunlit Sea | R | SEN | 12 |
| D6.4 | Replication study and first-project definition | WP6 | EDP | R | SEN | 30 |
| D6.5 | Investment-ready business plan and commercialisation roadmap | WP6 | Sunlit Sea | R | SEN | 36 |
| D6.6 | Dissemination, exploitation and communication plan | WP6 | SINTEF | DEC | PU | 6 |
| D6.7 | Comparative site assessment | WP6 | EDP | R | SEN | 6 |

### Table 3.3d: List of KPIs and milestones

Milestones

| MS | Milestone name | WP(s) | Month | Means of verification |
|:--|:--|:--|:--|:--|
| MS1 | Design basis frozen | WP2, WP6 | 6 | D2.1 accepted; site design basis complete; comparative site assessment closed and the demonstration site confirmed (D6.7); first WP6 market findings incorporated |
| MS2 | Design verified and released to manufacture | WP2, WP3 | 12 | D2.2, D2.3, D3.1 accepted; design targets met numerically; change control in force |
| MS3 | Components manufactured and accepted | WP4 | 20 | D4.2, D4.3, D4.4 accepted; every unit carries a signed acceptance record; sensors calibrated |
| MS4 | Demonstrator commissioned and generating | WP5 | 22 | D5.2 accepted; system grid-connected; all monitoring streams live |
| MS5 | Performance quantified against design targets | WP5, WP3 | 30 | K2 attenuation and K3 load reduction measured across the encountered sea states and reported against target in D5.3; D6.2 delivered |
| MS6 | TRL 6 and commercial readiness achieved | all | 36 | D3.3, D5.4, D6.5 accepted; DNV statement of conformity issued; ≥ 3 LOIs held |

Key performance indicators

| KPI | Description | Target | Verified by | Month |
|:--|:--|:--|:--|:--|
| K1 | Demonstrator built and commissioned | Small-scale protected FPV array, grid-connected | D5.2 | 22 |
| K2 | Significant wave height reduction at the array | ≥ 50 % at design Hs | Paired IMU buoys, one outside the breakwater and one inside | 30 |
| K3 | Peak mooring and anchoring load vs. unprotected prediction | ≤ 50 % | Mooring and anchoring load cells vs. T3.1 | 30 |
| K4 | System availability over the campaign | ≥ 95 % | SCADA and inverter logs | 34 |
| K5 | Performance ratio | ≥ 0.80 | Inverter-metered production vs. pyranometer irradiance at the array | 34 |
| K6 | Water ingress per unit at recovery, by mass gain against factory-recorded dry weight | Within the acceptance threshold set at FAT | Post-recovery weighing under T5.5 | 34 |
| K7 | Model prediction error, motions, loads and yield | ≤ 20 % | D3.3 | 34 |
| K8 | Independent conformity | DNV statement of conformity issued | DNV | 34 |
| K9 | Accelerated ageing programme supporting the 25-year design life | Completed on production-representative assemblies, with before-and-after mechanical and bond-strength results | Accredited laboratory report | 30 |
| B1 | Organisations hosted at the operating demonstrator | ≥ 15 | D6.1 (M34 update) | 34 |
| B2 | Demonstration events held at the site | ≥ 3 | D6.6 | 34 |
| B3 | LCOE quantified at 1, 10 and 50 MW | 3 scales, built on demonstrator cost data | D6.2 | 30 |
| B4 | Defensibility secured | FTO confirmed for the demonstrator configuration; trade-secret regime in force; data-access article executed in the CA | D1.2 | 12 |
| B5 | Letters of Intent for post-project installations | ≥ 3 | Signed LOIs | 34 |
| B6 | Investor engagement and investment readiness | ≥ 10 investor meetings; business plan delivered | D6.5 | 36 |

### Table 3.3e: Critical risks for implementation \#@RSK-MGT-RM@#

| Description of risk (Likelihood / Severity) | WP(s) | Proposed risk-mitigation measures |
|:--|:--|:--|
| R1. Wave attenuation or load reduction falls short of the 50 % targets. (Medium / High) | WP2, WP3, WP5 | Configuration verified numerically before build (T3.1); breakwater is modular so spacing, draft and ballast can be adjusted in the water; measured shortfall is diagnosed against the model and the design envelope is restated with quantified performance rather than abandoned. |
| R2. A freshwater site evidences the load envelope of the target market but leaves salinity and biofouling to be shown by other means for the adjacent coastal segment. (High / Medium) | WP4, WP6 | Accepted and addressed by design: the saline strand of the accelerated ageing programme (T4.6, K9); Sunlit Sea's first-generation units already in service in Norwegian salt water; the validated model chain exercised across the marine load envelope. TRL 6 is claimed for exposed inland water, with coastal stated as the adjacent segment. |
| R3. Manufacturing or long-lead delivery delay pushes the installation past the weather window. (Medium / High) | WP4, WP5 | Design frozen at M12 with change control; long-lead procurement starts M7; fixed-price subcontracts; FAT gate at M20 with four months of float to the M21–M22 window; alternative spring window identified. |
| R4. Manufacturing cost overrun in the budget-heavy WP4. (Medium / High) | WP4 | Fixed-price subcontracts for cast-PU and breakwater materials; scope defined per unit; instrumentation density is the designed flex, reducible without affecting the structural build. |
| R5. Instrumentation or data-platform failure loses operational data. (Medium / High) | WP4, WP5 | Redundant sensors on the K2/K3 critical channels; every sensor calibration-verified at FAT; remote sensor-health monitoring; local buffering with cloud sync; planned inspections at M26 and M30 allow replacement. |
| R6. Structural degradation, water ingress or component failure during operation. (Medium / Medium) | WP4, WP5 | Continuous mooring-load and motion monitoring, site camera and scheduled physical inspection at M26 and M30; modular array allows a failed unit to be removed and replaced without disturbing the array; failures are a project output, not only a project risk, and feed T5.4. |
| R7. Milder-than-design conditions during the campaign limit the validation envelope. (Medium / Medium) | WP3, WP5 | Monitoring dimensioned to extract fatigue statistics from ordinary conditions; model-based extrapolation with quantified error; operating period extendable at low cost because the site owner retains the breakwater. |
| R8. Permitting or site-access delay at Hainer See. (Low / High) | WP5 | Site secured with the owner in writing before submission; CLEMENT has built two marinas on the lake and holds the local relationships; private inland water body with a short permitting route; German permitting consultant subcontracted; T5.1 starts M15, six months ahead of installation. |
| R9. Energy yield below prediction from soiling, shading, humidity or degradation. (Medium / Medium) | WP3, WP5 | Module-level monitoring on a subset for spatial diagnosis; yield model validated and losses attributed rather than aggregated; results feed the bankability case either way. |
| R10. Market uptake or investor interest insufficient after the project. (Low / High) | WP6 | Customer engagement from M1, not M24; an end user with a 70 MW award inside the consortium; demonstrator used as a live sales instrument from M22; LOIs as a tracked KPI; certification pathway addressed as the actual barrier to financing. |

### Table 3.3f: Summary of staff effort

*Person-months over the whole duration, per work package and participant. Work-package leader shown in bold.*

| Participant | WP1 | WP2 | WP3 | WP4 | WP5 | WP6 | Total PM |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 1 — SINTEF (coordinator) | 7 | 3 | 9 | 5 | 3 | 1 | 28 |
| 2 — Sunlit Sea | 3 | 16 | 4 | 34 | 8 | 9 | 74 |
| 3 — CLEMENT Germany | 2 | 8 | 2 | 6 | 12 | 2 | 32 |
| 4 — EDP | 2 | 3 | 5 | 1 | 4 | 11 | 26 |
| Total Person-Months | 14 | 30 | 20 | 46 | 27 | 23 | 160 |

Requested lump sum per participant and work package (€)

| Participant | WP1 | WP2 | WP3 | WP4 | WP5 | WP6 | Total |
|:--|--:|--:|--:|--:|--:|--:|--:|
| SINTEF | 102 000 | 30 000 | 150 000 | 118 000 | 30 000 | 10 000 | 440 000 |
| Sunlit Sea | 24 000 | 128 000 | 32 000 | 555 000 | 64 000 | 72 000 | 875 000 |
| CLEMENT Germany | 17 000 | 68 000 | 17 000 | 471 000 | 285 000 | 17 000 | 875 000 |
| EDP | 19 000 | 33 500 | 47 500 | 9 500 | 44 000 | 136 500 | 290 000 |
| Total | 162 000 | 259 500 | 246 500 | 1 153 500 | 423 000 | 235 500 | 2 480 000 |

### Table 3.3g: 'Subcontracting costs' items

*For each participant, tasks to be subcontracted and their justification. No core task of the project is subcontracted.*

| Participant | Cost (€) | Description of tasks and justification |
|:--|--:|:--|
| 1 — SINTEF | | |
| Subcontracting | 60 000 | Independent design-basis review and statement of conformity (DNV or equivalent notified body) against DNV-RP-0584, DNV-ST-C108 and DNV-ST-E309. Must be performed by a body independent of the designers; a beneficiary cannot certify its own design. This is an investment-readiness deliverable, not a technical one. |
| 2 — Sunlit Sea | | |
| Subcontracting | 105 000 | Cast polyurethane frame production and supplier qualification (€55 000) — specialist casting capability, including tool-set adjustment, first-article inspection and qualification of the UV-resistant formulation; Sunlit Sea holds the design, not the casting plant. Accredited accelerated ageing programme (€35 000) — UV, thermal and freeze-thaw cycling, immersion and a saline strand, with mechanical and bond-strength testing; an accredited laboratory is required for results that support a twenty-five year design-life claim. Peak assembly labour (€15 000) — temporary capacity during the M16–M18 build peak to hold the delivery date without compromising quality control. |
| 3 — CLEMENT Germany | | |
| Subcontracting | 85 000 | Permitting and environmental consultancy, Saxony (€25 000) — local water-body permitting and environmental screening requires a locally licensed consultant. Electrical contractor for grid connection and AC-side works (€45 000) — local certified electrical works at the point of connection; regulated activity requiring German certification. Independent installation review / marine warranty surveying (€15 000) — independent verification of the installation method, required for insurance of the floating asset. |
| 4 — EDP | | |
| Subcontracting | 12 000 | Communication and design agency (€12 000) — video, technical briefs and case-study production for dissemination; specialist creative capability not held in house. |
| Total subcontracting | 262 000 | 10.6 % of the requested lump sum. |

### Table 3.3h: 'Purchase costs' items

*Completed for participants whose purchase costs exceed 15 % of their personnel costs.*

| Participant 2 — Sunlit Sea | Cost (€) | Justification |
|:--|--:|:--|
| Cast PU raw materials | 45 000 | Frame, interior foam and connector rods for the full array, including formulation-trial quantity for the UV-resistant variant. |
| Standard commercial PV modules | 38 000 | Glass/glass 710–740 Wp modules for the demonstrator array. |
| Production tooling | 38 000 | Moulds, jigs and fixtures at production quality, including hinge-placement jigs. Required to manufacture at consistent tolerance rather than prototype tolerance. |
| Aluminium 5083-H111 sheet, 0.8 mm | 26 000 | Bottom plates for the full array plus quality-reject buffer. |
| Electrical BoM | 21 000 | Inverters, string cabling, connectors, junction boxes, terminal boxes. |
| Packaging and transport Norway → Saxony | 10 000 | Transport-ready packaging and inland freight. |
| Total | 178 000 | 30 % of Sunlit Sea personnel costs. |

| Participant 1 — SINTEF | Cost (€) | Justification |
|:--|--:|:--|
| Instrumentation and telemetry hardware | 68 000 | Two moored IMU wave buoys, mooring and anchoring load cells, pyranometer with thermal sensor, site camera, gateway and data-acquisition units. SINTEF specifies this equipment under T4.1, builds the telemetry and analysis platform around it under T4.4, and operates it through the campaign, so procurement sits with the partner that owns the measurement. |
| Total | 68 000 | 24 % of SINTEF personnel costs. |

| Participant 3 — CLEMENT Germany | Cost (€) | Justification |
|:--|--:|:--|
| Concrete, reinforcement and aggregate | 215 000 | Materials for the breakwater modules; the concrete mix is selected under T2.4 by weighing service performance, cost and CO₂ footprint. |
| Mooring lines, chain, connectors and anchors | 98 000 | Complete mooring spread for breakwater and array, to the T2.4 design. |
| Towing, crane and workboat hire | 78 000 | Installation at M21–M22 and recovery at M33–M34. |
| Steel connectors, hinges and transition elements | 62 000 | Breakwater-to-breakwater and breakwater-to-array structural interfaces. |
| Mould and formwork adaptation | 45 000 | Adaptation of existing pontoon formwork to the demonstrator geometry. |
| Site works and decommissioning equipment | 20 000 | Shore-side staging, mooring pre-lay support, recovery equipment. |
| Total | 518 000 | 190 % of CLEMENT personnel costs. |

*EDP purchase costs do not exceed 15 % of its personnel costs; no table is required.*

\#§QUA-LIT-QL§# \#§WRK-PLA-WP§#

---

# ANNEXES TO PROPOSAL PART B

The annexes to be uploaded for this call are available on the SEP submission platform.

- COMMITMENT LETTER FOR IP RIGHTS — not required. SINTEF, Sunlit Sea and CLEMENT were beneficiaries of SUREWAVE (101083342) and are the owners or holders of the results developed further here.
- LUMP SUM DETAILED BUDGET TABLE — prepared, broken down per work package and beneficiary by personnel, subcontracting, purchase and other costs, consistent with tables 3.3f–3.3h. — mandatory; per work package and participant, consistent with tables 3.3f–3.3h.
- CLINICAL TRIALS — not applicable.
- ETHICS — ethics self-assessment is provided in Part A; no serious ethics issues are expected and no annex is required.

Supporting letters to annex (not template annexes but strongly recommended): the signed Letter of Intent between CLEMENT Germany GmbH and LeipzigSeen GmbH for Hainer See, dated 8 September 2026; EDP letter of support referencing board approval; customer letters from the Norwegian pipeline.

---
