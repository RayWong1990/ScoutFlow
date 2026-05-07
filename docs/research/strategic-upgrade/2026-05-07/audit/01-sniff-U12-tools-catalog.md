---
title: Sniff Report — U12-tools-catalog
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U12-tools-catalog

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 119 |
| Total size (bytes) | 447,102 |
| Total words (CJK+Latin token approx) | 165,637 |
| Avg words / file | 1,391 |
| Mermaid blocks | 13 |
| Claim labels | 0 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 22 / 119 (18%) |
| authority: not-authority | 0 / 119 (0%) |
| Missing status frontmatter | 97 |

**Files missing frontmatter status (sample ≤10):**
- 01-global-code-reviewer.md
- 02-global-build-error-resolver.md
- 03-global-e2e-runner.md
- 04-global-tdd-guide.md
- 05-global-refactor-cleaner.md
- 06-global-doc-updater.md
- 07-global-brainstorm-five-lens.md
- 08-global-writing-plan.md
- 09-global-executing-plan.md
- 10-global-context-loader.md

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `playwright_selenium_active` | 1 |

⚠️ **1 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `REDUNDANCY-CONFLICT-DETECTION.md` → `playwright_selenium_active`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
⚠️ README not found or stdout fields not extracted

## §6 Key Files Detected
- README: `NOT FOUND`
- SELF-AUDIT: `outputs/U12-tools-catalog/09_SYNTHESIS/SELF-AUDIT-FINDINGS.md`
- MASTER: `outputs/U12-tools-catalog/09_SYNTHESIS/MASTER-CATALOG-INDEX.md`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 1 boundary regex pairs (may be quote, inspect Phase B2)
- 97 files missing status frontmatter
- only 18% files marked status: candidate
