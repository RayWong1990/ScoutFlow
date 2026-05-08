# Decision Log

> 薄版决策日志。只记录已经 user 拍板的工程/产品决策，不替代 PRD/SRD。

## 2026-05-08 — Phase 1 Remediation Sub-wave Lane Open (post Opus-2 Visual REJECT, post Codex critique on v2)

- 触发: Opus-2 Visual Truth Audit verdict `VISUAL_REJECT (3.6/10)`，`VT-P0-01/02/03` + `VT-P1-01/02/03` + `VT-P2-01/02` 全部 stop-line。
- v3 修订 (vs v2): Codex critique 6 条全采纳 — delete Active 4 amendment / delete Playwright / Bat-Prep docs-only / 加 Lane D explicit user gate / Opus-3 V-PASS-CLEAR closeout / 加 Commander Monitor。
- Lane 占用 (Active 3 不动): D + B + C。Lane A 在 Blocked 表，blocked-by visual truth remediation；`PR-B / Round 3` 再 promote A 替换 D。
- 边界: 不解禁 runtime / true write / migration / browser automation / dependency install。master spec §13 全 Hold 仍在（含 `browser_automation`，含 `dbvnext_migration`）。`write_enabled=False` 不变。
- 派单 pack 路径: `~/workspace/raw/05-Projects/ScoutFlow/dispatches/RUN-2026-05-08-NIGHT/remediation-wave/`（raw PARA，非 git tracked）。
- Closure: `PR-A / Round 1` + `Round 2` 7 窗 + `PR-B / Round 3` + `Round 3` Lane A + `Round 4` 战友 localhost `V-PASS` + `Round 5` Opus-3 `V-PASS-CLEAR` + `PR-C / Round 6` closeout。

## 2026-05-08 — Authority rebase after PR #253 / #254 / #255 merged

- Decision (1): refresh live authority anchor to `origin/main = e18d45a` (`PR #254`, merged at `2026-05-08T05:04:01Z`); current first-parent merged chain snapshot = `e18d45a` (`#254`) ← `d0dcbfe` (`#255`) ← `cf283f9` (`#253`) ← `02ccbdc` (`#252`).
- Decision (2): absorb `PR #253 / cf283f9` as the missing Layer C closeout for `T-P1A-156 / W2C`; this PR did not open a new product lane.
- Decision (3): absorb `PR #255 / d0dcbfe` as `T-P1A-157 / W1B PF-C4-EXT` landed and closed; Active product count remains `0/3`, and there is no currently open code-bearing lane.
- Decision (4): absorb `PR #254 / e18d45a` as `W3E PF-C0-O1` docs-only candidate starter cluster landed on `main`; it remains candidate-only and does not consume an active product slot.
- Decision (5): capture-station authority baseline is no longer “W2C data shell only”; it is now `W2C truthful runtime surfaces + W1B trust-trace graph/timeline/error-path bounded lanes landed`.
- Decision (6): live refresh snapshot at writeback time = `merged PR 248 / open PR 0`; this is a refresh-time snapshot only, and future truth must continue to come from live GitHub checks.
- Decision (7): 5 overflow lanes remain Hold; `write_enabled=False` remains hard truth; no runtime / migration / browser automation / vault true write / full-signal execution approval is granted by this rebase.

## 2026-05-08 — T-P1A-157 W1B lane opened after W2C closeout

- Decision: open `T-P1A-157` as the current active code-bearing lane after `T-P1A-156 / W2C` closed.
- Scope: `apps/capture-station/src/features/trust-trace/**` bounded graph / timeline / error-path implementation, plus W1B receipts, scope note, and carry-forward doc sync.
- Boundary: `path-A self-rolled only`; `d3` fallback remains blocked until evidence + Hermes + user gate.
- Boundary: no backend DTO / enum / receipt schema change; no runtime / browser / vault / migration unlock.
- W3E PF-C0-O1 remains docs-only candidate work and does not consume an active product slot.

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

## 2026-05-04 — T-P1A-025 frozen as merged research; research backlog rows synced

- Decision: merge PR `#42` and freeze `docs/research/t-p1a-025-db-ledger-vnext.md` as research input only.
- PR: `https://github.com/RayWong1990/ScoutFlow/pull/42`
- Merge commit: `7a120f22efbf4e5455ad96a0c5cffb796c433c31`
- Scope: `docs/research/t-p1a-025-db-ledger-vnext.md` only.
- Boundary: not authority; not migration approval; not runtime approval.
- Rule: no further edits to the frozen research note; any DB decision evolution must land in `docs/specs/db-vnext-design-2026-05-04.md`, the later SRD amendment, or an explicit amendment addendum.
- Decision: close stale `research/backlog` rows for `T-P1A-022/023/024/025` in `docs/task-index.md`, because all four research notes are already merged on `main` and should now be treated as frozen research inputs rather than mutable backlog.
- Merge facts:
  - `T-P1A-022`: PR `#38`, merge commit `ed81b3a066e78dae25f8e4a7ca8dd69c0d08c0d9`
  - `T-P1A-023`: PR `#45`, follow-up wording fix PR `#46`, final merge commit `d23abee7fc2daac234f2bad69689309ad855bf67`
  - `T-P1A-024`: PR `#40`, merge commit `05c545a6c17d8006d113f7c39a5179d9c057540c`
  - `T-P1A-025`: PR `#42`, merge commit `7a120f22efbf4e5455ad96a0c5cffb796c433c31`
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

## 2026-05-04 — Post-T-P1A-019 merge ledger sync

- Decision: mark T-P1A-019 (metadata probe dry-run orchestrator) as `done`. PR `#44` merged into `main` as merge commit `44e87a147ba6ba962731757c9d99baf40fcf0dd3`. Audit-fix commit `6dead72` addressed Opus PR-#44 review (P0-1 provenance gate URL-derived BV id vs probe.platform_item_id; P0-2 failure receipt path for non-ok platform_result).
- Decision: T-P1A-020 (Trust Trace / Explore contract hardening) is the next executable lane. T-P1A-019 orchestration / external_tools / bridge contract is now frozen for the duration of 020.
- Active count update: `2/3` → `1/3` (019 done; 020 remains active).
- Bridge extension: `build_metadata_fetch_failure_receipt` added in `services/api/scoutflow_api/metadata_probe_receipt_bridge.py` within T-P1A-019 allowed paths. Emits `WorkerReceipt` with `produced_assets=[]`, `platform_result=<non-ok>`, `next_status="metadata_fetched"`. Storage gates capture-state advance on `job_status=succeeded`, so failure receipt: job→failed, capture→discovered (unchanged), `receipt_ledger.present=false`.
- Boundary preserved: `migrations/**` remains FORBIDDEN for all lanes; `audio_transcript` runtime remains blocked; live BBDown / yt-dlp / ffmpeg / ASR / browser automation remain blocked; `subprocess.run` not invoked by orchestrator (tripwire test); `PlatformResult` enum / `WorkerReceipt` schema / Trust Trace DTO shape unchanged across 019 closure.
- During T-P1A-020 execution: `storage.py` / `captures.py` / `jobs.py` / `main.py` remain read-only (018 contract frozen); `external_tools/**` / `orchestration/**` / `metadata_probe_receipt_bridge.py` remain read-only (019 contract frozen).
- Ledger note: research lanes T-P1A-022/023/024 produced research notes that landed on main during the 019 cycle; their task-index status currently remains `research/backlog` (status allows research notes; promotion to `done` deferred to a subsequent housekeeping sync to keep this entry scoped to 019/020).
- Scope of this entry: docs-only authority sync after merge — no product code, no schema, no migrations, no runtime change.

