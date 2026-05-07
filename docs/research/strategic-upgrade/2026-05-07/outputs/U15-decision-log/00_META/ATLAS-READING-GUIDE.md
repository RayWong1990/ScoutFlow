---
title: Atlas Reading Guide
status: candidate / not-authority
authority: not-authority
---

# Atlas Reading Guide

Use this package as a decision-memory layer, not as a replacement for GitHub or canonical documents. The most efficient path is: inventory first, amendment trail second, anchor PRs third, topic views fourth, and pattern library last. That order keeps the reader from overfitting to a single dramatic amendment before seeing the broader PR sequence.

## 1. Start with inventory

Open `09_inventory/PR-INVENTORY-LOCK.md`. Confirm the selected PR set and notice that #229 is intentionally excluded because it was closed but not merged. This matters: the package is designed around merged decision cards. A closed unmerged PR can be useful evidence, but it should not be counted as a merged decision unless a later PR adopts its content.

## 2. Read the amendment trail

Open `05_amend_trail/AMEND-TRAIL-MAP.md`. The map is the fastest way to understand why #231, #239, and #240 are treated as anchors. #231 exposes Run-1 scope drift and records amend-and-proceed. #239 repairs Run-2 traceability and downgrades over-strong evidence claims. #240 preserves mixed results in a compressed single-PR closeout. These three cards explain the governance style of the whole package: keep useful work, but narrow claims when evidence is partial.

## 3. Read anchor PR cards

Open the PR decision files for #231, #239, and #240. Do not read them as blame documents. Read them as correction documents. The important distinction is introduced versus exposed. A later amendment often exposes a risk created by an earlier implementation or receipt. The atlas preserves this so the project does not accidentally blame the repair PR for the original condition.

## 4. Use topic views for questions

If the question is about preview, vault, createCapture, PF-GLOBAL controls, PF-C3 object handling, or authority sync, use `04_topics/`. Topic views are built for retrieval. They are less chronological than timelines and more useful when you want to answer “what did we already decide about this surface?”

## 5. Use patterns for future prompts

The files in `02_patterns/` are designed to become reusable prompt vocabulary. Examples include `amend_and_proceed`, `boundary_preservation`, `candidate_not_authority_frontmatter`, `truthful_stdout_contract`, `preview_only_before_write`, and `partial_signal_preservation`. A future cloud prompt can ask a model to apply these patterns without reconstructing the entire ScoutFlow history from scratch.

## 6. Respect blocked links

The package does not invent U11 anti-pattern IDs or U10 runbook IDs. The right workflow is to load those registries later and then add exact links. A missing registry should remain a gap, not a hallucinated mapping. This is also why ContentFlow legacy files are placed under `07_legacy/` and marked as candidate hypotheses.

## 7. Promotion workflow

To promote any part of this atlas, use a separate PR. The promotion PR should identify the exact source file, the exact section to promote, the target canonical file, and the reason the claim is now stronger than candidate memory. For example, a PR card can support a decision-log entry, but the card itself should not silently become the decision log. This separation keeps the single-writer and source-of-record discipline intact.

## 8. Audit workflow

A useful human audit can be small. Pick one cluster index, check five PR cards against GitHub, inspect the amend-chain fields, and verify that the introduced/exposed attribution is fair. Then repeat for the anchor amendments. The package is structured so partial audit still improves confidence.

## 9. Red flags

Red flags include: a PR card that says runtime when the PR body says preview-only; an anti-pattern ID that is not present in U11; a legacy claim treated as canonical without the ContentFlow source; a compressed closeout that hides partial status; and a candidate doc that appears to modify authority state without a separate authority-sync PR.

## 10. Expected next best step

The next best step is not to rewrite this package. It is to run a focused U15-A evidence lock against the full PR ledger, U10, U11, docs/decision-log.md, PRD/SRD amendments, and ContentFlow L1. Then compare that evidence lock against this zip. Keep the parts that survive, demote the parts that are too broad, and add missing links where registry evidence exists.


## 11. Minimal operator checklist

Before using this atlas for a future planning prompt, apply this minimal operator checklist. Confirm the target cluster. Confirm whether the desired output is evidence, candidate planning, authority wording, implementation, receipt repair, or amendment. Confirm whether the action requires a human gate. Confirm whether a source-of-record write is being requested. Confirm whether the work could accidentally imply runtime approval, write approval, migration approval, browser automation approval, or vendor acceptance. Confirm whether a later amendment already downgraded the claim. Confirm whether the atlas card is enough or whether the live PR body and diff must be reopened. Confirm whether the decision should remain candidate-only. Confirm whether a missing U10 or U11 registry link would change the risk reading. Confirm whether ContentFlow legacy reasoning is being used as a hypothesis or as verified source. This checklist is intentionally plain because the most common failure is not complex reasoning; it is skipping the boundary readback before generating confident prose.


Final reminder: keep every future promotion explicit, reversible, source-cited, scope-bounded, human-reviewed, registry-linked, and honest about partial evidence.


Audit confidence increases only when evidence, boundary, authority, amendment, receipt, registry, and downstream dependency all agree.


Keep claims narrow. Keep receipts visible. Keep promotion separate.
