# PF-LP-01 — Bridge router mount in create_app

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
Mount `scoutflow_api.bridge.router` inside `services/api/scoutflow_api/main.py:create_app()` so bridge health, vault-preview, and vault-commit dry-run routes are reachable while write remains disabled.

## 2-3. Output / dependencies
output: `services/api/scoutflow_api/main.py + tests/api/test_main_app_routers.py`; depends: PF-C0-MERGED-03+04, PF-O1-01R

## 4. Files preview
```yaml
files_to_create:
  - tests/api/test_main_app_routers.py
files_to_modify:
  - services/api/scoutflow_api/main.py:create_app() import bridge router and app.include_router(bridge_router)
  - services/api/scoutflow_api/bridge/schemas.py:BridgeVaultCommitResponse add write_enabled: Literal[False]
  - services/api/scoutflow_api/bridge/vault_commit.py:dry-run response sets write_enabled=False
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
```

## 8. T-PASS condition
OpenAPI exposes `/bridge/health`, `/captures/{capture_id}/vault-preview`, and `/captures/{capture_id}/vault-commit`; no route or response introduces `write_enabled=True`.

`tests/api/test_main_app_routers.py` MUST include at least 3 explicit assertions; empty tests or tests lacking these assertions count as `REJECT_AS_DOCS_ONLY_PROOF`.

### Required test assertions
1. bridge router is included in `create_app().routes` using path-based assertions for all three mounted paths
2. `/bridge/health` returns HTTP 200 and a body whose `blocked_by` includes `write_disabled`
3. `/captures/{capture_id}/vault-commit` response schema includes `write_enabled` and dry-run response resolves it to `false`


## 12. Validation
```bash
pytest tests/api/test_main_app_routers.py -q
python -c 'from scoutflow_api.main import create_app; app=create_app(); paths={r.path for r in app.routes}; assert "/bridge/health" in paths; assert "/captures/{capture_id}/vault-preview" in paths; assert "/captures/{capture_id}/vault-commit" in paths'
python -c 'from scoutflow_api.main import create_app; schema=create_app().openapi(); assert "/bridge/health" in schema["paths"]; assert "/captures/{capture_id}/vault-preview" in schema["paths"]; assert "/captures/{capture_id}/vault-commit" in schema["paths"]'
python tools/check-docs-redlines.py && python tools/check-secrets-redlines.py && git diff --check
```

## 13. Evidence shape
```yaml
proof_kind: preview_only
evidence_shape:
  capture_id: required from `/captures/discover` or fixture capture row
  fetch_response_path: docs/research/post-frozen/evidence/PF-LP-01-fetch-response.json
  markdown_excerpt_lines: >=20
  copy_action_log: docs/research/post-frozen/evidence/PF-LP-01-copy-action.log
  download_filename: scoutflow-preview-{capture_id}.md
```
