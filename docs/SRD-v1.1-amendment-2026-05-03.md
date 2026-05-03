# SRD v1.1 Amendment — 2026-05-03

> 本文件是对 `docs/SRD-v1.1-amendment-2026-05-02.md` 的补充修订，不是 SRD 主体重写。
> 目标：把 A001-A015 收敛成开工安全补丁，只收口 Phase 0 / Phase 1A 的当前执行面。
> 状态：`草案`，待 user 拍板；未拍板前，本文中的“锁定项”都只代表待采纳补丁，不代表已生效事实。

## 0. 元信息

| 字段 | 值 |
|---|---|
| amendment ID | `SRD-A001-A015` |
| 文件角色 | `开工安全补丁` |
| 基线文档 | `docs/SRD-v1-2026-05-02.md` |
| 上一版补丁 | `docs/SRD-v1.1-amendment-2026-05-02.md` |
| 当前目标 | 缩窄 Step0 / Phase 0 / Phase 1A 的实现边界 |
| 当前不做 | SRD 主体全文重写、产品代码实现、目录骨架实现 |
| 当前输出类型 | amendment、task ledger、contract docs、入口文档 |

## 1. 生效规则

- 本文件补充 `docs/SRD-v1-2026-05-02.md` 与 `docs/SRD-v1.1-amendment-2026-05-02.md`
- 若 `2026-05-03` 与 `2026-05-02` amendment 在同一主题上冲突，当前以 `2026-05-03` 的补充口径为准
- 本文件不自动改写 base SRD；base SRD 的正文替换动作由后续明确任务执行
- 未经 user 明确拍板前，A001-A015 仅是 `proposed contract / pending user approval`
- 当前建议使用以下状态机管理 amendment：

```text
draft
  -> user_approved
  -> base_srd_patched
  -> phase0_ready
  -> superseded_by_next_amendment
```

## 2. 修订总览

| ID | 主题 | 当前目的 |
|---|---|---|
| `A001` | Authority Chain 修订 | 防止 SRD 越权覆盖 PRD/amendment |
| `A002` | Claude Design 移除 | 消除当前不可用工具依赖 |
| `A003` | Task Index | 建立轻量共享任务账本 |
| `A004` | `capture_mode` / `quick_capture_preset` 命名统一 | 稳定 DB enum，分离 UI 便捷字段 |
| `A005` | `source_kind` 命名统一 | 消除 `capture_plan_triggered` 漂移 |
| `A006` | `artifact_assets` 命名残留修正 | 清理 `media_assets` 当前实体残留 |
| `A007` | NFR 分级 | 把阻断项与观察项分层 |
| `A008` | Tool Roster 更新 | 同步当前真实工具栈 |
| `A009` | Tool Roster & Research Note Protocol | 给外部研究输出一个轻量协议 |
| `A010` | Phase Scope Freeze | 把 Phase 2-4 降为参考 outline |
| `A011` | Definition of Ready / Done / Stop-the-line | 让多工具协作有开工门槛和停线门 |
| `A012` | Capture Entry API Semantics | 锁死 `/captures/discover` 的当前语义 |
| `A013` | Worker Receipt & Artifact Ledger Contract | 给 Phase 1A 报账与台账统一协议 |
| `A014` | Platform Adapter Risk Contract | 把平台失败分类 typed 化 |
| `A015` | Raw Response Redaction & Credential Safety | 防止凭据混入 evidence |

## 3. A001 — Authority Chain 修订

### 当前补丁

当前建议把仲裁链改为：

```text
user 最新口头
  > docs/specs/locked-principles.md
  > docs/decision-log.md
  > PRD + amendment
  > SRD
  > Operating Model
  > 历史对话 / agent 记忆
```

### 当前规则

- SRD 是工程规约，不是产品哲学真源
- SRD 可以覆盖 Operating Model 的工程细节
- SRD 不能单方面覆盖 PRD / amendment
- 任何 SRD 与 PRD/amendment 冲突，都必须升级为 amendment 或 user 决策

### 后续需要 patch 的 base SRD 位置

- `docs/SRD-v1-2026-05-02.md` §0.4
- `docs/SRD-v1-2026-05-02.md` §11.F

## 4. A002 — Claude Design 移除

### 当前补丁

- 当前 Tool Roster 中移除 `Claude Design`
- `DESIGN.md` 保留为未来设计 brief 文件，不再绑定特定原型工具
- 当前 UI 方向工作流改为：
  - `Claude Code / VSCode`：IA / 文案 / screenshot critique
  - `Codex Desktop`：后续实现与联调
  - `user`：双屏审阅与拍板

### 当前限制

- 当前任务不实现 `Signal Workbench`
- 当前任务不为 `Phase 2` 建高保真原型依赖

## 5. A003 — Task Index

### 当前补丁

- 当前引入 `docs/task-index.md`
- 当前只允许 `1-3` 个 Active tasks
- 当前 task index 只承担薄账本职责，不承担正式 review 队列职责

