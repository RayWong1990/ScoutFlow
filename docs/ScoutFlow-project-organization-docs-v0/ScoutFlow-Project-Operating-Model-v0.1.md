# ScoutFlow 项目组织管理方式 v0.1

> 文档定位：ScoutFlow 的项目组织、技术栈、目录结构、协作机制、Phase 推进与前端设计路线。  
> 适用对象：user / Codex / Opus / Claude Design / ChatGPT Pro / Hermes / OpenClaw。  
> 当前裁决：**C-prime：Balanced Contract Platform**。长期按 C 的平台化组织模型走，短期按 A 的 Python Core 交付重心跑 Phase 1A。

---

## 0. 一句话结论

ScoutFlow 不应该选纯 A、纯 B 或纯 C，而应该采用：

```text
C-prime = Balanced Platform 的组织结构
        + Python Core 的交付收口
        + shared-contracts 的薄生成层
        + docs/tools/CI 的轻治理约束
```

更直白地说：

```text
长期组织：C，避免前端、后端、worker、docs 各自漂移。
短期推进：A，先把 B 站单条 URL → Library 可检索闭环做出来。
坚决不选：B，Product Web First 前期 UI 快，但很容易把 source adapter、worker contract、FS layout、state words 打散。
```

C 的问题是慢。解决办法不是退回 A，而是把 C 的平台化压缩成 **Phase 0 的薄骨架**：git、目录、AGENTS、OpenAPI、migration、lint、FS checker、API stub、Console mock。不要在 Phase 0 做完整平台、完整 Signal Workbench、完整多 agent UI。

---

## 1. 三个方案的裁决

| 方案 | 优点 | 风险 | 裁决 |
|---|---|---|---|
| A. Python Core + Thin Web | 最贴 ScoutFlow 的真实闭环；采集、ASR、worker、FS layout、state words 都由 Python 后端收口 | 前端容易只是控制面，产品体验可能弱 | **作为 Phase 1A 交付重心采用** |
| B. Product Web First | UI 迭代最快；Claude Design / Claude Code 交互顺 | 后端、worker、source adapter、contracts 容易被前端节奏带漂；前期像 SaaS 仓 | **不建议作为主路线** |
| C. Balanced Platform | 最符合长期多 agent 并行、contract-first、docs/tools/CI 的项目组织 | 最稳也最慢，容易 Phase 0 就平台化过重 | **采用 C-prime：薄平台骨架 + 垂直切片交付** |

### 推荐路线

```text
Phase 0: C 的骨架，但只做薄骨架
Phase 1A: A 的执行重心，B 站单条真实闭环
Phase 1B: RAW Link stub
Phase 2: C 的 Signal Workbench / Capture Plan / Scope Gate 完整启用
Phase 3+: Hermes / 推荐 / 多 agent UI
```

---

## 2. 项目组织原则

### 2.1 强 contract，轻治理

ScoutFlow 的稳定性不靠厚重治理目录，而靠工程契约：

```text
SQLite schema
FS artifact layout
state words / lifecycle
OpenAPI / API route contract
worker write-zone rules
lint / tests / CI
```

治理文件只保留必要入口：

```text
README.md
AGENTS.md
CLAUDE.md
docs/project-context.md
docs/current.md
docs/decision-log.md
docs/specs/*
docs/research/*
```

暂不在项目根建立：

```text
candidates/
dispatches/
audits/
amendments/
stage-ledger/
```

这些目录只有在真实出现 3+ agent 高频并发、PR/branch/current.md 不够时再加，并且优先加在 `docs/` 下，保持薄、可 lint。

### 2.2 LP 与 D-lock 分开

`decision-log.md` 是历史决策档案，应该薄。

LP（Locked Principles）是工程行为约束，不能只写在文档里。能工具化的必须工具化。

```text
D-lock = 决策历史
LP     = 工程约束
```

示例：

```text
LP-001 Capture Scope Gate
  -> API middleware/test enforce

LP-002 Plan estimate -> approve -> run
  -> API state transition guard/test enforce

LP-005 命名禁区
  -> tools/check-banned-words enforce
```

