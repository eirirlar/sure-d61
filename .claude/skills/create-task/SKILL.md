---
name: create-task
description: Create a new T-numbered task in `TASKS.md` with the correct next T-number, activity tag and insertion position. Trigger when the user asks to "create a task", "add a task", "track this as a task", "make this T-whatever", or similar. Enforces archive-first search, the single continuous T-sequence across activities, and ascending-ID sort order.
---

# create-task

## When to use

- User says: "create a task", "add this as a task", "track this", "T-this", "add it to TASKS.md".
- A piece of work is being deferred and the user wants it captured for later.
- Processing the `## New items (unprocessed)` section at the top of `TASKS.md`.

## Procedure

1. **Search `ARCHIVE.md` first** for anything that already closes the request. If a closed task covers the same ground, surface it to the user before creating a duplicate.

2. **Find the next T-number** across *both* `TASKS.md` and `ARCHIVE.md`:

   ```bash
   grep -h "^### T" TASKS.md ARCHIVE.md | grep -oP 'T\d+' | sort -t T -k2 -n | tail -1
   ```

   The T-sequence is continuous across all activities (`[SURE]`, `[GEN2]`, `[COM]`, `[FUND]`, `[GENERIC]`). Use the next free integer. For a subtask of an existing parent, use `T<parent>.NN` (e.g. T106.07) and sort it under its parent.

3. **Pick the activity tag:**
   - `[SURE]` — SuRE WP6 (Horizon Europe FPV model chain, D6.1/D6.2 side).
   - `[GEN2]` — Gen 2 product development.
   - `[COM]` — Commercial.
   - `[FUND]` — Funding / EU reporting.
   - `[GENERIC]` — Cross-cutting / infrastructure / repo management. Use only when the task genuinely spans multiple activities or lives outside the main streams.
   - `[SUREWAVE]` is reserved and not yet in use — do not introduce it unilaterally.

   If the task spans two activities, pick the primary one.

4. **Write the task block.** Format:

   ```markdown
   ### T<N> `[ ]` [TAG] <Title>

   <Description — one or two paragraphs; the "what" and the "why"; any constraints; blocked-on dependencies.>
   ```

   For a task that is already partly done or that has a known approach, add a `**Context files:**` list and/or a `**Deliverable:**` line. If blocked, use `**[BLOCKED — needs input from PERSON/ORG]**` on its own line.

5. **Insert at the right position.** Tasks in `TASKS.md` are sorted ascending by T-number — never append to the bottom without checking. Use the `## Index` section at the top of `TASKS.md` to find the right insert point, then insert into the main `## Tasks` block between the preceding and following T# headers. Subtasks sort under their parent.

6. **Update the Index.** Add a new bullet to the `## Index` section in the same ascending order:

   ```
   - T<N> `[ ]` [TAG] <Title>
   ```

7. **Confirm with the user.** Report the new T-number, the chosen tag, and the insert position.

## Applicable rules

- CLAUDE.md "**Task numbering**" — grep command above.
- CLAUDE.md "**Activity tag**" — every title starts with a bracketed tag.
- CLAUDE.md "**Task sorting**" — ascending by T-number across the file and the Index.
- CLAUDE.md "**Archiving tasks**" — never archive on your own initiative; search ARCHIVE before creating.
- CLAUDE.md "**Do not start tasks automatically**" — creating the task is the end of this skill. Do not start the work the task describes without a separate explicit instruction.
- CLAUDE.md "**File changes require confirmation**" — do not create a task from a casual mention. Wait for a clear "add this as a task" or equivalent.

## Historical references

- T125 — most recent new task (EUPI-PV budget position), shows the standard full-structure form.
- T126 — the current meta-restructure task, uses the subtask form (T126.01/T126.02/T126.03) under a parent.
- T106 — large multi-subtask thread (T106.01 through T106.06), useful reference for how subtasks sort under their parent.
- T104 — in-progress (`[~]`) task with ongoing iteration under one entry, useful reference for when a task should stay open rather than being split.

## Known pitfalls

- **Appending to the end** instead of inserting in ID order — the file is sorted, not chronological.
- **Reusing an archived T-number** — the grep must cover both `TASKS.md` and `ARCHIVE.md`, not just one.
- **Wrong activity tag** — `[GENERIC]` is a catch-all, but overusing it hides real activity signal. Prefer the specific activity tag when the task is anchored in one stream.
- **Starting the task immediately after creating it** — these are two separate user instructions; wait for the second one.
- **Forgetting the Index** — the TOC at the top of `TASKS.md` must stay in sync with the task body or the Phase 1 investment degrades over time.
