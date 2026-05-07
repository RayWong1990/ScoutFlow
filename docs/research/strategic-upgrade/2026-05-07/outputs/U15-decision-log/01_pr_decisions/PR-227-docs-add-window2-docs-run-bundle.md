---
decision_id: "PR-227-docs-add-window2-docs-run-bundle"
status: "candidate / decision-atlas / not-authority"
authority: "not-authority"
pr_number: 227
pr_exists_verified: true
merged: true
pr_url: "https://github.com/RayWong1990/ScoutFlow/pull/227"
pr_title: "docs: add window2 docs run bundle"
merged_at: "2026-05-06T09:57:32Z"
cluster: "C05 PF-LP Run-2 / Window-2 / PF-GLOBAL / PF-C3"
decision_kind: "other"
impact_radius: "single-cluster"
introduced_or_exposed: "introduced"
attribution_confidence: "medium-high"
source_depth: "live GitHub PR metadata and PR body summary inspected in this run"
amend_chain: {"amends": [], "amended_by": [], "related_prs": []}
linked_patterns: ["dispatch_lineage"]
linked_anti_patterns: []
canonical_decision_log_unchanged: true
---

# PR #227 — docs: add window2 docs run bundle

## Evidence snapshot

| Field | Value |
|---|---|
| PR | [#227](https://github.com/RayWong1990/ScoutFlow/pull/227) |
| Merged at | `2026-05-06T09:57:32Z` |
| Cluster | `C05 PF-LP Run-2 / Window-2 / PF-GLOBAL / PF-C3` |
| Decision kind | `other` |
| Impact radius | `single-cluster` |
| Introduced/exposed | `introduced` |
| Attribution confidence | `medium-high` |

## Mission

This card turns the merged PR into a searchable decision object. It is not the canonical PR body, not a replacement for `docs/decision-log.md`, and not a claim that every downstream consequence has been proven. Its job is to preserve enough context to answer: what changed, why this boundary was acceptable, what was not promoted, and which later amendments or patterns should be checked.

## Context

Added RUN-W2 report, diff bundle, and final checkpoint for Window 2 docs run.

The context is interpreted conservatively. If the PR body says docs-only, preview-only, candidate-only, or no authority writeback, this atlas keeps those words as governing constraints. If the PR touches implementation seams or tests, the card treats the work as bounded and checks whether a later amendment exposed scope drift. This is especially important for PF-LP and post-frozen runs because several PRs are not isolated: they form chains of preview, receipt, coverage, and amendment truth.

## Options considered

The decision space for this PR can be reconstructed as three bounded choices. Option A was to defer the item and keep the previous surface unchanged. Option B was to land the described candidate or evidence artifact but keep it explicitly non-authority. Option C was to promote the work as runtime/canonical truth. The selected posture is closest to Option B: land the smallest useful artifact, preserve the boundary language, and leave promotion to a later authority or amendment gate.

## Chosen decision

The chosen decision was to merge **docs: add window2 docs run bundle** as a other item inside **C05 PF-LP Run-2 / Window-2 / PF-GLOBAL / PF-C3**. The operational payload, as observed from the PR metadata/body summary, was: Added RUN-W2 report, diff bundle, and final checkpoint for Window 2 docs run.

## Rationale

The rationale is not simply “ship the file”. In ScoutFlow terms, the PR turns a loose memory item into a reviewable artifact while maintaining candidate/not-authority separation. This is why the atlas marks the impact as `single-cluster` and attribution as `introduced`. When the PR introduced a new candidate, the value was future-searchability and controlled continuation. When it exposed a gap, the value was traceability: a later auditor can see which claim was narrowed, which evidence was downgraded, and which boundary remained intact. The recurring design choice is to prefer an explicit partial truth over an implicit complete-sounding claim.

## Outcome and downstream signal

The immediate outcome is a merged checkpoint in the PR ledger at `2026-05-06T09:57:32Z`. Downstream, this card should be read together with linked patterns `dispatch_lineage` and with the amend chain `{'amends': [], 'amended_by': [], 'related_prs': []}`. No U11 anti-pattern ID is attached because the U11 registry was not available in this build; inventing AP IDs would make the atlas less useful. The package therefore records a cross-link gap rather than pretending the registry was loaded.



## Lessons

Lessons for future dispatches: keep source-of-record changes separate from candidate docs; name blocked lanes directly; avoid treating preview-only proof as runtime approval; preserve `write_enabled=false` when that is the governing contract; and record whether a PR introduced a structure or merely exposed a flaw. This PR is useful to grep because it binds title, merged date, cluster, decision kind, and outcome in one file.

## Cross-links

- Cluster index: `06_indexes/`
- Pattern files: `02_patterns/PATTERN-dispatch_lineage.md`
- Amend chain: `{"amends": [], "amended_by": [], "related_prs": []}`
- U11 anti-pattern cross-link: blocked because U11 registry was not loaded; see `08_crosslinks/LINKED-ANTI-PATTERN-CROSS-LINK.md`.

## Audit notes

1. PR number was not invented; it came from live GitHub connector metadata used in this run.
2. The card is intentionally candidate/not-authority.
3. No credentials, tokens, private reviewer names, or nonessential identity details are included.
4. The atlas should be treated as a retrieval and learning layer. Promotion to canonical decision log requires a separate human-controlled write.
5. The most important future validation is diff-level review for implementation-bearing PRs and registry-level review for U10/U11 links.


## Extended audit scaffolding

This section is deliberately repetitive across PR cards because it gives the atlas a consistent audit surface. For this PR, the next reviewer should verify four things before promoting any claim out of candidate status.

First, verify **source identity**. Confirm that the PR URL, number, title, and merged timestamp still match GitHub. Do not rely on the atlas title alone. If the PR was superseded, replaced, or amended, record that relationship in `amend_chain` instead of silently editing the historical card.

Second, verify **claim strength**. A merged PR does not automatically mean runtime approval, canonical approval, product approval, or write approval. The safe reading is the narrowest reading supported by the PR body. If the body says docs-only, candidate-only, preview-only, shape-only, or no authority writeback, the future decision should carry that label forward until a separate promotion gate exists.

Third, verify **boundary compatibility**. Check whether the PR touched authority files, implementation paths, test paths, generated fixtures, staging directories, or only docs/research paths. A useful PR can still expose a boundary risk if it makes downstream readers believe more was approved than the PR actually approved. For implementation-bearing PRs, inspect whether later amendment cards such as #231 or #239 changed how the PR should be interpreted.

Fourth, verify **downstream dependency**. Ask which later PRs consumed this decision. If a later PR depends on it, the card becomes part of a chain rather than an isolated event. If a later PR repairs or downgrades it, the atlas should preserve both facts: the original merge and the later repair.

### Retrieval queries

Use these grep-style questions when this PR comes up again:

- “Which PR introduced this surface, and which PR exposed the caveat?”
- “Was the output candidate, authority, receipt, implementation, or amendment?”
- “Did the PR assert preview-only, write-disabled, docs-only, or NOT_EXECUTION_APPROVED?”
- “Is the evidence a real runtime result, a synthetic/localhost proof, a JSDOM/curl proof, a readback, or a receipt bundle?”
- “Does a later amendment downgrade `works` to `partial`, record a gate bypass, or separate execution SHA from audit SHA?”

### Promotion and demotion rules

Promotion requires positive evidence from the relevant source of record. A candidate doc can become authority only through an explicit authority-write PR. A preview result can become runtime proof only through an explicit runtime acceptance path. A partial synthetic proof can become a stronger claim only if the missing evidence is actually supplied. Demotion is equally important: if a later audit finds that a claim was too broad, preserve the original card and add the amendment relationship instead of deleting the earlier interpretation.

### Memory value

The lasting value of this PR card is not the prose itself. The value is that future work can search by PR number, cluster, decision kind, impact radius, introduced/exposed attribution, amend chain, and pattern tags. That makes ScoutFlow's history queryable without relying on fragile human memory or one-off grep sessions.
