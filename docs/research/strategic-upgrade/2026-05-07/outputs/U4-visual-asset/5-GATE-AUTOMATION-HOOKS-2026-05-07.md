---
status: candidate / not-authority / not-runtime-approval
created_for: Cloud Prompt U4 Visual Asset Spine
requested_date: 2026-05-07
generated_in_session_date: 2026-05-06
write_enabled: false
claim_scope: spec-only; no production code modification; no dispatch authorization
---

# 5-GATE AUTOMATION HOOKS — visual_asset state machine

> claim label: ≥95% for hook design; `needs_local_refresh` for canonical `~/.claude/rules/aesthetic-first-principles.md` because the file was not present in this container.

## 1. Hook purpose

5-Gate must be a state-machine guard, not a nice checklist in a doc. U4 therefore attaches gate audit records to `visual_asset` and only allows `state='locked'` when all five gates pass. The hook is intentionally conservative: automated heuristics can create warnings and suggested failures, but a locked pass requires structured gate evidence. This avoids the common failure mode where a rendered screenshot, generated image, or Playwright smoke result is mislabeled as “visual approved.”


## Source Register / 证据边界

- PRD-v2/SRD-v2 的稳定事实：ScoutFlow 是 single-user、local-first、SQLite + FS + state words 的 authority-first 工作台；当前不得自动批准 SaaS、多用户、runtime 扩张、media/ASR、browser automation、vault true write 或 migration。
- Capture Station 的已读事实：`apps/capture-station/package.json` 是 React 18 + Vite 5，未把 Tailwind/shadcn/Panda/Radix/React Flow/TanStack/Lucide 写成已批准依赖；现有 H5 代码使用深海蓝 palette、inline style、URL Bar + Vault Preview/Dry Run + Live Metadata + Capture Scope + Trust Trace 的工作台结构。
- Visual docs 的已读事实：`design-brief.md` 固定 4 面板扫描顺序；`five-gate-checklist.md` 要求 5 gate 全过才可称 visual pass；`trust-trace-graph-spec.md` 固定 `capture -> capture_state -> metadata_job -> probe_evidence -> receipt_ledger -> media_audio -> audit` 节点链。
- 本地缺口：容器内没有 `~/workspace/ScoutFlow`、没有 `~/.claude/rules/aesthetic-first-principles.md`、没有 PF-V 实际 `INDEX.csv`，因此相关内容均标为 `needs_local_refresh`。
- Live web 缺口：本运行环境禁用实时网页浏览；任何 vendor / 2026 工具状态只能列为待验证 URL 种子，不得写成已访问事实。

## 2. Gate definitions used in this candidate

The container did not include the global canonical rule file. The available H5 visual checklist defines these gates:

| gate | candidate name | pass requirement |
|---:|---|---|
| 1 | Visual Hierarchy | URL Bar + Capture Action are first attention; metadata values outrank notes; Trust Trace does not steal primary action. |
| 2 | Spacing & Alignment | Four panels share grid; lower columns/spacing stable; graph/title/value align. |
| 3 | Occlusion Safety | Badge/legend/toast/tooltip do not cover URL, key state, title, or node label. |
| 4 | Typography Readability | Machine strings readable; hierarchy clear; contrast supports long scanning. |
| 5 | Visual Weight | Active/current/proven path has more weight than blocked/future lanes. |

When the canonical file is later available, this table should be checked and amended, not silently assumed identical.

