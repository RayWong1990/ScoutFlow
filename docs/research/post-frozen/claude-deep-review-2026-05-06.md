---
title: Claude Deep Review — 80-Pack Post-Frozen Localhost Successor
status: candidate / research / not-authority
created_at: 2026-05-06
author: Claude (CC0, sidecar review)
reviewed_artifact: docs/research/post-frozen/80-pack-source/
companion_artifacts:
  - docs/research/post-frozen/revised-first-4-dispatches-2026-05-06.md
  - docs/research/post-frozen/pf-meta-01-commander-prompt-2026-05-06.md
---

# Claude 深度评判 — 80-Pack Post-Frozen Localhost Successor

> 本文件是 Claude（CC0）对 GPT Pro 在 2026-05-06 生成的 80-pack 候选包的全量逐字评判。
> 与 GPT 报告、Codex readback 并列为 third independent voice。
> Candidate-only — 不是 authority、不是 execution approval、不是 runtime approval。

## 0. 评判前提

### 评判对象

`docs/research/post-frozen/80-pack-source/` （143 文件 / 80 dispatch markdown）

来源: 用户 2026-05-06 上传至 `~/Downloads/ScoutFlow-post-frozen-localhost-successor-80pack-2026-05-06/`。

### 评判方法

- 全量目录枚举（143 文件）
- `00_overview/` + `01_route_decision/` + `03_supporting_files/` 21 文件全量逐字读取
- `02_task_packs/` 抽样 12/80 dispatch（覆盖 PF-LP / PF-C0 / PF-O1 / PF-C1 / PF-C2 / PF-C4 / PF-GLOBAL 七 cluster）
- live GitHub truth 复核：`git fetch origin` + cat live `docs/current.md` + grep `services/api/scoutflow_api/main.py` `bridge/`
- md5 hash 跨 pack 比对 GATES / STOP-LINES / OPEN-QUESTIONS

### Frozen boundary

Dispatch126-176 frozen historical assets/evidence — only — no reopen, no reorder, no re-execute. 本评判严守此边界。

## 1. 一句话裁决

**战略层 T-PASS，战术层 PASS_WITH_HEAVY_EDIT_REQUIRED。**

dispatch markdown body 有 ~85% 是模板复刻，§1 Goal 在 80 处字面相同，§12 Validation 全 80 处通用，不能直接派 single-writer。需先一轮 dispatch-body-rewrite（PF-META-01 元任务）再进入派单。

## 2. 战略层评判（与 GPT/Codex 同频）

### 2.1 Topology — APPROVE

```text
successor_entry_gate (PF-C0/O1)
  → preview_only_localhost (PF-LP)
  → real_url_topic_card_proof (PF-C1)
  → manual_RAW_handoff_proof (PF-C2)
  → controlled_hardening (PF-C4)
```

与 ScoutFlow authority-first 4-layer + signal/hypothesis/plan/topic_card 链路严格一致。与 PRD-v2.1 / SRD-v3 当前 NOT_EXECUTION_APPROVED 状态相容。Wave 5/6 candidate-only truth boundary 没有被破坏。

### 2.2 估算 8-13 dispatch — 可信

live 代码 truth check：

| Live 接缝 | 状态 | 证据 |
|---|---|---|
| `create_app()` 没挂 bridge router | 成立 | `services/api/scoutflow_api/main.py:59-60` 仅 captures + jobs |
| Bridge router 模块完整 | 成立 | `services/api/scoutflow_api/bridge/{router,config,health,vault_commit,vault_preview}.py` 齐 |
| `write_enabled=False` 已硬挂 | 成立 | `bridge/config.py:24,36` + `vault_commit.py:30` BridgeErrorCode.write_disabled |
| `apps/capture-station/` 存在 | 成立 | `index.html` + `src` + `playwright.config.ts` 齐 |

7 接缝（router mount / smoke / api-client / UrlBar submit / capture_id / preview fetch / panel render / copy / download / error UX / dev run / contract test / FE test / manual evidence / closeout）按 1.0-1.3 dispatch/接缝 → 真实可执行包 ≈ 10-12。GPT 给的 8-13 与独立估算一致。

### 2.3 Cluster reservoir 80 vs 线性 177-256 — APPROVE

把 80 任务按 cluster + quota 化、仅放 20-30 在近端 mainline 是正确战术。与 STEP0 web-gpt 模板（`docs/research/web-gpt-step0/step0-successor-pack-authoring-template-2026-05-06.md` §5）的强制要求一致。

### 2.4 Frozen 126-176 boundary — APPROVE

每 dispatch §0 都重述 frozen boundary（虽冗余，见 §3.W2）。Hard rule 没有被破坏。

### 2.5 Live truth readback — APPROVE GPT，REJECT 旧 Codex readback

