---
title: PII redaction scan（regex + word boundary）
status: candidate
authority: not-authority
created_at: 2026-05-07
runbook_id: RB-BND-05
cluster: Boundary / Audit
trigger_keywords:
  - PII
  - redaction
  - 手机号
  - 邮箱
  - 身份证
risk_level: high
single_user_applicable: true
multi_agent_applicable: false
linked_dispatch:
  - P4-BND-BND-PII-REDACTION
  - P4-BND-HARD-REDLINES
linked_pr:
  - none
linked_tools:
  - redaction regex
  - word boundary review
  - sensitive_fields_removed
linked_skill:
  - boundary-audit
linked_rule:
  - ~/.claude/rules/security.md
  - ~/.claude/rules/testing.md
  - ~/.claude/rules/development-workflow.md
  - ~/.claude/rules/execution-discipline.md
source_basis:
  - uploaded Cloud Prompt U10 2026-05-07
  - ScoutFlow post176 cloud audit pack 2026-05-05
  - PRD-v2 / SRD-v2 / AGENTS / current.md excerpts present in audit pack
  - Dispatch127-176 manifest and Codex audit excerpts present in audit pack
boundary_statement: candidate SOP only; does not approve runtime, authority write, package change, migration, browser automation, ASR, or vault true write.
---
## 1. Mission / mission

[candidate procedure] 本 runbook 把 `PII redaction scan（regex + word boundary）` 固化为 single-user prosumer 可重复 SOP。目标不是批准动作，而是让用户在遇到 `PII, redaction, 手机号` 这类触发词时，能先检查边界、证据与 rollback，再决定是否另开获授权执行。

[canonical fact] 本库采用 PRD-v2/SRD-v2 口径：ScoutFlow 是 single-user、local-first 工作台，authority-first 以 SQLite + FS + state words 为核心；Console 只是 projection，Worker 不能直写 SQLite，所有有效写入都必须走 Thin API 或明确授权的 repo authority writer。

[boundary note] 该场景风险等级为 `high`。风险来自：不得过度依赖宽松 regex；不得把 false negative 当安全通过。 因此本文件只提供候选步骤和审计点，不构成 runtime approval、migration approval、browser automation approval、ASR approval、vault true write approval 或 package approval。

## 2. Trigger / trigger

[operator trigger] 当用户输入、handoff、dispatch 或下游请求出现以下关键词时启用本 SOP：PII, redaction, 手机号, 邮箱, 身份证。如果同时出现更高风险关键词，例如 credential、migration、runtime、browser automation、ASR、true write、authority edit，则先按 Boundary / Audit cluster 重新分级。

[negative trigger] 不要在以下情况下启用本 SOP 的执行路径：不得过度依赖宽松 regex；不得把 false negative 当安全通过。 如果只是研究、复盘、教育用途，可以阅读本 SOP；如果要实际运行命令或写文件，必须另有明确 dispatch、allowed_paths、owner 和 validation plan。

## 3. Preconditions / preconditions

[precondition] P1. ScoutFlow 是 single-user / local-first 的内容采集与证据整理系统；事实源以 SQLite + FS + state words 为核心。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P2. PRD-v2/SRD-v2 明确 Phase 1A 只批准 Bilibili manual_url + metadata_only 的窄闭环。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P3. LP-001 要求 recommendation / keyword / RAW gap 不得直接创建 capture。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P4. LP-006 要求 authority conflict domain 单写者；parallel review 可以多，但 authority writer max=1。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P5. LP-007 要求高风险或 material task 以 PR diff / workflow run / external audit evidence 为事实源。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P6. LP-SEC-001 要求 credential material never evidence；cookie/token/signed URL/browser profile path 不进入 Git、PR、CI、logs、DB artifacts 或 tracked docs。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P7. audio_transcript、BBDown live、yt-dlp、ffmpeg、ASR、browser automation、vault true write、migration、Phase 2-4 runtime 均仍 gated。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P8. XHS 与 YouTube runtime capture 在 SRD-v2 当前口径下必须拒绝；XHS 更严格只读处理。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[security precondition] 必须确认没有 cookie、token、signed URL、browser profile path、QR 图片、auth sidecar、raw stdout/stderr secret 进入 durable artifact。任何 evidence 都先 redaction，再 receipt / handoff / export。

## 4. Steps / steps

[operator step] S1. 把场景改写成一句可审计任务：对 evidence、handoff、RAW candidate、dispatch report 做 PII 与敏感字段边界扫描。

[operator step] S2. 锁定检查对象：authority files、allowed_paths、forbidden_paths、runtime flags、frontmatter、secrets、PII。

