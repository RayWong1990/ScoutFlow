---
title: PR262 consistency full repair scope note
status: reference storage
created_at: 2026-05-08
scope: PR226-PR261 consistency full repair
---

# PR262 Consistency Full Repair Scope Note

## Scope

This PR is a bounded governance + UI truth repair for PR226-PR261 consistency gaps. It is not a new feature lane and does not open an active product slot.

## Allowed Paths

- `docs/current.md`
- `docs/task-index.md`
- `docs/decision-log.md`
- `docs/00-START-HERE.md`
- `docs/research/repairs/**`
- `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/**`
- `tools/refresh-start-here.py`
- `tools/check-docs-redlines.py`
- `tests/tools/test_refresh_start_here.py`
- `tests/tools/test_check_docs_redlines.py`
- `.github/workflows/docs-check.yml`
- `apps/capture-station/src/features/trust-trace/lanes/ErrorPathLane.tsx`
- `apps/capture-station/src/features/trust-trace/lanes/ErrorPathLane.test.tsx`
- `apps/capture-station/src/features/trust-trace/lanes/GraphLane.tsx`
- `apps/capture-station/src/features/trust-trace/lanes/GraphLane.test.tsx`
- `apps/capture-station/src/features/trust-trace/lanes/TimelineLane.tsx`
- `apps/capture-station/src/features/trust-trace/lanes/TimelineLane.test.tsx`

## Forbidden Paths

- `services/api/**`
- `services/api/migrations/**`
- `workers/**`
- `packages/**`
- `data/**`
- `referencerepo/**`
- DTO/schema files
- `PlatformResult` enum
- `WorkerReceipt` schema
- runtime tool enablement files
- true vault write enablement files
- browser automation enablement files

## Why App Path Changes Are Allowed

The app changes are limited to the PR255 W1B trust-trace lane truth bug repair:

- `ErrorPathLane` must not classify failed/error audit `platform_result` as clear just because evidence path and artifact count exist.
- `GraphLane` must use `media_audio.status` and `audio_transcript` together for media node tone.
- `GraphLane` and `TimelineLane` must not dump future raw `audio_transcript` into UI; they only show blocked / not_present / preview / truncated text.

No backend, DTO, schema, service, worker, migration, runtime tool, vault true-write, or browser automation behavior changes are included.

## Validation Commands

- `python -m pytest tests/tools/test_refresh_start_here.py tests/tools/test_check_docs_redlines.py -q`
- `python tools/check-docs-redlines.py`
- `python tools/check-docs-redlines.py --full-status-scan`
- `python tools/check-secrets-redlines.py`
- `python tools/refresh-start-here.py --check`
- `python tools/refresh-start-here.py --check --ref HEAD`
- `pnpm --dir apps/capture-station test -- ErrorPathLane GraphLane TimelineLane`
- `pnpm --dir apps/capture-station exec vitest --run src/features/trust-trace/lanes/ErrorPathLane.test.tsx src/features/trust-trace/lanes/GraphLane.test.tsx src/features/trust-trace/lanes/TimelineLane.test.tsx`
- `pnpm --dir apps/capture-station typecheck`
- `pnpm --dir apps/capture-station lint`
- `git diff --check`

## Known Not Fixed

- No true runtime is opened.
- No migration is opened.
- No browser automation is opened.
- No vault true write is opened.
- No PR262 merge truth is assumed until this PR is created and merged.
