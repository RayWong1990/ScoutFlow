---
title: ScoutFlow Obsidian and Vault Shoulder Probe Batch
date: 2026-05-05
type: shoulder-probe-batch
status: candidate / research-only / not-authority / not-runtime-approval
wave: 3B
related_task: T-P1A-054
---

# ScoutFlow Obsidian and Vault Shoulder Probe Batch

## Scope

- This dispatch narrows the vault-facing shoulder lane to the existing PARA / Obsidian boundary already scanned and locked in ADR form.
- The goal is to restate the usable vault contract for later bridge/vault work without approving any write runtime.
- This report does not create a new vault, does not write `00-Inbox/`, and does not widen ScoutFlow into a knowledge-base manager.

## Inputs

- The frontmatter scan already established that the user vault is an existing PARA tree, that `System/frontmatter-templates.md` is the single source of truth, and that ScoutFlow's raw export contract should stay on the 4-field template ([docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md:L19-L27](docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md), [docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md:L29-L55](docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md)).
- The same scan narrowed the future write path to `${SCOUTFLOW_VAULT_ROOT}/00-Inbox/` and rejected direct writes into `01-Wiki/`, `02-Raw/`, or `System/**` ([docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md:L138-L156](docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md)).
- ADR-001 already locked the PARA boundary, the `00-Inbox/` entrypoint, and the rule that ScoutFlow must not rebuild a second vault or second intake chain ([docs/architecture/ADR-001-obsidian-para-lock-2026-05-04.md:L23-L39](docs/architecture/ADR-001-obsidian-para-lock-2026-05-04.md), [docs/architecture/ADR-001-obsidian-para-lock-2026-05-04.md:L57-L63](docs/architecture/ADR-001-obsidian-para-lock-2026-05-04.md)).
- The baseline roadmap and contracts index keep `SCOUTFLOW_VAULT_ROOT` as a candidate default at PRD level but a fail-loud requirement for SRD/spec/implementation layers ([docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md:L178-L181](docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md), [docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md:L209-L209](docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md), [docs/specs/contracts-index.md:L45-L45](docs/specs/contracts-index.md)).

## Batch verdict

| shoulder | decision | integration proposal | confidence | next_action |
|---|---|---|---:|---|
| `OBSIDIAN / existing PARA vault` | continue | `reference_only -> bridge/vault spec input only` | 0.86 | keep `00-Inbox + raw 4-field + fail-loud env` locked |

## Probe findings

### shoulder OBSIDIAN / existing PARA vault

Decision: keep the existing PARA / Obsidian vault as a locked reference boundary and future bridge target, but do not treat it as an approved runtime surface yet.

Why:

- The scan already proved ScoutFlow does not need a new vault and must instead reuse the existing PARA tree with `00-Inbox` as the entrypoint ([docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md:L19-L27](docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md), [docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md:L138-L156](docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md)).
- The raw export contract is already narrow and stable: `title`, `date`, `tags`, `status`, with `tags: 调研/ScoutFlow采集` and `status: pending`, and the scan explicitly rejects early smuggling of wiki-only fields into raw export ([docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md:L31-L55](docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md), [docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md:L195-L200](docs/research/shoulders/obsidian-frontmatter-compat-scan-2026-05-04.md)).
- ADR-001 formalizes the same boundary: ScoutFlow writes only to `${SCOUTFLOW_VAULT_ROOT}/00-Inbox/`, does not rebuild `/intake` or `/compile`, and keeps its own cockpit under `05-Projects/ScoutFlow/` instead of inventing a second vault structure ([docs/architecture/ADR-001-obsidian-para-lock-2026-05-04.md:L25-L39](docs/architecture/ADR-001-obsidian-para-lock-2026-05-04.md), [docs/architecture/ADR-001-obsidian-para-lock-2026-05-04.md:L49-L55](docs/architecture/ADR-001-obsidian-para-lock-2026-05-04.md)).
- The roadmap and contracts index keep one more engineering guard visible: PRD may mention `~/workspace/raw` as a candidate default, but SRD/spec/implementation must fail loud if `SCOUTFLOW_VAULT_ROOT` is unset, so later bridge/vault work cannot silently drift into an accidental path ([docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md:L178-L181](docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md), [docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md:L209-L209](docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md), [docs/specs/contracts-index.md:L45-L45](docs/specs/contracts-index.md)).

Carry-forward:

- keep `00-Inbox` as the only allowed future write entrypoint
- keep raw export on the 4-field frontmatter template
- keep `SCOUTFLOW_VAULT_ROOT` fail-loud at spec/implementation level
- do not approve vault runtime from this report alone

## Result

This batch keeps the vault conclusion tight and reusable:

- existing PARA / Obsidian vault remains the reference shoulder
- ScoutFlow stays a capture-to-inbox bridge, not a vault manager
- the future bridge/vault lane already has a stable contract shape, but not runtime approval
