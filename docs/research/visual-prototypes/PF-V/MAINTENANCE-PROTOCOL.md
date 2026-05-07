---
title: PF-V Lane Maintenance Protocol — Per-Session Routine
status: candidate / protocol / not-authority
created_at: 2026-05-07
purpose: HARD checklist Claude (CC0) MUST run after EACH session output to prevent drift / lost data / orphan references
---

# Why this exists

PF-V lane runs at 5-10 min/session. Without explicit checklist, easy to:
- Move images but forget INDEX.csv
- Update master-context but forget README sync
- Skip sessions but forget update plan
- Make a tradeoff but forget capture lesson

This protocol locks the routine. **Claude (CC0) MUST execute this checklist after every session before moving on.**

# After every session (S0X) — 7-step checklist

```
[1] Read all N images from ~/Downloads/gptPRO图片/
[2] Map each image to variant axis (V1-VN)
[3] Per-image verdict (5-Gate + anti-pattern + token + language + path)
[4] Move + rename to images-P{phase}-{surface}/ with pattern: pfv-S{N}-V{V}-cn-{descriptor}[-TOP{X}].png
[5] APPEND row(s) to 04-INDEX.csv with all 19 fields filled
[6] If session revealed lesson → APPEND to LESSONS-LEARNED.md
[7] Update README §1 PM table to mark session ✅ + add TOP picks to that row
```

**No exceptions.** If user says "下个 session 直接给 prompt"，still complete steps 1-7 first, then give prompt.

# After significant decision (跳过 session / 合成 anchor / 工作流变更)

```
[A] Update README PM table to reflect decision
[B] Append decision rationale to LESSONS-LEARNED.md as new L# entry
[C] If decision affects future prompts → update 01-session-prompts-P0-to-P6.md
[D] If decision affects ALL future sessions → update 00-master-context.md
```

# After master-context update (any reason)

```
[X] Edit 00-master-context.md
[Y] Cross-reference: do other docs (README / 01-session-prompts / LESSONS) need echo?
[Z] Verify Self-verification checklist in master-context still covers the new constraint
```

# Per-phase milestones

After each PHASE complete (P0 / P1 / P2 / P3 / P4 / P5 / P6):

```
[α] Run quick INDEX query: 该 phase 所有 session 是否都有 row?
[β] Validate: 每 session 至少 1 个 V-PASS row?
[γ] If gap → either re-shoot OR document why intentional in LESSONS
[δ] Update README §1 phase status from 🟡 to ✅
```

# Per-trio sync (every 3 sessions)

```
[i] Compare TOP picks across sessions — visual consistency check (palette / typography / mood)
[ii] If divergence detected — either anchor refresh OR document tolerance in LESSONS
[iii] Quick spot-check super-anchor inheritance still strong
```

# Critical anti-patterns CC0 MUST NOT do

| Anti-pattern | Why bad |
|---|---|
| ❌ Move image without filling INDEX | Loss of provenance, can't reconstruct verdict graph at P8 |
| ❌ Update master-context without README cross-sync | docs drift, future user confused which is canonical |
| ❌ Skip session without updating PM plan | Plan becomes fictional, user loses trust in tracking |
| ❌ Discover lesson but not capture | Same mistake recurs in next session |
| ❌ Give next session prompt before completing 7-step checklist | Compounds debt, user catches it eventually (like S10 INDEX gap) |

# This protocol's own maintenance

If a new gap pattern emerges (like S10 INDEX gap revealed routine缺失):
1. Add new step to 7-step checklist
2. Document in LESSONS-LEARNED.md as L# entry
3. Sync to README §11 if behavior change spans phases

**This protocol IS the prevention. If CC0 follows it, future sessions don't compound debt.**
