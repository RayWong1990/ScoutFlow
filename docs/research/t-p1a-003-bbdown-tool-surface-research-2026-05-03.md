---
title: BBDown tool-surface research for ScoutFlow Phase 1A
date: 2026-05-03
status: note-draft
owner_tool: codex-dispatch-c
not_authority: true
not_implementation_approval: true
not_for_change:
  - services/**
  - workers/**
  - apps/**
  - runtime capture
question: How should ScoutFlow evaluate BBDown as a future external adapter without approving runtime capture?
confidence: medium
recommendation: Phase 1A should not run BBDown next; build the API receipt endpoint and redaction scanner first, then open a separate wrapper task if approved.
---

# T-P1A-003 BBDown Tool-Surface Research

> 本 note 是 sidecar research，不是 authority，不是 implementation approval。它不批准 BBDown runtime、真实下载、ASR、workers、frontend、cookies、token、Authorization、浏览器 profile、真实 Bilibili URL 访问或 `audio_transcript` 执行。

## 0. 本次边界

本文件只写入 `docs/research/**`。本轮没有修改 `docs/current.md`、`docs/task-index.md`、`docs/decision-log.md`，也没有创建 `docs/specs/bbdown-adapter-contract-draft.md`。

读取并对齐的 ScoutFlow 本地 contract：

| 文件 | 本 note 使用方式 |
|---|---|
| `AGENTS.md` | 确认 `T-P1A-003` 只能做 research / draft proposal，不做 runtime |
| `docs/current.md` | 确认 Phase 1A 当前禁止 BBDown / yt-dlp / ffmpeg 真运行、禁止 worker runtime |
| `docs/task-index.md` | 确认本任务 allowed path 为 `docs/research/**` |
| `docs/specs/contracts-index.md` | 确认 research note 不能直接升级为主线 contract |
| `docs/specs/platform-adapter-risk-contract.md` | 复用 `platform_result` 分类口径 |
| `docs/specs/worker-receipt-contract.md` | 未来 BBDown 只能经 receipt / artifact ledger 报账 |
| `docs/specs/raw-response-redaction.md` | 凭据不是 evidence，raw output 必须先脱敏 |
| `docs/SRD-v1.1-amendment-2026-05-03.md` | 对齐 A009 research note protocol、A010 scope freeze、A013-A015 安全补丁 |

## 1. Public Primary Sources

本轮只用 BBDown public primary sources；没有运行 BBDown，没有访问真实 Bilibili URL，没有下载媒体。

| Source | Evidence used |
|---|---|
| [nilaoda/BBDown README](https://github.com/nilaoda/BBDown) | CLI 表面：`-info`、`--audio-only`、`--work-dir`、`--ffmpeg-path`、`--mp4box-path`、`--cookie`、`--access-token`、`--debug`、`serve`；外部 `ffmpeg` / `mp4box` 依赖；个人学习研究与合法授权提示 |
| [BBDown releases](https://github.com/nilaoda/BBDown/releases) | Latest release `1.6.3`，published `2024-08-14`; release note 包含 Cookie 转义、TV parser、互动视频、EP/SS ID parser 相关变化 |
| [json-api-doc.md](https://github.com/nilaoda/BBDown/blob/master/json-api-doc.md) | `serve` 的 `/get-tasks/*`、`/add-task`、`/remove-finished*`；`/add-task` 成功为 `200 OK`；单任务取消与并发限制限制说明 |
| [BBDown/MyOption.cs](https://github.com/nilaoda/BBDown/blob/master/BBDown/MyOption.cs) | Future wrapper 可见字段：`OnlyShowInfo`、`AudioOnly`、`SkipSubtitle`、`SkipCover`、`Cookie`、`AccessToken`、`WorkDir`、`FFmpegPath`、`Mp4boxPath`、`Debug` |
| [BBDown/BBDownApiServer.cs](https://github.com/nilaoda/BBDown/blob/master/BBDown/BBDownApiServer.cs) | `serve` 的 in-memory task lists、broad CORS、HTTP-only URL validation、async task add、`DownloadTask.SavePaths` |
| [Issue #1071](https://github.com/nilaoda/BBDown/issues/1071) | `-info` stdout 可出现 `upos-*` / media URL 与 signed query 参数，同时出现未登录提示和 403 complaint |
| [Issue #1091](https://github.com/nilaoda/BBDown/issues/1091) | 新 BV shape / parser drift signal |
| [Issue #1094](https://github.com/nilaoda/BBDown/issues/1094) | Login / local cookie / auth friction signal |
| [Issue #1046](https://github.com/nilaoda/BBDown/issues/1046) | ffmpeg merge / member-content / toolchain failure signal |
| [Issue #854](https://github.com/nilaoda/BBDown/issues/854) | `serve` `/add-task` 不直接返回 AID 的 ergonomics gap |
| [Issue #790](https://github.com/nilaoda/BBDown/issues/790) / [Issue #804](https://github.com/nilaoda/BBDown/issues/804) | `serve` command usage and task queue concern signals |

补充取证：GitHub API 显示 `master` inspected commit 为 `259a5558cee0a349a7ebb60bd31e40c88e5bc1ed`，committer date `2026-01-10T14:15:14Z`。这只用于标记本次 source snapshot，不是 ScoutFlow authority。

## 2. Q1: `BBDown -info` 对 `metadata_only` / `metadata_fetch` 是否可用？

结论：可作为未来 `metadata_fetch` external adapter probe 的候选，但 Phase 1A 下一步不应直接运行 BBDown。

BBDown README 把 `-info, --only-show-info` 定义为“仅解析而不进行下载”。这对 ScoutFlow 的 `metadata_only` 方向有价值，因为它可能给出：

- tool version 与运行提示。
- login / cookie 检测状态。
- `aid` / BV 解析结果。
- 标题、发布时间、UP 相关字段。
- 分 P 列表、单 P 时长。
- 可用视频流、音频流、编码、码率、估算体积。

但它不能被当成稳定、安全的 raw evidence：

- stdout 是人类可读日志，不是稳定 JSON contract。
- Issue #1071 证明 `-info` 输出可能打印 temporary media URL 和 signed query 参数。
- 登录检查、cookie 加载、本地路径、debug 信息都可能进入 stdout/stderr。
- 输出结构受 parser、API、release 变化影响；Issue #1091 是 parser drift 风险信号。

ScoutFlow 草案处理方式：

| Surface | Draft treatment |
|---|---|
| `metadata_only` UI / API intent | 仍由 ScoutFlow API authority 判定，不由 BBDown 判定 |
| `metadata_fetch` job | 未来可把 `BBDown -info` 作为 external adapter，必须另开任务 |
| stdout/stderr | 不保存原文；只保存 redacted excerpt 和 typed extracted fields |
| parser failure | 映射 `parser_drift`，停线，不静默降级 |
| unsafe URL/token residue | redaction 失败时不得写 receipt / ledger |

## 3. Q2: 未来 `--audio-only` 的边界、输出文件、`ffmpeg` / `mp4box` 关系

结论：`--audio-only` 只属于未来 `audio_transcript` runtime；本 note 不批准它。

BBDown README 暴露 `--audio-only`、`--work-dir`、`--ffmpeg-path`、`--mp4box-path`、`--skip-subtitle`、`--skip-cover`。README 同时说明普通视频混流需要外部 `ffmpeg` 或 `mp4box`。Release `1.5.3` 说明开启 `--audio-only` 时输出文件会改为 `m4a` 格式。

未来若 user 明确批准 `audio_transcript` runtime，建议 command shape 只能是 proposal：

```text
BBDown --audio-only --work-dir <job_temp_dir> --ffmpeg-path <approved_ffmpeg_path> --skip-subtitle --skip-cover <manual_url>
```

边界建议：

- `--audio-only` 不得作为 `metadata_only` 的副作用。
- `--work-dir` 必须是 per-job isolated temp dir；receipt 只能提交相对路径，不能提交本机绝对路径。
- `ffmpeg` / `mp4box` path 必须显式探测并记录版本；缺失时不能继续。
- 默认 `--skip-subtitle` / `--skip-cover`，除非后续 contract 批准字幕或封面 artifact kind。
- 默认不启用 `--debug`；debug 输出风险高，可能包含 headers、raw JSON、本地路径、temporary URL。
- cookies/tokens 不得通过 shell command string 传递；secret injection 必须等 `T-P1A-004` 或后续安全任务定义后再做。

## 4. Q3: 为什么首版不采用 `BBDown serve`

结论：首版不采用 `BBDown serve` 作为队列或 runtime。

Primary source 风险：

- README 暴露 `serve` server mode，但这只是 BBDown 自身 server，不是 ScoutFlow authority。
- `json-api-doc.md` 显示 `/add-task` 成功返回 `200 OK`，并不返回 ScoutFlow receipt-shaped result。
- `json-api-doc.md` 明确单个下载任务当前没有好方法取消。
- `json-api-doc.md` 明确 server 目前没有并发任务数量限制。
- `BBDownApiServer.cs` 使用内存中的 `runningTasks` / `finishedTasks`，状态不在 ScoutFlow DB/FS authority 内。
- `BBDownApiServer.cs` 配置 `AllowAnyOrigin`、`AllowAnyMethod`、`AllowAnyHeader`。
- `BBDownApiServer.cs` 只接受 `http` listener URL；需要 HTTPS 时要求另配 reverse proxy。
- Issue #854 要求 `/add-task` 返回 AID，说明当前 server ergonomics 对外部 job tracking 不够直接。
- Issue #804 提到 API queue concern，说明把它当首版队列层会放大不确定性。

ScoutFlow 更合适的首版形态是：

```text
short-lived subprocess
  -> explicit timeout
  -> isolated temp workdir
  -> captured stdout/stderr
  -> mandatory redaction
  -> typed platform_result
  -> API receipt endpoint
  -> artifact ledger
```

## 5. Q4: BBDown failure / stderr / issue patterns 到 `platform_result` 的草案映射

以下为 proposal only，不是 contract 变更。

| BBDown signal | Draft `platform_result` | Treatment |
|---|---|---|
| exit code `0`; required fields parsed; redaction success | `ok` | 仍只写 typed fields 和 redacted excerpt |
| 未登录、cookie 缺失/过期、token 缺失/过期、login timeout | `auth_required` | 不自动刷新凭据；人工处理 |
| 风控、冷却、anti-abuse、短期重复限制 | `rate_limited` | 不做紧循环 retry |
| HTTP 403 / Forbidden，且无明确 auth 缺失证据 | `forbidden` | fail-fast；保留安全摘要 |
| 条目不存在、删除、无效 ID、无效分 P | `not_found` | fail-fast；人工核 URL |
| 地区不可用、area/intl 限制 | `region_blocked` | 人工决策 |
| VIP、付费、课程、大会员权限不足 | `vip_required` | 不绕过 |
| expected field 缺失、BV shape 解析失败、output layout 改变、parse exception | `parser_drift` | stop-the-line |
| DNS/TLS/connect reset/proxy transient | `network_error` | 可按现有 contract 重试 |
| subprocess timeout | `timeout` | 可按现有 contract 重试 |
| upstream 5xx 或服务不可用 | `unavailable` | 可按现有 contract 重试 |
| nonzero exit 且无法分类 | `unknown_error` | 单次 retry 后人工审查 |

分类优先级：

- 同一次运行同时出现 auth wording 和 403 时，默认 `auth_required`；只有确认登录态有效且仍被拒绝时才用 `forbidden`。
- parser 结构变化优先 `parser_drift`，不能压成 `unknown_error`。
- redaction 失败不是 `ok`；即使 metadata parse 成功，也不得写入 receipt / ledger。

## 6. Q5: 强制脱敏清单

以下字段、材料或位置不得进入 repo、DB、artifact ledger、job events、stdout/stderr artifact 或 PR description：

- `Cookie`
- `Set-Cookie`
- `Authorization`
- `Proxy-Authorization`
- `X-API-Key`
- `SESSDATA`
- `bili_jct`
- `DedeUserID`
- `token`
- `access_token`
- `refresh_key`
- `csrf`
- `auth_key`
- `signed media URL`
- `upos-*` / `bilivideo.com` media URL
- media URL query parameters such as `deadline`, `upsig`, `trid`, `uparams`, `mid`, `oi`, `buvid`
- browser profile path
- local absolute path containing username, credential file path, or app data path
- full debug logs
- raw HTTP headers
- raw response body that has not passed `credentials-v1`

允许保存的最小形态：

- typed extracted fields。
- `safe_stdout_excerpt` / `safe_stderr_excerpt`，且只在 redaction success 后保存。
- `redaction_applied=true`。
- `redaction_policy=credentials-v1`。
- `sensitive_fields_removed` 明确列出移除项。

## 7. Q6: 未来 adapter model / function names 草案

以下全部是 proposal only；不是 implementation approval，不是 services change。

```python
class BBDownToolProbeResult:
    tool_name: str
    tool_version: str | None
    available: bool
    platform_result: PlatformResult
    safe_stdout_excerpt: str | None
    safe_stderr_excerpt: str | None


class ExternalToolRunResult:
    tool_name: str
    tool_version: str | None
    command_shape: str
    exit_code: int | None
    duration_seconds: float
    timed_out: bool
    platform_result: PlatformResult
    safe_stdout_excerpt: str | None
    safe_stderr_excerpt: str | None
    redaction_applied: bool
    redaction_policy: str
    sensitive_fields_removed: list[str]


class BilibiliMetadataProbeResult:
    platform_item_id: str
    title: str | None
    duration_seconds: int | None
    estimated_media_bytes: int | None
    page_count: int | None
    selected_page: str | None
    uploader_name: str | None
    uploader_id: str | None
    stream_summary: list[dict[str, str | int | None]]
    platform_result: PlatformResult
    redaction_applied: bool


class BilibiliAudioProbePlan:
    platform_item_id: str
    selected_page: str | None
    expected_audio_bytes: int | None
    expected_duration_seconds: int | None
    command_shape: str
    platform_result: PlatformResult
```

```python
def probe_bbdown_version(timeout_seconds: int) -> BBDownToolProbeResult: ...

def run_bbdown_info(manual_url: str, timeout_seconds: int) -> ExternalToolRunResult: ...

def parse_bbdown_info_output(result: ExternalToolRunResult) -> BilibiliMetadataProbeResult: ...

def classify_bbdown_failure(
    exit_code: int | None,
    safe_stdout: str,
    safe_stderr: str,
) -> PlatformResult: ...

def build_bbdown_audio_plan(
    metadata: BilibiliMetadataProbeResult,
) -> BilibiliAudioProbePlan: ...
```

后续实现约束草案：

- 复用现有 `PlatformResult` enum；不得另起平行 enum。
- `producer -> adapter -> parser -> redactor -> receipt` 保持分层。
- 先做 sanitized fixture parser，再考虑 live `-info`。
- parser drift 是 stop-the-line。
- receipt 只提交相对路径。
- external adapter tool 不拥有 authority。

## 8. Suggested State Machine

BBDown wrapper 如后续获批，建议至少四态并带 gate：

```text
not_configured
  -> tool_available
  -> metadata_probe_ready
  -> metadata_probe_ok
  -> receipt_candidate
  -> api_ledger_written
```

Transition gates:

- `not_configured -> tool_available`: future `BBDown --version` probe succeeds without real URL。
- `tool_available -> metadata_probe_ready`: user approves metadata probe for Bilibili `manual_url`。
- `metadata_probe_ready -> metadata_probe_ok`: `-info` exits `0`，parser extracts required fields，redaction succeeds。
- `metadata_probe_ok -> receipt_candidate`: mapped to typed `platform_result`，no unsafe raw output retained。
- `receipt_candidate -> api_ledger_written`: `T-P1A-002` receipt endpoint validates and writes ledger。

## 9. Rejected First-Version Choices

| Choice | Verdict | Reason |
|---|---|---|
| Run BBDown directly in Phase 1A next step | reject | 先缺 API receipt endpoint 与 redaction scanner foundation |
| Use `BBDown serve` as ScoutFlow queue/runtime | reject | 状态、并发、取消、CORS、HTTP-only、receipt shape 都不匹配 |
| Save full `-info` stdout | reject | Issue #1071 shows media URL / signed query risk |
| Pass cookies/tokens through command string | reject | 容易进入 process list、shell history、logs、debug output |
| Use `--audio-only` under `metadata_only` | reject | 越过当前 scope freeze |
| Treat all failures as `unknown_error` | reject | 丢失 auth / forbidden / parser drift / VIP 等关键分类 |

## 10. Conclusion And Recommendation

结论建议保持如下：

1. Phase 1A 下一步不直接运行 BBDown。
2. 先用 `T-P1A-002` API receipt endpoint + `T-P1A-004` redaction scanner 建基础。
3. BBDown wrapper / runtime 必须另开任务，并且只能作为 external adapter tool，不是 authority。
4. 首版不采用 `BBDown serve` 作为队列或 runtime。
5. 本 note 中的 adapter model / function names 全部是 proposal only；若要提升为 draft spec，需要主写入 agent 另行同步 `docs/specs/contracts-index.md` 并取得 user 拍板。
