---
title: Sniff Report — U9-dispatch-catalog
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U9-dispatch-catalog

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 96 |
| Total size (bytes) | 1,454,239 |
| Total words (CJK+Latin token approx) | 185,637 |
| Avg words / file | 1,933 |
| Mermaid blocks | 15 |
| Claim labels | 2237 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 96 / 96 (100%) |
| authority: not-authority | 96 / 96 (100%) |
| Missing status frontmatter | 0 |

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `alembic_new_migration` | 82 |
| `playwright_selenium_active` | 2 |

⚠️ **78 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `MOD-AGENT-01-agent-fleet-ledger-Agent-fleet-ledger.md` → `alembic_new_migration`
- `MOD-AGENT-02-cost-attribution-ledger-Cost-attribution-ledger.md` → `alembic_new_migration`
- `MOD-AGENT-03-commander-subagent-handoff-Commander-subagent-handoff.md` → `alembic_new_migration`
- `MOD-EGRESS-01-raw-egress-contract-RAW-egress-contract.md` → `alembic_new_migration`
- `MOD-EGRESS-02-diloflow-egress-contract-DiloFlow-egress-contract.md` → `alembic_new_migration`
- `MOD-EGRESS-03-obsidian-egress-contract-Obsidian-egress-contract.md` → `alembic_new_migration`
- `MOD-EGRESS-04-supersede-egress-contract-Supersede-egress-contract.md` → `alembic_new_migration`
- `MOD-RETRIEVAL-01-visual-dam-object-contract-Visual-DAM-object-contract.md` → `alembic_new_migration`
- `MOD-RETRIEVAL-02-hybrid-search-fixture-Hybrid-search-fixture.md` → `alembic_new_migration`
- `MOD-RETRIEVAL-03-source-freshness-router-Source-freshness-router.md` → `alembic_new_migration`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
| Field | Value |
|---|---|
| files_count | 95 |
| total_words_cjk_latin_approx | 184143 |
| total_thinking_minutes | 12.3 |
| self_audit_findings | 36 |
| boundary_preservation_check | clear |
| ready_for_user_audit | yes |

## §6 Key Files Detected
- README: `outputs/U9-dispatch-catalog/README-deliverable-index-2026-05-07.md`
- SELF-AUDIT: `outputs/U9-dispatch-catalog/00_supporting/SELF-AUDIT-FINDINGS-2026-05-07.md`
- MASTER: `outputs/U9-dispatch-catalog/00_supporting/MASTER-ROADMAP-PHASE-2-4-2026-05-07.md`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 78 boundary regex pairs (may be quote, inspect Phase B2)
