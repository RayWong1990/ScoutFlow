---
title: Entity cluster index
status: candidate / supplementary / not-authority
created_at: 2026-05-07
---

# Entity cluster index

Entities define actors, objects, and system surfaces. This index is a navigation aid, not a replacement for the individual node files or source documents.

```mermaid
flowchart TD
  ROOT["Entity cluster index"]
  ROOT --> E_SCOUTFLOW["E-SCOUTFLOW<br/>ScoutFlow / 采集线"]
  E_SCOUTFLOW -.-> E_BRIDGE_THIN_API["E-BRIDGE-THIN-API"]
  E_SCOUTFLOW -.-> E_H5_CAPTURE_STATION["E-H5-CAPTURE-STATION"]
  ROOT --> E_RAW_VAULT["E-RAW-VAULT<br/>RAW vault / 长期知识 SoR"]
  E_RAW_VAULT -.-> E_DILOFLOW["E-DILOFLOW"]
  E_RAW_VAULT -.-> E_SCOUTFLOW["E-SCOUTFLOW"]
  ROOT --> E_DILOFLOW["E-DILOFLOW<br/>DiloFlow sibling consumer"]
  E_DILOFLOW -.-> E_CONTENTFLOW["E-CONTENTFLOW"]
  E_DILOFLOW -.-> E_RAW_VAULT["E-RAW-VAULT"]
  ROOT --> E_CONTENTFLOW["E-CONTENTFLOW<br/>ContentFlow / L retrospective siblin"]
  E_CONTENTFLOW -.-> E_DILOFLOW["E-DILOFLOW"]
  E_CONTENTFLOW -.-> E_USER_PROSUMER["E-USER-PROSUMER"]
  ROOT --> E_USER_PROSUMER["E-USER-PROSUMER<br/>用户：single-user prosumer / 最大马力 owner"]
  E_USER_PROSUMER -.-> E_AI_AGENTS["E-AI-AGENTS"]
  E_USER_PROSUMER -.-> E_CONTENTFLOW["E-CONTENTFLOW"]
  ROOT --> E_AI_AGENTS["E-AI-AGENTS<br/>AI agent mesh: GPT Pro / Codex / CC "]
  E_AI_AGENTS -.-> E_SIGNAL["E-SIGNAL"]
  E_AI_AGENTS -.-> E_USER_PROSUMER["E-USER-PROSUMER"]
  ROOT --> E_SIGNAL["E-SIGNAL<br/>Signal entity v0"]
  E_SIGNAL -.-> E_AI_AGENTS["E-AI-AGENTS"]
  E_SIGNAL -.-> E_HYPOTHESIS["E-HYPOTHESIS"]
  ROOT --> E_HYPOTHESIS["E-HYPOTHESIS<br/>Hypothesis entity v0"]
  E_HYPOTHESIS -.-> E_CAPTURE_PLAN["E-CAPTURE-PLAN"]
  E_HYPOTHESIS -.-> E_SIGNAL["E-SIGNAL"]
  ROOT --> E_CAPTURE_PLAN["E-CAPTURE-PLAN<br/>CapturePlan entity v0"]
  E_CAPTURE_PLAN -.-> E_HYPOTHESIS["E-HYPOTHESIS"]
  E_CAPTURE_PLAN -.-> E_TOPIC_CARD["E-TOPIC-CARD"]
  ROOT --> E_TOPIC_CARD["E-TOPIC-CARD<br/>TopicCard / topic-card-lite"]
  E_TOPIC_CARD -.-> E_CAPTURE_PLAN["E-CAPTURE-PLAN"]
  E_TOPIC_CARD -.-> E_H5_CAPTURE_STATION["E-H5-CAPTURE-STATION"]
  ROOT --> E_H5_CAPTURE_STATION["E-H5-CAPTURE-STATION<br/>H5 Capture Station / strong visual s"]
  E_H5_CAPTURE_STATION -.-> E_BRIDGE_THIN_API["E-BRIDGE-THIN-API"]
  E_H5_CAPTURE_STATION -.-> E_SCOUTFLOW["E-SCOUTFLOW"]
  ROOT --> E_BRIDGE_THIN_API["E-BRIDGE-THIN-API<br/>Bridge / Thin API boundary"]
  E_BRIDGE_THIN_API -.-> E_H5_CAPTURE_STATION["E-H5-CAPTURE-STATION"]
  E_BRIDGE_THIN_API -.-> E_SCOUTFLOW["E-SCOUTFLOW"]
  ROOT --> E_VAULTWRITER["E-VAULTWRITER<br/>VaultWriter / vault preview-write sp"]
  E_VAULTWRITER -.-> E_BRIDGE_THIN_API["E-BRIDGE-THIN-API"]
  E_VAULTWRITER -.-> E_RECEIPT_LEDGER["E-RECEIPT-LEDGER"]
  ROOT --> E_RECEIPT_LEDGER["E-RECEIPT-LEDGER<br/>Receipt ledger / artifact_assets"]
  E_RECEIPT_LEDGER -.-> E_SCOUTFLOW["E-SCOUTFLOW"]
  E_RECEIPT_LEDGER -.-> E_TRUST_TRACE["E-TRUST-TRACE"]
  ROOT --> E_TRUST_TRACE["E-TRUST-TRACE<br/>Trust Trace / trace projection"]
  E_TRUST_TRACE -.-> E_RECEIPT_LEDGER["E-RECEIPT-LEDGER"]
  E_TRUST_TRACE -.-> E_SCOUTFLOW["E-SCOUTFLOW"]
```

