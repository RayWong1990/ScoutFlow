---
title: Cloud Prompt — U16 Cross-Session Memory Graph Reconstruction v0 (≥75 文件)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
expected_zip_files: 75+
expected_zip_words_cjk_latin: 110000+
expected_thinking_minutes: 150+
---

# Cloud Prompt — U16 Cross-Session Memory Graph Reconstruction

## §1 Mission

ScoutFlow 用户多 session / 多窗口 / 多 AI agent (CC / Codex / Hermes / OpenClaw / GPT Pro) 累积大量记忆: ~/.claude/projects/.../memory/ + handoff trail + claude-mem corpora SQLite + ChromaDB + decision-log + retrospective + memory file. 这些记忆**散在不同存储 / 不同格式 / 不同 session**, **没有结构化为可查 / 可演化 / 可追溯的图谱**. 跨 session 假设上下文持续 → 实际丢失 → 重新发现 → 再次踩坑 = 无效内耗.

本任务: 把全 cross-session 记忆重组为 **≥60 个 single-file knowledge node markdown** + 完整知识图谱 (Mermaid + JSON adjacency list) + entity / theme / pattern / lesson 4 类 clustering + 历史 milestone map + 关键决策 cross-session attribution + memory evolution timeline.

外加 8 cluster index + 5 supporting (master atlas / graph-adjacency / theme-evolution-timeline / cross-link-to-decision-and-runbook / README) = **≥75 文件**.

## §2 Inputs

