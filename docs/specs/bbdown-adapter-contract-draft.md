# BBDown Adapter Contract Draft

> 状态：`draft / review candidate`。
> 权限警告：本文不是 final authority，不是 implementation approval，也不是 runtime approval。
> 范围：仅服务 `T-P1A-006`；从 `docs/research/t-p1a-003-bbdown-tool-surface-research-2026-05-03.md` 提炼 BBDown adapter draft spec。

## 0. Status / Scope / Non-authority warning

本文是未来 Bilibili `manual_url` adapter 的候选 contract 草案。它可以作为后续任务的输入，但不授权以下事项：

- 运行 BBDown
- 运行 yt-dlp
- 运行 ffmpeg
- 运行 ASR
- 下载媒体
- 创建 `workers/**`
- 创建或修改 frontend
- 读取 browser profile
- 将 cookie、token、凭据、未脱敏 stdout/stderr 或本地 auth 材料写入 Git、PR、CI、logs、DB rows 或 tracked artifacts

对齐来源：

| Source | 本 draft 的使用方式 |
|---|---|
| `docs/research/t-p1a-003-bbdown-tool-surface-research-2026-05-03.md` | BBDown tool-surface research snapshot |
| `docs/specs/platform-adapter-risk-contract.md` | 复用现有 `PlatformResult` enum 与 retry 口径 |
| `docs/specs/worker-receipt-contract.md` | 将未来 adapter 输出映射到 receipt / artifact ledger |
| `docs/specs/raw-response-redaction.md` | 继承凭据与 raw response 安全规则 |
| `docs/archive/PRD-v1.1-amendment-2026-05-02.md` | 对齐 LP-001 quick_capture 边界 |
| `docs/archive/SRD-v1.1-amendment-2026-05-03.md` | 对齐 Phase scope freeze、`source_kind`、`artifact_assets` 与 `POST /captures/discover` 语义 |

已吸收的用户口径：

- BBDown 是当前偏好的 Bilibili 主 adapter 候选。
- BBDown / ffmpeg / ASR 未来可以引入，但必须分阶段、有 gate 推进。
- 这是个人本地开发，不是 SaaS；隐私合规风险按项目形态视为低。
- 隐私风险低不等于凭据边界放松：secret 仍不得进入 Git、PR、CI、logs、DB artifacts 或 tracked files。
- 首版 runtime 不采用 `BBDown serve`。
- 后续首版 runtime 候选形态优先 short-lived subprocess，而不是 long-running server。
- 本文只是 draft，不批准 runtime。

## 1. Why BBDown

BBDown 适合作为 Bilibili adapter 候选，原因是 research note 已确认它提供了直接面向 Bilibili URL 的 CLI surface：

- `-info` / `--only-show-info` 后续可作为 no-auth public metadata probe 候选。
- `--audio-only` 可以保留给未来 audio path，但必须等 user 明确批准。
- `--work-dir`、`--ffmpeg-path` 等参数有助于设计 per-job isolation 与 dependency preflight。
- BBDown issue patterns 暴露出的风险能落到 ScoutFlow 现有 contract：auth gap、parser drift、forbidden、ffmpeg failure、unsafe stdout/stderr residue。

本文把 BBDown 定位为 platform boundary 上的 external tool。ScoutFlow authority 仍在 API contract、receipt、state guard、redaction 与 artifact ledger。

## 2. Non-goals

本文不定义、不批准：

- live BBDown execution
- media download
- audio extraction
- ASR
- `audio_transcript` runtime
- browser automation
- browser profile reading
- `BBDown serve`
- persistent adapter queue
- auth refresh automation
- 通过 shell command string 传 cookie 或 token
- `services/**`、`workers/**`、`apps/**`、`packages/**`、`tests/**` 的代码变更
- Phase 2-4 runtime logic
- 让 `recommendation / keyword / RAW gap` 直接创建 capture 的任何路径

## 3. Adapter layering

未来实现必须把 BBDown 保持为可替换的 subprocess adapter，而不是 authority：

```text
BBDown subprocess adapter
  -> stdout/stderr capture
  -> redaction
  -> parser
  -> PlatformResult classifier
  -> receipt candidate
  -> POST /jobs/{job_id}/complete
  -> artifact_assets ledger
```