## 2026-05-04 — T-P1A-027 Wave 2 Authority Ledger Reconciliation

- Decision: close Wave 2 in authority surfaces after PR #51 merged.
- Scope: ledger-only authority reconciliation; no product code, no schema, no migration, no runtime.
- Closed lanes:
  - `T-P1A-020` Trust Trace / Explore contract hardening — main PR `#43` (merge commit `6d959ab`), follow-up invariants PR `#49` (merge commit `8694c06`); PR `#48` superseded by PR `#49` with no semantic delta (stacked-base squash artifact); 5-state Trust Trace snapshot contract frozen; no `storage.py` change.
  - `T-P1A-026` SRD-v3 candidate amendment for DB vNext — PR `#51` (merge commit `fdf0673`); ID-reuse user-authorized: original dispatch 26 "Wave 2 ledger close" scope substituted with Stage 2 SRD-v3 candidate authoring at user direction; ledger-close functionality fulfilled by T-P1A-027 (this PR).
- Cleanup: removed stale `T-P1A-021` Backlog/Research row (was dual-registered against Done; closeout drift).
- Reset: Active count `1/3` → `0/3`; Wave 2 Conflict Domain table retained as historical reference only.
- Parallel Lane Identity:
  - `T-P1A-027` (S0, this PR) = sole ledger authority writer; occupies Authority writer slot 1/1; writes `docs/current.md` / `AGENTS.md` / `docs/task-index.md` / `docs/decision-log.md` / `docs/specs/contracts-index.md`.
  - `T-P1A-028` (S1) = candidate-contract writer; does NOT occupy ledger authority writer slot; does NOT write any of the five ledger authority files; touches only `docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md` and `docs/specs/db-vnext-design-2026-05-04.md`.
  - File-domain zero overlap → S0/S1 真并行 OK.
- Boundary: `audio_transcript` runtime / BBDown live / ffmpeg / ASR / `migrations/**` / workers / frontend remain blocked; `PlatformResult` enum / `WorkerReceipt` schema / Trust Trace DTO unchanged.
- Sequencing gate: a third execution window that reads current state from main must NOT start until S0 merges (avoid stale `current.md` propagation).
- Next gate: after S0 + S1 both merge, user explicit gate required for Phase 2A migration dry-run plan or any Wave 3 candidate.
- Known follow-up debt (not addressed by S0/S1):
  - F-010: `WorkerReceipt.next_status="metadata_fetched"` semantics on failure receipts (currently set but ignored when `job_status=failed`) — defer to Phase 2A migration prep.
  - F-012: `PRAGMA foreign_keys=ON` not enabled in `Storage._connect()` — Phase 2A migration approval blocked until enabled (S1 records this as hard gate; not a code change here).

## 2026-05-04 — T-P1A-029 Post-S0/S1 Authority + Candidate Wording Fix

- Decision: close PR #52/#53 merge aftermath before any Phase 2A migration dry-run plan.
- Scope: authority + candidate wording only; no product code, no schema migration, no runtime, no credentials.
- Authority sync:
  - `T-P1A-027` PR `#52` merged as `c2bcac0`; recorded in Done.
  - `T-P1A-028` PR `#53` merged as `c1c2565`; recorded in Done.
  - `docs/current.md`, `AGENTS.md`, and `docs/specs/contracts-index.md` now reflect S1 merged state instead of "wait for S1".
- Candidate fix:
  - F-012 wording narrowed: SQLite FK / `ON DELETE RESTRICT` / composite FK guards depend on `PRAGMA foreign_keys=ON`; storage CHECK clauses and triggers remain enforced independently.
  - Evidence identity columns `capture_id` / `evidence_kind` / `lineage_variant` are declared immutable after insert via `trg_evidence_identity_columns_immutable`, closing the inbound supersession target-lineage mutation gap.
- Boundary preserved: SRD-v3 candidate remains candidate-only; not promoted authority; not migration approval; not runtime approval.
- Next gate: user explicit authorization required for Phase 2A migration dry-run plan or any Wave 3 candidate.

## D-001: doc3 PR55-PR74 顺延为 PR56-PR75 (T-P1A-031 ~ T-P1A-050)

- 日期: 2026-05-04
- PR: #56 (本 PR)
- 决议: `docs/research/pr55-pr74-worklist-candidate-2026-05-04.md` §1-§20 中列举的 PR55-PR74（T-P1A-030 ~ T-P1A-049）在执行编号上统一顺延 +1，实际为 PR56-PR75（T-P1A-031 ~ T-P1A-050）。
- 原因: PR #55 已被 T-P1A-030 Wave 3 reference docs landing 占用（merge commit `395a7e6`）；doc3 §1（原 PR55）顺延为本 PR（PR #56）。
- 适用范围: 后续每个 dispatch header 引用 doc3 §N 时用“顺延后 PR{N+1}（原 doc3 §M PR{N}）”双标记；doc3 文件本身不修订。
- 引用: `docs/research/pr55-pr74-worklist-candidate-2026-05-04.md`；`${SCOUTFLOW_VAULT_ROOT}/05-Projects/ScoutFlow/dispatches/PR55-T-P1A-030-wave3-refdocs-landing.md` pr_numbering_note；`${SCOUTFLOW_VAULT_ROOT}/05-Projects/ScoutFlow/dispatches/PR56-T-P1A-031-wave3a-ledger-open.md`。

## D-002: Wave 3A open — V3 acceptance + amendments + shoulder scan

- 日期: 2026-05-04
- PR: #56 (本 PR / T-P1A-031)
- 决议: 启动 Wave 3A；范围 = 顺延后 PR56-PR67（12 PR，T-P1A-031 ~ T-P1A-042）；内容 = ledger open + ADR-001 vault lock + PRD/SRD candidate amendments + shoulder scan + PR factory tooling plan + Wave 3A closeout。
- 不解禁: 任何 runtime（`audio_transcript` / BBDown live / yt-dlp / ffmpeg / ASR / browser automation 全部仍 blocked）。
- 不修改: `PRD-v2-2026-05-04.md` / `SRD-v2-2026-05-04.md` base authority；`docs/specs/contracts-index.md` / `docs/specs/locked-principles.md` / `docs/specs/parallel-execution-protocol.md` 留给 PR60 surge + PR67 closeout。
- 引用: `docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md` §3.2；`docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md` §10；`docs/research/pr55-pr74-worklist-candidate-2026-05-04.md` §1；`docs/research/doc1-doc2-doc3-v1.1-acceptance-errata-report-2026-05-04.md`；`docs/research/opus-v3-acceptance-prd-srd-amendment-roadmap-review-2026-05-04.md`。
- 入口条件: PR54/PR55 merged；user 显式 gate（本 dispatch 即 gate）。
- 出口条件: 顺延后 PR67（T-P1A-042）Wave 3A closeout PR 完成，含 errata P0-5 contracts-index 登记。

