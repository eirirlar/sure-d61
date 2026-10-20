---
persona: Lars Petersson — Swedish grid / DSO engineer
focus: Gotland DSO interface, nätanslutning, grid code compliance, PPA options, protection coordination
---

## 1. Grid connection problems and risks

**1. Gotland's constrained transmission capacity to the mainland**
Gotland is currently connected to the mainland via two aging HVDC Light cables, each rated at approximately 130 MW, giving a combined nominal capacity of about 260 MW for both import and export. These cables date from the mid-1980s and were not designed for the bidirectional flexibility that high wind and solar penetration demand. Svenska Kraftnät is planning two new 220 kV AC submarine cables (total ~440 MW capacity) expected in service in the early 2030s. Until that reinforcement is in place, new generation requesting grid access on Gotland enters a system that is already at or near its export ceiling on high-wind days. A 1 MWp FPV installation is modest in isolation, but it still needs a queue position in a congested island grid.

**2. Vattenfall Eldistribution's current moratorium posture for new production**
Following the conclusion that the existing HVDC cables cannot support significant additional generation without endangering security of supply, Vattenfall Eldistribution (as DSO for Gotland, operating the 130 kV, 20 kV and 10 kV distribution networks on the island) has at various points frozen or severely rationed queue slots for new wind and solar connections. The risk for the project is that an application submitted in late 2027 lands in a queue with a multi-year wait, pushing the connection date past the planned 2029 commissioning target. Clarifying the DSO's current access posture is the first task — before the grant is even submitted.

**3. Nätförstärkningsanalys and cost allocation under Ellagen 4 kap.**
Under Ellagen (1997:857) 4 kap. the connection customer bears the cost of the connection point up to and including the mätarpunkt, while the DSO bears reinforcement costs that benefit other network users. However, if the Storugns 20 kV or 10 kV feeder has insufficient spare capacity and must be upgraded solely to accommodate the FPV plant, the DSO can charge the full reinforcement cost to the producer. A 1 MWp inverter-interfaced plant at 0.9 power factor produces approximately 1.1 MVA of apparent power. The spare capacity on the nearest feeder at Storugns is unknown and must be confirmed through a formal nätförstärkningsanalys. If the feeder is already loaded near its thermal limit during summer peaks (tourist load plus Nordkalk industry), a cable upgrade could cost several million SEK and delay the project by 12–18 months.

**4. Voltage regulation on a weak 10/20 kV rural feeder**
Northern Gotland's distribution feeders serving the Storugns area are long rural lines with relatively high impedance. Injecting 1 MWp at unity or leading power factor into such a feeder can cause voltage rise above the permitted EN 50160 band (230 V ± 10 %) at the connection point and at intermediate customers. The DSO will require a voltage impact study as part of the connection assessment. Reactive power compensation or active droop control (Q(U) characteristic per EIFS 2018:2) will likely be a condition of the connection agreement. The inverter specification must cover this from the start.

**5. Fault level and short-circuit contribution**
The existing fault level at a rural 20 kV or 10 kV busbar in northern Gotland is relatively low — potentially in the range of 5–15 MVA at the point of common coupling. Adding inverter-based generation increases prospective fault current, which can cause protection relay coordination problems for the DSO's existing overcurrent and earth-fault relays. Conversely, inverter-interfaced generation contributes fault current for only a few cycles and does not provide the sustained short-circuit current that protection schemes depend on. A protection coordination study is mandatory, and the DSO will want confirmation of the inverter's fault ride-through behaviour and its current-limiting characteristics.

**6. Protection relay coordination for inverter-interfaced sources**
Gotland's distribution protection relies on overcurrent schemes designed for a radial network supplied from one direction only. Adding a 1 MWp source changes the directionality of fault current on the feeder segment between the FPV plant and the substation. The DSO will require directional overcurrent protection or a dedicated interface protection relay (interfasåterkoppling, often called "anti-islanding" in Swedish practice) at the connection point. The relay settings must be coordinated with the existing feeder protection to avoid unwanted trips during external faults and to ensure the plant disconnects promptly on islanding. This adds engineering cost and schedule time that must be built into the project plan.

