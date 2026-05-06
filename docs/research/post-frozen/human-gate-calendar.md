---
title: Human gate calendar
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-GLOBAL-08
---

# Human gate calendar

## gate_table

| gate | when it matters | evidence needed first | not_unlocked_until |
|---|---|---|---|
| `visual_terminal_verdict` | after screenshot or preview packet exists | screenshot bundle + proof scorecard | human says useful and visually acceptable |
| `usefulness_verdict` | after topic-card-lite / capture-plan-lite loop is tangible | preview walkthrough + evidence source matrix | a reviewer accepts the loop is worth expanding |
| `true_write_approval` | before any vault commit path | RAW handoff proof + write-disabled replacement plan | explicit human approval |
| `runtime_approval` | before BBDown live / ffmpeg / ASR / automation | repo-external safety proof + scoped dispatch | explicit human approval |
| `migration_approval` | before `services/api/migrations/**` | candidate-vs-authority wording cleanup + audit | explicit human approval |

## scheduling_note

- Human gates are calendar events, not silent implications of CI green.
- A merged docs-only PR may prepare a gate, but never satisfies it alone.

## verdict

- `T-PASS` for gate planning only.
