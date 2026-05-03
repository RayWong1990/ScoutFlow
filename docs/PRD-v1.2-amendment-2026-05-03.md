# PRD v1.2 Amendment — 2026-05-03

> 本文件是 `T-P1A-010C` 的 PRD amendment repair draft。
> 状态：`candidate / draft / not final authority / not runtime approval`。
> 本文件补充 `docs/PRD-v1-2026-05-02.md` 与 `docs/PRD-v1.1-amendment-2026-05-02.md`，不做 base PRD 全文重写。
> 当前用途：把 `T-P1A-009` 的真实结论、Wave 1 并行策略、BBDown no-auth gate、QR / manual auth 风险、`audio_transcript` 阻塞条件写成待拍板产品补丁。

## 0. 元信息

| 字段 | 值 |
|---|---|
| amendment ID | `PRD-A034-A040` |
| 任务来源 | `T-P1A-010C` |
| 触发原因 | `T-P1A-009` 未找到本地 `BBDown` executable，未触达平台边界；旧 PRD / amendment 对 `audio_transcript`、BBDown、auth、runtime gate 的表达需要收紧 |
| 基线文档 | `docs/PRD-v1-2026-05-02.md` |
| 上一版补丁 | `docs/PRD-v1.1-amendment-2026-05-02.md` |
| 本文件角色 | PRD 层产品边界补丁，不是 SRD 细化实现 |
| 当前不批准 | product code、BBDown execution、QR login、manual auth、media download、ffmpeg、ASR、workers、frontend、Phase 2-4 runtime |

## 1. 生效规则

- 未经 user 拍板前，本文件所有条目都是 `candidate amendment`。
- 若本文件与 v1 / v1.1 在 BBDown runtime、manual auth、`audio_transcript`、并行执行边界上冲突，后续应以 user 拍板后的 v1.2 口径为准。
- 本文件不直接修改 base PRD 的故事线、信息架构、Phase 2-4 outline；只列出后续机械 patch 清单。
- 本文件不得被解释为 `T-P1A-010A`、`T-P1A-010B` 或任何 runtime task 的完成依据。

建议状态机：

```text
draft_candidate
  -> user_reviewed
  -> user_approved_candidate
  -> base_prd_patch_authorized
  -> superseded_or_archived
```

## 2. A034 — Runtime Gate Amendment

### 产品结论

BBDown 的本地工具可用性与 Bilibili 平台访问结果必须拆开。`T-P1A-009` 的结论是：

- `BBDown` executable 未在当前 `PATH` 中找到。
- 未执行 `BBDown -info`。
- 未触达 Bilibili 平台边界。
- 没有 `PlatformResult`。
- 只有 `tool_preflight_result=executable_not_found`。

### 产品规则

- `ToolPreflightResult` 表示本地工具链是否可启动，不表示平台允许或拒绝访问。
- `PlatformResult` 只在平台 probe 或 adapter 已经实际触达平台边界后产生。
- `executable_not_found` 是本地工具可用性阻塞，不是 `auth_required`、`forbidden`、`parser_drift`、`unknown_error` 或任何其他 `PlatformResult`。
- 任何把 `T-P1A-009` 写成 BBDown adapter runtime 成功的表达都必须修正。

### 当前用户体验含义

当前产品口径只能显示为“本机未找到 BBDown，需要先处理工具路径 / 安装 / wrapper preflight”。不能显示为“B 站访问失败”“需要登录”“平台禁止”或“解析失败”。

## 3. A035 — Parallel Execution Amendment

### 产品结论

Wave 1 可以并行，但并行单位是 conflict domain，不是所有 agent 都能改同一 authority 文件。

### 产品规则

- `T-P1A-010A`、`T-P1A-010B`、`T-P1A-010C` 可在不同分支并行推进。
- 同一 conflict domain 必须单写者。
- `docs/current.md` 与 `docs/task-index.md` 是 ledger-owner writeback 文件；执行 PR 不应自行改写任务状态。
- review / sidecar 可以给 patch suggestion，但不能绕过 ledger owner 写 authority。

### PRD 层影响

ScoutFlow 的轻治理不等于随意并发。产品协作设计应保留 `Single Writer / Multi Reviewer`，并把“谁能更新任务账本”与“谁能写 research / draft”分开。

## 4. A036 — BBDown No-Auth Metadata Gate

### 产品结论

BBDown no-auth metadata 是进入后续 `audio_transcript` 讨论前的窄门，但它本身仍不是 media / ASR approval。

### Gate 顺序

```text
tool_preflight
  -> no_auth_info_probe
  -> redacted_parser_classified_evidence
  -> receipt_candidate_design
  -> explore_trust_trace
```

### 产品规则

- tool preflight 必须先于 `-info`。
- `-info` 必须先于 receipt。
- receipt discipline 必须先于 Explore Trust Trace。
- no-auth metadata gate 不允许 media download、ffmpeg、ASR、manual auth、QR login、browser profile 读取或凭据注入。
- user-provided sample URL 可在未来获批的 no-auth metadata probe 中使用，但不得用于 auth、media download 或范围扩展。

### 最小可接受证据

no-auth metadata gate 至少需要：

