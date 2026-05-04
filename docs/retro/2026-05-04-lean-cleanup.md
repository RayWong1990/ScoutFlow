# Lean Cleanup Retro — 2026-05-04

## A. 砍 (Drop)

- NFR-REL-07 季度备份演练 — 单人项目无 SLA，rsync + Time Machine 已够
- NFR-USA-01..05 主观 UX / frontend 指标 — Phase 2+ frontend，不进当前硬 NFR
- NFR-OBS-01 全端点 audit log — FastAPI 默认 access log 已够；仅保留 state-changing job receipt / decision-log audit
- NFR-OBS-05/06/07 dashboard / token / Source Health — Phase 2+
- NFR-MAINT-07 docstring 强制 — 单人项目自我消耗，type hint 已覆盖主要边界
- NFR-SEC-12 LLM 月预算 — 供应商后台已有
- NFR-TEST-08 测试时长 — 个人 CI 无 cost concern
- NFR-PERF-03/05~11 — Phase 1A 末或 Phase 2+，不作为当前硬门
- CR-ToS-05 fair use <=30s — SaaS 思维；保留个人研究 / 不公开分发
- LP-003 merger-of-record — 已被 LP-006 覆盖
- LP-005 命名禁区 LP — 由 docs-redlines lint 替代

## B. 降级 (Relax)

- NFR-MAINT-01 测试覆盖率 — 核心 95%，非核心按风险
- NFR-MAINT-02 type hint — 边界 100%，内部按需
- NFR-MAINT-03 TypeScript strict — `[DEFERRED until Phase 1B+ frontend lane]`
- NFR-MAINT-04/06 文件行数 / 嵌套 — 改为 retro 解释，不强制 lint
- NFR-PERF-01/02 — 合并为本机三端点 P95：`/captures/discover` < 500ms、`/jobs/{id}/complete` < 1s、`/captures/{id}/trust-trace` < 500ms
- NFR-OBS-02 — receipt schema 由 C-WRK-001 严格定义；NFR 不重复字段清单
- NFR-SEC-04 — 保留默认 bind 127.0.0.1，不要求额外 lint
- LP-007 GitHub audit — 降级为 high-risk / material task only
- API user-friendly error — dev mode 可显示 stack；persisted / prod logs 仍不泄露凭据

## C. 吸收 (Absorb)

- LP-003 -> 并入 LP-006 `Single Writer / Multi Reviewer` 描述段
- LP-005 命名禁区 -> 由 `tools/check-docs-redlines.py` lint enforce
- C-TOOL-001 / C-TOOL-002 / C-NFR-001 -> 降为 historical amendment references，不再作为独立 active contract group

## D. 不动 (Keep)

- 4 层架构 + state words + receipt schema + PlatformResult enum
- LP-001 Capture Scope Gate（硬 test）
- LP-006 Single Writer
- C-SEC-001 redaction 全部红线
- C-WRK-001 worker receipt 完整 schema
- C-PLT-001 12 enum
- Trust Trace 分层 DTO
- `audio_transcript` blocked

## E. Active lane 修订

- 旧：活动任务上限 3
- 新：Active product lane max = 3 + Authority writer max = 1
- 理由：user 目标是"能并行就并行"；防 state drift 应防 authority 双写，不防多 lane

## F. 入口三件套减重

- `README.md`: <=30 行
- `AGENTS.md`: <=45 行
- `CLAUDE.md`: <=20 行
- 历史叙述移到 `docs/task-index.md` / `docs/decision-log.md`
