# ScoutFlow
ScoutFlow 是个人本地研究工作流的 `Authority-first` 内容采集、转写、规整与证据账本项目。

## 当前入口

- 🚀 **新 agent / 新 session 起点**：`docs/00-START-HERE.md` (含 5 级阅读 ladder)
- 当前 Phase / task / gate：`docs/current.md` (顶部 5 行 TL;DR)
- 任务账本：`docs/task-index.md`
- 决策日志：`docs/decision-log.md`
- Agent 边界：`AGENTS.md`；Claude sidecar 差异：`CLAUDE.md`

## 路线图 / 战略层 (PR #243 baseline 后)

- 采集线 north-star roadmap：`docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` (candidate north-star, 11 wave + 4-agent v3 + 现在没做的全部 inventory)
- 16 ZIP 储能层 (~1.48M 字 / 895 file, grep-able reference storage)：`docs/research/strategic-upgrade/2026-05-07/audit/PHASE-A-B-SUMMARY.md`
- 历史 doc1/doc2/doc3 (2026-05-04 三件套)：见 `docs/00-START-HERE.md` §5

## PRD / SRD baseline

- PRD canonical：`docs/PRD-v2-2026-05-04.md` + `docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md` (promoted addendum)
- SRD canonical：`docs/SRD-v2-2026-05-04.md` + `docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md` (promoted addendum)
- Contract 总索引：`docs/specs/contracts-index.md`；硬原则：`docs/specs/locked-principles.md`
- 架构记录：`docs/architecture/**` (含 doc1 / doc2, candidate baseline; not authority)

## 阅读顺序 (扁平化)

1. `docs/00-START-HERE.md` (5 min cold start)
2. `docs/current.md` TL;DR (1 min)
3. 视任务跳 master spec / PRD / SRD / specs / 储能层 U[1-16]
## 当前不做
- 不写 `workers/`、`apps/`、`packages/`、`services/**` 新 runtime
- 不碰 `data/`、`referencerepo/`、凭据、raw cookie/token
- 不自动执行 BBDown / yt-dlp / ffmpeg / ASR / browser automation
- 不启用 `audio_transcript` runtime
- 不把 research note / draft spec 当 final authority
- 不启动 Phase 2-4 runtime
任务状态以 `docs/current.md` 与 `docs/task-index.md` 为准；跨工具审计以 GitHub PR diff / workflow run 为事实源。
