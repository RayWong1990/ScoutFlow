---
title: Run-3 + Run-4 Combined Codex CLI Commander Prompt — PF-C1 + PF-C2 (24 dispatch / ABC batch)
status: candidate / commander-prompt / not-authority
created_at: 2026-05-06
target_writer: fresh Codex CLI window (unattended overnight-style, 1 user gate at C1-08)
project_root: /Users/wanglei/workspace/ScoutFlow
github_repo: https://github.com/RayWong1990/ScoutFlow
batch_topology: ABC (dependency-safe, not strict 8/8/8; Batch A fixed / Batch B gate+go-no-go / Batch C downstream C2)
total_dispatches: 24
user_gate_count: 1 (C1-08 human usefulness verdict)
estimated_duration: 60-90 min Codex unattended + 15-20 min user verdict
relates_to:
  - 80-pack-source/02_task_packs/PF-C1-proof-pair-pack/
  - 80-pack-source/02_task_packs/PF-C2-raw-handoff-pack/
  - run-2-amendment-fix-commander-prompt-2026-05-06.md (Run-2 收尾参照)
  - plan/archive/2026-05-05-dispatch127-176-superseded-drafts/dispatch127-176-batch-topology-recommendation-2026-05-05.md (ABC 黄金范式)
---

# Run-3 + Run-4 Combined Commander Prompt — PF-C1 + PF-C2 一发跑完

> 24 dispatch / 3 batch ABC 拓扑 / subagent 在 batch 边界自审 / 仅 1 个 user gate (C1-08)。
> 沿用 dispatch127-176 的 50/2h 节奏：Codex ~2-3 min/dispatch + canary-first + authority rows serial + boundary subagent audit + 0 user 接管 except C1-08。
> Run-3 = PF-C1 proof pair（12 dispatch / 真 URL 价值证明）。Run-4 = PF-C2 RAW handoff（12 dispatch / 不二进 inbox 证明）。
> 本版按真实 manifest / API / worktree 约束修正：优先 obey dependency chain，不再死守机械 `8/8/8`。

---

## 已锁前提（fresh Codex 必读）

- **origin/main HEAD**: `2dbf2c19ae7c93f626929191bc9d0d4e3979958f`（Run-2 amendment 收尾后）
- **3 条 canary URL（user 已选）**:
  - URL-1 ordinary（信息密度普通）: `https://www.bilibili.com/video/BV16ooQBsEah/?spm_id_from=333.337.search-card.all.click`
  - URL-2 edge（边缘案例）: `https://www.bilibili.com/video/BV1zhoUB1Ebg/?spm_id_from=333.337.search-card.all.click&vd_source=4be6ac946264764a925966c890c00b25`
  - URL-3 high-signal（高质量 follow-worthy）: `https://www.bilibili.com/video/BV1A196BpESQ/?spm_id_from=333.337.search-card.all.click&vd_source=4be6ac946264764a925966c890c00b25`
  - canonical: 三条都剥 `?spm_id_from=...` + `?vd_source=...`，留 `https://www.bilibili.com/video/BVxxx/`
- **UAT mode**: synthetic 沿用（curl backend probe + JSDOM，**禁** Playwright/Selenium/真浏览器，user 已授权 partial-evidence 模式）
- **PF-V 并行**: user 在另窗口跑视觉原型，与本主线 git lock 不冲突，C1-02 contract 决策 **不依赖** PF-V 完成（PF-V 视觉作 reference candidate，不强依赖）

## ABC Batch 拓扑

| Batch | Dispatch | 焦点 | Subagent self-audit | User EXIT |
|---|---|---|---|---|
| **Batch0 preflight** | (no slot exec) | live truth readback + authority delta verify + pack repair scan | 无（你 cold-start 就当 preflight） | 无 |
| **Batch A** | `C1-01,02,03,06 -> C1-04 -> C1-05 -> C1-07` | foundation + transformer + markdown companion + 3 URL 真跑 | 1 次（边界） | 无 |
| **Batch B** | `C1-08 EXIT -> C1-09 -> C1-10 -> C1-11(cond) -> C1-12(cond) -> C2-01..05` | ★ C1 usefulness + C2 go/no-go + C2 prep surfaces | 1 次（C1 closeout / C2 open 后） | **1 次（C1-08）** |
| **Batch C** | `C2-06 -> C2-07 -> C2-08/09/10 -> C2-11 -> C2-12` | manual handoff staging + readback + script-seed + SoR matrix + 收尾 | 1 次（最终） | 无 |

