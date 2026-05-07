---
title: PF-V Lane Lessons Learned (live document)
status: candidate / lessons / not-authority
created_at: 2026-05-07
purpose: Live capture of design + execution lessons during PF-V image generation. Append-only.
---

# Why this file exists

PF-V lane runs at ~5-10 min/session pace. Without a lessons-learned doc, each session's mistakes risk being forgotten by the time downstream PF-C4 lane consumes the bundle. This doc is **append-only** — every time we observe something worth carrying forward, add an entry.

# Lessons

## L1 — UI chrome 必须默认简体中文（master-context bug）

**事件**: S00 第一批 10 张图全部输出英文 UI chrome。
**根因**: 我写 master-context 时 §Realistic dummy content 段只锁了"内容"语言（视频标题 CN），没锁"UI chrome"语言。GPT Pro 默认走英文 fallback。
**修法**: master-context 加 §Language policy 段 + 完整术语对照表 + Self-verification checklist 增加 CN 检查项。
**后效**: S00 第二批起所有 sessions UI 100% CN。
**对下游影响**: 0 — EN 版本归档为 reference, 不进 P7 batch.
**预防 rule**: 任何 master-context update 后立即检查 self-verification checklist 是否覆盖。

## L2 — Vault path dummy 偏离真实系统（master-context bug）

**事件**: S08 (vault-preview) 10 张图全部用 `~/scoutflow-vault/2026-05/...md` dummy 路径，但真实路径是 `~/workspace/raw/00-Inbox/...md`（user 私人 Obsidian raw vault）。
**根因**: master-context 写 dummy 数据时虚构了 "scoutflow-vault" 路径，没用 user 实际系统的真实路径。
**修法**: master-context §Realistic dummy content 全替换为 `~/workspace/raw/00-Inbox/...` + 加 §Downstream system context 段说明 ScoutFlow 责任边界（"交付干净 markdown 到 Obsidian inbox 为止；enrich/wiki/知识飞轮在 Obsidian 内发生"）.
**后效**: S09 起所有 sessions 路径正确，且 V2 主动写出"实际入库后由 Obsidian 接管 (enrich / wiki / 知识飞轮)" tooltip — 治理边界视觉化。
**对下游影响**: S08 10 张标记 V-PASS-with-path-concern；P7 image-to-html5 阶段会从更新后 master-context 拿真路径，输出代码不受影响。
**预防 rule**: master-context 任何 dummy 数据必须基于 user 真实系统的实际路径，不许虚构。

## L3 — INDEX.csv maintenance routine 缺失（PM 失误）

**事件**: P0-S10 共 92 张图落地，但 INDEX.csv 一直是空模板。User 在 S10 后才发现并质问。
**根因**: 我跟着 user 节奏跑得快（5-10 min/session），focus 在 review/move/rename，**没建立"每 session 完成后立即填 INDEX"的 routine**。
**修法**: 一次性补完 92 行 INDEX.csv + 删除空模板 + 加 README §11 maintenance protocol 锁住每 session 完成后必做的事。
**对下游影响**: 0 — 数据没丢，只是没记录；现在 INDEX 已完整。
**预防 rule**: 每 session 出图 → review → move → rename → **填 INDEX 行** → 然后才能给下个 session prompt。中间任一步漏掉，停下来补。

## L4 — S00 axis 设计混了三类轴

**事件**: S00 prompt 我写了 10 个变体轴，但实际上是 7 个状态轴 + 1 个布局轴 + 2 个密度轴混合。User 问"10 选 1 还是状态库"时我才意识到设计含糊。
**根因**: 我没区分"挑 anchor 的 mood 探索"和"状态/密度/布局的覆盖"两个不同 session 目的。
**修法**: 接受现状（V4 当 anchor + 其他作 specialized reference）+ 在 02-image-to-image-evolution-patterns.md 里写明"如何区分这两类 session"。
**对下游影响**: 0 — 实际产出反而是意外的 state coverage 红利，省了 P4 部分 session。
**预防 rule**: 写新 session prompt 前先问 "这个 session 是为了挑 1 个 anchor，还是为了覆盖一系列状态？两者不能混。"

