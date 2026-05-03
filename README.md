# ScoutFlow

ScoutFlow 是一个面向个人研究工作流的 authority-first 内容采集、转写、规整与证据账本工作台。

## 当前阶段

- 当前阶段：`Phase 1A`
- 当前任务与状态：以 `docs/current.md` 为准
- 当前焦点：`T-P1A-009` BBDown local-only runtime spike report 已通过 PR `#19` 合入 `main`；`T-P1A-008` BBDown sanitized fixture parser 已通过 PR `#17` 合入 `main`
- 当前不做：workers / frontend / 浏览器自动化 / 真实下载 / BBDown runtime / yt-dlp runtime / ffmpeg runtime / ASR / `audio_transcript` runtime

## 当前基调

- `authority-first`：SQLite、FS layout、state words 是后续实现的约束中心
- `/captures/discover` 是 `capture 创建入口（capture creation entrypoint）`
- `recommendation / keyword / RAW gap` 当前不得直接创建 capture
- PR `#10` 的 BBDown note 只是 `docs/research/**` research note，不是 authority 或 runtime approval
- `docs/specs/bbdown-adapter-contract-draft.md` 只允许作为 `draft / not final authority / not runtime approval`
- Phase 2-4 当前只作参考 outline

## 阅读顺序

1. `AGENTS.md`
2. `docs/current.md`
3. `docs/task-index.md`
4. `docs/specs/contracts-index.md`
5. `docs/SRD-v1.1-amendment-2026-05-03.md`

## 仓库边界

- `data/` 不进 git
- `referencerepo/` 不进 git
- 不建立 `candidates/`、`dispatches/`、`audits/` 顶层目录

## GitHub 外部审计工作流

ScoutFlow 当前把 GitHub 记录作为跨工具审计真源：

1. `Codex Desktop` / `Claude Code` / `Hermes Agent` / `OpenClaw` 等工具按任务边界交付变更。
2. 执行工具 push 到 GitHub，保留 commit / PR / workflow run。
3. user 贴 `commit hash + run id + 回写摘要`；无 CI run 时写 `run id: none`。
4. 网页版 `GPT Pro` 直接从 GitHub 的 commit / PR diff / workflow run 审计。
5. 审计意见回到任务账本和当前状态文档，不以聊天摘要替代仓库事实。

任务状态以 `docs/current.md` 与 `docs/task-index.md` 为准；并行执行协议见 `docs/specs/parallel-execution-protocol.md`。

## 当前范围

- 当前无 active product task；`T-P1A-009` 已完成并收口为 report-only runtime spike merged
- `T-P1A-008` 仅表示 fixture-only parser / classifier baseline merged，不批准 broader BBDown runtime、媒体下载、ffmpeg、ASR、workers 或 frontend；`T-P1A-009` 也不构成正式 adapter runtime approval
- GitHub queue / sync smoke / Codex adapter 只作为通信测试，当前已暂停或关闭
- 当前已批准 `T-P1A-001` / `T-P1A-002` / `T-P1A-004` 的 API-side 和安全 baseline；PR `#10` / `#14` / `#15` 合入的 research / draft spec 也不等于批准 broader Phase 1A runtime
