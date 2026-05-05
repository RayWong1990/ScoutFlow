---
type: tooling-plan-candidate
version: 1.1
title: ScoutFlow PR Factory Tooling Plan
date: 2026-05-05
authority_status: research-only / tooling-candidate / not-authority / not-runtime-approval
suggested_commit_path: docs/architecture/pr-factory-tooling-plan-2026-05-04.md
source_trace:
  - docs/research/pr55-pr74-worklist-candidate-2026-05-04.md §11
  - docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md §4.2-§4.3, §7.2
  - docs/research/doc1-doc2-doc3-v1.1-acceptance-errata-report-2026-05-04.md P1-5
  - docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md §6-§7
related_task: T-P1A-041 / T-P1A-041A
dispatch_mapping:
  original_backbone_slot: PR65 / T-P1A-040
  current_dispatch_slot: PR66 / T-P1A-041
verdict: "本文档把原始 `tools/pr-factory/` 六文件候选收敛为一个 architecture plan 加一个单文件 Python CLI helper。当前交付只服务本地 shoulder 生命周期辅助，不修改 services/apps/workers/packages，不批准 runtime，也不把 surge candidate 提前写成生效基线。"
---

# ScoutFlow PR Factory Tooling Plan

> 定位：Wave 3A tooling candidate。它把原始 shell directory 方案压缩为一个单文件 CLI，优先解决 macOS 兼容、默认 dry-run、显式 `--execute`、`.git` 后缀清洗、以及 `referencerepo/` resolved containment 这几个审计焦点。
>
> 生效边界：本计划只描述本地 helper 的命令契约与安全边界，不修改 `AGENTS.md`、`docs/current.md`、`docs/task-index.md`、`docs/decision-log.md`、`docs/specs/parallel-execution-protocol.md`，也不把 `product_lane_max=5` 之类候选值提前落成 authority。

## §1 Why This PR Shrinks The Original Backbone

原始 backbone 想在 `tools/pr-factory/` 下落 3 个 shell script、1 个模板和 1 个 README。当前 dispatch 把它收窄成两个 tracked artifact：

- `docs/architecture/pr-factory-tooling-plan-2026-05-04.md`
- `tools/scoutflow_pr_factory.py`

这样收窄有三个原因：

1. 当前仓库还没有 `tools/` 子树分包惯例。一次性引入 `tools/pr-factory/**` 会把 review 面做大。
2. v1.1 errata 已经点明 macOS `sed -i ''`、`.git` 后缀和 `--dry-run` 是核心风险；这些风险用 Python 单文件更容易一次性收口。
3. Wave 3A closeout 还没发生，当前目标是把 shoulder lifecycle 的机械动作写成可验证工具，而不是顺带扩展一整套 dispatch 脚手架目录。

结论：V1 先交付一个单文件 helper，把 shell directory 拆分留给未来 candidate，不在 PR66 里一次吃完。

## §2 Scope

### 2.1 V1 做什么

- 提供一个单文件 CLI：`tools/scoutflow_pr_factory.py`
- 覆盖三个本地 shoulder 机械动作：
  - `fork-shoulder`
  - `sync-shoulder`
  - `archive-shoulder`
- 默认 dry-run；只有显式传入 `--execute` 才执行 side-effect command
- 强制检查 `.gitignore` 已包含 `referencerepo/`
- 强制校验 `category` / `shoulder_id` 是单段 path segment
- 强制所有 shoulder path resolved 后仍位于 `<repo>/referencerepo/**`
- 统一清洗 upstream URL，避免 `repo.git.git`
- 把 local-only 元数据写进 `referencerepo/**/_SCOUTFLOW_*.local.md`

### 2.2 V1 明确不做什么

- 不创建 `tools/pr-factory/**`
- 不改 `docs/specs/parallel-execution-protocol.md`
- 不写 `docs/shoulders-index.md`
- 不写 `docs/research/shoulders/**`
- 不创建 `services/**`、`apps/**`、`workers/**`、`packages/**`
- 不批准任何 runtime、migration、frontend、vault write

## §3 Command Set