**7. Anti-islanding and island grid risk**
Gotland itself operated as an island grid for extended periods when the HVDC links were unavailable. If the new 220 kV AC cables provide a more robust connection, island operation becomes less frequent — but the risk does not disappear. An FPV plant that continues generating into a Gotland island during a mainland cable outage could sustain an uncontrolled islanded network. The inverter must comply with the anti-islanding requirements in EIFS 2018:2, and the interface protection settings must be coordinated with the DSO's system-level island detection scheme. This is a specific Gotland risk not present in mainland Swedish projects.

**8. Voltage ride-through and low-voltage ride-through (LVRT) requirements**
Under EIFS 2018:2 (implementing RfG Regulation (EU) 2016/631 for Type A and B generating plants), even a sub-1 MWp plant must remain connected during voltage dips defined in the ride-through profile. At a weak rural busbar the voltage dip during a nearby fault can be severe. The inverters' LVRT capability must be documented and confirmed against the DSO's protection scheme. The project's inverter procurement specification should explicitly require compliance with EIFS 2018:2 and the Swedish national parameter settings.

**9. Metering boundary and balance responsibility**
Swedish balance responsibility (balansansvar) under the Ellagen requires every production facility to have a nominated balance responsible party (BRP). The metering boundary (mätarpunkt) must be agreed with Vattenfall Eldistribution and registered in the Ediel/Edig@s system used for settlement. For a behind-the-meter PPA arrangement with Nordkalk, the metering topology becomes more complex: one meter for gross FPV output, one for Nordkalk's offtake, and the residual export to the grid. Vattenfall Eldistribution must approve the metering configuration. This is administratively straightforward but takes 3–6 months to formalise once the connection agreement is signed.

**10. Grid code compliance — EIFS 2018:2 and RfG categorisation**
At 1 MWp the plant is likely a Type A or Type B generating module under RfG (EU) 2016/631 as transposed by EI's EIFS 2018:2. Type B threshold in Sweden is 1.5 MW (approximate; EI confirms the threshold). Below that threshold the technical requirements are somewhat lighter, but the DSO still requires documentation of frequency response capability, reactive power range, and power quality compliance. If the project includes a battery storage system alongside the FPV, total registered capacity may push it into Type B with stricter requirements. EI (Energimarknadsinspektionen) is the regulatory authority; Svenska Kraftnät publishes the national parameter settings applicable to EIFS 2018:2.

**11. Curtailment risk and redispatch arrangements**
Even after connection, the DSO can curtail output if the feeder is congested. Vattenfall Eldistribution has been developing flexibility contracts (flex-pilot schemes published in 2025) that allow curtailment in exchange for accelerated connection. The project must evaluate whether accepting a flex curtailment contract is better than waiting for a full firm connection. Curtailment of 10–20 % of annual energy yield changes the business case significantly and must be modelled in the financial projections submitted with the EIC proposal.

**12. Winter–summer loading contrast and seasonal hosting capacity**
Gotland's resident population increases dramatically in summer (tourism), raising residential and commercial load significantly. In winter the island is predominantly industrial and agricultural load. The hosting capacity on the Storugns feeder may be higher in winter (heavy industrial load absorbs local generation) and tighter in summer when tourist-driven loads are lighter relative to midday solar peak. This seasonal asymmetry can make summer the constraining condition for voltage rise even though summer has the highest solar irradiation. The hosting capacity analysis must cover both seasons.

**13. Interaction with Nordkalk's industrial load profile**
Nordkalk's Klinthagen quarry operates crushing and grinding equipment with substantial inductive motor loads and episodic demand spikes from blasting sequences and kiln operations. This non-linear, non-steady load profile creates voltage fluctuations and harmonic content on the local feeder. The FPV plant's inverter must be verified for harmonic emission compliance (IEC 61000-3-12 or the applicable standard) and must not aggravate existing voltage quality issues. A power quality baseline measurement at the proposed connection point before connection is advisable and may be required by the DSO.

**14. Ellagen classification — elproduktion vs. nätverksamhet**
The FPV plant, being a generation asset selling power either to Nordkalk directly or to the grid, is an elproduktionsanläggning under Ellagen — not a network activity (nätverksamhet). This is important because nätverksamhet is a natural monopoly subject to EI revenue regulation. As a producer the project company needs no concession under Ellagen 2 kap. for the generating facility itself, but the cable from the FPV plant to the connection point may require a nätkoncession för linje if it crosses third-party land. This should be verified with EI or legal counsel before finalising the connection route.

