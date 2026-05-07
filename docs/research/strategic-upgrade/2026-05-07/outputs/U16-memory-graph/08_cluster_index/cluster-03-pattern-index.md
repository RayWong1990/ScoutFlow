---
title: Pattern cluster index
status: candidate / supplementary / not-authority
created_at: 2026-05-07
---

# Pattern cluster index

Patterns define repeatable operating moves that prevent context loss. This index is a navigation aid, not a replacement for the individual node files or source documents.

```mermaid
flowchart TD
  ROOT["Pattern cluster index"]
  ROOT --> P_AUTHORITY_READBACK_BEFORE_WORK["P-AUTHORITY-READBACK-BEFORE-WORK<br/>先读 authority，再开工"]
  P_AUTHORITY_READBACK_BEFORE_WORK -.-> P_FROZEN_DISPATCH_AS_EVIDENCE["P-FROZEN-DISPATCH-AS-EVIDENCE"]
  P_AUTHORITY_READBACK_BEFORE_WORK -.-> R_CURRENT_TASK_DECISION["R-CURRENT-TASK-DECISION"]
  ROOT --> P_FROZEN_DISPATCH_AS_EVIDENCE["P-FROZEN-DISPATCH-AS-EVIDENCE<br/>冻结 dispatch 作为 evidence layer"]
  P_FROZEN_DISPATCH_AS_EVIDENCE -.-> M_DISPATCH127_176_FROZEN["M-DISPATCH127-176-FROZEN"]
  P_FROZEN_DISPATCH_AS_EVIDENCE -.-> P_AUTHORITY_READBACK_BEFORE_WORK["P-AUTHORITY-READBACK-BEFORE-WORK"]
  ROOT --> P_PROOF_PAIR_CANARY["P-PROOF-PAIR-CANARY<br/>Topic-card proof pair canary"]
  P_PROOF_PAIR_CANARY -.-> E_TOPIC_CARD["E-TOPIC-CARD"]
  P_PROOF_PAIR_CANARY -.-> P_FROZEN_DISPATCH_AS_EVIDENCE["P-FROZEN-DISPATCH-AS-EVIDENCE"]
  ROOT --> P_OBJECTS_AFTER_PROOF["P-OBJECTS-AFTER-PROOF<br/>先 proof 后对象化扩张"]
  P_OBJECTS_AFTER_PROOF -.-> L_OVEROBJECTIFICATION["L-OVEROBJECTIFICATION"]
  P_OBJECTS_AFTER_PROOF -.-> P_API_AS_WRITE_BOUNDARY["P-API-AS-WRITE-BOUNDARY"]
  ROOT --> P_API_AS_WRITE_BOUNDARY["P-API-AS-WRITE-BOUNDARY<br/>API-as-write-boundary"]
  P_API_AS_WRITE_BOUNDARY -.-> P_LOCAL_ONLY_AUTH_SAFETY["P-LOCAL-ONLY-AUTH-SAFETY"]
  P_API_AS_WRITE_BOUNDARY -.-> P_OBJECTS_AFTER_PROOF["P-OBJECTS-AFTER-PROOF"]
  ROOT --> P_LOCAL_ONLY_AUTH_SAFETY["P-LOCAL-ONLY-AUTH-SAFETY<br/>local-only auth / credential isolati"]
  P_LOCAL_ONLY_AUTH_SAFETY -.-> L_BILIBILI_CRED_RISK["L-BILIBILI-CRED-RISK"]
  P_LOCAL_ONLY_AUTH_SAFETY -.-> P_API_AS_WRITE_BOUNDARY["P-API-AS-WRITE-BOUNDARY"]
  ROOT --> P_PR_FACTORY_LANE_SHAPING["P-PR-FACTORY-LANE-SHAPING<br/>PR Factory lane shaping"]
  P_PR_FACTORY_LANE_SHAPING -.-> P_LOCAL_ONLY_AUTH_SAFETY["P-LOCAL-ONLY-AUTH-SAFETY"]
  P_PR_FACTORY_LANE_SHAPING -.-> P_OVERFLOW_NOT_BLOCKER["P-OVERFLOW-NOT-BLOCKER"]
  ROOT --> P_OVERFLOW_NOT_BLOCKER["P-OVERFLOW-NOT-BLOCKER<br/>Overflow captures options without bl"]
  P_OVERFLOW_NOT_BLOCKER -.-> P_DUAL_TRUTH_SEPARATION["P-DUAL-TRUTH-SEPARATION"]
  P_OVERFLOW_NOT_BLOCKER -.-> P_PR_FACTORY_LANE_SHAPING["P-PR-FACTORY-LANE-SHAPING"]
  ROOT --> P_DUAL_TRUTH_SEPARATION["P-DUAL-TRUTH-SEPARATION<br/>Zip truth / GitHub live truth / RAW "]
  P_DUAL_TRUTH_SEPARATION -.-> P_OVERFLOW_NOT_BLOCKER["P-OVERFLOW-NOT-BLOCKER"]
  P_DUAL_TRUTH_SEPARATION -.-> P_VISUAL_REVIEW_5_GATE["P-VISUAL-REVIEW-5-GATE"]
  ROOT --> P_VISUAL_REVIEW_5_GATE["P-VISUAL-REVIEW-5-GATE<br/>5-Gate visual review"]
  P_VISUAL_REVIEW_5_GATE -.-> P_DUAL_TRUTH_SEPARATION["P-DUAL-TRUTH-SEPARATION"]
  P_VISUAL_REVIEW_5_GATE -.-> P_HANDOFF_COLD_START["P-HANDOFF-COLD-START"]
  ROOT --> P_HANDOFF_COLD_START["P-HANDOFF-COLD-START<br/>cold-start handoff packet"]
  P_HANDOFF_COLD_START -.-> E_AI_AGENTS["E-AI-AGENTS"]
  P_HANDOFF_COLD_START -.-> P_SELF_AUDIT_CLAIM_LABELS["P-SELF-AUDIT-CLAIM-LABELS"]
  ROOT --> P_SELF_AUDIT_CLAIM_LABELS["P-SELF-AUDIT-CLAIM-LABELS<br/>claim labels + self-audit as anti-dr"]
  P_SELF_AUDIT_CLAIM_LABELS -.-> E_CONTENTFLOW["E-CONTENTFLOW"]
  P_SELF_AUDIT_CLAIM_LABELS -.-> P_HANDOFF_COLD_START["P-HANDOFF-COLD-START"]
```

