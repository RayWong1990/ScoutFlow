---
title: Lesson cluster index
status: candidate / supplementary / not-authority
created_at: 2026-05-07
---

# Lesson cluster index

Lessons preserve historical failure modes and stop lines. This index is a navigation aid, not a replacement for the individual node files or source documents.

```mermaid
flowchart TD
  ROOT["Lesson cluster index"]
  ROOT --> L_AUTHORITY_DRIFT["L-AUTHORITY-DRIFT<br/>踩坑：authority drift"]
  L_AUTHORITY_DRIFT -.-> L_RUNTIME_APPROVAL_DRIFT["L-RUNTIME-APPROVAL-DRIFT"]
  L_AUTHORITY_DRIFT -.-> T_AUTHORITY_FIRST["T-AUTHORITY-FIRST"]
  ROOT --> L_RUNTIME_APPROVAL_DRIFT["L-RUNTIME-APPROVAL-DRIFT<br/>踩坑：runtime approval drift"]
  L_RUNTIME_APPROVAL_DRIFT -.-> L_AUTHORITY_DRIFT["L-AUTHORITY-DRIFT"]
  L_RUNTIME_APPROVAL_DRIFT -.-> L_MIGRATION_DRIFT["L-MIGRATION-DRIFT"]
  ROOT --> L_MIGRATION_DRIFT["L-MIGRATION-DRIFT<br/>踩坑：DB/migration 被 candidate 偷渡"]
  L_MIGRATION_DRIFT -.-> L_RUNTIME_APPROVAL_DRIFT["L-RUNTIME-APPROVAL-DRIFT"]
  L_MIGRATION_DRIFT -.-> L_VAULT_PREVIEW_AS_TRUE_WRITE["L-VAULT-PREVIEW-AS-TRUE-WRITE"]
  ROOT --> L_VAULT_PREVIEW_AS_TRUE_WRITE["L-VAULT-PREVIEW-AS-TRUE-WRITE<br/>踩坑：把 vault preview 当 true write"]
  L_VAULT_PREVIEW_AS_TRUE_WRITE -.-> L_MIGRATION_DRIFT["L-MIGRATION-DRIFT"]
  L_VAULT_PREVIEW_AS_TRUE_WRITE -.-> L_SECOND_KNOWLEDGE_BASE["L-SECOND-KNOWLEDGE-BASE"]
  ROOT --> L_SECOND_KNOWLEDGE_BASE["L-SECOND-KNOWLEDGE-BASE<br/>踩坑：第二知识库 / mirror truth"]
  L_SECOND_KNOWLEDGE_BASE -.-> L_HANDOFF_OVERLONG["L-HANDOFF-OVERLONG"]
  L_SECOND_KNOWLEDGE_BASE -.-> L_VAULT_PREVIEW_AS_TRUE_WRITE["L-VAULT-PREVIEW-AS-TRUE-WRITE"]
  ROOT --> L_HANDOFF_OVERLONG["L-HANDOFF-OVERLONG<br/>踩坑：handoff 过长但不可执行"]
  L_HANDOFF_OVERLONG -.-> L_CANDIDATE_PROMOTION["L-CANDIDATE-PROMOTION"]
  L_HANDOFF_OVERLONG -.-> L_SECOND_KNOWLEDGE_BASE["L-SECOND-KNOWLEDGE-BASE"]
  ROOT --> L_CANDIDATE_PROMOTION["L-CANDIDATE-PROMOTION<br/>踩坑：candidate 漂移成 authority"]
  L_CANDIDATE_PROMOTION -.-> L_HANDOFF_OVERLONG["L-HANDOFF-OVERLONG"]
  L_CANDIDATE_PROMOTION -.-> L_MULTIWINDOW_RACE["L-MULTIWINDOW-RACE"]
  ROOT --> L_MULTIWINDOW_RACE["L-MULTIWINDOW-RACE<br/>踩坑：多窗口 race / authority writer 冲突"]
  L_MULTIWINDOW_RACE -.-> L_CANDIDATE_PROMOTION["L-CANDIDATE-PROMOTION"]
  L_MULTIWINDOW_RACE -.-> L_TOKEN_BUDGET["L-TOKEN-BUDGET"]
  ROOT --> L_TOKEN_BUDGET["L-TOKEN-BUDGET<br/>踩坑：token over budget / 全量读取错觉"]
  L_TOKEN_BUDGET -.-> L_BILIBILI_CRED_RISK["L-BILIBILI-CRED-RISK"]
  L_TOKEN_BUDGET -.-> L_MULTIWINDOW_RACE["L-MULTIWINDOW-RACE"]
  ROOT --> L_BILIBILI_CRED_RISK["L-BILIBILI-CRED-RISK<br/>踩坑：Bilibili / credential / C&D 风险"]
  L_BILIBILI_CRED_RISK -.-> L_PRODUCT_CLOSURE_MISTAKE["L-PRODUCT-CLOSURE-MISTAKE"]
  L_BILIBILI_CRED_RISK -.-> L_TOKEN_BUDGET["L-TOKEN-BUDGET"]
  ROOT --> L_PRODUCT_CLOSURE_MISTAKE["L-PRODUCT-CLOSURE-MISTAKE<br/>踩坑：工程闭环误当产品闭环"]
  L_PRODUCT_CLOSURE_MISTAKE -.-> L_BILIBILI_CRED_RISK["L-BILIBILI-CRED-RISK"]
  L_PRODUCT_CLOSURE_MISTAKE -.-> L_OVEROBJECTIFICATION["L-OVEROBJECTIFICATION"]
  ROOT --> L_OVEROBJECTIFICATION["L-OVEROBJECTIFICATION<br/>踩坑：过早对象化 / 单人 prosumer 工具链膨胀"]
  L_OVEROBJECTIFICATION -.-> L_PRODUCT_CLOSURE_MISTAKE["L-PRODUCT-CLOSURE-MISTAKE"]
  L_OVEROBJECTIFICATION -.-> P_OBJECTS_AFTER_PROOF["P-OBJECTS-AFTER-PROOF"]
```