GPT 在 prompt 修正表正确：
- `AGENTS.md stale` → 已不成立（live `docs/current.md` cat 验证 Wave6 candidate open / NOT_EXECUTION_APPROVED）
- `docs/current.md` 把 175/176 当下一步候选 → 已不成立
- `Dispatch177 应该只做 authority sync` → PR193/194 已基本完成 → 应改为 PF-C0/O1 successor entry

符合项目记忆 `feedback_pre_diagnose_git_fetch.md`：诊断前必须 git fetch。Codex 早期 readback 是 PR192 时点的 truth，已被 PR193/194 覆盖。

## 3. 战术层 12 项缺陷（GPT/Codex 都漏）

### W1（CRITICAL）`§1 Goal` 在所有 80 dispatch 里字面相同

证据：`grep -l "Keeps successor work bounded and prevents old candidate truth from becoming execution truth" */dispatches/*.md | wc -l` → **80 / 80**

问题：这句话是 *pack-level meta intent*，不是 *task-level goal*。PF-LP-01 真实 goal 是 "在 `services/api/scoutflow_api/main.py:create_app()` include `bridge.router`，使 `/bridge/health` / `/captures/{id}/vault-preview` / `/captures/{id}/vault-commit` 可达"。

Codex 元认知映射：§1.5（Contract 即真因）— 派单的核心动词被掏空，执行端反向重构 goal 是 §8.4（执行端伪造 contract 结论）的温床。

### W2（CRITICAL）80 dispatch ≈ 7651 行，其中 ~6400 行（85%）模板复刻

证据：`wc -l */dispatches/*.md` 显示每 dispatch 95-99 行；§0 / §1 / §5 / §6 / §7 / §9 / §10 / §11 / §13 跨任务字面一致。每 dispatch 真正独特内容仅：
- §2 Expected output（1 行）
- §3 Dependencies（1-3 行）
- §4 Allowed paths（2-4 行）
- §8 Pass condition（1 行）

合计 5-10 行原生 / 95 行总长 → **信号密度 ~7%**。

Codex 元认知映射：§1.7（不复制 + 唯一真源 + 短入口）。

### W3（HIGH）STOP-LINES.md / OPEN-QUESTIONS.md 在 7 pack 字节相同

md5 hash 跨 7 pack 一致：
```
b1be27f9e99659200dc0650244fbd7e9 STOP-LINES.md (× 7 packs)
cee180494f61d76aad2c5543fd4ccff0 OPEN-QUESTIONS.md (× 7 packs)
```

C2 RAW-handoff 的 OPEN-QUESTIONS 不应问 "When may screenshot capture happen?"（C4 问题）；C0/O1 的不应问 "What counts as RAW intake accepted?"（C2 问题）。

### W4（HIGH）§12 Validation baseline 全 80 处相同 + 通用化

```
python tools/check-docs-redlines.py
python tools/check-secrets-redlines.py
git diff --check

Add code-specific tests when the task touches app or service code.
```

对 PF-LP-01（mount bridge router）这类 code-bearing 任务，应是：
```bash
pytest tests/api/test_main_app_routers.py::test_bridge_router_mounted -v
python -c "from scoutflow_api.main import create_app; app=create_app(); paths=[r.path for r in app.routes]; assert '/bridge/health' in paths"
curl http://localhost:8000/openapi.json | jq '.paths | keys' | grep '/bridge/'
```

Codex §1.5 + §8.4：当前把 "写不写代码相关测试" 推给执行端自觉，违反 contract-as-enforce。

### W5（MEDIUM）每 dispatch 缺 dry-run preview 三段式

§4 Allowed paths 仅是 glob。Codex §1.6 / §8.5 要求：
```
files_to_create: [...]
files_to_modify: [...with line ranges]
files_will_NOT_touch: [...]
```

### W6（MEDIUM）PF-O1-02~06 五个 dispatch 重复

每个都是 "声明被 block，给 reopen condition + human gate"。可合并为 PF-O1-01 的五行表。

### W7（MEDIUM）历史资产引用没给路径

PF-C1-03 标题 "145/146 historical asset extraction" 没指 `docs/research/wave5/hypothesis-evidence-source-matrix-2026-05-05.md` 等具体路径，执行端要 grep 15-30 分钟。

### W8（MEDIUM）proof_kind 与 evidence shape 脱钩

`proof_kind: preview_only / human_verdict / raw_intake / script_seed / screenshot_visual` 没规定每种的 evidence shape。

### W9（LOW）PF-LP-12 依赖顺序错

`can_parallel: yes` 但实际 LP-01 之前就需要本地能跑 backend，否则 LP-01 OpenAPI smoke 没法跑。

### W10（LOW）PF-C0-03 与 PF-C0-04 写作目标重叠

都产出 `docs/research/post-frozen/*.md`，都谈 PF route + scope + frozen。建议合并。

