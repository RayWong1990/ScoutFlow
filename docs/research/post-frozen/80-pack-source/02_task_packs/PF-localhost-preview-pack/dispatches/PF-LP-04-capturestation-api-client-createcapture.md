# PF-LP-04 — CaptureStation API client createCapture

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
Add `createCapture(canonicalUrl)` to `apps/capture-station/src/lib/api-client.ts` so the H5 URL panel can call `/captures/discover` with fixed manual_url metadata_only payload.

## 2-3. Output / dependencies
output: `apps/capture-station/src/lib/api-client.ts`; depends: PF-LP-01

## 4. Files preview
```yaml
files_to_create:
  []
files_to_modify:
  - apps/capture-station/src/lib/api-client.ts:createCapture() request/response types and method
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
  - apps/capture-station/src/features/url-bar/UrlBar.tsx
```

## 8. T-PASS condition
API client tests cover request body shape, error propagation, and capture_id return mapping.

### Required test assertions
1. Vitest verifies request body includes `platform=bilibili`, `source_kind=manual_url`, and `quick_capture_preset=metadata_only`
2. Vitest verifies success response exposes `capture_id` and `canonical_url` to caller
3. Vitest verifies non-2xx response preserves status, code, and payload in `CaptureStationApiError`


## 12. Validation
```bash
pnpm --dir apps/capture-station typecheck
pnpm --dir apps/capture-station test -- api-client
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 12.5. Manual evidence step
- Open localhost in a normal browser tab after frontend wiring lands
- Capture screenshot of create-capture success or error UI if this dispatch is manually reviewed
- Save manual note to docs/research/post-frozen/evidence/PF-LP-04-manual-note.md
- Do NOT use Playwright or browser automation

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: returned by mocked `/captures/discover` success response
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-04-create-capture-response.json
  markdown_excerpt_lines: not_applicable_api_client_only
  copy_action_log: not_applicable_api_client_only
  download_filename: not_applicable_api_client_only
```
