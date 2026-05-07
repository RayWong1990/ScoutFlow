---
title: "Run-2 global controls and PF-C3"
status: candidate / cluster-index / not-authority
authority: not-authority
count: 18
---

# Run-2 global controls and PF-C3

## Included PRs

| PR | kind | impact | introduced/exposed | title |
|---:|---|---|---|---|
| #208 | other | single-cluster | introduced | docs: add PF-C3-01 object inventory |
| #209 | other | multi-cluster | introduced | tools: add PF-GLOBAL-01 manifest verifier |
| #210 | other | multi-cluster | introduced | docs: add PF-GLOBAL-02 near-term commander prompt |
| #211 | other | multi-cluster | introduced | docs: add PF-GLOBAL-03 preview review checklist |
| #212 | contract | multi-cluster | introduced | docs: add PF-GLOBAL-04 proof scorecard schema |
| #213 | other | multi-cluster | introduced | docs: add PF-GLOBAL-05 runlog resume protocol |
| #214 | audit-evidence | multi-cluster | exposed | docs: add PF-GLOBAL-06 audit packet generator candidate |
| #215 | other | multi-cluster | introduced | docs: add PF-GLOBAL-07 branch grouping policy |
| #216 | implementation-boundary | multi-cluster | both | PF-LP-05: wire url bar create capture submit |
| #217 | boundary | multi-cluster | introduced | docs: add PF-GLOBAL-08 human gate calendar |
| #218 | boundary | multi-cluster | introduced | docs: add PF-GLOBAL-09 kill switch registry |
| #219 | other | multi-cluster | introduced | docs: add PF-GLOBAL-10 external research queue |
| #220 | candidate-scope | multi-cluster | introduced | docs: add PF-GLOBAL-11 runtime lane research note |
| #221 | audit-evidence | multi-cluster | exposed | docs: add PF-GLOBAL-12 reservoir closeout map |
| #222 | other | single-cluster | introduced | docs: add PF-C3-02 keep list |
| #223 | other | single-cluster | introduced | docs: add PF-C3-03 compress list |
| #224 | other | single-cluster | introduced | docs: add PF-C3-05 language patch |
| #225 | audit-evidence | single-cluster | exposed | docs: add PF-C3-06 closeout |

## Cluster reading rule

Read this cluster as a local decision system, not just a list of merges. The common thread is the boundary language carried by each PR. A candidate doc is useful because it scopes future work; an evidence receipt is useful because it prevents overclaiming; an implementation-bearing PR is useful only when its tests and later amendments keep the allowed surface honest.

## Risks to audit later

- Whether the cluster contains silent flexibility not yet captured by an amendment.
- Whether candidate/not-authority language is repeated consistently across downstream docs.
- Whether any authority writeback happened in a separate PR and should be cross-linked.
- Whether U10/U11 registries add missing runbook or anti-pattern links after this package.
