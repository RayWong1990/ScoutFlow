# SRD v1.1 Amendment — 2026-05-02

> 说明：本文件已被 `docs/SRD-v1.1-amendment-2026-05-03.md` 作为当前审计修复基线补充覆盖。
> 当前执行与审计请优先阅读 `2026-05-03` 版本；本文件仅保留为历史参考。
> 以下旧强口径如“与 SRD 一同生效”“必须 Phase 0 开工前合入”“最新工程契约”等仅作为历史文本保留，不再作为当前执行依据。

> **非全文重写，仅补丁。** 与 `SRD-v1-2026-05-02.md` 一同生效。
> 冲突时 amendment > SRD-v1（amendment 是最新工程契约）。
> 8 条修订（SRD-A001 至 SRD-A008），全部为 user 在 SRD 通审后提出，必须 Phase 0 开工前合入。

---

## 0. Amendment 元信息

| 字段 | 值 |
|---|---|
| amendment ID | SRD-A001-008（合并为单 amendment） |
| 版本 | SRD v1.1 |
| 提案日期 | 2026-05-02 |
| 提案人 | user |
| 触发原因 | SRD v1 通审后发现 8 处必修：仲裁链越权 / Claude Design 不可用 / capture_mode 与 audio_transcript 冲突 / source_kind 命名漂 / artifact_assets 残留 / NFR 全部当 Phase 0 阻断不合理 / LLM 模型名写死 / 缺 task-index |
| 影响章节（SRD-v1） | §0.4 / §2.3 / §3.10 / §3.6 / §6 / §7 / §10 / §11 / DR-INT-02 |
| 不动章节（SRD-v1） | §3.1-§3.5（业务实体 FR 主体）/ §4 DR-FS / §5 IF（除明确指出）/ §10 追溯矩阵主体 |
| 本 amendment 行数 | ~1100 |
| 状态 | DRAFT，待 user 拍板锁定（拍后立即合入开工） |
| 落地优先级 | **Phase 0 开工前必合**（8 条全部，否则 Phase 1A 直接踩漂） |

---

## 1. 修订总览

| ID | 修订主题 | 严重度 | Phase 影响 |
|---|---|---|---|
| **SRD-A001** | Authority Chain 修订（SRD 不能压过 PRD/amendment） | **CRITICAL** | 0 |
| SRD-A002 | Claude Design 移除 + UI 工作流改 Claude Code in VSCode | HIGH | 0 / 2 |
| SRD-A003 | capture_mode 命名清晰化（DB enum 不变 + 新增 quick_capture_preset） | HIGH | 1A |
| SRD-A004 | source_kind 命名统一（取消 `capture_plan_triggered`） | HIGH | 1A |
| SRD-A005 | artifact_assets 残留 `media_assets` 清理 | MEDIUM | 0 / 1A |
| SRD-A006 | NFR 三档分层（Hard Gate / Quality Target / Observation Baseline） | HIGH | 1A |
| SRD-A007 | LLM 模型名抽象化（角色别名 + .env 映射） | MEDIUM | 1A |
| SRD-A008 | 新增 `docs/task-index.md` 共享任务账本 | HIGH | 0 |

---

## 2. SRD-A001 — Authority Chain 修订（CRITICAL，最先合入）

### 2.1 SRD-v1 §0.4 错误条款（必废止）

SRD-v1 §0.4 写：

> 仲裁链：`用户最新口头 > SRD > PRD + amendment > Operating Model > 历史对话`
>
> SRD 与 PRD/amendment 冲突时**以 SRD 为准**（SRD 是工程契约最终态）。

**这一条越权，必须废止。**

理由：
- PRD / amendment 是产品哲学契约，SRD 是工程规约
- 工程规约不应该单方面覆盖产品哲学
- 否则 Codex 写代码时发现 SRD 与 PRD 冲突，会自动按 SRD 覆盖，等于让工程层凌驾产品层

### 2.2 新仲裁链（lock，替代 SRD §0.4）

```text
user 最新口头
  > docs/specs/locked-principles.md      （5 LP，工具化 enforce）
  > docs/decision-log.md                 （D-lock 历史档案）
  > PRD + amendment                      （产品哲学契约）
  > SRD                                  （工程规约）
  > Operating Model                       （项目组织）
  > 历史对话 / agent 记忆
```

### 2.3 SRD 与 PRD/amendment 冲突时的处理

旧（错误）：SRD 自动覆盖 PRD/amendment。
**新（lock）**：

- 任何 agent / SRD 编辑发现 SRD 与 PRD/amendment 冲突 → **必须停下**
- 生成一条 SRD amendment（如本文）或 GitHub issue
- 提交给 user 拍板
- user 决定：
  - A. 改 SRD 跟 PRD（默认）
  - B. 改 PRD 跟 SRD（必须走 PRD amendment 流程）
  - C. 双方都改（双 amendment）
- 不允许 SRD 单方"以工程合理性为由"覆盖 PRD

### 2.4 SRD-v1 §0.4 / §11.F 必修文本

| 位置 | 旧 | 新 |
|---|---|---|
| §0.4 | "SRD 与 PRD/amendment 冲突时**以 SRD 为准**" | "SRD 与 PRD/amendment 冲突 → **生成 amendment + user 拍板**，不自动覆盖" |
| §11.F | "任何 PRD/amendment/OM 与 SRD 冲突 → 以本 SRD 为准" | "任何 PRD/amendment/OM 与 SRD 冲突 → 生成 amendment + user 拍板，不自动覆盖" |
| §0.2 编号约定 | — | 新增 `SRD-A` 前缀（SRD amendment ID）|

