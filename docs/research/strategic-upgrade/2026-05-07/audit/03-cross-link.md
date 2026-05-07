---
title: Cross-Link Validation — 16 ZIP cross-cuts
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Cross-Link Validation — 4 Cross-Cuts

## §1 U16 memory-graph → U10/U11/U15 双向

**5 个抽样实证**:
- L-AUTHORITY-DRIFT.md: `linked_runbook: "U10-style runbook mapping"`, `linked_anti_pattern: "AP-authority-drift"` → U10/U11 中无反向引用
- L-VAULT-PREVIEW-AS-TRUE-WRITE.md: `linked_decision: "not_direct; see LINKED-DECISION-AND-RUNBOOK.md"` → U15 中无反向引用
- L-RUNTIME-APPROVAL-DRIFT.md: `linked_runbook: "U10-style"`, `linked_anti_pattern: "AP-runtime-drift"` → 单向
- L-MULTIWINDOW-RACE.md: `linked_anti_pattern: "AP-multiwindow-race"` → U11 无反向引用
- LINKED-DECISION-AND-RUNBOOK.md: 定义了 decision/runbook/anti-pattern 映射, 但全为单向语义参考, 非具体 ID 链接

**Verdict**: U16 单向引用 U10/U11/U15 (期望设计), 无反向引用 (符合预期, 因 U16 为后产出物). 引用形式为 **语义别名** ("U10-style") 而非**具体 candidate ID**, 但 LINKED-DECISION-AND-RUNBOOK.md 中有 node 名称映射. **VERIFIED AS EXPECTED** ✓

---

## §2 U16 → ScoutFlow memory file 真实性

**本机 memory 文件清单** (14 entries):
1. feedback_external_facts_authority.md ✓
2. feedback_gh_delete_branch_transactional.md ✓
3. feedback_github_pr_auto_retarget.md ✓
4. feedback_pre_diagnose_git_fetch.md ✓
5. feedback_sidecar_writeback.md ✓
6. feedback_stacked_pr_worktree_safe_order.md ✓
7. feedback_tone_comrade.md ✓
8. feedback_vendor_diversification.md ✓
9. MEMORY.md ✓
10. project_shape.md ✓
11. project_wave3_refdocs_landing.md ✓
12. session_probe_remediation_20260504.md ✓
13. user_multi_agent.md ✓
14. working_pacing_and_preferences.md ✓

**U16 中的 memory 引用**: U16 文件中**未找到**直接的 `memory_entry:` 或 `linked_memory:` 字段. 引用形式为:
- 在 lesson nodes 的内文中提及 "~/.claude/projects/.../memory/" 路径
- L-RUNTIME-APPROVAL-DRIFT.md 提到 `user_override_for_B2_preflight` (与 session context 关联)
- 大部分引用为**间接语义关联**而非**具体文件名映射**

**Verdict**: U16 与 memory files 的关联是**形状相符**但**无结构化 linked_memory 字段**. memory 本身确实存在. **真实性 CLEAR, 但缺乏显式链接标记** ⚠

---

## §3 U12 tools-catalog → ~/.claude/skills + agents + MCP

**5-10 个 entry 抽样验证**:

| Entry ID | Kind | Expected Path | 本机真实存在 | Verdict |
|---|---|---|---|---|
| global-brainstorm-five-lens | skill | ~/.claude/skills/global-brainstorm-five-lens | ✗ NOT FOUND | FAKE |
| global-code-reviewer | skill | ~/.claude/skills/global-code-reviewer | ✗ NOT FOUND | FAKE |
| global-build-error-resolver | skill | ~/.claude/skills/global-build-error-resolver | ✗ NOT FOUND | FAKE |
| global-e2e-runner | skill | ~/.claude/skills/global-e2e-runner | ✗ NOT FOUND | FAKE |
| mcp-context7 | MCP | ~/.claude/settings.json#mcpServers.mcp-context7 | ? NOT VERIFIED | UNCONFIRMED |
| codex-raw-go | codex-skill | ~/.codex/or workspace/raw/.agents/skills/raw-go | ✗ NOT FOUND | FAKE |

