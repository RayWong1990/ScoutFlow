---
title: STEP2 Local Mode And pack_lint v2.5 Surface Note
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
scope: STEP2A items 2A-2 and 2A-3
---

# STEP2 Local Mode And `pack_lint v2.5` Surface Note

> State: candidate / not authority / not execution approval.

## 1. Local Mode Verification

The local-mode requirement is satisfied in substance, but one previously used command shape is invalid.

Verified facts:

- `codex-cli` version is `0.128.0`.
- `codex --help` shows `--remote` as explicit opt-in, so default CLI behavior is local.
- `codex exec --help` does not expose `--remote`, which means bounded non-interactive execution naturally uses the local CLI path.
- `codex login status` returns `Logged in using ChatGPT`.
- Local smoke probe succeeded using:

```bash
printf 'Return exactly LOCAL_MODE_SMOKE and nothing else.\n' | codex exec --ephemeral --skip-git-repo-check -C /Users/wanglei/workspace/ScoutFlow -
```

Operational rule for STEP3:

- use local Codex CLI
- do not pass `--remote`

Incorrect command shape that must not be reused:

```bash
codex --compact-mode local
```

This CLI form is not supported and would fail with an argument error.

Preferred command shapes:

```bash
# interactive local CLI
codex -C /Users/wanglei/workspace/ScoutFlow

# bounded non-interactive local execution
codex exec --ephemeral -C /Users/wanglei/workspace/ScoutFlow -
```

## 2. `pack_lint v2.5` Minimum Upgrade Surface

Current baseline:

- parser is legacy `PR*.md` oriented
- rule assembly is legacy PR-pack oriented
- CLI currently takes `pack_dir` plus severity/output/rule knobs
- existing tests cover the legacy path only

Minimum v2.5 scope:

1. Add mode selection:
   - `legacy`
   - `dispatch-v25`
   - `auto`
2. In `auto` mode:
   - if `manifest.jsonl` and `dispatches/` exist, use v2.5 logic
   - otherwise keep legacy behavior
3. Add manifest loader:
   - parse `manifest.jsonl`
   - count total dispatches by manifest entries
4. Add dispatch markdown loader:
   - read `dispatches/*.md`
   - compare frontmatter against manifest fields
5. Add minimum rule set:
   - manifest JSONL parse and line count
   - file existence for manifest file paths
   - `dispatch_slot` and `task_id` range/uniqueness
   - no live `PR #` hardcode in dependency fields
   - no commander-injected commit hash / sha256 hardcode
   - handoff chain parseability
   - forbidden/allowed path collision checks
   - stop-class detectability for commander-consumed fields
   - credential/token/cookie rejection
6. Preserve legacy tests and add a small v2.5 fixture set:
   - happy path
   - manifest/file mismatch
   - duplicate/range violation
   - hardcoded PR/hash rejection
   - handoff chain break
   - forbidden path collision

Items explicitly not required in the v2.5 minimum scope:

- automatic `visual_touchpoint` inference
- `product_lane_max` scope audit
- narrative quality checks

Those belong in commander/readback or audit layers, not lint.

## 3. Blockers

Only one hard blocker was identified for STEP2 documentation:

- any document or prompt that still says `codex --compact-mode local` must be corrected before STEP3

Non-blocking caveats:

- local CLI may emit plugin/analytics `403` warnings while still succeeding
- v2.5 implementation will need its first manifest/dispatch fixture set before promotion

## 4. Primary Evidence Paths

- [step2-prep-checklist-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/step2-prep-checklist-2026-05-05.md:105)
- [dispatch127-176-pack-design-v3-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/dispatch127-176-pack-design-v3-2026-05-05.md:178)
- [pack_lint.py](/Users/wanglei/workspace/ScoutFlow/tools/pack_lint.py:113)
- [test_pack_lint.py](/Users/wanglei/workspace/ScoutFlow/tests/tools/test_pack_lint.py:55)
