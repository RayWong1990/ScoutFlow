# ChatGPT Session Prompts Archive — 2026-05-03

> Source: 网页版 GPT「采集线」项目会话。
> Purpose: 保存本轮外部审计、任务派单、并行协作规则和 prompt 结构，降低 user 在 Codex / GPT / Claude / OpenClaw / Hermes 之间复制粘贴成本。
> Status: reference note only.
> Authority: 本文件不替代 `docs/current.md`、`docs/task-index.md`、`docs/specs/contracts-index.md`、`AGENTS.md` 或 locked-principles / LP。
> Product-code approval: No.
> Archive integrity note: 原始 prompt 中的旧状态检测短语已语义化保留，避免被误判为当前 authority 状态。

## 1. Session Context

本轮会话围绕 ScoutFlow Phase 0 / Step0 的 repo bootstrap、文档红线 lint、GitHub 外部审计和多工具并行协作展开。

已审计/推动的任务包括：

- `T-P0-001 review-fix + close`
- `T-P0-003 docs redline lint stub`
- `T-P0-003 review-fix + close`
- `T-P0-002 parallel execution protocol baseline` 派单准备
- ChatGPT session prompt archive 归档建议

本轮形成的关键协作结论：

- GitHub commit / PR diff / workflow run 是跨工具审计真源。
- 网页版 GPT Pro 负责外部审计、prompt architect、commit / PR reviewer。
- Codex Desktop 是 repo writer / commit owner。
- Claude Code / VSCode 适合文档审读、IA / UX 评论、局部文案修订、contract 校对。
- OpenClaw / GLM 适合次级 research、风险反驳、资料整理，默认 read-only。
- Hermes Agent / Kimi 适合调度设计参考、长上下文归纳、任务拆解建议，默认 read-only。
- user 保留任务选择、范围审批、合并推进和越界判断权。

## 2. Prompt: T-P0-001 review-fix + close

Purpose:
修复 `T-P0-001 review` 审计发现的文档口径问题，并闭合 `T-P0-001` 为 `done`。

Core instructions:
- 修复 `AGENTS.md` 中 `T-P0-001` 的旧 `执行中` 状态残留。
- 修复 `docs/task-index.md` 中 `T-P0-002` / `T-P0-003` 的 forbidden paths，补齐 `candidates/`、`dispatches/`、`audits/`。
- 更新 `docs/decision-log.md`，记录 `T-P0-001 review-fix completed`。
- 将 `T-P0-001` 从 Review 移到 Done。
- `docs/current.md` 中 `T-P0-001` 状态改为 `done`。
- 不进入 `T-P0-002` / `T-P0-003`。
- 不创建 API / worker / Console 产品代码。

Validation used:
- `git status --short`
- `git diff -- AGENTS.md docs/current.md docs/task-index.md docs/decision-log.md`
- `grep -RIn "T-P0-001.*执行中\|in_progress" AGENTS.md docs/current.md docs/task-index.md docs/decision-log.md`
- forbidden root dirs check
- `data/` and `referencerepo/` local-only checks

Commit message suggested:
`Close T-P0-001 review with doc consistency fixes`

## 3. Prompt: T-P0-003 docs redline lint stub

Purpose:
创建 Phase 0 的最小文档红线 lint stub，并同步入口文档，防止 agent 误入产品代码或重治理目录。

Core instructions:
- 创建 `tools/check-docs-redlines.py`。
- 更新 `.github/workflows/docs-check.yml`，运行 docs redline lint。
- `README.md` 不再写死当前任务 `T-P0-001`，改为以 `docs/current.md` 为准。
- `AGENTS.md` 当前活动任务切到 `T-P0-003`。
- `CLAUDE.md` 增加状态源、Claude sidecar 定位和 forbidden paths。
- `docs/current.md` 当前任务改为 `T-P0-003`，状态 `review`。
- `docs/task-index.md` 将 `T-P0-003` 放入 Review，`T-P0-002` 保持 backlog。
- 不创建 `apps/ services/ workers/ packages/ candidates/ dispatches/ audits/`。
- 不写 API / worker / Console 产品代码。

Lint requirements:
- required docs exist
- forbidden root dirs absent
- `data/` and `referencerepo/` not tracked
- banned naming scan
- `T-P0-001` old `执行中` status absent
- `AGENTS.md` / `docs/current.md` / `docs/task-index.md` task state consistency

Commit message suggested:
`Implement T-P0-003 docs redline lint stub`

## 4. Prompt: T-P0-003 review-fix + close

Purpose:
修复 `T-P0-003` 审计发现的 task-index Done 表状态解析问题，然后闭合 `T-P0-003` 为 `done`。

Audit finding:
`tools/check-docs-redlines.py` 旧版 `task_index_state()` 只适配 Review / Backlog 表。Done 表第三列是完成时间，不能当状态解析。若 `T-P0-003` 移入 Done，`docs/current.md` 写 `done`，旧 lint 会误判为状态冲突。

