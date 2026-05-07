---
title: Feedback cluster index
status: candidate / supplementary / not-authority
created_at: 2026-05-07
---

# Feedback cluster index

Feedback nodes capture user operating preferences and hard corrections. This index is a navigation aid, not a replacement for the individual node files or source documents.

```mermaid
flowchart TD
  ROOT["Feedback cluster index"]
  ROOT --> F_MAX_HORSEPOWER["F-MAX-HORSEPOWER<br/>用户反馈：最大化马力 / 最大效率"]
  F_MAX_HORSEPOWER -.-> E_USER_PROSUMER["E-USER-PROSUMER"]
  F_MAX_HORSEPOWER -.-> F_LOOSER_NOT_CEREMONY["F-LOOSER-NOT-CEREMONY"]
  ROOT --> F_LOOSER_NOT_CEREMONY["F-LOOSER-NOT-CEREMONY<br/>用户反馈：松一点，不堆 ceremony"]
  F_LOOSER_NOT_CEREMONY -.-> F_MAX_HORSEPOWER["F-MAX-HORSEPOWER"]
  F_LOOSER_NOT_CEREMONY -.-> F_STRONG_VISUAL_FIRST_CLASS["F-STRONG-VISUAL-FIRST-CLASS"]
  ROOT --> F_STRONG_VISUAL_FIRST_CLASS["F-STRONG-VISUAL-FIRST-CLASS<br/>用户反馈：强视觉是一级轴"]
  F_STRONG_VISUAL_FIRST_CLASS -.-> F_LOOSER_NOT_CEREMONY["F-LOOSER-NOT-CEREMONY"]
  F_STRONG_VISUAL_FIRST_CLASS -.-> F_SAFE_PARALLEL["F-SAFE-PARALLEL"]
  ROOT --> F_SAFE_PARALLEL["F-SAFE-PARALLEL<br/>用户反馈：安全前提下最大并行"]
  F_SAFE_PARALLEL -.-> F_GPT_PRO_AS_WORKER["F-GPT-PRO-AS-WORKER"]
  F_SAFE_PARALLEL -.-> F_STRONG_VISUAL_FIRST_CLASS["F-STRONG-VISUAL-FIRST-CLASS"]
  ROOT --> F_GPT_PRO_AS_WORKER["F-GPT-PRO-AS-WORKER<br/>用户反馈：用 GPT Pro 干活"]
  F_GPT_PRO_AS_WORKER -.-> F_AMEND_AND_PROCEED["F-AMEND-AND-PROCEED"]
  F_GPT_PRO_AS_WORKER -.-> F_SAFE_PARALLEL["F-SAFE-PARALLEL"]
  ROOT --> F_AMEND_AND_PROCEED["F-AMEND-AND-PROCEED<br/>用户反馈：amend_and_proceed"]
  F_AMEND_AND_PROCEED -.-> F_DIRECT_MERGE_OK["F-DIRECT-MERGE-OK"]
  F_AMEND_AND_PROCEED -.-> F_GPT_PRO_AS_WORKER["F-GPT-PRO-AS-WORKER"]
  ROOT --> F_DIRECT_MERGE_OK["F-DIRECT-MERGE-OK<br/>用户反馈：可直 merge，但要不越界"]
  F_DIRECT_MERGE_OK -.-> F_AMEND_AND_PROCEED["F-AMEND-AND-PROCEED"]
  F_DIRECT_MERGE_OK -.-> F_NOT_HEAVY_KM["F-NOT-HEAVY-KM"]
  ROOT --> F_NOT_HEAVY_KM["F-NOT-HEAVY-KM<br/>用户反馈：不要重 KM / 第二知识库"]
  F_NOT_HEAVY_KM -.-> F_DIRECT_MERGE_OK["F-DIRECT-MERGE-OK"]
  F_NOT_HEAVY_KM -.-> F_SINGLE_USER_PROSUMER["F-SINGLE-USER-PROSUMER"]
  ROOT --> F_SINGLE_USER_PROSUMER["F-SINGLE-USER-PROSUMER<br/>用户反馈：单人 prosumer max horsepower"]
  F_SINGLE_USER_PROSUMER -.-> F_DISPATCH_FROZEN_CORRECTION["F-DISPATCH-FROZEN-CORRECTION"]
  F_SINGLE_USER_PROSUMER -.-> F_NOT_HEAVY_KM["F-NOT-HEAVY-KM"]
  ROOT --> F_DISPATCH_FROZEN_CORRECTION["F-DISPATCH-FROZEN-CORRECTION<br/>用户反馈：126-176 已执行冻结"]
  F_DISPATCH_FROZEN_CORRECTION -.-> F_SINGLE_USER_PROSUMER["F-SINGLE-USER-PROSUMER"]
  F_DISPATCH_FROZEN_CORRECTION -.-> T_CANDIDATE_NOT_AUTHORITY["T-CANDIDATE-NOT-AUTHORITY"]
```

## Node table

| node_id | title | risk | degree |
|---|---|---:|---:|
| `F-MAX-HORSEPOWER` | 用户反馈：最大化马力 / 最大效率 | critical | 3 |
| `F-LOOSER-NOT-CEREMONY` | 用户反馈：松一点，不堆 ceremony | high | 3 |
| `F-STRONG-VISUAL-FIRST-CLASS` | 用户反馈：强视觉是一级轴 | high | 3 |
| `F-SAFE-PARALLEL` | 用户反馈：安全前提下最大并行 | critical | 5 |
| `F-GPT-PRO-AS-WORKER` | 用户反馈：用 GPT Pro 干活 | medium | 3 |
| `F-AMEND-AND-PROCEED` | 用户反馈：amend_and_proceed | high | 3 |
| `F-DIRECT-MERGE-OK` | 用户反馈：可直 merge，但要不越界 | medium | 3 |
| `F-NOT-HEAVY-KM` | 用户反馈：不要重 KM / 第二知识库 | critical | 4 |
| `F-SINGLE-USER-PROSUMER` | 用户反馈：单人 prosumer max horsepower | high | 3 |
| `F-DISPATCH-FROZEN-CORRECTION` | 用户反馈：126-176 已执行冻结 | critical | 3 |

## Cluster reading guidance

Read this cluster with three questions. First, which nodes are canonical/promoted facts and which are candidate synthesis? Second, which nodes are approval gates rather than progress claims? Third, which nodes should be read before any new dispatch or implementation starts? For ScoutFlow, the answer almost always routes back through `R-CURRENT-TASK-DECISION`, `T-AUTHORITY-FIRST`, `T-CANDIDATE-NOT-AUTHORITY`, and `T-EXECUTION-GATES`.

The cluster is deliberately redundant with the master graph. Redundancy here is defensive: a cold-start reader may enter from entities, lessons, feedback, or risk. Every path should rediscover the same hard boundaries: frozen dispatch evidence, no runtime/migration/front-end/vault true-write approval by default, and no second knowledge base.

## Maintenance note

When a node is added or removed, regenerate this index from the adjacency JSON. Manual edits to cluster diagrams are discouraged because they are a common source of graph drift.
