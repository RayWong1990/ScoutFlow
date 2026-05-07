---
title: Sniff Report — U2-deep
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — U2-deep

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | 9 |
| Total size (bytes) | 227,890 |
| Total words (CJK+Latin token approx) | 28,622 |
| Avg words / file | 3,180 |
| Mermaid blocks | 7 |
| Claim labels | 39 |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | 9 / 9 (100%) |
| authority: not-authority | 9 / 9 (100%) |
| Missing status frontmatter | 0 |

## §3 Boundary Scan
| Pattern | Hits |
|---|---:|
| `BBDown_run` | 1 |
| `alembic_new_migration` | 10 |
| `ffmpeg_run` | 1 |
| `playwright_selenium_active` | 8 |
| `yt_dlp_run` | 1 |

⚠️ **11 (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.

**Top 10 file-pattern pairs:**
- `FAIL-MODE-CASE-STUDIES-2026-05-07.md` → `alembic_new_migration`
- `LANE-1-true-vault-write-spike-commands-2026-05-07.md` → `alembic_new_migration`
- `LANE-2-runtime-tools-spike-commands-2026-05-07.md` → `BBDown_run`
- `LANE-2-runtime-tools-spike-commands-2026-05-07.md` → `alembic_new_migration`
- `LANE-2-runtime-tools-spike-commands-2026-05-07.md` → `ffmpeg_run`
- `LANE-2-runtime-tools-spike-commands-2026-05-07.md` → `yt_dlp_run`
- `LANE-3-browser-automation-spike-commands-2026-05-07.md` → `alembic_new_migration`
- `LANE-3-browser-automation-spike-commands-2026-05-07.md` → `playwright_selenium_active`
- `LANE-4-dbvnext-migration-spike-commands-2026-05-07.md` → `alembic_new_migration`
- `LANE-5-signal-workbench-spike-commands-2026-05-07.md` → `alembic_new_migration`

## §4 Secret Scan
✅ No secret pattern hit

## §5 Truthful Stdout (extracted from README)
| Field | Value |
|---|---|
| files_count | 9 |
| total_words_cjk_latin_approx | 28889 |
| total_thinking_minutes | actual_wall_clock_not_120; live long-run requirement not met in this environment |
| live_web_browsing_used | false |
| self_audit_findings | 24 |
| boundary_preservation_check | clear |
| ready_for_user_audit | yes |

## §6 Key Files Detected
- README: `outputs/U2-deep/README-supplement-index-2026-05-07.md`
- SELF-AUDIT: `NOT FOUND`
- MASTER: `NOT FOUND`

## §7 Sniff Verdict

**Verdict: `CONCERN`**

Reasons:
- 11 boundary regex pairs (may be quote, inspect Phase B2)
