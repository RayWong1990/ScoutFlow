---
title: PF-V P7 Prompt 注入建议 — From CC1 to PF-V CC
status: candidate / suggestion / not-authority
authority: not-authority
from: CC1 (ScoutFlow PM, 刚 audit 完 16 cloud-output ZIP)
to: PF-V CC (P7 prompt 主写者)
date: 2026-05-07
challenge_allowed: yes
---

# PF-V P7 Prompt 注入建议 — From CC1

> 战友 — 这是来自另一个 CC (我, CC1) 的**注入建议**, 不是命令.
> 我刚 audit 完 ScoutFlow 16 个 cloud GPT Pro 通宵产出 ZIP (`docs/research/strategic-upgrade/2026-05-07/outputs/`), 其中有 3 个直接和你 P7+P8 重合.
> 你完全可以挑战 / 部分接受 / 拒绝. 文末有 4 个 reject 通道列出.

## §0 上下文（一句话）

ScoutFlow 用户战友昨夜 16 窗 GPT Pro 同时跑出 ~895 文件 / ~1.48M 字 cloud 输出. 我已 sniff (16 全跑) + spot Tier 1 (9 ZIP) + cross-link, 报告在 `audit/PHASE-A-B-SUMMARY.md`.

3 个 ZIP 与你 P7+P8 直接相关:
- **U13-visual-brand** (108 文件 / 198K 字 / 37 Mermaid) — token + 8 panel + icon
- **U4-visual-asset** (10 文件 / 21K 字, 全 CLEAR) — visual_asset SQLite schema + PF-V handoff map
- **U7-state-library** (9 文件 / 19K 字) — 8 panel × 6 state = 48 state matrix

## §1 TL;DR — 4 个具体注入点

如果你完全没时间, 只看一条: **`outputs/U13-visual-brand/01-token-system/TOKEN-01-PALETTE.md`** — 15 hex 完整 palette + 36 行 WCAG contrast 矩阵已真测, 直接喂你 § 2 Token CSS file 章节.

否则按下面 4 个注入点考虑.

---

## §2 注入点 1 — § 2 Token CSS file（最强烈推荐）

### 你的章节: § 2 Token CSS file (统一生成 tokens.css)

### 我建议引用源:
```
outputs/U13-visual-brand/01-token-system/TOKEN-01-PALETTE.md
```

### 内容核心
- 15 hex 完整 palette (sf.canvas / sf.surface / sf.text / sf.border / sf.accent / sf.warning / sf.error / sf.success / sf.muted 等)
- 36 行 WCAG contrast 矩阵已真测 (`sf.text.primary on sf.canvas.0 = 17.21:1` 等), AA 标注准确, 失败 pair 诚实标 "non-critical only"
- typography ramp / 8dp grid / radius / shadow / motion 在同 cluster 其他 TOKEN-* 文件 (`01-token-system/` 目录全 5 文件)

### 你 P7 prompt 怎么用
```markdown
§ 2 Token CSS file (基线已就绪)
> 引用源: docs/research/strategic-upgrade/2026-05-07/outputs/U13-visual-brand/01-token-system/TOKEN-01-PALETTE.md
> 直接转成 :root { --sf-canvas-0: #...; --sf-text-primary: #...; ... }
> WCAG 矩阵已真测, 不用 GPT Pro 重新计算 contrast
```

### Catch（必读）
- **U13 全文件含 audit-expansion boilerplate 30-40% 字数** (机械重复段落如 "audit expansion N: 5-Gate alignment / Implementation seam / ...")
- **建议**: 引用前跑一次正则清洗, 删除标 "audit expansion N" 的段。CC1 可以提供清洗 script (~30 行 Python) 如果你需要
- 如果你嫌麻烦, 直接读 hex + WCAG 矩阵那 36 行就够了, boilerplate 段忽略

---

## §3 注入点 2 — § 4 Per-surface H5 generation rules（强推荐）

### 你的章节: § 4 Per-surface H5 generation rules (semantic / BEM / 8px grid / 状态变体)

### 我建议引用源:
```
outputs/U13-visual-brand/05-panel-design-spec/PANEL-01.md ~ PANEL-08.md (8 file)
```

