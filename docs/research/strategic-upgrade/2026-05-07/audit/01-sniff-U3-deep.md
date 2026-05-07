---
title: Sniff Report — U3-deep
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U3-deep

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 9 |
| Total size (bytes) | 310,174 |
| Total words (CJK+Latin token approx) | 35,867 |
| Avg words / file | 3,985 |
| Mermaid blocks | 3 |
| Claim labels | 838 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 9 / 9 (100%) |
| authority: not-authority | 9 / 9 (100%) |
| Missing status frontmatter | 0 |

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `alembic_new_migration` | 4 |

⚠️ **1 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `MIGRATION-V0-TO-V1-WORKED-EXAMPLES-2026-05-07.md` → `alembic_new_migration`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
| Field | Value |
|---|---|
| files_count | 9 |
| total_words_cjk_latin_approx | 35661 |
| total_thinking_minutes | "not_attested_wall_clock; real execution was single-session best-effort" |
| live_web_browsing_used | false |
| self_audit_findings | 22 |
| boundary_preservation_check | "clear" |
| ready_for_user_audit | "yes" |

## §6 Key Files Detected
- README: `outputs/U3-deep/README-supplement-index-2026-05-07.md`
- SELF-AUDIT: `NOT FOUND`
- MASTER: `NOT FOUND`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 1 boundary regex pairs (may be quote, inspect Phase B2)
