---
title: Cloud Prompt — U15 240+ PR Decision Log Atlas v0 (≥100 文件)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
expected_zip_files: 100+
expected_zip_words_cjk_latin: 130000+
expected_thinking_minutes: 180+
---

# Cloud Prompt — U15 240+ PR Decision Log Atlas

## §1 Mission

ScoutFlow 已 land 240+ PR (从 #1 ~ #240+). 这些 PR 蕴含的**决策**散在 commit message / PR description / merge commit / amend ledger / decision-log.md / handoff trail 里, **没有结构化为可查 / 可分类 / 可学的 atlas**. 用户每次想"我们之前为什么这么做"靠 grep + git log + 记忆, 跨 phase 决策模式无法抽象.

本任务: 把关键 80-100 个 PR (并非每个都重要) 沉淀为 **single-file decision log** 集合, 每 PR = 一个 markdown (context / options / chosen / rationale / outcome / lessons / cross-link). 加按 cluster (PF-LP / C1 / C2 / C3 / META / Wave 4-5 / strategic-upgrade) 组织 + timeline view + topic view + decision pattern abstraction + amend trail map.

外加 11 cluster index + 5 supporting (master atlas / decision-pattern-library / amend-trail-map / cross-link-to-anti-pattern / README) = **≥110 文件**.

## §2 Inputs

### A. ScoutFlow git history + PR ledger
1. `gh pr list --repo RayWong1990/ScoutFlow --state merged --limit 250 --json number,title,mergedAt,labels,author,body`
2. `git log --all --pretty=format:'%H | %ai | %s' main` (commit timeline)
3. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/decision-log.md (现有 decision log, 是 base)
4. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-amendments/ + SRD-amendments/ (amendment trail)
5. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/ (4 run audit)
6. CHECKPOINT-Run1/Run2/Run3-4.json (decision evidence in receipts)
7. PR #231 / #239 / #240 (3 amendment / single-PR examples)

### B. 历史 80-pack 体系
8. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/post-dispatch176-roadmap-candidate-2026-05-05.md
9. 80-pack source (Wave 4-5 / PF-META / PF-LP / PF-C1 / PF-C2 / PF-C3 体系)

### C. Cross-link target
10. U10 runbook + U11 anti-pattern (decision → 后果 映射)

## §3 Multi-pass Work Plan (≥12 pass, ≥180 min)

1. **Pass 1 — PR inventory**: 列全 240+ merged PR (按 number 排序, 含 title / mergedAt / cluster / amend trail flag), 输出全 PR list 但**只挑选 ≥80 关键 PR** 进 atlas (基于: 标 amend / 改 contract / 设 boundary / 新增 module / 删除 lane / 引入 vendor / promote / archive 等)

2. **Pass 2 — Schema 设计**: 每 PR decision 单文件 ~1300-1600 字, frontmatter (decision_id = PR-{number}-{short-name} / pr_number / cluster / merged_at / amend_chain[] / authority_writer / author / decision_kind ∈ {scope/contract/boundary/vendor/promote/archive/amendment/other} / impact_radius ∈ {single-file/single-cluster/multi-cluster/cross-phase} / introduced_or_exposed (元认知 §1.8)), body 含 8 段 (mission / context / options / chosen / rationale / outcome / lessons / linked)

3. **Pass 3 — Cluster 1: 80-pack + Wave 4-5 + PF-META (~25-30 PR)**: 早期 PR (< #199) 选 ~25 个最重要 (T-P1A-* / META 系列 / wave 系列)

4. **Pass 4 — Cluster 2: PF-LP Run-1 (#199-#206, 8 PR)**: 全选

5. **Pass 5 — Cluster 3: PF-LP Run-2 + Window-2 (#207-#230, ~24 PR)**: 选 ~15 关键

6. **Pass 6 — Cluster 4: Run-1 amendment (#231)** + **Cluster 5: Run-2 amendment (#239)** + **Cluster 6: Run-3+4 single PR (#240)**: 全选 (3 amendment 是关键)

7. **Pass 7 — Cluster 7: 后续 #241+ 当前 strategic-upgrade**: 选 ~5 关键 (cloud prompt land 等)

8. **Pass 8 — Cluster 8: ContentFlow → ScoutFlow legacy decision (~5)**: 跨项目继承的关键决策 (4 层架构 / single-writer / single-user / preview-only / vendor 多元化)

9. **Pass 9 — Decision pattern library 抽象 (≥15 pattern)**:
   - amend_and_proceed pattern
   - 3-window cloud audit pattern
   - silent flexibility detection pattern
   - boundary preservation pattern (write_enabled / 5 overflow / authority files)
   - vendor [evaluation-candidate] vs [accepted] pattern
   - candidate / not-authority frontmatter pattern
   - SoR (System of Record) split pattern
   - egress contract pattern
   - dispatch lineage pattern
   - amendment trail (PR226-228 packed repair / 5-dispatch silent merge / partial cascade) pattern
   - introduced vs exposed attribution pattern
   - claim label discipline (canonical fact / promoted_addendum / candidate-carry-forward / tentative)
   - truthful stdout contract pattern
   - human-in-loop gate pattern
   - rollback path pattern

10. **Pass 10 — Timeline view + Topic view + Amend trail map**:
    - Timeline (按月): 4-5 timeline file (2026-04 / 05)
    - Topic: cluster-based (PF-LP / C1 / C2 / C3 / META) topic file
    - Amend trail map (Mermaid graph 显示 amend chain: PR-X amended by PR-Y)

11. **Pass 11 — Cross-link to U11 anti-pattern**: 每 amend / silent-flexibility / boundary-leak decision → linked_anti_pattern (U11 AP-X-XX)

12. **Pass 12 — 11 cluster index + 5 supporting + README + truthful stdout**

## §4 Hard Boundaries

- candidate / not-authority 全 ≥110 文件
- 不修改 docs/decision-log.md (canonical authority, 只读 + atlas 是 candidate supplementary)
- 不修改 PRD/SRD-amendments/ canonical (只读)
- 不暴露 commit/PR 中可能的 PII / 凭据 (mask)
- 引用 PR # 必须真实存在 (不许脑补 PR)
- introduced_or_exposed 字段必须诚实 (元认知 §1.8 — 不许默认归因到最近 PR)

## §5 Live Web Evidence

非 required — 历史回溯 / 综合任务.

## §6 Cross-local Search

- ScoutFlow `gh pr list` + `git log` 真实查询
- ContentFlow L1 retrospective (跨项目 legacy 决策 source)
- ~/.claude/projects/.../memory/ ScoutFlow 项目级 memory (历史决策记忆)

## §7 Output Deliverables

ZIP filename: `cloud-output-U15-pr-decision-log-atlas-2026-05-07.zip`
File count: **≥110**

| 类别 | 文件数 | min 字 |
|---|---:|---:|
| Cluster 1: 80-pack/Wave/META | ≥25 | 1300 |
| Cluster 2: Run-1 (#199-206) | 8 | 1300 |
| Cluster 3: Run-2/Window-2 | ≥15 | 1300 |
| Cluster 4-6: 3 amendment + Run-3+4 | 3 | 2200 (重要 PR 加倍) |
| Cluster 7: #241+ strategic-upgrade | ≥5 | 1300 |
| Cluster 8: ContentFlow legacy | ≥5 | 1300 |
| Decision pattern library (≥15) | 15 | 1500 |
| Timeline view (按月 4-5) | 5 | 2000 |
| Topic view (按 cluster ~7) | 7 | 1800 |
| Amend trail map | 1 | 2200 (Mermaid) |
| Cluster index (11) | 11 | 1500 |
| MASTER-DECISION-ATLAS | 1 | 3500 |
| DECISION-PATTERN-INDEX | 1 | 2500 |
| INTRODUCED-VS-EXPOSED-MAP | 1 | 2500 |
| LINKED-ANTI-PATTERN-CROSS-LINK | 1 | 2200 |
| README | 1 | 1500 |
| **总计** | **≥111** | ≥140000 |

claim label coverage ≥85%; Mermaid: amend trail + timeline + topic ≥4 = ≥6 张

## §8 Self-audit (≥30)

- 每 PR # 真实存在 (不许脑补)
- introduced_or_exposed 是否诚实区分
- amend_chain 真实 (PR-X amended by PR-Y 真发生)
- decision pattern 是否真抽象 (vs 复制具体 PR)
- timeline 排序真按 mergedAt
- topic view 不重复 cluster (无冗余)
- 与 U11 anti-pattern 真双向 link
- 与 docs/decision-log.md canonical 不冲突 (atlas 是 supplementary, 不替代)
- ContentFlow legacy 决策真延伸到 ScoutFlow (vs 强行联系)
- single-user 视角 vs 团队 audit log drift

## §9 Truthful Stdout Contract

```yaml
CLOUD_U15_PR_DECISION_LOG_ATLAS_COMPLETE: true
zip_filename: cloud-output-U15-pr-decision-log-atlas-2026-05-07.zip
files_count: <真实, ≥110>
total_words_cjk_latin_approx: <真实, ≥130000>
total_thinking_minutes: <真实>
prs_documented: <真实, ≥80>
amendment_prs_documented: <真实, 期望 ≥3 (#231 #239 #240)>
decision_patterns_extracted: <真实, ≥15>
timelines_count: <真实, ≥4>
topic_views_count: <真实, ≥7>
amend_trail_mermaid_nodes: <真实>
introduced_count: <真实>
exposed_count: <真实>
contentflow_legacy_decisions: <真实>
mermaid_diagrams: <真实, ≥6>
multi_pass_completed: <真实/12>
self_audit_findings: <真实, ≥30>
canonical_decision_log_unchanged: confirmed
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U15-pr-decision-log-atlas-2026-05-07.zip`

## §11 Format Guard

- 每 PR decision frontmatter 含 `pr_number` `merged_at` `cluster` `decision_kind` `impact_radius` `introduced_or_exposed`
- amend_chain 字段真实 (PR-X 真被 PR-Y amended)
- linked_anti_pattern (U11) cross-link 真存在
- timeline 按 ISO 日期排序
- 任何 PR # < 1 或 > 实际最大 PR # → reject (脑补阻止)
