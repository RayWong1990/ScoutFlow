---
title: Cloud Prompt — U11 Anti-Pattern Encyclopedia v0 (≥75 文件 / ≥60 anti-pattern)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
new_lane: yes
expected_zip_files: 75+
expected_zip_words_cjk_latin: 110000+
expected_thinking_minutes: 150+
---

# Cloud Prompt — U11 Anti-Pattern Encyclopedia v0

## §1 Mission

ScoutFlow 4 run / 80-pack / Wave 4-5 / ContentFlow L1 / Codex+Opus 元认知差异 / 多窗口协作历史 沉淀了大量**实测踩坑**, 但**没有结构化为可查 / 可 detect / 可 prevent 的 anti-pattern 库**. 用户每次踩同样的坑, 重新发现 + 重新沉淀, 工作记忆不可复用.

本任务: 把所有踩坑沉淀为 **≥60 个 single-file anti-pattern markdown**, 每 anti-pattern = 一个具体反例 + 触发 signal + 后果 + 正例对照 + detect rule + prevent rule + escape clause + 真实历史 attribution.

外加 10 cluster index + 5 supporting (master index / detect-rule-catalog / prevent-rule-catalog / escape-clause-catalog / cross-link-to-runbook / README) = **≥75 文件**.

特别强调: 区分 **introduced (新引入)** vs **exposed (历史债被新动作暴露)** — 这是 ContentFlow L1 沉淀的元认知 §1.8 关键纠偏, 大部分团队默认归因到最近变更 = 错误归因.

## §2 Inputs

### A. ScoutFlow 4 run + 80-pack 实测踩坑
1. https://github.com/RayWong1990/ScoutFlow/tree/main/docs/research/post-frozen/runs (4 run audit ledger)
2. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/EXTERNAL-AUDIT-REPORT-2026-05-07.md
3. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/decision-log.md
4. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-amendments/ (PRD 修订 trail)
5. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-amendments/
6. PR #231 (Run-1 amendment) / PR #239 (Run-2 amendment) / PR #240 (Run-3+4 single PR) — 全部 amendment 都有 anti-pattern 触发记录
7. CHECKPOINT-Run1/Run2/Run3-4.json amend_trigger / silent_flexibility / scope_drift 字段
8. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md

### B. ContentFlow L1 retrospective (重要 anti-pattern 源)
9. ~/workspace/contentflow/L/reports/L1-production-retrospective-OPUS-EXTENSION-2026-04-27.md (1749 行 retrospective, 21 swap, 24 Codex 反馈条款)
10. ~/workspace/contentflow/L/reports/L2-STEP0-PRELAUNCH-PLAN-2026-04-27.md (附录 E timeline)
11. ~/.claude/rules/codex-metacognition-learnings.md (8 条 Opus 可学 Codex + 4 条反向 + 8 条自检 + 实战命中验证)

### C. 全局规则 (canonical, 引用不重写)
12. ~/.claude/rules/aesthetic-first-principles.md (5 Gate 红线)
13. ~/.claude/rules/parallel-safety.md (并行碰撞历史)
14. ~/.claude/rules/execution-discipline.md (假设暴露 / 规划 ≤2 轮)
15. ~/.claude/rules/session-closure.md (沉淀六步)
16. ~/.claude/rules/token-hygiene.md (60% / 85% 黄红灯)
17. ~/.claude/rules/agents.md (Agent 使用门槛)
18. ~/.claude/rules/security.md
19. ~/.claude/rules/testing.md

### D. 8 strategic-upgrade prompt + U9 dispatch catalog + U10 runbook (cross-link target)
20. https://github.com/RayWong1990/ScoutFlow/tree/main/docs/research/strategic-upgrade/2026-05-07

## §3 Multi-pass Work Plan (≥10 pass, ≥150 min)

1. **Pass 1 — Anti-pattern inventory**: 读 §2 A/B/C, 抽出所有踩坑实例, 分 10 cluster (Silent-Flexibility / Authority-Confusion / Boundary-Leak / Visual-5Gate-Failure / Vendor-SupplyChain / Memory-CrossSession / Multi-Agent-Collab / Cost-Token / Engineering-Discipline / Documentation-Truthfulness)

