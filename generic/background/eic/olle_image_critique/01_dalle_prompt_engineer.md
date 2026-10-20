---
persona: DALL-E 3 / ChatGPT image generation prompt engineer
focus: parsing failure modes, negation leaks, abstract-reference failure, compound-constraint attrition
---

# DALL-E 3 Prompt Engineer Critique — Olle Slide Deck Images

## Image 1 — Projektet i korthet (isometric FPV overview)

### 1. Prediction of what ChatGPT will actually render

The model will produce a brightly lit, clean-looking top-down diagram that superficially resembles an isometric infographic. The solar panels will likely be rendered as a flat blue rectangle — a generic "solar farm" grid — not a floating structure. The breakwater ring is the weakest element: it will probably appear as a white or grey border rectangle, possibly with rounded corners, but without any realistic floating-unit geometry (no barge-shapes, no catenary chains descending into water). The water underneath will be a flat blue fill, not translucent turquoise. The overall style will drift toward a SaaS-product marketing illustration: rounded corners, slight drop shadows, possibly slight 3D extrusion — the phrase "flat shading with subtle gradients" tends to produce exactly this corporate infographic look rather than a technical diagram. Chains and anchor details will either be absent or rendered as decorative lines.

### 2. Specific failure modes

1. **"Isometric cutaway" + specific technical geometry (breakwater units, anchor chains)** — The model's weakest combination. "Catenary mooring" and "floating breakwater units" are outside reliable training distribution for isometric illustration. The model will fabricate geometry that looks plausible on a thumbnail but is physically wrong. Severity: **high**.

2. **Compound-constraint attrition** — The prompt contains at least 15 discrete specifications (shape, size in metres, color of panels, color of water, cloud count, shadow rule, people count, vessel count, lighting direction, style label, shading type, palette description, aspect ratio, text rule, brand reference). Early concepts (solar panels, water, sky) will dominate; late constraints (breakwater geometry, anchor chains, no shadows) will be partially or wholly dropped. The "50 by 20 metres" dimension specification is meaningless to the model. Severity: **high**.

3. **Abstract style reference: "echoing the visual language of a Horizon Europe technical brochure"** — "Horizon Europe technical brochure" is not in the model's training as a specific visual style. The model will substitute a generic "corporate technical illustration" interpretation, which is not inherently wrong but is unpredictable and provides no real guidance. This phrase wastes token budget that could anchor useful positive style descriptors. Severity: **medium**.

4. **Negation leak: "no shadows, no people, no vessels, no military elements of any kind"** — Every negated concept is tokenised. "Military elements" is particularly risky: the model attends to the token and has a non-trivial probability of rendering something — an anchor shape that reads maritime-security, a geometric form that reads sensor array — that a viewer with military context might associate with defence. The "no military elements" phrase is the highest-stakes negation here. Severity: **high** (for the "no military elements" negation specifically; medium for the others).

5. **"Muted colour palette"** — Inconsistent model interpretation. Combined with "bright Nordic midday" and "turquoise water", the model will likely choose one of the two competing signals and ignore the other. The result will be either too saturated (bright midday wins) or too flat (muted wins). Severity: **medium**.

6. **Size specification in metres ("roughly 50 by 20 metres")** — The model has no understanding of real-world scale from metric dimensions. This description is wasted text that could crowd out a more useful constraint. Severity: **low** (wasted rather than harmful).

### 3. Concrete redraft

```
A clean isometric illustration of a floating solar panel array on calm sea water, viewed from a high angle. The array is a rectangular grid of deep-blue photovoltaic panels lying flat on the water surface. A ring of pale grey, barge-shaped floating units encircles the panel grid, with thin chains visible descending from them into the clear water. The sky above is pale blue with a few small white clouds. Lighting is soft and even, no cast shadows. Visual style: flat-colour technical illustration, minimal detail, white background borders, soft blue-grey-cream colour palette. Aspect ratio 16:9.
```

Key changes: removed all negations, dropped the metric dimensions, dropped the brand-style reference, shortened the compound list from ~15 to ~8 constraints, replaced "echoing Horizon Europe" with concrete palette words, converted "no military elements" to silence (not mentioned at all).

---

## Image 2 — Platsen på Gotland (aerial coastline)

### 1. Prediction of what ChatGPT will actually render

The model will produce a photorealistic aerial shot that looks convincing at a glance. The limestone coast detail is likely to work reasonably well — pale cliffs, pine vegetation, blue-grey sea — as this is a well-represented landscape type. The "industrial area set back from the water" with "conveyor belts and a small cargo pier" is the risk zone: the model will probably render this as a generic industrial port scene that may look more like a container terminal or a bulk chemical plant than a limestone handling terminal. The bulk cargo vessel will likely be rendered correctly in proportion and hull type. The seabirds will appear as generic white specks. The most likely compositional failure is that the model will place the industrial area in the centre rather than the middle distance, making it the dominant subject rather than the coastline.

