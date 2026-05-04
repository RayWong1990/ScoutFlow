---
type: shoulder-scan-report
stage: stage-2-scan
task_id: T-P1A-039
pr_number: PR #64
title: ScoutFlow Console Reference Scan - OpenWhispr + shadcn
date: 2026-05-05 Asia/Shanghai
authority_status: research-only / not-authority / not-runtime-approval / not-frontend-implementation-approval
scope: console-reference only; no frontend implementation approval; no repo-local clone tracking
verdict: "Vite browser H5 path stays favored; router remains deferred; OpenWhispr is a stack signal rather than an app shell donor; satnaing/shadcn-admin is the strongest single clone candidate for Wave 3B local-only reference."
---

# ScoutFlow Console Reference Scan - OpenWhispr + shadcn

> 本文档是 `T-P1A-039 / PR #64` 的 stage-2 console reference scan。
> 结论只服务 `reference_only / prototype input`，不构成前端代码批准，不构成 runtime 批准，不回写 `docs/shoulders-index.md`。

## 0. 总结论

这波 scan 的核心不是“挑一个现成后台模板直接上”，而是把三类信号拆开：

1. `OpenWhispr/openwhispr` 证明了一套现代桌面 AI 工具常用的前端栈组合确实成立：`React 19 + Tailwind v4 + shadcn/ui + better-sqlite3 + Zustand`。
2. `Kiranism/*` 与 `satnaing/shadcn-admin` 证明了浏览器 H5 端也可以稳定承载 `shadcn + TanStack + Zustand + Recharts/Lucide` 这类组合。
3. ScoutFlow 自己的目标不是桌面 dictation app，也不是 SaaS admin panel，所以要明确切断三条错误继承：
   - `no SSR requirement`
   - `no Electron`
   - `no admin-dashboard template lock-in`

本次 scan 后的建议是：

- `Build/UI/Data/State/Style/Icon` 方向可以继续沿 `Vite + shadcn + TanStack Query + Zustand + Tailwind v4 + Lucide` 收敛。
- 路由先不要锁；必须明确 `不预锁 React Router 6`。当前更像是 `TanStack Router` 略占优，但要把最终决定延后到 `PR72 prototype` 之后。
- `satnaing/shadcn-admin` 是最适合做 Wave 3B local-only clone 的单一参考；`Kiranism/tanstack-start-dashboard` 保留为第二参考，用于路由 / form / query 组合比对。

## 1. Scan 目标与 ScoutFlow H5 限制

### 1.1 本次 scan 要回答的问题

- ScoutFlow 的 H5 capture station 是否继续坚持浏览器单页路线，而不是 Next.js / Electron 双壳路线。
- `shadcn` 生态里哪些 repo 适合作为“组件借鉴源”，哪些只是“模板视觉参考”。
- `OpenWhispr` 这类成熟 AI 桌面工具能提供哪些工程信号，哪些信号不能直接搬进 ScoutFlow。
- 在不批准任何前端代码的前提下，Wave 3B prototype 该用什么最小技术组合。

### 1.2 约束先锁死

| 约束 | 本次结论 | 含义 |
|---|---|---|
| `no SSR requirement` | 保持成立 | ScoutFlow 当前目标是本机浏览器 H5 工作台，不需要先引入 SSR / RSC / server actions 假设 |
| `no Electron` | 保持成立 | 当前不做桌面壳，不引入原生热键、系统音频 tap、打包器、自动更新 |
| `no admin-dashboard template lock-in` | 保持成立 | 可以借控件、表单、表格、布局片段，但不能继承 sidebar-first 后台信息架构 |
| `不预锁 React Router 6` | 必须写明 | 路由仍是待验证项；不能因为某个 starter 用 React Router 6 或 TanStack Router 就提前定案 |

### 1.3 参考仓快照（live scan at 2026-05-05）