### 当前规则

- 任何 Active task 都必须写明 owner、scope、allowed paths、forbidden paths、related PRD/SRD/contract、validation、stop-the-line
- 任务状态变化先写 `docs/task-index.md`
- `docs/current.md` 负责活状态，`docs/task-index.md` 负责任务面

## 6. A004 — `capture_mode` / `quick_capture_preset` 命名统一

### 当前补丁

DB `capture_mode` 仅保留：

```text
metadata_only
audio
video
transcript_only
```

UI / API 便捷字段 `quick_capture_preset` 仅保留：

```text
metadata_only
audio_transcript
```

### 当前规则

- `quick_capture_preset` 不入 DB
- API 在入口层把 `quick_capture_preset` 展开成 `capture_mode + requested_outputs`
- `audio_transcript` 不再作为 DB enum 使用

## 7. A005 — `source_kind` 命名统一

### 当前补丁

当前建议统一：

```text
source_kind:
  manual_url
  capture_plan

created_by_path:
  quick_capture
  capture_plan
  manual_admin
```

### 当前规则

- Phase 1A 仅允许 `source_kind=manual_url`
- Phase 2 才允许 `source_kind=capture_plan`
- `recommendation / keyword / list / raw_gap / agent` 不属于 `capture 创建入口` 的 `source_kind`
- 上述来源应归到 `signal / source_item / origin_kind` 一层，而不是 `/captures/discover` 的入口枚举
- `capture_plan_triggered` 视为旧口径，后续 patch 时全部替换

## 8. A006 — `artifact_assets` 命名残留修正

### 当前补丁

- 当前实体名统一使用 `artifact_assets`
- `media_assets` 只允许作为历史改名记录出现

### 当前需要 patch 的 base SRD 位置

- `docs/SRD-v1-2026-05-02.md` §4.5 `DR-INT-02`
- `docs/SRD-v1-2026-05-02.md` §5.1.3 及相关引用

### 当前规则

- worker、API、contract 文档当前都不再新增 `media_assets` 口径

## 9. A007 — NFR 分级

### 当前补丁

当前把 NFR 分成三层：

- `Hard Gate`
- `Quality Target`
- `Observation Baseline`

### 当前规则

- `LP enforcement`、authority 边界、凭据安全、命名规则、migration 纪律属于 `Hard Gate`
- 覆盖率、type hint、API P95、前端首屏属于 `Quality Target`
- ASR 速度、normalize 耗时、全链路时长、token 成本属于 `Observation Baseline`

### 当前目的

- Phase 1A 先跑通闭环，再用 baseline 驱动优化

## 10. A008 — Tool Roster 更新

### 当前 Tool Roster

| 工具 | 当前角色 | 当前可改范围 | 当前不应做 |
|---|---|---|---|
| `user` | showrunner / final arbiter | 全部拍板层 | 不需要审每个低层细节 |
| `Codex Desktop` | Step0 文档、contract、后续代码主执行 | `docs/` 与后续主线代码 | 当前任务中不写产品代码 |
| `Claude Code / VSCode` | 文档审读、IA/UX 评论、局部说明 | 文档与后续小范围补丁 | 不主导当前代码主线 |
| `ChatGPT Pro` | 外部研究 note | `docs/research/` 证据型输出 | 不改主线事实 |
| `OpenClaw` | 次级 research / scout note | research note | 不直写 authority |
| `Hermes CLI` | 未来调度与 signal 参考 | 设计 note | 当前不抢跑推荐采集 |

## 11. A009 — Tool Roster & Research Note Protocol

### 当前补丁

当前不恢复重治理 review 队列。外部研究统一进入 `docs/research/`。

### 当前文件协议

推荐 frontmatter：

```yaml
title: 题目
date: 2026-05-03
owner_tool: chatgpt-pro
status: note-draft
question: 待回答问题
sources:
  - 来源一
confidence: medium
recommendation: 一句话结论
not_for_change: 当前不应直接改动的范围
needs_user_decision: 仍需拍板的点
```

### 当前规则

- `ChatGPT Pro`、`OpenClaw`、`Hermes` 的研究输出先写成 research note
- research note 可以被主线引用，但不能直接改写主线 contract
- 当前不在项目根建立重治理目录
- 正式 review 队列只保留为 Phase 4 outline

## 12. A010 — Phase Scope Freeze

### 当前候选范围

当前只把以下内容视为候选实现基准：

- Phase 0 bootstrap 文档入口
- Phase 1A Bilibili `manual_url` quick_capture 主路径
- LP baseline
- `artifact_assets` 与 worker receipt baseline
- platform risk 与 raw response 安全 baseline

### 当前仅作参考 outline

- Phase 1B
- Phase 2
- Phase 3
- Phase 4

### 当前禁止抢跑的内容

- `Signal Workbench` 真实实现
- `Capture Plan` UI / runtime 真逻辑
- XHS / YouTube 真实采集
- Hermes 调度
- 正式 Dispatch UI
- 推荐与重排
- 评论链路
- 浏览器自动化