| Subcommand | 目标 | Tracked repo writes | Local-only writes |
|---|---|---|---|
| `fork-shoulder` | 建立本地 clone + fork remote + local meta | none | `referencerepo/<category>/<id>/**` |
| `sync-shoulder` | 看 upstream 漂移、输出 sync report | none | none |
| `archive-shoulder` | 把本地 shoulder 移到 `_archived/` 并记 archive note | none | `referencerepo/_archived/<category>/<id>/**` |

V1 的 command set 故意只覆盖 local-only 机械动作。任何 tracked 文档同步仍然留给 authority 或 research PR 去做，避免工具越界写 ledger。

## §4 CLI Contract

### 4.1 Global contract

- 默认 workspace root = 脚本所在仓库根目录
- 允许 `--workspace-root` 覆盖
- 所有命令都先验证 `.gitignore` 含 `referencerepo/`
- 所有命令默认只输出 dry-run plan；必须显式加 `--execute` 才会执行
- `--dry-run` 仍可显式传入，用于保留旧命令习惯
- dry-run 输出必须把将执行的 shell 命令和将写入的 local-only 文件都列出来

### 4.2 `fork-shoulder`

```text
python tools/scoutflow_pr_factory.py fork-shoulder [--dry-run|--execute] <shoulder_id> <category> <upstream_url> <github_user>
```

动作顺序：

1. 规范化 upstream URL，去掉结尾 `.git`
2. 在 `referencerepo/<category>/` 下 clone `<shoulder_id>`
3. `origin -> upstream`
4. 准备 `gh repo fork ... --clone=false`
5. 追加 `origin = git@github.com:<github_user>/<repo_name>.git`
6. 创建 `scoutflow-fork` branch
7. 写 `_SCOUTFLOW_META.local.md`
8. 写 `_SCOUTFLOW_FORK.local.md`

### 4.3 `sync-shoulder`

```text
python tools/scoutflow_pr_factory.py sync-shoulder [--dry-run|--execute] <shoulder_path>
```

动作顺序：

1. `git fetch upstream`
2. `git checkout scoutflow-fork`
3. 统计本地 patch 数
4. 统计 upstream 新 commit 数
5. 输出 diff file list

V1 只负责报告，不自动 merge upstream，也不自动改 tracked docs。

### 4.4 `archive-shoulder`

```text
python tools/scoutflow_pr_factory.py archive-shoulder [--dry-run|--execute] <shoulder_id> <category> <reason>
```

动作顺序：

1. 把 `referencerepo/<category>/<id>/` 移到 `referencerepo/_archived/<category>/<id>/`
2. 追加 `_SCOUTFLOW_ARCHIVE.local.md`
3. 输出提醒：tracked `docs/shoulders-index.md` 与 decision-log 仍需单独 authority/research PR

## §5 Safety Invariants

### 5.1 `referencerepo/` 永远 local-only

工具在执行任何操作前都必须确认：

- 仓库根 `.gitignore` 存在
- `.gitignore` 中明确有一行 `referencerepo/`

如果这条不成立，CLI 必须 fail loud。不能因为脚本方便就把 local-only 目录变成 tracked path。

### 5.2 Dry-run first, explicit execute

V1.1 的默认行为不是“直接执行”，而是：

1. 默认生成 dry-run plan，或显式传入 `--dry-run`
2. 看输出步骤和目标路径
3. 确认无误后再用 `--execute` 真执行

这和 PR Factory 的 `dispatch define -> worktree prepare -> worker execute -> self-validate` 顺序一致。工具本身不跳过 dry-run gate。

### 5.3 `.git` suffix stripping

`fork-shoulder` 必须从 upstream URL 派生干净 repo name。接受：

- `https://github.com/foo/bar`
- `https://github.com/foo/bar.git`
- `git@github.com:foo/bar.git`

统一生成 `bar`，而不是 `bar.git`。

### 5.4 no authority writes

本工具不能直接改：

- `AGENTS.md`
- `docs/current.md`
- `docs/task-index.md`
- `docs/decision-log.md`
- `docs/shoulders-index.md`
- `docs/research/shoulders/**`

理由很简单：这些是 closeout、probe、decision lane 的 write-set，不应被 local helper 偷写。

### 5.5 resolved path containment

T-P1A-041A 追加约束：

