# Sunlit Sea – working repo (project context)

## What this is

Working repository for Sunlit Sea's ongoing activities. Content is organised by **activity**, not by artefact type. Each activity has its own top-level folder with its own README describing scope and contents. Tasks across all activities share a single `T`-numbered sequence in the top-level `TASKS.md`.

Repo owner: Eirik Larsen (Sunlit Sea).

The activity streams currently tracked:

| Folder | Activity | Notes |
|---|---|---|
| `sure/` | SuRE WP6 – FPV model chain | Anchor activity. D6.1 delivered; D6.2 in preparation. Partners: IFE (FEM/CFD), TNO (LCA), MariSol/Accura (forming trials). |
| `gen2/` | Gen 2 product development | P3 → P4 → P5 prototype evolution, mould/cast decisions, materials testing, supplier work. Overlaps with SuRE but has its own product lifecycle. |
| `funding/` | Grants, EU reporting, financial | Horizon Europe periodic reporting, CINEA reviews, grant applications, financial reporting. |
| `surewave/` | SUREWAVE Horizon Europe project | Distinct EU project from SuRE (Grant Agreement 101083342). Coordinated by SINTEF; Sunlit Sea is a beneficiary. Reference archive of consortium deliverables, Grant Agreement, Proposal, Annex 1 Part B. Tasks currently tagged `[GENERIC]` — a dedicated `[SUREWAVE]` tag may be added if enough project-specific work accumulates. |
| `generic/` | Cross-cutting / shared | Material that spans SuRE, Gen 2 and Funding (or predates the activity split): company-level correspondence, historical investor updates, legal excerpts, market intel, outgoing customer replies. Contains `background/` (inputs) and `deliverable/` (outputs). |

Commercial/market intel (previously under `commercial/`) is folded into `generic/background/` alongside other cross-cutting material — one-off market snapshots and competitor scans are date-prefixed like other background files. Commercial tasks may still carry the `[COM]` tag.

See `TASKS.md` for the open task list, `ARCHIVE.md` for closed tasks, `README.md` for conversion tooling and script usage.

## Pointers

- `docs/rules/` — long-form elaboration of individual working rules referenced below.
- `docs/pandoc_conversion.md` — Pandoc + mermaid-filter installation, DOCX/PDF commands, Letter/letterhead output.
- `docs/scripts.md` — reference for every helper script in `scripts/`.
- `docs/background_convention.md` — background inbox pipeline and conversion recipes.
- `docs/project_facts.md` — canonical lookup for current project facts (company, people, products, projects, grant IDs, sites, counterparties, legal references). Consult before drafting any deliverable that names a proper noun, place, product, grant, site or counterparty.
- `docs/sure_images.md` — authoritative image asset catalogue with provenance tags (real photo / CAD render / AI concept render / AI vector illustration / FEM output). Covers `sure/images/`, repo-root assets, and SUREWAVE deliverable imagery.
- `docs/surewave_configurations.md` — SUREWAVE open-sea reference plant (full-ring breakwater) vs nearshore directional-breakwater strategy. Which imagery and prose apply to which deliverable context.
- `cases/<case>/INDEX.md` — case indexes for cross-cutting threads that span multiple activity folders. Current: `cases/prinsippendring_arsregnskap_2025/`, `cases/eic_transition_surewave/`.
- `.claude/skills/` — recurring workflows captured as Claude Code skills (process-inbox, create-task, generate-letter, generate-slides, generate-surewave-docx, generate-surewave-pptx, check-deliverable, extract-pdf-with-images). Index at `.claude/skills/README.md`.

---

## Files and folders (top level)

```
sure-d61/
├── CLAUDE.md                  – this document (project context for AI)
├── TASKS.md                   – open task list (single T-sequence across all activities)
├── ARCHIVE.md                 – closed tasks
├── README.md                  – tools, workflows, conventions, activity contents (only README in repo)
├── docs/                      – topic-level documentation and rule elaborations (see Pointers above)
├── cases/                     – case indexes for cross-cutting threads (pointers only; no file duplication)
├── generic/                   – cross-cutting / shared material
│   ├── background/            – date-prefixed background files + new/ inbox
│   └── deliverable/           – outgoing material (customer replies, quotes, generic company-level deliverables)
├── sure/                      – SuRE WP6 activity
├── gen2/                      – Gen 2 product development
├── funding/                   – Grants, EU reporting, financial
│   ├── background/            – date-prefixed background inputs (nye/ inbox)
│   └── deliverables/          – outbound funding documents (auditor packs, mails, notes, applications, board resolutions)
└── surewave/                  – SUREWAVE Horizon Europe project (Grant Agreement 101083342)
    ├── background/            – Filed consortium deliverables, Grant Agreement, Proposal, Annex 1 Part B
    └── deliverables/          – Sunlit Sea authored SUREWAVE outputs
```

