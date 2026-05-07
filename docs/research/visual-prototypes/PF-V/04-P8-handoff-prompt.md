---
title: PF-V P8 Handoff Prompt — for GPT Pro to write final P8 deliverables
status: candidate / batch_handoff_prompt / not-authority
created_at: 2026-05-07
purpose: After P7 success (25 min, 76 files V-PASS), use GPT Pro to author P8 handoff documentation that CC0 will then audit + apply + open PR for
target: GPT Pro web (云端，thinking mode, 15-25 min run)
---

# How to use this file

1. CC0 builds `pfv-p8-bundle.zip` (~1MB) via `scripts/build-p8-bundle.sh`.
2. User opens NEW GPT Pro session (clean context).
3. Upload `pfv-p8-bundle.zip` (drag/drop into chat).
4. Paste the **P8 PROMPT** from this file (the fenced block below).
5. GPT Pro thinks 15-25 min, outputs 6 markdown files via canvas / file attachment.
6. User downloads outputs to `~/Downloads/PF-V-P8-output/`.
7. User tells CC0 "P8 ZIP 下好了".
8. CC0 audits 6 markdown outputs, applies patches to PF-V files, moves P7 output into `p7-output/`, updates INDEX, creates branch + commit, opens PR with the GPT-Pro-authored PR description.

---

# P8 PROMPT (paste this block after uploading bundle)

