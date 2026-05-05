---
title: Backbone Taxonomy
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-05
scope: STEP2 item 2B-5 backbone contract for Cloud ChatGPT Pro Dispatch127-176 draft generation
related_files:
  - docs/research/repairs/dispatch127-176-pack-design-v3-2026-05-05.md
  - docs/research/repairs/wave5-scope-and-template-extraction-2026-05-05.md
  - docs/research/repairs/readback-manifest-2026-05-05.md
---

# Backbone Taxonomy

> State: candidate / not authority / not execution approval / not runtime approval / not migration approval.
> This file is the bounded input contract for Cloud ChatGPT Pro. It is not a dispatch pack, not a merged implementation plan, and not a runtime unlock.

## 1. Backbone Rules

- every row must carry `contract_source`
- if `contract_source=inference`, then `inference_from` and `risk_flag=tentative` are required
- `DB vNext` stays context/overflow by default and does not drive early rows
- no row may imply `BBDown live`, `audio_transcript`, migration approval, or vault true-write approval
- rows `127-130` are Wave 4 continuation / closeout oriented
- rows `131-176` are Wave 5 candidate-oriented

## 2. Slot Table

| slot | task_id | title | lane | wave_hint | expected_diff_shape | contract_source | inference_from | risk_flag | visual_touchpoint_for_user |
|---|---|---|---|---|---|---|---|---|---|
| 127 | T-P1A-106 | Wave 4 post-mid-checkpoint continuation map | authority | 4-final | authority | batch1 worklist §50/§55 | — | normal | no |
| 128 | T-P1A-107 | Wave 4 visual touchpoint roster and localhost plan | research | 4-final | docs-only | promoted_addendum: SRD v3 H5/Bridge §17.1 | — | normal | yes |
| 129 | T-P1A-108 | Wave 4 bridge-vault continuation gap matrix | spec | 4-final | docs-only | promoted_addendum: SRD v3 H5/Bridge §17.2-§17.3 | — | normal | no |
| 130 | T-P1A-109 | Wave 4 closeout and Wave 5 opening candidate | authority | 4-final | authority | canonical: PRD v2 §9.1-§9.2 | — | normal | no |
| 131 | T-P1A-110 | Signal entity glossary candidate | docs | 5-frozen | docs-only | canonical: PRD v2 §4.3 | — | normal | no |
| 132 | T-P1A-111 | Signal state map candidate | spec | 5-frozen | docs-only | canonical: SRD v2 §2.7 | — | normal | no |
| 133 | T-P1A-112 | Hypothesis lifecycle candidate | docs | 5-frozen | docs-only | canonical: PRD v2 §4.3 | — | normal | no |
| 134 | T-P1A-113 | Capture plan entity surface candidate | docs | 5-frozen | docs-only | canonical: PRD v2 §4.3 | — | normal | no |
| 135 | T-P1A-114 | Topic card entity surface candidate | docs | 5-frozen | docs-only | canonical: SRD v2 §2.7 | — | normal | no |
| 136 | T-P1A-115 | Signal workbench boundary note | spec | 5-frozen | docs-only | canonical: PRD v2 §7.2 | — | normal | no |
| 137 | T-P1A-116 | Manual-url continuity constraints for Wave 5 | docs | 5-frozen | docs-only | canonical: PRD v2 §5.2 | — | normal | no |
| 138 | T-P1A-117 | Trust-trace to topic-card mapping candidate | docs | 5-frozen | docs-only | inference | canonical: PRD v2 §5.2 + SRD v2 §3.2-§3.4 | tentative | no |
| 139 | T-P1A-118 | Metadata evidence normalization continuation | spec | 5-frozen | docs-only | canonical: SRD v2 §3.2-§3.4 | — | normal | no |
| 140 | T-P1A-119 | H5 panel to signal-hypothesis mapping | docs | 5-frozen | docs-only | promoted_addendum: SRD v3 H5/Bridge §17.1 | — | normal | yes |
| 141 | T-P1A-120 | Topic card review flow candidate | docs | 5-frozen | docs-only | inference | canonical: PRD v2 §4.3 + §9.1-§9.2 | tentative | no |
| 142 | T-P1A-121 | Capture plan input-output contract candidate | spec | 5-frozen | docs-only | canonical: SRD v2 §2.7 | — | normal | no |
| 143 | T-P1A-122 | Signal scoring vocabulary candidate | docs | 5-tentative | docs-only | inference | canonical: PRD v2 §4.3 | tentative | no |
| 144 | T-P1A-123 | Hypothesis evidence-source matrix | docs | 5-tentative | docs-only | inference | canonical: PRD v2 §5.2 + SRD v2 §3.2-§3.4 | tentative | no |
| 145 | T-P1A-124 | Topic card vault rendering candidate | product | 5-tentative | bounded-code | promoted_addendum: SRD v3 H5/Bridge §17.3 | — | tentative | yes |
| 146 | T-P1A-125 | Topic card preview shape candidate | product | 5-tentative | bounded-code | promoted_addendum: SRD v3 H5/Bridge §17.3 | — | tentative | yes |
| 147 | T-P1A-126 | Capture plan dry-run note shape | docs | 5-tentative | docs-only | promoted_addendum: SRD v3 H5/Bridge §17.3 | — | tentative | no |
| 148 | T-P1A-127 | Wave 5 docs-pack PR factory packaging | docs | 5-tentative | docs-only | promoted_addendum: PRD v2.1 §X.4 | — | tentative | no |
| 149 | T-P1A-128 | Wave 5 file-domain matrix draft | spec | 5-tentative | docs-only | batch1 worklist §51 | — | normal | no |
| 150 | T-P1A-129 | Wave 5 dependency graph draft | spec | 5-tentative | docs-only | batch1 worklist §52-§54 | — | normal | no |
| 151 | T-P1A-130 | Signal workbench API placeholder contract | spec | 5-tentative | docs-only | canonical: SRD v2 §4.1-§4.3 | — | tentative | no |
| 152 | T-P1A-131 | Topic card frontend IA candidate | docs | 5-tentative | docs-only | promoted_addendum: PRD v2.1 §X.1 | — | tentative | yes |
| 153 | T-P1A-132 | Capture plan frontend IA candidate | docs | 5-tentative | docs-only | promoted_addendum: PRD v2.1 §X.1 | — | tentative | yes |
| 154 | T-P1A-133 | Hypothesis comparison UX candidate | docs | 5-tentative | docs-only | inference | promoted_addendum: PRD v2.1 §X.1 | tentative | yes |
| 155 | T-P1A-134 | Signal ingestion audit lane candidate | audit | 5-tentative | docs-only | inference | canonical: PRD v2 §5.2 | tentative | no |
| 156 | T-P1A-135 | Wave 5 visual reporting candidate | docs | 5-tentative | docs-only | batch1 worklist §55 | — | tentative | yes |
| 157 | T-P1A-136 | Localhost review roster for Wave 5 surfaces | docs | 5-tentative | docs-only | promoted_addendum: SRD v3 H5/Bridge §17.1 + V3 visual pipeline | — | normal | yes |
| 158 | T-P1A-137 | STEP3 commander prompt contract note | docs | 5-tentative | docs-only | promoted_addendum: PRD v2.1 §X.4 + SRD v3 H5/Bridge §17.4 | — | normal | no |
| 159 | T-P1A-138 | Cloud draft resume and packaging rules | docs | 5-tentative | docs-only | batch1 worklist §54 + V3 cloud prompt structure | — | normal | no |
| 160 | T-P1A-139 | Readback delta application rules | docs | 5-tentative | docs-only | inference | V3 readback + batch2 summary | tentative | no |
| 161 | T-P1A-140 | Deferred and overflow registry candidate | docs | 5-tentative | docs-only | batch1 worklist §53 | — | normal | no |
| 162 | T-P1A-141 | Bridge hardening post-110 continuation | spec | 5-tentative | docs-only | promoted_addendum: SRD v3 H5/Bridge §17.2 | — | tentative | no |
| 163 | T-P1A-142 | Vault preview continuation candidate | spec | 5-tentative | docs-only | promoted_addendum: SRD v3 H5/Bridge §17.3 | — | tentative | no |
| 164 | T-P1A-143 | Vault dry-run continuation candidate | spec | 5-tentative | docs-only | promoted_addendum: SRD v3 H5/Bridge §17.3 | — | tentative | no |
| 165 | T-P1A-144 | 5 Gate CI continuation note | docs | 5-tentative | docs-only | batch1 worklist §53 + §55 | — | normal | no |
| 166 | T-P1A-145 | Playwright smoke extension candidate | docs | 5-tentative | docs-only | batch1 worklist §53 | — | tentative | yes |
| 167 | T-P1A-146 | Visual regression reporting continuation | docs | 5-tentative | docs-only | batch1 worklist §55 | — | tentative | yes |
| 168 | T-P1A-147 | Runtime-log schema for Dispatch127-176 run | docs | 5-tentative | docs-only | inference | V3 runtime-log model | normal | no |
| 169 | T-P1A-148 | RUN-SUMMARY schema for Dispatch127-176 run | docs | 5-tentative | docs-only | inference | V3 closeout and runtime-log model | normal | no |
| 170 | T-P1A-149 | Product-lane override evidence packet | docs | 5-tentative | docs-only | promoted_addendum: PRD v2.1 §X.4 | — | tentative | no |
| 171 | T-P1A-150 | Global pool staging health-check contract | docs | 5-tentative | docs-only | inference | V3 staged rollout + STEP2A 2A-6 note | normal | no |
| 172 | T-P1A-151 | Branch protection and merge policy note | docs | 5-tentative | docs-only | inference | STEP2A 2A-6 note | normal | no |
| 173 | T-P1A-152 | Wave 5 closeout template | authority | 5-tentative | authority | batch1 worklist §53/§55 | — | tentative | no |
| 174 | T-P1A-153 | Wave 6 ledger-open candidate | authority | 5-tentative | authority | canonical: PRD v2 §9.1-§9.2 | — | tentative | no |
| 175 | T-P1A-154 | Overflow candidate registry for DB vNext and blocked runtime lanes | docs | 5-tentative | docs-only | candidate_context: DB vNext + batch1 blocked lanes | — | tentative | no |
| 176 | T-P1A-155 | STEP3 cold-start handoff packet contract | docs | 5-tentative | docs-only | inference | V3 single prompt goal + STEP2 inventory/readback | normal | no |

## 3. Notes

- Rows with `tentative` risk are allowed, but they must later preserve that marking in cloud generation.
- The backbone intentionally avoids making `DB vNext` the default driver of early slots.
- The backbone intentionally treats post-110 continuation as docs/spec/candidate-heavy rather than as implicit runtime approval.

## 4. Overflow Candidates Reserved For Wave 6

These are not part of the 50-slot table above and should stay outside default Cloud Draft Gate unless the user later overrides:

- DB vNext DDL-first docs pack
- BBDown live runtime candidate chain
- `audio_transcript` unlock exploration
- migration dry-run plan and schema change line

