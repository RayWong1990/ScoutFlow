# PF-LP-08 — VaultPreviewPanel real data mode

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
Refactor `VaultPreviewPanel.tsx` to render provided preview data with explicit empty, loading, and error states so placeholderPreview is no longer the default proof surface.

## 2-3. Output / dependencies
output: `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx`; depends: PF-LP-07

## 4. Files preview
```yaml
files_to_create:
  []
files_to_modify:
  - apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx:props-driven real data render states
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
  - apps/capture-station/src/features/vault-commit/**
```

## 8. T-PASS condition
Component tests prove empty, loading, error, and real markdown render states; placeholder data cannot be used as proof evidence.

### Required test assertions
1. Vitest verifies empty state renders no markdown proof claim
2. Vitest verifies loading/error states are visually distinct and operator-readable
3. Vitest verifies real preview renders `capture_id`, `target_path`, frontmatter, and `body_markdown`


## 12. Validation
```bash
pnpm --dir apps/capture-station typecheck
pnpm --dir apps/capture-station test -- VaultPreviewPanel
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: from provided preview prop
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-08-rendered-preview.json
  markdown_excerpt_lines: >=20
  copy_action_log: not_applicable_render_only
  download_filename: not_applicable_render_only
```
