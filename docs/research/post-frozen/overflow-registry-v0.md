---
title: Overflow registry v0
status: candidate / research / not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-06
related_dispatch: PF-O1-01R
---

# Overflow registry v0

> Scope: record the five high-risk lanes that must stay outside Run-1 mainline even while successor-entry and localhost preview work move forward.

| topic | blocked_reason | reopen_condition | human_gate | kill_switch_ref | owner |
|---|---|---|---|---|---|
| `true_vault_write` | Bridge and vault work are still preview/dry-run only; `write_enabled=False` remains hardcoded and no RAW handoff proof exists. | `PF-C2`-class RAW handoff proof lands, true-write path gets its own dispatch, and write-disabled semantics are explicitly replaced under review. | `true_write_approval` | `REJECT_AS_TRUE_WRITE_UNLOCK` | `PF-O1 successor gate + future RAW handoff lane owner` |
| `runtime_tools` | `BBDown live` / `yt-dlp` / `ffmpeg` / `ASR` / `audio_transcript` remain blocked by current project redlines and are outside preview-only localhost proof. | Separate runtime dispatch, repo-external safety boundary, explicit preflight evidence, and scoped review all land first. | `explicit_runtime_approval` | `REJECT_AS_RUNTIME_CREEP` | `future runtime lane owner` |
| `browser_automation` | Browser automation and Playwright execution are not the accepted proof surface for Run-1; current line is manual/localhost preview only. | Screenshot packet or local proof produces a human-reviewed visual gate, and a separate automation dispatch is explicitly opened. | `visual_verdict` | `REJECT_AS_BROWSER_AUTOMATION_UNLOCK` | `future C4 visual-gate owner` |
| `dbvnext_migration` | DB vNext remains candidate-only and `services/api/migrations/**` stays forbidden in the current phase. | A migration-specific dispatch opens after explicit user approval and external audit, with candidate-vs-authority wording resolved first. | `explicit_migration_approval` | `REJECT_AS_MIGRATION_UNLOCK` | `future DB/migration lane owner` |
| `full_signal_workbench` | Full ranking/scoring/workbench expansion is ahead of current proof depth; docs-only or preview-only output cannot justify opening that product lane. | Topic-card-lite / preview proof demonstrates usefulness, a narrower successor path is accepted, and a dedicated downstream package opens. | `usefulness_verdict` | `REJECT_AS_DOCS_ONLY_PROOF` | `future PF-C1/PF-C4 successor owner` |
