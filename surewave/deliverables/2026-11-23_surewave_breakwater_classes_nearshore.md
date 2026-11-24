---
internal_title: Floating breakwater classes for nearshore sites, indicative pricing and coverage method (working note, internal)
---

# Floating breakwater classes for nearshore sites

Working note · Sunlit Sea AS · 23 November 2026 · internal

SUREWAVE designed and costed one breakwater: the heavy open-sea unit, in a full ring around a 10 MW plant. Sunlit Sea's markets are mainly nearshore sites. Waves there are limited by the fetch, lower and shorter than at sea, and they come from only some directions.

This note:

- defines three breakwater classes for such sites, matched to three wave classes and three anchoring classes;
- gives each class an indicative installed cost per metre, built up from the SUREWAVE design and cost model plus the cost items that model does not contain;
- sets out a method that turns a plant and a site into a breakwater layout, length and cost.

All figures are indicative and are to be checked with Clement Germany before they are used in D8.4 or the financial plan. The calculations are in `scripts/breakwater_classes.py`, so every figure can be rerun with other assumptions.

## 1. Basis

| Source | Used for |
|---|---|
| D3.2 Floating breakwater design (Clement) | The SUREWAVE unit: 20 × 5.0 × 2.5 m, draft 2.03 m, 123 t, double keel, centre of gravity and radius of inertia; the 120 t limit for handling by mobile cranes. The Macagno transmission formula. The finding that the critical wave periods for the PV array are 1–3 s and that the unit reduces them to a transmission coefficient of 0.4 or less, and that floating breakwaters do little for periods of 5–7 s and longer |
| D5.1 (MARIN, SINTEF) | 10 MW ring of 56 breakwater pontoons. Natural periods of the unit: roll 3.75 s, heave 3.57 s ("the breakwater rolls in short waves"). Hinge-load response of the array peaks at wave periods of 1.2–2 s. The largest mooring line loads come from short, steep waves (Mediterranean: Hs 2.0 m, Tp 3.6 s). Site water depth 38 m (Mediterranean) |
| D7.4 version 2.0 and cost model v3 | Conventional breakwater for 10 MW: €1,221,594, which is tonnes × €/t of concrete, EPS and reinforcement. Structural steel (214.9 t at €600/t) and rubber (31.9 t at €400/t) for all 91 pontoons: €141,700. Installation of the 91 pontoons (56 breakwater, 35 bridge) €798,000. Anchors 58.4 t at €2,000/t and chains 30.6 t at €3,000/t with 26 anchors (Mediterranean 10 MW case); the model uses these weights as totals, while the glossary defines them per anchor and per chain. Array to breakwater 30 m (15 m to the transition element plus 15 m) for 10 MW, 7.5 + 7.5 m for 2 MW |
| Proposal (Annex 1 Part B) | Power density of the plant area, 150 W/m² (the D7.4 ring layout gives about 145 W/m²) |

## 2. Wave classes

Nearshore design waves are limited by the fetch, the stretch of open water the wind blows over towards the site. The classes use fetch-limited JONSWAP spectra, with the SPM 1984 growth curves, a design wind of 22 m/s at 10 m (adjusted wind 31.8 m/s) and a peak enhancement factor of 3.3:

| Wave class | Design Hs (m) | Peak period (s) | Fetch at U10 22 m/s (km) | Typical depth (m) | Short-wave Hs, ≤ 3 s (m) | Platform |
|---|---:|---:|---:|---:|---:|---|
| mild | 0.65 | 2.3 | 1.6 | 8 | 0.64 | sheltered |
| medium | 1.00 | 3.1 | 3.8 | 12 | 0.76 | sheltered |
| rough | 1.30 | 3.7 | 6.4 | 20 | 0.69 | exposed |

A site whose short waves stay below about 0.45 m and whose total design wave height stays below 0.6 m needs no breakwater. Above about 1.3 m, or with open-sea swell, the site is in the open-sea class that SUREWAVE designed for, with design waves up to 6.5 m in the Mediterranean contour.

## 3. Breakwater classes

### 3.1 Sizing criteria

Both criteria are applied to the spectrum transmitted behind the breakwater, with the Macagno formula used in D3.2 and D5.1:

1. Short waves, periods of 3 s and less: transmitted significant height at most 0.45 m. That is a 0.5 m limit with a 10 % margin [to confirm]. This is the band D3.2 names as critical for the PV array, and where D5.1 finds the hinge-load response peaking.
2. All waves: transmitted significant height at most the platform's limit for the longer waves the hinged array rides. The limit is 0.6 m for the sheltered-site platform and 0.8 m for the exposed-site platform under development in the EIC Transition proposal [both to confirm].

Longer waves pass a floating breakwater largely unattenuated, so criterion 2 decides the class at medium and rough sites. Rough sites therefore need the exposed-site platform, even behind the SUREWAVE unit.

Cross-sections keep a width-to-draft ratio between 2 and 3, near that of the SUREWAVE unit (2.5), with a minimum width of 2.5 m for stability and access. Wider, shallower pontoons look better in the Macagno formula, but they follow the waves, which the formula does not capture.

### 3.2 Search and chosen classes

The lightest cross-section meeting both criteria, found by search in steps of 0.5 m width and 0.1 m draft:

| Wave class | Lightest section (W × d, m) | Short-wave Hs at array (m) | Total Hs at array (m) |
|---|---|---:|---:|
| mild | 2.5 × 0.9 | 0.27 | 0.28 |
| medium | 3.0 × 1.2 | 0.34 | 0.60 |
| rough | 4.5 × 1.5 | 0.18 | 0.78 |

The medium and rough search results sit at the limit of criterion 2. The chosen classes add margin:

| Breakwater class | For waves | Anchoring | Width × draft × height (m) | Mass per 20 m unit (t) | Short-wave Hs at array (m) | Total Hs at array (m) | Limit total (m) | Freeboard / crest of the largest wave (m) |
|---|---|---|---|---:|---:|---:|---:|---|
| light | mild | weak | 2.5 × 1.0 × 1.5 | 30 | 0.25 | 0.26 | 0.60 | 0.50 / 0.60 |
| medium | medium | medium | 4.0 × 1.5 × 2.2 | 73 | 0.24 | 0.47 | 0.60 | 0.70 / 0.93 |
| heavy | rough | strong | 5.0 × 2.03 × 2.5 (SUREWAVE unit) | 123 | 0.13 | 0.67 | 0.80 | 0.47 / 1.21 |

The rough class is the SUREWAVE unit itself, so the SUREWAVE breakwater is the heavy class of the family. The lighter classes are scaled-down versions with the same construction and double-keel shape. A 30 t light unit can be cast, trucked and lifted with ordinary harbour equipment, so small sites need no heavy marine plant.

Checks on the cross-sections:

- Freeboard: the crest of the largest wave (about 1.86 Hs high) exceeds the freeboard in all three classes, so some overtopping occurs in design storms, as it does for the SUREWAVE unit at its design sites. Macagno does not include overtopping, so transmission in storms is somewhat higher than shown.
- Resonance: D5.1 gives the SUREWAVE unit natural periods of 3.75 s in roll and 3.57 s in heave. Scaled by Froude similarity with the width, the classes have natural periods of about 2.7 / 2.5 s (light), 3.4 / 3.2 s (medium) and 3.8 / 3.6 s (heavy), close to the peak periods of their own design waves (2.3, 3.1 and 3.7 s). Near resonance a floating breakwater moves most and radiates waves on its lee side. The rigid Macagno formula is least reliable there, and D5.1 finds the largest line loads at such short periods. The transmitted heights are therefore probably higher than shown, and the classes may need to be heavier, better damped (keels, mooring stiffness) or detuned. This is the main technical uncertainty of the classes.

### 3.3 Anchoring classes

Anchoring follows the wave class:

- weak anchoring for short, low waves in shallow water;
- medium anchoring;
- strong anchoring as for the SUREWAVE heavy unit at nearshore depths.

Line loads scale with the square of the design wave height, relative to Hs 2.0 m where D5.1 finds the largest line loads. Chain length scales with depth.

## 4. Indicative cost per metre

### 4.1 Build-up

D7.4 costs the breakwater pontoons as material per tonne (concrete €100/t, EPS €1,100/t, reinforcement €980/t), rates that sit between bare material and in-place prices, plus steel and rubber for couplings and fenders, also per tonne. Casting labour, formwork and moulds, the yard and transport to site are not listed separately. The build-up therefore adds them as assumptions:

