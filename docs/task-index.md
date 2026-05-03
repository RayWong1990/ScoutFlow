# ScoutFlow Task Index

> 共享薄账本。当前只服务 Step0 与 Phase 0 开工，不承担重治理职能。
> 当前限制：活动任务仅允许 `1-3` 条。

## 规则

- 当前只维护 Step0 / Phase 0 / Phase 1A 开工安全相关任务
- 任务状态变化时先写本文件，再更新 `docs/current.md`
- 外部研究统一落 `docs/research/`，不在项目根建立重治理目录
- 任何活动任务都必须写明 owner、scope、allowed paths、validation

## 当前 Phase

`Phase 1A — metadata_only manual_url quick_capture contract`

## Review

| 任务 ID | 标题 | 状态 | Owner Tool | 范围 | Allowed Paths | Forbidden Paths | 关联 PRD / SRD / Contract | Validation | Stop-the-line | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| `T-P1A-001` | Bilibili `manual_url` quick_capture metadata contract | `review` | `Codex Desktop` | API-side `metadata_only only` contract；不写 workers / frontend；不实现真实下载 | `services/api/**`, `tests/**`, `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, `docs/specs/**`, `README.md`, `AGENTS.md`, `.github/**`, `tools/**`, `pyproject.toml` | `apps/**`, `workers/**`, `packages/**`, `data/**`, `referencerepo/**`, `example/**`, `examples/**`, `candidates/**`, `dispatches/**`, `audits/**` | `docs/plans/phase1a-manual-url-quick-capture-readiness-2026-05-03.md`; `docs/plans/t-p1a-001-manual-url-quick-capture-implementation-dispatch-draft-2026-05-03.md`; `docs/specs/contracts-index.md`; `docs/specs/locked-principles.md`; `docs/specs/worker-receipt-contract.md`; `docs/specs/platform-adapter-risk-contract.md`; `docs/specs/raw-response-redaction.md`; `docs/SRD-v1.1-amendment-2026-05-03.md` | `python -m py_compile tools/check-docs-redlines.py`; `python tools/check-docs-redlines.py`; `python -m pytest tests/api tests/contracts -q`; `git diff --check`; forbidden path checks | `audio_transcript` runtime；workers；browser automation；Phase 2-4 runtime；`recommendation / keyword / RAW gap` direct capture；credential leak | branch=`task/T-P1A-001-manual-url-quick-capture`; first code-bearing Phase 1A task；default=`metadata_only only` |

## Backlog

| 任务 ID | 标题 | 状态 | Owner Tool | 范围 | Allowed Paths | Forbidden Paths | 关联 PRD / SRD / Contract | Validation | Stop-the-line | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` |

## Blocked

| 任务 ID | 标题 | 阻塞原因 | 需要动作 | 时间 |
|---|---|---|---|---|
| `—` | `—` | `—` | `—` | `—` |

## Done

| 任务 ID | 标题 | 完成时间 | 备注 |
|---|---|---|---|
| `T-P0-000` | Step0 Execution Plan + SRD 开工安全补丁（含 audit-fix） | `2026-05-03` | user 已批准作为后续实现候选基准 |
| `T-P0-001` | GitHub Bootstrap + Initial Repository Baseline | `2026-05-03` | initial=`22c2c2014b9d10f48a6a8fe11fc73f38ba1b0045`; second=`d1c12326450f5a92d8b0b6f32c0cac51f5f5ee5a`; remote=`https://github.com/RayWong1990/ScoutFlow.git`; private repo；无产品代码 |
| `T-P0-002` | 入口文档深化 + 并行执行协议固化 | `2026-05-03` | branch=`task/T-P0-002-parallel-execution-protocol`; commit=`ee1f4cfd34282e39be74afc20310ef7801ac4b25`; PR=`#1`; merge commit=`bafeb56c79c69a43f2806aaec88ea7014db36815`; workflow run=`25271451489`; docs-check=`success`; GPT Pro external audit=`COMMENT review, no blocking issue`; 无产品代码；未批准 Phase 1A 产品实现 |
| `T-P0-003` | 目录骨架 + 文档 lint stub + 入口文档同步 | `2026-05-03` | commit=`b32ae22edd7e60becc39d5d5d0bca8381b948254`; final close commit=`efe607dbafe3c398d582aaf0a0d5e9521ff2a814`; docs-check run=`25270586304`; 创建 docs redline lint stub；接入 GitHub Actions docs-check；同步 README / AGENTS / CLAUDE 入口口径；无产品代码 |
| `T-P0-004` | 通信测试清理与 ScoutFlow 主线恢复 | `2026-05-03` | GitHub queue / sync smoke / Codex adapter 探索按 user 决定暂停或关闭；`T-P0-005` / `T-P0-006` 不列为活动产品任务；`example/` 与 smoke-only `examples/` 移除；PR `#2` 与 Issue `#3/#4/#5` 关闭；无产品代码；未批准 Phase 1A 产品实现 |
| `T-P0-007` | Phase 1A Bilibili `manual_url` quick_capture readiness pack | `2026-05-03` | branch=`task/T-P0-007-phase1a-readiness`; reviewed commit=`40aa2f325bf5defe9fad9427fd0c8a006bf84436`; PR=`#6`; merge commit=`cc649030437dfab1ea52f062d454c1da789703c5`; workflow run=`25276308045`; docs-smoke=`success`; GPT Pro external audit=`PASS`; docs-only readiness planning；merged to `main`；`T-P1A-001` 已获 user 显式批准 |

## Stop-the-line

- 发现 schema / state words / FS layout / LP 冲突
- 发现 raw response、日志或报账结构带出凭据
- 发现任务开始落 Phase 2-4 真实逻辑
- 发现有人尝试让 `recommendation / keyword / RAW gap` 直接创建 capture
