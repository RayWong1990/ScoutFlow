# PF-LP-13 — Backend contract validation bundle

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
mount_does_not_unlock_write: `bridge/config.py:24,36` keeps `write_enabled=False`.

## 1. Goal
Add contract validation that compares mounted Bridge OpenAPI paths and vault-preview / vault-commit response shapes against golden schema expectations while preserving write-disabled semantics.

## 2-3. Output / dependencies
output: `tests/contracts/test_bridge_openapi_golden_contract.py + tests/contracts/golden/bridge-openapi-2026-05-06.json`; depends: PF-LP-01, PF-LP-02

## 4. Files preview
```yaml
files_to_create:
  - tests/contracts/test_bridge_openapi_golden_contract.py
  - tests/contracts/golden/bridge-openapi-2026-05-06.json
files_to_modify:
  []
files_will_NOT_touch:
  - docs/current.md
  - AGENTS.md
  - docs/task-index.md
  - docs/decision-log.md
  - services/api/migrations/**
  - services/api/scoutflow_api/bridge/config.py
  - workers/**
  - packages/**
  - data/**
  - referencerepo/**
```

## 8. T-PASS condition
1. `GET /bridge/health` exists in OpenAPI with expected status `200`; response schema must include `bridge_available`, `spec_version`, `write_enabled`, and `blocked_by`; golden diff command: `python -m pytest tests/contracts/test_bridge_openapi_golden_contract.py -q --golden tests/contracts/golden/bridge-openapi-2026-05-06.json`.
2. `GET /captures/{capture_id}/vault-preview` exists in OpenAPI with expected status `200`; response schema must include `capture_id`, `target_path`, `frontmatter`, `body_markdown`, and `warnings`; golden diff command: same golden pytest command.
3. `POST /captures/{capture_id}/vault-commit` exists in OpenAPI with expected status `200`; response schema must include `capture_id`, `dry_run`, `committed`, `write_enabled`, `target_path`, and `error`; golden diff command: same golden pytest command.
4. Vault-preview error responses include statuses `404` and `409`; error schema must include `code` and `message`; golden diff command: same golden pytest command.
5. All bridge/config and dry-run commit schemas keep `write_enabled=false`; response schema field list must contain `write_enabled` and contract test must assert it resolves to false in dry-run mode; golden diff command: same golden pytest command.

### Required test assertions
1. Pytest compares generated OpenAPI JSON with `tests/contracts/golden/bridge-openapi-2026-05-06.json` and fails on path drift.
2. Pytest asserts vault-preview and vault-commit response fields exactly include the listed required fields.
3. Pytest asserts every `write_enabled` field exposed by health/config/commit resolves to `False` and never `True`.

## 12. Validation
```bash
pytest tests/contracts/test_bridge_openapi_golden_contract.py -q
python -m pytest tests/contracts/test_bridge_openapi_golden_contract.py -q --golden tests/contracts/golden/bridge-openapi-2026-05-06.json
python -c 'from scoutflow_api.main import create_app; schema=create_app().openapi(); assert "/bridge/health" in schema["paths"]; assert "/captures/{capture_id}/vault-preview" in schema["paths"]; assert "/captures/{capture_id}/vault-commit" in schema["paths"]'
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: contract fixture capture_id
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-13-openapi-contract.json
  markdown_excerpt_lines: ">=20 via vault-preview schema fixture"
  copy_action_log: not_applicable_backend_contract
  download_filename: not_applicable_backend_contract
  golden_schema_path: tests/contracts/golden/bridge-openapi-2026-05-06.json
```
