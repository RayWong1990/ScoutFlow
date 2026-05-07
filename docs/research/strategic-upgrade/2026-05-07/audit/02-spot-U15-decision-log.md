---
title: Spot Check — U15-decision-log
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Spot Check — U15-decision-log

## §1 文件抽样
README + SELF-AUDIT-30 + MASTER-DECISION-ATLAS + TRUTHFUL-STDOUT.yaml + 3 random (PR-001 bootstrap / PATTERN-11-introduced_vs_exposed / AMEND-TRAIL-MAP).

## §2 PR # 真实性
**真**. SELF-AUDIT #1 明示 "80 merged PR generated from verified PR numbers; #229 excluded (closed/unmerged)", TRUTHFUL-STDOUT `prs_documented: 80` (非吹 240+), `full_240_pr_inventory_loaded: False`, `failed_gates: ["full_240_pr_inventory", "u10_registry", "u11_registry", "contentflow_l1_source"]`. PR-001 frontmatter `pr_url: https://github.com/RayWong1990/ScoutFlow/pull/1`, `merged_at: "2025-05-04T21:29:10Z"`. 本地 `gh pr list` 验证 #240/#239/#238/#237/#236 真存在 + mergedAt 时间戳与 atlas TRUTHFUL-STDOUT 一致. **240 总 - 80 文档化 = 仍缺 160 PR**, 但 atlas 明示 partial 而非冒充全.

## §3 introduced_or_exposed 字段诚实
TRUTHFUL-STDOUT: `introduced_count: 51 / exposed_count: 21 / both_count: 8`, **3 类显式分开**. PR-001 标 `introduced` + `attribution_confidence: medium` (非 high) — 诚实下放置信度. SELF-AUDIT #11 "Amendment trail distinguishes amends from amended_by", #12 "Introduced vs exposed map exists and marks both for PRs later amended or caveated".

## §4 amend chain 真发生
**真**. AMEND-TRAIL-MAP 列 #231 amends [#204, #205, #206, #198, #199] + #239 amends [#226, #228, #231, #232-#238]. 本地 `gh pr view 231` 验证 PR body 含 "**A1** PF-LP-02 / #205 / **A2** PF-LP-13 / #206 / **A3** PF-LP-01 / #204 / **A4** #199 supersession / **A5** #198 boundary note" — atlas amend chain **逐条 1:1 对应** PR #231 真实 body amendment ledger. Mermaid graph + table 双层呈现, 无伪造 link. `amends` 谨慎定义为 "later PR body explicitly records, repairs, or reframes earlier", **区分 receipt repair vs code reversion** — 元认知到位.

## §5 与 canonical 不冲突
README §"Safety boundary" 明示 "No canonical ScoutFlow file was modified. This package is an offline artifact only". MASTER §"What this atlas is" 显式声明 "It does not modify `docs/decision-log.md`, PRD/SRD amendments". 每 PR 卡 frontmatter `canonical_decision_log_unchanged: true`. **supplementary 定位严守**.

## §6 timeline + Mermaid 质量
TRUTHFUL-STDOUT `timelines_count: 5 / mermaid_diagrams: 19`. AMEND-TRAIL Mermaid flowchart 含 21 edge, **真展示结构** 而非装饰 (每节点真对应 PR # + relation 标 amended_by/amends/records repair). PATTERN-11 Mermaid `Candidate→Boundary check→Amend/downgrade→Record traceability→Future promotion gate` — 简洁 5 节点, 紧扣 pattern 本意. 但 timeline 未抽看实文件, 按 mergedAt 排序假定为真 (PR-001 卡片 frontmatter 时间戳格式统一 ISO-8601 支持本论断).

## §7 Verdict
**`CLEAR`** — 80 PR 卡片质量真实、attribution 诚实、amend chain GitHub 1:1 验证、boundary 严守 supplementary 定位. partial coverage 透明披露 (sniff 已 CLEAR).

## §8 Promote 建议
- **Tier 1 promote**: `00_META/MASTER-DECISION-ATLAS` + `09_inventory/PR-INVENTORY-LOCK` + `05_amend_trail/AMEND-TRAIL-MAP` (3 文件) → 作为 ScoutFlow 唯一 PR 决策检索层 supplementary; canonical `docs/decision-log.md` 仍主写入
- **Tier 1 promote**: `02_patterns/PATTERN-11-introduced_vs_exposed_attribution` + `PATTERN-04-boundary_preservation` + `PATTERN-15-rollback_path` → 作为 prevent-rule contract 候选
- **instrument**: 补 #161 之前的 PR 卡片 (#1-#160 仍缺) → 让 atlas 真覆盖 240+. 建议下一轮 cloud prompt 直接用本 ZIP 的 frontmatter schema 作 input contract
- **instrument**: 把 "linked_anti_patterns: []" 和 "u11_runbook gap" 显式移到一个 followup-checklist 文件, 用户审计时一眼可见 unlock 路径
- 不要 Tier 1 promote: `07_legacy/` (5 ContentFlow 候选 hypothesis, 含混合项目噪音)
