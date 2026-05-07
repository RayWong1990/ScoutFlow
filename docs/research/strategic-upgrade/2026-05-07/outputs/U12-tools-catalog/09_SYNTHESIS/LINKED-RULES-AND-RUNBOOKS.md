---
title: Linked Rules and Runbooks
status: candidate / evidence-bounded / not-authority
created_at: 2026-05-06
---

# Linked Rules and Runbooks

## Rule Classes

本 catalog 采用四类规则链接。第一类是 hard boundary：只读 catalog、不修改 `.claude`、不修改 `.codex`、不运行 skill/agent/tool/hook/script、不输出 credential value。第二类是 authority discipline：candidate/research/draft 不得直接写入 final authority；ScoutFlow 状态类文件需要遵守 task index/current/decision-log 或项目等价写回顺序。第三类是 routing discipline：混合意图先澄清或单目标路由，不让多个工具同时抢 owner。第四类是 quality discipline：source verifier、quality gate、handoff 和 stdout auditor 负责收束。

## Runbook Links in this Pack

| Runbook | Purpose |
|---|---|
| `00_EVIDENCE/LOCAL-RESCAN-CHECKLIST.md` | 把 prompt-specified entry 升级成本地 verified entry |
| `09_SYNTHESIS/REDUNDANCY-CONFLICT-DETECTION.md` | 处理同名/近义能力与自动化冲突 |
| `09_SYNTHESIS/CROSS-TOOL-COLLABORATION-GRAPH.md` | 理解多工具协作路径和 authority gate |
| `09_SYNTHESIS/SELF-AUDIT-FINDINGS.md` | 审计本包自身边界、失败项和后续动作 |
| `09_SYNTHESIS/TRUTHFUL-STDOUT.yml` | 机器可读完成状态与真实计数 |

## Mapping to Entries

每个 entry frontmatter 都包含 `linked_rules`、`linked_runbook`、`linked_dispatch`、`linked_anti_pattern` 字段。当前值是候选映射：因为真实 U9/U10/U11 runbook 未随本次输入提供，所以本包没有伪造双向链接，只保留字段和 fallback 指向。升级版应在真实仓库中查找 U9 dispatch、U10 runbook、U11 anti-pattern 文件，然后把这些字段改为真实路径。

## Anti-pattern Library

最重要的 anti-pattern 有六个：tool sprawl without catalog；duplicate role without owner；hook cascade；authority drift；unverified memory persistence；GUI/database overreach。它们分别对应“工具太多找不到”“同名工具互抢职责”“自动化互相触发”“候选事实写成真相”“临时偏好写成长记忆”“能用文件/API 却强行走高风险界面”。这些反模式不是抽象洁癖，而是会直接造成错误写入、错误路线、重复劳动和用户信任损失。

## Local Upgrade Contract

升级时请保持三个不变：schema 不变、boundary 不变、truthful stdout 不变。可以增加字段、增加 source path、补充真实版本、删除不存在条目，但不能把 unknown 改成 guessed，不能把 candidate 改成 authority，不能为了满足数字指标虚构安装事实。真正完成 U12 的标准，是用户能打开 catalog，搜索任意工具名，看到真实路径、触发方式、风险、冲突、替代入口和协作方式。
