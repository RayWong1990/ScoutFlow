# PF-LP-06 — Capture id state bridge

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
Introduce a bounded H5 state seam so `UrlBar` capture_id can flow to the preview panel without adding global authority state or direct storage writes.

## 2-3. Output / dependencies
output: `apps/capture-station/src/layout/FourPanelShell.tsx + local state seam`; depends: PF-LP-05

## 4. Files preview
```yaml
files_to_create:
  []
files_to_modify:
  - apps/capture-station/src/layout/FourPanelShell.tsx:local capture state seam
  - apps/capture-station/src/features/url-bar/UrlBar.tsx:callback prop for capture result
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
  - workers/**
  - packages/**
```

## 8. T-PASS condition
Tests prove local state receives capture_id, resets on new URL, and never writes storage or vault directly.

### Required test assertions
1. Vitest verifies successful UrlBar submit updates shell-local capture_id state
2. Vitest verifies editing URL after success clears stale preview state
3. Vitest verifies no direct storage, fs, or vault write API is imported by H5 components


## 12. Validation
```bash
pnpm --dir apps/capture-station typecheck
pnpm --dir apps/capture-station test -- FourPanelShell UrlBar
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: shell-local state after UrlBar submit
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-06-state-transition.json
  markdown_excerpt_lines: not_applicable_state_only
  copy_action_log: not_applicable_state_only
  download_filename: not_applicable_state_only
```