```
===BEGIN PF-V P8 HANDOFF PROMPT===

# § 0  Role + Scope

You are authoring the **final P8 handoff documentation bundle** for ScoutFlow's PF-V Visual Prototype Lane. P0-P7 are complete (152 mockup images + 76-file rough HTML5 wireframe output). Your job is to produce **6 markdown files** that CC0 (Claude Code, local) will audit + apply + commit + open a PR for.

You DO produce (6 markdown files, exact filenames required):
1. `05-HANDOFF-to-PF-C4-protocol.md` — formal v1 handoff contract (replaces v0 candidate from input)
2. `P8-PR-DESCRIPTION.md` — complete PR body markdown
3. `P8-PF-V-README-PATCH.md` — patch instructions for `PF-V-README.md` (§1 PM table P7+P8 ✅ + new "P8 closure" section)
4. `P8-LESSONS-PATCH.md` — append-only L12 + L13 entries to LESSONS-LEARNED
5. `P8-ACCEPTANCE-CHECKLIST.md` — 30-item checklist for PF-C4 lane to run when receiving the PR
6. `P8-CHANGELOG-ROW.md` — single-row entry for adding to a future docs/CHANGELOG.md if applicable

You DO NOT produce:
- Any code changes (HTML / CSS / SVG / TSX / Python / SQL)
- Any actual file deletions or moves (CC0 does the file ops)
- Any commands (no git / no shell / no npm)
- Any new image generation (P0-P6 image phase is closed)
- Direct edits to PF-V authoritative files (you produce PATCHES, CC0 applies)

# § 1  Input materials in the uploaded ZIP

The ZIP contains:
```
pfv-p8-bundle.zip
├── p7-output/                                    ← 76 files GPT Pro produced 25 min ago (your output to deliver)
│   ├── tokens.css, density-compact.css, type-weight-heavy.css
│   ├── html5-rough/*.html (13 surfaces) + *.module.css + *.model.json
│   ├── css-modules-candidate/*.module.css + *.html (15 components)
│   ├── icons/system.svg + state.svg
│   ├── MAPPING.md
│   └── README.md
├── PF-V-README.md                                ← lane overview + 16-session PM table
├── PF-V-INDEX.csv                                ← 152 image rows, 19-column schema
├── PF-V-LESSONS-LEARNED.md                       ← L1-L11 captured during P0-P6
├── PF-V-MAINTENANCE-PROTOCOL.md                  ← 7-step per-session routine
├── PF-V-03-P7-batch-prompt-v2.md                 ← P7 prompt + P8 backlog table
├── PF-V-05-HANDOFF-protocol-v0-candidate.md      ← v0 placeholder you replace
├── PF-V-00-master-context.md                     ← 15-token system + anti-patterns
├── PROJECT-CLAUDE.md                             ← project-root sidecar rules
└── P8-PROMPT.md                                  ← this prompt (canonical reference)
```

Read all input files. Authority hierarchy:
1. PROJECT-CLAUDE.md — top (sidecar reviewer rules, single-writer constraints)
2. PF-V-README.md — lane overview, what's done
3. PF-V-LESSONS-LEARNED.md — captured judgments, do not contradict
4. PF-V-INDEX.csv — image inventory (152 rows, V-verdict per image)
5. p7-output/ — actual deliverable (your handoff target)
6. PF-V-05-HANDOFF-protocol-v0-candidate.md — v0 baseline you replace, not authority

# § 2  Authority + Boundary (do not violate)

ScoutFlow project rules (from PROJECT-CLAUDE.md):
- PF-V is a research lane in `docs/research/visual-prototypes/PF-V/`. NOT runtime code.
- PF-V outputs MAY be referenced by future PF-C4-01 lane but are NOT authoritative implementation source.
- All deliverables are **candidate / not-authority**, status frontmatter must reflect this.
- Active product lane max=3, authority writer max=1. PF-V occupies one research lane slot.
- Authority files (`docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`) are NOT touched by P8.
- Single-writer constraint: only the designated CC0 writes authority docs. P8 outputs are research lane edits.

Boundary you must respect:
- ScoutFlow delivers clean Markdown to `~/workspace/raw/00-Inbox/` (Obsidian raw vault inbox).
- Enrich / wiki backfill / knowledge flywheel happens **inside Obsidian**, NOT in ScoutFlow.
- PF-V handoff to PF-C4 is **local frontend bootstrap reference**, NOT production component delivery.
- PF-C4 lane decides its own React TSX conventions; P7 output is rough wireframe reference only.

# § 3  Deliverable spec for each of the 6 markdown files

---

## 3.1  `05-HANDOFF-to-PF-C4-protocol.md` (replaces v0)

**Purpose**: Formal contract from PF-V to PF-C4-01 Local Frontend Bootstrap lane.

**Required frontmatter**:
```yaml
---
title: PF-V → PF-C4 Handoff Protocol v1 (post-P7 finalized)
status: candidate / handoff_contract / not-authority
authority: not-authority
from_lane: PF-V (Visual Prototype Lane, P0-P8)
to_lane: PF-C4-01 (Local Frontend Bootstrap)
date: 2026-05-07
supersedes: 05-HANDOFF-to-PF-C4-protocol.md (v0 candidate, 2026-05-06)
---
```

**Required sections**:
1. **§1 What you receive** — list ALL deliverables PF-C4 gets:
   - 152 source mockup PNGs (in `docs/research/visual-prototypes/PF-V/images-P*/`)
   - INDEX.csv (152 rows, 19 columns, source of truth for image provenance)
   - p7-output/ (13 H5 + 30 component css/html + 2 SVG sprite + tokens.css + 3 override CSS + MAPPING + README)
   - LESSONS-LEARNED.md (L1-L13, design decisions captured during PF-V)
   - master-context.md (token system definitions, anti-patterns, language policy)

2. **§2 What PF-C4 should DO with each deliverable** — explicit consumption guide:
   - p7-output/html5-rough/*.html → read for IA + state class semantics
   - p7-output/tokens.css → import as global CSS Variables (single source of truth)
   - p7-output/css-modules-candidate/ → translate to actual CSS Modules in component folders
   - p7-output/icons/*.svg → use via `<svg><use href>` reference, NOT inline copy
   - LESSONS-LEARNED → respect L8 sync badge cross-system pattern, L11 orthogonal density×typography matrix

3. **§3 What PF-C4 must NOT do** — explicit reject list:
   - Do not import raw HTML at runtime (wireframe only)
   - Do not copy class names verbatim (translate via React/CSS Module conventions)
   - Do not hardcode hex outside tokens.css
   - Do not adopt Tailwind / shadcn / Panda (zero-install policy)
   - Do not mock vault path differently from `~/workspace/raw/00-Inbox/` (Obsidian boundary)
   - Do not mutate PF-V research lane files; PF-C4 lane writes its own TSX

4. **§4 TODO placeholders inventory** — every `<!-- TODO -->` in p7-output/ enumerated with:
   - File + line number
   - Reason (what dynamic / library / data wiring is needed)
   - Suggested implementation library (D3 / vis-network / cytoscape / etc)
   - Priority (P0 = blocks PF-C4 first commit / P1 = post-skeleton / P2 = polish)

5. **§5 Density × Typography matrix** — explain the 100-cell orthogonal config space:
   - density: V1-V10 spectrum (S17), recommended baseline = V3 Compact
   - typography: V1-V10 spectrum (S18), recommended baseline = V4 Weight Heavy
   - PF-C4 may toggle by importing density-compact.css / type-weight-heavy.css as additive layers

6. **§6 Cross-system Sync semantic** — sync-badge component contract:
   - 3-tier states: synced / pending / external-changed
   - Always paired with state.svg icons (success / warning / focus)
   - Pattern propagates wherever ScoutFlow ↔ Obsidian data interaction occurs (per LESSONS L8)

7. **§7 Acceptance criteria for PF-C4 to "receive" the handoff** — the moment PF-C4 declares ready to start implementation:
   - All 76 files in p7-output/ verified rendering correctly in browser
   - tokens.css + override CSSes confirmed lossless when copied to PF-C4 codebase
   - 30-item ACCEPTANCE-CHECKLIST (separate file) all green
   - PF-C4 lane opens its own first PR (e.g., `feat(capture-station): scaffold p7-reference`)

8. **§8 Risk register + acknowledgements** — known frictions PF-C4 should be aware of:
   - PF-V mockups are 1152px wide (resized from 2K source); pixel-perfect implementation is NOT goal
   - Some surfaces use `<dialog open>` natively; older browsers need polyfill (deferred to PF-C4 to decide)
   - Container queries used over @media; Safari < 16 fallback may be needed
   - 13 model.json files are bonus; PF-C4 may ignore if React component tree differs from JSON model

9. **§9 P8 deferred items (from CC1 audit)** — re-state the 5 candidate references from `PF-V-03-P7-batch-prompt-v2.md` "P8 Handoff Backlog" section:
   - U7 props_json schema (for React component props interface)
   - U4 visual_asset SQLite schema (for asset state machine)
   - U4 PF-V-INTEGRATION-MAP (for INDEX → table migration)
   - U8 HANDOFF-MANIFEST schema (for downstream variants)
   - U13 PANEL spec (for state grammar cross-validation)

10. **§10 Sign-off statement** — PF-V lane closes with this handoff; future updates only via PF-C4-initiated changes.

Total length expectation: 2500-3500 words. Bilingual headers (EN + 中文 sub-line) acceptable but body 中文 prose preferred (matching PF-V doc convention).

---

## 3.2  `P8-PR-DESCRIPTION.md`

**Purpose**: Complete PR body markdown that CC0 will paste into `gh pr create --body` when opening the P8 PR.

**Required structure**:
```markdown
## PF-V → PF-C4 Handoff (P8 Final)

