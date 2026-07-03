---
title: "Sunlit Sea × Norsmaterials — partner brief"
subtitle: "Gen 2 float PU-development collaboration"
author: "Sunlit Sea AS"
date: "2026-07-03"
---

## Purpose of this brief

We are exploring a working collaboration with Norsmaterials on the polyurethane parts of our Gen 2 floating photovoltaic (FPV) product. This document is written for your R&D team, so we start the technical conversation from the same baseline: where we are, how we got here, and what we want to learn from each test cast.

We are calibrating deliberately: we skip PU-fundamentals (you know that better than we do) and instead focus on the specifics of our geometry, our interfaces, our environment and our development schedule.

---

## Who we are

Sunlit Sea AS is a Norwegian FPV company. We design, manufacture and deploy floating photovoltaic units for calm-to-moderate sea states, with a target 25-year aquatic operating life. Our first-generation product (Gen 1) is deployed; we are now developing **Gen 2**, which redesigns the float body, infill and interfaces.

We are a partner in the **Horizon Europe SuRE project (WP6)**, where our task is to build and demonstrate a full model chain covering pressing simulation, structural response, thermal behaviour and life-cycle impact for successive Gen 2 prototypes. The D6.1 deliverable (Model chain description) has been submitted; D6.2 (Multi-domain design screening) is in preparation.

---

## The Gen 1 → Gen 2 story in one page

| Aspect | Gen 1 (deployed) | Gen 2 (in development) |
|---|---|---|
| Float body | Two pressed aluminium half-shells, bonded, air-filled | Same topology, but redesigned pressing and infill |
| Aluminium sheet | 1.5 mm (5083-H111) | 0.8 mm (5083-H111), pressed via **hydroforming** rather than punch/die |
| Infill | Polystyrene cup infill | **PU foam** infill (thermal-bridge behaviour is different — see below) |
| PU top layer | Dark blue, absorptivity **0.88–0.91** measured | **Off-white**, expected absorptivity **~0.35** (not yet measured) |
| Distance PV → water | 8.5 cm | 6 cm (with a 2° panel tilt) |
| Design driver | Empirical iteration | **Risk-based, model-chain-driven** iteration across four domains (pressing, structural, thermal, LCA) |

The Gen 1 dark-blue PU absorptivity caused significant panel over-heating; that finding drove the switch to off-white PU in Gen 2. The switch from punch-and-die pressing to hydroforming was driven by tool wear and thinning risk we saw in FEM simulations of the punch/die approach.

---

## Where PU sits in Gen 2

PU has two structural jobs in the Gen 2 float:

1. **Infill** — replaces the Gen 1 polystyrene. Blocks the thermal-bridge path from the PV lamination stack down through the cup and into the sea. Whether we *want* that bridge is an open architectural question — see the open questions section.
2. **Underside / seal** — mates with the pressed aluminium cup and takes UV, salt-spray and mechanical loading in service.

Two architectural decisions on PU are still open, and they are what we most need help thinking through:

- **A. Cast-on-frame vs. separate-and-mount.** Cast-on-frame means we cast PU directly onto the pressed-aluminium float body. Separate-and-mount means we produce PU parts independently and bond them at assembly. We must decide before we build P5.
- **B. Whether to reintroduce a controlled thermal bridge** via a pressed-cup or honeycomb-aluminium infill topology. This is an open D6.2 question.

---

## What we've measured, and what we haven't

| Measurement | Status |
|---|---|
| Gen 1 dark-blue PU absorptivity | Measured: 0.88–0.91 |
| Gen 2 off-white PU absorptivity | Expected ~0.35; **not yet measured** |
| Gen 2 PU UV exposure (~480 h, Condition A1) on P3 | In progress at IFE |
| P3 adhesion — shear (PU/glass, long sides) and tensile (loose hinges) after UV | Planned; not started |
| Aluminium material card (Al 5083-H111) | Complete: r0≈0.71, r45≈0.84, r90≈0.64, rbb≈1.13 (Yld2003 + Voce fits) |
| P4 mould cast | Started |
| 25-year aquatic durability, real conditions | Not tested. Primer we are aware of reports ~20 years in aquatic use; we need 25 — dedicated testing needed. |

---

