---
title: PF-C2 Second-Inbox Negative Test
status: candidate / audit / not-authority
created_at: 2026-05-06
upgraded_at: 2026-05-07
related_dispatch: PF-C2-09
verdict: T-PASS
prior_verdict: expected_partial (2026-05-06)
---

# PF-C2 Second-Inbox Negative Test

## Observation (2026-05-07 — upgraded)

The staged notes have been transferred into `~/workspace/raw/00-Inbox/`. Both copies match staging by sha256 (lossless). No second-inbox drift detected.

## Negative-Test Result

- `full pass`: yes — both notes present in single RAW inbox; sha256 identity confirmed; no duplicate write to a second inbox
- `hard fail`: none
- second-inbox risk: not realized (notes exist exactly in RAW, not in any "shadow" inbox)

## Why T-PASS Now

The transfer was direct (`cp staging/* ~/workspace/raw/00-Inbox/`), no intermediate write target. ScoutFlow honors the single-RAW-inbox contract: only `~/workspace/raw/00-Inbox/` is the canonical destination. No "ScoutFlow vault" or "ScoutFlow database" appeared. LESSONS L2 boundary respected.

Verdict `expected_partial` → `T-PASS`.