### 2.5 影响

- 影响 SRD §0.4 / §11.F 文本
- 影响 Codex / Opus 处理 SRD 的默认行为：见冲突先停 + 提 amendment，不自动改
- 不影响 FR / NFR / TC 内容（仅改仲裁规则）

---

## 3. SRD-A002 — Claude Design 移除

### 3.1 修订原因

user 反馈 Claude Design 不可用。SRD §2.3 用户角色表 + §3.10 FR-UI-003 风险段还在引用 Claude Design 高保真 mock，必须改。

### 3.2 SRD §2.3 user 角色表修订

旧：

| 角色 | 类型 | 主要职责 | 可触发 SRD 操作集 |
|---|---|---|---|
| Claude Design | LLM agent | UI 原型 / 视觉方向 | FR-UI-mock-* |

**删除该行**。

### 3.3 新 UI 工作流（替代 Claude Design 路径）

| 工作 | 由谁 | 说明 |
|---|---|---|
| UI direction / IA critique | Claude Code（VSCode）/ Opus / user | 不输出生产代码，只输出方向描述 + 信息架构判断 |
| UI implementation | Codex Desktop 或 Claude Code CLI | 直接写 React/Vite/shadcn/ui 实现 |
| UI review | user 双屏 localhost + 截图 | 截图回喂 Claude Code / Codex |
| 视觉方向探索 | Claude Code in VSCode 截图迭代 | 不依赖外部原型工具 |

### 3.4 SRD §3.10 FR-UI-003 风险段修订

旧：

> Risks: UX 复杂度高，Phase 2 启动前需 Claude Design 高保真 mock

新：

> Risks: UX 复杂度高，Phase 2 启动前需先在 Claude Code in VSCode 中迭代 3 轮静态 mock + user 截图反馈 + Codex 实现，**不依赖 Claude Design**。

### 3.5 DESIGN.md 角色重写（lock）

DESIGN.md **保留**，但内容从"Claude Design 使用规则"改为：

```text
DESIGN.md 必含：
- 设计原则（dark-first / high-density / evidence ledger / mission control）
- 页面信息密度（每页字数 / 卡片密度 / 状态色密度）
- 状态色谱（observed / opened / hypothesized / capturing / evidence_locked / failed）
- 组件清单（AppShell / SignalCard / SignalWorkbenchLayout / ScopeBuilder / BudgetMeter / PipelineCanvas / JobDetailDrawer / TranscriptTimeline / LibraryCard / RawPatchPreview）
- shadcn/ui 使用约束（不抽 packages/ui，组件直接放 apps/console/src/components）
- Signal Workbench 三栏布局规范
- Capture Pipeline 可视化原则（节点状态 / 失败 / 重试）
- 禁止：iframe / WebView 平台内嵌（LP-004）
- 禁止：在 UI 层加业务逻辑（INV-A1）
```

DESIGN.md **不再包含**：

```text
- "Claude Design Prompt"（旧 docs/ScoutFlow-Claude-Design-Brief-v0.1.md §4-§7 内容）
- "Claude Design Handoff 格式"（旧 §8）
- "Claude Design 已知限制"（旧 §9）
```

旧 `ScoutFlow-Claude-Design-Brief-v0.1.md` **归档**到 `docs/archive/`，标 `superseded by SRD-A002`。

### 3.6 落地动作

- [ ] SRD-v1 §2.3 user 角色表删除 Claude Design 行
- [ ] SRD-v1 §3.10 FR-UI-003 Risks 段更新
- [ ] DESIGN.md 重写
- [ ] 旧 Claude Design Brief 归档到 `docs/archive/ScoutFlow-Claude-Design-Brief-v0.1.md`
- [ ] AGENTS.md §1 角色表同步删除 Claude Design

---

## 4. SRD-A003 — capture_mode 命名清晰化

### 4.1 冲突描述

PRD §7.5.5 / SRD §3.5 锁定 `captures.capture_mode` enum：

```text
metadata_only / audio / video / transcript_only
```

但 amendment §1.2 / SRD §3.5 / FR-CAP-003 写：

```text
capture_mode ∈ {metadata_only, audio_transcript}
```

`audio_transcript` 不在 DB enum 中，会让 Codex 实现时困惑：是 DB enum 还是 UI 便捷字段。

### 4.2 修订（lock）

#### 4.2.1 DB enum 保持 PRD 原版（不变）

```sql
captures.capture_mode CHECK (capture_mode IN
    ('metadata_only', 'audio', 'video', 'transcript_only'))
```

DB enum **永远只有这 4 个值**。

#### 4.2.2 新增 quick_capture_preset（UI/API 便捷字段）

```text
quick_capture_preset:
  metadata_only       # 等价 capture_mode='metadata_only', no further outputs
  audio_transcript    # capture_mode='audio' + requested_outputs=['transcript','normalized','index']
```

`quick_capture_preset` **仅在 quick_capture API payload 出现**，不进 DB schema。

#### 4.2.3 API 拆字段

quick_capture 请求 payload：

