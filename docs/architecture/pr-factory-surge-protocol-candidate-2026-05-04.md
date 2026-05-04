---
type: protocol-candidate
version: 1.0
title: ScoutFlow PR Factory Surge Protocol Candidate
date: 2026-05-04
authority_status: research-only / protocol-candidate / not-authority / not-runtime-approval
suggested_commit_path: docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md
source_trace:
  - docs/research/pr55-pr74-worklist-candidate-2026-05-04.md §5
  - docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md §2.1
  - docs/research/doc1-doc2-doc3-v1.1-acceptance-errata-report-2026-05-04.md
dispatch_mapping:
  original_backbone_slot: PR59 / T-P1A-034
  current_dispatch_slot: PR60 / T-P1A-035
verdict: "本文档只定义 PR Factory surge 的候选协议，不改当前生效基线；在 PR60 candidate 被显式 promoted 且 PR67 closeout 明确批准前，ScoutFlow 继续执行 product_lane_max=3 与 authority_writer_max=1。"
---

# ScoutFlow PR Factory Surge Protocol Candidate

> 定位：Wave 3A 的 protocol candidate。它服务于 dispatch 设计、并行排程和 closeout 审核，不直接修改 `AGENTS.md` 或 `docs/specs/parallel-execution-protocol.md` 的当前生效口径。
>
> 生效边界：在 `PR60` candidate 被显式 promoted 且 `PR67` closeout 明确批准之前，本文所有 surge 条款都只能视为候选，不得作为代码、CI、runtime、contract enforcement 或分支化逻辑的依据。

## §1 Scope And Status

### 1.1 本文档解决什么

Wave 3A 已经形成一个现实问题：研究类、prototype 类、audit 类任务可以安全并行，但当前生效协议只把 `product_lane_max=3` 和 `authority_writer_max=1` 写成硬基线，没有把“高峰期 PR Factory 如何扩容但不误伤 authority”说成一个独立候选协议。

本文只补这一层：

- 给当前基线命名为 `Enforced baseline`
- 给调度视图里的非 authority 并行池命名为 `Tracked advisory pools`
- 给未来可能升级的 product surge 命名为 `Surge candidate`
- 明确 surge 触发门、文件域互斥协议、PR Factory 7-step workflow、rollback target

### 1.2 本文档不做什么

- 不修改 `AGENTS.md`
- 不修改 `docs/specs/parallel-execution-protocol.md`
- 不修改 `docs/current.md`、`docs/task-index.md`、`docs/decision-log.md`
- 不把 `product_lane_max=5` 提前写成当前 authority
- 不创建 `tools/pr-factory/**`
- 不给任何 product code、runtime、migration、worker、frontend 开新通道

### 1.3 编号映射

旧 backbone 文档把本主题写在 `PR59 / T-P1A-034`。Wave 3A 重排后，本次实际 dispatch 落点是 `PR60 / T-P1A-035`，但 deliverable 仍然是同一份 surge protocol candidate。后续 closeout、audit、tooling 讨论都应以当前编号为准，不再沿用旧编号做 authority 判断。

## §2 Enforced Baseline

### 2.1 当前生效口径

当前真正生效的并行基线只来自两个地方：

- `AGENTS.md`
- `docs/specs/parallel-execution-protocol.md`

在这两个 authority 入口被正式改写之前，下面四条视为唯一硬基线：

| Baseline field | Current enforced value | 说明 |
|---|---:|---|
| `product_lane_max` | `3` | 只计算 product code / runtime / authority-bearing product implementation |
| `authority_writer_max` | `1` | `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` 永远单写者 |
| `same_file_group_writer_max` | `1` | 同一 conflict domain 单写者 |
| `review_audit_research_not_counted_as_product` | `true` | 仅当它们不写 authority 时成立 |

### 2.2 当前基线的直接含义

1. 研究、审计、原型可以多 lane 并行，但它们不能借机提升 product 并发上限。
2. `product_lane_max=3` 仍然是当前唯一可执行的 product 并发上限。
3. `authority_writer_max=1` 仍然覆盖所有 ledger / closeout / task-state 同步动作。
4. 任何 surge 讨论只要影响 authority、CI gating、runtime branching、工具默认值，就必须先回到本节基线判断。

### 2.3 当前 rollback target

无论 surge 候选之后如何讨论，当前默认回退目标已经固定：

- `product_lane_max=3`
- `authority_writer_max=1`

只要发生 lane 冲突、职责歧义、file-domain 交叉、closeout 未完成、CI 无法证明边界清晰，系统就应回到这个 `Enforced baseline`，而不是发明第三种临时口径。

