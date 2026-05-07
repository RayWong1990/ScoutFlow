---
status: candidate / not-authority / not-runtime-approval
created_for: Cloud Prompt U4 Visual Asset Spine
requested_date: 2026-05-07
generated_in_session_date: 2026-05-06
write_enabled: false
claim_scope: spec-only; no production code modification; no dispatch authorization
---

# MODULE — prompt_template spec

> claim label: ≥95% for prompt registry structure; `needs_local_refresh` for actual S00-S18 bodies and Run-1~Run-5 dispatch prompt bodies.

## 1. Module mission

`prompt_template` gives ScoutFlow a local prompt registry without pretending to be a full LLMOps SaaS. PF-V already has GPT Pro session prompts S00-S18, image generation prompts, audit prompts, code-generation prompts, and dispatch prompts that evolve across runs. Today those prompts are implicit: a user can reuse them by memory or by copying from another window, but ScoutFlow has no schema for lineage, parameterization, version, cost, output quality, or phase usage.

The module stores prompts as durable local artifacts. It keeps lineage (`parent_prompt_id`, `superseded_by`), body, parameter schema, cost estimate, quality score, and phase usage. It does not run prompts, does not authorize agents, and does not make external API calls by default. It is a registry and backfill bridge.


## Source Register / 证据边界

- PRD-v2/SRD-v2 的稳定事实：ScoutFlow 是 single-user、local-first、SQLite + FS + state words 的 authority-first 工作台；当前不得自动批准 SaaS、多用户、runtime 扩张、media/ASR、browser automation、vault true write 或 migration。
- Capture Station 的已读事实：`apps/capture-station/package.json` 是 React 18 + Vite 5，未把 Tailwind/shadcn/Panda/Radix/React Flow/TanStack/Lucide 写成已批准依赖；现有 H5 代码使用深海蓝 palette、inline style、URL Bar + Vault Preview/Dry Run + Live Metadata + Capture Scope + Trust Trace 的工作台结构。
- Visual docs 的已读事实：`design-brief.md` 固定 4 面板扫描顺序；`five-gate-checklist.md` 要求 5 gate 全过才可称 visual pass；`trust-trace-graph-spec.md` 固定 `capture -> capture_state -> metadata_job -> probe_evidence -> receipt_ledger -> media_audio -> audit` 节点链。
- 本地缺口：容器内没有 `~/workspace/ScoutFlow`、没有 `~/.claude/rules/aesthetic-first-principles.md`、没有 PF-V 实际 `INDEX.csv`，因此相关内容均标为 `needs_local_refresh`。
- Live web 缺口：本运行环境禁用实时网页浏览；任何 vendor / 2026 工具状态只能列为待验证 URL 种子，不得写成已访问事实。

## 2. Prompt kinds

| kind | use | boundary |
|---|---|---|
| `gpt_pro_session` | S00-S18 long-running GPT Pro session prompt | registry only, no session automation |
| `dispatch_prompt` | Run-1~Run-5 / wave dispatcher prompt | not authorization, not authority write |
| `image_gen` | GPT-Image-2 / visual generation prompt | no image generation in module |
| `code_gen` | code translation / image-to-code / refactor prompt | candidate only, no production patch |
| `audit_prompt` | 5-Gate, visual, boundary, self-audit prompt | may create audit notes, not product pass alone |

## 3. SQLite DDL

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS prompt_templates (
  prompt_id TEXT PRIMARY KEY,
  kind TEXT NOT NULL CHECK (kind IN (
    'gpt_pro_session','dispatch_prompt','image_gen','code_gen','audit_prompt'
  )),
  title TEXT NOT NULL,
  version TEXT NOT NULL DEFAULT 'v0',
  parent_prompt_id TEXT REFERENCES prompt_templates(prompt_id) ON DELETE SET NULL,
  template_body TEXT NOT NULL,
  parameter_schema_json TEXT NOT NULL DEFAULT '{}',
  cost_per_run_usd REAL CHECK (cost_per_run_usd IS NULL OR cost_per_run_usd >= 0),
  output_quality_score REAL CHECK (output_quality_score IS NULL OR (output_quality_score >= 0 AND output_quality_score <= 1)),
  used_in_phase_json TEXT NOT NULL DEFAULT '[]',
  superseded_by TEXT REFERENCES prompt_templates(prompt_id) ON DELETE SET NULL,
  source_ref TEXT,
  claim_label TEXT NOT NULL DEFAULT 'candidate',
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(kind, title, version)
);