- `category` 与 `shoulder_id` 必须是单段 path segment；空字符串、`.`、`..`、slash、backslash、absolute path 均 fail loud
- `fork-shoulder` / `sync-shoulder` / `archive-shoulder` 的目标 path 必须在 `Path.resolve()` 后仍位于 `<repo>/referencerepo/**`
- `sync-shoulder` 不接受 `/tmp`、repo root、`docs`、`../docs`、`<repo>/docs` 或裸 `referencerepo` root
- containment 使用 `Path.relative_to()` 语义，不用 string-prefix 判断

## §6 Local-only Files Written By V1

| File | Purpose | Track status |
|---|---|---|
| `_SCOUTFLOW_META.local.md` | clone/fork metadata, cadence, timestamps | local-only |
| `_SCOUTFLOW_FORK.local.md` | fork patch ledger template | local-only |
| `_SCOUTFLOW_ARCHIVE.local.md` | archive reason and time | local-only |

这些文件都在 `referencerepo/**` 下，故意带 `.local.md` 后缀，避免被误认为可提交文档。

## §7 Why Python Instead Of Shell For V1

原始 candidate 倾向 3 个 shell script。当前改成单文件 Python，不是为了“更高级”，而是为了更少审计噪音：

- Python 直接规避了 BSD/GNU `sed` 分歧
- `argparse` 能稳定提供 `--help`
- dry-run 输出更容易结构化
- 一个文件就能统一 URL 清洗、路径约束、metadata 模板
- review diff 比 3 个 shell script + 2 个 markdown 更小

这里的取舍是：先保留 shell 的动作语义，再把执行层压到一个更好验证的实现里。

## §8 Mapping To The Surge Protocol

`docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md` 已经定义了 PR Factory 的 7 步骤。V1 tool 与它的关系如下：

| Surge step | V1 tool role |
|---|---|
| `dispatch define` | 不负责 |
| `worktree prepare` | 不负责 |
| `worker execute` | 只负责 local-only shoulder mechanical ops |
| `self-validate` | 负责 `--dry-run`、path guard、URL normalization |
| `publish PR` | 不负责 |
| `audit lane` | 不负责 |
| `merge or bounce` | 不负责 |

所以 V1 不是完整 PR Factory，而是其中一个“repo 外 / local-only shoulder 运维 helper”。

## §9 Future Split Boundary

未来如果真要展开成 `tools/pr-factory/**`，建议按下面拆分：

1. `tools/pr-factory/shoulders.py`
   - 专管 fork/sync/archive shoulder
2. `tools/pr-factory/dispatch.py`
   - 生成 dispatch skeleton
3. `tools/pr-factory/worktree.py`
   - 开/清理 worktree
4. `tools/pr-factory/audit.py`
   - 汇总 validation evidence
5. `tools/pr-factory/README.md`
   - 汇总命令用法

但这一步需要新 dispatch；PR66 不提前开这个面。

## §10 Validation Contract For PR66

PR66 里至少要证明以下事实：

1. `docs/architecture/pr-factory-tooling-plan-2026-05-04.md` 存在且 >100 行
2. `tools/scoutflow_pr_factory.py` 存在且 >100 行
3. `python -m py_compile tools/scoutflow_pr_factory.py` 通过
4. `python tools/scoutflow_pr_factory.py --help` 通过
5. `python tools/scoutflow_pr_factory.py fork-shoulder --dry-run TEST capture https://github.com/foo/bar.git someuser` 通过
6. 代码中确实存在 `--dry-run`
7. 代码中确实存在 `.git` suffix stripping
8. 没有创建 `tools/pr-factory/**`
9. 没有触碰 `services/**`、`apps/**`、`workers/**`、`packages/**`

## §11 Closeout Carry-forward

PR67 closeout 需要把这次 tooling lane 作为已落地 candidate 记账，但不需要把它升级成 authority。closeout 里应该只做三件事：

- 记录 `PR66 / T-P1A-041` 已 merged
- 在 `docs/specs/contracts-index.md` 里登记 tooling candidate 的文件路径
- 保持 `Active product lane max=3`、`Authority writer max=1`

也就是说，PR66 完成后，系统得到的是“更可执行的 local helper”，不是“更激进的并发基线”。
