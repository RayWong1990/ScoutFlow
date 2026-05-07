---
title: ScoutFlow CC1 Session Retrospective + Master Spec Utilization Audit
status: candidate / retrospective / not-authority
session_id: 1852adc0-f7af-4379-b183-f8c949cc6962
session_model: Claude Opus 4.7 (1M context)
session_window: 2026-05-07 14:30 - 22:30 GMT+8 (~8h, 含 1 次 auto-compact + 多次 SessionStart 重连)
agent_role: CC1 (Anthropic, sidecar reviewer + conductor + auditor)
co_audit_by: CC0 (并行 session, 多次 catch 我的错误形成校准)
trigger: 战友质疑 "今天下午聊很久写出来的 master spec / 文档体系你用了吗"
created_at: 2026-05-07
purpose: |
  本次会话级 retrospective archive. 给未来 ScoutFlow session 留一份 "CC1 在 PR #243 后整治期间犯了什么错 / 学了什么 instinct" 的可复利档案. 不进 authority writer slot, 不要求 user 拍板细节, 仅作 reference storage.
related_files:
  - docs/00-START-HERE.md (current authority, 入口)
  - docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md (candidate north-star, 11 wave routing)
  - docs/research/strategic-upgrade/2026-05-07/audit/PHASE-A-B-SUMMARY.md (16 ZIP audit summary)
  - ~/.claude/rules/codex-metacognition-learnings.md (元认知 §1-§9 全集)
  - ~/.claude/projects/-Users-wanglei-workspace-ScoutFlow/memory/ (CC1 持久 memory)
---

# ScoutFlow CC1 Session Retrospective — 2026-05-07

> 本文是 CC1 (Anthropic Opus 4.7) 在 ScoutFlow PR #243 land 后的整治期内 (2026-05-07 下午~晚) 一次 ~8h 长 session 的自审档案.
>
> **包含**:
> - §1 二次调研报告 — master spec 利用度章节级 audit
> - §2 10 条本次会话识别错误 + 元认知归因
> - §3 6 条新增 instinct (加在元认知 §3 自检清单后)
> - §4 项目治理体系优化建议
> - §5 给未来 ScoutFlow session 的冷启动指导 (含 START-HERE §10 增补)
> - §6 元元洞察 + 沉淀路径
>
> **目的**: 让未来 CC1/CC0 session 不重复犯同样错误. 不替代任何 authority, 是 reference storage 的一员.

---

## §0 上下文锚点

### 0.1 触发

战友在 22:11 GMT+8 抛出: "我想问下 我今天下午和你聊了很久 写出来的 master spec 以及 基础文档的组建体系你有用到吗?"

随后给我看 CC0 在另一窗口的"重新判断"段落 — CC0 自己也反思了治理立场，从 "多 agent 团队治理硬度" 校准到 "单人本地三句话原则".

战友的真实意图: **不是只要一个二次调研, 而是要 CC1 自审整个 session 的纪律落地度, 形成长期档案**.

### 0.2 本次 session 起止状态

```text
session 起 (2026-05-07 ~14:30):
  main HEAD = e1deda6 (PR #243 PF-C4-01 land)
  PFV / C2 / 80packs Run-3+4 已完毕
  Active 0/3, Authority writer 0/1, Wave 6 candidate open
  5 overflow lane Hold
  task: 协助战友规划 PR #243 后整治 + 下一波 wave 启动

session 止 (2026-05-07 22:30):
  main HEAD 不变 (e1deda6)
  PR #244 整治分支由 CC0 起头 (尚未 merge)
  无新代码改动 (CC1 sidecar role 限制)
  4-agent v3 memory + 派单 7 原则 memory + GPT Pro Heavy Producer memory 已沉淀
  本 retrospective 文件作为本次 session 唯一 deliverable 入档
```

### 0.3 协作模式 (本次 session 实证)

| 维度 | 实测 |
|---|---|
| CC1 / CC0 双 Opus 并行 | ✅ 实证 — CC0 catch 我 4+ 次错, 我也 catch 过 CC0 (over-engineered W2D Codex prompt) |
| GPT Pro 已 closed (本次 session 无新 paste) | — |
| Codex Long Runner 已 closed (本次 session 无新 paste) | — |
| Hermes 候选角色 (本次 session 战友未 paste 给 Hermes) | — |
| 战友主审 + 拍板 | ✅ 多次 (Top-3 推荐 / W2D 选项 / Codex prompt / 二次调研) |
| Auto-compact | 1 次 (token 占用 ~80%) |

**协作发现**: 双 Opus 互审是稳定纪律层. CC0 不是"竞争 CC1", 而是"独立审 CC1 漏洞 + 反向 CC1 也审 CC0". 三方独立外审不必等 Hermes — 双 Opus 已有此功能 (vendor 不独立但工程纪律独立).

---

## §1 二次调研报告 — Master Spec 利用度章节级 Audit

### §1.1 调研方法

