---
title: Spot Check — U13-visual-brand
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Spot Check — U13-visual-brand

## §1 文件抽样
README + SELF-AUDIT-25-FINDINGS + MASTER-BRAND-ATLAS + 3 random (TOKEN-01-PALETTE / I01-capture-start-icons / PANEL-04-trust-trace) + GATE-04-typography 抽看.

## §2 Icon SVG / WCAG / 字体 license / 5-Gate / 8 Panel
- **Icon SVG**: I01 给两个 24×24 viewBox + 真 path data (`M4 5H20V19H4Z M7 8H17 ...`) — **真渲染** 而非占位文字. 但 30 文件 × 2 icon = 60 candidate, **全部 self-audit 标 "ScoutFlow-original candidate path"**, 无第三方对比 — license 真合规但单调
- **WCAG**: TOKEN-01 内联 36 行 contrast 矩阵 (`sf.text.primary on sf.canvas.0 = 17.21:1` etc.) — 真测每对, AA 标注准确. `sf.text.muted` on `panel.bg.raised` 3.78:1 诚实标 "non-critical only / fail for body"
- **字体 license**: BRAND-VOICE 提及 "OFL/system 历史 notes" 但**未真测每 font** — SELF-AUDIT #06 明示 "partial; no fonts redistributed" — 诚实但浅
- **5-Gate audit case**: ⚠️ **重大问题**. `GATE-04-typography` 6 case (case-01 ~ case-06) **完全相同 boilerplate**: "The screen/template keeps `mixed Chinese/English and machine strings remain readable`" — 6 次原文复制, **无好坏对照差异**. 其他 4 个 GATE 文件预期同款. 30 case 名义上有, 实际 **1 个 case × 6 重复 × 5 gate ≈ 5 个真 case**
- **8 Panel design**: PANEL-04 真用 token 引用 (`sf.panel.bg / sf.border.panel / display.station / sf.space.2-5`) — **无 hex 硬编码**, state variants 6 态 (idle/loading/ready/candidate/blocked/stale) + good vs bad 表 + Mermaid stateDiagram. 质量优

## §3 audit-expansion 模板病
**严重 boilerplate 污染**: 每文件尾部都被 4-13 段 "audit expansion N" 自动追加, 内容是 5-Gate alignment / Implementation seam / Linked-state grammar / Review discipline 4 个固定模板的 round-robin 重复. README.md 单文件就有 9 段重复, TOKEN-01 有 8 段, PANEL-04 有 12 段, GATE-04 有 13 段. **约 30-40% 字数是机械重复**, "198K 字"实际信息密度 ≈ 120-130K.

## §4 PR / 5-Gate 集成
SELF-AUDIT 30 条诚实标 #25-#28 `blocked / pending` (cross-local source / GitHub U4-U7 connector 失败). MASTER 明示 "无 live web / 无 ~/workspace/ScoutFlow / 无 ~/.claude/rules". boundary 在每文件 frontmatter `authority: not-authority` 严守, 无 package install / runtime / migration 暗示.

## §5 Verdict
**`CONCERN-MINOR`** — 单文件深度优秀 (token contrast 真测、panel token 真引、icon SVG 真路径), 但 7+8 cluster 的 audit-expansion 模板污染稀释 30%+ 字数 + 5-Gate 30 case 实质只有 5 个 unique scenario.

## §6 Promote 建议
- **Tier 1 promote**: `01-token-system/TOKEN-01-PALETTE` (15 hex + 36 行 WCAG 矩阵) → 可作为 `apps/capture-station` future CSS Variables 真实 source
- **Tier 1 promote**: `05-panel-design-spec/PANEL-01~08` 8 文件 (token-only 引用 + state grammar + good/bad 表)
- **Tier 1 promote**: `02-icon-library` 30 文件 (60 SVG candidate path)
- **instrument**: `07-5-gate-audit-tests` 5 GATE → 必须重做 case 1-6, 每 case 给独立 scenario + screenshot 占位 + 真 good/bad 对照
- **instrument**: 全 108 文件批量删除 audit-expansion 段 (机械可正则去除), 可减 60K 字回归 ~138K 字密度
- 不要 Tier 1 promote: `06-multi-medium-template` PPT/H5/poster 模板 (未抽看, 但鉴于 5-Gate case 模板病疑似同模式)
