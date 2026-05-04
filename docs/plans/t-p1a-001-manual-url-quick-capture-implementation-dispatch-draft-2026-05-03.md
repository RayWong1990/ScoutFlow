# T-P1A-001 Dispatch Draft — Bilibili manual_url quick_capture

> Status: draft for user approval
> Product-code approval: No
> May be executed only after user explicitly approves T-P1A-001
> Source readiness pack: docs/plans/phase1a-manual-url-quick-capture-readiness-2026-05-03.md

## 1. Purpose

本文件是 `T-P1A-001` 的代码开工派单草案，用来把已完成的 readiness pack 转成一个可审查的首个 Phase 1A code-bearing task 轮廓。

当前文件不是执行授权。没有 user 对 `T-P1A-001` 的明确批准前，本草案不得被当成可执行派单。

## 2. User approval required before execution

执行前至少需要 user 明确批准以下事项：

- 允许开始第一项 Phase 1A 产品代码任务
- 确认实现模式是 `metadata_only only` 还是 `metadata + audio_transcript`
- 确认 quick_capture 阈值是否保持 `100 MB / 30 min / 50k token`
- 确认 `manual_admin` 是否纳入首个实现任务
- 确认 `auth_required` 的首版处理口径
- 确认 PR 切分方式

若没有上述批准，任何实现都属于越权。

## 3. Allowed future scope

经 user 批准后，`T-P1A-001` 候选实现只允许覆盖：

- `POST /captures/discover` 的最小 API contract skeleton
- Bilibili `manual_url` payload parser / validator
- `manual_url` quick_capture 最小创建路径
- `artifact_assets` / receipt / redaction contract 对齐
- LP-001 对 `recommendation / keyword / raw_gap` 的拒收
- 最小 docs-check 与 contract tests

## 4. Forbidden future scope

即使 `T-P1A-001` 获批，也不得包含：

- recommendation-driven capture
- keyword / RAW gap direct capture
- Signal Workbench runtime
- Capture Plan UI / runtime
- XHS / YouTube / Hermes scheduling
- browser automation
- comment chain
- multi-user / SaaS
- Phase 2-4 runtime logic
- 真实推荐 / 重排 / dispatch UI

## 5. Candidate branch

建议分支名：

```text
task/T-P1A-001-manual-url-quick-capture
```

该分支只能在 user 明确批准后创建。

## 6. Candidate allowed paths

经 user 批准后，候选允许路径建议为：

```text
services/api/**
workers/**
tests/**
docs/current.md
docs/task-index.md
docs/decision-log.md
docs/specs/**
README.md
.github/**
tools/**
```

说明：

- 当前仓库尚未创建上述产品目录
- 本草案只定义候选写入范围
- 当前 `T-P0-007` 不得创建这些目录

## 7. Candidate forbidden paths

即使未来开始 `T-P1A-001`，下列路径仍默认禁止：

```text
data/**
referencerepo/**
candidates/**
dispatches/**
audits/**
example/**
examples/**
```

若 `T-P1A-001` 想扩大到 Phase 2+ 行为，应先停线并回到新的 readiness / amendment 任务。

## 8. Required contracts

后续 `T-P1A-001` 必须直接引用：

- `docs/plans/phase1a-manual-url-quick-capture-readiness-2026-05-03.md`
- `docs/specs/contracts-index.md`
- `docs/specs/locked-principles.md`
- `docs/specs/worker-receipt-contract.md`
- `docs/specs/platform-adapter-risk-contract.md`
- `docs/specs/raw-response-redaction.md`
- `docs/specs/parallel-execution-protocol.md`
- `docs/archive/SRD-v1.1-amendment-2026-05-03.md`

实现中至少要满足：

- `C-CAP-001`
- `C-CAP-002`
- `C-CAP-003`
- `C-ART-001`
- `C-WRK-001`
- `C-PLT-001`
- `C-SEC-001`
- `C-SCOPE-001`
- `C-PROC-001`

## 9. Implementation slices

候选切片只作为草案，不可直接执行：

- Slice 1 — API contract skeleton for `/captures/discover`
- Slice 2 — schema / migration stub only if explicitly approved
- Slice 3 — Bilibili `manual_url` parser / validator
- Slice 4 — artifact ledger / receipt mapping tests
- Slice 5 — LP-001 rejection tests for `recommendation` / `keyword` / `raw_gap`
- Slice 6 — redaction tests for raw response / receipt / logs

建议默认按单个小 PR 完成，避免 API / worker 拆成多个未闭环 PR。

## 10. Test plan

候选测试计划：

- API payload validation tests
- LP-001 rejection tests
- receipt / ledger mapping tests
- redaction tests
- typed `platform_result` tests
- docs-check / lint baseline

如果首版仅做 `metadata_only`，测试也应保持在该闭集内，不提前为 `audio_transcript` 编写真执行链路。

## 11. Validation commands

候选验证命令草案：

```bash
python -m py_compile tools/check-docs-redlines.py
python tools/check-docs-redlines.py
pytest tests/api -q
pytest tests/contracts -q
git diff --stat
git diff --check
```

若未来实际目录或测试命令不同，必须在正式 `T-P1A-001` 派单里改成仓库真实命令，不得照抄本草案假装通过。

## 12. Stop-the-line rules

命中以下任一情况，`T-P1A-001` 必须停线：

- user 未明确批准却开始产品代码
- `/captures/discover` 语义漂移为 source discovery / search / recommendation discovery
- `recommendation / keyword / RAW gap` 被允许直接创建 capture
- 产物或日志带出凭据
- `platform_result` 没有 typed contract
- 引入 Phase 2-4 runtime logic
- 需要创建超出授权范围的新目录
- PR scope 从 tiny implementation 膨胀为多阶段实现

## 13. PR body template

```md
## Summary
- Implemented the smallest approved `manual_url` quick_capture path for Bilibili.
- Kept scope inside the approved `T-P1A-001` contract boundary.
- Added contract tests for LP-001, receipt mapping, and redaction.

## Scope
- `/captures/discover` candidate implementation only
- No Phase 2-4 runtime behavior
- No recommendation-driven capture

## Validation
- [list real commands run]

## Boundary
- No browser automation
- No XHS / YouTube / Hermes
- No direct capture from recommendation / keyword / RAW gap

## User gate
- Confirm whether this tiny implementation PR is acceptable as the first Phase 1A code-bearing step.
```

## 14. Final回写 template

```md
Branch
task/T-P1A-001-manual-url-quick-capture

Commit
<sha>

PR
<number / url>

Validation
- docs-check: passed/failed
- contract tests: passed/failed
- LP-001 rejection tests: passed/failed
- receipt / ledger tests: passed/failed
- redaction tests: passed/failed

Boundary
- No Phase 2-4 runtime: yes/no
- No recommendation direct capture: yes/no
- No browser automation: yes/no
- No credential leak in artifacts/logs: yes/no

Remaining decisions
- merge?
- broaden from `metadata_only` to `audio_transcript`?
- keep single tiny PR or reopen scope?
```
