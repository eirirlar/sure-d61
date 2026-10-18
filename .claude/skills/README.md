# Claude Code skills — sunlit-sea working repo

Skills defined here register at session start. Each lives at `.claude/skills/<name>/SKILL.md` and is triggered by Claude Code when the user's language matches the skill's description or when the user types `/<name>` explicitly.

## Defined skills

| Skill | Purpose | When to use |
|---|---|---|
| [`process-inbox`](process-inbox/SKILL.md) | Convert files in `*/background/new/` to date-prefixed `.md` and move them to the right `background/` folder | User asks to process the inbox; session start finds unprocessed files |
| [`create-task`](create-task/SKILL.md) | Create a new T-numbered task in `TASKS.md` with correct numbering, tag and insert position | User asks to create / add / track a task |
| [`generate-letter`](generate-letter/SKILL.md) | Produce `.docx` or `.pdf` of a Sunlit Sea official letter via `scripts/md_to_letter.py` | User explicitly asks for a letter output |
| [`generate-slides`](generate-slides/SKILL.md) | Produce a `.pdf` slide deck in Sunlit Sea's visual profile via `scripts/md_to_slides.py` | Board decks, GF, pitch decks, grant presentations, WP8 outputs with Sunlit strap |
| [`generate-surewave-docx`](generate-surewave-docx/SKILL.md) | Produce a SUREWAVE-branded `.docx` from `.md` via pandoc `--reference-doc` on the consortium template | SUREWAVE D-reports, WP8 outputs, consortium brochure sections |
| [`generate-surewave-pptx`](generate-surewave-pptx/SKILL.md) | Produce a SUREWAVE-branded `.pptx` from `.md` via pandoc `--reference-doc` on the consortium template | SUREWAVE WP8 presentations, final-event talks, interview decks |
| [`check-deliverable`](check-deliverable/SKILL.md) | Pre-send checklist on an outgoing deliverable (stand-alone, typography, YAML, source freshness) | Before converting or sending any external deliverable |
| [`extract-pdf-with-images`](extract-pdf-with-images/SKILL.md) | Batch PDF → Markdown with embedded images inlined per page (the T100 combined recipe) | PDF set with figures that must survive into the `.md` |

## Candidates considered, not yet defined

Captured here so future sessions don't re-survey.

- **generate-report-with-mermaid** — the standard `pandoc + mermaid-filter` pipeline for SuRE deliverables (D6.1 / D6.2). Low frequency (two deliverables), high encoding overhead; procedure is already fully documented in [`../../docs/pandoc_conversion.md`](../../docs/pandoc_conversion.md).
- **archive-task** — move a T# from `TASKS.md` to `ARCHIVE.md`. Low frequency, trigger is explicit user request only, procedure is one working-rule bullet in CLAUDE.md.
- **clean-investor-updates** — the T73 `scripts/clean_investor_updates.py` workflow. One-off cleanup series completed in 2026-07; not expected to recur frequently enough to warrant a skill.
- **revisorpakke-update** — the prinsippendring / aktivering / nedskrivingstest iteration pattern seen in T81–T86. Tied to a specific case rather than a general work pattern; the [`cases/prinsippendring_arsregnskap_2025/INDEX.md`](../../cases/prinsippendring_arsregnskap_2025/INDEX.md) index covers that case directly.
- **surewave-deliverable-review** — WP8 / consortium deliverable review passes (T116, T117, T121). Tied to the SUREWAVE project's run-out; low expected recurrence.

Promote candidates to skills when:

1. The pattern recurs across at least two separate tasks that are not part of the same immediate thread.
2. The procedure can be stated as discrete steps without case-specific judgement.
3. There is error-history or clear safety value in codifying.

## How these integrate with the repo

Skills reference the authoritative repo documents rather than duplicating them:

- `CLAUDE.md` — working rules, overall conventions.
- `docs/rules/` — rule elaboration, precedents.
- `docs/pandoc_conversion.md`, `docs/scripts.md`, `docs/background_convention.md` — script and tool reference.
- `cases/<case>/INDEX.md` — case-specific pointers for cross-cutting threads.

When a working rule changes in CLAUDE.md, check the corresponding skill(s) for stale references. When a template (`generic/background/2026-10-10_sunlit_sea_letterhead.docx`, `surewave/background/2026-10-16_surewave_docx_template.docx`, `surewave/background/2026-10-16_surewave_pptx_template.pptx`) is replaced with a newer version, update the referenced path in the corresponding skill.
