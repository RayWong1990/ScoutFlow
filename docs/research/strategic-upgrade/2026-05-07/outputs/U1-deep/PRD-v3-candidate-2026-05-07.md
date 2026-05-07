---
title: PRD v3 Compiled Candidate Shell
status: candidate / north-star / not-authority
authority: not-authority
promoted: false
created_at: 2026-05-07
created_by: cc1 compiled (来源 PRD-v2 + PRD-v2.1 amend + U1-deep 4 supplement, 非正式 base)
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
frontend_implementation_approval: not-approved
sources:
  - docs/PRD-v2-2026-05-04.md (canonical base)
  - docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md (promoted addendum)
  - docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/PRD-v3-supplement-worked-examples-2026-05-07.md
  - docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/NFR-SINGLE-USER-CAPACITY-2026-05-07.md
  - docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/SIBLING-PROJECT-EGRESS-CONTRACT-2026-05-07.md
  - docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/TRACEABILITY-MATRIX-EXTENDED-2026-05-07.md
sunset_trigger: |
  Deprecated when (a) cloud-output base file PRD-v3-candidate-2026-05-07.md is recovered and replaces this shell, or
  (b) commander synthesizes a real promoted PRD-v3 base PR that absorbs the 4 U1-deep supplements directly.
disclaimer: |
  这是 thin compiled candidate, 不是正式 PRD-v3 base.
  cloud-output PRD-v3-candidate-2026-05-07.md base file 暂未在本机找回 (find -maxdepth 8 + Downloads/ 全部 negative).
  本 shell 让 U1-deep 的 4 个 supplement 引用不再孤儿, 不构成正式 PRD-v3 promote.
  当 cloud-output base 找回, 或战友综合 PRD-v2/v2.1 + 真态写新 base 时, 本 shell 自动 sunset.
---

# PRD-v3 Compiled Candidate Shell

## §0 status banner (必读 / read-first)

> 本 shell **不是正式 PRD-v3 base**.
>
> - 它是 cc1 compiled candidate, 来源 = PRD-v2 + PRD-v2.1 amendment + U1-deep 4 supplement.
> - 它存在的唯一目的: 让 U1-deep 的 4 个 supplement (worked examples / NFR / sibling-egress / traceability-extended) 引用本文件时不再孤儿.
> - 它**不构成** runtime / migration / frontend implementation / authority writer 升级.
> - 当前 promoted PRD canonical 仍是 `docs/PRD-v2-2026-05-04.md` + `docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md`.
> - 任何 dispatch / runtime / migration 必须以 PRD-v2 + PRD-v2.1 为事实源, 不得引本 shell 作为 enforcement 依据.

cloud-output zip 解压后的 base 文件 `PRD-v3-candidate-2026-05-07.md` 在 2026-05-07 17:41 GMT+8 找回时间点之前**未在本机找回**:

- `find /Users/wanglei -maxdepth 6 -name "PRD-v3-candidate-2026-05-07.md"` → 空
- `find /Users/wanglei -maxdepth 8 -name "PRD-v3*.md"` → 仅 `PRD-v3-supplement-worked-examples-2026-05-07.md` (是 supplement, 不是 base)
- `ls /Users/wanglei/Downloads/` → 仅 `prd-v3-srd-v4-wave5-outline-candidate-*.md`, 与本 base 不是同一文件

## §1 来源对照表

