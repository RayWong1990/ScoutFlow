# ScoutFlow Contracts Index

> 作用：列出当前 Step0 / Phase 0 / Phase 1A 会实际约束实现的 contract。未列入“待拍板候选基准”的内容默认不进入当前 backlog。

## 待拍板候选基准

| Contract ID | Contract | 当前候选文档 | Owner | 当前阶段 |
|---|---|---|---|---|
| `C-AUTH-001` | Authority Chain | `docs/SRD-v1.1-amendment-2026-05-03.md` A001 | user | Step0 |
| `C-TASK-001` | Task Index 规则 | `docs/task-index.md` + amendment A003 / A011 | Codex | Step0 |
| `C-TOOL-001` | Tool Roster | `docs/SRD-v1.1-amendment-2026-05-03.md` A008 | user | Step0 |
| `C-TOOL-002` | Research Note Protocol | `docs/SRD-v1.1-amendment-2026-05-03.md` A009 | user | Step0 |
| `C-SCOPE-001` | Phase Scope Freeze | `docs/SRD-v1.1-amendment-2026-05-03.md` A010 | user | Step0 |
| `C-PROC-001` | Definition of Ready / Done / Stop-the-line | `docs/SRD-v1.1-amendment-2026-05-03.md` A011 | user | Step0 |
| `C-CAP-001` | Capture Entry API Semantics | `docs/SRD-v1.1-amendment-2026-05-03.md` A012 | Codex | Phase 1A |
| `C-CAP-002` | `capture_mode` / `quick_capture_preset` | `docs/SRD-v1.1-amendment-2026-05-03.md` A004 | Codex | Phase 1A |
| `C-CAP-003` | `source_kind` / `created_by_path` | `docs/SRD-v1.1-amendment-2026-05-03.md` A005 | Codex | Phase 1A |
| `C-ART-001` | `artifact_assets` 命名与台账入口 | `docs/SRD-v1.1-amendment-2026-05-03.md` A006 + `docs/specs/worker-receipt-contract.md` | Codex | Phase 1A |
| `C-WRK-001` | Worker Receipt & Artifact Ledger | `docs/specs/worker-receipt-contract.md` | Codex | Phase 1A |
| `C-PLT-001` | Platform Adapter Risk Contract | `docs/specs/platform-adapter-risk-contract.md` | Codex | Phase 1A |
| `C-SEC-001` | Raw Response Redaction & Credential Safety | `docs/specs/raw-response-redaction.md` | Codex | Phase 1A |
| `C-NFR-001` | NFR 分级 | `docs/SRD-v1.1-amendment-2026-05-03.md` A007 | user | Step0 |
| `C-OPS-001` | Parallel Execution Protocol | `docs/specs/parallel-execution-protocol.md` | Codex | Step0 / Phase 0 candidate baseline |
| `C-OPS-002` | GitHub External Audit Workflow | `README.md` + `AGENTS.md` + `docs/specs/parallel-execution-protocol.md` | Codex | Step0 / Phase 0 candidate baseline |
| `C-OPS-003` | Single Writer / Multi Reviewer | `AGENTS.md` + `CLAUDE.md` + `.github/pull_request_template.md` | Codex | Step0 / Phase 0 candidate baseline |

> `C-OPS-001` / `C-OPS-002` / `C-OPS-003` 只约束 Step0 / Phase 0 的协作方式，不是产品代码 approval。
> `T-P1A-001` 当前只实现 API-side `capture_manifest` ledger stub；完整 worker receipt endpoint 与 worker-side artifact writeback 仍属后续任务范围。

## 当前引用但未落地的上游文档

| Upstream | 当前用途 | 说明 |
|---|---|---|
| `docs/PRD-v1-2026-05-02.md` | 产品叙事与原始 contract 背景 | 仍含旧 `decisions.md` / 顶层 review 队列口径 |
| `docs/PRD-v1.1-amendment-2026-05-02.md` | LP-001~005、quick_capture、artifact_assets、merger 规则 | Step0 继续引用，但研究 note 口径已改轻 |
| `docs/SRD-v1-2026-05-02.md` | FR / NFR / IF / DR 主体 | 仍有待 amendment patch 的旧残留 |
| `docs/ScoutFlow-project-organization-docs-v0/ScoutFlow-Project-Operating-Model-v0.1.md` | 目录、角色、薄治理原则 | 仍含旧 Claude Design 与重治理想法 |

## 仅作参考 outline 的内容

| Outline | 当前不进入实现 | 主要来源 |
|---|---|---|
| Phase 1B | RAW link 真逻辑 | PRD / SRD |
| Phase 2 | Signal Workbench、Capture Plan、XHS 真逻辑 | PRD / SRD |
| Phase 3 | 推荐、重排、Hermes 调度 | PRD / SRD |
| Phase 4 | Dispatch UI、正式 review 队列 | PRD / SRD |

## 更新规则

- 任何新 contract 先入本文件，再进入任务实施
- contract 若仍是 outline，必须明确标 `reference only`
- 当前阶段不把外部研究 note 直接升级为主线事实
- user 未拍板前，本表不代表已锁定 contract
