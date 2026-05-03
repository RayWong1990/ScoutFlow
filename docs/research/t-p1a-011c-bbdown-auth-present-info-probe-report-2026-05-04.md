# T-P1A-011C BBDown Auth-Present Metadata Probe Report — 2026-05-04

> 状态：`complete / auth-present metadata evidence captured`。
> 作用：记录在 `T-P1A-011B` local-only auth state 已存在的前提下，对授权 sample URL 执行单次 `BBDown -info` metadata probe 的安全结果。

## 1. Scope

本次只执行：

- external local-only executable/auth store
- repo 外 temp cwd
- 单次 `BBDown -info`
- stdout/stderr redaction
- parser classification

本次未执行：

- media download
- ffmpeg
- ASR
- receipt / artifact ledger
- capture state advancement

## 2. Probe Result

```text
tool_preflight_result=executable_found
tool_preflight_version=1.6.3
platform_boundary_reached=true
platform_result=ok
tool_exit_code=0
```

Parsed fields:

```text
platform_item_id=116493572377107
title=Agent 编排的四种模式：到底谁说了算？| 7 分钟看懂工业级多 Agent 系统｜AI编程实战 #06
duration_seconds=430
page_count=1
selected_page=P1
uploader_name=not_parsed
estimated_media_bytes=not_parsed
```

## 3. Safety Confirmation

- auth store existed before probe: `yes`
- auth store existed after probe: `yes`
- repo-local executable/cwd used: `no`
- temp QR/probe cwd cleaned: `yes`
- media files created in temp tree: `no`
- QR image remained after probe: `no`
- credentials in Git / PR / logs / tracked files: `no`

## 4. Important Implementation Note

执行中发现 `bbdown_info_parser.py` 对真实 `BBDown 1.6.3` 输出有两个直接阻塞：

1. `检测账号登录...` 被误判成 `auth_required`
2. `获取aid结束` / `视频标题` / `P1: ... [07m10s]` / `共计 1 个分P` 这些真实中文行格式没有被提取

因此本任务内补了最小 parser repair 与 contract test，修复后同一次 live probe 得到 `platform_result=ok`。

## 5. Safe Excerpt Summary

安全摘要显示：

- BBDown 成功加载本地 cookie
- 成功获取 aid
- 成功解析视频标题和分P
- 枚举了视频流
- 所有 signed media URL 已被替换为 redacted placeholders

本报告不保留原始 signed URL、cookie、token 或 repo 外 auth path。

## 6. Next Gate

本次 `011C` 只证明：

- auth-present metadata probe 可以在 repo 外 local-only boundary 内安全执行
- 当前 sample URL 在现有 local-only auth state 下可获得 `platform_result=ok` 的 redacted metadata evidence

本次 `011C` 不证明：

- receipt / trust-trace 已打开
- media / ffmpeg / ASR 已批准
- `audio_transcript` 已批准

下一步如果继续，需要 user 明确授权后续 evidence-consumption gate（例如 receipt candidate design / trust-trace mapping），或授权另一个特定 sample URL probe。
