---
title: Sniff Report — U10-runbook
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U10-runbook

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 82 |
| Total size (bytes) | 677,906 |
| Total words (CJK+Latin token approx) | 164,681 |
| Avg words / file | 2,008 |
| Mermaid blocks | 10 |
| Claim labels | 78 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 82 / 82 (100%) |
| authority: not-authority | 82 / 82 (100%) |
| Missing status frontmatter | 0 |

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `BBDown_run` | 5 |
| `playwright_selenium_active` | 4 |

⚠️ **5 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `LINKED-DISPATCH-CATALOG-2026-05-07.md` → `BBDown_run`
- `MASTER-RUNBOOK-INDEX-2026-05-07.md` → `BBDown_run`
- `RB-CAP-07-BBDown-legal-posture-recheck-before-run-工具姿态复核.md` → `BBDown_run`
- `RB-INDEX-Visual-2026-05-07.md` → `playwright_selenium_active`
- `RB-VIS-09-Storybook-style-browser-launch-本地预览门控.md` → `playwright_selenium_active`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
⚠️ README not found or stdout fields not extracted

## §6 Key Files Detected
- README: `NOT FOUND`
- SELF-AUDIT: `outputs/U10-runbook/01_supporting/SELF-AUDIT-FINDINGS-2026-05-07.md`
- MASTER: `outputs/U10-runbook/01_supporting/MASTER-RUNBOOK-INDEX-2026-05-07.md`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 5 boundary regex pairs (may be quote, inspect Phase B2)
