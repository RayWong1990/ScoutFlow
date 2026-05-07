---
status: candidate / not-authority / not-runtime-approval
created_for: Cloud Prompt U4 Visual Asset Spine
requested_date: 2026-05-07
generated_in_session_date: 2026-05-06
write_enabled: false
claim_scope: spec-only; no production code modification; no dispatch authorization
---

# MODULE — visual_asset spec

> claim label: ≥95% for candidate schema / local implementation shape; `needs_local_refresh` for PF-V actual file inventory; `live_web_not_used` for external vendor comparison.

## 1. Module mission

`visual_asset` 是 ScoutFlow U4 视觉资产骨架的第一个横切面。它不是企业 DAM，也不是极简“把图片丢进文件夹”。它只解决单人 prosumer 模式里已经实际发生的问题：GPT-Image-2 逆向 H5、raw screenshot、mockup、SVG、icon、illustration、token visual、pattern refinement 之间需要一个稳定账本，能够回答“这张图从哪个 prompt 来、归属哪个 phase、是否通过 5-Gate、能否跨 phase 复用、是否和另一张图只是小改款”。

该模块保持 sidecar 语义：它可以写自己的 `visual_assets.sqlite`，但不写 ScoutFlow capture authority，不修改 `apps/capture-station/**`，不把视觉通过等价为 runtime 通过。它的价值在于让强视觉工作不再只存在于聊天窗口、下载目录和截图文件名里。

## 2. Scope

### In scope

- 记录视觉文件：raw screenshot、GPT image output、SVG、mockup、icon、illustration、token visual。
- 记录 lineage：父资产、prompt_id、pattern_tag、phase、state。
- 记录质量字段：sha256、perceptual_hash、dimensions、5_gate_audit_passed。
- 生成 thumbnail 与 pHash，允许跨 phase 复用查询。
- 支持 PF-V 的 S00-S18 / Pattern A-J / INDEX.csv 迁移，但迁移器必须动态识别列名，不能假装已读取当前 CSV。

### Out of scope

- 不做企业 DAM 的权限、分享、审批、品牌 portal、多团队 review、云同步。
- 不做浏览器自动截图批准；截图如需生成必须另走 gate。
- 不替换 capture-station CSS，不批准 token cascade 落地。
- 不把 `locked` 资产写成产品 authority；它只是视觉资产侧的锁定状态。


## Source Register / 证据边界

- PRD-v2/SRD-v2 的稳定事实：ScoutFlow 是 single-user、local-first、SQLite + FS + state words 的 authority-first 工作台；当前不得自动批准 SaaS、多用户、runtime 扩张、media/ASR、browser automation、vault true write 或 migration。
- Capture Station 的已读事实：`apps/capture-station/package.json` 是 React 18 + Vite 5，未把 Tailwind/shadcn/Panda/Radix/React Flow/TanStack/Lucide 写成已批准依赖；现有 H5 代码使用深海蓝 palette、inline style、URL Bar + Vault Preview/Dry Run + Live Metadata + Capture Scope + Trust Trace 的工作台结构。
- Visual docs 的已读事实：`design-brief.md` 固定 4 面板扫描顺序；`five-gate-checklist.md` 要求 5 gate 全过才可称 visual pass；`trust-trace-graph-spec.md` 固定 `capture -> capture_state -> metadata_job -> probe_evidence -> receipt_ledger -> media_audio -> audit` 节点链。
- 本地缺口：容器内没有 `~/workspace/ScoutFlow`、没有 `~/.claude/rules/aesthetic-first-principles.md`、没有 PF-V 实际 `INDEX.csv`，因此相关内容均标为 `needs_local_refresh`。
- Live web 缺口：本运行环境禁用实时网页浏览；任何 vendor / 2026 工具状态只能列为待验证 URL 种子，不得写成已访问事实。

## 3. State machine

```text
gen
  -> candidate
  -> refined
  -> locked
  -> deprecated
```

State 解释：

| state | meaning | allowed next | stop condition |
|---|---|---|---|
| `gen` | 刚产生，只有文件和最小来源 | candidate / deprecated | 缺文件、sha 不匹配、来源未知 |
| `candidate` | 可进入人工/自动视觉审查 | refined / locked / deprecated | 未通过关键 5-Gate 不得 locked |
| `refined` | 已按 prompt/pattern 修过，保留上游 parent | candidate / locked / deprecated | lineage 断裂必须回 candidate |
| `locked` | 当前 phase 的可复用参考资产 | deprecated | 需要 `5_gate_audit_passed=1` 与 sha/pHash 完整 |
| `deprecated` | 不再用于新 phase，但保留审计 | none | 不物理删除，除非文件损坏且另有 ledger |