**15. Lead time for DSO connection process**
Based on experience with comparable projects in Vattenfall Eldistribution's service area, the formal nätanslutningsprocess for a 1 MWp production facility typically takes 18–36 months from initial inquiry to energisation. This includes: pre-study (4–8 weeks), capacity assessment (8–16 weeks), connection offer and negotiation (8–12 weeks), engineering and civil works (12–18 months). On Gotland, with a constrained grid and limited local contractor capacity, the upper end of this range is more likely. Starting the pre-inquiry in H1 2027 (assuming EIC funding confirmed late 2026) risks not achieving the 2029 commissioning target. Pre-application engagement should begin no later than Q2 2027, and ideally before grant confirmation.

---

## 2. Grid-connection tasks for Olle

### Early-stage nätanslutningsförfrågan

**Task G-01: Initial contact with Vattenfall Eldistribution, Gotland**
Contact Vattenfall Eldistribution AB's regional office in Visby and submit an informal inquiry (föranmälan) about the feasibility of connecting a 1 MWp solar PV production facility at coordinates 57.844°N 18.797°E, Storugns. Ask for an indication of connection possibility (anvisning om anslutningsalternativ) at the nearest suitable voltage level (10 kV or 20 kV), including approximate reinforcement scope and indicative cost. Deliverable: written DSO response with connection point indication. Time: 4–8 weeks from submission. Dependencies: land/water area rights clarification (to define the cable route). Counterparty: Vattenfall Eldistribution AB, nätanslutning, Gotland district.

**Task G-02: Identify and confirm candidate connection point**
Assess whether Nordkalk's own industrial high-voltage substation at Storugns is a viable point of common coupling, and whether Nordkalk would consent to a behind-the-meter connection. If not, identify the nearest Vattenfall Eldistribution 20 kV or 10 kV node with adequate hosting capacity. Deliverable: connection point options memo with pros/cons for each scenario. Time: concurrent with G-01, 4–6 weeks. Dependencies: Nordkalk initial contact (Task G-10). Counterparty: Nordkalk facility engineer; Vattenfall Eldistribution.

**Task G-03: Formal nätanslutningsansökan submission**
Submit the formal connection application to Vattenfall Eldistribution using their standard form for production facilities over 63 A. The application requires: installed capacity (kWp), inverter count and unit ratings, power factor range, fault contribution data, proposed connection point, and preliminary single-line diagram. Deliverable: submitted application acknowledgement. Time: submit within 4 weeks of receiving G-01 response. Dependencies: G-01, G-02, inverter specification. Counterparty: Vattenfall Eldistribution nätanslutning.

### Nätanslutningsavtal and tariff

**Task G-04: Negotiate nätanslutningsavtal**
Negotiate the formal grid connection agreement (nätanslutningsavtal) with Vattenfall Eldistribution. Key terms to secure: connection capacity (kW), voltage level, connection point coordinates, cost allocation for any nätförstärkning (Ellagen 4 kap. basis), timeline commitments, and any flex curtailment conditions. If a flex contract is offered, model the financial impact before accepting. Deliverable: signed nätanslutningsavtal. Time: 8–16 weeks post-application. Dependencies: G-03, DSO capacity study. Counterparty: Vattenfall Eldistribution.

