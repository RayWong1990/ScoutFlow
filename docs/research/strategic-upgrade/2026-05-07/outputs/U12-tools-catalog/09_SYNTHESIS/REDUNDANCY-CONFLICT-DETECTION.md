---
title: Redundancy and Conflict Detection
status: candidate / evidence-bounded / not-authority
created_at: 2026-05-06
findings_count: 18
---

# Redundancy and Conflict Detection

## Method

本检测基于名称相似度、职责动词、触发方式、风险层和来源层进行归纳。由于真实本机目录不可读，以下是“候选冲突”，不是已验证冲突。它们应作为 local rescan 的优先检查清单：先找同名或近义 entry，再看 settings、plugin manifest、agent file、skill file、script path 是否真实存在。

## Findings

| # | Candidate Conflict | Risk | Recommended Owner |
|---:|---|---|---|
| 1 | code-reviewer skill vs code-reviewer agent vs ECC reviewer command | medium | agent for delegated review; skill for checklist |
| 2 | build-error-resolver skill vs agent vs CI script | medium | script for deterministic log scan; agent for diagnosis |
| 3 | e2e-runner skill vs Playwright MCP vs GUI bridge | high | Playwright MCP for browser evidence; GUI bridge last resort |
| 4 | doc-updater skill vs doc-updater agent vs handoff-writer script | medium | doc-updater for repo docs; handoff-writer for session close |
| 5 | source-verifier skill vs raw-source-verifier Codex skill | medium | project-specific Codex skill inside RAW; global skill elsewhere |
| 6 | wiki-compile skill vs raw-wiki-compile Codex skill | medium | RAW skill for vault; global skill for non-RAW reports |
| 7 | superpowers writing-plan vs planner agent | low | writing-plan for artifact structure; planner for execution routing |
| 8 | executing-plan vs dispatch-commander agent | medium | dispatch-commander for ScoutFlow lane constraints |
| 9 | claude-mem hook vs memory-governor agent | high | governor decides durable memory; hook records only allowed events |
| 10 | PreToolUse path guard vs script allowlist | high | hook blocks before call; script validates again locally |
| 11 | PostToolUse audit vs single Write discipline | high | disable append-like post actions on protected paths |
| 12 | context-loader vs SessionStart hook | medium | hook gives minimal context; loader performs explicit reconstruction |
| 13 | Firecrawl MCP vs Exa research vs browser research | medium | Exa for discovery; Firecrawl for extraction; browser for dynamic state |
| 14 | GitHub App connector vs GitHub MCP | medium | one owner per repo operation; avoid split live truth |
| 15 | Supabase MCP vs SQLite-Chroma memory server | high | separate app data from memory data; never cross-write silently |
| 16 | cc-resilient wrapper vs incident recovery workflow | medium | wrapper handles command resilience; workflow handles evidence and report |
| 17 | quality-gate skill vs quality-gate script | medium | script for deterministic checks; skill for narrative audit |
| 18 | RAW ops console vs watchtower | low | ops console shows current visible state; watchtower gives periodic oversight |

## Conflict Principles

1. **Owner before alias**：每个 intent 只能有一个默认 owner，其他同名入口写成 secondary lens。  
2. **Lower privilege first**：能用纯文档 skill 解决，不调用 browser/database/filesystem server。  
3. **Project-specific beats global**：RAW/ScoutFlow 内部任务优先用项目 routing 表，因为它们携带本项目 stop-line。  
4. **Automation must be reversible**：hook 和 script 要么只读，要么有明确 allowlist、日志和禁用路径。  
5. **Candidate never becomes authority by accident**：研究报告、外部比较、chat summary 都要经过 writer gate。

## Operational Triage

local rescan 后建议把冲突分三批处理：P0 是高风险自动化和写入路径，包括 PostToolUse、filesystem、database、GUI bridge、memory 写入；P1 是同名 skill/agent/plugin command，包括 review、build、e2e、doc、quality；P2 是低风险规划/写作/上下文类能力，可以先保留别名，但要在 catalog 中写 owner。处理完冲突后，才能开始新增 skill，否则新增项会继续扩大 tool sprawl。