## 4. SQLite DDL

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS visual_assets (
  asset_id TEXT PRIMARY KEY,
  kind TEXT NOT NULL CHECK (kind IN (
    'raw_screenshot','gpt_image_2','svg','mockup','icon','illustration','token_visual'
  )),
  state TEXT NOT NULL DEFAULT 'gen' CHECK (state IN (
    'gen','candidate','refined','locked','deprecated'
  )),
  parent_asset_id TEXT REFERENCES visual_assets(asset_id) ON DELETE SET NULL,
  prompt_id TEXT,
  pattern_tag TEXT,
  sha256 TEXT NOT NULL,
  perceptual_hash TEXT,
  width INTEGER,
  height INTEGER,
  file_path TEXT NOT NULL UNIQUE,
  thumbnail_path TEXT,
  phase TEXT NOT NULL,
  five_gate_audit_passed INTEGER NOT NULL DEFAULT 0 CHECK (five_gate_audit_passed IN (0,1)),
  quality_score REAL CHECK (quality_score IS NULL OR (quality_score >= 0 AND quality_score <= 1)),
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  CHECK (pattern_tag IS NULL OR length(pattern_tag) BETWEEN 1 AND 8)
);

CREATE INDEX IF NOT EXISTS idx_visual_assets_phase_state
  ON visual_assets(phase, state, kind);
CREATE INDEX IF NOT EXISTS idx_visual_assets_prompt
  ON visual_assets(prompt_id);
CREATE INDEX IF NOT EXISTS idx_visual_assets_pattern
  ON visual_assets(pattern_tag);
CREATE INDEX IF NOT EXISTS idx_visual_assets_phash
  ON visual_assets(perceptual_hash);

