---
title: PRD v2.1 Strong Visual H5 PARA PR Factory Addendum
status: amendment / promoted
task_id: T-P1A-033
promotion_task_id: T-P1A-103
pr_number: PR #58
candidate: false
not_authority: false
promotion_basis: user_override_for_B2_preflight
not_runtime_approval: true
not_frontend_implementation_approval: true
walking_skeleton_evidence: future_gated
base_prd: docs/PRD-v2-2026-05-04.md
sunset_trigger: Deprecated when equivalent sections are absorbed into PRD-v3 or a later promoted base PRD after future implementation evidence is reviewed.
related_inputs:
  - docs/research/pr55-pr74-worklist-candidate-2026-05-04.md
  - docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md
  - docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md
  - docs/research/doc1-doc2-doc3-v1.1-acceptance-errata-report-2026-05-04.md
  - docs/research/opus-v3-acceptance-prd-srd-amendment-roadmap-review-2026-05-04.md
  - /Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/REPORT-Wave4-Batch1-Dispatch76-90-CODEX0-2026-05-05.md
---

> Status: `promoted addendum / not runtime approval / not frontend implementation approval`.
> Promotion basis: `user_override_for_B2_preflight` recorded by `T-P1A-103`. This addendum extends `docs/PRD-v2-2026-05-04.md` for B2 planning and contract baseline while leaving the base file unchanged.

This file narrows the accepted product direction for the next wave of B2 planning work:

- strong visual happens at capture time in an H5 surface, not inside wiki reading surfaces
- the existing PARA / Claudian vault remains the downstream knowledge system
- fixed shoulders are recorded as product choices or candidates, not as runtime approval
- PR factory surge remains candidate-only until protocol and closeout gates promote it

## §X.1 Strong Visual Capture H5

ScoutFlow's strong visual product surface is a local H5 Capture Station used during capture and scope confirmation. It is not a second authority layer, and it is not a wiki rendering project.

Product intent:

- make the capture moment legible enough for a single operator to judge scope, evidence, and blocked gates in one screen
- keep product feedback close to the existing API and trust-trace surfaces instead of inventing a parallel dashboard truth
- show approved and blocked states explicitly so later runtime layers are not visually implied before approval

The candidate H5 is a four-panel surface:

1. `URL Bar`: manual URL paste and bounded capture action
2. `Live Metadata`: title, uploader, duration, page count, and probe feedback
3. `Capture Scope`: current allowed preset plus greyed blocked layers
4. `Trust Trace Graph`: capture/state/job/probe/receipt/media/audit projection

The H5 role is intentionally narrow:

- `projection surface`: show state, evidence, and gates clearly
- `operation surface`: receive manual URL input and bounded actions
- `not authority`: SQLite + FS + state words remain the authority source of truth
- `not approval`: candidate stack or screen layout language here does not unlock frontend implementation

Current candidate interaction model:

```text
manual_url_entered
  -> metadata_probe_requested
  -> metadata_visible
  -> scope_confirmed_or_blocked
  -> future_commit_gate
```

Transition gates:

- `manual_url_entered -> metadata_probe_requested`: only for approved manual URL entry
- `metadata_probe_requested -> metadata_visible`: only after allowed metadata probe evidence exists
- `metadata_visible -> scope_confirmed_or_blocked`: only after Capture Scope rules are rendered explicitly
- `scope_confirmed_or_blocked -> future_commit_gate`: only as a future gated capability, not enabled by this amendment

Visual acceptance remains candidate but explicit: every H5-facing PR should be judged with the five-check visual gate referenced in `~/.claude/rules/aesthetic-first-principles.md`, especially visual hierarchy, space/alignment, occlusion safety, readability, and visual weight. A technical render pass is not a visual pass.

## §X.2 Existing PARA / Claudian Vault Integration

ScoutFlow reuses the user's existing PARA / Claudian vault instead of creating a second knowledge base. At the product level, the recommended default root is `${SCOUTFLOW_VAULT_ROOT:-~/workspace/raw}`. This recommendation is product guidance only; implementation-level fail-loud behavior belongs to later SRD and runtime work.

Product boundary:

- ScoutFlow only writes candidate output to `00-Inbox/`
- ScoutFlow does not write directly into `02-Raw/`, `01-Wiki/`, `03-Output/`, or `System/`
- ScoutFlow does not replace `/intake`, `/compile`, `/enrich`, `/query`, or `/lint`
- ScoutFlow does not redefine Obsidian as the capture UI; Obsidian remains the downstream knowledge environment

Required vault discipline:

- downstream markdown must follow the raw four-field template from `System/frontmatter-templates.md`
- ScoutFlow project coordination inside `${SCOUTFLOW_VAULT_ROOT}/05-Projects/ScoutFlow/` is a mirror or handoff surface, not repo authority
- changes to vault taxonomy, domain maps, or intake rules are outside this amendment

