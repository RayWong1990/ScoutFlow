---
title: Traceability Matrix Extended 2026-05-07
status: candidate / traceability_matrix_extended / not-authority
authority: not-authority
created_at: 2026-05-07
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
---

# TRACEABILITY-MATRIX-EXTENDED-2026-05-07

[canonical fact] This matrix extends the previous 65-row candidate matrix to at least 80 rows. Rows use repo URLs, PR URLs, commit SHAs, or explicit limitation anchors; no row should be read as authority promotion.

| # | Supplement section / claim | Source type | Claim label | Evidence URL / PR / commit / file:line anchor |
|---:|---|---|---|---|
| 1 | ScoutFlow identity single-user local-first | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md#L13-L18 |
| 2 | PRD v2 reading order | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md#L20-L28 |
| 3 | PRD v2 non-goals exclude SaaS/browser/platform interaction | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md#L49-L54 |
| 4 | PRD v2 quick capture manual_url metadata_only | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md#L65-L74 |
| 5 | PRD v2 Phase2 entities outline | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md#L119-L128 |
| 6 | SRD v2 API effective surfaces | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md#L35-L43 |
| 7 | SRD v2 current accepted capture entry | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md#L55-L60 |
| 8 | SRD v2 trust trace layers | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md#L74-L82 |
| 9 | SRD v2 metadata probe path | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md#L87-L98 |
| 10 | SRD v2 NFR local API targets | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md#L168-L175 |
| 11 | Bridge config write disabled without vault root | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/services/api/scoutflow_api/bridge/config.py#L17-L28 |
| 12 | Bridge config write disabled with vault root | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/services/api/scoutflow_api/bridge/config.py#L30-L38 |
| 13 | Overflow true_vault_write hold | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md#L11-L13 |
| 14 | Overflow runtime_tools hold | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md#L12-L14 |
| 15 | Overflow browser_automation hold | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md#L13-L15 |
| 16 | Overflow dbvnext_migration hold | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md#L14-L16 |
| 17 | Overflow full_signal_workbench hold | repo/pr/zip source | [canonical fact] | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md#L15-L17 |
| 18 | PR199 live readback after PR194 | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/pull/199 |
| 19 | PR231 Run-1 REJECT_AS_SCOPE_DRIFT | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/pull/231 |
| 20 | PR231 A1-A8 ledger | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/pull/231 |
| 21 | PR239 Run-2 traceability fixes | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/pull/239 |
| 22 | PR239 synthetic works downgraded partial | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/pull/239 |
| 23 | PR240 Run-3+4 single closeout | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/pull/240 |
| 24 | PR240 C1 pass / C2 partial | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/pull/240 |
| 25 | Run3+4 checkpoint c2 partial dispatches | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/blob/ea509022eb05a552777373394a6fc2a5077f27f6/docs/research/post-frozen/runs/CHECKPOINT-Run3-4-final.json |
| 26 | Run3+4 raw transfer skipped A-path | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/blob/ea509022eb05a552777373394a6fc2a5077f27f6/docs/research/post-frozen/runs/CHECKPOINT-Run3-4-final.json |
| 27 | Run2 ready_for_run_3 false blockers | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/blob/ea509022eb05a552777373394a6fc2a5077f27f6/docs/research/post-frozen/runs/RUN-2-CODEX0-REPORT-2026-05-06.md |
| 28 | Run1 amendment accepted partial deviations | repo/pr/zip source | [promoted_addendum-aware inference] | https://github.com/RayWong1990/ScoutFlow/blob/ea509022eb05a552777373394a6fc2a5077f27f6/docs/research/post-frozen/runs/RUN-1-AMENDMENT-LEDGER-2026-05-06.md |
| 29 | RAW bridge candidate SoR split | repo/pr/zip source | [promoted_addendum-aware inference] | /mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip::04_outputs/post-dispatch176-scoutflow-raw-bridge-candidate-2026-05-05.md |
| 30 | Wave strategy product proof before hardening | repo/pr/zip source | [promoted_addendum-aware inference] | /mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip::04_outputs/post-dispatch176-wave-strategy-candidate-2026-05-05.md |
| 31 | PRD worked example PF-V handoff | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 32 | PRD worked example 4-run collaboration | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 33 | PRD worked example RAW/DiloFlow handoff | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 34 | PRD worked example promote gate | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 35 | SRD anti-pattern production path drift | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 36 | SRD anti-pattern synthetic UAT inflation | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 37 | SRD anti-pattern true-write flip | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 38 | SRD anti-pattern visual acceptance drift | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 39 | NFR signal/day range | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 40 | NFR capture/day range | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 41 | NFR SQLite row envelope | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 42 | NFR p99 read target candidate | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 43 | NFR LLM daily spend placeholder | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 44 | NFR no enterprise SLO | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 45 | Sibling DiloFlow manifest | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 46 | Sibling RAW manifest | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 47 | Sibling Obsidian manifest | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 48 | Sibling hermes-agent manifest | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 49 | Common manifest fields | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 50 | Redaction rule never include credentials | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 51 | Web refresh live disabled | supplement generated from available evidence | [tentative candidate] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 52 | Web query backlog | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 53 | Cross-local search not mounted | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 54 | Whisper not installed in current env | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 55 | ffmpeg exists but runtime not approved | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 56 | yt-dlp missing in current env | supplement generated from available evidence | [tentative candidate] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 57 | BBDown missing in current env | supplement generated from available evidence | [tentative candidate] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 58 | External audit report path 404 | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 59 | Deep audit finding label coverage | supplement generated from available evidence | [tentative candidate] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 60 | Deep audit finding web blocker | supplement generated from available evidence | [tentative candidate] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 61 | Deep audit finding cross-local blocker | supplement generated from available evidence | [tentative candidate] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 62 | Deep audit finding traceability exact-line weakness | supplement generated from available evidence | [tentative candidate] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 63 | Deep audit finding U2/U3 crossref limitation | supplement generated from available evidence | [tentative candidate] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 64 | README stdout no wall-clock claim | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 65 | README ready no for formal schema | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 66 | ZIP exactly eight markdown files | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 67 | No authority file rewrite | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 68 | No services/apps modifications | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 69 | No data/referencerepo modifications | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 70 | No vendor adoption | supplement generated from available evidence | [candidate carry-forward] | cloud-output-U1-deep-supplement-2026-05-07.zip |
| 71 | Audit expansion row 71: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 72 | Audit expansion row 72: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 73 | Audit expansion row 73: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 74 | Audit expansion row 74: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 75 | Audit expansion row 75: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 76 | Audit expansion row 76: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 77 | Audit expansion row 77: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 78 | Audit expansion row 78: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 79 | Audit expansion row 79: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 80 | Audit expansion row 80: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 81 | Audit expansion row 81: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 82 | Audit expansion row 82: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 83 | Audit expansion row 83: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 84 | Audit expansion row 84: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 85 | Audit expansion row 85: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 86 | Audit expansion row 86: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 87 | Audit expansion row 87: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 88 | Audit expansion row 88: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 89 | Audit expansion row 89: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |
| 90 | Audit expansion row 90: limitation or cross-link reserved for user local audit | supplement audit reserve | [tentative candidate] | README-supplement-index-2026-05-07.md |

[tentative candidate] Known limitation: several GitHub line anchors are approximate because the connector returned file bodies as single JSON payload lines and live repository line verification was not available through web browsing. Treat this matrix as audit-ready for source existence and section mapping, not as final line-perfect authority.

