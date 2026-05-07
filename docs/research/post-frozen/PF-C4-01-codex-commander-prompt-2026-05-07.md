---
title: PF-C4-01 Codex Commander Prompt — Local Frontend Bootstrap + p7-reference Scaffold + 13 surface TSX
status: candidate / commander_prompt / not-authority
authority: not-authority
target_executor: Codex (本地 long-runner mode)
expected_runtime: 5-7h Codex 通宵
created_at: 2026-05-07
inputs:
  - PR #241 (PF-V handoff merged 2026-05-07 05:47 UTC)
  - docs/research/visual-prototypes/PF-V/p7-output/ (76 files)
  - docs/research/post-frozen/80-pack-source/02_task_packs/PF-C4-controlled-hardening-pack/dispatches/PF-C4-01-*.md
---

# PF-C4-01 Codex Commander Prompt

> 战友 — 这是给 Codex 的通宵 commander prompt. CC1 设计 + 用户授权后 paste 给 Codex 跑.
> 4 phase / **20 dispatch** (P1×1 + P2×3 + P3×14 + P4×2) / ~5-7h. 严格 boundary 守 / amend_and_proceed pattern / 单 PR direct merge or 4 PR per phase 选一.

## §0 Codex 角色与上下文

你是 Codex, ScoutFlow 项目的 **Long Runner Coder** (4-agent 分工 v3 角色). 你将在本地 worktree 通宵长跑 PF-C4-01 lane, 把 PF-V P7 输出迁入 `apps/capture-station/`, 完成 13 surface React TSX 翻译 + scaffold + build green.

**协作模式**:
- CC1 (Claude, 当前 PM) 设计本 prompt + 后期 audit
- 你 (Codex) 本地长跑执行 + commit + amend_and_proceed
- 必要时 Hermes 三方独立外审 (用户决定)

**实证战绩参考**: 你在 ScoutFlow 已完成 ~84 dispatch 跨 5 run 通宵不掉线. Run-3+4 24 dispatch packed PR #240 是本 commander 模式的成功先例.

**用户 mid-run 介入**: 战友 (用户) 可能 mid-run 来打断你. 你的默认行为: 立刻停下 + 写 "user-interrupt receipt" 入 `docs/research/post-frozen/PF-C4-01/receipts/user-interrupt-<timestamp>.md`, 含当前 phase / dispatch / state, 等用户重新指示再继续.

## §1 Mission

把 PF-V P7 输出 (76 file, 13 HTML surface + tokens + icons + CSS modules) 迁移到 `apps/capture-station/`, 实现 React TSX components + 集成 tokens.css + npm build green. 不引入 Tailwind / shadcn / Panda. 不解禁 5 overflow lane. 不改 authority files.

## §2 Inputs (must read in order)

### A. 必读 (handoff contract)
1. `docs/research/visual-prototypes/PF-V/05-HANDOFF-to-PF-C4-protocol.md` — **PF-V → PF-C4 handoff v1 完整契约 (160 行)**, §7 acceptance criteria 是你 lane closeout 标准
2. `docs/research/visual-prototypes/PF-V/06-ACCEPTANCE-CHECKLIST.md` — **30 项检验清单**
3. `docs/research/visual-prototypes/PF-V/LESSONS-LEARNED.md` — **L1-L13**, 特别 L8 (sync badge 3 档) / L11+L13 (density × typography 正交矩阵) / L10 (caption-as-spec)
4. `docs/research/post-frozen/80-pack-source/02_task_packs/PF-C4-controlled-hardening-pack/dispatches/PF-C4-01-local-frontend-dependency-bootstrap-repair.md` — 80-pack 既有 dispatch, 是 Phase 1 baseline

