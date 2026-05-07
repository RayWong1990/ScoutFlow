---
title: Cloud Prompt — U10 Single-User Prosumer SOP / Runbook Library v0 (≥65 文件)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
new_lane: yes
expected_zip_files: 65+
expected_zip_words_cjk_latin: 100000+
expected_thinking_minutes: 150+
---

# Cloud Prompt — U10 Single-User Prosumer SOP / Runbook Library v0

## §1 Mission

ScoutFlow 用户在 single-user / max horsepower / strong visual / multi-AI fleet 模式下已沉淀大量**事实工作流** (4 run / 80-pack / amend_and_proceed / 3-window cloud audit / dispatch protocol / multi-window 协作 / 视觉生产 / RAW handoff / overflow guard / etc), 但**这些工作流没有结构化沉淀成可重复的 SOP/Runbook**. 用户每次执行靠记忆 + 参考过去 handoff, 容易漏步骤 / 跳前置检查 / 忘 rollback path.

本任务: 把所有事实工作流抽象为 **≥55 个 single-file runbook**, 每 runbook = 一个具体场景的 step-by-step SOP, 用户在新场景里**直接读 runbook 即可执行**, 不需要每次重新推理.

每 runbook 强 schema: trigger / preconditions / steps / verification / rollback / lessons learned (4 run 历史 / ContentFlow L 历史 踩坑) / linked dispatch / linked tools / linked skill.

外加 8 cluster index + 5 supporting = **≥68 文件**.

## §2 Inputs

### A. ScoutFlow 4 run + 80-pack 历史
1. https://github.com/RayWong1990/ScoutFlow/tree/main/docs/research/post-frozen/runs (4 run ledger)
2. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/EXTERNAL-AUDIT-REPORT-2026-05-07.md (Run-3+4 audit)
3. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md (LP-001/006/007/SEC-001 4 协作纪律)
4. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md
5. https://github.com/RayWong1990/ScoutFlow/blob/main/AGENTS.md
6. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/dispatch-template.md
7. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md
8. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/post-dispatch176-roadmap-candidate-2026-05-05.md

### B. 8 strategic-upgrade prompt (供 reference)
9. https://github.com/RayWong1990/ScoutFlow/tree/main/docs/research/strategic-upgrade/2026-05-07

### C. ContentFlow L1 历史 (multi-agent 协作模式 4h27m / 21 swap 沉淀)
10. ~/workspace/contentflow/L/reports/L1-production-retrospective-OPUS-EXTENSION-2026-04-27.md (1749 行 retrospective)
11. ~/.claude/rules/codex-metacognition-learnings.md (8 元认知差异 + 实战命中)

### D. 全局规则 (引用不重写)
12. ~/.claude/rules/aesthetic-first-principles.md (5 Gate)
13. ~/.claude/rules/agents.md (Agent 使用门槛 / 并行限制)
14. ~/.claude/rules/development-workflow.md (TDD / code-review)
15. ~/.claude/rules/testing.md (80% / 100% bar)
16. ~/.claude/rules/security.md
17. ~/.claude/rules/parallel-safety.md
18. ~/.claude/rules/session-closure.md (沉淀六步)
19. ~/.claude/rules/token-hygiene.md (60% / 85% 黄红灯)
20. ~/.claude/rules/execution-discipline.md (规划 ≤2 轮 / 假设暴露)

## §3 Multi-pass Work Plan (≥10 pass, ≥150 min)

1. **Pass 1 — Workflow inventory**: 读 §2 A/B/C/D, 抽出所有事实工作流, 分 8 cluster (Capture / Dispatch / Boundary-Audit / Visual / Memory / Egress / Tooling / Recovery), 每 cluster ≥5 workflow

2. **Pass 2 — Runbook schema 设计**: 每 runbook 单文件 ~1500-1800 字, frontmatter 含 (runbook_id / cluster / trigger_keywords / risk_level ∈ {low/medium/high/critical} / single_user_applicable / multi_agent_applicable / linked_dispatch / linked_pr / linked_tools / linked_skill / linked_rule), body 含 9 段 (mission / trigger / preconditions / steps / verification / rollback / lessons / linked / footer)

3. **Pass 3 — Cluster A: Capture / Acquisition (8-10 runbook)**:
   - RB-CAP-01 Single Bilibili URL metadata-only capture (current Phase 1A 能力)
   - RB-CAP-02 Single XHS URL capture (无官方 API 现状)
   - RB-CAP-03 Single YouTube URL capture
   - RB-CAP-04 Batch URL ingestion (Phase 2)
   - RB-CAP-05 Failed capture retry + rollback
   - RB-CAP-06 网络降级 / 弱网 capture
   - RB-CAP-07 BBDown legal posture recheck before run
   - RB-CAP-08 ASR local install verify (Whisper / Parakeet / Voxtral)
   - RB-CAP-09 capture scope gate enforce (LP-001 推荐/关键词/RAW gap 不直接 capture)
   - RB-CAP-10 quick capture vs scope-gated capture

