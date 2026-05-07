---
title: Sniff Report — U8-egress
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U8-egress

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 10 |
| Total size (bytes) | 96,694 |
| Total words (CJK+Latin token approx) | 20,973 |
| Avg words / file | 2,097 |
| Mermaid blocks | 0 |
| Claim labels | 0 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 10 / 10 (100%) |
| authority: not-authority | 10 / 10 (100%) |
| Missing status frontmatter | 0 |

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `write_enabled_True` | 2 |

⚠️ **2 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `EGRESS-CONTRACT-DiloFlow-2026-05-07.md` → `write_enabled_True`
- `HANDOFF-MANIFEST-JSON-SCHEMA-2026-05-07.md` → `write_enabled_True`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
| Field | Value |
|---|---|
| files_count | 10 |
| total_words_cjk_latin_approx | 21949 |
| total_thinking_minutes | "not wall-clock audited; current-session synchronous generation" |
| live_web_browsing_used | false |
| self_audit_findings | 18 |
| boundary_preservation_check | clear |
| ready_for_user_audit | yes_with_live_web_gap |

## §6 Key Files Detected
- README: `outputs/U8-egress/README-deliverable-index-2026-05-07.md`
- SELF-AUDIT: `NOT FOUND`
- MASTER: `NOT FOUND`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 2 boundary regex pairs (may be quote, inspect Phase B2)
