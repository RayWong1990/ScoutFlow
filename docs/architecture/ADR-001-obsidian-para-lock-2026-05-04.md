---
type: architecture-decision-record
title: ADR-001 Obsidian PARA Lock
date: 2026-05-05
status: Accepted (candidate)
authority_status: research-only / not-authority / not-runtime-approval
related_task: T-P1A-032
related_pr: PR #57
---

# ADR-001 Obsidian PARA Lock

## Context

ScoutFlow 需要把 repo 内 authority、repo 外 vault、以及既有 Claudian 工作流的边界锁死，避免在 Wave 3A 期间一边讨论采集系统，一边无意重造新的知识库结构。现有事实已经足够清楚：

- user 已有可运行的 PARA vault，不需要 ScoutFlow 再造一套顶层目录。
- `00-Inbox/` 已是现有 intake 入口，后续 `/intake` 与 `/compile` 依赖它。
- `System/frontmatter-templates.md` 已锁定 `02-Raw` 原始材料为 4 字段 frontmatter。
- `05-Projects/ScoutFlow/` 已有 project cockpit；`05-Projects/ContentFlow/` 证明兄弟项目也走同一模式。
- Wave 3A 当前只允许 docs/research/prototype，不批准 runtime、migration、vault side effects。

## Decision

D1. ScoutFlow 不创建新 vault，也不重排现有 PARA 顶层结构。
实现边界是引用 user 既有 `${SCOUTFLOW_VAULT_ROOT}`，而不是新增 `ScoutFlowVault/`、单独 Obsidian workspace、或 repo 内镜像 vault。

D2. ScoutFlow 只允许把 tracked 输出写入 `${SCOUTFLOW_VAULT_ROOT}/00-Inbox/`。
`02-Raw/`、`01-Wiki/`、`03-Output/` 的移动、编译、整理继续交给既有 `/intake`、`/compile` 和人工审阅链路；ScoutFlow 不直写这些层。

D3. ScoutFlow 写入 vault 时复用 RAW 的 4 字段原始材料 frontmatter 契约。
最小字段集合保持 `title`、`date`、`tags`、`status`，并与 `System/frontmatter-templates.md` 的 `02-Raw` 模板一致；不为 ScoutFlow 单独发明第二套 raw schema。

D4. ScoutFlow 不重建 Claudian 命令链。
现有 `/intake`、`/compile`、`/lint`、`/query` 继续是 vault 内处理主链；ScoutFlow 负责把材料安全送到 `00-Inbox/`，而不是复制一套 intake/compile orchestrator。

D5. ScoutFlow 的 vault 项目驾驶舱固定落在 `${SCOUTFLOW_VAULT_ROOT}/05-Projects/ScoutFlow/`。
dispatch archive、decision 拆分、handoff-log、ingest-log 等项目管理材料都归这个 cockpit；与兄弟项目 `05-Projects/ContentFlow/` 保持同一层级，不单开旁路目录。

## Consequences

- 好处：vault 边界清晰，ScoutFlow 不会把 repo 内 authority 变成 repo 外流程重写工程。
- 好处：raw frontmatter、intake 规则、project cockpit 都复用现有真相源，减少双维护。
- 好处：ContentFlow / DiloFlow / Hermes 这类兄弟项目能继续按既有 `05-Projects/*` 习惯消费 ScoutFlow 产物。
- 代价：ScoutFlow 不能把“写进 vault”扩张成“接管 vault”；任何更深层自动化都必须单独立项。
- 代价：若 `${SCOUTFLOW_VAULT_ROOT}` 未设置，SRD/implementation 必须 fail loud，而不是偷偷回退到另一个目录。
- 代价：若未来需要 richer metadata，也必须先证明与 `frontmatter-templates.md` 不冲突，再走新 dispatch。

## Configuration Boundary

`SCOUTFLOW_VAULT_ROOT` 是明确的配置边界。

- PRD 层可以把 `~/workspace/raw` 记为默认候选。
- SRD 与 implementation 层必须把“未设置”视为硬失败并显式报错。
- 本 ADR 不批准任何 runtime fallback、隐式目录创建、或 repo 内假 vault 替代方案。

## Rejected alternatives

1. Create a brand-new ScoutFlow vault: 拒绝。这样会复制 PARA 顶层、复制 intake 规则，并把项目从“采集系统”膨胀成“第二知识库”。
2. Write directly into `02-Raw/` or `01-Wiki/`: 拒绝。这样会绕过 `00-Inbox/` 入口和既有 Claudian 分类链，破坏现有审计面。
3. Invent a ScoutFlow-only raw frontmatter schema: 拒绝。RAW 已经把 4 字段模板定义成真相源，再造 schema 只会引入双轨维护。
4. Rebuild `/intake` and `/compile` inside ScoutFlow: 拒绝。ScoutFlow 当前职责是 capture-to-inbox bridge，不是替代 Claudian 知识编译系统。
5. Put project operations outside `05-Projects/ScoutFlow/`: 拒绝。会让 dispatch、decision、handoff 与兄弟项目失去共同索引位置。

## Reference map

1. `docs/research/pr55-pr74-worklist-candidate-2026-05-04.md` §2 - PR57/T-P1A-032 backbone and acceptance.
2. `docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md` §2.0-§2.1 - ScoutFlow bridge writes only to vault `00-Inbox/` and keeps project cockpit in `05-Projects/ScoutFlow/`.
3. `docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md` §0-§1 - local-only shoulder lifecycle and non-runtime posture.
4. `docs/research/opus-v3-acceptance-prd-srd-amendment-roadmap-review-2026-05-04.md` §0-§3 - RAW/PARA boundary and Obsidian-first framing.
5. `~/workspace/raw/System/frontmatter-templates.md` - `02-Raw` 4-field frontmatter source of truth.
6. `~/workspace/raw/System/intake-rules.md` - `00-Inbox/` to `02-Raw/` intake contract.
7. `~/workspace/raw/05-Projects/_project-template.md` - canonical project cockpit structure.
8. `~/workspace/raw/05-Projects/ScoutFlow/decisions/D-003-obsidian-para-lock.md` - existing vault-side lock stub.
9. `~/workspace/raw/05-Projects/ScoutFlow/README.md` - ScoutFlow cockpit placement and sibling-consumption notes.
10. `~/workspace/raw/05-Projects/ContentFlow/README.md` - sibling project precedent for shared `05-Projects/*` layout.

## Non-goals

- 不批准 vault commit runtime。
- 不修改 `docs/PRD-v2-2026-05-04.md`、`docs/SRD-v2-2026-05-04.md`、`docs/specs/**`。
- 不批准 `apps/**`、`services/**`、`workers/**`、`packages/**`、`migrations/**` 任何实现。
