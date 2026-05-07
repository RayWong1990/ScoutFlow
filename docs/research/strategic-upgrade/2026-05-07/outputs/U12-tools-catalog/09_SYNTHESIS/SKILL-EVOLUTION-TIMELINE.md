---
title: Skill Evolution Timeline
status: candidate / evidence-bounded / not-authority
created_at: 2026-05-06
---

# Skill Evolution Timeline

## Reading the Timeline

本时间线不是从真实 `.claude` git history 生成的，而是从上传的 U12 prompt、ScoutFlow/RAW audit pack、AGENTS 规则和 dispatch evidence 中抽象出来的“演化模型”。它用来解释为什么现在需要 U12 catalog：工具链从单一助手，演化到多 AI fleet、多项目规则、多插件、多 hook、多 MCP server、多脚本并行后，原先靠记忆和习惯调用工具的方式已经不够可靠。

## Phase 0 — Manual Craft and Ad-hoc Tools

最初阶段通常是用户手写 prompt、脚本和少量技能说明。工具的优势是灵活，问题是没有统一 frontmatter、source path、activation、risk、dependency。此时“重复发明”成本不高，但随着 ScoutFlow/RAW 这类项目出现，路径规则、authority 写回顺序、质量门和 dispatch 状态越来越多，单靠个人记忆开始失效。

## Phase 1 — Claude Skills and Agents

第二阶段出现全局 skills 与 agents：code-reviewer、build-error-resolver、e2e-runner、tdd-guide、doc-updater 等能力把常见工程任务封装起来。收益是速度变快，问题是 skill 和 agent 的边界开始重叠：一个负责 checklist，一个负责委派执行；如果没有 owner，用户会不知道该调哪个。U12 catalog 的 Cluster A/B 正是为了解决这类重叠。

## Phase 2 — Plugins and Marketplace Cache

第三阶段出现 ECC、superpowers、claude-mem、dx 等 plugin。插件把 commands、skills、agents、hooks 聚合在一起，能力密度大幅提升，也带来版本漂移、隐性触发和重复包装。比如 superpowers 的计划/执行模式可能与 planner agent 重叠，claude-mem 的记忆 hook 可能与 memory-governor 的政策判断重叠。此阶段需要把 plugin 本体和 plugin 暴露能力分开 catalog。

## Phase 3 — MCP as External State Interface

第四阶段引入 GitHub、Supabase、Firecrawl、Context7、Exa、Playwright、Notion、Engram 等 MCP servers。此时工具不再只是“写文本”，而是能读 live repo、访问数据库、开浏览器、抓网页、查文档、写页面。风险等级显著上升，catalog 必须记录 server 边界、参数最小化、source hierarchy 和输出证据如何进入审计链。

## Phase 4 — Hooks, Scripts, and Resilience Layer

第五阶段是自动化：PreToolUse/PostToolUse/SessionStart/Stop/PreCompact 等 hook，与 cc-resilient、quality-gate、pack-builder、handoff-writer 等脚本结合。它们解决了连续工作、失败恢复、质量门和打包，但也引入 cascade cancel、自动写入、临时事实固化、并行 writer 冲突。ScoutFlow/RAW 的 hard guardrails 对这一阶段尤其关键：自动化只能增强边界，不能削弱边界。

## Phase 5 — Codex Adaptation and Multi-AI Fleet

第六阶段是 Codex CLI skill surface：raw-go、raw-context、raw-start-day、raw-comment-sweep、raw-session-carry-forward、raw-review-router、raw-delivery-closer、raw-source-verifier 等。它们体现出“Claude assets source of truth，Codex adaptation additive”的策略。多 AI fleet 带来吞吐量，也要求每个引擎知道自己的边界：Codex 主写入、Claude read-only review、GPT Pro external review、OpenClaw/Hermes research/rebuttal。

## Phase 6 — U12 Catalog Control Plane

U12 目标是把上述能力统一成 ≥70 个 single-file entry，并加 cross-tool graph、redundancy/conflict detection、timeline、linked rules/runbooks、truthful stdout。它不是再新增一个超级工具，而是建立控制平面：先 inventory，再 schema，再 cluster，再 cross-tool map，再 audit。成熟后的 catalog 应该让用户在写新 skill 前先查旧条目，在派发 agent 前看冲突，在开 MCP 前看权限，在启用 hook 前看副作用。

## Future Direction

下一步不是盲目扩容，而是本地复扫 + 归并。理想状态是每个 entry 都能追溯到真实源文件、版本、owner、触发方式、测试证据和弃用策略；每个重复入口都能说明为什么保留；每个高风险 hook/MCP/script 都能在禁用状态下被安全审计。这样工具链才会从“事实运转但不可见”变成“可搜索、可协同、可治理”的个人 AI operating system。
