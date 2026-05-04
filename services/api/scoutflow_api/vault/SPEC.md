# ScoutFlow VaultWriter Contract SPEC

> Status: candidate / spec only, no Python code
> Task: `T-P1A-047`
> PR slot: `PR #72`
> Scope: vault contract only; no runtime write, no handler code, no migration

## 1. Purpose

This spec defines the future VaultWriter contract for ScoutFlow. It answers one narrow question: when a capture is ready to emit a raw markdown candidate, what exact contract governs target path, frontmatter, idempotency, and fail-loud behavior?

The VaultWriter is not a generic knowledge exporter. It is a thin raw-material emitter into the user's existing PARA/Claudian vault flow.

## 2. Hard boundary

The only allowed target subtree is:

`"${SCOUTFLOW_VAULT_ROOT}/00-Inbox/"`

This spec does not approve direct writes to:

- `01-Wiki/`
- `02-Raw/`
- `03-Output/`
- any repo-local mirror vault

## 3. `SCOUTFLOW_VAULT_ROOT`

### 3.1 Required behavior

- `SCOUTFLOW_VAULT_ROOT` must be explicit at SRD/implementation level
- missing env is a hard failure
- no hidden fallback to another path
- no auto-creating an alternative root under the repo

### 3.2 Fail-loud rule

If `SCOUTFLOW_VAULT_ROOT` is unset, future implementation must return a bridge/vault-layer error immediately.

Example response intent:

```json
{
  "code": "vault_root_unset",
  "message": "SCOUTFLOW_VAULT_ROOT is not configured"
}
```

## 4. Raw frontmatter contract

The raw export contract is the minimal 4-field template proven by the frontmatter compatibility scan:

```yaml
---
title: "<human-readable title>"
date: 2026-05-05
tags: 调研/ScoutFlow采集
status: pending
---
```

Field rules:

- `title`: human-readable string
- `date`: `YYYY-MM-DD`
- `tags`: single string value, not YAML list
- `status`: `pending`

Non-goals:

- no `domain`
- no `type`
- no `source`
- no `priority`
- no article-level wiki fields

## 5. Target path and filename

Recommended target shape:

`"${SCOUTFLOW_VAULT_ROOT}/00-Inbox/scoutflow-{capture_id}-{slug}.md"`

Filename rules:

- prefix stays `scoutflow-`
- `capture_id` remains the stable identity anchor
- `slug` is sanitized from title
- no path traversal
- no operator-provided raw path fragments

## 6. Path containment

Future implementation must validate path containment before any write attempt.

Minimum contract:

1. resolve vault root
2. resolve candidate target path
3. verify target path is inside resolved `00-Inbox/`
4. reject if escaped, absolute in wrong subtree, or symlinked outside

This is a vault-layer contract, not a platform-layer result. Errors therefore use the vault/bridge namespace rather than `PlatformResult`.

## 7. Idempotency

VaultWriter must be idempotent at the file-identity level.

Minimum expectations:

- same `capture_id` + same slug should not create duplicate sibling files silently
- repeated preview should produce stable content for the same upstream state
- repeated commit should either:
  - confirm same file already exists with same content
  - or fail with explicit conflict information

This spec does not decide whether the final implementation uses overwrite, no-op, or compare-and-skip. It only locks that duplicate silent fan-out is forbidden.

## 8. Error namespace

VaultWriter errors use the bridge/vault namespace, not `PlatformResult`.

Recommended literals:

| Code | Meaning |
|---|---|
| `vault_root_unset` | missing `SCOUTFLOW_VAULT_ROOT` |
| `vault_target_blocked` | write path disabled in current phase |
| `frontmatter_invalid` | raw 4-field contract cannot be rendered safely |
| `path_escape_blocked` | resolved path escapes the allowed inbox subtree |
| `vault_conflict` | idempotency/file conflict detected |

`BridgeErrorCode` is the correct family for bridge/vault local failures. `PlatformResult` remains reserved for adapter/platform boundary outcomes.

## 9. Test matrix

Future implementation must cover:

| Case | Expected |
|---|---|
| env unset | `vault_root_unset` |
| target path escapes inbox | `path_escape_blocked` |
| invalid date/tags/status render | `frontmatter_invalid` |
| duplicate same-file commit | explicit idempotent result or `vault_conflict` |
| commit while write lane still gated | `vault_target_blocked` |

## 10. Carry-forward

- bridge route-group spec defines when preview/commit routes exist
- this vault spec defines what preview/commit must obey once implemented
- real write code remains blocked until a later dispatch after Wave 3B spec/design/prototype lanes converge
