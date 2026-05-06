---
title: Strategic Upgrade — PM Master Plan (3 Cloud Lanes Parallel, PF-V Side-by-Side)
status: candidate / commander-prompt-master / not-authority
created_at: 2026-05-07
target_writer: 3 cloud GPT Pro windows (parallel) + user audit after download
project_root: /Users/wanglei/workspace/ScoutFlow
github_repo: https://github.com/RayWong1990/ScoutFlow
audit_baseline_sha: ea509022eb05a552777373394a6fc2a5077f27f6
parallel_lanes: [PF-V (visual prototype), U1 (PRD-v3+SRD-v3), U2 (Phase 2 Unlock Playbook), U3 (Entity v0 Contracts)]
---

# Strategic Upgrade — PM Master Plan

> 用户 4h 睡眠窗口内并行 3 cloud GPT Pro lane（U1 / U2 / U3）+ 你自己另窗口跑的 PF-V，全部独立可并行。
> Cloud GPT Pro 只能 read GitHub 不能 push，所有产物以 **download link / ZIP** 形式给回，用户下载到本地审计。
> 沿用过去 76-125 pack（50 dispatch ZIP）+ Run-1/Run-2 amendment 模式：cloud 写 candidate → 用户/Claude 审计 → 决定 promote 或 amend。

---

## 0. 战略定位（升级维度的本质）

当前 ScoutFlow 在 80-pack 局部最优解状态：
- ✅ 4 run + 1 window-2 实证 80-pack 7-cluster 工程纪律有效
- ✅ Run-1/2/3+4 receipt traceability + 3-window external audit + amend_and_proceed 模式立住
- ❌ 但产品价值仍在 preview-only / metadata_only / write_enabled=False 局部最优 — Phase 2 runtime（真 metadata / 真 transcript / 真 vault write / browser auto / migration）全 Hold
- ❌ PRD-v2 / SRD-v2 是 2026-05-04 base，3 天 8 amendment + 实证未 fold
- ❌ SRD §1.3 outline 4 entity (signals / hypotheses / capture_plans / topic_cards) 仍是 future
- ❌ 5 overflow lane + ScoutFlow→DiloFlow 接口未定

**升级方向**: 从"80-pack 工程纪律"切到"Phase 2 unlock + entity contract + v3 base"，让下一阶段（Run-5 PF-C4 hardening + 真产品价值）有清晰 anchor。

---

## 1. 3 Cloud Lane 设计

| Lane | 目标 | 关键输入 | ZIP 产物文件数 | GPT Pro 思考时长 |
|---|---|---|---|---|
| **U1** | PRD-v3 / SRD-v3 candidate (折叠 v2 + 8 amendment + 4 run 实证 + U2/U3 输入) | PRD-v2 + SRD-v2 + 8 amendment + 4 run 收尾 receipt | 7 | 2-2.5h |
| **U2** | Phase 2 Unlock Playbook (5 lane: true_vault_write / runtime_tools / browser_automation / dbvnext / signal_workbench) | overflow registry + BBDown gate matrix + ASR prestudy + 2 月 web 研究 | 11 | 2-2.5h |
| **U3** | Signal/Hypothesis/CapturePlan v0 + TopicCard v1 contract | SRD §1.3 outline + topic-card-lite v0 + 145/146 历史 + 2 月 ontology 研究 | 10 | 1.5-2h |

总计 **28 markdown 文件 / ~37K 中英文字数 / ~46K tokens / cumulative GPT Pro 6h**。

PF-V (你另窗口跑) 与 3 cloud lane 独立无冲突：
- PF-V 写 `docs/research/visual-prototypes/PF-V/**`
- U1/U2/U3 写 `docs/research/strategic-upgrade/2026-05-07/cloud-output/**`（user 下载后 land）

---

## 2. Pre-flight（user 必跑一次，让 3 cloud window 都能 fetch GitHub）

