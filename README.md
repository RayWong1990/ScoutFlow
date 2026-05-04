# ScoutFlow
ScoutFlow 是个人本地研究工作流的 `Authority-first` 内容采集、转写、规整与证据账本项目。
## 当前入口
- 当前 Phase / task / gate：`docs/current.md`
- 任务账本：`docs/task-index.md`
- Agent 边界：`AGENTS.md`；Claude sidecar 差异：`CLAUDE.md`
- Contract 总索引：`docs/specs/contracts-index.md`；硬原则：`docs/specs/locked-principles.md`
## 阅读顺序
1. `docs/current.md`
2. `AGENTS.md`
3. `docs/task-index.md`
4. `docs/specs/contracts-index.md`
5. `docs/specs/parallel-execution-protocol.md`
## 当前不做
- 不写 `workers/`、`apps/`、`packages/`、`services/**` 新 runtime
- 不碰 `data/`、`referencerepo/`、凭据、raw cookie/token
- 不自动执行 BBDown / yt-dlp / ffmpeg / ASR / browser automation
- 不启用 `audio_transcript` runtime
- 不把 research note / draft spec 当 final authority
- 不启动 Phase 2-4 runtime
任务状态以 `docs/current.md` 与 `docs/task-index.md` 为准；跨工具审计以 GitHub PR diff / workflow run 为事实源。