后续实现任务至少应遵守以下 state machine：

```text
not_configured
  -> tool_available
  -> metadata_probe_ready
  -> metadata_probe_parsed
  -> receipt_candidate
  -> api_ledger_written
```

Transition gates：

| Transition | Required gate |
|---|---|
| `not_configured -> tool_available` | 未来 tool-version preflight 成功，且不触碰真实 Bilibili URL |
| `tool_available -> metadata_probe_ready` | user 明确批准后续 no-auth metadata probe task |
| `metadata_probe_ready -> metadata_probe_parsed` | BBDown output 已 capture、redact，并解析成 required typed fields |
| `metadata_probe_parsed -> receipt_candidate` | parser 映射 typed `platform_result`；不保留 unsafe raw output |
| `receipt_candidate -> api_ledger_written` | `POST /jobs/{job_id}/complete` 校验 paths、hashes、redaction metadata 与 `next_status` |

## 4. Command surface

下表只是后续 gated task 的 proposal surface；`T-P1A-006` 不运行这些命令。

| Surface | Candidate shape | 当前状态 |
|---|---|---|
| Tool preflight | `BBDown --version` | Future preflight only；不传真实 URL |
| No-auth metadata probe | `BBDown -info --work-dir <job_temp_dir> <manual_url>` | 后续如获批准，优先作为首个 live adapter 方向 |
| Future audio extraction | `BBDown --audio-only --work-dir <job_temp_dir> --ffmpeg-path <approved_ffmpeg_path> --skip-subtitle --skip-cover <manual_url>` | 未批准；属于后续 audio task |
| Server mode | `BBDown serve ...` | 首版 runtime reject |
| Debug mode | `BBDown --debug ...` | 默认 reject；泄露风险高 |
| Command-string auth | `--cookie ...` / `--access-token ...` | 默认 reject；除非后续单独批准并证明不泄露 |

后续 command builder 规则：

- 用 command array，不做 shell interpolation。
- log 只能记录 command shape，不记录 credential values。
- `manual_url` 必须来自 LP-001 允许的 user 单条粘贴 URL 路径。
- stdout/stderr 在 redaction 成功前只能停留在内存或 temp file。
- redaction 前不得把 stdout/stderr 写入 tracked artifacts。
- metadata-only 路径不得产生 media output。

## 5. Auth policy

| Mode | Draft recommendation | Current authority |
|---|---|---|
| No-auth public metadata | 候选首版 adapter path | 可设计；本任务不批准运行 |
| Manual-auth local-only | 未来可设计本地个人使用 | 需要后续明确 contract |
| Auth refresh automation | Out of scope | 不进入 Phase 1A active tasks |
| Cookie/token in command string | 默认禁止 | 后续例外必须有显式批准和不泄露证明 |
| Browser profile reading | 默认禁止 | 当前 scope 不允许 |

Credential policy：

- credentials are not evidence。
- credentials 不得进入 Git、PR、CI、logs、tracked files、DB artifacts、receipt payloads 或 job events。
- local manual-auth design 必须把 auth material 放在 ScoutFlow tracked artifacts 之外。
- local manual-auth design 不得依赖 browser profile export。
- auth failure 映射 `platform_result=auth_required`；不得在同一任务里继续试探凭据。

## 6. No-auth metadata probe

如果后续 user 批准第一个 live adapter task，建议从 no-auth public metadata only 开始。

Candidate input：

- `platform=bilibili`
- `source_kind=manual_url`
- `quick_capture_preset=metadata_only`
- user 粘贴的一条 canonical Bilibili URL

Candidate extracted fields：

| Field | Requirement |
|---|---|
| `tool_name` | 固定逻辑值，候选为 `BBDown` |
| `tool_version` | 从 future preflight 或 safe output 获取 |
| `platform_item_id` | BV / AV / EP / SS parser result，若输出存在 |
| `title` | parser fixture 稳定前可选 |
| `duration_seconds` | 用于 quick_capture risk estimation 时应有 |
| `page_count` | 可选；用于后续 P selection |
| `selected_page` | 仅当后续任务支持 P selection 时需要 |
| `estimated_media_bytes` | 若用于 quick_capture threshold，必须可靠 |
| `safe_stdout_excerpt` | 可选，必须 redacted |
| `safe_stderr_excerpt` | 可选，必须 redacted |