```bash
cd /Users/wanglei/workspace/ScoutFlow

# 1. 验当前 origin/main
git fetch origin --prune
git rev-parse origin/main  # 期望: ea509022eb05a552777373394a6fc2a5077f27f6

# 2. 把 3 个 cloud prompt 推到 strategic-upgrade-handoff 分支（让 cloud 拉到）
git checkout -b strategic-upgrade-handoff origin/main
git add docs/research/strategic-upgrade/2026-05-07/
git commit -m "chore(strategic): land 3-lane cloud prompts (U1 PRD-v3/SRD-v3 + U2 Phase 2 unlock + U3 entity v0)"
git push -u origin strategic-upgrade-handoff

# 3. 临时 public（仅 4h 窗口）
gh repo edit RayWong1990/ScoutFlow --visibility public --accept-visibility-change-consequences

# 4. 验证可达
curl -sI "https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md" -o /dev/null -w "%{http_code}\n"
# 期望: 200

# 5. 同时丢 3 cloud window
echo '''
窗口 1 (U1 PRD-v3/SRD-v3):
https://github.com/RayWong1990/ScoutFlow/blob/strategic-upgrade-handoff/docs/research/strategic-upgrade/2026-05-07/cloud-prompt-U1-prd-v3-srd-v3.md

窗口 2 (U2 Phase 2 Unlock Playbook):
https://github.com/RayWong1990/ScoutFlow/blob/strategic-upgrade-handoff/docs/research/strategic-upgrade/2026-05-07/cloud-prompt-U2-phase-2-unlock-playbook.md

窗口 3 (U3 Entity v0 Contracts):
https://github.com/RayWong1990/ScoutFlow/blob/strategic-upgrade-handoff/docs/research/strategic-upgrade/2026-05-07/cloud-prompt-U3-entity-v0-contracts.md
'''

# 6. 4h 后收齐 ZIP，flip 回 private
gh repo edit RayWong1990/ScoutFlow --visibility private --accept-visibility-change-consequences
```

---

## 3. 每 Lane 通用约束（写入每个 prompt frontmatter + body）

### 3.1 角色
- 你是 ScoutFlow Cloud GPT Pro 高级架构师 / 产品系统工程师 / 元认知严格审计员。
- 只读 + 只写 ZIP 交付。**禁** push / merge / 改任何 ScoutFlow 文件。
- 输出 = 1 个下载链接（ZIP / 公开 gist / Cloud-hosted 文件）含 N 个 markdown，每个文件结构由 deliverable schema 严格规定。

### 3.2 思考节奏
- 强制 **多 pass 工作流**（每 lane 8-10 pass，每 pass 至少 5-15 min 深度思考）
- 每个 pass 结束做 **self-check**（自相矛盾 / 过度承诺 / claim label 错误 / 边界漂移）
- 完成所有 pass 后做 **adversarial audit**（找 5+ 自找毛病）
- 总时长 ≥ 1.5h，理想 2-2.5h

### 3.3 Claim Label 规则（沿用 PRD-v3 prompt 范例）
强制使用 4 类 label：
- `[canonical fact]`: 直接来自 base authority docs 或 4 run receipts
- `[promoted_addendum-aware inference]`: 从 PRD-v2.1 / SRD-v3 H5/Bridge addenda + 8 amendment 推导
- `[candidate carry-forward]`: candidate-only，未来可能 absorb，目前**不**算 authority
- `[tentative candidate]`: 新提出的 outline / 未来结构

任何 claim 不带 label = 视为 fail。

### 3.4 边界硬规则（违任一即失败）
- 不写任何 final authority 文本（不替代 docs/current.md / task-index.md / decision-log.md / AGENTS.md）
- 不声明 PRD-v3 已 promote / Phase 2 已 unlock / runtime 已 approve
- 不 enable BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migration / true vault write
- 措辞用 `T-PASS / V-PASS / partial / FAIL_ENV / REJECT_AS_X / clear / concern / reject` — 禁裸 PASS / DONE / OK
- candidate-only frontmatter 强制：`status: candidate / [type] / not-authority`

### 3.5 ZIP 交付硬规则
- ZIP 内每文件 frontmatter 全 candidate / not-authority
- 含 `README-deliverable-index.md` 列全部文件 + 字数 + claim label 占比
- 含 `SELF-AUDIT.md` 列 GPT Pro 自找的 5+ 缺陷
- 文件名严格用 dispatch 风格 `KIND-SLUG-2026-05-07.md`
- 不内嵌 binary / image / chart 图片 — 仅 markdown + 必要 mermaid 文本

---

## 4. 收齐后用户操作（4h 后）