总 ~60-90 min Codex unattended + ~15-20 min user verdict at C1-08。

---

## 24 Dispatch 真依赖图

```
Batch A (dependency-safe fixed order)
├─ C1-01 ★ canary solo（URL pack 录入 + 三档分配）
├─ Foundation 并行（3）
│   ├─ C1-02 topic-card-lite v0 contract（5-7 字段）
│   ├─ C1-03 145/146 historical asset extraction（不重启历史）
│   └─ C1-06 human usefulness rubric（4 档分类）
├─ C1-04 transformer candidate（依赖 PF-LP-17 + C1-02）
├─ C1-05 topic-card-lite markdown companion（依赖 C1-04）
└─ C1-07 ★ 3 URL 真跑 → preview md + topic-card-lite（依赖 C1-04；artifact 需匹配 C1-02 contract）
   → subagent self-audit boundary：
       * 验 C1-04 / C1-05 只触 topic-card-preview / topic-card-vault allowed surface
       * 验 C1-07 3 URL artifacts 真存在 + 各 1 个 preview json + 1 个 preview md + 1 个 topic-card-lite
       * 验 API probe payload / vault-preview response shape 与当前 contract 一致

Batch B (single user gate + C2 open decision)
├─ ★★★ C1-08 USER VERDICT EXIT ★★★
│   stdout 输出 "WAITING FOR C1-08 VERDICT"
│   写 evidence skeleton 到 docs/research/post-frozen/evidence/PF-C1-08-human-verdict-2026-05-06.md
│   user 看 3 个 topic-card-lite + preview md，逐条判 follow / park / reject / needs-edit
│   user 填 ≥3 行 verdict + total_useful_count（例 2/3 useful）+ overall (pass / partial / fail)
│   user 同时填 `c2_go_no_go: yes|no`；如允许 C1-12 authority writeback，再填 `allow_authority_writeback: yes|no`
│   user 重 paste 同段 prompt → Codex 检测 evidence file verdict 字段非占位 → 续跑
│
├─ C1-09 false-positive + edit-cost log（依赖 C1-08）
├─ C1-10 C1 proof readback（依赖 C1-08 + C1-09，记录 pass/partial/fail + 是否 C2 可开）
├─ C1-11 conditional 2nd canary（仅当 C1-10 = partial 才跑，pass 直接跳）
├─ C1-12 C1 closeout + C2 go/no-go（依赖 C1-10；是否写 authority 取决于同一份 C1-08 evidence 的 `allow_authority_writeback`）
├─ C2-01 RAW note candidate contract v0（仅当 `c2_go_no_go=yes`）
├─ C2-02 RAW frontmatter compatibility check（C2-01 后）
├─ C2-03 manual handoff runbook（仅当 `c2_go_no_go=yes`）
├─ C2-04 RAW intake acceptance rubric（仅当 `c2_go_no_go=yes`）
└─ C2-05 script seed proof contract（仅当 `c2_go_no_go=yes`）
   → subagent self-audit boundary：
       * 验 C1-10/12 verdict 与 C1-08 user 真原话对齐
       * 验若 `allow_authority_writeback!=yes`，则 C1-12 不得偷写 authority surface
       * 验 C2-01..05 全 candidate / not-authority
       * 验 C2 cluster 只在 `c2_go_no_go=yes` 后开启，符合 `reservoir_after_c1_go_no_go`

Batch C (downstream C2 only)
├─ C2-06 ★ 2-note manual RAW handoff RUN（依赖 C1-07 + C2-01 + C2-03 + C1-10）
│   → 把 C1-07 中 ≥2 条 useful preview markdown 复制到 docs/research/post-frozen/raw-handoff-staging/
│   → 写 manual transfer note 给 user（"请把 staging 下的 .md 拷到 ~/workspace/raw/00-Inbox/"）
│   → dispatch verdict = partial（user 实拷之前不能 pass，符合 §"partial pass" gate）
├─ C2-07 RAW intake/readback result（依赖 C2-06 + C2-04；若 user 当下没拷，标 pending / partial）
├─ C2-08 script seed generation result（依赖 C2-07 + C2-05）
├─ C2-09 second-inbox negative test（依赖 C2-07；若无 intake evidence，本轮标 expected_partial，不得伪装 pass）
├─ C2-10 ScoutFlow/RAW SoR handoff matrix（依赖 C2-07）
├─ C2-11 C2 proof readback（依赖 C2-08 + C2-09）
└─ C2-12 true-write future gate draft（overflow only，不进 mainline）
   → final subagent self-audit + 收尾：
       * 验 C2-12 标 overflow / future_gate / not_in_mainline
       * 验全 24 dispatch 没有任何 true vault write / browser automation / migration 痕迹
       * 验 RAW handoff staging 全在 docs/research/post-frozen/ 内（**不写** ~/workspace/raw/）
       * 验 `C2-07/08/09/10/11` 没把 pending user transfer 写成 pass
       * 写 RUN-3-4-CODEX0-REPORT + DIFF-BUNDLE + CHECKPOINT 三件
```