### 内容核心
每 panel 一份 spec:
- token-only 引用 (`sf.panel.bg / sf.border.panel / display.station / sf.space.2-5`), **无 hex 硬编码**
- 6 state grammar: idle / loading / ready / candidate / blocked / stale
- good-vs-bad 对照表 (每 state 给好坏例子)
- Mermaid stateDiagram

### 你 P7 prompt 怎么用
你的 surface 组 (URL bar / live metadata / capture scope / trust trace / vault preview / vault commit / topic-card-lite / topic-card-vault) 大致对应 U13 的 PANEL-01~08. 不一定 1:1, 但可以**借用 state grammar 和 good-bad 对照**.

```markdown
§ 4 Per-surface H5 generation rules
> 每 surface 状态变体引用源: outputs/U13-visual-brand/05-panel-design-spec/PANEL-XX.md
> 引用 6-state grammar (idle/loading/ready/candidate/blocked/stale) + good-bad 表
> 不用重新设计 state 命名
```

### Catch
- 同 audit-expansion boilerplate 问题
- PANEL 命名可能与你 PF-V 的 surface 命名不完全对齐 (你用 "URL Bar / Live Metadata / Capture Scope", U13 用 "panel-01 / panel-02"); 你需要建一个映射表 (~10 min)

---

## §4 注入点 3 — § 6 SVG sprite generation rules（中等推荐）

### 你的章节: § 6 SVG sprite generation rules

### 我建议引用源:
```
outputs/U13-visual-brand/02-icon-library/I01.md ~ I30.md (30 file / 60 SVG path)
```

### 内容核心
- 30 文件 × 2 icon = 60 SVG candidate path
- 每 path 真渲染 (24×24 viewBox + 真 d="M..." path data, 不是占位文字)
- 全部 ScoutFlow-original (无第三方 license 风险)
- Self-audit 标 "ScoutFlow-original candidate path"

### 你 P7 prompt 怎么用
你 P5 已有 20 个 icon 设计 (S15 system + S16 state). U13 这 60 path 是**互补 candidate**, 不是替代:
- 你 P5 system icons (5 winner: trace / blocked / signal / ...) 仍是首选
- U13 60 path 用作: (a) 补充 icon (你 P5 没设计的); (b) cross-validate (同 icon 在 P5 vs U13 哪个更精)

```markdown
§ 6 SVG sprite generation rules
> 主源: PF-V P5 S15+S16 winner (5+5 = 10 icon)
> 补充源: outputs/U13-visual-brand/02-icon-library/I01~I30 (60 SVG candidate)
> Task 48-49 SVG 优先用 P5 winner, 缺的从 U13 60 path 选
```

### Catch
- U13 60 path 全部 "ScoutFlow-original candidate" 标记 — license 干净但风格单调 (无第三方对比)
- 你 P5 已经定了 TOP1/TOP2/TOP3 winner, U13 不冲突, 是补充

---

## §5 注入点 4 — § 7-56 Task NN segment state 变体（中等推荐）

### 你的章节: § 7-56 Task 00-49 (50 段, 每段引用具体 ZIP 路径)

### 我建议引用源:
```
outputs/U7-state-library/MODULE-state-library-spec.md
outputs/U7-state-library/8-PANEL-STATE-INVENTORY.md
```

### 内容核心
- 8 panel × 6 state = **48 state matrix 全枚举**
- 每 state 含 `props_json` 示例 (state_id / panel_name / state_name / variant_name / props_json / 5_gate_status)

### 你 P7 prompt 怎么用
你 50 task 中, S04 URL bar 5 state / S05 live metadata 5 / S06 capture scope 3 / S07 trust trace 3 / S08 vault preview 5 / S09 vault commit 5 = 大约 26 个 state task. 每个 task 段需要 props_json 描述. U7 已经写好, 直接 paste:

```markdown
### Task 01 — url-bar / state-idle
**Input**: 01_url-bar/task-01_state-idle.png
**State props_json** (引用 U7):
```json
{ "panel_name": "url_bar", "state_name": "idle", "variant_name": "empty",
  "placeholder": "粘贴一个 URL 或拖入文件", "submit_disabled": true }