### 2.3 垂直切片，不铺大网

不要先把 76 个 API、20+ 表、9 页面、所有 worker、Signal Workbench、Topic Card 全部铺开。

交付节奏必须是：

```text
每个 Phase 都有可运行闭环
每个闭环都能被测试
每个测试都能约束下一个 agent
```

---

## 3. 仓库形态：true monorepo / dual-core / thin shared-contracts

### 3.1 推荐目录

```text
ScoutFlow/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── DESIGN.md                         # 设计系统 / Claude Design 使用规则，Phase 0 可先薄版
├── package.json
├── pnpm-workspace.yaml
├── pyproject.toml
├── uv.lock                           # 如果采用 uv
├── Makefile                          # 或 justfile，统一命令入口
├── .env.example
├── .gitignore
│
├── .github/
│   ├── workflows/
│   │   ├── lint-test.yml
│   │   └── contract-check.yml
│   └── pull_request_template.md
│
├── docs/
│   ├── project-context.md            # agent 10 分钟读懂项目
│   ├── current.md                    # 当前 Phase / 本周可改 / 禁止改 / 最新验证
│   ├── decision-log.md               # 薄版 D-lock 历史，不写成治理巨册
│   ├── product-design.md             # UI/UX 方向、信息架构、设计原则
│   ├── specs/
│   │   ├── architecture.md
│   │   ├── fs-layout.md
│   │   ├── locked-principles.md
│   │   ├── schema-v1.1.md
│   │   ├── api-routes-v1.1.md
│   │   ├── worker-contract.md
│   │   ├── signal-workbench-ui.md
│   │   └── capture-plan-estimator.md
│   ├── research/
│   │   ├── reference-repo-index.md
│   │   └── 2026-05-03-scoutflow-reference-repo-probe.md
│   └── archive/
│
├── apps/
│   └── console/
│       ├── src/
│       │   ├── app/
│       │   ├── pages/
│       │   ├── components/
│       │   ├── features/
│       │   ├── lib/
│       │   ├── styles/
│       │   └── routes/
│       ├── public/
│       ├── vite.config.ts
│       ├── tsconfig.json
│       └── package.json
│
├── services/
│   └── api/
│       ├── scoutflow_api/
│       │   ├── main.py
│       │   ├── routes/
│       │   ├── middleware/
│       │   │   └── scope_gate.py
│       │   ├── schemas/
│       │   ├── models/
│       │   ├── db/
│       │   ├── services/
│       │   │   ├── state_guard.py
│       │   │   ├── artifact_registry.py
│       │   │   └── job_receipts.py
│       │   └── settings.py
│       ├── migrations/               # 重要：migration 脚本进 git，不放 gitignored data/
│       │   ├── 001_init.sql
│       │   ├── 002_artifact_assets.sql
│       │   └── ...
│       └── tests/
│
├── workers/
│   ├── common/
│   ├── bili/
│   ├── media/
│   ├── asr/
│   ├── asr_postprocess/
│   ├── normalize/
│   ├── index/
│   ├── raw_linker/
│   ├── plan_estimator/
│   ├── recommender/
│   └── reranker/
│
├── packages/
│   └── shared-contracts/
│       ├── openapi/
│       │   └── scoutflow.v1.1.yaml
│       ├── generated/
│       │   ├── ts/
│       │   └── py/
│       └── package.json
│
├── tools/
│   ├── check-banned-words
│   ├── check-fs-layout
│   ├── lint-docs
│   ├── lint-contracts
│   ├── check-worker-zones
│   ├── seed-demo-capture
│   └── generate-openapi
│
├── tests/
│   ├── integration/
│   ├── fixtures/
│   └── e2e/
│
├── data/                              # runtime truth，整目录 gitignored
│   ├── db/
│   ├── artifacts/
│   ├── exports/
│   ├── tmp/
│   ├── logs/
│   └── backups/
│
└── referencerepo/                     # 本地参考仓，只读，gitignored
```

### 3.2 migration 路径修正