---

```
<<<COMMANDER PROMPT BEGIN>>>

你是 ScoutFlow Codex0 fresh 单写者，执行 Run-3 + Run-4 合并跑：PF-C1 12 dispatch + PF-C2 12 dispatch = 24 dispatch，ABC batch 拓扑，subagent 在 batch 边界自审，仅 1 个 user EXIT (C1-08 verdict)。

## 项目身份
- repo: /Users/wanglei/workspace/ScoutFlow
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- origin/main HEAD: `2dbf2c19ae7c93f626929191bc9d0d4e3979958f`
- 你是 Codex0 唯一 main writer + checkpoint truth owner
- subagent 只读 + 提 findings，不写 authority

## 3 条 canary URL（user 已选，三档已绑）
- ordinary: `https://www.bilibili.com/video/BV16ooQBsEah/?spm_id_from=333.337.search-card.all.click`
- edge: `https://www.bilibili.com/video/BV1zhoUB1Ebg/?spm_id_from=333.337.search-card.all.click&vd_source=4be6ac946264764a925966c890c00b25`
- high-signal: `https://www.bilibili.com/video/BV1A196BpESQ/?spm_id_from=333.337.search-card.all.click&vd_source=4be6ac946264764a925966c890c00b25`

C1-01 dispatch 直接录入这 3 条，不用再问 user。canonical 形态自动剥 query string。

## UAT 模式
- synthetic 沿用 Run-2: `curl` backend probe（uvicorn :8000）+ `pnpm test --` JSDOM 单测
- **禁**: Playwright / Selenium / Puppeteer / 真浏览器 / 自动化 click
- evidence 标 frontmatter `synthetic_partial` + `verdict: partial / synthetic_result: works/partial/broken`，**不允许** verdict = `works` 单写（Run-2 amendment 教训）

## ABC Batch + 真依赖图

详见上方 `## 24 Dispatch 真依赖图` 段。Codex 严格按 batch 顺序跑；**真实依赖优先于表面均分**：

- Batch A 跑完 → 做 1 次 boundary subagent self-audit → 自决 fix 任何 finding（不 EXIT）→ 进 Batch B
- Batch B 第一 dispatch = C1-08，**EXIT 等 user verdict**
  - C1-08 evidence skeleton 由 Codex 写到 `docs/research/post-frozen/evidence/PF-C1-08-human-verdict-2026-05-06.md`
  - skeleton 含 3 个 verdict 槽（per URL: follow / park / reject / needs-edit）+ total_useful_count 字段 + overall 字段（pass/partial/fail）+ `c2_go_no_go` + `allow_authority_writeback`
  - stdout 输出 `WAITING FOR C1-08 USER VERDICT`，列 evidence file 路径 + 3 条 URL 对应 topic-card-lite artifacts 路径，让 user 速判
  - user 重 paste 同段 prompt → Codex 检测 evidence file `overall_verdict` / `c2_go_no_go` 已非占位 → 续跑后续 dispatch
- Batch B 跑完 → boundary subagent self-audit → 进 Batch C
- Batch C 跑完 → final subagent self-audit + 写 RUN-3-4 receipt 三件 → exit