### B. P7 输出资产 (实施源)
5. `docs/research/visual-prototypes/PF-V/p7-output/README.md` + `MAPPING.md` — 76 文件使用指南 + 65 PNG → 76 H5 映射
6. `docs/research/visual-prototypes/PF-V/p7-output/tokens.css` — **15 主色 token + state bg + typography + spacing + radius + shadow** (56 行, 单源真相)
7. `docs/research/visual-prototypes/PF-V/p7-output/density-compact.css` — V3 Compact baseline (overlay 层)
8. `docs/research/visual-prototypes/PF-V/p7-output/type-weight-heavy.css` — V4 Weight Heavy baseline (overlay 层)
9. `docs/research/visual-prototypes/PF-V/p7-output/html5-rough/*.html` — **13 surface HTML rough** (00-app-shell ~ 12-type-spec)
10. `docs/research/visual-prototypes/PF-V/p7-output/html5-rough/*.module.css` — **13 surface CSS module rough**
11. `docs/research/visual-prototypes/PF-V/p7-output/html5-rough/*.model.json` — **13 JSON UI structural model** (Step 1 reference, 不是约束)
12. `docs/research/visual-prototypes/PF-V/p7-output/css-modules-candidate/` — **15 component candidate** (panel-card / url-input / state-badge / lifecycle-stepper / evidence-table / tag-list / capture-id-chip / topic-card / sync-badge / modal / governance-tooltip / live-pulse / btn / frontmatter-block / promote-gate)
13. `docs/research/visual-prototypes/PF-V/p7-output/icons/system.svg` + `icons/state.svg` — **2 SVG sprite**

### C. 既有 capture-station 现状 (实施目标)
14. `apps/capture-station/package.json` — Vite 5.4.10 + React 18.3.1 + TS 5.6.3 strict + Vitest 2.1.3
15. `apps/capture-station/vite.config.ts` + `tsconfig.json`
16. `apps/capture-station/src/features/` — **8 既有 feature 目录** (capture-scope / live-metadata / topic-card-preview / topic-card-vault / trust-trace / url-bar / vault-commit / vault-preview), url-bar/UrlBar.tsx 已有实现, 其他可能空或半成品
17. `apps/capture-station/src/lib/api-client.ts` — 既有 backend 接线

## §3 Hard Boundaries (硬红线, 违反任何一条 = kill signal)

```yaml
write_enabled: false                        # services/api/scoutflow_api/bridge/config.py 不变
can_open_C4: true                          # 你就是在跑 PF-C4-01, 这条允许
can_open_runtime: false                    # 不解禁 BBDown live / yt-dlp / ffmpeg / ASR
can_open_migration: false                  # 不动 services/api/migrations/**
can_open_browser_automation: false         # 不引入 Playwright / Selenium runtime
can_open_true_vault_write: false           # ~/workspace/raw/ 永不写
authority_files_writable: false            # docs/current.md / task-index.md / decision-log.md / AGENTS.md 不写
```

### 允许路径
- `apps/capture-station/**` (Phase 1-3 主 work)
- `docs/research/post-frozen/PF-C4-01/receipts/*.md` (你的 lane 收据, **子目录化**, 不污染顶层)
- `docs/research/post-frozen/PF-C4-01/PF-C4-01-CHECKPOINT.json` (lane 收尾 ledger)
- `docs/research/post-frozen/PF-C4-01/PF-C4-01-lane-closeout-2026-05-07.md` (closeout narrative)
- `docs/research/post-frozen/frontend-local-bootstrap-repair.md` (Phase 1 narrow report, 80-pack 既有 dispatch §2 expected output)

### 禁止路径
- `services/api/migrations/**`
- `workers/**`
- `packages/**`
- `data/**`
- `referencerepo/**`
- `docs/research/visual-prototypes/PF-V/**` (PF-V P8 后锁定, 不回写)
- `docs/research/post-frozen/runs/CHECKPOINT-Run*.json` (历史 ledger immutable, **永不修改**)
- `docs/research/post-frozen/runs/EXTERNAL-AUDIT-REPORT-*.md` (历史 audit 报告 immutable)
- `docs/PRD-*.md` / `docs/SRD-*.md` / `docs/decision-log.md` / `docs/task-index.md` / `docs/current.md` / `AGENTS.md`
- `~/workspace/raw/**` (用户真 vault, 永不污染)

### 禁止 claim
- `vendor accepted` (任何新依赖必须先 explicit 用户授权)
- `runtime approved`
- `migration approved`
- `true vault write approved`
- `5 overflow lane unlocked`

