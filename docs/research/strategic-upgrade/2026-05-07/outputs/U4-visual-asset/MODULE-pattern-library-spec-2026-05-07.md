---
status: candidate / not-authority / not-runtime-approval
created_for: Cloud Prompt U4 Visual Asset Spine
requested_date: 2026-05-07
generated_in_session_date: 2026-05-06
write_enabled: false
claim_scope: spec-only; no production code modification; no dispatch authorization
---

# MODULE — pattern_library spec

> claim label: ≥95% for candidate registry / bidirectional contract; `needs_local_refresh` for actual PF-V Pattern A-J definitions.

## 1. Module mission

`pattern_library` turns repeated creative/operational moves into named, auditable patterns. PF-V already has 10 evolution patterns A-J, but without a registry those patterns are hard to reuse outside the current GPT Pro window. This module records pattern letter, domain, description, when-to-use, when-not-to-use, usage count, success rate, and example artifacts. It links directly to `visual_asset.pattern_tag`, but it can extend beyond image refinement into code refactor, copy, data extraction, and dispatch prompt shaping.

The module should feel like a single-creator pattern memory, not a corporate design system. It is allowed to be opinionated and compact. It is not a governance board, not a multi-user voting system, and not a replacement for prompt lineage.


## Source Register / 证据边界

- PRD-v2/SRD-v2 的稳定事实：ScoutFlow 是 single-user、local-first、SQLite + FS + state words 的 authority-first 工作台；当前不得自动批准 SaaS、多用户、runtime 扩张、media/ASR、browser automation、vault true write 或 migration。
- Capture Station 的已读事实：`apps/capture-station/package.json` 是 React 18 + Vite 5，未把 Tailwind/shadcn/Panda/Radix/React Flow/TanStack/Lucide 写成已批准依赖；现有 H5 代码使用深海蓝 palette、inline style、URL Bar + Vault Preview/Dry Run + Live Metadata + Capture Scope + Trust Trace 的工作台结构。
- Visual docs 的已读事实：`design-brief.md` 固定 4 面板扫描顺序；`five-gate-checklist.md` 要求 5 gate 全过才可称 visual pass；`trust-trace-graph-spec.md` 固定 `capture -> capture_state -> metadata_job -> probe_evidence -> receipt_ledger -> media_audio -> audit` 节点链。
- 本地缺口：容器内没有 `~/workspace/ScoutFlow`、没有 `~/.claude/rules/aesthetic-first-principles.md`、没有 PF-V 实际 `INDEX.csv`，因此相关内容均标为 `needs_local_refresh`。
- Live web 缺口：本运行环境禁用实时网页浏览；任何 vendor / 2026 工具状态只能列为待验证 URL 种子，不得写成已访问事实。

## 2. Domains

| domain | examples | guard |
|---|---|---|
| `image_refine` | H5 screenshot evolution, GPT-Image-2 reverse mockup | must link to assets when possible |
| `code_refactor` | screenshot-to-code guard, inline style normalization | candidate patch only |
| `copy` | panel microcopy, blocked lane wording | no authority claim |
| `data_extract` | CSV index normalization, artifact metadata pull | fail closed on unknown columns |
| `dispatch_prompt` | prompt shape for parallel agent tasks | not authorization |

## 3. SQLite DDL

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS pattern_entries (
  pattern_id TEXT PRIMARY KEY,
  domain TEXT NOT NULL CHECK (domain IN (
    'image_refine','code_refactor','copy','data_extract','dispatch_prompt'
  )),
  pattern_letter TEXT CHECK (pattern_letter IS NULL OR pattern_letter GLOB '[A-Z]*'),
  slug TEXT NOT NULL,
  description TEXT NOT NULL,
  when_to_use TEXT NOT NULL,
  when_not_to_use TEXT NOT NULL,
  usage_count INTEGER NOT NULL DEFAULT 0 CHECK (usage_count >= 0),
  success_rate REAL CHECK (success_rate IS NULL OR (success_rate >= 0 AND success_rate <= 1)),
  example_artifacts_json TEXT NOT NULL DEFAULT '[]',
  status TEXT NOT NULL DEFAULT 'candidate' CHECK (status IN ('candidate','active','deprecated')),
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(domain, slug)
);

CREATE INDEX IF NOT EXISTS idx_pattern_letter_domain
  ON pattern_entries(pattern_letter, domain);