**Task G-05: Nättariff assessment and balance responsibility registration**
Determine the applicable distribution tariff category (produktionstariff for Gotland, Vattenfall Eldistribution's tariff schedule). Register the project company as a balance responsible party (BRP) or procure BRP services from a third-party actor. Register the production metering point in Ediel. Deliverable: BRP agreement and Ediel registration confirmation. Time: 3–6 months from connection agreement. Dependencies: G-04, Swedish energy company registration. Counterparty: Vattenfall Eldistribution mätning; Nord Pool or chosen BRP.

### Technical connection study

**Task G-06: Nätförstärkningsanalys — commission or review DSO study**
If the DSO requires or offers a network reinforcement study, review the methodology and cost allocations carefully. Commission an independent review if the reinforcement cost appears disproportionate (benchmark: >2 MSEK for a 1 MWp connection would be unusual but possible given Gotland conditions). Deliverable: reviewed nätförstärkningsanalys with cost allocation commentary. Time: 8–16 weeks (DSO-led study). Dependencies: G-03. Counterparty: Vattenfall Eldistribution network planning; independent consultant.

**Task G-07: Voltage impact and hosting capacity study**
Commission a voltage impact study for the proposed connection point, covering both summer and winter loading scenarios. Confirm that voltage rise stays within EN 50160 limits (230 V ± 10 % at low voltage, ± 10 % band at medium voltage) and identify any required reactive compensation. Deliverable: voltage impact report with recommended Q(U) settings for inverters. Time: 6–10 weeks. Dependencies: G-02 (confirmed connection point). Counterparty: grid consultant or Vattenfall Eldistribution.

### Protection and metering design

**Task G-08: Interface protection design and relay coordination study**
Engage a protection engineer to design the interface protection at the connection point: directional overcurrent relay, anti-islanding relay (ROCOF or voltage vector shift), and earth-fault detection. Coordinate settings with Vattenfall Eldistribution's existing feeder protection to avoid nuisance trips. Document compliance with EIFS 2018:2 anti-islanding requirements. Deliverable: protection philosophy document and relay settings sheet, approved by DSO. Time: 10–14 weeks. Dependencies: G-06 (fault level data from DSO). Counterparty: protection consultant; Vattenfall Eldistribution protection team.

**Task G-09: Metering topology design for PPA arrangement**
Design the metering scheme to support either (a) behind-the-meter direct supply to Nordkalk with grid export of residual, or (b) full grid injection. Confirm metering boundary with Vattenfall Eldistribution. Specify meter types compliant with Swedish requirements (Elmätarförordningen). Deliverable: approved metering single-line diagram. Time: 4–6 weeks after connection point confirmation. Dependencies: G-04, G-10 (PPA structure agreed). Counterparty: Vattenfall Eldistribution mätning; metering equipment supplier.

### PPA options — behind-the-meter with Nordkalk vs. grid sale

**Task G-10: Nordkalk initial PPA conversation**
Engage Nordkalk's facility management and energy team at Storugns to explore interest in a direct supply arrangement. Key questions: does Nordkalk have load profiles that match solar generation hours (daytime crushing and grinding)? Is Nordkalk willing to grant access for a connection cable to their substation? What is their preferred commercial structure (fixed price PPA, discount to spot, capacity reservation)? Deliverable: non-binding letter of interest or term sheet from Nordkalk. Time: 6–10 weeks. Dependencies: initial project presentation to Nordkalk management. Counterparty: Nordkalk Sweden AB, Storugns facility director.

**Task G-11: PPA structure and price basis analysis**
Model two scenarios: (1) behind-the-meter PPA with Nordkalk at a price between Nordkalk's retail tariff and spot (capturing distribution tariff savings), (2) full grid injection selling at Nord Pool spot. For scenario (1) obtain Nordkalk's annual load profile data to calculate coincidence factor with FPV generation. Deliverable: PPA scenario analysis for EIC proposal financial model. Time: 4–6 weeks. Dependencies: G-10, Nord Pool price forecasts. Counterparty: financial adviser; Nordkalk.

**Task G-12: OX2 / Gotland renewable energy stakeholder mapping**
Note that OX2 and Nordkalk have an existing e-fuel collaboration on Gotland. This means Nordkalk already has a relationship with a large renewable energy developer. Assess whether this creates competition for Nordkalk's substation access and bandwidth, or whether there is an opportunity for alignment. Deliverable: stakeholder map memo. Time: 2–3 weeks. Dependencies: none. Counterparty: public sources; OX2 communications if appropriate.

### Grid code compliance — EIFS 2018:2 and successor regulations

**Task G-13: RfG categorisation and compliance documentation**
Determine the plant's categorisation under RfG (EU) 2016/631 as implemented by EI's EIFS 2018:2. Confirm whether the plant is Type A (below 1.5 MW) or Type B, and document applicable requirements: frequency response, reactive power range, LVRT, anti-islanding, power quality. Deliverable: compliance matrix against EIFS 2018:2 requirements, cross-referenced to inverter datasheets. Time: 4–6 weeks. Dependencies: inverter selection. Counterparty: EI (Energimarknadsinspektionen) for regulatory clarification; inverter supplier.

**Task G-14: SvK notification (if applicable)**
For Type B and above, notification to Svenska Kraftnät is required. Even for Type A, check whether SvK has issued specific requirements for new inverter-interfaced generation on Gotland given the island's unique grid characteristics. Submit any required SvK notification. Deliverable: SvK notification acknowledgement or confirmation that notification is not required. Time: 2–4 weeks. Dependencies: G-13. Counterparty: Svenska Kraftnät, produktionsanslutning.

**Task G-15: Harmonic and power quality pre-assessment**
Conduct a power quality baseline measurement at the proposed connection point (minimum 7-day recording per IEC 61000-4-30 Class A). Assess existing harmonic levels from Nordkalk's industrial loads. Commission harmonic emission study to confirm the FPV inverters do not exceed limits. Deliverable: power quality report; harmonic emission assessment. Time: 4–6 weeks (measurement) + 4 weeks (analysis). Dependencies: G-02 (access to connection point). Counterparty: independent measurement contractor.

### Commissioning and energisation

**Task G-16: Commissioning plan and DSO acceptance testing**
Develop a commissioning plan in agreement with Vattenfall Eldistribution, covering: pre-energisation checks, protection relay testing (primary injection), anti-islanding test, power quality measurement at energisation, ramp-up sequence. Deliverable: commissioning plan approved by DSO. Time: 6–8 weeks before planned energisation. Dependencies: G-08, G-09. Counterparty: Vattenfall Eldistribution; commissioning contractor.

**Task G-17: Formal energisation and operational notification**
Complete DSO acceptance test, register the plant as operational in Ediel, and notify EI of commissioning (as required under EIFS 2018:2 for the applicable plant type). Deliverable: DSO energisation permit; EI operational registration. Time: 1–2 weeks at commissioning. Dependencies: G-16; all prior tasks complete. Counterparty: Vattenfall Eldistribution; EI.

### Curtailment and dispatch arrangements

**Task G-18: Flex contract assessment**
Evaluate Vattenfall Eldistribution's flex curtailment contract terms (if offered as a condition of earlier or cheaper connection). Model curtailment impact on annual yield and revenue. If curtailment risk exceeds 10 % of annual output, consider whether firm connection (with later availability date) is financially preferable. Deliverable: flex contract recommendation memo. Time: 3–4 weeks after flex offer received. Dependencies: G-04. Counterparty: Vattenfall Eldistribution; financial model team.

**Task G-19: Congestion and redispatch monitoring protocol**
Establish a protocol for monitoring congestion notifications from Vattenfall Eldistribution once the plant is operational, and a procedure for responding to curtailment instructions within the timeframe specified in the connection agreement. Deliverable: operating procedure document. Time: 4 weeks before commissioning. Dependencies: G-04 (curtailment terms in connection agreement). Counterparty: plant operator; Vattenfall Eldistribution.

---

## 3. Suggested sequencing

**Before grant confirmation (pre-application, H1 2027 at the latest, ideally Q4 2026):**
The Swedish DSO queue is the single longest item on the critical path. The nätanslutningsprocess can take 18–36 months. This means the application must be filed well before the EIC grant is awarded — not after. The EIC proposal submission in December 2026 should already reference a submitted or at least an initiated pre-inquiry (föranmälan) to Vattenfall Eldistribution. Before the grant is confirmed: complete Tasks G-01 (initial DSO contact), G-02 (connection point identification), and G-10 (Nordkalk initial conversation). These are preliminary, non-binding steps that require no significant expenditure, but they establish a queue position and give the project a credible connection timeline to include in the proposal.

**Critical path items:**
The critical path runs: G-01 → G-03 → G-04 (nätanslutningsavtal) → G-06 (reinforcement study) → G-08 (protection design) → G-16 (commissioning plan) → G-17 (energisation). The longest individual step is G-04/G-06 combined: negotiating the connection agreement while the DSO completes its network study. This sequence realistically takes 12–24 months from application submission to signed agreement, and a further 12–18 months for civil works and equipment delivery. A 2029 energisation target requires a signed connection agreement no later than mid-2027, which in turn requires a formal application no later than early 2027.

**DSO queue as schedule risk:**
Vattenfall Eldistribution on Gotland has a limited engineering team and has been managing a large backlog of renewable connection requests driven by the island's decarbonisation ambitions and the planned OX2/Nordkalk e-fuel project. The DSO's own workload is the primary schedule risk. There is no procedural shortcut: applications are processed in order of receipt under Ellagen. Olle must establish contact and submit a formal pre-inquiry in Q4 2026 or at the very latest Q1 2027, treating this as a grant-parallel activity rather than a post-award activity.

**Parallel tracks that can proceed without grant confirmation:**
G-10 (Nordkalk PPA conversation), G-12 (stakeholder mapping), G-13 (preliminary grid code compliance assessment against inverter specifications) and G-15 (power quality baseline measurement, if site access is available) can all proceed in parallel with G-01 through G-03 and do not require grant confirmation. These tasks reduce risk and improve the quality of the EIC proposal's financial and technical annexes.

**Where the new SvK HVDC connection matters:**
The new 220 kV AC Gotland cables (planned early 2030s) will, when in service, substantially increase available export capacity and reduce curtailment risk. A 2029 energisation for the FPV plant means it will operate for approximately 1–2 years under the current constrained regime before the new cables arrive. The financial model should stress-test for 10–20 % curtailment in those initial years.

---

## 4. Key Swedish/Gotland institutions and contacts

**Vattenfall Eldistribution AB — Gotland district**
The sole DSO for Gotland, operating all distribution voltage levels (130/40/20/10/0.4 kV) on the island. Responsible for nätanslutning, hosting capacity assessments, and the nätanslutningsavtal. The regional office is in Visby. Contact point: nätanslutning, Gotlandsregionen. Website: vattenfalleldistribution.se. Primary counterparty for G-01 through G-07, G-08 (protection), G-09 (metering), G-16 and G-17.

**Svenska Kraftnät (SvK)**
The Swedish TSO, responsible for the national transmission grid and for the planned new Gotland 220 kV connection. SvK sets the national parameter settings for EIFS 2018:2 and manages balance settlement through Svk's Balansansvarig system. SvK publishes the Nätutvecklingsplan and the Gotlandsförbindelsen project documentation. Contact point: produktionsanslutning and regionnätanslutning units. For Gotland specifically, the Gotlandsförbindelsen project office is the relevant contact regarding transmission planning. svk.se.

**Energimarknadsinspektionen (EI)**
The Swedish energy market regulator. EI issues EIFS 2018:2 (implementing RfG), regulates DSO tariffs and revenue caps, oversees concession (nätkoncession) approvals, and is the authority for any disputes with the DSO over connection terms or cost allocation. EI publishes guidance on Type A/B/C categorisation thresholds. Contact point: EI's tillstånd och tillsyn unit; also EI's nätreglering unit for tariff questions. ei.se.

**Länsstyrelsen Gotland**
If the connection cable from the FPV plant to the shore requires a nätkoncession för linje crossing third-party land or foreshore areas, the application goes to EI but Länsstyrelsen may have a consultative role, particularly for any Natura 2000 or coastal zone planning aspects. Länsstyrelsen is also the permitting authority for the water area use permit (vattenverksamhet under Miljöbalken) required for the mooring and anchoring of the FPV array — though this is more relevant to the maritime/planning stream than the grid stream. Contact point: Länsstyrelsen Gotland, samhällsbyggnad and miljöprövning.

**Nordkalk Sweden AB — Storugns facility**
Nordkalk's site management and energy/maintenance team at Klinthagen/Storugns are the primary counterparty for PPA discussions and substation access negotiations. Nordkalk has an existing renewable energy collaboration with OX2 (e-fuel/hydrogen project) which means the facility has some familiarity with the commercial structures of power purchase agreements.

**Gotlands Energi AB (GEAB)**
GEAB is a local energy company on Gotland involved in local grid development investments including battery storage projects. GEAB is not the DSO (that is Vattenfall Eldistribution) but has been active in flexibility solutions and may be relevant as a flexibility aggregator or as a source of local grid expertise. geab.se.

**Region Gotland**
Region Gotland has published an energi- och klimatstrategi that promotes solar and wind development on the island. Region Gotland may be a relevant stakeholder for permitting (oversea area planning) and for community acceptance, though they have no direct role in the DSO connection process. Contact point: samhällsutvecklingsförvaltningen, energi och klimat.

**Energiföretagen Sverige**
The industry association for Swedish energy companies. Publishes technical recommendations (Tekniska krav för anslutning av produktionsanläggningar) that DSOs reference in their connection conditions. Relevant for understanding standard practice on protection and metering requirements.

**OX2**
A major Swedish wind and solar developer with an existing Gotland presence (e-fuel project with Nordkalk). Not a regulatory body, but potentially a local knowledge resource and possibly a competitive interest for Nordkalk's substation bandwidth. Monitor their project development activities on Gotland.

---

## 5. Open questions and things to verify

**Is Nordkalk's industrial substation suitable as a connection point?**
The Klinthagen quarry has its own industrial high-voltage substation serving the crushing, grinding, and kiln operations. The voltage level, transformer capacity, spare busbar capacity, and protection philosophy of this substation are unknown from public sources. If Nordkalk's substation operates at 10 kV or 20 kV with a direct DSO feed, injecting the FPV plant behind Nordkalk's meter may be technically straightforward (and would also avoid the need for a separate DSO connection entirely, with the FPV plant becoming a producer under Nordkalk's existing connection). This would dramatically simplify the grid connection — but it requires Nordkalk's active cooperation and an amendment to their own nätanslutningsavtal. This must be explored with Nordkalk and Vattenfall Eldistribution jointly in the earliest phase.

**What is the current hosting capacity at Storugns?**
Vattenfall Eldistribution publishes a kapacitetskarta (capacity map) on their website showing indicative hosting capacity by geographic area. This map should be checked for the Storugns/northern Gotland area before the first DSO contact. If the map shows hosting capacity below 1 MW at the nearest network node, the conversation with Vattenfall Eldistribution starts from a deficit position and a nätförstärkningsanalys is essentially certain.

**Is the Fårö cable landing relevant?**
The northernmost tip of Gotland (Fårö) has been discussed in connection with offshore wind and potential submarine cable landing points. Whether any cable infrastructure in that area (if it exists or is planned) is relevant to the FPV project's grid connection is unclear. If a 20 kV or higher voltage cable runs close to the Storugns coast, it might offer a connection option with less reinforcement cost than a connection via the inland feeder network. This should be explored with Vattenfall Eldistribution.

**Does the installation count as nätverksamhet or elproduktionsanläggning?**
As noted in Section 1, the FPV plant should be classified as an elproduktionsanläggning (generator), not as nätverksamhet. However, the internal cable between the FPV array and the shore, and the onshore cable from the shore to the connection point, may require nätkoncession för linje if they cross third-party land or foreshore. This needs legal confirmation. If the cable route stays entirely within area covered by the FPV operator's own marine concession or within Nordkalk's property, the concession requirement may not be triggered. Seek a brief opinion from a Swedish energy law firm early in the project.

**Are there SvK-specific restrictions on new inverter-interfaced generation on Gotland?**
Svenska Kraftnät may have issued specific technical conditions or a moratorium for new type-A or type-B generation on Gotland pending completion of the new 220 kV interconnection. This was reported as a risk in the DSO's own 2025-2034 network development plan. Olle should formally ask both Vattenfall Eldistribution and SvK whether any such restrictions are currently in force, and whether the planned new cables change this assessment.

**What is the current congestion and curtailment state of the island grid?**
Vattenfall Eldistribution's nätutvecklingsplan 2025–2034 notes constraints on Gotland. The specific feeder serving northern Gotland (the Storugns/Kappelshamn area) may already be operating with active congestion management. Requesting recent congestion statistics from Vattenfall Eldistribution — or accessing EI's nätövervakning data — would give a quantitative basis for the curtailment risk assessment. If the feeder has experienced >200 hours/year of active management, the business case for a flex-only connection weakens considerably.

**OX2/Nordkalk e-fuel project interaction**
OX2 and Nordkalk announced a collaboration on e-fuel (hydrogen/methanol) production on Gotland using renewable electricity. This project would require substantial amounts of renewable generation connected at or near Storugns. If this project has already been allocated capacity at Nordkalk's substation or at the nearest DSO node, the capacity available for the FPV plant may be diminished. Clarifying the status and grid reservation of the OX2/Nordkalk project is a priority before filing the FPV connection application.

**Power quality baseline at Storugns**
Nordkalk's industrial operations (motor start-up, arc furnace analogs from kiln operations, blasting vibration effects on measurement equipment) may create a noisy power quality environment at the connection point. Establishing a pre-connection baseline measurement — voltage harmonics, flicker, unbalance — protects the FPV project from liability for pre-existing power quality issues that the DSO or Nordkalk might otherwise attribute to the new generation source.
