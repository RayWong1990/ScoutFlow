# PF-LP-07 — Real vault preview fetch after capture

```yaml
status: candidate_task_draft_not_authority
pack: PF-localhost-preview-pack
cluster: PF-localhost-preview
dispatch_class: proof_mainline
open_after_state: successor_entry_ready
proof_kind: preview_only
human_gate: none
priority: high
inherits: ../../_PACK-DEFAULTS.md
```

## 0/5/6/7/9/10/11. Shared clauses
Inherits `_PACK-DEFAULTS.md`.


## 1. Goal
Fetch `/captures/{capture_id}/vault-preview` after capture_id arrives so the H5 loop displays server-rendered markdown rather than `placeholderPreview`.

## 2-3. Output / dependencies
output: `apps/capture-station preview fetch seam`; depends: PF-LP-06, PF-LP-02

## 4. Files preview
```yaml
files_to_create:
  []
files_to_modify:
  - apps/capture-station/src/lib/api-client.ts:getVaultPreview usage typing if needed
  - apps/capture-station/src/layout/FourPanelShell.tsx:preview fetch orchestration
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
  - apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx
```

## 8. T-PASS condition
Tests prove preview fetch runs after capture_id, handles 409 vault-root unset, and surfaces body_markdown when configured.

### Required test assertions
1. Vitest verifies `getVaultPreview(capture_id)` is called only after capture_id exists
2. Vitest verifies 409 vault-root unset maps to visible fail-loud state
3. Vitest verifies successful preview stores `body_markdown` and `target_path` for render handoff


## 12. Validation
```bash
pnpm --dir apps/capture-station typecheck
pnpm --dir apps/capture-station test -- preview
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: captured from PF-LP-06 state seam
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-07-vault-preview-response.json
  markdown_excerpt_lines: >=20
  copy_action_log: not_applicable_fetch_only
  download_filename: not_applicable_fetch_only
```
