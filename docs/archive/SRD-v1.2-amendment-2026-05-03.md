# SRD v1.2 Amendment — 2026-05-03

> 本文件是 `T-P1A-010C` 的 SRD amendment repair draft。
> 状态：`candidate / draft / not final authority / not runtime approval`。
> 本文件补充 `docs/SRD-v1-2026-05-02.md` 与 `docs/SRD-v1.1-amendment-2026-05-03.md`，不做 base SRD 全文重写。
> 当前用途：把 BBDown tool preflight、no-auth metadata gate、QR / manual auth、parallel conflict domain、`audio_transcript` blocker 写成待拍板工程补丁。

## 0. 元信息

| 字段 | 值 |
|---|---|
| amendment ID | `SRD-A016-A022` |
| 任务来源 | `T-P1A-010C` |
| 基线文档 | `docs/SRD-v1-2026-05-02.md` |
| 上一版补丁 | `docs/SRD-v1.1-amendment-2026-05-03.md` |
| 关联 PRD 补丁 | `docs/PRD-v1.2-amendment-2026-05-03.md` |
| 关联 contracts | `C-AUTH-001`、`C-SCOPE-001`、`C-PROC-001`、`C-BBD-001`、`C-PLT-001`、`C-SEC-001`、`C-OPS-001`、`C-OPS-003` |
| 当前不批准 | product code、BBDown execution、QR login、manual auth、media download、ffmpeg、ASR、workers、frontend、Phase 2-4 runtime |

## 1. 生效规则

- 未经 user 拍板前，本文件所有条目都是 `candidate amendment`。
- 本文件只定义工程边界和后续 patch 指向，不修改现有代码 schema。
- `ToolPreflightResult` 是后续工程 contract 候选名；若代码实现采用不同命名，必须保持同等语义分离。
- 本文件不把 `docs/specs/bbdown-adapter-contract-draft.md` 升级为 final authority。

建议状态机：

```text
draft_candidate
  -> user_reviewed
  -> contract_index_registered
  -> implementation_task_authorized
  -> superseded_or_archived
```

## 2. A016 — Runtime Gate Amendment

### 当前事实

`T-P1A-009` 只证明当前环境没有找到 `BBDown` executable：

```text
tool_preflight_result=executable_not_found
platform_boundary_reached=false
platform_result=not_emitted
bbdown_info_executed=false
receipt_emitted=false
```

### Contract 修订

必须把本地工具 preflight 与平台访问结果分层：

| Layer | 候选对象 | 产生条件 | 不得承载 |
|---|---|---|---|
| local tool preflight | `ToolPreflightResult` | 查找 executable、运行 safe version command、检查本地 dependency | 平台 auth、平台 forbidden、parser drift、receipt 状态 |
| platform adapter result | `PlatformResult` | adapter 已实际触达平台边界并可分类平台 / parser / network 结果 | executable lookup failure、missing local binary、ffmpeg missing |

### 候选 `ToolPreflightResult`

当前只在文档层提出候选取值，代码实现需由后续任务锁定：

```text
tool_available
executable_not_found
not_executable
version_check_failed
timeout
unsupported_version
dependency_missing
unknown_preflight_error
```

`executable_not_found` 不得写入 `PlatformResult` enum，也不得映射成 `unknown_error`。

## 3. A017 — Parallel Execution Amendment

### Conflict domain

| Domain | 单写者要求 | 示例 |
|---|---|---|
| `ledger-authority` | 必须单写者 | `docs/current.md`、`docs/task-index.md` |
| `contract-index` | 必须单写者或串行 patch | `docs/specs/contracts-index.md` |
| `tool-preflight-code` | 可与 docs 并行 | `services/api/scoutflow_api/external_tools/**`、`tests/contracts/**` |
| `adapter-shell-code` | 可与 docs 并行，但不得改 ledger | injected runner、sanitized fixtures、parser integration |
| `amendment-docs` | 一个 docs writer | PRD / SRD v1.2 draft amendment |

### 工程规则

- 不同 conflict domain 可并行。
- 同一 conflict domain 必须 single writer。
- `docs/current.md` / `docs/task-index.md` 的状态回写只由 ledger owner 执行。
- 执行 PR 可在 PR body 提供建议 ledger text，但不能自行覆盖 ledger owner。

## 4. A018 — BBDown No-Auth Metadata Gate

### Gate 顺序

```text
not_configured
  -> tool_preflight_clear
  -> no_auth_info_probe_authorized
  -> no_auth_info_probe_executed
  -> redacted_parser_classified
  -> receipt_candidate_allowed
  -> explore_trust_trace_allowed
```

### Transition gates

| Transition | Required gate | Stop condition |
|---|---|---|
| `not_configured -> tool_preflight_clear` | executable found；safe version check succeeds；no URL used | missing executable、unsupported version、unsafe stdout/stderr |
| `tool_preflight_clear -> no_auth_info_probe_authorized` | user approves one no-auth metadata probe against one manual URL | no user approval、URL expands scope |
| `no_auth_info_probe_authorized -> no_auth_info_probe_executed` | command array only；no auth；no media flags；bounded temp workdir | QR prompt、auth request、media output |
| `no_auth_info_probe_executed -> redacted_parser_classified` | stdout/stderr redacted before durable write；parser returns typed classification | redaction cannot prove safety、parser drift |
| `redacted_parser_classified -> receipt_candidate_allowed` | evidence is safe and maps to existing receipt discipline | raw output, credentials, signed media URL |
| `receipt_candidate_allowed -> explore_trust_trace_allowed` | receipt design is reviewed; no authority bypass | direct DB / artifact write |