### 2. Specific failure modes

1. **"Civilian industrial area… limestone handling terminal with conveyor belts"** — Specificity of industrial subtype is unreliable. The model will render a generic port industrial scene. "Conveyor belts" specifically may produce a mining/quarry aesthetic that looks more like a gravel pit than a coastal limestone terminal. The visual could read as a heavy industrial extraction site, which is not inherently a problem but is different from what was intended. Severity: **medium**.

2. **Negation: "no military presence of any kind, no vehicles beyond the single industrial cargo vessel"** — "Military presence" is tokenised. Given that the site is Gotland (a significant Swedish defence location by training data), the model may have a non-trivial prior toward rendering military infrastructure in a Gotland coastal scene. The negation prompt will likely fail to suppress this prior reliably. The phrase "no vehicles beyond" also inadvertently cues "vehicles" as a token concept. Severity: **high** (Gotland military prior is the specific risk).

3. **Compositional specification: "in the middle distance"** — The model will place the industrial cluster where composition looks balanced, not where the prompt specifies. "Middle distance" as a spatial directive is approximated. The industrial area will likely dominate the frame more than intended. Severity: **medium**.

4. **"Cinematic drone photography, naturalistic colours"** — These are somewhat contradictory: "cinematic" typically generates colour grading (lifted blacks, slightly desaturated), while "naturalistic" pushes toward unprocessed documentary. The model will pick one interpretation; likely "cinematic" wins, producing a slightly stylised look. Severity: **low** (aesthetics preference, not a content risk).

5. **"A few seabirds in flight"** — Seabirds in flight are a known compositional wildcard. The model tends to place them centrally or to make them distractingly large relative to an aerial frame. They add noise to the composition without advancing the slide's argument. Severity: **low** (drop if the element doesn't earn its place).

6. **No mention of what the image is for** — The prompt does not anchor "this is an aerial overview establishing the project site." Without a compositional anchor like "the coastline is the primary subject, the sea fills the upper half of the frame", the model's default composition will be arbitrary. Severity: **medium**.

### 3. Concrete redraft

```
A high oblique aerial photograph of a pale limestone coastline on a clear summer day. The coastline — low white-grey cliffs edged with pine and juniper scrub — runs across the lower third of the frame. Calm blue-grey sea fills the upper two-thirds, fading to a hazy horizon. Set back from the water, a small industrial area: low pale concrete buildings, a short cargo pier with a single bulk-cargo vessel moored alongside. The water near shore is shallow and translucent over a pale limestone seabed. Photorealistic drone photography style, natural daylight, blue and stone-grey palette. Aspect ratio 16:9.
```

Key changes: removed all negations (Gotland not named — removes military location prior), dropped "seabirds" (noise), dropped "conveyor belts" (fabrication risk), dropped "cinematic" (contradiction), added explicit compositional anchor (coastline lower third, sea upper two-thirds), shortened compound list.

---

## Image 3 — Hur tekniken fungerar (ground-level sea view with FPV)

### 1. Prediction of what ChatGPT will actually render

This prompt will likely produce the most visually satisfying image of the four — ground-level sea photography with warm late-afternoon light is well within training distribution. The FPV installation in the middle distance will probably appear as a flat dark rectangle on the water, which is acceptable. The reflection quality is unpredictable: a glassy mirror reflection of a solar panel array is a compositionally complex element; the model may produce it passably or may produce a confused double-image. The breakwater units (described as "rounded, barge-shaped") will likely be reduced to a white perimeter blob — correct in colour, incorrect in shape. The warm golden horizontal light will compete with the "pale strip of coastline on the far horizon" for visual priority; one or the other will be suppressed.

### 2. Specific failure modes

1. **"Glassy and reflective, mirroring the panels and the Nordic late-afternoon sky"** — Water reflections are a known failure point. The model will attempt the reflection but often produces physically inconsistent results: panels reflected at the wrong angle, sky reflections appearing in foreground water while the panels are reflected in midground. A "glassy mirror" sea is achievable but unreliable with complex reflected objects. Severity: **medium**.

2. **"Natural, understated photographic style — documentary rather than promotional"** — These are reading-intent descriptors. The model does not interpret "documentary rather than promotional" as a style directive; it renders objects. "Natural" and "understated" have inconsistent model interpretation. The result will be a generic well-lit sea photograph — which may be fine, but the descriptor is giving the impression of more control than it provides. Severity: **low** (ineffective rather than harmful).