Base PRD 里曾把 migrations 放到 `data/db/migrations/`。这在运行层面能理解，但工程上有风险：`data/` 应该整体 gitignore，migration 脚本如果放进去会随运行数据一起失去版本控制。

因此执行目录建议改为：

```text
services/api/migrations/*.sql     # migration 脚本，进 git

data/db/scoutflow.sqlite          # 运行时 DB，不进 git
migrations table                  # DB 内记录已应用 migration
```

这不是推翻 PRD 的 schema 方向，而是把 migration 从 runtime data 移到 source-controlled code surface。

### 3.3 shared-contracts 必须薄

`packages/shared-contracts/` 只做生成层，不放业务逻辑。

允许：

```text
OpenAPI snapshot
TS generated API types
Python generated schema snapshot
contract test fixtures
```

不允许：

```text
推荐排序业务逻辑
worker 状态机实现
前端组件库
设计系统大包
数据库访问代码
```

共享契约的目标是防止前后端漂移，不是再造一个第三核心。

---

## 4. 四层架构与 dual-core

### 4.1 Authority-first 四层

```text
L3 Console       React/Vite 产品投影层，只调用 API
L2 Thin API      FastAPI 契约执行层：validation / idempotency / state transition / receipt
L1 Workers       Python stateless workers，业务处理与外部工具调用
L0 Authority     SQLite + FS artifact layout + state words
```

Console 不直接写 DB / FS。Worker 不直连 DB。API 不承载重业务逻辑，但必须承载 contract enforcement。

### 4.2 dual-core 的定义

ScoutFlow 是 dual-core，但不是双真源。

```text
Python Core：
  API / schema / migrations / workers / job queue / artifact registry / state guard

Product Web Core：
  Console / 9 页面 / Signal Workbench / Library / Pipeline / Knowledge Bridge

Contract Bridge：
  OpenAPI snapshot + generated TS client + contract tests
```

双核之间通过 API contract 汇合：

```text
FastAPI Pydantic schemas
  -> generated OpenAPI
    -> packages/shared-contracts/generated/ts
      -> Console typed API client
```

---

## 5. 技术栈

### 5.1 前端

| 层 | 选择 | 说明 |
|---|---|---|
| Framework | React 19 | 成熟、生态稳定，适合高密度 Console |
| Build | Vite | 快速开发和构建 |
| Language | TypeScript | 前端 contract 安全 |
| Router | TanStack Router | 类型安全路由 |
| Server state | TanStack Query | API 数据缓存、错误、重试管理 |
| Local state | Zustand | 简单 UI 状态，避免过早复杂化 |
| UI | Tailwind CSS + shadcn/ui | 可定制、适合深色高密度工具台 |
| Base primitives | Radix UI | 通过 shadcn 间接使用 |
| Icons | lucide-react | 简洁一致 |
| Pipeline | React Flow | Capture Pipeline / Plan progress 可视化 |
| Charts | Recharts | Mission Control 统计和预算图 |
| Media | wavesurfer.js + video.js | Transcript Studio 后置启用 |
| Markdown | react-markdown + remark-gfm | normalized.md / RAW patch preview |
| Test | Vitest + Testing Library；Playwright 后置 | Phase 0/1A 先轻测试 |

### 5.2 设计与原型

| 工具 | 用法 | 边界 |
|---|---|---|
| Claude Design | 做视觉方向探索、交互原型、Signal Workbench 高保真 mock、演示 deck | 不直接把生成代码合入主仓 |
| Claude / Opus | IA、产品叙事、设计 critique、UI copy | 不直接绕过 contract 改代码 |
| Claude Code / Codex | 按已定 contract 实现 React/FastAPI/workers | 不单方面改 LP / FS layout / schema lock |
| Figma | 可选；当 Claude Design 输出需要人工精修时用 | Phase 0 不强依赖 |
| Canva / PPTX | 用于对外展示或回顾，不作为产品真源 | 不进入工程主路径 |

### 5.3 后端

