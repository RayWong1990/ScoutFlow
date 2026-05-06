# PF-META-01 Diff Summary — 2026-05-06

## 1. Old vs new line count

| path | code | old_lines | new_lines |
|---|---:|---:|---:|
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/dispatches/PF-C0-01-live-authority-readback-after-pr194.md` | `PF-C0-01R` | 100 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/dispatches/PF-C0-03-successor-entry-gate-memo.md` | `PF-C0-MERGED-03+04` | 97 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/dispatches/PF-C0-06-near-term-execution-matrix-20-30-mainline-only.md` | `PF-C0-06R` | 96 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/dispatches/PF-O1-01-overflow-registry-v0.md` | `PF-O1-01R` | 96 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-01-bridge-router-mount-in-create_app.md` | `PF-LP-01` | 98 | 37 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-02-bridge-preview-route-smoke-tests.md` | `PF-LP-02` | 97 | 37 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-03-vault-preview-environment-contract-note.md` | `PF-LP-03` | 97 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-04-capturestation-api-client-createcapture.md` | `PF-LP-04` | 97 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-05-urlbar-real-submit-wiring.md` | `PF-LP-05` | 96 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-06-capture-id-state-bridge.md` | `PF-LP-06` | 97 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-07-real-vault-preview-fetch-after-capture.md` | `PF-LP-07` | 98 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-08-vaultpreviewpanel-real-data-mode.md` | `PF-LP-08` | 96 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-09-markdown-copy-action.md` | `PF-LP-09` | 96 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-10-markdown-download-action.md` | `PF-LP-10` | 96 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-11-preview-error-and-blocked-state-ux.md` | `PF-LP-11` | 97 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-12-localhost-dev-run-instructions.md` | `PF-LP-12` | 97 | 36 |
| `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-13-backend-contract-validation-bundle.md` | `PF-LP-13` | 98 | 37 |

## 2. §1 Goal old/new comparison

| code | old goal | new goal |
|---|---|---|
| `PF-C0-01R` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Record a live readback table in `docs/research/post-frozen/live-authority-readback-after-pr194.md` that separates zip-derived fact, PR192-era readback, PR193/PR194 live GitHub fact, and current localhost code seams. |
| `PF-C0-MERGED-03+04` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Write one successor memo in `docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md` that joins PF cluster routing, preview-only localhost pass bar, and rejection of automatic `Dispatch177+` sequencing. |
| `PF-C0-06R` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Build `docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md` to classify all 80 authored tasks into near-term mainline, reservoir, and overflow with priority and open_after_state. |
| `PF-O1-01R` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Write `docs/research/post-frozen/overflow-registry-v0.md` with five overflow gate rows for true write, runtime tools, browser automation, DBvNext/migration, and full Signal Workbench. |
| `PF-LP-01` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Mount `scoutflow_api.bridge.router` inside `services/api/scoutflow_api/main.py:create_app()` so bridge health, vault-preview, and vault-commit dry-run routes are reachable while `bridge/config.py` keeps write disabled. |
| `PF-LP-02` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Add backend smoke tests that create a manual_url metadata_only capture and verify `/captures/{capture_id}/vault-preview` returns markdown while unset `SCOUTFLOW_VAULT_ROOT` fails loud. |
| `PF-LP-03` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Document `SCOUTFLOW_VAULT_ROOT` preview semantics in `docs/research/post-frozen/vault-preview-env-contract-2026-05-06.md` so unset, missing, and configured states are explicit before H5 consumes preview. |
| `PF-LP-04` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Add `createCapture(canonicalUrl)` to `apps/capture-station/src/lib/api-client.ts` so the H5 URL panel can call `/captures/discover` with fixed manual_url metadata_only payload. |
| `PF-LP-05` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Wire `UrlBar.tsx` Create capture button to `createCapture()` so clicking a valid manual URL emits loading, error, and capture_id states instead of static placeholder UI. |
| `PF-LP-06` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Introduce a bounded H5 state seam so `UrlBar` capture_id can flow to the preview panel without adding global authority state or direct storage writes. |
| `PF-LP-07` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Fetch `/captures/{capture_id}/vault-preview` after capture_id arrives so the H5 loop displays server-rendered markdown rather than placeholderPreview. |
| `PF-LP-08` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Refactor `VaultPreviewPanel.tsx` to render provided preview data with explicit empty/loading/error states so placeholderPreview is no longer the default proof surface. |
| `PF-LP-09` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Add a copy markdown action to `VaultPreviewPanel.tsx` that writes `body_markdown` to clipboard and logs success/failure state in the UI. |
| `PF-LP-10` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Add a download `.md` action to `VaultPreviewPanel.tsx` that generates a safe filename from capture_id and downloads the rendered markdown preview. |
| `PF-LP-11` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Render fail-loud UX for unset vault root, missing capture, and write-disabled commit states so localhost users can distinguish preview failure from runtime unlock. |
| `PF-LP-12` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Write `docs/research/post-frozen/localhost-preview-dev-runbook-2026-05-06.md` with backend/H5 run commands and evidence capture steps for the preview-only loop. |
| `PF-LP-13` | Keeps successor work bounded and prevents old candidate truth from becoming execution truth. | Add contract validation that compares mounted Bridge OpenAPI paths and vault-preview response shape against golden expectations while preserving write_disabled semantics. |

## 3. Sample before/after excerpts

### PF-LP-01

Before:
```markdown
## 1. Goal

Keeps successor work bounded and prevents old candidate truth from becoming execution truth.

```

After:
```markdown
## 1. Goal
Mount `scoutflow_api.bridge.router` inside `services/api/scoutflow_api/main.py:create_app()` so bridge health, vault-preview, and vault-commit dry-run routes are reachable while `bridge/config.py` keeps write disabled.
## 2-3. Output / dependencies
output: `services/api/scoutflow_api/main.py + tests/api/test_main_app_routers.py`; depends: none
```

### PF-C0-01R

Before:
```markdown
## 1. Goal

Keeps successor work bounded and prevents old candidate truth from becoming execution truth.

```

After:
```markdown
## 1. Goal
Record a live readback table in `docs/research/post-frozen/live-authority-readback-after-pr194.md` that separates zip-derived fact, PR192-era readback, PR193/PR194 live GitHub fact, and current localhost code seams.
## 2-3. Output / dependencies
output: `docs/research/post-frozen/live-authority-readback-after-pr194.md`; depends: none
```

### PF-O1-01R

Before:
```markdown
## 1. Goal

Keeps successor work bounded and prevents old candidate truth from becoming execution truth.

```

After:
```markdown
## 1. Goal
Write `docs/research/post-frozen/overflow-registry-v0.md` with five overflow gate rows for true write, runtime tools, browser automation, DBvNext/migration, and full Signal Workbench.
## 2-3. Output / dependencies
output: `docs/research/post-frozen/overflow-registry-v0.md`; depends: none
```