Repo name (`sure-d61`) is historical and predates the multi-activity restructure.

---

## Activity tagging on tasks

Tasks in `TASKS.md` and `ARCHIVE.md` carry an activity tag as a bracketed prefix in the title:

```
### T25 `[ ]` [SURE] Do the thing
### T88 `[ ]` [GEN2] Order P4 mould from subcontractor
### T92 `[ ]` [COM] Draft pilot-deployment MoU with customer X
### T95 `[ ]` [FUND] Q3 periodic report to CINEA
### T99 `[ ]` [GENERIC] Reply to customer enquiry from X
```

Tag vocabulary (extend when a new stream is added):

| Tag | Activity |
|---|---|
| `[SURE]` | SuRE WP6 |
| `[GEN2]` | Gen 2 product development |
| `[COM]` | Commercial |
| `[FUND]` | Funding / EU reporting |
| `[GENERIC]` | Cross-cutting / shared (spans multiple activities or predates the split) |

The `T`-number sequence is authoritative and continuous across activities. Tags are for scanning; they do not affect sorting.

---

## Working rules

- **Read these first:** At the start of a task, or whenever context is missing, read `README.md`, `TASKS.md`, `ARCHIVE.md` and `docs/project_facts.md`. Search ARCHIVE before starting a new task to avoid duplicated work.
- **Project facts are canonical in `docs/project_facts.md`.** Consult it before drafting any deliverable that names a proper noun, place, product, grant, site or counterparty. Do not inherit phrasing from older background files without cross-checking the facts file. If a background file contradicts the facts file, the facts file wins — the background file is historical context, not current state. When the user corrects a fact in-session, append or correct the line in the facts file as part of the correction, not later.
- **Scan available skills at task start.** At the start of a task, scan the available skills list (shown in the system reminder) for any whose trigger conditions match the task shape — current actions or anticipated ones (e.g. `/check-deliverable` before converting any Markdown to PDF/docx via a wrapper; `/create-task` when the user asks to add a task; `/process-inbox` when `*/background/new/` has files; `/last-ned-paragraf` before citing a specific lovparagraf). Treat matching skills as part of the task plan from the outset, not as an optional lookup later. Not consulting a skill whose trigger clearly fires for the current task is a rule violation, on the same footing as skipping `git`/`gh` permission checks.
- **Single README:** the top-level `README.md` is the *only* README in the repo. Do not create per-folder README files (no `sure/README.md`, no `generic/README.md`, etc.). If a folder's contents need documenting, add or update the description in the *Activity contents* section of the top-level `README.md`.
- **Persistent scripts live in `scripts/`:** Any helper script that will be re-run (batch converters, cleaners, ad-hoc data processors) goes in `scripts/` at the repo root, never inside a data folder like `generic/`, `sure/`, `gen2/`, `funding/` etc. Document each new script in `docs/scripts.md` — purpose, how to invoke, inputs/outputs, safety notes. Follows the same pattern as the neighbouring `../fjordgata30` project. Truly single-use one-off commands can stay inline in the conversation without becoming a script.
- **Batch in-place edits require dry-run + backups:** Default to a non-destructive mode (write to `<name>.cleaned.<ext>` sibling files, or a separate output folder). Only overwrite originals after a dry-run has printed per-file word-count / line-count deltas and a human has confirmed none are surprising. Any single file that shrinks below ~70% of its original size is a red flag. See [`docs/rules/batch-edits.md`](docs/rules/batch-edits.md).
- **Permissions:** Always ask before running code or touching files outside the project folder (`sure-d61/`), even when running with `--dangerously-skip-permissions`. This includes reading from `../` neighbour projects — read there if useful, but never write without explicit approval.
- **File changes require confirmation:** Do not edit files or create new ones without an explicit request. If the user is discussing, asking or requesting a plan/description, respond with text — not with edits. Wait for a clear "do it" or equivalent before touching files.
- **Estimate effort before starting:** Before starting a task, judge complexity and give a rough time estimate ("this takes ~30 seconds" or "this is a large operation that could take 5–10 minutes"). If the estimate is above ~2 minutes, require explicit confirmation before starting — even if you already have a general "do it".
- **Task documentation:** When a task is done, document the solution under the task's context section in `TASKS.md` and mark the status `[x]`. Do not just flip status without noting what was done and which files were created/changed.
- **"Done" means end-to-end functional, not scaffolded.** A task is `[x]` only when the user can execute what they asked for and get the expected result. Files existing, docs looking reasonable, "the code should work" — none of that counts. Before flipping to `[x]`: for a skill, run the skill end-to-end against a real input; for a script, invoke it and verify the output; for a deliverable, open the rendered file. If a dependency is missing, broken or still aspirational, the task is `[~]`, not `[x]` — and the solution note says what's missing. The user's definition of done is their definition.
- **Task numbering:** Before creating a new task, find the highest existing T-number across **both** `TASKS.md` and `ARCHIVE.md`: `grep -h "^### T" TASKS.md ARCHIVE.md | grep -oP 'T\d+' | sort -t T -k2 -n | tail -1`. Use the next free number. The T-sequence is continuous across all activities; a `[SURE]` task and a `[GEN2]` task share the same counter.
- **Activity tag:** Every new task title must start with an activity tag (`[SURE]`, `[GEN2]`, `[COM]`, `[FUND]`, `[GENERIC]`). If a task spans two activities, pick the primary one; use `[GENERIC]` only when the task is genuinely cross-cutting or lives outside the three main activities. If a new stream is needed, propose an addition to the tag vocabulary and update this document.
- **Task sorting:** Tasks in `TASKS.md` and `ARCHIVE.md` are always sorted ascending on T-number. When creating a new task, insert it at the right position — do not append to the end without checking the number. Subtasks (T01.02 etc.) are sorted under their parent.
- **Archiving tasks:** Closed tasks are moved from `TASKS.md` to `ARCHIVE.md` only when the user explicitly asks. Never archive on your own initiative. Always search `ARCHIVE.md` before starting a task to avoid duplicated work.
- **Archiving documents (per-case):** Mirror the TASKS → ARCHIVE pattern for documents when a case closes. Pattern: `<domain>/archive/<case>/` under the domain folder where the case primarily lives (`funding/archive/<case>/`, `generic/background/archive/<case>/`, etc.). Only archive on explicit user request per case — never on your own initiative. Distinguish Type 1 (closed case / completed series — verdict in, grant disbursed, inspection cycle finished → archive) from Type 2 (permanent reference used rarely — legal texts, foundational records, baseline reports still binding → stays in its topical folder, never archived). When in doubt: if the material could plausibly be referenced in a future deliverable, it is Type 2 and stays put. Any case index at `cases/<case>/INDEX.md` must be updated with the new archive paths at the same time.
- **Case indexes (`cases/<case>/INDEX.md`):** For cross-cutting threads that span multiple activity folders (SuRE / Gen 2 / Funding / Generic / Surewave), consult the relevant `cases/<case>/INDEX.md` before starting work. The index is pointers only — timeline, main concept, status, source documents, legal/source references, related T-numbers, related cases. Files live in their original folders; the index does not duplicate content. When a case gains or loses files, update the index. Create a new case index only when the thread genuinely spans multiple folders *and* reaches ~15+ files or ~5+ T-numbers — otherwise the file is navigation overhead without the payoff.
- **Do not start tasks automatically:** Never begin a task without an explicit instruction from the user in the current conversation. When a task is finished, wait for the next instruction — do not pick and start the next task on your own.
- **README maintenance:** Always consider whether `README.md` and the relevant file in `docs/` needs updating as part of solving a task. New files, changed file names, changed folder structure or new dependencies must be reflected there — including in the *Activity contents* section for changes inside an activity folder.
- **PDF conversion:** Always use `pdftotext` (or an equivalent CLI tool) via Bash to convert PDF to text. Never use the Read tool page-by-page on PDF files — it is very expensive and loses structured text. Example: `pdftotext -layout "filename.pdf" - > filename.txt`
- **"New items" section in TASKS.md:** When reading `TASKS.md`, always check whether `## New items (unprocessed)` contains unprocessed bullet points. If so: ask the user whether they should be processed. Processing means converting each bullet into a numbered T-task with description (including the activity tag), and deleting the bullet.
- **`background/new/` inbox check:** At the start of every working session, check whether `generic/background/new/` (repo-level, cross-cutting inbox) or any `*/background/new/` (activity-level inbox, e.g. `sure/background/new/`, `funding/background/new/`) contains files. If any are present, list them and ask the user whether they should be processed — do not process on your own initiative. Processing means converting to Markdown per the pipeline in [`docs/background_convention.md`](docs/background_convention.md) (`pdftotext -layout` for PDFs, `pandoc … --wrap=none` for DOCX/PPTX/ODT/RTF/HTML, keep pictures as-is), date-prefixing the result, and moving it to the corresponding `background/` folder.
- **Date-prefix naming convention:** Every content file added to the repo carries a date-prefix of the form `YYYY-MM-DD_short_description.ext`. The date is the document's *own* date (issued / written / sent for external material; created or last substantially rewritten for internally authored material) — not the day it was filed. Full exemption list and examples: [`docs/rules/date-prefix.md`](docs/rules/date-prefix.md).
- **Ask before suboptimal approach:** If you see you are about to do something inefficiently (many steps, large token cost, detours), stop and ask the user whether they are sure they want you to continue — even when running with `--dangerously-skip-permissions`.
- **Git and gh are NEVER allowed without explicit permission in the current conversation:** Never run `git`, `gh` or other commands that invoke git. Applies to all operations including read-only ones (`git status`, `git log`, `gh pr list`, etc.) and compound Bash commands where git appears anywhere. Before every Bash command, check whether `git` or `gh` appears — if yes, stop and ask. See [`docs/rules/git-gh-forbidden.md`](docs/rules/git-gh-forbidden.md).
- **Do not convert to docx automatically:** Never generate `.docx` of a deliverable (via Pandoc, a helper script or anything else) as part of a task — not even when an existing docx attachment has changed and "should be regenerated for consistency". The Markdown source is the deliverable; conversion to docx happens **only when the user explicitly orders it**. When in doubt: mention in the wrap-up that docx has not been regenerated, so the user can order it themselves.
- **Pandoc is the chosen conversion tool** for `.docx`, `.pptx` and `.pdf`. Use pandoc commands directly (`pandoc input.md -o output.docx` etc.) when the user orders conversion. Do not suggest alternative pipelines (LibreOffice, Word COM, weasyprint, etc.) without pandoc being tried and rejected first. PDF conversion requires a separate engine (pdflatex/xelatex/wkhtmltopdf) — if none is available, deliver docx and leave PDF conversion to the user in Word/Office.
- **Letters on the Sunlit Sea letterhead:** When the user asks for an *official letter* (brev, henvendelse til myndighet/kunde/partner, formelle svarbrev, styreprotokoller som sendes eksternt) as `.docx` or `.pdf`, use `python scripts/md_to_letter.py <input.md>` (default `.docx`) or `python scripts/md_to_letter.py --pdf <input.md>` (produces `.pdf`). Never use plain `pandoc` for these — the wrapper is what guarantees the SUNLIT SEA wordmark, cream "A" watermark, Letter page size, margins and styles land correctly in both formats. Both paths treat `generic/background/2026-10-10_sunlit_sea_letterhead.docx` as the single source of truth. Full documentation in [`docs/pandoc_conversion.md`](docs/pandoc_conversion.md). The *Do not convert to docx automatically* rule still applies — only convert when the user explicitly orders it.
- **Generic PDF dispatcher:** When the user says *"create pdf of file FFF.md"* without specifying the template (slides / report / letter), run `python scripts/md_to_pdf.py <FFF.md>`. The dispatcher reads a `sunlit_template:` field from the file's YAML frontmatter and calls the right wrapper (`md_to_slides.py` for `slides`, `md_to_sunlit_report.py` for `report`, `md_to_letter.py --pdf` for `letter`). If the field is missing it infers from markdown shape; if inference is ambiguous it errors with a prompt to add the field. New Markdown deliverables that will be rendered to PDF should declare `sunlit_template: slides|report|letter` in the YAML header so the dispatcher is deterministic and does not have to guess. Per-template documentation in [`docs/scripts.md`](docs/scripts.md); each wrapper can still be invoked directly when a specific flag or output path is needed. The *Do not convert automatically* rule still applies — only convert when the user explicitly orders it.
- **Mermaid deliverables:** When delivering a docx, ensure mermaid diagrams are in fenced code blocks with proper line breaks, AND export each diagram as a standalone `.mmd` file to the activity's `figures/` folder (e.g. `sure/figures/`). Figures appear near the first reference and are numbered relative to their chapter.
- **Installing system packages or tools requires explicit permission:** Commands that install or modify system level (`tlmgr install`, `apt install`, `pip install --system`, `pip install --user`, `npm install -g`, `choco install`, `winget install`, `uv tool install`, `cargo install`, `gem install` etc.) always require explicit approval in the current conversation — including when a tool is missing to finish the requested task. Stop and ask.
- **Tools must only access files they were asked to access.** Any helper or wrapper introduced in this repo must be sandboxed so it does not read, write, or lock files outside the paths it was explicitly given — in particular, it must not touch `%userprofile%\Documents`, `~\Pictures` or other Windows-protected folders, since those trigger Controlled Folder Access alerts. Example: LibreOffice headless `soffice` is always invoked via `scripts/render_docx_pdf.sh`, which passes `-env:UserInstallation=file:///<tempdir>` to point LibreOffice at a disposable profile. Never call `soffice` directly from the Bash tool. When adding a new external tool, verify it respects this rule before standardising on it.
- **`rm` and other destructive operations require explicit permission for files I did not create myself in the current conversation.** Before every `rm`, `mv --force`, `> file` (overwrite) or equivalent: check whether the file is something I generated in this session. If not — stop and ask. Signals the file belongs to the user and the detailed check-before-delete list: [`docs/rules/destructive-ops.md`](docs/rules/destructive-ops.md).
- **Clean up after Agent invocations:** For tasks that invoke the `Agent` tool (particularly with `isolation: "worktree"`), always check at the end that `.claude/worktrees/agent-*` folders have been cleaned up. Document in the task solution note that cleanup was done.
- **Agent tool always creates worktrees – plan for cleanup:** The `Agent` tool creates a worktree per spawn regardless, even without `isolation: "worktree"` set explicitly. This also applies to agents that only read files. Cleanup sequence: [`docs/rules/agent-worktrees.md`](docs/rules/agent-worktrees.md).
- **Process feedback, don't parrot it:** When the user gives feedback on a deliverable, don't paste their words into the document. Extract the underlying claim, weigh whether it belongs and at what level of detail, and integrate the substance in the register of the surrounding prose. Argue for a better formulation when the direct version weakens the text. Their feedback is input for our collaboration; only use their exact wording when they say to.
- **Re-read source material immediately before drafting a deliverable:** When a deliverable draws on a background/context file, re-read that file immediately before drafting — not only at task start. Facts may have been added between task setup and drafting. See [`docs/rules/reread-source.md`](docs/rules/reread-source.md).
- **Image guidance in deliverables uses existing project assets, not invented ChatGPT prompts.** Before writing image recommendations or prompts in a deliverable, inventory the catalogued visual assets ([`docs/sure_images.md`](docs/sure_images.md)) and verify provenance (real photo vs AI concept render vs AI vector illustration vs CAD render vs FEM output). SUREWAVE D8.3 brochure figures `fig01`, `fig03`, `fig04` show the full-ring open-sea reference plant and are AI-generated — do not describe them as photographs and do not use them for nearshore deliverables ([`docs/surewave_configurations.md`](docs/surewave_configurations.md)). Prefer real Sunlit Sea deployment photos and Gen 1/Gen 2 CAD renders already in the repo. For angles not yet rendered, ask the user for a CAD snapshot from the Gen 2 FreeCAD model rather than writing a generic prompt. ChatGPT prompts are a last-resort fallback. Precedent and full rule: [`docs/rules/image-guidance.md`](docs/rules/image-guidance.md).
- **Treat agent/subagent outputs as hypotheses, not sources.** When a subagent (spawned via the `Agent` tool with any persona — "lawyer", "engineer", "visualisation specialist", etc.) asserts a design fact, specification, quantitative claim or technical constraint, verify against the primary source in the repo (project spec in `gen2/` or `sure/` background, SUREWAVE deliverables, Grant Agreement, Lovdata text, vendor datasheet) before propagating the assertion into any deliverable, doc, image prompt or follow-on task. The persona is a prompt device, not a credential. Precedent (T135): a subagent asserted FPV sits "~0.4–0.5 m above sea level" with "zero tilt"; the real spec (`gen2/norsmaterials_brief.md` line 44) is 6 cm freeboard at the lowest edge with 2° tilt — order-of-magnitude error that propagated into five files before the user caught it during image review. Full rule: [`docs/rules/subagent-outputs.md`](docs/rules/subagent-outputs.md).
- **Law paragraphs are cited against a verbatim downloaded source — never from memory.** Before naming a specific paragraph, subsection or sentence (e.g. `aksjeloven § 9-2 annet ledd`, `regnskapsloven § 5-3 tredje ledd`) in a deliverable *or* in a chat draft, confirm the paragraph exists as a verified `.md` file in `generic/background/lover/` with a metadata header (`kilde`, `lovnr`, `url`, `hentet`) and verbatim text. If it does not exist, either (a) download it first via the `last-ned-paragraf` skill, or (b) rephrase to general language without the paragraph name (`etter aksjeloven`, not `etter asl. § 9-2`). Users regularly paste chat drafts straight into letters; a paragraph reference from memory in chat goes to the recipient just as readily as one in a finished file. **Verification of stored files means curl against Lovdata and verbatim diff — never header-audit alone.** When the user says "verify / check / audit the laws" (or "sjekk lovene"), run the `last-ned-paragraf` extraction on every stored Lovdata file, compare the extracted text verbatim against the stored body, and replace any file whose content differs from current Lovdata. Inspecting YAML fields only tests that we wrote a header; it does not test that the stored text matches the law in force. Precedent: T123 cited the pre-2013 `aksjeloven § 9-2` 10 %-rule from memory; T130 verification pass then found `regnskapsloven § 5-6` stored with 586 chars of outdated text while current Lovdata was 355 chars (amendment in force since 1 juli 2021 that the stored file missed). Full rule and verification procedure: [`docs/rules/lovparagrafer.md`](docs/rules/lovparagrafer.md).
- **WebFetch is forbidden for law citations and formal statements from forvaltningsorganer** — use `curl` via Bash. WebFetch returns AI-processed content (paraphrase/summary), which is catastrophic for verbatim legal text. The fjordgata30 T157 audit (2026-10-06) documented that WebFetch paraphrases systematically leaked into letters sent to forvaltningsorganer, even when the prompt explicitly asked for verbatim text. For everyday lookups where a summary is fine (company info, general web pages, background reading) WebFetch is still allowed. If the user says *"bruk curl"*, *"ikke bruk webfetch"*, *"curl bare"* or similar in a conversation, WebFetch is forbidden for the entire conversation — no exceptions — until the user lifts the override. Full rule: [`docs/rules/webfetch.md`](docs/rules/webfetch.md).
- **Converted `.md` files must be self-contained:** After converting a `.docx`, `.pdf`, `.xlsx` etc. to markdown, the resulting `.md` must stand on its own. Do not add a YAML `source:` field pointing at the original binary, and do not write body text like "converted from `foo.docx`" or "the source document contains an EMF table". The original is often deleted after conversion, so any live reference becomes a broken pointer. Describe format quirks in generic terms ("this template's original form contains an EMF table") if needed, not as a pointer to a specific file path.
- **Follow conventions written this session:** Do not deviate from a rule or convention that has been written into `CLAUDE.md`, `README.md`, `docs/`, or a task solution note during the current conversation. No "one-off pragmatic" carve-outs. See [`docs/rules/follow-conventions.md`](docs/rules/follow-conventions.md).
- **Rules and preferences live in `CLAUDE.md` and `docs/`, not in per-machine memory:** This is a shared git repo used across machines. Working rules, tone rules, writing preferences and any other durable guidance go into `CLAUDE.md` (with elaboration in `docs/`) so they travel with the project. Do not save such rules to Claude Code's user-memory system — those files only exist on one machine and will not be seen from another.