| 层 | 选择 | 说明 |
|---|---|---|
| Language | Python 3.12 | ASR / LLM / subprocess / worker 生态统一 |
| Package manager | uv | 推荐；也可 Poetry，但 uv 更轻更快 |
| Web | FastAPI | 自动 OpenAPI，配 Pydantic v2 |
| Validation | Pydantic v2 | API contract 和 settings |
| DB access | SQLAlchemy Core 或轻 ORM | schema 以 SQL migration 为准，ORM 不做权威 |
| Migration | repo-tracked SQL migrations | `services/api/migrations/*.sql` |
| Queue | SQLite-backed queue | Phase 1A 不上 Redis / Celery |
| Scheduler | APScheduler 或自建 tick loop | Hermes 前先简单实现 |
| Test | pytest + pytest-asyncio | API / state transition / worker unit |
| Lint | ruff | Python 格式 + lint |

### 5.4 数据与文件

| 层 | 选择 | 说明 |
|---|---|---|
| DB | SQLite + WAL | 本地优先，Phase 1A/1B 足够 |
| Full-text | SQLite FTS5 | Library 初期检索足够 |
| Vector | 后置：Qdrant / Chroma / sqlite-vec 评估 | Phase 1A 不上 |
| Large artifacts | APFS 本地文件系统 | `data/artifacts/<platform>/<capture_id>/...` |
| Backups | SQLite copy + rsync artifacts | Phase 1 后加 |

### 5.5 Workers / 外部工具

| Worker | 栈 | 说明 |
|---|---|---|
| bili | BBDown + Python wrapper | Phase 1A 主入口 |
| media | ffmpeg | audio extract / waveform 后置 |
| ASR | faster-whisper | 默认 |
| ASR advanced | WhisperX | diarization / word alignment 后置 |
| normalize | Claude / OpenAI 路由 | Phase 1A 只做基础 summary / structured.md |
| raw_linker | LLM + RAW scanner | Phase 1B |
| xhs | xhs-research / ReaJason/xhs | Phase 2 metadata 起 |
| youtube | yt-dlp | Phase 2+，不抢 Phase 1A |

### 5.6 当前不建议上的东西

```text
Docker / Kubernetes
Redis / Celery
外部搜索服务
Tauri / Electron 真 WebView
完整向量库
完整 Agent Dispatch UI
完整候选/审计行政目录
前端组件库抽包
```

这些不是永远不做，而是不要阻塞 Phase 1A。

---

## 6. 前端设计路线：Claude Design 适合做原型，不适合做真源

### 6.1 Claude Design 的位置

Claude Design 应该被当作：

```text
设计探索器
高保真原型器
产品方向比较器
交互演示生成器
```

不应该被当作：

```text
生产代码生成器
前端架构真源
组件库真源
API contract 真源
```

### 6.2 推荐设计流程

```text
Step 1: Claude Design 生成 3 个视觉方向
        A. Dense Console / Linear-like
        B. Evidence Lab / dark research workstation
        C. Mission Control / spatial dashboard

Step 2: user + Opus 选择方向，形成 DESIGN.md

Step 3: Claude Design 输出 Signal Workbench / Capture Pipeline / Library 三个高保真页面

Step 4: Codex 按 React/Vite/shadcn 实现，不直接复制 Claude Design 生成代码

Step 5: 将可复用组件沉淀到 apps/console/src/components，不急着抽 packages/ui

Step 6: tools/lint-ui-redlines 检查不允许出现违反 LP 的按钮或文案
```

### 6.3 ScoutFlow UI 风格建议

ScoutFlow 不要做成下载器，也不要做成通用 SaaS 后台。更合适的视觉语言：

```text
高密度研究工作站
暗色优先
证据感 / 日志感 / 时间线感
状态明确
卡片 + 三栏工作区
少营销，多操作
```

参考气质：

```text
Linear 的清晰度
Raycast 的命令感
Karakeep 的卡片收藏感
ArchiveBox 的 evidence/durability 感
ComfyUI / React Flow 的 pipeline 可视化感
```

### 6.4 设计系统最小集

Phase 0 不需要完整 Design System，但需要最小 token：

