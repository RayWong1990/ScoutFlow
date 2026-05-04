# Decision Log

> 薄版决策日志。只记录已经 user 拍板的工程/产品决策，不替代 PRD/SRD。

## 2026-05-03 — Step0 safety baseline accepted for Git bootstrap

- Decision: `A001-A015` accepted as candidate implementation baseline for `Phase 0 / Phase 1A`.
- Scope: Git bootstrap and subsequent Phase 0 tasks.
- Not a full product-code approval.
- Source:
  - `docs/SRD-v1.1-amendment-2026-05-03.md`
  - `docs/specs/contracts-index.md`

## 2026-05-03 — Decision log filename

- Decision: use `docs/decision-log.md`.
- Decision: do not use `docs/decisions.md` during `Phase 0`.

## 2026-05-03 — Bootstrap task approval

- Decision: close `T-P0-000` as done.
- Decision: 启动 `T-P0-001` 执行阶段。
- Scope: Git initialization, private GitHub repository, root baseline docs/config only.

## 2026-05-03 — GitHub bootstrap completed

- Decision: initialize local git repository on branch `main`.
- Decision: create private GitHub repository `RayWong1990/ScoutFlow`.
- Initial commit: `22c2c2014b9d10f48a6a8fe11fc73f38ba1b0045`
- Remote URL: `https://github.com/RayWong1990/ScoutFlow.git`
- Scope: docs, contracts, and repo baseline only.

## 2026-05-03 — T-P0-001 review-fix completed

- Decision: `T-P0-001 review-fix` 仅修复文档口径，不批准产品代码。
- Decision: `d1c12326450f5a92d8b0b6f32c0cac51f5f5ee5a` 是进入 `review` 前的状态同步 commit。
- Decision: `T-P0-001` 可以从 `review` 闭合为 `done`。

## 2026-05-03 — T-P0-003 docs redline lint stub completed

- Decision: `T-P0-003` completed and closed as done.
- Commit: `b32ae22edd7e60becc39d5d5d0bca8381b948254`
- GitHub Actions run: `25270586304`
- Scope: docs redline lint stub, docs-check workflow, README / AGENTS / CLAUDE / current / task-index synchronization.
- Not a product-code approval.
- No API / worker / Console implementation.

## 2026-05-03 — T-P0-003 final close recorded

- Decision: 补记 `T-P0-003 final close`。
- Close commit: `efe607dbafe3c398d582aaf0a0d5e9521ff2a814`
- GitHub Actions run: `25270929463`
- Scope: close review, harden task-index Done state parsing, update entry docs.
- Not a product-code approval.

## 2026-05-03 — T-P0-002 parallel execution protocol started

- Decision: start `T-P0-002` as entry docs deepening + parallel execution protocol candidate baseline.
- Scope: docs and lightweight repo coordination files only.
- Not a product-code approval.
- Branch mode: `task/T-P0-002-parallel-execution-protocol`

## 2026-05-03 — T-P0-002 closed after external audit

- Decision: close `T-P0-002` as `done` after PR `#1` external audit.
- PR: `https://github.com/RayWong1990/ScoutFlow/pull/1`
- Branch: `task/T-P0-002-parallel-execution-protocol`
- Reviewed commit: `ee1f4cfd34282e39be74afc20310ef7801ac4b25`
- GitHub Actions run: `25271451489`; docs-check=`success`
- GPT Pro external audit: COMMENT review; no blocking issue.
- Scope: Step0 / Phase 0 collaboration protocol, entry docs, and GitHub external audit workflow only.
- Not a product-code approval.
- No Phase 1A product code approval.

## 2026-05-03 — PR #1 merged after T-P0-002 audit

- Decision: user authorized merge of PR `#1`.
- Merge commit: `bafeb56c79c69a43f2806aaec88ea7014db36815`
- Scope: Step0 / Phase 0 collaboration protocol only.
- Not a product-code approval.
- No Phase 1A product code approval.

## 2026-05-03 — Communication tests paused and ScoutFlow mainline restored

