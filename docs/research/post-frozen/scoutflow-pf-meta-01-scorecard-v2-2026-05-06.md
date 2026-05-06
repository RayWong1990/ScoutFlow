# PF-META-01-FIX Scorecard v2 — 2026-05-06

## Dispatch table

| code | status | §1_goal_distinct? | §4_three_section? | §8_assertion_contract? | §12_specific? | §13_evidence_shape? | overall_verdict |
|---|---|---|---|---|---|---|---|
| `PF-C0-01R` | active R-version | yes | yes | not_applicable | yes | yes | clean |
| `PF-C0-MERGED-03+04` | active R-version | yes | yes | not_applicable | yes | yes | clean |
| `PF-C0-06R` | active R-version | yes | yes | not_applicable | yes | yes | clean |
| `PF-O1-01R` | active R-version | yes | yes | not_applicable | yes | yes | clean |
| `PF-LP-01` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-LP-02` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-LP-03` | active R-version | yes | yes | not_applicable | yes | yes | clean |
| `PF-LP-04` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-LP-05` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-LP-06` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-LP-07` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-LP-08` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-LP-09` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-LP-10` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-LP-11` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-LP-12` | active R-version | yes | yes | not_applicable | yes | yes | clean |
| `PF-LP-13` | active R-version | yes | yes | yes | yes | yes | clean |
| `PF-C0-02` | deprecated_by_PF_META_01 | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | deprecated_clean |
| `PF-C0-04` | deprecated_by_PF_META_01 | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | deprecated_clean |
| `PF-C0-05` | deprecated_by_PF_META_01 | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | deprecated_clean |
| `PF-O1-02` | deprecated_by_PF_META_01 | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | deprecated_clean |
| `PF-O1-03` | deprecated_by_PF_META_01 | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | deprecated_clean |
| `PF-O1-04` | deprecated_by_PF_META_01 | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | deprecated_clean |
| `PF-O1-05` | deprecated_by_PF_META_01 | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | deprecated_clean |
| `PF-O1-06` | deprecated_by_PF_META_01 | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | deprecated_clean |

## B1-B5 + W-LP01-Δ fix verification

| fix | verification | verdict |
|---|---|---|
| B1 | PF-LP-01 places `tests/api/test_main_app_routers.py` in files_to_create and not files_to_modify | clean |
| B2 | PF-LP-04/09/10/11 have no `manual:` inside bash and include §12.5 manual evidence step | clean |
| B3 | 8 old PF-C0/O1 dispatches have deprecated frontmatter + `_DEPRECATED-INDEX.md` + PACK-INDEX ⚪ rows | clean |
| B4 | PF-LP-01 validation uses `python -c '...'` outer single quotes and no `\"` escaped quote pattern | clean |
| B5 | PF-LP-13 has 5 numbered contracts, each with method/status, schema fields, and golden diff command; §13 includes golden_schema_path | clean |
| W-LP01-Δ | PF-LP-01 §8 lists 3 required assertions; empty tests count as `REJECT_AS_DOCS_ONLY_PROOF` | clean |

aggregate: `25/25 clean_or_deprecated_clean`; active_clean: `17/17`; deprecated_clean: `8/8`