No-auth probe rejection rules：

- required metadata 缺失时，返回 `parser_drift` 或更具体的 non-`ok` result。
- output 在 redaction 后仍有 unsafe media URL 或 signed query residue 时，不写 receipt。
- no-auth access 需要登录时，返回 `auth_required`；同一任务内不进入 manual auth。
- size / duration estimate 不足以支持 quick_capture 判断时，reject quick path，转 Scope / manual judgment。

## 7. Manual-auth local-only policy

Manual auth 只允许作为未来设计方向；当前 draft 不启用。

后续 manual-auth contract 必须说明：

- local auth material 放在哪里
- 如何排除 Git 与 tracked artifacts
- adapter 如何接收 auth，且不泄露到 command string
- 如何避免 process-list、shell-history、debug-log、crash-log 泄露
- redaction 如何证明 auth material 未进入 stdout/stderr
- 如何用 `auth_required` 告知 human action
- expired auth 如何处理，且不引入 auth refresh automation

默认 reject 的 manual-auth pattern：

- 在 command string 中传 cookie 或 token values
- 读取 browser profile state
- 将 credential files 复制到 `bundle/`、`logs/`、temp artifact roots 或 PR attachments
- 为了 debug 方便保存 full stdout/stderr

## 8. ffmpeg relation

ffmpeg 是未来 media dependency，不属于 metadata-only probe。

Draft boundaries：

- no-auth metadata 不应依赖 ffmpeg。
- missing ffmpeg 不应阻塞 metadata-only work。
- future audio extraction 必须有 explicit ffmpeg path/version preflight。
- future receipt metadata 应记录 audio task 使用的 dependency version。
- ffmpeg failure 不是 Bilibili platform authority；后续任务需要决定是否沿用当前 `PlatformResult`，或在 `PlatformResult` 外增加 tool-preflight result。

当前 non-authority note：本文不批准 ffmpeg execution。

## 9. ASR relation

ASR 位于 audio extraction 下游，不属于当前 active tasks。

Draft boundaries：

- BBDown adapter 不调用 ASR。
- audio extraction 与 ASR 必须是 separate jobs。
- `audio_transcript` 不是 DB enum，只能作为 UI/API preset 展开为底层 outputs。
- BBDown metadata adapter 不产生 transcript artifact。
- future ASR receipts 必须走现有 `artifact_assets` / receipt discipline，不旁路 API authority。

当前 non-authority note：本文不批准 ASR 或 `audio_transcript` runtime。

## 10. PlatformResult mapping

Adapter 必须复用现有 `PlatformResult` enum，不得另建 parallel enum。

| BBDown signal | Draft `platform_result` | Treatment |
|---|---|---|
| exit code `0`；required fields parsed；redaction succeeds | `ok` | 只产生 typed fields 与 redacted evidence 的 receipt candidate |
| login required、missing local auth、expired auth、login timeout | `auth_required` | 停止当前 job，要求 human action |
| risk-control wording、cooldown wording、short-cycle repetition limit | `rate_limited` | 不做 tight retry |
| HTTP 403 或 forbidden wording，且没有明确 missing-auth evidence | `forbidden` | fail-fast；保留 safe diagnostic summary |
| invalid ID、deleted item、missing item、invalid page | `not_found` | fail-fast；user 检查 URL |
| region / area / intl limitation | `region_blocked` | 需要 human judgment |
| VIP / paid / course / permission-required content | `vip_required` | 不绕过 |
| required field missing、parser exception、output layout drift、new BV shape | `parser_drift` | stop-the-line；新建 parser repair task |
| DNS、TLS、connect reset、proxy transient | `network_error` | 仅按 existing retry policy 重试 |
| subprocess timeout | `timeout` | 仅按 existing retry policy 重试 |
| upstream 5xx 或 service unavailable wording | `unavailable` | 仅按 existing retry policy 重试 |
| nonzero exit 且无法安全分类 | `unknown_error` | one retry 后 human review |

Priority rules：