### 反模式 (禁止引入)
- ❌ Tailwind / shadcn / Panda / styled-components
- ❌ 任何全局 CSS 重置除 tokens.css
- ❌ tokens.css 外硬编码 hex 色值
- ❌ inline style hex
- ❌ 把 P7 raw HTML 直接 import 到 runtime
- ❌ 逐字照搬 P7 class name (P7 class name 是 review reference, 不是 production naming)
- ❌ 把 PNG 当 approved IA 或 pixel-perfect spec
- ❌ **L8 sync-badge collapse 成 binary saved/not-saved** (必须保留 synced / pending / external-changed 3 档语义, LESSONS L8 强制)

## §4 4-Phase 执行计划 + 20 dispatch

### Phase 1 — Dependency Bootstrap Repair (30-60 min, 1 dispatch)

**dispatch ID**: PF-C4-01-P1-bootstrap-repair

**Mission**: 80-pack 既有 PF-C4-01 dispatch — 让 `apps/capture-station/` npm test/build 能跑或 failure 收窄.

**Steps**:
0. **先决定 lock 策略**: `cd apps/capture-station && ls -la *.lock pnpm-lock.yaml package-lock.json yarn.lock 2>/dev/null`
   - 如已有 `pnpm-lock.yaml` (untracked OR tracked) → 用 pnpm, 跑 `pnpm install --frozen-lockfile` 失败再 `pnpm install`
   - 如已有 `package-lock.json` → 用 npm, 跑 `npm ci` 失败再 `npm install`
   - 两个都没 → 默认 pnpm install (生成 pnpm-lock.yaml 入 commit)
   - **不要混用 pnpm + npm**, 单一 lock 策略
1. install (按 Step 0 决定的工具)
2. `pnpm run typecheck` (or `npm run typecheck`) — 修任何 TS 错误
3. `pnpm run lint` — 修任何 ESLint 错误
4. `pnpm run build` — 修 Vite build 错误
5. `pnpm run test` — Vitest 全过 (允许 0 测试如本来就空, 但不允许 fail)
6. 如某步 fail 且不能 narrow 到 reproducible env issue (如 node 版本 / 平台特定包) → 标 partial pass + 写 narrow report 入 `docs/research/post-frozen/frontend-local-bootstrap-repair.md`

**Pass condition**: build green OR failure narrowed to env (含 narrow report)

**Output**:
- 修复 commit (如有)
- `docs/research/post-frozen/frontend-local-bootstrap-repair.md` (narrow report, 即使无修复也写)

---

### Phase 2 — feat(capture-station): scaffold p7-reference (1 h, 3 dispatch)

**dispatch ID**: PF-C4-01-P2-scaffold-{tokens,icons,components}

#### P2-01 tokens scaffold

**Mission**: 把 P7 tokens.css + density-compact.css + type-weight-heavy.css 迁入 capture-station, 作为 single source of truth.

**Steps**:
1. 创建 `apps/capture-station/src/styles/tokens/` 目录
2. 复制 (cp / git mv 不重要, 用 cp + git add OK):
   - `docs/research/visual-prototypes/PF-V/p7-output/tokens.css` → `apps/capture-station/src/styles/tokens/tokens.css`
   - `docs/research/visual-prototypes/PF-V/p7-output/density-compact.css` → `apps/capture-station/src/styles/tokens/density-compact.css`
   - `docs/research/visual-prototypes/PF-V/p7-output/type-weight-heavy.css` → `apps/capture-station/src/styles/tokens/type-weight-heavy.css`
3. 在 `src/main.tsx` 或 `src/App.tsx` import 顺序: tokens.css → density-compact.css (overlay) → type-weight-heavy.css (overlay)
4. 验证 dev server: `pnpm run dev` — 浏览器看 :root vars 生效
5. 写 `apps/capture-station/src/styles/tokens/README.md` 说明 layered overlay 顺序

**Boundary**: 只允许 :root 变量 cascade, 不允许 token 文件外硬编码 hex.