## Node table

| node_id | title | risk | degree |
|---|---|---:|---:|
| `L-AUTHORITY-DRIFT` | 踩坑：authority drift | critical | 3 |
| `L-RUNTIME-APPROVAL-DRIFT` | 踩坑：runtime approval drift | critical | 4 |
| `L-MIGRATION-DRIFT` | 踩坑：DB/migration 被 candidate 偷渡 | critical | 4 |
| `L-VAULT-PREVIEW-AS-TRUE-WRITE` | 踩坑：把 vault preview 当 true write | critical | 6 |
| `L-SECOND-KNOWLEDGE-BASE` | 踩坑：第二知识库 / mirror truth | critical | 4 |
| `L-HANDOFF-OVERLONG` | 踩坑：handoff 过长但不可执行 | high | 3 |
| `L-CANDIDATE-PROMOTION` | 踩坑：candidate 漂移成 authority | critical | 3 |
| `L-MULTIWINDOW-RACE` | 踩坑：多窗口 race / authority writer 冲突 | critical | 5 |
| `L-TOKEN-BUDGET` | 踩坑：token over budget / 全量读取错觉 | high | 3 |
| `L-BILIBILI-CRED-RISK` | 踩坑：Bilibili / credential / C&D 风险 | critical | 4 |
| `L-PRODUCT-CLOSURE-MISTAKE` | 踩坑：工程闭环误当产品闭环 | critical | 4 |
| `L-OVEROBJECTIFICATION` | 踩坑：过早对象化 / 单人 prosumer 工具链膨胀 | high | 3 |

## Cluster reading guidance

Read this cluster with three questions. First, which nodes are canonical/promoted facts and which are candidate synthesis? Second, which nodes are approval gates rather than progress claims? Third, which nodes should be read before any new dispatch or implementation starts? For ScoutFlow, the answer almost always routes back through `R-CURRENT-TASK-DECISION`, `T-AUTHORITY-FIRST`, `T-CANDIDATE-NOT-AUTHORITY`, and `T-EXECUTION-GATES`.

The cluster is deliberately redundant with the master graph. Redundancy here is defensive: a cold-start reader may enter from entities, lessons, feedback, or risk. Every path should rediscover the same hard boundaries: frozen dispatch evidence, no runtime/migration/front-end/vault true-write approval by default, and no second knowledge base.

## Maintenance note

When a node is added or removed, regenerate this index from the adjacency JSON. Manual edits to cluster diagrams are discouraged because they are a common source of graph drift.
