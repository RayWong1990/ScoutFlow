---
entry_id: hook-userpromptsubmit
title: "UserPromptSubmit Hook"
kind: hook
cluster: E / Hooks
source: 00_EVIDENCE/SOURCE-INVENTORY.md
source_class: global
activation: hook/auto
risk_level: medium
verification_status: specified-by-U12-prompt
expected_runtime_path: "~/.claude/settings.json#hooks.hook-userpromptsubmit"
cost_per_invoke: unknown / estimate-only
parameters: ["prompt text", "project", "routing table"]
dependencies: ["settings_hooks", "event_payload", "safe_exit"]
linked_rules: [read-only-catalog, candidate-not-authority, credential-redaction, local-rescan-required]
linked_runbook: 00_EVIDENCE/LOCAL-RESCAN-CHECKLIST.md
linked_dispatch: ScoutFlow-post176 audit pack / dispatch127-176 evidence where applicable
linked_anti_pattern: [tool-sprawl-without-catalog, duplicate-role-without-owner, hook-cascade, authority-drift]
---

# UserPromptSubmit Hook

## 1. Mission

用户请求进入时的路由、敏感路径、任务分类。本条的核心使命不是替代真实工具实现，而是在 U12 catalog 中给它一个可审计、可比较、可升级的位置。hook 条目强调“事件驱动的自动性”。它最容易与 Edit/Write、子代理回收、会话关闭和记忆写入发生隐性冲突。 对单人 prosumer 工具链尤其重要，因为同一类任务常同时存在 Claude skill、Codex skill、agent、plugin command、MCP server 和 shell script；没有 catalog 时，用户每次都会重新发明入口，或者把高风险能力误当成低风险文档技能。

## 2. When to Use

当任务目标与“用户请求进入时的路由、敏感路径、任务分类”直接相关，并且输入材料已经能满足 `prompt text, project, routing table` 这类最低输入契约时，可以考虑使用本条。典型场景包括：需要把模糊请求落到一个明确产物；需要在 ScoutFlow/RAW 这种多规则项目里保留 candidate/authority 边界；需要把审查、执行、记录和交付拆开；需要在多个 AI fleet 成员之间给出清晰 handoff。若目标是临时问答，且不会产生持久产物，通常只需要普通对话，不需要启动完整能力。

## 3. When Not to Use

不要在三类情况下使用：第一，source path 尚未本地验证，却准备写入真实 authority 文件；第二，任务包含 credential、私密 settings、数据库变更或 GUI 自动化，而用户没有给出明确范围；第三，已有更窄、更低风险、更靠近事实源的 entry 可以完成同一工作。对于 `medium` 风险条目，尤其要避免“因为工具存在所以调用”的工具膨胀。catalog 的价值是减少误触发，而不是鼓励每个请求都跑一遍完整编排。

## 4. Activation Method

activation=`hook/auto`。由事件自动触发；catalog 阶段只描述事件、输入和风险，不模拟事件。 本包没有执行任何 skill、agent、plugin、MCP、hook 或 script；它只把触发关系写成候选目录。真实采用前，操作者应在 settings、plugin manifest、skill frontmatter 或 Codex skill 文件中确认触发词、事件名、可用工具和禁用项。

## 5. Parameters and Input Contract

最低输入应包含：prompt text, project, routing table。此外还需要三类上下文：一是 authority map，即哪些文件是事实源、哪些只是 research/candidate；二是 stop-line，即哪些路径、状态词、运行态或隐私边界不可触碰；三是 evidence packet，即可以支持输出判断的文件、日志、diff、截图或报告。输入不足时，本条应输出缺口清单，而不是补写猜测。对于跨工具调用，还应在 handoff 中写清上一工具产生了什么、没有做什么、下一工具可安全使用哪些证据。

## 6. Output Contract

标准输出应包含四层：结论、证据、风险、下一步。结论要区分 verified、specified、inferred、unknown；证据要指向文件或可复扫路径；风险要标出并发、权限、版本、重复职责和质量门；下一步要能落地到本地 rescan、配置检查、文档更新或弃用决策。若输出是报告，应保留 `status: candidate / not-authority`；若输出是 action plan，应明确不自动执行高风险命令。

## 7. Cost and Operational Burden

cost_per_invoke 在本环境为 unknown，只能做估算。低成本来自纯文档和规划，中成本来自读取大量文件或组织 agent 回收，高成本来自浏览器、数据库、外部搜索、长链路 hook 或大规模源码扫描。主要风险是写入范围、过期事实、工具间重复职责、质量门漏检，需要前置验收和回滚条件。 该条的隐藏成本通常不是单次调用耗时，而是结果回收：如果没有统一 schema，多个工具会分别产生“看似完整但口径不同”的报告，最终增加用户判断负担。

## 8. Lessons and Risk Notes

从 ScoutFlow/RAW 材料可抽象出三个经验：第一，任何工具链 catalog 都不能把 candidate、draft、research note 写成 authority；第二，跨引擎协作必须显式记录当前文件路径、状态词和 stop-line，否则下一轮会把历史 dispatch 当成待执行包；第三，自动化 hook 和子代理不共享完整记忆，prompt 中必须把禁止项、输入摘要、输出 schema 写成字面约束，而不是依赖隐含上下文。 对 `UserPromptSubmit Hook` 来说，最需要防范的是职责重叠和触发混乱：同名 skill 与 agent 可能都叫 code reviewer；plugin command 可能又包装一个 agent；hook 可能在 Write 后自动追加审计，和主流程的单次写入策略冲突。因此 catalog entry 必须把“调用谁、何时停、谁合并结果、谁写 authority”写清楚。

## 9. Linked Collaboration

关联上游：U12 catalog prompt、ScoutFlow Post176 audit pack、RAW/ScoutFlow AGENTS 规则摘录、local rescan checklist。关联下游：cluster index、master catalog、collaboration graph、redundancy/conflict detection、skill evolution timeline。采用本条前，应先把 `verification_status` 从 prompt-specified 升级为 local-verified；如果无法升级，则只能把它当成架构规划和迁移清单。 推荐协作模式是：先用 source-verifier 或 context-loader 明确事实范围，再让 `UserPromptSubmit Hook` 执行自己的窄职责，最后由 quality-gate 或 stdout-auditor 做收束。若本条与其他 entry 冲突，应优先保留更接近事实源、更低权限、更可回滚的路径。

## 10. Local Verification Notes

本运行没有读到真实安装目录，所以本条的最重要后续动作是本地复扫。复扫时先确认 source path、frontmatter、依赖、hook 注册、插件版本和 settings 事件名，再决定是否合并、弃用或拆分。对高风险条目，还要检查是否会写 authority 文件、是否会访问 GUI 或数据库、是否会触发并行写入。任何未验证参数都应保持为空或 `unknown`，不能用记忆补齐。✅