#### P2-02 icons scaffold

**Mission**: 迁 SVG sprite + 建立 Icon component.

**Steps**:
1. `apps/capture-station/src/assets/icons/` 复制 system.svg + state.svg
2. 创建 `apps/capture-station/src/components/Icon.tsx` 含 `<svg><use href={`#${id}`} /></svg>` semantic
3. 创建 `apps/capture-station/src/components/Icon.module.css` 引用 tokens
4. 验证: 至少在一个既有 feature (url-bar) 用 `<Icon name="trace" sprite="system" />` 渲染

**Boundary**: SVG path 不内联到组件, 永远从 sprite 引用.

#### P2-03 component candidate scaffold

**Mission**: 把 15 component candidate (panel-card / state-badge / sync-badge / btn / etc) 翻译成 React component.

**Steps**:
1. 对 P7 `css-modules-candidate/` 15 candidate, 每个建 `apps/capture-station/src/components/<ComponentName>/<ComponentName>.tsx + .module.css`:
   - panel-card / state-badge / sync-badge / btn / lifecycle-stepper / evidence-table / tag-list / capture-id-chip / topic-card / modal / governance-tooltip / live-pulse / frontmatter-block / promote-gate / url-input
2. 每个 component:
   - 函数组件 + typed props (TS strict)
   - 引用 tokens.css 变量, 不硬编码 hex
   - 状态修饰用 className 而非 inline style
   - 按需暴露 default prop 供 sync-badge 3 档 / state-badge 6 态等
3. 不要求每个 component 完美; 目标是骨架就绪, 后续 Phase 3 surface 用时打磨
4. **L8 sync-badge contract 必须遵守**:
   - 3 档 state: synced / pending / external-changed
   - 不允许 collapse 成 binary saved/not-saved

**Boundary**: 不引入新 styling lib. 不照抄 P7 class name 作 production naming, 但 BEM-style modifier 可保留 (`--synced` / `--pending`).

---

### Phase 3 — 13 surface TSX 翻译 (3-5 h, **14 dispatch** = 13 surface + 1 cross-consistency check)

**dispatch ID 模式**: PF-C4-01-P3-{NN}-{surface-short-name}

#### Cross-surface consistency contract (所有 13 dispatch 共同遵守)

```yaml
naming:
  feature_dir: apps/capture-station/src/features/<kebab-name>/
  component_file: <PascalName>.tsx
  module_css: <PascalName>.module.css
  prop_interface: <PascalName>Props
  state_test: __tests__/<PascalName>.test.tsx (Vitest + RTL)

token_discipline:
  - 所有颜色 ref tokens.css var
  - 8px grid spacing (var(--space-*))
  - 字体 typography (var(--type-*))

state_grammar:
  - sync-badge: synced / pending / external-changed (L8 强制)
  - state-badge: idle / loading / ready / candidate / blocked / stale
  - URL bar 5 态: empty / focus / validating / error / history-open
  - Topic Card Vault 5 态: default / aggregated / promote / modal / sync

i18n:
  - 中文 UI 文案保留 P7 原文 (P7 已对齐 LESSONS L8 跨系统 sync 中文标签)
  - 不翻译成英文

react_pattern:
  - 函数组件 only (no class)
  - hooks: useState / useMemo / useEffect 按需
  - props 严格 typed
  - default export 每个 surface 一个

testing:
  - Vitest + jsdom 已配置
  - 每 surface 至少 1 smoke test (renders without crash)
  - state-rich surface (URL bar / Topic Card Vault) 至少 3 state test

todo_placeholder_4_items (PF-V handoff §4):
  - 02-live-metadata.html L69 thumbnail: 用 <img alt="" /> placeholder + comment "// TODO P1: bind to BBDown metadata pipeline"
  - 04-trust-trace.html L21 graph: 用 <div data-todo="trust-trace-graph"> placeholder + comment "// TODO P1: D3/cytoscape decision (PF-C4-EXT)"
  - 04-trust-trace.html L40 timeline: 同上 placeholder
  - 04-trust-trace.html L64 error-path: 同上 placeholder
```