---

## Language and tone

- All SuRE / D6.1 / D6.2 documents are in **English** (EU deliverable language). Other activities default to English too unless the audience is explicitly Norwegian.
- Be concrete and factual — do not "sell" the work, let documented facts speak.
- Reports must address the reader's concerns directly (CINEA reviewers: interface data-transfer status, KPI evidence, model-chain coverage; commercial: pricing basis, delivery, risk).
- **External deliverables stand alone.** Anything sent to an external reader (investor, auditor, regulator, funder, partner) must stand entirely on its own — the reader does not have the rest of the repo. No repo file paths, no `background/…` references, no task numbers, no internal framing like "draft" / "rewrite" / "offered to X". Also no references to companion documents by role: "as described in the løypemelding" is a broken reference if the reader doesn't have the løypemelding. Include necessary facts inline instead. Cite laws and standards by their canonical citation (`regnskapsloven § 5-3 tredje ledd`, `NRS(F) Nedskrivning av anleggsmidler pkt. 3`) — never by internal file path. Cross-references within the same document are fine (`jf. pkt. 6.3`). YAML `title`, `author`, `date` render as a visible title block in docx/PDF: rename to `internal_title` etc. when metadata is for us rather than the reader. Check the converted file, not just the markdown, before sending.
- **No bold in body text.** `**...**` is reserved for titles and subtitles (headings at the top of a document or section) — never inside sections. That includes paragraphs, list items, table cells, and any in-section prose. If a phrase truly needs to stand out, restructure the sentence, break it to its own line, or promote it to a subheading; do not reach for bold. Italics for defined terms are still fine; this rule is about `**` specifically.
- **Markdown lists render correctly.** Plain newlines join lines into one paragraph in markdown. For enumerations use `-` or `1.`; for stacked signature/address blocks use two trailing spaces at the end of each line except the last; for separate paragraphs leave a blank line. Verify the rendered output before delivering docx/PDF.
- **Avoid emphasis-by-assertion phrasing.** Do not lean on constructions that tell the reader how significant something is instead of showing it: *which is precisely*, *this is exactly*, *it is worth noting*, *crucially*, *importantly*, *the very X*, *not merely X but Y*, *no amount of X would*. They read as machine-written, they talk down to the reader, and a reviewer trips on them. State the fact and let it carry its own weight. If a sentence needs *precisely* to land, the sentence is the problem. Check for these before delivering any prose.
- **Lead with the positive claim, not the negation.** Readers remember what appears first. Don't tell the reader what to ignore — tell them what to focus on. Avoid patterns like "This is not X — it is Y"; write the Y directly, with X implied by contrast. If a "not" is essential to the meaning, put it *after* the core message so the positive statement lands first (e.g. "Y, not X"). Reserve outright negation for the rare case where the reader is likely to assume X and needs to be turned away from it — and even then, do it briefly.

