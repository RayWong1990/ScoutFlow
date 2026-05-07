---
status: "candidate / cloud_prompt / not-authority"
authority: "not-authority"
created_at: "2026-05-07"
title: "DETECT-RULE-CATALOG-2026-05-07"
kind: "detect-rule-catalog"
no_actual_rule_deployment_implied: true
---

# Detect Rule Catalog

[evidence-backed] 本 catalog 汇总所有候选 detect rule，按 regex、static、grep、human、audit 五类组织。它不部署 hook，只提供可转写为后续 schema/hook/review checklist 的候选规则。

## grep

### AP-SF-04 — Worker-guessed scope expansion

[candidate] 主规则：扫描 `worker 从“应该补 proof”推断出 production expansion、conftest 或 contract test change，而没有在派单内获得对应 allowed_paths。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-SF-04|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-SF-07 — Allowed path silent change

[candidate] 主规则：扫描 `新父目录被创建时没有说明它仍在 allowed path 语义内，reviewer 只能在“新目录=越界”和“必须创建”之间猜。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-SF-07|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-SF-08 — Threshold silent loosen

[candidate] 主规则：扫描 `synthetic UAT/readback 从 works 被写成 partial 前没有保留触发依据，或者相反把 partial 偷升为 works。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-SF-08|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-SF-09 — Verdict wording silent escalate

[candidate] 主规则：扫描 `外部审计有 reject/concern，但 closeout 摘要只写 clear/pass/done，让后续窗口以为没有 amendment debt。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-SF-09|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-AC-01 — Dual-window writes docs/current.md

[candidate] 主规则：扫描 `两个窗口同时认为自己可以更新 docs/current.md，最终一个覆盖另一个，且没有 single-writer ledger。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-AC-01|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-AC-03 — task-index numbering conflict

[candidate] 主规则：扫描 `并行窗口各自分配 task 编号，没有先读 authority task-index，造成 ID 碰撞或重复语义。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-AC-03|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-AC-04 — decision-log append rewritten as replace

[candidate] 主规则：扫描 `应 append 的决策日志被 rewrite，抹掉 earlier verdict、rejection、amendment 与用户授权链。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-AC-04|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-AC-06 — AGENTS.md rewritten instead of amended

[candidate] 主规则：扫描 `为适配一次 run 重写 AGENTS.md，破坏全局工作流约束，且没有 authority promotion audit。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-AC-06|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-AC-07 — Authority promote skips audit gate

[candidate] 主规则：扫描 `candidate/not-authority 文件被后续窗口引用为 PRD/SRD/current authority，省略 promotion gate。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-AC-07|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-BL-01 — write_enabled=False implies future unlock

[candidate] 主规则：扫描 `看到 dry-run helper 和 write_enabled=false，就写成“commit path ready，只差打开开关”。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-BL-01|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-BL-02 — BBDown live runtime implied approval

[candidate] 主规则：扫描 `BBDown 从 research/prestudy 进入默认 run body，而不是继续标 runtime blocked/overflow-only。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-BL-02|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-BL-03 — ASR runtime implied approval

[candidate] 主规则：扫描 `audio_transcript/ASR/ffmpeg 从 future/candidate 语义漂移为可执行 worker。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-BL-03|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-BL-04 — Browser automation implied approval

