# Current

## 当前状态

- Phase：`1A`
- Step：`T-P1A-010 wave1 ledger open / T-P1A-009 done`
- 主任务：`T-P1A-010-wave1-ledger-open`
- 工作模式：Wave 1 已打开；`T-P1A-010A` / `T-P1A-010B` / `T-P1A-010C` 可并行开独立分支；仍遵守 `Single Writer / Multi Reviewer`
- 当前任务状态：`T-P1A-010=done`; `T-P1A-010A=active`; `T-P1A-010B=active`; `T-P1A-010C=active`; `T-P1A-009=done`; `T-P1A-008=done`
- 当前结论：`main` 当前已合入 `T-P1A-001` metadata-only API-side baseline、`T-P1A-002` receipt / artifact ledger baseline、`T-P1A-004` text redaction / secret scan safety baseline，并已通过 PR `#10` 合入 `T-P1A-003` BBDown research note、通过 PR `#14` 合入 `T-P1A-006` BBDown adapter draft spec、通过 PR `#15` 合入 `T-P1A-007` Explore URL UX research note、通过 PR `#17` 合入 `T-P1A-008` BBDown sanitized fixture parser、通过 PR `#19` 合入 `T-P1A-009` BBDown local runtime spike report，并通过 PR `#20` 完成 `T-P1A-009` close hardening。`T-P1A-009` merge commit=`af1cbcedf92409e187e77217cc0b39449738d1ba`，PR `#20` merge commit=`f10226fc6cd7724f7af7bd410ed8022ecb500a69`。`T-P1A-009` 结果为 `BBDown` executable 未在当前 PATH 中找到，未执行 `-info`；no `PlatformResult` emitted；`tool_preflight_result=executable_not_found`。当前 Active count=`3/3`，Review count=`0`；当前不创建 workers，不调用真实 BBDown / yt-dlp / ffmpeg / ASR，不下载媒体，不读取凭据或 browser profile，不启用 `audio_transcript` runtime，不进入 Phase 2-4。

## 当前允许

- authority 同步文件：`docs/task-index.md`、`docs/current.md`、`docs/decision-log.md`、`docs/specs/contracts-index.md`
- 入口同步文件：`AGENTS.md`、`README.md`，仅在状态口径需要时修改
- 已合入主线的 `docs/specs/bbdown-adapter-contract-draft.md` 与 `docs/research/t-p1a-007-explore-url-ux-brainstorm-2026-05-03.md` 当前只作参考，不自动授权后续代码修改
- `T-P1A-009` report-only 文件：`docs/research/t-p1a-009-bbdown-local-runtime-spike-report-2026-05-03.md`
- `T-P1A-010A` / `T-P1A-010B` / `T-P1A-010C` 的具体写入边界以 `docs/task-index.md` Active 表为准；代码分支不得自行改 `docs/current.md` 或 `docs/task-index.md`

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
- 真下载 / ASR / yt-dlp / ffmpeg runtime
- 任何 BBDown runtime，除非后续任务再次显式授权；PR `#19` 中的 `BBDown --version` 尝试和未执行的 `-info` 只作为历史 spike 结果，不构成当前可复用许可
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
- 活动任务上限 `3`；当前 Active count=`3/3`，Review count=`0`
- 项目根不建立重治理目录

> `T-P1A-001` / `T-P1A-002` / `T-P1A-004` 的合并只表示对应 API-side 和安全基线进入 `main`；`T-P1A-003` 的合并只表示 research note 进入 `docs/research/**`。这些都不等于批准 broader Phase 1A runtime、workers、frontend、`audio_transcript` 或 Phase 2-4 产品代码。

## 当前任务

- `T-P1A-010A`：BBDown executable discovery / tool preflight package；状态 `active`；仅允许 tool path discovery、preflight result modeling、mockable `BBDown --version` wrapper；不允许真实 BBDown 执行、URL、`-info`、auth、media、ffmpeg、ASR、receipt 或 capture state
- `T-P1A-010B`：BBDown no-auth `-info` adapter shell with injected runner and parser integration；状态 `active`；仅允许 command builder、injected runner、sanitized fixture 与现有 parser integration；不允许真实 BBDown 执行、auth、media、receipt 或 capture state
- `T-P1A-010C`：PRD/SRD amendment repair pack + next dispatch plan + red-team checklist；状态 `active`；默认 sidecar read-only，只有 user 授权一个 docs writer 时才可写 draft amendment；不得写 product code、runtime 或 authority override
- `T-P1A-010`：Wave 1 ledger open；状态 `done`；只登记 `T-P1A-010A` / `T-P1A-010B` / `T-P1A-010C`，不执行 BBDown 或任何 runtime
- `T-P1A-009`：BBDown local runtime spike；状态 `done`；已通过 PR `#19` 合并入 `main`，只产出 report-only runtime spike 文档；`BBDown` executable 未在 PATH 中找到，未执行 `-info`；no `PlatformResult` emitted；`tool_preflight_result=executable_not_found`
- `T-P1A-008`：BBDown sanitized fixture parser；状态 `done`；已通过 PR `#17` 合并入 `main`，只作为 fixture-only parser / classifier baseline；不批准 broader runtime
- `T-P1A-007`：Explore URL UX / risk / receipt status brainstorm；状态 `done`；已通过 PR `#15` 合并入 `main`，只作为 research note / decision pack
- `T-P1A-006`：BBDown adapter contract draft；状态 `done`；已通过 PR `#14` 合并入 `main`，只作为 merged draft spec，不实现或调用 runtime capture
- `T-P1A-003`：BBDown tool-surface research note；状态 `done`；已通过 PR `#10` 合并入 `main`，只作为 research note
- `T-P1A-005`：Dispatch 0 human gate sync；状态 `done`；已通过 PR `#12` 合并入 `main`，只同步 authority / ledger，不批准 runtime
- `T-P1A-002`：API jobs / receipt / artifact ledger foundation；状态 `done`；已通过 PR `#9` 合并入 `main`
- `T-P1A-004`：Redaction / secret scan / CI hardening；状态 `done`；已通过 PR `#8` 合并入 `main`
- `T-P1A-001`：Bilibili `manual_url` quick_capture metadata contract；状态 `done`；已通过 PR `#7` 合并入 `main`

## 下一步候选

- 推荐合并顺序：先合并 Wave 1 ledger PR，再让 `T-P1A-010A` / `T-P1A-010B` / `T-P1A-010C` 各自用独立分支推进
- `audio_transcript` readiness gate 仍阻塞，必须等 BBDown tool availability 与一次 no-auth metadata probe 产生 redacted、parser-classified evidence 后再议

## 阻塞

- 不允许让 `recommendation / keyword / RAW gap` 直接创建 capture
- 不允许把 `/captures/discover` 语义写成 source discovery / search / recommendation discovery
- 不允许把 BBDown research note、draft spec、或“后续希望复用 BBDown”解释为 runtime approval
- 不允许把 `T-P1A-009` 的 local-only spike 写成媒体下载、ffmpeg、ASR、worker、artifact、receipt、capture 状态变更或 `audio_transcript` approval
- 不允许 `T-P1A-010A` / `T-P1A-010B` / `T-P1A-010C` 的执行 PR 独立改写 `docs/current.md` 或 `docs/task-index.md`；后续状态回写由 ledger owner 处理
