---
title: MASTER Decision Atlas
status: candidate / not-authority
authority: not-authority
created_at: 2026-05-07
---

# MASTER Decision Atlas

This zip is a direct-delivery candidate atlas for U15. It packages **80 merged PR decision cards**, **20 decision patterns**, **5 timelines**, **7 topic views**, **1 amend trail map**, **11 cluster indexes**, **5 legacy decision hypotheses**, and supporting metadata.

## What this atlas is

It is a retrieval layer over PR decisions. Each PR card is intended to answer the practical question: “what did we decide, what boundary did we preserve, and what should future work check before claiming success?” The atlas is not canonical authority. It does not modify `docs/decision-log.md`, PRD/SRD amendments, or any repository file. It is a candidate memory artifact that can be audited and selectively promoted later.

## Strongest verified anchors

- #231: Run-1 amendment ledger + external audits; `REJECT_AS_SCOPE_DRIFT` with `amend_and_proceed`.
- #239: Run-2 receipt traceability amendment; synthetic UAT/readback downgraded to `partial` and SHA/coverage topology clarified.
- #240: Run-3+4 compressed closeout; C1 pass, C2 partial, C4 blocked, Run-5 pending PF-V handoff.

## Coverage

The package uses recent live GitHub PR metadata for #161-#240, excluding #229 because it was closed but not merged, and adds PR #1 as bootstrap. That yields exactly 80 merged PR decision cards. The local Post176 audit pack is included as context, especially for Dispatch127-176 and Wave 4-5, but the atlas does not claim full 240+ coverage.

## How to read it

Start with `09_inventory/PR-INVENTORY-LOCK.md`, then open `05_amend_trail/AMEND-TRAIL-MAP.md`, then read the three anchor PR cards (#231, #239, #240). For topic-based questions, use `04_topics/`. For recurring decision shapes, use `02_patterns/`. For gaps and honesty status, use `00_META/SOURCE-COVERAGE-MATRIX.md` and `00_META/TRUTHFUL-STDOUT.yaml`.

## Non-negotiable caveats

- U10 runbook registry was not loaded.
- U11 anti-pattern registry was not loaded; no AP IDs were invented.
- ContentFlow legacy decisions are candidate hypotheses only.
- Diff-level review is not included for every implementation-bearing PR.
- This package is useful now, but still requires human audit before canonical promotion.
