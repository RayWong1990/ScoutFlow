# PF-LP-11 — Preview error and blocked-state UX

```yaml
status: candidate_task_draft_not_authority
pack: PF-localhost-preview-pack
cluster: PF-localhost-preview
dispatch_class: proof_mainline
open_after_state: successor_entry_ready
proof_kind: preview_only
human_gate: none
priority: medium
inherits: ../../_PACK-DEFAULTS.md
```

## 0/5/6/7/9/10/11. Shared clauses
Inherits `_PACK-DEFAULTS.md`.


## 1. Goal
Render fail-loud UX for unset vault root, missing capture, and write-disabled commit states so localhost users can distinguish preview failure from runtime unlock.

## 2-3. Output / dependencies
output: `apps/capture-station preview error UI`; depends: PF-LP-07, PF-LP-08

## 4. Files preview
```yaml
files_to_create:
  []
files_to_modify:
  - apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx:error state variants
  - apps/capture-station/src/features/vault-commit/VaultCommitDryRunButton.tsx:write-disabled wording if needed
files_will_NOT_touch:
  - docs/current.md
  - AGENTS.md
  - docs/task-index.md
  - docs/decision-log.md
  - services/api/migrations/**
  - workers/**
  - packages/**
  - data/**
  - referencerepo/**
  - services/**
  - true vault write
```

## 8. T-PASS condition
Tests prove three blocked-state messages and no UI copy implies true vault write.

### Required test assertions
1. Vitest verifies unset vault root renders `SCOUTFLOW_VAULT_ROOT is not configured` style message
2. Vitest verifies missing capture error renders `capture_not_found` style message
3. Vitest verifies write-disabled state displays dry-run only and never labels commit as executed


## 12. Validation
```bash
pnpm --dir apps/capture-station typecheck
pnpm --dir apps/capture-station test -- VaultPreviewPanel VaultCommitDryRunButton
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 12.5. Manual evidence step
- Open localhost in a normal browser tab
- Observe unset vault-root or write-disabled state if triggered
- Save operator-visible state note to docs/research/post-frozen/evidence/PF-LP-11-blocked-state.md
- Do NOT use browser automation

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: real or fixture capture_id from preview loop
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-11-error-response.json
  markdown_excerpt_lines: not_applicable_error_state
  copy_action_log: not_applicable_error_state
  download_filename: not_applicable_error_state
```