1. Material: €1,091 per metre for the heavy unit (€1,221,594 / 1,120 m), scaled with the cross-section for lighter classes.
2. Fabrication (casting labour, formwork and moulds, yard, curing, quality control): 1.0 × the material cost [to confirm; range 0.5–1.5].
3. Couplings and fenders: D7.4's steel and rubber, €1,557 per pontoon, times 2.0 for machining, galvanising and fitting [to confirm].
4. Transport from yard to site: €4,000 per heavy unit [to confirm].
5. Installation: €8,770 per pontoon from D7.4 (€798,000 / 91), €438 per metre for a 20 m heavy unit.

For items 3–5, 20 % of the cost is fixed per unit and 80 % scales with the cross-section for lighter classes [to confirm].

6. Anchoring: D7.4's anchors and chains per metre as its model uses them (as totals), scaled with line load and depth (section 3.3), with a floor of 35 % for practical minimum anchoring. An open arc lacks the closed ring's self-restraint, so it is multiplied by 1.5; closed rings are not. Two extra anchor sets are added at each open end, in the site cost. Section 4.3 shows the alternative reading of D7.4's weights.
7. Supplier factor: 1.25 for the supplier's design, project management and margin [to confirm].
8. Mobilisation: €40,000 per site for crane, tug and crew [to confirm], in the site cost.

| Breakwater class | Material | Fabrication | Couplings, fenders | Transport | Installation | Anchoring | Production | Installed incl. supplier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| light | 269 | 269 | 62 | 79 | 174 | 64 | 916 | 1 146 |
| medium | 645 | 645 | 105 | 135 | 295 | 68 | 1 892 | 2 365 |
| heavy (nearshore) | 1 091 | 1 091 | 156 | 200 | 438 | 93 | 3 069 | 3 836 |
| Open-sea reference: D7.4 ring built the same way (closed ring, Mediterranean loads, 38 m) | | | | | | | | 3 952 |

All figures are € per metre, open arcs. A light breakwater costs about 30 % of the heavy one per metre. The fabrication factor moves the installed cost by about €170 (light), €400 (medium) and €680 (heavy) per metre for each 0.5 up or down.

### 4.2 Comparison with D7.4

On D7.4's own basis (material, couplings and fenders, 56/91 of the pontoon installation, anchoring), the 10 MW ring costs about €201/kWp, or €251/kWp with the supplier factor. Built up the same way as the classes here, with open-sea loads and a closed ring, it costs about €443/kWp. The difference comes from the assumptions added here: fabrication, extra work on couplings, and transport. If D7.4's per-tonne rates do not include casting labour, formwork and yard costs (question 3 in section 8), D7.4's breakwater cost is too low by roughly that much.

### 4.3 Anchoring: two readings of D7.4

Update 2026-11-23: Clement's report on material demand (3 February 2025, Tables 9 and 11–13) gives the anchor and chain weights per pile and per chain, with their numbers, so the per-anchor reading below is the correct one. D7.4 version 2.0 is delivered with the cost model v3 and its anchoring as modelled, and is not corrected. For SUREWAVE documents (D8.4) the "as modelled" figures apply; the per-anchor figures are for Sunlit Sea's internal use.

D7.4's model multiplies its anchor and chain weights (58.4 t and 30.6 t) by the price per tonne as totals for all 26 anchors, about 2.2 t per anchor. Its glossary defines them as the weight per anchor and per chain. A 2.2 t anchor is small for the line loads in D5.1 (up to 3,467 kN in the Mediterranean). The per-anchor reading is physically more plausible.

If the weights are per anchor and per chain, anchoring rises about 26-fold:

| Breakwater class | Anchoring €/m | Installed €/m incl. supplier |
|---|---:|---:|
| light | 1 659 | 3 140 |
| medium | 1 777 | 4 501 |
| heavy | 2 430 | 6 757 |
| Open-sea reference (D7.4 ring) | | 9 774 |

| Standard site (3.2 MWp) | €/kWp to the solar plant, anchoring per anchor |
|---|---:|
| A Mild: one exposed side | 401 |
| B Medium: two exposed sides | 633 |
| B' Medium, half paid by dual use | 317 |
| C Rough nearshore: three sides | 1 333 |

For the light and medium classes these figures are an upper bound: the scaling keeps the 35 % floor and scales load only with wave height, while smaller breakwaters reflect less and need fewer, lighter lines. For D7.4 itself the reading matters: at about €9,800 per metre, the open-sea ring would cost about €1,100/kWp instead of about €200/kWp, which would change D7.4's results. Which reading is right should be settled with Clement, who supplied the mooring specifications (question 4) [Eirik to decide how to raise it with the coordinator].

