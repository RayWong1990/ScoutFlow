---
title: PF Pack Defaults For Post-Frozen Successor Dispatches
status: shared_default / candidate / not-authority
created_at: 2026-05-06
---

# _PACK-DEFAULTS

## Purpose
Shared clauses for PF-META-01 rewritten dispatches. Each dispatch inherits this file and keeps only task-native Goal, files preview, validation, and evidence shape.

## 0. Frozen historical boundary
- Dispatch126-176 are frozen historical assets/evidence only.
- Do not reopen, reorder, or re-execute Dispatch126-176.
- Cite frozen work only as evidence or inherited design input.
- Never call frozen dispatches active candidates, waiting tasks, or runnable packs.
- Violation verdict: `REJECT_AS_REOPEN_FROZEN_HISTORY`.

## 5. Forbidden paths / claims
Forbidden paths:
- `docs/current.md`, `AGENTS.md`, `docs/task-index.md`, `docs/decision-log.md`
- `services/api/migrations/**`, `workers/**`, `packages/**`, `data/**`, `referencerepo/**`
- credential stores, cookies, auth sidecars, QR files, raw stdout/stderr with secrets

Forbidden claims:
- true vault write approval
- BBDown live / yt-dlp / ffmpeg / ASR / `audio_transcript` approval
- browser automation approval
- DBvNext / migration approval
- full Signal Workbench implementation approval
- docs-only output as product proof
- visual checklist as visual terminal verdict

## 6. Blocked claims that remain blocked
```yaml
no_true_vault_write: true
no_runtime_approval: true
no_browser_automation: true
no_migration: true
no_ASR: true
no_BBDown_live: true
no_full_signal_workbench: true
```

Bridge hard fact:
```yaml
mount_does_not_unlock_write: services/api/scoutflow_api/bridge/config.py keeps write_enabled=False
```

Frontend hard fact:
```yaml
manual_screenshot_note_is_review_evidence_not_browser_automation: true
preview_ui_does_not_equal_visual_terminal_verdict: true
```

## 7. Enter condition
- `open_after_state` is satisfied.
- Pack STOP-LINES inherit `_SHARED-STOP-LINES.md`.
- §1 Goal has verb + object + seam.
- §4 uses `files_to_create`, `files_to_modify`, `files_will_NOT_touch`.
- §12 is task-specific.
- §13 binds evidence_shape to proof_kind.
- Blocked claims remain blocked.

## 9. partial condition
A dispatch may be `partial` only when output exists, the missing evidence is named, and no downstream gate opens.
Allowed labels:
```yaml
partial_missing_validation: validation command or environment failed without product claim
partial_missing_human_gate: human verdict not supplied
partial_missing_evidence_shape: required evidence fields incomplete
partial_scope_reduced: allowed paths narrowed with reason
```

## 10. FAIL_ENV / REJECT_AS_X
Use `FAIL_ENV` for local environment failure without false proof.
Use `REJECT_AS_X` for boundary violations:
```yaml
REJECT_AS_REOPEN_FROZEN_HISTORY
REJECT_AS_RUNTIME_CREEP
REJECT_AS_TRUE_WRITE_UNLOCK
REJECT_AS_BROWSER_AUTOMATION_UNLOCK
REJECT_AS_MIGRATION_UNLOCK
REJECT_AS_DOCS_ONLY_PROOF
REJECT_AS_PLACEHOLDER_PROOF
REJECT_AS_SECOND_INBOX
REJECT_AS_AUTHORITY_DRIFT
```

## 11. Kill signal
Stop immediately on any attempt to:
- enable true vault writes;
- add runtime tools or browser automation;
- edit migrations or authority four-file;
- treat docs, placeholder, fixture, dry-run, or checklist as proof;
- reopen Dispatch126-176.

## 13. Evidence shape dictionary
```yaml
shape_only:
  output_path: required
  required_sections: required_list
  required_rows: optional_int
  required_columns: optional_list
preview_only:
  capture_id: required
  fetch_response_path: required
  markdown_excerpt_lines: int >= 20
  copy_action_log: required
  download_filename: required
human_verdict:
  verdict_table_path: required
  useful_count: int
  reject_count: int
  edit_cost_log_path: required
  threshold: useful_count >= 2 of 3
raw_intake:
  note_paths: list >= 2
  intake_evidence_path: required
  not_second_inbox_check: true
script_seed:
  seed_path: required
  downstream_consumer_log: required
screenshot_visual:
  screenshot_paths: list >= 3
  visual_verdict_path: required
  five_gate_checklist: true
  human_terminal_verdict: required
```

## Vocabulary
Use `T-PASS`, `V-PASS`, `partial`, `FAIL_ENV`, and `REJECT_AS_X`. Avoid bare success labels.