```json
POST /captures/discover
{
  "platform": "bilibili",
  "platform_item_id": "BV1xxx",
  "canonical_url": "https://...",
  "source_kind": "manual_url",
  "quick_capture_preset": "audio_transcript",   // UI 便捷字段
  "_resolved": {                                 // API 在收到后自动展开
    "capture_mode": "audio",
    "requested_outputs": ["audio", "transcript", "normalized", "index"]
  }
}
```

API 内部把 `quick_capture_preset` 展开为 `capture_mode` + `requested_outputs`，DB 只存 `capture_mode`。

`requested_outputs` 不入 DB（运行时由 jobs 表 + lifecycle 表达），**只在 API payload 用作"我要哪些处理步骤"的声明**。

#### 4.2.4 capture_plan 路径不影响

capture_plan 路径下的 capture 创建不使用 `quick_capture_preset`，直接由 plan.scope.targets[].actions 决定：

```json
{
  "platform": "bilibili",
  "platform_item_id": "BV1xxx",
  "source_kind": "capture_plan",
  "capture_plan_id": "01HXX...",
  "capture_mode": "audio",
  // capture_plan 已经在 scope_json 里指定 actions，不需要 quick_capture_preset
}
```

### 4.3 SRD-v1 §3.5 FR-CAP-003 修订

旧：

> capture_mode ∈ {metadata_only, audio_transcript}

新：

> quick_capture_preset ∈ {metadata_only, audio_transcript}（仅 quick_capture 路径有效；API 内部展开为 capture_mode + requested_outputs）

### 4.4 影响

- DR-States §4.3 capture_mode enum 锁定不变
- 新增 enum：quick_capture_preset
- IF-API-Captures-Discover schema 调整
- FR-CAP-003 acceptance 调整：测 `quick_capture_preset` 展开后的 capture_mode 是否符合预期

---

## 5. SRD-A004 — source_kind 命名统一

### 5.1 冲突描述

SRD-v1 中 `source_kind` 出现两种写法：

| 位置 | 写法 |
|---|---|
| §3.5 FR-CAP-001 Inputs | `source_kind` / Outputs `created_by_path='quick_capture'` |
| §5.1.3 IF-API-Captures-Discover | `source_kind: "manual_url" \| "capture_plan_triggered"` |
| §5.1.3 验证段 | "若 source_kind=manual_url" / "若 source_kind=capture_plan_triggered" |
| FR-LP-001 / TC-LP001 | `source_kind=recommendation` / `keyword` / `raw_gap` |

`capture_plan_triggered` 又长又与 `created_by_path='capture_plan'` 重复语义。

### 5.2 修订（lock）

#### 5.2.1 source_kind enum

```text
source_kind ∈ {
  manual_url,             # user 手动粘贴单条 URL
  capture_plan,           # 由 approved capture_plan 触发
  recommendation,         # 推荐流（Phase 1A reject）
  keyword,                # 关键词扫描（Phase 1A reject）
  list,                   # 列表源（Phase 1A reject）
  raw_gap,                # Reverse Discovery（Phase 1A reject）
  agent                   # agent 触发（Phase 1A reject）
}
```

LP-001 enforcement Phase 1A 仅允许 `manual_url`；Phase 2+ 允许 `capture_plan`；其他永远走 capture_plan 路径不直接 discover。

#### 5.2.2 created_by_path enum

```text
created_by_path ∈ {
  quick_capture,          # quick_capture 路径
  capture_plan,           # capture_plan 路径
  manual_admin            # user 通过 admin tool 创建（运维场景）
}
```

#### 5.2.3 source_kind 与 created_by_path 的关系

| API source_kind | DB created_by_path | 何时 |
|---|---|---|
| `manual_url` + 满足 quick_capture 条件 | `quick_capture` | Phase 1A 主路径 |
| `manual_url` + 不满足 quick_capture | 拒绝（422，提示走 capture_plan） | Phase 1A |
| `capture_plan` | `capture_plan` | Phase 2+ |
| `recommendation` / `keyword` / `list` / `raw_gap` / `agent` | （不创建 capture，前置 422 + 提示走 capture_plan） | Phase 1A 全 reject |
| 任意（user CLI 工具运维）| `manual_admin` | 故障恢复场景 |

#### 5.2.4 SRD §5.1.3 IF-API-Captures-Discover schema 修订

```diff
  Body:
    platform: ...
    platform_item_id: ...
    canonical_url: ...
-   capture_mode: "metadata_only" | "audio" | "video" | "transcript_only"
-   source_kind: "manual_url" | "capture_plan_triggered"
+   source_kind: "manual_url" | "capture_plan"
+   quick_capture_preset: "metadata_only" | "audio_transcript"  // 仅 source_kind=manual_url 时
+   capture_mode: "metadata_only" | "audio" | "video" | "transcript_only"  // 仅 source_kind=capture_plan 时
    source_id: string?
-   capture_plan_id: string?
+   capture_plan_id: string?  // 仅 source_kind=capture_plan 时必填
    hit_mode: enum?
```

### 5.3 全文搜索清理

amendment 落地时需 grep 全 SRD：

```bash
grep -n "capture_plan_triggered" docs/SRD-v1-*.md
grep -n "capture_plan_triggered" docs/PRD-*.md
```

发现的所有 `capture_plan_triggered` 替换为 `capture_plan`（API source_kind 语境）或 `capture_plan` path（DB created_by_path 语境）。

### 5.4 影响