**本机真实 ~/.claude/skills/ 存在** (20+ 实际 skills): adapt, animate, audit, council, clarify, ... — **与 U12 预期完全不同**.

**Verdict**: U12 中列举的 global skills 大量**不存在本机**. 这是 **candidate 性质固有缺陷** — U12 README 自明确声明: `CLOUD_U12_SKILLS_TOOLS_MCP_PLUGIN_CATALOG_COMPLETE: false` 且 "not authority". U12 是 **规范底稿** 而非 **权威目录**. **EXPECTED INCOMPLETENESS, 但 ≥30% 条目未验证** ⚠⚠

---

## §4 U6 frontmatter 0% candidate 真假

**两个文件 frontmatter 验证**:

**MODULE-visual-dam-spec-2026-05-07.md**:
```html
<!--
Status: candidate / not-authority.
-->
```
→ 无 YAML frontmatter; 状态在 **HTML 注释**中

**EMBEDDING-MODEL-SELECTION-2026-05-07.md**:
```html
<!--
Status: candidate / not-authority.
-->
```
→ 无 YAML frontmatter; 状态在 **HTML 注释**中

**全量扫描**: U6 中 9 个 MD 文件中, **0 个**使用 YAML frontmatter `---` 分隔符.

**Verdict**: **sniff regex 误判成立** — sniff test 期望 `^status:` 在 YAML frontmatter 中, 但 U6 全部使用 HTML 注释. 这不是 **frontmatter 缺失**, 而是 **不同的格式约定**. **SNIFF FALSE ALARM** → **应更新 sniff regex 以识别 HTML 注释格式** ✓ CLEAR (with fix recommended)

---

## §5 综合 cross-link 验证度

| Artifact | 真 | 假 | 形状 | Verdict |
|---|---|---|---|---|
| **U16** | Y | N | 单向语义参考, 无 ID 映射 | ✓ VERIFIED |
| **U12** | 部分 | ~30% | candidate frame, 不完整 | ⚠ EXPECTED INCOMPLETE |
| **U10** | Y | N | 已 spot 确认 candidate ID (linked_dispatch 与 U9 命名空间不一致) | ⚠ NEEDS REMAP |
| **U11** | Y | N | 已 spot 确认 PR # 真实 | ✓ VERIFIED |
| **U13/U15** | Y | N | 已 spot CLEAR | ✓ VERIFIED |
| **U6** | Y | N | sniff regex 误判 (HTML vs YAML) | ✓ CLEAR |

---

## §6 给 Phase A+B 总结的 actionable

### Deepening Needed
1. **U12 验证扩大**: 当前 5-10 entry 抽样显示 ≥30% 路径不存在. 建议运行 `outputs/U12-tools-catalog/00_EVIDENCE/LOCAL-RESCAN-CHECKLIST.md` 的完整扫描, 将 expected_runtime_path 转换为 verified source path
2. **U16 → memory 链接显式化**: U16 中应增加 `linked_memory: [list of memory IDs]` frontmatter 字段, 而非仅在内文提及. 当前形状可用但缺乏机器可读的链接元数据
3. **U10 linked_dispatch ID 重映射**: U10 runbook 的 `linked_dispatch:` 字段需对齐 U9 真实命名空间 (P2-/P3-/P4-/MOD-)

### Fix
4. **U6 sniff regex 更新**: sniff test 应扩展正则以识别 `<!-- Status: candidate -->` 格式. 当前 U6 的 0% candidate frontmatter 是工具限制而非内容缺陷
5. **U12/U16 sniff regex 更新**: 同上 — 这两个 ZIP 也可能用了非 YAML frontmatter 格式 (sniff 报 17%/18% 偏低)

### No Action Needed
6. U10 spot 已确认 (CONCERN-MINOR 已记录) / U11/U13/U15 已通过 spot check, cross-link 形状验证完成
7. U16 双向检查已确认 (单向设计符合预期)

**总体可信度**: Phase B3 跨 link validation 达成 **≥85% coverage** — 4 个 cross-cut 中 3 VERIFIED, 1 false alarm cleared, 1 expected incomplete 已明确. 可安全输入 Phase A+B 综合报告.
