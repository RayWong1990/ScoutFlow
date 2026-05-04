---
title: OPUS V3 接纳评判与 PRD/SRD Amendment 建议
date: 2026-05-04
owner_tool: codex-desktop
status: review / amendment-recommendation
baseline_commit: c133e0e514a18e0211133a914a46e17a64051472
baseline_pr: "#54 T-P1A-029 Post-S0/S1 authority + candidate wording fix"
source_report: /Users/wanglei/workspace/data/exports/scoutflow-v3-obsidian-para-h5-pr-factory-20260504-211500.md
not_authority: true
not_prd_srd_promote: true
not_runtime_approval: true
not_migration_approval: true
not_frontend_implementation: true
---

# OPUS V3 接纳评判与 PRD/SRD Amendment 建议

## 0. 结论

OPUS V3 可以接纳，但只能接纳为 **下一轮 PRD/SRD amendment 输入包**，不能原样升权为路线图 authority。

推荐判定：

| 维度 | 判定 | 处理方式 |
|---|---|---|
| 强视觉 = H5 采集工作站，不是 Obsidian wiki 视觉 | 接纳 | 写入 PRD amendment；后续 H5 仍需单独 frontend gate |
| 复用 `/Users/wanglei/workspace/raw` PARA + Claudian 基座 | 接纳但收窄 | 写入 PRD/SRD：ScoutFlow 只写 `00-Inbox`，不重造 `/intake`、`/compile`、frontmatter |
| thin Bridge 写 RAW vault | 接纳但改形 | 不新增第二个 HTTP 进程；作为现有 FastAPI API 的 `vault_export` 能力落地 |
| PR Factory / 多 agent 协作升级 | 接纳为 surge candidate | 当前 enforced 仍是 product lane max=`3` + authority writer max=`1`；扩到 `5/8/3/3` 需先 amendment |
| `shoulders-index.md` | 接纳 | 作为轻量依赖/参考索引；不等于批准 dependency 或 runtime |
| 350 PR 路线图 | 降级 | 作为 capacity envelope，不作为承诺计划；后续按 phase outcome gate 推进 |
| Wave 3A PR54-65 | 必须重排 | #54 已被 T-P1A-029 占用，下一轮从 #55 或任务 ID 重新排 |
| 修改 RAW `domain-map.md` 新增“内容采集” | 暂不接纳 | 先用 `02-Raw/调研/` + `tags: 调研/ScoutFlow采集`；新增 domain 需 RAW 侧单独 gate |
| OpenDesign H5 prototype | 接纳但隔离 | repo 外 placeholder-only prototype；不带真实 URL、账号、token、平台请求 |

一句话：**V3 的方向是对的，执行节奏要降噪；先把 H5/PARA/PR Factory 写成候选 contract，再开代码。**

## 1. 基线事实

本报告以 `main` HEAD 为基线：

```text
c133e0e T-P1A-029 post S0 S1 authority candidate fix (#54)
```

已确认事实：

- PR #54 已 merged，merge commit=`c133e0e514a18e0211133a914a46e17a64051472`。
- `docs/current.md` 仍声明：Phase 1A / Wave 2 closed / S0/S1 audit-fix merged / Phase 2A migration dry-run gated。
- Active product count=`0/3`，Authority writer max=`1`。
- `PRD-v2-2026-05-04.md` 与 `SRD-v2-2026-05-04.md` 仍是 base authority。
- DB vNext 仍是 candidate-only；not SRD-v3 promoted authority；not migration approval；not runtime approval。
- `audio_transcript` runtime、BBDown live、yt-dlp、ffmpeg、ASR、browser automation 仍 blocked。
- `services/api/migrations/**` 仍 forbidden，Phase 2A migration dry-run plan 也需要 user 显式 gate。

RAW 侧已核对事实：

- `/Users/wanglei/workspace/raw` 是稳定 Obsidian vault，顶层结构为 `00-Inbox`、`01-Wiki`、`02-Raw`、`03-Output`、`04-Atlas`、`05-Projects`、`System`。
- `System/frontmatter-templates.md` 中 `02-Raw` 原始材料模板是 4 字段：`title`、`date`、`tags`、`status`。
- `System/domain-map.md` 当前 domain 是 9 值枚举，没有“内容采集”。
- `System/intake-rules.md` 已定义 `00-Inbox -> 02-Raw` 流程；Probe / 调研 / 研究默认落 `02-Raw/调研/`。

