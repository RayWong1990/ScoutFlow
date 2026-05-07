---
status: "candidate / cloud_prompt / not-authority"
authority: not-authority
created_at: 2026-05-07
anti_pattern_id: AP-BL-01
cluster: "Boundary-Leak / Overflow Slip"
risk_level: critical
first_seen_in: "Wave4 retro PR #113/#129 dry-run note"
introduced_or_exposed: exposed
detect_method: grep
prevent_method: contract
escape_difficulty: critical
linked_runbook: RB-BL-01
linked_dispatch: P3-BL-01
linked_rule: "~/.claude/rules/security.md"
no_actual_rule_deployment_implied: true
---
# AP-BL-01 — write_enabled=False implies future unlock

## 1. Mission

[evidence-backed] 本条 anti-pattern 的任务是把 `Boundary-Leak / Overflow Slip` 中的一个具体失败形态固化为可查、可 detect、可 prevent 的单文件规则。它不部署任何 hook，也不修改任何 authority 文件；它只把历史锚点、触发 signal、后果、正例、检测与预防条款写成 candidate spec。核心要保护的是：快速并行仍然必须保留显式授权、真实边界、证据标签和 introduced/exposed 归因，不允许把最近动作自动解释成更大权限。

## 2. 反例描述 / Anti-example

[evidence-backed] 反例是：看到 dry-run helper 和 write_enabled=false，就写成“commit path ready，只差打开开关”。 这个反例危险的地方不在于某个单点动作必然错误，而在于它把“可继续分析”“可作为候选库存”“可在本地预览”“被用户追认保留”混写成“已获执行授权”。当多窗口同时工作时，这种写法会让后续 agent 只看到顺滑叙述，看不到 stop-line、partial、not-authority 或 blocked lane。

[derived] 在实际执行中，最常见的口头信号包括“顺手补一下”“这个应该也算同一 scope”“只是 docs 不是 authority”“既然 preview 能跑，write 也快了”“既然前一个 PR merged，后面可继续”。这些短语本身不是罪证，但当它们没有配套 allowed_paths、owner、receipt、gate、evidence label，就会变成 silent flexibility。

## 3. 触发 signal / Trigger signals

[evidence-backed] 触发 signal 需要同时看文本、diff 和 ledger。文本 signal 是出现 `看到 dry-run helper 和 write_enabled=false，就写成“commit path ready，只差打开开关”。` 或与其同义的含混授权；diff signal 是 touched path 超过派单或 authority writer 不清；ledger signal 是 closeout 只写 done/pass/clear，却缺少 amendment、partial、reject、needs-edit 或 user-authorized 字段。

[candidate] 推荐 grep/static/human 混合检查：`grep -RInE '(顺手|顺便|works|PASS|DONE|ready|approved|unlock|write_enabled|migration|browser automation|BBDown|ASR)' docs/research/post-frozen docs/PRD-amendments docs/SRD-amendments`。命中不等于违规，但命中后必须追问：这句话是事实、推断、候选，还是授权？

## 4. 后果 / Consequences

[derived] 后果通常分三层。第一层是局部 truth 被污染：一个 preview、partial、candidate 或 reported validation 被写成 complete。第二层是协作策略被污染：下一个窗口不再知道自己是在修复 introduced defect，还是处理 exposed historical debt。第三层是路线决策被污染：本该进入 overflow 的 runtime、migration、vendor 或 authority promotion 被塞进默认主线。

[derived] 对 ScoutFlow 这种“最大马力 + 安全并行 + 强视觉 + 飞轮迭代”的系统，最贵的不是多写一个文件，而是让后续 agent 继承错误前提。错误前提会让成本、token、PR topology、视觉验收和 evidence provenance 全部继续偏移。

## 5. 正例对照 / Positive counterexample

[evidence-backed] 正例不是停工，而是把继续推进所需的边界写清楚：保留候选资产，但写明 not-authority；保留 preview，但写明 not true write；合并 run 或 PR，但写明 pre-authorization、partial 保留、held-back 原因；发现偏差后，区分 introduced vs exposed，并让 receipt 明确 user-authorized / accepted_partial_scope_deviation / rollback / defer。

[candidate] 对本条而言，正例句式是：`This change is candidate-only; no actual rule deployment implied; authority files untouched; introduced_or_exposed=exposed; evidence source = Wave4 retro PR #113/#129 dry-run note; escalation requires explicit user authorization.` 这类句式虽然啰嗦，但能让未来窗口快速判断自己能不能继续。

