---
title: Single Bilibili URL metadata-only capture（Phase 1A 窄门）
status: candidate
authority: not-authority
created_at: 2026-05-07
runbook_id: RB-CAP-01
cluster: Capture / Acquisition
trigger_keywords:
  - bilibili
  - manual_url
  - metadata_only
  - 单条URL
  - quick capture
risk_level: medium
single_user_applicable: true
multi_agent_applicable: false
linked_dispatch:
  - P2-CAP-CAP-METADATA-ONLY
linked_pr:
  - T-P1A-002
  - T-P1A-011C
linked_tools:
  - POST /captures/discover
  - POST /jobs/{job_id}/complete
  - GET /captures/{capture_id}/trust-trace
  - python tools/check-secrets-redlines.py
linked_skill:
  - capture-scope-gate
linked_rule:
  - ~/.claude/rules/security.md
  - ~/.claude/rules/execution-discipline.md
  - ~/.claude/rules/parallel-safety.md
source_basis:
  - uploaded Cloud Prompt U10 2026-05-07
  - ScoutFlow post176 cloud audit pack 2026-05-05
  - PRD-v2 / SRD-v2 / AGENTS / current.md excerpts present in audit pack
  - Dispatch127-176 manifest and Codex audit excerpts present in audit pack
boundary_statement: candidate SOP only; does not approve runtime, authority write, package change, migration, browser automation, ASR, or vault true write.
---
## 1. Mission / mission

[candidate procedure] 本 runbook 把 `Single Bilibili URL metadata-only capture（Phase 1A 窄门）` 固化为 single-user prosumer 可重复 SOP。目标不是批准动作，而是让用户在遇到 `bilibili, manual_url, metadata_only` 这类触发词时，能先检查边界、证据与 rollback，再决定是否另开获授权执行。

[canonical fact] 本库采用 PRD-v2/SRD-v2 口径：ScoutFlow 是 single-user、local-first 工作台，authority-first 以 SQLite + FS + state words 为核心；Console 只是 projection，Worker 不能直写 SQLite，所有有效写入都必须走 Thin API 或明确授权的 repo authority writer。

[boundary note] 该场景风险等级为 `medium`。风险来自：不得下载媒体、不得触发 BBDown live、不得扩到作者主页/推荐列表/评论/ASR。 因此本文件只提供候选步骤和审计点，不构成 runtime approval、migration approval、browser automation approval、ASR approval、vault true write approval 或 package approval。

## 2. Trigger / trigger

[operator trigger] 当用户输入、handoff、dispatch 或下游请求出现以下关键词时启用本 SOP：bilibili, manual_url, metadata_only, 单条URL, quick capture。如果同时出现更高风险关键词，例如 credential、migration、runtime、browser automation、ASR、true write、authority edit，则先按 Boundary / Audit cluster 重新分级。

[negative trigger] 不要在以下情况下启用本 SOP 的执行路径：不得下载媒体、不得触发 BBDown live、不得扩到作者主页/推荐列表/评论/ASR。 如果只是研究、复盘、教育用途，可以阅读本 SOP；如果要实际运行命令或写文件，必须另有明确 dispatch、allowed_paths、owner 和 validation plan。

## 3. Preconditions / preconditions

[precondition] P1. ScoutFlow 是 single-user / local-first 的内容采集与证据整理系统；事实源以 SQLite + FS + state words 为核心。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P2. PRD-v2/SRD-v2 明确 Phase 1A 只批准 Bilibili manual_url + metadata_only 的窄闭环。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P3. LP-001 要求 recommendation / keyword / RAW gap 不得直接创建 capture。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P4. audio_transcript、BBDown live、yt-dlp、ffmpeg、ASR、browser automation、vault true write、migration、Phase 2-4 runtime 均仍 gated。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P5. XHS 与 YouTube runtime capture 在 SRD-v2 当前口径下必须拒绝；XHS 更严格只读处理。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[precondition] P6. 本 runbook 的直接场景是：只处理用户明确给出的单个 Bilibili URL，目标是拿到 redacted metadata evidence、receipt ledger 和 trust-trace safe summary。 这条前置条件必须在执行前被 readback；如果当前环境无法验证，就在 ledger 中写 `unverified_in_current_environment`，不要补成肯定事实。