| Source | 路径 | 角色 | 本 shell 吸收哪部分 |
|---|---|---|---|
| PRD-v2 canonical base | `docs/PRD-v2-2026-05-04.md` | promoted authority base | §2 整段产品定义 + 4-layer architecture + LP-001/006/007/SEC-001 + 当前 quick capture 红线 |
| PRD-v2.1 promoted addendum | `docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md` | promoted addendum (T-P1A-103 / PR #58) | §3 strong visual capture H5 + PARA vault 边界 + fixed product shoulders + PR factory operating mode |
| U1-deep supplement A | `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/PRD-v3-supplement-worked-examples-2026-05-07.md` | candidate / not-authority | §5 worked examples 密度补 + 8 个 PRD-v3 章节双 worked example |
| U1-deep supplement B | `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/NFR-SINGLE-USER-CAPACITY-2026-05-07.md` | candidate / not-authority | §5 单用户容量 envelope (signals/captures/topic-cards/SQLite/latency/disk/concurrency) |
| U1-deep supplement C | `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/SIBLING-PROJECT-EGRESS-CONTRACT-2026-05-07.md` | candidate / not-authority | §5 file-first egress to DiloFlow / RAW / Obsidian / hermes-agent (non-SDK) |
| U1-deep supplement D | `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/TRACEABILITY-MATRIX-EXTENDED-2026-05-07.md` | candidate / not-authority | §5 80+ row traceability matrix (PRD-v2 line-anchor / PR #199/231/239/240 / overflow registry / supplement self-cite) |

## §2 跟 PRD-v2 + v2.1 关系

本 shell **不 supersede** PRD-v2, 也**不 supersede** PRD-v2.1. 三者关系:

```
PRD-v2 (promoted base, canonical authority)
  └─ PRD-v2.1 (promoted addendum, T-P1A-103 / PR #58)
       └─ PRD-v3 compiled candidate shell (本文件, candidate, not-authority)
              └─ U1-deep 4 supplement (candidate, not-authority)
```

- **PRD-v2 锁定**: 单 user / local-first / 4-layer architecture / LP-001 capture scope gate / LP-006 single writer / LP-SEC-001 credential never evidence / `audio_transcript` runtime blocked / `T-P1A-011C` metadata probe path 已可信 / 当前 quick capture 仅 `manual_url + metadata_only`.
- **PRD-v2.1 promoted**: strong visual H5 capture-side (4 panel: URL bar / live metadata / capture scope / trust trace graph) + PARA vault 下游边界 (`SCOUTFLOW_VAULT_ROOT`, 仅写 `00-Inbox/`, 不写 `02-Raw/01-Wiki/03-Output/System/`) + fixed product shoulders (BBDown / Whisper / Obsidian PARA / OpenDesign / Vite+React+shadcn+TanStack+ReactFlow) + PR factory operating mode.
- **PRD-v3 candidate (本 shell + 4 supplement)**: worked examples 密度补 / NFR 单用户容量 / sibling project egress contract / 80+ row traceability matrix. 全部 candidate, 全部 not-authority, 全部 future-gated.

## §3 跟 U1-deep 4 supplement 关系

| supplement | 引用本 shell 哪节 | 本 shell 哪节吸收 supplement |
|---|---|---|
| `PRD-v3-supplement-worked-examples-2026-05-07.md` | §0 candidate banner / §2 PRD-v2 关系 / §3 PRD-v2.1 H5 + PARA + shoulder | §5.1 worked examples 密度补 |
| `NFR-SINGLE-USER-CAPACITY-2026-05-07.md` | §2 单 user / local-first 假设 / §3 H5 + PARA vault | §5.2 单用户容量 envelope |
| `SIBLING-PROJECT-EGRESS-CONTRACT-2026-05-07.md` | §2 ScoutFlow → 下游 RAW / Obsidian / DiloFlow 边界 | §5.3 file-first egress contract |
| `TRACEABILITY-MATRIX-EXTENDED-2026-05-07.md` | §1 来源对照 / §2 PRD-v2 line anchor / §3 PRD-v2.1 line anchor / §4 已 promoted / §5 candidate 各项 | §5.4 80+ row traceability matrix |

## §4 已 PROMOTED 的部分 (来自 PRD-v2 / v2.1, 锁定不变)

下列条目**不构成本 shell 的新承诺**, 仅复述 PRD-v2 + v2.1 已 promoted 的硬约束, 让 U1-deep supplement 的 candidate 内容有清晰 contrast 锚点:

### §4.1 产品身份 (PRD-v2 §0.1 + §1.1)

- 项目名 `ScoutFlow`, 项目根 `/Users/wanglei/workspace/ScoutFlow/`
- 类型: 单 user / local-first 内容采集 + 证据整理系统
- 上下游: 输出 evidence + 文案资产; RAW / Obsidian / DiloFlow 是 downstream consumer, 非本项目一部分
- 平台窗口: Bilibili + XHS first, YouTube later

### §4.2 4-layer authority architecture (PRD-v2 §3.1)

```text
L0 Authority  = SQLite + FS artifact layout + state words
L1 Workers    = stateless execution units
L2 Thin API   = contract enforcement / validation / state transitions / receipt ingestion
L3 Console    = projection layer
```

- Console 不直接写 authority, 所有写走 API
- Worker 不持有独家状态, 不直接写 SQLite
- 任何一层下线不应把事实留在进程内存

### §4.3 协作纪律 (PRD-v2 §3.3)

- `LP-001` Capture Scope Gate: 推荐 / 关键词 / RAW gap 不得直接采集
- `LP-006` Single Writer / Multi Reviewer: authority conflict domain 单写者
- `LP-007` GitHub Audit Source: 高风险 / material task 以 PR diff / workflow run 为事实源
- `LP-SEC-001` Credential Material Is Never Evidence

### §4.4 quick capture 红线 (PRD-v2 §4.2)

- 来源必须 user 手动粘贴单条 URL
- 当前实际开放 preset 仅 `metadata_only`
- `audio_transcript` 仍 blocked, 不因任何文档 promote 自动解锁
- 不得借 quick capture 顺手扩到作者扩展 / 关键词扩展 / 列表扩展 / 评论 / OCR / 图片原图

### §4.5 5 overflow lane Hold (Overflow Registry v0)

- `true_vault_write` Hold
- `runtime_tools` Hold
- `browser_automation` Hold
- `dbvnext_migration` Hold
- `full_signal_workbench` Hold

### §4.6 PRD-v2.1 Strong Visual Capture H5 (PRD-v2.1 §X.1)

- 4 panel: URL Bar / Live Metadata / Capture Scope / Trust Trace Graph
- 角色: projection surface + operation surface
- 不是: authority / approval / browser automation / runtime
- 状态机: `manual_url_entered → metadata_probe_requested → metadata_visible → scope_confirmed_or_blocked → future_commit_gate`
- 视觉验收: 5 gate (visual hierarchy / spacing / occlusion safety / readability / visual weight) per `~/.claude/rules/aesthetic-first-principles.md`

### §4.7 PRD-v2.1 PARA / Claudian Vault 下游边界 (PRD-v2.1 §X.2)

- 默认 root: `${SCOUTFLOW_VAULT_ROOT:-~/workspace/raw}` (产品 guidance only, 实现层 fail-loud 在 SRD)
- ScoutFlow 仅写 `00-Inbox/` candidate
- 不写 `02-Raw/`, `01-Wiki/`, `03-Output/`, `System/`
- 不替换 `/intake`, `/compile`, `/enrich`, `/query`, `/lint`
- 不重定义 Obsidian 为 capture UI
- 项目协调入口 `${SCOUTFLOW_VAULT_ROOT}/05-Projects/ScoutFlow/` 是 mirror / handoff, 不是 repo authority

### §4.8 PRD-v2.1 Fixed Product Shoulders (PRD-v2.1 §X.3)

| Surface | 角色 | 当前 status |
|---|---|---|
| BBDown | Bilibili capture shoulder | 锁定方向, runtime 仍 gated |
| Whisper family | local ASR | 锁定 family, 实现 benchmark 仍开 |
| Obsidian PARA vault | downstream knowledge | 锁定 destination |
| OpenDesign | visual reference | repo-external 视觉 probe candidate only |
| Vite + React + shadcn + TanStack + React Flow | H5 stack family | candidate family only, version lock 延后 |

## §5 CANDIDATE 的部分 (来自 U1-deep, 待 promote)

下列条目是 U1-deep 4 supplement 提供的 candidate carry-forward 内容, 全部 not-authority, 全部 future-gated, 全部不构成 runtime / migration / frontend implementation 解锁.

### §5.1 worked examples 密度补 (来自 supplement A)

- 每个 PRD-v3 章节配 2 个 worked example (manual URL intake / metadata receipt / PF-V handoff / 4-run collaboration / RAW DiloFlow handoff / promote gate)
- 全部标 `[candidate carry-forward]` 或 `[promoted_addendum-aware inference]` 或 `[canonical fact]` claim label
- worked example **不解锁 runtime**, 仅作 PRD explanatory supplement

### §5.2 单用户容量 envelope (来自 supplement B)

| 维度 | candidate target |
|---|---|
| Signal intake/day | 5-50 |
| Manual captures/day | 1-20 (metadata-only) |
| Topic cards/day | 1-10 |
| SQLite scale | 50k-250k rows 触发 schema/index review |
| Local API latency | p99 < 100ms (indexed read) / < 500ms (capture creation) |
| Preview rendering | < 1s |
| Traceability matrix audit | 80-150 rows / 30-45 min human-auditable |
| Daily LLM spend | placeholder USD 1-5/day (pricing 未刷新) |
| Local disk | 1-5GB/month (metadata-only, media excluded) |
| Concurrency | 1 authority writer + ≤3 active product lanes |

反企业声明: 无 multi-region / 99.9% SLA / RBAC / autoscaling / Temporal-LangGraph orchestration / 默认 vector DB.

### §5.3 file-first egress contract (来自 supplement C)

| Sibling | manifest | directory candidate | rule |
|---|---|---|---|
| DiloFlow | `diloflow_handoff_v0.candidate.json` | `handoff/diloflow/YYYY-MM-DD/<capture_id>/` | DiloFlow 可改 narrative, source claim provenance 仍引 ScoutFlow/RAW |
| RAW vault | `raw_handoff_v0.candidate.json` (frontmatter_mode=raw_4_field) | RAW `00-Inbox/ScoutFlow/<date>/` (manual copy only) | RAW compile 不反向 write repo authority |
| Obsidian | markdown frontmatter (source_system / status / capture_id / artifact_sha256 / review_state) | user vault path (repo-external) | Obsidian properties 是 review metadata, 不是 ScoutFlow state words |
| hermes-agent | `hermes_job_candidate_v0.json` | repo-external temp workdir | hermes 可 propose normalization, API/receipt validator 仍 own durable admission |

### §5.4 80+ row traceability matrix (来自 supplement D)

- 行号 ≥ 80, 涵盖 PRD-v2 line anchor (#L13-L18 / #L20-L28 / #L49-L54 / #L65-L74 / #L119-L128) + SRD-v2 line anchor + bridge config + overflow registry + PR #199/231/239/240 + Run-2/Run-3+4 checkpoint + RAW bridge candidate + supplement self-cite
- claim label 覆盖: `[canonical fact]` / `[promoted_addendum-aware inference]` / `[candidate carry-forward]` / `[tentative candidate]`
- 行 ≥ 51 后多为 supplement-self-cite, 不直接进 promoted authority

## §6 何时升 PRD-v3 promoted base

触发条件 (任一满足即可 sunset 本 shell):

1. **cloud-output base 找回**: `cloud-output-U1-prd-v3-srd-v3-2026-05-07.zip` 解压版 `PRD-v3-candidate-2026-05-07.md` 落到本机 → `mv` replace 本 shell, 验证 sha256, 更新 supplement 引用 line anchor
2. **commander 综合写新 PRD-v3 promoted base PR**: 综合本 shell + PRD-v2 + v2.1 + 4 supplement + 真态 (PR #199-240 / Run-1-4 ledger / overflow registry / Hermes 外审 / 用户 verdict) → 写 PRD-v3 promoted base, 走 single-writer + audit gate + user explicit promote verdict, 走完后本 shell 自动 sunset
3. **U1-deep 4 supplement 被吸收到正式 PRD-v3 promoted base**: supplement 内容已 inline 进 base, 4 个 supplement 文件可标 sunset 同步, 本 shell 同步 sunset

每条触发都要求**显式 user verdict + redline scan + claim label scan + write_enabled=False bridge config 验证 + 5 overflow lane 仍 Hold**.

## §7 不构成 (boundary recap)

本 shell 明确**不构成**:

- runtime approval (BBDown / yt-dlp / ffmpeg / Whisper / browser automation 全 blocked)
- migration approval (DB vNext 仍 Hold)
- frontend execution gate (Vite+React+shadcn 仍 candidate stack family, 版本锁延后)
- authority writer (PRD canonical 仍 PRD-v2 + v2.1, SRD canonical 仍 SRD-v2)
- live web vendor freshness (browsing disabled, 所有 vendor pricing/version 待刷新)
- SDK coupling (DiloFlow / RAW / Obsidian / hermes-agent 全 file-first manifest, 非 SDK)

## §8 维护 / sunset

- **位置**: `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/PRD-v3-candidate-2026-05-07.md`
- **owner**: cc1 compiled, 由 ledger owner 维护
- **修改**: 仅在 4 个 supplement 改动需要同步 cross-link 时修改; 不得作为 PRD substantive 修订入口
- **sunset**: 见 §6 三条触发任一满足
- **不替代**: 不替代 PRD-v2 / PRD-v2.1 / SRD-v2; 不替代 cloud-output 真 base 找回流程