| Repo | 角色 | License | Stars | Updated (UTC) | 初判 |
|---|---|---:|---:|---|---|
| `OpenWhispr/openwhispr` | AI 桌面整栈参考 | MIT | 2867 | 2026-05-04 | stack signal 强，壳层不借 |
| `OpenWhispr/openwhispr-mcp` | OpenWhispr API/MCP 旁路 | none shown | 0 | 2026-04-18 | API/MCP 参考，可留存 |
| `Kiranism/next-shadcn-dashboard-starter` | Next.js admin starter | MIT | 6365 | 2026-05-04 | 组件 cookbook 强，框架假设过重 |
| `Kiranism/tanstack-start-dashboard` | TanStack Start + Vite dashboard | MIT | 544 | 2026-05-03 | 最接近目标栈，但仍带 Start/Nitro 假设 |
| `arhamkhnz/next-shadcn-admin-dashboard` | Next.js 16 admin dashboard | MIT | 2198 | 2026-05-04 | 主题系统有价值，整体过像后台模板 |
| `satnaing/shadcn-admin` | Vite + TanStack Router dashboard UI | MIT | 11928 | 2026-05-04 | 当前最佳单 clone 候选 |
| `SSV0726/next-shadcn-dashboard-starter` | Kiranism fork | MIT | 0 | 2025-03-31 | 明显落后，不建议继续 |

### 1.4 状态机（只针对本次 reference 决策）

```text
candidate_discovered
  -> stage2_scanning
  -> reference_candidate
  -> prototype_input
  -> implementation_candidate

Gate A: 不违反 no SSR requirement / no Electron / no admin-dashboard template lock-in
Gate B: 能抽出可复用模式，而不是只能整模板继承
Gate C: 不把 stage-2 扫描误写成实现批准
Gate D: prototype 跑完后才能升级 router / layout / shell 决策
```

## 2. 七个候选 verdict

### 2.1 `OpenWhispr/openwhispr` - 栈信号强，桌面壳不借

已看到的强信号：

- README 直接写出 `React 19 + Tailwind CSS v4 + Electron 41 + better-sqlite3 + shadcn/ui`。
- `package.json` 进一步确认 renderer 端是 `vite`，状态管理用 `zustand`，本地数据层用 `better-sqlite3`。
- 项目活跃，最近仍在更新，说明这套组合不是停留在 demo 阶段。

适合借的：

- React 19 / Tailwind v4 / shadcn/ui / Zustand / better-sqlite3 的并存经验。
- 本地优先桌面工具把“结构化本地数据 + UI 组件系统”串起来的方式。
- 把 AI 功能放在产品能力层，而不是把 UI 做成传统后台面板的做法。

不适合借的：

- Electron 壳、原生热键、系统音频 tap、模型下载器、跨平台打包链。
- dictation / meeting transcription 的产品结构。
- 任何对 `whisper.cpp`、`sherpa-onnx`、`ffmpeg` 的直接继承假设。

Stage-2 verdict：

- `decision`: continue
- `integration_mode_proposal`: `reference_only`
- `confidence`: `0.90`
- `blockers`: Electron/native 假设与当前 H5 范围不一致
- `next_action`: 保留为 stack signal；只在 Wave 4+ 再看 `better-sqlite3` 本地桥接价值

### 2.2 `OpenWhispr/openwhispr-mcp` - 有 API/MCP 参考价值，但不是 H5 UI 骨架

已看到的强信号：

- README 清楚给出远程 MCP server 形态、鉴权方式和工具列表。
- `package.json` 很轻：`@modelcontextprotocol/sdk + zod`，说明它是 API/MCP 薄层，不是 UI 项目。

适合借的：

- 远程 MCP 的工具边界写法。
- API key scope 最小化思路。
- 文档表达上“工具清单 + required scopes + example prompts”的结构。

不适合借的：

- 这不是前端控制台项目，对 `capture station` 布局、状态流、交互面板都没有帮助。
- 也不能反推 ScoutFlow 当前就应该做 MCP server。

Stage-2 verdict：

- `decision`: continue
- `integration_mode_proposal`: `reference_only`
- `confidence`: `0.62`
- `blockers`: 与当前 console H5 scan 的直接相关性有限
- `next_action`: 只在未来 bridge/API 文档里引用，不进入当前 H5 winner 列表

### 2.3 `Kiranism/next-shadcn-dashboard-starter` - 组件 cookbook 强，但 Next 假设过重

已看到的强信号：

- README 和 `package.json` 都很完整，`TanStack Query / TanStack Form / Zustand / Recharts / shadcn/ui` 组合成熟。
- 组件覆盖度高，表单、表格、命令面板、主题、布局都有现成例子。
- 项目非常活跃，维护面明显优于零星 fork。