## 5. Coverage method

### 5.1 Formula

The plant is taken as a circle of radius r, with area set by the power density (150 W/m²). The breakwater stands at a stand-off s from the array edge: 15 m including the transition element [to confirm; D7.4 uses 30 m at 10 MW and 15 m at 2 MW]. The exposure sector θ is the share of the 360° from which design waves come, widened by 10° of directional spreading on each side.

Two layouts are compared, and the shorter is used.

Arc of radius R = r + s around the plant centre. To shield the whole array from every direction in the widened sector, the arc spans the sector plus the array's angular width seen from the arc:

L_arc = R · (θ + 2·asin(r / R)) + 2e.

Straight breakwater tangent to the stand-off circle, facing the centre of the sector, for sectors up to 120°:

L_straight = 2·(r + s)·tan(θ / 2) + 2r·sec(θ / 2) + 2e.

The end extension e covers waves bending around the ends. At the geometric shadow line the diffraction coefficient is about 0.5 and falls inside the shadow (straight-edge approximation). The extension is the distance at which it falls to the allowable short-wave height over the incident short-wave height, with a minimum of 10 m [to confirm]. For all three classes the target is above 0.5, so the minimum governs.

A closed ring (2πR) has no ends and needs no open-arc anchoring; it is used when the arc would exceed it. The length is rounded up to whole 20 m units. Then:

Cost = units × 20 m × installed €/m + end anchor sets + mobilisation.

If another use (boat berths, a bathhouse or sauna platform, a boathouse, a café) carries a share f of the breakwater, the solar plant carries (1 − f).

Calibration: for 10 MWp with D7.4's 30 m stand-off, the full ring comes out at 1,104 m, against 1,120 m in D7.4 (ratio 0.99).

Exposure classes:

- mild: about 20°, one exposed side;
- medium: about 60°, two sides or one long side;
- rough: about 180°, three sides.

Exposure and wave class are separate axes. A site can be exposed from one direction only but to rough waves, and the breakwater class follows the waves.

### 5.2 Standard sites (3.2 MWp)

| Standard site | Plant (kWp) | Exposure | Class | Layout | Breakwater length (m) | Units | Cost (k€) | €/kWp | €/kWp to the solar plant |
|---|---:|---:|---|---|---:|---:|---:|---:|---:|
| A Mild: one exposed side | 3 200 | 20° | light | straight | 266 | 14 | 375 | 117 | 117 |
| B Medium: two exposed sides | 3 200 | 60° | medium | arc | 352 | 18 | 906 | 283 | 283 |
| B' Medium, half paid by dual use | 3 200 | 60° | medium | arc | 352 | 18 | 906 | 283 | 141 |
| C Rough nearshore: three sides | 3 200 | 180° | heavy | arc | 556 | 28 | 2 205 | 689 | 689 |

### 5.3 Effect of plant size (€/kWp)

| Plant size (kWp) | A mild, light, 20° | B medium, medium, 60° | C rough, heavy, 180° | Full ring, heavy |
|---:|---:|---:|---:|---:|
| 350 | 547 | 1 101 | 2 793 | 3 152 |
| 1 000 | 260 | 574 | 1 361 | 1 559 |
| 3 200 | 117 | 283 | 689 | 748 |
| 10 000 | 58 | 152 | 374 | 391 |

## 6. What this means

- A breakwater is a large cost at nearshore scale. With D7.4's anchoring as modelled, a light breakwater on one side of a 3.2 MWp plant costs about €0.12/W, close to a fifth of the EPC direct cost in the financial plan (€0.64/W). A medium site costs about €0.28/W. With the per-anchor reading of D7.4's anchoring, both are higher, up to about €0.40 and €0.63/W.
- Three levers bring the cost down, each by about half or more:
  - Sheltered water: sites below the thresholds in section 2 need no breakwater at all.
  - Plant size: cost per kWp roughly halves from 3.2 to 10 MWp.
  - Dual use: with half paid by berths or a platform, a medium site costs the solar plant about €0.14/W, close to a mild site without dual use.
