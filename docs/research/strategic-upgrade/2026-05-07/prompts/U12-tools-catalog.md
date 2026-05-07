---
title: Cloud Prompt — U12 Skills + Tools + MCP + Plugin Complete Catalog v0 (≥80 文件)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
expected_zip_files: 80+
expected_zip_words_cjk_latin: 110000+
expected_thinking_minutes: 150+
---

# Cloud Prompt — U12 Skills + Tools + MCP + Plugin Catalog

## §1 Mission

用户在 Claude Code / Codex / Hermes / OpenClaw 多 AI fleet 模式下累积大量 skill / agent / tool / MCP server / plugin / hook / cron / cc-resilient.sh / 自定义 script. 这些**事实运转**但**没有结构化 catalog**, 用户每次找工具 / 写新 skill 时不知道是否已存在 / 是否有重叠 / 跨工具如何协同.

本任务: 把全工具链结构化为 **≥70 个 single-file catalog entry**, 每 entry = 一个 skill/agent/tool/MCP/plugin/hook 完整描述. 加 cross-tool collaboration graph + skill evolution timeline + redundancy/conflict detection + 跨域调用 example.

外加 8 cluster index + 5 supporting = **≥83 文件**.

## §2 Inputs

### A. ~/.claude/ 全 catalog
1. ~/.claude/skills/ (全 skill .md, 含 learned/ 和 system 默认)
2. ~/.claude/agents/ (全 agent .md)
3. ~/.claude/rules/ (全 rule .md, 引用不重写)
4. ~/.claude/plugins/ (各 plugin marketplace)
5. ~/.claude/projects/-Users-wanglei-workspace-ScoutFlow/memory/ (skill 演化记忆)
6. ~/.claude/scripts/ (cc-resilient.sh / pre/post hook scripts)
7. ~/.claude/settings.json (env / hooks 注册)
8. ~/.claude/CLAUDE.md (用户全局 CLAUDE)
9. ~/.codex/ (Codex CLI 配置 + skills)

### B. ECC + superpowers + claude-mem + 其他 plugin
10. ~/.claude/plugins/cache/everything-claude-code/ (skills/agents/hooks/commands)
11. ~/.claude/plugins/cache/superpowers/ (brainstorming / writing-plans / executing-plans)
12. claude-mem v12.1.0 (9 hooks / 7 events / SQLite + ChromaDB)
13. dx skill (clone/handoff/gha)

### C. MCP servers (settings.json 注册)
14. github / supabase / firecrawl / context7 / exa / playwright / sequential-thinking / engram / notion / claude-mem / etc

### D. ScoutFlow features (~/.claude/projects/.../skills 项目级)
15. ~/workspace/ScoutFlow/ 项目级 skill (如有)

## §3 Multi-pass Work Plan (≥10 pass, ≥150 min)

1. **Pass 1 — Inventory scan**: 跨 §2 A-D 全 ls + 读 frontmatter, 统计总数 (skill / agent / tool / MCP / plugin / hook / script)
2. **Pass 2 — Schema 设计**: 每 entry 单文件 ~1300-1600 字, frontmatter (entry_id / kind ∈ {skill/agent/tool/mcp/plugin/hook/script/cron} / source ∈ {global/plugin/project/cli} / activation ∈ {manual/auto/hook/keyword} / cost_per_invoke / risk_level / dependencies / linked_rules), body 含 9 段 (mission / when_to_use / when_not_to_use / activation_method / parameters / output / cost / lessons / linked)
3. **Pass 3 — Cluster A: Global Skills (~15-20 entry)**: ~/.claude/skills/learned/ + system 默认 skill 全
4. **Pass 4 — Cluster B: Agents (~20)**: planner / architect / tdd-guide / code-reviewer / build-error-resolver / e2e-runner / refactor-cleaner / doc-updater / 中书令/工部/刑部 etc
5. **Pass 5 — Cluster C: Plugins (~10)**: ECC (32 skills + 17 hooks + agents) / superpowers (brainstorming/writing-plans/executing-plans) / claude-mem (memory) / dx / 其他
6. **Pass 6 — Cluster D: MCP Servers (~15)**: github / supabase / firecrawl / context7 / exa / playwright / sequential-thinking / engram / notion / claude-mem / iflytek / etc
7. **Pass 7 — Cluster E: Hooks (~10)**: PreToolUse / PostToolUse / Stop / SessionStart / SessionEnd / PreCompact 各事件 hook
8. **Pass 8 — Cluster F: Scripts (~10)**: cc-resilient.sh / token-threshold / sedimentation / observe / quality-gate / etc
9. **Pass 9 — Cluster G: Codex CLI Skills (~5)**: ixf-* / brainstorm-five-lens (Codex pointer) / 其他
10. **Pass 10 — Cluster H: Cross-tool collaboration**: 多工具协同 graph (Mermaid 大图) + 跨域调用 example + redundancy/conflict detection + skill evolution timeline + 每 cluster index + master + linked-rules + linked-runbook + README + truthful stdout

