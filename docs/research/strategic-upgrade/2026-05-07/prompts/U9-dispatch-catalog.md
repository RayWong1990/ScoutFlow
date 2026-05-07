---
title: Cloud Prompt — U9 Phase 2-4 Dispatch Catalog v0 (≥65 文件 actionable 派单库)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式 (deep-research mode preferred)
new_lane: yes (master synthesis / 最大综合任务)
expected_zip_files: 65+
expected_zip_words_cjk_latin: 110000+
expected_thinking_minutes: 180+
---

# Cloud Prompt — U9 Phase 2-4 Dispatch Catalog v0

## §1 Mission

ScoutFlow 当前已沉淀大量 candidate spec (PRD-v2/SRD-v2 + 4 run receipts + overflow-registry + 7 cluster 体系 + U1-U8 strategic upgrade 候选). 但**这些都是 spec / boundary / playbook**, 没有一个是**用户拿来就能派发给 Codex/CC/Hermes 的 ready-to-paste dispatch prompt**.

本任务: 综合所有已有 candidate, 写出 **Phase 2-4 完整 dispatch 候选库 ≥55 个 ready-to-paste prompt skeleton**, 每 dispatch 单文件, 含: mission / input URL / multi-pass plan / hard boundaries / output schema / self-audit / truthful stdout / prerequisite / can_open_X gating. 用户授权后**直接复制**即可派发.

外加 11 cluster index + 5 supporting (master roadmap / dependency graph / vendor recap / self-audit / README) = **≥71 文件**.

这是 80-pack 续作 (dispatch127-176 之后), 是 ScoutFlow 接下来 6-12 个月的执行图.

## §2 Inputs (must read)

### A. 现有 base
1. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md
2. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md
3. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md (5 overflow lane)
4. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/EXTERNAL-AUDIT-REPORT-2026-05-07.md (Run-3+4 audit)
5. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/dispatch-template.md (派单模板)
6. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/specs/contracts-index.md (contract group)
7. https://github.com/RayWong1990/ScoutFlow/blob/main/AGENTS.md
8. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/post-dispatch176-roadmap-candidate-2026-05-05.md (上一轮 roadmap)

### B. 4 run dispatch 历史 pattern (供借鉴风格)
9. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/RUN-2-CODEX0-REPORT-2026-05-06.md (Run-2 14 dispatch)
10. https://github.com/RayWong1990/ScoutFlow/tree/main/docs/research/post-frozen/runs (4 run 完整 ledger)
11. CHECKPOINT-Run3-4-final.json (24 dispatch / C1 pass / C2 partial / amend trigger)

### C. 8 个 strategic-upgrade prompt (你将依据此推断 dispatch 内容)
12. https://github.com/RayWong1990/ScoutFlow/tree/main/docs/research/strategic-upgrade/2026-05-07 (含 U1-U8 8 个 cloud-prompt + README)

### D. **如本机可访问** ~/Downloads/ 下 cloud-output ZIP (上轮成果)
13. cloud-output-U1-prd-v3-srd-v3-2026-05-07.zip (PRD-v3 / SRD-v3 candidate)
14. cloud-output-U2-phase-2-unlock-playbook-2026-05-07.zip (5 lane playbook)
15. cloud-output-U3-entity-v0-contracts-2026-05-07.zip (4 entity)

### E. Live web (recap, 不重新研究)
16. 2-month vendor / pattern recap from prompt-paste-time evidence

## §3 Multi-pass Work Plan (≥12 pass, ≥180 min wall-clock target)

1. **Pass 1 — Inventory**: 读 §2 A/B/C/D 全集, 抽出 7 cluster (PF-C0/O1/LP/C1/C2/C3/C4) + 5 new module (visual/agent/retrieval/state/egress) 的当前 state + 已 land PR # + outstanding gap

2. **Pass 2 — Phase 2-4 dimension matrix**: 
   - Phase 2 = single-lane unlock (true_vault_write / runtime_tools / browser / dbvnext / signal_workbench 任选一)
   - Phase 3 = entity v0 → v1 promote (Signal/Hypothesis/CapturePlan/TopicCard 各自)
   - Phase 4 = signal workbench + DiloFlow handoff
   - 横轴 7 cluster × 5 module = 12 dimension; 纵轴 Phase 2/3/4
   - 每 (dim, phase) cell candidate dispatch 2-5

3. **Pass 3 — Dispatch ID 命名规范**: 
   - Phase 2: `P2-<lane>-<seq>-<short-name>` 例 `P2-LANE1-01-vault-write-shadow-mode-spike`
   - Phase 3: `P3-<entity>-<seq>-<short-name>` 例 `P3-Signal-01-v0-table-creation-fixture`
   - Phase 4: `P4-<workbench>-<seq>` 例 `P4-WB-01-signal-list-readonly-preview`
   - Module: `MOD-<module>-<seq>` 例 `MOD-VISUAL-01-visual-asset-table-creation`

