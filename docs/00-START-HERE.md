---
title: ScoutFlow Start Here — 入口 + Agent Cold Start Ladder
status: current authority
purpose: 单人本地项目入口 + 新 agent / 新 session 冷启动地图
created_at: 2026-05-07
last_updated: 2026-05-08
anchor_refresh_tool: tools/refresh-start-here.py
refresh_interval_pr: 50
next_forced_refresh_pr: 300
last_refreshed_from_main_pr: 259
last_refreshed_from_main_sha: 5777389
status_words_locked:
  - current authority   # 真状态 (current.md / task-index.md / decision-log.md / 本文件)
  - promoted addendum   # PRD/SRD 已升级 (PRD-v2.1 / SRD-v3 h5-bridge)
  - candidate north-star # 候选路线图 (master spec / PRD-v3 thin shell / SRD-v3 thin shell)
  - reference storage   # 储能层 grep-able (16 ZIP / archive / research)
---

# ScoutFlow Start Here

> **新 agent / 新 session 第一份必读**. 5 min 看完, 后续按 ladder 深度阅读.

---

## §0 TL;DR (5 行)

- **是什么**: 单人本地内容采集 / 转写 / 改写 / 入库 raw 系统 (operator workstation, 不是 SaaS)
- **当前 baseline**: 见 §1 auto-managed 真态锚点 (`git log -1 origin/main` + authority docs); capture-station 已 landed 基线 = W2C truthful runtime surfaces + 5 态 state machine + W1B Trust Trace graph/timeline/error-path bounded lanes；`W3E PF-C0-O1` 仅为 docs-only candidate starter cluster
- **当前状态**: Active 0/3 / Authority writer 0/1 / `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
- **5 overflow lane Hold**: write_enabled=False / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench (永不偷开, 走 authority 升级 PR)
- **入口 4 文件**: `current.md` (真态) / `task-index.md` (lane registry) / `decision-log.md` (决策) / **本文件** (导航)

---

## §1 当前真态锚点

> 本段由 `python tools/refresh-start-here.py` 维护；closeout / merge 后跑 refresh，CI 走 `--check`。

<!-- START_HERE_AUTO_ANCHORS_BEGIN -->
| 维度 | 值 |
|---|---|
| repo | `/Users/wanglei/workspace/ScoutFlow` |
| main HEAD | `5777389` (PR #259) ← `beb0fef` (PR #258) ← `1fa0e9a` (PR #260) |
| capture-station stack | React 18.3.1 + Vite 5.4.10 + CSS Modules + tokens.css 三层 overlay + 自写 SVG sprite |
| checkpoint dispatch 累计 | `38`（`docs/research/post-frozen/runs/CHECKPOINT-Run*-final.json` 当前求和；不含 Amendment / PF-C4-01 / governance lane） |
| PRD canonical | PRD-v2 + PRD-v2.1 amend (promoted, PR #58) |
| SRD canonical | SRD-v2 + SRD-v3 h5-bridge amend (promoted, PR #64) |
| 16 ZIP 储能层 | `docs/research/strategic-upgrade/2026-05-07/audit/PHASE-A-B-SUMMARY.md` 当前摘要 = `895 markdown / 1,479,998 字` |
<!-- START_HERE_AUTO_ANCHORS_END -->

**详细**: 见 [`docs/current.md`](./current.md).

---

## §2 状态词字典 (4 类, 不再增)

| 状态词 | 含义 | 例子 |
|---|---|---|
| `current authority` | 真状态, 最新事实源 | `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, 本文件 |
| `promoted addendum` | PRD/SRD 升级补丁, 已 user 拍板 | PRD-v2.1, SRD-v3 h5-bridge |
| `candidate north-star` | 候选路线图, 不构成 authority | `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`, PRD-v3 thin shell, SRD-v3 thin shell |
| `reference storage` | 储能层 grep-able reference | 16 ZIP / `docs/archive/` / `docs/research/` |

**严禁**: 引入新状态词. 任何文档 frontmatter `status:` 字段必须用这 4 类之一.