- IF-API-Captures-Discover schema 修订（§5.1.3）
- TC-LP001-007 / TC-LP001-008 测试 input 字段更新
- FR-CAP-001 Inputs 字段名规范化
- AGENTS.md / decisions.md 后续创建时使用统一命名

---

## 6. SRD-A005 — artifact_assets 残留 media_assets 清理

### 6.1 残留位置

SRD-v1 §4.5 DR-Integrity 表内：

> DR-INT-02 | DB **media_assets**.file_path ↔ FS 实际存在

amendment v1.1 §4.2 已经把 `media_assets` 改名 `artifact_assets`（D026）。SRD 应同步。

### 6.2 修订（lock）

#### 6.2.1 SRD §4.5 DR-Integrity 修订

```diff
- DR-INT-02 | DB media_assets.file_path ↔ FS 实际存在
+ DR-INT-02 | DB artifact_assets.file_path ↔ FS 实际存在
```

#### 6.2.2 全文 grep + 修订

落地时跑：

```bash
grep -nE 'media_assets' docs/SRD-v1-*.md
grep -nE 'media_assets' docs/PRD-v1-2026-05-02.md  # PRD §7.5.10 标题历史保留
grep -nE 'media_assets' docs/PRD-v1.1-amendment-2026-05-02.md  # 仅 §4.2 改名章节保留
```

修订原则：

- **历史段落（PRD §7.5.10 标题）保留 `media_assets → artifact_assets`** 的改名文字（这是变更日志）
- **任何引用当前实体的位置使用 `artifact_assets`**
- amendment §4.2.2 / §4.2.3 内容已正确

### 6.3 SRD §10.3 D-lock 追溯检查

D026（artifact_assets 改名）映射到 SRD ID：DR-Mig-001 / DR-Mig-004。

DR-Mig-001 应该**直接命名 `artifact_assets`**（不要先建 `media_assets` 再改名）。DR-Mig-004 仅作"历史 schema 升级"占位，**当前不实际执行**（合并到 001）。

### 6.4 worker / API / Console 命名

落地时 grep `apps/`/`services/`/`workers/` 任何 `MediaAsset` / `media_assets` / `media_asset` → 改为 `ArtifactAsset` / `artifact_assets` / `artifact_asset`。

`tools/check-banned-words` 暂不加 `media_assets` 到禁用词（因为它是历史命名，可能在 PRD §7.5.10 中合规出现）；改名工作通过 code review enforce。

---

## 7. SRD-A006 — NFR 三档分层

### 7.1 修订原因

SRD-v1 §6 NFR 50+ 条全部默认作 Phase 0/1A 阻断项。但实际上：

- **架构 / 安全** 类 NFR 必须 Phase 0/1A 硬上（如 LP enforcement / 凭据安全 / worker write-zone）
- **质量** 类 NFR（如 coverage 70% / type hint 90% / API P95 < 100ms）应作 Phase 验收推荐，未达不阻断（warning）
- **观察** 类 NFR（如 ASR 速度 / normalize cost / wall time）应作 Phase 1A 跑出来后**记录 baseline**，不预设阈值，等数据出来后再调整

如果全部当 Hard Gate，Phase 1A 第一条 B 站 URL 还没跑通，已经被 ASR 速度 / coverage 阻塞。

### 7.2 三档分层（lock）

#### 7.2.1 Hard Gate（Phase 阻断，不达不发布）

| NFR ID | 含义 |
|---|---|
| NFR-SEC-01 | 凭据存 `~/.scoutflow/credentials.json` mode 600 |
| NFR-SEC-02 | 凭据不进 git |
| NFR-SEC-04 | API 仅 bind 127.0.0.1 |
| NFR-SEC-05 | LP-001 enforcement 100% 生效（Phase 1A）|
| NFR-SEC-08 | 命名禁区 lint 100% 生效 |
| NFR-SEC-09 | RAW 主仓不被 ScoutFlow 直接修改 |
| NFR-REL-01 | worker crash 重启后不丢状态 |
| NFR-REL-02 | API 重启后 DB/FS 一致性自检 |
| NFR-MAINT-09 | 任何 schema 改 → 必 migration + 单测 |
| INV-A1 至 INV-A5 | 所有架构不变量 |

**Phase 0/1A 这些不达 → 不验收**。

#### 7.2.2 Quality Target（Phase 验收推荐，未达 warning）

| NFR ID | 目标 | 行为 |
|---|---|---|
| NFR-MAINT-01 | 单测覆盖 ≥ 70%（1A）/ ≥ 80%（2+） | 报告偏差；< 50% 才阻断 |
| NFR-MAINT-02 | type hint ≥ 90% | 同上 |
| NFR-MAINT-03 | TS strict | binary，必上 |
| NFR-MAINT-04 至 06 | 单文件 / 函数 / 嵌套深度 | warning |
| NFR-PERF-01 | API GET P95 < 100ms | Phase 1A 测，未达调优；< 500ms 才阻断 |
| NFR-PERF-02 | API POST discover P95 < 200ms | 同上 |
| NFR-PERF-03 | FTS5 P95 < 200ms | 同上 |
| NFR-PERF-07 | Console 首屏 < 2s dev | 同上 |
| NFR-OBS-01 至 07 | 可观测性 | 必上但不数量化阻断 |

**Phase 1A 这些未达 → 报告 + warning，可放行进 Phase 1B**。