## Subagent self-audit 在 batch 边界跑什么（统一规则）

每次 boundary 开 1 个 read-only subagent，喂以下检查清单：

```
[A] Authority untouched check:
    默认 grep diff $BASE_REF..HEAD 是否触及 docs/current.md / docs/task-index.md / docs/decision-log.md / AGENTS.md
    仅当 C1-08 evidence 明示 `allow_authority_writeback=yes` 时，允许 C1-12 触及 docs/current.md / docs/task-index.md / docs/decision-log.md / docs/specs/contracts-index.md
[B] 硬红线 check:
    grep BBDown / yt-dlp / ffmpeg / audio_transcript / subprocess.run / playwright / selenium / puppeteer / alembic 新 migration
[C] write_enabled invariant:
    services/api/scoutflow_api/bridge/config.py 仍含 write_enabled=False 两处
[D] candidate-only frontmatter:
    本 batch 写的所有 .md frontmatter 全部 status 含 `candidate / not-authority` 或 `evidence` 类
[E] 真 RAW 路径未污染:
    git diff 不含 ~/workspace/raw/ 下任何写操作；handoff staging 全在 docs/research/post-frozen/raw-handoff-staging/
[F] dispatch §8 acceptance:
    本 batch 跑过的每 dispatch 都满足其 §8 pass_bar (assertion 数 ≥3 per dispatch §8 line, per W-LP01-Δ rule)
```

任一 finding → Codex 主写自决 fix，**不要 EXIT**。fix 后再跑一遍同段 audit，clear 才进下一 batch。
（"松一点"原则：subagent finding ≠ user 接管。Codex 自决修。）

## Cold-start 必跑（90 秒）
1. `git fetch origin --prune`；记录 `BASE_REF=$(git rev-parse origin/main)`；若与 prompt 中 `2dbf2c19ae7c93f626929191bc9d0d4e3979958f` 不同，先把差异写进 truth-conflict note，再决定是否继续
2. 读 3 条 dispatch 源文件 抽样 §4 + §8（验你能解析 manifest）：
   - `docs/research/post-frozen/80-pack-source/02_task_packs/PF-C1-proof-pair-pack/dispatches/PF-C1-01-canary-url-pack-selection.md`
   - `docs/research/post-frozen/80-pack-source/02_task_packs/PF-C1-proof-pair-pack/dispatches/PF-C1-07-run-3-real-url-preview-proofs.md`
   - `docs/research/post-frozen/80-pack-source/02_task_packs/PF-C2-raw-handoff-pack/dispatches/PF-C2-06-two-note-manual-raw-handoff-run.md`
3. 验 Run-2 amendment 已 land：grep `RUN-2-AMENDMENT-LEDGER-2026-05-06.md` 在 `docs/research/post-frozen/runs/`
4. `export SCOUTFLOW_VAULT_ROOT=/tmp/scoutflow-vault`（未设此 env 时 `/captures/{capture_id}/vault-preview` 会 409）
5. 起 backend 备用：`cd services/api && uvicorn scoutflow_api.main:create_app --factory --port 8000 &`（C1-07 跑 3 URL 时 curl probe 用）
6. 起一个 worktree 给 Codex 主写：`git worktree add -b codex/run3-4-combined /tmp/scoutflow-run3-4-<rand> origin/main`
7. `cd /tmp/scoutflow-run3-4-<rand>`；后续所有改动 / git 操作都在该 worktree 内完成，原 repo 仅作 truth reference

## 不停歇协议
- 24 dispatch 全部 unattended，per-dispatch one PR + auto-merge on `mergeStateStatus=CLEAN` + 5 checks 全绿
- 唯一 EXIT：C1-08 user verdict（其他全自决 fix）
- subagent boundary audit 找问题 → Codex 自修，不停
- mid-batch 失败 → slot-local retry 自决；control-plane interruption 自接住；ledger interruption 用 GitHub live truth 补
- 真接不住才 EXIT 报 user

## C1-07 Real URL 真跑细节（最关键 backend touch）

C1-07 dispatch 把 3 URL 走 backend。注意两点：
- `POST /captures/discover` 需要完整 payload：`platform + canonical_url + source_kind + quick_capture_preset`
- `GET /captures/{capture_id}/vault-preview` 返回的是 JSON，不是裸 markdown；必须显式抽 `body_markdown`