## L5 — Mobile/Tablet 跳过决策迟到

**事件**: S02/S03 prompt 我抄了 design-brief §4 的 desktop/tablet/mobile 三档 responsive 模式，user 直接质问"为啥要移动端？ScoutFlow 是 localhost 桌面工具"。
**根因**: 我没用脑子重新评估 design-brief 是否适合 ScoutFlow 实际场景，跟着模板做。
**修法**: 跳 S02 + S03，省 20 张图 + 40 min；同时压缩 S06 (capture scope) 和 S07 (trust trace) 从 10 张到 5 张（super anchor 已锁 stepper + graph，不需要 10 个变体探索）。
**对下游影响**: 净省 ~40 张图 / 80 min 时间 + ~$8 cost；产品保真度无损（mobile mockup 反正下游 PF-C4 不会实施）。
**预防 rule**: 每个 session 启动前问 "这条产品线真的需要这个 surface/device 吗？还是我在抄过度设计的模板？"

## L6 — Super Anchor 合成 = 关键转折点（设计决策 win）

**事件**: S01 第 5 张引入 trust trace graph 化 + 第 4 张引入 capture scope stepper，这两个是 design-brief 一直缺的元素。我建议合成 super anchor，把 graph + stepper + footer 融进 master，user 同意 Path A。
**根因**: S01 detail 变体里出现"质变型"元素（不只是 mood 微调），如果不合成会在下游每个 session 都缺这些核心视觉。
**修法**: 单独一个合成 session（4 张图作 reference），出 3 个变体（A 完整 / B 无 footer / C graph 留白），user 选 B。
**对下游影响**: super anchor 锁定后所有 P2-P3 sessions 都自动继承 graph + stepper 视觉语言，省了 S07 (trust trace) 和 S06 (capture scope) 各 5 张原本要做"graph 从无到有"探索的工作。
**预防 rule**: detail session 里出现"质变型"元素时，立刻提议合成 anchor 升级，不要让它埋在 detail 里。

## L7 — Topic Card "1 个 master 紧迫性低于 anchor"

**事件**: S04 (URL Bar) 10 个状态全 V-PASS, 我建议"不挑 1 个 master, 全留作 PF-C4 acceptance spec", user 接受。
**根因**: Component-level session 不像 anchor session, 不需要"挑 1 个调性 master", 而是"全状态覆盖给下游 implementation 当 spec"。
**修法**: 在 INDEX 用 `downstream_use=PF-C4-html-source-priority` 标记 TOP picks, 但所有 V-PASS 都进 P7 bundle。
**预防 rule**: Component / state / variant session 默认全保留 V-PASS, 不强制挑 1 个 master。

## L8 — Cross-system sync state 是新视觉契约（S11 发现）

**事件**: S11-V10 (Obsidian 同步状态) 第一次把"ScoutFlow 与 Obsidian 双向同步"视觉化为 3 档 sync badge: success 已同步 / warn 待同步 / focus 外部已改。
**根因**: 之前所有 sessions 都把 ScoutFlow / Obsidian 当独立系统设计，没专门处理"双系统数据一致性"问题。S11-V10 第一次把这个问题摆到 UI 上。
**影响**: 这个 3 档 sync badge pattern 应该 propagate 到其他 ScoutFlow 内 surface — 凡是有"本地状态 vs raw vault 状态"对比的地方都该用这个 pattern。
**未来 sessions 应用**:
- 任何 surface 若涉及与 Obsidian raw vault 的数据交互 → 使用 3 档 sync badge
- Sync badge 颜色 token 锁: accent_success (已同步) / accent_warn (待同步) / accent_focus (外部已改, 需人工裁决)
**预防 rule**: 设计跨系统交互的 surface 时，第一性问"双向同步如何视觉化"，不要只设计单向流。
**positive note**: master-context 的 §Downstream system context 段（L2 修复）已经明示 ScoutFlow / Obsidian 边界，S11 是该原则的视觉化具象，证明 master-context 设计正确。

## L9 — P4 states matrix 跳过决策（pending → resolved）

