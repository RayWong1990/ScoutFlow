---
title: PR261 validation and closeout erratum
status: reference storage
created_at: 2026-05-08
scope: PR261 validation readback and START-HERE/current anchor drift
---

# PR261 Validation And Closeout Erratum

## What PR261 Fixed

PR #261 fixed real issues:

- `docs/memory/**` taxonomy was moved back to `reference storage`.
- W2C runtime stale refresh guard was added.
- Vault write remained default-blocked.
- Status taxonomy guard was added.
- Prior errata for PR245, PR247-249, PR254, PR255, and PR257 were recorded.

## Validation Correction

PR261 body validation and CI readback did not agree:

- PR body listed `python tools/refresh-start-here.py --check --ref HEAD`.
- CI docs-smoke failed on START-HERE freshness.
- PR261 also left START-HERE/current anchored to PR259 / branch-HEAD context rather than PR261 merge truth.

PR262 repairs that closeout gap by aligning START-HERE and `docs/current.md` to PR #261 / `5902ecf`, repairing `refresh-start-here.py` check semantics, and recording this erratum.

## Boundary

This erratum does not invalidate the useful PR261 repairs. It only corrects the validation and closeout claim.

No runtime, migration, browser automation, vault true-write, DTO/schema, `PlatformResult`, or `WorkerReceipt` unlock is granted here.