## 6. Detect rule

[candidate] `detect_method=grep`。最低限度检测规则：在 PR body、checkpoint、run-report、dispatch frontmatter 和 changed filenames 中同时扫描四类字段：授权字段、scope 字段、evidence 字段、boundary 字段。任何一个字段从 blocked/candidate/partial/not-authority 变成 works/pass/approved/authority，必须要求 reviewer 写出来源。

[candidate] 可执行伪规则：`if claim in ['works','PASS','DONE','approved','ready_for_next'] and not evidence_ref: flag`. 对路径类风险：`if touched_path not in allowed_paths and not explicit_amendment: flag`. 对本条特有风险：`if 'AP-BL-01' mapped signal appears and introduced_or_exposed is blank: flag`. 这些规则只是候选 detect rule，不表示已经部署。

## 7. Prevent rule

[candidate] `prevent_method=contract`。预防应写进 dispatch schema、PR body template、run report template 或 review checklist，而不是靠记忆。每个可疑升级都必须同时填：`scope_delta`、`authority_surface_touched`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。缺任一项，只能写 concern/partial，不得写 clear。

[rule-derived] 与 `~/.claude/rules/security.md` 的关系是反向约束：本文件不复制 canonical 规则，只把该规则在本项目中的失败反例写成候选百科条目。真正部署时应改规则或 hook；本 U11 包只提供 candidate spec。

## 8. Escape clause

[candidate] `escape_difficulty=critical`。发现此 anti-pattern 后，不应立刻 rollback 或继续冲刺，而应先做三步逃逸：第一，冻结新写入，生成 delta table；第二，把每个 claim 改标为 canonical fact / reported evidence / candidate / inference / needs_refresh；第三，请用户或 authority writer 选择 keep、rollback、defer 或 amend_and_proceed。

[derived] 如果已经 merge，则 escape clause 不是假装没发生，而是写 amendment ledger：列出受影响文件、最初错误句、正确句、保留原因、是否改变 downstream gate。若它只是 exposed historical debt，应写“暴露而非引入”，避免把责任压到最近 PR。

## 9. 真实 attribution / Historical attribution

- [evidence-backed] 01_external_reports/wave4-retrospective-v2-2026-05-05.zh.md — Dry-run commit is not a true commit; keep dry_run=true and write_enabled=false until approval.; The document did not rerun tests and marks PR validation as reported evidence.; Candidate docs are not authority and must not become execution packs silently.
- [evidence-backed] PR #240 `Run-3+4: PF-C1 proof pair + PF-C2 RAW handoff` — Run-3 and Run-4 were combined into a single PR by pre-authorization.; C2 remained partial and can_open_c4 stayed false.; Per-dispatch PRs were held back to preserve honest partial signal.; Boundary explicitly forbids BBDown, yt-dlp, ffmpeg, browser automation and migration; write_enabled=False preserved.

[evidence-backed] 归因结论：`introduced_or_exposed=exposed`。这个字段是本条的核心，因为许多问题不是最近动作创造的新缺陷，而是新动作把旧边界、旧工具、旧文档措辞或旧派单 schema 的不足暴露出来。没有这个区分，团队会在错误层级修补。

## 10. Linked runbook / dispatch / rule

[candidate] linked_runbook: `RB-BL-01`；linked_dispatch: `P3-BL-01`；linked_rule: `~/.claude/rules/security.md`。U9/U10 实源在本环境未命中，因此这些 ID 是候选映射形状，不是 authority runbook 事实。

[boundary] 本文件不批准 execution、runtime、migration、browser automation、vendor adoption、authority promotion 或 hook deployment。它只能作为 U11 candidate anti-pattern encyclopedia 的一个可审计条目。

[derived] 补充判据：当 reviewer 看到 `write_enabled=False implies future unlock` 时，应优先问三个问题：一，当前句子是否把证据层、推断层和授权层分开；二，当前动作是 introduced defect 还是 exposed debt；三，是否存在更窄的 safe continuation。只要任一问题没有答案，就不应把 closeout 写成 clear，而应写 partial 或 needs-amendment。

[derived] 补充判据：当 reviewer 看到 `write_enabled=False implies future unlock` 时，应优先问三个问题：一，当前句子是否把证据层、推断层和授权层分开；二，当前动作是 introduced defect 还是 exposed debt；三，是否存在更窄的 safe continuation。只要任一问题没有答案，就不应把 closeout 写成 clear，而应写 partial 或 needs-amendment。
