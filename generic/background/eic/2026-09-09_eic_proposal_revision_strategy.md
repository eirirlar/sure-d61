---
title: "EIC Transition SUREWAVE_EIC — proposal revision strategy"
author: Sunlit Sea AS (Eirik Larsen)
date: 2026-09-09
type: Internal review and revision strategy for the SINTEF-coordinated EIC Transition proposal
reviewed_document: generic/background/eic/2026-09-09_sintef.md (SINTEF draft, 9 September 2026)
call: HORIZON-EIC-2026-TRANSITIONOPEN
status: Internal working note — not consortium-facing in this form
---

# EIC Transition SUREWAVE_EIC — proposal revision strategy

## 0. Caveat on call rules

Everything below about scoring, thresholds, duration limits and the Booster Grant must be checked
against the **2026 EIC Work Programme and the call text on the Funding & Tenders portal** before it
is acted on. Where a point depends on a call rule I am not certain of, it is marked **[VERIFY]**.
The substance of the review — consistency, argument quality, evidence — does not depend on those
checks.

---

## 1. Bottom line

The draft has a strong Excellence narrative and a genuinely good technical story. It is not
submittable in its current state, for three reasons, in order of severity:

1. **The proposal describes a marine nearshore demonstration; the consortium has decided on a
   freshwater lake.** The text still says the demonstrator goes in **Trondheim**, calls WP6
   "Demonstrator Sea Trials", and builds the whole Excellence and Impact case on "nearshore",
   "coastal" and "marine". The actual site is Hainer See, an inland lake in Saxony. This is not a
   find-and-replace problem. It goes to the heart of the TRL 6 claim, and an evaluator will find it
   in the first ten minutes.
2. **The Impact section is empty.** Sections 2.1, 2.2 and 2.3 contain only the template's guidance
   text plus one answered question. Impact is one of three scored criteria. As submitted today,
   the proposal would likely fail the Impact threshold on completeness alone.
3. **The document contradicts itself throughout.** Duration is M36 in one table and M42 in another.
   Deliverables reference a WP8 that does not exist. A deliverable is assigned to WavEC, who left
   the consortium five days ago. There are two tasks numbered 2.3. Cross-references point at task
   numbers that were deleted. This is exactly what the "Quality and efficiency of the
   implementation" criterion is designed to catch.

The good news: none of this is a technology problem. The technology case is genuinely strong and
unusually well de-risked for a Transition call. The work needed is writing, arithmetic and
decision-making, not research.

### Triage against the deadline

The deadline is roughly a week away. Prioritise like this.

| Priority | Item | Owner | Why |
|---|---|---|---|
| **P0 — must** | Resolve the site/environment framing (§2) | Eirik + Balram | Everything else depends on it |
| **P0 — must** | Fill Impact 2.1 / 2.2 / 2.3 | EDP + Eirik | A scored criterion is blank |
| **P0 — must** | Fix duration, WP numbering, dead cross-references (§4) | Balram | Cheap; costs points if left |
| **P0 — must** | Person-month table, budget table, subcontracting table | Balram | Mandatory; lump-sum call |
| **P1 — high** | Concrete, measurable technology KPIs (§6) | Eirik + SINTEF | Named EIC criterion |
| **P1 — high** | IP / patent position, even if the answer is "trade secret" | Eirik | Blank patent table is a red flag |
| **P1 — high** | Annex the Hainer See LOI and an EDP letter of support | Balram | Turns a claim into evidence |
| **P2 — if time** | Cut deliverable count from 24 to ~14 (§9) | Balram | Improves credibility |
| **P2 — if time** | Trim WP3 research creep (§9) | Balram | Removes a reviewer objection |
| **P3 — skip** | Gender dimension, open science | Balram | Two short honest paragraphs; do not overinvest |

---

## 2. The decision that comes first: what "relevant environment" means

This is the single most important thing in the whole revision, so it goes first.