[security precondition] 必须确认没有 cookie、token、signed URL、browser profile path、QR 图片、auth sidecar、raw stdout/stderr secret 进入 durable artifact。任何 evidence 都先 redaction，再 receipt / handoff / export。

## 4. Steps / steps

[operator step] S1. 把场景改写成一句可审计任务：只处理用户明确给出的单个 Bilibili URL，目标是拿到 redacted metadata evidence、receipt ledger 和 trust-trace safe summary。

[operator step] S2. 确认输入来源：如果不是用户明确给出的 single manual URL，先转入 scope gate，而不是继续 capture。

[operator step] S3. 确认平台与 preset：当前 Phase 1A 只允许 Bilibili manual_url metadata_only；其他平台必须降级为候选记录。

[operator step] S4. 先执行 redline mental check：是否触及 BBDown live、yt-dlp、ffmpeg、ASR、browser automation、credential、RAW gap。

[operator step] S5. 只在获授权环境中通过 Thin API 入口记录动作；不要由 worker 直写 SQLite 或 FS authority。

[operator step] S6. receipt 前确认 evidence 已 redacted，并且 platform_result、artifact kind、source_surface 与当前 phase 一致。

[operator step] S7. 读取 trust-trace 时只解释 safe summary，不把 metadata success 推导成 media/audio readiness。

[operator step] S8. 把禁止项写入任务头：不得下载媒体、不得触发 BBDown live、不得扩到作者主页/推荐列表/评论/ASR。

[operator step] S9. 如果任何一步发现 authority、runtime、secret、legal posture 或 same-file ownership 不清楚，立即转入 rollback/hold，而不是继续补假设。

## 5. Verification / verification

[verification item] V1. frontmatter 是否含 status: candidate、authority: not-authority、risk_level、trigger_keywords、linked_dispatch、linked_rule。

[verification item] V2. allowed_paths 与 forbidden_paths 是否能从 dispatch、manifest 或 prompt 中读到；读不到时必须标为 blocked。

[verification item] V3. 是否没有把 research note、draft spec、local probe report、chat summary、preview artifact 写成 final authority。

[verification item] V4. 是否有 rollback path；如果 rollback 只写“人工处理”，则视为 verification fail。

[verification item] V5. 是否保留 source label：canonical fact、candidate procedure、operator inference、environment limitation。

[verification item] V6. trust-trace 是否只显示 safe summary；receipt 是否没有提升 media/audio approval。

[verification item] V7. LP-001 分类是否通过：manual_url 与 recommendation/keyword/RAW gap 已明确区分。

## 6. Rollback / rollback

[rollback instruction] R1. 如果发现前置条件不成立，立即把任务状态改为 hold/deferred/superseded，而不是继续执行。

[rollback instruction] R2. 如果已经生成候选文件，保留原文件并追加 supersede header 或 quarantine marker；不要静默删除证据。

[rollback instruction] R3. 如果已经产生 PR/diff，先用 git diff 定位越界范围，再选择 revert、reset to HEAD、narrow follow-up PR 或 audit note。

[rollback instruction] R4. 如果出现 secret/PII 暴露，先停止传播并隔离 artifact，再做 redaction repair 与 downstream notification。

[rollback instruction] R5. 如果 authority surface 被误写，必须由唯一 authority writer 按 current/task-index/decision-log/contracts-index 顺序修复。

[rollback instruction] R6. 失败 capture 不删除；记录 failed platform_result、retry lineage、operator note，并防止 failed evidence 被重命名为 success。

## 7. Lessons learned / lessons

[lesson] L1. Wave 4 的核心教训是 terminal report 不等于所有 plane clear；每个结论都要说明它证明了哪一层、没有证明哪一层。