[candidate] 主规则：扫描 `视觉审查需要截图，被误读成已经批准 Playwright/browser automation。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-BL-04|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-BL-05 — Migration implied approval

[candidate] 主规则：扫描 `DB vNext 或 evidence ledger 研究稿被读成 migrations/** 可写入执行授权。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-BL-05|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-BL-08 — Vendor candidate silently accepted

[candidate] 主规则：扫描 `把 vendor spike、OpenDesign reference 或 tool research 当作 accepted implementation dependency。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-BL-08|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-BL-09 — Preview-only drifts into production write

[candidate] 主规则：扫描 `preview panel、dry-run commit、markdown renderer 串联后被写成 production write path 已经可用。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-BL-09|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-BL-10 — Candidate file silently becomes authority

[candidate] 主规则：扫描 `post-frozen research、external report、候选 PRD/SRD outline 被直接提升为 authority，不经 audit/promotion。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-BL-10|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VS-06 — Whisper local install not verified

[candidate] 主规则：扫描 `把 Whisper/本地 ASR 写进方案，但没有验证依赖、模型下载、磁盘、权限和离线失败模式。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VS-06|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MC-05 — MEMORY.md grows past usable size

[candidate] 主规则：扫描 `MEMORY.md 成为长篇 history dump，真正的 current gates、recent decisions 和 open risks 被淹没。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MC-05|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MC-07 — Recover without git fetch

[candidate] 主规则：扫描 `恢复任务时不刷新 origin/main，不比较 PR truth，就诊断 authority drift。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MC-07|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MA-04 — Silent-flexibility detector not run

[candidate] 主规则：扫描 `run closeout 没有扫描 amend_trigger、silent_flexibility、scope_drift 字段，导致已知坑继续扩散。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MA-04|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-CT-06 — Repeat prompt without cache

[candidate] 主规则：扫描 `相同长 prompt 在多个窗口重复跑，没有 cache evidence snapshot，输出差异无法归因。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-CT-06|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-ED-04 — No verification loop

[candidate] 主规则：扫描 `文档或代码变更后不跑 redline、secrets、diff check、JSON parse 或对应 app test。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-ED-04|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-ED-06 — Diagnose without git fetch

[candidate] 主规则：扫描 `不刷新 origin/main 就判断 authority/current state，尤其在多 PR 快速合并后高危。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-ED-06|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-ED-08 — Hooks skipped for speed

[candidate] 主规则：扫描 `为了最大马力跳过 hooks，结果 redline/secrets/diff/format 问题被下游审计才发现。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-ED-08|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-DT-01 — PASS/DONE/OK wording creep

[candidate] 主规则：扫描 `候选态或 reported evidence 被写成 PASS/DONE/OK，掩盖 reject、partial、not-rerun 或 needs-edit。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-DT-01|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-DT-02 — Fake wall-clock duration

[candidate] 主规则：扫描 `为了满足 expected_thinking_minutes 写入虚假的 150+ 分钟，而不是记录真实执行时间。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-DT-02|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-DT-03 — Live web claimed without live web

[candidate] 主规则：扫描 `没有联网或没有刷新资料，却在文档写“live web checked/public web truth”。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-DT-03|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-DT-04 — Claim label missing

[candidate] 主规则：扫描 `段落没有 canonical fact / inference / tentative / needs refresh 标签，后续 agent 无法判断可用性。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-DT-04|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-DT-06 — Tested claim without evidence

[candidate] 主规则：扫描 `没有实际运行测试，却写“经测试/works/pass”，或者只引用 PR body 不标 reported evidence。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-DT-06|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-DT-07 — Synthetic evidence labelled works

[candidate] 主规则：扫描 `synthetic UAT/readback 被标 works，直到 amendment 才降级为 partial。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-DT-07|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

## static

### AP-SF-06 — Checkpoint field silent rename

[candidate] 主规则：扫描 `final checkpoint 新增或改名字段时，只让读者自行推断 LP-06/07 dual coverage，而不写兼容字段。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-SF-06|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-AC-02 — Sidecar agent writes authority files

[candidate] 主规则：扫描 `sidecar/worker 以“只是补文档”为由修改 current.md、decision-log.md、AGENTS.md 或 task-index.md。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-AC-02|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-AC-05 — contract-index baseline drift

[candidate] 主规则：扫描 `contracts-index 仍把 DB vNext/candidate-only 作为 blocked/context，但新文档把它当默认 backbone。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-AC-05|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-AC-08 — Authority writer max=1 violation

[candidate] 主规则：扫描 `manifest 已限制 authority_writer，但执行时多个 commander_self 或 agent 同时写同一 authority surface。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-AC-08|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-BL-07 — Dispatch schema lacks can_open flags

[candidate] 主规则：扫描 `run closeout 只写 ready_for_next，不拆 can_open_c4、can_open_runtime、can_open_migration 等细粒度 gate。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-BL-07|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MA-05 — Single-writer race

[candidate] 主规则：扫描 `worker 与 commander_self 同时写 authority，review 只看最终 diff，无法看到竞争过程。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MA-05|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-CT-05 — API retry without backoff

[candidate] 主规则：扫描 `抓取 GitHub、ASR、LLM 或 vendor API 时盲目 retry，放大成本、速率限制和过期证据。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-CT-05|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-ED-02 — Coverage threshold below 80 without waiver

[candidate] 主规则：扫描 `测试覆盖下降或未度量，却在 PR body 写“tests pass”替代 coverage waiver。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-ED-02|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-ED-05 — Import path assumption

[candidate] 主规则：扫描 `validator 或 test 假设旧路径/旧 glob，面对 Dispatch*.md 新形状仍返回 clear。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-ED-05|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

## audit

### AP-SF-01 — Packed repair without explicit authorization

[candidate] 主规则：扫描 `把 PR #226 的 bounded preview seam 与 PR #228 的 larger repair 当成同一条连续事实，不显式说明 replacement vs incremental truth。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-SF-01|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-SF-02 — Run-1 amendment proceeds without explicit gate replay

[candidate] 主规则：扫描 `在 amend_and_proceed 后继续推进，但 receipt 没有把 gate bypass 的用户授权写回，后续窗口只能猜测。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-SF-02|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-SF-05 — Multi-PR topology drift

[candidate] 主规则：扫描 `repair PR 覆盖或替代早前 PR，但 ledger 仍按“增量累加”叙述，制造两套 truth。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-SF-05|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-SF-10 — Boundary silent expand

[candidate] 主规则：扫描 `从 preview、handoff 或 raw staging 推断 browser automation、migration、BBDown、yt-dlp、ffmpeg 等 runtime lane 可以顺手打开。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-SF-10|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-BL-06 — Five overflow lanes unlocked in one PR

[candidate] 主规则：扫描 `DB、runtime、ASR、browser automation、true vault write 被同一个“hardening PR”同时打开。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-BL-06|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VF-08 — Good-enough visual pass

[candidate] 主规则：扫描 `技术渲染 pass 后写“视觉差不多可以”，没有逐 Gate 判断。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VF-08|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VF-09 — Retrofitted visual after code

[candidate] 主规则：扫描 `代码先做完，再把 visual review 当成最后截图润色，导致 IA 与证据流无法修正。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VF-09|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VS-01 — Single vendor lane lock-in

[candidate] 主规则：扫描 `把某一个 downloader、ASR 或 design reference 固定为唯一未来路径，不写替代方案或 kill switch。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VS-01|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VS-02 — Vendor selection without spike audit

[candidate] 主规则：扫描 `直接把 vendor 放进 dispatch allowed work，而没有安装、许可、输入输出、失败模式和替代方案 spike。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VS-02|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VS-05 — ASR vendor not benchmarked

[candidate] 主规则：扫描 `ASR vendor 只按名气选择，没有本地样本、成本、延迟、分段 provenance 与失败恢复对比。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VS-05|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VS-07 — Cloud API treated as free

[candidate] 主规则：扫描 `把 cloud API 当作无限免费 retry 资源，长 prompt、重复跑、无 cache 导致成本和 evidence drift。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VS-07|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MC-02 — Handoff missing closure Step 5

[candidate] 主规则：扫描 `session 结束前没有沉淀 next action、redline、evidence gap 和 owner，下一窗口重踩。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MC-02|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MC-06 — Cross-session context assumed persistent

[candidate] 主规则：扫描 `新窗口假设自己记得上一窗口的授权，不重新区分 zip truth、GitHub truth 和 inference。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MC-06|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MA-01 — Multi-window dispatch no ledger

[candidate] 主规则：扫描 `多个窗口各自跑 dispatch，但没有统一 ledger 记录 owner、write surface、merge order 和 receipt status。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MA-01|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MA-02 — amend_and_proceed skips user authorization

[candidate] 主规则：扫描 `发现 scope drift 后直接 amend_and_proceed，却不记录用户是否接受 keep、rollback 或 partial deviation。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MA-02|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MA-03 — Three-window cloud audit only uses one or two windows

[candidate] 主规则：扫描 `对外声称 3-window audit，但 synthesis 只纳入部分窗口或漏记 dissent。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MA-03|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MA-06 — introduced vs exposed ignored

[candidate] 主规则：扫描 `把被新动作暴露的历史债归因给最近 PR，导致修错层级并惩罚错误 owner。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MA-06|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MA-07 — Cross-window memory drift

[candidate] 主规则：扫描 `窗口 A 记得 partial，窗口 B 只看到 merged PR，于是把 C2 partial 写成 done。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MA-07|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-ED-01 — No TDD before implementation

[candidate] 主规则：扫描 `bounded frontend seam 先做实现再补测试，无法证明 preview/reset/fail-loud 行为真被保护。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-ED-01|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-ED-03 — Code-review agent skipped

[candidate] 主规则：扫描 `高风险 boundary PR 没有独立 code review，仅由执行窗口自证。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-ED-03|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-DT-05 — Evidence not refreshed

[candidate] 主规则：扫描 `引用旧 pack 或旧 PR body，不刷新 current repo truth，却做 final route decision。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-DT-05|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

## human

### AP-SF-03 — Multi-dispatch silent merge

[candidate] 主规则：扫描 `把多个 dispatch 或多个 run 合并成单 PR，却不写 pre-authorization、partial 保留与 held-back per-dispatch PR 的原因。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-SF-03|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VF-01 — Primary title loses hierarchy to subtitle

[candidate] 主规则：扫描 `强视觉 surface 中标题、状态和值没有层级，副标题或 decoration 抢走第一注意点。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VF-01|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VF-02 — Subtitle or toast occludes critical content

[candidate] 主规则：扫描 `tooltip、toast、字幕或 overlay 压住 URL、blocked state、trust trace 等关键证据。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VF-02|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VF-03 — Random spacing and alignment

[candidate] 主规则：扫描 `panel 间距、输入框、状态 chip 与证据行缺少栅格节奏，看起来像拼装 dashboard。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VF-03|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VF-04 — Contrast below durable review threshold

[candidate] 主规则：扫描 `长 URL、ID、state 与 caption 对比不足，操作者不能长时间扫描。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VF-04|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VF-05 — Decoration heavier than evidence

[candidate] 主规则：扫描 `network/glow/card decoration 比 evidence row、blocked state 和 dependency edge 更显眼。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VF-05|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VF-06 — Saturation hijacks attention

[candidate] 主规则：扫描 `高饱和警示色、渐变或 cyberpunk 效果抢走工作台的证据优先级。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VF-06|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VF-07 — CJK/Latin baseline mismatch

[candidate] 主规则：扫描 `中文说明、英文 URL、代码 ID 混排时 baseline 与行高错位，影响审阅。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VF-07|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VF-10 — Mobile safe-area occlusion

[candidate] 主规则：扫描 `移动端 safe-area、键盘或固定操作条挡住 blocked state/URL/action，使用户误以为 lane 已批准。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VF-10|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VS-03 — BBDown cease-and-desist not rechecked

[candidate] 主规则：扫描 `BBDown 被当作技术问题而不是法律/平台边界问题，未在每次 runtime unlock 前复核。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VS-03|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-VS-04 — yt-dlp legal refresh skipped

[candidate] 主规则：扫描 `yt-dlp 从“用户自己已有工具”变成系统默认依赖，没有最新合法性和平台条款复核。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-VS-04|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MC-01 — Handoff as transcript dump

[candidate] 主规则：扫描 `handoff 只是流水账，缺少 what changed / what is blocked / what must not be inferred。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MC-01|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MC-03 — /clear decided by duration not semantic boundary

[candidate] 主规则：扫描 `只因为聊久了就 /clear，或者因为还能回复就不 /clear，不看任务是否跨越 authority gate。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MC-03|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-MC-04 — /compact without anchor

[candidate] 主规则：扫描 `/compact 前没有列出 source anchors、PR anchors、blocked lanes 和 pending questions，压缩后只剩结论。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-MC-04|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-CT-01 — Dispatch without token estimate

[candidate] 主规则：扫描 `派单没有估算读取、生成、复核 token，导致中途压缩或截断时丢失关键 anchors。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-CT-01|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-CT-02 — Long session without /clear

[candidate] 主规则：扫描 `长 session 连续处理多个 cluster，不在语义边界清理，旧上下文继续污染新判断。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-CT-02|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-CT-03 — /compact loses anchors

[candidate] 主规则：扫描 `/compact 后保留了结论，丢掉 PR #、dispatch ID、blocked lane 和 source path。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-CT-03|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-CT-04 — No cost dashboard

[candidate] 主规则：扫描 `每次 deep research 不记录 model/window/tool cost，无法比较本地、cloud 与 agent fan-out。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-CT-04|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

### AP-ED-07 — Destructive git misuse

[candidate] 主规则：扫描 `为清理 run 使用 reset/clean/checkout 覆盖未保存 artifacts，没有先确认 worktree 与 user-owned files。` 的同义表达，并核对 `evidence_label`、`user_authorization_ref`、`allowed_paths`、`authority_surface_touched`、`introduced_or_exposed` 是否齐全。命中后输出 concern，不自动判 fail。

[candidate] Example command: `grep -RInE 'AP-ED-07|approved|works|PASS|DONE|partial|not-authority|write_enabled|migration|browser automation|BBDown|ASR' docs/ .github/ tools/`。

## regex

[candidate] 本批次没有以该 method 作为主检测方式的条目，但可作为辅助检测。

