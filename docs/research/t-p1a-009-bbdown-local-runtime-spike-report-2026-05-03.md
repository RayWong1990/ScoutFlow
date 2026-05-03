# T-P1A-009 BBDown Local Runtime Spike Report — 2026-05-03

> 状态：`report candidate / local-only runtime spike evidence`。
> 权限边界：本文不是 final authority，不是正式 adapter runtime approval，不是 `audio_transcript` approval。

## 1. Task Boundary

`T-P1A-009` 只验证本地 BBDown runtime 最小可用性，允许范围限定为：

- `BBDown --version`
- 如当前会话 user 提供公开 Bilibili URL 并批准 no-auth probe，则一次 `BBDown -info <user_provided_public_url>`

本任务明确不批准：

- media download
- ffmpeg
- ASR
- credentials / cookie / token / browser profile
- workers
- frontend
- artifact / receipt / capture state change
- `/jobs/{job_id}/complete`
- `audio_transcript` runtime

## 2. User Approval Record Summary

当前 Codex 会话中，user 明确批准 `T-P1A-009` 进行本地 BBDown runtime spike，并限定：

- 只允许 `BBDown --version`
- 如 user 提供公开 Bilibili URL，才允许一次 `BBDown -info` no-auth metadata probe
- 不允许下载媒体
- 不允许运行 ffmpeg
- 不允许运行 ASR
- 不允许读取 cookie / token / browser profile
- 不允许提交任何本地 runtime 原文产物

user 同时提供了一个 Bilibili `www.bilibili.com/video/<BV>/` URL。执行时先进行 tool availability preflight；由于 preflight 未通过，未执行 `-info`，该 URL 未被传给 BBDown。

## 3. Local Environment Minimum Info

- Repo branch: `task/T-P1A-009-bbdown-local-runtime-spike`
- Base gate: latest `origin/main`
- PR `#14`: merged, merge commit `014e37a11427922c52d35b56c3962110d3711d17`
- PR `#17`: merged, merge commit `0cfcef58533bba1902eec6ed19a3f7fbed308a64`
- Runtime wrapper posture: in-memory subprocess capture with temporary `HOME` and temporary working directory outside the repo
- Raw stdout/stderr persistence: none

## 4. BBDown Availability

- BBDown available: `no`
- BBDown version: `not available`
- Version preflight result: executable lookup failed before BBDown launched
- Safe stdout excerpt: `not produced`
- Safe stderr excerpt: `not produced`

Diagnostic summary:

```text
BBDown executable was not found in the current PATH during the allowed version preflight.
```

No BBDown stdout/stderr was produced because the executable did not launch.

## 5. No-auth `-info` Probe

- Executed `-info`: `no`
- Reason: `BBDown --version` availability preflight failed because `BBDown` was not found in current PATH
- User URL status: provided, but not used after tool availability failure
- Public / no-auth / non-paid confirmation: not probed; no-auth probe did not run

Since `-info` was not executed:

- `PlatformResult`: `not emitted`
- Reason: `BBDown -info` did not run, so no platform boundary was reached.
- `tool_preflight_result`: `executable_not_found`
- parser success: `not assessed`
- required fields present: `not assessed`
- `blocks_quick_capture`: `true` by operational policy, because no platform metadata was obtained

## 6. Redaction Result

- Redaction applied to BBDown stdout/stderr: `not_applicable`
- Reason: BBDown produced no stdout/stderr
- Raw stdout/stderr committed to Git: `no`
- Signed media URL observed: `no`
- temporary media URL observed: `no`
- URL query secret observed: `no`
- Cookie / Authorization / SESSDATA / bili_jct / DedeUserID / token observed: `no`
- Browser profile path observed: `no`

No redaction failure was observed. The stronger finding is that no BBDown output existed to persist or report.

## 7. Boundary Confirmation

- Media downloaded: `no`
- ffmpeg run: `no`
- ASR run: `no`
- Credential read: `no`
- Cookie jar read: `no`
- Browser profile read: `no`
- Worker created: `no`
- Artifact created: `no`
- Receipt created: `no`
- Capture created or state-changed: `no`
- `/jobs/{job_id}/complete` called: `no`

## 8. Interpretation

This spike did not reach the Bilibili platform boundary. The current blocker is local tool availability, not URL access, auth, parser drift, or platform policy.

Because BBDown was not found in PATH, this report cannot support:

- BBDown metadata adapter runtime approval
- `audio_transcript` readiness
- ffmpeg readiness
- ASR readiness
- formal wrapper approval
- capture state advancement

## 9. Next Recommended Gate

Recommended next step:

- Add a separate BBDown tool-path readiness gate or rerun `T-P1A-009` after user confirms where the BBDown executable is installed.
- If a wrapper hardening task is opened, map executable-not-found into an explicit tool-preflight result before any platform URL probe.
- Do not open `T-P1A-010 audio_transcript readiness gate` until BBDown tool availability and one no-auth metadata probe have produced redacted, parser-classified evidence.

This recommendation is only a next-gate suggestion. It is not final authority and does not approve media, ffmpeg, ASR, workers, artifacts, receipts, capture state changes, or broader adapter runtime.