### The problem

TRL 6 is *"technology demonstrated in a relevant environment"*. The proposal defines the end-user
application as **"nearshore renewable electricity generation"** in a **marine** setting, and claims
the project reaches TRL 6. The demonstration will happen in a **freshwater lake**.

An evaluator will ask, correctly: *if your market is exposed coastal water, how does a lake
demonstrate the relevant environment?* If the proposal has no crisp answer, the TRL 6 claim
collapses, and with it the Excellence and Impact cases. This is the highest-probability reason for
rejection.

### The answer to give

Do not defend the lake as "almost marine". Redefine "relevant environment" by the **load envelope**,
which is what actually drives the engineering, and then be honest and specific about what the lake
does *not* cover and how that gap is closed by other evidence.

**Argument, in the order it should appear in the text:**

1. The SUREWAVE breakthrough is *wave-load management*, not corrosion management. The technical
   barrier the breakwater removes is wave-induced motion, structural load and fatigue on the PV
   array. The relevant environment is therefore defined by significant wave height, wave period,
   fetch, wind and thermal/UV cycling.
2. Hainer See delivers a genuine load case: ~3 km fetch in the prevailing W/SW direction, wind
   waves around 1 m, adequate depth. State the design load cases and show the site covers them.
   (Eirik's note of ~1.5 m and Thomas's ~1 m need to be reconciled to one sourced number before
   this goes in writing.)
3. Name the boundary explicitly. A lake does **not** cover: salinity and galvanic corrosion,
   biofouling, tidal range, long-period swell, and marine navigation/permitting regimes.
4. Close each of those gaps with evidence that exists or can be cheaply generated:
   - **Salinity and corrosion** — Sunlit Sea's Gen 1 units already operate in Norwegian salt water;
     add an accelerated salt-spray and immersion programme on production-representative coupons and
     assemblies, run in parallel with the lake demonstration. This is cheap and it is the single
     highest-value addition available to this proposal.
   - **Swell** — covered analytically. The MARIN basin campaigns already tested harsh irregular
     seas; state that the validated models are exercised over the marine load envelope in WP3 and
     validated against the lake data at the overlapping conditions.
   - **Biofouling and tidal** — declare them out of scope for TRL 6 and name them as the content of
     the *next* step. This is a strength, not a weakness: it shows a credible staged plan.
5. State the TRL claim precisely. Something like: *"TRL 6 for the integrated protected-FPV system
   over the wave-load envelope characteristic of exposed inland and sheltered nearshore water
   bodies; the marine-specific corrosion and fouling envelope is addressed by parallel accelerated
   testing and is the subject of the first commercial deployment."*

### The site question with EDP

EDP's board joined on condition of exploring a Portuguese demonstration. Balram has proposed a six
month comparison of the two sites. **Do not put an open site decision in the implementation plan.**
For a Transition call, an unresolved demonstration site at proposal stage reads as immaturity and
invites a low Implementation score. Reviewers want a named site with permitting status.

The way to satisfy both: **name Hainer See as the demonstration site**, with the LOI and permitting
status annexed, and place the Portuguese site in the **business work package** as a
*replication and second-market study* — a real, funded task producing a site-transfer assessment
and a European replication map. EDP leads it. Their board gets Portuguese content and a route to a
follow-on installation; the implementation plan keeps one site and one schedule.

This is also the strongest available form of Eirik's argument in the 9 September mail: it protects
the schedule without telling EDP no.

---

## 3. Section-by-section review

### 3.1 Excellence — currently the strongest section

**What works.** The "protected operating environment" framing is genuinely good and is the sentence
the whole proposal should hang on. The de-risking argument (two MARIN campaigns, hinge redesign
after identified failure modes, validated model chain) is exactly what a Transition evaluator wants
to see, because it distinguishes a Transition proposal from a Pathfinder one.

**What to fix.**