- Decision: Treat `T-P0-005` / `T-P0-006` GitHub queue / Codex adapter work as communication tests, not ScoutFlow product tasks.
- Decision: Close/pause smoke issues and communication-test dispatches.
- Decision: Remove `example/` and smoke-only `examples/` files from repo.
- Decision: Delete two archive/test branches: `task/archive-chatgpt-session-prompts-2026-05-03` and `task/archive-t-p0-002-audit-dispatch`.
- Scope: cleanup only; no API / worker / Console implementation.
- Not a Phase 1A product-code approval.
- Product direction restored to PRD/SRD authority-first ScoutFlow / 采集线 mainline.

## 2026-05-03 — T-P0-007 Phase 1A readiness planning started

- Decision: start `T-P0-007` as a docs-only Phase 1A Bilibili `manual_url` quick_capture readiness pack.
- Decision: do not reuse `T-P0-005` / `T-P0-006` for product-mainline work.
- Decision: delete leftover branch `task/p0-004-repo-hygiene-dispatch` only after confirming it has no unique commits.
- Scope: readiness planning, task ledger, current-state sync, and implementation gate definition only.
- Not a product-code approval.
- Not a Phase 1A implementation approval.
- Next user gate: whether `docs/plans/phase1a-manual-url-quick-capture-readiness-2026-05-03.md` may become the basis for `T-P1A-001`.

## 2026-05-03 — T-P0-007 readiness pack closed after external audit

- Decision: close `T-P0-007` as docs-only readiness pack after GPT Pro external audit.
- PR: `https://github.com/RayWong1990/ScoutFlow/pull/6`
- Branch: `task/T-P0-007-phase1a-readiness`
- Reviewed commit: `40aa2f325bf5defe9fad9427fd0c8a006bf84436`
- GitHub Actions run: `25276308045`; docs-smoke=`success`
- Audit conclusion: PASS — no blocking issue.
- Scope: Phase 1A Bilibili `manual_url` quick_capture readiness planning only.
- Not a product-code approval.
- Not a Phase 1A implementation approval.
- Next gate: user decides whether to merge PR `#6` and whether to authorize `T-P1A-001`.

## 2026-05-03 — PR #6 merged after readiness approval

- Decision: user approved merge of PR `#6`.
- Merge commit: `cc649030437dfab1ea52f062d454c1da789703c5`
- Scope: merge readiness pack and `T-P1A-001` draft dispatch into `main`.
- Not a direct approval for broader Phase 1A scope beyond the explicit `T-P1A-001` defaults.

## 2026-05-03 — T-P1A-001 authorized as first Phase 1A code-bearing task

- Decision: user approved PR `#6` readiness pack and authorized `T-P1A-001`.
- Scope: Bilibili `manual_url` quick_capture, `metadata_only only`.
- Explicit non-goals: `audio_transcript` runtime, workers, browser automation, `recommendation / keyword / RAW gap` direct capture, Phase 2-4 runtime.
- Required validation: docs-check, API tests, LP-001 rejection tests, redaction tests, platform_result enum tests.

## 2026-05-03 — T-P1A-002 dispatch execution authorized

- Decision: user authorized executing `/Users/wanglei/Downloads/dispatch-t-p1a-002-api-jobs-receipt-ledger.md`.
- Branch: `task/T-P1A-002-api-jobs-receipt-ledger`.
- Scope: API-side `POST /jobs/{job_id}/complete`, receipt validation, `jobs` / `job_events` minimum schema, and `artifact_assets` ledger mapping.
- Non-goals: workers, BBDown / yt-dlp / ffmpeg invocation, ASR, `audio_transcript` runtime, browser automation, Phase 2-4 runtime.
- Local validation verdict: `verdict=clear` for the full dispatch command set.
- PR: `https://github.com/RayWong1990/ScoutFlow/pull/9`
- Pre-audit GitHub Actions run after PR `#9` head update: `25277857106`; `docs-smoke=pass`; `api-contract-tests=pass`; superseded by Dispatch B audit-fix.

## 2026-05-03 — T-P1A-002 Dispatch B audit-fix authorized

