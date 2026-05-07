---
title: PF-V Visual Prototype Lane — Master Plan + Operating Manual
status: candidate / lane_plan / complete-handed-off / not-authority / not-implementation-approval
created_at: 2026-05-06
parent_strategy: docs/research/repairs/opendesign-reuse-strategy-candidate-2026-05-05.md
parent_brief: docs/visual/h5-capture-station/design-brief.md
token_source: docs/research/prototypes/h5-design-tokens-extraction-2026-05-05.md
target_models:
  generation: gpt-image-2 (OpenAI ChatGPT Pro web, thinking mode)
  vectorization_fallback: nano-banana-pro / SVGMaker / Vectorizer.AI
  image_to_code: GPT Pro 同 session（50 张 bundle）
runtime_approval: not-approved
package_approval: not-approved
parallel_with: Run-3 PF-C1 (proof pair)
downstream_consumer: PF-C4-01 / PF-C4-05 (controlled hardening)
estimated_total_images: ~180
estimated_user_time: 3-4 hours
---

# PF-V Visual Prototype Lane

> **What this is**: A parallel lane that produces L3 visual reference candidates (per OpenDesign reuse strategy) using `gpt-image-2` for ScoutFlow's H5 Capture Station. Output: ~180 mockup images + ~15 rough HTML5 files + ~30 SVG icons + 1 generation index + 1 handoff doc.
>
> **What this is NOT**: An implementation approval. An IA rewrite. A package adoption. A migration. A runtime change. An authority change.
>
> **Where it sits**: Parallel to Run-3 PF-C1 (real-URL proof pair). Feeds PF-C4-01 / PF-C4-05 visual hardening downstream.

## 0. 入口 — 文件清单 + 使用顺序

```
docs/research/visual-prototypes/PF-V/
├── README.md                          ← 你在这里。先读这个
├── 00-master-context.md               ← 每次 GPT Pro 新 session 第一条贴这个 (含 §Language policy + §Downstream system context Obsidian 飞轮边界)
├── 01-session-prompts-P0-to-P6.md     ← 18 session prompt 模板 (S02/S03 已标跳过)
├── 02-image-to-image-evolution-patterns.md  ← 演化句式（winner 精修用）
├── 03-P7-batch-image-to-html5-prompt.md ← P7 收尾：50-image bundle → N H5 + 2N 组件
├── 04-INDEX.csv                       ← ★ 实时索引 (每图 19 字段 verdict + downstream_use)
├── 04-INDEX-schema.md                 ← 索引表字段说明
├── 05-HANDOFF-to-PF-C4-protocol.md    ← P8 流水线交接协议
├── 99-self-check-and-verdict.md       ← V-PASS / V-CONCERN / V-REJECT 协议
├── LESSONS-LEARNED.md                 ← ★ 活档案 (语言/路径/PM/anchor 合成等关键教训)
├── MAINTENANCE-PROTOCOL.md            ← ★ CC0 每 session 必跑的 7 步 checklist
└── (生成阶段产出)
    ├── images-P0-EN-reference/        ← S00 EN 反例归档 (10 张, archive-only)
    ├── images-P0/                     ← S00 CN (10 张) + Super Anchor FINAL + A archive
    ├── images-P1-desktop/             ← S01 (10 张)
    ├── images-P2-url-bar/             ← S04 (10 张)
    ├── images-P2-live-metadata/       ← S05 (10 张)
    ├── images-P2-capture-scope/       ← S06 (5 张)
    ├── images-P2-trust-trace/         ← S07 (5 张)
    ├── images-P2-vault-preview/       ← S08 (10 张, V-PASS-with-path-concern)
    ├── images-P2-vault-commit/        ← S09 (10 张, knowledge flywheel boundary 已视觉化)
    ├── images-P3-topic-card-lite/     ← S10 (10 张)
    ├── (待生成) images-P3-topic-card-vault/  ← S11
    ├── (待生成) images-P3-signal-hypothesis-ia/ + images-P3-capture-plan-ia/  ← S12
    ├── (待生成) images-P4-states/ + images-P4-lifecycle/  ← S13/S14
    ├── (待生成) images-P5-icons-system/ + images-P5-icons-state/  ← S15/S16
    ├── (P7 输出) html5-rough/                   ← rough HTML5
    ├── (P7 输出) css-modules-candidate/         ← CSS Modules
    └── (P7 输出) icons-svg/                     ← 矢量化 icons
```

## 1. PM 总表 — 实时进度（CRITICAL DECISION: 跳过 S02 mobile + S03 tablet, ScoutFlow 是 localhost 桌面工具）