## Development pipeline that Norsmaterials would plug into

We are running a risk-based, prototype-per-cycle development approach: P1 → P2 → P3 (built, in test) → P4 (mould cast started) → P5 (design pending). Each prototype is designed with input from the four modelling domains (pressing feasibility, structural response, thermal behaviour, life-cycle impact), and each is tested against the failure modes that are highest-risk at that stage.

The model chain that supports this is documented in SuRE D6.1 and — for the pressing side — generates ~1,300 feasible cup geometries that are then screened structurally, thermally and by LCA (D6.2, in progress). This means the design space we are casting into is *large* and *ranked* — we are not casting a single geometry blindly and hoping.

For a Norsmaterials collaboration to plug into this cleanly, we would need:

- A shared understanding of which candidate geometries are being cast when.
- A per-cast learning objective — what specifically is each cast testing?
- A per-cast feedback pass — your observations on castability, cure, adhesion behaviour, defects, surface finish, mould release.
- A running list of test-plan revisions that we and you both agree to.

---

## What we want from Norsmaterials — concretely

1. **PU formulation choice.** Given the environment (Al 5083-H111 substrate, laminated glass on the topside, seawater, UV, temperature range roughly −10 °C to +50 °C surface, 25-year target), which NORSelast® variant fits — or is a hybrid (NORSelast + NORSfoam) the right answer? We have read your public material list (01, 02, S4, EL, PIR, Spray, AF, NORSfoam®) but do not have hardness, temperature or UV data to reason from.
2. **Mould-design collaboration.** Help us design moulds so that each cast teaches us something specific — not just "a part came out." We can supply the geometry (we already have the CAD and, per prototype, the STEP files).
3. **Test-casting service.** Small batches on our moulds, or on moulds you make. Fast turnaround so we can iterate.
4. **Adhesion strategy.** PU-to-aluminium and PU-to-glass, both mechanical and chemical. Any pre-treatment recommendations you can share.
5. **Long-term aquatic durability.** Any prior work from your aquaculture / marine customers that speaks to 25-year targets in salt water with UV loading and biofouling — especially where the failure mode was PU adhesion rather than bulk PU.
6. **Biofouling.** You market biofouling-resistant materials for aquaculture. Are any of those directly applicable to a topside FPV panel?

---

## Open questions we want your input on

1. Which NORSelast (or NORSfoam) variant fits an **off-white, low-absorptivity, UV-exposed PU** sitting on aluminium in seawater for 25 years?
2. Cast-on-frame vs. separate-and-mount — given demoulding, adhesion, field-repair and long-term reliability trade-offs, which architecture do you recommend?
3. What test-cast protocol would you propose to maximise learning per iteration on: (a) adhesion to Al 5083-H111, (b) adhesion to laminated glass, (c) UV / salt-spray / thermal-cycling durability?
4. What is the smallest sensible test batch you can produce, and what turnaround should we plan for?
5. Any prior projects — public or NDA-restricted — that share our combination of marine + UV + Al-adhesion + biofouling?

---

## What we can share to help you help us

- Gen 1 assembly diagram (all components, bond regions, sealant strategy).
- Gen 1 float photos as built.
- Gen 1 passive-cooling paths.
- Gen 2 P3 and P4 CAD views (STEP available on request).
- Pressing pipeline flow diagram from SuRE D6.1.
- Target cup shape.
- Aluminium material card (5083-H111) with r-values, Voce hardening, Yld2003 fit.
- Nathan Roosloot's (IFE) FEM/CFD results for P3 to date.

A companion presentation deck is being prepared from this brief.

---

## Practical

- **Timeline:** we want to iterate on P4 moulds through Q3 2026 and freeze the P5 architecture in Q4 2026.
- **Next step:** a virtual meeting with your R&D team on the questions above, then an on-site session (Sandane or Trondheim) when concrete casts are on the table.
- **Contact:** Eirik Larsen, Sunlit Sea AS.

---

## Sources for the company profile Norsmaterials shared publicly

- [NORSmaterials home](https://norsmaterials.com/)
- [NORSelast® product page](https://norsmaterials.com/norselast/)
- [NORSmaterials on LinkedIn](https://no.linkedin.com/company/norsmaterials)