2. **Pass 2 — Schema 设计**: 每 anti-pattern 单文件 ~1500-1800 字, frontmatter (anti_pattern_id / cluster / risk_level ∈ {low/medium/high/critical} / first_seen_in (PR# 或 ContentFlow timeline) / introduced_or_exposed / detect_method ∈ {regex/static/grep/human/audit} / prevent_method ∈ {schema/contract/template/hook/skill} / escape_difficulty ∈ {trivial/moderate/hard/critical}), body 含 10 段 (mission / 反例描述 / 触发 signal / 后果 / 正例对照 / detect rule / prevent rule / escape clause / 真实 attribution / linked)

3. **Pass 3 — Cluster A: Silent-Flexibility / Scope Drift (8-10 anti-pattern)**:
   - AP-SF-01 Run-2 PR226-228 packed repair without explicit authorization
   - AP-SF-02 Run-1 5 dispatch silent merge (amend trigger)
   - AP-SF-03 Codex 自作主张合并 5 dispatch (silent flexibility)
   - AP-SF-04 派单未 explicit but worker 推测扩 scope
   - AP-SF-05 Multi-PR drift (本应 6 实际 5)
   - AP-SF-06 Naming silent change (字段名 silent rename)
   - AP-SF-07 File path silent change
   - AP-SF-08 Threshold silent loosen
   - AP-SF-09 Verdict silent escalate (concern → clear)
   - AP-SF-10 Boundary silent expand

4. **Pass 4 — Cluster B: Authority-Confusion / Single-Writer (6-8)**:
   - AP-AC-01 双窗口同写 docs/current.md
   - AP-AC-02 Authority files 被 sidecar agent 误写
   - AP-AC-03 task-index.md task 编号冲突 (2026-05-04 实例)
   - AP-AC-04 decision-log.md append vs rewrite
   - AP-AC-05 contract-index.md baseline drift
   - AP-AC-06 AGENTS.md 重写而非 amend
   - AP-AC-07 Authority promote 跳过 audit gate
   - AP-AC-08 Authority writer max=1 violation

5. **Pass 5 — Cluster C: Boundary-Leak / Overflow Slip (8-10)**:
   - AP-BL-01 write_enabled=False 暗示 unlock
   - AP-BL-02 BBDown live runtime 暗示批准
   - AP-BL-03 ASR runtime 暗示批准
   - AP-BL-04 Browser automation 暗示批准
   - AP-BL-05 Migration 暗示批准
   - AP-BL-06 5 overflow lane 单 PR 多 unlock
   - AP-BL-07 派单 schema 缺 can_open_X 三 flag
   - AP-BL-08 vendor [evaluation-candidate] silent → [accepted]
   - AP-BL-09 preview-only 漂移成 production-write
   - AP-BL-10 candidate 文件 silent → authority

6. **Pass 6 — Cluster D: Visual / 5-Gate Failure (6-8)** [引用 aesthetic-first-principles.md]:
   - AP-VF-01 主标题字号 < 副标题 30%
   - AP-VF-02 字幕压住关键内容 (occlusion safety)
   - AP-VF-03 元素位置随机 (spacing alignment)
   - AP-VF-04 WCAG contrast < 4.5:1
   - AP-VF-05 重要元素视觉重量 < 装饰
   - AP-VF-06 色彩饱和抢戏
   - AP-VF-07 中英混排 baseline 错位
   - AP-VF-08 "差不多就行" 违反硬门
   - AP-VF-09 事后修补违反 Day-0 设计输入
   - AP-VF-10 移动版 safe-area 被压

7. **Pass 7 — Cluster E/F (Vendor + Memory)** (5-7 each):
   - Cluster E Vendor: 单 vendor lane 锁死 / vendor 选型未 spike audit / BBDown C&D 未 recheck / yt-dlp legal 未 refresh / ASR vendor 未 benchmark / Whisper 未 local install verify / Cloud API 当免费
   - Cluster F Memory: handoff 流水账 / handoff Step 5 缺失 / /clear 按 session 时长 / /compact focus arg 漏 anchor / MEMORY.md 超 200 行 / 跨 session 假设上下文持续 / recover 不 git fetch

8. **Pass 8 — Cluster G/H (Multi-Agent + Cost-Token)** (5-7 each):
   - Cluster G Multi-Agent: 多窗口 dispatch 无 ledger / amend_and_proceed 跳过 user authorize / 3-window cloud audit 仅 1-2 窗口 / silent flexibility detect 漏 / single-writer race / 元认知差异忽视 (introduced vs exposed) / cross-window memory drift
   - Cluster H Cost-Token: 派单不估 token / 长 session 不 /clear / /compact 后丢 anchor / 无 cost dashboard / API retry no backoff / 重复跑同 prompt 不 cache

9. **Pass 9 — Cluster I/J (Engineering + Documentation)** (5-7 each):
   - Cluster I Engineering: 不 TDD / 测试覆盖 < 80% / 跳 code-review agent / 不 verification loop / import 路径假设 / 不 git fetch 即诊断 / 误用 destructive git / skip hooks
   - Cluster J Documentation: PASS/DONE/OK 措辞滑坡 (元认知 §1.1) / 伪造 wall-clock / live web 声称但未联网 / claim label 未标 / evidence not refreshed / "经测试" 无 evidence

10. **Pass 10 — 10 cluster index + 5 supporting + README + truthful stdout**:
    - 10 cluster index file (一 cluster 一个, 含 cluster mission / risk profile / anti-pattern 清单 / cross-link)
    - MASTER-ANTI-PATTERN-INDEX-2026-05-07.md (10 cluster matrix + risk_level heatmap + introduced/exposed 分布)
    - DETECT-RULE-CATALOG-2026-05-07.md (regex / static check / grep / hook / human review 全集)
    - PREVENT-RULE-CATALOG-2026-05-07.md (写进 schema / contract / template / skill 全集)
    - ESCAPE-CLAUSE-CATALOG-2026-05-07.md (检测后纠正路径)
    - CROSS-LINK-TO-RUNBOOK-AND-DISPATCH-2026-05-07.md (与 U10 runbook + U9 dispatch 双向映射)
    - SELF-AUDIT-FINDINGS (≥25 issue inline)
    - README

## §4 Hard Boundaries

- candidate / not-authority frontmatter 全 ≥75 文件
- write_enabled=False 不变
- 不批准任何 anti-pattern detect/prevent rule 实际部署 — 仅 candidate spec
- authority files 不写
- 5 overflow lane Hold 不变
- 不修改 production code / hook / skill / rule (只引用 ~/.claude/rules/* canonical)
- 真实历史 attribution 必须有 PR # 或 ContentFlow timeline 锚点 (无锚点的脑补 anti-pattern → 标 [hypothetical] 不混入)
- introduced vs exposed 字段必须诚实区分

## §5 Live Web Evidence

非 required — 本任务是历史复盘 + 沉淀, 不是新 research.

## §6 Cross-local Search

- ~/workspace/contentflow/L/ 完整 retrospective (1749 行) — 重要 anti-pattern 源
- ~/.claude/rules/codex-metacognition-learnings.md — 元认知差异 + 实战命中
- ~/.claude/rules/* 全规则 — 反向推已存在 prevent rule
- ScoutFlow 4 run audit + amendment ledger
- ContentFlow 历史 audit 记录

## §7 Output Deliverables

ZIP filename: `cloud-output-U11-anti-pattern-encyclopedia-2026-05-07.zip`
File count: **≥75** (硬下限)

| 类别 | 文件数 | min 字 / 文件 | 总字数 |
|---|---:|---:|---:|
| Cluster A Silent-Flexibility | ≥9 | 1500 | ≥13500 |
| Cluster B Authority-Confusion | ≥7 | 1500 | ≥10500 |
| Cluster C Boundary-Leak | ≥9 | 1500 | ≥13500 |
| Cluster D Visual-5Gate | ≥9 | 1500 | ≥13500 |
| Cluster E Vendor-SupplyChain | ≥6 | 1500 | ≥9000 |
| Cluster F Memory-CrossSession | ≥6 | 1500 | ≥9000 |
| Cluster G Multi-Agent-Collab | ≥6 | 1500 | ≥9000 |
| Cluster H Cost-Token | ≥5 | 1500 | ≥7500 |
| Cluster I Engineering-Discipline | ≥6 | 1500 | ≥9000 |
| Cluster J Documentation-Truthfulness | ≥5 | 1500 | ≥7500 |
| Cluster index (10 cluster) | 10 | 1500 | ≥15000 |
| MASTER-INDEX | 1 | 3000 | 3000 |
| DETECT-RULE-CATALOG | 1 | 2500 | 2500 |
| PREVENT-RULE-CATALOG | 1 | 2500 | 2500 |
| ESCAPE-CLAUSE-CATALOG | 1 | 2200 | 2200 |
| CROSS-LINK-TO-RUNBOOK-DISPATCH | 1 | 2200 | 2200 |
| SELF-AUDIT | 1 | 3500 | 3500 |
| README | 1 | 1500 | 1500 |
| **总计** | **≥85** | — | **≥133900** |

claim label coverage ≥90% paragraph
Mermaid: master heatmap + cluster index ≥3 张 = ≥4 张

## §8 Self-audit (Pass 10 内嵌)

≥25 findings inline. 涵盖:
- 每 anti-pattern attribution 是否真有 PR # / timeline 锚点 (非脑补)
- introduced vs exposed 是否诚实区分 (元认知 §1.8)
- detect rule 是否真可执行 (vs 概念性)
- prevent rule 是否真能写进 schema/contract/template (元认知 §1.5)
- escape clause 是否考虑用户 already 踩坑后的纠偏路径
- 与 U10 runbook 是否真双向映射 (no orphan)
- 与 U9 dispatch 是否真 cross-link
- 与 ~/.claude/rules/* 全局规则是否冲突 (anti-pattern 应是规则的反向)
- 是否漂移成企业 SRE incident postmortem 重型方案
- 真实 ScoutFlow 历史 vs 通用 software anti-pattern 区分

## §9 Truthful Stdout Contract

```yaml
CLOUD_U11_ANTI_PATTERN_ENCYCLOPEDIA_COMPLETE: true
zip_filename: cloud-output-U11-anti-pattern-encyclopedia-2026-05-07.zip
files_count: <真实, ≥75>
total_words_cjk_latin_approx: <真实, ≥130000>
total_thinking_minutes: <真实, 不许伪造>
anti_patterns_count_total: <真实, ≥60>
cluster_a_silent_flexibility: <真实>
cluster_b_authority_confusion: <真实>
cluster_c_boundary_leak: <真实>
cluster_d_visual_5gate: <真实>
cluster_e_vendor_supplychain: <真实>
cluster_f_memory_crosssession: <真实>
cluster_g_multi_agent_collab: <真实>
cluster_h_cost_token: <真实>
cluster_i_engineering_discipline: <真实>
cluster_j_documentation_truthfulness: <真实>
introduced_count: <真实>
exposed_count: <真实>
hypothetical_marked_count: <真实, 应 ≤总 10%>
real_pr_anchor_count: <真实>
contentflow_timeline_anchor_count: <真实>
mermaid_diagrams_count: <真实, ≥4>
multi_pass_completed: <真实/10>
self_audit_findings: <真实, ≥25>
boundary_preservation_check: clear
no_actual_rule_deployment_implied: confirmed
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U11-anti-pattern-encyclopedia-2026-05-07.zip` — 严格匹配

## §11 Format Guard (cloud 自检)

- `find . -name "AP-*.md" | wc -l` 期望 ≥60
- 每 anti-pattern frontmatter 含 `anti_pattern_id` / `cluster` / `risk_level` / `first_seen_in` / `introduced_or_exposed` / `detect_method` / `prevent_method`
- 每 anti-pattern body 含 10 段 (mission/反例/signal/后果/正例/detect/prevent/escape/attribution/linked)
- 总字数 ≥130000
- Mermaid ≥4
- introduced + exposed + hypothetical 三类计数和 = 总 anti-pattern 数 (无遗漏)
- linked_runbook 字段引用 U10 runbook ID (RB-X-XX)
- linked_dispatch 字段引用 U9 dispatch ID (P2-/P3-/P4-/MOD-)
- linked_rule 字段引用 ~/.claude/rules/*.md 真实文件名
- 任何 anti-pattern 未声称"绝对可 detect" / "已自动 prevent"
