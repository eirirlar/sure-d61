To: Matas Rudzikas (MetSolar)
Cc: Nathan Roosloot (IFE), Algirdas (MetSolar)
From: Eirik Larsen (Sunlit Sea)
Subject: Re: SuRE — scope for MetSolar prototyping

Dear Matas,

Thanks for the write-up. This is what we think would fit the SuRE failure questions best.

1. Salt-water and freshwater ingress in service — 25 years in the sea.
2. PU degradation under combined UV and heat.
3. Adhesion at the PU–glass and PU–aluminium interfaces (the mechanism feeding 1).

The electrical tests (I–V, EL, wet leakage, walking-load) cover what standard PV module qualification already does. We would rather point the budget at ingress and the interfaces.

Three concrete suggestions:
1. Dummy boxes, not laminated modules. Glass top, 0.8 mm 5083-H111 aluminium bottom, PU frame, infill — no cells, no wiring. Cheap per sample, lets you iterate on the PU process, which is where the variance sits.
2. Sized for IFE's 1 m³ climate chamber. A corner coupon with two PU–glass edges and a PU–aluminium seam is enough, and lets you run proper matrices over humidity, temperature and (if IFE can co-locate) UV.
3. Consider passive moisture collectors instead of electronic sensors. Sealed absorbent objects at the junction-box positions and along the interfaces, destructively extracted after exposure, weighed, analysed. No hard preference from our side — mainly a question of how electronic sensors would be powered inside a sealed dummy without a cable feedthrough, and the feedthrough itself then becomes an ingress path.

From your list we would keep, with some scope changes:

- Damp-heat on the dummy boxes — as a preliminary screen at MetSolar. Full characterisation (including combined UV + heat, which has driven every PU failure we have seen) is IFE's speciality and belongs there.
- Adhesion at the PU–glass and PU–aluminium interfaces on the inside of the box. This is a different interface from what Nathan has already tested — the inside has not been characterised. MetSolar is well placed to measure it pre-sealing and pre-exposure, while the sample is still open; IFE then measures it post-exposure after destructive extraction. We can share the Roosloot / Selj / Otnes 2024 IEEE JPV methodology as a starting point.
- Mechanical check — qualitative only. Clamp a box at a table edge and hang weights on it, just to get a feel for build quality. Not a scientific experiment.
- Foam-application process; honeycomb vs foam vs combined.

We would drop the thermal tests. IFE has already done the thermal modelling, and the sandwich's low heat conductivity is known.

Good next step: short alignment with Nathan on sample geometry (dimensions, interface types per coupon, extraction timing) and exposure protocol. We can send over the Gen 2 interface geometry as STEP and the material cards from D6.1.

Side note: this work would also build the capability Sunlit Sea will need from a production partner for the shipping Gen 2 product. Worth factoring in.

Best,
Eirik
