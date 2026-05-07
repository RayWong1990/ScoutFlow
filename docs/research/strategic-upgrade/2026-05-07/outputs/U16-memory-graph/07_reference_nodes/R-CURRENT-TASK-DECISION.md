---
node_id: "R-CURRENT-TASK-DECISION"
title: "current/task-index/decision-log live readback"
kind: "reference"
source: "decision_log"
source_path: 
  - "02_repo_sources/docs/current.md"
  - "02_repo_sources/docs/task-index.md"
  - "api_tool:docs/current.md#turn2file0"
  - "api_tool:docs/task-index.md#turn3file0"
  - "api_tool:docs/decision-log.md#turn1file0"
first_seen_at: "2026-05-03"
last_updated_at: "2026-05-06"
linked_nodes:
  - "P-AUTHORITY-READBACK-BEFORE-WORK"
  - "R-DISPATCH127-176-PACK"
  - "R-PRD-SRD-CONTRACTS"
  - "T-CANDIDATE-NOT-AUTHORITY"
cross_session_count: 16
risk_if_forgotten: "critical"
claim_label: "canonical reference"
linked_decision: "docs/decision-log.md / api_tool turn1file0"
linked_runbook: "Dispatch127-176 runbook / COMMANDER-RUN-PROMPT / readback delta rules"
linked_anti_pattern: "AP-authority-drift"
atlas_status: "candidate / supplementary / not-authority"
availability_note: "source available in uploaded zip or GitHub connector citation"
---

# current/task-index/decision-log live readback

## 1. Mission

本 node 的任务，是把 `R-CURRENT-TASK-DECISION` 从跨 session 的散点记忆里抽出来，作为一个可查、可演化、可追溯的知识节点。它不是新 authority，也不替代 ScoutFlow 的 `docs/current.md`、`docs/task-index.md`、`docs/decision-log.md`、PRD/SRD、RAW 规则或原始 handoff；它只把已经可见的证据、用户口径、候选报告与 live readback 组织成一个 supplementary view。current/task-index/decision-log 是执行前必读 authority；本次 live readback 更新到了 Wave 6 candidate open。

## 2. What

`current/task-index/decision-log live readback` 在本 atlas 中的定义是：一个与 `reference` 相关的记忆事实/模式/教训/引用单元。它的 claim label 是 `canonical reference`，因此阅读时必须区分三层：第一，来自 repo authority 或已经合并决策的 canonical/promoted 事实；第二，来自 Dispatch127-176、外部六份报告、post176 输出的 candidate synthesis；第三，来自本次任务 prompt 或不可访问本机 memory 的 unavailable placeholder。凡是第三类，都不能被写成确定历史。

本节点对当前后续主线的价值在于：它让团队/agent 不需要再次从零重建上下文，也不需要把所有 transcript、handoff、memory file 重新全读一遍。正确用法是：先读本 node 建立方向，再回到 source_path 做事实核验；若 source_path 是 GitHub connector 或 unavailable local path，则必须把它当成 readback requirement，而不是当成已验证本机文件。

## 3. Why

这个节点之所以重要，是因为 ScoutFlow 的历史已经出现了典型的跨 session 复杂度：多个窗口、多 agent、多层 authority、RAW mirror、candidate report、dispatch pack、external audit 与用户即时修正同时存在。只靠“我记得之前说过”会产生三类损耗：一是重新发现，二是重复踩坑，三是把候选语气渐渐说成事实。遗忘后的风险是 critical：可能直接导致 authority drift、runtime/migration 越界、凭据泄露、第二知识库或多窗口 race。

对于单人 prosumer 项目，最稀缺的不是文档数量，而是下一次冷启动能否快速恢复正确判断。这个节点把“要推进什么”和“绝对不能偷渡什么”放在同一页：既服务最大马力，也保留 stop-the-line guard。它的存在目的不是让流程变重，而是减少下一窗口、下一模型、下一工具在同一风险上反复烧时间。

## 4. When

first_seen_at=`2026-05-03`，last_updated_at=`2026-05-06`，cross_session_count≈`16`。这个时间范围不是精确法证结论，而是基于上传 ZIP、GitHub connector readback 和 prompt 所能确定的窗口。若未来可以访问 `~/.claude/projects/.../memory/`、claude-mem SQLite/ChromaDB 或 handoff trail，应当用真实创建/更新时间修正本节点，而不是把当前估计永久化。