- Decision: user authorized executing `/Users/wanglei/Downloads/dispatch-b-t-p1a-002-pr9-rebase-auditfix-cn.md`.
- Scope: clean PR `#9` diff against latest `origin/main`, remove T-P1A-004 pollution from PR `#9`, and add merge-blocking audit fixes for receipt / ledger contracts.
- PR `#8` status at start: open, not merged; therefore PR `#9` must not carry T-P1A-004 safety files as its own diff.
- Local audit-fix validation verdict: `verdict=clear`; `python -m pytest tests/api tests/contracts -q` -> `42 passed`.
- GitHub Actions run: `25278781456`; `docs-smoke=success`; `api-contract-tests=success`
- Non-goals unchanged: workers, BBDown / yt-dlp / ffmpeg invocation, ASR, `audio_transcript` runtime, browser automation, frontend, Phase 2-4 runtime.

## 2026-05-03 — T-P1A-003 research note recorded on GitHub

- Record: `T-P1A-003` BBDown tool-surface research note is recorded in draft PR `#10`.
- PR: `https://github.com/RayWong1990/ScoutFlow/pull/10`
- Branch: `task/T-P1A-003-bbdown-tool-surface-research`
- Head commit: `42baf4165d7bf9022a9e8742d989a7428ae3ee4b`
- GitHub Actions run: `25278481839`; `docs-smoke=success`; `api-contract-tests=success`
- Scope: `docs/research/t-p1a-003-bbdown-tool-surface-research-2026-05-03.md` only.
- Boundary: not authority; not implementation approval; no runtime capture; no BBDown execution; no docs/task authority writeback.
- Remaining gate: keep as draft research note unless user explicitly approves draft spec extraction.

## 2026-05-03 — PR #9 merged after Dispatch B audit-fix

- Decision: merge PR `#9` after audit-fix and verification.
- PR: `https://github.com/RayWong1990/ScoutFlow/pull/9`
- Reviewed head: `7e54ec0d0b1a8aae5fcd041b02a6f1f56ac28e97`
- Merge commit: `1449f0d753c2da1476178f99934cf66c3add372c`
- GitHub Actions run: `25278781456`; `docs-smoke=success`; `api-contract-tests=success`
- Local validation: `python -m pytest tests/api tests/contracts -q` -> `42 passed`
- Scope: API-side receipt endpoint, receipt validation, `jobs` / `job_events` minimum schema, artifact ledger mapping, idempotency / DB guard hardening.
- Boundary: no workers; no BBDown / yt-dlp / ffmpeg invocation; no ASR; no `audio_transcript` runtime; no frontend; no Phase 2-4 runtime.

## 2026-05-03 — PR #8 merged after rebased safety baseline

- Decision: rebase PR `#8` onto the new `main`, drop stale authority-ledger sync commit, keep only the safety baseline itself, then merge.
- PR: `https://github.com/RayWong1990/ScoutFlow/pull/8`
- Rebased head: `7c74233095c3c297d4634a7e342547830d77bf32`
- Merge commit: `4f6af1ce3d823c84fc8f38cefee0790ec1830c62`
- GitHub Actions run: `25279195327`; `docs-smoke=success`; `api-contract-tests=success`
- Local validation: `python -m pytest tests/contracts -q` -> `25 passed`; `python -m pytest tests/api tests/contracts -q` -> `50 passed`
- Scope: text redaction, secret scan, CI hardening, contract tests, and raw-response redaction safety docs.
- Boundary: no BBDown / yt-dlp / ffmpeg runtime; no workers; no frontend; no downloads; no credentials; no `audio_transcript` runtime.

## 2026-05-03 — Dispatch 0 human-gate sync after PR #10