3. **"Muted colour palette"** contradicting "warm golden horizontal light** — Same conflict as Image 1. Warm golden light is visually saturated; muted palette is desaturated. The model will pick one. With "warm golden" appearing later in the sentence, it will likely win, producing a sunset-toned image rather than a muted one. Whether this is a problem depends on the slide's visual tone. Severity: **medium** (decide which is wanted and drop the other).

4. **Negation: "no military elements"** — Same tokenisation risk as Images 1 and 2. The floating installation on Baltic water with a pale coastline does not inherently cue military content, so this risk is lower here than in Images 1–2. But the phrase still wastes token attention. Severity: **low** here specifically.

5. **"About forty rectangular PV panels"** — The count will be ignored or approximated. "About forty" is not reliably renderable; the model will produce a panel array that looks plausible in density without respecting the count. This is harmless unless the count carries meaning in the slide. Severity: **low**.

6. **"Pale concrete floating breakwater units — rounded, barge-shaped"** — As in Image 1, this specific geometry is outside reliable training distribution for realistic photography. The model will produce white/grey floating objects that may or may not read as breakwater units. Severity: **medium**.

### 3. Concrete redraft

```
A ground-level photograph across a flat, calm sea on a late summer afternoon. In the middle distance, a dark-blue rectangular array of solar panels lies flat on the water surface, surrounded by pale grey floating units forming a loose perimeter. The water surface is smooth, reflecting the warm low sun and pale sky. The coastline is a thin pale line at the horizon. Warm amber afternoon light, long low sun angle, soft shadows on the water. Photorealistic, wide-angle lens perspective, natural colour temperature. Aspect ratio 16:9.
```

Key changes: removed all negations, dropped the "forty panels" count, dropped the "documentary vs promotional" intent-reading instruction, resolved the colour-palette conflict by picking warm amber explicitly, simplified breakwater description to "pale grey floating units", dropped "mirroring" (unreliable) in favour of "smooth, reflecting."

---

## Image 4 — Olles roll (civilian coordinator on jetty)

### 1. Prediction of what ChatGPT will actually render

The model will render a middle-aged man on a jetty or pier, facing away or at three-quarter angle, looking at water. This is a common stock-photography composition and well within training distribution. The civilian clothing (softshell jacket, grey trousers, walking boots) will be rendered correctly; this is unambiguous. The most likely compositional failure is the dual-prop: the model will render the man holding either the notebook or the phone but rarely both convincingly — the two-item specification frequently produces one item held awkwardly and the other tucked under an arm or barely visible. The FPV installation in the "middle distance" will probably be rendered as a barely-visible dark element on the water — either too small (correct but unrecognisable) or too prominent (compositionally wrong). The "few coastal pines in the lower-left corner" compositional placement is very likely to be ignored.

### 2. Specific failure modes

1. **Dual hand-prop: "holding a notebook and a mobile phone"** — A well-documented failure mode. The model distributes objects between hands in ways that look staged. The result is typically a man with one item in each hand looking like he is about to perform a product demonstration rather than doing routine site liaison. Severity: **high**. Pick one prop only.

2. **"Three-quarter view from behind the man's left shoulder"** — Camera angle specification is frequently approximated. "Behind the left shoulder" is a subtle positional distinction that the model will interpret as a generic back-view or generic side-view. The specific "left" shoulder distinction is unlikely to be respected. Severity: **medium** (the general intent — man from behind, looking at water — will survive; the specific shoulder is lost).