## 2. OPUS V3 评判

### 2.1 高价值判断

1. **把强视觉从 Obsidian 消费端移回采集 H5，是正确修正。**
   当前 ScoutFlow 已有 Trust Trace DTO、metadata job、receipt ledger 方向；强视觉应服务“采集时刻的判断、反馈、scope 确认”，而不是在 wiki 里重做展示。

2. **不重造 RAW vault，是正确工程边界。**
   RAW 已有 `frontmatter-templates`、`intake-rules`、`routing-*`、`audit-wiki.py`。ScoutFlow 若自定义 frontmatter、domain 或 wiki 渲染，会制造第二套知识系统。

3. **PR Factory 思路可用，但不能覆盖现有治理硬约束。**
   当前 repo 的可执行约束是 Single Writer / Multi Reviewer、GitHub as Audit Source、product lane max=`3`。V3 的 `5 product + 8 research + 3 prototype + 3 audit` 可以作为 surge mode 设计目标，但不能在没有 amendment 和 lint 支撑前直接执行。

4. **shoulders-index 是更合适的“参考仓吸收”承载方式。**
   ScoutFlow 不适合继续为每个外部参考写重 ARD。用一张表记录 upstream、mode、output contract、failure mode、kill switch、owner lane，更符合轻治理产品仓。

### 2.2 必须纠偏的问题

| 优先级 | 问题 | 证据 | 纠偏 |
|---|---|---|---|
| P0 | V3 把 Wave 3A 从 PR54 开始，但 PR #54 已被 T-P1A-029 占用 | GitHub / local HEAD 均为 `c133e0e (#54)` | 后续 PR 编号从 #55 重排；报告里的 PR54-65 只能作为旧编号参考 |
| P0 | Lane 上限与当前 `parallel-execution-protocol.md` 冲突 | 当前 enforced 是 product lane max=`3`，authority writer max=`1` | 先写 Process amendment；surge mode 未 promote 前不得用 5 product lanes |
| P0 | V3 的 `Bridge on localhost:27124` 会和现有 FastAPI authority/API 边界重叠 | 当前代码已有 `services/api/scoutflow_api/main.py`、`captures.py`、`jobs.py`、`trust-trace` | Bridge 改成现有 API 内的 `vault_export` capability，不新增第二个事实写入服务 |
| P0 | V3 低估 Phase 2A DB/F-012 gate | SRD-v3 DB candidate 明确 `PRAGMA foreign_keys=ON` 是 hard gate | 任何 DB vNext / evidence-chain / vault-export receipt 之前，先做 FK enforcement proof |
| P1 | V3 提议 RAW 新 domain“内容采集”过早 | RAW domain-map 当前 9 值枚举；RAW AGENTS 要保持顶层架构稳定 | 先不改 domain-map；使用 `02-Raw/调研/` 和 `tags: 调研/ScoutFlow采集` |
| P1 | V3 把 RAW `05-Projects/ScoutFlow/dispatches` 当项目管理中心，可能和 ScoutFlow repo authority 双写 | ScoutFlow authority 在 repo 的 `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` | RAW `05-Projects/ScoutFlow` 只能做 Obsidian mirror / handoff，不做 repo authority |
| P1 | H5 stack 版本号不应直接进 PRD/SRD authority | 前端依赖会漂移；当前 repo 无 frontend package | PRD/SRD 写 stack family 和 selection criteria；具体版本进 `FRONTEND-STACK-LOCK` |
| P2 | 350 PR 容易变成 vanity metric | 当前真实 gating 是 task / PR / validation，不是数量 | 保留 phase envelope；每 phase 以 outcome 和 gate 结束 |

## 3. PRD Amendment 新增意见

建议新增一份 candidate 文档，而不是直接改 `PRD-v2`：

```text
docs/PRD-amendments/strong-visual-h5-para-pr-factory-candidate-2026-05-05.md
```

如果暂不创建新目录，也可以先落在：

```text
docs/research/prd-amendment-candidate-strong-visual-h5-para-2026-05-05.md
```

### 3.1 新增章节 A：产品形态改写

建议写入：

