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

Commercial/market intel (previously under `commercial/`) is folded into `background/` alongside other cross-cutting material — one-off market snapshots and competitor scans are date-prefixed like other `background/` files. Commercial tasks may still carry the `[COM]` tag.

See `TASKS.md` for the open task list, `ARCHIVE.md` for closed tasks, `README.md` for conversion tooling (Pandoc, mermaid-filter, pdftotext).

---

## Files and folders (top level)

```
sure-d61/
├── CLAUDE.md                  – this document (project context for AI)
├── TASKS.md                   – open task list (single T-sequence across all activities)
├── ARCHIVE.md                 – closed tasks
├── README.md                  – tools, workflows, conventions, activity contents (only README in repo)
├── background/                – cross-cutting background material (date-prefixed files) + new/ inbox
├── sure/                      – SuRE WP6 activity
├── gen2/                      – Gen 2 product development
└── funding/                   – Grants, EU reporting, financial
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
```

Tag vocabulary (extend when a new stream is added):

| Tag | Activity |
|---|---|
| `[SURE]` | SuRE WP6 |
| `[GEN2]` | Gen 2 product development |
| `[COM]` | Commercial |
| `[FUND]` | Funding / EU reporting |

The `T`-number sequence is authoritative and continuous across activities. Tags are for scanning; they do not affect sorting.

---

## Working rules

