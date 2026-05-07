---
title: Linked Decision and Runbook Attribution
status: candidate / supplementary / not-authority
created_at: 2026-05-07
---

# Linked Decision and Runbook Attribution

## Decision attribution map

| Decision / source | Graph nodes | Meaning |
|---|---|---|
| Step0 bootstrap / decision-log 2026-05-03 | `M-GIT-BOOTSTRAP`, `R-CURRENT-TASK-DECISION`, `T-AUTHORITY-FIRST` | 形成 repo authority 与薄账本起点 |
| T-P1A-001 manual_url metadata-only | `M-PHASE1A-MANUALURL`, `E-SCOUTFLOW`, `T-EXECUTION-GATES` | 当前 product baseline 很窄，不能自动变 runtime/audio |
| T-P1A-002 receipt ledger | `M-RECEIPT-LEDGER`, `E-RECEIPT-LEDGER`, `E-TRUST-TRACE` | evidence ledger 使状态可追溯 |
| T-P1A-013 Trust Trace | `M-TRUST-TRACE`, `E-TRUST-TRACE`, `P-API-AS-WRITE-BOUNDARY` | probe/receipt/capture/media readiness 分层 |
| PRD-v2/SRD-v2 promote | `M-PRD-SRD-V2`, `R-PRD-SRD-CONTRACTS`, `T-AUTHORITY-FIRST` | forward baseline and arbitration chain |
| PRD-v2.1 + SRD-v3 H5/Bridge addenda | `E-H5-CAPTURE-STATION`, `E-BRIDGE-THIN-API`, `E-VAULTWRITER`, `T-STRONG-VISUAL` | 强视觉与 H5/Bridge/Vault 进入 promoted planning，但不是 runtime/frontend/migration approval |
| Wave4 Batch2/3 landed | `M-WAVE4-BATCH2-BATCH3`, `P-VISUAL-REVIEW-5-GATE` | candidate surfaces landed, still gated |
| Dispatch127-176 frozen correction | `M-DISPATCH127-176-FROZEN`, `F-DISPATCH-FROZEN-CORRECTION`, `T-FROZEN-DISPATCH-EVIDENCE` | 历史包只能作为 evidence layer |
| Wave6 candidate open / no code-bearing gate | `M-WAVE6-CANDIDATE-OPEN`, `P-AUTHORITY-READBACK-BEFORE-WORK` | 后续必须新 dispatch + user gate |

## Runbook attribution map

| Runbook discipline | Graph nodes | Operational rule |
|---|---|---|
| Authority readback first | `P-AUTHORITY-READBACK-BEFORE-WORK`, `R-CURRENT-TASK-DECISION` | 当前状态以 live GitHub readback 为准，不以 ZIP snapshot 为准 |
| Frozen evidence handling | `P-FROZEN-DISPATCH-AS-EVIDENCE`, `R-DISPATCH127-176-PACK` | 读取 frozen pack 复盘，不重开、不改、不重跑 |
| Single authority writer | `T-PARALLEL-LANES`, `L-MULTIWINDOW-RACE`, `P-PR-FACTORY-LANE-SHAPING` | product lanes 可并行，authority write 必须串行 |
| API write boundary | `P-API-AS-WRITE-BOUNDARY`, `T-THIN-API-BOUNDARY`, `E-BRIDGE-THIN-API` | H5/worker/Bridge 不直写 authority |
| Preview-only vault | `T-PREVIEW-ONLY-VAULT`, `E-VAULTWRITER`, `L-VAULT-PREVIEW-AS-TRUE-WRITE` | preview/dry-run 不等于 true write |
| Claim labels | `P-SELF-AUDIT-CLAIM-LABELS`, `T-CANDIDATE-NOT-AUTHORITY` | 每个结论标 canonical/promoted/candidate/inference/unavailable |
| Product proof first | `T-PRODUCT-PROOF-NOT-BREADTH`, `P-PROOF-PAIR-CANARY`, `E-TOPIC-CARD` | post176 主线先做 topic-card proof canary |
| Overflow isolation | `T-OVERFLOW-REGISTRY`, `P-OVERFLOW-NOT-BLOCKER`, `L-MIGRATION-DRIFT` | blocked runtime/DB/migration 不挤占 proof |

## Anti-pattern attribution

| Anti-pattern | Nodes that guard against it | Stop line |
|---|---|---|
| AP-authority-drift | `L-AUTHORITY-DRIFT`, `L-CANDIDATE-PROMOTION`, `T-CANDIDATE-NOT-AUTHORITY` | research/draft/chat summary written as final authority |
| AP-runtime-drift | `L-RUNTIME-APPROVAL-DRIFT`, `T-EXECUTION-GATES` | BBDown/yt-dlp/ffmpeg/ASR/browser automation implied approved |
| AP-migration-drift | `L-MIGRATION-DRIFT`, `T-OVERFLOW-REGISTRY` | migration files or schema change started without explicit gate |
| AP-second-km | `L-SECOND-KNOWLEDGE-BASE`, `T-SCOUTFLOW-RAW-BOUNDARY`, `T-SECOND-KM-RISK` | ScoutFlow preview/RAW mirror/repo authority all treated as same truth |
| AP-proof-after-breadth | `L-PRODUCT-CLOSURE-MISTAKE`, `L-OVEROBJECTIFICATION`, `T-PRODUCT-PROOF-NOT-BREADTH` | more objects/specs before product proof |
| AP-multiwindow-race | `L-MULTIWINDOW-RACE`, `P-HANDOFF-COLD-START` | more than one authority writer, stale handoff, no readback delta |
| AP-token-overread | `L-TOKEN-BUDGET`, `MEMORY-EVOLUTION-TIMELINE` | transcript full-read or unmasked PII as shortcut |

## Cross-session attribution conclusion

The durable decision chain is: authority-first baseline → metadata-only scope → receipt/trust trace → H5/Bridge/Vault promoted planning → Wave4 candidate surfaces → Dispatch127-176 frozen evidence → Wave6 candidate open with no execution approval. The durable runbook chain is: read back live authority → preserve frozen evidence → run product proof pair → keep overflow isolated → write authority only through a serialized gate.
