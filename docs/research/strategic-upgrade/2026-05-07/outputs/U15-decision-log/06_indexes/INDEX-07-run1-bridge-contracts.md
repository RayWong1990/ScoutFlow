---
title: "Run-1 bridge and contracts"
status: candidate / cluster-index / not-authority
authority: not-authority
count: 4
---

# Run-1 bridge and contracts

## Included PRs

| PR | kind | impact | introduced/exposed | title |
|---:|---|---|---|---|
| #204 | contract | multi-cluster | both | feat(api): mount bridge router in create_app |
| #205 | implementation-boundary | multi-cluster | both | test(api): add bridge vault preview smoke coverage |
| #206 | contract | multi-cluster | both | test(contracts): add bridge openapi golden contract |
| #207 | implementation-boundary | multi-cluster | introduced | PF-LP-04: add capture station createCapture client |

## Cluster reading rule

Read this cluster as a local decision system, not just a list of merges. The common thread is the boundary language carried by each PR. A candidate doc is useful because it scopes future work; an evidence receipt is useful because it prevents overclaiming; an implementation-bearing PR is useful only when its tests and later amendments keep the allowed surface honest.

## Risks to audit later

- Whether the cluster contains silent flexibility not yet captured by an amendment.
- Whether candidate/not-authority language is repeated consistently across downstream docs.
- Whether any authority writeback happened in a separate PR and should be cross-linked.
- Whether U10/U11 registries add missing runbook or anti-pattern links after this package.
