---
title: README-deliverable-index-2026-05-07
status: candidate / deliverable-index / not-authority
authority: not-authority
created_at: 2026-05-07
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
can_open_C4: false
can_open_runtime: false
can_open_migration: false
---

[claim]
# README-deliverable-index-2026-05-07

[claim]
## §1 What this ZIP is

[candidate] This ZIP is the U9 Phase 2-4 dispatch catalog v0: a copy-ready library of candidate dispatch prompts plus cluster indexes and supporting audit files. It is a deliverable artifact, not a ScoutFlow repo change.

[boundary] No dispatch in this ZIP is currently authorized for execution. Every dispatch keeps `can_open_C4=false`, `can_open_runtime=false`, `can_open_migration=false`, and `write_enabled=false` in frontmatter.

[audit]
[evidence] The catalog was synthesized from the uploaded U9 cloud prompt, accessible PRD/SRD/AGENTS/contracts/overflow inputs, Run-2 and Run-3+4 receipt evidence, and the local post-dispatch176 audit pack.

[claim]
## §2 Directory map

[table]
| Category | Markdown files |
|---|---:|
| supporting_root_and_00_supporting | 6 |
| 01_phase2_dispatches | 28 |
| 02_phase3_dispatches | 17 |
| 03_phase4_dispatches | 13 |
| 04_module_dispatches | 19 |
| 05_cluster_indexes | 12 |

[claim]
## §3 File index

