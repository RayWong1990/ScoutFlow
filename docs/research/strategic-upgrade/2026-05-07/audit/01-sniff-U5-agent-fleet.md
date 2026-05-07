---
title: Sniff Report — U5-agent-fleet
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U5-agent-fleet

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 10 |
| Total size (bytes) | 225,038 |
| Total words (CJK+Latin token approx) | 30,159 |
| Avg words / file | 3,015 |
| Mermaid blocks | 0 |
| Claim labels | 0 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 10 / 10 (100%) |
| authority: not-authority | 0 / 10 (0%) |
| Missing status frontmatter | 0 |

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `alembic_new_migration` | 3 |
| `write_enabled_True` | 3 |

⚠️ **3 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `ORCHESTRATION-PRIMITIVE-LIB-2026-05-07.md` → `alembic_new_migration`
- `ORCHESTRATION-PRIMITIVE-LIB-2026-05-07.md` → `write_enabled_True`
- `SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07.md` → `write_enabled_True`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
| Field | Value |
|---|---|
| files_count | 10 |
| total_words_cjk_latin_approx | 28964 |
| total_thinking_minutes | "not wall-clock audited; current response work estimate under 120m" |
| live_web_browsing_used | false |
| self_audit_findings | 18 |
| boundary_preservation_check | clear |
| ready_for_user_audit | yes |

## §6 Key Files Detected
- README: `outputs/U5-agent-fleet/README-deliverable-index-2026-05-07.md`
- SELF-AUDIT: `NOT FOUND`
- MASTER: `NOT FOUND`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 3 boundary regex pairs (may be quote, inspect Phase B2)
