---
title: ScoutFlow PR Factory Orchestration Shoulder Probe Batch
date: 2026-05-05
type: shoulder-probe-batch
status: candidate / research-only / not-authority / not-runtime-approval
wave: 3B
related_task: T-P1A-056
---

# ScoutFlow PR Factory Orchestration Shoulder Probe Batch

## Scope

- This dispatch probes one shoulder only: the local PR Factory helper/orchestration pattern already landed as a tooling candidate.
- The report extracts orchestration value from the plan, the CLI helper, the containment tests, and the surge workflow mapping.
- This report does not approve merge automation, authority writes, or any expansion into `services/**`, `apps/**`, `workers/**`, `packages/**`, or runtime logic.

## Inputs

- The tooling plan already narrowed the original multi-file shell idea into one architecture doc plus one single-file Python helper, with dry-run, `.git` suffix stripping, and resolved containment as the core safety goals ([docs/architecture/pr-factory-tooling-plan-2026-05-04.md:L20-L39](docs/architecture/pr-factory-tooling-plan-2026-05-04.md), [docs/architecture/pr-factory-tooling-plan-2026-05-04.md:L43-L64](docs/architecture/pr-factory-tooling-plan-2026-05-04.md)).
- The helper itself encodes local-only layout checks, path-segment validation, referencerepo containment, and dry-run-first execution semantics ([tools/scoutflow_pr_factory.py:L15-L18](tools/scoutflow_pr_factory.py:L15-L18), [tools/scoutflow_pr_factory.py:L38-L58](tools/scoutflow_pr_factory.py:L38-L58), [tools/scoutflow_pr_factory.py:L65-L80](tools/scoutflow_pr_factory.py:L65-L80), [tools/scoutflow_pr_factory.py:L97-L119](tools/scoutflow_pr_factory.py:L97-L119)).
- The test suite proves the critical negative cases: no path escapes, no root-level sync target, and `--execute` remains opt-in ([tests/tools/test_scoutflow_pr_factory.py:L45-L72](tests/tools/test_scoutflow_pr_factory.py:L45-L72), [tests/tools/test_scoutflow_pr_factory.py:L117-L135](tests/tools/test_scoutflow_pr_factory.py:L117-L135), [tests/tools/test_scoutflow_pr_factory.py:L162-L171](tests/tools/test_scoutflow_pr_factory.py:L162-L171), [tests/tools/test_scoutflow_pr_factory.py:L194-L217](tests/tools/test_scoutflow_pr_factory.py:L194-L217)).
- The surge protocol candidate already places this helper inside a wider 7-step PR Factory flow and explicitly denies it any authority over dispatch definition, PR publication policy, or merge verdicts ([docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md:L181-L206](docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md), [docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md:L210-L218](docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md)).

## Batch verdict

| shoulder | decision | integration proposal | confidence | next_action |
|---|---|---|---:|---|
| `PR-FACTORY / local helper candidate` | continue | `reference_only -> local helper for shoulder lifecycle only` | 0.84 | keep dry-run-first, local-only orchestration guardrails |

## Probe findings

### shoulder PR-FACTORY / local helper candidate

Decision: keep the PR Factory helper as a `reference_only` orchestration shoulder for local-only lifecycle actions, but do not let it expand into authority, merge, or runtime automation.

Why:

- The tooling plan is already explicit that V1 only covers local-only shoulder mechanics and refuses to touch authority surfaces or product code; that boundary is part of the value, not a temporary omission ([docs/architecture/pr-factory-tooling-plan-2026-05-04.md:L57-L64](docs/architecture/pr-factory-tooling-plan-2026-05-04.md), [docs/architecture/pr-factory-tooling-plan-2026-05-04.md:L132-L174](docs/architecture/pr-factory-tooling-plan-2026-05-04.md)).
- The CLI helper itself enforces the right orchestration discipline: repository layout check, `referencerepo/` local-only guard, single-segment path validation, resolved containment, and explicit dry-run/execute split ([tools/scoutflow_pr_factory.py:L38-L45](tools/scoutflow_pr_factory.py:L38-L45), [tools/scoutflow_pr_factory.py:L48-L58](tools/scoutflow_pr_factory.py:L48-L58), [tools/scoutflow_pr_factory.py:L65-L80](tools/scoutflow_pr_factory.py:L65-L80), [tools/scoutflow_pr_factory.py:L220-L234](tools/scoutflow_pr_factory.py:L220-L234)).
- The tests prove the tool is defending the exact failure modes that matter most here: `../docs` escapes, `/tmp` escapes, bare `referencerepo` root misuse, and accidental execution when the user only wanted a plan ([tests/tools/test_scoutflow_pr_factory.py:L58-L72](tests/tools/test_scoutflow_pr_factory.py:L58-L72), [tests/tools/test_scoutflow_pr_factory.py:L117-L135](tests/tools/test_scoutflow_pr_factory.py:L117-L135), [tests/tools/test_scoutflow_pr_factory.py:L162-L171](tests/tools/test_scoutflow_pr_factory.py:L162-L171), [tests/tools/test_scoutflow_pr_factory.py:L174-L217](tests/tools/test_scoutflow_pr_factory.py:L174-L217)).
- The surge protocol keeps the tool in the right place in the larger orchestration story: helper for worker execution and self-validation, not for dispatch authority, PR creation policy, audit verdicts, or merge control ([docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md:L185-L206](docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md), [docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md:L210-L218](docs/architecture/pr-factory-surge-protocol-candidate-2026-05-04.md)).

Carry-forward:

- keep dry-run-first as a hard orchestration default
- keep all side effects under `referencerepo/**` local-only boundaries
- keep authority, audit, and merge decisions outside the helper
- keep the helper as shoulder-lifecycle tooling, not as a general PR robot

## Result

This batch keeps the PR Factory conclusion narrow and useful:

- the helper is worth carrying forward
- its value is disciplined local-only orchestration
- it should not mutate into an authority or merge engine