当前最关键的时间修正是：上传 ZIP 里的 `docs/current.md` 仍反映较早的 Wave 4 mid-checkpoint 视角，而 GitHub live readback 已显示 Wave 6 candidate open / NOT_EXECUTION_APPROVED / no code-bearing next gate。也就是说，ZIP truth 与 GitHub live truth 必须分开读；不能把 ZIP 中的旧 current 当成现在 authority，也不能把 live readback 反向改写 ZIP 历史。

## 5. Where / Evidence

本节点的 source_path 记录在 frontmatter。可见证据摘录如下，供后续审计回跳：

- `02_repo_sources/docs/current.md:L1` — # Current
- `02_repo_sources/docs/task-index.md:L9` — - 任务状态变化时先写本文件，再更新 `docs/current.md`
- `02_repo_sources/docs/task-index.md:L55` — **Authority writer slot [L4]**: T-P1A-017 / T-P1A-026 各自占用 Authority writer slot 1/1，跑期间禁止任何其他 authority writer 同时改 `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md`。
- `02_repo_sources/docs/task-index.md:L99` — | `T-P1A-050` | Wave 3B closeout + Wave 4 ledger candidate | `2026-05-05` | PR=#75; scope=AGENTS/current/task-index/decision-log/shoulders-index/contracts-index; result=Wave 3B closed; Wave 4 not yet user-gated; ledger candidate only |

这些摘录不是全文替代。它们只是 anchor：证明本节点不是凭空编写，同时提醒读者回到原始材料核验。对于 prompt 指定但沙盒不可访问的来源，例如 `~/.claude` memory、jsonl transcript、claude-mem corpora、ContentFlow/DiloFlow 本地 memory，本 atlas 只记录“任务要求”和“不可访问状态”，不伪造 observation ID 或本机路径存在性。

## 6. How

使用本节点时，推荐按四步执行。第一，先看 risk_if_forgotten，判断它是路线决策、边界防护还是纯 reference。第二，沿 linked_nodes 查相邻节点，尤其是 authority-first、candidate-not-authority、execution-gates、ScoutFlow↔RAW boundary 和 frozen dispatch evidence。第三，回到 source_path 做 readback；如果涉及当前状态，必须以 GitHub live authority 为准。第四，把本节点只作为起手上下文，不直接 copy 到 PRD/SRD/current/task-index。

对于实际推进，`R-CURRENT-TASK-DECISION` 最常见的错误用法是把它当成“已经批准”或“已经完成”的证明。正确用法是把它变成决策前的 checklist：是否有 user gate，是否有 external audit，是否有 CI/validation，是否与 current/task-index 一致，是否引入 runtime/migration/frontend/vault true-write 漂移，是否让 RAW 与 ScoutFlow 的 SoR 关系变得模糊。

## 7. Linked

本节点在图谱中的主要邻居包括：P-AUTHORITY-READBACK-BEFORE-WORK, R-DISPATCH127-176-PACK, R-PRD-SRD-CONTRACTS, T-CANDIDATE-NOT-AUTHORITY。这些链接经过双向化处理：如果 A 指向 B，B 的 frontmatter 也会包含 A。图谱链接代表“需要一起读”，不是因果证明。比如 theme 可以连接 lesson，lesson 可以连接 pattern，pattern 可以连接 milestone；这只是为了降低冷启动成本，不代表所有节点有同等 authority 级别。

在后续维护中，任何新增链接都必须保留三条纪律：一是 link 要双向；二是 link 不能让 candidate node 看起来像 authority node；三是 link 变更要同步 `GRAPH-ADJACENCY-JSON.json` 与 Mermaid master graph，避免 orphan node 或图谱漂移。

## 8. Lessons-if-forgotten

如果忘记 `current/task-index/decision-log live readback`，下一次 session 很可能会发生以下连锁：先误读来源层级，再误判当前 gate，最后把本来可以快推的 proof 变成大包重排，或把本来需要停线的 runtime/migration/authority 变成“似乎已经被前面批准”。这正是 cross-session memory graph 要解决的问题：不是让模型背更多历史，而是让模型在启动时就知道哪些历史必须谨慎、哪些资产可以复用、哪些内容必须重新 readback。

本节点的最短复述是：current/task-index/decision-log 是执行前必读 authority；本次 live readback 更新到了 Wave 6 candidate open。。在用户要求“深度复盘研究”时，应把它作为证据化复盘的一部分；在用户要求“继续执行”时，应把它作为边界检查的一部分；在用户要求“路线怎么接”时，应把它作为判断 post176 主线是否聚焦 product proof 的一部分。
