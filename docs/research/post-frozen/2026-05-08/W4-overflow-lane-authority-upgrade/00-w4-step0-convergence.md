---
title: ScoutFlow W4-B Step0 Convergence
status: "candidate north-star"
type: "convergence / 裁决 / 重排"
not_authority_writeback: true
not_runtime_approval: true
created_at: 2026-05-08
base_ref: origin/main
main_sha: 3d209d4bbdda8b5ca85cd5c6e85bb88217865397
historical_prompt_values_are_reference_only: true
---

# W4-B Step0 Convergence

> 这是 `candidate north-star`，不是 authority writeback，不是 runtime approval，不是 migration approval。
> Step0 的职责是裁决、重排、统一引用；它不是新的真相源，不解禁任何 overflow lane，不预先批准任何 vendor、migration 或 `write_enabled` flip。

## §0 Prerequisite Check

| Check | Live result | Verdict |
|---|---|---|
| `git fetch origin` | completed | pass |
| `git rev-parse origin/main` | `3d209d4bbdda8b5ca85cd5c6e85bb88217865397` | pass |
| `git log -1 --oneline origin/main` | `3d209d4 Merge pull request #256 from RayWong1990/codex/w4-a-step0_5-authority-rebase` | pass |
| `python tools/check-docs-redlines.py` | pass | pass |
| `python tools/check-secrets-redlines.py` | pass | pass |
| `00-w4-step0-convergence.md` pre-exists? | no | pass |
| authority rebase absorbed? | yes, PR #256 already on `origin/main` | pass |

**Boundary restatement**