#### Phase 3 dispatch 列表 (13 surface):

| # | Surface | P7 source | apps/ target | 估时 |
|---|---|---|---|---|
| P3-00 | App Shell | `00-app-shell.html/.module.css` | `src/App.tsx` 重构 + `src/components/AppShell/` | 30 min |
| P3-01 | URL Bar | `01-url-bar.html` | `src/features/url-bar/UrlBar.tsx` (已有, 升级) | 20 min |
| P3-02 | Live Metadata | `02-live-metadata.html` | `src/features/live-metadata/LiveMetadata.tsx` | 20 min |
| P3-03 | Capture Scope | `03-capture-scope.html` | `src/features/capture-scope/CaptureScope.tsx` | 20 min |
| P3-04 | Trust Trace | `04-trust-trace.html` | `src/features/trust-trace/TrustTrace.tsx` (含 4 TODO placeholder) | 30 min |
| P3-05 | Vault Preview | `05-vault-preview.html` | `src/features/vault-preview/VaultPreview.tsx` | 20 min |
| P3-06 | Vault Commit | `06-vault-commit.html` | `src/features/vault-commit/VaultCommit.tsx` | 20 min |
| P3-07 | Topic Card Lite | `07-topic-card-lite.html` | `src/features/topic-card-preview/TopicCardLite.tsx` | 20 min |
| P3-08 | Topic Card Vault | `08-topic-card-vault.html` (含 sync-badge 3 档 L8) | `src/features/topic-card-vault/TopicCardVault.tsx` | 25 min |
| P3-09 | Signal/Hypothesis IA | `09-signal-hypothesis.html` | `src/features/signal-hypothesis/SignalHypothesis.tsx` (新 feature) | 20 min |
| P3-10 | Capture Plan IA | `10-capture-plan.html` | `src/features/capture-plan/CapturePlan.tsx` (新 feature) | 20 min |
| P3-11 | Density Spec ref | `11-density-spec.html` | `src/features/_specs/DensitySpec.tsx` (reference 页) | 15 min |
| P3-12 | Type Spec ref | `12-type-spec.html` | `src/features/_specs/TypeSpec.tsx` (reference 页) | 15 min |
| P3-CC | Cross-surface consistency check | — | 跑全 13 surface, 验 token discipline / sync-badge L8 / 8px grid / 中文文案 / TS strict 全过 | 30 min |

**每 dispatch 通用 schema**:
```yaml
input:
  - p7-output/html5-rough/<surface>.html
  - p7-output/html5-rough/<surface>.module.css
  - p7-output/html5-rough/<surface>.model.json (Step 1 ref)
  - 既有 feature TSX (如有) — 升级保留 api-client 接线
output:
  - apps/capture-station/src/features/<surface>/<Component>.tsx
  - apps/capture-station/src/features/<surface>/<Component>.module.css
  - apps/capture-station/src/features/<surface>/__tests__/<Component>.test.tsx
verification:
  - pnpm typecheck (整 capture-station 全过)
  - pnpm test (该 surface smoke test 过)
  - pnpm run build (整 capture-station build green)
verdict:
  - clear / concern (<原因>) / partial (<原因>) / reject (<原因>)
boundary:
  - 不照抄 P7 class name 作 production
  - 不引 Tailwind / shadcn
  - tokens.css 外不硬编码 hex
  - L8 sync-badge 3 档 (Topic Card Vault 必须)
amend_trigger:
  - silent_flexibility 触发: 不许偷加 vendor / runtime / migration / authority write
  - 触发 amend → 写 amend record 入 receipt + revert + 重派
```

---

### Phase 4 — Lane Closeout (30-60 min, 2 dispatch)

#### P4-01 — npm build/test full green

**Mission**: capture-station 整 lane 满足 PF-V handoff §7 acceptance criteria.

**Steps**:
1. `pnpm typecheck && pnpm lint && pnpm test && pnpm run build` 全过
2. 浏览器 `pnpm run dev` 看 13 surface 实际渲染 (至少 console no error)
3. `apps/capture-station/PF-C4-01-acceptance-checklist.md` — 写 30 项检查 (复制 PF-V handoff §7 + tick)
4. 跑 `python tools/check-docs-redlines.py` (如存在)
5. 跑 `python tools/check-secrets-redlines.py` (如存在)
6. `git diff --check`

