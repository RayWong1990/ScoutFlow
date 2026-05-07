---
status: candidate / supplement_index / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
supplement_for: cloud-output-U3-entity-v0-contracts-2026-05-07.zip
---
# README-supplement-index-2026-05-07

[canonical] This ZIP is a second-round supplement for the prior U3 entity-v0 contract bundle. It does not rewrite or supersede the original 10 files; it adds sample data, migration worked examples, referential integrity tests, OpenAPI fragments, cluster trace mapping, and a second self-audit.
[canonical] Truthful execution note: live web browsing was not available in this environment, so this supplement does not claim fresh 2026 web verification. Cross-local search of ~/workspace/DiloFlow, ~/workspace/contentflow, local Notion/Obsidian/FlowUs exports was also not available. GitHub-accessible ScoutFlow files and local uploaded ZIPs were used instead.
[candidate] The strongest added value is not freshness; it is making the prior abstract contracts auditable through 40 sample instances, 36 referential integrity cases, 16 candidate OpenAPI operations, and 28 cluster/entity trace cells.

## §1 File index

| # | File | Approx count units | Primary contents |
|---:|---|---:|---|
| [candidate] 1 | [candidate] ENTITY-Signal-v0-sample-data-2026-05-07.md | [candidate] 1731 | [candidate] 10 Signal fixtures, dedupe/broken-reference/AI boundary notes |
| [candidate] 2 | [candidate] ENTITY-Hypothesis-v0-sample-data-2026-05-07.md | [candidate] 1765 | [candidate] 10 Hypothesis fixtures with support/counter/user verdict/cascade links |
| [candidate] 3 | [candidate] ENTITY-CapturePlan-v0-sample-data-2026-05-07.md | [candidate] 1683 | [candidate] 10 CapturePlan fixtures with LP-001, rollback, blocked runtime fields |
| [candidate] 4 | [candidate] ENTITY-TopicCard-v1-sample-data-2026-05-07.md | [candidate] 2176 | [candidate] 10 TopicCard v1 fixtures carrying lite-v0 six fields plus relations |
| [candidate] 5 | [candidate] MIGRATION-V0-TO-V1-WORKED-EXAMPLES-2026-05-07.md | [candidate] 1240 | [candidate] 4 entity v0→v1 worked examples, candidate SQL, dual-read windows |
| [candidate] 6 | [candidate] REFERENTIAL-INTEGRITY-TEST-SET-2026-05-07.md | [candidate] 1064 | [candidate] 36 referential integrity tests and pseudo-runner |
| [candidate] 7 | [candidate] OPENAPI-GOLDEN-FRAGMENT-2026-05-07.md | [candidate] 1356 | [candidate] OpenAPI 3.1 candidate fragment with 16 non-implemented operations |
| [candidate] 8 | [candidate] CLUSTER-ENTITY-TRACE-MAP-2026-05-07.md | [candidate] 985 | [candidate] 4 entities × 7 clusters trace matrix and Mermaid graph |

## §2 Multi-pass workflow summary

[candidate] Pass 1: reread the previous ZIP and marked at least three shallow areas per core entity sample surface.
[candidate] Pass 2: reread PRD/SRD v2 boundaries and aligned the supplement to Phase 2 outline / not runtime.
[candidate] Pass 3: inspected bridge schema/router and TypeScript topic-card preview/vault shapes available through GitHub; live web refresh was unavailable and is marked false.
[candidate] Pass 4: expanded sample data to 10 instances per entity, 40 total, with explicit unverified author metadata rather than fabricated live facts.
[candidate] Pass 5: wrote v0→v1 worked examples for all four entities, with candidate SQL and dual-read/consumer-pin notes.
[candidate] Pass 6: wrote 36 referential integrity tests covering orphan, circular, cascade, dual-write, cross-platform, broken_reference, and anti-second-inbox cases.
[candidate] Pass 7: drafted OpenAPI 3.1 candidate fragment with 16 non-implemented operations and schema examples.
[candidate] Pass 8: mapped four entities across seven clusters, 28 trace cells, with one Mermaid diagram.
[candidate] Pass 9: ran second self-audit with 22 findings and inline fixes.
[candidate] Pass 10: packaged exactly nine markdown files into the required ZIP.