---

## §3 Agent Cold Start Ladder (新 agent / 新 session 分级阅读)

| 级 | 时间 | 文件 | 用途 |
|---|---|---|---|
| **L0** | 5 min | `docs/current.md` (TL;DR) + `docs/task-index.md` + `docs/decision-log.md` + 本文件 | 真态 + 决策 + 入口 |
| **L1** | 15 min | + `docs/PRD-v2-2026-05-04.md` + `docs/SRD-v2-2026-05-04.md` + `docs/PRD-amendments/prd-v2.1-...md` + `docs/SRD-amendments/h5-bridge-para-vault-srd-v3-...md` + `docs/project-context.md` + `AGENTS.md` + `CLAUDE.md` | PRD/SRD baseline + 项目元层 |
| **L2** | 30 min | + `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` (north-star roadmap) | 11 wave routing + 4-agent 分工 + 现在没做的全部 inventory |
| **L3** | 1 h | + 任务相关 U (见 §6 储能层地图) + `docs/specs/contracts-index.md` + `docs/specs/locked-principles.md` | 储能层 + 合约 |
| **L4** | 按需 | `docs/architecture/`, `docs/research/repairs/`, `docs/research/strategic-upgrade/2026-05-07/audit/` 全集 | 架构 + 修复 + 16 ZIP audit |

---

## §4 文档地图 (按层级)

```
A. 治理 authority 层 (顶级, 真 authority)
   ├── docs/current.md            ← current authority (真态 ledger)
   ├── docs/task-index.md         ← current authority (lane registry, max=3)
   ├── docs/decision-log.md       ← current authority (Authority writer max=1)
   └── docs/00-START-HERE.md      ← current authority (本文件, 导航)

B. PRD 链
   ├── docs/PRD-v2-2026-05-04.md                                              ← canonical promoted base
   ├── docs/PRD-amendments/prd-v2.1-...md                                     ← promoted addendum
   ├── docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/PRD-v3-candidate.md  ← candidate north-star (thin shell)
   └── docs/archive/PRD-v1*.md × 3                                            ← reference storage (superseded)

C. SRD 链
   ├── docs/SRD-v2-2026-05-04.md                                              ← canonical promoted base
   ├── docs/SRD-amendments/h5-bridge-para-vault-srd-v3-...md                  ← promoted addendum (PR #64)
   ├── docs/SRD-amendments/db-vnext-srd-v3-...md                              ← candidate north-star (still)
   ├── docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/SRD-v3-candidate.md  ← candidate north-star (thin shell)
   └── docs/archive/SRD-v1*.md × 4                                            ← reference storage (superseded)

D. 项目元层
   ├── docs/project-context.md           ← ScoutFlow 是什么 / 不是什么 / 4-layer
   ├── AGENTS.md (顶级)                  ← agent 行为规范
   ├── CLAUDE.md (顶级)                  ← Claude sidecar 默认职责
   ├── docs/dispatch-template.md
   └── docs/shoulders-index.md

E. 路线图 / 战略层
   └── docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md  ← candidate north-star (PR #243 后采集线 11 wave + 4-agent v3 + inventory)

F. 合约 / 架构
   ├── docs/specs/contracts-index.md          ← 合约总索引
   ├── docs/specs/locked-principles.md        ← LP-001~005 硬原则
   ├── docs/specs/parallel-execution-protocol.md
   ├── docs/specs/{bbdown-adapter, db-vnext-design, platform-adapter-risk, raw-response-redaction, worker-receipt}-contract*.md
   └── docs/architecture/{ADR-001-obsidian-PARA-lock, baseline-roadmap-after-pr54, shoulders-lifecycle-handbook, pr-factory-*}.md

G. 历史 doc1/doc2/doc3 (战友 2026-05-04 cloud GPT Pro 三件套, ACCEPT WITH ERRATA)
   ├── doc1 = docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md (路线图方向锚)
   ├── doc2 = docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md (Shoulders lifecycle)
   ├── doc3 = docs/research/pr55-pr74-worklist-candidate-2026-05-04.md (PR55-74 dispatch backbone)
   └── errata = docs/research/doc1-doc2-doc3-v1.1-acceptance-errata-report-2026-05-04.md
   状态: reference storage (历史价值, 已被 PR55-74 + Wave 5/6 实施超过)

H. 储能层 (reference storage, grep-able)
   ├── docs/research/strategic-upgrade/2026-05-07/  ← 16 ZIP / 895 file / 1.48M 字 (见 §6 地图)
   ├── docs/research/repairs/                       ← 30+ scope-note / errata / triage
   ├── docs/research/                                ← 跨 t-p1a / dispatch / probe 报告
   └── docs/archive/                                 ← 历史 PRD/SRD / 退场文档

I. 创世文档 v0.1 (2026-05-03, reference storage)
   └── docs/ScoutFlow-project-organization-docs-v0/  ← AGENTS-draft / Claude-Design-Brief / Phase0-Bootstrap / Project-Operating-Model / Reference-Repo-Index / probe-video-capture
```