Core instructions:
- 改造 `tools/check-docs-redlines.py`，使其按 section 解析 `docs/task-index.md`：
  - Review / Backlog 使用 Status 列
  - Done 返回 `done`
  - Blocked 返回 `blocked`
  - duplicate task ID 报错
- 增加最小 parser self-check：
  - Review 表解析为 `review`
  - Done 表解析为 `done`
  - duplicate 任务报错
- 将 `T-P0-003` 从 Review 移到 Done。
- `docs/current.md` 中 `T-P0-003` 状态改为 `done`。
- `AGENTS.md` 标明 `T-P0-003` 已闭合。
- `docs/decision-log.md` 记录 `T-P0-003 completed`。
- 不进入 `T-P0-002` 或 Phase 1A。

Commit message suggested:
`Close T-P0-003 review and harden docs redline state parsing`

## 5. Prompt: T-P0-002 parallel execution protocol baseline

Purpose:
将多窗口 / 多 agent 并行协作规则落到 repo 文档中，降低 user 复制粘贴、人审节点和跨工具交接成本。

Recommended mode:
Branch / PR mode, not direct push to main.

Branch:
`task/T-P0-002-parallel-execution-protocol`

Core document to create:
`docs/specs/parallel-execution-protocol.md`

Required principles:
- Single Writer
- Multi Reviewer
- GitHub as Audit Source
- Ledger First
- No Sidecar Authority Writes
- Branch Before Parallel
- Human Gate

Required tool roles:
- Codex Desktop: 主写入者 / repo writer / commit owner，可调 subagent，但最终单点 commit
- Codex subagent: 并行 scan / lint / diff review / 风险列举，不独立写回 task-index/current
- 网页版 GPT Pro: GitHub 外部审计、prompt architect、PR / commit reviewer，不直接改 repo
- Claude Code / VSCode: 文档审读、IA / UX 评论、局部文案、contract 校对，不主导代码主线
- OpenClaw / GLM: 次级 research、资料整理、风险反驳，默认 read-only
- Hermes Agent / Kimi: 调度设计参考、长上下文归纳、任务拆解建议，默认 read-only
- user: 选择任务、审批范围、处理合并、判断是否进入下一阶段

Files to update:
- `docs/current.md`
- `docs/task-index.md`
- `docs/decision-log.md`
- `docs/project-context.md`
- `docs/specs/contracts-index.md`
- `docs/specs/locked-principles.md`
- `docs/specs/parallel-execution-protocol.md`
- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `.github/pull_request_template.md`
- `tools/check-docs-redlines.py` only if required
- `.github/workflows/docs-check.yml` only if required

New LPs proposed:
- `LP-006 — Single Writer / Multi Reviewer`
- `LP-007 — GitHub Audit Source`

New contracts proposed:
- `C-OPS-001 Parallel Execution Protocol`
- `C-OPS-002 GitHub External Audit Workflow`
- `C-OPS-003 Single Writer / Multi Reviewer`

Commit message suggested:
`Start T-P0-002 parallel execution protocol baseline`

## 6. Parallel Execution Default for Future Prompts

Future GPT dispatches should default to:

- reduce user copy/paste burden
- prefer GitHub commit / PR / run as fact source
- use branch / PR mode once parallel work begins
- keep `docs/current.md` and `docs/task-index.md` as authority
- only main writer updates authority docs
- sidecars are read-only unless explicitly authorized
- Codex may use subagents for scan/review/validation
- OpenClaw / Hermes / Claude are useful but should not directly mutate authority
- GPT Pro remains external auditor and prompt architect

## 7. Cloud / Local Agent Communication Model

Current practical model:

- GitHub is the shared message bus.
- Local agents communicate by creating commits, branches, PRs, workflow runs, and optionally GitHub issues.
- Web GPT audits GitHub artifacts and emits next prompts or review decisions.
- User does not need to paste full files if commit hash + run id + summary are available.
- If user is away, autonomous local execution still requires a local/cloud agent with repo write permissions. Web GPT in this session does not wake local tools by itself.

Recommended exchange packet:

```text
Task ID:
Branch:
Commit:
PR:
Workflow run:
Changed files:
Validation:
Risks:
Next decision needed:
```

## 8. Stop-the-line Rules Preserved

Stop if any task:

- creates `apps/ services/ workers/ packages/`
- tracks `data/` or `referencerepo/`
- creates `candidates/ dispatches/ audits/`
- writes API / worker / Console product code before approval
- introduces browser automation
- moves Phase 2-4 outline into current implementation
- lets recommendation / keyword / RAW gap directly create capture
- leaks credentials, token, raw response, or sensitive logs
- allows multiple agents to mutate `docs/current.md` or `docs/task-index.md` in the same task without explicit merge order

## 9. Notes for Future Review

This archive is a reference note only. It should not be used as authority over:

- `docs/current.md`
- `docs/task-index.md`
- `AGENTS.md`
- `docs/specs/contracts-index.md`
- `docs/specs/locked-principles.md`

If conflict appears, use authority docs and GitHub commit / PR / workflow run as source of truth.
