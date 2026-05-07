---
title: MEMORY.md 维护（200 行限制 / 归档过时）
status: candidate
authority: not-authority
created_at: 2026-05-07
runbook_id: RB-MEM-05
cluster: Memory / Cross-Session
trigger_keywords:
  - MEMORY.md
  - 200行
  - archive stale
  - memory maintenance
risk_level: low
single_user_applicable: true
multi_agent_applicable: true
linked_dispatch:
  - MOD-MEM-MEM-MEMORY-MAINTAIN
  - P3-DSP-LANE-GUARD
linked_pr:
  - none
linked_tools:
  - memory audit
  - stale marker
  - archive pointer
linked_skill:
  - cross-session-memory
linked_rule:
  - ~/.claude/rules/session-closure.md
  - ~/.claude/rules/token-hygiene.md
  - ~/.claude/rules/execution-discipline.md
source_basis:
  - uploaded Cloud Prompt U10 2026-05-07
  - ScoutFlow post176 cloud audit pack 2026-05-05
  - PRD-v2 / SRD-v2 / AGENTS / current.md excerpts present in audit pack
  - Dispatch127-176 manifest and Codex audit excerpts present in audit pack
boundary_statement: candidate SOP only; does not approve runtime, authority write, package change, migration, browser automation, ASR, or vault true write.
---
## 1. Mission / mission

[candidate procedure] 本 runbook 把 `MEMORY.md 维护（200 行限制 / 归档过时）` 固化为 single-user prosumer 可重复 SOP。目标不是批准动作，而是让用户在遇到 `MEMORY.md, 200行, archive stale` 这类触发词时，能先检查边界、证据与 rollback，再决定是否另开获授权执行。

[canonical fact] 本库采用 PRD-v2/SRD-v2 口径：ScoutFlow 是 single-user、local-first 工作台，authority-first 以 SQLite + FS + state words 为核心；Console 只是 projection，Worker 不能直写 SQLite，所有有效写入都必须走 Thin API 或明确授权的 repo authority writer。

[boundary note] 该场景风险等级为 `low`。风险来自：不得把临时推理、未验证事实、旧 PR 状态写成长期记忆。 因此本文件只提供候选步骤和审计点，不构成 runtime approval、migration approval、browser automation approval、ASR approval、vault true write approval 或 package approval。

## 2. Trigger / trigger

[operator trigger] 当用户输入、handoff、dispatch 或下游请求出现以下关键词时启用本 SOP：MEMORY.md, 200行, archive stale, memory maintenance。如果同时出现更高风险关键词，例如 credential、migration、runtime、browser automation、ASR、true write、authority edit，则先按 Boundary / Audit cluster 重新分级。

[negative trigger] 不要在以下情况下启用本 SOP 的执行路径：不得把临时推理、未验证事实、旧 PR 状态写成长期记忆。 如果只是研究、复盘、教育用途，可以阅读本 SOP；如果要实际运行命令或写文件，必须另有明确 dispatch、allowed_paths、owner 和 validation plan。

## 3. Preconditions / preconditions

[precondition] P1. ScoutFlow 是 single-user / local-first 的内容采集与证据整理系统；事实源以 SQLite + FS + state words 为核心。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P2. PRD-v2/SRD-v2 明确 Phase 1A 只批准 Bilibili manual_url + metadata_only 的窄闭环。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P3. LP-001 要求 recommendation / keyword / RAW gap 不得直接创建 capture。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P4. ContentFlow L1 本地报告在当前容器不可读；本库只使用提示中给出的 4h27m / 21 swap / multi-agent 协作沉淀作为 lesson anchor。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P5. 跨模型协作的通用教训是：换窗前需要短 handoff、下一会话 prompt、上下文差异说明、owner single-writer、rollback path。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P6. silent flexibility 不是自动正确；它需要被 detect、ledger record、readback 验证，不能让模型自行扩大 scope。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P7. 本 runbook 的直接场景是：维护长期记忆时只保留稳定偏好、固定边界与当前项目指针，过时内容归档。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[lane precondition] 必须确认当前 lane owner 与 same-file owner。并行可提高 coverage，但 authority writer 仍只能有一个；review/audit/research lane 不得写 authority。

## 4. Steps / steps

[operator step] S1. 把场景改写成一句可审计任务：维护长期记忆时只保留稳定偏好、固定边界与当前项目指针，过时内容归档。

[operator step] S2. 先判断是否需要换窗、压缩或清空：按 token 阈值、风险等级、authority 写入状态，不按主观疲劳。

[operator step] S3. 收集最小事实：当前目标、source order、completed evidence、blocked lanes、owner、next action、rollback。

[operator step] S4. 把 handoff 限制为可执行合同，避免长篇回忆；关键命令、文件路径、停线项优先。

[operator step] S5. 下一窗口启动时必须 readback，而不是直接执行上一窗口最后一句。

[operator step] S6. 发现 compact 后上下文缺口时，先恢复边界，再恢复任务。

[operator step] S7. 归档过时记忆，避免旧 PR、旧 phase、旧 approval 污染新工作。

[operator step] S8. 把禁止项写入任务头：不得把临时推理、未验证事实、旧 PR 状态写成长期记忆。

[operator step] S9. 如果任何一步发现 authority、runtime、secret、legal posture 或 same-file ownership 不清楚，立即转入 rollback/hold，而不是继续补假设。

## 5. Verification / verification

