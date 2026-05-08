---
status: candidate north-star
---

# T-P1A-160 Lane A app scope repair note

## Purpose

This note names every `apps/**` path changed by PR `codex/pr264-lane-a-p3-preview-vertical-slice` so docs redline can verify that the Lane A preview-only implementation stayed inside explicit tracked scope.

## Boundary

- preview-only single-item operator flow
- no authority writeback
- no runtime tool execution
- no true vault write
- no browser automation approval
- no DB migration approval

## Explicit app paths

- `apps/capture-station/src/App.tsx`
- `apps/capture-station/src/App.module.css`
- `apps/capture-station/src/App.test.tsx`
- `apps/capture-station/src/components/Icon/Icon.tsx`
- `apps/capture-station/src/features/surfaces.smoke.test.tsx`
- `apps/capture-station/src/features/trust-trace/TrustTrace.tsx`
- `apps/capture-station/src/features/trust-trace/TrustTrace.test.tsx`
- `apps/capture-station/src/features/vault-commit/VaultCommit.tsx`
- `apps/capture-station/src/features/vault-commit/VaultCommitDryRunButton.tsx`
- `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx`
- `apps/capture-station/src/features/rewrite-output/RewriteOutputPreview.tsx`
- `apps/capture-station/src/features/rewrite-output/RewriteOutputPreview.module.css`
- `apps/capture-station/src/features/rewrite-output/RewriteOutputPreview.test.tsx`
- `apps/capture-station/src/fixtures/rewrite-output-v1/index.ts`
- `apps/capture-station/src/fixtures/rewrite-output-v1/ok-with-transcript.json`
- `apps/capture-station/src/fixtures/rewrite-output-v1/blocked-no-transcript.json`
- `apps/capture-station/src/fixtures/rewrite-output-v1/partial-rewrite.json`

## Why these paths moved

- `App.tsx` and `App.module.css` convert the old gallery shell into the dispatch-required single-screen workstation flow.
- `TrustTrace.tsx` reorders the top summary to error-path-first and consumes the merged Lane D lane-order token file.
- `RewriteOutputPreview.tsx` and its fixtures add a frontend-only `RewriteOutputV1` mock surface with truthful happy / blocked / partial states.
- `Icon.tsx` converts inline SVG sprite URLs into usable blob URLs so local browser verification no longer throws sprite same-origin console errors.
- `VaultCommitDryRunButton.tsx` and `VaultPreviewPanel.tsx` are compatibility shims for existing placeholder E2E contract tests; they do not approve runtime or true write.

## Non-goals

- `docs/current.md`
- `docs/task-index.md`
- `docs/decision-log.md`
- `services/**`
- `workers/**`
- `packages/**`
- Lane D owned component and token paths