#### P4-02 — Lane closeout receipt + CHECKPOINT

**Mission**: 写 lane 收尾 receipt + CHECKPOINT.json.

**Output**:
- `docs/research/post-frozen/PF-C4-01-lane-closeout-2026-05-07.md` — narrative receipt (≥1500 字, 含 4 phase summary + 20 dispatch verdict + cross-surface consistency check + L8 sync-badge 强制 / 4 TODO placeholder honest 等)
- `docs/research/post-frozen/PF-C4-01-CHECKPOINT.json` — schema 同 Run-3+4:
  ```json
  {
    "lane_id": "PF-C4-01",
    "execution_mode": "local_worktree_long_runner_codex",
    "phases_total": 4,
    "phases_completed": 4,
    "dispatches_total": 20,
    "dispatches_completed": 20,
    "dispatches_partial": [],
    "amend_trail": [],
    "build_green": true,
    "test_pass": true,
    "boundary_preservation_check": "clear",
    "no_runtime_unlock": "confirmed",
    "no_migration": "confirmed",
    "no_true_vault_write": "confirmed",
    "raw_vault_untouched": "confirmed",
    "tokens_css_single_source": "confirmed",
    "l8_sync_badge_3_states_in_topic_card_vault": "confirmed",
    "todo_placeholders_honest_count": 4,
    "ready_for_user_audit": "yes"
  }
  ```

## §5 PR 策略 (战友拍板)

### 选项 A — 单 PR direct merge (Run-3+4 模式, 推荐)
- 20 dispatch 全在一个 worktree branch (`codex/pf-c4-01-2026-05-07`)
- 全过 + closeout 后开 1 PR + amend_and_proceed pattern
- 用户授权后 direct merge
- 优点: 简单, 与 Run-3+4 PR #240 一致风格
- 缺点: PR 大, review 难

### 选项 B — 4 PR per phase (渐进, 备选)
- Phase 1 → PR 1 (build repair) merge
- Phase 2 → PR 2 (scaffold) merge
- Phase 3 → PR 3 (13 surface translation) merge
- Phase 4 → PR 4 (closeout) merge
- 优点: review 颗粒细
- 缺点: 4 次 amend_and_proceed 仪式累

**默认走选项 A** (除非用户在 commander prompt paste 时改). Codex 你按 A 跑.

## §6 amend_and_proceed pattern

如执行中遇到:
- silent flexibility 触发 (你偷加超出 scope 的事)
- 不可避免的 vendor 选择 (e.g. trust-trace D3 vs cytoscape, 但本 commander 已经放 placeholder, 不在本 lane 决定)
- build red 不能修复 (env / dep 真问题)

**做法**:
1. 立即停止 dispatch
2. 写 amend record 入对应 receipt: 触发条件 / 原状态 / 决定 (revert vs continue with note)
3. 推荐 revert 然后写 narrow report; 不推荐 continue
4. 写 `amend_trail[]` 入 CHECKPOINT.json
5. **per lane total ≤ 1 自主 amend** (跨 20 dispatch 累计 1 次, 不是每 phase 1 次也不是每 dispatch 1 次). 第 2 次 amend 必须停下写 receipt + 等用户授权再继续.

## §7 Self-audit (你必须跑)

每 phase closeout 跑 5 项 self-check (写入 receipt):
1. **Boundary**: write_enabled / 5 overflow / authority files / forbidden_paths 是否触碰
2. **Anti-pattern**: Tailwind / shadcn / hex 硬编码 / inline style hex 是否引入
3. **L8 sync-badge**: Topic Card Vault 是否含 3 档 state (synced / pending / external-changed)
4. **TODO placeholder honest**: 4 placeholder (thumbnail / graph / timeline / error-path) 是否标 `// TODO P1/P2:` 而不是伪实现
5. **tokens.css single source**: grep `apps/capture-station/src/**/*.module.css` 找硬编码 `#[0-9a-f]{3,6}` — 期望 0 命中

