# Dispatch Template Extract Retro - 2026-05-04

## Decision

Shared dispatch boilerplate now lives in `docs/dispatch-template.md`.
New dispatch files should keep task-specific content short and reference the shared template.
The dispatch self-audit shape is reduced from 7-8 segments to 5 segments: Scope, Authority, Safety, Validation, and Next gate.

## Why

Older dispatch files repeatedly copied validation commands, audit wording, and final-report text.
That made prompts longer, increased drift risk, and mixed shared process with task-specific instructions.
The older Boundary / Authority / Enum / Next-gate split mostly duplicated the same scope and safety checks.

## Not Changed

- Existing dispatch files in `~/Downloads/` are not retroactively rewritten.
- Product code is untouched.
- PRD, SRD, locked-principles, and specs contracts are untouched.
- `docs/current.md`, `docs/task-index.md`, and `docs/decision-log.md` are untouched in this task because T-P1A-015 is concurrently writing authority surfaces.

## Follow-Up

New dispatch files from `T-P1A-017+` should use the shared template.
Template edits should run as a separate bounded task.