4. **Pass 4 — Cluster B: Dispatch / Multi-Agent (10-12 runbook)**:
   - RB-DSP-01 Single dispatch 派给 Codex
   - RB-DSP-02 Single dispatch 派给 CC1
   - RB-DSP-03 Single dispatch 派给 Hermes
   - RB-DSP-04 Parallel multi-window dispatch (3-5 worktree)
   - RB-DSP-05 amend_and_proceed pattern (Run-1/2 模型)
   - RB-DSP-06 3-window cloud audit (Codex/GPT Pro/Hermes)
   - RB-DSP-07 silent flexibility detect (4 run 实测)
   - RB-DSP-08 silent flexibility recover (PR226-228 案例)
   - RB-DSP-09 single-writer enforce (LP-006)
   - RB-DSP-10 dispatch ledger record (与 U5 联动)
   - RB-DSP-11 cost attribution record (与 U5 联动)
   - RB-DSP-12 packed PR vs per-dispatch PR 决策

5. **Pass 5 — Cluster C: Boundary / Audit (8-10 runbook)**:
   - RB-BND-01 write_enabled scan (bridge/config.py:24,36)
   - RB-BND-02 5 overflow lane Hold scan
   - RB-BND-03 Authority files scan (current.md/task-index.md/decision-log.md/AGENTS.md)
   - RB-BND-04 Credential / secret scan (strict pattern + exclude rule)
   - RB-BND-05 PII redaction scan (regex + word boundary)
   - RB-BND-06 Legal posture recheck (Bilibili C&D / yt-dlp / scrapers)
   - RB-BND-07 can_open_C4 / can_open_runtime / can_open_migration 三 flag verify
   - RB-BND-08 Post-merge integrity check (origin/main SHA / authority untouched / hard redlines)
   - RB-BND-09 Boundary scan automation (CI / pre-commit hook)
   - RB-BND-10 Frontmatter status validator (candidate / not-authority)

6. **Pass 6 — Cluster D: Visual Production (8-10 runbook)**:
   - RB-VIS-01 GPT-Image-2 batch generation (云端 ZIP 工作流)
   - RB-VIS-02 Pattern A-J refinement loop
   - RB-VIS-03 Image → React TSX (PF-V handoff)
   - RB-VIS-04 5-Gate self-audit (3 自动 + 2 human-in-loop)
   - RB-VIS-05 Design token cascade rebuild
   - RB-VIS-06 State library register (8 panel × 6 state)
   - RB-VIS-07 Visual asset perceptual hash dedup
   - RB-VIS-08 WCAG 2.2 contrast ≥4.5:1 audit
   - RB-VIS-09 Storybook-style browser launch
   - RB-VIS-10 Visual asset cross-phase reuse query

7. **Pass 7 — Cluster E: Memory / Cross-Session (5-7 runbook)**:
   - RB-MEM-01 Handoff 创建 (≤80 行 + Step 5 next-session prompt)
   - RB-MEM-02 Handoff 阅读 (next session 起手)
   - RB-MEM-03 /clear 时机决策 (60% 黄 / 85% 红 / 不按 session 时长)
   - RB-MEM-04 /compact 操作 + focus arg
   - RB-MEM-05 MEMORY.md 维护 (200 行限制 / 归档过时)
   - RB-MEM-06 跨 session prompt 输出 (沉淀六步 Step 5)
   - RB-MEM-07 PreCompact 兜底 + SessionStart(compact) 恢复

8. **Pass 8 — Cluster F: Egress / Downstream (5-7 runbook)**:
   - RB-EGR-01 DiloFlow handoff (manifest publish)
   - RB-EGR-02 RAW vault staging (永不直写)
   - RB-EGR-03 Obsidian export
   - RB-EGR-04 hermes-agent integration
   - RB-EGR-05 Supersede protocol (旧版本 deprecated)
   - RB-EGR-06 Redaction enforce (PII / 凭据 / 法律敏感)
   - RB-EGR-07 Cross-system manifest schema validate