- 同时出现 auth wording 与 403 时，默认优先 `auth_required`，除非已证明 valid auth。
- parser drift 不得压成 `unknown_error`。
- redaction failure 即使 metadata parsing succeeded，也不得创建 receipt。
- `ok` 同时要求 tool success、parser success 与 redaction success。

## 11. Receipt mapping

未来 BBDown metadata jobs 必须通过 `POST /jobs/{job_id}/complete` 报账；不得直接写 authority。

Candidate receipt mapping：

| Receipt field | Draft mapping |
|---|---|
| `job_type` | no-auth metadata probe 使用 `metadata_fetch` |
| `producer` | future adapter logical id；具体值留给 implementation task |
| `producer_version` | ScoutFlow adapter version，不只等于 BBDown release |
| `engine` | `BBDown` |
| `engine_version` | 来自 preflight 或 safe output 的 BBDown version |
| `platform_result` | 按 section 10 映射 |
| `produced_assets[]` | 只允许 redacted evidence 与 safe logs |
| `logs.job_log_path` | 若写入，则为 safe job log relative path |
| `logs.stderr_path` | 若写入，则为 safe stderr excerpt relative path |
| `duration_seconds` | subprocess wall time |
| `next_status` | 仅当 API state guard 允许时使用 `metadata_fetched` |

Candidate produced assets：

| Zone | Artifact kind | Draft content |
|---|---|---|
| `bundle` | `raw_api_response` | redacted parsed metadata evidence，不是 full raw stdout |
| `logs` | `job_log` | safe command shape、timing、version、platform result |
| `logs` | `stderr` | 仅 redaction succeeds 后保存 safe stderr excerpt |

Receipt rules：

- receipt paths 必须是 relative path。
- API 校验 file existence、`sha256`、`bytes`、`zone` 与 path containment。
- non-`ok` receipts 将 job 标记为 failed，且不得推进 capture status。
- successful metadata receipt 可请求 `next_status=metadata_fetched`。
- idempotency 复用现有 `job_id + dedupe_key` 行为。
- receipt 不得包含 credentials、full request headers、full response headers 或 unredacted tool output。

## 12. Redaction requirements

Redaction 必须发生在任何 durable artifact、receipt、job event 或 PR description 写入前。

必须移除或屏蔽的材料：

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
- signed media URLs
- `upos-*` / `bilivideo.com` media URLs
- signed query parameters，例如 `deadline`、`upsig`、`trid`、`uparams`、`mid`、`oi`、`buvid`
- browser profile paths
- 暴露 username、credential file location 或 app data location 的 local absolute paths
- full debug logs
- raw HTTP headers
- 未通过 `credentials-v1` 的 raw response bodies

任何 `raw_api_response` artifact 必须带：

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

如果 redaction 无法证明安全，adapter 不得产生 receipt，必须输出 non-`ok` diagnostic 供 human review。

## 13. Filesystem / temp workdir rules

未来 BBDown subprocess runs 必须使用 per-job isolated temp workdir。

Rules：

- temp workdir 按 job attempt 创建。
- temp workdir 不在 tracked repo paths 下。
- temp workdir 不提交、不附到 PR、不复制进 docs。
- receipt 只使用 approved capture artifact root 下的 relative paths。
- stdout/stderr temp captures 只有在 redacted 且明确需要作为 safe log artifact 时才写入；否则删除。
- local absolute paths 不得进入 receipt 或 artifact metadata。
- metadata-only work 禁止 media output。
- future audio output paths 需要单独任务，并走 receipt / artifact ledger mapping。

本文不锁定最终 filename。后续 implementation task 必须在写代码前决定具体 artifact names。

## 14. Retry / timeout policy

本文继承 `docs/specs/platform-adapter-risk-contract.md`。

Candidate future timeouts：

| Operation | Draft timeout posture |
|---|---|
| Tool preflight | short timeout；不传真实 URL |
| No-auth metadata probe | bounded subprocess timeout |
| Future audio extraction | 只有明确批准后才设置 separate longer timeout |

Retry rules：

