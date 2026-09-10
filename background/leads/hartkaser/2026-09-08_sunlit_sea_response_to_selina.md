---
title: "Response to Selina Photovoltaic — Hartkaser floating PV inquiry"
from: Per Lindberg (Sunlit Sea AS) <per@sunlitsea.no>
to: Lukas Becska (Selina Photovoltaic GmbH) <l.becska@selina-pv.com>
cc: Andreas Huber (Selina Photovoltaic GmbH) <andreas.huber@selina-pv.com>
date: 2026-09-08
type: outbound reply — technical response to inbound inquiry (2026-09-07)
basis: >
  Answers built from Sunlit Sea Gen 2 technical baseline in `gen2/norsmaterials_brief.md`,
  SuRE D6.1 requirements/report in `sure/requirements.md` and `sure/report.md`,
  and the HORA hazard extract in `background/leads/hartkaser/2026-09-07_ehora_hartkaser_en.md`.
  Frames the alpine reservoir case honestly against Sunlit Sea's marine-nearshore design envelope.
---

Subject: Re: Technical Inquiry Sunlit Sea — Pilot Project for a Floating PV System on an Alpine Reservoir in Austria

Dear Lukas,

Thank you for reaching out about the Hartkaser pilot for Bergbahnen Wilder Kaiser. This is the kind of project we like to engage with, and we appreciate the level of detail you provided in the first contact — including the eHORA extract, which we have gone through carefully.

Before the individual answers, a short framing note. Our Sunlit Sea CONNECT Gen 2 product is developed for calm-to-moderate marine and nearshore conditions with a 25-year continuous-aquatic operating life. The Hartkaser site's characteristic conditions — 9.8 kN/m² snow load at 1470 m elevation, complete-drainage-and-refill cycles, and the alpine freeze-thaw regime — bring a small number of specific engineering questions that need dedicated attention, but they do not sit fundamentally at odds with how our system is designed. The largest single item to design around is the interaction between winter ice cover and the drain-refill cycle; several of the others follow from it. Where a straight answer is possible we give one; where the situation is genuinely new for us we say so.

Answers to your ten questions follow, in your order:

**1. Approval / suitability for reservoirs that are completely and regularly drained.**

In principle yes, with one specific caveat around freeze-in-then-drain. Anchoring and mooring for a reservoir with drain-and-refill cycles is a project-specific design task that falls to the developer — as with any mooring, it is out of scope for our standard product. On the Sunlit Sea side of the interface, slowly lowering the array with the water is not a problem: the loads during a controlled level drop are considerably lower than the wave loads our system is designed for.

The failure mode we would want you to design against is this one: if the reservoir surface freezes around the units in winter and the water is then drained beneath the ice/panel layer, an air gap forms under the frozen-in modules. Any subsequent load — snow, additional ice — has nothing to bear onto until the ice-and-panel sandwich eventually gives way and crashes down onto the reservoir bottom. The operating protocol for the pilot should prevent that sequence: drain before freeze-up, or hold the water level constant through the frozen months, or engineer for the crash-down event as a design case.

**2. Safe resting on a flat lined reservoir bottom without damaging the liner.**

Safe, as far as we can tell from our Gen 2 geometry. The outward-facing perimeter of a Gen 2 unit is cast PU: the aluminium bottom plate sits inside the PU frame, and the CONNECT hinge halves on all four sides are cast integrally with that frame. No aluminium edge is exposed to the liner. PU-against-HDPE or PU-against-PVC is a soft-on-soft contact — the surface texture and radius of curvature are within what typical liner specifications allow. We would still want to sight-check your specific liner spec (allowable point load, minimum contact radius, seam locations) before confirming, but there is no sharp-edge concern with our geometry.

**3. Maximum snow, wind and ice loads the system can withstand.**

The load story on our Gen 2 units is not a purely structural one — it is a hydrostatic one, and this is central to understanding the load capacity. The PV panel, PU-foam infill and 0.8 mm aluminium bottom plate form a flexible sandwich. Any load on the top surface — a person walking on the module, snow accumulation, water at height — makes the module flex down until the aluminium bottom contacts the water, at which point the load transfers into the water column as hydrostatic pressure. In this floating-and-flexing mode our units easily carry a full-grown adult standing on the panel, and by extension can handle very substantial snow loads: the water carries the weight, not the frame.

The important qualifier is that the hydrostatic mechanism only works while the module is floating and free to flex. Two site-specific conditions defeat it:

- **Frozen-in module.** If the array freezes into a surface ice sheet that prevents the module from flexing down onto the water, load must instead be carried by the structural resistance of the sandwich alone — glass panel + PU frame + PU-foam infill + aluminium bottom. This is much less than the hydrostatic-supported capacity, and it is what the 9.8 kN/m² Hartkaser characteristic snow load would need to be evaluated against. Our default 2° panel tilt helps here in that snow tends to slide off rather than accumulating to full theoretical depth, but this is not a substitute for verification.
- **Beached module.** If the reservoir is drained and the array is resting on the bottom, the hydrostatic mechanism is again unavailable. See Q1 for the freeze-in-then-drain sequence, which is the more critical variant of this.

Wind: our current design work assumes the DNV-RP-0584 wind-load regime for a Northern European nearshore site (open water, terrain category 0). The Hartkaser vb,0 = 35.57 m/s (qb,0 = 0.79 kN/m²) is inside the envelope we design for at the reference height, but the alpine terrain category and topographic acceleration around a mountain-side reservoir must be assessed site-specifically.