- **Read these first:** At the start of a task, or whenever context is missing, read `README.md`, `TASKS.md` and `ARCHIVE.md`. Search ARCHIVE before starting a new task to avoid duplicated work.
- **Single README:** the top-level `README.md` is the *only* README in the repo. Do not create per-folder README files (no `sure/README.md`, no `background/README.md`, etc.). If a folder's contents need documenting, add or update the description in the *Activity contents* section of the top-level `README.md`.
- **Persistent scripts live in `scripts/`:** Any helper script that will be re-run (batch converters, cleaners, ad-hoc data processors) goes in `scripts/` at the repo root, never inside a data folder like `background/`, `sure/`, `gen2/` etc. Document each new script in the *Scripts* section of the top-level `README.md` — purpose, how to invoke, inputs/outputs, safety notes. Follows the same pattern as the neighbouring `../fjordgata30` project. Truly single-use one-off commands can stay inline in the conversation without becoming a script.
- **Batch in-place edits require dry-run + backups:** When writing a script that transforms many files with regex/pattern replacement, the default must be a non-destructive mode (write to `<name>.cleaned.<ext>` sibling files, or a separate output folder). Only overwrite originals after a dry-run has printed per-file word-count / line-count deltas and a human has confirmed none of them are surprising. Any single file that shrinks below ~70% of its original size is a red flag until inspected — an over-broad regex can silently truncate content. Convention exists because of the T73 investor-update incident where two files silently lost ~90% of content to a signature-start regex that matched markdown horizontal rules.
- **Permissions:** Always ask before running code or touching files outside the project folder (`sure-d61/`), even when running with `--dangerously-skip-permissions`. This includes reading from `../` neighbour projects — read there if useful, but never write without explicit approval.
- **File changes require confirmation:** Do not edit files or create new ones without an explicit request. If the user is discussing, asking or requesting a plan/description, respond with text — not with edits. Wait for a clear "do it" or equivalent before touching files.
- **Estimate effort before starting:** Before starting a task, judge complexity and give a rough time estimate ("this takes ~30 seconds" or "this is a large operation that could take 5–10 minutes"). If the estimate is above ~2 minutes, require explicit confirmation before starting — even if you already have a general "do it".
- **Task documentation:** When a task is done, document the solution under the task's context section in `TASKS.md` and mark the status `[x]`. Do not just flip status without noting what was done and which files were created/changed.
- **Task numbering:** Before creating a new task, find the highest existing T-number across **both** `TASKS.md` and `ARCHIVE.md`: `grep -h "^### T" TASKS.md ARCHIVE.md | grep -oP 'T\d+' | sort -t T -k2 -n | tail -1`. Use the next free number. The T-sequence is continuous across all activities; a `[SURE]` task and a `[GEN2]` task share the same counter.
- **Activity tag:** Every new task title must start with an activity tag (`[SURE]`, `[GEN2]`, `[COM]`, `[FUND]`). If a task spans two activities, pick the primary one. If a new stream is needed, propose an addition to the tag vocabulary and update this document.
- **Task sorting:** Tasks in `TASKS.md` and `ARCHIVE.md` are always sorted ascending on T-number. When creating a new task, insert it at the right position — do not append to the end without checking the number. Subtasks (T01.02 etc.) are sorted under their parent.
- **Archiving tasks:** Closed tasks are moved from `TASKS.md` to `ARCHIVE.md` only when the user explicitly asks. Never archive on your own initiative. Always search `ARCHIVE.md` before starting a task to avoid duplicated work.
- **Do not start tasks automatically:** Never begin a task without an explicit instruction from the user in the current conversation. When a task is finished, wait for the next instruction — do not pick and start the next task on your own.
- **README maintenance:** Always consider whether `README.md` needs updating as part of solving a task. New files, changed file names, changed folder structure or new dependencies must be reflected there — including in the *Activity contents* section for changes inside an activity folder.
- **PDF conversion:** Always use `pdftotext` (or an equivalent CLI tool) via Bash to convert PDF to text. Never use the Read tool page-by-page on PDF files — it is very expensive and loses structured text. Example: `pdftotext -layout "filename.pdf" - > filename.txt`
- **"New items" section in TASKS.md:** When reading `TASKS.md`, always check whether `## New items (unprocessed)` contains unprocessed bullet points. If so: ask the user whether they should be processed. Processing means converting each bullet into a numbered T-task with description (including the activity tag), and deleting the bullet.
- **`background/new/` inbox check:** At the start of every working session, check whether `background/new/` (root-level, cross-cutting inbox) or any `*/background/new/` (activity-level inbox, e.g. `sure/background/new/`) contains files. If any are present, list them and ask the user whether they should be processed — do not process on your own initiative. Processing means converting to Markdown per the pipeline in the *Background convention* section of `README.md` (`pdftotext -layout` for PDFs, `pandoc … --wrap=none` for DOCX/PPTX/ODT/RTF/HTML, keep pictures as-is), date-prefixing the result, and moving it to `background/` (or the activity's `background/`).
- **`background/` naming convention:** Every file in a `background/` folder (root or activity-level) must have a date-prefix of the form `YYYY-MM-DD_short_description.ext`. The date is the document's *own* date (issued / written / sent), not the day it was filed. When you add a new file to a `background/` folder, apply the prefix immediately. When you find an un-prefixed file already there, rename it at next touch and note the rename in the task solution.
- **Ask before suboptimal approach:** If you see you are about to do something inefficiently (many steps, large token cost, detours), stop and ask the user whether they are sure they want you to continue — even when running with `--dangerously-skip-permissions`.
- **Git and gh are NEVER allowed without explicit permission in the current conversation:** Never run `git`, `gh` or other commands that invoke git (including scripts that call git internally and compound Bash commands where git appears anywhere — `pwd && git ...` is just as forbidden as plain `git ...`). This applies to **all** operations, including "harmless" read-only commands: `git status`, `git diff`, `git log`, `git branch`, `git show`, `git ls-files`, `git rev-parse`, `git worktree list`, `gh pr list`, `gh issue view` etc. Before every Bash command, explicitly check whether `git` or `gh` appears anywhere — if yes, stop and ask, even when you need info quickly. If you need info that could have come from git: use Read/Glob/Grep, or ask the user to paste the output.
- **Do not convert to docx automatically:** Never generate `.docx` of a deliverable (via Pandoc, a helper script or anything else) as part of a task — not even when an existing docx attachment has changed and "should be regenerated for consistency". The Markdown source is the deliverable; conversion to docx happens **only when the user explicitly orders it**. When in doubt: mention in the wrap-up that docx has not been regenerated, so the user can order it themselves.
- **Pandoc is the chosen conversion tool** for `.docx`, `.pptx` and `.pdf`. Use pandoc commands directly (`pandoc input.md -o output.docx` etc.) when the user orders conversion. Do not suggest alternative pipelines (LibreOffice, Word COM, weasyprint, etc.) without pandoc being tried and rejected first. PDF conversion requires a separate engine (pdflatex/xelatex/wkhtmltopdf) — if none is available, deliver docx and leave PDF conversion to the user in Word/Office.
- **Mermaid deliverables:** When delivering a docx, ensure mermaid diagrams are in fenced code blocks with proper line breaks, AND export each diagram as a standalone `.mmd` file to the activity's `figures/` folder (e.g. `sure/figures/`). Figures appear near the first reference and are numbered relative to their chapter.
- **Installing system packages or tools requires explicit permission:** Commands that install or modify system level (`tlmgr install`, `apt install`, `pip install --system`, `pip install --user`, `npm install -g`, `choco install`, `winget install`, `uv tool install`, `cargo install`, `gem install` etc.) always require explicit approval in the current conversation — including when a tool is missing to finish the requested task. Stop and ask.
- **`rm` and other destructive operations require explicit permission for files I did not create myself in the current conversation.** Before every `rm`, `mv --force`, `> file` (overwrite) or equivalent: check whether the file is something I generated in this session. If not — stop and ask. Signals that the file belongs to the user (and must not be touched): file size or mtime that differs from my own output, filename that does not match my pipeline, files that "seem odd to have" in the folder. Deleting is worse than letting it be — ask instead.
- **Clean up after Agent invocations:** For tasks that invoke the `Agent` tool (particularly with `isolation: "worktree"`), always check at the end that `.claude/worktrees/agent-*` folders have been cleaned up. Document in the task solution note that cleanup was done.
- **Agent tool always creates worktrees – plan for cleanup:** The `Agent` tool in Claude Code (this harness version) creates a worktree per spawn regardless, even without `isolation: "worktree"` set explicitly. This also applies to agents that only read files. After the session ends and the pid is dead, worktrees can be cleaned with: `git worktree repair` → `git worktree unlock` → `git worktree remove --force` → `git branch -D` (and finally `git worktree prune`). For Cygwin/Windows mismatch: run cleanup in Git Bash, not Cygwin.

---

## Language and tone

- All SuRE / D6.1 / D6.2 documents are in **English** (EU deliverable language). Other activities default to English too unless the audience is explicitly Norwegian.
- Be concrete and factual — do not "sell" the work, let documented facts speak.
- Reports must address the reader's concerns directly (CINEA reviewers: interface data-transfer status, KPI evidence, model-chain coverage; commercial: pricing basis, delivery, risk).

---

## SuRE background images (`sure/images/`)

These are the images used in the D6.1 / D6.2 reports.

### Material & Product
- `cup_shape.png` — Sample cup shape showing the target geometry produced by the pressing process
- `alu_sheet_vs_pressed.jpg` — Before/after comparison of raw aluminium sheet vs. the pressed final product
- `chemical_composition_alu5083h111.png` — Composition breakdown of 5083-H111 aluminium alloy (the material used)

### Gen 1 FPV system
- `fpv_gen1_assembly.png` — Assembly diagram showing all Gen 1 components: glass/PET solar panels, polystyrene cup infill, butyl/silicone edge sealant, 2-component silicone potting, two pressed aluminium parts bonded together as a float with air inside (forming the bottom plate, part of infill, and float system), and brackets on the float lip for the connect system
- `fpv_gen1_float.png` — The actual Gen 1 product as built
- `fpv_matrix_and_mooring_system_for_25kwp.png` — Layout showing how different form factors affect the matrix arrangement and mooring system for a 25 kWp installation *(removed from report; kept in folder as reference)*

### Heat transfer
- `gen1_cooling_of_pv_from_heat_transfer_to_water.png` — Natural heat-dissipation paths through infill and pressed aluminium bottom plate in Gen 1; passive heat flow visualisation

### Pressing equipment & simulation
- `punch_and_die.png` — STEP file image of the punch and die setup; early iteration of the pressing FEM simulation
- `meshed_punchdie.png` — Finite-element mesh of the punch and die components for FEM analysis
- `punch_die_mesh_with_gripper.png` — Meshed punch/die setup with gripper ring; tests flow control and metal-thinning reduction
- `punch_die_mesh_without_gripper.png` — Baseline for comparison; the gripper approach was later abandoned in favour of fluid forming

### CAD export process
- `freecad_to_step_1.png` — FreeCAD interface showing design properties and parameters that control the geometry
- `freecad_to_step_2.png` — STEP file rendered from one angle
- `freecad_to_step_3.png` — STEP file rendered from a second angle
- `freecad_to_step_4.png` — STEP file rendered from a third angle

### Tool failure analysis
- `punchdie_rip1.png` — Tool damage/failure scenario 1 showing tearing/ripping under pressing loads
- `punchdie_rip2.png` — Tool damage/failure scenario 2 showing tearing/ripping under pressing loads
