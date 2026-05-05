# ScoutFlow Contracts Index

> 作用：列出当前 Step0 / Phase 0 / Phase 1A 会实际约束实现的 contract。未列入本页 baseline 的内容默认不进入当前 backlog。
> `Authority-first` 产品 4 层架构仍以 PRD/SRD 为准；本页只维护当前 contract group 视图、旧 ID alias 与已落地 baseline。

## 待拍板候选基准（8 group）

| Group | 旧 ID alias | 主文档 | 当前阶段 |
|---|---|---|---|
| `Authority` | C-AUTH-001, C-TASK-001, C-SCOPE-001, C-PROC-001 | docs/SRD-v2-2026-05-04.md + AGENTS.md + locked-principles.md | Step0/Phase 1A baseline |
| `Capture` | C-CAP-001, C-CAP-002, C-CAP-003, LP-001 | docs/PRD-v2-2026-05-04.md + docs/SRD-v2-2026-05-04.md + captures.py | Phase 1A baseline (merged) |
| `Receipt-Ledger` | C-WRK-001, C-ART-001 | docs/specs/worker-receipt-contract.md + jobs/complete.py | Phase 1A baseline (merged) |
| `Platform` | C-PLT-001, C-BBD-001, C-BBD-002 | docs/specs/platform-adapter-risk-contract.md + bbdown-adapter-contract-draft.md | Phase 1A baseline + draft |
| `Security` | C-SEC-001 | docs/specs/raw-response-redaction.md | Phase 1A baseline (merged) |
| `State` | state words / audio_transcript blocked / Phase Scope Freeze | docs/PRD-v2-2026-05-04.md + docs/SRD-v2-2026-05-04.md | Phase 1A baseline |
| `Process` | C-OPS-001, C-OPS-003, LP-006 | parallel-execution-protocol.md + AGENTS.md | Phase 0 baseline |
| `Audit` | C-OPS-002, LP-007 | parallel-execution-protocol.md + README.md | Phase 0 baseline (high-risk task only) |

> Former C-TOOL-001 / C-TOOL-002 / C-NFR-001 remain historical references but are not separate active contract groups after T-P1A-014 and T-P1A-015.
> `C-BBD-001` is still draft only. `C-BBD-002` stays `candidate draft only`: its gate language is now promoted into PRD/SRD v2 as baseline wording, but BBDown runtime itself is still not approved.

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
| docs/architecture/ADR-001-obsidian-para-lock-2026-05-04.md | PR #57 merged ADR candidate | Research-only ADR candidate；locks PARA boundary for later bridge/vault work；not base PRD/SRD authority；not runtime approval |
| docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md | PR #58 merged candidate amendment | Candidate amendment only；not promoted base PRD；not runtime approval |
| docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md | PR #64 merged candidate amendment | Candidate amendment only；not SRD-v3 promoted authority；not runtime approval；not migration approval |
| docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md | PR #59 merged protocol candidate | Candidate only；keeps enforced baseline at product_lane_max=3 and authority_writer_max=1 until explicit closeout approval |
| docs/architecture/pr-factory-tooling-plan-2026-05-04.md + tools/scoutflow_pr_factory.py | PR #66 merged tooling candidate | Local-only shoulder helper candidate；--dry-run and referencerepo guard landed；future `tools/pr-factory/**` split deferred；not runtime approval |
| services/api/scoutflow_api/bridge/SPEC.md | PR #70 merged spec candidate | spec only；locks thin route-group shape and BridgeErrorCode；not runtime approval |
| docs/visual/h5-capture-station/** | PR #71 merged design candidate | design-only package；locks 4-panel H5 station and 5-Gate audit；not frontend implementation approval |
| services/api/scoutflow_api/vault/SPEC.md | PR #72 merged spec candidate | spec only；locks SCOUTFLOW_VAULT_ROOT fail-loud, raw 4-field frontmatter, path containment, idempotency；not runtime approval |
| docs/research/h5-prototype-mock-pointer-2026-05-05.md | PR #73 merged prototype pointer | repo-external prototype pointer only；ScoutFlow tracked diff stayed pointer-only；not frontend implementation approval |
| docs/research/shoulders/adapt-decision-table-2026-05-05.md | PR #74 merged decision candidate | candidate-only shoulder decision table；narrows adapt/reference_only route without approving implementation |
| docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md | PR #51 candidate amendment + PR #53 audit-fix merged on main | Candidate amendment only; not SRD-v3 promoted authority; not migration approval; not runtime approval; F-012 wording and evidence identity immutability guard addressed by T-P1A-029 |
| docs/PRD-v2-2026-05-04.md + docs/SRD-v2-2026-05-04.md | promoted v2 base | Promoted base；runtime boundaries still gated；keeps `audio_transcript` blocked |

## 当前引用但未落地的上游文档

| Upstream | 当前用途 | 说明 |
|---|---|---|
| docs/PRD-v2-2026-05-04.md | promoted PRD base，含 v1 + v1.1 + v1.2 的稳定产品规则 | 当前产品 authority baseline |
| docs/SRD-v2-2026-05-04.md | promoted SRD base，含 v1 + v1.1 + v1.2 的稳定工程规则 | 当前工程 authority baseline |

## Promoted Amendments

| Amendment | Promoted scope | Promotion gate evidence | Still-gated boundary |
|---|---|---|---|
| docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md | extends `docs/PRD-v2-2026-05-04.md`：H5 Capture Station product surface + PARA vault knowledge layer + PR factory surge product direction | T-P1A-102, 2026-05-05; gates: Wave 3A closeout (T-P1A-031~042 merged), PR #77 pack-lint durability gate (T-P1A-101) | runtime approval still gated; frontend implementation approval still gated; sunset when PRD-v3 base supersedes |
| docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md | extends `docs/SRD-v2-2026-05-04.md`：L3 H5 projection shape + L2 Bridge route group + VaultWriter contract on PARA vault | T-P1A-102, 2026-05-05; gates: Wave 3A closeout, PR #77 pack-lint durability gate; revalidation folded into this gate | runtime approval still gated; frontend approval still gated; migration approval still gated; sunset when SRD-v3 base supersedes |

> Promoted Amendments 与 PRD-v2 / SRD-v2 base 同等参与 contract group 决策；但运行时、前端实装、migration 仍受各自独立 gate 约束，不因 promotion 自动解禁。
> Filenames retain "-candidate-2026-05-04" suffix for path stability; YAML frontmatter `status: amendment / promoted` 是真源。
> Distinct from the separate DB-schema SRD-v3 candidate (an independent amendment tracked in the research/draft contract section above; **未** promote at T-P1A-102).

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