- `network_error`、`timeout`、`unavailable`：最多三次，backoff 复用现有 platform risk contract。
- `rate_limited`：不做 tight retry；记录 cooldown reason。
- `auth_required`、`forbidden`、`region_blocked`、`vip_required`、`parser_drift`：不 retry。
- `unknown_error`：one retry 后 human review。
- redaction failure：不得 retry 出 artifacts；停线做 human review。

任何 future retry 都必须保持 idempotency，且不得创建重复 artifact ledger entries。

## 15. Parser drift policy

BBDown stdout/stderr 不是稳定 ScoutFlow schema，parser 是受控边界。

Parser rules：

- 只从 redacted output parse。
- required field definitions 必须在 implementation task 中明确。
- parser fixtures 必须 sanitized。
- parser tests 必须包含 success 与 drift cases。
- output layout changes 映射 `parser_drift`。
- missing required fields 默认映射 `parser_drift`，除非能证明更具体的 platform result。
- parser drift 是 stop-the-line condition。
- parser drift 不得静默降级为 `unknown_error`。
- parser drift 不得推进 capture state。

Future parser evidence 应记录：

- BBDown version
- source snapshot if known
- parser version
- required fields present / missing
- safe diagnostic excerpt

## 16. Test strategy

当前 `T-P1A-006` validation 只做 docs/security validation，不创建 tests。

Future gated test plan：

| Test area | Required coverage |
|---|---|
| Command builder | command array、no shell interpolation、logged shape 不带 credential values |
| Failure classifier | BBDown 可触发的 existing `PlatformResult` mappings |
| Redaction | credentials、signed URLs、local paths、debug residue |
| Parser | sanitized success fixture 与 sanitized drift fixture |
| Receipt mapper | `job_type`、`engine`、paths、hashes、redaction metadata、`next_status` |
| Idempotency | repeat receipt 不重复写 ledger rows |
| Non-goals | no `BBDown serve`、metadata-only path no media output、no browser profile access |

Fixture policy：

- 只用 sanitized fixtures。
- 不保存含 unsafe material 的 real BBDown stdout/stderr。
- parser tests 不运行 BBDown；除非后续任务明确批准 live runtime。

## 17. Gated implementation roadmap

此 roadmap 不是 approval。每一步都需要单独 task gate。

| Gate | Candidate task | Allowed outcome | Not allowed |
|---|---|---|---|
| Gate 0 | `T-P1A-006` | 本 draft spec 进入 review | runtime、tests、BBDown execution |
| Gate 1 | `T-P1A-008` after this draft merges | sanitized fixture parser proposal / tests | live BBDown、real URL、credentials |
| Gate 2 | future tool preflight | 明确批准后仅 `BBDown --version` | media download、auth、real URL |
| Gate 3 | future no-auth metadata probe | short-lived subprocess `-info` against an approved manual URL | media download、manual auth、ASR |
| Gate 4 | future manual-auth local-only | local-only auth design with leak-proof proof points | command-string credentials、browser profile reading |
| Gate 5 | future audio extraction | `--audio-only` with ffmpeg preflight and receipt mapping | ASR in same adapter、broad runtime |
| Gate 6 | future ASR chain | separate ASR job and receipt contract | treating BBDown as ASR owner |

`T-P1A-009` 仍为 backlog/gated，必须等 `T-P1A-006` 与 `T-P1A-008` 完成，并由 user 再次明确批准 runtime spike 后才可打开。

## 18. Open questions for user

以下不是本 draft 的 blocker，但进入实现前需要 user 决策：

- 第一个 live adapter task 是否只做 no-auth `-info`，且不产生 media output？
- future Bilibili BBDown adapter 的 receipt `producer` 精确值是什么？
- 哪些 metadata fields 是 `metadata_fetched` 的 required fields，哪些只是 optional enrichment？
- 如果 BBDown 无法可靠估算 media bytes，quick_capture 是否默认 reject？
- Manual-auth local-only 应采用 ignored local config、environment injection，还是其他 local secret mechanism？
- ffmpeg preflight errors 是先映射当前 `unknown_error`，还是在 `PlatformResult` 外新增 tool-preflight result？
- safe stderr excerpts 应存成 `logs/stderr`，还是只在 `job_events` 写摘要？
- 打开 `T-P1A-009` runtime spike 需要的 user approval phrase 应该是什么？