#### 7.2.3 Observation Baseline（Phase 1A 仅记录，不预设阈值）

| NFR ID | 行为 |
|---|---|
| NFR-PERF-04 | 单 capture 全链路（B 站 14min）总耗时 → 记录为 baseline，不预设 ≤ 20 min |
| NFR-PERF-05 | ASR 速度（faster-whisper / Mac M5）→ 记录 baseline，不预设 ≥ 1.5x realtime |
| NFR-PERF-06 | normalize 单 capture 耗时 → 记录 baseline，不预设 ≤ 60s |
| NFR-PERF-09 | worker 内存峰值 → 记录 baseline，不预设 < 8GB |
| NFR-PERF-10 | DB 写入并发 → 记录 baseline |
| NFR-PERF-11 | plan estimate 耗时 → Phase 2 记录 |
| LLM token 成本 / capture | 记录 baseline，每月聚合（Phase 2+）|

**Phase 1A 跑通后**，这些 baseline 写到 `docs/observations/phase-1a-baseline-YYYY-MM-DD.md`，作为 Phase 2 的优化目标。

### 7.3 Phase 验收 §8.7 修订

旧 Phase 1A 验收（§8.7）：

```
[ ] 单测覆盖 ≥ 70%
[ ] make test ≤ 5 min
```

新（拆 Hard Gate / Quality Target / Observation）：

```text
Hard Gate（必过）：
[ ] LP-001 enforcement TC 全过（TC-LP001-001 至 008）
[ ] LP-005 lint 全过
[ ] worker write-zone 测试全过（INV-A3）
[ ] FS layout 完全符合 PRD §5
[ ] artifact_assets 表数据正确（每文件 sha256 登记）
[ ] 单 B 站 URL → Library 可检索（功能 binary 通过）
[ ] make migrate 跑通
[ ] make api-up + healthz 200

Quality Target（推荐过，warning 不阻断）：
[ ] 单测覆盖 ≥ 70%
[ ] type hint ≥ 90%
[ ] make test ≤ 5 min
[ ] FTS5 检索 P95 < 200ms（如 DB ≤ 1 GB）

Observation Baseline（仅记录到 docs/observations/）：
[ ] 单 capture 全链路平均耗时
[ ] ASR 速度（large-v3 / Mac M5）
[ ] normalize 单 capture 耗时
[ ] worker 内存峰值
[ ] LLM token 成本
```

### 7.4 影响

- SRD §6 整体保留，但加 §6.0 三档分层说明
- §8.7 Phase 1A / 1B / 2 验收 checklist 全部按三档重排
- 新增文档 `docs/observations/phase-1a-baseline-template.md`（Phase 1A 跑通后填写）

---

## 8. SRD-A007 — LLM 模型名抽象化

### 8.1 修订原因

PRD / SRD / amendment 多处写死模型名：

| 位置 | 写法 |
|---|---|
| PRD §16.6 | `claude-haiku-4-5` / `claude-sonnet-4-6` / `claude-opus-4-7` |
| SRD §3.6 FR-WRK-Norm-001 至 003 | 默认引擎 `claude-haiku-4-5` / `claude-sonnet-4-6` |
| amendment v1.1 §16.6 LLM 路由 | 同上 |

模型升级（4.5 → 4.7）后必须改 PRD/SRD，治理重。

### 8.2 修订（lock）— 角色别名

#### 8.2.1 LLM 角色别名 enum

| 角色别名 | 用途 | Phase 启用 |
|---|---|---|
| `LLM_SUMMARY_FAST` | 三句摘要 / 标签 / 简单分类 | 1A |
| `LLM_NORMALIZE_MAIN` | structured.md / claims / quotes / topic_candidates | 1A |
| `LLM_RAW_LINKER` | RAW node 匹配 + patch 生成 | 1B |
| `LLM_RERANKER` | 推荐重排 + 推荐理由 | 3 |
| `LLM_LONG_CONTEXT` | 大于 30 min 视频 / 长文跨段关联 | 1A 末 / 2 |
| `LLM_PLAN_ESTIMATOR` | plan 估算（仅 token 数估算） | 2 |
| `LLM_REVERSE_DISCOVERY` | RAW gap → keywords | 2 |

#### 8.2.2 .env 映射

```env
# .env.example 加
SCOUTFLOW_LLM_SUMMARY_FAST=claude-haiku-4-5
SCOUTFLOW_LLM_NORMALIZE_MAIN=claude-sonnet-4-6
SCOUTFLOW_LLM_RAW_LINKER=claude-sonnet-4-6
SCOUTFLOW_LLM_RERANKER=claude-sonnet-4-6
SCOUTFLOW_LLM_LONG_CONTEXT=claude-opus-4-7
SCOUTFLOW_LLM_PLAN_ESTIMATOR=claude-haiku-4-5
SCOUTFLOW_LLM_REVERSE_DISCOVERY=claude-sonnet-4-6

# fallback 映射（主模型不可用时）
SCOUTFLOW_LLM_SUMMARY_FAST_FALLBACK=gpt-4-mini
SCOUTFLOW_LLM_NORMALIZE_MAIN_FALLBACK=gpt-4o
```

#### 8.2.3 settings.py 中央加载

