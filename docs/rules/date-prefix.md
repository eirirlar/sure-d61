# Date-prefix naming convention

Every content file added to the repo carries a date-prefix of the form `YYYY-MM-DD_short_description.ext`.

The date is the document's *own* date — issued / written / sent for external material; created or last substantially rewritten for internally authored material — not the day it was filed.

## Applies to

- Every file in any `background/` folder (`generic/background/`, `sure/background/`, `funding/background/`, `surewave/background/`, `gen2/background/`).
- Every file in any `deliverable/` or `deliverables/` folder (`generic/deliverable/`, `sure/deliverables/`, `funding/deliverables/`, `surewave/deliverables/`).
- Standalone content files at an activity root (single-purpose reports, status snapshots, curated indexes) if any ever appear there. Current practice is to keep such files inside `background/` or `deliverables/` rather than at the activity root, but the date-prefix rule still applies if a root-level content file is added.

## Exemptions

- Structural / index files that live at the repo root or at an activity root and function as the navigation entry point: `README.md`, `CLAUDE.md`, `TASKS.md`, `ARCHIVE.md`, and per-activity README-equivalent index files.
- Binary asset files inside a per-source subfolder that already carries a date prefix (e.g. individual images inside `surewave/images/2026-09-29_sunlit_sea_webpage/`) — the parent folder's date carries.

## Discipline

When you add a new file, apply the prefix immediately. When you find an un-prefixed content file already there, rename it at next touch and note the rename in the task solution — and update any references (grep the repo for the old filename first).