CREATE INDEX IF NOT EXISTS idx_pattern_status
  ON pattern_entries(status);

CREATE TABLE IF NOT EXISTS pattern_artifact_links (
  pattern_id TEXT NOT NULL REFERENCES pattern_entries(pattern_id) ON DELETE CASCADE,
  asset_id TEXT NOT NULL,
  link_kind TEXT NOT NULL CHECK (link_kind IN ('example','source','counterexample','locked_output')),
  note TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY(pattern_id, asset_id, link_kind)
);

CREATE TABLE IF NOT EXISTS pattern_domain_stats (
  domain TEXT PRIMARY KEY,
  total_patterns INTEGER NOT NULL DEFAULT 0,
  total_uses INTEGER NOT NULL DEFAULT 0,
  avg_success_rate REAL,
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TRIGGER IF NOT EXISTS trg_pattern_entries_touch
AFTER UPDATE ON pattern_entries
BEGIN
  UPDATE pattern_entries SET updated_at = datetime('now') WHERE pattern_id = NEW.pattern_id;
END;
```

## 4. Candidate Pattern A-J v0

Actual PF-V Pattern A-J definitions were not available in this container. The following names are **candidate placeholders** designed to be overwritten or confirmed after PF-V INDEX/session notes are provided.

| letter | candidate name | domain first | description | when to use | when not to use |
|---|---|---|---|---|---|
| A | Anchor Screenshot | image_refine | Start from a raw screenshot or stable H5 frame and preserve IA before style changes. | When layout truth matters more than beauty. | When the source screenshot is already off-scope or misleading. |
| B | Palette Convergence | image_refine | Drive multiple generations toward the same deep-sea token family. | When outputs drift into random neon or marketing gradients. | When layout/semantics are still wrong. |
| C | Panel Spine Lock | image_refine | Keep URL → Metadata → Scope → Trust Trace scan order fixed. | When experimenting with component surfaces. | When the goal is non-H5 illustration. |
| D | State Weight Contrast | image_refine | Make allowed/current/blocked/candidate visually distinct by weight and wording. | When blocked lane looks too active. | When status semantics are not known. |
| E | Trust Trace Semantic Graph | image_refine | Render graph as dependency chain, not decorative network. | When right panel needs deep inspection clarity. | When graph would hide text/list fallback. |
| F | Token Visual Extract | image_refine | Convert a successful mockup into token swatches and reusable visual rules. | When 2+ images converge on same palette. | When the image is still a one-off moodboard. |
| G | Negative Prompt Guard | image_refine | Explicitly ban SaaS admin, hero, sidebar, cyberpunk, decorative KPI. | When generation keeps importing wrong genre. | When negative list becomes longer than actual objective. |
| H | 5-Gate Repair Loop | image_refine | Fail one gate at a time and regenerate/annotate only that failure. | When close to locked but one gate fails. | When the entire layout is wrong. |
| I | Code Translation Boundary | code_refactor | Convert visual intent to CSS/React seams without package or donor transplant. | When image-to-code tooling is tempting. | When production code approval is absent. |
| J | Handoff Lock | dispatch_prompt | Package asset, prompt, token, gate result, and next action into audit-ready handoff. | When a phase closes or an asset becomes reusable. | When unresolved gate failures remain. |

## 5. Python CRUD + bidirectional link (candidate ≤300 LOC)

```python
#!/usr/bin/env python3
from __future__ import annotations
import json, sqlite3, uuid
from pathlib import Path
DB = Path('pattern-library/patterns.sqlite')

def con():
    DB.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    c.execute('PRAGMA foreign_keys=ON')
    return c

def add_pattern(domain, letter, slug, description, when_to_use, when_not_to_use):
    pid = f'pa_{uuid.uuid4().hex[:16]}'
    with con() as db:
        db.execute("""INSERT INTO pattern_entries
          (pattern_id, domain, pattern_letter, slug, description, when_to_use, when_not_to_use)
          VALUES (?,?,?,?,?,?,?)""",
          (pid, domain, letter, slug, description, when_to_use, when_not_to_use))
    return pid

def link_asset(pattern_id, asset_id, kind='example', note=None):
    with con() as db:
        db.execute("""INSERT OR REPLACE INTO pattern_artifact_links
          (pattern_id, asset_id, link_kind, note) VALUES (?,?,?,?)""",
          (pattern_id, asset_id, kind, note))

def record_use(pattern_id, success: bool | None):
    with con() as db:
        row = db.execute('SELECT usage_count, success_rate FROM pattern_entries WHERE pattern_id=?', (pattern_id,)).fetchone()
        if not row: raise SystemExit('missing pattern')
        n = row['usage_count'] + 1
        if success is None:
            rate = row['success_rate']
        else:
            prev_successes = (row['success_rate'] or 0) * row['usage_count']
            rate = (prev_successes + (1 if success else 0)) / n
        db.execute('UPDATE pattern_entries SET usage_count=?, success_rate=? WHERE pattern_id=?', (n, rate, pattern_id))
```

## 6. Relationship to visual_asset

`visual_asset.pattern_tag` is a fast denormalized tag for filtering. `pattern_artifact_links` is the richer relation. When both exist, they must agree:

```sql
SELECT v.asset_id, v.pattern_tag, p.pattern_letter, p.slug
FROM visual_assets v
JOIN pattern_artifact_links l ON l.asset_id = v.asset_id
JOIN pattern_entries p ON p.pattern_id = l.pattern_id
WHERE v.pattern_tag IS NOT NULL
  AND p.pattern_letter IS NOT NULL
  AND v.pattern_tag <> p.pattern_letter;
```

If this query returns rows, the registry should block lock/handoff until the mismatch is resolved.

## 7. Extension rules

- New letters after J may exist, but must not reuse A-J semantics.
- A pattern can span domains, but the canonical row has one primary domain; add sibling rows for cross-domain adaptation.
- A pattern with success_rate below 0.35 after 10 uses should be deprecated or rewritten.
- Example artifacts should include both successes and counterexamples. Counterexamples are vital for negative prompt guard and 5-Gate repair.

## 8. Acceptance checklist

- A-J placeholders are clearly marked and replaceable.
- Pattern links can reference visual assets without making visual_asset depend on pattern DB at insert time.
- Usage stats cannot be gamed into a pass/fail authority claim.
- Dispatch patterns state non-authorization boundary.
- Pattern library supports image/code/copy/data/dispatch domains in one local registry.


## 9. Pattern record anatomy

A useful pattern entry should be operational, not poetic. It should answer five questions:

```yaml
pattern_id: pa_...
letter: E
slug: trust-trace-semantic-graph
domain: image_refine
input_signal: "graph looks decorative or hides node labels"
move: "restore canonical node chain, active path, downgraded blocked edge"
output_signal: "node order and edge direction match Trust Trace spec"
counterexample: "freeform glowing network background"
```

This anatomy makes the pattern reusable by an image prompt, a visual audit, and a code review prompt. If a pattern cannot be written in this shape, it may be a mood preference rather than a pattern.

## 10. Cross-domain adaptations

A pattern letter can inspire sibling patterns in other domains, but the sibling should use its own slug and primary domain.

| source pattern | adapted domain | adaptation |
|---|---|---|
| A Anchor Screenshot | data_extract | anchor CSV mapping to real headers before transforming rows |
| C Panel Spine Lock | code_refactor | prevent React refactor from changing panel order |
| D State Weight Contrast | copy | write explicit `blocked/candidate/allowed` microcopy |
| G Negative Prompt Guard | dispatch_prompt | include forbidden outputs and boundary stop rules |
| H 5-Gate Repair Loop | code_refactor | patch one visual failure at a time, not broad restyle |
| J Handoff Lock | data_extract | package stdout, row counts, and unresolved gaps |

This prevents the image library from becoming isolated. The same mental moves can guide code, copy, data, and dispatch without pretending every pattern is a UI component.

## 11. Success-rate interpretation

Success rate is a rough local memory. It should not be used as an authority gate. A pattern with low success may still be valuable if it catches rare catastrophic failures, such as `dispatch_auth_leak` or `browser_automation_unlock`. A pattern with high success may still be inappropriate for a new domain. The pattern registry should display success rate with sample size:

```text
Pattern H — 5-Gate Repair Loop
uses: 14
success_rate: 0.71
last_counterexample: va_bad_mobile_toast_003
recommendation: active, but inspect gate-specific notes
```

## 12. Counterexample library

Counterexamples are first-class. For visual work, negative examples often teach more than success images. Store them as `pattern_artifact_links.link_kind='counterexample'` and keep the failure note short:

```yaml
asset_id: va_counter_sidebar_001
pattern: G
failure: "generic SaaS admin sidebar; violates 4-panel scan order"
reuse: "negative prompt example only"
```

Counterexamples should never be accidentally selected by the cross-phase reuse query for positive reference. That is why `link_kind` matters.

## 13. Pattern seeding command

```text
pattern-library seed-a-j --placeholder-only
pattern-library update --letter E --slug trust-trace-semantic-graph --from-file pattern-e.md
pattern-library link --letter E --asset-id va_... --kind example
pattern-library link --letter G --asset-id va_bad_... --kind counterexample
pattern-library use --letter H --success true --note "fixed gate 3 mobile occlusion"
```

The command should print whether a placeholder was replaced. If a placeholder is still active, downstream reports should show `placeholder_definition: true` so a later user audit does not confuse candidate names with PF-V canon.

## 14. Dispatch prompt safety pattern

Any `dispatch_prompt` pattern must include a stop rule. Example:

```text
When asked to produce code-bearing work, stop unless the current lane explicitly authorizes production patch.
When asked to cite live web, stop or mark unverified if browsing is disabled.
When asked to write vault/capture authority, stop unless write_enabled is true and the relevant gate is open.
```

This keeps pattern reuse aligned with ScoutFlow's authority-first discipline.


## 15. Pattern review cadence

A practical cadence is phase-based rather than daily. At the end of each PF-V phase, review:

```text
patterns used
assets linked
counterexamples added
success_rate changes
patterns that caused drift
patterns that deserve promotion from placeholder to active
```

This keeps the pattern library light. The user should not have to curate every generation. Only patterns that explain repeated wins or repeated failures deserve updates.

## 16. Promotion from placeholder to active

A placeholder can become active when three conditions are met:

1. It has at least one positive example asset.
2. It has at least one counterexample or clear `when_not_to_use` rule.
3. The user can explain the pattern in a sentence without referencing a private chat window.

Promotion does not require enterprise review. It is a local memory quality threshold.

## 17. Pattern conflict handling

Patterns can conflict. Pattern B may push palette convergence while Pattern D may demand stronger status contrast. The conflict resolver is the 5-Gate audit: if palette convergence makes blocked lanes too pretty or too active, Gate 5 wins. If a pattern conflicts with ScoutFlow boundaries, boundaries win before aesthetics. This hierarchy should be printed in pattern audit reports so creative work does not override system truth.

## 18. Pattern markdown export

Each pattern should export to a single markdown card:

```text
# Pattern E — Trust Trace Semantic Graph
Status: candidate/active
Use when: graph is becoming decorative
Do not use when: list fallback is missing
Positive assets: va_...
Counterexamples: va_...
Prompt snippet: "render dependency chain, not network background"
Gate risks: Gate 3 occlusion, Gate 5 visual weight
```

Markdown cards make the pattern library usable outside SQLite and easy to feed back into prompts.


## 19. Pattern prompt snippets

Each active pattern should expose a short reusable snippet. Examples:

```text
Pattern C: preserve URL → Metadata → Scope → Trust Trace scan order; do not introduce sidebar-first admin IA.
Pattern D: current/allowed/blocked/candidate must differ by text, badge, contrast, and weight; color alone is insufficient.
Pattern H: repair exactly one failed gate; do not restyle unrelated surfaces.
```

Snippets should be short enough to combine. If a snippet becomes a full prompt, it belongs in `prompt_template`, not `pattern_library`.

## 20. Pattern retirement

A pattern should retire when it no longer predicts success or when it encodes a phase-specific taste. Retirement is healthy. The old row stays for audit, but `status='deprecated'` removes it from default prompt snippets and reuse recommendations.


## Appendix C — success rate calculation

`success_rate` 不应追求统计学严肃性；它是单人复用提示灯。建议每次 pattern 被使用后记录 `outcome ∈ {success, partial, fail, unknown}`，计算时把 success 记 1、partial 记 0.5、fail 记 0、unknown 不计入分母。少于 3 次使用的 pattern 标记为 `low_sample=true`，避免一个偶然成功的视觉套路被误认为稳定策略。

pattern 的成功定义按 domain 分开：image_refine 看 5-Gate 与视觉复用；code_refactor 看测试和边界保持；copy 看是否减少歧义；data_extract 看字段完整性与证据可追溯；dispatch_prompt 看 agent 是否少问澄清且不越权。这样 A-J 可以先来自 PF-V，再自然延伸到代码、文案、数据、调度，而不会把“修图套路”硬套到所有工作。