```bash
# backend 已在 cold-start 起好；先准备 artifact root
ARTIFACT_ROOT="docs/research/post-frozen/proof-artifacts/run-3-c1-07"
mkdir -p "$ARTIFACT_ROOT"

run_one() {
  local LABEL="$1"
  local URL="$2"
  local CAPTURE_JSON="$ARTIFACT_ROOT/URL-${LABEL}-capture.json"

  curl -s -X POST http://127.0.0.1:8000/captures/discover \
    -H 'Content-Type: application/json' \
    -d "{\"platform\":\"bilibili\",\"canonical_url\":\"$URL\",\"source_kind\":\"manual_url\",\"quick_capture_preset\":\"metadata_only\"}" \
    > "$CAPTURE_JSON"

  local CAPTURE_ID
  CAPTURE_ID=$(jq -r '.capture_id' "$CAPTURE_JSON")

  local PREVIEW_JSON="$ARTIFACT_ROOT/URL-${LABEL}-preview-${CAPTURE_ID}.json"
  local PREVIEW_MD="$ARTIFACT_ROOT/URL-${LABEL}-preview-${CAPTURE_ID}.md"
  local CARD_JSON="$ARTIFACT_ROOT/URL-${LABEL}-card-${CAPTURE_ID}.json"

  curl -s "http://127.0.0.1:8000/captures/$CAPTURE_ID/vault-preview" > "$PREVIEW_JSON"
  jq -r '.body_markdown' "$PREVIEW_JSON" > "$PREVIEW_MD"

  node - "$CAPTURE_JSON" "$PREVIEW_JSON" "$CARD_JSON" <<'EOF'
const fs = require("fs");
const [capturePath, previewPath, outPath] = process.argv.slice(2);
const capture = JSON.parse(fs.readFileSync(capturePath, "utf8"));
const preview = JSON.parse(fs.readFileSync(previewPath, "utf8"));
const card = {
  capture_id: capture.capture_id,
  title: preview.frontmatter?.title || capture.platform_item_id,
  canonical_url: capture.canonical_url,
  platform_item_id: capture.platform_item_id,
  export_posture: "handoff_candidate",
  target_path: preview.target_path,
  status: preview.frontmatter?.status || "pending"
};
fs.writeFileSync(outPath, JSON.stringify(card, null, 2));
EOF
}

run_one ordinary "https://www.bilibili.com/video/BV16ooQBsEah/"
run_one edge "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
run_one high-signal "https://www.bilibili.com/video/BV1A196BpESQ/"
```

各 URL 产出 `capture json + preview json + preview md + topic-card-lite`，写到 `docs/research/post-frozen/proof-artifacts/run-3-c1-07/`：
- `URL-{ordinary|edge|high-signal}-capture.json`
- `URL-{ordinary|edge|high-signal}-preview-{capture_id}.json`
- `URL-{ordinary|edge|high-signal}-preview-{capture_id}.md`
- `URL-{ordinary|edge|high-signal}-card-{capture_id}.json`

C1-04 transformer 不要再指向不存在的 `tools/preview-to-topic-card-lite.py`。优先方案：
- 在 `apps/capture-station/src/features/topic-card-preview/**` 内落可测试的最小 transform seam
- C1-07 artifact 可以先用上面的 inline `node` 提取 5-7 字段 candidate，但最终字段集必须回对 C1-02 contract，且不得偷偷膨胀成 full workbench / scoring schema

跑完关 backend：`pkill -f 'uvicorn scoutflow_api'`。

## C1-08 user verdict skeleton 模板

```yaml
---
title: PF-C1-08 Human Usefulness Verdict
status: candidate / human_verdict / pending_user_fill
date: 2026-05-06
overall_verdict: TODO_pass_or_partial_or_fail
total_useful_count: TODO_X_of_3
c2_go_no_go: TODO_yes_or_no
allow_authority_writeback: TODO_yes_or_no
---

## URL-1 ordinary
- url: https://www.bilibili.com/video/BV16ooQBsEah/
- preview_md: docs/research/post-frozen/proof-artifacts/run-3-c1-07/URL-ordinary-preview-{capture_id}.md
- topic_card_lite: docs/research/post-frozen/proof-artifacts/run-3-c1-07/URL-ordinary-card-{capture_id}.json
- verdict: TODO_follow_or_park_or_reject_or_needs-edit
- one_liner: TODO_one_sentence_why

## URL-2 edge
（同结构）

## URL-3 high-signal
（同结构）

## Overall
- ≥2/3 useful (follow|needs-edit) = pass
- 1/3 useful = partial
- 0/3 useful = fail
- decision: TODO
```