- Remove "Trondheim" (line 123 of the draft). Remove every instance of "nearshore", "coastal",
  "marine", "offshore" and "sea trials" that describes the *demonstration*, and keep them only where
  they describe the *target market*. Make the distinction explicit and deliberate rather than
  accidental.
- Reconcile the TRL statement. The text says TRL 4-5 in one place and TRL 5 in another. Pick TRL 5
  and substantiate it in one paragraph.
- Fix the truncated citation `[mordorinte...igence.com]`, which appears three times. Every market
  claim needs a real, citable source with a year. ">20% CAGR" and "hundreds of gigawatts" with no
  source will be read as unsupported.
- Compress the objectives. Ten objectives (O1–O10) is too many; several are restatements. Five to
  six, each with a number attached, reads as more disciplined.
- The technology objectives have no measurable targets. "Collection of high-quality operational
  data" is not a target. See §6.

### 3.2 Impact — currently the weakest section by a wide margin

Sections 2.1 (business model, IP, commercialisation), 2.2 (economic and societal benefits) and 2.3
(investment readiness) are **empty**. Only the "path to market" question is answered, and that
answer is good. This is the single largest scoring risk after the site framing.

**2.1 — what must be written.**

- The methodology for validating the business model. Not "we will engage stakeholders" — say how
  many interviews, with which customer segments, on what schedule, producing which artefact.
- IP strategy. The patent table is empty. For an EIC Transition proposal, an empty IP section is a
  red flag: the call is about turning research results into a defensible commercial asset. If there
  are no granted patents, say so plainly and state the strategy that replaces them: which elements
  are trade secrets (PU formulation, casting process, hinge geometry tolerances), which are
  know-how held in manufacturing, what the freedom-to-operate position is, and what will be filed
  during the project. A deliberate trade-secret strategy, argued well, scores. A blank table does
  not.
- Regulatory, certification and standardisation. This is a real strength that is currently
  underplayed. DNV-RP-0584, and the new DNV-ST-C108 and DNV-ST-E309 released in May 2026, give a
  concrete certification pathway. Say that the project produces a certification-ready documentation
  set, and name DNV as a subcontractor for an independent statement (see §7). For an evaluator
  assessing bankability, an external certification body in the plan is worth more than three
  paragraphs of assertion.

**2.2 — what must be written.**

- Scale-up potential with arithmetic, not adjectives. Take the demonstrator cost, apply a stated
  learning rate and stated economies of scale, and give a target LCOE at 10 MW and 50 MW with the
  assumptions visible.
- EU strategic autonomy. This is a strong and currently unused argument. Sunlit Sea manufactures in
  Norway; the breakwater is European concrete produced by CLEMENT in Germany; the value chain is
  European end to end, in a sector where module supply is dominated by non-EU manufacturing. Say
  this explicitly and connect it to the EU's stated solar manufacturing objectives.
- Land use. Say what a gigawatt of protected FPV saves in hectares of land, with a source.
- Employment and regional effect, briefly and concretely.

**2.3 — what must be written.**

- The go-to-market pathway selection box in the template is unanswered. Answer it.
- Time to market. Give a year and a first commercial project scale.
- Revenue model. Sunlit Sea sells systems; EDP develops projects. Say which revenue accrues where,
  and what the CA will need to say about it.
- The financing plan. If a raise is planned during or shortly after the project — Eirik's own
  material references a planned emission — say so, with a target size and use of funds. EIC
  explicitly asks for this.
- Named investor and customer engagement. The existing pipeline (Endra, Fagne, Haugaland
  Næringspark) is real evidence and should be used, with permission.

### 3.3 Quality and efficiency of the implementation — structurally broken, easily fixed

The narrative parts are fine. The tables and the numbering are not. See §4 and §5.

Two specific content gaps:

- **Section 3.2 (KPIs, milestones and risks narrative) is empty.** The tables 3.3d and 3.3e exist
  and are decent, but the criterion explicitly asks for a narrative here. Two or three paragraphs.