适合借的：

- `shadcn` 组件组织方式。
- `TanStack Query` 与 UI 组件的结合方式。
- `TanStack Form + Zod` 的表单写法。
- 面板、dialog、table、toast、command palette 这些局部模式。

不适合借的：

- Next.js 16 / Clerk / Sentry / Nuqs / Docker / deploy 假设。
- `admin dashboard` 整体 IA：sidebar + auth-first + SaaS panel 逻辑。
- 把 Capture Station 做成现成后台模板的冲动。

Stage-2 verdict：

- `decision`: continue
- `integration_mode_proposal`: `reference_only`
- `confidence`: `0.82`
- `blockers`: `no SSR requirement` 与 `no admin-dashboard template lock-in`
- `next_action`: 作为组件 cookbook 留存，不作为 single winner clone

### 2.4 `Kiranism/tanstack-start-dashboard` - 最接近目标栈，但仍带 Start/Nitro 服务器假设

已看到的强信号：

- README 直接给出 `Vite 7 + TanStack Router + TanStack Query + TanStack Form + Zustand + Shadcn UI`。
- 这是本批次里最像“浏览器 H5 + 现代 React + type-safe router”组合的样本。
- 适合验证如果不用 Next.js，还能保留多少开发体验。

需要额外小心的点：

- README 自带 caution：当前版本仍在旧的 Vinxi 版本上，作者还在往 Vite 版本迁移。
- TanStack Start 仍不是“纯浏览器单页”，它带 `Nitro`、`createServerFn()`、部署 preset 这些服务端影子。
- 它证明 `TanStack Router` 很能打，但不等于 ScoutFlow 现在必须锁 TanStack Start。

Stage-2 verdict：

- `decision`: continue
- `integration_mode_proposal`: `reference_only`
- `confidence`: `0.85`
- `blockers`: Start/Nitro/server fn 假设超出当前需求
- `next_action`: 用作 router/query/form 组合对照样本；不要把它直接等同于最终 scaffold

### 2.5 `arhamkhnz/next-shadcn-admin-dashboard` - 主题系统可借，整体仍偏后台模板

已看到的强信号：

- README 强调主题预设、布局控制、多 dashboard 视图，说明视觉层打磨比较深。
- `package.json` 里 `react-hook-form + zustand + tanstack table + lucide-react` 这些常用件齐全。

适合借的：

- theme preset 思路。
- layout density 与视觉风格上的节制做法。
- colocation 的文件组织描述。

不适合借的：

- Next.js 16 App Router 假设。
- 多 dashboard / auth / RBAC / multi-tenant 这些后台产品前设。
- 它更像“可卖的 dashboard 模板”，不是“本机采集工作台”。

Stage-2 verdict：

- `decision`: continue
- `integration_mode_proposal`: `reference_only`
- `confidence`: `0.68`
- `blockers`: template 心智过强，容易把产品做偏
- `next_action`: 只借主题与 layout 控制度，不作为 clone 优先项

### 2.6 `satnaing/shadcn-admin` - 当前最强的 Vite browser donor

已看到的强信号：

- README 明确：`Admin Dashboard UI crafted with Shadcn and Vite`。
- README 与 `package.json` 一起确认：`Vite + TanStack Router + TanStack Query + React Hook Form + Zod + Lucide + Zustand`。
- 活跃度和社区规模在这批候选里很强，而且不是 Next.js 模板。

它为什么比 Kiranism/tanstack 更适合单 clone：

- 更接近“浏览器 UI 参考件”而不是“全栈启动器”。
- 没有 `Nitro` / `createServerFn()` / server deployment 负担。
- 适合作为 `layout primitives + ui components + router shell` 的 local-only donor。

它的不足也要写清：

- 作者自己说这不是 starter template，所以它更像 UI collection。
- 仍然是 dashboard IA，不能整体照搬 sidebar-first。
- 表单体系主要是 `React Hook Form`，不代表我们必须放弃 `TanStack Form`。

Stage-2 verdict：

- `decision`: continue
- `integration_mode_proposal`: `reference_only`
- `confidence`: `0.91`
- `blockers`: dashboard IA 仍需去模板化
- `next_action`: 作为 PR67 local-only clone 的首选 winner

