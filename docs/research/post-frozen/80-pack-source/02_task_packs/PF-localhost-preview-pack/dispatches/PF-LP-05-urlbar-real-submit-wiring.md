# PF-LP-05 — UrlBar real submit wiring

```yaml
status: candidate_task_draft_not_authority
pack: PF-localhost-preview-pack
cluster: PF-localhost-preview
dispatch_class: proof_mainline
open_after_state: successor_entry_ready
proof_kind: preview_only
human_gate: none
priority: blocker
inherits: ../../_PACK-DEFAULTS.md
```

## 0/5/6/7/9/10/11. Shared clauses
Inherits `_PACK-DEFAULTS.md`.


## 1. Goal
Wire `UrlBar.tsx` Create capture button to `createCapture()` so a valid manual URL emits loading, error, and capture_id states instead of static placeholder UI.

## 2-3. Output / dependencies
output: `apps/capture-station/src/features/url-bar/UrlBar.tsx`; depends: PF-LP-04

## 4. Files preview
```yaml
files_to_create:
  []
files_to_modify:
  - apps/capture-station/src/features/url-bar/UrlBar.tsx:onClick submit handler and state callbacks
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
  - apps/capture-station/src/features/vault-preview/**
```

## 8. T-PASS condition
Component tests prove click submit, disabled invalid URL, and error render paths.

### Required test assertions
1. Vitest verifies clicking Create capture calls `createCapture()` exactly once for a valid URL
2. Vitest verifies invalid URL keeps button disabled and does not call API
3. Vitest verifies API error renders operator-visible error text without claiming preview proof


## 12. Validation
```bash
pnpm --dir apps/capture-station typecheck
pnpm --dir apps/capture-station test -- UrlBar
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: emitted by UrlBar success callback
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-05-create-capture-click.json
  markdown_excerpt_lines: not_applicable_submit_only
  copy_action_log: not_applicable_submit_only
  download_filename: not_applicable_submit_only
```
