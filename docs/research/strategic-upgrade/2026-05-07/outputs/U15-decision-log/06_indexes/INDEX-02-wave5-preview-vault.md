---
title: "Wave5 preview/vault candidate surfaces"
status: candidate / cluster-index / not-authority
authority: not-authority
count: 20
---

# Wave5 preview/vault candidate surfaces

## Included PRs

| PR | kind | impact | introduced/exposed | title |
|---:|---|---|---|---|
| #161 | candidate-scope | single-cluster | introduced | T-P1A-124: Topic card vault rendering candidate |
| #162 | candidate-scope | single-cluster | introduced | T-P1A-125: Topic card preview shape candidate |
| #163 | authority-sync | cross-phase | introduced | T-P1A-126: Capture plan dry-run note shape |
| #164 | authority-sync | cross-phase | introduced | T-P1A-127: Wave 5 docs-pack PR factory packaging |
| #165 | candidate-scope | single-cluster | introduced | T-P1A-128: Wave 5 file-domain matrix draft |
| #166 | candidate-scope | single-cluster | introduced | T-P1A-129: Wave 5 dependency graph draft |
| #167 | authority-sync | cross-phase | introduced | T-P1A-130: Signal workbench API placeholder contract |
| #168 | candidate-scope | single-cluster | introduced | T-P1A-131: Topic card frontend IA candidate |
| #169 | authority-sync | cross-phase | introduced | T-P1A-132: Capture plan frontend IA candidate |
| #170 | candidate-scope | single-cluster | introduced | T-P1A-133: Hypothesis comparison UX candidate |
| #171 | audit-evidence | single-cluster | exposed | T-P1A-134: Signal ingestion audit lane candidate |
| #172 | candidate-scope | single-cluster | introduced | T-P1A-135: Wave 5 visual reporting candidate |
| #173 | other | single-cluster | introduced | T-P1A-136: Localhost review roster for Wave 5 surfaces |
| #174 | authority-sync | cross-phase | introduced | T-P1A-137: STEP3 commander prompt contract note |
| #175 | candidate-scope | single-cluster | introduced | T-P1A-138: Cloud draft resume and packaging rules |
| #176 | authority-sync | cross-phase | exposed | T-P1A-139: Readback delta application rules |
| #177 | boundary | single-cluster | introduced | T-P1A-140: Deferred and overflow registry candidate |
| #178 | implementation-boundary | single-cluster | introduced | T-P1A-141: Bridge hardening post-110 continuation |
| #179 | candidate-scope | single-cluster | introduced | T-P1A-142: Vault preview continuation candidate |
| #180 | authority-sync | cross-phase | introduced | T-P1A-143: Vault dry-run continuation candidate |

## Cluster reading rule

Read this cluster as a local decision system, not just a list of merges. The common thread is the boundary language carried by each PR. A candidate doc is useful because it scopes future work; an evidence receipt is useful because it prevents overclaiming; an implementation-bearing PR is useful only when its tests and later amendments keep the allowed surface honest.

## Risks to audit later

- Whether the cluster contains silent flexibility not yet captured by an amendment.
- Whether candidate/not-authority language is repeated consistently across downstream docs.
- Whether any authority writeback happened in a separate PR and should be cross-linked.
- Whether U10/U11 registries add missing runbook or anti-pattern links after this package.