Ice: freeze-thaw effects on the PU frame and the seals are under separate investigation on our Gen 2 development (UV + heat + moisture is our primary failure-mode driver today; a freeze-thaw axis at −20 °C to +10 °C would be a required addition for alpine use). Ice loading on the array surface (glaze, rime) and lateral ice pressure from a partially-frozen reservoir surface are not in our current model chain.

**4. Steeper module inclination or reinforced version for alpine conditions.**

The Gen 2 modules sit at 2° tilt (panel geometry constrained by the CONNECT-hinge inter-module coupling and the 6 cm lower-edge freeboard). A steeper tilt would require a different frame geometry and a rethink of the inter-module hydrodynamic coupling. A reinforced version — thicker aluminium (we started at 1.5 mm on Gen 1 before optimising down to 0.8 mm; going back up is possible), added structural PU volume, or a truss-supported topology — is engineering-feasible but is a distinct product variant that would need its own design and validation cycle.

**5. Bifacial glass-glass PV modules.**

Glass-glass: yes, and in fact that is our standard panel choice — we specify glass-glass on Gen 2 for its mechanical robustness and its resistance to water ingress from the panel face down into the module. Standard commercial glass-glass panels in the 710–740 Wp / 2384 × 1303 mm class drop straight into the Gen 2 architecture.

The bifacial function specifically: not usable in our design. The back half of a Gen 2 module is filled with cast PU foam, which optically closes the rear face of the panel. Light cannot reach the cells from underneath, so a bifacial panel would work fine mechanically but the bifacial gain would be zero. Our recommendation is to specify monofacial glass-glass — you get the robustness and water-ingress benefits without paying for a bifacial rating that is not usable.

**6. Anchoring without underwater anchoring or membrane penetration.**

Sunlit Sea's own mooring approach is external to the float (mooring buoys with independent anchoring), so we do not rely on penetration of any surface the array sits on. For Hartkaser, the natural adaptation is shore-based anchoring — anchor points cast into or bolted onto the reservoir crown / perimeter structures — with tensioned lines around the array perimeter. This is standard practice on lined reservoirs and is straightforward once the crown-wall structure and load ratings are known. We would need the site drawings to advise on specifics.

**7. Behaviour during lowering, resting on the bottom, and refilling.**

Broadly manageable — subject to the two conditions already flagged (Q1 avoid freeze-in-then-drain; Q3 no rigid ice cover under heavy snow load):

- **Lowering** — the array touches down progressively as the water level drops. The Gen 2 CONNECT hinges are robust and are cast PU, so most of the bending that arises from uneven touchdown (a moderately sloped bottom, general unevenness) is absorbed by the hinges themselves. The specific concern is a point or curved obstruction beneath the *middle* of an individual float — for example a rock or fixture that would force a single module to bend around it. A reasonably smooth bottom without protrusions inside the module footprints is what to design for.
- **Resting on the bottom** — see Q2. The outward-facing perimeter of each unit is cast PU, so the load path onto the liner is soft-on-soft.
- **Refilling** — the leading refill front creates asymmetric buoyancy across the array (some modules floating while adjacent ones are still beached). This differential uplift loads the CONNECT hinges laterally, which is a load direction the hinge is designed for — comparable to what our wave-tank testing at MARIN under the Surewave programme has already exercised. Refill rate is not a limiting factor from our side.

**8. Reference projects in alpine regions or under comparable snow/ice conditions.**

No Gen 2 references — Gen 2 is not yet in commercial deployment. However, our Gen 1 deployment at **Skiftestjørna (105 kWp)** has regularly frozen into surface ice and taken snow loading over multiple winters, and it is the direct reference for the freeze-in and snow-load behaviour discussed in Q1 and Q3. The operational experience from Skiftestjørna is the source of much of what we know about how our architecture behaves under freeze-thaw and accumulated snow, and that knowledge has been transferred into the Gen 2 design decisions. It is not an alpine reservoir case, but it is a real reference for the freeze-and-snow question you are asking about.

**9. Technical information you can provide for a preliminary design and budgetary quotation.**

Yes — please send everything you offered:

- Site plans and cross-sections of the reservoir.
- Waterproofing membrane specification (material, thickness, seam locations, allowable point-load and edge-load ratings, minimum contact-radius requirements).
- Preliminary project description as submitted to the Austrian funding programme.

Additionally we would ask for:

- Bathymetry of the reservoir bottom (evenness, slope, any protrusions or drainage sumps).
- Water-level operating profile: typical annual draw-down/refill cycle, rates of level change, minimum retention time at each level.
- Ice-cover history if available (extent, thickness, duration).
- Crown-wall / perimeter structural drawings for shore-anchoring assessment.
- Grid-connection point and inverter siting constraints.
- Access route and lifting-equipment constraints at the reservoir (vessel-free deployment implies crane or manual assembly).

**10. Interest in supporting the project as system supplier and technical development partner.**

Yes on the technical-development-partner role, subject to a joint scoping. As a straight system-supplier role, no — we are not the right choice today, because the product is not qualified for the operating regime you need. As a joint development partner where the Hartkaser pilot is used to extend our design envelope into alpine reservoir conditions, this is exactly the kind of engineering programme our team is set up for, and the Austrian funding programme is a good vehicle for that framing.

If that framing works for you, the next step would be a technical call between your reservoir engineers and ours to scope what a co-development pilot would cover, what the funding programme allows on that basis, and what a realistic timeline would be. We could target 30 minutes to align on scope, followed by a longer working session once we have your site documentation.

Please share the site plans, the liner specification and the project description at your convenience and we will come back with a scoped technical proposal.

Best regards,

Per Lindberg
Sunlit Sea AS
