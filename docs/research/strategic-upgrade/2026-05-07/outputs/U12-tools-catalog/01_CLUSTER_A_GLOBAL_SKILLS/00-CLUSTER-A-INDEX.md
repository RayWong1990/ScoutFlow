---
title: Cluster A Index — Global Skills
status: candidate / evidence-bounded / not-authority
created_at: 2026-05-06
cluster: A
entries_count: 18
---

# Cluster A: Global Skills

## Scope

Global Skills 是用户实际调用时最容易复用的一层，但也是最容易被 agent、plugin command 和 Codex skill 重复包装的一层。此 cluster 的治理重点是：把“能力标签”与“执行权限”分开；把文档/规划 skill 与浏览器/导出/测试 skill 分开；把通用能力与 ScoutFlow/RAW 项目规则分开。 本索引只描述目录和治理建议，不激活任何能力，不修改任何 settings，不把 prompt 中的 expected path 当成已经存在的本地事实。所有条目都需要在真实机器上经过 local rescan 后再升级状态。

## Entry Table

| entry_id | kind | activation | risk | file |
|---|---|---|---|---|
| global-code-reviewer | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/01-global-code-reviewer.md` |
| global-build-error-resolver | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/02-global-build-error-resolver.md` |
| global-e2e-runner | skill | manual/tool-assisted | high | `01_CLUSTER_A_GLOBAL_SKILLS/03-global-e2e-runner.md` |
| global-tdd-guide | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/04-global-tdd-guide.md` |
| global-refactor-cleaner | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/05-global-refactor-cleaner.md` |
| global-doc-updater | skill | manual/keyword | low | `01_CLUSTER_A_GLOBAL_SKILLS/06-global-doc-updater.md` |
| global-brainstorm-five-lens | skill | manual/keyword | low | `01_CLUSTER_A_GLOBAL_SKILLS/07-global-brainstorm-five-lens.md` |
| global-writing-plan | skill | manual/keyword | low | `01_CLUSTER_A_GLOBAL_SKILLS/08-global-writing-plan.md` |
| global-executing-plan | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/09-global-executing-plan.md` |
| global-context-loader | skill | manual/keyword | low | `01_CLUSTER_A_GLOBAL_SKILLS/10-global-context-loader.md` |
| global-source-verifier | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/11-global-source-verifier.md` |
| global-vault-lint | skill | manual/keyword | low | `01_CLUSTER_A_GLOBAL_SKILLS/12-global-vault-lint.md` |
| global-wiki-compile | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/13-global-wiki-compile.md` |
| global-export-pdf | skill | manual/tool-assisted | medium | `01_CLUSTER_A_GLOBAL_SKILLS/14-global-export-pdf.md` |
| global-deep-intake | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/15-global-deep-intake.md` |
| global-solution-writer | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/16-global-solution-writer.md` |
| global-ux-ia-review | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/17-global-ux-ia-review.md` |
| global-quality-gate | skill | manual/keyword | medium | `01_CLUSTER_A_GLOBAL_SKILLS/18-global-quality-gate.md` |

## Governance Summary

本 cluster 的核心治理问题是“边界压缩”：只保留足够完成任务的最窄入口，把高风险操作留给显式授权，把重复入口合并到 owner entry。若用户发出模糊请求，应优先通过 routing/context/source-verifier 明确事实范围，再调用本 cluster 中的具体条目。若一个条目同时属于文档、执行、记忆、浏览器或数据库多个层面，应拆为 entry 与 workflow 两层，不应把所有职责塞进一个超级工具。

## Risk Hotspots

高/中风险条目数量：13。这些条目在迁移到真实目录时，需要额外检查：事件自动触发、settings 注册、插件版本、外部服务权限、文件写入范围、并行 writer、以及是否可能把 candidate 误写成 authority。对于 GUI、database、browser、repo 写入类入口，需要保留最小参数、截图或日志证据、以及明确的回滚说明。

## Redundancy Candidates

本 cluster 与其他 cluster 可能有重叠。例如 Global Skill 与 Agent 可能同名；Plugin 可能包装同名 command；MCP server 可能提供和 script 相似的数据读取能力。初步处理原则是：skill 管“如何做”、agent 管“谁做”、MCP 管“访问什么外部状态”、hook 管“何时自动触发”、script 管“可重复命令”、workflow 管“多工具如何协同”。按这个原则可以显著降低 tool sprawl。

## Upgrade Path

升级时先验证 source path，再读取 frontmatter 或 manifest，最后写回 catalog。不要直接按本包的 expected path 改 settings；本包只是候选目录。升级版应能回答四个问题：这个入口真实存在吗？它何时触发？它会读取或写入什么？它和哪个 entry 冲突或互补？只有四个问题都有证据，才把 `verification_status` 改成 `verified-local-path`。

## Mermaid Mini-map

```mermaid
flowchart LR
  Intent[User Intent] --> Route[Context / Router]
  Route --> Cluster[Cluster A: Global Skills]
  Cluster --> Gate[Quality / Risk Gate]
  Gate --> Output[Candidate Output]
  Output --> Audit[Local Rescan Audit]
```