## D-003: Wave 3A closeout + Wave 3B gate

- 日期: 2026-05-05
- PR: #67（本 PR / T-P1A-042）
- 决议: Wave 3A 完整收口。live GitHub PR 映射按事实写回：
  - `T-P1A-032=#57`
  - `T-P1A-033=#58`
  - `T-P1A-034=#64`
  - `T-P1A-035=#59`
  - `T-P1A-036=#62`
  - `T-P1A-037=#65`
  - `T-P1A-038=#60`
  - `T-P1A-039=#61`
  - `T-P1A-040=#63`
  - `T-P1A-041=#66`
- 决议: `docs/specs/contracts-index.md` 在本 closeout 中登记 Wave 3A 候选工件：ADR-001、PRD v2.1 strong visual H5 candidate、SRD v3 H5 bridge PARA vault candidate、PR Factory surge protocol candidate、PR Factory tooling plan + single-file helper。
- 决议: `docs/specs/parallel-execution-protocol.md` 同步 `Codex Commander Fan-out` 实战硬化；该同步是流程基线补丁，不代表 lane 上限升级。当前生效口径仍是 `Active product lane max=3` 与 `Authority writer max=1`。
- Go/No-Go: `GO` for `T-P1A-043 / PR #68` Wave 3B ledger open only。`PR69+` 仍受 PR68 ledger open、clone plan、以及各自前置产物约束。
- 不解禁: runtime / migration / Phase 2+ promotion 仍未批准；`audio_transcript` / BBDown live / yt-dlp / ffmpeg / ASR / browser automation 继续 blocked。
- 证据:
  - `${SCOUTFLOW_VAULT_ROOT}/05-Projects/ScoutFlow/dispatches/REPORT-PR57-PR65-CODEX0-2026-05-05.md`
  - `${SCOUTFLOW_VAULT_ROOT}/05-Projects/ScoutFlow/dispatches/REPORT-PR66-PR75-CODEX0-2026-05-05.md`

## D-004: Wave 3B open + shoulders clone plan

- 日期: 2026-05-05
- PR: #68（本 PR / T-P1A-043）
- 决议: 正式打开 Wave 3B 账本，登记 `T-P1A-044 ~ T-P1A-050` 为 backlog，并把当前 next gate 切到 `T-P1A-044 / PR #69`。
- 决议: 当前 Wave 3B clone/probe 优先顺序锁为 4 个 planned clones + 2 个 reserve：
  - planned clones: `iFurySt/RedNote-MCP`、`ShellyDeng08/rednote-analyzer-mcp`、`satnaing/shadcn-admin`、`yt-dlp/yt-dlp`
  - reserve only: `Nemo2011/bilibili-api`、`Kiranism/tanstack-start-dashboard`
- 决议: `docs/research/shoulders/clone-plan-2026-05-05.md` 与 `docs/research/shoulders/referencerepo-index-2026-05-05.md` 是本轮 tracked mirror；`referencerepo/**` 继续 local-only，不得进入 Git tracked diff。
- 决议: shoulders-index 状态推进到 `3 locked / 5 scanning / 11 discovered`。`REDNOTE-XHS`、`BILIBILI-COMPARATOR`、`CONSOLE-CLI` 继续保持 scanning 但写明 clone/probe 顺序；`YT-DLP` 从 discovered 升到 scanning；`OBSIDIAN-FRONTMATTER` 继续 scanning，等待 vault SPEC。
- 不解禁: 仍不批准 runtime / migration / apps / frontend implementation / Wave 4。

## D-005: Wave 3B closeout + Wave 4 candidate

- 日期: 2026-05-05
- PR: #75（本 PR / T-P1A-050）
- 决议: Wave 3B 完整收口。live GitHub PR 映射按事实写回：
  - `T-P1A-044=#69`
  - `T-P1A-045=#70`
  - `T-P1A-046=#71`
  - `T-P1A-047=#72`
  - `T-P1A-048=#73`
  - `T-P1A-049=#74`
- 决议: `docs/specs/contracts-index.md` 在本 closeout 中登记 Wave 3B 候选工件：Bridge route-group SPEC、H5 design package、VaultWriter SPEC、repo 外 prototype pointer、adapt decision table。
- 决议: `docs/shoulders-index.md` 状态推进到 `3 locked / 5 integrated / 11 discovered`，表示 Wave 3B 的 clone/probe/spec/design/decision 已被当前主线吸收为 candidate truth，不代表 runtime 或 code approval。
- 决议: Wave 4 not yet user-gated; ledger candidate only。
- 不解禁: runtime / migration / apps / workers / packages / Phase 2+ promotion 仍未批准。

## D-006: T-P1A-103 Wave 4 B1 control-plane repair + B2 preflight override

- 日期: 2026-05-05
- PR: T-P1A-103 repair PR（supersedes PR #93）
- 决议: user 已授权新修复 PR、最终 merge，并推进到 Wave 4 Batch 2 启动临界点；PR #93 不得原样合并，需由 T-P1A-103 supersede。
- 决议: Wave 4 B1 PR body/diff layer `verdict=clear` 保留；RAW control-plane checkpoint/report/diff bundle/local evidence manifest 由 `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/REPAIR-Wave4-B1-control-plane-and-B2-preflight-2026-05-05.md` 修复为 B2 preflight 的输入证据。
- 决议: PRD-v2.1 + SRD-v3 H5/Bridge 通过 `user_override_for_B2_preflight` promoted 为 B2 planning/contract addenda；这是 user-authorized planning/contract promotion override，不是 walking skeleton、frontend implementation、Bridge/VaultWriter runtime、vault commit、migration 或 visual gate 已满足的证据。
- 边界: DB vNext SRD-v3 继续 candidate-only；runtime / frontend / migration / BBDown live / yt-dlp / ffmpeg / ASR / browser automation 均仍 gated。
- 出口状态: `B2_PREFLIGHT_CLOSED / B2_COMMANDER_READY`；下一步只能进入 commander prompt 准备，不自动启动 code-bearing runtime lane。

## D-007: T-P1A-104 RAW control-plane hash manifest

