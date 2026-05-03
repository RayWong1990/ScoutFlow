# Current

## 当前状态

- Phase：`1A`
- Step：`T-P1A-008 done / T-P1A-009 gated`
- 主任务：`T-P1A-008`
- 工作模式：PR `#17` 已合入 `main`；当前进入 `T-P1A-008` 小账本同步收口；仍遵守 `Single Writer / Multi Reviewer`
- 当前任务状态：`T-P1A-008=done`; `T-P1A-009=backlog/gated`; `T-P1A-006=done`; `T-P1A-007=done`; `T-P1A-005=done`; `T-P1A-003=done`
- 当前结论：`main` 当前已合入 `T-P1A-001` metadata-only API-side baseline、`T-P1A-002` receipt / artifact ledger baseline、`T-P1A-004` text redaction / secret scan safety baseline，并已通过 PR `#10` 合入 `T-P1A-003` BBDown research note、通过 PR `#14` 合入 `T-P1A-006` BBDown adapter draft spec、通过 PR `#15` 合入 `T-P1A-007` Explore URL UX research note、通过 PR `#17` 合入 `T-P1A-008` BBDown sanitized fixture parser。`T-P1A-008` merge commit=`0cfcef58533bba1902eec6ed19a3f7fbed308a64`，GitHub run=`25282572121`，`docs-smoke=success` / `api-contract-tests=success`。`T-P1A-008` 只是 fixture-only parser / classifier baseline，不是 runtime approval。当前 Active count=`0/3`，Review count=`0`；当前不创建 workers，不调用 BBDown / yt-dlp / ffmpeg / ASR，不访问真实 Bilibili URL，不下载媒体，不启用 `audio_transcript` runtime，不进入 Phase 2-4。

## 当前允许

- authority 同步文件：`docs/task-index.md`、`docs/current.md`、`docs/decision-log.md`、`docs/specs/contracts-index.md`
- 入口同步文件：`AGENTS.md`、`README.md`，仅在状态口径需要时修改
- 已合入主线的 `docs/specs/bbdown-adapter-contract-draft.md` 与 `docs/research/t-p1a-007-explore-url-ux-brainstorm-2026-05-03.md` 当前只作参考，不自动授权后续代码修改

## 当前禁止

- `apps/`
- `workers/`
- `packages/`
- `data/`
- `referencerepo/`
- `candidates/`
- `dispatches/`
- `audits/`
- `audio_transcript` runtime
- 真下载 / ASR / BBDown / yt-dlp / ffmpeg runtime
- 浏览器自动化
- Phase 2-4 真实逻辑
- 把 BBDown research note 直接写成 final authority
- 把用户“隐私合规风险低”解释为可以提交 cookie / token / secret

## 当前候选基准

- `T-P1A-001` = `metadata_only API-side capture creation baseline merged`
- `T-P1A-002` = `API-side receipt ingestion and artifact ledger mapping merged baseline`
- `T-P1A-004` = `redaction / secret scan / CI hardening merged baseline`
- `T-P1A-003` = `BBDown public-source research note merged as reference only`
- `docs/specs/bbdown-adapter-contract-draft.md` = `T-P1A-006` merged draft；仍必须是 `draft / not final authority / not runtime approval`
- `docs/research/t-p1a-007-explore-url-ux-brainstorm-2026-05-03.md` = `T-P1A-007` merged Explore UX decision pack；仍只是 research note
- `POST /captures/discover` = `capture 创建入口（capture creation entrypoint）`
- `POST /jobs/{job_id}/complete` = `worker receipt API-side validation and ledger entrypoint`; 当前只接收已存在 job 的 receipt，不创建 worker queue runtime
- `recommendation / keyword / RAW gap` 不直接创建 capture
- 活动任务上限 `3`；当前 Active count=`0/3`，Review count=`0`
- 项目根不建立重治理目录

> `T-P1A-001` / `T-P1A-002` / `T-P1A-004` 的合并只表示对应 API-side 和安全基线进入 `main`；`T-P1A-003` 的合并只表示 research note 进入 `docs/research/**`。这些都不等于批准 broader Phase 1A runtime、workers、frontend、`audio_transcript` 或 Phase 2-4 产品代码。

## 当前任务

- `T-P1A-008`：BBDown sanitized fixture parser；状态 `done`；已通过 PR `#17` 合并入 `main`，只作为 fixture-only parser / classifier baseline；不批准 runtime
- `T-P1A-009`：BBDown local runtime spike；状态 `backlog/gated`；前置为 `T-P1A-006` + `T-P1A-008` + user 再次明确批准；不得下载媒体，不跑 ASR
- `T-P1A-007`：Explore URL UX / risk / receipt status brainstorm；状态 `done`；已通过 PR `#15` 合并入 `main`，只作为 research note / decision pack
- `T-P1A-006`：BBDown adapter contract draft；状态 `done`；已通过 PR `#14` 合并入 `main`，只作为 merged draft spec，不实现或调用 runtime capture
- `T-P1A-003`：BBDown tool-surface research note；状态 `done`；已通过 PR `#10` 合并入 `main`，只作为 research note
- `T-P1A-005`：Dispatch 0 human gate sync；状态 `done`；已通过 PR `#12` 合并入 `main`，只同步 authority / ledger，不批准 runtime
- `T-P1A-002`：API jobs / receipt / artifact ledger foundation；状态 `done`；已通过 PR `#9` 合并入 `main`
- `T-P1A-004`：Redaction / secret scan / CI hardening；状态 `done`；已通过 PR `#8` 合并入 `main`
- `T-P1A-001`：Bilibili `manual_url` quick_capture metadata contract；状态 `done`；已通过 PR `#7` 合并入 `main`

## 下一步候选

- `T-P1A-008` 已完成；当前不自动打开任何 code-bearing task
- `T-P1A-009` 必须等 `T-P1A-006` + `T-P1A-008` 完成后，并由 user 再次明确批准 runtime spike 后再开
- 当前不自动开启任何 code-bearing task

## 阻塞

- 不允许让 `recommendation / keyword / RAW gap` 直接创建 capture
- 不允许把 `/captures/discover` 语义写成 source discovery / search / recommendation discovery
- 不允许把 BBDown research note、draft spec、或“后续希望复用 BBDown”解释为 runtime approval
