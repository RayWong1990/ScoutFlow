# Bridge OpenAPI Contract Notes

> Status: research-only / not-authority / not-runtime-approval
> Task: `T-P1A-085`
> Scope: bridge OpenAPI contract hardening after route-group scaffold, health/config handlers, preview, dry-run commit, and bridge-local error helper all landed on `main`

## 1. Why this note exists

Wave 4 Batch 2 needed one last contract pass that was narrower than "the route works":

- freeze the four bridge paths that now exist in code
- freeze which response schemas each path exposes in OpenAPI
- freeze that preview / commit error responses stay on `ErrorResponse`, not `PlatformResult`
- record what still remains downstream and is not unlocked by this pass

This is a contract note, not a runtime approval note.

## 2. Paths locked by the snapshot test

The snapshot contract now covers these paths:

| Path | Method | Success schema |
|---|---|---|
| `/bridge/health` | `GET` | `BridgeHealthResponse` |
| `/bridge/vault/config` | `GET` | `BridgeVaultConfigResponse` |
| `/captures/{capture_id}/vault-preview` | `GET` | `BridgeVaultPreviewResponse` |
| `/captures/{capture_id}/vault-commit` | `POST` | `BridgeVaultCommitResponse` |

For preview and commit, the `404 / 409 / 503` error branches are explicitly pinned to `ErrorResponse`.

## 3. Contract details pinned here

- `BridgeErrorCode` remains a bridge-local namespace and keeps at least:
  - `write_disabled`
  - `capture_not_found`
  - `vault_root_unset`
- `BridgeVaultCommitResponse` keeps an explicit `dry_run: boolean` flag
- the bridge route group stays separate from `PlatformResult`
- no change in this pass expands route semantics beyond the already landed handler logic

## 4. What this pass still does not approve

- no vault write
- no migration
- no browser automation
- no BBDown live runtime
- no ASR / `audio_transcript` runtime unlock
- no frontend visual gate closure

## 5. Downstream dependency still outside this pass

The route contract is now harder, but visual and operator acceptance are still downstream work.
In particular, the later 5-Gate visual / CI harness lane after the H5 mock remains separate.
This note does not claim that the H5 surface is visually approved or that bridge/H5 integration has passed human review.