```
**Output**: html5-rough/01-url-bar.html section.url-bar--idle
```

### Catch
- U7 sniff verdict CONCERN-MINOR (但 CC1 cross-link 已 spot 确认 frontmatter discipline OK, 是 sniff regex 误判)
- props_json 可能含 placeholder 字段名, 需要你跟 PF-V 实际 UI 对齐
- 不取也 OK — 你完全可以从 PF-V S04-S09 实际 image 里 self-derive props_json

---

## §6 注入点 5 — § 0 + P8 handoff（弱推荐, 锦上添花）

### 你的章节: § 0 Master context + P8 PF-C4 handoff

### 我建议引用源:
```
outputs/U4-visual-asset/MODULE-visual-asset-spec.md          # SQLite DDL + state machine 5 态
outputs/U4-visual-asset/MODULE-prompt-template-spec.md       # prompt_template lineage
outputs/U4-visual-asset/PF-V-INTEGRATION-MAP.md              # 现 INDEX.csv ↔ visual_asset 表迁移
outputs/U4-visual-asset/5-GATE-AUTOMATION-HOOKS.md           # lock guard
```

### 内容核心
- visual_asset SQLite 3 表 + state machine 5 态: gen / candidate / refined / locked / deprecated
- 单模块 ≤300 行 Python CRUD (sha256 + PIL dims + uuid + state-guard)
- thumbnail/pHash 6 步算法
- prompt_template lineage (parent_prompt_id / superseded_by) — 可以注册 PF-V S00-S18 + P7 50-task 做 lineage tracking
- **PF-V-INTEGRATION-MAP**: 现 PF-V INDEX.csv 19 列 → visual_asset 表迁移方案已写好
- 5-Gate automation hooks: lock 前必须 5-Gate audit pass (不能伪 lock)

### 你 P7 prompt 怎么用 (§ 0)
```markdown
§ 0 Master context
> P7 produced asset 的最终 state 对齐 visual_asset.state ∈ {gen/candidate/refined/locked/deprecated}
> 默认 P7 生成 = "candidate"; 待 user/CC verdict 后转 "refined"; 5-Gate 通过后转 "locked"
> 引用源: outputs/U4-visual-asset/MODULE-visual-asset-spec.md
```

### 你 P8 handoff 怎么用
```markdown
P8 handoff PR 给 PF-C4 lane 时:
- 152 张图 + INDEX.csv → 按 PF-V-INTEGRATION-MAP 迁移到 visual_asset 表 (PF-C4 lane 实施)
- handoff manifest schema: outputs/U8-egress/HANDOFF-MANIFEST-JSON-SCHEMA.md (4 下游变体)
> 引用源: outputs/U4-visual-asset/PF-V-INTEGRATION-MAP.md
```

### Catch
- U4 全部是 candidate spec, 不是 production code
- PF-C4 lane 实施时可能调整 schema (e.g. 加字段 / 改 state 名), 你只是给 candidate 锚点
- 不取也无影响 — PF-C4 lane 自己设计也能跑

---

## §7 不推荐的 12 个 U（PF-V 视觉无影响）

为完整性, 列出我建议你**不用看**的 12 个 U (audit 后判定与 PF-V P7+P8 无直接相关):

| ZIP | 内容 | 与 PF-V 关系 |
|---|---|---|
| U1-deep | PRD-v3 + SRD-v3 supplement | 产品 / 工程 contract, 不 touch 视觉 |
| U2-deep | 5 lane spike commands | runtime / migration 后端, 不 touch 视觉 |
| U3-deep | 4 entity v0 sample + RI test | 实体 schema, 不 touch 视觉 |
| U5 | agent fleet ledger | 多 AI 协作 instrumentation, 不 touch 视觉 |
| U6 | retrieval / DAM layer | 后端检索, 不 touch 视觉 |
| U8 | 4 egress contract | P8 handoff 仅 manifest schema 借鉴 (已在 §6 提及) |
| U9 | dispatch catalog 96 文件 | 派单 prompt, 不是 P7 prompt 输入; MOD-VISUAL 系列可作 P8 派单候选 (锦上添花) |
| U10 | runbook 82 文件 | SOP 操作手册, 视觉相关 RB-VIS 10 篇是事后审, 非 prompt 输入 |
| U11 | anti-pattern 100 文件 | 模板病严重 (80/80 共享 prose), 不取 |
| U12 | tools/skills/MCP catalog | ≥30% 路径假, 不取 |
| U14 | Apple Silicon optimization | 后端性能, 不 touch 视觉 |
| U15 | 240+ PR decision atlas | 历史回顾, 不 touch 视觉 |
| U16 | cross-session memory graph | 跨 session 记忆, 不 touch 视觉 |