- Decision: merge PR `#10` as `docs/research/**` research note only.
- PR: `https://github.com/RayWong1990/ScoutFlow/pull/10`
- PR head: `42baf4165d7bf9022a9e8742d989a7428ae3ee4b`
- Merge commit: `8328c567e26db118ad456b29f8616066174b3568`
- GitHub Actions run: `25280084928`; `docs-smoke=success`; `api-contract-tests=success`
- Boundary: PR `#10` is not authority, not implementation approval, and not runtime approval.
- Decision: user approves extracting `docs/specs/bbdown-adapter-contract-draft.md` from the research note under `T-P1A-006`.
- Boundary: the draft spec must remain `draft / not final authority / not runtime approval`.
- Decision: future direction may reuse BBDown and may later consider BBDown / ffmpeg / ASR by staged tasks.
- Decision: user prefers BBDown as the likely Bilibili main adapter direction, rather than staying indefinitely at abstract research.
- Decision: this is personal local development, not public SaaS; privacy/compliance risk is treated as low for this project shape.
- Boundary: cookie / token / secret material must not enter Git, PRs, CI, logs, DB artifacts, or tracked files.
- Decision: manual-auth / local-only auth design may be considered later, but requires an explicit future contract.
- Decision: Explore URL paste, risk prompts, and receipt status display require separate user brainstorm under `T-P1A-007`.
- Task sync: `T-P1A-003=done`; `T-P1A-006=active`; `T-P1A-007=active`; `T-P1A-008=backlog/gated`; `T-P1A-009=backlog/gated`.
- Non-goals unchanged: no workers, no frontend, no real download, no ASR, no browser automation, no `audio_transcript` runtime, no Phase 2-4 runtime.

## 2026-05-03 — PR #12 merged after Dispatch 0 authority sync

- Decision: merge PR `#12` to close `T-P1A-005`.
- PR: `https://github.com/RayWong1990/ScoutFlow/pull/12`
- Reviewed head: `e10c9fc3808668fd34b6dc2150db151186640743`
- Merge commit: `419546de000f4a163d4158f2ced9784ba263c09c`
- GitHub Actions run: `25280435814`; `docs-smoke=success`; `api-contract-tests=success`
- Scope: authority sync only across `AGENTS.md`, `README.md`, `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, `docs/specs/contracts-index.md`
- Task sync: `T-P1A-005=done`; `T-P1A-006=active`; `T-P1A-007=active`; `T-P1A-008=backlog/gated`; `T-P1A-009=backlog/gated`
- Non-goals unchanged: no runtime approval; no BBDown / yt-dlp / ffmpeg / ASR execution; no workers; no frontend; no browser automation; no `audio_transcript` runtime

## 2026-05-04 — PR #20 merged after close hardening

- Decision: user authorized Codex to merge PR `#20`.
- PR: `https://github.com/RayWong1990/ScoutFlow/pull/20`
- Head commit: `89ac13dc0c29bc3fffd5d2d6e9f31736af968af1`
- Merge commit: `f10226fc6cd7724f7af7bd410ed8022ecb500a69`
- Scope: `T-P1A-009` close wording hardening only.
- Boundary: PR `#19` remains historical report-only spike; `BBDown --version` attempt and unexecuted `-info` are not reusable runtime permission; no `audio_transcript` approval.

## 2026-05-04 — Wave 1 ledger opened

- Decision: open Wave 1 ledger as `T-P1A-010`.
- Active tasks: `T-P1A-010A` BBDown executable discovery / tool preflight package; `T-P1A-010B` BBDown no-auth `-info` adapter shell with injected runner and parser integration; `T-P1A-010C` PRD/SRD amendment repair pack + next dispatch plan + red-team checklist.
- Active count: `3/3`; Review count: `0`.
- Ledger rule: coding PRs for `T-P1A-010A` and `T-P1A-010B` must not independently edit `docs/current.md` or `docs/task-index.md`; they should provide status text for the ledger owner to write back.
- Boundary: no real BBDown execution, no media download, no ffmpeg, no ASR, no browser automation, no credentials, no browser profile, no Phase 2-4 runtime, and no authority override beyond draft amendments.

## 2026-05-04 — Wave 1 PRs merged after 05 red-team

