# Platform Adapter Risk Contract

> 作用：把平台访问失败从“一个通用 failed 字符串”提升为 typed risk contract，便于 API、job 日志和后续 UI 使用统一口径。
> 当前范围：仅服务 Phase 1A 的 Bilibili `manual_url` quick_capture 主路径。

## 1. 当前生效范围

- 当前平台主路径：Bilibili `manual_url`
- 当前允许的技术表面：metadata fetch、`BBDown`、`yt-dlp` fallback、`ffmpeg`
- 当前不做：XHS / YouTube 真采集、评论链路、账号扩展、关键词扩展、浏览器自动化

## 2. 核心原则

- 平台 adapter 是易变边界，不是 authority
- 当前必须把失败分类成 typed `platform_result`
- 若预估信息拿不稳，quick_capture 默认拒绝，不赌执行
- 凭据问题、限流问题、解析漂移问题必须能区分

## 3. `platform_result` 枚举

| `platform_result` | 含义 | 当前处理 |
|---|---|---|
| `ok` | 平台访问与本地工具链成功 | 正常推进 |
| `auth_required` | 凭据缺失、过期或登录态失效 | 停止当前任务，要求人工刷新 |
| `rate_limited` | 平台要求冷却或显式限流 | 不做紧循环重试 |
| `forbidden` | 平台拒绝访问 | 停止当前任务并记录 |
| `not_found` | 条目不存在、已删除或链接无效 | 停止当前 capture |
| `region_blocked` | 地域限制 | 进入人工判断 |
| `vip_required` | 付费或权限限制 | 进入人工判断 |
| `parser_drift` | 工具输出结构变化或解析失败 | 触发停线 |
| `network_error` | 网络抖动 | 可重试 |
| `timeout` | 超时 | 可重试 |
| `unavailable` | 上游服务不可用 | 可重试 |
| `unknown_error` | 无法分类的异常 | 单次重试后人工审查 |

## 4. 候选状态映射（待 user 拍板）

> 本表是当前建议值，不是已锁定 contract；经 user 拍板后才进入 implementation baseline。

| `platform_result` | `jobs` 处理 | `source.status` 建议 | 操作员动作 |
|---|---|---|---|
| `ok` | complete | `ready` | 无 |
| `auth_required` | fail-fast | `manual`，连续失败后 `blocked` | 刷新凭据 |
| `rate_limited` | delay / stop | `blocked` | 等冷却后再试 |
| `forbidden` | fail-fast | `blocked` | 审核权限边界 |
| `not_found` | fail-fast | 保持 `ready` | 检查 URL 本身 |
| `region_blocked` | fail-fast | `manual` | user 决策 |
| `vip_required` | fail-fast | `manual` | user 决策 |
| `parser_drift` | stop-the-line | `blocked` | 新建修复任务 |
| `network_error` | retryable | 保持 `ready` | 自动重试 |
| `timeout` | retryable | 保持 `ready` | 自动重试 |
| `unavailable` | retryable | 保持 `ready` | 自动重试 |
| `unknown_error` | one-retry-then-stop | `manual` | 人工审查日志 |

## 5. 当前重试策略

- `network_error` / `timeout` / `unavailable`：最多 `3` 次，退避 `1s / 5s / 30s`
- `rate_limited`：不做同会话紧循环；必须显式记录冷却原因
- `auth_required` / `forbidden` / `region_blocked` / `vip_required` / `parser_drift`：不自动重试
- `unknown_error`：允许 `1` 次重试；再次失败后转人工

## 6. quick_capture 预估安全门

- 若无法稳定获得媒体大小、时长或风险等级，当前 quick_capture 默认拒绝
- 预估拒绝时，返回“走 Scope / 人工判断”，不继续下载
- 当前不允许通过放宽风险分类来绕过 quick_capture 门槛

## 7. 当前日志与报账要求

- 每次 adapter 失败必须写 `platform_result`
- receipt 与 job event 必须同时携带 `platform_result`
- 若底层工具返回 stderr，日志中保留安全后的错误摘要，不带凭据
- `parser_drift` 必须带最小可诊断上下文，如工具名、版本、异常类别

## 8. 当前禁止

- 通过浏览器自动化补平台缺口
- 未分类错误直接映射成统一 `failed`
- 平台已回 `auth_required` 仍继续重试
- 平台已回 `rate_limited` 仍做短周期轮询

## 9. 仅作 Phase 2+ outline

- XHS / YouTube 的真实 adapter 策略
- comments、sub-comments、account/list source 的风险分层
- 多平台统一冷却窗口调度
- 更细的 operator notification 机制
