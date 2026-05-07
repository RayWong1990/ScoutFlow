---
title: Source Inventory and Evidence Boundary
status: candidate / evidence-bounded / not-authority
created_at: 2026-05-06
---

# Source Inventory and Evidence Boundary

本文件是本包的证据总账。它不把上传材料重写成 authority，也不声称已经读到用户真实工作站上的 `~/.claude`、`~/.codex`、插件缓存或 MCP 配置。可验证证据只有两类：一是上传的 U12 catalog prompt；二是上传的 ScoutFlow Post176 audit pack。运行环境内显式检查过 `/root/.claude`、`/root/.codex`、`/mnt/data/.claude`、`/mnt/data/.codex`、`/home/oai/.claude`、`/home/oai/.codex`、`/Users/wanglei/.claude`、`/Users/wanglei/.codex`，均未发现可扫描目录。

## 可用输入

| 输入 | 文件名 | 字节 | sha256 前 12 位 | 用途 |
|---|---:|---:|---:|---|
| U12 prompt | `cloud-prompt-U12-skills-tools-mcp-plugin-catalog-2026-05-07.md` | 7495 | `bd5a2a015415` | 任务规格、目标文件数、cluster 架构、边界、stdout contract |
| ScoutFlow audit pack | `ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip` | 444235 | `157d1d036cd0` | ScoutFlow/RAW 项目规则、Codex skill routing 表、dispatch 和 repo evidence |

## ScoutFlow pack 解包观察

解包后可见 `100` 个普通文件。主要区域包括：`00_overview`、`01_external_reports`、`02_repo_sources`、`03_raw_sources`、`04_outputs`。这些材料支持对 RAW/ScoutFlow 项目的协同边界、agent 分工、read-only 路径、dispatch 冻结状态、Wave 4/5/6 关系进行归纳；它们不能替代真实 GitHub live truth，也不能证明 U12 prompt 所列每个 Claude skill/plugin/MCP server 确已安装。

## 证据等级

1. **verified-in-upload**：来自本包内 `00_EVIDENCE/INPUT-MANIFEST.json` 所列上传材料或 ScoutFlow audit pack 的实际文件路径。  
2. **specified-by-U12-prompt**：来自 U12 prompt 的枚举、目标或 schema 要求；它是任务规格，不是运行事实。  
3. **expected-runtime-path-unverified**：prompt 预期应在用户机器上存在的路径，但本环境未能读取。  
4. **inferred-collaboration-pattern**：从 ScoutFlow/RAW AGENTS、dispatch pack、U12 schema 推导出的协作模式，用于规划，不当作已部署事实。  

## 对 catalog 的影响

因此，本包采用“证据边界优先”的 catalog 策略：每个 entry 都保留完整 frontmatter、mission、适用/不适用场景、触发方式、参数、输出、成本、经验、关联；同时增加 `verification_status` 和 `expected_runtime_path`。这样做牺牲了“已全量本机扫描”的完成声明，但保住了可审计性。用户拿到后，可在真实机器上运行 `LOCAL-RESCAN-CHECKLIST.md` 的命令，把 `expected-runtime-path-unverified` 逐项升级为 `verified-local-path`。