- Red-team verdict: `PASS_WITH_FIXES`.
- Decision: accept non-blocking PR body fixes, then merge PR `#23`, PR `#22`, and PR `#24` in that order.
- PR `#23`: `T-P1A-010A BBDown tool preflight package`; head=`155e0b8a2910e81fc26625dd3be4391ab792e289`; merge commit=`0b5d4350c4dad3ebae3d594245ddfcfb65a22f91`; workflow run=`25284770283`; docs-smoke=`success`; api-contract-tests=`success`.
- PR `#22`: `T-P1A-010B BBDown info adapter shell`; head=`73bc85443241c336d03bf74c5cef5a676a9a4957`; merge commit=`b6a23a9d46c94e07974404d7eec19ba2dffe7092`; workflow run=`25284816246`; docs-smoke=`success`; api-contract-tests=`success`.
- PR `#24`: `T-P1A-010C PRD SRD amendment repair pack`; head=`02ab26ebf8e966b7af30abc90d8a56733f1c636e`; merge commit=`297d286a13b8d60d9627db80925289fb85674a8a`; workflow run=`25284792684`; docs-smoke=`success`; api-contract-tests=`success`.
- Wave 1 state: `closed`; `T-P1A-010A=done`; `T-P1A-010B=done`; `T-P1A-010C=done`; Active count=`0/3`; Review count=`0`.
- Contract note: `ToolPreflightResult` / `PlatformResult` separation entered code and candidate amendment docs; `executable_not_found` remains tool preflight evidence, not `PlatformResult`.
- Boundary: no-auth `-info` adapter shell is not live runtime proof; it uses injected runner / parser contract coverage only.
- Boundary: PRD/SRD v1.2 amendment remains `candidate / draft / not final authority / not runtime approval`.
- Boundary: `audio_transcript` remains blocked; no live BBDown, QR/manual auth, media download, ffmpeg, ASR, workers, frontend, or Phase 2-4 runtime approval.
- Next gate: `T-P1A-011 live no-auth BBDown -info probe` remains `gated / requires explicit user approval`; 06 must not auto-start.

## 2026-05-04 — T-P1A-011B manual-auth QR local-only gate executed

- Decision: user explicitly requested `执行07`, which is treated as execution approval for `T-P1A-011B`.
- Scope: local-only `BBDown login` gate only; no `BBDown -info`; no media; no ffmpeg; no ASR; no receipt / artifact ledger / capture state.
- Execution boundary:
  - use repo-external local-only executable/auth store
  - use repo-external temp cwd for QR display
  - do not use browser profile
  - do not use command-string credentials
  - do not use `--debug`
- Observed lesson: with local BBDown `1.6.3`, `qrcode.png` may be written to cwd and `BBDown.data` / `BBDownTV.data` may be written next to the executable, so repo-local executable/cwd are not acceptable for this gate.
- Result: QR displayed locally, user completed scan, safe tool output confirmed auth completion, temp QR cwd cleaned, auth sidecar stayed outside Git.
- Boundary: this does not approve no-auth or auth-present `BBDown -info`, does not emit `PlatformResult`, and does not approve broader runtime.

## 2026-05-04 — T-P1A-011C auth-present metadata probe executed with parser repair

- Decision: user explicitly authorized a new metadata probe gate after `T-P1A-011B`.
- Scope: single authorized sample URL, repo-external local-only executable/auth store, repo-external temp cwd, one `BBDown -info`, redaction, parser classification only.
- Observed blocker: real `BBDown 1.6.3` output caused two direct parser mismatches:
  - benign login-status lines triggered false `auth_required`
  - real Chinese lines such as `获取aid结束`, `视频标题`, `P1: [...] [07m10s]`, and `共计 1 个分P` were not parsed into typed fields
- Decision: repair `services/api/scoutflow_api/external_tools/bbdown_info_parser.py` and add regression coverage in `tests/contracts/test_bbdown_info_parser_contract.py` within the same task, because parser drift was the immediate blocker to a truthful gate result.
- Result after repair: `platform_result=ok`; parsed fields include `platform_item_id=116493572377107`, title, duration `430`, page count `1`, selected page `P1`; no media files created in temp tree.
- Boundary: this still does not approve receipt / artifact ledger / capture state, media download, ffmpeg, ASR, or `audio_transcript`.