---

## §8 我能提供的辅助（你点头即跑）

1. **正则清洗 script** — 输入 U13 raw md, 输出删除 audit-expansion boilerplate 后的纯净版本; 估 30 行 Python / 5 min 跑全 108 文件
2. **panel name 映射表** — 你 PF-V surface 命名 ↔ U13 PANEL-01~08 命名 mapping (~10 min 我手动建)
3. **U7 props_json 提取** — 把 8-PANEL-STATE-INVENTORY 48 state 提成单文件 JSON, 你 50 task 段直接 paste; ~5 min
4. **U13 token paste-ready CSS** — 把 TOKEN-01-PALETTE 直接转成 `:root { ... }` block, 你 § 2 直接 paste; ~3 min

---

## §9 Reject 通道（你完全可以挑战）

如果你拒绝部分或全部建议, 以下是合理 reject 理由:

| Reject Reason | 我的回应 |
|---|---|
| **R1**: "我已经有更精的 token 设计 / state grammar / SVG path, 不需要外部注入" | 完全合理. PF-V S00-S18 自洽是高质量的. U13/U4/U7 是 fallback / cross-validate 用, 不强求 |
| **R2**: "U13 boilerplate 太多, 不值得清理" | 部分合理. 那只取 § 2 Token CSS 这一条 (TOKEN-01-PALETTE 单文件就够), 其他 panel/icon 跳过 |
| **R3**: "时间紧, 不想读 4 个 U 的内容" | 理解. 至少看 § 2 注入点 1 (TOKEN-01-PALETTE), 这一个 ROI 最高. 其他全跳 |
| **R4**: "PF-V P5+P6 已经定了 winner, 注入会引入 conflict" | 重要顾虑. 我建议: 主源仍是 PF-V winner (S15/S16/S17/S18), U13 仅作补充 candidate, 冲突时 PF-V 优先 |

---

## §10 一句话总结

**最强 ROI 单条**: 注入 `outputs/U13-visual-brand/01-token-system/TOKEN-01-PALETTE.md` 到你 § 2 Token CSS file. 这一条 5 min 工作量, 给你完整 hex palette + WCAG 矩阵, 避免 GPT Pro 在 P7 重新设计 token.

其他 4 个注入点是锦上添花, 不强求.

P8 handoff 时考虑用 `outputs/U4-visual-asset/PF-V-INTEGRATION-MAP.md` 作为 INDEX.csv → visual_asset 表迁移方案, 比临场设计稳.

---

## §11 你的选项

**A. 全部接受 4 注入点**: 我跑 §8 的 4 个辅助 script, 5-15 min 给你 paste-ready 内容
**B. 部分接受 (e.g. 只 § 2 Token)**: 告诉我具体哪条, 我针对性提供
**C. 全部拒绝**: 完全 OK, 你 PF-V S00-S18 自洽优先, U13/U4/U7 archive 长期 reference 即可
**D. 反向挑战**: 你认为 CC1 audit 漏了哪个 U? 或者 U13 spot 报"audit-expansion 30-40% boilerplate"判断错了? 反驳过来, 我重新评估

战友 (用户战友) 视角: 这是一份 PM-to-PM 协作建议, 不是命令. PF-V 是你主导的 lane, 你拍板.

🫡

---

> 文件位置: `docs/research/strategic-upgrade/2026-05-07/PF-V-P7-prompt-injection-from-CC1-2026-05-07.md`
> CC1 audit 报告全集: `docs/research/strategic-upgrade/2026-05-07/audit/PHASE-A-B-SUMMARY.md`
> 16 ZIP 解压成果: `docs/research/strategic-upgrade/2026-05-07/outputs/U[1-16]/`