```text
status colors:
  observed / opened / hypothesized / plan_ready / capturing / evidence_locked / failed

artifact zones:
  bundle / media / transcript / normalized / links / logs

priority:
  low / medium / high / blocked

typography:
  UI sans + code mono + transcript readable text

layout:
  shell / left nav / command bar / right drawer / 3-column workbench
```

### 6.5 Phase 0 必做的 UI 红线

UI 层不能诱导违反 LP：

```text
Source/Signal Radar 默认不出现 [采集] 按钮
推荐流默认动作是 [打开 Scope] / [验证信号]
Evidence Browser Phase 1 不真内嵌平台登录页
quick_capture 只在 manual_url 且满足条件时出现
RAW 不出现 [自动合并]，只出现 [写入 RAW inbox]
```

---

## 7. Phase 推进

### Phase 0：薄平台骨架

目标：把 C 的平台结构打薄落地，不做真实采集。

交付：

```text
git init + private GitHub 或本地 commit checkpoint
README.md / AGENTS.md / CLAUDE.md / DESIGN.md
docs/project-context.md / current.md / decision-log.md
repo skeleton
FastAPI healthz / readyz
OpenAPI generation stub
React Console 9 页面 mock
SQLite migration runner + 001_init.sql 最小版
FS layout sample + tools/check-fs-layout
tools/check-banned-words
tools/lint-docs
tools/lint-contracts
```

验收：

```bash
pnpm --filter console build
uv run pytest
uv run ruff check .
python tools/check-fs-layout
python tools/check-banned-words
python tools/lint-docs
python tools/lint-contracts
```

### Phase 1A：B 站单条 URL → Library

目标：只证明一条 B 站 URL 能稳定进入本地文案库并被检索。

链路：

```text
Explore 粘贴 B 站 URL
→ quick_capture
→ metadata
→ audio
→ ASR
→ segments
→ normalize
→ FTS index
→ Library 可搜索
```

必做 enforcement：

```text
LP-001 API 层从 Phase 1A 就开始 enforce
/captures/discover 只允许 manual_url quick_capture
recommendation / keyword / RAW gap 一律 422 或 open_scope placeholder
```

### Phase 1B：RAW Link stub

目标：indexed capture 能生成 RAW patch suggestion，但不自动合并。

链路：

```text
indexed capture
→ raw_linker
→ links/raw-suggestions.jsonl
→ Knowledge Bridge 展示
→ user accept
→ 写入 RAW inbox
```

### Phase 2：Signal Workbench / Capture Plan / XHS metadata

目标：启用 v1.1 的前置判断系统。

交付：

```text
signals / hypotheses / capture_plans / topic_cards
Signal Workbench 三栏 UI
Scope Builder
plan_estimator
browsing_sessions / browsing_events
XHS metadata + note text
Reverse Discovery
```

### Phase 3：主动推荐 / Hermes

目标：让系统主动发现信号，但不直接采集。

交付：

```text
Hermes source scan
recommender
reranker
Source/Signal Radar
open_scope / verify_signal 默认动作
```

### Phase 4：多 agent 治理 UI

目标：当真实协作压力出现后，再把 Agent Dispatch UI 做出来。

前置条件：

```text
已经有多个 agent 高频并发
PR/handoff/current.md 不够
真实出现漂移或冲突
```

---

## 8. Locked Principles enforce 路径

| LP | 原则 | enforce 方式 | 文件/测试 |
|---|---|---|---|
| LP-001 | Capture Scope Gate | API 拒绝非 manual_url quick_capture；推荐/关键词/RAW gap 不直接 discover | `services/api/middleware/scope_gate.py` / `tests/api/test_lp001_scope_gate.py` |
| LP-002 | Plan estimate → approve → run | API state transition guard；未 estimated / approved 不允许 run | `services/api/services/state_guard.py` / `tests/api/test_lp002_plan_state.py` |
| LP-003 | merger-of-record | AGENTS + PR template + branch discipline | `.github/pull_request_template.md` / `AGENTS.md` |
| LP-004 | Evidence Browser 不真嵌 | AGENTS 红线 + UI redline lint；Phase 1 不允许 WebView/iframe 登录 | `tools/check-ui-redlines` / `docs/product-design.md` |
| LP-005 | 命名禁区 | banned words lint | `tools/check-banned-words` |

