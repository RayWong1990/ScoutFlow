# ScoutFlow Bridge Route Group SPEC

> Status: candidate / spec only, no Python code
> Task: `T-P1A-045`
> PR slot: `PR #70`
> Scope: route-group specification only; no route registration, no handler code, no runtime approval

## 1. Purpose

This spec defines the future thin API route group for ScoutFlow's bridge layer. The bridge is not a separate process. It is a route group inside the existing API surface that turns validated capture state into:

- vault configuration visibility
- previewable markdown output
- gated vault commit

The bridge must stay thin. It reuses the existing capture / job / receipt / trust-trace truth instead of inventing a second orchestration layer.

## 2. Non-goals

- No Python implementation in this PR
- No route registration in `main.py`
- No storage schema change
- No `migrations/**`
- No direct write to `${SCOUTFLOW_VAULT_ROOT}` in this PR
- No `audio_transcript` unlock
- No browser automation

## 3. Route Surface

| Route | Method | Purpose | Response class |
|---|---|---|---|
| `/bridge/health` | `GET` | show bridge feature availability without mutating state | `BridgeHealthResponse` |
| `/bridge/vault/config` | `GET` | expose resolved vault config and fail-loud state | `BridgeVaultConfigResponse` |
| `/captures/{capture_id}/vault-preview` | `GET` | render the markdown preview for a capture without writing it | `BridgeVaultPreviewResponse` |
| `/captures/{capture_id}/vault-commit` | `POST` | gated future commit endpoint | `BridgeVaultCommitResponse` |

`vault-commit` remains spec-only in Wave 3B. The point of defining it now is to lock request/response shape and gate semantics before any write path exists.

## 4. Preconditions And State Gates

### 4.1 Global gates

- `SCOUTFLOW_VAULT_ROOT` must be resolved before preview/commit routes are considered available
- base PRD/SRD authority remains `PRD-v2` / `SRD-v2`
- `audio_transcript` remains blocked
- bridge routes must not bypass receipt/trust-trace evidence already recorded by the existing API

### 4.2 Capture-specific gates

`vault-preview` and `vault-commit` require all of the following:

1. capture exists
2. capture has metadata sufficient to build the raw markdown body
3. current capture state is allowed to produce a raw vault candidate
4. no path-escape or filename-sanitization violation is detected

### 4.3 Commit-specific extra gates

`vault-commit` adds stricter gates:

1. preview payload has already been materialized by bridge logic
2. frontmatter contract is valid for the raw 4-field template
3. operator explicitly requested commit
4. route is enabled by a future dispatch; until then, implementation must reject even if the spec exists

## 5. Data Contracts

### 5.1 `BridgeHealthResponse`

```json
{
  "bridge_available": false,
  "spec_version": "v0",
  "write_enabled": false,
  "blocked_by": ["bridge_not_implemented"]
}
```

### 5.2 `BridgeVaultConfigResponse`

```json
{
  "vault_root_resolved": false,
  "vault_root": null,
  "preview_enabled": false,
  "write_enabled": false,
  "frontmatter_mode": "raw_4_field",
  "error": {
    "code": "vault_root_unset",
    "message": "SCOUTFLOW_VAULT_ROOT is not configured"
  }
}
```

### 5.3 `BridgeVaultPreviewResponse`

```json
{
  "capture_id": "cap_xxx",
  "target_path": "${SCOUTFLOW_VAULT_ROOT}/00-Inbox/scoutflow-{id}-{slug}.md",
  "frontmatter": {
    "title": "Human readable title",
    "date": "2026-05-05",
    "tags": "调研/ScoutFlow采集",
    "status": "pending"
  },
  "body_markdown": "...",
  "warnings": []
}
```

### 5.4 `BridgeVaultCommitResponse`

```json
{
  "capture_id": "cap_xxx",
  "committed": false,
  "target_path": null,
  "error": {
    "code": "write_disabled",
    "message": "Bridge write path is not approved in the current phase"
  }
}
```

## 6. Error Model

Bridge routes do not reuse `PlatformResult`. Platform adapters answer platform-boundary questions. Bridge routes answer local bridge/vault boundary questions. The route group therefore uses a separate literal error namespace:

| BridgeErrorCode | Meaning |
|---|---|
| `bridge_not_implemented` | route exists only at spec level |
| `vault_root_unset` | `SCOUTFLOW_VAULT_ROOT` is missing |
| `capture_not_found` | capture id is unknown |
| `capture_state_blocked` | capture state cannot produce preview/commit |
| `metadata_missing` | required metadata is absent |
| `frontmatter_invalid` | raw 4-field output cannot be rendered safely |
| `path_escape_blocked` | resolved path escapes the allowed vault subtree |
| `write_disabled` | write route exists only as future contract |

The route group must return `BridgeErrorCode` in response payloads and, once implemented, in logs and operator-visible failures.

## 7. Security And Redaction Rules

- never echo cookies, raw tokens, or raw headers
- never return resolved local paths outside the allowed vault subtree
- preview may show rendered markdown body, but must not leak secret-bearing raw responses
- commit must always target `${SCOUTFLOW_VAULT_ROOT}/00-Inbox/`
- any future implementation must fail loud when `SCOUTFLOW_VAULT_ROOT` is unset

## 8. Test Matrix

Future implementation must cover at least these cases:

| Case | Expected result |
|---|---|
| `GET /bridge/health` before implementation | `bridge_available=false`, `write_enabled=false` |
| `GET /bridge/vault/config` with missing env | `BridgeErrorCode=vault_root_unset` |
| preview on unknown capture id | `BridgeErrorCode=capture_not_found` |
| preview on blocked capture state | `BridgeErrorCode=capture_state_blocked` |
| preview with bad frontmatter render | `BridgeErrorCode=frontmatter_invalid` |
| commit before write approval | `BridgeErrorCode=write_disabled` |
| commit path escape attempt | `BridgeErrorCode=path_escape_blocked` |

## 9. Carry-forward

- Wave 3B stops at spec/design/prototype boundaries
- actual vault write semantics belong to `services/api/scoutflow_api/vault/SPEC.md`
- any real bridge implementation requires a later dispatch after PR70, PR71, and PR72 converge
