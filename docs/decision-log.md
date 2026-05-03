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
- Local target-test verdict: `verdict=clear` for `python -m pytest tests/api tests/contracts -q` with `46 passed`.
- Remaining gate: full validation command set plus GitHub PR / Actions audit before merge decision.