[verification item] V1. frontmatter 是否含 status: candidate、authority: not-authority、risk_level、trigger_keywords、linked_dispatch、linked_rule。

[verification item] V2. allowed_paths 与 forbidden_paths 是否能从 dispatch、manifest 或 prompt 中读到；读不到时必须标为 blocked。

[verification item] V3. 是否没有把 research note、draft spec、local probe report、chat summary、preview artifact 写成 final authority。

[verification item] V4. 是否有 rollback path；如果 rollback 只写“人工处理”，则视为 verification fail。

[verification item] V5. 是否保留 source label：canonical fact、candidate procedure、operator inference、environment limitation。

## 6. Rollback / rollback

[rollback instruction] R1. 如果发现前置条件不成立，立即把任务状态改为 hold/deferred/superseded，而不是继续执行。

[rollback instruction] R2. 如果已经生成候选文件，保留原文件并追加 supersede header 或 quarantine marker；不要静默删除证据。

[rollback instruction] R3. 如果已经产生 PR/diff，先用 git diff 定位越界范围，再选择 revert、reset to HEAD、narrow follow-up PR 或 audit note。

[rollback instruction] R4. 如果出现 secret/PII 暴露，先停止传播并隔离 artifact，再做 redaction repair 与 downstream notification。

[rollback instruction] R5. 如果 authority surface 被误写，必须由唯一 authority writer 按 current/task-index/decision-log/contracts-index 顺序修复。

[rollback instruction] R6. 如果 handoff 丢失，回到 authority surface 与 git diff 重建，不凭记忆补长叙事。

## 7. Lessons learned / lessons

[lesson] L1. Wave 4 的核心教训是 terminal report 不等于所有 plane clear；每个结论都要说明它证明了哪一层、没有证明哪一层。

[lesson] L2. Dispatch127-176 audit 说明 candidate pack 可以结构强、manifest clean，但仍不是 execution approval；高质量包也要等 readback 与 gate。

[lesson] L3. ContentFlow L 提示中的 4h27m / 21 swap 经验提醒：多窗口工作最大的失败模式是上下文丢边界，不是写得慢。

[lesson] L4. silent flexibility 需要被记录和复核；模型主动修复可能有价值，但没有显式 amendment 就不能改变 scope。

[lesson] L5. 产品 proof 应早于硬化：topic-card-lite、RAW handoff、user-visible review 比继续堆 dispatch 更能证明真实价值。

[lesson] L6. 长期记忆越短越可靠；旧事实不删会反向污染新任务。

## 8. Linked artifacts / linked

[linked reference] A1. linked_dispatch: MOD-MEM-MEM-MEMORY-MAINTAIN, P3-DSP-LANE-GUARD

[linked reference] A2. linked_tools: memory audit, stale marker, archive pointer

[linked reference] A3. linked_rules: ~/.claude/rules/session-closure.md, ~/.claude/rules/token-hygiene.md, ~/.claude/rules/execution-discipline.md

[linked reference] A4. linked_skill: cross-session-memory

[linked reference] A5. source_docs: PRD-v2、SRD-v2、AGENTS、current.md、contracts-index、Dispatch127-176 manifest、Codex audit、post-dispatch176 strategy/roadmap/raw bridge candidate。

## 9. Footer / footer

[footer boundary] RB-MEM-05 是 candidate / not-authority SOP。读者可以用它做 checklist、audit、prompt scaffold 或 dispatch draft；不能把它当作用户授权、runtime unlock、legal conclusion、production code change、authority writeback 或 downstream publish approval。

[footer next action] 下一步如果要执行，必须另开任务：写明 owner、allowed_paths、forbidden_paths、validation command、rollback plan、evidence sink、是否需要 external audit。直到这些字段齐全，本 SOP 的安全结论保持 hold。

## Appendix — operator audit card

[scenario triage] `RB-MEM-05` 的最小可执行判断不是“这个场景是否有价值”，而是“在 `MEMORY.md 维护（200 行限制 / 归档过时）` 中，当前输入是否精确命中 `MEMORY.md / 200行 / archive stale / memory maintenance`，并且没有触发更高风险 lane”。跨 session 不是摘要越长越好，而是保留下一轮可执行的边界、未解锁项、证据位置和 next-session prompt。 这张卡用于开工前 60 秒 readback：说清楚 source、owner、gate、evidence sink 与 stop condition；说不清楚时，状态保持 hold。

[failure mode] 本场景风险等级为 `low`，需要优先防止“把候选 SOP 当执行批准”的漂移。最危险的捷径是用 /clear 或 /compact 清掉 boundary context，导致下一窗口重新发明 scope 或漏掉 rollback。 复盘时要把失败分成三类：前置证据不足、步骤越界、验证口径过宽；不要笼统写成“模型理解有误”。

[verification cue] 人工复核 token waterline、handoff 行数、MEMORY.md 新旧性、compact focus、SessionStart 恢复与 archive decision。 对每个 cue 都要留下可审计文字：`checked_by`、`checked_at`、`source_ref`、`result`、`residual_risk`。如果 cue 只能凭记忆确认，就写 `unverified_in_current_environment`，不要补写成通过。

[handoff card] handoff 必须包含 last_safe_state、open_questions、blocked_lanes、next_prompt、source_refs 和 forbidden assumptions。 推荐在下一窗口开头复制四行：`intent:`、`allowed:`、`blocked:`、`verify:`。这能把 ContentFlow L 提示里的多窗口换手教训转成可操作记忆，减少 21 次 swap 类场景中的边界遗失。