9. **Pass 9 — Cluster G/H + cluster index + supporting**:
   - Cluster G Tooling (RB-TOL-01..06): Whisper / bge-m3 / ollama / sqlite-vec / mlx / cc-resilient.sh
   - Cluster H Recovery (RB-REC-01..06): ~/workspace/raw wiped / SQLite corrupt / git 误删 / worktree 占用 / branch 误删 / token over budget
   - 8 cluster index file (RB-INDEX-{Capture/Dispatch/Boundary/Visual/Memory/Egress/Tooling/Recovery}-2026-05-07.md)
   - MASTER-RUNBOOK-INDEX (8 cluster cross-link + risk_level matrix)
   - RUNBOOK-SCHEMA-CONTRACT (frontmatter spec + body 9 段)
   - LINKED-RULES-INDEX (与 ~/.claude/rules/* canonical 全局规则映射)
   - LINKED-DISPATCH-CATALOG (与 U9 dispatch 映射)
   - SELF-AUDIT-FINDINGS (≥25 issue inline fixed)

10. **Pass 10 — README + truthful stdout**

## §4 Hard Boundaries

- candidate / not-authority frontmatter 全 ≥68 文件
- write_enabled=False 不变 (本 ZIP 不解禁)
- 不批准任何 runbook 实际执行 — runbook 仅 candidate, 用户 read-only 参考
- authority files 不写
- 5 overflow lane Hold 不变 (即使 RB-CAP-08 ASR install runbook 也是 candidate, 不实际 install)
- 不修改 production code
- 不重写 ~/.claude/rules/* 全局规则 (只引用)
- 每 runbook trigger / preconditions 字段必须诚实, 不许伪自动化或暗示无 risk

## §5 Live Web Evidence

非 required — 本任务是 synthesis, 不是 research. 可使用 paste-time evidence 作为 lessons learned 部分锚点.

## §6 Cross-local Search

- ~/workspace/contentflow/L/ 历史 retrospective (multi-agent 协作模式)
- ~/.claude/rules/ 全局规则
- ~/.claude/skills/ 全局 skill catalog
- ScoutFlow docs/research/ 全
- 4 run handoff + checkpoint

## §7 Output Deliverables

ZIP filename: `cloud-output-U10-prosumer-sop-runbook-library-2026-05-07.zip`
File count: **≥68** (硬下限)

| 类别 | 文件数 | min 字 / 文件 | 总字数 |
|---|---:|---:|---:|
| Cluster A Capture | ≥9 | 1500 | ≥13500 |
| Cluster B Dispatch | ≥11 | 1500 | ≥16500 |
| Cluster C Boundary | ≥9 | 1500 | ≥13500 |
| Cluster D Visual | ≥9 | 1500 | ≥13500 |
| Cluster E Memory | ≥6 | 1500 | ≥9000 |
| Cluster F Egress | ≥6 | 1500 | ≥9000 |
| Cluster G Tooling | ≥5 | 1500 | ≥7500 |
| Cluster H Recovery | ≥5 | 1500 | ≥7500 |
| Cluster index (8 cluster) | 8 | 1500 | ≥12000 |
| MASTER-RUNBOOK-INDEX | 1 | 3000 | 3000 |
| RUNBOOK-SCHEMA-CONTRACT | 1 | 1800 | 1800 |
| LINKED-RULES-INDEX | 1 | 2200 | 2200 |
| LINKED-DISPATCH-CATALOG | 1 | 2200 | 2200 |
| SELF-AUDIT-FINDINGS | 1 | 3500 | 3500 |
| README | 1 | 1500 | 1500 |
| **总计** | **≥73** | — | **≥116200** |

claim label coverage ≥90% paragraph
Mermaid: master index + 至少 4 cluster index = ≥5 张

## §8 Self-audit (Pass 9 内嵌)

≥25 findings inline fix-or-bound. 涵盖:
- runbook 是否真覆盖 4 run 实测 (vs 脑补)
- trigger 关键词是否真区分场景 (无重叠)
- precondition 是否真前置 (不漏)
- rollback path 是否真可执行 (不是声明无 risk)
- single-user vs multi-agent 标记是否准确
- linked rules 是否真存在 ~/.claude/rules/
- linked dispatch 是否对齐 U9 catalog
- 是否漂移成企业 ITIL / SRE 重型 SOP
- ContentFlow L 教训是否真嵌入 lessons (vs 复制 boilerplate)

## §9 Truthful Stdout Contract

```yaml
CLOUD_U10_PROSUMER_SOP_RUNBOOK_LIBRARY_COMPLETE: true
zip_filename: cloud-output-U10-prosumer-sop-runbook-library-2026-05-07.zip
files_count: <真实, ≥68>
total_words_cjk_latin_approx: <真实, ≥116000>
total_thinking_minutes: <真实, 不许伪造>
runbooks_count_total: <真实, ≥55>
cluster_a_capture_count: <真实>
cluster_b_dispatch_count: <真实>
cluster_c_boundary_count: <真实>
cluster_d_visual_count: <真实>
cluster_e_memory_count: <真实>
cluster_f_egress_count: <真实>
cluster_g_tooling_count: <真实>
cluster_h_recovery_count: <真实>
mermaid_diagrams_count: <真实, ≥5>
linked_rules_validated: <真实, ~/.claude/rules/* 是否真存在>
linked_dispatch_validated: <真实, 与 U9 是否真对齐>
multi_pass_completed: <真实/10>
self_audit_findings: <真实, ≥25>
critical_issues_fixed_inline: <真实>
known_limitations:
  - <列出>
boundary_preservation_check: clear
no_actual_execution_implied: confirmed
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U10-prosumer-sop-runbook-library-2026-05-07.zip` — 严格匹配

## §11 Format Guard (cloud 自检)

- `find . -name "RB-*.md" | wc -l` 期望 ≥55
- 每 runbook frontmatter 含 `status: candidate` `risk_level` `trigger_keywords[]`
- 每 runbook body 含 9 段 (mission/trigger/preconditions/steps/verification/rollback/lessons/linked/footer)
- 总字数 ≥116000
- Mermaid 块 ≥5
- 任何 runbook 未声称"无 risk" / "无 precondition"
- linked_dispatch 字段引用 U9 dispatch ID (P2-/P3-/P4-/MOD-)
- linked_rules 字段引用 `~/.claude/rules/*.md` 真实文件名
