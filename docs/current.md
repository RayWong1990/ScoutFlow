# Current

## 当前状态

- Phase：`1A`
- Step：`T-P1A-013B authority sync + docs-check suffix task hardening done`
- 主任务：`T-P1A-013B-authority-docs-check-hardening`
- 工作模式：当前无 active product task；继续遵守 `Single Writer / Multi Reviewer`
- 当前任务状态：`T-P1A-013B=done`; `T-P1A-013A=done`; `T-P1A-013=done`; `T-P1A-012R=done`; `T-P1A-012=done`; `T-P1A-011G=done`; `T-P1A-011F=done`; `T-P1A-011E=done`; `T-P1A-011D=done`; `T-P1A-011C=done`; `T-P1A-011B=done`; `T-P1A-011=done`; `T-P1A-010=done`; `T-P1A-010A=done`; `T-P1A-010B=done`; `T-P1A-010C=done`; `T-P1A-009=done`; `T-P1A-008=done`
- 当前结论：`T-P1A-013B` 已完成，补了 post-013A 的 authority/docs-check gap。第一，`docs/current.md` 中残留的 `T-P1A-013A 状态 active` stale line 已删除，authority state 现在只保留 `013A=done`。第二，`tools/check-docs-redlines.py` 已升级为精确识别带后缀的任务编号，并补了 current-doc 自检，因此 `T-P1A-011D/E/F/G`、`T-P1A-012R`、`T-P1A-013A/B` 不再被截断成三位数字任务，同时 `Active count=0/3` 与后续 `状态 active` 冲突也会被直接拦下。当前 Active count=`0/3`，Review count=`0`；本轮未改任何产品/API/runtime 行为，不下载媒体，不运行 BBDown、ffmpeg 或 ASR，未读取 browser profile，不启用 `audio_transcript` runtime，不进入 Phase 2-4。

## 当前允许

- authority 同步文件：`docs/task-index.md`、`docs/current.md`、`docs/decision-log.md`、`docs/specs/contracts-index.md`
- 入口同步文件：`AGENTS.md`、`README.md`，仅在状态口径需要时修改
- `docs/retro/**`：最小 retrospective scaffold；当前只作 non-authority 回溯支架
- `docs/research/t-p1a-011d-second-retro-remediation-triage-2026-05-04.md`、`docs/research/t-p1a-011f-dispatch-08-09-patch-report-2026-05-04.md`、`docs/research/t-p1a-011g-sidecar-review-07x-and-patched-08-09-2026-05-04.md`：当前只作 triage / patch / review reference
- 已合入主线的 `docs/specs/bbdown-adapter-contract-draft.md` 与 `docs/research/t-p1a-007-explore-url-ux-brainstorm-2026-05-03.md` 当前只作参考，不自动授权后续代码修改
- `T-P1A-009` report-only 文件：`docs/research/t-p1a-009-bbdown-local-runtime-spike-report-2026-05-03.md`
- 当前无 active product task；`T-P1A-013B` 已完成

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
- `T-P1A-010A` = `ToolPreflightResult code and contract tests merged`; not live BBDown approval
- `T-P1A-010B` = `injected-runner no-auth -info adapter shell merged`; not live runtime proof
- `docs/PRD-v1.2-amendment-2026-05-03.md` + `docs/SRD-v1.2-amendment-2026-05-03.md` = `T-P1A-010C` candidate amendment pack；仍是 `candidate / draft / not final authority / not runtime approval`
- `docs/research/t-p1a-011-bbdown-noauth-info-probe-report-2026-05-03.md` = `T-P1A-011` blocked probe report；是 repair 输入，不是 runtime approval
- 活动任务上限 `3`；当前 Active count=`0/3`，Review count=`0`
- 项目根不建立重治理目录

> `T-P1A-001` / `T-P1A-002` / `T-P1A-004` 的合并只表示对应 API-side 和安全基线进入 `main`；`T-P1A-003` 的合并只表示 research note 进入 `docs/research/**`；PR `#23` / `#22` / `#24` 的合并只表示 Wave 1 code/doc packages 进入 `main`。这些都不等于批准 broader Phase 1A runtime、workers、frontend、`audio_transcript` 或 Phase 2-4 产品代码。

## 当前任务