- **Partner-number justification is missing.** The criterion asks "is the number of project
  partners well justified?". Four partners after WavEC's departure. Write one short paragraph
  explaining why four is right: technology owner, breakwater and marine works, research and
  modelling, end user. Note that the consortium was deliberately reduced to concentrate budget on
  the demonstrator. Framed that way, WavEC's departure becomes evidence of discipline rather than
  instability.

---

## 4. Hard defects — the fix-list

These are objective errors. Each one is cheap to fix and each one costs points.

| # | Defect | Where | Fix |
|---|---|---|---|
| D1 | Demonstrator located in "Trondheim" | Excellence, breakthrough section | Hainer See, or the agreed framing per §2 |
| D2 | Duration is M36 in table 3.3a, M42 in WP1/WP6/WP7 task text, deliverables and MS7 | Throughout | Choose one. **36 months recommended** — the template's own reporting-period table stops at 36, and a shorter project reads better for a Transition call |
| D3 | Deliverables D8.1–D8.7 reference a **WP8 that does not exist** (only WP1–WP7 defined) | Table 3.3c | Renumber to the final WP set |
| D4 | D7.1–D7.4 are validation deliverables but WP7 is the exploitation WP | Table 3.3c | Renumber |
| D5 | **D4.2 is assigned to WavEC**, who left the consortium on 4 September | Table 3.3c | Reassign to SINTEF |
| D6 | T4.1 text references "the **WavEC** data-acquisition platform in **T4.3**" — wrong partner, and T4.3 does not exist | WP4 | Rewrite |
| D7 | **Two tasks numbered 2.3** ("Floating Breakwater Optimization" and "FPV Platform Design") | WP2 | Renumber; note this also breaks T2.4 |
| D8 | "WP6.4 Reliability Assessment" is a task, not a work package | WP6 | Renumber to T6.4 |
| D9 | T7.1 and T7.3 reference "Task 8.2" / "T8.2 engagement stream" | WP7 | Fix cross-references |
| D10 | Demonstrator scale is 200–300 kWp in the narrative, 50–300 kWp in T2.1 and T5.2 | Throughout | Commit to **one number**. Lump-sum funding requires defined scope; a 6× range invites a scope objection |
| D11 | PM column in table 3.3a is **empty**; table 3.3f is **empty** | Tables | Mandatory. Fill |
| D12 | Table 3.3g (subcontracting) and 3.3h (purchase costs) are **empty** | Tables | Mandatory where thresholds are met. See §7 and §8 |
| D13 | Patent table is **empty** | Section 3 | Fill, or state the trade-secret strategy — see §3.2 |
| D14 | Women-led consortium box unanswered | Table 3.3a area | Tick it. Coordinator main contact is Balram, so the answer is No unless the coordinator contact changes **[VERIFY the exact definition in the call]** |
| D15 | Gender dimension and open science questions unanswered | Excellence | Two short honest paragraphs each |
| D16 | Cover page confirmation boxes unticked; "other linked projects" table left as template placeholder text | Cover page | The template warns this can make the proposal **inadmissible**. Check before submission |
| D17 | T2.3 and T5.4 text contains PDF-extraction damage — "instru ments", "Sun lit Sea", "anacceleratedversionof" | WP2, WP5 | Proofread; this text came out of a PDF and the word-breaks survived |
| D18 | T2.2 participants listed as "XXX" | WP2 | Fill in |
| D19 | Duplicate paragraph in T2.3 breakwater task ("The resulting optimised design forms the technical basis...") appears twice | WP2 | Delete one |
| D20 | Reporting periods described as "M1 to M24 and M25 to M42" in T1.1, but the template table gives 12+24 for a 36-month project | WP1 | Align to the chosen duration |

---

## 5. Recommended work-package restructure

The current structure has seven WPs, broken numbering, a monitoring WP that is really part of
manufacturing, and site selection buried in WP6 at the *end* of the design chain even though WP2
depends on it. Reviewers notice dependency inversions.

