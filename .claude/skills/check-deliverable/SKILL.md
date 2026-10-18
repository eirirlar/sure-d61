---
name: check-deliverable
description: Run a pre-send checklist on an outgoing deliverable (external letter, auditor pack, grant application text, board paper, report, slide deck) before conversion to docx/PDF or before the user sends it. Trigger when the user says "check the deliverable", "run the deliverable checklist", "ready to send?", "verify before conversion", or when wrapping up a draft that will leave the repo. Catches the common failures: internal references leaking out, bold-in-body, emphasis-by-assertion, YAML metadata rendering as a title block, stale background facts.
---

# check-deliverable

## When to use

- User says: "check this before I send it", "run the deliverable checklist", "ready for conversion?", "verify the output".
- Just before converting a `.md` to `.docx` or `.pdf` for an external reader.
- Pre-flight for any file in `funding/deliverables/`, `surewave/deliverables/`, `sure/deliverables/`, or `generic/deliverable/`.

**Do not use** for internal working notes, draft task descriptions, or files under `background/`. Those are allowed to be internal in tone.

## Procedure

Run through each check and surface findings to the user as a bulleted report before converting. Do not fix issues unilaterally — the user chooses what to accept.

### 1. Stand-alone check

The reader does not have the rest of the repo.

- No repo file paths (`funding/background/…`, `generic/background/…`).
- No `[background](…)` or `[deliverables/…](…)` Markdown links to internal files.
- No task numbers (`T81`, `T106.04`).
- No internal framing: "draft", "rewrite", "offered to X", "working version", "revisorpakke v2".
- No references to companion documents by role: "as described in the løypemelding", "see the earlier mail", "jf. T100-pakken" — unless the companion document is included in the same send.
- Cross-references within the same document are fine: `jf. pkt. 6.3`, `se tabell 2`.
- Laws and standards cited by canonical form only: `regnskapsloven § 5-3 tredje ledd`, `NRS(F) Nedskrivning av anleggsmidler pkt. 3`.

### 2. YAML metadata

- `title`, `author`, `date` in YAML render as a visible title block in docx/PDF output. If any of these are for us rather than the recipient (internal file naming, draft date), rename to `internal_title` etc.

### 3. Typography and emphasis

- No `**bold**` in body text. Bold is reserved for titles and subtitles at the top of a document or section. Paragraph bold, list-item bold and table-cell bold all violate.
- No emphasis-by-assertion phrasing. Flag: *which is precisely*, *this is exactly*, *it is worth noting*, *crucially*, *importantly*, *the very X*, *not merely X but Y*, *no amount of X would*. If any phrase like this appears, propose a replacement.
- No negation-first framing where the positive would land better. Flag: "This is not X — it is Y" — rewrite to lead with Y.
- Italics for defined terms are allowed.

### 4. Markdown rendering integrity

- Enumerations use `-` or `1.`.
- Stacked signature/address blocks have two trailing spaces at end of each line (or `\`) — otherwise lines fold into one paragraph.
- Separate paragraphs have blank lines between them.

### 5. Source freshness

- If the deliverable draws on a `background/` file: re-read that background file *now*, before signing off. Facts may have been added since task start. See `docs/rules/reread-source.md` (T80 precedent).
- If a canonical reference (law text, NRS, grant call text) is cited, confirm the citation matches the current version in `generic/background/lover/` or similar.

### 6. Norwegian-language deliverables

If the deliverable is in Norwegian, verify finance/clean-tech vocabulary is Norwegian not English (see CLAUDE.md "Norwegian-language deliverables" table): `fornybar-teknologi` not `cleantech`, `egenkapital` not `equity`, etc. Currency and units follow the number: `15 mrd USD`, `10 mill. NOK`, `0.060 EUR`.

### 7. Converted-output check (if applicable)

If a `.docx` or `.pdf` already exists:

- Open it. Do not skip to "the markdown looks fine".
- Verify YAML metadata rendering is intentional (title block visible / absent as planned).
- Check table rendering (borders, column widths — see `scripts/format_docx.py` for pandoc docx table fixing).
- Check that numbers do not break across lines in narrow PDF columns (use `scripts/nbsp_numbers.py` if they do).

## Applicable rules

All of CLAUDE.md "Language and tone", plus:

- CLAUDE.md "**External deliverables stand alone**"
- CLAUDE.md "**No bold in body text**"
- CLAUDE.md "**Avoid emphasis-by-assertion phrasing**"
- CLAUDE.md "**Lead with the positive claim, not the negation**"
- CLAUDE.md "**Markdown lists render correctly**"
- CLAUDE.md "**Re-read source material immediately before drafting**" + `docs/rules/reread-source.md`
- CLAUDE.md "**Converted `.md` files must be self-contained**" (for the self-containedness check from the other direction)
- CLAUDE.md "**Do not convert to docx automatically**"
- CLAUDE.md "**Norwegian-language deliverables**" vocabulary table

## Historical references

- T80 — delivered with 2 of 4 reasons because background had been filled after task start and was not re-read before drafting. Precedent for the re-read step.
- T73 — investor-update truncation incident; precedent for inspecting rendered output, not just the markdown.
- T85 — avrunding av beløp i revisorpakken til hele tusen; shows how post-draft number formatting is a legitimate round of edits.
- T84 — PDF-layoutfiks (NBSP in numbers + table font size); the kind of rendering problem the converted-output check catches.
- T125 — explicit statement in the solution note that the deliverable is YAML-clean (`title`, `date`, `author` only, all intended for rendering).

## Known pitfalls

- **Checking only the markdown.** The rendering can surprise. Open the docx/PDF.
- **Trusting the YAML.** `title: Draft of letter to auditor` ships as a visible title block to the auditor if left in place.
- **Letting bold-in-body slip through.** `**mandatory**` or `**NB**` in prose is the common form. Rewrite the sentence, break to its own line, or promote to a subheading.
- **Keeping internal file paths.** `(see funding/background/…)` is the easy one to miss — it is often added during drafting as a working reference.
- **Not re-reading the background.** The T80 pattern repeats whenever the user has filled in background between task start and drafting.
- **Fixing without surfacing.** This skill reports findings; the user decides whether to accept each one. Do not silently rewrite.
