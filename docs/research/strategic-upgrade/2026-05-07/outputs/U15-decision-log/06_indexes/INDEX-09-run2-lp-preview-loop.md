---
title: "Run-2 LP preview loop"
status: candidate / cluster-index / not-authority
authority: not-authority
count: 12
---

# Run-2 LP preview loop

## Included PRs

| PR | kind | impact | introduced/exposed | title |
|---:|---|---|---|---|
| #216 | implementation-boundary | multi-cluster | both | PF-LP-05: wire url bar create capture submit |
| #226 | implementation-boundary | multi-cluster | both | PF-LP-06/07: add preview shell bridge |
| #227 | other | single-cluster | introduced | docs: add window2 docs run bundle |
| #228 | contract | multi-cluster | both | PF-LP-06-15 repair: land preview shell and panel loop |
| #230 | boundary | multi-cluster | introduced | PF-LP-12: add localhost preview dev runbook |
| #232 | authority-sync | cross-phase | exposed | docs(post-frozen): record PF-LP-10 coverage evidence under #228 |
| #233 | authority-sync | cross-phase | exposed | docs(post-frozen): record PF-LP-09 coverage evidence under #228 |
| #234 | authority-sync | cross-phase | exposed | docs(post-frozen): record PF-LP-14 coverage evidence under #228 |
| #235 | other | single-cluster | exposed | docs(post-frozen): add PF-LP-16 synthetic localhost evidence |
| #236 | audit-evidence | single-cluster | exposed | docs(post-frozen): add PF-LP-17 preview-only readback |
| #237 | authority-sync | cross-phase | exposed | docs(post-frozen): add PF-LP-18 authority-safe closeout note |
| #238 | audit-evidence | single-cluster | exposed | docs(post-frozen): add Run-2 closeout receipt bundle |

## Cluster reading rule

Read this cluster as a local decision system, not just a list of merges. The common thread is the boundary language carried by each PR. A candidate doc is useful because it scopes future work; an evidence receipt is useful because it prevents overclaiming; an implementation-bearing PR is useful only when its tests and later amendments keep the allowed surface honest.

## Risks to audit later

- Whether the cluster contains silent flexibility not yet captured by an amendment.
- Whether candidate/not-authority language is repeated consistently across downstream docs.
- Whether any authority writeback happened in a separate PR and should be cross-linked.
- Whether U10/U11 registries add missing runbook or anti-pattern links after this package.
