---
title: MOD-VISUAL-01-visual-asset-table-creation — Visual asset table creation
status: candidate / dispatch-prompt / not-authority
authority: not-authority
created_at: 2026-05-07
phase: Module
cluster: visual
lane: VISUAL
parent_dispatch_id: U9-phase-2-4-dispatch-catalog-v0
owner_tool: Claude Code / OpenDesign reviewer
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
write_enabled: false
can_open_C4: false
can_open_runtime: false
can_open_migration: false
prerequisites:
  - U4-U8 strategic-upgrade prompt/output ZIP manually reviewed if available
  - PRD/SRD v3 candidate not promoted unless user says so
blocks:
  - downstream dispatches must cite this output before expanding scope
verification_method: module contract audit
risk_level: medium
---

[claim]
# MOD-VISUAL-01-visual-asset-table-creation — Visual asset table creation

[claim]
## §1 Mission

[candidate] 把 visual_asset table creation 限定为 docs-only candidate contract，连接 topic-card preview 但不写 migration。

[lineage] This prompt is a ready-to-paste candidate dispatch skeleton, not a live task order. It exists so a later human-authorized Codex / Claude Code / Hermes run can copy the instructions without re-inventing boundaries. It does not grant any execution right by itself.

[boundary]
[evidence] Baseline facts used here: PRD/SRD v2 仍把可执行基线收束在 manual_url + metadata_only + receipt + trust trace，Phase 2-4 是 outline，不是可执行承诺。 AGENTS 规定 Active product lane max=3、Authority writer max=1，且 current.md / task-index.md / decision-log.md / AGENTS.md 属于高风险 authority surface。 contracts-index 明确 Wave5/后续 surface 多为 candidate；BBDown contract 仍是 draft，frontend/runtime/migration/vault true write 均不得由研究文档自动打开。

[boundary] Lane-specific boundary: U4 visual module 必须以 design-only / fixture-only 为主，不得复用外部项目 runtime/code/layout。

[claim]
## §2 Inputs to read before writing

[deliverable]
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/specs/contracts-index.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/dispatch-template.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/AGENTS.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md
- https://github.com/RayWong1990/ScoutFlow/blob/ea509022eb05a552777373394a6fc2a5077f27f6/docs/research/post-frozen/runs/RUN-3-4-CODEX0-REPORT-2026-05-06.md
- https://github.com/RayWong1990/ScoutFlow/blob/ea509022eb05a552777373394a6fc2a5077f27f6/docs/research/post-frozen/runs/CHECKPOINT-Run3-4-final.json
- local:/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip#04_outputs/post-dispatch176-roadmap-candidate-2026-05-05.md

[claim] Treat every URL above as an input for readback, not as an instruction to change the repository. If one URL is missing or has moved, record `verdict: concern` and keep all can_open flags false.

[claim]
## §3 Prerequisites and lineage

[deliverable]
- `U4-U8 strategic-upgrade prompt/output ZIP manually reviewed if available`
- `PRD/SRD v3 candidate not promoted unless user says so`

[lineage] These prerequisites are semantic gates. They do not open the lane automatically; they only say what the worker must acknowledge before drafting the candidate artifact.

[boundary]
[blocking] Downstream prompts that depend on this task must cite the final output path and must restate `can_open_C4: false`, `can_open_runtime: false`, and `can_open_migration: false` in their own frontmatter.

[claim]
## §4 Multi-pass plan

[boundary]
1. **Pass 1 — baseline readback** — Read PRD/SRD v2, AGENTS, contracts-index, dispatch-template, overflow-registry, Run-2 and Run-3+4 receipts; write a two-column readback that separates repo fact from candidate inference.
2. **Pass 2 — scope proof** — Map this task to visual / VISUAL and identify exactly which prior proof or partial result is being used; never infer a runtime gate from a candidate doc.
3. **Pass 3 — artifact shape** — Draft only the files listed in Output Deliverables; include claim labels, local-only path cautions, and a failure taxonomy for clear/concern/reject/partial.
4. **Pass 4 — boundary audit** — Run the boundary checklist before finalizing: authority files untouched, five overflow lanes still Hold, write_enabled=False preserved, no secrets, no hidden runtime.
5. **Pass 5 — reviewer readback** — Produce a short human readback explaining what changed, what did not change, and which later dispatches remain blocked.
6. **Pass 6 — stdout truth** — Emit the YAML stdout contract exactly, with real files_changed, validation status, and amend_trigger fields; do not smooth partial into clear.