CREATE TABLE IF NOT EXISTS visual_asset_events (
  event_id TEXT PRIMARY KEY,
  asset_id TEXT NOT NULL REFERENCES visual_assets(asset_id) ON DELETE CASCADE,
  event_kind TEXT NOT NULL CHECK (event_kind IN (
    'created','state_changed','thumbnail_generated','phash_generated','gate_audited','reused','deprecated'
  )),
  event_payload_json TEXT NOT NULL DEFAULT '{}',
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS visual_asset_phase_use (
  asset_id TEXT NOT NULL REFERENCES visual_assets(asset_id) ON DELETE CASCADE,
  phase TEXT NOT NULL,
  use_kind TEXT NOT NULL CHECK (use_kind IN ('reference','source','locked_output','rejected_example')),
  consumer TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY(asset_id, phase, use_kind, consumer)
);

CREATE TRIGGER IF NOT EXISTS trg_visual_assets_touch
AFTER UPDATE ON visual_assets
BEGIN
  UPDATE visual_assets SET updated_at = datetime('now') WHERE asset_id = NEW.asset_id;
END;
```

## 5. File layout

```text
visual-assets/
  raw_screenshot/phase-*/YYYYMMDD/{asset_id}.png
  gpt_image_2/phase-*/YYYYMMDD/{asset_id}.png
  svg/phase-*/{asset_id}.svg
  mockup/phase-*/{asset_id}.png
  token_visual/phase-*/{asset_id}.png
  thumbs/{asset_id}.webp
  visual_assets.sqlite
```

路径不是 authority；SQLite 记录才是账本。文件移动必须通过 `update_file_path` 记录事件，不能手工改目录后让 DB 失真。

## 6. Python CRUD script (candidate ≤300 LOC)

```python
#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sqlite3, uuid
from pathlib import Path
from PIL import Image

DB = Path('visual-assets/visual_assets.sqlite')
ROOT = Path('visual-assets')

def connect() -> sqlite3.Connection:
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    con.execute('PRAGMA foreign_keys=ON')
    return con

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def image_dims(path: Path) -> tuple[int|None, int|None]:
    try:
        with Image.open(path) as im:
            return im.width, im.height
    except Exception:
        return None, None

def add_asset(args) -> str:
    path = Path(args.file_path)
    if not path.exists():
        raise SystemExit(f'missing file: {path}')
    asset_id = args.asset_id or f'va_{uuid.uuid4().hex[:16]}'
    width, height = image_dims(path)
    with connect() as con:
        con.execute("""INSERT INTO visual_assets
          (asset_id, kind, state, parent_asset_id, prompt_id, pattern_tag, sha256,
           width, height, file_path, phase, notes)
          VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
          (asset_id, args.kind, args.state, args.parent_asset_id, args.prompt_id,
           args.pattern_tag, sha256_file(path), width, height, str(path), args.phase, args.notes))
        con.execute('INSERT INTO visual_asset_events(event_id, asset_id, event_kind, event_payload_json) VALUES (?,?,?,?)',
          (f've_{uuid.uuid4().hex[:16]}', asset_id, 'created', json.dumps({'file_path': str(path)})))
    return asset_id

def transition(asset_id: str, state: str) -> None:
    with connect() as con:
        row = con.execute('SELECT state, five_gate_audit_passed FROM visual_assets WHERE asset_id=?', (asset_id,)).fetchone()
        if not row:
            raise SystemExit('asset not found')
        if state == 'locked' and row['five_gate_audit_passed'] != 1:
            raise SystemExit('cannot lock asset before 5-Gate pass')
        con.execute('UPDATE visual_assets SET state=? WHERE asset_id=?', (state, asset_id))
        con.execute('INSERT INTO visual_asset_events VALUES (?,?,?, ?, datetime("now"))',
          (f've_{uuid.uuid4().hex[:16]}', asset_id, 'state_changed', json.dumps({'from': row['state'], 'to': state})))

def list_reuse(phase: str, pattern: str | None, min_score: float) -> list[sqlite3.Row]:
    sql = """SELECT asset_id, kind, state, pattern_tag, prompt_id, quality_score, file_path
             FROM visual_assets
             WHERE state IN ('refined','locked') AND phase <> ?
               AND (quality_score IS NULL OR quality_score >= ?)"""
    params = [phase, min_score]
    if pattern:
        sql += ' AND pattern_tag = ?'
        params.append(pattern)
    sql += ' ORDER BY state DESC, quality_score DESC, created_at DESC LIMIT 50'
    with connect() as con:
        return con.execute(sql, params).fetchall()
```

## 7. Thumbnail + pHash cron

Cron should be safe and idempotent. It only fills missing `thumbnail_path` / `perceptual_hash`, never mutates state.

```bash
# local-only, not repo authority
*/30 * * * * cd ~/workspace/ScoutFlow && python tools/visual_assets.py cron-thumbs --db visual-assets/visual_assets.sqlite
```

Candidate algorithm:

1. Select assets where `thumbnail_path IS NULL OR perceptual_hash IS NULL`.
2. Read image with Pillow; skip SVG unless rasterizer is locally approved.
3. Generate `thumbs/{asset_id}.webp` at max 512px width.
4. Compute perceptual hash using average-hash or dHash implemented inline if `imagehash` is not installed.
5. Record event `thumbnail_generated` and `phash_generated`.
6. If file sha changed since registration, do not overwrite fields; write `integrity_mismatch` note and require manual inspection.

## 8. Cross-phase reuse query

```sql
SELECT
  v.asset_id,
  v.kind,
  v.state,
  v.phase AS source_phase,
  v.pattern_tag,
  v.prompt_id,
  v.quality_score,
  v.file_path,
  GROUP_CONCAT(u.phase || ':' || u.use_kind) AS prior_uses
FROM visual_assets v
LEFT JOIN visual_asset_phase_use u ON u.asset_id = v.asset_id
WHERE v.state IN ('locked','refined')
  AND v.phase <> :target_phase
  AND (:pattern_tag IS NULL OR v.pattern_tag = :pattern_tag)
  AND v.five_gate_audit_passed = 1
GROUP BY v.asset_id
ORDER BY v.state DESC, v.quality_score DESC, v.created_at DESC
LIMIT 30;
```

This query is the core prosumer win: it stops PF-V from regenerating the same panel mood, token visual, icon treatment, or Trust Trace mockup every new phase.

## 9. PF-V backfill stance

PF-V actual `INDEX.csv` was not present in this container. The backfill script must therefore introspect headers and only require a minimal column set:

| PF-V concept | visual_assets field | fallback |
|---|---|---|
| file path / output path | `file_path` | fail closed |
| asset kind / source type | `kind` | infer from extension + prompt source |
| prompt/session | `prompt_id` | `unknown_prompt_v0` |
| pattern A-J | `pattern_tag` | NULL |
| phase/run/session | `phase` | `PF-V-unknown` |
| quality/pass | `quality_score`, `five_gate_audit_passed` | NULL / 0 |
| dimensions/hash | `width`, `height`, `sha256`, `perceptual_hash` | compute |

Backfill must never turn unknown quality into pass. A screenshot can be `candidate` with `five_gate_audit_passed=0`; it cannot be `locked` without a real gate audit.

## 10. Acceptance checklist

- DDL creates exactly the sidecar tables and does not touch ScoutFlow capture authority.
- Insert rejects missing file and invalid enum.
- `locked` transition fails if 5-Gate has not passed.
- pHash cron is idempotent and records events.
- Cross-phase query returns only `refined/locked` assets from other phases.
- PF-V CSV migration is header-driven and fail-closed.
- No production code is modified; no dispatch is authorized.


## 11. CRUD command surface

The CLI should stay boring and predictable. A single user should be able to run it from a terminal without remembering hidden workflow state.

```text
visual-assets init
visual-assets add --file <path> --kind gpt_image_2 --phase PF-V-S07 --prompt-id pt_s07_v0 --pattern-tag E
visual-assets show --asset-id va_x
visual-assets list --phase PF-V-S07 --state candidate
visual-assets transition --asset-id va_x --state refined
visual-assets audit-hash --asset-id va_x
visual-assets thumbs --missing-only
visual-assets reuse --target-phase U5 --pattern-tag E --min-score .75
visual-assets deprecate --asset-id va_x --reason "fails gate 3 on mobile"
```

`init` may create the SQLite file and schema. It must never scan arbitrary folders automatically. `add` requires an explicit file path because PF-V may have many discarded generations that should not enter the ledger. `deprecate` changes state but does not delete the file. Physical cleanup is a separate manual maintenance task and should print the affected rows before touching disk.

## 12. Integrity and duplicate policy

The module stores both `sha256` and `perceptual_hash` because they answer different questions. `sha256` answers whether the file bytes changed. `perceptual_hash` answers whether two images look similar enough to deserve human review. The registry must never merge or overwrite by pHash alone.

| condition | interpretation | action |
|---|---|---|
| same sha256, same path | exact duplicate registration attempt | reject or return existing `asset_id` |
| same sha256, different path | copied file | allow only if phase/use differs, warn |
| different sha256, similar pHash | variant or minor edit | show lineage suggestion, do not merge |
| same parent, wildly different pHash | large visual fork | allow, require pattern note |
| locked asset hash changed | integrity violation | block reuse until re-registered |

A practical pHash threshold can start as Hamming distance `<= 6` for near-duplicates and `<= 12` for family resemblance. These numbers are review hints, not correctness claims.

## 13. Example row lifecycle

```yaml
asset_id: va_8f2c19e4a9d04b31
kind: gpt_image_2
state: candidate
parent_asset_id: va_raw_h5_001
prompt_id: pt_s07_v0
pattern_tag: E
sha256: <computed>
perceptual_hash: <computed_after_cron>
width: 1536
height: 1024
file_path: visual-assets/gpt_image_2/PF-V-S07/20260507/va_8f2c19e4a9d04b31.png
phase: PF-V-S07
five_gate_audit_passed: 0
quality_score: null
notes: "Trust Trace right-panel variant; candidate only."
```

After manual 5-Gate review, the same asset may become:

```yaml
state: locked
five_gate_audit_passed: 1
quality_score: 0.88
visual_asset_phase_use:
  - phase: U5
    use_kind: reference
    consumer: prompt_template:pt_u5_h5_seed_v0
```

## 14. Failure modes to surface in stdout

A prosumer registry fails when it hides uncertainty. Every command should prefer explicit stdout over silent success:

```yaml
VISUAL_ASSET_ADD_COMPLETE: true
asset_id: va_...
state: candidate
sha256: <hash>
phash_generated: false
five_gate_audit_passed: false
lockable: false
warnings:
  - prompt_id not found in prompt_templates
  - pattern_tag E uses placeholder definition
```

This makes the module useful for multi-agent fleet work: agents can pass local stdout to the user or to later audit prompts without creating an authority illusion.

## 15. Why this is not enterprise DAM

Enterprise DAM usually optimizes for brand governance, searchable shared libraries, permissioned distribution, campaign analytics, rights metadata, and cloud synchronization. U4 optimizes for a single local creator who needs rapid iteration and honest lineage. The scope is deliberately smaller but deeper on the fields PF-V actually needs: prompt, phase, pattern, hash, pHash, state, gate pass, and reuse. That is the dividing line: if a feature does not help those fields, it belongs outside v0.


## 16. Operator workflows

### Workflow A — fast generation capture

A user finishes a GPT-Image-2 generation and saves `panel_trace_v4.png`. The correct behavior is not to decide immediately whether it is beautiful. The first step is to register it:

```text
add -> compute sha/dimensions -> link prompt/session -> tag pattern -> state=candidate
```

Only after that should the user compare it with prior locked assets. This ordering prevents a subtle loss: when a user judges first and records later, rejected images lose their counterexample value. A bad sidebar-first image is useful as Pattern G evidence; a failed mobile occlusion image is useful as Pattern H evidence.

### Workflow B — phase reuse

Before a new visual phase starts, run the reuse query by `pattern_tag` and by `kind`. The user may discover that a locked Trust Trace mockup already exists and only needs token refresh. That saves generation cost and reduces visual drift. The registry should print reuse candidates with source phase, quality score, and failure notes so the user understands why a prior asset is trustworthy.

### Workflow C — deprecation

Deprecation should be easy. Visual systems improve by killing weak references. A deprecated asset remains searchable because future prompts need negative examples, but cross-phase positive reuse must exclude it. The event note should capture the reason in one line: `fails gate 5`, `generic admin shell`, `token drift`, `stale prompt`, or `hash mismatch`.

## 17. Minimal API if later promoted

If ScoutFlow later promotes this from sidecar to API, keep endpoints narrow:

```text
GET  /visual-assets?phase=&state=&pattern=
GET  /visual-assets/{asset_id}
POST /visual-assets/{asset_id}/events
POST /visual-assets/{asset_id}/gate-audits
```

Do not expose upload, public sharing, or batch delete in the first promotion. The sidecar scripts already cover local ingestion; API promotion should begin as projection and audit surface only.


## 18. Review prompts produced from assets

A registered asset should be able to produce a review prompt automatically:

```text
Review asset {{asset_id}} against ScoutFlow H5 four-panel design brief.
Use file {{file_path}}. Treat state={{state}} and phase={{phase}} as candidate facts.
Check prompt={{prompt_id}}, pattern={{pattern_tag}}, and five gates.
Return pass/fail per gate and do not claim production/runtime approval.
```

This reverses the usual flow. The asset registry is not just a passive catalog; it can feed the next audit prompt with enough context to reduce hallucinated assumptions. That is especially valuable when multiple AI sessions work on the same visual direction.

## 19. Search fields v0

Search should start simple: phase, state, kind, pattern, prompt, dimensions, pHash similarity, text notes. Full image embedding search is not needed in v0. If later added, it should remain advisory like pHash. The local user needs fast answers to practical questions: “show locked Trust Trace examples,” “show failed Gate 3 mobile examples,” “show token visuals from S06,” and “show assets derived from this raw screenshot.” These queries are covered by the proposed schema without adding vector databases or DAM-scale indexing.


## Appendix D — operator recovery and duplicate handling

visual_asset 的另一个单人高频场景是“昨天生成过，但今天忘了文件名”。因此 CRUD 脚本必须支持三种恢复入口：按 `sha256` 精确查重、按 `perceptual_hash` 近似查重、按 `prompt_id + pattern_tag + phase` 回放来源。精确查重只返回同一文件；近似查重返回 hamming distance 阈值内的候选，并要求 stdout 标明 `duplicate_candidate_only=true`，避免脚本自动覆盖旧资产。若一个文件从 `candidate` 升为 `locked`，同源近似图不得自动废弃；它们只能标成 `deprecated` 或保留为 `refined` lineage。这个规则保护 PF-V 的演化轨迹：A-J pattern 的失败、偏差、局部成功都可能成为后续 prompt template 的证据，而不是只保存最终好看的图。

建议 CLI 增加：

```bash
python tools/visual_asset.py dedupe --file assets/pfv/S08-run3.png --max-hamming 8
python tools/visual_asset.py lineage --asset-id va_20260507_0042
python tools/visual_asset.py reuse --phase U4 --pattern A --state locked
```

每个命令只读或写 visual spine DB，不触碰 capture runtime，也不创建 ScoutFlow capture。