## 2026-05-04 — T-P1A-011D second retro triage recorded

- Decision: pre-08 retro / remediation keeps the `T-P1A-011D/E/F/G/H` namespace; `T-P1A-012` stays Dispatch `08`, `T-P1A-013` stays Dispatch `09`.
- Decision: the success evidence source for patched Dispatch `08` is `T-P1A-011C`, not blocked `T-P1A-011`.
- Decision: before `08`, only the minimal retro scaffold, prompt patch, and sidecar review are kept; no 19-file remediation package.
- Boundary: legal/vendor external facts stay candidate-only unless later verified.

## 2026-05-04 — Minimal retro skeleton added

- Decision: add a minimal `docs/retro/` scaffold after the second deep review.
- Scope: `README` + three templates + first week retro only.
- Boundary: not authority, not PRD/SRD amendment, not vendor/legal policy, not runtime approval.
- Next: patched Dispatch `08` evidence-consumption wiring, then `T-P1A-012R` retro after real `08` work.

## 2026-05-04 — Patched Dispatch 08/09 pack accepted as working input

- Decision: keep the repo-external patched Dispatch `08/09` prompt files as the working input pack.
- Decision: Dispatch `08` consumes existing `T-P1A-011C` redacted metadata evidence only; it does not re-run BBDown.
- Decision: Dispatch `09` must preserve the layering `probe evidence != receipt ledger != capture state != media/audio readiness`.
- Boundary: external patched prompt files are not GitHub authority by themselves; repo authority remains in `docs/current.md`, `docs/task-index.md`, and `docs/decision-log.md`.

## 2026-05-04 — T-P1A-011G sidecar review closed with PASS_WITH_FIXES

- Decision: review verdict is `PASS_WITH_FIXES`.
- Minimal fix: sync `AGENTS.md`, `README.md`, `docs/current.md`, `docs/task-index.md`, and this log from the stale `011C` end-state to `07.x remediation complete`.
- Dispatch `08` readiness: `ready`.
- Dispatch `09` readiness: `ready`.

## 2026-05-04 — T-P1A-012 metadata receipt wiring completed

- Decision: execute patched Dispatch `08` against the existing `T-P1A-011C` auth-present metadata evidence only.
- Scope: add a `metadata_probe_receipt_bridge` helper, materialize safe evidence files, and bridge them into the existing `/jobs/{job_id}/complete` + `artifact_assets` baseline.
- Implementation boundary: no BBDown runtime, no new `BBDown -info`, no media download, no ffmpeg, no ASR, no manual auth, no browser profile, no `audio_transcript`, no frontend / workers.
- Contract hardening: `metadata_fetch` receipts now only allow `raw_api_response`, `metadata_probe_summary`, and `safe_metadata_evidence`; safe metadata written to ledger now includes `evidence_source_task_id`, `evidence_source_report_path`, and `probe_mode`.
- Evidence boundary: success evidence must stay `T-P1A-011C auth-present`; blocked `T-P1A-011` must not be treated as success evidence.
- Next: `T-P1A-012R` receipt-wiring retro, then patched `T-P1A-013` Trust Trace.

## 2026-05-04 — T-P1A-012R retro completed

- Decision: keep `08.1` for now.
- Reason: this retro was concrete enough to separate “tests proved receipt mapping” from “runtime readiness”, so the ceremony tax paid for itself in this case.
- Boundary: `012R` does not change product code, receipt rows, artifact ledger, or runtime approval.

## 2026-05-04 — T-P1A-013 Trust Trace API surface completed

- Decision: execute patched Dispatch `09` in `API/CLI` mode, not frontend mode.
- Scope: add `GET /captures/{capture_id}/trust-trace` and keep `probe evidence`, `receipt ledger`, `capture state`, and `media/audio readiness` as separate layers.
- Surface rule: before receipt exists, keep label `Status / Trust Trace / 采集状态`; after receipt ledger exists, allow `Receipt / Ledger Trace`.
- Boundary: no recommendation semantics, no BBDown runtime, no manual auth, no media / ffmpeg / ASR, no `audio_transcript`, no frontend / workers.
- Result: Trust Trace now exposes safe summary only, labels `auth-present` evidence correctly, and keeps media/audio as `not_approved`.