**事件**: P3 完成后评估 P4 (S13 state matrix grid + S14 lifecycle visualization) 必要性。
**根因**: P2-P3 总共 80 张图已经把所有 state 类型覆盖完: idle/loading/ready/error/blocked/disabled/active/empty/success 都有 V-PASS 版本，且分散在各 surface 的实际语境里 (URL Bar 有 URL 错误态, Vault Preview 有写禁用态, Topic Card Vault 有空过滤态等)。
**修法**: 跳过 P4 (S13 + S14)，省 20 张图 + ~25 min。在 INDEX 标 P4=skipped, README PM 表标删除线 + 注 "covered in P2/P3"。
**对下游影响**: 0 — PF-C4 实施 component 时按 surface 查 state spec 比"通用 state cheat sheet"更精准。Lifecycle 故事在 S06-V1/V2/V3/V4 stepper + S04 success cascade 都有。
**预防 rule**: 设计 cross-cutting cheat-sheet session 前先 audit 已有素材，confirm 增量价值 ≥ session 成本。
**残留风险**: 未来若需要"全状态总览图"作 designer onboarding 资产，可临时补 1 session 5 张（不需 10 张）。

## L10 — caption-as-spec = audit 0 误差（派单技巧 win）

**事件**: S17 (density) + S18 (typography) 各 10 张 variant，每张右下角 caption 强制标完整 spec（e.g., "Density: V3 Compact" / "Type: V4 Weight Heavy / hero 28/800 / title 20/700 / body 14/400"）。
**根因**: 之前 S15/S16 icons 只在 caption 标 variant 名（"焦距 (focus)"），UUID → V 映射靠我用眼对 — 偶尔会犹豫 (S15-V5 blocked vs S16-V5 blocked 是不同 mood，需读图对比)。
**修法**: S17+S18 prompt 里强制 caption 必须含 spec（hero/title/body 字号+weight，或 density tier name）。
**后效**: S17/S18 各 10 张 UUID → V 映射 0 错误 0 犹豫，省 ~5 min/session cross-check 时间。GPT Pro thinking mode 100% 遵守。
**对下游影响**: 0 副作用 — caption 是图外的 metadata，不影响 PF-C4 实施时的视觉。
**预防 rule**: 任何"梯度/光谱/矩阵"类 session（V1-V10 都基于同一 anchor 改一个 axis）prompt 里强制 caption 标完整 spec。变体差异越细微（如 letter-spacing -2% vs +5%），caption-as-spec 越关键。

## L11 — 正交维度梯度 session = 二维矩阵参考（设计方法 win）

**事件**: S17 density × S18 typography 都是基于 SUPER-ANCHOR-FINAL 的"单 axis 梯度"，IA/调色板/dummy data 全部不变。
**根因**: P5 之前的 sessions（S04-S12）混了多个 axis（state + variant + bias），下游 PF-C4 拿到 50 张 mockup 难以形成"组合矩阵"参考。S17/S18 强制单 axis，让 PF-C4 实施时能正交叠加（"我要 V3 density × V4 weight" = 直接可拼）。
**后效**: 下游交付物从"mockup 库"升级为"二维矩阵 spec"（density 10 档 × typography 10 档 = 100 个组合潜在配置）。
**对下游影响**: PF-C4 实施时 toggle 切换更精准，不需要从 50 张图里"找最像的"，而是直接"density=V3 + type=V4"组装。
**预防 rule**: 任何 refinement/精修类 session 都用单 axis spectrum，不许混 axis。Component/state 类 session 才允许多 axis。

## L12 — P7 一次出齐零返修（GPT Pro batch image-to-HTML5 工作流验证）

