---
title: Branch grouping and PR naming policy
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-GLOBAL-07
---

# Branch grouping and PR naming policy

## branch_pattern

| artifact_class | branch pattern | title pattern |
|---|---|---|
| `PF-C3` docs | `task/pf-c3-<code>-<slug>` | `docs: add <code> <short purpose>` |
| `PF-GLOBAL` docs | `task/pf-global-<code>-<slug>` | `docs: add <code> <short purpose>` |
| support script | `task/pf-global-01-manifest-verifier` | `tools: add successor pack manifest verifier` |
| run summary | `task/window2-run-report` | `docs: add window2 run report bundle` |

## grouping_rules

- One dispatch, one branch, one PR.
- Cross-dispatch bundling is allowed only for the final run report bundle because it depends on many merged PRs.
- A docs-only branch must not quietly include authority or runtime-path edits.

## naming_rules

- Put the dispatch code in both branch and PR title.
- Use `docs:` for candidate notes and `tools:` only for the manifest checker.
- Avoid vague titles like `misc fixes`, `polish`, or `support docs`.

## verdict

- `T-PASS` means future writers have a consistent naming baseline.