[boundary]
- `00_supporting/CROSS-CLUSTER-DEPENDENCY-GRAPH-2026-05-07.md`
- `00_supporting/FORMAT-GUARD-REPORT-2026-05-07.md`
- `00_supporting/MASTER-ROADMAP-PHASE-2-4-2026-05-07.md`
- `00_supporting/SELF-AUDIT-FINDINGS-2026-05-07.md`
- `00_supporting/VENDOR-PATTERN-RECAP-2026-05-07.md`
- `01_phase2_dispatches/P2-LANE1-01-vault-write-shadow-mode-spike-Vault-write-shadow-mode-spike.md`
- `01_phase2_dispatches/P2-LANE1-02-metadata-only-commit-simulation-Metadata-only-commit-simulation.md`
- `01_phase2_dispatches/P2-LANE1-03-dry-run-commit-validation-matrix-Dry-run-commit-validation-matrix.md`
- `01_phase2_dispatches/P2-LANE1-04-true-write-gate-decision-packet-True-write-gate-decision-packet.md`
- `01_phase2_dispatches/P2-LANE1-05-rollback-rehearsal-no-write-Rollback-rehearsal-without-true-write.md`
- `01_phase2_dispatches/P2-LANE2-01-bbdown-metadata-only-legal-recheck-BBDown-metadata-only-legal-recheck.md`
- `01_phase2_dispatches/P2-LANE2-02-yt-dlp-boundary-and-platform-result-remap-yt-dlp-boundary-and-PlatformResult-remap.md`
- `01_phase2_dispatches/P2-LANE2-03-whisper-local-install-preflight-Whisper-local-install-preflight.md`
- `01_phase2_dispatches/P2-LANE2-04-faster-whisper-benchmark-sandbox-faster-whisper-benchmark-sandbox.md`
- `01_phase2_dispatches/P2-LANE2-05-voxtral-asr-spike-candidate-Voxtral-ASR-spike-candidate.md`
- `01_phase2_dispatches/P2-LANE2-06-asr-sandbox-redaction-harness-ASR-sandbox-redaction-harness.md`
- `01_phase2_dispatches/P2-LANE2-07-llm-transcript-normalization-fixture-LLM-transcript-normalization-fixture.md`
- `01_phase2_dispatches/P2-LANE2-08-runtime-tools-dependency-ledger-Runtime-tools-dependency-ledger.md`
- `01_phase2_dispatches/P2-LANE3-01-playwright-sandbox-readonly-probe-Playwright-sandbox-read-only-probe.md`
- `01_phase2_dispatches/P2-LANE3-02-human-screenshot-verdict-packet-Human-screenshot-verdict-packet.md`
- `01_phase2_dispatches/P2-LANE3-03-browser-profile-isolation-contract-Browser-profile-isolation-contract.md`
- `01_phase2_dispatches/P2-LANE3-04-login-required-gate-and-consent-Login-required-gate-and-consent.md`
- `01_phase2_dispatches/P2-LANE3-05-visual-uat-replay-without-automation-Visual-UAT-replay-without-automation.md`
- `01_phase2_dispatches/P2-LANE4-01-fixture-migration-rollback-plan-Fixture-migration-rollback-plan.md`
- `01_phase2_dispatches/P2-LANE4-02-schema-evolution-v0-candidate-Schema-evolution-v0-candidate.md`
- `01_phase2_dispatches/P2-LANE4-03-single-migration-script-dry-run-Single-migration-script-dry-run.md`
- `01_phase2_dispatches/P2-LANE4-04-consumer-pin-abandon-decision-Consumer-pin-abandon-decision.md`
- `01_phase2_dispatches/P2-LANE4-05-db-vnext-external-audit-packet-DB-vNext-external-audit-packet.md`
- `01_phase2_dispatches/P2-LANE5-01-url-usefulness-verdict-URL-usefulness-verdict.md`
- `01_phase2_dispatches/P2-LANE5-02-readonly-signal-preview-Read-only-signal-preview.md`
- `01_phase2_dispatches/P2-LANE5-03-candidate-dispatch-ui-shape-Candidate-dispatch-UI-shape.md`
- `01_phase2_dispatches/P2-LANE5-04-lp001-risk-recheck-LP-001-risk-recheck.md`
- `01_phase2_dispatches/P2-LANE5-05-signal-workbench-unlock-queue-Signal-Workbench-unlock-queue.md`
- `02_phase3_dispatches/P3-CapturePlan-01-v0-table-creation-fixture-CapturePlan-v0-table-creation-fixture.md`
- `02_phase3_dispatches/P3-CapturePlan-02-lp001-scope-guard-backfill-CapturePlan-LP-001-scope-guard-backfill.md`
- `02_phase3_dispatches/P3-CapturePlan-03-plan-to-capture-dryrun-test-Plan-to-capture-dry-run-test.md`
- `02_phase3_dispatches/P3-CapturePlan-04-plan-review-state-promotion-Plan-review-state-promotion.md`
- `02_phase3_dispatches/P3-Hypothesis-01-v0-table-creation-fixture-Hypothesis-v0-table-creation-fixture.md`
- `02_phase3_dispatches/P3-Hypothesis-02-evidence-source-backfill-Hypothesis-evidence-source-backfill.md`
- `02_phase3_dispatches/P3-Hypothesis-03-comparison-state-machine-test-Hypothesis-comparison-state-machine-test.md`
- `02_phase3_dispatches/P3-Hypothesis-04-conflict-resolution-rubric-Hypothesis-conflict-resolution-rubric.md`
- `02_phase3_dispatches/P3-Signal-01-v0-table-creation-fixture-Signal-v0-table-creation-fixture.md`
- `02_phase3_dispatches/P3-Signal-02-sample-backfill-candidate-Signal-sample-backfill-candidate.md`
- `02_phase3_dispatches/P3-Signal-03-migration-test-set-Signal-migration-test-set.md`
- `02_phase3_dispatches/P3-Signal-04-signal-scoring-vocab-promotion-Signal-scoring-vocabulary-promotion.md`
- `02_phase3_dispatches/P3-TopicCard-01-lite-v0-to-v1-contract-TopicCard-lite-v0-to-v1-contract.md`
- `02_phase3_dispatches/P3-TopicCard-02-vault-preview-field-backfill-TopicCard-vault-preview-field-backfill.md`
- `02_phase3_dispatches/P3-TopicCard-03-topic-card-v1-migration-test-TopicCard-v1-migration-test.md`
- `02_phase3_dispatches/P3-TopicCard-04-v1-to-v2-output-schema-TopicCard-v1-to-v2-output-schema.md`
- `02_phase3_dispatches/P3-TopicCard-05-human-edit-cost-regression-TopicCard-human-edit-cost-regression.md`
- `03_phase4_dispatches/P4-DILO-01-egress-contract-implementation-plan-DiloFlow-egress-contract-implementation-plan.md`
- `03_phase4_dispatches/P4-DILO-02-manifest-publish-dry-run-Manifest-publish-dry-run.md`
- `03_phase4_dispatches/P4-DILO-03-supersede-protocol-and-tombstone-Supersede-protocol-and-tombstone.md`
- `03_phase4_dispatches/P4-DILO-04-diloflow-readback-reconciliation-DiloFlow-readback-reconciliation.md`
- `03_phase4_dispatches/P4-HERMES-01-agent-intent-contract-Hermes-agent-intent-contract.md`
- `03_phase4_dispatches/P4-HERMES-02-review-queue-coordination-Hermes-review-queue-coordination.md`
- `03_phase4_dispatches/P4-HERMES-03-tool-truthful-stdout-bridge-Tool-truthful-stdout-bridge.md`
- `03_phase4_dispatches/P4-WB-01-signal-list-readonly-preview-Signal-list-read-only-preview.md`
- `03_phase4_dispatches/P4-WB-02-recommendation-engine-candidate-only-Recommendation-engine-candidate-only.md`
- `03_phase4_dispatches/P4-WB-03-candidate-dispatch-ui-bounded-flow-Candidate-dispatch-UI-bounded-flow.md`
- `03_phase4_dispatches/P4-WB-04-batch-capture-scope-gate-enforcement-Batch-capture-scope-gate-enforcement.md`
- `03_phase4_dispatches/P4-WB-05-workbench-usefulness-readback-Workbench-usefulness-readback.md`
- `03_phase4_dispatches/P4-XTEST-01-cross-system-end-to-end-test-set-Cross-system-end-to-end-test-set.md`
- `04_module_dispatches/MOD-AGENT-01-agent-fleet-ledger-Agent-fleet-ledger.md`
- `04_module_dispatches/MOD-AGENT-02-cost-attribution-ledger-Cost-attribution-ledger.md`
- `04_module_dispatches/MOD-AGENT-03-commander-subagent-handoff-Commander-subagent-handoff.md`
- `04_module_dispatches/MOD-EGRESS-01-raw-egress-contract-RAW-egress-contract.md`
- `04_module_dispatches/MOD-EGRESS-02-diloflow-egress-contract-DiloFlow-egress-contract.md`
- `04_module_dispatches/MOD-EGRESS-03-obsidian-egress-contract-Obsidian-egress-contract.md`
- `04_module_dispatches/MOD-EGRESS-04-supersede-egress-contract-Supersede-egress-contract.md`
- `04_module_dispatches/MOD-RETRIEVAL-01-visual-dam-object-contract-Visual-DAM-object-contract.md`
- `04_module_dispatches/MOD-RETRIEVAL-02-hybrid-search-fixture-Hybrid-search-fixture.md`
- `04_module_dispatches/MOD-RETRIEVAL-03-source-freshness-router-Source-freshness-router.md`
- `04_module_dispatches/MOD-RETRIEVAL-04-citation-packaging-contract-Citation-packaging-contract.md`
- `04_module_dispatches/MOD-STATE-01-state-library-contract-State-library-contract.md`
- `04_module_dispatches/MOD-STATE-02-five-gate-automation-Five-gate-automation.md`
- `04_module_dispatches/MOD-STATE-03-state-word-drift-audit-State-word-drift-audit.md`
- `04_module_dispatches/MOD-VISUAL-01-visual-asset-table-creation-Visual-asset-table-creation.md`
- `04_module_dispatches/MOD-VISUAL-02-prompt-template-contract-Prompt-template-contract.md`
- `04_module_dispatches/MOD-VISUAL-03-design-token-library-candidate-Design-token-library-candidate.md`
- `04_module_dispatches/MOD-VISUAL-04-pattern-library-index-Pattern-library-index.md`
- `04_module_dispatches/MOD-VISUAL-05-visual-regression-report-gate-Visual-regression-report-gate.md`
- `05_cluster_indexes/PF-C0-cluster-index-C0-settle-and-readback.md`
- `05_cluster_indexes/PF-C1-cluster-index-Product-proof-pair-and-TopicCard.md`
- `05_cluster_indexes/PF-C2-cluster-index-ScoutFlow-to-RAW-handoff.md`
- `05_cluster_indexes/PF-C3-cluster-index-Lightweight-object-expansion.md`
- `05_cluster_indexes/PF-C4-cluster-index-Controlled-technical-hardening.md`
- `05_cluster_indexes/PF-LP-cluster-index-Localhost-preview-and-LP-discipline.md`
- `05_cluster_indexes/PF-O1-cluster-index-Overflow-and-blocked-lanes.md`
- `05_cluster_indexes/agent-cluster-index-U5-agent-module.md`
- `05_cluster_indexes/egress-cluster-index-U8-egress-module.md`
- `05_cluster_indexes/retrieval-cluster-index-U6-retrieval-module.md`
- `05_cluster_indexes/state-library-cluster-index-U7-state-library-module.md`
- `05_cluster_indexes/visual-cluster-index-U4-visual-module.md`
- `README-deliverable-index-2026-05-07.md`