## §8 Truthful Stdout Contract (lane 收尾)

写入 `PF-C4-01-CHECKPOINT.json`:
```yaml
codex_long_runner_session: <真实 session id>
phases_completed: <真实, 期望 4/4>
dispatches_completed: <真实, 期望 20/20>
dispatches_partial: [<真实列表>]
amend_trail: [<真实记录>]
total_wall_clock_minutes: <真实, 期望 5-7h = 300-420 min>
silent_flexibility_triggers: <真实计数, 期望 0>
build_green: <true|false>
test_pass: <true|false>
typescript_strict_pass: <true|false>
lint_pass: <true|false>
boundary_preservation_check: <"clear" | "concern: <原因>">
authority_files_untouched: confirmed
raw_vault_untouched: confirmed
tokens_css_single_source: <"confirmed" | "concern: <硬编码 hex 命中数>">
l8_sync_badge_3_states_in_topic_card_vault: <"confirmed" | "missing">
todo_placeholders_honest_count: <真实, 期望 4>
ready_for_user_audit: <"yes" | "no_with_reason">
```

**禁止**: 伪造 wall-clock / 伪造 build green / 伪造 boundary preservation / 跳过 self-audit

## §9 Kill signals (立即停下)

如下任一发生立即停 + 写 kill receipt:
- 触碰 `services/api/migrations/**` 或任何 forbidden path
- 引入 BBDown live / yt-dlp / ffmpeg / ASR / browser automation runtime
- 修改 docs/PRD-*.md / SRD-*.md / decision-log.md / task-index.md / current.md / AGENTS.md
- **修改 `docs/research/post-frozen/runs/CHECKPOINT-Run*.json` 或 `EXTERNAL-AUDIT-REPORT-*.md` 等历史 ledger** (immutable, 永不写)
- 写 ~/workspace/raw/**
- 执行 `alembic revision` 或新 migration
- 任何 SQLite schema 修改进入 services/api/migrations/

写 kill receipt 入 `docs/research/post-frozen/PF-C4-01/receipts/kill-receipt-<reason>-<timestamp>.md`, 暂停, 等用户决定.

## §10 你的 worktree

- Branch: `codex/pf-c4-01-2026-05-07`
- 起点 baseline: `origin/main` (PR #241 已 merged)
- 全 commit 推到该 branch
- Phase 4 closeout 后开 PR target main, title `feat(capture-station): PF-C4-01 local frontend bootstrap + p7 reference scaffold + 13 surface TSX (20 dispatch)`

## §11 给战友 (用户) 的 paste-时 alterations

如战友想改:
- A vs B PR 策略 → 改 §5
- 加 / 减 dispatch → 改 §4
- 改 boundary → 改 §3
- 加 Hermes 三方独立外审 → 加 §12 audit-window 子段
- 改 worktree branch 名 → 改 §10

## §12 (空) — 用户授权后 paste 完整 prompt 给 Codex

战友: 这是 paste-ready prompt. 你 review + 改 (如需) + paste 给 Codex 跑通宵.

CC1 后续 audit:
- 通宵后 Codex 写完 receipt + CHECKPOINT
- CC1 (我) 跑 sniff + spot + cross-link audit (类似 16 ZIP audit 模式)
- 输出 PF-C4-01-AUDIT-REPORT.md
- 用户主审 → A (direct merge) 或 B (amend 后 merge) 或 C (reject)

---

> **File path**: `docs/research/post-frozen/PF-C4-01-codex-commander-prompt-2026-05-07.md`
> **Status**: candidate / commander_prompt / not-authority
> **Total dispatch**: **20** (P1×1 + P2×3 + P3×14 + P4×2)
> **Expected runtime**: 5-7h Codex 通宵
> **PF-V handoff PR**: #241 (merged 2026-05-07 05:47 UTC)
> **CC1 audit 16 ZIP report**: `docs/research/strategic-upgrade/2026-05-07/audit/PHASE-A-B-SUMMARY.md`