4. **Pass 4 — Dispatch skeleton template**: 每 dispatch 单文件 ~1500-2200 字, 含:
   - frontmatter (status / authority / phase / cluster / parent_dispatch_id / prerequisites / can_open_C4 / can_open_runtime / can_open_migration)
   - § Mission (1 段, 1 句话定义)
   - § Inputs (3-8 URL specific)
   - § Multi-pass Plan (≥5 pass)
   - § Hard Boundaries (write_enabled / 5 overflow / authority files / 不解禁红线)
   - § Output Deliverables (file count / 字数 / claim label coverage)
   - § Self-audit Requirements (≥5 finding)
   - § Truthful Stdout Contract (verdict ∈ {clear/concern/reject/partial} + amend trigger fields)
   - § PR Pattern (单 PR / packed / amendment 选择)
   - § Verification Method (audit window / 3-window / informal)

5. **Pass 5 — Phase 2 dispatch authoring (~22 dispatch)**:
   - LANE-1 true_vault_write: 4-5 dispatch (shadow mode spike / metadata-only commit / dry-run validation / true-write gate / rollback rehearsal)
   - LANE-2 runtime_tools sub-lanes: 5-7 dispatch (BBDown metadata-only / yt-dlp legal recheck / Whisper local install / faster-whisper benchmark / Voxtral spike / ASR sandbox / LLM normalization fixture)
   - LANE-3 browser_automation: 3-4 dispatch (Playwright sandbox / human screenshot verdict / browser profile isolation / login-required gate)
   - LANE-4 dbvnext_migration: 3-4 dispatch (fixture migration rollback / schema evolution v0 / single migration script / consumer-pin abandon)
   - LANE-5 signal_workbench: 3-4 dispatch (URL usefulness verdict / read-only preview / candidate-only dispatch UI / LP-001 risk recheck)

6. **Pass 6 — Phase 3 dispatch authoring (~12 dispatch)**:
   - Signal v0 → v1: 3 dispatch (table creation fixture / sample backfill / migration test set)
   - Hypothesis v0 → v1: 3 dispatch
   - CapturePlan v0 → v1: 3 dispatch
   - TopicCard v0 → v1 → v2: 3 dispatch (含 lite v0 → v1 promotion 已半 land)

7. **Pass 7 — Phase 4 dispatch authoring (~10 dispatch)**:
   - Signal Workbench full mode: 4 dispatch (recommendation engine / candidate dispatch UI / batch capture / scope gate enforce)
   - DiloFlow handoff: 3 dispatch (egress contract impl / manifest publish / supersede protocol)
   - hermes-agent integration: 2 dispatch
   - cross-system test set: 1 dispatch

8. **Pass 8 — Module dispatch authoring (~12 dispatch)**:
   - U4 visual_asset / prompt_template / design_token / pattern_library: 4 dispatch
   - U5 agent_fleet_ledger / cost_attribution: 2 dispatch  
   - U6 visual-DAM / hybrid-search: 2 dispatch
   - U7 state-library / 5-gate-automation: 2 dispatch
   - U8 4 egress contract impl: 2 dispatch

9. **Pass 9 — 11 cluster index files**: 每 cluster 一个 markdown index (PF-C0 / O1 / LP / C1 / C2 / C3 / C4 / visual / agent / retrieval / egress + state-library), 含: cluster mission / current state (已 land PR + outstanding) / dispatch 清单 + 顺序 / cross-cluster dependency / can_open gating

10. **Pass 10 — 5 supporting files**: 
    - MASTER-ROADMAP-PHASE-2-4-2026-05-07.md (12-month execution map)
    - CROSS-CLUSTER-DEPENDENCY-GRAPH-2026-05-07.md (Mermaid 大图)
    - VENDOR-PATTERN-RECAP-2026-05-07.md (paste-time recap, 不重新 research)
    - SELF-AUDIT-FINDINGS-2026-05-07.md (≥30 issue inline fixed)
    - README-deliverable-index-2026-05-07.md

11. **Pass 11 — Cross-dispatch lineage**: 每 dispatch 标 prerequisites (依赖哪个 dispatch 先 land) + 阻挡哪些后续 dispatch + can_open_X gating

12. **Pass 12 — Format guard + truthful stdout**: 文件数 / 字数 / claim label / Mermaid / boundary preservation 全过

## §4 Hard Boundaries (硬红线)