### LP-001 Phase 1A 最小实现

```python
# services/api/routes/captures.py
@router.post('/captures/discover')
def discover(payload: DiscoverCapturePayload):
    if payload.source_kind != 'manual_url':
        raise HTTPException(
            status_code=422,
            detail=(
                'LP-001: Phase 1A only allows manual_url quick_capture. '
                'Recommendation, keyword, RAW gap, and agent-originated inputs must use capture_plan in Phase 2.'
            ),
        )
    # continue quick_capture validation
```

---

## 9. 多 agent 协作方式

### 9.1 角色分工

| Agent | 主责 | 不应该做 |
|---|---|---|
| user | showrunner / final arbiter | 不需要审每个 worker 细节，但要拍板 lock 项 |
| Codex | API / schema / migration / workers / tests / CI / contract lint | 不单方面改产品叙事、IA、LP |
| Opus | PRD / IA / UX / 架构纠偏 / design critique | 不绕过 Codex 改代码主路径 |
| Claude Design | 原型 / 视觉探索 / 高保真 mock / handoff bundle | 不作为生产代码真源 |
| ChatGPT Pro | research / 参考仓分析 / 方案比较 / prompt 草案 | 不直接进主线代码 |
| Hermes | source scan / signal generator / scheduler | Phase 1A 不抢跑推荐采集 |
| OpenClaw | secondary scout / executor | 不直写 authority |

### 9.2 merger-of-record

| 变更类型 | merger-of-record | 是否 user 拍板 |
|---|---|---|
| API / worker / tests / CI | Codex | 否，除非触碰 lock |
| schema / state words / FS layout | Codex + Opus 双审 | 是 |
| PRD / IA / 产品叙事 | Opus draft + Codex sanity check | 是 |
| migration | Codex | 涉及 lock 时是 |
| LP / 安全边界 | Codex + Opus 双审 | 是 |
| UI 高保真方向 | Opus + user | 是 |
| 前端实现 | Codex | 否，除非违背 UI 红线 |

### 9.3 PR / handoff 必填

每个 agent 输出或 PR 必须包含：

```markdown
## 1. 改了什么

## 2. 触碰了哪些 contract
- [ ] SQLite schema
- [ ] FS layout
- [ ] state words
- [ ] OpenAPI
- [ ] worker write-zone
- [ ] LP / safety boundary

## 3. 是否需要 migration

## 4. 如何验证

## 5. 风险是什么

## 6. 触碰了哪个其他 worker 的写区
- 没有 / 有：...
- 如有，是否需要 cross-zone audit：是 / 否

## 7. introduced vs exposed
- 本次变更引入的问题：...
- 本次变更暴露的历史债：...
```

`introduced vs exposed` 是故障复盘默认模板，避免把历史债全部归因到最近 PR。

---

## 10. Worker 写区边界

| Worker | 允许写 | 禁止写 |
|---|---|---|
| bili metadata | `bundle/` | `media/`, `transcript/`, `normalized/`, `links/` |
| media | `media/` | `transcript/`, `normalized/`, `links/` |
| asr | `transcript/raw.json` | `normalized/`, `links/` |
| asr_postprocess | `transcript/segments.jsonl`, `media/derived/` | `normalized/`, `links/` |
| normalize | `normalized/` | `transcript/`, `links/` |
| index | DB FTS/index tables | FS |
| raw_linker | `links/` | `normalized/`, RAW 主仓 |
| plan_estimator | `capture_plans.estimate_json` | artifacts |
| recommender | `recommendations`, `signals` | captures / artifacts |
| reranker | `recommendations` score/reason | captures / artifacts |

Console 永远不直接写 DB / FS。Worker 永远不直连 DB。RAW 永远不被自动修改，只写 RAW inbox。

---

## 11. Git 与分支策略

### 11.1 Phase 0 第一件事：git init