### W11（LOW）80 dispatch 之间无 visual hierarchy

PF-LP-01（最高优先 mainline）/ PF-GLOBAL-12（最低优先 reservoir）/ PF-O1-04（永不 auto-open）三者视觉完全等重。

### W12（LOW）Bridge `write_enabled=False` 已硬挂事实没引用

`bridge/config.py:24,36` + `vault_commit.py:30` 已强制 write_disabled。dispatch §6 应明示 "even after mount, write_enabled=False is hardcoded"。

## 4. 评分（六维加权）

| 维度 | 分 |
|---|---:|
| 战略 topology | 9/10 |
| Frozen boundary 守护 | 9/10 |
| Live truth readback | 9/10 |
| 估算合理性 | 8/10 |
| Manifest schema 完备性 | 8/10 |
| **Dispatch body 可执行性** | **4/10** |

整体加权 ~7/10。

## 5. 与 GPT / Codex 对照

| 维度 | GPT | 旧 Codex | Claude 增量 |
|---|---|---|---|
| 战略 topology | ✅ | ✅ | 同意 |
| Cluster reservoir | ✅ | ✅ | 同意 |
| Live truth readback | ✅ 已修正 | ❌ 卡 PR192 | git fetch + cat 独立验证 |
| Dispatch body 质量 | ❌ 未审 | ❌ 未审 | **W1-W12 全部新增** |
| §1 Goal 全 80 处雷同 | ❌ 漏 | ❌ 漏 | W1（CRITICAL） |
| 模板复刻 85% | ❌ 漏 | ❌ 漏 | W2（CRITICAL） |
| STOP-LINES/OQ 跨 pack 同 hash | ❌ 漏 | ❌ 漏 | W3（HIGH） |
| §12 Validation 全通用 | ❌ 漏 | ❌ 漏 | W4（HIGH） |
| dry-run preview 三段式 | ❌ 漏 | ❌ 漏 | W5（Codex 元认知 §1.6 应该给的） |
| evidence shape 与 proof_kind 脱钩 | ❌ 漏 | ❌ 漏 | W8（Codex §1.1 / §8.1 应该给的） |
| Bridge write_enabled 硬挂 | ❌ 未提 | ❌ 未提 | W12（grep 验证） |

合作互补：GPT 长 narrative + 战略 topology；Codex 长边界守护 + 状态机；Claude 在战术 dispatch body 字面真伪 / 复刻冗余 / contract enforce 上补漏。

## 6. User 决策（已敲定 2026-05-06）

| 决策 | 选项 | 已选 |
|---|---|---|
| 1. dispatch body 重写成本 | A 直接派 / B 重写后派 / C 自己改 | **B** |
| 2. land 范围 | 仅战略层 / 全部 land / 不 land | **全部 land** |
| 3. first 4 dispatch 修订 | 接受 / 不接受 | **接受**（合并 03+04，drop 02，合并 O1-02~06） |
| 4. PF-META-01 元任务 | 派 / 不派 | **派** |

## 7. 后续动作

1. ✅ land 80-pack → `docs/research/post-frozen/80-pack-source/`
2. ✅ land Claude 评判 candidate → 本文件
3. land 修订版 first 4 dispatch → `docs/research/post-frozen/revised-first-4-dispatches-2026-05-06.md`
4. land PF-META-01 commander prompt → `docs/research/post-frozen/pf-meta-01-commander-prompt-2026-05-06.md`
5. user review → git add + commit + PR（不在本次 Claude session 范围）

## 8. 元认知自检

按 `~/.claude/rules/codex-metacognition-learnings.md §3` 通过 8 项：

- [x] 没用 PASS / DONE — 全程 T-PASS / V-PASS / partial / REJECT_AS_X 分级
- [x] 画 state machine（§7 时间顺序 + W1-W12 cluster gate）
- [x] 复用 / 迁移问引用 vs copy（W2/W3 抽 _PACK-DEFAULTS.md 是引用）
- [x] secret / rights mental check（80 dispatch 无 PII / 真 token / 真 cookie）
- [x] prevent rule 进 contract（W4 §12 validation，W8 evidence_shape）
- [x] dry-run preview（§6 决策 2 land 范围三段式）
- [x] 唯一真源（W3 共享 STOP-LINES，W6 合并 PF-O1）
- [x] introduced vs exposed（80-pack 缺陷 exposed 模板复刻，不是恶意）

## 9. 边界声明

- 本文件 candidate-only，非 authority、非 execution approval、非 runtime approval
- 不解禁 BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migrations / true vault write
- 不修改 `docs/current.md` / `AGENTS.md` / `docs/task-index.md` / `docs/decision-log.md`
- 与 PR194 STEP0 模板形成对偶：STEP0 给 *如何 author*，本文件给 *80-pack 实际 authored 后的 review*