---

## §5 doc1 / doc2 / doc3 关系说明 (战友常问)

**背景**: 2026-05-04 cloud GPT Pro 一夜跑出 3 个文档 (doc1+doc2+doc3), 加 1 个 errata report, ACCEPT WITH ERRATA verdict, 后被 PR55-74 + Wave 5/6 实施超过.

| 名 | 文件 | 行数 | 角色 | 状态 |
|---|---|---|---|---|
| **doc1** | `docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md` | 723 | 路线图方向锚 (PR54 后 ScoutFlow main baseline) | reference storage |
| **doc2** | `docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md` | 972 | Shoulders lifecycle system of record | reference storage |
| **doc3** | `docs/research/pr55-pr74-worklist-candidate-2026-05-04.md` | 2055 | PR55-PR74 dispatch backbone | reference storage |
| errata | `docs/research/doc1-doc2-doc3-v1.1-acceptance-errata-report-2026-05-04.md` | — | 接纳后 10 条细节修订建议 | reference storage |

**当前价值**: 历史 reference (PR55-74 已实施完). 新 lane 启动时**不直接 paste** doc1/2/3, 应 paste master spec 或具体 dispatch.

---

## §6 储能层地图 (16 ZIP × 895 file × 1.48M 字, grep-able reference storage)

来源: 2026-05-07 凌晨战友 16 窗口 GPT Pro 一夜并行产出, Phase A+B audit 已完成 (`docs/research/strategic-upgrade/2026-05-07/audit/PHASE-A-B-SUMMARY.md`).

