---
title: Vault preview environment contract
status: candidate / research / not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-06
related_dispatch: PF-LP-03
---

# Vault preview environment contract

> Scope: document current preview semantics around `SCOUTFLOW_VAULT_ROOT` before the localhost preview loop consumes Bridge routes. This file does not approve true write, runtime, or browser automation.

## contract_table

| state | expected_response | operator_message |
|---|---|---|
| `unset_state` | `GET /bridge/vault/config` returns `vault_root_resolved=false`, `preview_enabled=false`, `write_enabled=false`, `error.code=vault_root_unset`; preview fetch should fail loud rather than silently degrade. | Set `SCOUTFLOW_VAULT_ROOT` explicitly before treating preview as available. Missing env is a contract failure, not a soft warning. |
| `invalid_or_missing_root_state` | Current seam distinguishes only empty vs non-empty env at config time. A non-empty but wrong path may still be echoed by config as resolved, while write remains disabled and no true-write path opens. | Do not interpret a non-empty `vault_root` echo as proof that the filesystem target exists, is writable, or is approved for commit. Additional proof remains future work. |
| `configured_preview_state` | With a non-empty env value, config echoes the resolved path, keeps `frontmatter_mode=raw_4_field`, and preserves `write_enabled=false`; preview route may render a target path under `${SCOUTFLOW_VAULT_ROOT}/00-Inbox/`. | Preview readiness means path resolution is present for preview shaping only. It does not upgrade the lane from preview-only to commit-approved. |

## unset_state

- Source seam:
  - `services/api/scoutflow_api/bridge/config.py`
  - `services/api/scoutflow_api/bridge/vault_preview.py`
  - `services/api/scoutflow_api/vault/writer.py`
- Current fail-loud behavior:
  - empty or missing `SCOUTFLOW_VAULT_ROOT` returns `vault_root_unset`
  - `write_enabled` remains `false`
  - preview route returns an explicit error instead of a silent placeholder path

## invalid_or_missing_root_state

- Current contract is intentionally narrow:
  - bridge config checks whether the env var is present and non-empty
  - it does not prove the referenced filesystem path already exists
  - it does not prove write approval, writability, or downstream RAW acceptance
- Result:
  - "configured" in the current seam means "string resolved", not "runtime-approved vault target"
  - any future stronger path validation belongs to a later dispatch, not to this preview-only contract note

## configured_preview_state

- When `SCOUTFLOW_VAULT_ROOT` is set:
  - bridge config echoes the path
  - `preview_enabled` can become truthy when the preview module exists
  - preview target path stays under `00-Inbox`
  - frontmatter mode stays `raw_4_field`
- The preview shape is bounded to preview rendering and dry-run semantics only.

## no_true_write_boundary

- `SCOUTFLOW_VAULT_ROOT` being configured does **not** unlock true vault write.
- Hard boundary remains:
  - `services/api/scoutflow_api/bridge/config.py` keeps `write_enabled=false`
  - current commit path is still dry-run / blocked by contract
  - no migration, browser automation, or runtime tool approval is implied by this env note
- Verdict: this file is an environment contract note for preview-only localhost work, not a write gate and not a runtime approval artifact.
