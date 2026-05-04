# PRD/SRD Promote to v2 Retro — 2026-05-04

## 决策

把 PRD v1 + v1.1 amendment + v1.2 amendment promote 成 `docs/PRD-v2-2026-05-04.md`。
SRD 同样 promote 成 `docs/SRD-v2-2026-05-04.md`。
旧文件全部 `mv` 到 `docs/archive/`。

## 为什么 promote

- amendment 链已经稳定，继续叠读成本过高
- `T-P1A-014` 已把入口、LP、NFR/CR 减重到可维护状态
- 新 agent 不应再读三四份文件才能拼出当前 base
- promote 时保留 `T-P1A-014` 的减重结果，不恢复被砍掉的条目

## 决策范围

- promote = 文档基线重整；不批准任何新 runtime / capability
- `audio_transcript` / BBDown runtime / workers / frontend / Phase 2-4 实现仍 gated
- 新 amendment 仍可发起，但 base 从 v2 起算

## 不做的事

- 不动产品代码：`services/**`、`tests/**`、`migrations/**`
- 不改 `raw-response-redaction` / `worker-receipt-contract` / `platform-adapter-risk-contract` / `bbdown-adapter-contract-draft` 的语义本体
- 不改 LP 4 条硬约束
- 不解锁任何 Phase 2-4 runtime

## archive 路径

旧文件全部进 `docs/archive/`，由 `docs/archive/README.md` 维护 mapping。

## 后续

- 历史 retro / decision-log / research note 引旧 amendment 时，改指向 archive
- forward authority 一律指向 v2

## Path-only reference maintenance exceptions

During stale-forward-reference cleanup, this task also updated a few historical reference paths outside the original narrow forward-authority list:

- `docs/plans/**`: old PRD/SRD live-path references were rewritten to `docs/archive/**`
- `docs/research/**`: old PRD/SRD live-path references were rewritten to `docs/archive/**`
- `docs/specs/bbdown-adapter-contract-draft.md`: old amendment live-path references were rewritten to `docs/archive/**`

These edits are path-only reference maintenance. They do not change product semantics, runtime approval, BBDown contract meaning, redaction rules, receipt schema, PlatformResult enum, or Trust Trace DTO.

This exception is explicitly recorded because `bbdown-adapter-contract-draft.md` was a forbidden semantic-edit surface in the original dispatch; the audit-fix authorizes only path reference correction, not contract body changes.