- 日期: 2026-05-05
- 决议: 针对 T-P1A-103 外审 residual risk，新增 tracked repair evidence manifest：`docs/research/repairs/t-p1a-104-control-plane-hash-manifest-2026-05-05.md`。
- 决议: manifest 只记录 RAW final report / full diff bundle / local evidence manifest / archived partial report / checkpoint 的绝对路径、bytes、SHA-256、结构计数和本地清理核验，不复制 RAW 正文、Hermes 配置、cookies、tokens、credential material 或 local-only clone 内容。
- 决议: T-P1A-033 / T-P1A-034 Done 历史行保留原始 candidate landing 事实，同时追加 `superseded_for_B2_planning_by=T-P1A-103`，避免后续 agent 只搜旧行时误读当前状态。
- 边界: T-P1A-104 是可审计性补丁，不改变 `B2_PREFLIGHT_CLOSED / B2_COMMANDER_READY` 状态，不解禁 runtime / frontend / migration / vault commit / BBDown live / yt-dlp / ffmpeg / ASR / browser automation。

## D-008: T-P1A-105 commander-mode template extension + local plan workspace

- 日期: 2026-05-05
- 决议: 将 commander-mode dispatch header 扩展固化进 `docs/dispatch-template.md`，包括 `Expected Baseline`、`Authority Writer`、`External Audit`、`Worker Topology`、`Live PR Number` 和 `Manual Gates Required`。
- 决议: `manual_gates_required` 采用可 grep / 可执行验证的文本格式，避免 pack 内不存在的前置条件被混写进 `Depends On` 后只能靠人工脑补。
- 决议: `plan/` 定义为 gitignored local handoff workspace，用于保留本机 handoff/dispatch 草稿，但不进入 repo authority truth，也不再污染根 worktree `git status`。
- 边界: T-P1A-105 是 process/template 补丁，不解禁 runtime / frontend / migration，不改变 `B2_PREFLIGHT_CLOSED / B2_COMMANDER_READY` 状态。

## D-009: T-P1A-072 Wave 4 ledger open

- 日期: 2026-05-05
- PR: T-P1A-072 authority PR
- 决议: 在 `T-P1A-103` 已写回的 `B2_PREFLIGHT_CLOSED / B2_COMMANDER_READY` 真相之上，正式将 Wave 4 ledger open 写回 authority。
- 决议: 当前 next gate 切到 `T-P1A-073 / slot-label PR #98`，用于进入 `apps/capture-station` scaffold；这表示可以按 dispatch 进入 bounded execution，不表示 unscoped frontend/runtime approval。
- 决议: `apps/**` 与 `services/**` 从 blanket forbid 调整为 `只有当前 dispatch 明确授权路径时才可动`；`workers/**`、`packages/**`、`migrations/**`、`data/**`、`referencerepo/**`、BBDown live、ffmpeg、ASR、browser automation 仍继续 gated。
- 决议: `user_override_for_B2_preflight` 仍只代表 B2 planning/contract addenda promotion；walking skeleton、vault commit、migration、runtime 和 visual final approval 依然需要未来证据。

## D-010: Wave 4 Batch2 execution closure and post-PR123 authority cleanup

- 日期: 2026-05-05
- PR: Batch2 closeout authority/scope hardening PR
- 决议: `T-P1A-073 ~ T-P1A-085` 已通过 PR `#103 ~ #115` landed on `main`，当前 authority 不再将 `T-P1A-073 / slot-label PR #98` 视为未来 next gate。
- 决议: 当前 authority 状态更新为 `WAVE_4_LEDGER_OPEN / B2_COMPLETE_PENDING_REVIEW`；这表示 Batch2 execution chain 已 terminal enough to close the stale next-gate pointer，但不自动打开 STEP3 / Wave 5 的 code-bearing gate。
- 决议: 当前 authority 未登记新的 code-bearing next gate；任何后续 Wave 4 / STEP3 continuation 必须基于 post-`PR #123` mainline 与新 dispatch + user 显式 gate。
- 决议: `batch2-audit-summary-2026-05-05.md` 在保留 historical body 的前提下补充局部旁注，明确 Stage A Node validation later repaired by PR `#119`，slot98 repair scope later narrowed by correction note。
- 决议: `tools/check-docs-redlines.py` 的 apps diff guard 从“known app path may auto-pass”收紧为“当前 `apps/**` diff 必须被 tracked dispatch/repair scope note 明确点名”；历史存在的 app surface 不再自动构成当前 PR 授权。
- 边界: 本次 authority/guard 收口不解禁 bridge runtime、vault true write、migration、BBDown live、yt-dlp、ffmpeg、ASR、browser automation 或 `audio_transcript` runtime。

## D-011: Wave 4 mid checkpoint after T-P1A-086 ~ T-P1A-099

- 日期: 2026-05-05
- PR: slot-label `PR #125 / T-P1A-100`
- 决议: `T-P1A-086 ~ T-P1A-099` 已通过 Wave 4 Batch 3 live PR chain landed；其中 `T-P1A-099` 完成 visual reporting truth，当前 authority 状态提升为 `WAVE_4_MID_CHECKPOINT / NOT_CLOSEOUT`。
- 决议: Batch 3 landed surfaces now include:
  - vault helper stack: `T-P1A-086 ~ T-P1A-090`
  - placeholder/e2e baseline: `T-P1A-091 ~ T-P1A-095`
  - visual/CI/tooling/reporting baseline: `T-P1A-096 ~ T-P1A-099`
- 决议: `PR127 / T-P1A-101` 被记录为下一轮 continuation handoff，仅作 named next-hop；它不是已打开的 code-bearing next gate。
- 决议: same-PR scope-note repair pattern is now proven for app-diff slots; `T-P1A-092` and later `apps/**` slots required tracked repair notes to satisfy `tools/check-docs-redlines.py`.
- 不解禁: 当前仍无 screenshot evidence、无本轮 Playwright execution evidence、无人类视觉终判；bridge runtime、vault true write、migration、BBDown live、yt-dlp、ffmpeg、ASR、browser automation、`audio_transcript` runtime 继续 gated。

## D-012: T-P1A-106 post-mid-checkpoint continuation map

- 日期: 2026-05-05
- PR: authority-only continuation-map dispatch
- 决议: `Dispatch127 / T-P1A-106` 被登记为 post-mid-checkpoint continuation map；它只负责把 continuation candidate chain 写回 authority，不构成 code-bearing next gate。
- 决议: 当前 candidate 下游链固定为 `Dispatch128 / T-P1A-107`、`Dispatch129 / T-P1A-108`、`Dispatch130 / T-P1A-109`；后续 handoff 与依赖默认使用 dispatch slot + task ID，不再把历史 handoff 名称当作执行许可。
- 决议: `Dispatch127-130` 当前都属于 continuation candidate chain；它们可以收口 Wave 4 closeout / Wave 5 opening wording，但不自动解禁 runtime、migration、frontend implementation、browser automation、vault true write、BBDown live、yt-dlp、ffmpeg、ASR 或 `audio_transcript` runtime。

## D-013: T-P1A-109 Wave 4 closeout and Wave 5 candidate opening