**事件**: P7 batch（65 task / 76 输出文件）在 GPT Pro thinking mode 中约 25 min 一次出齐，CC0 audit 判定 V-PASS，0 个需要 delta correction 的反模式。实际输出包括 13 个 surface HTML、13 个 surface CSS、13 个 structural model JSON、15 组 component candidate、2 个 SVG sprite、`tokens.css`、`density-compact.css`、`type-weight-heavy.css`、`MAPPING.md` 与 `README.md`。
**根因**: prompt v2 的三个设计共同作用。第一，三步 pipeline 强制 image → JSON structural model → HTML5 → component extraction，中间模型让模型先结构化再写代码。第二，`tokens.css` 关键 schema paste-ready 写进 prompt，颜色、字号、间距、圆角和阴影不让 LLM 自创。第三，65 task 段引用具体 ZIP 文件名并一一对应目标输出，减少 batch 歧义。
**修法**: P7 不再要求模型自由综合，而是把结构、token、文件映射、TODO placeholder 策略和 anti-pattern 全部前置。复杂图谱、时间轴、缩略图与后端接线不伪造，用 `<!-- TODO -->` 明确留给 PF-C4。
**后效**: P7 从预估 1-2h 压缩到实测约 25 min；CC0 audit 时间从预估约 30 min 降到约 10 min，因为没有 Tailwind、inline hex、英文 UI chrome、路径漂移或 runtime import 这类需要返修的 delta。
**对下游影响**: 0 负担。PF-C4 lane 收到的是已 V-PASS 的干净 wireframe reference；TODO 已按文件和行号枚举，不会误导为已接线功能。更重要的是，PF-C4 不需要花时间清理 Tailwind class、英文 UI、错误路径或 token drift，可以把第一轮精力放在本地前端 skeleton 与真实数据接线。
**预防 rule**: 任何 batch 转码 / 综合产出类 prompt，强制三步 pipeline + paste-ready 关键 schema + 1-to-1 file mapping。不要让 LLM 自由发挥关键 schema，也不要让模型伪造动态数据接线。若任务规模超过 20 个文件，必须提供 output manifest 或 mapping table，让 audit 可以按文件逐项核对。

## L13 — caption-as-spec + 二维矩阵 spec 都在 P7 实战印证（LESSONS L10/L11 升级）

**事件**: S17 density × S18 typography 各 10 张梯度图使用 caption-as-spec 设计，并在 P7 中落成单独 H5 reference 与 additive override CSS。PF-C4 现在可正交叠加 density V1-V10 与 typography V1-V10，形成 100 个潜在配置组合；推荐 baseline 是 density V3 Compact + typography V4 Weight Heavy。
**根因**: L10 的 caption-as-spec 让细微变体在 audit 时零歧义；L11 的单 axis 梯度让 density 与 typography 不互相污染。P7 prompt 把 V3 Compact 与 V4 Heavy 明确生成 `11-density-spec.html`、`12-type-spec.html`、`density-compact.css` 与 `type-weight-heavy.css`，因此 PF-C4 切换 toggle 可以直接 import override layer，而不是改 IA 或重写组件。
**修法**: 对"轴梯度 + 基线 + override layer"的 refinement，继续保持单 axis 设计。密度只改 spacing/type size 相关变量，字重只改 font-weight/type mono 相关变量；两者都叠在 `tokens.css` 后面，不写进单个组件。
**后效**: PF-C4 实施 density / typography 切换时是配置组合，不是视觉重做。未来如果用户要求更紧凑或更重字重，PF-C4 可先调整 token layer，再验证 surface 渲染，而不是从 20 张图里人工挑"最像"的样式。
**对下游影响**: 正向影响。PF-C4 的初始 baseline 更清晰：V3 Compact 适合高频本地操作员日常视图；V4 Weight Heavy 提供更强 workstation 语气。两者均已在 P7 output 中有文件证据，而且两个 override file 的变量范围很小，方便 PF-C4 在复制后做 lossless diff。
**预防 rule**: 任何"轴梯度 + 基线 + override layer"模式都走这条路；不要让 PF-C4 通过 prop drilling 切换 token，也不要把多个 refinement axis 混进同一个 session 或同一个 override file。

# Pending lessons (待观察 — P7/P8 已完成不再适用)

- ~~L12: P7 (image→H5 batch) 50 张 bundle 实测能否 1 次出齐？~~ → 已实证 L12（25 min one-shot V-PASS）
- ~~L13: 后续 surfaces 应用 L8 sync badge pattern 是否需要 master-context 加 §Cross-system Sync 规约段？~~ → 见上方正式 L13 + handoff §6 已固化 sync semantic 合同
