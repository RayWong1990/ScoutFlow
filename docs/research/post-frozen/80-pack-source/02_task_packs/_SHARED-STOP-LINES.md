---
title: Shared Stop Lines For PF Successor Packs
status: shared_stop_lines / candidate / not-authority
created_at: 2026-05-06
---

# _SHARED-STOP-LINES

## Global stop-lines

| Stop-line | Verdict if triggered | Reason |
|---|---|---|
| Reopen / reorder / re-execute Dispatch126-176 | `REJECT_AS_REOPEN_FROZEN_HISTORY` | Frozen historical dispatches are evidence only. |
| Claim docs-only output as proof | `REJECT_AS_DOCS_ONLY_PROOF` | Candidate docs are not product proof. |
| Claim placeholder / fixture / dry-run as closed loop | `REJECT_AS_PLACEHOLDER_PROOF` | Preview-only and dry-run are bounded evidence, not delivery. |
| Enable true vault write | `REJECT_AS_TRUE_WRITE_UNLOCK` | Current route remains preview/dry-run only. |
| Add BBDown live / yt-dlp / ffmpeg / ASR / audio_transcript | `REJECT_AS_RUNTIME_CREEP` | Runtime tools remain blocked. |
| Add browser automation as mainline | `REJECT_AS_BROWSER_AUTOMATION_UNLOCK` | Browser automation remains separately gated. |
| Touch `services/api/migrations/**` | `REJECT_AS_MIGRATION_UNLOCK` | Migration needs explicit separate gate. |
| Edit authority four-file from this meta pack | `REJECT_AS_AUTHORITY_DRIFT` | This package is authoring-only. |
| Turn RAW handoff into a second inbox | `REJECT_AS_SECOND_INBOX` | RAW handoff must show intake or downstream seed. |

## Required local phrase

Every pack-specific STOP-LINES.md should say it inherits this file and then add only cluster-specific overrides.