```python
# services/api/scoutflow_api/settings.py（也供 workers 引用）
class LLMRouting(BaseSettings):
    summary_fast: str = "claude-haiku-4-5"  # default 但被 env 覆盖
    normalize_main: str = "claude-sonnet-4-6"
    raw_linker: str = "claude-sonnet-4-6"
    reranker: str = "claude-sonnet-4-6"
    long_context: str = "claude-opus-4-7"
    plan_estimator: str = "claude-haiku-4-5"
    reverse_discovery: str = "claude-sonnet-4-6"

    summary_fast_fallback: str = "gpt-4-mini"
    normalize_main_fallback: str = "gpt-4o"

    class Config:
        env_prefix = "SCOUTFLOW_LLM_"
```

#### 8.2.4 worker 调用

```python
# workers/normalize/main.py
from services.api.scoutflow_api.settings import LLMRouting

llm_routing = LLMRouting()
model_name = llm_routing.normalize_main  # 不写死字符串

response = anthropic_client.messages.create(model=model_name, ...)
```

### 8.3 SRD §3.6 FR-WRK-Norm-* 字段修订

旧：

```
默认引擎 claude-haiku-4-5
```

新：

```
默认引擎 LLM_SUMMARY_FAST（从 env 读，default claude-haiku-4-5）
```

### 8.4 PRD §16.6 修订

PRD §16.6 LLM 路由表保留**作为默认值参考**，并加一条说明：

> 表中模型名仅为初始默认值；实际 worker 调用必须读 env / settings.LLMRouting，**不在代码中硬编码模型名**。模型升级时仅改 .env，不改 PRD/SRD/代码。

PRD §16.6 表内容不删，但加表头说明。

### 8.5 影响

- 所有 worker 不硬编码模型名
- env / settings.py 是模型名唯一真源
- 模型升级 = 改 .env（不动 PRD/SRD/代码）

---

## 9. SRD-A008 — 新增 docs/task-index.md 共享任务账本

### 9.1 修订原因

SRD §11.E 落地任务清单 P0-P6 是**总目录**，按 Phase 分组。但缺一个**每日动态任务索引**，作为多个 AI 编程工具（Claude Code / Codex Desktop / Cursor / 其他）之间的共享账本。

旧 5 份 organization docs 提到 `docs/current.md` 是"agent handoff 文件"，但 current.md 是**单一活状态源**（≤80 行硬上限），不适合放任务清单。

### 9.2 task-index.md 定位（lock）

| 维度 | docs/current.md | **docs/task-index.md** | docs/specs/api-routes-v1.1.md |
|---|---|---|---|
| 内容 | 当前 phase / 本周可改 / 禁止改 / 最新验证 | **当前所有 active / pending / blocked 任务** | API 契约 |
| 行数 | ≤ 80 | ≤ 300 | 不限 |
| 写权 | user 主写 + 任意 agent 同步 | **任意 agent 任意时刻可写** | Codex 主笔 |
| 频率 | 每天 1-3 次 | **每个 commit / 每个 session 必更新** | migration 时 |
| 治理 | 极轻 | **薄账本（不是 Jira / 不是 Agent Dispatch）** | 中等 |
| 与 PR/handoff 关系 | handoff 写 current 简版 | **PR 完成后必更新 task-index 对应行** | — |

### 9.3 task-index.md schema（lock）

文件路径：`docs/task-index.md`

格式：

```markdown
# ScoutFlow Task Index

> 共享任务账本。任意 agent 任意时刻可写。每个 commit / session 必更新。
> 不是 Jira。不是 Agent Dispatch。是薄账本。

## 当前 Phase: 1A

## Active（在跑）

| ID | Title | Owner | Started | Phase | Status | Touches | Notes |
|---|---|---|---|---|---|---|---|
| T-001 | FR-LP-001 scope_gate.py middleware | Codex | 2026-05-02 | 1A | in_progress | services/api/middleware/ + tests/api/ | 配 TC-LP001-001 至 008 |
| T-002 | FR-CAP-001 quick_capture happy path | Codex | 2026-05-03 | 1A | blocked_on_T-001 | services/api/routes/captures.py | 等 scope_gate 合入 |

## Pending（待启）

| ID | Title | Phase | Priority | Depends |
|---|---|---|---|---|
| T-003 | FR-WRK-Bili-001 metadata fetch | 1A | P0 | T-002 |
| T-004 | FR-WRK-Media-001 audio extract | 1A | P0 | T-003 |
...

## Blocked（受阻）

| ID | Title | Blocked Reason | Action Needed | Blocked Since |
|---|---|---|---|---|
| T-099 | XHS adapter 实现 | Phase 2 未启用 | wait Phase 2 | 2026-05-02 |

## Done（最近 10 条）

| ID | Title | Completed | Commit |
|---|---|---|---|
| T-000 | git init + Phase 0 docs | 2026-05-02 | abc123 |
...

## 维护规则

1. 每个新任务由发起方 agent 加 row 到 Pending（可 user 手动加）
2. 拉任务进 Active 时填 Owner + Started + Status
3. 完成 commit 后移 row 到 Done（保留最近 10 条，超过移到 docs/archive/task-index-YYYY-MM.md）
4. blocked 时移到 Blocked + 写 reason
5. 任何 agent 发现 Active 任务 24h 无进展 → 标 stale 并提醒 user
6. 不写细节，细节进 PR / handoff / commit message
```

### 9.4 task-index.md 与其他文件的边界

