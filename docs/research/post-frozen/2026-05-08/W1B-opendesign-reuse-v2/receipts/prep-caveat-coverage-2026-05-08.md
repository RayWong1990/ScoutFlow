---
title: W1B Prep Receipt - Master Self-flag Caveat Coverage Check
status: candidate / prep_receipt / not-authority
authority: not-authority
created_by: Codex W1B-PREP
created_at: 2026-05-08
scope: W1B master self-flag caveat carry-forward into candidate docs and PR-description surfaces
disclaimer: "This receipt is candidate-only prep evidence. It does not mean Hermes audit happened, does not approve packages, and does not unlock runtime, browser automation, vault write, or migration."
---

# W1B caveat coverage prep receipt

## Verdict

`verdict=clear_after_source_refresh`

3 条 master caveat 现在已经在 W1B candidate docs 里显式 carry-forward。早先 prep 阶段发现的两个缺口已被 source doc 刷新修复：

1. `04-w1b-hermes-audit-prompt-skeleton.md` 现已写明 browser visual evidence 的两个合法限定路径。
2. candidate-doc PR description surface 在 `02-w1b-dispatch-pack.md` 的 `D-W1B-003` 现已显式要求 PR body inline 3 条 caveat。

## Source set

- `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/W1B-MASTER-SELFFLAG.md`
- `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/01-w1b-cluster-spec.md`
- `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/02-w1b-dispatch-pack.md`
- `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/03-w1b-codex-commander-prompt-skeleton.md`
- `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/04-w1b-hermes-audit-prompt-skeleton.md`

## Master caveat baseline

| Caveat | Master requirement | Evidence |
|---|---|---|
| C1 authority anchor split-truth | W1B register 前 refresh authority anchor；Hermes pre-review 也要先 verify | `W1B-MASTER-SELFFLAG.md:19-25` |
| C2 bundle/tree-shaking evidence | `50kB gzip` 与 tree-shaking 只能由本地 build/measure 证明，不能从 GPT Pro 文档推断 | `W1B-MASTER-SELFFLAG.md:27-32` |
| C3 browser visual evidence conditional | visual review 只能写成 `browser_automation lane 解禁后` 或 `local manual screenshot capture without runtime` 之一；不能暗示已解禁 | `W1B-MASTER-SELFFLAG.md:33-39` |

## Coverage matrix

| Surface | C1 | C2 | C3 | Notes |
|---|---|---|---|---|
| `01-w1b-cluster-spec.md` | clear | clear | clear | 有 split-truth prerequisite、bundle evidence 条件、`v2-E9` blocked-note honesty。见 `01-w1b-cluster-spec.md:25-32,117-125,343-345` |
| `02-w1b-dispatch-pack.md` | clear | clear | clear | 有 split-truth note、D-W1B-007 本地 build evidence、browser visual blocked honesty。见 `02-w1b-dispatch-pack.md:25-30,257-276,652-655` |
| `03-w1b-codex-commander-prompt-skeleton.md` | clear | clear | clear | prerequisite check、bundle local-build honesty、browser visual blocked evidence、PR body 含 self-flag。见 `03-w1b-codex-commander-prompt-skeleton.md:31-47,175-205,225-247` |
| `04-w1b-hermes-audit-prompt-skeleton.md` | clear | clear | clear | 已补齐 visual evidence 的两条合法限定路径，并要求缺失时给出 concern/reject。见 `04-w1b-hermes-audit-prompt-skeleton.md:54-68,126-132` |

## PR-description surface check

| Surface | Result | Evidence | Concern |
|---|---|---|---|
| candidate-doc PR surface (`D-W1B-003`) | clear | `02-w1b-dispatch-pack.md:122-146` 已要求 `PR body with candidate-only boundary and all 3 Master Self-flag caveats inlined` | no remaining gap |
| implementation PR surface (`D-W1B-015` + `03` prompt) | clear | `02-w1b-dispatch-pack.md:546-581`, `03-w1b-codex-commander-prompt-skeleton.md:225-247` | 03 的 self-flag 已覆盖 3 条 caveat，但依赖后续 paste/执行时不丢失 |

## Detailed observations

### 1. Caveat 1 carry-forward

Carry-forward 基本成立。`01/02/03/04` 都保留了 split-truth 和 `historical reference / live truth` 口径，且 `04` 明写 Hermes 必须先跑 prerequisite check，不得静默采用历史数字。

### 2. Caveat 2 carry-forward

Carry-forward 基本成立。`01` 把 `50kB gzip` 标成 candidate threshold，`02` 的 D-W1B-007 要求 `pnpm build` 与 before/after evidence，`03` 禁止伪造 bundle data，`04` 也提醒 Hermes 没有本地 build artifact 时只能标 `evidence-required`。

### 3. Caveat 3 carry-forward

Carry-forward 现已完整。`04` 已明确 visual evidence 只能走两条合法限定路径之一，并要求 Hermes 对缺失/泛化写法报 `CONCERN` 或 `REJECT`。

### 4. Master requirement that PR body inline all 3 caveats

`W1B-MASTER-SELFFLAG.md:45-51` 明写 `PR body 也必 inline 这 3 条`。当前 candidate-doc PR surface 已将这条要求显式写入，不再依赖隐含 carry-forward。

## Prep conclusion

当前可判为：

- candidate docs coverage: `clear`
- PR-description coverage: `clear`
- downstream Hermes prep safety: `locked at candidate-doc level`

这份 receipt 只是 prep evidence，不是 authority，不表示任何审计已经发生，也不表示 package path、runtime、browser automation、vault write、migration 已获得许可。