## 2026-05-04 — T-P1A-013A receipt / trust trace audit hardening completed

- Decision: close the two post-merge audit gaps before any future worker/runtime lane.
- Fix 1: metadata bridge materialization now validates path containment before writing, so malicious `PreparedMetadataProbeAsset.relative_path` cannot escape capture root.
- Fix 2: current-phase generic metadata-fetch receipts can no longer treat blocked `T-P1A-011` or `probe_mode=no-auth` as success evidence for `safe_metadata_evidence` / `metadata_probe_summary`.
- Boundary: no runtime, no media / ffmpeg / ASR, no manual auth, no browser profile, no frontend / workers.
- Result: Trust Trace layering remains unchanged while the generic API path now matches the bridge-level safety contract.

## 2026-05-04 — T-P1A-013B authority/docs-check hardening completed

- Decision: fix the stale `T-P1A-013A active` line in `docs/current.md` instead of carrying that contradiction into the next lane.
- Decision: upgrade `tools/check-docs-redlines.py` so suffix task IDs are parsed exactly (`011D/E/F/G`, `012R`, `013A/B`) rather than truncated.
- Decision: add current-doc self-checks so `Active count=0/3` plus a later concrete `状态 active` line is rejected by docs-check.
- Boundary: no product code, no API/runtime expansion, no BBDown, no media / ffmpeg / ASR, no frontend / workers.

## 2026-05-04 — T-P1A-014 lean constraints cleanup completed locally

- Decision: accept the lean cleanup direction for local PR execution: entry docs are shortened, contracts collapse from 19 separate IDs into 8 groups with old aliases preserved, and hard LPs collapse from 7 to 4.
- Decision: Active lane wording changes from generic "activity max 3" to `Active product lane max=3 + Authority writer max=1`; review / audit / research lanes do not count as product lanes unless they write authority.
- Decision: drop / relax / absorb details are recorded in `docs/retro/2026-05-04-lean-cleanup.md`.
- Boundary preserved: no product runtime, no schema/state-machine change, no receipt schema change, no PlatformResult enum change, no redaction contract body change, no Trust Trace DTO change.
- Gate: GPT Pro quick external audit and PR merge are still required before `T-P1A-015` or `T-P1A-016` may start.

## 2026-05-04 — T-P1A-014 GPT Pro external audit accepted

- Decision: external audit verdict is `PASS WITH NOTES`; no blocking issue found for scope, CI, hard boundaries, lane protocol, LP reduction, contract groups, or entry slimming.
- Fix: apply the non-blocking wording repair in `docs/specs/contracts-index.md` so the first-screen summary no longer mixes product architecture with the contract-group authority view.
- Next gate: merge PR `#33`, then keep `T-P1A-015` / `T-P1A-016` behind explicit user authorization.

## 2026-05-04 — PR #33 merged and T-P1A-015 unlocked

- Decision: merge PR `#33` into `main` as merge commit `f1b4992398d89eb3742a57a585ee9378ad6266b5`.
- Decision: `T-P1A-015` is now unlocked by merged `T-P1A-014`; `T-P1A-016` still requires an explicit user gate.

## 2026-05-04 — T-P1A-015 PRD/SRD promote completed locally

- Decision: promote PRD/SRD base docs to `docs/PRD-v2-2026-05-04.md` and `docs/SRD-v2-2026-05-04.md`.
- Decision: move v1 + amendment chain into `docs/archive/` and add `docs/archive/README.md` for mapping stability.
- Decision: switch forward authority references to v2 and historical trail references to archive paths.
- Boundary preserved: no product code, no runtime approval, no schema change, no spec contract semantics rewrite.

## 2026-05-04 — T-P1A-016 dispatch template extracted

