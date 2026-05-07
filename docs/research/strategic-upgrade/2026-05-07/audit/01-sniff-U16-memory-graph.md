---
title: Sniff Report — U16-memory-graph
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U16-memory-graph

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 96 |
| Total size (bytes) | 579,701 |
| Total words (CJK+Latin token approx) | 145,965 |
| Avg words / file | 1,520 |
| Mermaid blocks | 12 |
| Claim labels | 4 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 17 / 96 (17%) |
| authority: not-authority | 0 / 96 (0%) |
| Missing status frontmatter | 79 |

**Files missing frontmatter status (sample ≤10):**
- E-AI-AGENTS.md
- E-BRIDGE-THIN-API.md
- E-CAPTURE-PLAN.md
- E-CONTENTFLOW.md
- E-DILOFLOW.md
- E-H5-CAPTURE-STATION.md
- E-HYPOTHESIS.md
- E-RAW-VAULT.md
- E-RECEIPT-LEDGER.md
- E-SCOUTFLOW.md

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `alembic_new_migration` | 2 |

⚠️ **2 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `L-MIGRATION-DRIFT.md` → `alembic_new_migration`
- `T-EXECUTION-GATES.md` → `alembic_new_migration`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
⚠️ README not found or stdout fields not extracted

## §6 Key Files Detected
- README: `NOT FOUND`
- SELF-AUDIT: `outputs/U16-memory-graph/03_pattern_nodes/P-SELF-AUDIT-CLAIM-LABELS.md`
- MASTER: `outputs/U16-memory-graph/09_supporting/MASTER-MEMORY-ATLAS.md`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 2 boundary regex pairs (may be quote, inspect Phase B2)
- 79 files missing status frontmatter
- only 17% files marked status: candidate
