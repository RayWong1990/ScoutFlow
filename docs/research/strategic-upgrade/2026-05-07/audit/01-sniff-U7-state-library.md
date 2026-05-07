---
title: Sniff Report — U7-state-library
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U7-state-library

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 9 |
| Total size (bytes) | 161,516 |
| Total words (CJK+Latin token approx) | 19,730 |
| Avg words / file | 2,192 |
| Mermaid blocks | 0 |
| Claim labels | 0 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 9 / 9 (100%) |
| authority: not-authority | 0 / 9 (0%) |
| Missing status frontmatter | 0 |

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `playwright_selenium_active` | 4 |

⚠️ **2 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `LIVE-WEB-EVIDENCE-2026-05-07.md` → `playwright_selenium_active`
- `MODULE-5-gate-automation-spec-2026-05-07.md` → `playwright_selenium_active`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
| Field | Value |
|---|---|
| files_count | 9 |
| total_words_cjk_latin_approx | 20369 |
| total_thinking_minutes | 28 |
| live_web_browsing_used | false |
| self_audit_findings | 20 |
| boundary_preservation_check | clear |
| ready_for_user_audit | yes |

## §6 Key Files Detected
- README: `outputs/U7-state-library/README-deliverable-index-2026-05-07.md`
- SELF-AUDIT: `NOT FOUND`
- MASTER: `NOT FOUND`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 2 boundary regex pairs (may be quote, inspect Phase B2)