- 日期: 2026-05-05
- PR: authority-only closeout/opening dispatch
- 决议: `Dispatch128 / T-P1A-107` 与 `Dispatch129 / T-P1A-108` 已作为 repo-visible candidate surfaces landed；前者负责 Wave 4 visual touchpoint roster / localhost manual-review plan，后者负责 bridge-vault continuation gap matrix；二者都不构成 runtime、browser automation 或 vault true write approval。
- 决议: authority 状态从 `WAVE_4_MID_CHECKPOINT / NOT_CLOSEOUT` 切到 `WAVE_5_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`；这表示 Wave 4 closeout wording 已写回，Wave 5 candidate docs/spec lane 可以继续，但仍没有已打开的 code-bearing next gate。
- 决议: 当前 Wave 5 candidate continuation 以 `Dispatch131-144 / T-P1A-110 ~ T-P1A-123` 为 docs/spec 主链；更晚的 bounded app rows、runtime-gate rows 和 authority rows仍需各自按 dispatch 执行，不得由当前 authority 自动放行。

## D-014: Wave 5 candidate closeout

- 日期: 2026-05-05
- PR: authority-only `T-P1A-152`
- 决议: `Dispatch131-172 / T-P1A-110 ~ T-P1A-151` 已全部以 candidate docs/spec/visual/audit lanes landed on `main`，当前 authority 状态从 `WAVE_5_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED` 收口为 `WAVE_5_CANDIDATE_CLOSED / NOT_EXECUTION_APPROVED`。
- 决议: `T-P1A-124 / T-P1A-125` 两个 bounded frontend candidate surface 已 landed，且后续 residual repair 已补齐 local frontend validation 与 bounded screenshot packet / Playwright execution evidence；但该证据仍只适用于 bounded candidate surfaces，不构成全局 visual terminal verdict、product UI approval、package strategy approval、runtime approval 或 frontend execution gate。
- 决议: `T-P1A-126 ~ T-P1A-151` 的 docs/spec/visual/audit candidate pack 只形成 repo-visible planning / contract / audit surfaces；不解禁 runtime、browser automation、migration、vault true write、BBDown live、yt-dlp、ffmpeg、ASR 或 `audio_transcript` runtime。
- 决议: 当前仍没有已打开的 code-bearing next gate；后续若进入 Wave 6，仍需通过新的 authority dispatch 和显式 gate。

## D-015: Wave 6 candidate ledger open

- 日期: 2026-05-05
- PR: authority-only `T-P1A-153`
- 决议: authority 状态从 `WAVE_5_CANDIDATE_CLOSED / NOT_EXECUTION_APPROVED` 推进到 `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`。
- 决议: 这只表示 Wave 6 candidate planning / overflow / handoff lane 可以继续收口 `Dispatch175 / T-P1A-154` 与 `Dispatch176 / T-P1A-155`；不构成 code-bearing gate，不构成 runtime、migration、browser automation、BBDown live、yt-dlp、ffmpeg、ASR、`audio_transcript` runtime 或 vault true write approval。
- 决议: `T-P1A-152` 关闭的 Wave 5 candidate chain 继续保留为历史 landed truth；Wave 6 仍需后续 dispatch 明确各自范围和证据。

## D-016: Wave 6 overflow and handoff candidate landing

- 日期: 2026-05-05
- PR: `T-P1A-154` + `T-P1A-155`
- 决议: `Dispatch175 / T-P1A-154` 与 `Dispatch176 / T-P1A-155` 已 landed on `main`，分别收口 Wave 6 overflow candidate registry 与 STEP3 cold-start handoff packet contract。
- 决议: 当前 authority 继续保持 `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`；`Dispatch175/176` 的 landed truth 不构成 code-bearing next gate，也不构成 runtime、migration、browser automation、BBDown live、yt-dlp、ffmpeg、ASR、`audio_transcript` runtime 或 vault true write approval。
- 决议: 当前 Wave 6 仅保留 candidate planning / overflow / handoff continuation truth；任何后续 code-bearing、runtime-bearing 或 migration-bearing 动作都必须走新 dispatch + 外审。

## 2026-05-07 — Baseline navigation consolidated (PR #244)

- Decision (1): 新 `docs/00-START-HERE.md` 作为 `current authority` 入口, 含 Agent Cold Start Ladder + 4 状态词字典 + 文档地图.
- Decision (2): PR #243 master spec 从 `docs/research/post-frozen/` 提升到 `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` 顶级, 跟 PRD/SRD 同级 visibility.
- Decision (3): master spec 状态 = `candidate north-star`, **不是** PRD-v3 / SRD-v3 / runtime approval / migration approval / authority writer (顶部边界声明硬锁).
- Decision (4): PRD-v3 / SRD-v3 thin compiled candidate shell 落到 `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/`, 来源 = PRD-v2 + v2.1 + U1-deep supplement (PRD) / SRD-v2 + h5-bridge promoted + db-vnext + supplement (SRD), 让孤儿 supplement 引用闭环, 不假装正式 base.
- Decision (5): 16 ZIP 储能层 (~1.48M 字 / 895 file) 状态 = `reference storage`, grep-able reference 不行动基线.
- Decision (6): doc1/doc2/doc3 frontmatter 加 `status_word: reference storage` + cross-link 字段, 跟 00-START-HERE.md §5 三向闭环.
- Decision (7): 状态词锁 4 类 forward-going: `current authority` / `promoted addendum` / `candidate north-star` / `reference storage`. 严禁引入新状态词. 历史遗留文件按 grandfather rule, 不强制 retroactive 整改.
- Source:
  - `docs/00-START-HERE.md`
  - `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`
  - `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/PRD-v3-candidate-2026-05-07.md` (thin shell)
  - `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/SRD-v3-candidate-2026-05-07.md` (thin shell)

## 2026-05-07 — START-HERE dynamic maintenance harness accepted (PR #246)

- Decision (1): `docs/00-START-HERE.md` 的易漂移锚点改为 4 层维护机制，而不是继续靠口头约束。
- Decision (2): `Layer A` 生效：§0 减 hard-code，§1 改成 `python tools/refresh-start-here.py` auto-managed 真态锚点。
- Decision (3): `Layer B` 生效：`python tools/refresh-start-here.py --check` 接入 docs-check；main SHA / checkpoint dispatch 求和 / forced refresh 阈值漂移时直接 fail。
- Decision (4): `Layer C` 生效：每次 wave / governance lane closeout 必须按 `docs/task-index.md -> docs/current.md -> docs/decision-log.md -> python tools/refresh-start-here.py` 顺序写回，并人工复核 START-HERE §7 与关联文档的旧 PR / SHA / wave 状态引用。
- Decision (5): `Layer D` 生效：当前 refresh 已在 PR `#246` 执行；下一次 forced refresh = `PR #300`，之后每 `+50 PR` 再做一次 refresh sprint。
- Decision (6): PR #244 合并后遗留的 authority 漂移本次一并收口：`docs/current.md` main SHA 对齐 `e207664`，`docs/task-index.md` 关闭 `T-DOC-244` Active 行。
- Source:
  - `docs/00-START-HERE.md`
  - `docs/current.md`
  - `docs/task-index.md`
  - `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`
  - `tools/refresh-start-here.py`

## 2026-05-07 — PR #246 merged + closeout (D-017 follow-up)