## 3. SQLite DDL

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS visual_gate_audits (
  audit_id TEXT PRIMARY KEY,
  asset_id TEXT NOT NULL,
  gate_1_pass INTEGER NOT NULL CHECK (gate_1_pass IN (0,1)),
  gate_2_pass INTEGER NOT NULL CHECK (gate_2_pass IN (0,1)),
  gate_3_pass INTEGER NOT NULL CHECK (gate_3_pass IN (0,1)),
  gate_4_pass INTEGER NOT NULL CHECK (gate_4_pass IN (0,1)),
  gate_5_pass INTEGER NOT NULL CHECK (gate_5_pass IN (0,1)),
  overall_pass INTEGER GENERATED ALWAYS AS (
    CASE WHEN gate_1_pass=1 AND gate_2_pass=1 AND gate_3_pass=1 AND gate_4_pass=1 AND gate_5_pass=1 THEN 1 ELSE 0 END
  ) STORED,
  audit_source TEXT NOT NULL CHECK (audit_source IN ('manual_review','pfv_index_csv','heuristic_script','localhost_review','other')),
  audit_payload_json TEXT NOT NULL DEFAULT '{}',
  reviewer TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_visual_gate_asset
  ON visual_gate_audits(asset_id, created_at);
```

## 4. State-machine hook

```sql
-- after inserting an audit row, sync latest pass to visual_assets
UPDATE visual_assets
SET five_gate_audit_passed = CASE WHEN EXISTS (
  SELECT 1 FROM visual_gate_audits a
  WHERE a.asset_id = visual_assets.asset_id
    AND a.overall_pass = 1
  ORDER BY a.created_at DESC
  LIMIT 1
) THEN 1 ELSE 0 END
WHERE asset_id = :asset_id;
```

The stricter interpretation is “latest audit wins.” The safer first version is “any pass allows but later fail requires manual transition back to refined.” For single-user mode, use latest-audit-wins during active work and any-pass during archival migration only if explicitly noted.

## 5. CLI audit payload

```json
{
  "asset_id": "va_...",
  "audit_source": "manual_review",
  "gates": {
    "1_visual_hierarchy": {"pass": true, "notes": "URL action is primary"},
    "2_spacing_alignment": {"pass": true, "notes": "panel grid aligned"},
    "3_occlusion_safety": {"pass": false, "notes": "toast covers node label on mobile"},
    "4_typography_readability": {"pass": true, "notes": "ID and URL readable"},
    "5_visual_weight": {"pass": true, "notes": "blocked lower weight"}
  },
  "screenshots": ["desktop.png", "mobile.png"],
  "canonical_rule_ref": "~/.claude/rules/aesthetic-first-principles.md"
}
```

A single `false` means `overall_pass=0` and prevents lock.

## 6. Python hook (candidate ≤300 LOC)

```python
#!/usr/bin/env python3
from __future__ import annotations
import json, sqlite3, uuid
from pathlib import Path
DB = Path('visual-assets/u4_assets.sqlite')

def con():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    c.execute('PRAGMA foreign_keys=ON')
    return c

def record_gate_audit(payload_path: str):
    payload = json.loads(Path(payload_path).read_text())
    gates = payload['gates']
    vals = [1 if gates[k]['pass'] else 0 for k in gates]
    if len(vals) != 5: raise SystemExit('exactly five gates required')
    aid = f'ga_{uuid.uuid4().hex[:16]}'
    with con() as db:
        db.execute("""INSERT INTO visual_gate_audits
          (audit_id, asset_id, gate_1_pass, gate_2_pass, gate_3_pass, gate_4_pass, gate_5_pass,
           audit_source, audit_payload_json, reviewer)
          VALUES (?,?,?,?,?,?,?,?,?,?)""",
          (aid, payload['asset_id'], *vals, payload.get('audit_source','manual_review'),
           json.dumps(payload, ensure_ascii=False), payload.get('reviewer')))
        passed = all(vals)
        db.execute('UPDATE visual_assets SET five_gate_audit_passed=? WHERE asset_id=?',
                   (1 if passed else 0, payload['asset_id']))
    return aid

def assert_can_lock(asset_id: str):
    with con() as db:
        row = db.execute('SELECT five_gate_audit_passed FROM visual_assets WHERE asset_id=?', (asset_id,)).fetchone()
        if not row: raise SystemExit('missing asset')
        if row['five_gate_audit_passed'] != 1:
            raise SystemExit('cannot lock: 5-Gate audit has not passed')
```

## 7. Heuristic automation limits

A script can inspect dimensions, obvious blank image, pHash duplicates, and maybe contrast samples. It cannot reliably prove “visual hierarchy” or “occlusion safety” without structured screenshot annotations or human review. Therefore:

- Heuristic pass can recommend `candidate -> refined`, not `refined -> locked`.
- Heuristic fail can block lock until a manual override audit is added.
- Playwright/render pass, if later approved, is a technical render signal, not a visual pass.
- Browser automation remains out of scope unless a separate gate approves it.

## 8. Integration with visual_asset transition

`visual_assets.py transition --state locked` must call `assert_can_lock(asset_id)`. The transition script should also check prompt/pattern links via contract audit.

```text
transition_locked(asset)
  -> verify sha current
  -> verify prompt/pattern contract
  -> verify five_gate_audit_passed=1
  -> update state locked
  -> insert visual_asset_event state_changed
```

## 9. Acceptance checklist

- Five gate fields are explicit booleans, not a single vague quality score.
- Locking fails if any gate fails or audit is missing.
- Heuristic scripts cannot claim visual pass alone.
- Canonical rule file absence is recorded as `needs_local_refresh`.
- Gate payload stores screenshots/reviewer/source for audit replay.


## 10. Manual review checklist template

```text
Asset: va_...
Viewport(s): desktop / tablet / mobile
Gate 1 Visual Hierarchy:
  pass/fail:
  evidence:
Gate 2 Spacing & Alignment:
  pass/fail:
  evidence:
Gate 3 Occlusion Safety:
  pass/fail:
  evidence:
Gate 4 Typography Readability:
  pass/fail:
  evidence:
Gate 5 Visual Weight:
  pass/fail:
  evidence:
Decision: candidate / refined / locked / deprecated
Reviewer note:
```

The checklist is intentionally short. The reviewer should not need to write a design essay for every image. The important part is that each gate has a discrete pass/fail and evidence note.

## 11. Heuristic warning examples

| heuristic | possible warning | gate affected |
|---|---|---|
| image width below 800px | cannot verify desktop hierarchy | gate 1/2 |
| high pHash similarity to deprecated counterexample | may repeat known failure | depends on pattern |
| extremely low luminance contrast sample | possible readability issue | gate 4 |
| missing mobile screenshot for H5 asset | mobile occlusion unknown | gate 3 |
| no prompt_id | cannot replay generation intent | lock contract, not visual gate |

Heuristics should say “possible,” “unknown,” or “requires review.” They should not say “passed” unless the rule is mechanical and sufficient.

## 12. JSON schema-lite for audit payload

```json
{
  "required": ["asset_id", "audit_source", "gates"],
  "properties": {
    "asset_id": {"type": "string", "pattern": "^va_"},
    "audit_source": {"enum": ["manual_review", "pfv_index_csv", "heuristic_script", "localhost_review", "other"]},
    "gates": {"type": "object", "minProperties": 5, "maxProperties": 5},
    "screenshots": {"type": "array", "items": {"type": "string"}},
    "reviewer": {"type": ["string", "null"]}
  }
}
```

A future validator can use full JSON Schema, but v0 can check these fields directly in Python.

## 13. Relationship to Apple HIG / Material / WCAG

The prompt requests a global rule based on Apple HIG, Material 3, and WCAG. Because the canonical file was unavailable, this candidate does not quote or rewrite those sources. It only preserves the expected spirit: hierarchy, spacing, occlusion safety, readability, and visual weight. A browse/local-refresh run should reconcile exact wording and update the gate table. Until then, do not claim canonical compliance.

## 14. Lock event payload

When an asset locks, record the audit IDs that made it possible:

```json
{
  "from": "refined",
  "to": "locked",
  "gate_audit_id": "ga_...",
  "contract_audit": "pass",
  "sha256_verified": true
}
```

This lets a later reviewer answer why an asset was locked without re-opening every screenshot.


## 15. Gate failure repair routing

Each failed gate should route to a different repair path:

| failed gate | likely repair pattern | prompt direction |
|---|---|---|
| Gate 1 hierarchy | C or D | make URL/action first, reduce graph/KPI weight |
| Gate 2 spacing | C | restore shared grid and panel rhythm |
| Gate 3 occlusion | H | remove or relocate overlay/toast/legend |
| Gate 4 readability | F or D | increase contrast/type size/wrap behavior |
| Gate 5 weight | D or G | downgrade blocked/future lanes; remove decorative glow |

This routing makes 5-Gate actionable. A failed gate is not just a rejection; it becomes the next prompt/pattern input.

## 16. Latest-audit ambiguity

If an asset has one pass audit and one later fail audit, the registry should not silently keep it locked. Use one of two policies:

```text
strict active policy: latest audit wins; later fail moves lock_ready=false
archive policy: any historical pass remains, but new phase reuse requires latest pass
```

For active PF-V work, strict policy is safer. For archival import, archive policy can preserve history while still requiring a fresh pass before reuse.


## 17. Gate audit report query

```sql
SELECT
  SUM(CASE WHEN gate_1_pass=0 THEN 1 ELSE 0 END) AS gate_1_failures,
  SUM(CASE WHEN gate_2_pass=0 THEN 1 ELSE 0 END) AS gate_2_failures,
  SUM(CASE WHEN gate_3_pass=0 THEN 1 ELSE 0 END) AS gate_3_failures,
  SUM(CASE WHEN gate_4_pass=0 THEN 1 ELSE 0 END) AS gate_4_failures,
  SUM(CASE WHEN gate_5_pass=0 THEN 1 ELSE 0 END) AS gate_5_failures
FROM visual_gate_audits a
JOIN visual_assets v ON v.asset_id=a.asset_id
WHERE v.phase=:phase;
```

This query tells the next prompt which repair loop matters most. If Gate 3 dominates, generate occlusion-safe variants; if Gate 5 dominates, repair status weight and blocked-lane semantics.


## Appendix B — human override discipline

自动化 5-Gate 只能覆盖可检测部分：尺寸、遮挡启发式、对比度、文本可读风险、blocked/active 颜色权重。它不能替代审美判断。因此允许 `manual_override=true`，但必须写 `override_reason`、`gate_id`、`operator_decision`。override 只能把 `candidate` 推到 `refined`，不能直接推到 `locked`；locked 仍需要全部 gate pass 或一条明确的 later authority note。

```yaml
manual_override: true
gate_id: G2_space_alignment
operator_decision: allow_refined_not_locked
override_reason: "graph node spacing is acceptable for poster mockup but not final H5"
```

这个约束避免“自动审计不准”成为跳过审计的理由，也避免工具误判把有明显视觉问题的图直接锁定。