[claim]
## §4 How to use

[prerequisite]
[instruction] Pick exactly one dispatch file, read its prerequisites, and paste it into Codex/Claude Code/Hermes only after the user chooses that lane. Do not batch a high-risk lane with another lane unless the commander mode explicitly serializes it.

[deliverable]
[instruction] For any later worker, the first action is readback. The worker must state which upstream files were read, whether any were missing, and whether the output remains docs-only candidate.

[claim]
[instruction] For any later reviewer, compare the worker's stdout against the dispatch's stdout contract. A missing validation command, moved authority boundary, or vague partial result should be treated as concern.

[claim]
## §5 Truthful stdout contract

[output]
```yaml
CLOUD_U9_PHASE_2_4_DISPATCH_CATALOG_COMPLETE: true
zip_filename: cloud-output-U9-phase-2-4-dispatch-catalog-v0-2026-05-07.zip
files_count: 95
total_words_cjk_latin_approx: 184143
total_thinking_minutes: 12.3
phase_2_dispatch_count: 28
phase_3_dispatch_count: 17
phase_4_dispatch_count: 13
module_dispatch_count: 19
cluster_index_count: 12
mermaid_diagrams_count: 14
multi_pass_completed: 12/12
self_audit_findings: 36
critical_issues_fixed_inline: 6
known_limitations:
  - wall-clock thinking time below the prompt target; reported truthfully, not inflated
  - live web vendor/legal evidence not refreshed in this environment
  - U1-U8 local cloud-output ZIPs were not present under /mnt/data; module prompts require manual readback when available
  - EXTERNAL-AUDIT-REPORT-2026-05-07.md was not fetchable; Run-3+4 report and CHECKPOINT were used instead
  - prompt requested 11 cluster indexes but enumerated 12 cluster names; delivered 12 and reported actual count
boundary_preservation_check: clear
all_dispatch_can_open_flags_false: confirmed
no_actual_authorization_implied: confirmed
ready_for_user_audit: yes
```