### Norwegian-language deliverables

Norwegian text for Sunlit Sea (løypemeldinger, market intel, financial statements, board materials, letters to authorities) translates English finance and clean-tech jargon rather than borrowing it. Common replacements:

| English | Norwegian |
|---|---|
| cleantech | fornybar-teknologi |
| solar (adj.) | solkraft / solceller |
| equity | egenkapital |
| equity raise | innhenting av egenkapital |
| YoY / year-over-year | sammenlignet med samme periode i fjor (or `mot fjoråret`) |
| casting / cast | støping / støpt |
| mould design | støpeform-design |
| cure behavior | herdeforløp |
| R&D | FoU |
| in-house castings | egne støpetester |
| VC / venture capital | venturekapital |
| deployed | utrullet / installert |
| pre-committed (emission) | forhåndstegnet |
| H1 2026 | første halvår 2026 |

Currency and units follow the number, not precede it: `15 mrd USD` (not `$15 mrd`), `10 mill. NOK` (not `NOK 10M`), `0.060 EUR` (not `€0.060`). Note: English `billion` (10⁹) = Norwegian `milliard` (`mrd`) — do not use "billion" in Norwegian. Acronyms with no clean Norwegian equivalent (`PPA`, `LCOE`, `TRL`, `CAGR`, `Series A`, `Q1`) may stay in English; consider explaining on first use.

---

## Neighbour projects

The aluminium pressing simulation pipeline lives at `../thepressing/` (own git repo). It is the authoritative source for the pressing pipeline that D6.1 and D6.2 reference; when SuRE tasks need to look at pressing code (e.g. cup geometry generation in `freecadcupcalc.py`, the LS-DYNA `.k.hbs` templates, the `paretooptimizer.py` screening), read from `../thepressing/`, not from any copy inside this repo. Never write to `../thepressing/` without explicit approval (per the top-level *Permissions* rule).

Also read-only from this repo when useful for cross-project context: `../stotte/data/sunlit_sea/project_cards.json` (project card metadata for SuRE, Surewave, Enova, Skattefunn — grant references, durations, consortium partners, workpackages; use for prosjekt-navn and tidsrom, but *not* for budget-tall — accounting numbers come from regnskapsførers avstemminger).

Image references used in D6.1 / D6.2 are catalogued in [`docs/sure_images.md`](docs/sure_images.md).