Proposed six-WP structure, 36 months:

| WP | Title | Lead | Months | Rationale |
|---|---|---|---|---|
| WP1 | Management, IP and innovation management | SINTEF | M1–M36 | Unchanged |
| WP2 | Site characterisation and demonstrator engineering | Sunlit Sea (FPV) + CLEMENT (breakwater/mooring) co-lead | M1–M12 | Site is *fixed* at proposal stage; this WP characterises it, not selects it |
| WP3 | Design verification and model validation | SINTEF | M1–M36 | Tightly scoped — see §9 |
| WP4 | Manufacturing, instrumentation and factory acceptance | Sunlit Sea (FPV) / CLEMENT (breakwater) | M9–M20 | Monitoring hardware folded in; instruments are installed at build time anyway |
| WP5 | Deployment, operation and validation campaign | CLEMENT | M18–M32 | Renamed away from "Sea Trials" |
| WP6 | Business validation, exploitation and dissemination | EDP + Sunlit Sea | M1–M36 | Includes the Portuguese replication study |

Notes:

- **Co-leading WP2** resolves the open item Eirik already flagged: Sunlit Sea owns the FPV side,
  CLEMENT owns the breakwater and mooring side, and neither is subordinate to the other. It also
  matches where the money sits.
- Folding monitoring into manufacturing removes a WP and removes the WavEC-shaped hole.
- Site selection disappears as a task. Site *characterisation* remains, which is real work.

---

## 6. KPIs — the current set is not measurable

The business KPI table is good and should be kept nearly as is. The **technology** objectives have
no numbers at all. EIC names KPIs as an explicit sub-criterion. Proposed set, to be checked against
what the engineering can actually commit to:

| # | KPI | Target | Verified by | Month |
|---|---|---|---|---|
| K1 | Wave-height reduction behind the breakwater vs. incident | ≥ 50 % at design Hs | Wave gauges fore and aft | M30 |
| K2 | Peak structural load on FPV connectors vs. unprotected prediction | ≤ 50 % | Load cells at CONNECT hinges | M30 |
| K3 | System availability over the operational campaign | ≥ 95 % | Inverter and SCADA logs | M32 |
| K4 | Performance ratio of the FPV array | ≥ 0.80 | DC/AC metering vs. irradiance | M32 |
| K5 | Units with detected water ingress after 12 months | 0 of N instrumented units | Embedded ingress sensors | M32 |
| K6 | Mooring line peak tension vs. model prediction | within ± 20 % | Mooring load cells vs. WP3 | M30 |
| K7 | Model prediction error, motions and loads | ≤ 20 % on the validated envelope | T3.3 validation report | M34 |
| K8 | Modelled LCOE at 10 MW commercial scale | target value in €/MWh, stated | Techno-economic model | M34 |
| K9 | Corrosion/salt exposure programme | completed on production-representative samples | Accredited lab report | M30 |

Every one of those numbers must be one the consortium is willing to be measured against. It is
better to state a modest number and hit it than an ambitious one that becomes a review finding.

---

## 7. Subcontractors

The call requires each participant to describe and justify subcontracted tasks, and warns that
**core tasks should not be subcontracted**. Table 3.3g is currently empty. Recommended contents.

### Include