- tool executable 可定位且版本可安全记录。
- `-info` against approved single manual URL 已执行。
- stdout / stderr 已脱敏。
- parser 已给出 typed result。
- 若未产生 `PlatformResult`，必须明确说明未触达平台边界。

## 5. A037 — QR Login / Manual Auth Gate

### 产品结论

QR login / manual auth 是独立高风险 gate，不属于 no-auth metadata probe。

### 产品规则

- no-auth metadata probe 不应提示、等待或要求 QR login。
- 如果未来打开 manual auth gate，agent 必须暂停等待 human scan；不能代替 user 扫码或自动读取登录态。
- QR code image、cookie、token、authorization header、signed URL、browser profile path、本地凭据文件路径都不得进入 Git、PR、CI、logs、DB artifacts、receipt、fixtures 或 tracked files。
- 浏览器 profile reading 默认禁止，除非未来另有明确 contract 修改。
- manual auth 失败或缺失只可导向人工动作，不可在同一任务中继续试探凭据。

### 产品呈现建议

未来 UI / CLI 提示应区分：

- 本地工具未配置：先解决 `ToolPreflightResult`。
- no-auth metadata 不可用：停止当前 probe，给出安全摘要。
- manual auth required：转人工 gate，不自动读取或保存凭据。

## 6. A038 — Audio Transcript Blocker

### 产品结论

`audio_transcript` 仍保持阻塞。它不能因为 BBDown research note、draft spec、fixture parser 或 local runtime spike report 存在就进入 active runtime。

### 解锁前置条件

后续讨论 `audio_transcript` 前，至少需要：

1. BBDown tool preflight 证明 executable 可用。
2. 一次获批 no-auth metadata probe 产生 redacted evidence。
3. parser 对 evidence 给出 typed classification。
4. tool preflight result 与 `PlatformResult` 已正确分离。
5. receipt / ledger discipline 已证明不会旁路 API authority。
6. user 明确批准下一 gate。

当前仍不批准：

- audio extraction
- media download
- ffmpeg
- ASR
- transcript artifact
- worker runtime
- frontend flow

## 7. A039 — Patch List

### 后续应机械 patch 的 base PRD 位置

| Patch | Base PRD / Amendment 位置 | 未来动作 |
|---|---|---|
| `PRD12-P001` | `docs/PRD-v1-2026-05-02.md` §6.1 / §9 / §15 中 BBDown “本机已通”相关表达 | 改成“候选工具，需 tool preflight 证明当前环境可用” |
| `PRD12-P002` | `docs/PRD-v1-2026-05-02.md` §9.2 / §9.3 / §9.4 media 与 ASR pipeline | 标明当前 Phase 1A active tasks 只开放 metadata / receipt 基线，不开放 media / ASR runtime |
| `PRD12-P003` | `docs/PRD-v1.1-amendment-2026-05-02.md` §1.2 quick_capture 条件 | 保留 `audio_transcript` 为 preset 叙事，但加“当前阻塞，需 metadata gate 后另行批准” |
| `PRD12-P004` | `docs/PRD-v1.1-amendment-2026-05-02.md` §9.3 / §10 / §13 与 Phase 计划 | 加入 `ToolPreflightResult` / `PlatformResult` 分离和 no-auth-first gate |
| `PRD12-P005` | 所有 auth / cookie 相关表达 | 分离 no-auth metadata 与 QR / manual auth gate，禁止 browser profile reading 作为默认路径 |

### 应保留为 reference outline 的内容

- Phase 2 Signal Workbench / Scope Builder。
- Phase 3 推荐、重排、Hermes 调度。
- Phase 4 Dispatch UI / 正式 review 队列。
- XHS / YouTube 真采集。
- media / ffmpeg / ASR / `audio_transcript` runtime。

## 8. A040 — Next Dispatch Plan

推荐后续 dispatch 保持独立 conflict domain：

| Candidate | 目的 | 允许结果 | 不允许 |
|---|---|---|---|
| `T-P1A-010A-review` | 审计 BBDown tool preflight package | 确认 `ToolPreflightResult` model 与 wrapper 不触达 URL | `-info`、auth、media、receipt |
| `T-P1A-010B-review` | 审计 injected-runner `-info` adapter shell | 确认 command builder / parser / fixture 分离真实 subprocess | live BBDown、credentials、receipt state |
| `T-P1A-010D` | 010C amendment user review / base patch authorization | user 决定 v1.2 是否进入 base PRD/SRD mechanical patch | 自动全文重写或打开 Phase 2-4 |
| `T-P1A-011` | 获批后的一次 no-auth metadata live probe gate | 仅在 tool preflight clear 且 user 明确批准后执行单 URL `-info` | QR login、manual auth、media、ffmpeg、ASR |

## 9. Red-Team Checklist

- 是否把 `executable_not_found` 写成了 `PlatformResult`？若是，停线。
- 是否把 `T-P1A-009` 写成 runtime success？若是，停线。
- 是否让 no-auth metadata probe 包含 QR login / manual auth？若是，停线。
- 是否把 `audio_transcript` 从阻塞改成 active runtime？若是，停线。
- 是否把 sample URL 用于下载、登录、auth 或范围扩展？若是，停线。
- 是否把 research note / draft spec / local report 写成 final authority？若是，停线。
- 是否让 Phase 2-4 真实逻辑进入当前 active tasks？若是，停线。