```md
## X.Y Strong Visual Capture Station

ScoutFlow 的强视觉产品面是本机 H5 Capture Station，不是 Obsidian 内的 wiki 视觉层。

H5 的职责：
- 接收用户手动输入 URL。
- 展示 metadata fetch / receipt / Trust Trace 的实时状态。
- 把 Capture Scope Gate 显性化，阻止 recommendation / keyword / RAW gap 直接创建 capture。
- 在未来 gate 通过后展示 media / ASR / normalization 状态，但不得提前暗示 runtime 已批准。

H5 不是 authority。SQLite + FS + state words 仍是 L0 authority；所有写入必须走 API。
```

### 3.2 新增章节 B：RAW / PARA 集成边界

建议写入：

```md
## X.Y RAW PARA Integration Boundary

ScoutFlow 复用用户已有 Obsidian vault `/Users/wanglei/workspace/raw`。

产品承诺：
- ScoutFlow 可在 user 显式 gate 后，把已批准的 capture 摘要写入 RAW `00-Inbox/`。
- 写入文件必须遵守 RAW `System/frontmatter-templates.md` 的 `02-Raw` 原始材料 4 字段模板。
- ScoutFlow 不修改 `02-Raw/`、`01-Wiki/`、`System/`、`.obsidian/`。
- ScoutFlow 不调用或重造 `/intake`、`/compile`、`/enrich`、`/query`、`/lint`。
- RAW `05-Projects/ScoutFlow` 如存在，只作为 Obsidian 可读 mirror / handoff，不替代 ScoutFlow repo authority。

当前推荐落地：
- `tags: 调研/ScoutFlow采集`
- `status: pending`
- 默认让 RAW `/intake` 按现有规则进入 `02-Raw/调研/`
- 不新增 RAW domain，除非 RAW 项目另开 gate。
```

### 3.3 新增章节 C：PR Factory Surge Mode

建议写入：

```md
## X.Y PR Factory Surge Mode

ScoutFlow 默认并行模式仍为:
- product lane max = 3
- authority writer max = 1
- same file group writer max = 1
- review / research lanes 不计入 product lane，除非写 authority

未来可引入 surge mode:
- product lanes: up to 5
- research lanes: up to 8
- prototype lanes: up to 3
- audit lanes: up to 3

Surge mode 启用条件:
1. `docs/specs/parallel-execution-protocol.md` 已 amendment。
2. 每 wave 有文件域互斥矩阵。
3. 每个 product lane 使用独立 branch / PR。
4. authority writer 仍为 1。
5. GitHub PR diff / workflow run 是审计事实源。
```

### 3.4 新增章节 D：Shoulder Index

建议写入：

```md
## X.Y Shoulder Index

`docs/shoulders-index.md` 是外部参考、依赖候选、prototype source 和 kill-switch 的轻量登记表。

它不代表:
- dependency 已批准
- runtime 已批准
- adapter 已可信
- external repo 版本已冻结

每个 shoulder 至少记录:
- id
- upstream
- integration_mode
- output_contract
- failure_modes
- kill_switch
- owner_lane
- status
- next_action
```

### 3.5 PRD 不建议写入的内容

- 不写 “350 PR 一定完成”。
- 不写具体 React / Vite / Tailwind 版本号。
- 不写 “Bridge 约 1000 行” 这种不可验证承诺。
- 不写 “新增 RAW domain=内容采集”。
- 不写 OpenDesign 为运行时依赖。
- 不写 H5 可绕过 API 写 authority。

## 4. SRD Amendment 新增意见

建议新增一份 candidate 文档：

```text
docs/SRD-amendments/h5-raw-vault-bridge-srd-v3-candidate-2026-05-05.md
```

### 4.1 新增章节 A：API-first Bridge

V3 报告里的 `ScoutFlow Bridge` 概念应改为现有 API 的能力，不应变成第二个 authority service。

建议写入：

```md
## 18. ScoutFlow Capture Station + RAW Vault Export

### 18.1 API ownership

ScoutFlow does not introduce a second authority process for RAW export.
The existing FastAPI API remains the only authority write boundary.

Current routes retained:
- `POST /captures/discover`
- `POST /captures/{capture_id}/metadata-fetch/jobs`
- `POST /jobs/{job_id}/complete`
- `GET /captures/{capture_id}/trust-trace`

Future candidate routes:
- `GET /captures/{capture_id}/vault-export/preview`
- `POST /captures/{capture_id}/vault-export/commit`

The future `commit` route is gated and unavailable until a separate dispatch approves RAW vault export.
```