## §3 Self-audit v2 findings and inline fixes

[candidate] Finding 01: sample author fabrication risk. Inline fix: Fixed by using UNKNOWN_NOT_LIVE_VERIFIED and source_author_verification_state.
[candidate] Finding 02: prompt requested live web search but environment lacks web. Inline fix: Fixed by setting live_web_browsing_used=false and removing fresh-web claims.
[candidate] Finding 03: sample data could look like production seed data. Inline fix: Fixed by frontmatter not-authority and repeated fixture-only notes.
[candidate] Finding 04: candidate SQL could imply migration approval. Inline fix: Fixed by migration_approval:not-approved and redline comments before every SQL block.
[candidate] Finding 05: OpenAPI paths could imply actual FastAPI exposure. Inline fix: Fixed with /candidate-ir prefix, NotImplemented operationIds, and x-scoutflow-candidate-only.
[candidate] Finding 06: TopicCard RAW handoff could imply true write. Inline fix: Fixed with raw_handoff.true_write=not-approved.
[candidate] Finding 07: DiloFlow handoff could imply execution. Inline fix: Fixed with diloflow_handoff.execution=not-approved.
[candidate] Finding 08: CapturePlan could imply scheduler/runtime. Inline fix: Fixed with runtime_gate_state=not-approved and blocked_enrichments.
[candidate] Finding 09: Hypothesis reject could delete downstream plans. Inline fix: Fixed with cascade_suspend instead of delete.
[candidate] Finding 10: Signal could become second capture inbox. Inline fix: Fixed with anti_second_inbox_check and RI-032.
[candidate] Finding 11: cross-platform sample could create XHS capture. Inline fix: Fixed with needs_review and no new capture creation.
[candidate] Finding 12: multi-user sharing drift. Inline fix: Fixed by describing same-capture multi-workflow as single-user local sharing only.
[candidate] Finding 13: consumer-pin might be enterprise-heavy. Inline fix: Fixed by single local schema_version fixture pin.
[candidate] Finding 14: previous ZIP shallow findings could be buried. Inline fix: Fixed in each sample-data file §1.
[candidate] Finding 15: relation cycles could create deadlock. Inline fix: Fixed with RI-023 and nullable relation-table guidance.
[candidate] Finding 16: archived objects could be hidden too aggressively. Inline fix: Fixed by archive-readable / not delete rules.
[candidate] Finding 17: web evidence count could be falsely inflated. Inline fix: Fixed stdout live_search_queries_count=0.
[candidate] Finding 18: OpenAPI 3.1 vs JSON Schema details could overclaim current compatibility. Inline fix: Fixed by calling it a golden fragment only.
[candidate] Finding 19: TopicCard v1 could appear promoted from lite v0. Inline fix: Fixed by schema_version topic_card.v1.candidate and no promotion claim.
[candidate] Finding 20: sample count ambiguity. Inline fix: Fixed with explicit 10 per entity and sample_data_count_total=40.
[candidate] Finding 21: cluster trace could imply cluster ownership. Inline fix: Fixed by trace verbs and not-authority boundary column.
[candidate] Finding 22: README could omit exact limitations. Inline fix: Fixed by explicit unavailable web/cross-local notes in §0 and stdout.

## §4 Audit checklist for the user

[candidate] Confirm the ZIP contains exactly nine markdown files and no production code.
[candidate] Review whether UNKNOWN_NOT_LIVE_VERIFIED is acceptable for this environment or whether a later live-web pass must replace the samples.
[candidate] Check the candidate SQL for useful design language while rejecting migration execution.
[candidate] Check whether the OpenAPI fragment is useful as a cross-project egress anchor without mounting endpoints.
[candidate] Validate RI-001..RI-036 against the original corner cases and add project-specific cases if U1/U2 deep outputs introduce new lanes.
[candidate] Decide whether the cluster trace map should feed U1 SRD-v3 entity outline or stay as U3-only research.

## §5 Truthful stdout contract

