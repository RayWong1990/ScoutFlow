# ScoutFlow AGENTS
> Scope: repo root. 中文优先；任务事实以 `docs/current.md` / `docs/task-index.md` 为准。
## 1. 进入项目先读
1. `docs/current.md`
2. `AGENTS.md`
3. `docs/task-index.md`
4. `docs/specs/contracts-index.md`
5. 当前任务直接引用的 PRD / SRD / spec
## 2. 当前 Phase
- Phase：`1A`；当前指针：`docs/current.md`
- 当前活动任务：无 active product task；`T-P1A-072` 仅作为 authority ledger-open anchor 保留；`T-P1A-073 ~ T-P1A-099` 已通过 Wave 4 Batch 2 + Batch 3 live PR chain 落地；`Dispatch131 ~ Dispatch172 / T-P1A-110 ~ T-P1A-151` 已作为 Wave 5 candidate docs/spec/visual/audit chain landed；`Dispatch173 ~ Dispatch176 / T-P1A-152 ~ T-P1A-155` 已完成 Wave 5 closeout、Wave 6 candidate open 与 overflow/handoff candidate 落地；当前状态=`WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`；当前仍无已打开的 code-bearing next gate；`PR #93` 已由 `T-P1A-103` supersede，不能原样合并；PRD-v2.1 + SRD-v3 H5/Bridge 通过 `user_override_for_B2_preflight` promoted 为 B2 planning/contract addenda；`PR127 / T-P1A-101` 仅保留为历史 handoff 命名；DB vNext remains candidate-only / not migration approval / not runtime approval；详见 `docs/current.md` / `docs/task-index.md`。
- Active product lane max=`3`; Authority writer max=`1`; review / audit / research lane 不计入 product lane，除非写 authority。
## 3. 当前允许路径
- Quick answer: 可改状态/入口/contract/retro/research 授权路径；不可改 local-only 目录、未授权 runtime、凭据或 final authority 口径。
- 状态写回：`docs/task-index.md` -> `docs/current.md` -> `docs/decision-log.md`
- Entry / authority：`README.md`、`AGENTS.md`、`CLAUDE.md`
- Contracts：`docs/specs/contracts-index.md`、`docs/specs/locked-principles.md`、`docs/specs/parallel-execution-protocol.md`
- Retro / research / architecture：`docs/retro/**`、`docs/research/**`、`docs/architecture/**`；不得自动升级为 authority
## 4. 当前硬红线
- Stop-line summary: secrets / local-only dirs / runtime / final-authority drift / schema-state-FS-LP drift 都是立即停线项。
- 不修改 `data/`、`referencerepo/`，不提交 cookie / token / secret / raw credential material。
- 不创建或修改 `workers/`、`packages/`；`apps/**`、`services/**` 只有当前 dispatch 明确授权路径时才可动。
- 不自动运行 BBDown / yt-dlp / ffmpeg / ASR / browser automation。
- `recommendation / keyword / RAW gap` 不直接创建 capture。
- `POST /captures/discover` 是 capture creation entrypoint，不是 source discovery。
- `audio_transcript` runtime 仍 blocked。
- Research note / draft spec / chat summary 不得写成 final authority。
- 触碰 schema / state words / FS layout / LP 时先停线。
## 5. 写回顺序
- 任务状态变化：先 `docs/task-index.md`，再 `docs/current.md`，必要时追加 `docs/decision-log.md`。
- Contract 变化同步 `docs/specs/contracts-index.md`；LP 变化同步 `docs/specs/locked-principles.md`。
## 6. 并行规则
- 遵守 `docs/specs/parallel-execution-protocol.md`：lane=3 + authority writer=1。
- `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` 只能由当前主写入窗口修改。
## 7. 工具分工
| Tool | Role | Boundary |
|---|---|---|
| `Codex Desktop` | 主写入、验证、commit / PR owner | 不绕过账本 |
| `Codex subagent` | scan / review / risk list | 不写 authority |
| `Claude Code` | IA / UX / contract review | 默认 read-only |
| `GPT Pro` | GitHub 外审 | 不直接改 repo |
| `OpenClaw/Hermes` | research / rebuttal | 默认 read-only |
## 8. 输出要求
引用具体文件；区分 enforced contract、candidate、Phase 2+ outline；不把聊天内容当仓库事实。