[risk]
[method] The worker should execute the passes in order. If Pass 1 or Pass 2 produces a mismatch against PRD/SRD v2 or Run-3+4 receipts, stop after a concern report; do not continue into artifact drafting.

[claim]
## §5 Hard boundaries

[boundary] `write_enabled=False` must remain true as a preserved condition in any readback. Do not edit bridge config, do not create true vault writes, do not write RAW files, and do not simulate a successful durable write unless the output explicitly labels it as non-writing shadow or dry-run.

[boundary] Do not write `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, or `AGENTS.md`. If an authority writeback appears necessary, emit `verdict: concern` and a proposed amendment trigger; this dispatch is not the authority-writer lane.

[boundary] Do not touch `services/**`, `apps/**`, `workers/**`, `packages/**`, `data/**`, `referencerepo/**`, `services/api/migrations/**`, repo-local browser profiles, cookies, token material, raw stdout/stderr, QR images, auth sidecars, or signed URLs.

[boundary] Five overflow lanes stay Hold: `true_vault_write`, `runtime_tools`, `browser_automation`, `dbvnext_migration`, and `full_signal_workbench`. This prompt may describe an unlock spike, but the spike remains candidate-only and cannot change gate state.

[boundary] `audio_transcript` remains blocked. Media download, ffmpeg, ASR, BBDown live, yt-dlp live, browser automation, and migration execution are not permitted through this prompt.

[claim]
## §6 Output deliverables

[output] Required file outputs for a later authorized run:

[claim]
- `docs/research/post-frozen/modules/visual/visual-asset-table-creation.md`
- `docs/research/post-frozen/modules/module-readback-index.md`

[output] Minimum content shape: one candidate markdown artifact of at least 1,200 CJK+Latin units, one readback section, one risk table, one dependency section, one truthful stdout block, and one self-audit with at least five findings.

[output] Each output paragraph should carry a claim label such as `[candidate]`, `[evidence]`, `[boundary]`, `[instruction]`, `[audit]`, `[lineage]`, or `[limitation]`. Target claim-label coverage is at least 90% of non-heading paragraphs.

[claim]
## §7 Output schema

[output]
```yaml
dispatch_id: MOD-VISUAL-01-visual-asset-table-creation
verdict: <clear|concern|reject|partial>
files_written:
  - <path>
authority_files_touched: false
production_code_touched: false
write_enabled_preserved: true
can_open_C4: false
can_open_runtime: false
can_open_migration: false
overflow_lanes_preserved:
  true_vault_write: Hold
  runtime_tools: Hold
  browser_automation: Hold
  dbvnext_migration: Hold
  full_signal_workbench: Hold
amend_trigger:
  required: <true|false>
  reason: <only if concern/reject/partial>
  suggested_owner: <Codex Desktop|Claude Code|GPT Pro|Hermes|human>
```

[claim] `verdict: clear` only means this specific candidate artifact is internally consistent. It never means runtime, C4, migration, browser automation, true-write, or downstream egress is open.

[claim]
## §8 Self-audit requirements

[audit] Finding 1 must verify allowed paths versus actual files. Finding 2 must verify authority surfaces were not touched. Finding 3 must verify the overflow registry still blocks all five high-risk lanes. Finding 4 must verify no credential or local-only material entered durable output. Finding 5 must verify the output did not upgrade candidate language into authority language.

[audit] Additional findings should cover prerequisite accuracy, no circular dependency, truthful stdout fields, claim-label coverage, readback quality, and whether a later dispatch needs external audit.

[audit] If any self-audit item is uncertain, the worker must choose `verdict: concern` or `verdict: partial`; uncertainty is never hidden in prose.

[claim]
## §9 PR pattern

[claim]
[instruction] Preferred PR pattern is `single docs-only PR` unless this dispatch is packed with sibling candidate docs under the same phase directory. Packed execution is allowed only when the commander keeps authority writer count at zero and emits per-dispatch stdout.

[audit]
[instruction] External audit is required when the artifact changes schema wording, state words, receipt semantics, PlatformResult interpretation, egress contract semantics, or any future dispatch that touches `apps/**` or `services/**` paths.

[boundary]
[instruction] Amendment path: if an authorized worker discovers that this skeleton would need production code or authority files, stop, create an amendment proposal under `docs/research/post-frozen/amendments/`, and leave all can_open flags false.

[claim]
## §10 Verification method

[verification] Run docs redline, secrets redline, and diff whitespace checks when the repository is available. If no repo is available, perform a manual format guard and record `validation_unavailable_reason` in stdout.

[verification] Audit window: module contract audit. A 3-window audit should compare (1) prompt intent, (2) repo diff, and (3) receipt/readback. Informal audit is acceptable only for docs-only low-risk artifacts and must still report limitations.

[verification] Stop-the-line triggers include: a moved authority boundary, an implied runtime gate, a missing prerequisite, any credential-like string, any direct capture creation from recommendation/keyword/RAW gap, any migration path, or any claim that partial proof is full proof.

[claim]
## §11 Truthful stdout contract

[output]
```yaml
MOD-VISUAL-01-visual-asset-table-creation_COMPLETE: <true|false>
verdict: <clear|concern|reject|partial>
files_count: <int>
files_changed:
  - <path>
validation:
  docs_redlines: <pass|fail|not_run>
  secrets_redlines: <pass|fail|not_run>
  diff_check: <pass|fail|not_run>
claim_label_coverage_estimate: <percent>
boundary_preservation_check: <clear|concern|reject>
write_enabled_false_preserved: confirmed
can_open_C4: false
can_open_runtime: false
can_open_migration: false
no_actual_authorization_implied: confirmed
known_limitations:
  - <real limitation, not boilerplate>
next_gate:
  owner: <human|Codex Desktop|Claude Code|GPT Pro|Hermes>
  reason: <why a later gate is needed>
```

[limitation] This skeleton intentionally over-specifies boundaries because ScoutFlow has already seen useful proof chains remain partial. The safer behavior is to preserve a partial verdict until a later human-reviewed artifact closes the gap.

[claim]
[detail] Additional guard for `MOD-VISUAL-01-visual-asset-table-creation`: the worker must restate which evidence is durable, which evidence is synthetic, which evidence is missing, and which reviewer would be responsible for closing the missing proof. This keeps the dispatch useful even when the later run cannot access every upstream file.

[claim]
[detail] Additional guard for `MOD-VISUAL-01-visual-asset-table-creation`: the worker must restate which evidence is durable, which evidence is synthetic, which evidence is missing, and which reviewer would be responsible for closing the missing proof. This keeps the dispatch useful even when the later run cannot access every upstream file.

[claim]
[detail] Additional guard for `MOD-VISUAL-01-visual-asset-table-creation`: the worker must restate which evidence is durable, which evidence is synthetic, which evidence is missing, and which reviewer would be responsible for closing the missing proof. This keeps the dispatch useful even when the later run cannot access every upstream file.

[claim]
[detail] Additional guard for `MOD-VISUAL-01-visual-asset-table-creation`: the worker must restate which evidence is durable, which evidence is synthetic, which evidence is missing, and which reviewer would be responsible for closing the missing proof. This keeps the dispatch useful even when the later run cannot access every upstream file.

[claim]
[detail] Additional guard for `MOD-VISUAL-01-visual-asset-table-creation`: the worker must restate which evidence is durable, which evidence is synthetic, which evidence is missing, and which reviewer would be responsible for closing the missing proof. This keeps the dispatch useful even when the later run cannot access every upstream file.

[claim]
[detail] Additional guard for `MOD-VISUAL-01-visual-asset-table-creation`: the worker must restate which evidence is durable, which evidence is synthetic, which evidence is missing, and which reviewer would be responsible for closing the missing proof. This keeps the dispatch useful even when the later run cannot access every upstream file.

[claim]
[detail] Additional guard for `MOD-VISUAL-01-visual-asset-table-creation`: the worker must restate which evidence is durable, which evidence is synthetic, which evidence is missing, and which reviewer would be responsible for closing the missing proof. This keeps the dispatch useful even when the later run cannot access every upstream file.

[claim]
[detail] Additional guard for `MOD-VISUAL-01-visual-asset-table-creation`: the worker must restate which evidence is durable, which evidence is synthetic, which evidence is missing, and which reviewer would be responsible for closing the missing proof. This keeps the dispatch useful even when the later run cannot access every upstream file.

[claim]
[detail] Additional guard for `MOD-VISUAL-01-visual-asset-table-creation`: the worker must restate which evidence is durable, which evidence is synthetic, which evidence is missing, and which reviewer would be responsible for closing the missing proof. This keeps the dispatch useful even when the later run cannot access every upstream file.
