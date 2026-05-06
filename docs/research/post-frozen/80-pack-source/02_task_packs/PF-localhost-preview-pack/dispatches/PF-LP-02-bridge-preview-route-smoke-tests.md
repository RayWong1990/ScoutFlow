# PF-LP-02 — Bridge preview route smoke tests

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
mount_does_not_unlock_write: `bridge/config.py:24,36` keeps `write_enabled=False`.

## 1. Goal
Add API smoke coverage that creates a manual_url metadata_only capture and verifies vault-preview returns markdown while unset `SCOUTFLOW_VAULT_ROOT` fails loud.

## 2-3. Output / dependencies
output: `tests/api/test_bridge_vault_preview_smoke.py`; depends: PF-LP-01

## 4. Files preview
```yaml
files_to_create:
  - tests/api/test_bridge_vault_preview_smoke.py
files_to_modify:
  []
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
  - services/api/scoutflow_api/bridge/config.py
  - services/api/scoutflow_api/bridge/vault_commit.py
```

## 8. T-PASS condition
Smoke tests prove configured preview, unset vault-root failure, and write-disabled invariants without creating files.

### Required test assertions
1. manual_url metadata_only capture fixture returns a real capture_id before preview fetch
2. configured `SCOUTFLOW_VAULT_ROOT` preview returns `body_markdown` with at least 20 lines in evidence excerpt
3. unset `SCOUTFLOW_VAULT_ROOT` returns fail-loud error and never sets `write_enabled=True`


## 12. Validation
```bash
pytest tests/api/test_bridge_vault_preview_smoke.py -q
python -c 'from scoutflow_api.main import create_app; assert "/captures/{capture_id}/vault-preview" in create_app().openapi()["paths"]'
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: created by API smoke fixture
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-02-preview-response.json
  markdown_excerpt_lines: >=20
  copy_action_log: not_applicable_backend_smoke
  download_filename: not_applicable_backend_smoke
```
