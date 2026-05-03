# ScoutFlow Task Index

> 共享薄账本。当前只服务 Step0 与 Phase 0 开工，不承担重治理职能。
> 当前限制：活动任务仅允许 `1-3` 条。

## 规则

- 当前只维护 Step0 / Phase 0 / Phase 1A 开工安全相关任务
- 任务状态变化时先写本文件，再更新 `docs/current.md`
- 外部研究统一落 `docs/research/`，不在项目根建立重治理目录
- 任何活动任务都必须写明 owner、scope、allowed paths、validation

## 当前 Phase

`Phase 0 — Step0 文档与开工安全补丁`

## Review

| 任务 ID | 标题 | 状态 | Owner Tool | 范围 | Allowed Paths | Forbidden Paths | 关联 PRD / SRD / Contract | Validation | Stop-the-line | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| `T-P0-002` | 入口文档深化 + 并行执行协议固化 | `review` | `Codex Desktop` | Step0 docs + ops contract | `docs/`, `AGENTS.md`, `CLAUDE.md`, `README.md`, `.github/pull_request_template.md`, `tools/check-docs-redlines.py` 仅如需, `.github/workflows/docs-check.yml` 仅如需 | `apps/`, `services/`, `workers/`, `packages/`, `data/`, `referencerepo/`, `candidates/`, `dispatches/`, `audits/` | `C-OPS-001`, `C-OPS-002`, `C-OPS-003`, `LP-006`, `LP-007` | `python tools/check-docs-redlines.py`; `python -m py_compile tools/check-docs-redlines.py`; GitHub Actions docs-check; PR created or branch pushed; docs cross-reference check | 若写入产品代码、创建 forbidden paths、sidecar 直写 authority、或把外部研究直接写成主线事实则停线 | branch=`task/T-P0-002-parallel-execution-protocol`；等待 PR review，不置为 `done` |

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
| `T-P0-003` | 目录骨架 + 文档 lint stub + 入口文档同步 | `2026-05-03` | commit=`b32ae22edd7e60becc39d5d5d0bca8381b948254`; docs-check run=`25270586304`; 创建 docs redline lint stub；接入 GitHub Actions docs-check；同步 README / AGENTS / CLAUDE 入口口径；无产品代码 |

## Stop-the-line

- 发现 schema / state words / FS layout / LP 冲突
- 发现 raw response、日志或报账结构带出凭据
- 发现任务开始落 Phase 2-4 真实逻辑
- 发现有人尝试让 `recommendation / keyword / RAW gap` 直接创建 capture