## §3 Tracked Advisory Pools

### 3.1 定义

`Tracked advisory pools` 是调度可视化概念，不是当前 authority，不应被任何脚本、CI、runtime、branch naming 规则当成强制门。

候选池上限如下：

| Advisory pool | Candidate max | 当前用途 |
|---|---:|---|
| `research_pool_max` | `8` | dispatch 规划、scan/probe/backlog 压力盘点 |
| `prototype_pool_max` | `3` | repo 外 prototype 或 docs-only prototype 调度 |
| `audit_pool_max` | `3` | 反方审计、外审、review lane 预算 |

### 3.2 为什么只叫 advisory

这些数字目前只是帮助 Wave 3A / 3B 做排程，不具备下列权力：

- 不能替代 `product_lane_max=3`
- 不能替代 `authority_writer_max=1`
- 不能自动批准多 product lane 同时开工
- 不能自动批准 sidecar 改 authority
- 不能作为“既然池子还没满，就可以再开一个 product PR”的论据

### 3.3 与当前协议的关系

如果 dispatch 里出现“research 还有空位，所以可以顺手改协议、改 tool、改 runtime”的推导，应判为越权。`Tracked advisory pools` 只能做排程提示，不能做实施依据。

## §4 Surge Candidate

### 4.1 候选目标

`Surge candidate` 只讨论一个升级点：当 PR Factory 已经证明文件域治理、审计回路、CI 验证、closeout discipline 都足够稳定时，是否把 product 并发从 `3` 升到 `5`。

候选形态如下：

| Field | Candidate value | Status |
|---|---:|---|
| `product_lane_max` | `5` | candidate only |
| `authority_writer_max` | `1` | unchanged |
| `research_pool_max` | `8` | candidate only / advisory first |
| `prototype_pool_max` | `3` | candidate only / advisory first |
| `audit_pool_max` | `3` | candidate only / advisory first |

### 4.2 明确不是当前生效值

以下判断在当前都属于错误：

- “Wave 3A 现在已经是 `product_lane_max=5`”
- “只要 research/prototype 不冲突，就可以默认开到 5 个 product lane”
- “PR60 落地后可以在脚本里把 5 写死”
- “CI 以后按 5 个 product lane 去做默认分支化”

正确说法只有一句：

`Surge candidate` 只是 closeout 审核对象；在 promotion 发生前，当前生效基线仍是 `product_lane_max=3` 与 `authority_writer_max=1`。

### 4.3 authority 不随 surge 变化

即使未来 surge 被批准，`authority_writer_max=1` 也不跟着放宽。ScoutFlow 的高峰期治理问题，本质上是 product lane 扩容候选，不是 authority multi-writer 候选。

## §5 Activation Gates And File-Domain Matrix

### 5.1 Surge activation gates

`Surge candidate` 只有在下面条件全部满足时，才允许被 closeout 讨论为 promoted authority：

1. `PR60` 本文档被显式 promoted，而不是只停留在 architecture candidate。
2. `PR67` closeout 明确写出 surge verdict，而不是在聊天里默认生效。
3. Wave 内每个 dispatch 都声明自己的 `allowed_paths` 与 `forbidden_paths`。
4. 同一 wave 的 file-domain matrix 经人工核对后无交叉写入风险。
5. redlines、secrets、tests、diff-scope 检查持续可通过。
6. 没有出现“research / prototype lane 借道 authority 或 product code”的 incident。

只要其中任一项不成立，结论就必须回到 `Enforced baseline`，而不是给 surge 打半生效补丁。

### 5.2 File-domain matrix protocol

每个 wave 的 dispatch 都必须把文件域互斥写清楚。最小协议如下：

| Rule | 要求 |
|---|---|
| `dispatch_declares_paths` | 每个 PR 必须列 `allowed_paths` / `forbidden_paths` |
| `matrix_intersection_zero` | 两个并行 PR 的写路径交集必须为空，或被显式串行化 |
| `authority_group_reserved` | `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` 只归 authority writer |
| `same_file_group_single_writer` | 同一个冲突域永远单写者 |
| `forbidden_root_freeze` | `services/**`、`apps/**`、`workers/**`、`packages/**`、`migrations/**`、`data/**`、`referencerepo/**` 不能被 docs-only surge candidate 越权触碰 |

### 5.3 Merge sequencing

PR Factory 的 merge 顺序也必须服从文件域，而不是服从“谁先跑完”：