| Phase | Sessions | Images | 状态 | TOP 关键资产 |
|---|---|---|---|---|
| **P0 Bootstrap** | S00 (CN+EN) + Merge | 10+10+2+1 = 23 | ✅ 完成 | `pfv-SUPER-ANCHOR-FINAL-cn` (master anchor LOCKED) |
| **P1 Foundation desktop** | S01 | 10 | ✅ 完成 | S01-V5 graph + S01-V4 stepper 已并入 super anchor |
| ~~P1-mobile S02~~ | ~~10~~ | — | ❌ **跳过** (localhost 桌面工具，移动端无真实用例) |
| ~~P1-tablet S03~~ | ~~10~~ | — | ❌ **跳过** (同上) |
| **P2 Panel Detail** | S04 / S05 / S06 / S07 / S08 / S09 | 10+10+5+5+10+10 = 50 (S07 缺 1 张) | ✅ 完成 | TOP1: S04-V9 history / S05-V7 live counter / S06-V5 governance tooltip / S07-V3 time-axis / S08-V3 ready / S09-V2 knowledge-flywheel |
| **P3 Extended** | S10 / S11 / S12 | 10+10+10 = 30 | ✅ 完成 | S10-V2 video topic card / S10-V7 evidence pointers / S11-V7 promote-readiness gate / S11-V10 Obsidian sync badge (cross-system pattern) / S11-V5 source URL aggregation / S12-V8 plan dry-run automation / S12-V3 hypothesis 量化 confidence% / S12-V4 signal lifecycle stepper |
| ~~P4 States~~ | ~~S13 / S14~~ | — | ❌ **跳过 (重复度高，covered in P2/P3)** | (states + lifecycle 已分散覆盖于 S04/S05/S06/S07/S08/S09/S11) |
| **P5 Icons** | S15 ✅ / S16 ✅ | 20/20 | ✅ 完成 | S15 system: V9 trace / V5 blocked / V6 signal — S16 state: V7 focus / V1 live / V8 loading — 双套 P7 矢量化友好 |
| **P6 Refinement** | S17 ✅ / S18 ✅ | 20/20 | ✅ 完成 | S17 density: V3 Compact / V8 Mixed Dense / V4 Dense — S18 type: V1 Default (基线) / V4 Weight Heavy (生产推荐) / V6 Mono Emphasis (machine-truth) |
| **P7 image→H5** | 1 batch | 65 image tasks → 76 output files | ✅ 完成 | GPT Pro thinking mode 25 min 一次出齐；13 H5 + 13 surface CSS + 13 JSON model + 15 component pairs + 2 SVG sprite + `tokens.css` / density / type overrides；CC0 audit V-PASS 0 返修 |
| **P8 Handoff** | — | 6 markdown handoff files | ✅ 完成 | `05-HANDOFF-to-PF-C4-protocol.md` v1 + PR body + README patch + LESSONS L12/L13 patch + 30-item acceptance checklist + changelog row |

**当前已落: 152 张图 / 16 sessions / P7 76-file rough HTML5 bundle / P8 6-file handoff bundle**
**剩余: 全部完成 ✅ — 总耗时 ~210 min user 时间 / ~3.5h**

详细每图 verdict 见 `04-INDEX.csv`（152 行 19 列完整数据，TOP picks 字段 `downstream_use=PF-C4-html-source-priority` 或 `PF-C4-svg-source-priority` 标记）

## 2. 三件套结构

```
┌────────────────────────────────────────────────────────────┐
│ PF-V Lane Output Trio                                       │
├────────────────────────────────────────────────────────────┤
│                                                              │
│  Prompt Library                  Generation Output           │
│  ─────────────────              ─────────────────           │
│  00-master-context.md           images-P0/ ~ images-P6/     │
│  01-session-prompts ×18         html5-rough/                │
│  02-evolution-patterns          css-modules-candidate/      │
│  03-P7-batch-prompt             icons-svg/                  │
│                                                              │
│  Generation Index                Handoff Bundle              │
│  ─────────────────              ─────────────────           │
│  04-INDEX-template.csv          05-HANDOFF-to-PF-C4.md      │
│  04-INDEX-schema.md             99-self-check-verdict.md    │
│                                                              │
└────────────────────────────────────────────────────────────┘
```

## 3. Parallel non-interference 设计

PF-V 完全独立于 Run-3 PF-C1（Real-URL Topic-Card Proof）：