### 2.7 `SSV0726/next-shadcn-dashboard-starter` - 低价值 fork，建议 drop

已看到的信号：

- README 明说它是 Kiranism 仓库的 fork，定位没有明显增量。
- `package.json` 停在 `Next 15`、`eslint-config-next 15.1.0`、较旧的一批依赖。
- GitHub 元数据显示几乎没有社区信号。

为什么不继续：

- 对 Kiranism 原仓没有形成明确差异化价值。
- 依赖更旧，维护信号更弱。
- 在同类仓已经有更强原版时，再研究这个 fork 性价比很低。

Stage-2 verdict：

- `decision`: drop
- `integration_mode_proposal`: `drop`
- `confidence`: `0.95`
- `blockers`: 无独特增量，版本落后
- `next_action`: 不进入 Wave 3B clone pool

## 3. Stack 决策表

> 这张表只定义 prototype 输入倾向，不是 authority lock。尤其是路由行，必须保持“延后 + 不预锁 React Router 6”。

| 组件 | 候选 1 | 候选 2 | 当前选择 | 理由 |
|---|---|---|---|---|
| Build | Vite 7 | Next.js 16 | `Vite 7` | 当前是本机浏览器 H5，`no SSR requirement`，不需要先背 App Router / SSR 包袱 |
| UI 组件 | shadcn (vendored) | Material UI | `shadcn (vendored)` | 与当前参考仓重合度最高，组件粒度更适合按需抽取 |
| 路由 | TanStack Router | React Router 6 | `延后到 PR72 prototype 后定；当前不预锁 React Router 6` | `TanStack Router` 样本更强，但没有足够理由现在就把 React Router 6 排除 |
| 状态 | Zustand | Redux Toolkit | `Zustand` | 本地单页工作台更需要轻量共享状态，而不是厚 action/reducer 仪式 |
| 数据 | TanStack Query | SWR | `TanStack Query` | 与候选仓重合更高，适合 panel-based async surface |
| 表单 | TanStack Form + Zod | React Hook Form + Zod | `TanStack Form + Zod` | 作为 greenfield 默认更一致；允许在借来的局部组件里继续看到 RHF |
| 图/流程 | React Flow | `xyflow` 命名变体 | `React Flow` | 目标里已有 Trust Trace / state map 场景；`xyflow` 本质仍是同一套库命名体系 |
| 样式 | Tailwind v4 | CSS Modules | `Tailwind v4` | 当前样本一致性最高，和 shadcn 组件系天然协同 |
| Icons | Lucide | Heroicons | `Lucide` | 参考仓覆盖率最高，和 shadcn / local tooling 的组合最自然 |

## 4. OpenWhispr 借鉴矩阵

| 面向 | 借 | 不借 | 原因 | 时间边界 |
|---|---|---|---|---|
| renderer 技术栈 | `React 19 + Tailwind v4 + shadcn/ui + Zustand` | Electron shell | 前者证明组合可行；后者直接违反 `no Electron` | 现在即可借前者 |
| 本地数据层 | `better-sqlite3` 使用经验 | 会议转写 / diarization / model download 管线 | ScoutFlow 当前只需要本地 bridge/vault 方向信号，不要把音频 runtime 带进来 | `Wave 4+` 再议 |
| AI 工具扩展 | API/MCP 暴露方式 | 以 dictation 为中心的产品结构 | 对“可编排能力出口”有参考，但不适合当前 H5 IA | 研究保留 |
| UI 组织 | 功能模块化与现代组件系 | 原生热键、系统监听、自动更新 | H5 不需要桌面壳运维面 | 当前不借 |
| 产品心智 | AI 能力嵌入真实工具流 | “桌面助手”作为产品主叙事 | ScoutFlow 是采集/整编工作台，不是 dictation assistant | 当前不借 |

一句话结论：

`OpenWhispr` 对 ScoutFlow 的价值主要是“证明现代本地 AI 工具栈成立”，不是“提供可直接移植的前端骨架”。

## 5. shadcn starter 借鉴矩阵

