# Raw Response 脱敏与凭据安全规则

> 作用：约束“原始响应证据”在 ScoutFlow 中如何安全落地，避免把凭据、登录态和调试信息误当成 evidence。
> 当前范围：仅服务 Phase 1A 的 Bilibili `manual_url` quick_capture 主路径。

## 1. 核心规则

- 凭据不是 evidence
- 当前保存的 `raw_api_response` 必须是安全后的响应证据，不是完整 HTTP 抓包
- 请求头、cookie jar、本地登录态文件、浏览器 profile 都不进入 artifact ledger

## 2. 当前允许保存的内容

- 已脱敏的 response body JSON
- 安全后的响应元信息，如 `status_code`、安全 header、source URL
- 与产物核验有关的 `sha256`、`bytes`、`mime_type`

## 3. 当前禁止保存的内容

- `Cookie`
- `Authorization`
- `Proxy-Authorization`
- `X-API-Key`
- 完整 cookie jar
- 凭据文件原文
- 登录页截图
- 本地浏览器 profile 导出
- 含敏感 query 参数的原始 URL

## 4. 常见敏感字段处理

| 位置 | 处理 |
|---|---|
| request headers | 整体不落盘 |
| response headers | 仅保留安全字段；`Set-Cookie` 直接移除 |
| response body | 删除或掩码 `token`、`session_id`、`csrf`、`cookie`、`access_key`、`refresh_key` |
| 平台字段 | 已知平台凭据如 `SESSDATA`、`bili_jct`、`DedeUserID` 不落盘 |
| logs / stderr | 做同样的字段级脱敏 |

## 5. 当前 artifact 约束

- `artifact_kind=raw_api_response` 时，`redaction_applied` 必须为 `true`
- `redaction_policy` 当前统一为 `credentials-v1`
- `metadata_json` 至少记录：
  - `redaction_policy`
  - `sensitive_fields_removed`
  - `source_surface`

## 6. 与 Worker Receipt 的联动

receipt 中必须显式声明：

```json
{
  "redaction_applied": true,
  "redaction_policy": "credentials-v1",
  "sensitive_fields_removed": [
    "headers.cookie",
    "headers.authorization",
    "set_cookie",
    "token"
  ]
}
```

若 `raw_api_response` 缺少这些字段，API 必须拒绝写入 ledger。

## 7. 当前日志规则

- job 日志允许保留错误类别、工具版本、时间戳
- job 日志不允许保留凭据值、完整响应头、完整响应体
- stderr 若包含敏感字段，写盘前先脱敏

## 8. 当前审查清单

- raw response 是否只包含安全后的 body / metadata
- `Set-Cookie` 是否已移除
- URL query 中的敏感字段是否已删或掩码
- receipt 是否声明了脱敏策略
- `artifact_assets` 对应条目是否可追溯到 receipt

## 9. 当前禁止

- 把本地凭据文件复制进 `bundle/`
- 为了调试方便直接落完整 response
- 为了复现问题保存登录页或 authenticated browser state
- 在 job_events、日志、stderr 中泄露凭据

## 10. 仅作 Phase 2+ outline

- browsing event payload 的统一脱敏
- 多平台差异化字段清单
- 自动 secret scan 工具化
