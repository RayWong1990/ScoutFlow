# PF-LP-10 — Markdown download action

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
Add a download `.md` action to `VaultPreviewPanel.tsx` that generates a safe filename from capture_id and downloads the rendered markdown preview.

## 2-3. Output / dependencies
output: `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx download action`; depends: PF-LP-08

## 4. Files preview
```yaml
files_to_create:
  []
files_to_modify:
  - apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx:download .md action and filename sanitizer
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
Tests prove download button availability, Blob payload, and safe filename generation.

### Required test assertions
1. Vitest verifies download button is disabled until real `body_markdown` exists
2. Vitest verifies generated Blob contains exact markdown text
3. Vitest verifies filename is `scoutflow-preview-{capture_id}.md` with unsafe characters removed


## 12. Validation
```bash
pnpm --dir apps/capture-station typecheck
pnpm --dir apps/capture-station test -- VaultPreviewPanel
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 12.5. Manual evidence step
- Open localhost in a normal browser tab
- Click download after real preview is visible
- Record downloaded filename and first 20 markdown lines in docs/research/post-frozen/evidence/PF-LP-10-download-action.md
- Do NOT write to RAW vault

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: from real preview prop
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-10-preview-before-download.json
  markdown_excerpt_lines: >=20
  copy_action_log: not_applicable_download_only
  download_filename: scoutflow-preview-{capture_id}.md
```
