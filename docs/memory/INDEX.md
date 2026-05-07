---
title: ScoutFlow Cross-Session Memory Index
status: current authority
purpose: 跨 vendor 可读的 instinct memory 入口 (CC0 / CC1 / Codex / GPT Pro 云端 / Hermes 共享)
created_at: 2026-05-07
source_atlas: docs/research/strategic-upgrade/2026-05-07/outputs/U16-memory-graph/MASTER-MEMORY-ATLAS.md
batch_count: 17
---

# ScoutFlow Cross-Session Memory Index

> 本目录是 ScoutFlow 跨 vendor 可读的 instinct memory. 所有 vendor 通过 git tracked path 读, 不依赖 ~/.claude/.

## 跨 vendor 读法

| Vendor | 读法 |
|---|---|
| CC0 / CC1 (Claude Code) | Read 本目录文件; 也可从 `~/.claude/projects/-Users-wanglei-workspace-ScoutFlow/memory/` 读现有 19 条 (双源, 平行) |
| Codex CLI | Read 本目录文件 (clone repo 即有) |
| Cloud GPT Pro | 战友 paste GitHub raw URL, e.g. `https://github.com/RayWong1990/ScoutFlow/blob/main/docs/memory/lessons/L-CANDIDATE-PROMOTION.md` |
| Hermes | 同 GPT Pro |

## 第一批 17 条 (W2D U16 ingest, 2026-05-07; +1 post-Layer-2-audit fix L-AUTHORITY-DRIFT)

### Lessons (踩坑教训, 7 条)

| ID | 短名 | 风险 | 路径 |
|---|---|---|---|
| L-AUTHORITY-DRIFT | authority-drift | critical | `lessons/L-AUTHORITY-DRIFT.md` |
| L-CANDIDATE-PROMOTION | candidate-promotion-discipline | critical | `lessons/L-CANDIDATE-PROMOTION.md` |
| L-RUNTIME-APPROVAL-DRIFT | runtime-approval-drift | critical | `lessons/L-RUNTIME-APPROVAL-DRIFT.md` |
| L-MIGRATION-DRIFT | migration-drift | critical | `lessons/L-MIGRATION-DRIFT.md` |
| L-PRODUCT-CLOSURE-MISTAKE | product-closure-not-engineering | critical | `lessons/L-PRODUCT-CLOSURE-MISTAKE.md` |
| L-OVEROBJECTIFICATION | over-objectification | high | `lessons/L-OVEROBJECTIFICATION.md` |
| L-HANDOFF-OVERLONG | handoff-overlong | medium | `lessons/L-HANDOFF-OVERLONG.md` |

### Feedback (用户偏好, 5 条)

| ID | 短名 | 路径 |
|---|---|---|
| F-STRONG-VISUAL-FIRST-CLASS | strong-visual-first-class-axis | `feedback/F-STRONG-VISUAL-FIRST-CLASS.md` |
| F-DIRECT-MERGE-OK | direct-merge-ok-not-cross-boundary | `feedback/F-DIRECT-MERGE-OK.md` |
| F-NOT-HEAVY-KM | not-heavy-knowledge-mirror | `feedback/F-NOT-HEAVY-KM.md` |
| F-SAFE-PARALLEL | safe-parallel-not-saturate | `feedback/F-SAFE-PARALLEL.md` |
| F-DISPATCH-FROZEN-CORRECTION | dispatch-frozen-history-correction | `feedback/F-DISPATCH-FROZEN-CORRECTION.md` |

### Patterns (协作模式, 5 条)

| ID | 短名 | 路径 |
|---|---|---|
| P-PROOF-PAIR-CANARY | proof-pair-canary | `patterns/P-PROOF-PAIR-CANARY.md` |
| P-OBJECTS-AFTER-PROOF | objects-after-proof | `patterns/P-OBJECTS-AFTER-PROOF.md` |
| P-API-AS-WRITE-BOUNDARY | api-as-write-boundary | `patterns/P-API-AS-WRITE-BOUNDARY.md` |
| P-OVERFLOW-NOT-BLOCKER | overflow-not-blocker | `patterns/P-OVERFLOW-NOT-BLOCKER.md` |
| P-DUAL-TRUTH-SEPARATION | dual-truth-separation | `patterns/P-DUAL-TRUTH-SEPARATION.md` |