#### 9.4.1 task-index.md vs PR description

| 信息 | 落点 |
|---|---|
| 任务 ID + Title + Owner + Status | task-index.md |
| 触碰哪些 contract / 验证步骤 / 风险 | PR description |
| introduced vs exposed | PR description |
| 任务详细需求 | SRD FR-* |

#### 9.4.2 task-index.md vs current.md

| current.md | task-index.md |
|---|---|
| 当前 Phase | 当前 Phase（同步） |
| 本周可改 / 禁止改目录 | — |
| 最近一次验证结果 | — |
| 已锁 contract 提示 | — |
| — | active / pending / blocked / recently-done 任务表 |

current.md 写"我现在能改什么"，task-index.md 写"现在有哪些任务"。

#### 9.4.3 task-index.md vs SRD §11.E

| SRD §11.E | task-index.md |
|---|---|
| 总规划（P0-P6 全 Phase）| 当前活账（仅本 Phase 内任务）|
| 静态（amendment 才改）| 动态（每个 commit 更新）|
| 编号 P0/P1/... | 编号 T-NNN |
| 不写状态 / 不写 Owner | 必写 |

落地时：从 SRD §11.E 选当前 Phase 任务 → 拆成 T-NNN → 入 task-index.md Pending。

### 9.5 谁可以写 task-index.md

| Agent | 写权 | 限制 |
|---|---|---|
| user | 全权 | — |
| Codex | 全权（Active/Pending/Blocked/Done 行）| 必含 commit hash（在 Done 时） |
| Opus | 全权 | 偏重写 Pending（规划） / Blocked（识别） |
| Hermes | 加 Pending（Phase 3+ 触发的任务）| 不直接进 Active |
| OpenClaw | 同 Hermes | 同上 |
| Claude Code（VSCode）| 全权 | 同 Codex |

### 9.6 task-index.md 不做的事

- ❌ 不做 Jira / Linear（不要 epic / sprint / velocity / story points）
- ❌ 不做 Agent Dispatch UI 替代品（Phase 4 启用，与 task-index 分开）
- ❌ 不放任务详细需求（SRD 是真源）
- ❌ 不放 PR review 讨论（GitHub PR 是真源）
- ❌ 不超 300 行（超时移老条目到 archive/）

### 9.7 落地动作

- [ ] Phase 0 第一个 commit 必含 `docs/task-index.md`（初始化空账本，表头 + 维护规则）
- [ ] AGENTS.md 加一段说明 task-index.md 角色
- [ ] `tools/lint-docs` 加规则：task-index.md ≤ 300 行；Active 表格无 row 时仍要保留表头

---

## 10. SRD 主文件 amendment notice

在 `SRD-v1-2026-05-02.md` 顶部 H1 之后加：

```markdown
> ⚠ **重要 — 必须配合 amendment 一起读**
> 本 SRD 已有 v1.1 amendment（2026-05-02），文件：[`SRD-v1.1-amendment-2026-05-02.md`](./SRD-v1.1-amendment-2026-05-02.md)
> 冲突时 **amendment > base SRD**。
> 8 条修订：
> 1. SRD-A001 — Authority Chain 修订（CRITICAL：SRD 不能自动覆盖 PRD/amendment）
> 2. SRD-A002 — Claude Design 移除（UI 工作流改 Claude Code in VSCode）
> 3. SRD-A003 — capture_mode 命名清晰化（DB enum 不变 + quick_capture_preset 便捷字段）
> 4. SRD-A004 — source_kind 命名统一（取消 capture_plan_triggered）
> 5. SRD-A005 — artifact_assets 残留 media_assets 清理
> 6. SRD-A006 — NFR 三档分层（Hard Gate / Quality Target / Observation Baseline）
> 7. SRD-A007 — LLM 模型名抽象化（角色别名 + .env 映射）
> 8. SRD-A008 — 新增 docs/task-index.md 共享任务账本
> 影响章节：§0.4 / §2.3 / §3.5 / §3.10 / §4.5 / §5.1.3 / §6 / §8.7 / §11.E / §11.F
> **不动**：§3.1-§3.4 业务实体 FR / §4 DR-FS / §10 追溯矩阵主体
```

并在 §0.5 版本与变更表加一行：

```markdown
| v1.1 amendment | SRD-A001 至 SRD-A008（8 条必修） | 2026-05-02 | DRAFT，待 user 拍板 |
```

---

## 11. 不变项总览（amendment 不动）

确保 user 知道哪些**没动**：

- §1 范围 / 术语 / 引用 — 完整保留
- §2.1 系统架构 4 层堆栈 + 5 INV — 完整保留
- §2.2 系统组件清单 — 完整保留
- §2.4 CR-Runtime 运行环境约束 — 完整保留
- §2.5 高层数据流 — 完整保留
- §2.6 关键时序 UC-P1 — 完整保留
- §3.1 Sources / §3.2 Signals / §3.3 Hypotheses / §3.4 Capture Plans 业务实体 FR — 完整保留
- §3.5 captures FR 主体保留，仅 FR-CAP-003 quick_capture_preset 字段调整
- §4.1 DR-Schema migration 演进路径 — 保留（但 DR-Mig-001 直接用 artifact_assets，DR-Mig-004 折叠）
- §4.2 DR-FS 文件系统 layout — 完整保留
- §4.3 DR-States 状态词汇表 — 完整保留 + 新增 source_kind / created_by_path / quick_capture_preset / LLM 角色别名 enum
- §4.4 DR-Lifecycle — 完整保留
- §4.6 DR-Backup — 完整保留
- §5.2 IF-Worker — 完整保留
- §5.3 IF-Console — 完整保留
- §5.4 IF-RAW — 完整保留
- §5.5 IF-Hermes — 完整保留
- §5.6 IF-Contracts — 完整保留
- §6.1 至 §6.8 NFR 内容 — 完整保留，仅加 §6.0 三档分层说明
- §7 系统约束 — 完整保留
- §9 部署运维 — 完整保留 + .env 增补 LLM 角色别名
- §10 追溯矩阵主体 — 完整保留 + 加 SRD-A001 至 SRD-A008 追溯
- §11 附录 — 完整保留 + 增 SRD-A 编号约定