- Decision: PR #246 admin merged into main as squash commit `3c01a1c`.
- Audit chain: 4-commit (`20d18e6` → `9bf2251` → `1fb4582` → `7acafa0`); amend trail=4 (战友 explicit override "全部修复" per W6K governance lane scope).
- Layer 1 CC0 self-audit: CLEAR (catch H-1 + M-1 + M-2 + M-3 自审, 全修在 1fb4582 + 7acafa0).
- Layer 2 刑部尚书 subagent (Anthropic Opus 4.7, instinct §3 #16 自我应用 same-family weak audit): **CLEAR_WITH_LOW_FOLLOWUPS** (0 Critical / 0 High / 0 Medium / 4 Low post-merge).
- Layer 3 (cross-vendor strong gate): 推迟 W6K 长期议程 (Codex / GPT Pro / Hermes 一轮 audit, post-merge 不阻 merge).
- 4 LOW post-merge follow-up:
  - L-1: `tools/refresh-start-here.py:32-35` `RUNS_DIR.exists()` + `is_dir()` fail-loud check
  - L-2: master spec §16.1 第 3 条 vs START-HERE §9 第 3 条 authority files 措辞统一
  - L-4: `read_git_commits` REMOTE 存在性 preflight
  - W6K candidate PR: `~/.claude/rules/*` + `~/.claude/projects/.../memory/*` 镜像到 `docs/global-rules/` + `docs/agent-memory/` 真跨 vendor 共享
- Closeout 顺序 (本 PR #247, 跟 master spec §14.4 Layer C 锁):
  - `docs/task-index.md`: T-DOC-246 active → Done + Active 1/3 → 0/3 + Authority writer 1/1 → 0/1 ✓
  - `docs/current.md`: main SHA 改 `3c01a1c` ✓
  - `docs/decision-log.md`: 本 entry (PR #246 merged D-017 follow-up) ✓
  - `python tools/refresh-start-here.py`: 自动刷新 START-HERE §1 anchor 块 + frontmatter `last_refreshed_from_main_sha` / `last_refreshed_from_main_pr` ✓
- e2e-placeholder-baseline FAIL 是 PR #243 pre-existing tech debt (component 改名 vs e2e hardcode), 跟 PR #246 0 因果, admin override per F-DIRECT-MERGE-OK.

## 2026-05-08 — Authority refresh after PR #249 post-frozen cluster-suite landing

- Decision (1): `origin/main` 最新已到 `ec7870d` / PR #249，但 authority 入口仍停在 `c802de4` / PR #247；本次只做 authority refresh，不打开新的 code-bearing next gate。
- Decision (2): `PR #249` landed truth 被记录为 `docs/research/post-frozen/2026-05-08/{W1,W1B,W2,W4,W5}` candidate substrate；这些文件可作为 W2C/W1B/W3E/W4 后续 dispatch、audit、implementation 输入，但**不是** authority、runtime approval、migration approval、browser automation approval、vault true write approval 或 frontend execution approval。
- Decision (3): authority 状态继续保持 `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`；Active product lane 仍为 `0/3`，Authority writer 仍为 `0/1`。
- Decision (4): Layer C closeout 顺序再次适用：`docs/task-index.md -> docs/current.md -> docs/decision-log.md -> python tools/refresh-start-here.py`；`refresh-start-here.py` 仅负责 `docs/00-START-HERE.md` 收口，不替代前三张 authority 面同步。
- Decision (5): `README.md` 与 `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` 已做人审 stale-anchor 扫描；本轮未发现必须写回的 `PR #247 / c802de4` 残留。
- Source:
  - `docs/current.md`
  - `docs/task-index.md`
  - `docs/00-START-HERE.md`
  - `tools/refresh-start-here.py`
  - `https://github.com/RayWong1990/ScoutFlow/pull/249`

## 2026-05-08 — W2C lane open (`T-P1A-156`)

- Decision (1): 打开 `T-P1A-156 / W2C PF-C4-02 real-data wiring` 作为当前唯一 active product lane；Active product count=`1/3`，Authority writer count=`0/1`。
- Decision (2): `T-P1A-156` 边界锁为 frontend-first：默认 allowed path 仅含 `apps/capture-station/src/**`、选定 bridge/trust-trace test、以及 W2C receipt/checkpoint；默认不改 `services/api/**`。
- Decision (3): `trust-trace/**` 在本轮只允许 `/captures/{id}/trust-trace` readback + state shell；graph / timeline / error-path implementation 仍保留给 W1B，不在 W2C lane 内偷跑。
- Decision (4): 若 live router / DTO mismatch 阻断 truthful rendering，W2C 不得顺手扩 backend；必须 stop-the-line，拆单独 micro PR，并先过外审再回到 W2C 主实现。
- Decision (5): 打开 `T-P1A-156` 不改变全局状态词；authority 仍保持 `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`，不构成 runtime、migration、browser automation、vault true write 或 full-signal execution approval。
- Source:
  - `docs/task-index.md`
  - `docs/current.md`
  - `docs/specs/parallel-execution-protocol.md`
  - `docs/research/post-frozen/2026-05-08/W2-w2c/01-w2c-cluster-spec.md`
  - `docs/research/post-frozen/2026-05-08/W2-w2c/02-w2c-dispatch-pack.md`

## 2026-05-08 — W2C lane closeout (`T-P1A-156` PR #252 merged)

- Decision (1): `T-P1A-156 / W2C PF-C4-02 real-data wiring` 已闭合；PR #252 admin squash merge 到 main，merge commit=`02ccbdc151816d10acc517bd98181bb2b42f0fe8`，2026-05-08T03:46:55Z；4-PR pipeline (Stage 0 PR #250 + Stage 1-open-lane PR #251 + Stage 1-impl PR #252 + Stage 1-closeout 本 PR) 顺序 merged，符合 master spec §14.4 single-writer + Authority writer max=1 + 4 status word lock。
- Decision (2): W2C 实施范围 = 39 file / +4647 / -572 (gh pr view 252 changedFiles=39 真值)；13 surface (url-bar / live-metadata / capture-scope / topic-card-preview / topic-card-vault / vault-preview / vault-commit / signal-hypothesis / capture-plan / trust-trace / + AppShell + surfaces.smoke + lib/api-client + lib/w2c-runtime) 完成 existing read-only/dry-run route 真接 + 5 态 state machine (empty/loading/success/error/disabled) + sync-badge 推广 + Trust Trace data shell。
- Decision (3): Trust Trace 的 graph/timeline/error-path 真实现仍保留给 W1B，本 lane 仅落 `/captures/{id}/trust-trace` readback + state shell，未触碰 W1B 边界；instinct §3 #16 + cross-vendor-audit-layering v2 user-catch 适用：未来 W1B 启动需新 dispatch + 外审。
- Decision (4): 2 P1 修复 (Codex strict audit 自审捕获后修)：(a) `apps/capture-station/src/lib/w2c-runtime.tsx` discover 起手清旧 capture context，in-flight 请求不冒用旧 `capture_id`；(b) `apps/capture-station/src/features/capture-plan/CapturePlan.tsx` frontmatter 展示锁定后端 contract，仅认 `title / date / tags / status`。
- Decision (5): W2C 实施期间 5 overflow lane Hold 全守 (true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench)；`write_enabled=False` 硬不变；后端 DTO/`PlatformResult`/`WorkerReceipt` schema 不动 (前端消化，无 contract-fix micro PR 触发)；不构成 runtime / migration / vault commit / browser automation / package strategy / full-signal execution approval。
- Decision (6): CI 真态 = `docs-smoke + api-contract-tests + capture-station-node + five-gate-checklist` 4 pass；`e2e-placeholder-baseline` fail 是历史 stale 用例 (找已不存在的 `VaultCommitDryRunButton.tsx` + `VaultPreviewPanel.tsx`，本 W2C 实际产物是 `VaultCommit.tsx` + `VaultPreview.tsx`)；admin override squash merge 合规 (跟 PR #243-#248 同既有口径)；e2e placeholder 用例清理留 W6K refresh sprint。
- Decision (7): non-blocking 残留 = `apps/capture-station/src/App.test.tsx` 的 `act(...)` warning，`W2CRuntimeProvider` mount 阶段异步 load bridge state；不影响 W2C runtime truth 与 merge verdict，留 W1B 接班时清。
- Decision (8): Layer C closeout 顺序 (master spec §14.4 + 与 D-T-DOC-249 / D-W2C-LANE-OPEN 同节奏): `docs/task-index.md` (T-P1A-156 active → Done + Active 1/3 → 0/3) -> `docs/current.md` (main 锚 `cd9d866` → `02ccbdc` + W2C closed 表述 + capture-station code baseline 升到 `02ccbdc`) -> `docs/decision-log.md` (本 entry) -> `python tools/refresh-start-here.py` (自动刷 START-HERE §1 + frontmatter `last_refreshed_from_main_sha` / `last_refreshed_from_main_pr`)。
- Decision (9): 元教训 — Codex Stage 1-impl PR #252 strict audit subagent 自审 "无 blocking finding"，但漏 closeout 本步 (Stage 1-closeout 微分支)；CC1 cross-vendor catch P0 BLOCKING (Active 1/3 没 release / current.md main 锚 STALE / decision-log 漏 entry / `refresh-start-here.py --check` exit 1)；本 PR 即修。沉淀进 instinct §3 #22 + cross-vendor-audit-layering skill v3.2 (Post-Execution Process Completion Verification SOP, 输出层防御)。
- Source:
  - https://github.com/RayWong1990/ScoutFlow/pull/252
  - `docs/research/post-frozen/2026-05-08/W2-w2c/receipts/w2c-implementation-receipt-2026-05-08.md`
  - `docs/research/post-frozen/2026-05-08/W2-w2c/receipts/w2c-checkpoint-2026-05-08.json`
  - `docs/task-index.md`
  - `docs/current.md`
  - `tools/refresh-start-here.py`

## 2026-05-08 — W4 Tier 4 merge + authority closeout

- Decision (1): `PR #260 -> #258 -> #259` 已按顺序完成 squash merge；由于 GitHub 不允许直接 merge draft PR，本轮只做了最小机制性 fix-forward：先 `ready for review`，再 merge，未修改 lane 内容。
- Decision (2): merge commits = `1fa0e9a8143272f494f5795622ff84e30f69dab4` (PR #260) / `beb0fef9cfb47d03d83ad4f73555ab266e6ddb9a` (PR #258) / `5777389e64f46d9fa6e8a74470e29ba6b1ecd653` (PR #259)；`origin/main` 现已前进到 `5777389`。
- Decision (3): W4 Step0 + lane 1/2/4 Phase 1 candidate spec family 现已全部 landed on `main`；它们仍是 `candidate north-star` / candidate spec family，不构成 runtime approval、migration approval、browser automation approval、vault true-write approval 或任何 overflow lane 解禁。
- Decision (4): pre-merge truth gate 通过：3 个 PR 均为 `OPEN draft + MERGEABLE`，且 `docs-smoke`、`api-contract-tests`、`capture-station-node` 均为 `SUCCESS`。`e2e-placeholder-baseline` 三者失败栈一致，均为历史 stale placeholder failure（缺失 `VaultCommitDryRunButton.tsx` / `VaultPreviewPanel.tsx`），不是本轮 docs PR 新引入回归。
- Decision (5): lane 1 ↔ lane 2 handoff 字段对齐继续保持 9-field transcript handoff + 12-slot vault commit role contract；lane 4 adopted path 继续保持 `manual SQL + storage.py loader`，Alembic 继续保持 deferred candidate。
- Decision (6): `docs/research/repairs/pr255-authority-writeback-erratum-2026-05-08.md` 与 `docs/research/repairs/pr257-start-here-boundary-erratum-2026-05-08.md` 已补齐审计轨迹。修正点仅限 boundary / receipt truth：PR #255 实际发生 authority writeback；PR #257 实际发生 START-HERE refresh。两者都不改写各自 landed substance。
- Decision (7): `PR #255` 的 follow-up truth bug 仍只保留为 candidate：`ErrorPathLane` failed-audit clear 语义、`GraphLane` media-tone 只看 transcript literal、以及未来 `audio_transcript` truncate/redaction guard 都未在本 closeout 中伪装为已修。
- Decision (8): Layer C closeout 顺序本次再次执行：`docs/task-index.md -> docs/current.md -> docs/decision-log.md -> python tools/refresh-start-here.py`；当前没有 active code-bearing lane，Authority writer 保持 `0/1`，5 overflow lane 继续 Hold。
- Source:
  - https://github.com/RayWong1990/ScoutFlow/pull/260
  - https://github.com/RayWong1990/ScoutFlow/pull/258
  - https://github.com/RayWong1990/ScoutFlow/pull/259
  - `docs/research/repairs/pr255-authority-writeback-erratum-2026-05-08.md`
  - `docs/research/repairs/pr257-start-here-boundary-erratum-2026-05-08.md`
  - `docs/task-index.md`
  - `docs/current.md`

## 2026-05-08 — 批量化转写平台 companion roadmap 建立

- Decision (1): 新增 `docs/BATCH-TRANSCRIPTION-MASTER-ROADMAP-2026-05-08.md`，作为与 `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` 配套使用的 companion roadmap。
- Decision (2): 角色分工明确化：master spec 继续回答长期 north-star、全生命周期 inventory、11 wave 与升级路径；0508 roadmap 负责批量化转写平台的执行总纲，回答 P3 / PF-V / runtime_tools / true_vault_write / batch friction / DB architecture decision 的 program 顺序。
- Decision (3): 该 roadmap 状态固定为 `candidate north-star / not-authority`；不构成 runtime approval、migration approval、browser automation approval、true_vault_write approval 或 full-signal execution approval。
- Decision (4): 路线图主锚固定为 authority state、landed capability、5 overflow Hold 与每轮 preflight live readback；`main HEAD` / PR 号仅作历史 receipts，不作为 program 主锚。
- Decision (5): 2026-05-08 版核心修正已写入该 roadmap：`3 URL smoke batch + 10 URL friction batch`、新增 `Lane D = PF-V visual productization`、`UI stack decision candidate` 提前、`DB architecture decision` 提前而 `DB migration implementation` 后置、首次 runtime/ASR 只战术性选择一条 route 与一个 engine。
- Decision (6): `docs/task-index.md`、`docs/00-START-HERE.md` 与 `docs/current.md` 已补充该 companion roadmap 入口，后续新 session 的推荐读法变为 `current -> START-HERE -> master spec -> 0508 roadmap`。
- Source:
  - `docs/task-index.md`
  - `docs/BATCH-TRANSCRIPTION-MASTER-ROADMAP-2026-05-08.md`
  - `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`
  - `docs/00-START-HERE.md`
  - `docs/current.md`

## 2026-05-08 — T-P1A-158 W2C runtime truth repair bundle

- Decision (1): 在不重开 standing active lane 的前提下，`PR #261` 吸收了一个 bounded repair bundle：`apps/capture-station/src/lib/w2c-runtime.tsx` / `.test.tsx`、`tools/refresh-start-here.py`、`tools/check-docs-redlines.py`、`tests/tools/*`、`docs/memory/**` 与 4 张 repair/erratum note。
- Decision (2): `refreshCaptureBoundData()` 现已带 generation + currentCaptureId 双重 stale guard；旧 refresh 响应不会在 `clearCapture()` 或新 capture 建立后回写旧 trust-trace / vault-preview truth。
- Decision (3): `isVaultWriteBlocked` 改为默认悲观：只有 bridge health 与 bridge vault config 两端都显式 `write_enabled === true` 时才解除 blocked；在 ScoutFlow 当前边界下，这一条件实际上不会成立，因此 shared runtime boolean 不再对 loading/error/null 态过度乐观。
- Decision (4): `tools/refresh-start-here.py` 新增显式 `--ref`；CI docs-check 改为 `python tools/refresh-start-here.py --check --ref HEAD`，从而在 PR merge-ref / checked-out HEAD 场景验证 START-HERE freshness，而本地普通 refresh 仍保持 `origin/main` 语义。
- Decision (5): `tools/check-docs-redlines.py` 新增 frontmatter status taxonomy guard：只允许 4 个锁定状态词，且 `current authority` 仅允许出现在 `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `docs/00-START-HERE.md`。
- Decision (6): `docs/memory/**` 全量回退为 `reference storage`，并补 `memory_role`；`L-AUTHORITY-DRIFT` 的 authority surface 定义已收紧到 4 个 current-authority 文件，不再把 `AGENTS.md` / 根 `CLAUDE.md` 提升成同级 ledger。
- Decision (7): `docs/research/repairs/pr245-memory-authority-taxonomy-erratum-2026-05-08.md`、`docs/research/repairs/pr247-pr249-start-here-validation-erratum-2026-05-08.md` 与 `docs/research/repairs/pr254-start-here-authority-touch-erratum-2026-05-08.md` 已补齐审计轨迹；这些修正只改 boundary / validation / taxonomy truth，不回滚对应 PR 的 landed substance。
- Decision (8): 本 repair bundle 不触碰 `services/**`、`workers/**`、`packages/**`、`data/**`、`referencerepo/**`；不解禁 runtime、migration、browser automation、vault true-write；不改 DTO、schema、`PlatformResult` 或 `WorkerReceipt`。
- Decision (9): Layer C writeback 本次继续按 `docs/task-index.md -> docs/current.md -> docs/decision-log.md -> python tools/refresh-start-here.py` 执行；收口后仍保持 `Active product lane=0/3`、`Authority writer=0/1`、5 overflow lane 全 Hold。
- Source:
  - `apps/capture-station/src/lib/w2c-runtime.tsx`
  - `apps/capture-station/src/lib/w2c-runtime.test.tsx`
  - `tools/refresh-start-here.py`
  - `tools/check-docs-redlines.py`
  - `tests/tools/test_refresh_start_here.py`
  - `tests/tools/test_check_docs_redlines.py`
  - `docs/memory/README.md`
  - `docs/memory/INDEX.md`
  - `docs/memory/lessons/L-AUTHORITY-DRIFT.md`
  - `docs/research/repairs/pr245-memory-authority-taxonomy-erratum-2026-05-08.md`
  - `docs/research/repairs/pr247-pr249-start-here-validation-erratum-2026-05-08.md`
  - `docs/research/repairs/pr254-start-here-authority-touch-erratum-2026-05-08.md`
  - `docs/research/repairs/pr261-w2c-runtime-safety-scope-note-2026-05-08.md`

## 2026-05-08 — PR262 consistency full repair after PR261

- Decision (1): PR261 merge commit `5902ecf` is the closeout anchor for this repair; `docs/current.md` and `docs/00-START-HERE.md` must point at PR #261 / `5902ecf` before any later PR262 merge truth is claimed.
- Decision (2): PR261 validation readback was not clean: the PR body listed `python tools/refresh-start-here.py --check --ref HEAD`, while CI docs-smoke failed at START-HERE freshness.
- Decision (3): START-HERE / current.md are now aligned to PR261 merge truth by PR262; PR261 itself remains a valid repair bundle but not a fully clean validation closeout.
- Decision (4): `tools/refresh-start-here.py` semantics are repaired: main closeout refresh writes `origin/main` / main HEAD authority fields, while checked-out PR refs are probe/check inputs and must not be written as synthetic long-lived START-HERE truth.
- Decision (5): W4 lane spec validation pattern is repaired: forbidden phrase absence checks must use `! rg -n ...` or an equivalent no-match script, not a bare `rg -n ...` receipt line.
- Decision (6): W1B UI truth bugs are repaired in `ErrorPathLane` / `GraphLane` / `TimelineLane` without DTO, schema, backend, `PlatformResult`, or `WorkerReceipt` changes.
- Decision (7): 5 overflow lanes remain Hold; this PR grants no runtime, migration, browser automation, vault true-write, or full-signal workbench approval.
- Decision (8): PR262 is not a new feature lane; it is consistency repair / closeout. Active product lane remains `0/3`, Authority writer returns to `0/1`.
- Source:
  - `docs/current.md`
  - `docs/task-index.md`
  - `docs/00-START-HERE.md`
  - `tools/refresh-start-here.py`
  - `tools/check-docs-redlines.py`
  - `apps/capture-station/src/features/trust-trace/lanes/ErrorPathLane.tsx`
  - `apps/capture-station/src/features/trust-trace/lanes/GraphLane.tsx`
  - `apps/capture-station/src/features/trust-trace/lanes/TimelineLane.tsx`
  - `docs/research/repairs/pr258-pr260-w4-lane-validation-and-start-here-erratum-2026-05-08.md`
  - `docs/research/repairs/pr261-validation-and-closeout-erratum-2026-05-08.md`
