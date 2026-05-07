---
title: MASTER MEMORY ATLAS — U16 Cross-Session Memory Graph
status: candidate / supplementary / not-authority
created_at: 2026-05-07
input_zip: ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip
input_prompt: cloud-prompt-U16-cross-session-memory-graph-2026-05-07.md
nodes_count: 79
edges_count: 225
---

# MASTER MEMORY ATLAS

本 atlas 是 U16 任务的可审计候选版：它把上传 ZIP、post176 四份输出、外部六份报告、repo source snapshot、RAW source snapshot、Dispatch127-176 manifest 与 GitHub connector readback 组织成一个 cross-session memory graph。它不是 authority，不替代原始 memory，不写回 `~/.claude`，不写回 GitHub authority docs，也不替代 RAW。它的目的只有一个：降低下一次冷启动和跨窗口协同时的重复发现成本，同时把 high-risk guard 固定在图谱边上。

## Source split

- **ZIP truth**：上传包内 100 个实际文件；其中 `02_repo_sources/docs/current.md` 是较早 Wave4 snapshot，不能当作现在 live authority。
- **GitHub live truth**：connector 已读取 `docs/decision-log.md`、`docs/current.md`、`docs/task-index.md`；live current 显示 Wave 6 candidate open / NOT_EXECUTION_APPROVED / no code-bearing next gate。
- **Prompt truth**：U16 prompt 明确要求 ≥60 nodes、candidate/not-authority、不能改本机 memory、jsonl 只能抽样、truthful stdout。
- **Unavailable local truth**：`~/.claude` memory、handoff trail、claude-mem SQLite/ChromaDB、jsonl transcript、ContentFlow/DiloFlow 本机 memory 在当前沙盒不可访问；本 atlas 不伪造这些来源。
- **Inference**：所有主题压缩、节点命名、cluster、lesson、pattern 都是 candidate synthesis。

## Counts

| kind | count |
|---|---:|
| entity | 15 |
| feedback | 10 |
| lesson | 12 |
| milestone | 10 |
| pattern | 12 |
| reference | 5 |
| theme | 15 |
| total nodes | 79 |
| graph edges | 225 |
| source files available from ZIP | 100 |

## Master graph

