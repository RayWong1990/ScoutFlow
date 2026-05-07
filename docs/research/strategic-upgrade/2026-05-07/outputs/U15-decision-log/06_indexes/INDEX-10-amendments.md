---
title: "Amendment anchors"
status: candidate / cluster-index / not-authority
authority: not-authority
count: 2
---

# Amendment anchors

## Included PRs

| PR | kind | impact | introduced/exposed | title |
|---:|---|---|---|---|
| #231 | amendment | cross-phase | exposed | docs(post-frozen): Run-1 amendment ledger + 3 external audits |
| #239 | amendment | cross-phase | exposed | chore(post-frozen): amend run-2 receipt traceability |

## Cluster reading rule

Read this cluster as a local decision system, not just a list of merges. The common thread is the boundary language carried by each PR. A candidate doc is useful because it scopes future work; an evidence receipt is useful because it prevents overclaiming; an implementation-bearing PR is useful only when its tests and later amendments keep the allowed surface honest.

## Risks to audit later

- Whether the cluster contains silent flexibility not yet captured by an amendment.
- Whether candidate/not-authority language is repeated consistently across downstream docs.
- Whether any authority writeback happened in a separate PR and should be cross-linked.
- Whether U10/U11 registries add missing runbook or anti-pattern links after this package.
