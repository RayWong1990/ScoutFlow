---
title: Sniff Master Summary — 16 ZIP overall
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Master Summary — 16 ZIP

> 自动化 sniff test for 16 cloud-output ZIPs under `outputs/`. 不替代人审; 是 Phase B2 spot check 的输入信号。

## §1 Quantity Overview
| ZIP | Files | Words | Mermaid | Claim Labels | Verdict |
|---|---:|---:|---:|---:|---|
| `U1-deep` | 8 | 22,835 | 7 | 820 | ⚠️ |
| `U10-runbook` | 82 | 164,681 | 10 | 78 | ⚠️ |
| `U11-anti-pattern` | 100 | 178,011 | 5 | 1068 | ⚠️ |
| `U12-tools-catalog` | 119 | 165,637 | 13 | 0 | ⚠️ |
| `U13-visual-brand` | 108 | 198,247 | 37 | 0 | ✅ |
| `U14-apple-silicon` | 78 | 122,693 | 9 | 0 | ✅ |
| `U15-decision-log` | 142 | 118,765 | 19 | 0 | ✅ |
| `U16-memory-graph` | 96 | 145,965 | 12 | 4 | ⚠️ |
| `U2-deep` | 9 | 28,622 | 7 | 39 | ⚠️ |
| `U3-deep` | 9 | 35,867 | 3 | 838 | ⚠️ |
| `U4-visual-asset` | 10 | 21,898 | 0 | 0 | ✅ |
| `U5-agent-fleet` | 10 | 30,159 | 0 | 0 | ⚠️ |
| `U6-retrieval-dam` | 9 | 20,278 | 0 | 0 | ⚠️ |
| `U7-state-library` | 9 | 19,730 | 0 | 0 | ⚠️ |
| `U8-egress` | 10 | 20,973 | 0 | 0 | ⚠️ |
| `U9-dispatch-catalog` | 96 | 185,637 | 15 | 2237 | ⚠️ |
| **TOTAL** | **895** | **1,479,998** | **137** | — | — |

## §2 Frontmatter Discipline
| ZIP | candidate% | not-authority% | missing |
|---|---:|---:|---:|
| `U1-deep` | 100% | 100% | 0 |
| `U10-runbook` | 100% | 100% | 0 |
| `U11-anti-pattern` | 100% | 100% | 0 |
| `U12-tools-catalog` | 18% | 0% | 97 |
| `U13-visual-brand` | 100% | 100% | 0 |
| `U14-apple-silicon` | 100% | 100% | 0 |
| `U15-decision-log` | 98% | 98% | 1 |
| `U16-memory-graph` | 17% | 0% | 79 |
| `U2-deep` | 100% | 100% | 0 |
| `U3-deep` | 100% | 100% | 0 |
| `U4-visual-asset` | 100% | 0% | 0 |
| `U5-agent-fleet` | 100% | 0% | 0 |
| `U6-retrieval-dam` | 0% | 0% | 9 |
| `U7-state-library` | 100% | 0% | 0 |
| `U8-egress` | 100% | 100% | 0 |
| `U9-dispatch-catalog` | 100% | 100% | 0 |

## §3 Boundary Scan Cross-ZIP

### U1-deep
- `alembic_new_migration`: 1 hits
- `write_enabled_True`: 1 hits

### U10-runbook
- `BBDown_run`: 5 hits
- `playwright_selenium_active`: 4 hits

### U11-anti-pattern
- `BBDown_run`: 4 hits
- `alembic_new_migration`: 11 hits
- `ffmpeg_run`: 1 hits
- `playwright_selenium_active`: 3 hits
- `yt_dlp_run`: 1 hits

### U12-tools-catalog
- `playwright_selenium_active`: 1 hits

### U16-memory-graph
- `alembic_new_migration`: 2 hits

### U2-deep
- `BBDown_run`: 1 hits
- `alembic_new_migration`: 10 hits
- `ffmpeg_run`: 1 hits
- `playwright_selenium_active`: 8 hits
- `yt_dlp_run`: 1 hits

