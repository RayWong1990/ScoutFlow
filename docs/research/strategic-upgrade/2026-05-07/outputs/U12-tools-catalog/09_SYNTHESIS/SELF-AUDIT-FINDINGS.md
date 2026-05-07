---
title: Self Audit Findings
status: candidate / evidence-bounded / not-authority
created_at: 2026-05-06
findings_count: 28
---

# Self Audit Findings

| ID | Finding | Resolution |
|---|---|---|
| SA-01 | 运行环境没有真实 ~/.claude 目录 | original U12 complete=false; keep verification_status explicit |
| SA-02 | 运行环境没有真实 ~/.codex 目录 | Codex skill entries rely on uploaded AGENTS references |
| SA-03 | 上传 U12 prompt 是任务规格，不是安装证据 | mark prompt-derived entries specified-by-U12-prompt |
| SA-04 | ScoutFlow audit pack 是 candidate，不是 authority | do not promote pack outputs |
| SA-05 | Dispatch126-176 历史冻结口径需要保留 | do not treat as pending execution |
| SA-06 | 未执行任何 skill/agent/tool/MCP/plugin/hook/script | catalog only |
| SA-07 | 未修改 settings 或源目录 | all outputs written under /mnt/data output pack |
| SA-08 | 每个 entry 有 entry_id/kind/source/activation/risk_level | schema check pass |
| SA-09 | source 指向包内 evidence 文件而非假本机路径 | expected_runtime_path separate |
| SA-10 | 高风险 MCP/hook/script 均标 high 或 medium | risk tier applied |
| SA-11 | 同名 skill/agent/plugin command 已列为候选冲突 | redundancy table |
| SA-12 | PostToolUse 与 single Write 冲突已记录 | conflict finding |
| SA-13 | memory hook 与 memory governor 冲突已记录 | conflict finding |
| SA-14 | Playwright/GUI bridge/database 均不自动执行 | boundary preserved |
| SA-15 | cluster index 数量为 8 | A-H indexes created |
| SA-16 | cross-tool Mermaid 图不少于 4 | 5 diagrams created |
| SA-17 | truthful stdout 声明 complete=false | no false completion |
| SA-18 | local rescan checklist included | upgrade path available |
| SA-19 | U9/U10/U11 未提供真实文件 | fields retained but no fabricated paths |
| SA-20 | 未进行联网刷新 | web unavailable in current environment |
| SA-21 | GitHub connector仅用于登录检查 | no repo mutation |
| SA-22 | package contains no copied private CLAUDE.md/settings values | input manifest only |
| SA-23 | entry count exceeds 70 | 79 entries generated |
| SA-24 | file count exceeds 94 after synthesis | verified by script |
| SA-25 | self-audit distinguishes counts from authority completion | metrics separated |
| SA-26 | ScoutFlow/RAW tool role separation preserved | GPT Pro/Claude/Codex roles stated |
| SA-27 | single-authority-writer principle carried into graph | Diagram 5 |
| SA-28 | candidate/not-authority frontmatter used throughout | pack-level status |

## Audit Conclusion

本包通过了“诚实边界”自审：它完成了可交付的目录骨架、entry 文件、cluster index、协作图、冲突检测、时间线、runbook 链接和 stdout 合同；但没有通过原 U12 prompt 的最高标准，因为真实本机目录不可读，也没有 live web refresh。这个差距不是格式问题，而是证据问题。正确做法是保留 complete=false，并把本包作为本地复扫前的研究底稿。