- Below about 1 MWp the breakwater costs €260/kWp or more even at a mild site. Small plants need water that is sheltered already: behind an existing quay or marina breakwater, or a dual-use structure that the host wants anyway.
- Rough nearshore sites need both the SUREWAVE heavy unit and the exposed-site platform, at about €0.69/W for 3.2 MWp and €0.37/W for 10 MWp. That is the territory of the exposed-site demonstrator (EIC Transition), where larger plants and dual use must carry the cost.
- Dual use gives the breakwater case for CINEA its clearest form: the breakwater is built for berths, a bathhouse platform or other buildings, and the solar plant shares it. Floating buildings, marinas, passenger terminals and leisure infrastructure are all named as applications in Clement's exploitation summary, and, according to Eirik, Clement is moving further into such projects.
- Check on the financial plan: its sensitivity "breakwater on one side, not priced in" used €0.04/W. The figure here for a mild 3.2 MWp site is about €0.12/W. The plan's sensitivity should be updated when the Booster work resumes (T161).
- Sunlit Sea's planning tool already computes wave and wind conditions along the full perimeter of a planned plant, a SUREWAVE result. It can supply the exposure sector and wave class per site, so the method can be run for real sites.

## 7. Limits of the method

- Macagno treats the breakwater as rigid and fixed. D3.2 finds it good for short periods but optimistic as periods grow and the breakwater moves. All three classes have natural roll and heave periods close to the peak period of their design waves (section 3.2), where a moving breakwater transmits more. The classes may need to be heavier or better damped once this is modelled.
- The plant is a circle. Long, narrow plants placed parallel to the exposed side need a shorter breakwater; the method can be extended with the plant's width facing the waves.
- Directional spreading is set at 10° on each side of the exposure sector. Wind seas spread wider, but the energy at the edges is lower; whether the lengths are conservative or not depends on the site.
- The diffraction estimate is a straight-edge approximation. Reflection from the shore and refraction are not modelled.
- The allowable heights at the array (0.45 m for short waves; 0.6 m and 0.8 m in total) are assumptions. They should come from the hinge and float design limits of CONNECT, for the sheltered-site and exposed-site versions.
- Ice, navigation markings and lights, seabed conditions and permits are not in the cost.
- The cost build-up beyond D7.4 (fabrication, couplings, fenders, transport, supplier factor, mobilisation, anchoring scaling) is reasoning, not quotes.

## 8. Questions for Clement Germany

1. Are the three cross-sections (2.5 × 1.0 m, 4.0 × 1.5 m, 5.0 × 2.03 m) reasonable for the wave classes? Would Clement use other standard types for mild and medium sites, for example from its marina range? How would Clement keep the light unit's centre of gravity low?
2. Are the installed costs per metre (about €1,150, €2,350 and €3,850 with D7.4's anchoring as modelled) in the right range for a 200–600 m breakwater, including fabrication, couplings, fenders, transport, design and margin?
3. Does D7.4's per-tonne pontoon cost include casting labour, formwork and yard costs, or only material? This decides whether D7.4's breakwater cost needs correcting.
4. Are D7.4's anchor and chain weights (58.4 t and 30.6 t for the Mediterranean 10 MW ring) totals or per anchor and per chain? Which mobilisation cost, and how many anchor lines per metre and at the ends, are typical for an open arc at a nearshore site?
5. With natural roll and heave periods close to the design wave periods, how would Clement damp or detune the lighter classes?
6. For dual-use breakwaters (berths, bathhouse or sauna platforms, boathouses, cafés), what extra cost per metre does the added function bring, and who usually pays for it?
7. Can Clement share one or two anonymised examples of breakwaters at sheltered sites, with length, type and cost?

## Assumptions to confirm

- Allowable heights at the array: short waves 0.45 m; total 0.6 m (sheltered-site platform) and 0.8 m (exposed-site platform).
- Design wind 22 m/s at 10 m.
- Stand-off 15 m from the array edge.
- Directional spreading 10° on each side.
- Minimum end extension 10 m.
- Minimum width 2.5 m.
- Fabrication factor 1.0 (range 0.5–1.5).
- Couplings and fenders: D7.4 steel and rubber times 2.0; transport €4,000 per heavy unit; fixed share 20 % for per-unit items.
- Anchoring as modelled in D7.4 (totals); the per-anchor reading as the alternative.
- Anchoring floor 35 %, open-arc factor 1.5, two extra anchor sets per open end.
- Supplier factor 1.25.
- Mobilisation €40,000 per site.
- Power density 150 W/m².