```mermaid
flowchart LR
  subgraph ENTITY["Entities"]
    E_SCOUTFLOW["E-SCOUTFLOW<br/>ScoutFlow / 采集线"]
    E_RAW_VAULT["E-RAW-VAULT<br/>RAW vault / 长期知识 SoR"]
    E_DILOFLOW["E-DILOFLOW<br/>DiloFlow sibling consumer"]
    E_CONTENTFLOW["E-CONTENTFLOW<br/>ContentFlow / L retrospective sibling source"]
    E_USER_PROSUMER["E-USER-PROSUMER<br/>用户：single-user prosumer / 最大马力 owner"]
    E_AI_AGENTS["E-AI-AGENTS<br/>AI agent mesh: GPT Pro / Codex / CC / Hermes"]
    E_SIGNAL["E-SIGNAL<br/>Signal entity v0"]
    E_HYPOTHESIS["E-HYPOTHESIS<br/>Hypothesis entity v0"]
    E_CAPTURE_PLAN["E-CAPTURE-PLAN<br/>CapturePlan entity v0"]
    E_TOPIC_CARD["E-TOPIC-CARD<br/>TopicCard / topic-card-lite"]
    E_H5_CAPTURE_STATION["E-H5-CAPTURE-STATION<br/>H5 Capture Station / strong visual surface"]
    E_BRIDGE_THIN_API["E-BRIDGE-THIN-API<br/>Bridge / Thin API boundary"]
    E_VAULTWRITER["E-VAULTWRITER<br/>VaultWriter / vault preview-write split"]
    E_RECEIPT_LEDGER["E-RECEIPT-LEDGER<br/>Receipt ledger / artifact_assets"]
    E_TRUST_TRACE["E-TRUST-TRACE<br/>Trust Trace / trace projection"]
  end
  subgraph THEME["Themes"]
    T_AUTHORITY_FIRST["T-AUTHORITY-FIRST<br/>Authority-first 四层与 SoR discipline"]
    T_MAX_HORSEPOWER["T-MAX-HORSEPOWER<br/>最大马力开发 / 安全前提下并行"]
    T_STRONG_VISUAL["T-STRONG-VISUAL<br/>强视觉一级 axis / 5-Gate aesthetic"]
    T_SINGLE_USER_LOCAL_FIRST["T-SINGLE-USER-LOCAL-FIRST<br/>single-user / local-first 产品边界"]
    T_CANDIDATE_NOT_AUTHORITY["T-CANDIDATE-NOT-AUTHORITY<br/>candidate/not-authority discipline"]
    T_EXECUTION_GATES["T-EXECUTION-GATES<br/>runtime / migration / frontend / visual gate"]
    T_PRODUCT_PROOF_NOT_BREADTH["T-PRODUCT-PROOF-NOT-BREADTH<br/>post176 主线：proof not breadth"]
    T_SCOUTFLOW_RAW_BOUNDARY["T-SCOUTFLOW-RAW-BOUNDARY<br/>ScoutFlow ↔ RAW SoR boundary"]
    T_PARALLEL_LANES["T-PARALLEL-LANES<br/>3 product lanes + 1 authority writer"]
    T_OVERFLOW_REGISTRY["T-OVERFLOW-REGISTRY<br/>overflow registry / blocked lanes discipline"]
    T_PREVIEW_ONLY_VAULT["T-PREVIEW-ONLY-VAULT<br/>preview-only / write_enabled=False boundary"]
    T_RUNBOOK_READBACK["T-RUNBOOK-READBACK<br/>readback delta / runbook discipline"]
    T_THIN_API_BOUNDARY["T-THIN-API-BOUNDARY<br/>Thin API is the only write channel"]
    T_SECOND_KM_RISK["T-SECOND-KM-RISK<br/>第二知识库风险 / mirror drift"]
    T_FROZEN_DISPATCH_EVIDENCE["T-FROZEN-DISPATCH-EVIDENCE<br/>Dispatch126-176 frozen history, not reopenin"]
  end
  subgraph PATTERN["Patterns"]
    P_AUTHORITY_READBACK_BEFORE_WORK["P-AUTHORITY-READBACK-BEFORE-WORK<br/>先读 authority，再开工"]
    P_FROZEN_DISPATCH_AS_EVIDENCE["P-FROZEN-DISPATCH-AS-EVIDENCE<br/>冻结 dispatch 作为 evidence layer"]
    P_PROOF_PAIR_CANARY["P-PROOF-PAIR-CANARY<br/>Topic-card proof pair canary"]
    P_OBJECTS_AFTER_PROOF["P-OBJECTS-AFTER-PROOF<br/>先 proof 后对象化扩张"]
    P_API_AS_WRITE_BOUNDARY["P-API-AS-WRITE-BOUNDARY<br/>API-as-write-boundary"]
    P_LOCAL_ONLY_AUTH_SAFETY["P-LOCAL-ONLY-AUTH-SAFETY<br/>local-only auth / credential isolation"]
    P_PR_FACTORY_LANE_SHAPING["P-PR-FACTORY-LANE-SHAPING<br/>PR Factory lane shaping"]
    P_OVERFLOW_NOT_BLOCKER["P-OVERFLOW-NOT-BLOCKER<br/>Overflow captures options without blocking p"]
    P_DUAL_TRUTH_SEPARATION["P-DUAL-TRUTH-SEPARATION<br/>Zip truth / GitHub live truth / RAW truth se"]
    P_VISUAL_REVIEW_5_GATE["P-VISUAL-REVIEW-5-GATE<br/>5-Gate visual review"]
    P_HANDOFF_COLD_START["P-HANDOFF-COLD-START<br/>cold-start handoff packet"]
    P_SELF_AUDIT_CLAIM_LABELS["P-SELF-AUDIT-CLAIM-LABELS<br/>claim labels + self-audit as anti-drift"]
  end
  subgraph LESSON["Lessons"]
    L_AUTHORITY_DRIFT["L-AUTHORITY-DRIFT<br/>踩坑：authority drift"]
    L_RUNTIME_APPROVAL_DRIFT["L-RUNTIME-APPROVAL-DRIFT<br/>踩坑：runtime approval drift"]
    L_MIGRATION_DRIFT["L-MIGRATION-DRIFT<br/>踩坑：DB/migration 被 candidate 偷渡"]
    L_VAULT_PREVIEW_AS_TRUE_WRITE["L-VAULT-PREVIEW-AS-TRUE-WRITE<br/>踩坑：把 vault preview 当 true write"]
    L_SECOND_KNOWLEDGE_BASE["L-SECOND-KNOWLEDGE-BASE<br/>踩坑：第二知识库 / mirror truth"]
    L_HANDOFF_OVERLONG["L-HANDOFF-OVERLONG<br/>踩坑：handoff 过长但不可执行"]
    L_CANDIDATE_PROMOTION["L-CANDIDATE-PROMOTION<br/>踩坑：candidate 漂移成 authority"]
    L_MULTIWINDOW_RACE["L-MULTIWINDOW-RACE<br/>踩坑：多窗口 race / authority writer 冲突"]
    L_TOKEN_BUDGET["L-TOKEN-BUDGET<br/>踩坑：token over budget / 全量读取错觉"]
    L_BILIBILI_CRED_RISK["L-BILIBILI-CRED-RISK<br/>踩坑：Bilibili / credential / C&D 风险"]
    L_PRODUCT_CLOSURE_MISTAKE["L-PRODUCT-CLOSURE-MISTAKE<br/>踩坑：工程闭环误当产品闭环"]
    L_OVEROBJECTIFICATION["L-OVEROBJECTIFICATION<br/>踩坑：过早对象化 / 单人 prosumer 工具链膨胀"]
  end
  subgraph MILESTONE["Milestones"]
    M_GIT_BOOTSTRAP["M-GIT-BOOTSTRAP<br/>2026-05-03 GitHub bootstrap / Step0 baseline"]
    M_PHASE1A_MANUALURL["M-PHASE1A-MANUALURL<br/>Phase 1A manual_url metadata-only authorized"]
    M_RECEIPT_LEDGER["M-RECEIPT-LEDGER<br/>Receipt ledger / artifact_assets baseline"]
    M_TRUST_TRACE["M-TRUST-TRACE<br/>Trust Trace API surface completed"]
    M_PRD_SRD_V2["M-PRD-SRD-V2<br/>PRD-v2 / SRD-v2 promoted"]
    M_WAVE2_CLOSE["M-WAVE2-CLOSE<br/>Wave 2 closed / authority reconciliation"]
    M_WAVE3B_H5_BRIDGE_VAULT["M-WAVE3B-H5-BRIDGE-VAULT<br/>Wave 3B H5 / Bridge / Vault planning landed"]
    M_WAVE4_BATCH2_BATCH3["M-WAVE4-BATCH2-BATCH3<br/>Wave 4 Batch2/3 app+service candidate surfac"]
    M_DISPATCH127_176_FROZEN["M-DISPATCH127-176-FROZEN<br/>Dispatch126-176 executed and frozen"]
    M_WAVE6_CANDIDATE_OPEN["M-WAVE6-CANDIDATE-OPEN<br/>Wave 6 candidate open / no code-bearing next"]
  end
  subgraph FEEDBACK["Feedback"]
    F_MAX_HORSEPOWER["F-MAX-HORSEPOWER<br/>用户反馈：最大化马力 / 最大效率"]
    F_LOOSER_NOT_CEREMONY["F-LOOSER-NOT-CEREMONY<br/>用户反馈：松一点，不堆 ceremony"]
    F_STRONG_VISUAL_FIRST_CLASS["F-STRONG-VISUAL-FIRST-CLASS<br/>用户反馈：强视觉是一级轴"]
    F_SAFE_PARALLEL["F-SAFE-PARALLEL<br/>用户反馈：安全前提下最大并行"]
    F_GPT_PRO_AS_WORKER["F-GPT-PRO-AS-WORKER<br/>用户反馈：用 GPT Pro 干活"]
    F_AMEND_AND_PROCEED["F-AMEND-AND-PROCEED<br/>用户反馈：amend_and_proceed"]
    F_DIRECT_MERGE_OK["F-DIRECT-MERGE-OK<br/>用户反馈：可直 merge，但要不越界"]
    F_NOT_HEAVY_KM["F-NOT-HEAVY-KM<br/>用户反馈：不要重 KM / 第二知识库"]
    F_SINGLE_USER_PROSUMER["F-SINGLE-USER-PROSUMER<br/>用户反馈：单人 prosumer max horsepower"]
    F_DISPATCH_FROZEN_CORRECTION["F-DISPATCH-FROZEN-CORRECTION<br/>用户反馈：126-176 已执行冻结"]
  end
  subgraph REFERENCE["References"]
    R_PRD_SRD_CONTRACTS["R-PRD-SRD-CONTRACTS<br/>PRD/SRD/contracts authority stack"]
    R_CURRENT_TASK_DECISION["R-CURRENT-TASK-DECISION<br/>current/task-index/decision-log live readbac"]
    R_DISPATCH127_176_PACK["R-DISPATCH127-176-PACK<br/>Dispatch127-176 autoexec frozen pack"]
    R_RAW_SYSTEM_RULES["R-RAW-SYSTEM-RULES<br/>RAW system rules and frontmatter contracts"]
    R_EXTERNAL_SIX_REPORTS["R-EXTERNAL-SIX-REPORTS<br/>Six external reports as candidate research c"]
  end
  E_AI_AGENTS ---|entity_sequence| E_SIGNAL
  E_AI_AGENTS ---|entity_sequence| E_USER_PROSUMER
  E_AI_AGENTS ---|semantic| P_HANDOFF_COLD_START
  E_AI_AGENTS ---|entity_theme| T_AUTHORITY_FIRST
  E_AI_AGENTS ---|semantic| T_PARALLEL_LANES
  E_BRIDGE_THIN_API ---|entity_sequence| E_H5_CAPTURE_STATION
  E_BRIDGE_THIN_API ---|semantic| E_SCOUTFLOW
  E_BRIDGE_THIN_API ---|entity_sequence| E_VAULTWRITER
  E_BRIDGE_THIN_API ---|semantic| M_WAVE3B_H5_BRIDGE_VAULT
  E_BRIDGE_THIN_API ---|entity_theme| T_AUTHORITY_FIRST
  E_BRIDGE_THIN_API ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  E_BRIDGE_THIN_API ---|api_boundary| T_THIN_API_BOUNDARY
  E_CAPTURE_PLAN ---|entity_sequence| E_HYPOTHESIS
  E_CAPTURE_PLAN ---|semantic| E_HYPOTHESIS
  E_CAPTURE_PLAN ---|entity_sequence| E_TOPIC_CARD
  E_CAPTURE_PLAN ---|semantic| E_TOPIC_CARD
  E_CAPTURE_PLAN ---|entity_theme| T_AUTHORITY_FIRST
  E_CONTENTFLOW ---|entity_sequence| E_DILOFLOW
  E_CONTENTFLOW ---|semantic| E_DILOFLOW
  E_CONTENTFLOW ---|entity_sequence| E_USER_PROSUMER
  E_CONTENTFLOW ---|semantic| P_SELF_AUDIT_CLAIM_LABELS
  E_CONTENTFLOW ---|entity_theme| T_AUTHORITY_FIRST
  E_DILOFLOW ---|entity_sequence| E_RAW_VAULT
  E_DILOFLOW ---|entity_theme| T_AUTHORITY_FIRST
  E_DILOFLOW ---|semantic| T_SECOND_KM_RISK
  E_H5_CAPTURE_STATION ---|semantic| E_SCOUTFLOW
  E_H5_CAPTURE_STATION ---|entity_sequence| E_TOPIC_CARD
  E_H5_CAPTURE_STATION ---|semantic| M_WAVE3B_H5_BRIDGE_VAULT
  E_H5_CAPTURE_STATION ---|entity_theme| T_AUTHORITY_FIRST
  E_H5_CAPTURE_STATION ---|visual| T_STRONG_VISUAL
  E_HYPOTHESIS ---|entity_sequence| E_SIGNAL
  E_HYPOTHESIS ---|semantic| E_SIGNAL
  E_HYPOTHESIS ---|entity_theme| T_AUTHORITY_FIRST
  E_RAW_VAULT ---|entity_sequence| E_SCOUTFLOW
  E_RAW_VAULT ---|semantic| E_SCOUTFLOW
  E_RAW_VAULT ---|entity_theme| T_AUTHORITY_FIRST
  E_RAW_VAULT ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  E_RAW_VAULT ---|boundary| T_SCOUTFLOW_RAW_BOUNDARY
  E_RECEIPT_LEDGER ---|semantic| E_SCOUTFLOW
  E_RECEIPT_LEDGER ---|entity_sequence| E_TRUST_TRACE
  E_RECEIPT_LEDGER ---|entity_sequence| E_VAULTWRITER
  E_RECEIPT_LEDGER ---|semantic| M_PHASE1A_MANUALURL
  E_RECEIPT_LEDGER ---|entity_theme| T_AUTHORITY_FIRST
  E_RECEIPT_LEDGER ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  E_SCOUTFLOW ---|semantic| E_TRUST_TRACE
  E_SCOUTFLOW ---|semantic| E_VAULTWRITER
  E_SCOUTFLOW ---|entity_theme| T_AUTHORITY_FIRST
  E_SCOUTFLOW ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  E_SIGNAL ---|entity_theme| T_AUTHORITY_FIRST
  E_TOPIC_CARD ---|semantic| E_TRUST_TRACE
  E_TOPIC_CARD ---|semantic| E_VAULTWRITER
  E_TOPIC_CARD ---|semantic| P_PROOF_PAIR_CANARY
  E_TOPIC_CARD ---|entity_theme| T_AUTHORITY_FIRST
  E_TOPIC_CARD ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  E_TOPIC_CARD ---|boundary| T_SCOUTFLOW_RAW_BOUNDARY
  E_TOPIC_CARD ---|visual| T_STRONG_VISUAL
  E_TRUST_TRACE ---|entity_theme| T_AUTHORITY_FIRST
  E_USER_PROSUMER ---|semantic| F_MAX_HORSEPOWER
  E_USER_PROSUMER ---|entity_theme| T_AUTHORITY_FIRST
  E_USER_PROSUMER ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  E_USER_PROSUMER ---|semantic| T_MAX_HORSEPOWER
  E_USER_PROSUMER ---|semantic| T_SINGLE_USER_LOCAL_FIRST
  E_VAULTWRITER ---|semantic| M_WAVE3B_H5_BRIDGE_VAULT
  E_VAULTWRITER ---|entity_theme| T_AUTHORITY_FIRST
  E_VAULTWRITER ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  E_VAULTWRITER ---|boundary| T_SCOUTFLOW_RAW_BOUNDARY
  E_VAULTWRITER ---|api_boundary| T_THIN_API_BOUNDARY
  F_AMEND_AND_PROCEED ---|feedback_sequence| F_DIRECT_MERGE_OK
  F_AMEND_AND_PROCEED ---|feedback_sequence| F_GPT_PRO_AS_WORKER
  F_AMEND_AND_PROCEED ---|anti_orphan| T_AUTHORITY_FIRST
  F_DIRECT_MERGE_OK ---|feedback_sequence| F_NOT_HEAVY_KM
  F_DIRECT_MERGE_OK ---|anti_orphan| T_AUTHORITY_FIRST
  F_DISPATCH_FROZEN_CORRECTION ---|feedback_sequence| F_SINGLE_USER_PROSUMER
  F_DISPATCH_FROZEN_CORRECTION ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  F_DISPATCH_FROZEN_CORRECTION ---|semantic| T_FROZEN_DISPATCH_EVIDENCE
  F_DISPATCH_FROZEN_CORRECTION ---|frozen| T_FROZEN_DISPATCH_EVIDENCE
  F_GPT_PRO_AS_WORKER ---|feedback_sequence| F_SAFE_PARALLEL
  F_GPT_PRO_AS_WORKER ---|anti_orphan| T_AUTHORITY_FIRST
  F_LOOSER_NOT_CEREMONY ---|feedback_sequence| F_MAX_HORSEPOWER
  F_LOOSER_NOT_CEREMONY ---|feedback_sequence| F_STRONG_VISUAL_FIRST_CLASS
  F_LOOSER_NOT_CEREMONY ---|anti_orphan| T_AUTHORITY_FIRST
  F_MAX_HORSEPOWER ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  F_NOT_HEAVY_KM ---|feedback_sequence| F_SINGLE_USER_PROSUMER
  F_NOT_HEAVY_KM ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  F_NOT_HEAVY_KM ---|semantic| T_SECOND_KM_RISK
  F_SAFE_PARALLEL ---|feedback_sequence| F_STRONG_VISUAL_FIRST_CLASS
  F_SAFE_PARALLEL ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  F_SAFE_PARALLEL ---|semantic| T_PARALLEL_LANES
  F_SAFE_PARALLEL ---|api_boundary| T_THIN_API_BOUNDARY
  F_SINGLE_USER_PROSUMER ---|semantic| T_SINGLE_USER_LOCAL_FIRST
  F_STRONG_VISUAL_FIRST_CLASS ---|semantic| T_STRONG_VISUAL
  F_STRONG_VISUAL_FIRST_CLASS ---|visual| T_STRONG_VISUAL
  L_AUTHORITY_DRIFT ---|lesson_sequence| L_RUNTIME_APPROVAL_DRIFT
  L_AUTHORITY_DRIFT ---|semantic| T_AUTHORITY_FIRST
  L_AUTHORITY_DRIFT ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  L_BILIBILI_CRED_RISK ---|lesson_sequence| L_PRODUCT_CLOSURE_MISTAKE
  L_BILIBILI_CRED_RISK ---|lesson_sequence| L_TOKEN_BUDGET
  L_BILIBILI_CRED_RISK ---|semantic| P_LOCAL_ONLY_AUTH_SAFETY
  L_BILIBILI_CRED_RISK ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  L_CANDIDATE_PROMOTION ---|lesson_sequence| L_HANDOFF_OVERLONG
  L_CANDIDATE_PROMOTION ---|lesson_sequence| L_MULTIWINDOW_RACE
  L_CANDIDATE_PROMOTION ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  L_CANDIDATE_PROMOTION ---|semantic| T_CANDIDATE_NOT_AUTHORITY
  L_HANDOFF_OVERLONG ---|lesson_sequence| L_SECOND_KNOWLEDGE_BASE
  L_HANDOFF_OVERLONG ---|anti_orphan| T_AUTHORITY_FIRST
  L_MIGRATION_DRIFT ---|lesson_sequence| L_RUNTIME_APPROVAL_DRIFT
  L_MIGRATION_DRIFT ---|lesson_sequence| L_VAULT_PREVIEW_AS_TRUE_WRITE
  L_MIGRATION_DRIFT ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  L_MIGRATION_DRIFT ---|semantic| T_EXECUTION_GATES
  L_MIGRATION_DRIFT ---|approval_gate| T_EXECUTION_GATES
  L_MULTIWINDOW_RACE ---|lesson_sequence| L_TOKEN_BUDGET
  L_MULTIWINDOW_RACE ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  L_MULTIWINDOW_RACE ---|semantic| T_PARALLEL_LANES
  L_MULTIWINDOW_RACE ---|api_boundary| T_THIN_API_BOUNDARY
  L_OVEROBJECTIFICATION ---|lesson_sequence| L_PRODUCT_CLOSURE_MISTAKE
  L_OVEROBJECTIFICATION ---|semantic| P_OBJECTS_AFTER_PROOF
  L_OVEROBJECTIFICATION ---|anti_orphan| T_AUTHORITY_FIRST
  L_PRODUCT_CLOSURE_MISTAKE ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  L_PRODUCT_CLOSURE_MISTAKE ---|semantic| T_PRODUCT_PROOF_NOT_BREADTH
  L_RUNTIME_APPROVAL_DRIFT ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  L_RUNTIME_APPROVAL_DRIFT ---|semantic| T_EXECUTION_GATES
  L_RUNTIME_APPROVAL_DRIFT ---|approval_gate| T_EXECUTION_GATES
  L_SECOND_KNOWLEDGE_BASE ---|lesson_sequence| L_VAULT_PREVIEW_AS_TRUE_WRITE
  L_SECOND_KNOWLEDGE_BASE ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  L_SECOND_KNOWLEDGE_BASE ---|semantic| T_SCOUTFLOW_RAW_BOUNDARY
  L_TOKEN_BUDGET ---|anti_orphan| T_AUTHORITY_FIRST
  L_VAULT_PREVIEW_AS_TRUE_WRITE ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  L_VAULT_PREVIEW_AS_TRUE_WRITE ---|semantic| T_PREVIEW_ONLY_VAULT
  L_VAULT_PREVIEW_AS_TRUE_WRITE ---|boundary| T_SCOUTFLOW_RAW_BOUNDARY
  L_VAULT_PREVIEW_AS_TRUE_WRITE ---|api_boundary| T_THIN_API_BOUNDARY
  M_DISPATCH127_176_FROZEN ---|milestone_sequence| M_WAVE4_BATCH2_BATCH3
  M_DISPATCH127_176_FROZEN ---|milestone_sequence| M_WAVE6_CANDIDATE_OPEN
  M_DISPATCH127_176_FROZEN ---|semantic| P_FROZEN_DISPATCH_AS_EVIDENCE
  M_DISPATCH127_176_FROZEN ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  M_DISPATCH127_176_FROZEN ---|frozen| T_FROZEN_DISPATCH_EVIDENCE
  M_GIT_BOOTSTRAP ---|milestone_sequence| M_PHASE1A_MANUALURL
  M_GIT_BOOTSTRAP ---|anti_orphan| T_AUTHORITY_FIRST
  M_GIT_BOOTSTRAP ---|anti_orphan| T_CANDIDATE_NOT_AUTHORITY
  M_PHASE1A_MANUALURL ---|milestone_sequence| M_RECEIPT_LEDGER
  M_PHASE1A_MANUALURL ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  M_PRD_SRD_V2 ---|milestone_sequence| M_TRUST_TRACE
  M_PRD_SRD_V2 ---|milestone_sequence| M_WAVE2_CLOSE
  M_PRD_SRD_V2 ---|semantic| R_PRD_SRD_CONTRACTS
  M_PRD_SRD_V2 ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  M_RECEIPT_LEDGER ---|semantic| M_TRUST_TRACE
  M_RECEIPT_LEDGER ---|milestone_sequence| M_TRUST_TRACE
  M_RECEIPT_LEDGER ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  M_TRUST_TRACE ---|anti_orphan| T_AUTHORITY_FIRST
  M_WAVE2_CLOSE ---|milestone_sequence| M_WAVE3B_H5_BRIDGE_VAULT
  M_WAVE2_CLOSE ---|anti_orphan| T_AUTHORITY_FIRST
  M_WAVE3B_H5_BRIDGE_VAULT ---|milestone_sequence| M_WAVE4_BATCH2_BATCH3
  M_WAVE3B_H5_BRIDGE_VAULT ---|boundary| T_SCOUTFLOW_RAW_BOUNDARY
  M_WAVE3B_H5_BRIDGE_VAULT ---|visual| T_STRONG_VISUAL
  M_WAVE4_BATCH2_BATCH3 ---|semantic| T_STRONG_VISUAL
  M_WAVE6_CANDIDATE_OPEN ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  M_WAVE6_CANDIDATE_OPEN ---|semantic| T_FROZEN_DISPATCH_EVIDENCE
  P_API_AS_WRITE_BOUNDARY ---|pattern_sequence| P_LOCAL_ONLY_AUTH_SAFETY
  P_API_AS_WRITE_BOUNDARY ---|pattern_sequence| P_OBJECTS_AFTER_PROOF
  P_API_AS_WRITE_BOUNDARY ---|semantic| T_AUTHORITY_FIRST
  P_API_AS_WRITE_BOUNDARY ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  P_API_AS_WRITE_BOUNDARY ---|api_boundary| T_THIN_API_BOUNDARY
  P_AUTHORITY_READBACK_BEFORE_WORK ---|pattern_sequence| P_FROZEN_DISPATCH_AS_EVIDENCE
  P_AUTHORITY_READBACK_BEFORE_WORK ---|semantic| R_CURRENT_TASK_DECISION
  P_AUTHORITY_READBACK_BEFORE_WORK ---|semantic| T_AUTHORITY_FIRST
  P_AUTHORITY_READBACK_BEFORE_WORK ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  P_DUAL_TRUTH_SEPARATION ---|pattern_sequence| P_OVERFLOW_NOT_BLOCKER
  P_DUAL_TRUTH_SEPARATION ---|pattern_sequence| P_VISUAL_REVIEW_5_GATE
  P_DUAL_TRUTH_SEPARATION ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  P_DUAL_TRUTH_SEPARATION ---|boundary| T_SCOUTFLOW_RAW_BOUNDARY
  P_FROZEN_DISPATCH_AS_EVIDENCE ---|pattern_sequence| P_PROOF_PAIR_CANARY
  P_FROZEN_DISPATCH_AS_EVIDENCE ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  P_FROZEN_DISPATCH_AS_EVIDENCE ---|frozen| T_FROZEN_DISPATCH_EVIDENCE
  P_HANDOFF_COLD_START ---|pattern_sequence| P_SELF_AUDIT_CLAIM_LABELS
  P_HANDOFF_COLD_START ---|pattern_sequence| P_VISUAL_REVIEW_5_GATE
  P_HANDOFF_COLD_START ---|semantic| T_RUNBOOK_READBACK
  P_LOCAL_ONLY_AUTH_SAFETY ---|pattern_sequence| P_PR_FACTORY_LANE_SHAPING
  P_LOCAL_ONLY_AUTH_SAFETY ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  P_OBJECTS_AFTER_PROOF ---|pattern_sequence| P_PROOF_PAIR_CANARY
  P_OVERFLOW_NOT_BLOCKER ---|pattern_sequence| P_PR_FACTORY_LANE_SHAPING
  P_OVERFLOW_NOT_BLOCKER ---|approval_gate| T_EXECUTION_GATES
  P_PR_FACTORY_LANE_SHAPING ---|api_boundary| T_THIN_API_BOUNDARY
  P_PROOF_PAIR_CANARY ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  P_PROOF_PAIR_CANARY ---|semantic| T_PRODUCT_PROOF_NOT_BREADTH
  P_PROOF_PAIR_CANARY ---|visual| T_STRONG_VISUAL
  P_SELF_AUDIT_CLAIM_LABELS ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  P_VISUAL_REVIEW_5_GATE ---|visual| T_STRONG_VISUAL
  R_CURRENT_TASK_DECISION ---|reference_sequence| R_DISPATCH127_176_PACK
  R_CURRENT_TASK_DECISION ---|reference_sequence| R_PRD_SRD_CONTRACTS
  R_CURRENT_TASK_DECISION ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  R_DISPATCH127_176_PACK ---|reference_sequence| R_RAW_SYSTEM_RULES
  R_DISPATCH127_176_PACK ---|frozen| T_FROZEN_DISPATCH_EVIDENCE
  R_DISPATCH127_176_PACK ---|semantic| T_FROZEN_DISPATCH_EVIDENCE
  R_EXTERNAL_SIX_REPORTS ---|reference_sequence| R_RAW_SYSTEM_RULES
  R_EXTERNAL_SIX_REPORTS ---|anti_orphan| T_AUTHORITY_FIRST
  R_EXTERNAL_SIX_REPORTS ---|semantic| T_PRODUCT_PROOF_NOT_BREADTH
  R_PRD_SRD_CONTRACTS ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  R_RAW_SYSTEM_RULES ---|boundary| T_SCOUTFLOW_RAW_BOUNDARY
  R_RAW_SYSTEM_RULES ---|semantic| T_SCOUTFLOW_RAW_BOUNDARY
  T_AUTHORITY_FIRST ---|risk_guard| T_CANDIDATE_NOT_AUTHORITY
  T_AUTHORITY_FIRST ---|theme_sequence| T_MAX_HORSEPOWER
  T_CANDIDATE_NOT_AUTHORITY ---|risk_guard| T_EXECUTION_GATES
  T_CANDIDATE_NOT_AUTHORITY ---|theme_sequence| T_EXECUTION_GATES
  T_CANDIDATE_NOT_AUTHORITY ---|risk_guard| T_FROZEN_DISPATCH_EVIDENCE
  T_CANDIDATE_NOT_AUTHORITY ---|risk_guard| T_PARALLEL_LANES
  T_CANDIDATE_NOT_AUTHORITY ---|risk_guard| T_PREVIEW_ONLY_VAULT
  T_CANDIDATE_NOT_AUTHORITY ---|risk_guard| T_PRODUCT_PROOF_NOT_BREADTH
  T_CANDIDATE_NOT_AUTHORITY ---|risk_guard| T_SCOUTFLOW_RAW_BOUNDARY
  T_CANDIDATE_NOT_AUTHORITY ---|risk_guard| T_SECOND_KM_RISK
  T_CANDIDATE_NOT_AUTHORITY ---|theme_sequence| T_SINGLE_USER_LOCAL_FIRST
  T_CANDIDATE_NOT_AUTHORITY ---|risk_guard| T_THIN_API_BOUNDARY
  T_EXECUTION_GATES ---|approval_gate| T_OVERFLOW_REGISTRY
  T_EXECUTION_GATES ---|theme_sequence| T_PRODUCT_PROOF_NOT_BREADTH
  T_FROZEN_DISPATCH_EVIDENCE ---|theme_sequence| T_SECOND_KM_RISK
  T_MAX_HORSEPOWER ---|theme_sequence| T_STRONG_VISUAL
  T_OVERFLOW_REGISTRY ---|theme_sequence| T_PARALLEL_LANES
  T_OVERFLOW_REGISTRY ---|theme_sequence| T_PREVIEW_ONLY_VAULT
  T_PARALLEL_LANES ---|theme_sequence| T_SCOUTFLOW_RAW_BOUNDARY
  T_PARALLEL_LANES ---|api_boundary| T_THIN_API_BOUNDARY
  T_PREVIEW_ONLY_VAULT ---|theme_sequence| T_RUNBOOK_READBACK
  T_PREVIEW_ONLY_VAULT ---|boundary| T_SCOUTFLOW_RAW_BOUNDARY
  T_PREVIEW_ONLY_VAULT ---|api_boundary| T_THIN_API_BOUNDARY
  T_PRODUCT_PROOF_NOT_BREADTH ---|theme_sequence| T_SCOUTFLOW_RAW_BOUNDARY
  T_RUNBOOK_READBACK ---|theme_sequence| T_THIN_API_BOUNDARY
  T_SECOND_KM_RISK ---|theme_sequence| T_THIN_API_BOUNDARY
  T_SINGLE_USER_LOCAL_FIRST ---|theme_sequence| T_STRONG_VISUAL
```

