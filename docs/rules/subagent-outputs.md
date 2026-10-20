# Treat agent/subagent outputs as hypotheses, not sources

Rule: when a subagent (spawned via the `Agent` tool, including multi-persona critique passes) asserts a design fact, a specification, a quantitative claim, or a technical constraint, treat the assertion as a hypothesis. Verify against a primary source (project spec in `gen2/` or `sure/` background, SUREWAVE deliverables, Grant Agreement, Lovdata text, vendor datasheet) before propagating the assertion into any deliverable, doc, image prompt, or follow-on task.

Subagent output is a draft, not a source — regardless of the persona assigned to the subagent (lawyer, engineer, specialist, "with 30 years of experience in X"). The persona is a prompt device, not a credential; the subagent still has no privileged access to project reality.

## Why

Precedent (2026-10-19, T132 → T135):

In T132 one of five subagents (`generic/background/eic/olle_image_critique/03_fpv_industrial_visualization.md`) was prompted as an "industrial visualisation specialist (FPV, marine infrastructure, offshore energy)" and reviewed image prompts for the Olle Försvarsmakten presentation. The subagent asserted, as fact:

- *"~0.4–0.5 m above sea-level silhouette is the defining visual characteristic of the technology"* (line 19)
- *"zero tilt angle, no walkways between panels, no pontoon floats visible"* (line 40)
- *"the camera is at ~0.5 m above sea level looking across the water at panels that are themselves ~0.4–0.5 m above sea level"* (line 87)

The subagent cited no source. Both claims were false:

- The authoritative Gen 2 spec (`gen2/norsmaterials_brief.md` line 44) states: *"Distance PV → water: 6 cm at the lowest edge — the panel sits at a 2° tilt, so the opposite edge sits higher"*.
- The FDS (`sure/background/2024-08-27_fds_nextgen_product.md` line 212) confirms the drainage-angle intent.
- Real spec: ~6 cm freeboard (not 400–500 mm — an order-of-magnitude error) and 2° tilt (not zero).

The false claim then propagated into `docs/sure_images.md`, `docs/rules/image-guidance.md`, the Olle deck image prompts (slide 2 and slide 4), the SUREWAVE D8.3 figures spec, and TASKS.md historical notes — all before the user caught it during review of a ChatGPT-generated image that was then evaluated against the wrong geometry benchmark. Cleanup required T135 (this task).

The failure mode is systemic: a persona-primed subagent produces plausible-sounding assertions, those assertions enter the main context stream, and from there flow unchecked into deliverables.

## How to apply

Before incorporating a subagent assertion into any deliverable, doc, or follow-on action:

1. Identify every quantitative or specification claim the subagent made (dimensions, elevations, materials, tilt, temperatures, timelines, stakeholder positions, legal interpretations, standards citations).
2. For each claim, locate the primary source in the repo (project background folders, SUREWAVE deliverables, downloaded Lovdata files, Grant Agreement, vendor datasheets). If a primary source is not in the repo, flag the claim as unverified; do not propagate it.
3. If the subagent's claim contradicts the primary source, the primary source wins. Correct the subagent's output (via a correction header on the subagent file) and update any propagations.
4. In the subagent's output file, mark any assertion the subagent made without a source citation as unverified. When reusing the subagent's output in later work, re-check unverified assertions against primary sources at that point.

## Interaction with existing rules

- Extends CLAUDE.md **"Re-read source material immediately before drafting a deliverable"** — primary sources are the backstop regardless of what intermediate agents may have asserted.
- Reinforces CLAUDE.md **"Image guidance in deliverables uses existing project assets, not invented ChatGPT prompts"** — the agent spec itself can propagate invented facts if not checked.
- The `check-deliverable` skill's step 5 (Source freshness) now covers this when the subagent assertion ended up in the deliverable.

## Checklist for subagent-heavy workflows

Workflows that spawn multiple persona subagents (image-prompt critique, legal review, technical review passes) are highest risk:

- Before merging subagent outputs into a working document, extract their quantitative claims and verify each against primary sources.
- Mark the subagent output file as "critique / draft input" at the top so later readers do not treat it as authoritative.
- When the Opus orchestrator synthesises subagent outputs, carry forward only claims that the orchestrator has verified against primary sources — not every claim the subagents made.