### 4.2 新增章节 B：RAW Vault Export Contract

建议写入：

```md
### 18.2 RAW vault write contract

Configuration:
- `SCOUTFLOW_RAW_VAULT_ROOT=/Users/wanglei/workspace/raw`
- default disabled in tests and local dev unless explicitly configured

Allowed path:
- `${RAW_VAULT_ROOT}/00-Inbox/scoutflow-{capture_id}-{slug}.md`

Forbidden paths:
- `${RAW_VAULT_ROOT}/01-Wiki/**`
- `${RAW_VAULT_ROOT}/02-Raw/**`
- `${RAW_VAULT_ROOT}/03-Output/**`
- `${RAW_VAULT_ROOT}/04-Atlas/**`
- `${RAW_VAULT_ROOT}/05-Projects/**`
- `${RAW_VAULT_ROOT}/System/**`
- `${RAW_VAULT_ROOT}/.obsidian/**`
- `${RAW_VAULT_ROOT}/.claude/**`
- `${RAW_VAULT_ROOT}/.agents/**`

Frontmatter:
---
title: "<human-readable title>"
date: YYYY-MM-DD
tags: 调研/ScoutFlow采集
status: pending
---

Body must include:
- platform
- capture_id
- platform_item_id
- canonical_url
- metadata_fetched_at
- capture_scope
- Trust Trace summary
- source artifact references

Idempotency:
- same capture_id + same content digest returns existing path
- same path + different digest is conflict, not overwrite
- commit emits a receipt / event only after the file is written and hashed
```

### 4.3 新增章节 C：Directory Skeleton

建议采用分阶段骨架，而不是一次性建大目录。

```text
# 已有 / 保持
docs/
services/api/scoutflow_api/
services/api/migrations/
tests/
tools/

# Wave 3A docs-only candidate
docs/shoulders-index.md                         # 需单独 PR
docs/research/*-shoulder-scan-*.md
docs/research/*-h5-stack-lock-*.md
docs/SRD-amendments/h5-raw-vault-bridge-*.md    # candidate only

# Future frontend gate 通过后才允许
console/capture-station/
  package.json
  vite.config.ts
  src/
    app/
    components/
    features/capture/
    features/trust-trace/
    features/vault-export/
    lib/api-client.ts
    lib/state-machine.ts
  tests/

# Future API gate 通过后才允许
services/api/scoutflow_api/vault_export.py
services/api/scoutflow_api/settings.py
tests/api/test_vault_export_*.py
tests/contracts/test_raw_vault_export_contract.py
```

说明：

- 当前 AGENTS 禁止创建 `apps/`、`workers/`、`packages/`；因此不要用 `apps/h5`。
- `console/capture-station/` 也必须等 frontend gate 明确批准后再创建。
- `services/api/migrations/**` 仍需 Phase 2A migration gate。

### 4.4 新增章节 D：Visual QA Contract

建议写入：

```md
### 18.4 H5 Visual QA

Every H5 PR must provide:
- desktop screenshot
- mobile/narrow screenshot
- no-overlap check for URL bar, metadata cards, state machine, trust trace
- contrast/readability check
- empty / loading / failed / metadata_fetched states
- Playwright screenshot evidence when the H5 runtime exists

Technical render pass does not equal visual pass.
```

官方 stack 验证参考（截至本报告写作时已查官方文档）：

- Vite supports `react-ts` scaffolding and currently documents Node.js `20.19+` / `22.12+` compatibility requirements: <https://vite.dev/guide/>
- React Flow is installed as `@xyflow/react` and documents Tailwind CSS 4 stylesheet ordering: <https://reactflow.dev/learn/getting-started/installation-and-requirements>
- shadcn/ui has an official Vite + Tailwind v4 path: <https://v3.shadcn.com/docs/installation/vite>
- TanStack Query is appropriate for server-state fetching/caching/sync: <https://tanstack.com/query/latest/docs/framework/react/overview>
- TanStack Form has React documentation but should be locked by a stack PR, not PRD authority: <https://tanstack.com/form/latest/docs/framework/react>
- Tailwind CSS v4 has a first-party Vite plugin: <https://tailwindcss.com/blog/tailwindcss-v4>

## 5. 后续路线图

### 5.1 状态机

```text
S0_baseline_pr54_confirmed
  -> S1_v3_review_packet_written
  -> S2_prd_srd_amendment_candidates_written
  -> S3_amendment_promoted_or_rejected
  -> S4_phase2a_db_dry_run_plan_clear
  -> S5_api_projection_and_h5_skeleton
  -> S6_raw_vault_export_candidate
  -> S7_capture_runtime_expansion
  -> S8_asr_normalization_handoff
```

Gate：

| Transition | Gate |
|---|---|
| S0 -> S1 | Review report only；no authority edit |
| S1 -> S2 | User authorizes PRD/SRD amendment candidate task |
| S2 -> S3 | External audit + docs-check + contracts-index registration |
| S3 -> S4 | User explicitly chooses Phase 2A migration dry-run plan |
| S4 -> S5 | F-012 `PRAGMA foreign_keys=ON` proof + migration dry-run validation |
| S5 -> S6 | H5 projection-only passes visual QA; no runtime expansion |
| S6 -> S7 | RAW export idempotency/path-containment/receipt proof |
| S7 -> S8 | BBDown live / media / ASR gates separately approved |

### 5.2 建议 PR 波次

由于 PR #54 已占用，OPUS V3 的 Wave 3A 编号需重排：

| 建议 PR 段 | 目标 | 类型 | 备注 |
|---|---|---|---|
| #55 | OPUS V3 acceptance review packet | docs/research | 本报告可作为内容基础 |
| #56 | PRD amendment candidate: H5 + PARA + PR Factory | docs candidate | 不 promote |
| #57 | SRD amendment candidate: API-first vault export + H5 skeleton | docs candidate | 不开 frontend |
| #58 | `docs/shoulders-index.md` v0 | docs/spec-lite | status 以 scanning/reference 为主 |
| #59 | RAW vault contract probe | research | 只读 RAW specs，不写 RAW |
| #60 | Process amendment candidate for surge lanes | docs/spec candidate | 决定是否从 3 product lanes 提升 |
| #61-#66 | Phase 2A DB dry-run plan / F-012 proof | docs + code only after gate | 先启 FK proof，再谈 migration |
| #67-#78 | Bounded metadata runtime expansion | product | BBDown live 仍需 user gate |
| #79-#95 | H5 projection-only foundation | frontend | 先读 API，不写 vault |
| #96-#110 | RAW vault export preview/commit | API + tests | 只写 `00-Inbox`，不调用 `/intake` |
| #111+ | media / ASR / normalization / RAG | future | 各自单独 gate |

### 5.3 立即可执行的第一组任务

推荐顺序：

1. 写 `docs/shoulders-index.md` v0，但所有外部 repo 默认为 `scanning` 或 `reference_only`，不要写 `locked`。
2. 写 PRD amendment candidate，固定 “H5 是强视觉面；RAW 是下游 vault；不重造 Obsidian”。
3. 写 SRD amendment candidate，固定 “Bridge 是现有 FastAPI 的 vault_export 能力，不是第二个 authority service”。
4. 写 surge lane process candidate，决定是否允许超过当前 3 product lanes。
5. 再决定 Phase 2A DB dry-run plan 或 H5 projection skeleton。

## 6. 多 agent 协作落地

### 6.1 当前 enforced 模式

当前继续执行：

```text
Authority writer max = 1
Product lane max = 3
Same file group writer max = 1
Research / audit lane 不计入 product lane，除非写 authority
GitHub PR diff / workflow run = audit source
```

### 6.2 Surge candidate 模式

只有在 process amendment promote 后，才允许：

| Lane type | Candidate max | Write scope |
|---|---:|---|
| Authority writer | 1 | `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / entry authority |
| Product code lane | 5 | disjoint code modules and tests |
| Research lane | 8 | `docs/research/**` only |
| Prototype lane | 3 | repo-external prototype path or explicitly approved frontend path |
| Audit lane | 3 | read-only PR / diff / workflow review |

### 6.3 文件域互斥规则

每个 wave 开始前必须写：

```text
Lane ID:
Owner tool:
Allowed paths:
Forbidden paths:
Same-file group:
Authority touched? yes/no
Validation:
Kill condition:
```

示例：

| Lane | Owner | Allowed paths | Forbidden |
|---|---|---|---|
| W3A-PRD | Codex writer | `docs/PRD-amendments/**` or `docs/research/**` | `services/**`, `data/**`, `referencerepo/**` |
| W3A-SRD | Codex writer | `docs/SRD-amendments/**` | `services/api/migrations/**` |
| W3A-Shoulders | worker | `docs/shoulders-index.md` | authority docs |
| W3A-RAW-Probe | reviewer | read-only `/Users/wanglei/workspace/raw/System/**`; report to `docs/research/**` | RAW writes |
| W3A-Audit | GPT/Codex reviewer | PR diff only | repo writes |

## 7. 技术架构落地

### 7.1 推荐目标架构

```text
H5 Capture Station
  -> Existing FastAPI API
     -> Capture / Job / Receipt / Trust Trace
     -> Future vault_export preview / commit
        -> SQLite + artifact FS
        -> RAW 00-Inbox markdown write
RAW / Obsidian
  -> /intake
  -> /compile
  -> /enrich / /query / /lint
```

关键点：

- H5 只读/调用 API，不直写 SQLite、artifact FS、RAW。
- API 是唯一 write boundary。
- Vault export 先 preview，后 commit。
- `commit` 必须 path containment、frontmatter validation、idempotency、sha256 ledger。
- RAW 后续整理由 RAW 的既有命令链完成。

### 7.2 技术债优先级

| 优先级 | 债务 | 落地动作 |
|---|---|---|
| P0 | SQLite FK enforcement 未启用 | Phase 2A 前先做 `PRAGMA foreign_keys=ON` + test |
| P0 | DB vNext 仍 candidate-only | 单独 promote gate，不和 H5 混跑 |
| P0 | `WorkerReceipt.next_status=metadata_fetched` failure semantics 债务 | Phase 2A migration prep 内一并处理 |
| P1 | Trust Trace UI 需要 stable DTO | H5 先用现有 DTO snapshot，不要求新字段 |
| P1 | RAW vault export 缺 contract | 新增 preview/commit contract，先不写 RAW |
| P1 | H5 stack 未锁 | 独立 stack lock PR，验证 Node / package manager / TS strict / visual QA |
| P2 | External shoulders 未验证 | shoulder scan 只输出 status，不批准依赖 |

### 7.3 不建议落地的架构

- 不新增 `localhost:27124` 第二套 Bridge authority，除非先证明现有 API 不能承载。
- 不让 H5 直接写 RAW vault。
- 不在 ScoutFlow 内执行 RAW `/intake` 或 `/compile`。
- 不在 PRD/SRD 中固定不可验证的代码行数。
- 不把 OpenDesign 输出当实现源码。
- 不把 `05-Projects/ScoutFlow` 当 repo authority。

## 8. Acceptance Criteria

### 8.1 本报告之后的 T-PASS 条件

如果继续推进，下一步的最小 T-PASS：

- OPUS V3 被登记为 candidate source，不是 authority。
- PRD amendment candidate 能清楚区分 product shape、non-goals、runtime gates。
- SRD amendment candidate 能清楚区分 existing API、future vault_export、H5 projection、RAW write boundary。
- docs-check / secret-check / pytest / diff-check 通过。
- `docs/current.md` / `docs/task-index.md` 只在明确 authority task 中修改。

### 8.2 不应宣布完成的内容

即使 PRD/SRD amendment 写完，也不能宣布：

- SRD-v3 promoted
- migration approved
- frontend approved
- RAW vault export approved
- BBDown live approved
- ASR approved
- `audio_transcript` unlocked
- 5 product lanes 已启用

## 9. 推荐决策

我建议采用：

```text
ACCEPT_WITH_REWRITE
```

具体含义：

1. 接受 OPUS V3 的三大方向：H5 强视觉、RAW/PARA 复用、PR Factory。
2. 拒绝原样照搬 PR 编号、lane 上限、Bridge 端口、RAW domain 变更。
3. 先开两个 candidate amendment：PRD 一个、SRD 一个。
4. 先把 PR Factory surge mode 写成可审计协议，再考虑突破当前 3 product lanes。
5. 在任何 runtime / frontend / migration 之前，先清掉 Phase 2A DB/FK hard gate。