| U | 主题 | 关键文件 | 何时 paste / grep |
|---|---|---|---|
| **U1-deep** | PRD-v3 / SRD-v3 supplements | PRD-v3-supplement-worked-examples / SRD-v3-supplement-anti-patterns / NFR-SINGLE-USER-CAPACITY / SIBLING-PROJECT-EGRESS-CONTRACT / TRACEABILITY-MATRIX-EXTENDED + thin shell × 2 (compiled by cc1 2026-05-07) | PRD/SRD 升级时 |
| **U2-deep** | 5 overflow lane spike commands | LANE-1 true_vault_write / LANE-2 runtime_tools / LANE-3 browser_automation / LANE-4 dbvnext_migration / LANE-5 signal_workbench | overflow lane 解禁时 |
| **U3-deep** | 4 entity v0/v1 + migration | ENTITY-{CapturePlan, Hypothesis, Signal, TopicCard}-sample-data + MIGRATION-V0-TO-V1 + OPENAPI-GOLDEN | DB schema / entity 实施 |
| **U4-visual-asset** | 视觉 asset 4 模块 spec | MODULE-{visual-asset, design-token, pattern-library, prompt-template}-spec | 视觉强化第二波 |
| **U5-agent-fleet** | agent fleet dispatch ledger | (10 file) | dispatch ledger 实施 |
| **U6-retrieval-dam** | visual-DAM + hybrid-local-search | MODULE-visual-dam-spec / MODULE-hybrid-local-search-spec / EMBEDDING-MODEL-SELECTION | retrieval / DAM 实施 |
| **U7-state-library** | state machine library | (9 file) | state machine 实施 |
| **U8-egress** | cross-system egress manifest | (10 file) | ScoutFlow→ContentFlow/DiloFlow/Obsidian 时 |
| **U9-dispatch-catalog** | Phase 2-4 ≥71 dispatch prompt | 02_phase3_dispatches/P3-{Signal, Hypothesis, CapturePlan, TopicCard}-* | 80-pack 余量 / multi-PR 量产 |
| **U10-runbook** | prosumer SOP runbook | (83 file) | 单人操作 SOP |
| **U11-anti-pattern** | anti-pattern encyclopedia | cluster-{a, b, c, d, e}-* | pre-commit hook / anti-pattern guard |
| **U12-tools-catalog** | skills + tools + MCP + plugin catalog | (122 file) | 跨项目 skill 复用 |
| **U13-visual-brand** | visual style brand atlas (token + 8 panel + 30 icon) | (109 file) | 视觉强化 |
| **U14-apple-silicon** | Apple Silicon 优化全集 (Whisper.cpp Metal / VideoToolbox / CoreML / mlx) | cluster_{a-e}-* | Phase 2 ASR / 视频处理优化 |
| **U15-decision-log** | 240+ PR decision log atlas | (145 file, ≥110 prompt) | 历史决策回溯 |
| **U16-memory-graph** | cross-session memory graph | (100 file) | 跨 session 记忆图谱重建 |

**总览**: `docs/research/strategic-upgrade/2026-05-07/audit/PHASE-A-B-SUMMARY.md` (sniff master + 9 spot Tier 1 + cross-link audit).

---

## §7 当前 wave 候选 (链 master spec §13)

| Wave | 状态 | 时间 | 派给 |
|---|---|---|---|
| **W1A** untracked batch land (16 ZIP storage land) | 已 landed (`PR #244`) | — | CC1 |
| **W2C** PF-C4-02 真数据接线 + 微交互 | 进行中（`T-P1A-156`; frontend-first existing-route wiring） | 5-7h + validation | Codex |
| **W1B** PF-C4-EXT D3 graph + timeline + error-path 自写 | 候选 (依赖 OpenDesign v2 升级 PR) | 6-8h | Codex |
| **W2D** U16 memory ingest / memory graph baseline | 已 landed (`PR #245`)；后续扩到 50-100 待继续 | — | CC1 |
| **W3E** 80-pack 余量 cluster (PF-C0/O1/C3) | 候选 | 多日 | Codex multi-PR |
| **W4F** Phase 2 LANE-2 ASR spike | 候选 (依赖 runtime_tools 解禁) | 多日 | GPT Pro spec + Codex |
| **W4G** Phase 2 LANE-3 Rewrite | 候选 (依赖 W4F) | 多日 | GPT Pro spec + Codex |
| **W5H** Source matrix 扩展 (yt-dlp/XHS/抖音/Research) | 候选 (依赖 runtime_tools 解禁) | 多日 | Codex multi-PR |
| **W5I** 评论 / 楼中楼 子系统 | 候选 (依赖 W5H) | 多日 | Codex |
| **W6J** Vault commit 真解禁 | 候选 (依赖 W4F+W4G+W5H + true_vault_write 升级) | 多周 | GPT Pro + Codex |
| **W6K** Memory + 协作模式沉淀 | 持续沉淀（`PR #246` harness 已 landed；后续 refresh sprint / cross-vendor mirror 按需推进） | 任何 session 间隙 | CC1 |

**详见** [`docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`](./COLLECTION-LINE-MASTER-SPEC-2026-05-07.md) §13-§18.

---

## §8 4-agent v3 分工速查