## §4 Hard Boundaries

- candidate / not-authority frontmatter 全 ≥83 文件
- 不修改 ~/.claude/skills / agents / rules / plugins / hooks 任何文件 (只读 + catalog)
- 不修改 ~/.codex/ 任何
- 不修改 settings.json
- 不实际执行任何 skill/agent/tool — 仅 catalog
- 不暴露 ~/.claude/settings.json 中可能含的 secret (API key / token, 必须 mask)
- 用户全局 CLAUDE.md / AGENTS.md 私有内容 redaction (个人偏好 OK, 凭据/路径敏感信息 mask)

## §5 Live Web Evidence

非 required — synthesis 任务. 但可 refresh: ECC 1.10.0 changelog / claude-mem 12.1.0 / superpowers latest / MCP server registry 2026-05.

## §6 Cross-local Search

- ~/.claude/ 全递归 (skill / agent / rule / plugin / hook / script)
- ~/.codex/ 全
- ~/Library/Application Support/Claude/ (如有)
- which / brew list / pip list 验证本机 CLI 工具
- ScoutFlow 项目级 skill (~/workspace/ScoutFlow/.claude/ 如有)

## §7 Output Deliverables

ZIP filename: `cloud-output-U12-skills-tools-mcp-plugin-catalog-2026-05-07.zip`
File count: **≥83**

| 类别 | 文件数 | min 字 |
|---|---:|---:|
| Cluster A Global Skills | ≥15 | 1300 |
| Cluster B Agents | ≥18 | 1300 |
| Cluster C Plugins | ≥8 | 1300 |
| Cluster D MCP Servers | ≥12 | 1300 |
| Cluster E Hooks | ≥8 | 1300 |
| Cluster F Scripts | ≥8 | 1300 |
| Cluster G Codex CLI Skills | ≥5 | 1300 |
| Cluster H Cross-tool examples | ≥6 | 1500 |
| Cluster index (8) | 8 | 1500 |
| MASTER-CATALOG-INDEX | 1 | 3000 |
| CROSS-TOOL-COLLABORATION-GRAPH | 1 | 2200 (Mermaid) |
| REDUNDANCY-CONFLICT-DETECTION | 1 | 2000 |
| SKILL-EVOLUTION-TIMELINE | 1 | 2000 |
| LINKED-RULES-AND-RUNBOOKS | 1 | 2000 |
| README | 1 | 1500 |
| **总计** | **≥94** | ≥120000 |

claim label coverage ≥85%; Mermaid ≥4

## §8 Self-audit (≥25)

- 每 entry source path 真实 (本机存在)
- secret / API key 真 mask
- redundancy 是否真识别 (e.g. ECC code-reviewer vs 全局 code-reviewer)
- conflict 是否真识别 (parallel-safety / hook 冲突)
- cross-tool example 是否真可执行
- 与 U10 runbook (linked_tools 字段) 双向映射
- 与 ~/.claude/rules/* 引用是否真存在
- 隐私: 用户 CLAUDE.md 个人偏好 OK / 凭据 mask
- 单人 prosumer 工具链 vs 企业 tool sprawl

## §9 Truthful Stdout Contract

```yaml
CLOUD_U12_SKILLS_TOOLS_MCP_PLUGIN_CATALOG_COMPLETE: true
zip_filename: cloud-output-U12-skills-tools-mcp-plugin-catalog-2026-05-07.zip
files_count: <真实, ≥83>
total_words_cjk_latin_approx: <真实, ≥110000>
total_thinking_minutes: <真实>
entries_count_total: <真实, ≥70>
skills_count: <真实>
agents_count: <真实>
plugins_count: <真实>
mcp_servers_count: <真实>
hooks_count: <真实>
scripts_count: <真实>
codex_skills_count: <真实>
cross_tool_examples: <真实>
redundancy_conflicts_detected: <真实>
secrets_masked: confirmed
multi_pass_completed: <真实/10>
self_audit_findings: <真实, ≥25>
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U12-skills-tools-mcp-plugin-catalog-2026-05-07.zip`

## §11 Format Guard

- 每 entry frontmatter 含 `entry_id` `kind` `source` `activation` `risk_level`
- secret regex scan (api_key|token|sk-|eyJ|Bearer) 命中即 mask
- linked_runbook (U10) / linked_dispatch (U9) / linked_anti_pattern (U11) cross-link 字段填