### Current forbidden behavior

- no BBDown runtime in `T-P1A-010C`
- no real `BBDown -info` in this docs task
- no media download
- no ffmpeg
- no ASR
- no QR login
- no manual auth
- no browser automation
- no browser profile reading
- no receipt / capture state mutation

## 5. A019 — QR Login / Manual Auth Gate

### Contract 修订

Manual auth is a separate future gate. It is not part of metadata-only no-auth probe.

If a later task opens manual auth, it must define all of the following before execution:

1. human scan pause protocol
2. local auth material storage outside tracked artifacts
3. process-list and shell-history leakage control
4. stdout / stderr redaction proof
5. DB / receipt / job event exclusion rule for auth material
6. failure mapping to `auth_required`
7. explicit ban on browser profile reading unless separately amended

Observed implementation lesson from local BBDown `1.6.3`:

- `BBDown login` may write `qrcode.png` into the current working directory.
- `BBDown.data` / `BBDownTV.data` may be written next to the executable.
- Therefore a manual-auth gate must use:
  - a temp cwd outside the repo
  - an executable path whose auth-sidecar location is outside tracked repo paths
  - a report that describes auth storage only in abstract form such as `local BBDown auth store outside Git`

### Hard bans

- QR code image in Git / PR / CI / logs / fixtures / tracked files
- `BBDown.data` / `BBDownTV.data` in Git / PR / CI / logs / fixtures / tracked files
- cookie / token / authorization header in Git / PR / CI / logs / DB artifacts / receipts
- signed media URL in durable evidence before redaction
- local browser profile export
- command-string credentials
- debug mode that persists full stdout / stderr

## 6. A020 — Audio Transcript Blocker

### Blocker rule

`audio_transcript` remains blocked until the metadata-only BBDown path proves safe runtime evidence.

Required evidence before any future unlock discussion:

| Requirement | Current status |
|---|---|
| Tool preflight proves BBDown executable availability | not proven in `T-P1A-009` |
| No-auth `-info` probe executed against approved manual URL | not executed |
| Redacted stdout / stderr evidence exists | not produced |
| Parser classified evidence into typed result | not assessed |
| `ToolPreflightResult` and `PlatformResult` are separated | candidate amendment only |
| Receipt / ledger path is reviewed | not opened for runtime |
| User explicitly approves next gate | required |

The blocker covers:

- audio extraction
- media download
- ffmpeg
- ASR
- transcript artifact
- `audio_transcript` runtime
- worker runtime
- frontend flow

## 7. A021 — Patch List

### Future mechanical patch candidates

| Patch | Base SRD / Spec 位置 | 动作 |
|---|---|---|
| `SRD12-P001` | `docs/SRD-v1-2026-05-02.md` §2 component roster / runtime requirements | 把 BBDown / ffmpeg / ASR 从当前 active Phase 1A runtime 中降级为 gated dependency，除非任务另行批准 |
| `SRD12-P002` | `docs/SRD-v1-2026-05-02.md` §3.5 / §3.6 worker requirements | 把 media / ASR worker 表达标成 blocked runtime，不再作为当前 active implementation |
| `SRD12-P003` | `docs/SRD-v1-2026-05-02.md` §7 interface / worker receipt | 在 receipt 之前增加 tool preflight 与 no-auth metadata evidence gate |
| `SRD12-P004` | `docs/specs/platform-adapter-risk-contract.md` | 补充 `ToolPreflightResult` 与 `PlatformResult` 的分层说明，避免 missing executable 映射进平台 enum |
| `SRD12-P005` | `docs/specs/bbdown-adapter-contract-draft.md` | 更新 Gate 2 / Gate 3：`T-P1A-009` 已证明 executable missing，后续先开 tool preflight |
| `SRD12-P006` | `docs/specs/raw-response-redaction.md` | 明确 QR code image、`BBDown.data`、browser profile path、signed media URL、local auth path 不进入 durable evidence |
| `SRD12-P007` | `docs/specs/contracts-index.md` | 登记 v1.2 amendment 为 candidate / draft only |

### Reference outline only

- Phase 1B RAW link true logic
- Phase 2 Signal Workbench / Capture Plan runtime
- Phase 3 recommendation / reranking / Hermes scheduling
- Phase 4 Dispatch UI / formal review queue
- XHS / YouTube true capture
- manual-auth local-only design
- media / ffmpeg / ASR / `audio_transcript` runtime

## 8. A022 — Validation And Red-Team Checklist

### Required validation for this docs task

```bash
python tools/check-docs-redlines.py
python tools/check-secrets-redlines.py
python -m pytest tests/contracts -q
python -m pytest tests/api tests/contracts -q
git diff --check
find . -maxdepth 1 -type d \( -name apps -o -name workers -o -name packages -o -name candidates -o -name dispatches -o -name audits -o -name example -o -name examples \) -print
git ls-files | grep -E '^(data|referencerepo|example|examples)/' || true
```

### Red-team checklist

- `executable_not_found` 是否只出现在 tool preflight 语义中？
- 是否没有新增 `PlatformResult` enum？
- 是否没有把 `T-P1A-009` 写成 adapter runtime success？
- 是否没有打开 QR / manual auth？
- 是否没有把 user sample URL 用于 auth、download 或 broader scope？
- 是否没有写入 cookie、token、auth header、QR image、browser profile path、signed URL 或 raw stdout/stderr？
- 是否没有打开 product code、workers、frontend、ffmpeg、ASR 或 Phase 2-4 runtime？
- 是否没有把 research note / draft spec / local report 升级为 final authority？