user 至少填完 6 个核心 TODO：3 个 verdict + `overall_verdict` + `c2_go_no_go` + `allow_authority_writeback`。Codex 检测这些关键字段非占位 → 续跑。

## RAW handoff staging（C2-06 关键）

C2-06 把 C1-07 中标 `useful` (follow|needs-edit) 的 ≥2 条 preview md 复制到：

```
docs/research/post-frozen/raw-handoff-staging/
├── README-manual-transfer.md  （指引 user 怎么拷到 ~/workspace/raw/00-Inbox/）
├── note-1-{capture_id}.md     （preview + topic-card-lite-frontmatter 合体）
└── note-2-{capture_id}.md
```

**禁** Codex 主动写 `~/workspace/raw/`。staging 全在 repo 内 docs/research/post-frozen/。

C2-07 RAW intake/readback verdict = `pending_user_manual_transfer`（partial）。在 user 未实际拷入 `~/workspace/raw/00-Inbox/` 前：
- C2-07 不得写成 accepted / pass
- C2-08 只能从 staging note 抽 candidate script seed，不得伪称 “RAW accepted”
- C2-09 需显式标 `expected_partial`
- C2-10 / C2-11 必须引用上述 partial 现实，不得伪造 dual-SoR clean pass

## 边界硬规则（违反任一即停）
- Dispatch126-176 frozen，evidence-only 引用，不 reopen
- 默认不写 docs/current.md / docs/task-index.md / docs/decision-log.md / AGENTS.md
- 仅当 C1-08 evidence 同时给出 `c2_go_no_go=yes` + `allow_authority_writeback=yes` 时，C1-12 才可按 dispatch allowed paths 触及 authority surface；否则 C1-12 必须记为 partial/skip
- 不解禁 true vault write / BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migrations
- bridge/config.py:24,36 keep write_enabled=False
- 不写 ~/workspace/raw/（RAW handoff staging 全在 docs/research/post-frozen/raw-handoff-staging/）
- 措辞 T-PASS / V-PASS / partial / FAIL_ENV / REJECT_AS_X / clear / concern / reject — 禁裸 PASS / DONE / OK / works
- C1-07 真 backend probe 限 3 URL，不扩
- C2-12 true-write future gate **draft only into overflow**，绝不进 mainline
- 不开 PR 编号竞态（每 dispatch 一 PR，auto-merge on CLEAN）

## 末尾产出（外审用）
完成 24 dispatch + 3 batch 边界 audit 全 clear → 写：
1. `docs/research/post-frozen/runs/RUN-3-4-CODEX0-REPORT-2026-05-06.md`（24 stage receipt + 3 boundary audit verdict + C1-08 user verdict cite + 三类中断各几次）
2. `docs/research/post-frozen/runs/DIFF-BUNDLE-Run3-4-2026-05-06.md`（24 PR 跨 PR 一致性 diff，给三方外审）
3. `docs/research/post-frozen/runs/CHECKPOINT-Run3-4-final.json`（含 c1_verdict / c2_partial_count / can_open_c4 / final origin/main SHA）

stdout 末尾输出：
```
COMMANDER RUN-3+4 COMBINED COMPLETE
final_origin_main: <sha>
prs_merged: [23-24 PR numbers, depending on whether C1-12 authority writeback is authorized]
batch_a_audit: clear / concern / reject
batch_b_audit: clear / concern / reject
batch_c_audit: clear / concern / reject
c1_verdict: pass / partial / fail
c1_useful_count: X/3
c2_partial_count: X (期望 RAW handoff partial pending user)
c1_iteration_2_run: yes / no (仅 C1 partial 才 yes)
high_blast_audit_verdict: [PF-C1-04: clean | PF-C1-07: clean | PF-C2-06: clean]
interruption_count: {slot_local: N, control_plane: N, ledger: N}
diff_bundle_path: <path>
report_path: <path>
ready_for_external_audit: yes
ready_for_run_5: yes_pending_pf_v_handoff / yes_pending_user_raw_intake / no
```