1. authority / ledger / closeout 类 PR 先决议
2. product lane PR 按 conflict domain 合并
3. research / prototype PR 可以并行准备，但不能反向定义 authority
4. 任何需要改基线协议的内容，只能在明确 closeout 节点做 verdict

## §6 PR Factory 7-Step Workflow

### 6.1 Workflow

PR Factory 候选工作流固定为七步：

1. `dispatch define`
   - 生成 dispatch markdown
   - 锁定 task id、allowed paths、validation、stop-the-line
2. `worktree prepare`
   - 从已知 baseline 创建隔离 worktree
   - 绑定唯一分支
3. `worker execute`
   - 只在 dispatch 允许的文件域内产出
   - 禁止顺手扩写 authority 或 product code
4. `self-validate`
   - 跑 docs redline、secret scan、tests、diff check、grep / path checks
5. `publish PR`
   - `git add`、`git commit`、`git push`
   - `gh pr create`
6. `audit lane`
   - 由 Codex / Claude / GPT Pro 等做反方审计
   - 审核 diff scope、边界、验证结论、叙述与事实是否一致
7. `merge or bounce`
   - clear 才能 merge
   - 若发现 path drift、authority drift、validation drift，则退回修复或关闭

### 6.2 每一步的产物约束

| Step | 必需产物 | 不允许的偷换 |
|---|---|---|
| 1 | dispatch | 用聊天口头约定替代 allowed paths |
| 2 | fixed worktree + branch | 在主 repo 直接动手 |
| 3 | scoped diff | 顺手改 siblings / forbidden paths |
| 4 | command evidence | 只说“应该没问题” |
| 5 | PR link | 只本地 commit 不建 PR |
| 6 | audit verdict | 审计员直接写 authority |
| 7 | merge / bounce record | 把 candidate 自动视为 promoted |

## §7 Tooling Relationship And Rollback Protocol

### 7.1 与未来 PR Factory tooling 的关系

本候选协议允许引用未来 tooling 方向，但不在本 PR 内创建任何 `tools/pr-factory/**` 文件。工具化只是后续候选：

- dispatch helper
- worktree helper
- audit helper
- merge helper

如果后续 tooling 方案与本文冲突，以 authority closeout verdict 为准，而不是以先写出来的脚本为准。

### 7.2 Rollback triggers

出现以下任一情况时，应立即停止 surge 叙事并回退：

- 发现并行 PR 写路径有交叉
- 发现 docs-only candidate 被早期 wave 当成 enforceable contract
- 发现有人据此开第 4 / 第 5 个 product lane
- 发现 authority writer 被并行拆分
- 发现脚本、CI、dispatch 模板开始读取 `product_lane_max=5` 作为当前默认值

### 7.3 Rollback target

回退目标只有一个：

- `Enforced baseline`
- `product_lane_max=3`
- `authority_writer_max=1`

回退后需要做的动作：

1. 停止使用 surge 话术指挥新 PR
2. 在 closeout / incident 记录中写明触发原因
3. 重新核对 file-domain matrix
4. 只有 user 明确 gate 后，才允许再次讨论 surge promotion

## §8 Promotion Acceptance

### 8.1 Promotion 前必须回答的问题

`Surge candidate` 想从 candidate 升为 authority，至少要回答下面五个问题：

1. `PR60` 本文档是否被显式 promoted，而不是仅作为 architecture note 存档？
2. `PR67` closeout 是否明确批准 surge，而不是只记录“可以继续观察”？
3. PR Factory 的 file-domain matrix 是否在一个完整 wave 内证明可执行？
4. 是否已经有可审计的 tooling plan，但 tooling 本身还没有越权改基线？
5. `0` 个 authority collision 与 `0` 个 product-lane ambiguity 是否有证据支持？

### 8.2 Promotion 通过后的唯一允许变化

只有上面的问题都被 closeout 证据支撑后，后续 authority 才可以考虑把以下内容正式落入 baseline：

- `product_lane_max=5`
- `Tracked advisory pools` 是否保留为 advisory 或部分转成 enforced
- 对 dispatch template 的最小补充字段

在那之前，本文只能被引用为：

`research-only / protocol-candidate / not-authority / not-runtime-approval`

### 8.3 当前结论

截至本 PR，ScoutFlow 只拥有一份 surge protocol candidate，还没有一份生效的 surge protocol authority。当前仍应按下列口径执行：

- `Enforced baseline`
- `product_lane_max=3`
- `authority_writer_max=1`
- `Surge candidate` 仅供 PR67 closeout 审核
