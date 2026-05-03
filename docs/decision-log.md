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