## 派单顺序提示（最高马力）
- Batch A: C1-01 solo → C1-02/03/06 并行 → C1-04 → C1-05 → C1-07
- Batch B: C1-08 EXIT 等 user → user 回 → C1-09 → C1-10 → C1-11(仅 partial)；若 `c2_go_no_go=yes` 再开 C2-01/02/03/04/05；若 `allow_authority_writeback=yes` 再跑 C1-12 authority writeback
- Batch C: C2-06 → C2-07 → C2-08/09/10 并行 → C2-11 → C2-12
- 开足马力，但每 batch 边界做 1 次 self-audit

开始动笔。

<<<COMMANDER PROMPT END>>>
```

---

## 使用说明

### 启动
```bash
# fresh Codex CLI 窗口（cd 到 ScoutFlow 项目根）
cat /Users/wanglei/workspace/ScoutFlow/docs/research/post-frozen/run-3-4-combined-codex-commander-prompt-2026-05-06.md

# 复制 <<<COMMANDER PROMPT BEGIN>>>...<<<COMMANDER PROMPT END>>> 之间内容粘进去
# 跑 unattended，Batch A 完成后会在 C1-08 EXIT 等 user verdict
```

### C1-08 user verdict 步骤（~15-20 min）

1. Codex 跑到 C1-08 EXIT，stdout 提示 `WAITING FOR C1-08 USER VERDICT`
2. 打开 evidence file: `docs/research/post-frozen/evidence/PF-C1-08-human-verdict-2026-05-06.md`
3. 打开 3 条 URL 对应的 topic-card-lite 文件（路径在 stdout 列出）+ preview md
4. 逐条判 follow / park / reject / needs-edit
5. 算 total_useful_count（follow + needs-edit 都算 useful；park / reject 不算）
6. 填 overall: ≥2/3 useful = pass / 1/3 = partial / 0/3 = fail
7. 同一份 evidence 一并填 `c2_go_no_go`，如你愿意放开 authority writer slot 再填 `allow_authority_writeback=yes`
8. 重 paste 同段 commander prompt → Codex 检测 evidence 已填 → 续跑 Batch B 剩余 + Batch C

### 全程时间
- Codex unattended Batch A: ~25-35 min
- User C1-08 verdict: ~15-20 min
- Codex unattended Batch B 剩 + Batch C: ~30-40 min
- 收尾 receipt: ~3 min
- **总 ~75-100 min**

---

## 与 PF-V 并行不冲突保证

| Lane | 写面 | git lock |
|---|---|---|
| Run-3+4 主线 | `apps/capture-station/src/features/topic-card-preview/**` + `apps/capture-station/src/features/topic-card-vault/**` + `tests/**` + `docs/research/post-frozen/proof-artifacts/` + `raw-handoff-staging/` + `runs/` + `evidence/` | 主 worktree codex/run3-4-combined |
| PF-V 视觉 | `docs/research/visual-prototypes/PF-V/**` only | 独立 worktree |

PR 编号自动递增，无冲突。C1-02 contract 决策在 PF-V 视觉到位前可独立做（PF-V 视觉 candidate 后续可 amend cite）。

---

## 完成后下一步

24 dispatch 全 clear + C1 verdict pass → 收齐外审 ready 状态。下一步分支：

| C1 verdict | C2 状态 | 下一步 |
|---|---|---|
| pass | partial pending user RAW intake | user 拷 staging 到 ~/workspace/raw/ → C2 升 pass → 启 Run-5 (PF-C4) |
| partial | partial | C1-11 第 2 轮 canary 已自动跑（最多 2 新 URL）；如仍 partial → user 决定开 C4 或先补证据 |
| fail | 不开 | revert / 复盘 / amend C1-04 transformer 后再跑 |

Run-5 = PF-C4 (8 dispatch, 含 PF-C4-01 frontend bootstrap 接 PF-V handoff = HTML5 → React TSX) — 等本次 + PF-V 都到位后再启。
