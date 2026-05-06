---
title: Audit packet generator candidate
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-GLOBAL-06
---

# Audit packet generator candidate

## objective

- Define the minimum packet a later tool or script should assemble for cloud or sidecar audit.
- Keep the packet evidence-first and avoid dragging local-only artifacts into tracked truth.

## packet_inputs

| input | required | note |
|---|---|---|
| merged PR numbers | yes | source of diff truth |
| final run report | yes | human-readable slot receipts |
| checkpoint final json | yes | machine-readable run cursor |
| diff bundle | yes | cross-PR consistency audit surface |
| supporting candidate docs | optional | include only if cited by report |

## packet_outputs

| output | purpose |
|---|---|
| `audit-index.md` | tells the auditor what to read first |
| `pr-table.csv` | quick PR/branch/status matrix |
| `claim-map.md` | maps each major claim to a file or PR |
| `blocked-lanes.md` | re-states what stayed blocked |

## reject_conditions

- includes secrets, cookies, or auth sidecars
- includes raw stdout/stderr dumps that are not redacted
- labels candidate docs as authority truth
- omits final merged PR numbers while claiming completion

## verdict

- `T-PASS` for packet design only; no generator is implemented here.
