# Dispatch Authoring Guide

> User-facing guide for writing a dispatch that Codex Desktop can execute directly.

## Steps

1. Copy the shared header from `docs/dispatch-template.md`.
2. Fill only the task-specific sections: Goal, Allowed Paths, Forbidden Paths, Required Behavior, Stop-the-line, Branch / PR / Merge, Estimated Effort.
3. Reference `docs/dispatch-template.md` for Shared Validation, 5-Part Self-Audit, and Final Report instead of pasting them.
4. Decide whether the task is high risk. Schema, credential, state, receipt, redaction, Trust Trace, or runtime-gate work needs external audit.
5. Save the dispatch under `~/Downloads/scoutflow-dispatch-prompts-YYYY-MM-DD/NN-dispatch-T-P1A-NNN-<slug>.md`.
6. Paste the dispatch into Codex Desktop with any current user gate wording.

## Common Mistakes

- Repeating shared validation, audit, or final-report blocks.
- Inventing a new shared audit shape for one dispatch.
- Reusing an existing task ID or branch name; check with `grep -rE "T-P1A-NNN" ~/Downloads/scoutflow-dispatch-prompts-*/ docs/`.
- Marking retro or template tasks as product lanes when they are review / research / governance lanes.

## Numbering

- Product code task: use the next mainline `T-P1A-NNN`.
- Retro, template, and governance task: use the same mainline sequence, with small bounded steps.
- Amendment promotion task: use its own mainline number.