[lesson] L2. Dispatch127-176 audit 说明 candidate pack 可以结构强、manifest clean，但仍不是 execution approval；高质量包也要等 readback 与 gate。

[lesson] L3. ContentFlow L 提示中的 4h27m / 21 swap 经验提醒：多窗口工作最大的失败模式是上下文丢边界，不是写得慢。

[lesson] L4. silent flexibility 需要被记录和复核；模型主动修复可能有价值，但没有显式 amendment 就不能改变 scope。

[lesson] L5. 产品 proof 应早于硬化：topic-card-lite、RAW handoff、user-visible review 比继续堆 dispatch 更能证明真实价值。

[lesson] L6. metadata probe proof 只能证明 metadata，不证明 media/audio readiness。

## 8. Linked artifacts / linked

[linked reference] A1. linked_dispatch: P2-CAP-CAP-METADATA-ONLY

[linked reference] A2. linked_tools: POST /captures/discover, POST /jobs/{job_id}/complete, GET /captures/{capture_id}/trust-trace, python tools/check-secrets-redlines.py

[linked reference] A3. linked_rules: ~/.claude/rules/security.md, ~/.claude/rules/execution-discipline.md, ~/.claude/rules/parallel-safety.md

[linked reference] A4. linked_skill: capture-scope-gate

[linked reference] A5. source_docs: PRD-v2、SRD-v2、AGENTS、current.md、contracts-index、Dispatch127-176 manifest、Codex audit、post-dispatch176 strategy/roadmap/raw bridge candidate。

## 9. Footer / footer

[footer boundary] RB-CAP-01 是 candidate / not-authority SOP。读者可以用它做 checklist、audit、prompt scaffold 或 dispatch draft；不能把它当作用户授权、runtime unlock、legal conclusion、production code change、authority writeback 或 downstream publish approval。

[footer next action] 下一步如果要执行，必须另开任务：写明 owner、allowed_paths、forbidden_paths、validation command、rollback plan、evidence sink、是否需要 external audit。直到这些字段齐全，本 SOP 的安全结论保持 hold。

## Appendix — operator audit card

[scenario triage] `RB-CAP-01` 的最小可执行判断不是“这个场景是否有价值”，而是“在 `Single Bilibili URL metadata-only capture（Phase 1A 窄门）` 中，当前输入是否精确命中 `bilibili / manual_url / metadata_only / 单条URL / quick capture`，并且没有触发更高风险 lane”。把 URL、平台、preset 与 evidence sink 分开确认；任何 recommendation、keyword、RAW gap 都先降级成 signal，不直接进入 capture。 这张卡用于开工前 60 秒 readback：说清楚 source、owner、gate、evidence sink 与 stop condition；说不清楚时，状态保持 hold。

[failure mode] 本场景风险等级为 `medium`，需要优先防止“把候选 SOP 当执行批准”的漂移。最危险的捷径是把 metadata success 外推为 media/audio readiness，或把“用户给过平台名”误读成“用户给了可采集 URL”。 复盘时要把失败分成三类：前置证据不足、步骤越界、验证口径过宽；不要笼统写成“模型理解有误”。

[verification cue] 人工复核 URL 来源、platform_result、redaction_applied、receipt lineage、trust-trace safe summary。 对每个 cue 都要留下可审计文字：`checked_by`、`checked_at`、`source_ref`、`result`、`residual_risk`。如果 cue 只能凭记忆确认，就写 `unverified_in_current_environment`，不要补写成通过。

[handoff card] handoff 必须包含 source_url_hash、platform、preset、forbidden_runtime、rollback_sink 和下一步是否需要 legal posture recheck。 推荐在下一窗口开头复制四行：`intent:`、`allowed:`、`blocked:`、`verify:`。这能把 ContentFlow L 提示里的多窗口换手教训转成可操作记忆，减少 21 次 swap 类场景中的边界遗失。
