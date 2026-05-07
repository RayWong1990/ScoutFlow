---
title: Milestone cluster index
status: candidate / supplementary / not-authority
created_at: 2026-05-07
---

# Milestone cluster index

Milestones compress historical decision and delivery progress. This index is a navigation aid, not a replacement for the individual node files or source documents.

```mermaid
flowchart TD
  ROOT["Milestone cluster index"]
  ROOT --> M_GIT_BOOTSTRAP["M-GIT-BOOTSTRAP<br/>2026-05-03 GitHub bootstrap / Step0 "]
  M_GIT_BOOTSTRAP -.-> M_PHASE1A_MANUALURL["M-PHASE1A-MANUALURL"]
  M_GIT_BOOTSTRAP -.-> T_AUTHORITY_FIRST["T-AUTHORITY-FIRST"]
  ROOT --> M_PHASE1A_MANUALURL["M-PHASE1A-MANUALURL<br/>Phase 1A manual_url metadata-only au"]
  M_PHASE1A_MANUALURL -.-> E_RECEIPT_LEDGER["E-RECEIPT-LEDGER"]
  M_PHASE1A_MANUALURL -.-> M_GIT_BOOTSTRAP["M-GIT-BOOTSTRAP"]
  ROOT --> M_RECEIPT_LEDGER["M-RECEIPT-LEDGER<br/>Receipt ledger / artifact_assets bas"]
  M_RECEIPT_LEDGER -.-> M_PHASE1A_MANUALURL["M-PHASE1A-MANUALURL"]
  M_RECEIPT_LEDGER -.-> M_TRUST_TRACE["M-TRUST-TRACE"]
  ROOT --> M_TRUST_TRACE["M-TRUST-TRACE<br/>Trust Trace API surface completed"]
  M_TRUST_TRACE -.-> M_PRD_SRD_V2["M-PRD-SRD-V2"]
  M_TRUST_TRACE -.-> M_RECEIPT_LEDGER["M-RECEIPT-LEDGER"]
  ROOT --> M_PRD_SRD_V2["M-PRD-SRD-V2<br/>PRD-v2 / SRD-v2 promoted"]
  M_PRD_SRD_V2 -.-> M_TRUST_TRACE["M-TRUST-TRACE"]
  M_PRD_SRD_V2 -.-> M_WAVE2_CLOSE["M-WAVE2-CLOSE"]
  ROOT --> M_WAVE2_CLOSE["M-WAVE2-CLOSE<br/>Wave 2 closed / authority reconcilia"]
  M_WAVE2_CLOSE -.-> M_PRD_SRD_V2["M-PRD-SRD-V2"]
  M_WAVE2_CLOSE -.-> M_WAVE3B_H5_BRIDGE_VAULT["M-WAVE3B-H5-BRIDGE-VAULT"]
  ROOT --> M_WAVE3B_H5_BRIDGE_VAULT["M-WAVE3B-H5-BRIDGE-VAULT<br/>Wave 3B H5 / Bridge / Vault planning"]
  M_WAVE3B_H5_BRIDGE_VAULT -.-> E_BRIDGE_THIN_API["E-BRIDGE-THIN-API"]
  M_WAVE3B_H5_BRIDGE_VAULT -.-> E_H5_CAPTURE_STATION["E-H5-CAPTURE-STATION"]
  ROOT --> M_WAVE4_BATCH2_BATCH3["M-WAVE4-BATCH2-BATCH3<br/>Wave 4 Batch2/3 app+service candidat"]
  M_WAVE4_BATCH2_BATCH3 -.-> M_DISPATCH127_176_FROZEN["M-DISPATCH127-176-FROZEN"]
  M_WAVE4_BATCH2_BATCH3 -.-> M_WAVE3B_H5_BRIDGE_VAULT["M-WAVE3B-H5-BRIDGE-VAULT"]
  ROOT --> M_DISPATCH127_176_FROZEN["M-DISPATCH127-176-FROZEN<br/>Dispatch126-176 executed and frozen"]
  M_DISPATCH127_176_FROZEN -.-> M_WAVE4_BATCH2_BATCH3["M-WAVE4-BATCH2-BATCH3"]
  M_DISPATCH127_176_FROZEN -.-> M_WAVE6_CANDIDATE_OPEN["M-WAVE6-CANDIDATE-OPEN"]
  ROOT --> M_WAVE6_CANDIDATE_OPEN["M-WAVE6-CANDIDATE-OPEN<br/>Wave 6 candidate open / no code-bear"]
  M_WAVE6_CANDIDATE_OPEN -.-> M_DISPATCH127_176_FROZEN["M-DISPATCH127-176-FROZEN"]
  M_WAVE6_CANDIDATE_OPEN -.-> T_CANDIDATE_NOT_AUTHORITY["T-CANDIDATE-NOT-AUTHORITY"]
```

## Node table

| node_id | title | risk | degree |
|---|---|---:|---:|
| `M-GIT-BOOTSTRAP` | 2026-05-03 GitHub bootstrap / Step0 baseline | medium | 3 |
| `M-PHASE1A-MANUALURL` | Phase 1A manual_url metadata-only authorized | critical | 4 |
| `M-RECEIPT-LEDGER` | Receipt ledger / artifact_assets baseline | critical | 3 |
| `M-TRUST-TRACE` | Trust Trace API surface completed | high | 3 |
| `M-PRD-SRD-V2` | PRD-v2 / SRD-v2 promoted | critical | 4 |
| `M-WAVE2-CLOSE` | Wave 2 closed / authority reconciliation | medium | 3 |
| `M-WAVE3B-H5-BRIDGE-VAULT` | Wave 3B H5 / Bridge / Vault planning landed | high | 7 |
| `M-WAVE4-BATCH2-BATCH3` | Wave 4 Batch2/3 app+service candidate surfaces landed | high | 3 |
| `M-DISPATCH127-176-FROZEN` | Dispatch126-176 executed and frozen | critical | 5 |
| `M-WAVE6-CANDIDATE-OPEN` | Wave 6 candidate open / no code-bearing next gate | critical | 3 |

## Cluster reading guidance

Read this cluster with three questions. First, which nodes are canonical/promoted facts and which are candidate synthesis? Second, which nodes are approval gates rather than progress claims? Third, which nodes should be read before any new dispatch or implementation starts? For ScoutFlow, the answer almost always routes back through `R-CURRENT-TASK-DECISION`, `T-AUTHORITY-FIRST`, `T-CANDIDATE-NOT-AUTHORITY`, and `T-EXECUTION-GATES`.

The cluster is deliberately redundant with the master graph. Redundancy here is defensive: a cold-start reader may enter from entities, lessons, feedback, or risk. Every path should rediscover the same hard boundaries: frozen dispatch evidence, no runtime/migration/front-end/vault true-write approval by default, and no second knowledge base.

## Maintenance note

When a node is added or removed, regenerate this index from the adjacency JSON. Manual edits to cluster diagrams are discouraged because they are a common source of graph drift.