必须先 git init。

最低要求：

```bash
git init
git add README.md AGENTS.md CLAUDE.md docs/ .gitignore .env.example
git commit -m "Phase 0 skeleton: docs + LP + gitignore"
```

推荐：GitHub 私库。

如果暂时不想上 GitHub PR 流，至少使用本地 commit checkpoint，不要裸跑。

### 11.2 分支建议

```text
main                         永远可运行
phase/0-skeleton             Phase 0 主分支
feat/api-healthz             小功能分支
feat/console-mock            小功能分支
feat/lp001-scope-gate        小功能分支
```

### 11.3 commit 原则

```text
一个 commit 只解决一个问题
schema/migration 单独 commit
UI mock 单独 commit
worker 单独 commit
LP enforcement 单独 commit
```

---

## 12. CI / lint / test 最小集

Phase 0 就应有：

```text
ruff check
pytest
pnpm typecheck
pnpm build
tools/check-banned-words
tools/check-fs-layout
tools/lint-docs
tools/lint-contracts
```

Phase 1A 加：

```text
test_lp001_scope_gate
test_job_state_transition
test_worker_write_zones
test_artifact_registry
test_bili_quick_capture_fixture
test_library_fts_fixture
```

Phase 2 加：

```text
test_plan_estimate_approve_run
test_signal_lifecycle
test_browsing_events
test_ui_no_direct_capture_from_recommendation
```

---

## 13. reference repo 使用规则

`referencerepo/` 保持只读、本地存在、gitignored。

```text
referencerepo/ 不能被产品代码 import
referencerepo/ 不能作为 runtime dependency
referencerepo/ 只能作为研究参考
```

必须维护：

```text
docs/research/reference-repo-index.md
```

每个参考仓写清楚：

```text
仓库名
本地路径
借什么
不借什么
最后检查日期
```

---

## 14. decision-log.md 薄版规则

`docs/decision-log.md` 只记录已经拍板的关键决策，不写成长篇 PRD。

示例：

```markdown
# Decision Log

## 2026-05-02 — FS layout locked
- Decision: artifacts/<platform>/<capture_id>/{bundle,media,transcript,normalized,links,logs}
- Impact: all workers, API artifact registry, backup
- Source: PRD v1 §5

## 2026-05-02 — Capture Scope Gate adopted
- Decision: recommendation / keyword / RAW gap cannot directly create captures
- Impact: Source Radar, API /captures/discover, plan_estimator, workers
- Source: PRD v1.1 amendment LP-001
```

LP 不只放在 decision-log；LP 需要放在 `AGENTS.md` 顶部并连接到 enforce 路径。

---

## 15. 立即下一步

推荐从这个 commit 开始：

```text
Commit 1: Phase 0 skeleton: docs + LP + gitignore

包含：
- git init
- README.md
- AGENTS.md
- CLAUDE.md
- DESIGN.md
- docs/project-context.md
- docs/current.md
- docs/decision-log.md
- docs/specs/locked-principles.md
- docs/research/reference-repo-index.md
- .gitignore
- .env.example
```

然后再开：

```text
Commit 2: Phase 0 repo skeleton: apps + services + workers + packages
Commit 3: API healthz/readyz + migration runner stub
Commit 4: Console 9-page mock shell
Commit 5: LP-001 scope gate test + implementation
Commit 6: FS layout checker + demo capture fixture
```

---

## 16. 最终裁决

ScoutFlow 应该走：

```text
C-prime Balanced Contract Platform
```

它不是纯 A，因为长期多 agent、Signal Workbench、Capture Plan、worker contract 会让纯 Python Core 变成后端独裁，前端体验与 contract 可能脱节。

它不是纯 B，因为 Product Web First 会让漂亮 UI 先行，最危险的 source adapter / capture scope / FS layout / state guard 反而被拖成后端补丁。

它是 C 的长期形态，但必须用 A 的交付纪律压住节奏：

```text
先 git
再 contract
再 thin mock
再 B 站单条闭环
再 RAW stub
再 Signal Workbench
再推荐与多 agent UI
```