- `T-P1A-011`：BBDown tool preflight compatibility repair；状态 `done`；已修复 `BBDown 1.6.3` 对 `--version` 的命令形态兼容问题；contract tests 与 live local preflight verification 已通过；仍未重跑 `-info`
- `T-P1A-011B`：Manual-auth QR local-only gate；状态 `done`；已使用 repo 外 local-only executable/auth store 与 repo 外 temp cwd 完成 `BBDown login`；QR 已本地展示并完成扫码；临时 QR cwd 已清空；auth sidecar 留在 repo 外 local-only auth store；报告见 `docs/research/t-p1a-011b-bbdown-manual-auth-qr-local-only-report-2026-05-03.md`
- `T-P1A-011C`：Auth-present BBDown metadata probe；状态 `done`；已使用 `T-P1A-011B` 留下的 repo 外 local-only auth state，对授权 sample URL 执行单次 `BBDown -info`；`platform_result=ok`；已解析 `aid/title/duration/page_count/selected_page`；报告见 `docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md`
- `T-P1A-011D`：Second retro / remediation triage；状态 `done`；已固定 GitHub truth、Opus claim triage、编号修复与 `07.2 -> 07.4 -> 08 -> 08.1 -> 09` repair plan；报告见 `docs/research/t-p1a-011d-second-retro-remediation-triage-2026-05-04.md`
- `T-P1A-011E`：Minimal retro skeleton；状态 `done`；已创建最小 `docs/retro/` scaffold 与 first-week retro；不是 authority、不是 PRD/SRD amendment、不是 product scope 扩张
- `T-P1A-011F`：Dispatch 08/09 prompt patch；状态 `done`；已确认 repo 外 patched Dispatch `08/09` prompts 以 `011C` 为 success evidence source，且保持 no-runtime boundary；repo-side 报告见 `docs/research/t-p1a-011f-dispatch-08-09-patch-report-2026-05-04.md`
- `T-P1A-011G`：Sidecar review for `07.x` + patched `08/09`；状态 `done`；结论 `PASS_WITH_FIXES`；最小修复是把 repo authority docs 从 `011C` 单点焦点同步到 `07.x remediation complete`；报告见 `docs/research/t-p1a-011g-sidecar-review-07x-and-patched-08-09-2026-05-04.md`
- `T-P1A-012`：Metadata probe receipt / artifact ledger wiring；状态 `done`；执行输入采用 patched Dispatch `08`；新增 `metadata_probe_receipt_bridge` helper 和围绕 `011C` 的 contract/API tests；safe artifact kinds 为 `metadata_probe_summary` 与 `safe_metadata_evidence`；不允许新 BBDown runtime、media / ffmpeg / ASR、manual auth、frontend / workers
- `T-P1A-012R`：Receipt-wiring single-point retro；状态 `done`；只补 post-08 retro，不改产品代码；结论是 `012` 的证明范围只到 tests 内的 safe evidence-to-receipt mapping；报告见 `docs/retro/t-p1a-012-receipt-wiring-retro-2026-05-04.md`
- `T-P1A-013`：Explore Trust Trace minimal surface；状态 `done`；模式=`API/CLI`; 已新增 `GET /captures/{capture_id}/trust-trace`；Trust Trace 会分开返回 `capture / capture_state / metadata_job / probe_evidence / receipt_ledger / media_audio / audit`；不允许 frontend 模式、BBDown runtime、media / ffmpeg / ASR、manual auth、browser profile、`audio_transcript`
- `T-P1A-013A`：Receipt / Trust Trace audit hardening；状态 `done`；已收紧 metadata bridge 的 path containment，并把 generic receipt API 的当前 phase 成功证据源锁死为 `T-P1A-011C + auth-present + exact report path`；Trust Trace layering 维持不变
- `T-P1A-013B`：Authority sync + docs-check suffix task hardening；状态 `done`；已删除 `docs/current.md` 中 `T-P1A-013A 状态 active` stale line；checker 现在精确解析后缀任务 ID，并能拦住 `Active count=0/3` 与后续 `状态 active` 的 current-doc 冲突
- `T-P1A-010A`：BBDown executable discovery / tool preflight package；状态 `done`；已通过 PR `#23` 合并入 `main`；仅表示 `ToolPreflightResult` package 和 contract tests merged，不批准真实 BBDown 执行、URL、`-info`、auth、media、ffmpeg、ASR、receipt 或 capture state
- `T-P1A-010B`：BBDown no-auth `-info` adapter shell with injected runner and parser integration；状态 `done`；已通过 PR `#22` 合并入 `main`；仅表示 injected-runner adapter shell merged，不批准真实 BBDown 执行、真实 `BBDown -info`、auth、media、receipt 或 capture state
- `T-P1A-010C`：PRD/SRD amendment repair pack + next dispatch plan + red-team checklist；状态 `done`；已通过 PR `#24` 合并入 `main`；PRD/SRD v1.2 amendment 仍是 `candidate / draft / not final authority / not runtime approval`
- `T-P1A-010`：Wave 1 ledger open / close；状态 `done`；已登记并收口 `T-P1A-010A` / `T-P1A-010B` / `T-P1A-010C`，不执行 BBDown 或任何 runtime
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

- 下一步候选默认不自动启动；如需继续，要么显式授权更大的 product surface，要么回到 docs-only / candidate-only lane
- `T-P1A-011H` candidate-only legal/vendor notes 仍需显式授权；frontend mode 也仍需单独授权
- 不自动执行新的 `BBDown -info`；未来若要尝试新的 URL 或新的 runtime gate，仍需 user 再次显式批准；media、ffmpeg、ASR、workers、frontend、`audio_transcript` 仍未批准

## 阻塞

- 不允许让 `recommendation / keyword / RAW gap` 直接创建 capture
- 不允许把 `/captures/discover` 语义写成 source discovery / search / recommendation discovery
- 不允许把 BBDown research note、draft spec、或“后续希望复用 BBDown”解释为 runtime approval
- 不允许把 `T-P1A-009` 的 local-only spike 写成媒体下载、ffmpeg、ASR、worker、artifact、receipt、capture 状态变更或 `audio_transcript` approval
- 不允许把 PR `#23` / `#22` / `#24` 的合并解释为 live BBDown runtime proof
- 不允许把 `T-P1A-011` 的 preflight blocked report 写成 no-auth `-info` 成功或 runtime approval
