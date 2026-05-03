# T-P1A-011 BBDown No-Auth `-info` Probe Report — 2026-05-04

> 状态：`blocked / tool-preflight-did-not-clear`。
> 文件名沿用 06 dispatch 指定日期；本次实际执行时间为 `2026-05-04`（Asia/Shanghai）。
> 本报告是 redacted local probe report，不是 final authority，不是 BBDown adapter runtime approval，不是 media / audio / ASR approval。

## 1. Scope

User 授权执行 06：只对示范 URL 做一次 no-auth `BBDown -info` probe，且必须先执行 tool preflight。

示范 URL：

```text
https://www.bilibili.com/video/BV19D9eB9Etg/?spm_id_from=333.1007.tianma.3-1-7.click
```

本次执行遵守的硬边界：

- 不登录
- 不扫码
- 不读取 cookie / token / browser profile
- 不下载媒体
- 不运行 ffmpeg
- 不运行 ASR
- 不创建 workers / frontend
- 不调用 `/jobs/{job_id}/complete`
- 不创建 receipt
- 不写 artifact ledger
- 不推进 capture state

## 2. Tool Preflight Result

Preflight 结论：

```text
tool_preflight_result=subprocess_error
tool_preflight_version=not_emitted
path_lookup_BBDown=false
explicit_executable_available=true
```

说明：

- 当前 `PATH` 中未发现 `BBDown`。
- 本机存在一个显式本地 BBDown executable；报告中不持久化本地绝对路径。
- 使用 command array 运行 version preflight，`shell=false`。
- version preflight 使用隔离临时 `HOME` / `XDG_CONFIG_HOME` / `TMPDIR` 和隔离临时 cwd。
- `BBDown --version` 返回非零退出码，因此 preflight 没有 clear。

Version preflight command shape：

```text
[LOCAL_BBDOWN_EXECUTABLE] --version
```

Safe stdout excerpt after redaction：

```text
not_produced
```

Safe stderr excerpt after redaction：

```text
Required argument missing for command: 'BBDown'.
请使用 BBDown --help 查看帮助
```

## 3. URL Canonicalization Summary

URL 静态校验结果：

```text
source_kind=manual_url
platform=bilibili
platform_item_id=BV19D9eB9Etg
credential_query_detected=false
```

因为 tool preflight 未通过，示范 URL 没有传给 BBDown。

## 4. No-Auth `-info` Probe

`-info` 执行结果：

```text
bbdown_info_executed=false
sample_url_used=false
platform_boundary_reached=false
platform_result=not_emitted
parser_classification=not_applicable
redaction_before_parser=not_applicable
```

未执行的 planned command shape：

```text
[LOCAL_BBDOWN_EXECUTABLE] -info --work-dir [ISOLATED_TEMP_WORKDIR] <user-provided-bilibili-url>
```

`PlatformResult` 未产生。原因是 `BBDown -info` 没有运行，未触达 Bilibili 平台边界。`subprocess_error` 只属于 `ToolPreflightResult` 层，不得写成 `PlatformResult.unknown_error` 或任何其他平台结果。

## 5. Typed Result

```json
{
  "task_id": "T-P1A-011",
  "state": "blocked",
  "blocker": "tool_preflight_subprocess_error",
  "tool_preflight": {
    "tool_name": "BBDown",
    "path_lookup_BBDown": false,
    "explicit_executable_available": true,
    "result": "subprocess_error",
    "version": null,
    "safe_diagnostic": "BBDown --version exited with a non-zero status.",
    "safe_stdout_excerpt": "",
    "safe_stderr_excerpt": "Required argument missing for command: 'BBDown'.\n请使用 BBDown --help 查看帮助"
  },
  "url": {
    "provided": true,
    "passed_to_bbdown": false,
    "platform_item_id": "BV19D9eB9Etg"
  },
  "bbdown_info": {
    "executed": false,
    "platform_boundary_reached": false,
    "platform_result_emitted": false,
    "platform_result": null,
    "parser_classification": "not_applicable"
  },
  "safety": {
    "raw_stdout_persisted": false,
    "raw_stderr_persisted": false,
    "receipt_created": false,
    "artifact_ledger_written": false,
    "capture_state_advanced": false,
    "media_download_observed": false,
    "ffmpeg_run": false,
    "asr_run": false,
    "auth_material_used": false,
    "browser_profile_read": false,
    "qr_login_attempted": false
  }
}
```

## 6. Boundary Confirmation

- Media downloaded: `no`
- ffmpeg run: `no`
- ASR run: `no`
- Credential read: `no`
- Cookie / token used: `no`
- Browser profile read: `no`
- QR login attempted: `no`
- Worker created: `no`
- Frontend created: `no`
- Receipt created: `no`
- Artifact ledger written: `no`
- Capture created or state-changed: `no`
- `/jobs/{job_id}/complete` called: `no`
- Raw stdout / stderr persisted: `no`

## 7. Interpretation

本次 06 没有达到 no-auth `-info` probe 阶段。当前 blocker 是本地工具 version preflight 非零退出，不是 Bilibili 平台访问失败、不是 auth_required、不是 forbidden、不是 parser drift。

本报告不能支持以下结论：

- BBDown metadata adapter runtime approval
- `audio_transcript` readiness
- media download approval
- ffmpeg readiness
- ASR readiness
- receipt / artifact ledger approval
- capture state advancement

## 8. Next Gate

下一步若要继续，必须先单独处理 BBDown version/preflight contract：确认当前本地 BBDown executable 的合法 version command，或提供可通过 `BBDown --version` 的 executable。之后如需重新运行 no-auth `-info`，仍需要 user 再次显式批准。