| Subcontractor | For | Approx. | Why it belongs |
|---|---|---|---|
| **DNV** (or equivalent notified body) | Independent design-basis review and a statement of conformity against DNV-RP-0584 / ST-C108 / ST-E309 | €40–70k | The strongest single bankability signal available. Converts "certification-ready" from a claim into a third-party artefact. Directly serves the Investment Readiness criterion |
| **Norsmaterials** (or Tongge) | Cast-PU frame production, supplier qualification, UV-resistant formulation development | ~€55k | Already in Sunlit Sea's plan. Justify as specialist process capability Sunlit Sea does not hold in-house |
| **Accredited materials/environmental test lab** | Salt-spray, immersion, UV and accelerated-ageing programme on production-representative samples | €25–40k | This is what closes the freshwater-lake credibility gap identified in §2. Highest value per euro in the whole proposal |
| **German permitting / environmental consultant** | Water-body permits, environmental screening, local authority liaison at Hainer See | €20–30k | Local regulatory competence; de-risks the schedule and shows the permitting path is understood |
| **Local electrical contractor (DE)** | Grid connection and AC-side works at the site | €30–50k | Routine local works; not a core task |
| **Marine warranty surveyor / installation insurer** | Independent review of the installation plan | €10–20k | Standard practice for a floating installation; another bankability signal, cheap |
| **Assembly labour** | Peak-load assembly capacity during the build window | ~€15k | Already in Sunlit Sea's plan |
| **Communications/design agency** | Video, technical briefs, case studies | €10–15k | Small; supports dissemination |

### Consider, but probably not

- **MARIN.** Considered earlier as a third-country partner and dropped when EDP confirmed. Do not
  bring them back. A further basin campaign duplicates SUREWAVE work, spends budget that has no
  room, and slightly undercuts the "already validated" argument.

### Do not subcontract

- FPV design, manufacturing and factory acceptance (Sunlit Sea core).
- Breakwater design and manufacture (CLEMENT core).
- Numerical modelling and validation (SINTEF core).
- Techno-economic analysis and business model (EDP core).

### A flag on CLEMENT's €680k

CLEMENT quoted €680k + 25 % overhead for pontoon production, delivery, towing, installation and
dismantling, based on 5 pontoons. Two questions must be answered before that number goes in a
budget table:

1. **Is CLEMENT producing the pontoons in-house, or buying them?** If in-house, it is direct cost
   and the 25 % indirect rate applies normally. If bought from a yard, it is **subcontracting**, the
   25 % flat rate does **not** apply to it, and it may run into the "core tasks should not be
   subcontracted" rule, since building the breakwater is arguably CLEMENT's core contribution.
   **[VERIFY against the call and the HE lump-sum rules.]**
2. **Does the demonstrator need 5 pontoons?** €850k all-in is roughly a third of the whole grant for
   one line item. If the wave-attenuation objective can be met with fewer, the budget problem in §8
   largely resolves itself. This should be an explicit, modelled decision in WP2, and the answer
   should be in the proposal, not deferred.

---

## 8. Budget reality check — the numbers do not currently close

Using the figures the consortium has actually produced:

| Partner | Known ask | Source |
|---|---|---|
| CLEMENT | €680k + 25 % = **€850k** | Thomas, 4 September, fixed costs only — excludes CLEMENT personnel, software licences, travel |
| Sunlit Sea | **€715k** main envelope (+ €50k Booster, separate) | Sunlit Sea contribution note, 17 August |
| **Subtotal, two partners** | **€1 565k** | |
| **Remaining for SINTEF + EDP** | **€935k** | Out of the €2.5M envelope |

SINTEF is coordinator and leads the modelling and validation work; a realistic figure is €550–650k.
EDP leads energy yield, techno-economics and business development; €200–300k. That is €750–950k,
which fits — but **only just**, with **no contingency**, and CLEMENT's number explicitly excludes
their own personnel, licences and travel.

**Conclusion: the budget is over-subscribed once CLEMENT's personnel costs are added.** This must be
resolved before submission, not after. The available levers, in the order I would pull them:

1. **Reduce pontoon count.** Largest single lever. See §7.
2. **Cut WP3 scope.** The predictive-monitoring/machine-learning task (T3.4) is the clearest
   candidate — see §9.
3. **Reduce the demonstrator kWp.** Note that this saves *less* than it appears: Sunlit Sea's own
   analysis shows roughly two-thirds of the €310k manufacturing line is scale-independent TRL-step
   cost. Cutting from 300 to 100 kWp saves on the order of €30–50k, not €200k. Say this to the
   consortium before someone assumes otherwise.
