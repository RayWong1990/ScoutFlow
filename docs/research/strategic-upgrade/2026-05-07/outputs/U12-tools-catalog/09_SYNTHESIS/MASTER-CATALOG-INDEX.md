---
title: Master Catalog Index
status: candidate / evidence-bounded / not-authority
created_at: 2026-05-06
entries_count_total: 97
---

# Master Catalog Index

## Executive Finding

本包产出的是 U12 的“证据边界版 catalog”：文件数量、cluster 架构、frontmatter schema、cross-tool graph、redundancy/conflict、timeline 和 self-audit 均已落地；但它不声称完成原 prompt 所需的真实本机 `~/.claude` / `~/.codex` 全量扫描。根因是运行环境没有这些目录。本包最适合用作下一步本地复扫的审计底稿、迁移蓝图和冲突发现模板。

## Counts

| Dimension | Count |
|---|---:|
| Total catalog entries | 97 |
| Cluster A Global Skills | 18 |
| Cluster B Agents | 20 |
| Cluster C Plugins | 10 |
| Cluster D MCP Servers | 15 |
| Cluster E Hooks | 10 |
| Cluster F Scripts | 10 |
| Cluster G Codex CLI Skills | 8 |
| Cluster H Cross-tool Examples | 6 |

## Why this catalog exists

在 Claude Code / Codex / Hermes / OpenClaw 多 AI fleet 中，用户的实际问题不是缺少工具，而是缺少一个能回答“该用哪个、何时不用、和谁冲突、谁负责写 authority”的结构化目录。U12 prompt 把这个问题定义为 toolchain catalog：每个 entry 都要单文件、带 schema、带风险、带 linked rules，并配合协作图、演化时间线和冗余检测。本包严格保留这些治理形状，同时把证据状态写明，避免把未验证路径包装成事实。

## Entry Table