## 13. A011 — Definition of Ready / Done / Stop-the-line

### Definition of Ready

任务进入 `ready` 前至少满足：

1. 已在 `docs/task-index.md` 登记 `Task ID`
2. owner tool 明确
3. scope 明确
4. allowed paths 明确
5. forbidden paths 明确
6. 关联 PRD / SRD / contract 明确
7. validation 明确
8. 当前 Phase 明确
9. 停线条件明确
10. 当前任务不与 Phase Scope Freeze 冲突

### Definition of Done

任务进入 `review` 或 `merged` 前至少满足：

1. 改动已经落文件
2. validation 已执行
3. 没有改 `data/`
4. 没有改 `referencerepo/`
5. 若触碰 contract，已更新 `contracts-index`
6. 若状态变化，已回写 `task-index`
7. 若焦点变化，已回写 `current.md`
8. 已标明当前仍未拍板的点
9. 未引入 Phase 2-4 真实逻辑
10. 未泄露凭据或敏感 response

### Stop-the-line

命中以下任一条件，当前任务立刻转 `blocked`：

1. schema / state words / FS layout / LP 冲突
2. 试图让 `recommendation / keyword / RAW gap` 直接创建 capture
3. raw response、日志或 receipt 带出凭据
4. 试图把 Phase 2-4 逻辑塞进当前任务
5. worker 试图旁路 authority
6. `/captures/discover` 语义被写成 discovery/search
7. platform failure 无 typed 分类
8. 旧 `media_assets` 当前实体名回流

## 14. A012 — Capture Entry API Semantics

### 当前补丁

`POST /captures/discover` 当前保留原路由，但语义锁定为：

```text
capture 创建入口（capture creation entrypoint）
```

它不是：

- source discovery
- recommendation discovery
- search / scan

### 当前允许的入口 payload 形态

手动 quick_capture：

```json
{
  "platform": "bilibili",
  "platform_item_id": "BV1xx",
  "canonical_url": "https://www.bilibili.com/video/BV1xx",
  "source_kind": "manual_url",
  "quick_capture_preset": "audio_transcript"
}
```

未来 capture_plan：

```json
{
  "platform": "bilibili",
  "platform_item_id": "BV1xx",
  "canonical_url": "https://www.bilibili.com/video/BV1xx",
  "source_kind": "capture_plan",
  "capture_plan_id": "01HXPLAN0001",
  "capture_mode": "audio"
}
```

### 当前规则

- Phase 1A 只允许 `manual_url`
- 非 `manual_url` 当前返回 `422`
- quick_capture 不满足条件时返回“走 Scope / 人工判断”，不继续创建

## 15. A013 — Worker Receipt & Artifact Ledger Contract

### 当前补丁

当前把 `docs/specs/worker-receipt-contract.md` 视为 Phase 1A 候选 contract。

### 当前规则

- worker 只报相对路径
- API 负责映射 `artifact_assets`
- raw response 类产物必须声明脱敏字段
- `platform_result` 必须进入 receipt
- `next_status` 必须走 state guard

## 16. A014 — Platform Adapter Risk Contract

### 当前补丁

当前把 `docs/specs/platform-adapter-risk-contract.md` 视为 Phase 1A 候选 contract。

### 当前规则

- 平台失败必须 typed 化为 `platform_result`
- `auth_required`、`rate_limited`、`parser_drift` 等必须分开处理
- 当前不通过浏览器自动化补平台缺口

## 17. A015 — Raw Response Redaction & Credential Safety

### 当前补丁

当前把 `docs/specs/raw-response-redaction.md` 视为 Phase 1A 候选 contract。

### 当前规则

- 凭据不是 evidence
- `raw_api_response` 必须是脱敏后的 response evidence
- receipt、日志、job event 必须带同样的脱敏纪律

## 18. 对 base SRD 的最小机械修补清单

| Patch | Base SRD 位置 | 动作 |
|---|---|---|
| `P-001` | §0.4 | 仲裁链改为 A001 |
| `P-002` | §1.3 / §2.3 / §3.10 / §11.B | 移除 `Claude Design` 当前依赖 |
| `P-003` | §3.5 / §5.1.3 / §8.3 | `quick_capture_preset` / `source_kind` 口径改 A004 / A005 |
| `P-004` | §4.5 | `media_assets` 改 `artifact_assets` |
| `P-005` | §6 / §8.7 | 按 A007 做 NFR 分级 |
| `P-006` | §11.E / §11.F | 加 Step0 范围冻结与边界声明 |

## 19. 当前仍需 user 拍板

- `docs/decision-log.md` 与 `docs/decisions.md` 的最终命名
- quick_capture 当前阈值是否继续保持 `100 MB / 30 min / 50k token`
- `manual_admin` 是否保留在最小 Step0 contract 中
- `auth_required`、`region_blocked`、`vip_required` 对 `source.status` 的最终映射
- Phase 4 是否还保留正式 review 队列设计