## Core reading order

1. 先读 `T-FROZEN-DISPATCH-EVIDENCE` 与 `F-DISPATCH-FROZEN-CORRECTION`，因为用户最高优先级修正是 Dispatch126-176 已执行并冻结，不能重开。
2. 再读 `R-CURRENT-TASK-DECISION` 与 `P-AUTHORITY-READBACK-BEFORE-WORK`，因为 live GitHub truth 与 ZIP current snapshot 不一致时，必须以 live authority 为准。
3. 再读 `T-PRODUCT-PROOF-NOT-BREADTH`、`P-PROOF-PAIR-CANARY`、`E-TOPIC-CARD`，这是 post176 后真正可接主线的最短 proof 路径。
4. 最后读 `T-SCOUTFLOW-RAW-BOUNDARY`、`T-PREVIEW-ONLY-VAULT`、`T-SECOND-KM-RISK`，确保 product proof 不误变成第二知识库或 vault true-write。

## Top synthesis

本次复盘的主结论是：ScoutFlow 176 后不应默认继续扩大 spec/object breadth，而应围绕产品 proof 重新收束。最强 canary 是 topic-card-lite / vault preview / RAW handoff 组合：它能同时检验 H5 strong visual、Trust Trace provenance、Vault preview shape、RAW 00-Inbox candidate material 与用户 review 的真实循环。Signal/Hypothesis/CapturePlan 不是要丢弃，而是先保留为候选对象和 evidence vocabulary；在 product proof 成立前，不宜把它们全部升级为 DB authority 或大量 frontend surface。

这一路线与最大马力并不冲突。相反，最大马力应当被重新定义为：product proof lane 前置，research/audit/prototype lanes 辅助，authority writer 串行，overflow 收纳 blocked runtime/migration/DB package strategy。这样能避免“安全地做很多无价值候选文档”的内耗，也能避免“为了快把 runtime/migration/front-end/vault true-write gate 偷渡打开”的风险。

## Boundary reminder

所有 node frontmatter 都含 source_path、linked_nodes、risk_if_forgotten、claim_label、linked_decision/runbook/anti_pattern 字段。link 已双向化，adjacency JSON 与 Mermaid 使用同一 edge set。任何后续维护者都应先改 JSON/source map，再生成 node 与 Mermaid，避免图谱漂移。