- Decision: extract shared dispatch boilerplate to `docs/dispatch-template.md`.
- Decision: add `docs/runbooks/dispatch-authoring-guide.md`.
- Decision: compress dispatch self-audit from 7-8 segments to 5 segments: Scope / Authority / Safety / Validation / Next gate.
- Decision: existing user-managed dispatch files under `~/Downloads/` are not retroactively rewritten.
- Scope: docs-only meta-template extraction.
- Boundary: no product code, no PRD/SRD/LP/spec contract changes, no runtime approval.

## 2026-05-04 — T-P1A-015 audit-fix after T-P1A-016 merge

- Decision: rebase `T-P1A-015` after PR `#34` merge and absorb the `T-P1A-016` ledger update as the single authority writer.
- Fix: PRD v2 metadata probe wording now states the current success evidence is `T-P1A-011C auth-present metadata probe`; no-auth live platform success remains not proven.

## 2026-05-04 — T-P1A-017 Wave 2 ledger open

- Decision: open Wave 2 by registering three product lanes and five research/backlog lanes.
- Product lanes (Active count `3/3`): T-P1A-018 `metadata_fetch job enqueue API`; T-P1A-019 `metadata probe dry-run orchestrator`; T-P1A-020 `Trust Trace / Explore contract hardening`. Sequencing: 018 → 019 → 020 (storage layer first, then orchestration, then contract hardening).
- Research/backlog lanes (not product active; not runtime approval): T-P1A-021 BBDown runtime gate matrix; T-P1A-022 ASR pipeline prestudy; T-P1A-023 LLM normalization schema; T-P1A-024 Explore wireframe + state table; T-P1A-025 DB / evidence ledger vNext proposal.
- Conflict domain table locked in `docs/task-index.md` Wave 2 section: T-P1A-018 owns `storage.py`/`captures.py`/`jobs.py`/`main.py`/`test_jobs_complete.py`/`test_captures_discover.py`; T-P1A-019 owns `external_tools/**`/`orchestration/**`/`metadata_probe_receipt_bridge.py`; T-P1A-020 owns `test_capture_trust_trace.py`; `migrations/**` FORBIDDEN for all lanes.
- Authority writer slot [L4]: T-P1A-017 / T-P1A-026 each occupy Authority writer slot 1/1 during execution; no concurrent authority writer permitted on `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md`.
- Merge gate: PR must include user-approved lane plan sign-off before merge; T-P1A-018/019/020/021/022/023/024/025 must not start writing files before T-P1A-017 PR merges.
- No runtime / worker / frontend / ASR / `audio_transcript` approval granted by this ledger-open PR.
- Boundary: docs-only authority update; no product code, no schema changes, no migrations, no BBDown execution.
- Fix: path-only reference maintenance exceptions are formally recorded in `docs/retro/2026-05-04-prd-srd-promote.md`.

## 2026-05-04 — Post-T-P1A-018 merge ledger sync

- Decision: mark T-P1A-018 (metadata_fetch job enqueue API + OpenAPI UX audit-fix) as `done`. PR `#39` merged into `main` as merge commit `a1f965bdf22d027f173683ae324d2b2acd0a9f19`.
- Decision: T-P1A-019 (metadata probe dry-run orchestrator) is the next executable lane. 018 storage / job layer is contract-frozen for the duration of 019.
- Decision: T-P1A-021 (BBDown runtime gate matrix research) merged into `main` as commit `1e283457ff55d4e552b317bdfeb4b5a454a098d9` (PR `#37`); recorded in Done as research/candidate.
- Active count update: `3/3` → `2/3` (018 done; 019 + 020 remain active).
- Boundary preserved: `migrations/**` remains FORBIDDEN for all lanes; `audio_transcript` runtime remains blocked; `PlatformResult` enum / `WorkerReceipt` schema / Trust Trace data shape unchanged across 017/018/021 closures.
- During T-P1A-019 execution: `storage.py` / `captures.py` / `jobs.py` / `main.py` are read-only (frozen 018 contract); `test_capture_trust_trace.py` reserved for T-P1A-020.
- Scope of this entry: docs-only authority sync after merge — no product code, no schema, no migrations, no runtime change.
