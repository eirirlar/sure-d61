# Background convention

`generic/background/` holds **cross-cutting** background material — the material that spans activities (SuRE, Gen 2, Commercial, Funding) or predates the activity split. Company-level investor updates, legal documents, funding history, board correspondence, general Sunlit Sea history all belong here. Activity-specific background stays under the activity's own folder: `sure/background/`, `gen2/background/`, `funding/background/`.

## File-naming convention

Every file in any `background/` folder (`generic/background/` or activity-level `*/background/`) carries a date prefix:

```
YYYY-MM-DD_short_description.ext
```

Examples:

- `2025-11-14_investor_update_q3.md`
- `2024-02-01_shareholder_agreement.pdf`
- `2023-06-08_board_meeting_minutes.md`

The date is the date of the document (when it was written / issued / sent), not the day it was filed. When the exact date is unknown, use the best approximation and note the uncertainty in the file body.

## Inbox: `generic/background/new/`

Files that have not been processed yet land in `generic/background/new/` (or in an activity-level `*/background/new/` for activity-specific inputs). Typical sources: PDFs (scanned or exported), Word documents, PowerPoint decks, photos and screenshots, plain-text notes.

At the start of every working session, check `generic/background/new/` (and any `*/background/new/`) for unprocessed files. The `CLAUDE.md` working rules document this.

## Conversion pipeline

| Source format | Tool | Command shape |
|---|---|---|
| `.pdf` | `pdftotext` | `pdftotext -layout "generic/background/new/foo.pdf" generic/background/new/foo.txt` then hand-tidy into `.md` |
| `.docx`, `.pptx`, `.odt`, `.rtf`, `.html` | `pandoc` | `pandoc "generic/background/new/foo.docx" -o generic/background/new/foo.md --wrap=none` |
| `.md`, `.txt` | (already text) | tidy, then timestamp-prefix and move |
| `.png`, `.jpg`, `.jpeg` and other true binary evidence | keep as-is | timestamp-prefix and move; do not convert |

After conversion:

1. Review the `.md` and add a short preamble at the top noting the source file name and the document's original date (if known).
2. Rename to `YYYY-MM-DD_description.md`.
3. Move to `generic/background/` (or the activity's `*/background/`).
4. Remove the intermediate `.txt` from `pdftotext` — only the `.md` needs to stick around.
5. Keep the original binary in `background/` **only** if it is the authoritative source (signed PDFs, signed contracts, presentations we might redistribute). Otherwise the `.md` supersedes it and the original can be dropped.