3. **"Barely visible as a thin dark line on the sea surface"** — This is a compositional subtlety the model cannot reliably execute. The tendency will be to make the FPV installation more prominent (it's a named element) or to omit it entirely. A slightly-too-prominent FPV installation in this image is not a critical failure, but the expectation of "barely visible" should be abandoned. Severity: **low** (acceptable outcome if installation is more visible than intended).

4. **"A touch of warm pine green in the lower-left corner where a few coastal pines appear"** — Specific corner placement of a secondary element is reliably ignored. The pines may appear elsewhere in the frame, or not at all. Severity: **low**.

5. **Negation sequence: "No uniform, no high-visibility vest, no safety helmet, no military element whatsoever"** — Four negations in rapid succession. Each negated concept is tokenised. "Uniform" in particular is risky — the model may produce clothing that reads ambiguously (dark softshell jacket with collar detail that resembles a duty jacket). The phrase "no military element whatsoever" contains the same high-stakes negation risk as Images 1–3. Severity: **high** for "no uniform/no military"; medium for vest/helmet.

6. **"The image should read as 'local project coordinator doing routine site liaison' and nothing more"** — Classic reading-intent descriptor. The model does not read intent. This phrase is zero-signal. Severity: **low** (ineffective but harmless).

7. **Compositional specificity: "in the lower-left corner"** — Positional corner placement is unreliable. Already noted above. Severity: **low**.

### 3. Concrete redraft

```
A documentary photograph of a middle-aged man standing on a low stone jetty on a Baltic coastline, a bright overcast day. He faces away from the camera toward the sea, wearing a dark softshell jacket, grey hiking trousers and sturdy walking boots, holding a small notebook in one hand. Behind him and slightly to one side, the camera shows calm blue-grey water. In the distance, a small flat array of dark solar panels sits on the water with pale grey floating units around it. A few pine trees stand at the edge of the jetty. Soft diffuse natural daylight, blue-grey and dark green palette. Wide photorealistic shot, the man occupies the left half of the frame, water and installation fill the right half. Aspect ratio 16:9.
```

Key changes: dropped one prop (notebook only, phone removed), removed all negations (uniform/military/vest/helmet not mentioned), replaced reading-intent phrase with a concrete compositional split (man left, water right), dropped specific shoulder/corner placement, replaced "barely visible" with a size-neutral description of the installation, described clothing by positive attributes only.

---

## Meta-advice

### Negation is the single largest cross-cutting risk

All four prompts use "no military elements" (or close variants). Across a four-image deck, this phrase appears roughly four times, each time tokenising the concept it aims to exclude. The safer approach for this specific deck: never mention military in any prompt. The risk is not that the model will render a soldier; it is that some visual element — an anchor shape that reads naval, a structure that reads surveillance post, a vessel with a hull profile associated with coast guard — will land in the image and trigger a worried read by a Forsvarsmakten line manager who is already sensitised to dual-use framing. Silence is safer than negation.

### Specific geometry outside training distribution needs simplification, not more precision

Images 1, 2 and 3 all attempt to specify FPV installation geometry (breakwater units, catenary mooring, barge shapes) in detail. More detail does not produce more accuracy for out-of-distribution industrial content — it produces more fabrication. The right approach is to describe the visual effect you need, not the engineering reality: "a flat dark grid of panels surrounded by pale grey floating objects" produces a workable image; "rounded barge-shaped floating breakwater units with catenary anchor chains" produces a guess. Reserve detailed specification for elements that are well-represented in training data (human figures, coastlines, standard vehicle types, sky conditions).

### Resolve colour-tone conflicts before submitting

Images 1 and 3 both carry conflicting tone descriptors: "bright Nordic midday" + "muted palette" in Image 1; "warm golden horizontal light" + "muted colour palette" in Image 3. The model will resolve these conflicts by picking one signal, and it will not tell you which. Decide on a single visual tone per image (cool/muted or warm/golden) and express it consistently in one or two concrete terms. Drop the word "muted" entirely — it is a photographic/aesthetic judgment that the model interprets inconsistently and which contradicts any specific lighting description.

### Abstract style anchors waste token budget

"Echoing the visual language of a Horizon Europe technical brochure" (Image 1) and "cinematic drone photography" (Image 2) are the main offenders. Neither anchor describes something the model can retrieve. Replace abstract style references with three to four concrete visual properties: illustration type, colour palette, lighting condition, level of detail. For a set of four slides that should feel visually coherent, pick a shared style phrase that means something concrete — for example: "flat-colour technical illustration with a blue-grey-cream palette" for the diagram images, "photorealistic natural daylight, blue-grey palette, no post-processing" for the photography images — and repeat it verbatim across relevant prompts.

### Suggested approach to the deck as a set

Given the political sensitivity of the use case (a leave-request pitch to Forsvarsmakten management, where anything that reads as dual-use or security-relevant risks the leave being refused), the deck should use a conservative image strategy:

- Images 1 (isometric diagram) and 3 (sea-level FPV view) are the most controllable because they contain no human figures and no location-specific cues. Generate these first, accept the first generation that does not contain anything obviously wrong, and do not over-iterate.
- Image 2 (Gotland coastline) carries the highest location prior risk — the model has Gotland associated with defence in training data. Consider whether the image needs to be Gotland-specific at all, or whether a generic Baltic limestone coastline (without naming Gotland) delivers the same slide value at lower risk. If Gotland specificity matters, test multiple generations and evaluate each for inadvertent military cues before selecting.
- Image 4 (Olle figure) carries the highest human-rendering risk (clothing ambiguity, dual prop). Generate this last, after the visual tone of the other three is established, and match the lighting and palette to the established set. Commission only one prop. Review the clothing rendering carefully before accepting — a dark collar-detail jacket can read as a duty jacket in certain rendering styles.
