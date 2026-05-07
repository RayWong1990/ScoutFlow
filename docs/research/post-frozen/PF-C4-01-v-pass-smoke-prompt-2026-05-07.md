---
title: PF-C4-01 V-PASS Smoke Prompt (paste-ready, v2 post-audit)
status: candidate
authority: not-authority
purpose: 战友 paste 给 Codex (或自己跑) 启动 dev server + 走 5 Gate per surface + 输出 V-PASS verdict
created_at: 2026-05-07
target_pr: 243
target_branch: codex/pf-c4-01-2026-05-07
target_commit: a848e70
target_mergeable: MERGEABLE
target_merge_state_status: UNSTABLE
ci_status: 5/6 SUCCESS + 1/6 FAILURE (e2e-placeholder-baseline = expected supersede)
prerequisite: PR #243 已 build/lint/typecheck/test 全绿, dev smoke 4173 HTTP 200, 等 V-PASS 终判
boundary: 不改代码 (除非 V-REJECT 单点 amend), 不解禁 5 overflow lane, 不写 authority files
file_path: docs/research/post-frozen/PF-C4-01-v-pass-smoke-prompt-2026-05-07.md
---

# PF-C4-01 V-PASS Smoke Prompt (v2)

> **路径已选**: A — 接受 PR #243 (符合 OpenDesign reuse strategy candidate PR #122 §10 reject list + D5/E1/E6).
> - D5 = no styling package approval / E1 = zero-install styling (CSS Variables + CSS Modules) / E6 = token consumption CSS Variables primary
> **本 prompt 用途**: 战友走 5 Gate V-PASS 浏览器终判. Codex 此前已 build/test/lint/typecheck 全绿 + dev smoke 4173 HTTP 200 (证据: `docs/research/post-frozen/PF-C4-01/PF-C4-01-CHECKPOINT.json`), 但按 boundary 没做 browser automation, 视觉终判必须战友亲眼.
> **执行模式**: paste 给 Codex 启动 dev server 后台 + 战友自己开浏览器走表; 或战友自己 cd + pnpm + 开 browser.

---

## §1 真态锚点

- repo: `/Users/wanglei/workspace/ScoutFlow`
- branch: `codex/pf-c4-01-2026-05-07` (commit `a848e70`)
- PR: #243
  - `mergeable=MERGEABLE` (git 可合并, 无 conflict)
  - `mergeStateStatus=UNSTABLE` (1/6 CI check FAIL → 普通 merge 命令会被拒, **必须用 `--admin` 或 web UI override**, 见 §5 路径 1)
  - 6502+ / 1935- / 98 file
