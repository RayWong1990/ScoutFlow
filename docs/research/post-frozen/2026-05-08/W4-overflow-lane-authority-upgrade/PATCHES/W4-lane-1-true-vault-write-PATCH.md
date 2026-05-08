---
title: W4 Lane 1 (true_vault_write) Patch — live truth + spec hardening + §5.7 lane-specific
status: candidate / patch
authority: not-authority
created_by: gpt-pro
parent_cluster: W4
parent_lane: true_vault_write
created_at: 2026-05-08
upstream_finding: "audit catch — lane 1 不只缺 §5.7 lane-specific verify, 还需要把 live truth、12-field role contract、dry-run/true-write split、secret scan、rollback 前置条件压实"
disclaimer: 真态数字以 GitHub live main HEAD 为准; 撰写时刻数字仅为历史参考。
prerequisite_check: live_checked_with_authority_anchor_drift
main_head_drift: "docs/current.md main anchor still lags live origin/main=45e88d4 / PR #257; this patch records the drift but does not repair authority"
active_product_count: "0/3 (refreshed at §0.5 Check)"
authority_writer_count: "0/1 (refreshed at §0.5 Check)"
wave_state: "WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED"
write_enabled: false
memory_batch_count: 17
deliverable_type: patch
target_replacement_section:
  - "§0.5 Prerequisite Check"
  - "§1.4 实施前置条件"
  - "§5.7 amend_and_proceed pattern"

---
# Lane 1 Patch — true_vault_write

> State: candidate / patch / not-authority / not runtime approval / not migration approval / not lane unlock.

## §0.5 Prerequisite Check replacement

| Check | Live readback | Result |
|---|---|---|
| `origin/main` | `45e88d4` / `Merge pull request #257 from RayWong1990/codex/w4-b-step0-convergence` | use as live truth; older SHAs demoted to history only |
| docs/current.md | Active `0/3`, Authority writer `0/1`, `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`, 5 overflow lane Hold, but main anchor still older than `origin/main` | lane state matches; authority anchor drift remains out of scope here |
| docs/task-index.md | Active table empty; Review empty; product lane `0/3`; authority writer `0/1` | matches prompt authority state |
| docs redline / secret redline | both checks pass in worktree | text boundary clean; not equal to lane unlock |
| bridge config + schemas | both config branches keep `write_enabled=False`; frontmatter mode stays `raw_4_field`; commit response remains dry-run-only | confirms helper stack is still preview/dry-run continuity |

**prerequisite_check = `live_checked_with_authority_anchor_drift`**. This packet records the 2026-05-08 live truth but does not touch authority files.

## §0.5 B-lane sanity

Lane 1 §0.5 should now explicitly mention three live boundaries: `write_enabled=False` in both config branches, `frontmatter_mode=raw_4_field`, and `BridgeVaultCommitResponse` being dry-run-only. If any of these three truths are absent from the main doc, this patch should add them.

## §1.4 implementation prerequisites replacement

Replace generic wording with the following lane-specific tightenings:

1. `12-field` means **12 role slots**, not today's enforced schema names. Only 4 slots are live exact fields today: `title/date/tags/status`. The other 8 slots must be expressed as role contracts until a later promoted path locks names.
2. `dry-run response vs true-write response split` must cite live code truth:
   - preview = `BridgeVaultPreviewResponse`
   - commit dry-run = `BridgeVaultCommitResponse(committed=false, dry_run=true, write_enabled=false, error=write_disabled)`
   - future true-write response = separate contract family, not a wording tweak on dry-run
3. `secret scan` must cover title, URL, transcript, summary/rewrite, markdown body, and receipt fragments staged for vault. If transcript/summary is absent because Lane 2 is still Hold, the state must be written as `blocked/not_present`, not `scan passed`.
4. `atomic write + rollback` must stay honest:
   - require completeness gate, secret scan gate, path containment gate, render/hash gate, atomic write gate, receipt/rollback gate
   - no promise that rollback always restores history
   - if downstream RAW sync already absorbed the file, escalate to manual cleanup gate
5. `remaining Hold lanes readback` must stay visible in Lane 1:
   - runtime_tools Hold
   - dbvnext_migration Hold
   - browser_automation Hold
   - full_signal_workbench Hold
6. `preview helper != production writer` must be written as a first-class boundary, not left as implied context.

## §5.7 amend_and_proceed — lane-specific replacement

Replace the cloned generic §5.7 text with the following lane-specific stop rules:

### Amend trigger matrix

| Trigger | Lane-specific detection | Required action | Why no amend-continue |
|---|---|---|---|
| Secret leakage detected | cookie/token/API key/raw header/raw auth sidecar appears in vault preview, frontmatter draft, evidence packet, run receipt, stdout/stderr, or markdown body | STOP-THE-LINE; quarantine artifact path; write redacted drift report under `docs/research/post-frozen/W4/lane-1/receipts/`; do not continue until CC0/CC1 reviews | true vault write can permanently persist leaked material into raw vault; continuation would compound damage |
| Frontmatter completeness drift | any required vault frontmatter field is missing, renamed, semantically overloaded, or derived from unsafe evidence | STOP-THE-LINE; mark preview/commit evidence invalid; produce field-level drift matrix | vault frontmatter is the trust boundary; partial commits are worse than blocked writes |
| `write_enabled` flip drift | local config or branch makes `write_enabled` appear true, or Codex reads dry-run commit as true write permission | STOP-THE-LINE; re-read `bridge/config.py`, `bridge/schemas.py`, `docs/current.md`; write mismatch report | flipping this bit is an authority upgrade, not an implementation detail |
| Partial commit across 7-stage write | any stage after path resolve begins but before durable receipt/manifest closure fails | STOP-THE-LINE; capture exact stage; require rollback/reconciliation plan before next run | partial raw vault state can desync ScoutFlow and Obsidian truth |
| Credential material in evidence path | redaction policy absent or `sensitive_fields_removed` empty for evidence used to build vault content | STOP-THE-LINE; reject evidence as input; regenerate from safe evidence only | credential material is never evidence under LP-SEC-001 |
| Path containment uncertainty | target path contains absolute path, `..`, symlink ambiguity, or non-00-Inbox escape vector | STOP-THE-LINE; no dry-run promotion; record path policy failure | path escape is security-critical and cannot be patched inline |

### Replacement rule

Lane 1 does **not** use “amend and continue” after these triggers. It uses: stop → redacted drift report → CC0/CC1 review → explicit new dispatch if repair is needed. The only allowable continuation is a no-write documentation patch that narrows the failure without touching vault content.

### Receipt requirements

- Receipt path: `docs/research/post-frozen/W4/lane-1/receipts/<timestamp>-true-vault-write-drift.md`.
- Required fields: trigger, detection source, affected candidate output, redaction status, containment status, write-stage reached, rollback need, reviewer needed.
- Forbidden fields: raw credential, raw stdout/stderr, raw vault body, private cookie/header, unredacted target content.

## Self-flag

1. ⚠️ This patch now covers §0.5, §1.4, and §5.7. If the main doc already contains stricter local wording, CC0 should preserve the stricter variant rather than re-cloning this patch verbatim.
2. ⚠️ “12 fields” for frontmatter completeness came from the prompt’s lane-specific trigger language; live bridge schema still exposes `raw_4_field`, so this patch treats 12-field completeness as future role contract, not current bridge truth.
3. ⚠️ Partial commit stages must stay contract-level in this patch; exact implementation stage names belong to a later code-bearing PR, not this spec-only PR.