CREATE INDEX IF NOT EXISTS idx_prompt_kind_version
  ON prompt_templates(kind, title, version);
CREATE INDEX IF NOT EXISTS idx_prompt_parent
  ON prompt_templates(parent_prompt_id);
CREATE INDEX IF NOT EXISTS idx_prompt_superseded
  ON prompt_templates(superseded_by);

CREATE TABLE IF NOT EXISTS prompt_template_runs (
  run_id TEXT PRIMARY KEY,
  prompt_id TEXT NOT NULL REFERENCES prompt_templates(prompt_id) ON DELETE CASCADE,
  run_label TEXT,
  phase TEXT,
  parameter_values_json TEXT NOT NULL DEFAULT '{}',
  output_asset_id TEXT,
  output_quality_score REAL CHECK (output_quality_score IS NULL OR (output_quality_score >= 0 AND output_quality_score <= 1)),
  cost_actual_usd REAL CHECK (cost_actual_usd IS NULL OR cost_actual_usd >= 0),
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS prompt_template_usage (
  prompt_id TEXT NOT NULL REFERENCES prompt_templates(prompt_id) ON DELETE CASCADE,
  consumer_type TEXT NOT NULL CHECK (consumer_type IN ('visual_asset','pattern_library','design_token','dispatch','audit_note','external')),
  consumer_id TEXT NOT NULL,
  phase TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY(prompt_id, consumer_type, consumer_id)
);

CREATE TRIGGER IF NOT EXISTS trg_prompt_templates_touch
AFTER UPDATE ON prompt_templates
BEGIN
  UPDATE prompt_templates SET updated_at = datetime('now') WHERE prompt_id = NEW.prompt_id;
END;
```

## 4. Python CRUD + lineage query (candidate ≤300 LOC)

```python
#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sqlite3, uuid
from pathlib import Path

DB = Path('prompt-registry/prompt_templates.sqlite')

def con():
    DB.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    c.execute('PRAGMA foreign_keys=ON')
    return c

def put_prompt(kind, title, version, body, parent=None, schema='{}', phases='[]', source=None):
    prompt_id = f'pt_{uuid.uuid4().hex[:16]}'
    json.loads(schema); json.loads(phases)
    with con() as db:
        db.execute("""INSERT INTO prompt_templates
          (prompt_id, kind, title, version, parent_prompt_id, template_body,
           parameter_schema_json, used_in_phase_json, source_ref)
          VALUES (?,?,?,?,?,?,?,?,?)""",
          (prompt_id, kind, title, version, parent, body, schema, phases, source))
    return prompt_id

def supersede(old_id, new_body, new_version):
    with con() as db:
        old = db.execute('SELECT * FROM prompt_templates WHERE prompt_id=?', (old_id,)).fetchone()
        if not old: raise SystemExit('missing old prompt')
        new_id = put_prompt(old['kind'], old['title'], new_version, new_body,
                            parent=old_id,
                            schema=old['parameter_schema_json'],
                            phases=old['used_in_phase_json'],
                            source=old['source_ref'])
        db.execute('UPDATE prompt_templates SET superseded_by=? WHERE prompt_id=?', (new_id, old_id))
    return new_id

def lineage(root_id):
    sql = """WITH RECURSIVE tree(prompt_id, title, version, parent_prompt_id, depth, path) AS (
      SELECT prompt_id,title,version,parent_prompt_id,0,prompt_id
      FROM prompt_templates WHERE prompt_id=?
      UNION ALL
      SELECT p.prompt_id,p.title,p.version,p.parent_prompt_id,t.depth+1,t.path||'>'||p.prompt_id
      FROM prompt_templates p JOIN tree t ON p.parent_prompt_id=t.prompt_id
    ) SELECT * FROM tree ORDER BY depth, version"""
    with con() as db:
        return [dict(r) for r in db.execute(sql, (root_id,))]
```

## 5. Lineage semantics

`parent_prompt_id` means “derived from or refined from.” `superseded_by` means “do not use this as the default for new work.” They are not identical. A prompt may have multiple children, but at most one default successor. The registry should allow branching because PF-V can explore alternate visual directions; it should not force a single linear history.

Recommended lineage tree rendering:

```text
pt_s00_v0 S00 base session
├── pt_s01_v0 S01 asset intake
│   ├── pt_s01_v1 adds pattern tag extraction
│   └── pt_s01_alt_a high-visual variant
└── pt_s02_v0 S02 5-Gate audit loop
    └── pt_s02_v1 stricter occlusion checks
```

## 6. S00-S18 v0 backfill list

Actual bodies are not present in this run. The registry should backfill with placeholders only when the body can be recovered from PF-V notes or user-provided files. Until then, use a visible placeholder body and `claim_label='needs_body_backfill'`, not a fabricated prompt.

| prompt_id seed | kind | title | version | phase | body status |
|---|---|---|---|---|---|
| `pt_s00_v0` | gpt_pro_session | PF-V S00 bootstrap / index discipline | v0 | PF-V | needs_body_backfill |
| `pt_s01_v0` | gpt_pro_session | PF-V S01 H5 reverse asset intake | v0 | PF-V | needs_body_backfill |
| `pt_s02_v0` | gpt_pro_session | PF-V S02 visual direction selection | v0 | PF-V | needs_body_backfill |
| `pt_s03_v0` | gpt_pro_session | PF-V S03 pattern A-B exploration | v0 | PF-V | needs_body_backfill |
| `pt_s04_v0` | gpt_pro_session | PF-V S04 pattern C-D exploration | v0 | PF-V | needs_body_backfill |
| `pt_s05_v0` | gpt_pro_session | PF-V S05 panel layout refinement | v0 | PF-V | needs_body_backfill |
| `pt_s06_v0` | gpt_pro_session | PF-V S06 token visual extraction | v0 | PF-V | needs_body_backfill |
| `pt_s07_v0` | gpt_pro_session | PF-V S07 Trust Trace visual audit | v0 | PF-V | needs_body_backfill |
| `pt_s08_v0` | gpt_pro_session | PF-V S08 mobile/tablet adaptation | v0 | PF-V | needs_body_backfill |
| `pt_s09_v0` | gpt_pro_session | PF-V S09 5-Gate fail repair | v0 | PF-V | needs_body_backfill |
| `pt_s10_v0` | gpt_pro_session | PF-V S10 icon/illustration spine | v0 | PF-V | needs_body_backfill |
| `pt_s11_v0` | gpt_pro_session | PF-V S11 screenshot-to-code guard | v0 | PF-V | needs_body_backfill |
| `pt_s12_v0` | gpt_pro_session | PF-V S12 prompt compression | v0 | PF-V | needs_body_backfill |
| `pt_s13_v0` | gpt_pro_session | PF-V S13 candidate asset lock review | v0 | PF-V | needs_body_backfill |
| `pt_s14_v0` | gpt_pro_session | PF-V S14 cross-phase reuse review | v0 | PF-V | needs_body_backfill |
| `pt_s15_v0` | gpt_pro_session | PF-V S15 negative example library | v0 | PF-V | needs_body_backfill |
| `pt_s16_v0` | gpt_pro_session | PF-V S16 final visual audit | v0 | PF-V | needs_body_backfill |
| `pt_s17_v0` | gpt_pro_session | PF-V S17 README packaging | v0 | PF-V | needs_body_backfill |
| `pt_s18_v0` | gpt_pro_session | PF-V S18 handoff / next phase prompt | v0 | PF-V | needs_body_backfill |

## 7. Run-1 ~ Run-5 dispatch prompt backfill

Dispatch prompts are more dangerous than image prompts because a reader may treat them as authorization. For this module, each backfilled dispatch prompt must carry:

```json
{
  "authorization": "none",
  "write_enabled": false,
  "allowed_output": "candidate_spec_or_research_note",
  "forbidden_output": ["production_patch", "authority_write", "runtime_unlock"]
}
```

| seed | kind | version | body status | required warning |
|---|---|---|---|---|
| `pt_run1_dispatch_v0` | dispatch_prompt | v0 | needs_body_backfill | not dispatch authorization |
| `pt_run2_dispatch_v0` | dispatch_prompt | v0 | needs_body_backfill | not dispatch authorization |
| `pt_run3_dispatch_v0` | dispatch_prompt | v0 | needs_body_backfill | not dispatch authorization |
| `pt_run4_dispatch_v0` | dispatch_prompt | v0 | needs_body_backfill | not dispatch authorization |
| `pt_run5_dispatch_v0` | dispatch_prompt | v0 | needs_body_backfill | not dispatch authorization |

## 8. Parameter schema pattern

Use JSON Schema-lite, not a new DSL:

```json
{
  "type": "object",
  "required": ["asset_kind", "phase", "visual_goal"],
  "properties": {
    "asset_kind": {"enum": ["raw_screenshot", "gpt_image_2", "mockup", "token_visual"]},
    "phase": {"type": "string"},
    "pattern_tag": {"type": ["string", "null"], "pattern": "^[A-J]$"},
    "visual_goal": {"type": "string", "minLength": 20},
    "negative_constraints": {"type": "array", "items": {"type": "string"}}
  }
}
```

## 9. Acceptance checklist

- Prompt bodies are never fabricated during backfill.
- `dispatch_prompt` rows include non-authorization warning.
- Lineage query works for branch and successor cases.
- `output_quality_score` is per prompt or per run, not a visual pass claim.
- `used_in_phase_json` is a compact list; detailed consumer links go into `prompt_template_usage`.
- No external model call is executed by the registry script.


## 10. Prompt body conventions

Every prompt body should have an explicit header and a stable footer. This allows later diffing and lineage review without running the prompt.

```text
[ROLE]
You are operating on ScoutFlow U4 visual asset spine candidate material.

[INPUTS]
- phase: {{phase}}
- target asset kind: {{asset_kind}}
- pattern tag: {{pattern_tag}}
- design token ref: {{token_ref}}

[BOUNDARIES]
- candidate / not-authority
- no production code patch
- no runtime approval
- do not claim live web if browsing not performed

[OUTPUT]
Return markdown with source assumptions, decisions, failure cases, and truthful stdout.
```

The registry should reject prompt bodies that omit boundaries when `kind='dispatch_prompt'` or `kind='code_gen'`. For `image_gen`, the prompt can be shorter, but it should still reference candidate tokens, panel order, and negative constraints.

## 11. Quality scoring rubric

`output_quality_score` is a usefulness estimate, not a gate pass. A suggested rubric:

| score band | meaning | allowed state influence |
|---|---|---|
| 0.00-0.39 | unclear, off-scope, or harmful | deprecate or archive only |
| 0.40-0.59 | partially useful, needs repair | candidate only |
| 0.60-0.79 | useful with visible caveats | refined possible |
| 0.80-0.94 | strong reusable prompt/output | lock candidate if gates pass |
| 0.95-1.00 | exceptional and repeatedly proven | lock candidate; still requires explicit gate if visual |

A prompt can score high even when its generated asset fails a gate, because the prompt may have helped reveal the failure. Conversely, a beautiful image generated from an undocumented prompt should not be locked until the prompt lineage is backfilled.

## 12. Cost model

The module stores `cost_per_run_usd` and `cost_actual_usd` as optional numbers. For GPT Pro web sessions, true per-run cost may be unknowable. In that case, use `NULL`, not guessed dollars. For API calls, store actual known cost if available. This prevents false precision.

Recommended stdout after run registration:

```yaml
PROMPT_RUN_REGISTERED: true
run_id: ptr_...
prompt_id: pt_s07_v0
phase: PF-V-S07
cost_actual_usd: null
output_asset_id: va_...
quality_score: 0.72
warnings:
  - cost unknown because GPT Pro web session has no per-run API receipt
```

## 13. Backfill workflow

```text
1. seed placeholders: S00-S18 and Run-1~Run-5
2. import actual bodies when provided
3. compare body hash against placeholder
4. mark placeholder superseded or update in place only if body was empty
5. link prompt_id to visual assets by CSV/session labels
6. record prompt_template_usage for each imported asset
```

Do not overwrite a real body with a later guessed body. If two candidate bodies claim to be S07, create `pt_s07_v0_a` and `pt_s07_v0_b`, then let lineage review decide.

## 14. Prompt diff policy

Prompt changes should be diffed at semantic boundaries rather than just raw text. A small helper can split sections like `[ROLE]`, `[INPUTS]`, `[BOUNDARIES]`, `[OUTPUT]`, and show changes per section. This matters because boundary regressions are more dangerous than wording improvements. If a new version removes `not-authority`, `write_enabled=false`, or `no production patch`, the registry should flag `dispatch_auth_leak` or `boundary_regression` before allowing `superseded_by` to become default.

## 15. Examples of module consumers

| consumer | prompt kind | example |
|---|---|---|
| visual asset generation | `image_gen` | generate Trust Trace mockup with Pattern E and token set |
| visual audit | `audit_prompt` | evaluate an asset against 5-Gate with screenshot paths |
| design token extraction | `audit_prompt` | derive token candidates from locked images |
| pattern refinement | `gpt_pro_session` | compare five candidate images and propose Pattern H repair |
| code boundary review | `code_gen` | translate visual intent into CSS variable plan without app patch |

The same prompt may serve multiple consumers, but each use should be recorded so later phase closeout can explain where a prompt mattered.


## 16. Prompt safety lint

A tiny lint pass can catch the highest-risk mistakes before a prompt is used. Suggested checks:

| lint | applies to | fail when |
|---|---|---|
| boundary present | dispatch/code/audit | no `candidate`, `not-authority`, or `write_enabled=false` wording |
| live web honesty | research prompts | prompt asks to cite current sources but does not require browsing status |
| output scope | dispatch prompts | output permits production patch or authority write without gate |
| token source | image/code prompts | references palette without token or source note |
| gate separation | audit prompts | treats render/screenshot existence as visual pass |

Lint failures should not delete prompts. They should mark `claim_label='lint_failed'` or block setting a prompt as default successor.

## 17. Prompt storage and redaction

Prompt bodies may contain copied user context, file paths, or accidental secrets. The registry should provide a manual redaction path:

```text
prompt redact --prompt-id pt_x --replace "secret" "[REDACTED]" --new-version v1-redacted
```

Redaction creates a new version and supersedes the old one. It does not rewrite history silently. If a prompt contains credential material, the row should be marked `deprecated` or `redacted_required` and excluded from reuse until repaired. This mirrors ScoutFlow's broader rule that credential material is never evidence.

## 18. S00-S18 body import format

When the user later provides session prompt bodies, prefer a manifest file:

```yaml
- seed: S07
  prompt_id: pt_s07_v0
  title: PF-V S07 Trust Trace visual audit
  body_path: prompts/S07.md
  source_ref: GPT Pro session export / user-provided
  used_in_phase: [PF-V]
```

This avoids fragile filename inference. The importer can validate body existence, compute a body hash, and update placeholders safely.

## 19. Why not use only chat history

Chat history is not a registry. It is difficult to diff, difficult to query by phase, and easy to lose when multiple sessions run in parallel. A local prompt table does not replace the creative process; it preserves the parts that need to survive: lineage, version, parameters, cost, quality, and usage links.


## 20. Prompt registry queries

Useful v0 queries:

```sql
SELECT prompt_id,title,version,output_quality_score
FROM prompt_templates
WHERE kind='image_gen' AND superseded_by IS NULL
ORDER BY output_quality_score DESC NULLS LAST;
```

```sql
SELECT p.prompt_id,p.title,COUNT(u.consumer_id) AS uses
FROM prompt_templates p
LEFT JOIN prompt_template_usage u ON u.prompt_id=p.prompt_id
GROUP BY p.prompt_id
ORDER BY uses DESC;
```

These answer which prompts are current and which prompts are actually used. A prompt with elegant wording but zero uses should not dominate future work. A rough but frequently reused prompt deserves cleanup and versioning.

## 21. Prompt archival

Archive does not mean delete. Superseded prompts remain useful because they explain why older images look the way they do. The registry should hide superseded prompts from default selection while keeping them visible in lineage. This is the same principle as visual assets: history matters, but default reuse should be clean.


## Appendix C — prompt quality scoring rubric

`output_quality_score` 不能只是主观“好不好看”。本模块采用 0-5 的单人可执行评分：0 表示 prompt 输出无法使用或违背边界；1 表示只产生方向性材料；2 表示有局部可复用片段但需大改；3 表示可作为候选进入下一轮；4 表示可直接支持视觉/代码/审计产物；5 表示已被 locked asset 或正式 spec 多次复用。评分可以由用户手动写入，也可以由 audit prompt 产出建议值，但最终仍是 single-user authority。

建议记录的评分理由字段放入 `parameter_schema` 或 `notes_json` 扩展，而不是把表结构膨胀成企业评审系统。示例：

```json
{
  "score_reason": "S08 changed graph weight without breaking URL primary action",
  "gate_failures": [],
  "next_edit": "reduce blocked lane saturation",
  "rated_by": "operator"
}
```

### S00-S18 v0 backfill safety

S00-S18 的 backfill 先只收 prompt 名称、session 序号、用途、已知 pattern_tag、输出 asset 关系；如果另窗口的全文 prompt 尚未导入，不得编造 body。`template_body` 可写占位：`UNAVAILABLE_LOCAL_WINDOW_BODY_NEEDS_BACKFILL`，同时把 `quality_score` 置空。这样 prompt registry 先获得 lineage 骨架，再等待真实 prompt 文件补齐。
