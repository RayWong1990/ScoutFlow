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
> `main` 当前已合入 `T-P1A-001` 的 API-side `capture_manifest` ledger stub、`T-P1A-002` 的 receipt / ledger baseline、`T-P1A-004` 的 secret-scan / text-redaction safety baseline。`T-P1A-003` 的 PR `#10` 仍只算 research note，不进入 authority。

## 当前实现基线状态

| Contract ID | 当前代码基线 | 范围声明 |
|---|---|---|
| `C-WRK-001` | `main` baseline via `T-P1A-002`：`POST /jobs/{job_id}/complete`、receipt Pydantic models、`jobs` / `job_events` minimum schema、`idx_jobs_capture_type_dedupe` DB guard、artifact file sha/bytes validation、job/capture/dedupe 校验先于 artifact 文件校验、idempotent replay | API-side only；不创建 workers；不调用 BBDown / yt-dlp / ffmpeg；不启用 ASR 或 `audio_transcript` runtime |
| `C-ART-001` | `main` baseline via `T-P1A-002`：receipt `produced_assets[]` 映射为 `artifact_assets` 行，`idx_artifact_assets_capture_file` 保护同一 capture 下 file_path 唯一，metadata_json 保留 producer / redaction / idempotency / `source_surface` 追溯字段 | 仅登记已存在于 artifacts root 的文件；不定义 Phase 2+ FS 版本化 |
| `C-PLT-001` | `main` baseline via `T-P1A-002`：`platform_result` 使用既有 `PlatformResult` enum；非 `ok` receipt 将 job 标记为 `failed`，不推进 capture status，并在 `job_events` 记录 `platform_result` | 不新增平台状态映射；非 `ok` 的更细 operator 策略仍按后续任务收敛 |
| `C-SEC-001` | `main` baseline via `T-P1A-002` + `T-P1A-004`：`raw_api_response` receipt 仍要求 `redaction_applied=true`、`redaction_policy`、非空 `sensitive_fields_removed`；主线已提供 `redact_sensitive_text`、`check-secrets-redlines.py`、secret scan contract tests 与 CI hardening | 安全基线已进入 `main`；但不替代未来 tool adapter 的更细权限/凭据注入 contract |

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