4. **Shorten the operational campaign** from the implied 12+ months. This is the lever I would pull
   last, because operational duration is the evidence the whole project exists to produce.

### One more budget point

**[VERIFY]** The €50k Booster Grant is, to my understanding, applied for *after* a project is
granted, as a separate top-up — not budgeted inside the proposal. The draft has it as **T7.5 with
its own deliverable (D8.7)**. If that understanding is right, building Booster activities into the
work plan as a funded task is an error that a reviewer will notice, and it should be removed from
the WP structure and mentioned only as an intention.

---

## 9. What to drop

Cutting is as valuable as writing here, because the budget is over-subscribed and the deliverable
list is bloated.

| Drop | Why |
|---|---|
| **T3.4 Predictive monitoring framework (machine learning)** | Reads as research creep in a demonstration project. It does not serve the TRL 5→6 step, it is the least defensible line if a reviewer asks "why is this funded?", and it frees budget. If EDP wants to keep it, shrink it to a small analytics component inside model validation |
| **Circular concrete materials development as an activity** | Already achieved in SUREWAVE. Keep it in the "milestones already achieved" list where it is credibility, not in the work plan where it is cost |
| **"Circular and square configurations will be evaluated"** as an open design question | Decide it now and state the decision. Open design questions at proposal stage read as immaturity in a Transition call |
| **D8.5 and D8.6, "Technical Review Meeting Reports"** | Meetings are not deliverables. Inflates the count for no gain |
| **D1.1 "Project Website" as a standalone deliverable** | Fold into the dissemination plan |
| **Deliverable count generally: 24 → ~14** | 24 deliverables for a 36-month, €2.5M project signals administrative load rather than focus. Each one is a reporting obligation under lump-sum funding |
| **Every use of "offshore" and "sea trials" for the demonstration** | See §2 |
| **The 50–300 kWp range** | Commit to one number |

---

## 10. What to focus more on

In descending order of expected score gain per hour spent:

1. **Impact, sections 2.1–2.3.** Currently blank, worth a third of the score.
2. **The environment/TRL argument in §2.** Removes the highest-probability rejection reason.
3. **Investment readiness specifically.** This is EIC Transition's distinguishing criterion versus a
   normal Horizon collaborative project. Named investors, a raise plan, an IP position, LOIs.
4. **Evidence over assertion.** Every strong claim in this proposal has a real artefact behind it —
   MARIN test reports, D6.1 model chain, the Hainer See LOI, Gen 1 field deployments, the Norwegian
   customer pipeline, DNV standards alignment. Cite them. The draft asserts where it could
   evidence.
5. **The end-user story.** EDP is the proposal's biggest asset for the Impact criterion. Their
   letter of support, their site, their board approval and their named role should be far more
   visible than they currently are.
6. **Internal consistency.** Cheap points. A reviewer who finds three contradictions starts hunting
   for a fourth.

---

## 11. How EIC evaluates this, and what to bake in

Points to write *for*, beyond the obvious.

- **Three criteria, remote evaluation, then an interview.** Above-threshold proposals go to a jury
  interview. Write the document so it survives four independent expert readings, *and* so it hands
  the interview team a story that fits on one slide: *"We remove waves instead of resisting them.
  It is proven in the basin. We are building it at Hainer See. EDP will buy it."*
- **Technology and business maturation must advance in parallel.** This is the defining feature of
  EIC Transition. A proposal that reads as an engineering demonstration with a business annex scores
  badly. The current draft reads exactly that way. Fixing Impact fixes this.
- **Lump-sum funding changes how scope is judged.** Payment is tied to completed work packages, so
  vague scope is penalised harder here than in an actual-cost call. Every "50–300 kWp", every
  "approximately seven candidate sites", every "to be determined" is a scope risk in the evaluator's
  eyes.