| Agent | 角色 | 强项 | 弱项 |
|---|---|---|---|
| **GPT Pro** (OpenAI) | Heavy Producer | 一次性 24-30min 深度 thinking / 强 schema 大批量 / 长 narrative / 16 窗并行 | 无 git/shell / 一次性, 不能 long runner |
| **Codex** (OpenAI) | Long Runner Coder + Boundary Guard | 通宵 long-runner / 本地 git/shell / 多 PR commit / "50 个/2h" 节奏 / amend_and_proceed / 元认知 §1.4-§1.7 | 长 narrative 偏工程口吻 |
| **Claude Code** (Anthropic, CC0/CC1) | Conductor + Auditor + Engineer | 实时对话 + A/B/C 决策 / 派单 prompt 设计 / git 实时迭代 / cross-session memory | 单 turn audit 是 smoke test |
| **Hermes** (3rd party) | Independent Auditor | 跨 lane 三方独立外审 / 决策仲裁 (candidate role) | — |

**Vendor 真相**: OpenAI 占 2 (GPT Pro + Codex) / Anthropic 占 1 (Claude) / 3rd party 占 1 (Hermes), 战友独自薅全 vendor.

**详细决策树**: `~/.claude/projects/-Users-wanglei-workspace-ScoutFlow/memory/project_4_agent_division_v3.md`.

---

## §9 边界硬红线 (15 条速查, 永不踩)

1. ❌ `write_enabled=False` (`bridge/config.py:24,36`) 不能改
2. ❌ 5 overflow lane Hold (`true_vault_write` / `runtime_tools` / `browser_automation` / `dbvnext_migration` / `full_signal_workbench`)
3. ❌ Authority files 未经 authority-writer dispatch 不得写 (`current.md` / `task-index.md` / `decision-log.md` 仅 authority-writer dispatch 可写, max=1; 顶级 `AGENTS.md` / 根 `CLAUDE.md` 不主动触碰, 仅治理类 dispatch 显式授权时才改)
4. ❌ 历史 ledger immutable (`CHECKPOINT-Run*.json` / `EXTERNAL-AUDIT-REPORT-*.md` / `PF-C4-01-CHECKPOINT.json`)
5. ❌ `~/workspace/raw/` 永不污染 (除 true_vault_write 解禁后)
6. ❌ 引整套 vendored shadcn / Radix / TanStack / React Flow / Zustand
7. ❌ Tailwind / shadcn / Panda / Lucide / styled-components / @emotion / @stitches / panda-css / Mantine / Ant Design / Chakra UI / @mui
8. ❌ Hex 硬编码 (除 tokens.css / density / type-weight 三文件)
9. ❌ generic admin/dashboard 视觉气质 (战友审美红线)
10. ❌ Browser automation (playwright / selenium)
11. ❌ Trust Trace DTO / PlatformResult enum / WorkerReceipt schema 改字段名 / shape
12. ❌ `Vault Commit` + `Transcribe` 真接 future-gated route (UI 必须 disabled state)
13. ❌ Motion 渗透 wiki/reading surface (现在没 wiki, spec 显式锁)
14. ❌ Vendor lock-in (BBDown 当前 only, cease-and-desist 信号已现, 必须多元化)
15. ❌ 引入新状态词 (锁 4 类: current authority / promoted addendum / candidate north-star / reference storage)

**详细 + 升级路径**: `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` §16.

---

## §10 新 agent / 新 session 必跑的 8 件事

1. **Read** 本文件 (你正在做)
2. **Read** `docs/current.md` TL;DR (5 行) 看真态
3. **Read** `docs/task-index.md` 看 Active 是 0/3 还是已满
4. **Bash** `git log --oneline origin/main -5` 看最近 5 commit
5. **Read** master spec § 13.1 (11 wave) + § 15.2 (优先级 P0-P4) + § 16 (红线 + 升级路径) — single source of routing truth (CC1 retrospective sediment, 2026-05-07)
6. **Decide**: 你的任务在 §7 wave 的哪个? 找对应 master spec 章节 + storage U (此步依赖 5 的 master spec 输入).

> 以下 7-8 件为 CC1 retrospective sediment (2026-05-07) 增补 — 防止数据估值与 candidate 误读类常见错误:

7. **Bash** `find <dir> -type f | wc -l` 校验任何 "~N file" 估值 — 子目录会被 count, 直接用估值差 10x (元认知 instinct §3 find-type-f 校验条款)
8. **Verify** stack/路线/规范决策 → grep frontmatter `status:` + 核 PR merge 状态 — 文件名带 `candidate-` 后缀的不是 authority (元认知 instinct §3 candidate-vs-authority 条款)

如果你是 Codex Long Runner: 战友会 paste commander prompt + 你按 §13 master spec 4-agent 分工执行.

如果你是 GPT Pro: 战友会 paste spec 撰写 prompt + 你一次性 24-30 min thinking 输出.

如果你是 Hermes: 战友会 paste pre-flight / external audit 任务 + 你独立审查输出.

如果你是新 Claude session: 你按本 ladder 走 L0→L1→L2.

---

## §11 Ad-hoc 工作文件路径 Contract (CC1 retrospective sediment, 2026-05-07)

ScoutFlow ad-hoc 工作文件 (dispatch / commander prompt / 中间产物 / handoff 草稿) **必须放 raw PARA**:

- ✅ 真路径: `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/RUN-<wave>-<date>/`
- ❌ 反路径: ScoutFlow repo git tracked (会污染 main, 增加 PR 噪声)

**ScoutFlow repo 内只放最终 deliverable**:

- ✅ docs / code / spec / contract / authority files
- ✅ retrospective / decision-log entry / handoff (轻量, 内容 ≤ 15 行 frontmatter 不含, 用 `docs/research/post-frozen/handoff-template.md` 模板, 落 `docs/research/post-frozen/handoff/`)
- ❌ commander prompt 草稿 / Codex paste-ready / GPT Pro spec 中间产物 / Hermes 输入包

**触发**: mkdir / Write 任何 "工作中间文件" 前必先确认路径分类 (元认知 instinct §3 第 15 条).

---

## §12 维护规则 (本文件)

- 本文件标 `current authority`, 跟 `current.md` / `task-index.md` / `decision-log.md` 同级
- `Layer A — 减 hard-code, 改引用 + auto-managed anchor`: §0 只给入口和范围，不再重复写死 main SHA / dispatch 总数；§1 真态锚点由脚本维护。
- `Layer B — 脚本 + gate`: `python tools/refresh-start-here.py` 负责 refresh；`python tools/refresh-start-here.py --check` 进入 docs-check，防止 merge 后继续漂移。
- `Layer C — wave closeout 强制更新`: 每次 wave / governance lane closeout 按 `docs/task-index.md -> docs/current.md -> docs/decision-log.md -> python tools/refresh-start-here.py` 顺序写回；随后人工复核 §7 wave 表和 README / master spec / closeout receipt 的旧 PR / SHA / wave 状态引用。
- `Layer D — 定期 refresh sprint`: 当前轮 refresh 已在 `PR #246` 执行；下一次 forced refresh = `PR #300`，此后每 `+50 PR` 触发一次。若最新 merged PR 号达到 frontmatter `next_forced_refresh_pr`，docs-check 必须 fail 到 refresh 完成为止。
- 文档地图 §4 / §5 / §6 跟随实际 docs/ 目录变化更新。
- 状态词 §2 锁 4 类；任何新状态词需走 user 拍板 + decision-log entry。
- 边界硬红线 §9 跟随 `docs/current.md` "当前禁止" 段同步。
- §10 8 件事 + §11 ad-hoc 路径 跟随元认知 instinct §3 同步 (`~/.claude/rules/codex-metacognition-learnings.md`)。

---

> 本文件 by CC1 (Anthropic), 2026-05-07. 目的: 让任何新 agent / 新 session 5 min 找到方向, 不靠记忆 / 不靠人工口述.
> 关联: 战友 doc baseline 整治 PR #244 (single PR squash, 含 master spec promotion + PRD-v3/SRD-v3 thin shell + doc1/2/3 cross-link + README 整改).