[1-paragraph summary: what landed, why, what PF-C4 gets]

### What landed in this PR
- [bulleted list, ≤ 10 bullets]

### What this PR does NOT do
- [what's deferred to PF-C4 lane, ≤ 5 bullets]

### Files added / changed
[checklist of PF-V/ tree changes, organized by category]

### How to verify locally (zero-install)
```bash
cd docs/research/visual-prototypes/PF-V/p7-output/
python3 -m http.server 8080
# open http://localhost:8080/html5-rough/00-app-shell.html
```

### LESSONS captured in this PR
- L12: [headline]
- L13: [headline]

### Acceptance criteria
[link to ACCEPTANCE-CHECKLIST.md]

### Test plan
- [ ] [checklist item 1]
...

### Risk register
- [3-5 known frictions]

### Sign-off
PF-V lane closes after this PR merges. Reviewer: any one CC0/CC1/Codex assigned to PF-C4-01 lane.
```

Total length: 800-1500 words.

---

## 3.3  `P8-PF-V-README-PATCH.md`

**Purpose**: Specific patch instructions for `PF-V-README.md`. CC0 will read this and apply patches manually (no machine-applicable diff format needed; markdown narrative patch).

**Required content**:
- §A: Update the §1 PM table — mark P7 ✅ (76 files / 25 min one-shot V-PASS) and P8 ✅ (handoff complete)
- §B: Update the "remaining" line from "P7 + P8 ≈ 30-50 min" to "全部完成 ✅ — 总耗时 ~210 min user 时间 / ~3.5h"
- §C: Append a NEW section §13 "P7+P8 收尾总结" with:
  - 152 张图 / 16 sessions / 总耗时 / 总产出
  - P7 一次出齐零返修的关键设计因子（token discipline / 三步 pipeline / TODO placeholder / caption-as-spec）
  - 移交链：PF-V (research lane) → PF-C4-01 (Local Frontend Bootstrap implementation)
- §D: Update header status from "in_progress" to "complete-handed-off"
- §E: Add file pointer: `→ p7-output/` directory + `05-HANDOFF-to-PF-C4-protocol.md` v1

Total length: 600-1000 words.

---

## 3.4  `P8-LESSONS-PATCH.md`

**Purpose**: Append-only L12 + L13 entries (new lessons) for `PF-V-LESSONS-LEARNED.md`.

**L12 — P7 一次出齐零返修（GPT Pro batch image-to-HTML5 工作流验证）**:
- **事件**: P7 batch (65 task / 76 输出文件) GPT Pro thinking mode 25 min 一次出齐，CC0 audit V-PASS 0 反模式
- **根因**: prompt v2 三个关键设计共同作用 — (a) 三步 pipeline 强制 image→JSON→HTML 中间模型 self-check (b) tokens.css 完整 paste-ready 写进 prompt 不让 GPT 自创 (c) 65 task 段引用具体 ZIP 文件名一一对应 0 歧义
- **后效**: 节省 P7 预估的 1-2h 到实测 25 min；CC0 audit 时间从估 30 min 降到 ~10 min（因为零反模式无需 delta correction）
- **对下游影响**: 0 — PF-C4 lane 收到的是已 V-PASS 干净 wireframe
- **预防 rule**: 任何 batch 转码 / 综合产出类 prompt，强制三步 pipeline + paste-ready 关键 schema + 1-to-1 file mapping。不要让 LLM 自由发挥关键 schema。

**L13 — caption-as-spec + 二维矩阵 spec 都在 P7 实战印证（LESSONS L10/L11 升级）**:
- **事件**: S17 density × S18 typography 各 10 张梯度图 + caption-as-spec 设计，PF-C4 可正交叠加 100 个配置
- **根因**: P7 prompt 把 V3 Compact + V4 Heavy 都生成单独 H5 + override CSS 文件，PF-C4 切换 toggle 直接 import override layer 不动 IA
- **后效**: PF-C4 lane 实施时 density / typography 切换是配置而非重写，节省未来调整时间
- **预防 rule**: 任何"轴梯度 + 基线 + override layer"模式都该走这条路；不要让 PF-C4 通过 prop drilling 切换 token

Total length: 500-800 words.

---

## 3.5  `P8-ACCEPTANCE-CHECKLIST.md`

**Purpose**: 30-item checklist for PF-C4 lane to run as a single audit pass when receiving the PR. Each item is a single line `- [ ] description` with optional verify command.

**Required categories** (suggest 5 items per category):
1. File presence (all 76 p7-output files exist + 152 PNG images present)
2. Token discipline (tokens.css all 19 vars defined; zero hex in any *.module.css)
3. Semantic HTML (zero `<div>` proliferation; all use `<main>/<section>/<header>/<dialog>/<table>`)
4. Anti-pattern absence (no Tailwind class / no inline style / no English UI strings)
5. Cross-system / boundary (vault path 100% `~/workspace/raw/00-Inbox/`; Obsidian flywheel boundary respected in tooltips)
6. PF-C4 readiness (PF-C4 lane can open first commit; CSS Modules can be 1:1 ported; SVG sprites usable via `<use>`)

Each line should be actionable and verifiable. Example:
```
- [ ] tokens.css contains all 15 color tokens + 4 derived bg + typography + spacing + radius + shadow vars (verify: grep -c "^  --" p7-output/tokens.css)
- [ ] zero hex value outside tokens.css (verify: rg "#[0-9a-f]{3,6}" p7-output/ --type css | grep -v tokens.css | wc -l == 0)
- [ ] all 13 surface HTML files render in browser without console errors
- [ ] all 65 input images referenced in MAPPING.md (verify: grep -c "^| [0-9]" p7-output/MAPPING.md == 65)
- [ ] icon-blocked dual semantic correctly implemented (system.svg = padlock+X, state.svg = circle+slash)
- [ ] cross-system sync-badge has 3 tiers (synced/pending/external-changed) used in 08-topic-card-vault
```

Total length: 800-1200 words / 30 checklist items.

---

## 3.6  `P8-CHANGELOG-ROW.md`

**Purpose**: Single-row markdown for inserting into a future `docs/CHANGELOG.md` (if it exists; if not, CC0 may skip this).

Format:
```markdown
## 2026-05-07 PF-V Visual Prototype Lane closure (P0-P8)

- 152 张 mockup PNG + 76-file rough HTML5 wireframe handoff to PF-C4-01 Local Frontend Bootstrap lane
- 16 sessions / 总耗时 ~3.5h / 净产出 152 image + 13 H5 + 30 css module + 2 SVG sprite + tokens.css
- Key wins: P7 一次出齐零返修（25 min）/ caption-as-spec + 二维矩阵 spec 设计 / 知识飞轮边界视觉化
- Closes: PF-V lane (research lane closed; PF-C4-01 takes over implementation)
```

Total length: 100-300 words.

# § 4  Output structure

Deliver as ONE downloadable ZIP file named `PF-V-P8-output.zip` containing exactly these 6 markdown files at root:

```
PF-V-P8-output.zip
├── 05-HANDOFF-to-PF-C4-protocol.md
├── P8-PR-DESCRIPTION.md
├── P8-PF-V-README-PATCH.md
├── P8-LESSONS-PATCH.md
├── P8-ACCEPTANCE-CHECKLIST.md
└── P8-CHANGELOG-ROW.md
```

NO subdirectories. NO extra files (no images, no css, no html). NO bundled README.md (the protocol IS the README).

# § 5  Anti-patterns (any one present = REGENERATE that file)

- ❌ Authority claim — frontmatter MUST say `status: candidate / not-authority`
- ❌ Implementation prescriptions — do not tell PF-C4 which React framework / state library to use; only WHAT to deliver and WHAT NOT to do
- ❌ Re-litigating PF-V design decisions — LESSONS L1-L11 are settled, do not second-guess
- ❌ Adding new design (no new color tokens / no new icons / no new components — P0-P7 is closed)
- ❌ Touching authority files (no patches to docs/current.md / docs/task-index.md / docs/decision-log.md)
- ❌ Marketing / hype language — handoff doc is contractual, not promotional
- ❌ English-only handoff body — PF-V convention is bilingual; CN body + EN technical terms acceptable
- ❌ Promising features not in p7-output/ — only describe what actually exists in the bundle

# § 6  Self-verification before delivery

- [ ] Read all 8 input PF-V files (README / INDEX / LESSONS / MAINTENANCE / 03-prompt-v2 / 05-handoff-v0 / master-context / PROJECT-CLAUDE)
- [ ] Read p7-output/MAPPING.md + README.md to confirm what was actually delivered
- [ ] All 6 outputs reference real files / real LESSONS IDs / real INDEX rows (no fabricated entries)
- [ ] frontmatter `status: candidate / not-authority` on `05-HANDOFF-to-PF-C4-protocol.md`
- [ ] L12 + L13 lesson body uses LESSONS-LEARNED's existing format (事件 / 根因 / 修法 / 后效 / 对下游影响 / 预防 rule)
- [ ] PR description includes Test plan checklist
- [ ] ACCEPTANCE checklist 30 items cover all 6 categories evenly
- [ ] vault path 100% `~/workspace/raw/00-Inbox/` (no `~/scoutflow-vault/` virtual paths)
- [ ] Cross-system sync badge L8 pattern referenced
- [ ] Knowledge flywheel boundary L2 respected (ScoutFlow ends at Obsidian inbox)

# § 7  When uncertain

If you find:
- Conflicting information between PF-V files → trust LESSONS-LEARNED most recent (L11), then INDEX.csv, then README, then v0 handoff
- Missing reference (e.g., a TODO mentions a file that doesn't exist in p7-output) → flag in §8 risk register, do NOT fabricate
- Authority unclear (does PF-V close PR or PF-C4 take over?) → PF-V closes lane; PF-C4 opens a fresh lane after PR merges
- Bundle file is corrupted / unreadable → stop, report file name, ask for re-upload (do not produce partial output)

===END PF-V P8 HANDOFF PROMPT===
```

---

# Notes for CC0 (post-receipt audit)

When user returns with `~/Downloads/PF-V-P8-output/` containing 6 markdown files:

1. **Audit phase** (~5-10 min):
   - Read all 6 files
   - Cross-check against INDEX / LESSONS / p7-output for factual accuracy
   - Verify frontmatter `status: candidate / not-authority` on handoff doc
   - Check anti-patterns from § 5 are absent
   - Spot-check ACCEPTANCE checklist items are runnable

2. **Apply phase** (~10 min):
   - `mv ~/Downloads/PF-V-P7-output docs/research/visual-prototypes/PF-V/p7-output`
   - `cp ~/Downloads/PF-V-P8-output/05-HANDOFF-to-PF-C4-protocol.md docs/research/visual-prototypes/PF-V/05-HANDOFF-to-PF-C4-protocol.md` (replaces v0)
   - Apply README patches per `P8-PF-V-README-PATCH.md` instructions
   - Apply LESSONS patches per `P8-LESSONS-PATCH.md` (append-only, never edit existing L1-L11)
   - Save `P8-ACCEPTANCE-CHECKLIST.md` to `docs/research/visual-prototypes/PF-V/06-ACCEPTANCE-CHECKLIST.md`
   - Optionally create / update `docs/CHANGELOG.md` with row from `P8-CHANGELOG-ROW.md`
   - Update INDEX.csv if needed (P7 output rows can be added as supplementary)

3. **Commit + PR** (~5 min):
   - `git checkout -b feat/pf-v-p8-handoff`
   - `git add docs/research/visual-prototypes/PF-V/`
   - `git commit -m "feat(pf-v): P8 handoff to PF-C4 — 152 PNG + 76 H5/CSS/SVG bundle"`
   - `gh pr create --title "..." --body "$(cat ~/Downloads/PF-V-P8-output/P8-PR-DESCRIPTION.md)"`

4. **Notify user**:
   - Output PR URL
   - Suggest next step: PF-C4-01 lane bootstrap (separate session)
   - Update memory with PF-V lane closure note
