---
title: RAW Intake Acceptance Rubric
status: candidate / rubric / not-authority
created_at: 2026-05-06
related_dispatch: PF-C2-04
---

# RAW Intake Acceptance Rubric

| Verdict | Meaning | Requirement |
| --- | --- | --- |
| `accepted` | RAW can consume the note directly | body is usable with minimal cleanup |
| `needs-edit` | RAW sees value but needs cleanup | specific cleanup reason must be logged |
| `rejected` | note should not enter downstream flow | reason must be logged |
| `pending_user_manual_transfer` | user has not copied the file into RAW yet | this is partial, not pass |

## Second-Inbox Guard

If a note only accumulates in a holding area and no real intake or seed extraction happens, that is not an acceptance pass.