[operator step] S3. 先用快速 grep/manifest scan 找显性问题，再用语义 review 找“看似候选、实则批准”的 wording。

[operator step] S4. 对每个 finding 标注 severity、source、fix-or-bound、是否需要 human approval。

[operator step] S5. 如果触及 hard redline，停止下游动作；只允许写 audit note 或 rollback plan。

[operator step] S6. 修复后复跑同一检查，保留 before/after evidence pointer。

[operator step] S7. 把结果写成 candidate self-audit，不把本 audit 自动升级为 authority。

[operator step] S8. 把禁止项写入任务头：不得过度依赖宽松 regex；不得把 false negative 当安全通过。

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

## 7. Lessons learned / lessons

[lesson] L1. Wave 4 的核心教训是 terminal report 不等于所有 plane clear；每个结论都要说明它证明了哪一层、没有证明哪一层。

[lesson] L2. Dispatch127-176 audit 说明 candidate pack 可以结构强、manifest clean，但仍不是 execution approval；高质量包也要等 readback 与 gate。

[lesson] L3. ContentFlow L 提示中的 4h27m / 21 swap 经验提醒：多窗口工作最大的失败模式是上下文丢边界，不是写得慢。

[lesson] L4. silent flexibility 需要被记录和复核；模型主动修复可能有价值，但没有显式 amendment 就不能改变 scope。

[lesson] L5. 产品 proof 应早于硬化：topic-card-lite、RAW handoff、user-visible review 比继续堆 dispatch 更能证明真实价值。

[lesson] L6. redaction_applied=true 需要字段证明，而不是一行声明。

## 8. Linked artifacts / linked

[linked reference] A1. linked_dispatch: P4-BND-BND-PII-REDACTION, P4-BND-HARD-REDLINES

[linked reference] A2. linked_tools: redaction regex, word boundary review, sensitive_fields_removed

[linked reference] A3. linked_rules: ~/.claude/rules/security.md, ~/.claude/rules/testing.md, ~/.claude/rules/development-workflow.md, ~/.claude/rules/execution-discipline.md

[linked reference] A4. linked_skill: boundary-audit

[linked reference] A5. source_docs: PRD-v2、SRD-v2、AGENTS、current.md、contracts-index、Dispatch127-176 manifest、Codex audit、post-dispatch176 strategy/roadmap/raw bridge candidate。

## 9. Footer / footer

[footer boundary] RB-BND-05 是 candidate / not-authority SOP。读者可以用它做 checklist、audit、prompt scaffold 或 dispatch draft；不能把它当作用户授权、runtime unlock、legal conclusion、production code change、authority writeback 或 downstream publish approval。

[footer next action] 下一步如果要执行，必须另开任务：写明 owner、allowed_paths、forbidden_paths、validation command、rollback plan、evidence sink、是否需要 external audit。直到这些字段齐全，本 SOP 的安全结论保持 hold。

## Appendix — operator audit card

[scenario triage] `RB-BND-05` 的最小可执行判断不是“这个场景是否有价值”，而是“在 `PII redaction scan（regex + word boundary）` 中，当前输入是否精确命中 `PII / redaction / 手机号 / 邮箱 / 身份证`，并且没有触发更高风险 lane”。把 redline 当成独立审计面：先证明未触碰，再讨论功能是否完成；grep 结果只是一层证据。 这张卡用于开工前 60 秒 readback：说清楚 source、owner、gate、evidence sink 与 stop condition；说不清楚时，状态保持 hold。

[failure mode] 本场景风险等级为 `high`，需要优先防止“把候选 SOP 当执行批准”的漂移。最危险的捷径是用“没有明显关键词”替代 authority scan，或忽略 frontmatter wording 中的隐性批准语。 复盘时要把失败分成三类：前置证据不足、步骤越界、验证口径过宽；不要笼统写成“模型理解有误”。

[verification cue] 人工复核 write_enabled、overflow lane、authority files、secret/PII、legal posture、runtime flags 和 post-merge SHA。 对每个 cue 都要留下可审计文字：`checked_by`、`checked_at`、`source_ref`、`result`、`residual_risk`。如果 cue 只能凭记忆确认，就写 `unverified_in_current_environment`，不要补写成通过。

[handoff card] handoff 必须包含 scan command、matched files、false-positive rule、human review notes、hold reason 和 unblock owner。 推荐在下一窗口开头复制四行：`intent:`、`allowed:`、`blocked:`、`verify:`。这能把 ContentFlow L 提示里的多窗口换手教训转成可操作记忆，减少 21 次 swap 类场景中的边界遗失。