This amendment therefore adds a product integration boundary, not a storage implementation promise. The base PRD remains the authority source for current enforced product scope, and `docs/PRD-v2-2026-05-04.md` stays unchanged.

## §X.3 Fixed Product Shoulders

The following shoulders are accepted here as fixed product direction or bounded candidate direction. They are not equivalent to runtime approval, dependency freeze, or implementation-ready integration.

| Surface | Product role | Current status in this amendment |
|---|---|---|
| `BBDown` | primary Bilibili capture shoulder | locked product direction for bounded metadata/media capture discussions; runtime still separately gated |
| `Whisper family` | local ASR direction | fixed direction family; exact implementation benchmark and route remain open |
| `Obsidian PARA vault` | downstream knowledge base | fixed product output destination family |
| `OpenDesign` | visual reference source | repo-external visual probe candidate only |
| `Vite + React + shadcn + TanStack + React Flow` | H5 stack family | candidate stack family only; version lock and package decisions deferred |

Interpretation rules:

- fixed product shoulder means "this is the direction the product describes"
- it does not mean "already approved to run in repo"
- it does not mean "already integrated into code"
- it does not mean "promoted into contracts-index as enforced contract"

OpenDesign stays especially narrow: it is a repo-external reference and prototype source for H5 visual quality, not a declared runtime dependency, not a source drop into ScoutFlow, and not authority for product behavior.

## §X.4 PR Factory Product Operating Mode

ScoutFlow remains a single-operator system coordinated through bounded PRs, explicit file domains, and one authority writer at a time.

Enforced baseline today:

- `product lane max = 3`
- `authority writer max = 1`
- research lanes do not count against product lanes unless they write authority
- prototype lanes do not count against product lanes unless they write authority
- each PR must keep a small file domain, clear acceptance, and explicit validation

Candidate surge model, not yet promoted:

- product lanes may increase from `3` to `5`
- research lanes may scale as advisory capacity
- prototype lanes may scale as advisory capacity
- authority writer remains `1`

Promotion conditions for any surge mode:

1. protocol amendment lands with explicit wording and file-domain discipline
2. closeout confirms the candidate does not conflict with current enforced caps
3. the user explicitly gates promotion after wave evidence is reviewed

This section is a product-operating amendment, not a workflow override. Until later promotion, the enforced baseline in the current repo documents continues to win over this candidate.

## §X.5 Out of scope

This amendment does not expand ScoutFlow into a broader platform or a second operating system around the vault.

Out of scope in this candidate:

- SaaS or multi-user collaboration features
- Electron packaging or desktop-shell duplication of the H5 surface
- additional security-signing or supply-chain ceremony layers beyond the current single-user local-first baseline
- automatic unlock of BBDown live runtime, media download, ffmpeg, ASR, browser automation, or `audio_transcript`
- changing `docs/PRD-v2-2026-05-04.md` directly
- changing downstream vault taxonomy, frontmatter ownership, or project authority location

Also out of scope:

- claiming OpenDesign as an approved dependency
- claiming the H5 stack family is implementation-locked
- claiming surge parallelism is already enforced
- treating any mirror under `05-Projects/ScoutFlow/` as a replacement for repo authority

## §X.6 Promotion basis and future evidence gates

This addendum is promoted by user override for B2 preflight, not by claiming that the old walking-skeleton criteria already happened.

Promotion basis:

1. Wave 3A and Wave 3B closeout records landed on main.
2. Wave 4 B1 PR body/diff layer reached `verdict=clear`.
3. RAW control-plane defects were repaired by `T-P1A-103`.
4. User authorized `user_override_for_B2_preflight` for this PRD-v2.1 addendum.

Future evidence gates:

1. a future walking skeleton must still prove the H5 surface, API boundary, and downstream vault boundary cohere at a minimal end-to-end level
2. the H5 direction must still pass the five-check visual gate in that future review
3. no base PRD authority drift may be introduced during implementation
4. frontend implementation remains separately gated
5. runtime and media-tool execution remain separately gated

State machine:

```text
promoted_addendum_for_b2_preflight
  -> b2_commander_ready
  -> future_walking_skeleton_dispatch
  -> future_visual_gate_review
  -> future_runtime_or_frontend_gate
```

Interpretation:

- `promoted_addendum_for_b2_preflight` means B2 planning may use this product direction.
- It does not mean a walking skeleton exists.
- It does not unlock frontend implementation, BBDown live runtime, media download, ffmpeg, ASR, browser automation, or `audio_transcript`.
- If later authority text supersedes these sections, this file becomes deprecated per `sunset_trigger`.