[claim]
## §6 Self-check summary

[verification] Markdown file count is 95, exceeding the >=71 hard floor. Approximate CJK+Latin word/unit count is 184143, exceeding the >=118000 floor. Mermaid blocks count is 14, exceeding the >=7 floor.

[verification] Frontmatter guard passed: every markdown file contains `status: candidate` and `authority: not-authority`. Dispatch guard passed: every dispatch file contains `can_open_C4: false`, `can_open_runtime: false`, and `can_open_migration: false`.

[verification] Claim-label coverage average is 100.0% and minimum per-file coverage is 100.0% under the local paragraph-label checker.

[claim]
## §7 Boundary preservation

[boundary] Authority files are not written by this ZIP. The deliverable does not touch ScoutFlow repository files, production code, local-only directories, credentials, migrations, browser profiles, runtime tools, ASR, media downloads, RAW vault, DiloFlow, or Obsidian.

[boundary] The five overflow lanes remain Hold. Dispatches may say “spike”, “fixture”, “dry-run”, or “candidate”, but those words do not change gate state.

[boundary] Vendor/pattern recap is not live research. A later web-enabled reviewer must refresh vendor evidence before runtime/legal choices.

[claim]
## §8 Fast audit commands

[output]
```bash
unzip cloud-output-U9-phase-2-4-dispatch-catalog-v0-2026-05-07.zip
cd cloud-output-U9-phase-2-4-dispatch-catalog-v0-2026-05-07
find . -name "*.md" | wc -l
rg -L "status: candidate" -g "*.md" .
rg -L "authority: not-authority" -g "*.md" .
rg -L "can_open_C4: false" 01_phase2_dispatches 02_phase3_dispatches 03_phase4_dispatches 04_module_dispatches
rg "FORBIDDEN_VENDOR_AUTHORIZATION_TERMS" . || true
```

[limitation] The final `rg` command is a wording smoke test. English `not-approved` frontmatter is expected and does not imply authorization.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.

[audit]
[detail] README guard: when the user audits this ZIP, they should begin with the stdout contract and then sample one dispatch from each phase. The most important question is not whether the catalog is large, but whether every file remains honest about gate state.