| 维度 | PF-V | Run-3 PF-C1 | 隔离点 |
|---|---|---|---|
| Worktree | 主仓库 docs/ 子目录 | 各 codex/run3-* worktree | 不同分支 |
| Branch | 暂存本地，批量 PR | 多分支 | 不冲突 |
| Files | docs/research/visual-prototypes/PF-V/** | services/api/** + tests/** | 路径不相交 |
| Authority | 不动 design-brief.md / current.md | 不动 | 都不碰 authority |
| Token budget | GPT Pro 网页（你说无限） | Codex CLI 调用 | 独立 |
| Critical path | 不阻塞 PF-C1 | 不阻塞 PF-V | 完全并行 |

PF-V 完成 **不依赖** PF-C1 verdict（视觉证据可先于真 URL proof）。但 PF-V handoff 给 PF-C4 时，C4 实施会 **同时引用** PF-C1 verdict + PF-V mockup。

## 4. 三个 Hard Gate（不许跳）

### Gate G1 — P0 master anchor 必须 V-PASS

S00 出 10 张后，你 review，**至少 1 张 V-PASS**（调性对、5-Gate 全过）。否则不许进 P1 — 因为整套图的视觉语言会从 anchor 继承。

### Gate G2 — 每 phase 出完后立即更新 INDEX.csv

不积压。一个 phase 出完 → 索引表当场填行。否则 18 sessions 后回看会丢失谱系。

### Gate G3 — 图永远不上 main，全在 docs/research/visual-prototypes/

P0-P7 阶段 0 个 PR，全在本地工作树。**P8 之后** 一次性批量 PR（`docs(post-frozen): land PF-V visual prototype reference bundle`），frontmatter 全为 `candidate / visual_reference / not-implementation-approval`。

下游 PF-C4 lane 接管前，**任何图都不许被引用为 implementation source**。

## 5. 5-Gate 视觉硬验收（每图、每 H5 都要过）

来自全局 `~/.claude/rules/aesthetic-first-principles.md`，移植到本 lane：

1. **视觉层级**：URL Bar 是首要 scan 停留点（accent_live 高对比）；Trust Trace 视觉重量足够但不抢戏
2. **空间对齐**：8px grid 严守；text + icon baseline 对齐
3. **遮挡安全**：无 popup / scroll bar / 系统手势条压关键 ID / metadata
4. **字体可读**：主标题 ≥ 20px；正文 ≥ 4.5:1 对比；中英混排不错位
5. **视觉重量**：accent_live 一屏 ≤ 2 处；blocked layer 视觉降级但仍可见

每个 session prompt 末尾都嵌入这 5 条 self-check。每个 P7 H5 输出也要过这 5 条。

## 6. 接管协议预览（详见 05-HANDOFF）

```
PF-V output                      ─────►       PF-C4 input
─────────────                                  ─────────────
html5-rough/*.html              ─────►        作为 wireframe，转 React TSX
css-modules-candidate/*.css     ─────►        作为 token 引用样板，转 CSS Modules
icons-svg/*.svg                 ─────►        作为 icon source，import 到 components/icons/
INDEX.csv                       ─────►        作为 surface ↔ file 映射 + V-verdict
images-P0~P6/*.png              ─────►        仅 visual evidence，NOT implementation source
```

**接管后 PF-V 锁定**：state = `closed_with_handoff_to_PF-C4`，不再 regen，不再 evolve。后续视觉问题走 PF-C4-03 human visual verdict 通道。

## 7. 立即开始路径（你的 next 5 个动作）

1. **打开 GPT Pro 网页**，开新 session
2. **复制 `00-master-context.md` 全文** 贴第一条（thinking mode 自动 on）
3. **复制 `01-session-prompts-P0-to-P6.md` 里的 S00 prompt**，贴第二条
4. GPT Pro 出 10 张 → 你 review → 选 V-PASS winner → 在 `04-INDEX-template.csv` 填 1 行
5. 进 S01 — 把 winner 图（image-to-image 起点）+ S01 prompt 一起喂

Iteration 节奏：S00 → review → S01 → review → ... → S18。每次 5-10 min。

P7 触发条件：S00-S18 全过 V-PASS（或 V-CONCERN 但你接受）。打包 50 张图（按 INDEX 选 high-priority surfaces）→ 喂 `03-P7-batch-image-to-html5-prompt.md` 全文 → 收 zip → 解压到 `html5-rough/` `css-modules-candidate/` `icons-svg/`。

## 8. 已知风险 + Mitigation

| 风险 | Mitigation |
|---|---|
| GPT Pro 长 session 会"健忘"（context 漂移） | 每 3-5 sessions 重新贴 master-context；每 session 都引用 token 名而不是 hex |
| 文本生成精度 95-99% 但仍可能错（中英混排） | 在 prompt 显式列要渲染的 exact strings；review 时第一眼检查文本 |
| 图生图演化会偏离原始调性 | S00 anchor 锁定后，所有 image-to-image 都引用 anchor，不引用中间结果 |
| P7 50-image bundle 一次出 → 输出体积大 / 切片错 | 在 P7 prompt 里强制"按 surface 分组输出"，每 surface 独立 zip 子目录 |
| 5-Gate 视觉验收主观偏差 | self-check checklist 7 条具象问题，不留含糊空间 |
| 下游 PF-C4 lane 误把 PNG 当 implementation source | HANDOFF doc 显式 list "NOT implementation source" 项，加 INDEX.csv `forbidden_use` 列 |

## 9. 不在本 lane 做的事（边界守护）

- ❌ 安装任何 npm 包（Tailwind / shadcn / Panda 全不装）
- ❌ 修改 design-brief.md / current.md / decision-log.md（authority）
- ❌ 写 React / TSX 实现代码（H5 是 wireframe HTML，不是 production）
- ❌ 改 apps/capture-station/src/** 任何文件（implementation in PF-C4）
- ❌ 改 services/api/** / tests/** （这是 Run-3 PF-C1 的事）
- ❌ 创建 PR 直到 P8 完成
- ❌ 让任何 image / H5 升级为 approved IA

## 10. 完成判定（lane closeout）

PF-V 视为 closed_with_handoff 当且仅当：

- [ ] S00-S18 全部 sessions 在 INDEX.csv 有记录
- [ ] 每 session 至少 1 张 V-PASS 或显式 V-CONCERN 接受
- [ ] P7 输出 ≥ 12 个 H5 surface 文件 + ≥ 24 个 component 文件
- [ ] INDEX.csv 每行 verdict 字段非空
- [ ] HANDOFF-to-PF-C4 doc 列出全部 `accepted_files` + `not_accepted_files`
- [ ] 1 个 PR 把 docs/research/visual-prototypes/PF-V/** 全量 land 到 main
- [ ] PR body 显式声明 `not-implementation-approval / not-IA-override`
- [ ] PR 4-D sub-agent 独立审过（authority / redline / frontmatter / handoff completeness）

完成后 lane state → `closed_with_handoff_to_PF-C4` lock。后续视觉问题走 PF-C4-03 通道。

## 11. 一句话总结

**用 gpt-image-2 出 180 张工作站调性 mockup（3-4h）→ 50 图压缩包丢 GPT Pro 出 H5/CSS/SVG 半成品（1.5h）→ INDEX 索引 + HANDOFF 协议交给 PF-C4 lane 实施（15min）。全程不动 authority、不装包、不改 production code。**

## 13. P7+P8 收尾总结

PF-V lane 已完成 P0-P8：152 张 mockup PNG、16 sessions、总用户时间约 ~210 min / ~3.5h。最终净产出包括 152-row / 19-column `04-INDEX.csv`、P7 `p7-output/` 76-file rough HTML5 bundle、P8 `05-HANDOFF-to-PF-C4-protocol.md` v1、README/LESSONS patch、30-item `06-ACCEPTANCE-CHECKLIST.md` 与 changelog row。

P7 的关键结果是一次出齐零返修：65 个 image task 在 GPT Pro thinking mode 中约 25 min 生成完整 `p7-output/`，CC0 audit 为 V-PASS。关键设计因子有三项：第一，token discipline，把 `tokens.css` 关键变量 paste-ready 写入 prompt，避免模型自创颜色；第二，三步 pipeline，强制 image → JSON structural model → HTML5 → component extraction，中间模型可自检；第三，1-to-1 file mapping，65 个 task 明确对应 ZIP 文件名与目标输出，避免 batch 任务歧义。P7 还保留 TODO placeholder，不伪造 graph、timeline、thumbnail 或真实后端接线。

P8 的关键结果是把 PF-V 从 research lane 正式交给 PF-C4-01 Local Frontend Bootstrap。移交链为：PF-V 提供 visual evidence、INDEX、P7 rough wireframe、token discipline、LESSONS 与 handoff contract；PF-C4-01 自己编写 React TSX、CSS Modules、data wiring 与后续 PR。PF-V 不再 regen、不再 evolve，后续视觉/实现问题由 PF-C4 initiated changes 承接。

文件指针：
- `p7-output/` — P7 76-file rough HTML5/CSS/SVG reference bundle，PF-C4 的 primary structure reference
- `05-HANDOFF-to-PF-C4-protocol.md` — P8 v1 handoff contract，supersedes v0 candidate
- `06-ACCEPTANCE-CHECKLIST.md` — PF-C4 接收 handoff 时的 30-item audit pass

---

下一步 → PF-V lane 已 closed_with_handoff_to_PF-C4。后续由 PF-C4-01 Local Frontend Bootstrap lane 接管。