## Node table

| node_id | title | risk | degree |
|---|---|---:|---:|
| `E-SCOUTFLOW` | ScoutFlow / 采集线 | critical | 8 |
| `E-RAW-VAULT` | RAW vault / 长期知识 SoR | critical | 5 |
| `E-DILOFLOW` | DiloFlow sibling consumer | medium | 4 |
| `E-CONTENTFLOW` | ContentFlow / L retrospective sibling source | medium | 4 |
| `E-USER-PROSUMER` | 用户：single-user prosumer / 最大马力 owner | critical | 7 |
| `E-AI-AGENTS` | AI agent mesh: GPT Pro / Codex / CC / Hermes / OpenClaw | high | 5 |
| `E-SIGNAL` | Signal entity v0 | high | 3 |
| `E-HYPOTHESIS` | Hypothesis entity v0 | high | 3 |
| `E-CAPTURE-PLAN` | CapturePlan entity v0 | high | 3 |
| `E-TOPIC-CARD` | TopicCard / topic-card-lite | critical | 9 |
| `E-H5-CAPTURE-STATION` | H5 Capture Station / strong visual surface | high | 6 |
| `E-BRIDGE-THIN-API` | Bridge / Thin API boundary | critical | 7 |
| `E-VAULTWRITER` | VaultWriter / vault preview-write split | critical | 9 |
| `E-RECEIPT-LEDGER` | Receipt ledger / artifact_assets | critical | 6 |
| `E-TRUST-TRACE` | Trust Trace / trace projection | high | 4 |

## Cluster reading guidance

Read this cluster with three questions. First, which nodes are canonical/promoted facts and which are candidate synthesis? Second, which nodes are approval gates rather than progress claims? Third, which nodes should be read before any new dispatch or implementation starts? For ScoutFlow, the answer almost always routes back through `R-CURRENT-TASK-DECISION`, `T-AUTHORITY-FIRST`, `T-CANDIDATE-NOT-AUTHORITY`, and `T-EXECUTION-GATES`.

The cluster is deliberately redundant with the master graph. Redundancy here is defensive: a cold-start reader may enter from entities, lessons, feedback, or risk. Every path should rediscover the same hard boundaries: frozen dispatch evidence, no runtime/migration/front-end/vault true-write approval by default, and no second knowledge base.

## Maintenance note

When a node is added or removed, regenerate this index from the adjacency JSON. Manual edits to cluster diagrams are discouraged because they are a common source of graph drift.
