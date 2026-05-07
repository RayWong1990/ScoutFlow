---
title: Sniff Report — U1-deep
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U1-deep

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 8 |
| Total size (bytes) | 166,252 |
| Total words (CJK+Latin token approx) | 22,835 |
| Avg words / file | 2,854 |
| Mermaid blocks | 7 |
| Claim labels | 820 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 8 / 8 (100%) |
| authority: not-authority | 8 / 8 (100%) |
| Missing status frontmatter | 0 |

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `alembic_new_migration` | 1 |
| `write_enabled_True` | 1 |

⚠️ **2 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `SRD-v3-supplement-anti-patterns-2026-05-07.md` → `alembic_new_migration`
- `SRD-v3-supplement-anti-patterns-2026-05-07.md` → `write_enabled_True`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
| Field | Value |
|---|---|
| files_count | 8 |
| total_words_cjk_latin_approx | 22648 |
| total_thinking_minutes | not_claimed_no_wall_clock_timer_available |
| live_web_browsing_used | false |
| self_audit_findings | 25 |
| boundary_preservation_check | clear |
| ready_for_user_audit | yes_for_gap_audit_no_for_formal_acceptance |

## §6 Key Files Detected
- README: `outputs/U1-deep/README-supplement-index-2026-05-07.md`
- SELF-AUDIT: `NOT FOUND`
- MASTER: `NOT FOUND`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 2 boundary regex pairs (may be quote, inspect Phase B2)