- **The link to the previous project must be airtight.** The proposal builds on SUREWAVE
  (101083342). SINTEF, Sunlit Sea and CLEMENT were in SUREWAVE; **EDP was not**. Check whether the
  IP commitment letter annex is required, and make the ownership and access position explicit.
  **[VERIFY — this is an admissibility issue, not a scoring one.]**
- **Consistency between narrative, tables and budget is actively checked.** See §4.
- **Speed to market counts.** A shorter project reads better. Another argument for 36 months.
- **European strategic value.** EIC responds to proposals that build a European asset. The fully
  European value chain here is a real argument and it is currently unused.
- **The reviewer's implicit question throughout is "why now, and why you?"** The answer is strong:
  the standards landscape just moved (DNV, May 2026), the technology has been de-risked in two basin
  campaigns, the site and end user are secured, and the manufacturer already sells commercially.
  Say it plainly, early, in the Excellence section.

---

## 12. Annexes and admissibility checklist

- [ ] Cover-page confirmation boxes ticked
- [ ] "Other linked projects" table completed or properly marked as not applicable
- [ ] Lump-sum detailed budget table
- [ ] IP commitment letter, if required for EDP as a non-SUREWAVE partner **[VERIFY]**
- [ ] Hainer See site LOI (Eirik's 9 September note says this is secured — annex it)
- [ ] EDP letter of support, referencing board approval of 8 September
- [ ] Ethics self-assessment in Part A
- [ ] Clinical trials annex — not applicable, confirm it can be omitted
- [ ] Page limit checked against the call **[VERIFY]** — the current draft plus a filled Impact
      section will likely be over

---

## 13. Suggested split of work, given one week

**Eirik / Sunlit Sea — write these, they are ours and nobody else can:**

1. The environment and TRL argument (§2). Send it to Balram as finished prose, not as a comment.
2. IP and trade-secret strategy, with the FPV-side patent position.
3. Technology KPIs K1–K7 and K9 (§6), with numbers Sunlit Sea will stand behind.
4. The salt-exposure test programme as a costed sub-task.
5. Investment-readiness input: the raise plan, the investor network, the Norwegian customer
   pipeline.
6. The corrected FPV-side task text — T2.3 and T5.4 currently contain PDF-extraction damage.

**Push Balram on these:**

1. Duration: fix at 36 months and propagate it everywhere.
2. WP renumbering and the dead cross-references (§4).
3. Person-month and budget tables — and the budget gap in §8, which is a coordinator problem.
4. Site framing: Hainer See named, Portugal as a replication study in the business WP.
5. Whether the Booster Grant belongs in the work plan at all (§8).
6. Removing WavEC from D4.2 and from the T4.1 text.

**Ask EDP for:**

1. Impact 2.1–2.3 draft content — it is their criterion and their expertise.
2. The letter of support.
3. The Portuguese site description Balram already requested, scoped as replication-study input
   rather than as an alternative demonstration site.

---

## 14. Open questions I could not resolve from the material

1. **Wave height at Hainer See.** Eirik's summary says ~1.5 m; Thomas's 1 September mail says
   "around 1 m". These need reconciling to one sourced figure before either goes in writing.
2. **Demonstrator scale.** 50–300 kWp is a 6× range. What does the consortium actually intend?
3. **CLEMENT's total ask**, including personnel, licences and travel. Without it the budget cannot
   be closed.
4. **SINTEF's and EDP's asks.** Not in any document I have.
5. **Patent position.** Does Sunlit Sea hold any granted patents or pending applications relevant to
   the CONNECT architecture or the hinge?
6. **The Hainer See LOI** — is it signed, and by whom? Eirik's mail says secured; the annex needs a
   document.
7. **Project duration** — is 36 months the consortium's intention, or 42?
8. **Was EDP a SUREWAVE beneficiary?** Determines whether the IP commitment letter annex is needed.
