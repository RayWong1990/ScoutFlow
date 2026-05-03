# Worker Receipt 与 Artifact Ledger Contract

> 作用：定义 worker 完成一次任务后，如何通过统一 receipt 向 API 报账，并让 API 把产物登记进 `artifact_assets`。
> 当前范围：仅服务 Phase 1A 的 `manual_url` quick_capture 主路径。

## 1. 当前生效范围

- 当前只覆盖 `POST /jobs/{job_id}/complete`
- 当前允许的 FS 六区为：`bundle / media / transcript / normalized / links / logs`
- 当前只要求 Phase 1A 的最小必需产物区：`bundle / media / transcript / normalized / logs`
- `links` 区当前只保留为允许区，真实 RAW link 产物从 `Phase 1B` 起产生
- 当前不定义浏览器事件、版本分支、批量 plan capture 的扩展字段

## 2. 核心原则

- worker 只提交相对路径，不提交绝对路径
- API 负责把 receipt 映射成 `artifact_assets` 行
- `next_status` 由 API 校验，不由 worker 自行决定生效
- raw response 类产物必须声明脱敏信息
- 同一 `dedupe_key` 的重复报账必须可判定为幂等重放

## 3. Receipt 顶层字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `job_id` | string | 是 | 当前 job 主键 |
| `capture_id` | string | 是 | 对应 capture |
| `job_type` | string | 是 | 如 `metadata_fetch` / `audio_extract` / `asr` / `asr_postprocess` |
| `producer` | string | 是 | 逻辑 producer，如 `workers.bili` |
| `producer_version` | string | 是 | producer 版本 |
| `engine` | string | 否 | 底层工具，如 `BBDown` / `yt-dlp` / `ffmpeg` |
| `engine_version` | string | 否 | 底层工具版本 |
| `idempotency.job_attempt` | integer | 是 | 当前重试次数，从 `1` 开始 |
| `idempotency.dedupe_key` | string | 是 | 幂等键 |
| `platform_result` | string | 是 | 取值见 `platform-adapter-risk-contract.md` |
| `produced_assets` | array | 是 | 本次实际生成的产物列表 |
| `logs.job_log_path` | string | 否 | 相对 capture root 或日志根的路径 |
| `logs.stderr_path` | string or null | 否 | stderr 文件路径 |
| `duration_seconds` | number | 否 | 任务耗时 |
| `next_status` | string | 是 | 建议进入的 capture 状态，由 API 最终校验 |

## 4. `produced_assets[]` 字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `zone` | string | 是 | `bundle` / `media` / `transcript` / `normalized` / `links` / `logs` |
| `artifact_kind` | string | 是 | 比 zone 更细的类型，如 `raw_api_response` |
| `relative_path` | string | 是 | 相对 capture root 的路径 |
| `sha256` | string | 是 | 文件校验值 |
| `bytes` | integer | 是 | 文件大小 |
| `mime_type` | string | 否 | MIME 类型 |
| `is_raw_evidence` | boolean | 是 | 是否原始证据 |
| `is_derived` | boolean | 是 | 是否派生产物 |
| `redaction_applied` | boolean | 是 | 是否已脱敏 |
| `redaction_policy` | string or null | 否 | 如 `credentials-v1` |
| `sensitive_fields_removed` | string[] | 条件必填 | `raw_api_response` 时必填，列出已移除的敏感字段 |
| `source_url` | string | 否 | 触发本产物的原始 URL |
| `created_by_job` | string | 是 | 生成该产物的 job_id |

## 5. Phase 1A 最小示例

```json
{
  "job_id": "01HXJOB0001",
  "capture_id": "01HXCAP0001",
  "job_type": "metadata_fetch",
  "producer": "workers.bili",
  "producer_version": "0.1.0",
  "engine": "BBDown",
  "engine_version": "1.6.2",
  "idempotency": {
    "job_attempt": 1,
    "dedupe_key": "bilibili:BV1xx:metadata_fetch"
  },
  "platform_result": "ok",
  "produced_assets": [
    {
      "zone": "bundle",
      "artifact_kind": "raw_api_response",
      "relative_path": "bundle/raw-api-response.json",
      "sha256": "abc123",
      "bytes": 12345,
      "mime_type": "application/json",
      "is_raw_evidence": true,
      "is_derived": false,
      "redaction_applied": true,
      "redaction_policy": "credentials-v1",
      "sensitive_fields_removed": [
        "headers.cookie",
        "headers.authorization",
        "set_cookie",
        "token"
      ],
      "source_url": "https://www.bilibili.com/video/BV1xx",
      "created_by_job": "01HXJOB0001"
    }
  ],
  "logs": {
    "job_log_path": "logs/jobs/metadata-fetch-2026-05-03T034800Z.log",
    "stderr_path": null
  },
  "duration_seconds": 12.5,
  "next_status": "metadata_fetched"
}
```

- Phase 1A 不把 `bundle/metadata.json` 视为已生效 fixed filename
- 如后续需要额外 metadata 文件，必须先走 FS amendment / user 拍板
- 当前 metadata 摘要优先进入 `capture-manifest.json` 或 DB excerpt

## 6. API 校验规则

- `job_id` 与 `capture_id` 必须匹配当前 job 记录
- `relative_path` 必须位于当前 capture root 之下
- `zone` 必须与 `relative_path` 的首目录一致
- 文件必须已存在，且 `sha256` 与 `bytes` 可实测匹配
- `raw_api_response` 一类产物必须 `redaction_applied=true`
- `next_status` 必须经过 state guard 校验，不能跳过 lifecycle
- 同一 `dedupe_key` 的重复 successful receipt 返回幂等成功，不重复插入 ledger

## 7. `artifact_assets` 映射规则

- `capture_id` ← 顶层 `capture_id`
- `artifact_zone` ← `produced_assets[].zone`
- `artifact_kind` ← `produced_assets[].artifact_kind`
- `file_path` ← API 用 capture root 拼出完整相对项目根路径
- `size_bytes` ← `produced_assets[].bytes`
- `sha256` ← `produced_assets[].sha256`
- `producer_job_id` ← 顶层 `job_id`
- `is_raw_evidence` ← `produced_assets[].is_raw_evidence`
- `metadata_json.redaction_applied` ← `produced_assets[].redaction_applied`
- `metadata_json.redaction_policy` ← `produced_assets[].redaction_policy`
- `metadata_json.sensitive_fields_removed` ← `produced_assets[].sensitive_fields_removed`
- `metadata_json.is_derived` ← `produced_assets[].is_derived`
- `metadata_json.source_url` ← `produced_assets[].source_url`
- `metadata_json.created_by_job` ← `produced_assets[].created_by_job`
- `metadata_json.producer` ← 顶层 `producer`
- Phase 1A 即使不扩表，也必须能从 `artifact_assets.metadata_json` 追溯以上字段

## 8. 失败语义

- `422`：payload 合法但产物校验失败
- `409`：job 状态、capture 状态或幂等键冲突
- `503`：文件系统或 ledger 写入失败

## 9. 幂等要求

- API 幂等：由 `job_id + dedupe_key` 判定
- worker 幂等：依赖确定性的 `relative_path`、`sha256` 与 receipt 重放
- 若文件已生成但上次 complete 未成功，本次重放必须不要求重新生成新文件名

## 10. 仅作 Phase 2+ outline

- `versions/` 多版本写入
- browsing event 产物
- capture_plan 批量 capture 的 grouped receipt
- 更细粒度的 partial success 合并策略