## Node table

| node_id | title | risk | degree |
|---|---|---:|---:|
| `P-AUTHORITY-READBACK-BEFORE-WORK` | 先读 authority，再开工 | critical | 4 |
| `P-FROZEN-DISPATCH-AS-EVIDENCE` | 冻结 dispatch 作为 evidence layer | critical | 5 |
| `P-PROOF-PAIR-CANARY` | Topic-card proof pair canary | critical | 6 |
| `P-OBJECTS-AFTER-PROOF` | 先 proof 后对象化扩张 | high | 3 |
| `P-API-AS-WRITE-BOUNDARY` | API-as-write-boundary | critical | 5 |
| `P-LOCAL-ONLY-AUTH-SAFETY` | local-only auth / credential isolation | critical | 4 |
| `P-PR-FACTORY-LANE-SHAPING` | PR Factory lane shaping | high | 3 |
| `P-OVERFLOW-NOT-BLOCKER` | Overflow captures options without blocking proof | high | 3 |
| `P-DUAL-TRUTH-SEPARATION` | Zip truth / GitHub live truth / RAW truth separation | critical | 4 |
| `P-VISUAL-REVIEW-5-GATE` | 5-Gate visual review | high | 3 |
| `P-HANDOFF-COLD-START` | cold-start handoff packet | high | 4 |
| `P-SELF-AUDIT-CLAIM-LABELS` | claim labels + self-audit as anti-drift | critical | 3 |

## Cluster reading guidance

Read this cluster with three questions. First, which nodes are canonical/promoted facts and which are candidate synthesis? Second, which nodes are approval gates rather than progress claims? Third, which nodes should be read before any new dispatch or implementation starts? For ScoutFlow, the answer almost always routes back through `R-CURRENT-TASK-DECISION`, `T-AUTHORITY-FIRST`, `T-CANDIDATE-NOT-AUTHORITY`, and `T-EXECUTION-GATES`.

The cluster is deliberately redundant with the master graph. Redundancy here is defensive: a cold-start reader may enter from entities, lessons, feedback, or risk. Every path should rediscover the same hard boundaries: frozen dispatch evidence, no runtime/migration/front-end/vault true-write approval by default, and no second knowledge base.

## Maintenance note

When a node is added or removed, regenerate this index from the adjacency JSON. Manual edits to cluster diagrams are discouraged because they are a common source of graph drift.