| Cluster | entry_id | kind | risk | activation | file |
|---|---|---|---|---|---|
| A | global-code-reviewer | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/01-global-code-reviewer.md` |
| A | global-build-error-resolver | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/02-global-build-error-resolver.md` |
| A | global-e2e-runner | skill | high | manual/tool-assisted | `01_CLUSTER_A_GLOBAL_SKILLS/03-global-e2e-runner.md` |
| A | global-tdd-guide | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/04-global-tdd-guide.md` |
| A | global-refactor-cleaner | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/05-global-refactor-cleaner.md` |
| A | global-doc-updater | skill | low | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/06-global-doc-updater.md` |
| A | global-brainstorm-five-lens | skill | low | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/07-global-brainstorm-five-lens.md` |
| A | global-writing-plan | skill | low | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/08-global-writing-plan.md` |
| A | global-executing-plan | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/09-global-executing-plan.md` |
| A | global-context-loader | skill | low | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/10-global-context-loader.md` |
| A | global-source-verifier | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/11-global-source-verifier.md` |
| A | global-vault-lint | skill | low | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/12-global-vault-lint.md` |
| A | global-wiki-compile | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/13-global-wiki-compile.md` |
| A | global-export-pdf | skill | medium | manual/tool-assisted | `01_CLUSTER_A_GLOBAL_SKILLS/14-global-export-pdf.md` |
| A | global-deep-intake | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/15-global-deep-intake.md` |
| A | global-solution-writer | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/16-global-solution-writer.md` |
| A | global-ux-ia-review | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/17-global-ux-ia-review.md` |
| A | global-quality-gate | skill | medium | manual/keyword | `01_CLUSTER_A_GLOBAL_SKILLS/18-global-quality-gate.md` |
| B | agent-planner | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/01-agent-planner.md` |
| B | agent-architect | agent | high | manual/delegated | `02_CLUSTER_B_AGENTS/02-agent-architect.md` |
| B | agent-code-reviewer | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/03-agent-code-reviewer.md` |
| B | agent-build-error-resolver | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/04-agent-build-error-resolver.md` |
| B | agent-e2e-runner | agent | high | manual/delegated | `02_CLUSTER_B_AGENTS/05-agent-e2e-runner.md` |
| B | agent-refactor-cleaner | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/06-agent-refactor-cleaner.md` |
| B | agent-doc-updater | agent | low | manual/delegated | `02_CLUSTER_B_AGENTS/07-agent-doc-updater.md` |
| B | agent-tdd-guide | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/08-agent-tdd-guide.md` |
| B | agent-product-strategist | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/09-agent-product-strategist.md` |
| B | agent-audit-lens | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/10-agent-audit-lens.md` |
| B | agent-qa-gatekeeper | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/11-agent-qa-gatekeeper.md` |
| B | agent-dispatch-commander | agent | high | manual/delegated | `02_CLUSTER_B_AGENTS/12-agent-dispatch-commander.md` |
| B | agent-zhongshuling | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/13-agent-zhongshuling.md` |
| B | agent-gongbu | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/14-agent-gongbu.md` |
| B | agent-xingbu | agent | medium | manual/delegated | `02_CLUSTER_B_AGENTS/15-agent-xingbu.md` |
| B | agent-raw-review-router | agent | medium | manual/keyword | `02_CLUSTER_B_AGENTS/16-agent-raw-review-router.md` |
| B | agent-raw-watchtower | agent | low | manual/keyword | `02_CLUSTER_B_AGENTS/17-agent-raw-watchtower.md` |
| B | agent-raw-ops-console | agent | low | manual/keyword | `02_CLUSTER_B_AGENTS/18-agent-raw-ops-console.md` |
| B | agent-raw-memory-governor | agent | medium | manual/keyword | `02_CLUSTER_B_AGENTS/19-agent-raw-memory-governor.md` |
| B | agent-raw-gui-bridge | agent | high | manual/keyword | `02_CLUSTER_B_AGENTS/20-agent-raw-gui-bridge.md` |
| C | plugin-everything-claude-code | plugin | high | auto/plugin-cache | `03_CLUSTER_C_PLUGINS/01-plugin-everything-claude-code.md` |
| C | plugin-superpowers | plugin | medium | manual/keyword | `03_CLUSTER_C_PLUGINS/02-plugin-superpowers.md` |
| C | plugin-claude-mem | plugin | high | hook/auto | `03_CLUSTER_C_PLUGINS/03-plugin-claude-mem.md` |
| C | plugin-dx | plugin | medium | manual/keyword | `03_CLUSTER_C_PLUGINS/04-plugin-dx.md` |
| C | plugin-github-app | plugin | medium | manual/tool | `03_CLUSTER_C_PLUGINS/05-plugin-github-app.md` |
| C | plugin-playwright-automation | plugin | high | manual/tool | `03_CLUSTER_C_PLUGINS/06-plugin-playwright-automation.md` |
| C | plugin-context7-docs | plugin | medium | manual/tool | `03_CLUSTER_C_PLUGINS/07-plugin-context7-docs.md` |
| C | plugin-exa-research | plugin | medium | manual/tool | `03_CLUSTER_C_PLUGINS/08-plugin-exa-research.md` |
| C | plugin-firecrawl-ingestion | plugin | medium | manual/tool | `03_CLUSTER_C_PLUGINS/09-plugin-firecrawl-ingestion.md` |
| C | plugin-notion-bridge | plugin | medium | manual/tool | `03_CLUSTER_C_PLUGINS/10-plugin-notion-bridge.md` |
| D | mcp-github | mcp | medium | manual/tool | `04_CLUSTER_D_MCP_SERVERS/01-mcp-github.md` |
| D | mcp-supabase | mcp | high | manual/tool | `04_CLUSTER_D_MCP_SERVERS/02-mcp-supabase.md` |
| D | mcp-firecrawl | mcp | medium | manual/tool | `04_CLUSTER_D_MCP_SERVERS/03-mcp-firecrawl.md` |
| D | mcp-context7 | mcp | medium | manual/tool | `04_CLUSTER_D_MCP_SERVERS/04-mcp-context7.md` |
| D | mcp-exa | mcp | medium | manual/tool | `04_CLUSTER_D_MCP_SERVERS/05-mcp-exa.md` |
| D | mcp-playwright | mcp | high | manual/tool | `04_CLUSTER_D_MCP_SERVERS/06-mcp-playwright.md` |
| D | mcp-sequential-thinking | mcp | low | manual/tool | `04_CLUSTER_D_MCP_SERVERS/07-mcp-sequential-thinking.md` |
| D | mcp-engram | mcp | medium | manual/tool | `04_CLUSTER_D_MCP_SERVERS/08-mcp-engram.md` |
| D | mcp-notion | mcp | medium | manual/tool | `04_CLUSTER_D_MCP_SERVERS/09-mcp-notion.md` |
| D | mcp-claude-mem | mcp | high | hook/tool | `04_CLUSTER_D_MCP_SERVERS/10-mcp-claude-mem.md` |
| D | mcp-iflytek | mcp | medium | manual/tool | `04_CLUSTER_D_MCP_SERVERS/11-mcp-iflytek.md` |
| D | mcp-filesystem | mcp | high | manual/tool | `04_CLUSTER_D_MCP_SERVERS/12-mcp-filesystem.md` |
| D | mcp-sqlite-chroma | mcp | high | manual/tool | `04_CLUSTER_D_MCP_SERVERS/13-mcp-sqlite-chroma.md` |
| D | mcp-browser-research | mcp | high | manual/tool | `04_CLUSTER_D_MCP_SERVERS/14-mcp-browser-research.md` |
| D | mcp-slack-or-chatops | mcp | medium | manual/tool | `04_CLUSTER_D_MCP_SERVERS/15-mcp-slack-or-chatops.md` |
| E | hook-pretooluse | hook | high | hook/auto | `05_CLUSTER_E_HOOKS/01-hook-pretooluse.md` |
| E | hook-posttooluse | hook | high | hook/auto | `05_CLUSTER_E_HOOKS/02-hook-posttooluse.md` |
| E | hook-stop | hook | medium | hook/auto | `05_CLUSTER_E_HOOKS/03-hook-stop.md` |
| E | hook-sessionstart | hook | medium | hook/auto | `05_CLUSTER_E_HOOKS/04-hook-sessionstart.md` |
| E | hook-sessionend | hook | medium | hook/auto | `05_CLUSTER_E_HOOKS/05-hook-sessionend.md` |
| E | hook-precompact | hook | medium | hook/auto | `05_CLUSTER_E_HOOKS/06-hook-precompact.md` |
| E | hook-userpromptsubmit | hook | medium | hook/auto | `05_CLUSTER_E_HOOKS/07-hook-userpromptsubmit.md` |
| E | hook-notification | hook | low | hook/auto | `05_CLUSTER_E_HOOKS/08-hook-notification.md` |
| E | hook-subagentstop | hook | medium | hook/auto | `05_CLUSTER_E_HOOKS/09-hook-subagentstop.md` |
| E | hook-prefilewritegate | hook | high | hook/auto | `05_CLUSTER_E_HOOKS/10-hook-prefilewritegate.md` |
| F | script-cc-resilient | script | medium | manual/script | `06_CLUSTER_F_SCRIPTS/01-script-cc-resilient.md` |
| F | script-context-threshold | script | medium | cron/script | `06_CLUSTER_F_SCRIPTS/02-script-context-threshold.md` |
| F | script-sedimentation | script | low | cron/script | `06_CLUSTER_F_SCRIPTS/03-script-sedimentation.md` |
| F | script-observe | script | low | manual/script | `06_CLUSTER_F_SCRIPTS/04-script-observe.md` |
| F | script-quality-gate | script | medium | manual/script | `06_CLUSTER_F_SCRIPTS/05-script-quality-gate.md` |
| F | script-parallel-safety-check | script | high | manual/script | `06_CLUSTER_F_SCRIPTS/06-script-parallel-safety-check.md` |
| F | script-handoff-writer | script | low | manual/script | `06_CLUSTER_F_SCRIPTS/07-script-handoff-writer.md` |
| F | script-pack-builder | script | medium | manual/script | `06_CLUSTER_F_SCRIPTS/08-script-pack-builder.md` |
| F | script-secret-masker | script | high | manual/script | `06_CLUSTER_F_SCRIPTS/09-script-secret-masker.md` |
| F | script-stdout-auditor | script | low | manual/script | `06_CLUSTER_F_SCRIPTS/10-script-stdout-auditor.md` |
| G | codex-raw-go | skill | medium | manual/keyword | `07_CLUSTER_G_CODEX_CLI_SKILLS/01-codex-raw-go.md` |
| G | codex-raw-context | skill | low | manual/keyword | `07_CLUSTER_G_CODEX_CLI_SKILLS/02-codex-raw-context.md` |
| G | codex-raw-start-day | skill | low | manual/keyword | `07_CLUSTER_G_CODEX_CLI_SKILLS/03-codex-raw-start-day.md` |
| G | codex-raw-comment-sweep | skill | medium | manual/keyword | `07_CLUSTER_G_CODEX_CLI_SKILLS/04-codex-raw-comment-sweep.md` |
| G | codex-raw-session-carry-forward | skill | low | manual/keyword | `07_CLUSTER_G_CODEX_CLI_SKILLS/05-codex-raw-session-carry-forward.md` |
| G | codex-raw-review-router | skill | medium | manual/keyword | `07_CLUSTER_G_CODEX_CLI_SKILLS/06-codex-raw-review-router.md` |
| G | codex-raw-delivery-closer | skill | medium | manual/keyword | `07_CLUSTER_G_CODEX_CLI_SKILLS/07-codex-raw-delivery-closer.md` |
| G | codex-raw-source-verifier | skill | medium | manual/keyword | `07_CLUSTER_G_CODEX_CLI_SKILLS/08-codex-raw-source-verifier.md` |
| H | example-scoutflow-dispatch-audit | tool | medium | manual/workflow | `08_CLUSTER_H_CROSS_TOOL_EXAMPLES/01-example-scoutflow-dispatch-audit.md` |
| H | example-raw-wiki-enrich | tool | medium | manual/workflow | `08_CLUSTER_H_CROSS_TOOL_EXAMPLES/02-example-raw-wiki-enrich.md` |
| H | example-h5-bridge-vault-review | tool | high | manual/workflow | `08_CLUSTER_H_CROSS_TOOL_EXAMPLES/03-example-h5-bridge-vault-review.md` |
| H | example-memory-governance-loop | tool | medium | hook/workflow | `08_CLUSTER_H_CROSS_TOOL_EXAMPLES/04-example-memory-governance-loop.md` |
| H | example-incident-recovery | tool | high | manual/workflow | `08_CLUSTER_H_CROSS_TOOL_EXAMPLES/05-example-incident-recovery.md` |
| H | example-research-to-authority-separation | tool | medium | manual/workflow | `08_CLUSTER_H_CROSS_TOOL_EXAMPLES/06-example-research-to-authority-separation.md` |

## Reading Order

建议先读 `README.md`、`00_EVIDENCE/SOURCE-INVENTORY.md`、`09_SYNTHESIS/TRUTHFUL-STDOUT.yml`。然后读 `09_SYNTHESIS/CROSS-TOOL-COLLABORATION-GRAPH.md` 和 `09_SYNTHESIS/REDUNDANCY-CONFLICT-DETECTION.md`，建立全局结构。最后进入各 cluster index 和 entry。若用户要把它升级为 authority，请先运行 `00_EVIDENCE/LOCAL-RESCAN-CHECKLIST.md`，把每个 expected path 与真实文件对齐。

## Catalog Semantics

本包把 toolchain 拆成六种基本层：skill 是可复用能力说明；agent 是可委派角色；plugin 是能力集合和扩展包；MCP 是外部状态接口；hook 是事件驱动自动化；script 是可重复命令。Cross-tool workflow 则把这些层串成操作模板。这个拆法的目的，是让用户在写新 skill 或调用工具前先问：已有能力是否覆盖？是否存在低风险替代？是否需要先读 source verifier？是否会触碰 stop-line？

## Authority Discipline

所有文件均标记 candidate / not-authority。ScoutFlow/RAW 材料反复强调：research note、draft spec、chat summary 和候选报告不得自动升级为 final authority；状态写回要遵守 task index/current/decision-log 或项目等价规则；RAW vault 顶层结构和 `.claude` 私有资产必须保持 read-only。U12 catalog 的成熟度，也应以能否维护这种 authority discipline 为核心指标，而不是以工具数量为荣。

## Practical Next Move

最小下一步不是继续扩写，而是在真实机器上执行本地复扫，产出 `local-inventory.tsv`。然后把本包条目分为三类：已存在且应保留、已存在但重复/冲突、prompt 期望但不存在。对重复项要指定 owner；对冲突项要指定禁用或触发优先级；对不存在项要避免写成事实，只保留为 backlog。这样 U12 才能从研究包转为可维护 catalog。✨