| 步骤 | 动作 | 落地 |
|---|---|---|
| 1 | 真读 master spec § 13.1 (11 wave list) + § 13.2 (4-agent cross-wave) + § 13.3 (5 漏洞修订) + § 14 (pre-flight 5 步) + § 15.2 (优先级) + § 16.1-3 (红线 + 升级路径 + 风险矩阵) + § 17.1 (近期时间预算) | 在 turn N-1 完成 |
| 2 | 比对我前 turn 16 U ROI matrix vs master spec § 13.1 wave 列表 + § 9.x 12 子模块 | 落到 §1.4 表 |
| 3 | 检查我前 turn 给战友的 5 漏洞 vs master spec § 13.3 集成现状 | 落到 §1.3 表 |
| 4 | 回应 CC0 三句话治理原则 + 5 小建议 | 落到 §1.5-§1.6 |
| 5 | 输出单 PR 整治推荐 (不新增门禁) | 落到 §1.7 |

### §1.2 Master Spec 章节级 Audit

| Master Spec 章节 | 内容 | 我前 turn 用了吗 | 严重度 |
|---|---|---|---|
| § 4.x | Source 矩阵 + vendor 多元化 | ❌ 没读 | 中 (漏 W5H 路线) |
| § 5.x | ASR 模型 / 长音频 / 并行 (LANE-2) | ❌ 没读 | 中 (漏 W4F 路线) |
| § 6.x | LLM Router / 风格库 / Cost (LANE-3) | ❌ 没读 | 中 (漏 W4G 路线) |
| § 7.x | Trust Trace 4 子模块 + Frontmatter spec + Citation chain | ❌ 没读 | **高 (漏 W2C 主菜核心)** |
| § 8.1 | 13 surface × Bridge API mapping (修订自我之前漏洞 #2) | ⚠️ 部分 (重复提) | **高 (重复劳动)** |
| § 8.3 | 微交互动画 vocabulary | ❌ 没读 | 中 (漏 W2C 视觉 input) |
| § 8.5 | Capture state machine 6 状态 (U7 素材) | ❌ 没读 | 中 (漏 W2C state machine) |
| § 9.1-9.12 | 12 子模块 inventory (Asset DAM / Agent Fleet / Memory Graph / Cost Ledger / ...) | ⚠️ 仅 grep header | **高 (漏 12 U 对应路线)** |
| § 13.1 | **11 wave 列表** (W1A→W6K) | ❌ 没真用 | **重大** |
| § 13.2 | **4-agent cross-wave 分工矩阵** | ❌ 没真用 | **重大** (我自己重画过一次) |
| § 13.3 | **5 漏洞集成现状** | ❌ 没看见 | **重大** (我前 turn 重复给了 5 漏洞) |
| § 14.2 | pre-flight 5 步 | ⚠️ 部分 | 中 (提了 dispatch 注册但没引 §14.2) |
| § 15.1 | 依赖图 | ❌ 没读 | 中 |
| § 15.2 | **优先级 P0-P4** | ❌ 没读 | **重大** (我自己排 Top-3 不对齐) |
| § 16.1 | 15 条红线 | ⚠️ 间接 (从 START-HERE §9 看到) | 低 (转手用了) |
| § 16.2 | **合法升级路径** (D3 单点引 / runtime_tools / true_vault_write 等) | ❌ 没读 | **重大** (我前 turn 推 W1B 自写时没引这条) |
| § 16.3 | 风险矩阵 7 条 | ❌ 没读 | 中 |
| § 17.1 | 近期时间预算 | ❌ 没读 | 中 |

**统计**: 18 个核心章节, 真用 0 / 部分用 5 / 没用 13 = **真用 0%, 部分 28%, 没用 72%**.

### §1.3 我前 turn 给的 "5 漏洞" 已被 Master Spec § 13.3 集成

| 漏洞 | master spec 落地位置 | 我前 turn 重复提了? |
|---|---|---|
| W2C dispatch 注册 + Hermes pre-flight | § 14.2 5 步 / § 13.2 W2C 行 | ⚠️ 是 |
| surface-route mapping 显式 | § 8.1 表 | ⚠️ 是 |
| Trust Trace DTO 锁 | § 8.1 + § 16.1 第 11 条 | ⚠️ 是 |
| 16 ZIP Tier 分类 | W1A § 13.1 | ⚠️ 是 |
| Capture-side motion 边界 | § 8.3 | ⚠️ 是 |

**结论**: 我前 turn 给战友的 "5 漏洞补充" = **5 次重复劳动**. master spec 早已集成. CC0 跟我都没自动加载 master spec 全文 (只读 START-HERE) → 重复劳动是结构性问题, 不是个体疏忽.

### §1.4 我前 turn 16 U ROI Matrix vs Master Spec 对齐度

#### A. Top-3 推荐 vs § 15.2 P0-P1 优先级

| 我前 turn Top-3 | Master Spec § 15.2 | 差异 |
|---|---|---|
| 🥇 U13 visual-brand → W2C | W2C 已在 P1 ✅ | 对齐 |
| 🥈 U8 Egress → W2C handoff manifest | master spec § 9.10 写 U8 是 cross-system egress | **错位** — U8 真路线是 ScoutFlow → ContentFlow/Obsidian 输出, W2C 主菜是 13 surface 内部接 bridge API, 是两件事 |
| 🥉 U1-deep → strategic-upgrade docs | master spec § 19.2 写 U1-deep 是 PRD-v3/SRD-v3 supplement | 对齐但 framing 错 (我说 "进 strategic-upgrade", master spec 框架是 "升 PRD-v3 candidate shell") |
| 漏: **W1A** Tier 分类 | master spec § 15.2 P0 第一项 | **漏掉 P0** |
| 漏: **W1B step 1** OpenDesign v2 candidate | master spec § 15.2 P1 | 漏掉 P1 |

**对齐度**: 5 项推荐对齐 1.5 / 错位 1 / 漏掉 2. **33% 对齐**.

#### B. 16 U vs § 9.x 12 子模块对应

| U | Master Spec § 9.x | 我前 turn 标了吗 |
|---|---|---|
| U6 retrieval-dam | § 9.1 Asset DAM | ❌ |
| U5 agent-fleet | § 9.2 Agent Fleet Dispatch Ledger | ❌ |
| U16 memory-graph | § 9.3 Memory Graph (现状 17 → 50-100) | ❌ |
| U12 tools-catalog | § 9.5 Skills/Tools/MCP Catalog | ❌ |
| U11 anti-pattern | § 9.6 Anti-pattern Defense | ❌ |
| U13 visual-brand | § 9.7 Visual Brand Atlas Cascade | ❌ |
| U14 apple-silicon | § 9.8 Apple Silicon 优化 | ❌ |
| U7 state-library | § 9.9 State Machine Library | ❌ |
| U8 egress | § 9.10 Cross-System Egress | ❌ |
| U15 decision-log | § 9.11 Decision Log Atlas | ❌ |
| U10 runbook | § 9.12 Prosumer SOP Runbook | ❌ |
| U4 visual-asset | § 9.x (没显式映射, gap) | ❌ |
| U1/U2/U3-deep | § 19.2 inventory (PRD/SRD supplement / 5 lane / entity) | ❌ |

**12/16 U 跟 § 9 子模块一对一映射, 我没标**. 新 agent 拼不起来. 这是 master spec 跟 16 ZIP 储能层之间的"可见性断层".

### §1.5 § 16.2 合法升级路径 — D3 单点引是合法的, 我推 B 自写漏看了

我前 turn 推 W1B 选 B (自写 SVG graph), 理由是 "选 A 装 d3 撞 §10 reject list". 但 **master spec § 16.2 第 1 行明文写**:

```text
单点引 D3 (npm d3) → OpenDesign reuse strategy v2 candidate (D5/§5.2 升级 single-point graph lib slot) → spec PR + Hermes 外审 + merge
```

**这是合法升级路径**! 我把 "需走 v2 升级 PR" 当 "禁止". 

→ **应改推**: W1B 走 D 路径 (v2 升级 PR + 单点 d3 引), 自写代价省, 纪律仍守.

### §1.6 对 CC0 三句话治理原则的回应

| CC0 原则 | 我评 | 备注 |
|---|---|---|
| current.md 仍是状态真相, 但不承载全部导航 | ✅ 同意 | START-HERE 已分担导航; current.md 长段保留作 audit trace |
| PRD/SRD v2 + promoted addenda 是当前规划基线 | ✅ 同意 | 不再用 "not approval" 压低; 4 类状态词已锁 |
| master spec / U 层材料文件头明确 north-star / candidate / not runtime unlock | ✅ 同意 | START-HERE § 2 已锁 4 类状态词, 配套 OK |

**总评**: CC0 三句话比我之前的 "Hermes pre-flight 硬阻" 立场松 1 档, 更合 "单人本地" 语境. 我之前偏多 agent 团队治理硬度, CC0 校准对.

### §1.7 对 CC0 5 小建议的回应 + 单 PR 整治计划

| # | 建议 | 我评 | 落地动作 |
|---|---|---|---|
| 1 | README.md (line 1) 入口补 START-HERE + master spec + strategic-upgrade summary | ✅ 必做 | PR #244 一起 |
| 2 | docs/current.md 顶部加 5 行 TL;DR (保留原长段) | ⚠️ 同意但 careful | current.md 是 authority writer 单写, 需 D-XXX entry 配套; 不是 sidecar 直接写 |
| 3 | strategic-upgrade 不叫 "promote", 改叫 "storage/reference land" | ✅ 必做 | 状态词锁 reference storage |
| 4 | PR 前清 .DS_Store / .ruff_cache | ✅ 必做 | git status 已可见 untracked |
| 5 | decision-log.md 轻量记 1 个决策 | ✅ 必做 | 1 个 D-XXX entry, 不是长决策 |

**5 条全同意.**

#### PR #244 范围 (CC0 整治分支已起头, CC1 review)

| 动作 | 操作位置 | 时长 |
|---|---|---|
| docs/00-START-HERE.md 入口导航 | 已 v1, review | 0 (已存在) |
| master spec 顶级路径 | 已在 docs/ | 0 |
| 写 PRD-v3/SRD-v3 candidate shell (CC0 选 A→B-light) | docs/ 或 docs/PRD-amendments/ | 30min |
| README.md 补入口 | line 1 | 5min |
| current.md 顶 5 行 TL;DR (走 D-XXX entry) | docs/current.md | 15min + decision-log entry |
| strategic-upgrade 状态词改 reference storage | docs/research/strategic-upgrade/2026-05-07/README.md | 5min |
| 清 .DS_Store + .ruff_cache | working tree | 1min |
| Tier 1+2 land main / Tier 3 archive 分类 | strategic-upgrade outputs/ | 30-45min (走 master spec § 13.1 W1A) |
| doc1/2/3 关系说明 | START-HERE § 5 已含 | 0 |
| U 层储能地图 | START-HERE § 6 已含 | 0 |
| decision-log 1 行 D-XXX entry | docs/decision-log.md | 5min |

**总时长**: ~1.5h CC1 一气呵成 + 战友 V-PASS.

#### PR #244 不做

- ❌ 任何新门禁
- ❌ 升级 PRD/SRD 为新版本 (v2 + promoted addenda 仍是基线)
- ❌ 把 strategic-upgrade 全 promote (改叫 reference storage)
- ❌ 修改 §16.1 红线 (锁定 15 条不增不减)

---

## §2 本次会话识别错误清单 (10 条)

每条按以下维度归因:
- **错的事**: 具体描述
- **后果**: 给战友 / 协作的影响
- **元认知归因**: 根据 `~/.claude/rules/codex-metacognition-learnings.md` §1 八条
- **catch by**: 谁发现 (CC0 / 战友 / 自审)

### Error 1 — U16 file count 估错 10×

| | |
|---|---|
| 错的事 | W2D Codex prompt 估 U16 ~1004 file (真值 96 .md) |
| 根因 | `find` 命令没加 `-type f`, 子目录被 count 进总数 |
| 后果 | 给 Codex 的 prompt 期望 200-500 candidate / 6 subagent 并行 = 严重 over-engineering. 真值 96 file 应该 1 主 agent 30-60min 跑完 |
| 元认知归因 | §1.1 措辞精确度 (不验证就用估值) + §1.6 dry-run 文化 (没先 ls -la 校验) |
| catch by | CC0 (在另一窗口 ls -la 真 count, 报告 "差 10 倍, Codex 6 subagent 是 over-engineering") |

### Error 2 — 错引 baseline-roadmap-candidate 当 stack authority

| | |
|---|---|
| 错的事 | 战友问 "Z 开头是什么框架", 我答 "Zustand", 引 `docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md` § 117-119 stack 列表 |
| 根因 | 文件名 `-candidate-` 后缀明牌, 但我没 grep frontmatter `status:` 字段, 也没核 PR merge 状态. 把 brainstorm 期 candidate 当真理 |
| 后果 | 战友被误导. CC0 (architect) 在另一窗口反向 catch: "真 authority 是 PR #122 §10 reject list, 你引的 stack 直接违反 reject list 第 2/4 条" |
| 元认知归因 | §1.1 措辞精确度 (引 candidate 不带等级) + §1.7 唯一真源 (stack 决策应有唯一 authority, 我引第二份) |
| catch by | CC0 (architect) |

### Error 3 — GPT Pro 12 窗 over-saturate

| | |
|---|---|
| 错的事 | 推 "今晚最大马力 4-Tier" 含 GPT Pro 12 窗 (P0 ×3 + P1 ×4 + P2 ×5) |
| 根因 | 把战友 "最大马力" 字面理解成 "最多窗口", 没问 "每窗 24h 内是否有 actionable consumer" |
| 后果 | CC0 砍后 4 窗 (P0 ×3 + P1 #4) 才合理. P2 ×5 全是 5 overflow lane Hold spec, 跑出来 spec 也不能用, 等 3 个月红线/vendor 都变了 |
| 元认知归因 | §1.5 contract 即真因 (没把 "actionable within 24h" 写进资源分配 contract) + 反方意见薄弱 |
| catch by | CC0 |

### Error 4 — W2D Codex prompt over-engineering

| | |
|---|---|
| 错的事 | 给战友写 paste-ready Codex prompt, 含主 agent + 6 subagent 并行扫 1004 file (基于 Error 1 错估) |
| 根因 | (a) Error 1 的 file count 错估传染; (b) 没看清 GPT Pro 一夜已 atlas 完 79 nodes (judgment-ready), 把 judgment-heavy 任务当 read-heavy 任务 |
| 后果 | 战友差点 paste 给 Codex 跑 over-engineered 任务. CC0 在另一窗口 D 路径 (Read MASTER-MEMORY-ATLAS.md) 5min 看穿真态 |
| 元认知归因 | §1.2 状态机思维 (没看清任务真态 = judgment-heavy) + §1.6 dry-run 文化 (没先 ls -la 看 atlas 是否已 ready) |
| catch by | CC0 (D 路径核实) |

### Error 5 — 重复提 "5 漏洞", master spec § 13.3 已集成

| | |
|---|---|
| 错的事 | 给战友 critical review architect 7 wave 路线时, 提 "5 漏洞" (dispatch 注册 / surface-route mapping / DTO 锁 / 16 ZIP 分类 / motion 边界) |
| 根因 | master spec § 13.3 一张表早已集成这 5 漏洞修订. 我没读 § 13.3 就重复劳动. CC0 也没 catch (CC0 也没读 master spec 全文) |
| 后果 | 战友看到 5 漏洞误以为是新发现, 被多花一轮决策成本. master spec 写者 (CC1 在更早 session) 的劳动被埋没 |
| 元认知归因 | §1.7 唯一真源 (master spec 是 single source of routing truth, 不引就重复造) |
| catch by | 自审 (本次 retrospective §1.3) |

### Error 6 — W1B 推 B 自写, 漏看 § 16.2 D 升级路径

| | |
|---|---|
| 错的事 | 推 W1B (PF-C4-EXT 3 TODO 实施) 选 B 自写 SVG graph, 理由 "装 d3 撞 §10 reject list 第 2 条" |
| 根因 | master spec § 16.2 第 1 行明文写 "单点引 D3 → OpenDesign v2 candidate 升级 PR → 合法解禁". 我把 "需走升级 PR" 当 "禁止", 没把 "合法升级路径" 摆给战友 |
| 后果 | 战友若选 B 自写, 工作量大且 1-2 dispatch 才能完, vs D 路径升级 PR + 单点 d3 引可能更省 |
| 元认知归因 | §1.5 contract 即真因 (升级 PR 是 contract 内合法路径, 不是 boundary violation) + §1.8 归因纠偏 (没区分 "禁止" vs "需 escalate") |
| catch by | 自审 (本次 retrospective §1.5) |

### Error 7 — Top-3 推荐对齐 § 15.2 P0-P1 错位

| | |
|---|---|
| 错的事 | 我前 turn Top-3 (U13 + U8 + U1-deep) 是按 U 视角排, master spec § 15.2 P0-P1 是按 wave 视角排. 漏掉 W1A (P0) + W1B step 1 (P1) |
| 根因 | 我没引 § 15.2 优先级表, 自己重新排了一份 |
| 后果 | 战友看 Top-3 跟 master spec 优先级不对齐, 治理一致性受损. 重复劳动 |
| 元认知归因 | §1.7 唯一真源 (优先级排序应有唯一 authority) + §1.3 接口思维 (U 是接口元素, wave 才是消费动作) |
| catch by | 自审 |

### Error 8 — U8 → W2C handoff manifest 错位

| | |
|---|---|
| 错的事 | Top-3 第 2 推荐 "U8 Egress → W2C 接线 + handoff manifest". 但 U8 真路线是 cross-system egress (ScoutFlow → ContentFlow/Obsidian 输出 contract, master spec § 9.10) |
| 根因 | 没看 § 9.10 U8 在 master spec 里的真路线 |
| 后果 | W2C 真主菜是 13 surface 接 bridge API (内部), U8 真路线是输出 contract (外部), 是两件事. 推荐错位会让战友把不相关任务塞同一 wave |
| 元认知归因 | §1.3 接口思维 (没看接口归属) + §1.7 唯一真源 (§ 9.10 是 U8 真路线 source) |
| catch by | 自审 |

### Error 9 — 没标 12 U vs § 9.x 子模块对应

| | |
|---|---|
| 错的事 | 16 U ROI matrix 缺一列 "Master Spec § 9.x 对应". 12/16 U 跟 § 9 子模块 1:1 映射 |
| 根因 | 没看 § 9.x. 把 16 U 当孤立资产, 不知道 § 9.x 给的就是消费路线 |
| 后果 | 新 agent 拿到 ROI matrix 不知道 U → wave 的桥梁 (§ 9.x 是桥), 拼不起来. CC0 说的 "可见性断层" 实例 |
| 元认知归因 | §1.3 接口思维 (U 与 § 9 是接口对接, 没显式标) + §1.7 唯一真源 |
| catch by | 自审 |

### Error 10 — Hermes pre-flight 立场过硬

| | |
|---|---|
| 错的事 | 推 W2C 启动必须 Hermes pre-flight 外审硬阻. CC0 校准 "Hermes 是 candidate role, 失联会卡死 Codex 启动" |
| 根因 | 我把 Hermes 提到 "pre-flight 硬阻 gate" 等级, 但 Hermes 是 3rd-party candidate, 战友不一定能保证响应时效 |
| 后果 | 如果 Hermes 当晚不在线, W2C 通宵窗废, 损失整夜 |
| 元认知归因 | §1.5 contract 即真因 (硬阻 gate 必须有 SLA, Hermes 没 SLA) + §1.4 边界守护 (把 candidate role 当硬 gate 是过度守护) |
| catch by | CC0 (校准 "Hermes 建议性, 不阻 Codex 启动") |

---

## §3 11 条新增 instinct (#9-#19, 战友显式 8 条 + CC1 前 turn 加 3 条)

> 以下加在 `~/.claude/rules/codex-metacognition-learnings.md` §3 现有 8 条清单后, 编号 **9-19**. 其中:
> - **#9-#14** (6 条): CC1 self-audit 6 instinct (本 retrospective 原版)
> - **#15** (1 条): CC0 加的 raw PARA 路径 contract
> - **#16** (1 条): 战友加的 Anthropic Opus self-audit ≠ Layer 2 cross-vendor audit (PR #244/#245 实证)
> - **#17/#18/#19** (3 条): CC1 前 turn 加的 PR # 验证 / handoff trace / default 推荐 ⭐
>
> 详细 11 条内容见 instinct §3 ledger (PR #246 已 land). 本节只展开 #9-#14 (6 条原版), #15-#19 5 条详细见全局 rule 文件.

```text
[ ] 9. 任何 "file count" 估值前必加 `find -type f` 或 `wc -l` 二次校验
    → 子目录会被 count 进总数, 不校验直接用估值会差 10x
    → 触发: 给 Codex / GPT Pro / Hermes 任何 paste-ready prompt 含 "~N file" 时

[ ] 10. 审 stack / 路线 / 规范决策时第一步: grep frontmatter `status:` + 核 PR merge 状态
    → 文件名带 `candidate-` 后缀的不是 authority
    → 文件名不带 `candidate-` 也不一定是 authority (要看 frontmatter)
    → 触发: 任何 "<frame>是什么 / 用什么 stack / 哪个版本 baseline" 类问题

[ ] 11. 资源分配前必问 "每窗 / 每 agent / 每 dispatch 24h 内是否有 actionable consumer"
    → 没 consumer 的 spec 是 over-engineering, 等 3 个月红线/vendor/stack 都变了 spec 失效
    → 触发: 推 GPT Pro N 窗 / Codex M dispatch / 任何并行资源分配

[ ] 12. 派 agent 前先问 "task 是 read-heavy 还是 judgment-heavy"
    → read-heavy 适合 Codex N subagent 并行
    → judgment-heavy 适合 Opus 单跑 (Codex middleman 多余)
    → 检查方式: 源材料是否已被预处理? GPT Pro 一夜跑过的 atlas/index 通常 judgment-ready
    → 触发: 任何 "派 Codex N subagent" 决定

[ ] 13. 任何调研 / 推荐 / 派单 prompt 前必扫 master spec § 13 (wave list) + § 15.2 (优先级) + § 16 (红线 + 升级路径)
    → 这三段是 ScoutFlow 治理状态机的 single source of truth, 不引就是重复劳动
    → master spec § 13.3 已集成历史 5 漏洞修订, 不重复提
    → master spec § 16.2 给合法升级路径, 不要把 "需 escalate" 当 "禁止"
    → 触发: 给战友任何 "下一步该跑什么 wave / 推荐 / commander prompt" 类回答

[ ] 14. 16 ZIP / U 系列评估前必查 master spec § 9.x 子模块对应表
    → 12/16 U 跟 § 9 子模块 1:1 映射, § 9 给的就是消费路线
    → 不查 § 9.x 直接评 U 的 ROI 会推荐错位 (e.g. U8 真路线是 § 9.10 cross-system egress, 不是 W2C 内部接线)
    → 触发: 任何 "U 矩阵 / ZIP 储能层 / 16 cluster" ROI 评估
```

---

## §4 项目治理体系优化建议

### §4.1 Master Spec 显性化 (CC0 原始建议 + CC1 加固)

| # | 建议 | 落地动作 |
|---|---|---|
| 1 | Master spec 路径放 docs/ 顶级 (已在) | ✅ 已落 |
| 2 | START-HERE 顶级 → 5 min cold start (已在) | ✅ 已落 |
| 3 | START-HERE § 3 cold start ladder L0 必读 | 应增加 master spec § 13.1 / § 15.2 / § 16 三段为 L0 必读 (现在 L0 只列 current/task-index/decision-log/START-HERE) |
| 4 | Master spec 在 § 13.1 wave 表前加一行 "新 agent 起手必读本节" | 应加 |
| 5 | § 13.3 5 漏洞集成现状改为 changelog 式: "修订自 CC0 (yyyy-mm-dd, session X)" | 应加 — 让新 CC0 不重复提 |

### §4.2 16 U vs § 9.x 显式 cross-reference 表

| 落地位置 | 内容 |
|---|---|
| 加在 master spec § 9 章节末尾 (新 § 9.13) | "16 U → § 9.x 对应表" — 13 行 1:1 映射 + 4 行 gap (U1/U2/U3-deep + U4 没显式对应) |
| 或加在 START-HERE § 6 储能层地图末尾 | 同上, 但作为 ladder 入口 |

**作用**: 解决 §1.4 / Error 9 的可见性断层. 新 agent 看到 ROI matrix 立刻知道 wave 桥.

### §4.3 双 Opus 互审常态化

本次 session 实证 CC1 / CC0 双 Opus 互审 catch 4+ 错. 建议:

| 建议 | 落地 |
|---|---|
| 4-agent v3 memory 加一条 "双 Opus 互审 (CC1 ↔ CC0) = 工程纪律层独立, 不必等 Hermes" | 写进 `memory/project_4_agent_division_v3.md` |
| Hermes 降级为 "external sanity check, 战友按需调用, 不是 pre-flight 硬阻" | 写进 master spec § 13.2 W2C 行 |
| 战友 paste 流程: "战友 → CC1 → CC0 互看一轮 → 战友拍" 作为标准回路 | 写进 START-HERE § 8 4-agent 速查 |

### §4.4 Auto-compact 后的 CC1 self-check

本次 session 经历 1 次 auto-compact. 重连后我用了 ~30% master spec 而不是 100% — 因为 SessionStart 注入的 context 不含 master spec 全文.

**建议**: SessionStart hook 注入 START-HERE § 3 的 L0 必读路径 (含 master spec § 13.1), 让重连后 CC1 第一动作是 Read 这三段.

---

## §5 给未来 ScoutFlow Session 的冷启动指导

### §5.1 START-HERE § 10 增补 — "新 agent 必跑 5 件事" 升级版

```text
原 5 件事 (START-HERE § 10):
1. Read 本文件 (你正在做)
2. Read docs/current.md TL;DR
3. Read docs/task-index.md 看 Active 是 0/3 还是已满
4. Bash git log --oneline origin/main -5 看最近 5 commit
5. Decide: 你的任务在 §7 wave 的哪个?

CC1 增补 3 件 (本次 retrospective 沉淀):
6. Read master spec § 13.1 (11 wave 列表) + § 15.2 (优先级 P0-P4) + § 16 (红线 + 升级路径)
   → ScoutFlow 治理状态机的 single source of truth
   → 不读这三段就开工 = 重复劳动 / 路线漂移 / 红线漏踩

7. Bash find <dir> -type f | wc -l 校验任何 "~N file" 估值
   → 子目录会被 count 进总数, 不校验直接用估值会差 10x

8. 审 stack / 路线决策时 grep frontmatter `status:` + 核 PR merge 状态
   → 文件名带 `candidate-` 后缀的不是 authority
   → 这一步在 5 min 起手也要做, 不是 deep dive
```

### §5.2 错误反模式清单 (避免)

| 反模式 | 避免方法 |
|---|---|
| 把 candidate doc 当 authority 引 | grep `status:` + 核 PR merge |
| 给 Codex/GPT Pro 资源分配过 saturate | 每窗必问 "24h 内有 actionable consumer 吗" |
| 把 judgment-heavy 任务派给 Codex | 先问 "源材料是否已被预处理 / 是否 atlas-ready" |
| 重复提 master spec § 13.3 已集成的 5 漏洞 | 调研前必扫 § 13.3 |
| 推 W1B 自写不引 § 16.2 升级路径 | 调研前必扫 § 16.2 |
| 把 16 U 当孤立资产, 不查 § 9.x 对应 | 调研前必扫 § 9.x |
| 把 Hermes 提到 pre-flight 硬阻 | 4-agent v3 memory 已锁 "Hermes 候选, 不阻 Codex" |

### §5.3 双 Opus 协作 SOP

```text
战友抛任务 → CC1 (这边) 给 v1 → 战友 paste 给 CC0 → CC0 给 critical review → 战友 paste 给 CC1 → CC1 接住 + 自检 + 给 v2 → 战友拍 → 执行 (派 GPT Pro / Codex / 自做)

注意:
- 双方都不知道对方有什么 context, 战友是唯一 context bridge
- catch 错误是双向的, 不是 CC0 单 catch CC1
- v1 v2 命名让战友追踪迭代
- v2 后还要打架就升 v3, 不要无限迭代 (3 轮内拍板)
```

---

## §6 元元洞察 + 沉淀路径

### §6.1 元元洞察 — "可见性断层" 是治理的核心问题, 不是 "门禁不够硬"

我之前推 "Hermes pre-flight 硬阻" 是治理硬度方向错. CC0 校准 "单人本地三句话原则" 后, 真正的问题暴露:

> **不是文档不够多, 是文档拼不起来. 不是门禁不够硬, 是入口不够清.**

ScoutFlow 当前文档真态:
- current.md / task-index / decision-log = real-time 真态 (够)
- PRD-v2 + addenda + SRD-v2 + addenda = 规划基线 (够)
- master spec = 11 wave routing + 12 子模块 inventory (够)
- 16 ZIP 储能层 = 1.48M 字 reference (够)
- doc1/2/3 = 历史 reference (够)
- 17 memory = cross-session 复利 (够)

**够 ≠ 拼得起来**. 新 agent / 重连 CC1 / 新 CC0 都没有自动桥. 解决方向是:
1. START-HERE 作为 L0 入口 (已有, 需 § 3 ladder 增补)
2. master spec § 9.x 跟 16 U 显式 cross-reference (待加)
3. master spec § 13.3 改 changelog 式 (待加)
4. 双 Opus 互审常态化 (本次 session 实证可行)

### §6.2 元元洞察 — "战友是唯一 context bridge", 协作设计必须围绕这一事实

CC1 / CC0 / GPT Pro / Codex / Hermes 之间没有自动通信. 战友是唯一 paste 中介. 这意味着:

- 任何 agent 输出必须 paste-ready (战友不能再加工)
- 任何 agent 输入必须 self-contained (不假设对方知道前轮)
- 任何决策必须显式 (战友不背 implicit context)
- 任何拍板必须 3 选项以内 (战友决策疲劳)

我前 turn 给 "战友拍 4 问" 已经偏多. 下次推 "战友拍 1-2 问" 为常态.

### §6.3 沉淀路径 — 本次 session 4 类资产入档

| 资产 | 落地 | 状态 |
|---|---|---|
| memory `feedback_gpt_pro_heavy_producer.md` | `~/.claude/projects/.../memory/` | ✅ 已写 (前 turn) |
| memory `feedback_prompt_design_principles.md` (派单 7 原则) | 同上 | ✅ 已写 |
| memory `project_4_agent_division_v3.md` (Codex 双能力) | 同上 | ✅ 已写 (CC1 在另一窗口) |
| memory `feedback_codex_long_runner.md` (~84 dispatch 实证) | 同上 | ✅ 已写 (CC1 在另一窗口) |
| 本 retrospective | `docs/research/post-frozen/CC1-session-retrospective-2026-05-07.md` | ✅ 本次 |
| 元认知 §3 增补 #9-#19 (11 条, 战友显式 8 + CC1 加 3) | `~/.claude/rules/codex-metacognition-learnings.md` § 3 末尾 | ✅ 已 land PR #246 (commit 20d18e6) |
| START-HERE § 10 升 8 件 + 新 § 11 ad-hoc 路径 contract | `docs/00-START-HERE.md` § 10/§ 11/§ 12 | ✅ 已 land PR #246 |
| § 9.x ↔ 16 U cross-reference 表 (5 U gap, audit amend) | master spec § 9.13 | ✅ 已 land PR #246 |

---

## §7 战友拍板 (≤ 2 问)

战友总监视角拍板入口, 不要求逐条:

1. **本 retrospective 是否 land 进 PR #244?** — 当前路径 `docs/research/post-frozen/CC1-session-retrospective-2026-05-07.md`, 状态 `candidate / retrospective / not-authority`, 不需要走 authority writer slot
2. **§3 元认知增补 9-14 + §5.1 START-HERE § 10 增补 6/7/8 + §6.3 § 9.x ↔ U cross-reference 表 — 三组改动是否同意进 PR #244?** (实施成本 ~30 min)

战友拍 ✓ 我立刻动手. 拍 ✗ 也 OK, 本 retrospective 单独存档不进 PR 也是合规的 (reference storage).

---

## §8 致谢 + 自评

### §8.1 致谢

- **战友**: catch 我 "用了 master spec 多少" 是关键问 — 不问我自己不会自审
- **CC0** (并行 session): catch 我 4+ 处错 (1004 vs 96 file / Top-3 错位 / over-saturate / W2D over-engineering / Hermes 立场过硬)
- **GPT Pro 一夜 16 窗**: 提供了 1.48M 字储能层 + U16 79 nodes atlas (我虽然没全用上, 是我的问题不是它的问题)
- **Codex Long Runner**: 80packs Run-3+4 24 dispatch 一夜实证, 给我 Codex 真实能力的边界感

### §8.2 自评

| 维度 | 自评 | 说明 |
|---|---|---|
| 工作量 | 中 | ~8h session, 多次重启重连, 累计 ~30 turn |
| 决策质量 | 中-低 | 10 错误清单已暴露, 多数错误是 "应该读没读" 类, 不是 "读了想错" 类 |
| 协作纪律 | 中 | 双 Opus 互审 catch 错, 但前期 saturate 立场过硬 |
| 元认知应用 | 中 | §1.7 唯一真源 / §1.6 dry-run 多次违反, 增补 §3 后期望提升 |
| 战友带宽节约 | 中-低 | 多次 "拍 4 问" 偏多, 应该 "拍 1-2 问" |
| 输出 paste-ready 度 | 中 | markdown 格式 OK, 但有时段落过长不利于战友 paste 给 CC0 |

**总评**: 这次 session 是 "高量低质" 模式. 量是足的 (反思深 + 文档全), 质有缺 (10 错误是结构性问题). 增补 §3 6 instinct + START-HERE § 10 增补 + § 9.x ↔ U cross-reference 表 后, 期望下次 session "中量高质".

---

> **本文 by CC1 (Anthropic Opus 4.7), 2026-05-07 22:30 GMT+8**
> **目的**: ScoutFlow CC1 session 错误档案 + 元认知沉淀, 不是替代 authority 的整治方案
> **后续**: 等战友拍板进 PR #244 (作为 reference storage 一员) 或独立存档不进 PR (也合规)
> **回路**: 任何未来 CC1/CC0 session 起手, 建议读本文件 §2 错误清单 + §3 增补 instinct + §5 SOP. 5 min 内可消化.
