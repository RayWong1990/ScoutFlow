# ScoutFlow Contracts Index

> 作用：列出当前 Step0 / Phase 0 / Phase 1A 会实际约束实现的 contract。未列入本页 baseline 的内容默认不进入当前 backlog。
> `Authority-first` 四层仍保留：PRD/SRD -> specs/contracts -> code/tests -> ledger/current docs。

## 待拍板候选基准（8 group）

| Group | 旧 ID alias | 主文档 | 当前阶段 |
|---|---|---|---|
| `Authority` | C-AUTH-001, C-TASK-001, C-SCOPE-001, C-PROC-001 | docs/SRD-v1.1-amendment + AGENTS.md + locked-principles.md | Step0/Phase 1A baseline |
| `Capture` | C-CAP-001, C-CAP-002, C-CAP-003, LP-001 | docs/SRD-v1.1-amendment A012/A004/A005 + captures.py | Phase 1A baseline (merged) |
| `Receipt-Ledger` | C-WRK-001, C-ART-001 | docs/specs/worker-receipt-contract.md + jobs/complete.py | Phase 1A baseline (merged) |
| `Platform` | C-PLT-001, C-BBD-001, C-BBD-002 | docs/specs/platform-adapter-risk-contract.md + bbdown-adapter-contract-draft.md | Phase 1A baseline + draft |
| `Security` | C-SEC-001 | docs/specs/raw-response-redaction.md | Phase 1A baseline (merged) |
| `State` | state words / audio_transcript blocked / Phase Scope Freeze | PRD §6 + amendments | Phase 1A baseline |
| `Process` | C-OPS-001, C-OPS-003, LP-006 | parallel-execution-protocol.md + AGENTS.md | Phase 0 baseline |
| `Audit` | C-OPS-002, LP-007 | parallel-execution-protocol.md + README.md | Phase 0 baseline (high-risk task only) |

> Former C-TOOL-001 / C-TOOL-002 / C-NFR-001 remain historical amendment references but are not separate active contract groups after T-P1A-014.
> `C-BBD-001` is still draft only; `C-BBD-002` is still candidate draft only. Neither approves BBDown runtime, QR/manual auth, media download, ffmpeg, ASR, workers, frontend, or `audio_transcript` runtime.

## 当前实现基线状态

| Contract ID | 当前代码基线 | 范围声明 |
|---|---|---|
| C-WRK-001 | `main` baseline via `T-P1A-002`：`POST /jobs/{job_id}/complete`、receipt Pydantic models、`jobs` / `job_events` minimum schema、`idx_jobs_capture_type_dedupe` DB guard、artifact file sha/bytes validation、job/capture/dedupe 校验先于 artifact 文件校验、idempotent replay | API-side only；不创建 workers；不调用 BBDown / yt-dlp / ffmpeg；不启用 ASR 或 `audio_transcript` runtime |
| C-ART-001 | `main` baseline via `T-P1A-002`：receipt `produced_assets[]` 映射为 `artifact_assets` 行，`idx_artifact_assets_capture_file` 保护同一 capture 下 file_path 唯一，metadata_json 保留 producer / redaction / idempotency / `source_surface` 追溯字段 | 仅登记已存在于 artifacts root 的文件；不定义 Phase 2+ FS 版本化 |
| C-PLT-001 | `main` baseline via `T-P1A-002`：`platform_result` 使用既有 `PlatformResult` enum；非 `ok` receipt 将 job 标记为 `failed`，不推进 capture status，并在 `job_events` 记录 `platform_result` | 不新增平台状态映射；非 `ok` 的 operator 策略仍按后续任务收敛 |
| C-SEC-001 | `main` baseline via `T-P1A-002` + `T-P1A-004`：`raw_api_response` receipt 仍要求 `redaction_applied=true`、`redaction_policy`、非空 `sensitive_fields_removed`；主线已提供 `redact_sensitive_text`、`check-secrets-redlines.py`、secret scan contract tests 与 CI hardening | 安全基线已进入 `main`；但不替代未来 tool adapter 的更细权限/凭据注入 contract |

## 当前 research note / draft contract 状态

| Item | 当前状态 | 边界 |
|---|---|---|
| docs/research/t-p1a-003-bbdown-tool-surface-research-2026-05-03.md | PR #10 merged | Research note only；not authority；not implementation approval；not runtime approval |
| docs/specs/bbdown-adapter-contract-draft.md | `T-P1A-006` merged draft on `main` | Draft only；not final authority；not runtime approval |
| docs/research/t-p1a-007-explore-url-ux-brainstorm-2026-05-03.md | PR #15 merged research note | Research note only；not authority；not frontend / API / runtime approval |
| docs/PRD-v1.2-amendment-2026-05-03.md + docs/SRD-v1.2-amendment-2026-05-03.md | `T-P1A-010C` candidate amendment repair draft | Candidate draft only；not final authority；not runtime approval；keeps `audio_transcript` blocked |

## 当前引用但未落地的上游文档

| Upstream | 当前用途 | 说明 |
|---|---|---|
| docs/PRD-v1-2026-05-02.md | 产品叙事与原始 contract 背景 | 仍含旧 `decisions.md` / 顶层 review 队列口径 |
| docs/PRD-v1.1-amendment-2026-05-02.md | LP-001~005、quick_capture、artifact_assets、merger 规则 | Step0 继续引用，但当前硬 LP 已收敛到 `docs/specs/locked-principles.md` |
| docs/PRD-v1.2-amendment-2026-05-03.md | `T-P1A-010C` PRD 层 runtime gate / manual-auth / audio blocker candidate | Candidate draft only；待 user 拍板 |
| docs/SRD-v1-2026-05-02.md | FR / NFR / IF / DR 主体 | T-P1A-014 只调整 §6 / §7 的 lean constraints，不 promote v2 |
| docs/SRD-v1.2-amendment-2026-05-03.md | `T-P1A-010C` SRD 层 ToolPreflightResult / PlatformResult separation candidate | Candidate draft only；待 user 拍板 |

## 仅作参考 outline 的内容

| Outline | 当前不进入实现 | 主要来源 |
|---|---|---|
| Phase 1B | RAW link 真逻辑 | PRD / SRD |
| Phase 2 | Signal Workbench、Capture Plan、XHS 真逻辑 | PRD / SRD |
| Phase 3 | 推荐、重排、Hermes 调度 | PRD / SRD |
| Phase 4 | Dispatch UI、正式 review 队列 | PRD / SRD |

## 更新规则

- 任何新 contract 先入本文件，再进入任务实施。
- Contract 若仍是 outline，必须明确标 `reference only`。
- 当前阶段不把外部 research note 直接升级为主线事实。
- User 未拍板前，本表不代表已锁定未来 Phase 2+ contract。