```yaml
CLOUD_U3_DEEP_SUPPLEMENT_COMPLETE: true
zip_filename: "cloud-output-U3-deep-supplement-2026-05-07.zip"
files_count: 9
total_words_cjk_latin_approx: 35661
total_thinking_minutes: "not_attested_wall_clock; real execution was single-session best-effort"
live_web_browsing_used: false
live_search_queries_count: 0
sample_data_count_total: 40
referential_integrity_test_count: 36
openapi_endpoints_drafted: 16
cluster_entity_traces_count: 28
multi_pass_completed: "10/10 best-effort; live-web and cross-local passes transparently limited"
self_audit_findings: 22
boundary_preservation_check: "clear"
migration_approval: "not-approved"
ready_for_user_audit: "yes"
```


## §6 How to audit this supplement with the prior ZIP

[candidate] Audit step 1: Open the original entity contract for the entity under review. The expected result is a user decision about whether the supplement helps U1/U2 planning; it is not a decision to run migrations or expose endpoints.
[candidate] Audit step 2: Open the corresponding sample-data file in this supplement. The expected result is a user decision about whether the supplement helps U1/U2 planning; it is not a decision to run migrations or expose endpoints.
[candidate] Audit step 3: Check whether each abstract field has at least one concrete fixture value. The expected result is a user decision about whether the supplement helps U1/U2 planning; it is not a decision to run migrations or expose endpoints.
[candidate] Audit step 4: Check whether unknown metadata is explicit rather than guessed. The expected result is a user decision about whether the supplement helps U1/U2 planning; it is not a decision to run migrations or expose endpoints.
[candidate] Audit step 5: Check whether relation refs have tests in the referential integrity file. The expected result is a user decision about whether the supplement helps U1/U2 planning; it is not a decision to run migrations or expose endpoints.
[candidate] Audit step 6: Check whether migration examples preserve v0 readers during a v1 preview. The expected result is a user decision about whether the supplement helps U1/U2 planning; it is not a decision to run migrations or expose endpoints.
[candidate] Audit step 7: Check whether OpenAPI schemas include candidate_meta and NotImplemented operation names. The expected result is a user decision about whether the supplement helps U1/U2 planning; it is not a decision to run migrations or expose endpoints.
[candidate] Audit step 8: Check whether cluster trace cells are coordination hints, not task approval. The expected result is a user decision about whether the supplement helps U1/U2 planning; it is not a decision to run migrations or expose endpoints.

## §7 Compatibility with U1 / U2 deep outputs

[candidate] U1 SRD-v3 entity outline: this supplement can serve as design input only if the receiving lane preserves not-authority wording. The safest import is field vocabulary, test cases, and trace map rows. The unsafe import is copying candidate SQL into migration files, converting OpenAPI fragments into mounted endpoints, or treating sample data as platform-verified facts.
[candidate] U1 product language cleanup: this supplement can serve as design input only if the receiving lane preserves not-authority wording. The safest import is field vocabulary, test cases, and trace map rows. The unsafe import is copying candidate SQL into migration files, converting OpenAPI fragments into mounted endpoints, or treating sample data as platform-verified facts.
[candidate] U2 Lane-4 dbvnext unlock decision: this supplement can serve as design input only if the receiving lane preserves not-authority wording. The safest import is field vocabulary, test cases, and trace map rows. The unsafe import is copying candidate SQL into migration files, converting OpenAPI fragments into mounted endpoints, or treating sample data as platform-verified facts.
[candidate] U2 Lane-5 RAW/DiloFlow true-write gate: this supplement can serve as design input only if the receiving lane preserves not-authority wording. The safest import is field vocabulary, test cases, and trace map rows. The unsafe import is copying candidate SQL into migration files, converting OpenAPI fragments into mounted endpoints, or treating sample data as platform-verified facts.
[candidate] future C4 dispatch UI: this supplement can serve as design input only if the receiving lane preserves not-authority wording. The safest import is field vocabulary, test cases, and trace map rows. The unsafe import is copying candidate SQL into migration files, converting OpenAPI fragments into mounted endpoints, or treating sample data as platform-verified facts.
