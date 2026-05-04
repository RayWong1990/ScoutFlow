# Dispatch Template
> New dispatch files keep only task-specific content. Shared validation, self-audit, and final-report wording lives here.
> Target shape: each dispatch adds no more than 40 task-specific lines and references this file for shared sections.
## Shared Header
```text
# Dispatch <NN> - <Task ID> <Title>
> Task ID: <T-P1A-NNN>
> Owner Tool: <Codex Desktop / Claude Code / reviewer> single writer
> Mode: <docs-only | code-bearing | research note | audit | ...>
> Depends On: <prerequisite tasks or "none">
> Source: <source spec / review note / user request>
```
## State Snapshot
```bash
git fetch origin --quiet
git log origin/main --oneline -3
gh pr list --state merged --limit 3
# Confirm main HEAD and the Depends On line agree before writing.
```
## Task-Specific Required Sections
Each dispatch must define these concrete sections:
- Section 1 Goal: one-sentence target
- Section 2 Allowed Paths: exact file list
- Section 3 Forbidden Paths: task-specific no-write zones
- Section 4 Required Behavior: actual edits or checks
- Section 6 Stop-the-line: task-specific halt conditions
- Section 8 Branch / PR / Merge Guidance
- Section 9 Estimated Effort
## Shared Validation
Use `make verify` if it exists. Otherwise run:
```bash
python tools/check-docs-redlines.py
python tools/check-secrets-redlines.py
python -m pytest tests/api tests/contracts -q
git diff --check
git ls-files | grep -E '^(data|referencerepo|example|examples)/' || true
find . -maxdepth 1 -type d \( -name apps -o -name workers -o -name packages -o -name candidates -o -name dispatches -o -name audits -o -name example -o -name examples \) -print
```
## Shared 5-Part Self-Audit
Use this instead of the older 7-8 segment audit:
```text
1. Scope check - files changed and whether all are in Allowed Paths
2. Authority check - whether PRD/SRD/locked-principles/spec contracts changed
3. Safety check - redaction, credential, state machine, receipt schema, PlatformResult, audio_transcript blocker
4. Validation result - commands run and observed results
5. Next gate - still-unapproved surfaces: workers, frontend, BBDown runtime, ffmpeg, ASR, audio_transcript, Phase 2-4 runtime
```
## Final Report Template
```text
T-P1A-NNN <title> state=<complete|blocked>.
1. Scope check: <files changed>
2. Authority check: <authority docs touched or untouched>
3. Safety check: <hard rules untouched>
4. Validation: <commands and results>
5. Next gate: <still not approved>
PR: <url>
Merge commit: <hash>
Workflow run: <id>
```
## High-Risk Extra Review
Add GitHub external audit when a task touches schema, migrations, state words, receipt schema, raw responses, credentials, redaction, LP text, Trust Trace DTO fields, or a new runtime gate such as BBDown, ffmpeg, ASR, browser, workers, or frontend.
Docs cleanup, retro, and template-only tasks do not require external audit unless they change authority wording.
## Deprecated Boilerplate
- 7-part Mandatory Self-Audit
- Separate Boundary / Authority / Enum / Next-gate audit blocks
- Local-only storage audit except for manual-auth tasks
## Template Maintenance
Template changes require a separate dispatch-template-revise task. Existing dispatch files are not retroactively rewritten.
