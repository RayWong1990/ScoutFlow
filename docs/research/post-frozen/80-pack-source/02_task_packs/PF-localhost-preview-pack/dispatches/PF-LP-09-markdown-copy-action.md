# PF-LP-09 — Markdown copy action

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
Add a copy markdown action to `VaultPreviewPanel.tsx` that writes `body_markdown` to clipboard and logs success or failure state in the UI.

## 2-3. Output / dependencies
output: `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx copy action`; depends: PF-LP-08

## 4. Files preview
```yaml
files_to_create:
  []
files_to_modify:
  - apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx:copy button and clipboard status state
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
  - browser automation
```

## 8. T-PASS condition
Tests prove copy button availability, clipboard write payload, and failure-state rendering.

### Required test assertions
1. Vitest verifies copy button is disabled until real `body_markdown` exists
2. Vitest verifies clicking copy sends exact `body_markdown` to `navigator.clipboard.writeText`
3. Vitest verifies clipboard rejection renders failure state without hiding markdown


## 12. Validation
```bash
pnpm --dir apps/capture-station typecheck
pnpm --dir apps/capture-station test -- VaultPreviewPanel
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 12.5. Manual evidence step
- Open localhost in a normal browser tab
- Click copy after real preview is visible
- Record browser-visible copy status in docs/research/post-frozen/evidence/PF-LP-09-copy-action.log
- Do NOT use Playwright or browser automation

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: from real preview prop
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-09-preview-before-copy.json
  markdown_excerpt_lines: >=20
  copy_action_log: docs/research/post-frozen/evidence/PF-LP-09-copy-action.log
  download_filename: not_applicable_copy_only
```
