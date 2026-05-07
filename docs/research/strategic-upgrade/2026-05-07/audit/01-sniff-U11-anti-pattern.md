---
title: Sniff Report — U11-anti-pattern
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U11-anti-pattern

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 100 |
| Total size (bytes) | 698,914 |
| Total words (CJK+Latin token approx) | 178,011 |
| Avg words / file | 1,780 |
| Mermaid blocks | 5 |
| Claim labels | 1068 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 100 / 100 (100%) |
| authority: not-authority | 100 / 100 (100%) |
| Missing status frontmatter | 0 |

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `BBDown_run` | 4 |
| `alembic_new_migration` | 11 |
| `ffmpeg_run` | 1 |
| `playwright_selenium_active` | 3 |
| `yt_dlp_run` | 1 |

⚠️ **18 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `AP-AC-01-dual-window-writes-docs-current-md.md` → `alembic_new_migration`
- `AP-AC-02-sidecar-agent-writes-authority-files.md` → `alembic_new_migration`
- `AP-AC-03-task-index-numbering-conflict.md` → `alembic_new_migration`
- `AP-AC-08-authority-writer-max-1-violation.md` → `alembic_new_migration`
- `AP-BL-02-bbdown-live-runtime-implied-approval.md` → `BBDown_run`
- `AP-BL-04-browser-automation-implied-approval.md` → `playwright_selenium_active`
- `AP-BL-07-dispatch-schema-lacks-can-open-flags.md` → `alembic_new_migration`
- `AP-CT-01-dispatch-without-token-estimate.md` → `alembic_new_migration`
- `AP-MA-01-multi-window-dispatch-no-ledger.md` → `alembic_new_migration`
- `AP-MA-05-single-writer-race.md` → `alembic_new_migration`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
⚠️ README not found or stdout fields not extracted

## §6 Key Files Detected
- README: `NOT FOUND`
- SELF-AUDIT: `outputs/U11-anti-pattern/SELF-AUDIT-FINDINGS-2026-05-07.md`
- MASTER: `outputs/U11-anti-pattern/MASTER-ANTI-PATTERN-INDEX-2026-05-07.md`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 18 boundary regex pairs (may be quote, inspect Phase B2)