---

## 12. 落地任务清单（给 Codex / Opus / user）

### 12.1 P0 — user 拍板 amendment 后立即（在 Phase 0 git init 之前）

- [ ] **SRD-A001 仲裁链修订**：在 SRD-v1 §0.4 / §11.F 文本替换（仅这两处文本编辑）
- [ ] **SRD-A005 全文 grep `media_assets`**：手工检查 SRD-v1 / PRD / amendment，发现违规处即改
- [ ] **SRD-A002 DESIGN.md 重写**：按 §3.5 模板写新 DESIGN.md
- [ ] **SRD-A002 旧 Brief 归档**：mv `docs/ScoutFlow-project-organization-docs-v0/ScoutFlow-Claude-Design-Brief-v0.1.md` → `docs/archive/`
- [ ] **SRD-A002 AGENTS.md 删除 Claude Design 行**
- [ ] **SRD-A008 创建 docs/task-index.md**：按 §9.3 模板初始化空账本
- [ ] **SRD-A007 .env.example 增补 LLM 角色别名映射**：按 §8.2.2 加 7 + 2 行

### 12.2 P1 — Phase 0 落地时（在 commit 1-3 中）

- [ ] **SRD-A003 / SRD-A004 IF-API-Captures-Discover schema 实现**：按 §4.2.3 / §5.2.4 落 FastAPI Pydantic model
- [ ] **SRD-A006 §8.7 Phase 1A 验收 checklist 拆三档**：在 SRD-v1 §8.7 替换为新版
- [ ] **SRD-A007 settings.py LLMRouting 类**：按 §8.2.3 实现
- [ ] **SRD-A008 AGENTS.md 加 task-index 角色说明**

### 12.3 P2 — Phase 1A 落地时

- [ ] **SRD-A006 Hard Gate / Quality Target / Observation Baseline 三档逻辑**：CI 区分阻断 vs warning vs 仅记录
- [ ] **SRD-A006 docs/observations/phase-1a-baseline-template.md 创建**：Phase 1A 跑通后填写
- [ ] **SRD-A005 worker / API / Console 命名 grep**：任何 `MediaAsset` / `media_assets` 改 `ArtifactAsset` / `artifact_assets`

### 12.4 P3 — Phase 1B / Phase 2 落地时

- [ ] **SRD-A007 raw_linker / reranker / plan_estimator worker 用 LLM 角色别名**：不硬编码
- [ ] **SRD-A002 Signal Workbench UI 不依赖 Claude Design**：用 Claude Code in VSCode 迭代

---

## 13. SRD-A 编号约定（新增）

继承 SRD-v1 §0.2 编号约定，增补：

| 前缀 | 含义 | 示例 |
|---|---|---|
| `SRD-A` | SRD amendment ID | SRD-A001 |
| `T-` | task-index 任务 ID（§9.3） | T-001 |

后续 SRD 修订必须经 SRD-A 流程，编号递增（SRD-A009 / SRD-A010 / ...），不允许 in-place rewrite SRD-v1。

---

## 14. Amendment v1.1 完结声明

> **SRD v1.1 amendment 完结**
>
> 版本：v1.1（DRAFT，待 user 拍板）
> 起草：2026-05-02
> 行数：~1100
> 状态：8 条必修 amendment（SRD-A001 至 SRD-A008）
>
> 与 SRD-v1 一起读。冲突时 amendment > SRD-v1。
>
> ScoutFlow 工程契约总量（含本 amendment）：
> - 5 LP（locked principles）
> - 38 D-lock + 8 SRD-A
> - 5 INV（架构不变量）
> - 14 migrations
> - 76 API 路由
> - 25 张 DB 表
> - 9 Console 页面
> - 11 类 worker
> - 5 phase
>
> 关键工程契约修正：
>
> > **SRD 是工程规约，不是产品哲学真源。SRD 不能自动覆盖 PRD/amendment。**
>
> > **NFR 三档：Hard Gate（必过）/ Quality Target（推荐）/ Observation Baseline（仅记录）**
>
> > **task-index.md 是多 AI 编程工具的薄账本，不是 Jira。**
>
> 下一步：
>
> 1. user 通读 amendment（重点 §2 SRD-A001 仲裁链）
> 2. user 拍板锁定 SRD-A001 至 SRD-A008
> 3. 启动 §12.1 P0 任务（最紧的是 SRD-A001 文本替换 + SRD-A008 task-index 初始化）
> 4. 然后才进 OM § 11.E P0（git init + Phase 0 docs 入口三薄文档）