```bash
# 1. 下载 3 个 ZIP 到 /tmp/strategic-upgrade-cloud-out/
# (从 GPT Pro 给的 download link 拉)

# 2. 解压每个 ZIP
mkdir -p /tmp/strategic-upgrade-cloud-out/u1
mkdir -p /tmp/strategic-upgrade-cloud-out/u2
mkdir -p /tmp/strategic-upgrade-cloud-out/u3

unzip cloud-u1-output.zip -d /tmp/strategic-upgrade-cloud-out/u1
unzip cloud-u2-output.zip -d /tmp/strategic-upgrade-cloud-out/u2
unzip cloud-u3-output.zip -d /tmp/strategic-upgrade-cloud-out/u3

# 3. CC0 quick informal audit (我可以 5 min 扫一遍)
ls -la /tmp/strategic-upgrade-cloud-out/u*

# 4. 决定 land 路径（3 选）:
#   A. 直接 PR 入 main (沿用 Run-2 amendment 模式)
#   B. 推到 strategic-upgrade-handoff 分支等 3-window 外审
#   C. 部分接受 部分 amend
```

---

## 5. 与 PF-V 协调

| 时段 | PF-V (你窗口) | U1 cloud | U2 cloud | U3 cloud |
|---|---|---|---|---|
| T+0 ~ T+1h | P0-P3 生图 | base v2 read pass | overflow registry pass | SRD §1.3 outline read pass |
| T+1 ~ T+2h | P4-P5 状态 + icons | amendment fold pass | 5 lane vendor matrix pass | entity v0 design pass |
| T+2 ~ T+3h | P6 refinement | v3 outline + traceability pass | spike runbook + audit framework pass | DB schema + state machine pass |
| T+3 ~ T+4h | P7 image→HTML5 | self-audit + ZIP 打包 | risk register + ZIP 打包 | corner case + ZIP 打包 |
| T+4h | 全收齐 → user wake up | | | |

**git lock**: 3 cloud lane **不写** repo（只 read），与 PF-V 完全无冲突。

**rate limit**: 3 cloud window 同账号同 IP，可能撞 GitHub API rate limit (60/h anonymous, 5000/h auth)。建议每个 prompt 内告诉 GPT Pro fetch 频次自限制（每文件读一次，cache 后内推理）。

---

## 6. 风险 + 修正预案

| 风险 | 概率 | 修正 |
|---|---|---|
| Cloud GPT Pro 不能 fetch private repo（user 忘 flip public）| MED | prompt 内含 inline fallback 段（关键内容 1000 字摘要） |
| 3 window 同时跑撞 rate limit | LOW | 每 window 错开 30s 启动 |
| 输出 ZIP 不达 deliverable schema | MED | 每 prompt 末尾含 self-check checklist + reject criteria |
| 输出有 silent flexibility（如 cloud 私自标 promote 而非 candidate）| HIGH | 强制 claim label + frontmatter status 检查（用户审时第一项） |
| Cloud 跑 30 min 就草草输出 | MED | prompt 强调最少 1.5h + 8 pass 工作流 + adversarial audit |

---

## 7. 收齐后的下一步规划

| 路径 | 触发条件 | 后续动作 |
|---|---|---|
| **A. 全 land main** | 3 ZIP CC0 quick audit clear + 用户接受 | 沿用 Run-1/Run-2 amendment 模式：单 PR direct merge |
| **B. 部分 land + 部分 amend** | 部分内容有 silent flexibility 或 over-promotion | 写 amendment prompt 修补，再 land |
| **C. 重写 1 lane** | 某 lane 输出严重不达预期 | 重新发同段 prompt 给另一 cloud window |
| **D. land 后启 Run-5** | U1/U2/U3 + PF-V 全 land + ready_for_run_5 | 写 Run-5 commander prompt（PF-C4 hardening + PF-V handoff 接管） |

---

## 8. 索引

- 主 PM 文档（本文）：`README.md`
- U1 PRD-v3 / SRD-v3 cloud prompt：`cloud-prompt-U1-prd-v3-srd-v3.md`
- U2 Phase 2 Unlock Playbook cloud prompt：`cloud-prompt-U2-phase-2-unlock-playbook.md`
- U3 Entity v0 Contracts cloud prompt：`cloud-prompt-U3-entity-v0-contracts.md`

每个 cloud prompt 自带：
- §0 Mission
- §1 Required Inputs (GitHub URLs + inline fallback)
- §2 Multi-pass Work Plan (8-10 pass)
- §3 Required Output Structure (ZIP schema with N files)
- §4 Self-Audit Checklist
- §5 Hard Boundaries
- §6 Quality Criteria
- §7 Source References (web 2-month + local cross-reference)
- §8 Format Guard