- 本文只写 candidate north-star 层。
- 不改 `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `docs/00-START-HERE.md`。
- 不改 lane 1/2/4 主文档，不改对应 PATCH。
- hard-code 的 PR 号、SHA、count 只作撰写时参考；真值以本节 check 为准。

**Validation receipt guard (PR262 erratum)**

- 若验证目标是 forbidden phrase / forbidden claim **无命中**，receipt 必须使用 `! rg -n "pattern" path...` 或等价 no-match 脚本。
- 不允许用裸 `rg -n "pattern" path...` 伪装成 no-match pass；裸 `rg -n` 只适合证明应当存在的锚点。
- 不得为了让 no-match 命令通过而删除有意义的 boundary wording；修的是 validation command semantics，不是擦掉边界词。

## §1 §19.1 目标四层映射表

| Tier | 包含（must） | 不包含（must NOT） |
|---|---|---|
| Tier 1: current authority | `docs/current.md`、`docs/task-index.md`、`docs/decision-log.md`、`docs/00-START-HERE.md` | 任何代码、任何 amendment、任何 candidate |
| Tier 2: promoted addendum | `docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md`（promoted）、`docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md`（promoted）、`docs/research/repairs/opendesign-reuse-strategy-candidate-2026-05-05.md`（PR #122 promoted） | thin shell PRD-v3 / SRD-v3（仍 candidate）、任何未 promoted candidate |
| Tier 3: candidate north-star | `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`、`docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/**`、本文件 `00-w4-step0-convergence.md` | promoted addendum |
| Tier 4: reference storage | `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/` ~ `U16-memory-graph/`、`~/.claude/rules/*`、`~/.claude/projects/.../memory/*`、`bridge/config.py:24,36` 的 `write_enabled=False` invariant 文档化提及（不是代码本身） | 任何 candidate 或 authority |

### §1.1 现 §19.1 散列表逐条归层

| 旧 §19.1 条目 | 新层级 | 处理 |
|---|---|---|
| `docs/current.md` | Tier 1 | 保留为 current authority |
| `docs/task-index.md` | Tier 1 | 保留为 current authority |
| `docs/decision-log.md` | Tier 1 | 保留为 current authority |
| `docs/00-START-HERE.md` | Tier 1 | 补入 current authority |
| `docs/research/repairs/opendesign-reuse-strategy-candidate-2026-05-05.md` (PR #122 promoted) | Tier 2 | 从旧 Tier 1 迁到 promoted addendum |
| `docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md` | Tier 2 | 从旧 Tier 1 迁到 promoted addendum |
| `docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md` | Tier 2 | 从旧 Tier 1 迁到 promoted addendum |
| `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` | Tier 3 | 明确为 candidate north-star |
| `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/**` | Tier 3 | 明确为 W4 source bundle |
| `00-w4-step0-convergence.md` | Tier 3 | 新增 convergence artifact |
| `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/` ~ `U16-memory-graph/` | Tier 4 | 保持 reference storage，不直接当 authority |
| `~/.claude/rules/aesthetic-first-principles.md` 及同类规则 | Tier 4 | 从旧 Tier 1 迁到 reference storage |
| `~/.claude/projects/.../memory/*` | Tier 4 | 明确为外部记忆 reference |
| `bridge/config.py:24,36` | Tier 4 | 只保留 invariant 文档化提及，不把代码本身写成 authority |

## §2 Step0 12 条裁决 schema

| ID | 主题 | 裁决（adopted） | reject 备选 | 落地位置 | 触发再裁决条件 |
|---|---|---|---|---|---|
| D-01 | master spec §19.1 4 层映射 | 按 §1 四层映射表执行 | 维持混合列表现状 | `master spec §19.1` 修订 | 新 promoted addendum 加入时 |
| D-02 | Lane 4 toolchain | `manual SQL + storage.py loader` | `Alembic toolchain first` | Lane 4 spec PR（E 窗） | DB scale > 1M rows 或 schema 改频率 > 1 次/月时 |
| D-03 | Lane 2 download primary | `yt-dlp`（preferred first-pass hypothesis） | `BBDown primary` | Lane 2 spec PR（C 窗）§3 | `yt-dlp` legal refresh fail（30 day window） |
| D-04 | Lane 2 download fallback | `BBDown reserve-only`（preferred fallback hypothesis） | `yt-dlp` single-source | Lane 2 spec PR（C 窗）§3 | `yt-dlp` 主路 < 80% 成功率时 |
| D-05 | Lane 2 ASR primary | `Whisper.cpp Metal`（preferred first-pass hypothesis） | `FunASR primary` | Lane 2 spec PR（C 窗）§4 | Apple Silicon legal/perf benchmark V-PASS 后才锁定 |
| D-06 | Lane 2 ASR fallback | `FunASR`（preferred fallback hypothesis） | `OpenAI Whisper API` | Lane 2 spec PR（C 窗）§4 | benchmark cost > $10/h 或 transcript match < 80% 时 |
| D-07 | Lane 1 frontmatter 字段数 | `12`（含 `transcript_sha256` / `asr_engine` / `language`） | `4 raw` / `16 over-engineered` | Lane 1 spec PR（D 窗）§2 | promotion 到 PRD-v3 时再扩 |
| D-08 | Lane 1 secret scan 范围 | `title + url + transcript 全文 + summary` 全扫 | 仅 `url` 扫 | Lane 1 spec PR（D 窗）§3 | leak 事件后扩 |
| D-09 | `write_enabled` flip 路径 | 独立 flip PR / `1 PR 1 flip` / 不与 spec PR 合并 | 在 spec PR 内 flip | Phase 3 single-item closure §8 | — |
| D-10 | 16U 应用率 | 本轮真用 `5/16`（`U2 + U3 + U11 + U14 + U15`），见 §5 | 全 `16` 全用 / `0/16` 不用 | Step0 §5 | 后续 lane 实施时按需 promote |
| D-11 | PRD-v3 / SRD-v3 promotion gate | single-item closure V-PASS 后 promote，见 §4 | Phase 6 才临时设计 | Step0 §4 | — |
| D-12 | 5 PR Layer 2 audit | A/B/D 强制 cross-vendor；C/E 可放宽 | 全 Codex 自审 | `00-SHARED-BRIEF.md` §合并审计 SOP | C/E PR diff > 800 LOC 时升级强制 |

## §3 Lane 1 ↔ Lane 2 接口握手 contract draft

> 本节只定义 handshake draft。字段名在 C 窗 / D 窗 spec PR 中最终锁定；当前不授予 ASR、下载、vault true write 任何执行许可。

### §3.1 Transcript handoff schema（Lane 2 → Lane 1, draft）

```jsonc
{
  "transcript_text": "str",        // ASR 原文
  "language_detected": "str",      // ISO 639-1
  "duration_seconds": 0.0,
  "asr_engine": "str",             // whisper.cpp-large-v3 / funasr-paraformer
  "asr_model_sha256": "str",       // 模型权重 hash, 用于 reproducibility
  "extraction_seed": {
    "title_candidate": "str",
    "tags_candidate": ["str"],
    "summary_candidate": "str"
  },
  "trust_trace_id": "str",         // 引 W2C Trust Trace DTO (PR #252 已 land)
  "source_url": "str",
  "capture_date": "str"            // ISO 8601
}
```

### §3.2 Vault commit input schema（Lane 1 receives, draft）

12 fields:

1. `title`
2. `source_url`
3. `capture_date`
4. `transcript_engine`  ← 来自 transcript handoff schema `asr_engine`
5. `transcript_sha256`  ← Lane 1 自算（atomic write 前）
6. `duration_seconds`
7. `language`
8. `tags`
9. `summary`
10. `status`  ← `candidate / draft / promoted`
11. `domain`  ← `中文座舱 / 多语种 / 通用座舱 / ...`
12. `type`  ← `compiled / crafted`

### §3.3 Secret scan / atomic write / boundary

`secret_scan_range`

- `title`
- `source_url`
- `transcript_text`（full）
- `summary`

`atomic_write`

- 单文件 `.md`
- 路径策略：`path_policy.py` 决定
- rollback：写失败 → 删半成品 + 报告

`boundary`

- Lane 2 不得直接写 vault（输出 dict，不调 `vault.writer`）
- Lane 1 不得直接调 ASR / 下载（接收 dict，不知道 transcript 怎么来）
- preview helper 不等于 production writer
- Lane 1 secret scan = final defense，不可短路

## §4 Promotion Gate v0

| 候选 spec 段 | 可 promote 条件 | 目标 promoted 位置 | 不能 promote 条件 |
|---|---|---|---|
| Lane 2 `§vendor/fallback contract` | single-item Phase 3 + small-batch Phase 4 全 V-PASS | PRD-v3 `§runtime/source-strategy` | `yt-dlp` legal failure / vendor < 80% 成功率 |
| Lane 2 `§ASR benchmark` | Phase 3 transcript ≥ 90% match（vs ground truth subtitle） | SRD-v3 `§asr` | benchmark < 80% / cost > $10/h |
| Lane 1 `§12-field frontmatter` | Phase 3 first true write merged | SRD-v3 `§vault-commit` | secret scan miss event |
| Lane 1 `§secret scan contract` | Phase 4 small-batch 0 leak | SRD-v3 `§security` | 出现 leak |
| Lane 4 `§RI / backup / rollback` | Phase 5 真 migration drill V-PASS | SRD-v3 `§db` | drill fail |

### §4.1 本轮明确不能 promote

- Lane 3（`browser_automation`）— 本轮不动
- Lane 5（`full_signal_workbench`）— 本轮不动
- Alembic toolchain — deferred candidate，对应 D-02 reject 备选

### §4.2 lane spec PR 可 promote 段标注

- C 窗 / Lane 2：只允许把 `vendor/fallback contract` 与 `ASR benchmark` 作为 future-promotable 段标出来，不得把整篇 spec 预设为可 promote。
- D 窗 / Lane 1：只允许把 `12-field frontmatter` 与 `secret scan contract` 作为 future-promotable 段标出来，不得把 `write_enabled` flip 一并 promote。
- E 窗 / Lane 4：只允许把 `RI / backup / rollback` 标为 future-promotable；migration execution、Alembic、真实 SQL 仍留 future gate。

## §5 16U 应用率显式声明

### §5.1 本轮 W4 v4 真用（5/16）

| U | 用法 | 本轮消费位置 |
|---|---|---|
| U2 | lane spike commands | Lane 1/2/4 spec PR 直接消费（vendor matrix / spike commands） |
| U3 | 4 entity v0 contract | Lane 4 spec PR 消费（locked DTO guard） |
| U11 | anti-pattern | Lane 1/2 spec PR 消费（反模式避免） |
| U14 | Apple Silicon | Lane 2 spec PR 消费（Whisper.cpp Metal benchmark） |
| U15 | decision log | 全 lane 消费（历史 PR band 引用） |

### §5.2 留 next promotion candidate（3/16）

| U | 用法 | 触发 |
|---|---|---|
| U1 | PRD-v3 / SRD-v3 candidate | 配合 Promotion Gate v0（§4）在 Phase 6 消费 |
| U10 | prosumer SOP runbook | Phase 3 single-item closure 写 SOP 时消费 |
| U16 | memory graph | 已 land via PR #245，持续 cross-session 消费 |

### §5.3 留 next-wave candidate（8/16）

| U | 用法 | 触发 |
|---|---|---|
| U4 | visual_asset SQLite | W5I（评论 / 楼中楼）时消费 |
| U5 | agent_fleet_dispatch_ledger | W6K Memory 沉淀时消费 |
| U6 | visual-DAM thumbnail + pHash | W5H source matrix 时消费 |
| U7 | state machine library | W2C 已部分消费（5 态状态机），后续按需扩 |
| U8 | cross-system egress manifest | Phase 4 small-batch 时消费 |
| U9 | Phase 2-4 dispatch catalog ≥71 prompt | 如走 multi-PR swarm 时消费（本轮 5 窗够，不用） |
| U12 | skills + tools + MCP + plugin catalog | Phase 3 single-item closure 时消费（工具选型 reference） |
| U13 | visual style brand atlas | UI 已落（PR #252），持续 reference |

### §5.4 不留候选（0/16）

无。全 16U 至少有 future-trigger 路径。

### §5.5 触发再消费条件

- 任何 16U 沉睡 > 30 day → audit 是否 still relevant
- Promotion Gate v0（§4）通过 → 对应 U promote 到 PRD-v3 / SRD-v3 promoted base

## §6 PR band 内嵌引用方式

| PR band | 关键 lessons | retrieval 方式 |
|---|---|---|
| `#1-#54` | bootstrap / authority-first / single-writer / no-runtime 偷开 | U15 retrieval layer + decision-log |
| `#55-#160` | shoulders / bridge-vault / Phase 1A boundary / candidate-vs-authority | U15 retrieval layer + `docs/research/repairs/opendesign-reuse-strategy-candidate-2026-05-05.md` |
| `#161-#192` | Wave 5 candidate factory / Wave 6 open-closeout / docs-only candidate production | U15 retrieval layer + task-index Done section |
| `#193-#240` | post-frozen amendment / readback / proof-pair / partial closeout / introduced-vs-exposed | U15 retrieval layer + decision-log amend trail |
| `#241-#255` | PF-C4 / W2D / W2C / W1B / W3E 的 current baseline | task-index + decision-log + live GitHub `gh pr` |

> 反模式：逐条重述 248 PR。Step0 只定义 band + retrieval layer，不复制整本 PR atlas。

## §7 关系图（text）

1. Tier 1 current authority 决定当前真态边界，负责告诉 W4 哪些 lane 仍 blocked、哪些写口仍 forbidden。
2. Tier 2 promoted addendum 补 current authority 不宜塞入的稳定增量，提供 H5/Bridge/Vault/OpenDesign 的已提升合同。
3. Tier 3 candidate north-star 负责把 `master spec`、W4 source bundle、本文收敛为同一张 future map；它能裁决、能重排，但不能越权写回 authority。
4. doc1/doc2/doc3 只作为 Tier 3 的历史方向输入：`doc1` 给阶段路线，`doc2` 给 shoulders 生命周期，`doc3` 给 PR55-PR74 的工作链路；它们不直接当执行合同。
5. 16U 属于 Tier 4 reference storage：本轮按需抽 `U2/U3/U11/U14/U15` 进入 Step0 和后续 spec PR，其余保留 future trigger，不做“全量重读即完成”的假动作。
6. 因此关系顺序是：`Tier 1 真态` → `Tier 2 promoted addendum` → `Tier 3 convergence / lane source bundle`，而 `doc1/doc2/doc3 + 16U + ~/.claude/* + code invariant mention` 只在后方做 reference backing。
