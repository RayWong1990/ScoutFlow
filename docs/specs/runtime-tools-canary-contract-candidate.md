---
status: candidate / contract-only
authority: not-authority
task: T-P1A-161
lane: Lane B
updated_at: 2026-05-08
---

# Runtime Tools Canary Contract Candidate

> 这是 `T-P1A-161` 的 contract-only 候选文档。
> 它定义 bounded canary readiness 的结构与红线，不构成 runtime 结论，不构成 ASR 结论。

## 1. Scope

本候选仅覆盖：

- `Bilibili + manual_url`
- tactical route hypothesis=`yt-dlp metadata-first`
- fallback hypothesis=`BBDown fallback-comparator`
- `RuntimeCanaryManifestV1`
- safe stdout/stderr excerpt contract
- repo-external temp root rule
- `PlatformResult` failure classification mapping
- single-route canary readiness checklist

本候选不覆盖：

- live `yt-dlp` / `BBDown` / `ffmpeg` / `Whisper.cpp` / `FunASR`
- media download
- transcript
- batch execution
- browser automation
- DB migration
- vault true write

## 2. Manifest Shape

`RuntimeCanaryManifestV1` 必含以下字段：

| Field | Contract |
|---|---|
| `manifest_version` | 固定 `RuntimeCanaryManifestV1` |
| `lane_id` | 固定 `Lane B` |
| `task_id` | 固定 `T-P1A-161` |
| `source_family` | 固定 `bilibili` |
| `source_kind` | 固定 `manual_url` |
| `route_hypothesis` | 固定 `yt-dlp metadata-first` |
| `fallback_hypothesis` | 固定 `BBDown fallback-comparator` |
| `tool_execution_status` | `not_executed` / `preflight_only` / `future_approved_run` |
| `repo_external_temp_root` | 必须在 ScoutFlow repo 外 |
| `network_used` | 本 dispatch 默认 `false` |
| `media_downloaded` | 本 dispatch 默认 `false` |
| `raw_stdout_tracked` | 本 dispatch 默认 `false` |
| `raw_stderr_tracked` | 本 dispatch 默认 `false` |
| `credential_material_seen` | 本 dispatch 默认 `false` |
| `safe_stdout_excerpt_path` | 可空；若存在必须指向脱敏后 tracked fixture |
| `safe_stderr_excerpt_path` | 可空；若存在必须指向脱敏后 tracked fixture |
| `platform_result` | 运行前可空；未来运行时必须复用既有 `PlatformResult` |
| `failure_classification_reason` | 运行前默认 `not_executed_by_dispatch_boundary` |
| `remaining_holds` | 保留当前 hold truth |
| `human_runtime_gate_required` | 本 dispatch 固定 `true` |

## 3. Conservative Defaults

本 dispatch 写出的默认值必须保持保守：

| Field | Required value |
|---|---|
| `tool_execution_status` | `not_executed` |
| `network_used` | `false` |
| `media_downloaded` | `false` |
| `raw_stdout_tracked` | `false` |
| `raw_stderr_tracked` | `false` |
| `credential_material_seen` | `false` |
| `human_runtime_gate_required` | `true` |
| `platform_result` | `null` |
| `failure_classification_reason` | `not_executed_by_dispatch_boundary` |

## 4. Safe Excerpt Contract

只有满足全部条件，excerpt 才允许进入 tracked fixture：

- 先脱敏，再持久化
- 只保留短 diagnostic 片段，不保存 raw stdout/stderr
- 不含 cookie header
- 不含 `Authorization` / `Proxy-Authorization`
- 不含 token / signed URL / auth query residue
- 不含 local auth path / browser profile path
- 记录 `failure_classification_reason`
- 若无法证明安全，则不创建 excerpt

当前 fixture 仅作为 contract sample：

- `tests/fixtures/runtime_tools/safe_stdout_excerpt.txt`
- `tests/fixtures/runtime_tools/safe_stderr_excerpt.txt`

## 5. Repo-external Temp Rule

未来任何 runtime temporary output 都必须放在 repo 外，例如 `/tmp/scoutflow-runtime-tools`。
以下路径恒为非法 temp root：

- `ScoutFlow/**`
- `ScoutFlow/data/**`
- `ScoutFlow/referencerepo/**`

tracked 路径中只能保留：

- sanitized manifest
- sanitized excerpt fixture

## 6. Failure Classification Mapping

future run 若发生 platform-boundary failure，必须复用既有 `PlatformResult`：

| Stop-line family | `PlatformResult` mapping |
|---|---|
| credential missing / expired | `auth_required` |
| rate limit / risk control | `rate_limited` |
| forbidden | `forbidden` |
| not found / deleted | `not_found` |
| region limit | `region_blocked` |
| VIP / paid gate | `vip_required` |
| parser drift / output shape drift | `parser_drift` |
| timeout | `timeout` |
| network issue | `network_error` |
| upstream unavailable | `unavailable` |
| uncategorized failure | `unknown_error` |

tool preflight 本身仍是独立 contract，不冒充 `PlatformResult`。

## 7. Single-route Readiness Checklist

- source family 固定 `bilibili`
- source kind 固定 `manual_url`
- tactical route 仍是 hypothesis，不是 promotion
- fallback route 仍是 comparator hypothesis
- no live run
- no media download
- no transcript / ASR
- no raw stdout/stderr tracked
- no credential material in tracked files
- repo-external temp root 已定义
- human runtime gate 仍为 required

## 8. Stop-lines

出现以下任一情况即停线：

- 任何 live `yt-dlp` / `BBDown` / `ffmpeg` / `Whisper.cpp` / `FunASR`
- 任何 source URL 被直接写进 fixture
- 任何 raw stdout/stderr 被跟踪
- 任何 cookie / token / auth material 被写入 tracked 文件
- 任何 batch / browser automation / migration / vault true write 扩 scope
- 任何把 tactical route 写成 promotion 或已落地结论的文案

## 9. Current Boundary

当前 lane 仅产出 gate-readiness contract material。

- not runtime conclusion
- not ASR conclusion
- no live run
- no media download
- no raw stdout/stderr tracked
- tactical route remains hypothesis