### A. Memory file 全集
1. ~/.claude/projects/-Users-wanglei-workspace-ScoutFlow/memory/MEMORY.md (index)
2. ~/.claude/projects/-Users-wanglei-workspace-ScoutFlow/memory/*.md (全 memory file: user / feedback / project / reference 4 类)
3. ~/.claude/projects/.../bd735ce1*.jsonl (current session transcript, 不许全读, 但抽样 key points)
4. claude-mem corpora (SQLite + ChromaDB observations IDs from system reminders 命中)

### B. Handoff trail
5. ~/workspace/ScoutFlow/plan/handoffs/ (按日期归档的 handoff)
6. ScoutFlow handoff trail (cross-session 起手依赖)

### C. ScoutFlow 历史
7. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/decision-log.md (canonical decision)
8. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/current.md
9. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/task-index.md
10. ScoutFlow 4 run audit + retrospective + amendment trail

### D. Cross-project memory (sibling 影响)
11. ~/workspace/contentflow/L/ retrospective (跨项目元认知)
12. ~/workspace/DiloFlow/ memory (sibling consumer)
13. ~/.claude/rules/codex-metacognition-learnings.md

### E. 全局规则 (memory 政策)
14. ~/.claude/rules/session-closure.md
15. 用户全局 CLAUDE.md auto memory section

## §3 Multi-pass Work Plan (≥10 pass, ≥150 min)

1. **Pass 1 — Memory inventory**: 跨 §2 A-E 全 ls + 读 frontmatter, 统计总 memory file count / claude-mem observations 数 / handoff 数

2. **Pass 2 — Schema 设计**: 每 knowledge node 单文件 ~1300-1600 字, frontmatter (node_id / kind ∈ {entity/theme/pattern/lesson/decision/milestone/feedback/reference} / source ∈ {memory_file/handoff/decision_log/retrospective/claude_mem/jsonl_session} / source_path / first_seen_at / last_updated_at / linked_nodes[] / cross_session_count / risk_if_forgotten ∈ {low/medium/high/critical}), body 含 8 段 (mission / what / why / when / where / how / linked / lessons-if-forgotten)

3. **Pass 3 — Entity nodes (~12)**: 关键实体 (ScoutFlow / DiloFlow / ContentFlow / hermes-agent / 用户 (single-user prosumer) / 4 entity v0 (Signal/Hypothesis/CapturePlan/TopicCard) / RAW vault / Codex / CC0 / CC1 / GPT Pro / Hermes)

4. **Pass 4 — Theme nodes (~15)**: 跨 session 主题 (max horsepower / strong visual / 松一点 / 单人 prosumer / amend_and_proceed / 3-window cloud audit / 80-pack 体系 / silent flexibility / authority-first 4 layer / 5 overflow lane / write_enabled=False / candidate-not-authority discipline / 5-Gate aesthetic / vendor 多元化 / preview-only)

5. **Pass 5 — Pattern nodes (~12)**: 跨 session 行为模式 (元认知 §1.1-§1.8 八条 + 实战命中 + 反向 Codex 学 Opus + 5 透镜 brainstorm + ContentFlow 21 swap pattern)

6. **Pass 6 — Lesson nodes (~12)**: 历史踩坑 (Bilibili C&D / 多窗口 race / token over budget / handoff 过长 / /clear 时机 / Apple Silicon hook 不 fork / git fetch 前置 / candidate 漂移成 authority / Run-2 PR226-228 packed repair / Run-3+4 partial cascade / ContentFlow L1 W10f-S5A1 AV REJECT / 单人 prosumer 工具链膨胀)

7. **Pass 7 — Milestone nodes (~10)**: 历史里程碑 (ScoutFlow 立项 / Phase 1A baseline / Run-1 完成 / Run-2 完成 / Run-3+4 single PR / 4 run 收尾 / Strategic upgrade U1-U16 / PF-V image-to-React 启动 / 80-pack post-dispatch176 roadmap)

8. **Pass 8 — Feedback nodes (~10)**: 用户反馈 (松一点 / 不堆 ceremony / 直 merge OK / amend_and_proceed authorize / strategic 升级维度 / 单人 max horsepower / cloud 8 同时 / 不嫌弃多余 vs 嫌弃复杂 / 强视觉一级 axis / 用 GPT Pro 干活)

9. **Pass 9 — Reference nodes (~5)**: 外部资源 (raw vault / DiloFlow handoff / Notion / Obsidian / hermes-agent venv / 全局规则 ~/.claude/rules / Apple HIG / WCAG / 80-pack source)

10. **Pass 10 — Graph 构建 + 8 cluster index + 5 supporting + README + truthful stdout**:
    - Knowledge graph (Mermaid 大图, 全 ≥60 node)
    - JSON adjacency list (cross-link 完整)
    - Theme evolution timeline (按月)
    - 关键决策 cross-session attribution (哪决策跨几 session 一致)
    - Memory evolution timeline (memory file 创建/更新 历史)

## §4 Hard Boundaries

- candidate / not-authority 全 ≥75 文件
- 不修改 ~/.claude/projects/.../memory/ 任何 (只读 + 重组 atlas)
- 不修改 docs/current.md / decision-log.md / task-index.md (canonical, 只读)
- 不修改 ScoutFlow handoff (只读)
- 不修改 claude-mem corpora SQLite + ChromaDB (只读)
- jsonl session transcript 抽样 (不许全读以免 PII / 凭据 leak)
- 用户全局 CLAUDE.md 个人偏好 OK / 凭据 mask
- 重组成 atlas 不替代原 memory (atlas 是 supplementary view)

## §5 Live Web Evidence

非 required — 内部综合任务.

## §6 Cross-local Search

- ~/.claude/projects/.../memory/ 全
- ~/.claude/projects/.../bd735ce1*.jsonl 抽样 key turn (不全读)
- ~/workspace/ScoutFlow/plan/handoffs/ 全
- ~/workspace/contentflow/L/ retrospective
- ~/workspace/DiloFlow/ 如有 memory
- ~/.claude/rules/* 元规则

## §7 Output Deliverables

ZIP filename: `cloud-output-U16-cross-session-memory-graph-2026-05-07.zip`
File count: **≥75**

| 类别 | 文件数 | min 字 |
|---|---:|---:|
| Entity nodes | 12 | 1300 |
| Theme nodes | 15 | 1300 |
| Pattern nodes | 12 | 1500 |
| Lesson nodes | 12 | 1500 |
| Milestone nodes | 10 | 1500 |
| Feedback nodes | 10 | 1300 |
| Reference nodes | 5 | 1300 |
| Cluster index (8) | 8 | 1500 |
| MASTER-MEMORY-ATLAS | 1 | 3500 |
| GRAPH-ADJACENCY-JSON | 1 | 2200 |
| THEME-EVOLUTION-TIMELINE | 1 | 2500 |
| MEMORY-EVOLUTION-TIMELINE | 1 | 2200 |
| LINKED-DECISION-AND-RUNBOOK | 1 | 2200 |
| README | 1 | 1500 |
| **总计** | **≥90** | ≥120000 |

claim label coverage ≥85%; Mermaid: master graph (大图 ≥60 node) + theme evolution + memory evolution + cluster ≥3 = ≥6 张

## §8 Self-audit (≥25)

- node 是否真有 source path (本机 ~/.claude/projects/.../memory/ 真存在)
- entity / theme / pattern / lesson 4 类是否真区分 (无 cluster 重叠)
- cross-link 是否真双向 (graph 完整)
- jsonl session 抽样是否 PII / 凭据 mask
- claude-mem corpora 引用是否带 IDs
- handoff trail 顺序真按日期
- 与 U11 anti-pattern (lesson 节点 → AP 映射) 真双向
- 与 U15 PR decision (decision 节点 → PR 映射) 真双向
- 与 U10 runbook (pattern 节点 → RB 映射) 真双向
- single-user vs 企业 KM drift
- atlas 是否真 supplementary 不替代 canonical (CLAUDE.md / decision-log / memory)

## §9 Truthful Stdout Contract

```yaml
CLOUD_U16_CROSS_SESSION_MEMORY_GRAPH_COMPLETE: true
zip_filename: cloud-output-U16-cross-session-memory-graph-2026-05-07.zip
files_count: <真实, ≥75>
total_words_cjk_latin_approx: <真实, ≥110000>
total_thinking_minutes: <真实>
nodes_count_total: <真实, ≥60>
entity_nodes: <真实>
theme_nodes: <真实>
pattern_nodes: <真实>
lesson_nodes: <真实>
milestone_nodes: <真实>
feedback_nodes: <真实>
reference_nodes: <真实>
graph_edges_count: <真实>
mermaid_diagrams: <真实, ≥6>
master_graph_node_count: <真实, 期望 ≥60>
memory_files_referenced: <真实>
handoffs_referenced: <真实>
claude_mem_observations_referenced: <真实>
jsonl_sample_turns_referenced: <真实, 应少量, PII mask>
pii_credentials_masked: confirmed
canonical_memory_unchanged: confirmed
multi_pass_completed: <真实/10>
self_audit_findings: <真实, ≥25>
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U16-cross-session-memory-graph-2026-05-07.zip`

## §11 Format Guard

- 每 node frontmatter 含 `node_id` `kind` `source` `source_path` `first_seen_at` `linked_nodes[]` `risk_if_forgotten`
- linked_nodes 双向 (node A linked to B → B linked to A)
- jsonl 抽样不超过 10 turn
- master graph Mermaid 含全 ≥60 node
- adjacency JSON 与 Mermaid 一致 (无 orphan node)
- linked_decision (U15) / linked_runbook (U10) / linked_anti_pattern (U11) cross-link 字段填