- candidate / not-authority frontmatter 全 ≥71 文件强制
- write_enabled=False 不变 (本 ZIP 不解禁任何 lane)
- 不批准任何 dispatch 实际派发 — **dispatch prompt 仅 candidate, 等用户授权才能派**
- authority files (current.md / task-index.md / decision-log.md / AGENTS.md) 不写
- 5 overflow lane Hold 不变 (dispatch 写"unlock spike"也是 candidate, 不实际 unlock)
- 不修改 production code (services/** apps/** workers/** packages/** 仍 hold)
- 不引入新 vendor 作为"已采纳"
- 每 dispatch 必须有 can_open_C4 / can_open_runtime / can_open_migration 显式 false 字段, 防止意外暗示 unlock

## §5 Live Web Evidence (paste-time recap, 不重新 research)

本任务**不要求** live web — 因为是 synthesis 任务。可使用 prompt §2 D ZIP 内嵌的 paste-time evidence 作为 vendor / pattern recap。VENDOR-PATTERN-RECAP-2026-05-07.md 文件单独整合 ≥20 vendor / pattern, 标 [paste-time-from-U1-U8].

如环境支持 live web, 可 refresh 关键 vendor (Bilibili 法务 / Whisper / yt-dlp), 但**非强制**。

## §6 Cross-local Search

不 required (本任务是综合, 不是新 research)。

## §7 Output Deliverables (严格 schema)

ZIP filename: `cloud-output-U9-phase-2-4-dispatch-catalog-v0-2026-05-07.zip`
File count: **≥71** (硬下限)

| 类别 | 文件数 | min 字 / 文件 | 总字数 |
|---|---:|---:|---:|
| Phase 2 dispatch (LANE 1-5) | ≥22 | 1500 | ≥33000 |
| Phase 3 dispatch (4 entity v0→v1) | ≥12 | 1500 | ≥18000 |
| Phase 4 dispatch (workbench / handoff) | ≥10 | 1500 | ≥15000 |
| Module dispatch (U4-U8 5 module) | ≥12 | 1500 | ≥18000 |
| Cluster index (11 cluster) | 11 | 1800 | ≥19800 |
| MASTER-ROADMAP | 1 | 4000 | 4000 |
| CROSS-CLUSTER-DEPENDENCY-GRAPH | 1 | 2000 + Mermaid | 2000 |
| VENDOR-PATTERN-RECAP | 1 | 3500 | 3500 |
| SELF-AUDIT-FINDINGS (≥30 issue) | 1 | 4000 | 4000 |
| README-deliverable-index | 1 | 1500 | 1500 |
| **总计** | **≥71** | — | **≥118800** |

claim label coverage ≥90% paragraph 全文件
Mermaid: master roadmap + dependency graph + 至少 5 cluster index 共 ≥7 张

## §8 Self-audit (Pass 12)

≥30 findings, 每条 inline fix-or-bound. 涵盖:
- 是否暗示任何 dispatch 已授权 (必须仍 candidate)
- 是否绕过 5 overflow lane Hold 红线
- dispatch 顺序 prerequisite 是否真合理 (无环依赖)
- 每 dispatch boundary 是否真覆盖 (write_enabled / authority / overflow)
- can_open_X 字段是否每文件都 false
- claim label coverage 是否真 ≥90%
- ≥71 文件 count 是否准确
- vendor 是否仍 candidate, 无"已采纳"漂移
- 与 8 strategic-upgrade prompt (U1-U8) 是否冲突
- module dispatch 是否依赖 U4-U8 ZIP land 才能跑

## §9 Truthful Stdout Contract

输出 README §5 必须含:
```yaml
CLOUD_U9_PHASE_2_4_DISPATCH_CATALOG_COMPLETE: true
zip_filename: cloud-output-U9-phase-2-4-dispatch-catalog-v0-2026-05-07.zip
files_count: <真实数, ≥71>
total_words_cjk_latin_approx: <真实, ≥118000>
total_thinking_minutes: <真实, 不许伪造>
phase_2_dispatch_count: <真实>
phase_3_dispatch_count: <真实>
phase_4_dispatch_count: <真实>
module_dispatch_count: <真实>
cluster_index_count: <真实, 期望 11>
mermaid_diagrams_count: <真实, ≥7>
multi_pass_completed: <真实/12>
self_audit_findings: <真实, ≥30>
critical_issues_fixed_inline: <真实>
known_limitations:
  - <列出, 例如 wall-clock 不足 / paste-time evidence 未 refresh>
boundary_preservation_check: clear
all_dispatch_can_open_flags_false: confirmed
no_actual_authorization_implied: confirmed
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U9-phase-2-4-dispatch-catalog-v0-2026-05-07.zip` — 严格匹配

## §11 Format Guard (cloud 自检)

完成后自跑 (or 描述如何跑):
- `find . -name "*.md" | wc -l` 期望 ≥71
- 每文件 frontmatter 含 `status: candidate` 和 `not-authority`
- 每 dispatch frontmatter 含 `can_open_C4: false` `can_open_runtime: false` `can_open_migration: false`
- 总字数 ≥118000 (CJK 字符 + Latin token)
- Mermaid 块 ≥7
- README 含完整 stdout contract
- 任何 vendor 未出现"已采纳" / "已批准" / "已解禁" 字样
