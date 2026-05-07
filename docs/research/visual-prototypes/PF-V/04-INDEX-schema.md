---
title: PF-V Generation Index — Schema Reference
status: candidate / index_schema / not-authority
created_at: 2026-05-06
purpose: Field definitions for 04-INDEX-template.csv. Open this when filling rows.
---

# 索引表用法

每生成 1 张图（or 1 个 P7 输出文件），在 `04-INDEX-template.csv` 加 1 行。

CSV 字段顺序如下，全部非可空（除标记可空字段）。

# 字段表

| 列名 | 类型 | 必填 | 说明 | 示例 |
|---|---|---|---|---|
| `pfv_id` | string | yes | PF-V 全局唯一 ID。格式：`pfv-S{session}-{img_num_in_session}{-evo-{pattern}}?` | `pfv-S00-03` 或 `pfv-S04-07-evo-A` |
| `phase` | enum | yes | 生成所属 phase，P0-P8 之一 | `P0` / `P2` / `P7` |
| `session` | string | yes | session ID (S00-S18) 或 P7 (`P7-batch`) 或 P8 (`P8-handoff`) | `S04` / `P7-batch` |
| `surface` | string | yes | 描述哪个 surface（用 surface 列表里的 canonical 名） | `capture-station-desktop` / `url-bar` / `topic-card-lite` |
| `variant_axis` | string | yes | 这张图在 session 内是 axis 第几位（1-10）+ 简述 | `3-pasted-unverified` / `7-history-dropdown-open` |
| `state_shown` | enum | yes | 图里展示的 state | `idle` / `loading` / `ready` / `error` / `blocked` / `disabled` / `mixed` |
| `device` | enum | yes | 设备视口 | `desktop` / `mobile` / `tablet` / `icon-grid` / `multi-state-grid` |
| `aspect_ratio` | enum | yes | 长宽比 | `16:9` / `9:16` / `4:3` / `1:1` / `21:9` |
| `parent_id` | string | no | 若是 image-to-image 演化，填 base 的 pfv_id；否则空 | `pfv-S00-05` |
| `evolution_pattern` | enum | no | 若是演化，填 Pattern 字母 A-J；否则空 | `A` / `C` / `E` |
| `delta_axis` | string | no | 演化具体改了哪个 axis | `density-decrease-15pct` / `mono-font-correction` |
| `v_verdict` | enum | yes | 你审完的裁决 | `V-PASS` / `V-CONCERN` / `V-REJECT` |
| `v_5gate` | string | yes | 5-Gate 检查结果（5 字符串，逐个 `P`/`F`） | `PPPPP`（全过）/ `PPFPP`（第 3 项 occlusion fail） |
| `feedback_note` | string | no | V-CONCERN / V-REJECT 时简述哪里不对 | `accent_live appears 5 times in single panel`/`text 中文标点错位` |
| `local_path` | string | yes | 文件本地路径 | `images-P0/pfv-S00-03.png` / `html5-rough/url-bar-states.html` |
| `created_at_utc` | string | yes | ISO timestamp UTC | `2026-05-06T14:32:00Z` |
| `downstream_use` | enum | no | P8 决定该 artifact 给下游谁用 | `PF-C4-01-html-source` / `PF-C4-05-visual-evidence` / `not-accepted` / `pending-review` |
| `forbidden_use` | string | no | 显式禁止下游怎么用 | `not-implementation-source` / `not-IA-override` / `reference-only` |
| `notes` | string | no | 任何额外信息 | `winner of S04, recommended for P7 bundle` |

# 完整字段示例（CSV 一行）

```
pfv-S00-03,P0,S00,capture-station-desktop,3-metadata-loaded,ready,desktop,16:9,,,,,V-PASS,PPPPP,,images-P0/pfv-S00-03.png,2026-05-06T14:32:00Z,PF-C4-01-html-source,not-implementation-source,master anchor candidate
```

# Verdict 三档语义

## V-PASS
- 5-Gate 全过（5 P）
- 0 anti-pattern 出现
- token palette 准确（不漂）
- 文本渲染正确（中英混排无错位）
- 调性符合 master anchor (S00 winner)

→ 进入 P7 候选池

## V-CONCERN
- 5-Gate 4 项过 1 项不过 OR 5 项弱过
- 0 anti-pattern
- 有 1-2 个可修复的轻微瑕疵
- 调性大体对

→ 走 image-to-image evolution（Pattern A-I）尝试修复 → 修后再 verdict
→ 如果修复后仍 V-CONCERN，可以接受为"次选 V-PASS"（标记 `v_verdict=V-PASS-with-concern`）进 P7 候选池
→ 但**不许**作为 master anchor 使用

## V-REJECT
- 5-Gate 3 项以下过 OR 任一 anti-pattern 出现
- 文本严重错位 / 文字损坏
- 调性根本错（不是 operator workstation）

→ 不进 P7 候选池
→ 不要 image-to-image 演化（基础不行，演化只会更糟）
→ 如果整 session 全 V-REJECT，重发 session prompt（可能 master anchor 漂了）

# Pattern 字母对应表（见 02-image-to-image-evolution-patterns.md）

- `A`: 单轴密度调整
- `B`: 字体精度修复
- `C`: 色彩 accent 节制
- `D`: 单元素替换
- `E`: 状态变体生成
- `F`: anti-pattern 修正
- `G`: 长宽比适配
- `H`: 跨 surface mood lock（meta，不出图）
- `I`: 失败恢复
- `J`: forensic 色彩验证（meta，不出图）

# Surface canonical 名表

P7 batch prompt 也用这套名字，保持一致：

```
capture-station-desktop
capture-station-mobile
capture-station-tablet
url-bar
live-metadata
capture-scope
trust-trace
vault-preview
vault-commit-dry-run
topic-card-lite
topic-card-vault
signal-hypothesis-ia
capture-plan-ia
state-matrix
lifecycle-flow
icons-system-grid
icons-state-grid
```

# 索引表 review 节奏

- 每 session 完成立即填行（不积压超过 1 phase）
- 每 phase 完成 → 跑 1 次 verdict 分布检查（V-PASS 数量 / V-CONCERN 数量 / V-REJECT 数量）
- P5 完成（S15-S16）→ 跑一次全索引 audit：每个 surface 是否至少 1 V-PASS？是则继续 P6；否则 fill the gap
- P6 完成 → 锁定 P7 bundle（标记每 surface 1-3 个 P7 候选 in `notes` 字段）
- P7 完成 → 给每个 P7 输出 file 加 1 行索引（`local_path` = `html5-rough/...html`），verdict 这次按 "下游可用性" 评（不是视觉，是结构）
- P8 → fill `downstream_use` 列，把 INDEX 一起 PR

# 一个反例

错误示范（不要这样填）：
```
pfv-S04-07,P2,S04,UrlBar,paste error state,error,desktop,16:9,,,,V-PASS,GOOD,fine,images/img7.png,now,,,
```

问题：
- `state_shown` 写自由文本而不是 enum
- `v_5gate` 写 GOOD 而不是 5 字符 P/F 编码
- `feedback_note` 写 fine 没意义
- `local_path` 不规范
- `created_at_utc` 不是 ISO 格式

正确示范：
```
pfv-S04-07,P2,S04,url-bar,7-success-capture-id,ready,desktop,21:9,,,,V-PASS,PPPPP,,images-P2/pfv-S04-07.png,2026-05-06T15:14:00Z,PF-C4-01-html-source,not-implementation-source,success state cleanly rendered, capture_id chip mono correct
```

字段精确度直接影响 P7 bundle 选图 + P8 handoff 文档的可读性。
