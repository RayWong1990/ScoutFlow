---
title: Kill switch registry test packet
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-GLOBAL-09
---

# Kill switch registry test packet

## packet_rows

| kill_switch | trigger_example | expected_verdict |
|---|---|---|
| `REJECT_AS_REOPEN_FROZEN_HISTORY` | a note proposes rerunning Dispatch145 because wording changed | reject immediately |
| `REJECT_AS_RUNTIME_CREEP` | preview doc claims BBDown live can now run | reject immediately |
| `REJECT_AS_TRUE_WRITE_UNLOCK` | bridge router mount is described as enabling write | reject immediately |
| `REJECT_AS_BROWSER_AUTOMATION_UNLOCK` | screenshot capture is framed as browser automation approval | reject immediately |
| `REJECT_AS_MIGRATION_UNLOCK` | docs-only registry claims DB vNext is ready to migrate | reject immediately |
| `REJECT_AS_DOCS_ONLY_PROOF` | candidate checklist is described as product proof | reject immediately |
| `REJECT_AS_AUTHORITY_DRIFT` | a PF-GLOBAL note edits `docs/current.md` | reject immediately |

## how_to_use

1. Compare the PR diff against each kill-switch row.
2. If any row matches, stop review and mark the PR rejected.
3. Write the rejected row into the review receipt rather than negotiating it away in chat.

## verdict

- `T-PASS` means the registry is ready for audit use.
