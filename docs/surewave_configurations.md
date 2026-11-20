# SUREWAVE configurations: open-sea reference plant vs nearshore directional

This note exists so deliverables, image prompts and investor material do not conflate the SUREWAVE reference plant with the configurations Sunlit Sea actually brings to market in nearshore settings. The two look different and have different economics.

## Open-sea reference plant

Documented in `surewave/deliverables/2026-09-28_surewave_d8.3_technical_brochure.md`. 7 MWp installed on a 346 m diameter circular footprint; sixty-eight 14 × 14 FPV matrices (D3.4) packed inside a full ring of 56 floating breakwater units, with two crossing lines of bridge pontoons (17 + 18 units, D3.3) dividing the array into four sub-farms. Slack-catenary mooring with long chains, running from the ring to anchors both outside and inside the footprint. Validated across three European sea-basin classes (Baltic mild, Mediterranean mid, North Sea harsh). D3.3's layout study assumed a 10 MWp basis with about 18,600 panels of 537 Wp; the 7 MWp / 68-matrix figure is the later D3.4 system design and is what the brochure states.

Breakwater unit geometry (Clement Germany, confirmed in Thomas Pehlke's 2026-11-18 brochure review): rectangular cross-section that does not narrow towards the bottom, side walls continuing down as two keels, transverse interior walls, deep draft (2.03 m) and low freeboard (0.47 m).

The full-ring breakwater is the design-basis configuration for open-sea deployment: wave exposure is omnidirectional, so the breakwater perimeter is omnidirectional. Reference images:

- `surewave/images/2026-11-18_clement_d8.3_figure_inputs/` — Clement Germany CAD graphics (plant layout, mooring plan, moored ring, unit renders, sections). Authoritative geometry; used in the D8.3 brochure from 2026-11-18.
- `surewave/images/2026-09-28_surewave_d8.3_technical_brochure_lowres/fig01.png` — AI-generated concept render of the full installation (cover image).
- `surewave/images/.../fig03.png` — AI-generated vector illustration with labelled subsystems. Breakwater geometry is schematic (narrowing keel, high freeboard, short steep chain). Kept in the brochure at Clement's request, captioned as not to scale; do not use it for geometry.
- `surewave/images/.../fig04.png` — AI plan view, 346 m diameter. Superseded by the Clement layout 2026-11-18.

A 420 kWp pilot-scale variant is noted in D8.4 Section 2 as a mild-sea pilot stepping stone, but uses the same perimeter architecture.

## Nearshore configuration (Sunlit Sea's commercial direction)

Open-sea's omnidirectional wave exposure does not apply nearshore. One or two dominant wave directions dominate, set by the local wave rose, bathymetry and shoreline geometry. For nearshore sites the SUREWAVE breakwater is placed to intercept those critical wave directions rather than forming a full ring. The full ring is too expensive for nearshore economics and buys protection on the sheltered sides that is not needed.

The strategy is implemented in Sunlit Sea's own planning platform, built on the SUREWAVE nearshore wave-and-wind modelling framework (see `surewave/background/2026-09-30_sunlit_sea_exploitation_summary.md`, Exploitable Result 1). The platform evaluates wave and wind conditions along the full perimeter of a candidate installation and recommends placement for protective structural elements accordingly.

Example cases this applies to:

- **Gotland North demonstrator** — northern Gotland, Baltic coastline near Storugns. EUPI-PV Partnership proposal, submission 2026-12-01. The Baltic coastline sits inside a limited wave fetch and the critical direction depends on the specific shoreline — directional breakwater, not a ring.
- **Hainer See demonstrator** — inland mining lake in Saxony. Same EUPI-PV proposal. Inland lake fetch; directional breakwater against the dominant wind-wave direction. The consortium's current working position is that Hainer See's wind-wave conditions equal or exceed some nearshore sea conditions; whether the argument carries with evaluators is open.

## Implications for deliverables

- The ring layout visualised in D8.3 figures (`fig01`, `fig03`, `fig04`) is accurate for the open-sea reference plant and misleading for anything site-specific when the site is nearshore. Do not use ring imagery to represent a nearshore demonstrator.
- Site-specific imagery for Gotland or Hainer See should either show real Sunlit Sea deployment photographs of the panels (which do not include the SUREWAVE breakwater, so no configuration claim is made) or ask the user for a CAD snapshot of a directional-breakwater configuration — the Gen 2 FreeCAD model is live.
- In prose: *"an external floating breakwater placed to intercept the critical wave directions"* is correct for nearshore. *"A full circular ring of concrete breakwaters"* is only correct for the open-sea reference plant.

## See also

- [`docs/sure_images.md`](sure_images.md) — image asset catalogue with provenance tags.
- [`docs/rules/image-guidance.md`](rules/image-guidance.md) — rule for writing image guidance in deliverables.