## dedupe 决策 (vs 现有 ~/.claude/.../memory/ 19 条)

本批 16 条是 dedupe 后的真增量, 不跟现有 19 条 ≥70% 重叠. dedupe 表:

| U16 candidate | 已有 ~/.claude/ overlap | 决策 |
|---|---|---|
| L-AUTHORITY-DRIFT | feedback_sidecar_writeback (sidecar 写权 angle) | differentiated angle — promotion drift vs sidecar 写权 是 AP-authority-drift 同 anti-pattern 两侧, ATLAS LINKED-DECISION 列为独立 lesson, **本批收录** (post-Layer-2-audit fix, 刑部尚书 M-2 修订) |
| L-BILIBILI-CRED-RISK | feedback_vendor_diversification | full overlap, **本批未收录** |
| L-SECOND-KNOWLEDGE-BASE | feedback_external_facts_authority + F-NOT-HEAVY-KM | partial, F-NOT-HEAVY-KM 角度已覆盖 |
| L-MULTIWINDOW-RACE | user_multi_agent | partial (user_multi_agent 提了但没说 race), **本批未收录** (后续 follow-up) |
| L-TOKEN-BUDGET | ~/.claude/rules/token-hygiene.md | full (全局 rule), **本批未收录** |
| L-VAULT-PREVIEW-AS-TRUE-WRITE | START-HERE §9-12 | full, **本批未收录** |
| F-MAX-HORSEPOWER + F-LOOSER-NOT-CEREMONY | working_pacing_and_preferences | full, **本批未收录** |
| F-GPT-PRO-AS-WORKER | feedback_gpt_pro_heavy_producer | full, **本批未收录** |
| F-AMEND-AND-PROCEED | feedback_codex_long_runner | partial (Codex angle), **本批未收录** |
| F-SINGLE-USER-PROSUMER | project_shape | partial, **本批未收录** |
| P-AUTHORITY-READBACK-BEFORE-WORK | feedback_pre_diagnose_git_fetch | full, **本批未收录** |
| P-FROZEN-DISPATCH-AS-EVIDENCE | F-DISPATCH-FROZEN-CORRECTION | merged into F-DISPATCH-FROZEN-CORRECTION |
| P-LOCAL-ONLY-AUTH-SAFETY | feedback_vendor_diversification | partial, **本批未收录** |
| P-PR-FACTORY-LANE-SHAPING | feedback_stacked_pr_worktree_safe_order | partial (不同 angle), **本批未收录** |
| P-VISUAL-REVIEW-5-GATE | ~/.claude/rules/aesthetic-first-principles.md | full (全局 rule), **本批未收录** |
| P-HANDOFF-COLD-START | ~/.claude/rules/session-closure.md | full (全局 rule), **本批未收录** |
| P-SELF-AUDIT-CLAIM-LABELS | ~/.claude/rules/codex-metacognition-learnings.md §1.1 | full (全局 rule), **本批未收录** |

## 与 ~/.claude/.../memory/ 关系

- **现有 19 条** instinct memory (Claude Code 本机) 不动, 仍存在 LP-006 single-writer 锁
- **本目录 16 条**是 W2D U16 ingest 新增, 走 cross-vendor path
- **后续**: ~/.claude/ 19 条迁移到本目录是 separate effort (post-W2D follow-up, 不在本 PR scope)

## 维护规则

- 新 memory 加入: lessons/ / feedback/ / patterns/ 子目录 + 本 INDEX 表加行
- frontmatter 必含 `cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]` + `status: current authority`
- body ≤ 600 字 中文+半角混排 (rule + Why + How to apply 三段)
- source_atlas_node 字段链回 U16 ATLAS (本批) 或新 source

## 关联

- master spec: `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` §13 wave routing
- entry: `docs/00-START-HERE.md` §6 doc1/doc2/doc3 (历史 reference, 跟本目录不同 layer)
- claude local: `~/.claude/projects/-Users-wanglei-workspace-ScoutFlow/memory/MEMORY.md` (Claude Code 本机 instinct, 19 条)
- source atlas: `docs/research/strategic-upgrade/2026-05-07/outputs/U16-memory-graph/MASTER-MEMORY-ATLAS.md` (79 candidate node)