| Repo | 借 | 不借 | 结论 |
|---|---|---|---|
| `Kiranism/next-shadcn-dashboard-starter` | Query / Form / Table / Dialog / Theme / Command Palette 的写法 | Next.js 16、Clerk、Sentry、auth-first dashboard skeleton | 组件 cookbook 强，不能整模板继承 |
| `Kiranism/tanstack-start-dashboard` | `Vite + TanStack Router + Query + Form + Zustand` 的协同写法 | Start/Nitro/server fn 假设 | 技术对照价值高，适合作为第二参考 |
| `arhamkhnz/next-shadcn-admin-dashboard` | theme preset、layout density、colocation 说明 | 多 dashboard / RBAC / multi-tenant 方向 | 视觉与组织参考，可读即可 |
| `satnaing/shadcn-admin` | Vite browser UI、TanStack Router、Lucide、可复用控件与 layout primitives | sidebar-first dashboard IA 整体继承 | 最值得 local-only clone 的单一参考 |
| `SSV0726/next-shadcn-dashboard-starter` | 几乎无新增价值 | 老依赖、低维护、与上游重复 | drop |

这里要再强调一次：

- 我们要借的是 `component usage patterns`、`panel ergonomics`、`query/form/state wiring`。
- 我们不要借的是 `admin dashboard product shape`。
- `capture station != admin dashboard`，所以所有 sidebar / auth / tenant / CRM / finance 语义都只能当噪声处理。

## 6. Router 结论单列

必须单列写清楚，避免后续被文档误读：

- 本次 scan 没有证据支持“现在就锁 `React Router 6`”。
- 本次 scan 也没有证据支持“现在就锁死 TanStack Router，且排除 React Router 6”。
- 当前更合理的表达是：

```text
路由结论 = 延后到 PR72 prototype 验证后定；
当前更值得先试 TanStack Router，
但必须明确：不预锁 React Router 6。
```

原因：

1. `satnaing/shadcn-admin` 与 `Kiranism/tanstack-start-dashboard` 都给出了 TanStack Router 的强样本。
2. 但 ScoutFlow 自己还没有跑过四面板 capture station 原型，无法判断 TanStack Router 的搜索参数、嵌套路由、状态恢复收益是否真的覆盖复杂度。
3. 在这个阶段先锁路由，只会把 prototype 变成为框架辩护，而不是为真实交互验证服务。

## 7. Wave 3B 行动建议

这些建议只定义 prototype 输入，不批准任何 `apps/**` 或前端实现。

### 7.1 PR72 prototype mock 的输入建议

建议 prototype 输入栈暂定为：

- `Vite 7`
- `React 19`
- `shadcn (vendored)`
- `Tailwind v4`
- `TanStack Query`
- `TanStack Form + Zod`
- `Zustand`
- `React Flow`
- `Lucide`
- `router deferred`

这满足三个目标：

1. 尽量贴近当前 strongest references。
2. 不引入 Next.js / SSR / Electron 的无关复杂度。
3. 允许 prototype 先验证四面板交互，而不是先选框架立场。

### 7.2 PR67 local-only clone 建议

如果 Wave 3B 只 clone 一个 winner 到 `referencerepo/frontend/`，我建议优先：

- `satnaing/shadcn-admin`

原因：

- 它最接近浏览器 H5 donor，而不是全栈 starter。
- 维护活跃、规模足够、Vite/TanStack/Lucide 组合稳定。
- 更适合拆出局部控件和 layout primitives。

第二参考保留：

- `Kiranism/tanstack-start-dashboard`

但它更像“架构对照样本”，不是第一 clone winner。

### 7.3 明确不批准的内容

这份 scan 明确不批准：

- 任何 `apps/capture-station/**` 代码
- 任何 Next.js / Vite scaffold 落地
- 任何 router 最终定案
- 任何 Electron 或桌面壳尝试
- 任何 admin-dashboard layout 直接继承

## 8. 最终裁决

```text
Verdict: clear

- Vite browser H5 路线继续成立
- no SSR requirement / no Electron / no admin-dashboard template lock-in 需要继续作为红线
- satnaing/shadcn-admin = Wave 3B local-only clone 首选
- Kiranism/tanstack-start-dashboard = 路由/表单/查询第二参考
- OpenWhispr = stack signal，不是前端骨架
- 不预锁 React Router 6；router 延后到 PR72 prototype 验证后定
```
