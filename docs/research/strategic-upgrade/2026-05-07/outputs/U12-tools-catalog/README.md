---
title: README — U12 Skills Tools MCP Plugin Catalog Evidence-bounded Pack
status: candidate / evidence-bounded / not-authority
created_at: 2026-05-06
---

# U12 Skills + Tools + MCP + Plugin Catalog — Evidence-bounded Pack

这是根据用户上传的 U12 catalog prompt 和 ScoutFlow Post176 audit pack 生成的深度研究包。它的目标是帮助用户把事实运转中的 skill、agent、tool、MCP server、plugin、hook、script 和 Codex skill 组织成可搜索、可审计、可升级的目录。

## Important Status

**不是 authority。不是完整本机扫描。** 当前运行环境没有真实 `~/.claude` 或 `~/.codex`，所以本包选择诚实保留 `CLOUD_U12_SKILLS_TOOLS_MCP_PLUGIN_CATALOG_COMPLETE: false`。同时，它已经提供完整结构、候选条目、冲突检测、协作图和本地复扫清单，便于你在真实机器上升级为权威版本。

## Contents

| Area | Description |
|---|---|
| `00_EVIDENCE/` | 输入 manifest、证据边界、本地复扫 checklist |
| `01_CLUSTER_A_GLOBAL_SKILLS/` | Global skill 候选目录 |
| `02_CLUSTER_B_AGENTS/` | Agent 候选目录 |
| `03_CLUSTER_C_PLUGINS/` | Plugin 候选目录 |
| `04_CLUSTER_D_MCP_SERVERS/` | MCP server 候选目录 |
| `05_CLUSTER_E_HOOKS/` | Hook 候选目录 |
| `06_CLUSTER_F_SCRIPTS/` | Script 候选目录 |
| `07_CLUSTER_G_CODEX_CLI_SKILLS/` | RAW/Codex skill surface 候选目录 |
| `08_CLUSTER_H_CROSS_TOOL_EXAMPLES/` | 跨工具协同样例 |
| `09_SYNTHESIS/` | master index、graph、redundancy、timeline、self-audit、stdout |

## Best Reading Path

先读 `09_SYNTHESIS/TRUTHFUL-STDOUT.yml`，确认完成状态和计数；再读 `00_EVIDENCE/SOURCE-INVENTORY.md`，理解哪些证据可用、哪些目录缺失；然后读 `09_SYNTHESIS/MASTER-CATALOG-INDEX.md` 和 `09_SYNTHESIS/REDUNDANCY-CONFLICT-DETECTION.md`；最后进入 cluster index 和单 entry。

## Design Choices

每个 entry 都保留 `entry_id`、`kind`、`source`、`activation`、`risk_level` 等 frontmatter，并增加 `verification_status` 与 `expected_runtime_path`。这样做能避免一个常见错误：为了满足文件数和字数，把未验证路径说成已验证事实。真正的 U12 完成版应该在用户本地把每个 expected path 都复扫成真实 source path。

## Upgrade Path

1. 在真实机器上运行 `00_EVIDENCE/LOCAL-RESCAN-CHECKLIST.md` 的只读扫描。  
2. 把扫描结果合并到本 catalog。  
3. 将不存在条目标记为 backlog 或 removed。  
4. 将重复条目标记 owner/secondary。  
5. 将高风险 hook/MCP/script 单独过 allowlist 和禁用策略。  
6. 重新生成 truthful stdout，只有所有 source path 都真实时才把 complete 改为 true。

## Final Boundary

本包没有执行任何 skill、agent、plugin、MCP、hook 或 script；没有修改用户项目；没有读取真实私有 settings；没有联网刷新外部版本。它是一个可以立刻用于审计和复扫的高保真底稿。🌱