- 真 authority: `docs/research/repairs/opendesign-reuse-strategy-candidate-2026-05-05.md` (PR #122 已 merged 2026-05-05)
- stack 实际跑出: React 18.3.1 + react-dom + Vite 5.4.10 + CSS Modules + tokens.css + 自写 SVG sprite (符合 D5 / E1 / E6 / §10 reject list)
- 13 surface 是 sidebar nav 切换 (单页 setCurrent state), **不是 multi-route**, 战友打开 http://localhost:4173 后用左侧 sidebar 切 13 次
- 4 honest TODO 已标 (thumbnail BBDown / D3 graph / timeline hover / error-path) — 不阻塞 V-PASS, 后续单独 dispatch
- e2e-placeholder-baseline FAIL = expected supersede:
  - 本 PR 删除了 `apps/capture-station/src/features/vault-commit/VaultCommitDryRunButton.tsx` (placeholder shell, 109 删除行)
  - 旧 baseline test (`tests/e2e/test_h5_bridge_commit_dry_run_placeholder.py`) 还指向旧路径
  - 真 surface `VaultCommit.tsx` 已替换, 测试需要后续单独 PR 重指
  - **不是 bug, 是 baseline 滞后. merge 时用 admin override / web UI override 即可**
- 写边界 (来自 PF-C4-01 scope note): `apps/capture-station/**` only; 不动 services / workers / packages / data / referencerepo / authority files

---

## §2 启动 dev server (战友 paste 执行 — worktree 隔离推荐)

### 选项 A — worktree 隔离 (推荐, 不影响 main 工作树)

```bash
cd /Users/wanglei/workspace/ScoutFlow
git fetch origin --prune
git worktree add /tmp/sf-pf-c4-01 codex/pf-c4-01-2026-05-07
cd /tmp/sf-pf-c4-01/apps/capture-station
pnpm install --frozen-lockfile
pnpm run dev
```

### 选项 B — 在 main wt 切 branch (需先确认 git status 干净)

```bash
cd /Users/wanglei/workspace/ScoutFlow
git fetch origin --prune
git status -s   # 确认无追踪文件未提交修改; 有则先 `git stash push -u`
git checkout codex/pf-c4-01-2026-05-07
cd apps/capture-station
pnpm install --frozen-lockfile
pnpm run dev
```

### 期望

- 输出 `Local:   http://127.0.0.1:4173/` (vite.config.ts 已显式 `server.port=4173 + preview.port=4173`, 都 hardcoded 4173, 不会用默认 5173)
- 浏览器开 http://localhost:4173 → AppShell + 左侧 sidebar (13 surface 列表) + 右侧 surface 内容区

### 端口冲突排查

```bash
lsof -i :4173                              # 看占用
kill $(lsof -t -i :4173) 2>/dev/null || true   # kill 占用进程
# 或换端口启动:
pnpm run dev -- --port 5173
```

### Pnpm 版本兼容 fallback

```bash
# 若 lockfile schema 不兼容报错:
corepack enable && corepack prepare pnpm@latest --activate
pnpm install --frozen-lockfile
```

---

## §3 13 Surface V-PASS 清单 (战友逐个点 sidebar 走)

### 5 Gate 量化基线 (走表对照, 来源: `/Users/wanglei/.claude/rules/aesthetic-first-principles.md`)

| Gate | 量化标准 |
|---|---|
| Gate 1 视觉层级 | 主标题字号 vs 副标题字号差 ≥30%; 3 秒说出"重点是哪个"; 扫描路径符合 Z/F 形 |
| Gate 2 空间对齐 | 8px (8dp) 栅格遵守; 同类元素 baseline 对齐; 留白节奏一致 |
| Gate 3 遮挡安全 | 关键信息 0 遮挡; popup/badge 不压主内容; 安全区遵守 |
| Gate 4 字体可读 | 主标题 ≥20px (web), 行高 ≥1.3, 文字与背景对比 ≥4.5:1 (WCAG AA) |
| Gate 5 视觉重量 | 重要元素视觉质量 ≥次要元素 1.5x; 高饱和色不互相抢戏; 构图平衡或刻意倾斜 |

### Surface 列表 (按 sidebar 顺序, 13 项)

| # | ID | Title | 重点检查 |
|---|---|---|---|
| 0 | `00-app-shell` | App Shell | 工作站总览 + 4 panel grid + sidebar nav 自身视觉 |
| 1 | `01-url-bar` | URL Bar | 输入框 + 校验状态 + 历史下拉 + 中文 placeholder |
| 2 | `02-live-metadata` | Live Metadata | 元数据卡片状态集 (loading/error/ready) + thumbnail TODO 占位是否诚实 |
| 3 | `03-capture-scope` | Capture Scope | 生命周期 stepper + 边界标签 + 状态 modifier |
| 4 | `04-trust-trace` | Trust Trace | 图谱占位 (D3 TODO) + 时间轴占位 + 错误路径占位 — **3 个 honest TODO 是否诚实标注** |
| 5 | `05-vault-preview` | Vault Preview | frontmatter 块 + Markdown 预览 + 字体可读性 |
| 6 | `06-vault-commit` | Vault Commit | 干跑按钮 + Modal 弹窗 + write_disabled 提示文案 |
| 7 | `07-topic-card-lite` | Topic Card Lite | 新闻/视频/对比三态 + tag list + 节奏 |
| 8 | `08-topic-card-vault` | Topic Card Vault | 聚合 + promote gate + **L8 sync-badge 3 状态 (synced=已同步 / pending=待同步 / external-changed=外部已改)** |
| 9 | `09-signal-hypothesis` | Signal / Hypothesis | 展开/对比/生命周期 |
| 10 | `10-capture-plan` | Capture Plan | I/O 字段 + 干跑日志 + 错误态 |
| 11 | `11-density-spec` | Density Spec | V3 紧凑密度参考页 (overlay 验证) |
| 12 | `12-type-spec` | Type Spec | V4 高字重参考页 (overlay 验证) |

### Per-surface verdict 格式

每个 surface 走 5 Gate, 每 gate 1 行:

```
Gate 1 视觉层级:    [V-PASS / V-CONCERN / V-REJECT] — <1句>
Gate 2 空间对齐:    [V-PASS / V-CONCERN / V-REJECT] — <1句>
Gate 3 遮挡安全:    [V-PASS / V-CONCERN / V-REJECT] — <1句>
Gate 4 字体可读:    [V-PASS / V-CONCERN / V-REJECT] — <1句>
Gate 5 视觉重量:    [V-PASS / V-CONCERN / V-REJECT] — <1句>
Surface verdict:    [V-PASS / V-CONCERN / V-REJECT] — <2-3句 总评>
```

### 13 surface verdict 收集模板 (战友走完后 paste 给 CC1)

```
--- 走表元数据 ---
reviewer: 王磊
timestamp: 2026-05-07T<HH:MM>+08:00
branch: codex/pf-c4-01-2026-05-07
commit: a848e70
dev_server_url: http://localhost:4173

--- 13 surface verdict ---
Surface 00 App Shell:           [verdict] — <概述>
Surface 01 URL Bar:             [verdict] — <概述>
Surface 02 Live Metadata:       [verdict] — <概述>
Surface 03 Capture Scope:       [verdict] — <概述>
Surface 04 Trust Trace:         [verdict] — <概述> (4 TODO 是否诚实)
Surface 05 Vault Preview:       [verdict] — <概述>
Surface 06 Vault Commit:        [verdict] — <概述>
Surface 07 Topic Card Lite:     [verdict] — <概述>
Surface 08 Topic Card Vault:    [verdict] — <概述> (sync-badge 3 状态是否齐)
Surface 09 Signal/Hypothesis:   [verdict] — <概述>
Surface 10 Capture Plan:        [verdict] — <概述>
Surface 11 Density Spec:        [verdict] — <概述> (V3 overlay)
Surface 12 Type Spec:           [verdict] — <概述> (V4 overlay)

--- 整体 ---
整体 verdict: [V-PASS-ALL / V-CONCERN-PARTIAL / V-REJECT-MAJOR]
overall: <2-3句 总评 + 操作员工作站气质是否长出来了>
```

---

## §4 Codex 协助任务 (paste 给 Codex 跑)

战友自己开浏览器是 V-PASS 关键, 但 Codex 可以协助两件事 (不动代码):

### Task A — 启动 dev server (background)

```bash
cd /Users/wanglei/workspace/ScoutFlow
git fetch origin --prune
git worktree add /tmp/sf-pf-c4-01 codex/pf-c4-01-2026-05-07 2>/dev/null || true
cd /tmp/sf-pf-c4-01/apps/capture-station
pnpm install --frozen-lockfile
nohup pnpm run dev > /tmp/scoutflow-dev-$(date +%s).log 2>&1 &
sleep 5
curl -sI http://localhost:4173 | head -3
echo "---"
echo "DEV_SERVER_URL: http://localhost:4173"
echo "13 SURFACES (sidebar nav, single-page setState): 00-app-shell / 01-url-bar / 02-live-metadata / 03-capture-scope / 04-trust-trace / 05-vault-preview / 06-vault-commit / 07-topic-card-lite / 08-topic-card-vault / 09-signal-hypothesis / 10-capture-plan / 11-density-spec / 12-type-spec"
echo "INSTRUCTION: open http://localhost:4173, 用左侧 sidebar 切 13 个 surface, 每个走 5 Gate"
echo ""
echo "STOP 命令 (V-PASS 完成后清理):"
echo "kill \$(lsof -t -i :4173) 2>/dev/null || true"
echo "git worktree remove /tmp/sf-pf-c4-01"
```

### Task B — 静态自审 receipt (帮战友先扫一遍可发现的硬伤)

**前置守护 (必须先验证 cwd + branch)**:

```bash
# 必须在已 checkout PR branch 的 wt 跑
cd /tmp/sf-pf-c4-01   # 或战友 §2 选项 B 的 main wt
test "$(git rev-parse --abbrev-ref HEAD)" = "codex/pf-c4-01-2026-05-07" \
  || { echo "ABORT: not on PF-C4-01 branch (current: $(git rev-parse --abbrev-ref HEAD))"; exit 1; }
echo "OK: on codex/pf-c4-01-2026-05-07 / commit $(git rev-parse --short HEAD)"
```

**跑 grep 命令并把结果汇总到 receipt**:

```bash
# 1. Hex 硬编码扫描 (anti-pattern, 应只走 tokens.css var; 期望 0 命中)
grep -rEn '#[0-9a-fA-F]{3,8}' apps/capture-station/src --include='*.tsx' --include='*.module.css' \
  | grep -v 'tokens.css' \
  | grep -v 'density-compact.css' \
  | grep -v 'type-weight-heavy.css' \
  | head -50

# 2. Inline style hex (期望 0)
grep -rEn 'style=\{\{.*#[0-9a-fA-F]{3,8}' apps/capture-station/src --include='*.tsx' | head -20

# 3. SVG sprite 接入 (期望 <Icon> 调用 ≥10, Icon.tsx 内部 <use href> ==2)
grep -rEn '<Icon ' apps/capture-station/src --include='*.tsx' | wc -l
grep -rEn '<use href' apps/capture-station/src/components/Icon/Icon.tsx | wc -l

# 4. L8 sync-badge 3 状态 (.tsx + .module.css 双查)
grep -nE 'synced|pending|external-changed|externalChanged' apps/capture-station/src/components/SyncBadge/SyncBadge.tsx
grep -nE '\.synced|\.pending|\.externalChanged' apps/capture-station/src/components/SyncBadge/SyncBadge.module.css
grep -nE 'synced|pending|external-changed' apps/capture-station/src/features/topic-card-vault/TopicCardVault.tsx | head -10

# 5. 4 honest TODO 标注 (期望 thumbnail + D3 graph + timeline + error-path 全有 data-todo)
grep -rEn 'data-todo|TODO P[12]|placeholder' apps/capture-station/src/features/live-metadata apps/capture-station/src/features/trust-trace | head -30

# 6. Token 引用密度 (期望 var(--*) ≥100, 实测 375+)
grep -rEn 'var\(--' apps/capture-station/src --include='*.module.css' | wc -l

# 7. CSS-in-JS 反模式 (期望 0)
grep -rEn 'from .styled-components|from .@emotion|from .@stitches|from .vanilla-extract|from .panda-css' apps/capture-station/src --include='*.tsx' | head -10
grep -rEn 'from .@mui|from .antd|from .@chakra-ui|from .@mantine|from .lucide-react' apps/capture-station/src --include='*.tsx' | head -10

# 8. 反 stack 引入 (期望 0)
grep -rEn 'from .@radix-ui|from .@tanstack|from .reactflow|from .react-flow|from .zustand' apps/capture-station/src --include='*.tsx' | head -10
```

输出 receipt 到 `docs/research/post-frozen/PF-C4-01/receipts/v-pass-static-audit-2026-05-07.md`:

```markdown
---
title: PF-C4-01 V-PASS Static Audit Receipt
status: candidate
not_authority: true
created_at: 2026-05-07
auditor: codex
target_pr: 243
target_commit: a848e70
purpose: 帮战友先扫一遍 V-PASS 可发现的硬伤, 不替代浏览器视觉终判
---

# Static Audit Findings

## 1. Hex 硬编码扫描 (期望 0 命中, 排除 tokens/density/type-weight)
[N] 处命中, 列出 file:line + hex 值 (0 → CLEAN)

## 2. Inline style hex (期望 0)
[N] 处命中

## 3. SVG sprite 接入
- <Icon> 组件调用: [N] 处 (期望 ≥10)
- Icon.tsx 内部 <use href>: [N] 处 (期望 ==2; sprite 路由由组件集中, 业务层不直写 <use>)

## 4. L8 sync-badge 3 状态
- SyncBadge.tsx 类型联合: synced [yes/no] / pending [yes/no] / external-changed [yes/no]
- SyncBadge.module.css class: .synced [yes/no] / .pending [yes/no] / .externalChanged [yes/no]
- TopicCardVault.tsx 调用: [N] 处

## 5. 4 honest TODO 标注 (data-todo + TODO 注释双查)
- thumbnail (live-metadata): [honest / silent / missing]  — 期望 LiveMetadata.tsx:95 P1 BBDown
- D3 graph (trust-trace): [honest / silent / missing]     — 期望 TrustTrace.tsx:19 P1 D3/cytoscape
- timeline hover (trust-trace): [honest / silent / missing]  — 期望 TrustTrace.tsx:33 P2
- error-path (trust-trace): [honest / silent / missing]   — 期望 TrustTrace.tsx:47 P1

## 6. Token 引用密度
[N] 个 var(--*) 引用 (期望 ≥100, 实测应 ~375)

## 7. CSS-in-JS 反模式扫描 (期望 0 命中)
- styled-components / @emotion / @stitches / vanilla-extract / panda-css: [N]
- @mui / antd / @chakra-ui / @mantine / lucide-react: [N]

## 8. 反 stack 引入扫描 (期望 0 命中)
- @radix-ui / @tanstack / reactflow / zustand: [N]

## Verdict
[CLEAN / CONCERN / FAIL] — <一句 总评>

## 已知豁免
- e2e-placeholder-baseline FAIL = expected supersede (placeholder 路径已删除, baseline test 滞后, 不是真 bug)
```

---

## §5 V-PASS 后续路径 (战友走完后)

### 路径选择阈值 (战友走完 13 surface 后对照)

| 整体状况 | 路径 | 判定标准 |
|---|---|---|
| 13 surface 全 V-PASS / V-CONCERN-MINOR | 路径 1 V-PASS-ALL | 0 V-REJECT, V-CONCERN ≤ 3 |
| 1-3 surface V-CONCERN/V-REJECT | 路径 2 单点 amend | 单点 amend trail ≤ 1 (lane 总额) |
| ≥4 surface 任一 gate REJECT, 或 ≥2 surface 整 surface REJECT, 或 sidebar/AppShell V-REJECT | 路径 3 root cause | 单点修不动, 必走外审 |

### 路径 1 — V-PASS-ALL (整体 V-PASS, 13 surface 全 V-PASS 或 V-CONCERN-MINOR)

战友执行 (PR check 1/6 红是 expected supersede, 必须 admin / web UI override):

```bash
cd /Users/wanglei/workspace/ScoutFlow

# 路径 1A: gh CLI (需 repo admin / branch protection 允许 admin merge)
gh pr merge 243 --squash --delete-branch --admin

# 路径 1B: 若 admin merge 不开放, 走 web UI override
# open https://github.com/RayWong1990/ScoutFlow/pull/243
# 点 "Merge pull request" → 选 "Squash and merge" → UI 会显式提示 1 check failing → 点继续即可
# (e2e-placeholder-baseline FAIL = expected supersede, 详见 §1)

git checkout main && git pull --ff-only
git worktree remove /tmp/sf-pf-c4-01 2>/dev/null || true
```

然后写 closeout:
- `docs/research/post-frozen/PF-C4-01-v-pass-merged-2026-05-07.md` (war-room receipt: V-PASS verdict + merge SHA + 4 TODO 后续 dispatch 列表)
- 4 个 TODO 的后续 dispatch (各 1 个 candidate doc): `docs/research/post-frozen/PF-C4-EXT-{thumbnail,d3-graph,timeline,error-path}-candidate-2026-05-07.md`

### 路径 2 — V-CONCERN-PARTIAL (1-3 surface V-CONCERN, 单点 amend)

amend_and_proceed pattern (Run-1 / Run-2 / Run-3+4 已立). 单点 dispatch 模板 (paste 给 Codex):

```markdown
---
title: PF-C4-01 amend surface NN receipt
status: candidate
authority: amendment / not-authority
created_at: 2026-05-07
amend_trail_count: 1
lane_amend_total_max: 1
target_pr: 243
target_branch: codex/pf-c4-01-2026-05-07
---

# PF-C4-01 amend dispatch — Surface NN (替换 NN 为真 surface 编号, 如 04)

## 背景
PR #243 战友 V-PASS, surface NN (路径 apps/capture-station/src/features/<surface>/) 有以下 concern:
- Gate N: <具体>
- Gate M: <具体>

## 任务
单点修复 surface NN, 不动其他 surface, 不引入新 dependency.

## 边界
- 仅修 apps/capture-station/src/features/<surface>/*.tsx + *.module.css
- 不改 tokens.css (除非战友明确批 token 升级)
- 不改 OpenDesign reuse strategy candidate (PR #122)
- 不改 PF-C4-01-CHECKPOINT.json (lane closeout immutable)
- amend trail 计 +1 (lane total ≤ 1, 当前 0)

## 验收
- pnpm run lint / typecheck / test / build 全过
- 战友复审该 surface 5 Gate 全过
- 写 receipt: docs/research/post-frozen/PF-C4-01/receipts/amend-surface-{NN}-2026-05-07.md
  (NN 替换为 surface 编号, 如 surface 04 → amend-surface-04-2026-05-07.md)
```

战友 paste 给 Codex 跑, 跑完战友复审 single surface, V-PASS → merge.

### 路径 3 — V-REJECT-MAJOR (≥4 surface gate REJECT, 或 ≥2 surface 整 REJECT, 或 sidebar/AppShell V-REJECT)

不是 amend, 是 reject 重派. architect verdict 已说 stack 选择正确 + Codex 翻译质量全绿, V-REJECT-MAJOR 概率极低. 真走到了:
- 写 `docs/research/post-frozen/PF-C4-01-v-reject-postmortem-2026-05-07.md`
- 召集 Hermes 三方独立外审 (本 amend 单元成功率不够, 需要 root cause)
- **不直接重派**, 先做 root cause analysis: 是 prompt v1 缺陷? Codex 翻译走偏? 还是 P7 输出本身就缺 IA?

---

## §6 4 Honest TODO 后续 dispatch (不阻塞 PR #243 merge)

PR #243 的 4 honest TODO 是 expected unfinished, 不阻塞 merge. 后续单独走 §5.2 future styling/token strategy candidate slot 流程:

| TODO | Surface | 候选实现 | 边界 |
|---|---|---|---|
| Thumbnail | 02 Live Metadata (line 95) | BBDown 元数据接入 | **5 overflow lane "true_vault_write" / "runtime_tools" 仍 Hold**, 阻塞中. 不解禁前 TODO 是 honest 状态 |
| D3 graph | 04 Trust Trace (line 19) | D3 / cytoscape / vis-network 单点引 (走 §5.2 future slot) | **不引整套 shadcn vendored**. 单点引一个 graph lib + 自己写交互. 走 PR #122 v2 升级流程 |
| Timeline hover | 04 Trust Trace (line 33) | 自写 (CSS Variables + React state), 不引第三方 | 优先自写, 验证后单点引才考虑 |
| Error-path 高亮 | 04 Trust Trace (line 47) | 自写 (依赖 D3 graph) | 跟 D3 graph 一起设计 |

每个 TODO 单独 candidate doc + 单独 PR, 不打包. 命名空间: `PF-C4-EXT-{TODO-name}-candidate-2026-05-07.md` (与 TrustTrace.tsx:19 注释一致).

---

## §7 反模式 (V-PASS 时检查)

如发现以下任一, 直接 V-CONCERN/REJECT:

**主要禁用 (架构层)**:

- ❌ Tailwind utility class (任何 `text-*`, `bg-*`, `flex-*`, `p-*`, `m-*`)
- ❌ shadcn 组件命名 (`button-variant`, `card-component`, `dialog-overlay`)
- ❌ Lucide icon import (`from 'lucide-react'`)
- ❌ Radix UI primitive (`@radix-ui/*`)
- ❌ TanStack Query / Form / Table import (`@tanstack/*`)
- ❌ React Flow 真引入 (TODO 标注 OK, 真 import 不 OK)
- ❌ Zustand store import (`from 'zustand'`)

**CSS-in-JS 禁用 (style 层)**:

- ❌ styled-components / @emotion/styled / @emotion/react import
- ❌ @stitches/react / vanilla-extract / panda-css import

**组件库禁用 (整套 generic admin/dashboard 气质)**:

- ❌ Mantine / Ant Design / Chakra UI / @mui/* import

**视觉违规**:

- ❌ Hex 硬编码 (除 tokens.css / density / type-weight 文件)
- ❌ inline style hex
- ❌ generic admin/dashboard 视觉气质 (战友审美红线)
- ❌ L8 sync-badge 缺三状态 (synced / pending / external-changed 任缺一)
- ❌ silent TODO (4 honest TODO 应有显式占位 UI + 标注, 不能默默渲染空白)

如全过 → 操作员工作站气质合格 → V-PASS-ALL.

---

## §8 战友的最低 V-PASS 走表时间预算

- Codex Task A 启动 dev server: 2-3 min (pnpm install + dev start)
- Codex Task B 静态自审 receipt: 2-3 min
  (Codex 跑 Task B 时, 战友可并行开浏览器走表)
- 战友 13 surface × 5 Gate × 2-3 min/surface = 30-45 min
- 单点 amend (如有 1-3 surface V-CONCERN): 60-90 min × Codex 修复
  (含 build/lint/test/typecheck 4 步 + 战友单 surface 复审 5 Gate + commit/push)
- 整体 V-PASS-ALL → merge: 10 min (含 closeout 写 + admin/web override)

**预算总计**: 顺利 1-1.5h 内 merge, 需 amend 2.5-3.5h 内 merge.

---

## §9 严禁动作 (V-PASS 阶段)

- ❌ Codex 修代码 (除非战友明确派单 amend)
- ❌ 解禁 5 overflow lane (`true_vault_write` / `runtime_tools` / `browser_automation` / `dbvnext_migration` / `full_signal_workbench`)
- ❌ 写 authority files (`docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `AGENTS.md` / 根 `CLAUDE.md`)
- ❌ 修改 `docs/research/post-frozen/PF-C4-01/PF-C4-01-CHECKPOINT.json` (lane closeout ledger immutable; amend 只写新 receipt, 不动 CHECKPOINT)
- ❌ 修改 `docs/research/post-frozen/runs/CHECKPOINT-Run*.json` / `EXTERNAL-AUDIT-REPORT-*.md` (历史 ledger immutable)
- ❌ 修改 PR #122 OpenDesign reuse strategy candidate (那是另一个独立 PR 走升级流程, 非本 V-PASS 阶段动作)
- ❌ 引入任何新 npm dependency
- ❌ 跑 browser automation (playwright / selenium) — 视觉终判战友亲眼
- ❌ 污染 `~/workspace/raw/` (永不写)
- ❌ 跨过 PR #243 merge 直接开 PR #244 加 vendored shadcn (即 "candidate C 路径" — 接受 PR #243 + 渐进引入 vendored shadcn / TanStack / React Flow / Zustand; 已 architect verdict 否决, 因 vendored shadcn 在 OpenDesign reuse strategy §10 reject list 边界上反复试探, 是 transplant 软化诱惑)

---

## §10 输出物 (战友 V-PASS 走完后, 派 CC1 处理)

战友完成 V-PASS 后, paste 以下信息给 CC1:

```
PF-C4-01 V-PASS 走表完成.

--- 走表元数据 ---
reviewer: 王磊
timestamp: 2026-05-07T<HH:MM>+08:00
branch: codex/pf-c4-01-2026-05-07
commit: a848e70
dev_server_url: http://localhost:4173

--- 整体 ---
整体 verdict: [V-PASS-ALL / V-CONCERN-PARTIAL / V-REJECT-MAJOR]

--- 13 surface ---
Surface 00: ...
Surface 01: ...
...
Surface 12: ...

--- 关键检查 ---
L8 sync-badge: [3 状态齐 / 缺 X]
4 honest TODO: [全 honest / 缺 silent X]
反模式扫描 (Codex Task B receipt): [0 hit / N hit (列出)]

--- 下一步 ---
[merge PR #243 (路径 1) / amend surface X (路径 2) / root cause (路径 3)]
```

CC1 收到后:
- 路径 1 V-PASS-ALL → 写 closeout + 执行 `gh pr merge 243 --squash --delete-branch --admin` (或 web UI override)
- 路径 2 V-CONCERN-PARTIAL → 写 amend dispatch 给 Codex 单点修
- 路径 3 V-REJECT-MAJOR → 召 Hermes 三方外审

---

## §11 sentinel: 4 个 honest TODO 不阻塞 merge

PR #243 的 4 TODO 是 expected unfinished:
- thumbnail TODO: 等 5 overflow lane (`true_vault_write` / `runtime_tools`) 解禁
- D3 graph TODO: 等单独 PR 走 §5.2 future slot 选型
- timeline hover TODO: 优先自写, 后续 PR
- error-path TODO: 跟 D3 graph 一起

**这 4 TODO 在 V-PASS 时只检查"是否诚实标注 + 占位 UI 是否合理", 不检查"是否实现". 实现走后续单独 PF-C4-EXT-* dispatch.**

---

## §12 V-PASS 完成后清理

```bash
# 停 dev server
kill $(lsof -t -i :4173) 2>/dev/null || true

# 删 worktree (如 §2 选项 A)
cd /Users/wanglei/workspace/ScoutFlow
git worktree remove /tmp/sf-pf-c4-01 2>/dev/null || true
```

---

## §13 自审 self-check (CC1 / 战友任意一方修订本 prompt 后跑一遍)

```bash
PROMPT=/Users/wanglei/workspace/ScoutFlow/docs/research/post-frozen/PF-C4-01-v-pass-smoke-prompt-2026-05-07.md

# 1. overflow lane 真名 (期望 0 命中缩写)
grep -nE 'browser_auto[^m]|signal_workbench[^_]' "$PROMPT" | head

# 2. <use href> 期望阈值 (期望 0 命中 ">20")
grep -nE '<use href.*>20|期望 >20' "$PROMPT" | head

# 3. frozen-lockfile (期望 ≥2 命中: §2 + §4 Task A)
grep -cE 'frozen-lockfile' "$PROMPT"

# 4. admin / UNSTABLE (期望 ≥2 命中: 路径 1 + §1)
grep -cE 'admin|UNSTABLE|web UI override' "$PROMPT"

# 5. cd / branch 守护 (期望 §4 Task B 有 abort guard)
grep -nE 'ABORT.*not on PF-C4-01' "$PROMPT"

# 6. 5 Gate 量化阈值 (期望命中 4.5:1 + 8px + 1.5x)
grep -nE '4\.5:1|8px|1\.5x' "$PROMPT"

# 7. CSS-in-JS 反模式 (期望命中 emotion / styled-components)
grep -cE 'styled-components|@emotion|panda-css' "$PROMPT"

# 8. 路径 3 阈值 (期望明确 ≥4 surface)
grep -nE '≥4 surface|≥2 surface' "$PROMPT"
```

8 条全过 → prompt v2 ready.

---

> 本 prompt v2 by CC1, 2026-05-07 (post 刑部尚书严审修订: 7 Critical + 7 High + 9 Medium + 7 Low 全修)
> 关联: PR #243 / OpenDesign reuse strategy PR #122 / PF-C4-01 commander prompt v1 / `~/.claude/rules/aesthetic-first-principles.md`
> 下一步: 战友 paste § 2 + §4 Task A 给 Codex (或自己跑) → 13 surface V-PASS → 整体 verdict → CC1 merge / amend
> 文件路径: `docs/research/post-frozen/PF-C4-01-v-pass-smoke-prompt-2026-05-07.md`
