---
title: SRD v3 Compiled Candidate Shell
status: candidate north-star / not-authority / not promoted
authority: not-authority
created_at: 2026-05-07
created_by: cc1 compiled (来源 SRD-v2 + SRD-v3 h5-bridge promoted + SRD-v3 db-vnext candidate + U1-deep SRD supplement; 非正式 base)
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
frontend_approval: not-approved
authority_base: docs/SRD-v2-2026-05-04.md
sources:
  - docs/SRD-v2-2026-05-04.md (canonical engineering base; promoted)
  - docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md (promoted addendum, T-P1A-103 / PR #64)
  - docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md (still candidate, T-P1A-026)
  - docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/SRD-v3-supplement-anti-patterns-2026-05-07.md (supplement; not-authority)
disclaimer: |
  本文件是 thin compiled candidate shell, 不是正式 SRD-v3 promoted base.
  cloud-output 真态 SRD-v3-candidate-2026-05-07.md base file 暂未在本机查回 (find 0 hit @ 2026-05-07 17:41 GMT+8).
  本 shell 让 U1-deep `SRD-v3-supplement-anti-patterns-2026-05-07.md` 等下游引用不再孤儿,
  让"SRD-v3 候选 north-star"在工程层有可检索 anchor.
  本 shell 不构成:
    - SRD-v3 promote
    - migration approval (db-vnext)
    - runtime approval (BBDown / ffmpeg / Whisper / browser automation)
    - frontend execution gate
    - vault-commit true_write_approval (write_enabled invariant 仍 False)
    - authority writer (SRD canonical 仍是 SRD-v2 + h5-bridge promoted addendum)
revalidate_before_promote: true
sunset_trigger: |
  Replaced when (1) cloud-output 真态 SRD-v3 base 找回并 mv 替换本 shell, 或
  (2) 战友综合 SRD-v2 + h5-bridge promoted + db-vnext promote 后写出新 SRD-v3 promoted base PR.
---

# SRD-v3 Compiled Candidate Shell

## §0 Status banner (必读)

> 本文件 **不是正式 SRD-v3 promoted base**.
> 本文件是 4 份真态 source 的 thin index + 关系映射 shell, 让下游 supplement / research 不再 dangling.
> 仲裁链中, 本 shell 排在 `archive / historical notes` 之前, 排在 `chat summary` 之后, **不能** 替代以下任一:
>   - `docs/SRD-v2-2026-05-04.md` (canonical engineering base)
>   - `docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md` (promoted addendum, T-P1A-103 / PR #64)
>   - `docs/decision-log.md` / `docs/current.md` / `docs/task-index.md` (主写入窗口 authority)
>
> 如果 SRD 与本 shell 冲突, **以 SRD-v2 + h5-bridge promoted addendum 为准**.
> 如果需要正式 SRD-v3 promote, 走战友裁决 + authority writer dispatch, **不能** 用本 shell 当 promote evidence.

## §1 来源对照表

| # | Source 文件 | 状态 | 行数 | 本 shell 引用章节 |
|---|---|---|---|---|
| 1 | `docs/SRD-v2-2026-05-04.md` | promoted base (canonical) | 284 | §2 SRD-v2 关系 |
| 2 | `docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md` | promoted addendum (T-P1A-103 / PR #64) | 373 | §3 h5-bridge promoted 关系 |
| 3 | `docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md` | candidate (T-P1A-026, promote_target=SRD-v3) | 936 | §4 db-vnext candidate 关系 |
| 4 | `docs/research/strategic-upgrade/2026-05-07/outputs/U1-deep/SRD-v3-supplement-anti-patterns-2026-05-07.md` | supplement (not-authority) | 393 | §5 anti-patterns supplement 关系 |

> 本 shell 的所有事实陈述均可追溯到上述 4 个 source 之一. 本 shell **不引入新事实**, 只做 index + 关系映射.

## §2 跟 SRD-v2 (canonical base) 的关系

### §2.1 继承

- 4-layer architecture (L0 raw / L1 SQLite + FS / L2 Thin API / L3 Console projection) 沿用 SRD-v2 §1.1.
- 仲裁链 `user 最新口头 > docs/current.md / docs/task-index.md / docs/decision-log.md > PRD v2 / SRD v2 > specs > archive > chat summary` 沿用 SRD-v2 §0.2.
- 单 user / local-first 假设 (127.0.0.1, SQLite + FS 双事实源, 不做多用户/RBAC/SaaS) 沿用 SRD-v2 §0.3.
- 当前生效路径 (`POST /captures/discover`, `POST /jobs/{job_id}/complete`, `GET /captures/{capture_id}/trust-trace`, redaction baseline, tool preflight, metadata probe evidence bridge) 沿用 SRD-v2 §1.2.
- Capture entry 限制 (`platform=bilibili` + `source_kind=manual_url` + `quick_capture_preset=metadata_only`) 沿用 SRD-v2 §2.1; 拒绝 recommendation / keyword / RAW gap / `audio_transcript` / XHS / YouTube runtime.
- Trust trace 7 层结构 (capture / capture_state / metadata_job / probe_evidence / receipt_ledger / media_audio / audit) 沿用 SRD-v2 §2.3.
- "no-auth live runtime / media download / ffmpeg / ASR / audio transcript" 仍是未批准路径, 沿用 SRD-v2 §2.4.

### §2.2 不动

- 本 shell 不 supersede SRD-v2.
- SRD-v2 仍是 canonical engineering base; 本 shell 是 candidate index, 排在 SRD-v2 之后.

## §3 跟 SRD-v3 H5 Bridge promoted addendum (T-P1A-103 / PR #64) 的关系

### §3.1 已 promote 的部分

- promoted addendum, promotion_basis = `user_override_for_B2_preflight`, 见 frontmatter.
- 不 edit SRD-v2 base, 不 edit `services/**` / `apps/**` / `workers/**` / `packages/**` / `migrations/**`.
- 不构成 runtime / frontend / migration 三种 approval.

### §3.2 已锁字段名 + shape

- §17.1 H5 Capture Station 4-panel projection (`URL Bar` / `Live Metadata` / `Capture Scope` / `Trust Trace`).
- candidate stack family (Vite / React+TS / shadcn+Radix / TanStack Query+Form+Table / React Flow / Zustand / Tailwind / Lucide).
- state projection model `manual_url_entered → capture_requested → metadata_visible → scope_visible → vault_preview_ready → future_commit_gate`.
- 5 Bridge routes 表 (URL / metadata / scope / trust-trace / vault-preview = read-only ✅; vault-commit / transcribe = future-gated 🚫). **注**: 真态 5-routes 详情见 source 文件 §17.2 (本 shell 不复制全表, 避免 drift).
- Trust Trace DTO / PlatformResult / WorkerReceipt 字段 shape 已锁.
- VaultWriter path policy + frontmatter contract + fixed body sections 已锁.

### §3.3 仍未解锁

- vault-commit true write 仍 `write_enabled=False` (见 §5 supplement [canonical fact]).
- transcribe / BBDown live / ffmpeg / Whisper / browser automation 仍 future-gated.
- frontend implementation 不在 promote scope 内.

## §4 跟 SRD-v3 DB vNext candidate (T-P1A-026) 的关系

### §4.1 仍是 candidate

- 本 amendment **shape-only**, 不是 migration script.
- 不构成 migration approval, 不构成 runtime approval, 不 supersede SRD-v2.
- promote_target = SRD-v3, revalidate_before_promote = true.

### §4.2 v2 → v3 diff (5 表)

| 表 | 状态 | 关键变化 |
|---|---|---|
| `captures` | carried over with specific change | 下游 evidence-chain FK 必须 explicit `ON DELETE RESTRICT`; 17-value status enum 在 SQL 层允许, reachability 仍 phase-bounded |
| `receipt_ledger` | NEW in v3 | durable receipt identity 与 `job_events` append log 分离; 复合 FK `(job_id, capture_id, job_type, dedupe_key) -> jobs(...)` 阻断跨 capture mismatch |
| `artifact_assets` | carried over with specific change | 加 nullable `evidence_id` 绑定 file artifact 到 evidence claim; delete semantics 收紧; 复合 FK `(evidence_id, capture_id) -> evidence_ledger(...)` 阻断跨 capture forward link (F-011) |
| `evidence_ledger` | NEW in v3 | materialize evidence-claim identity (`lineage_variant` / `receipt_id` / `superseded_by`); 复合 FK `(receipt_id, capture_id) -> receipt_ledger(...)` 与 `(source_artifact_asset_id, capture_id) -> artifact_assets(id, capture_id)` 阻断跨 capture (F-011) |
| `job_events` | carried over with specific change | self-contained 进 evidence chain (复合 FK `(job_id, capture_id) -> jobs(job_id, capture_id)`); optional receipt link 也绑 `(receipt_id, capture_id)`; 无 single-column orphan path |

### §4.3 SQL 层 invariant

- partial `UNIQUE INDEX (capture_id, evidence_kind, lineage_variant) WHERE superseded_by IS NULL` — 一个 lineage 一个 current 行.
- 三 SQLite trigger:
  - `trg_evidence_supersession_lineage_check_insert` (BEFORE INSERT)
  - `trg_evidence_supersession_lineage_check_update` (BEFORE UPDATE OF `superseded_by`)
  - `trg_evidence_identity_columns_immutable` (BEFORE UPDATE OF identity columns)
- evidence chain 仅 `ON DELETE RESTRICT`, 显式禁 `CASCADE` / `SET NULL`.
- 配套 4 个 research input: `t-p1a-025-db-ledger-vnext.md` / `t-p1a-022-asr-pipeline-prestudy` / `t-p1a-023-llm-normalization-schema` / `t-p1a-024-explore-capture-scope-state-table`.

### §4.4 仍未解锁

- migration step order / transaction choreography / rollback script / INSERT/backfill / `services/api/migrations/**` 编辑均 not allowed in this amendment.

## §5 跟 U1-deep SRD-v3 anti-patterns supplement 的关系

### §5.1 supplement 定位

- status: `candidate / srd_v3_supplement_anti_patterns / not-authority`.
- 不 modify `services/**`, `apps/**`, `workers/**`, `packages/**`, `data/**`, `referencerepo/**`.
- 描述基于 v2 base + post-v2 run evidence 的 engineering anti-patterns.
- canonical fact: `write_enabled=False` 在 vault root 缺失与已解析两种状态下都是 invariant; evidence 锚点为 `services/api/scoutflow_api/bridge/config.py`.

### §5.2 anti-pattern map (10 SRD section × 2 anti-pattern)

逐章覆盖:
- §0 元信息/仲裁链 — A: candidate 富文本被当 authority; B: candidate/not-authority 标签 + user promote verdict 后台.
- §1 系统总览 — A: 把 bridge router mount 当 full bridge runtime unlock; B: 描述为 preview/dry-run only.
- §2 API contract — A: 因为 example 需要就加新 endpoint; B: 用 `/captures/discover` / `/captures/{id}/vault-preview` / bridge health/config/commit dry-run 当 anchor.
- §3 Bridge / Vault boundary — A: 翻 `write_enabled=True` 证 RAW handoff; B: staging + manual transfer proof; true write 走单独 gate.
- §4 Phase 2 entity IR — A: signals/hypotheses 没 migration approval 就建生产表; B: IR shape 留 candidate, 走 U3/schema gate.
- §5 Runtime / browser / migration — A: Playwright/ASR 做漂亮 demo; B: blocked overflow + 显式 dispatch.
- §6 Multi-agent contract — A: subagent 静默扩 path; B: STOP + truth-conflict / amendment.
- §7 PF-V handoff — A: 生成图当 frontend acceptance; B: 走人审 verdict + future bootstrap dispatch.
- §8 DR / local-first — A: 把企业 SLO/RBAC/cloud DAM 抄进单用户工具; B: 守 local SQLite/FS/plain text + 小容量信封.
- §9 追溯 / archive — A: v3 干净就删旧 receipt; B: append archive/supersession note, 不擦审计.

### §5.3 silent flexibility 8 类 anti-pattern (来自 4 run evidence)

- A1 production code expansion (PF-LP-02; PR #231)
- A2 test harness expansion (PF-LP-13 conftest.py; PR #231)
- A3 companion test de-dup (PF-LP-01; PR #231)
- Run-2 synthetic UAT inflation (works → partial; PR #239)
- Run-2 SHA flattening (execution-final SHA vs audit-final-after-receipt-bundle SHA; PR #239)
- Run-3+4 single PR closeout (single-shot direct merge; PR #240)
- RAW transfer skip (user A-path; PR #240)
- PF-C4 premature opening (`can_open_c4=false`; PR #240)

通用 guard: 保留 verdict 词汇 (`T-PASS` / `partial` / `REJECT_AS_*` / `concern`), 记录 user authorization, 不允许 wording 把 synthetic proof 升级为 visual UAT.

### §5.4 8 条 implementation guardrail

来自 supplement §3:
1. Bridge route handler — fail-loud 或 dry-run, 不准当 side effect 建文件.
2. Vault preview markdown 可渲染, commit dry-run 不可 mutate RAW/vault, 直到 true_write_approval.
3. API schema 可含 future 字段, validator 必须 reject 不支持的写.
4. Frontend disabled action 文案必须说 "blocked", 默认不准说 "upcoming".
5. 本地 server / npm build proof 仅当 local proof, 不是 global runtime approval.
6. Codex/Claude/Hermes handoff 语言可用, single-writer-per-conflict-domain 仍 enforce.
7. Traceability 行不准用 "source: memory"; 必须 URL / file path / limitation marker.
8. 外审 path 2026-05-07 仍 404 时, 缺失即 blocker, 不准从 PR body 编造.

## §6 已 PROMOTED 的部分 (即 SRD-v3 候选 base 的"已锁地基")

来源: SRD-v2 (全文 promoted) + h5-bridge addendum (promoted via T-P1A-103 / PR #64).

- SRD-v2 §0–§9 全部内容 (元信息 / 系统总览 / FR / NFR / boundary / archive 链).
- H5 4-panel projection shape + state projection model.
- Bridge route group 5 routes 表 (read-only ✅ 与 future-gated 🚫 分类).
- VaultWriter path policy + frontmatter + fixed body section.
- Trust Trace DTO / PlatformResult / WorkerReceipt shape.
- candidate frontend stack family (非版本锁).

## §7 CANDIDATE 的部分 (待 promote)

| Candidate item | 来源 | 待 promote 触发 |
|---|---|---|
| DB v0 → v1 schema (5 表 diff) | db-vnext candidate | T-P1A-026 promote dispatch |
| evidence_ledger / receipt_ledger materialization | db-vnext candidate | 同上 + U3-deep entity samples 校核 |
| 三 SQLite trigger DDL | db-vnext candidate | 同上 |
| Phase 2 entity IR (CapturePlan / Hypothesis / Signal / TopicCard) | db-vnext + U3-deep | U3 schema gate |
| ASR pipeline (Whisper family) | research t-p1a-022 | Wave 6 unlock + runtime approval |
| LLM normalization schema | research t-p1a-023 | 同上 + schema gate |
| capture scope state table | research t-p1a-024 | promote 进 SRD-v3 §2 |
| transcribe pipeline | h5-bridge addendum (future-gated) | true_write_approval + Wave 6 |
| vault-commit true write | h5-bridge addendum (future-gated) | true_write_approval (替换 `write_enabled=False`) |
| browser automation | SRD-v2 §2.4 (未批准) | runtime approval dispatch |
| 本 shell 列举的 8 条 implementation guardrail | U1-deep supplement | 战友裁决 + 写进 SRD-v3 promoted base 或 dispatch contract |
| 10 anti-pattern map by section | U1-deep supplement | 同上 |

## §8 何时升 SRD-v3 promoted base

任一触发即可 sunset 本 shell:

1. cloud-output 真态 `SRD-v3-candidate-2026-05-07.md` base 找回 → `mv` 替换本 shell, 真态 base 走正常 promote dispatch.
2. db-vnext candidate (T-P1A-026) promote 完成 → 战友综合 SRD-v2 + h5-bridge promoted + db-vnext promoted 写新 SRD-v3 promoted base PR.
3. 战友显式裁决"以本 shell 为 SRD-v3 base 起草" → 走 authority writer dispatch (本 shell 仍不能自己 promote).

sunset 时, 本 shell 应:
- 移入 `docs/archive/` 或被新 SRD-v3 promoted base 直接覆盖.
- 在 `docs/decision-log.md` / supplement frontmatter 留下 supersession 记录 (anti-pattern §9 要求 append, 不准擦).

## §9 不构成 (硬红线复述)

本 shell **不构成**:

- runtime approval (BBDown live / ffmpeg / Whisper / browser automation 全部仍 blocked, 见 SRD-v2 §2.4).
- migration approval (db-vnext schema 仍 candidate, 不准生成 migration script / INSERT / backfill).
- frontend execution gate (h5-bridge addendum 明确 not frontend approval; PF-V handoff 走人审).
- vault-commit true write unlock (`write_enabled=False` invariant, 见 supplement [canonical fact]).
- transcribe unlock (future-gated in h5-bridge addendum).
- browser automation unlock.
- authority writer (SRD canonical 仍 = SRD-v2 + h5-bridge promoted addendum; `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` 仍是主写入窗口).
- candidate → promoted 的自动晋升路径 (任何 promote 必须走战友裁决 + dispatch).

## §10 维护

- 本 shell 由 cc1 sidecar 撰写 (CLAUDE.md sidecar 输出规则: 默认 read-only, 不直接成主线事实).
- 任何修改本 shell 必须保持 sources 列表与真态 source 文件 sha256 / commit 对齐.
- 真态 source 文件升级时 (例如 db-vnext candidate promote 或 SRD-v2 升 v3), 本 shell 必须同步或被 sunset.
- 不允许在本 shell 内引入 sources 之外的事实陈述.

---

> 文档结束. 战友若同意以本 shell 为 SRD-v3 候选 north-star anchor, 请在 `docs/decision-log.md` 记录 promote verdict 并触发 authority writer dispatch.