### U3-deep
- `alembic_new_migration`: 4 hits

### U5-agent-fleet
- `alembic_new_migration`: 3 hits
- `write_enabled_True`: 3 hits

### U7-state-library
- `playwright_selenium_active`: 4 hits

### U8-egress
- `write_enabled_True`: 2 hits

### U9-dispatch-catalog
- `alembic_new_migration`: 82 hits
- `playwright_selenium_active`: 2 hits

## §4 Secret Scan Cross-ZIP

✅ **No secret pattern hits across 16 ZIP**

## §5 Truthful Stdout Cross-ZIP
| ZIP | files (self-rep) | thinking_min | live_web | self_audit | ready |
|---|---|---|---|---|---|
| `U1-deep` | 8 | not_claimed_no_wall_clock_timer_available | false | 25 | yes_for_gap_audit_no_for_formal_acceptance |
| `U10-runbook` | ? | ? | ? | ? | ? |
| `U11-anti-pattern` | ? | ? | ? | ? | ? |
| `U12-tools-catalog` | ? | ? | ? | ? | ? |
| `U13-visual-brand` | ? | ? | ? | ? | ? |
| `U14-apple-silicon` | ? | ? | ? | ? | ? |
| `U15-decision-log` | ? | ? | ? | ? | ? |
| `U16-memory-graph` | ? | ? | ? | ? | ? |
| `U2-deep` | 9 | actual_wall_clock_not_120; live long-run requirement not met in this environment | false | 24 | yes |
| `U3-deep` | 9 | "not_attested_wall_clock; real execution was single-session best-effort" | false | 22 | "yes" |
| `U4-visual-asset` | 10 | "not ≥120; single-session generation under environment constraints" | false | 20 | yes |
| `U5-agent-fleet` | 10 | "not wall-clock audited; current response work estimate under 120m" | false | 18 | yes |
| `U6-retrieval-dam` | 9 | 32 | false | 20 | yes |
| `U7-state-library` | 9 | 28 | false | 20 | yes |
| `U8-egress` | 10 | "not wall-clock audited; current-session synchronous generation" | false | 18 | yes_with_live_web_gap |
| `U9-dispatch-catalog` | 95 | 12.3 | ? | 36 | yes |

## §6 Per-ZIP Verdict & Reasons
- **`U1-deep`**: `CONCERN` — 2 boundary pairs
- **`U10-runbook`**: `CONCERN` — 5 boundary pairs
- **`U11-anti-pattern`**: `CONCERN` — 18 boundary pairs
- **`U12-tools-catalog`**: `CONCERN` — 1 boundary pairs, 97 missing frontmatter, candidate% only 18%
- **`U13-visual-brand`**: `CLEAR`
- **`U14-apple-silicon`**: `CLEAR`
- **`U15-decision-log`**: `CLEAR`
- **`U16-memory-graph`**: `CONCERN` — 2 boundary pairs, 79 missing frontmatter, candidate% only 17%
- **`U2-deep`**: `CONCERN` — 11 boundary pairs
- **`U3-deep`**: `CONCERN` — 1 boundary pairs
- **`U4-visual-asset`**: `CLEAR`
- **`U5-agent-fleet`**: `CONCERN` — 3 boundary pairs
- **`U6-retrieval-dam`**: `CONCERN` — 9 missing frontmatter, candidate% only 0%
- **`U7-state-library`**: `CONCERN` — 2 boundary pairs
- **`U8-egress`**: `CONCERN` — 2 boundary pairs
- **`U9-dispatch-catalog`**: `CONCERN` — 78 boundary pairs

## §7 Phase B2 Spot Check Targets
Tier 1 (high promote probability): U1-deep, U2-deep, U3-deep, U4-visual-asset, U9-dispatch-catalog, U10-runbook, U11-anti-pattern, U13-visual-brand, U15-decision-log

For each Tier 1 ZIP, read README + SELF-AUDIT + MASTER + 2 random working files. Output `audit/02-spot-U[X].md`.
