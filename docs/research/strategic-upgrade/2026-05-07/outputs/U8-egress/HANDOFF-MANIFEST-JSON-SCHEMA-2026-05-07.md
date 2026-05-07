---
title: HANDOFF MANIFEST JSON SCHEMA — ScoutFlow Egress v1
status: candidate / schema / not-authority
authority: not-authority
claim_label: "95%"
created_at: 2026-05-07
generated_in_environment: 2026-05-06
manifest_json_variants: 4
write_enabled: false
---

# HANDOFF MANIFEST JSON SCHEMA — ScoutFlow Egress v1

## 0. 证据与边界口径

本交付只声明 ScoutFlow 单方面写出的文件级 egress contract，不定义 SDK、OpenAPI client、双向同步 broker，也不修改任何下游。PRD v2 的最高边界是：ScoutFlow 是单 user、local-first 的采集与证据工作台；RAW、Obsidian、DiloFlow 是下游消费者，不是 ScoutFlow 项目的一部分。SRD v2 的最高边界是：当前生效的是 metadata-only、receipt、trust trace、redaction/secret scan baseline；Phase 2+ 对象仍主要是 outline，不能被文件导出契约误读成 runtime unlock。

本环境已经读取上传的 post176 audit pack 与 GitHub 上的 PRD/SRD、Run-3+4 C2 文件。普通 live web 浏览在当前会话被禁用，所以本文所有外部 vendor/frontmatter 口径只作为“需刷新验证的公共模式候选”，不标记为 live verified。`~/workspace/DiloFlow/`、`~/workspace/raw/`、`~/workspace/hermes-agent/` 与 Obsidian 本地 vault 在当前容器没有出现；因此 DiloFlow 与 hermes-agent 的 receiver-side parser 只能给出单方、保守、低耦合的文件契约，不能声称已经被下游 repo 实测接受。

硬边界在所有下游一致：`write_enabled=false` 保持；ScoutFlow 永不直写 `~/workspace/raw/`；凭据、cookie、token、QR 图片、browser profile path、auth sidecar、raw stdout/stderr 中可能含秘密的片段不得进入 egress；Bilibili/XHS 等平台原作者隐私字段只允许最小必要、脱敏后的事实摘要；manifest 是一次 handoff 的索引，不是下游 acceptance 证明；supersede 只能标记资产生命周期，不允许反向覆盖下游知识库事实。

## 1. Schema 目标

U8 的 manifest schema 解决一个非常具体的问题：ScoutFlow 文件已经能生成 preview、RAW staging note 或 topic card，但下游不知道一次 handoff 里有几个 asset、每个 asset 从何而来、是否已 redaction、是否替代旧版本、是否需要人工复制。manifest 不是 SDK，不是 DB migration，不是 broker。它是文件夹级目录账本。

## 2. Schema 不变量

- `schema_version` 固定 `scoutflow.egress.v1`。
- `write_enabled` 必须为 `false`。
- 所有 `relative_path` 不允许绝对路径或 `..`。
- 每个 asset 必须有 checksum、redaction、supersede。
- `redaction.applied` 必须为 `true`。
- `target_downstream` 必须是四个下游之一。
- 下游 acceptance 只能在有 readback 证明时出现。
- manifest 允许人工步骤，不执行人工步骤。

## 3. 通用 manifest schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://scoutflow.local/schemas/egress/manifest-v1.json",
  "title": "ScoutFlow Egress Handoff Manifest v1",
  "type": "object",
  "required": [
    "schema_version",
    "handoff_id",
    "target_downstream",
    "created_at",
    "write_enabled",
    "assets",
    "redaction_summary",
    "supersede_summary"
  ],
  "properties": {
    "schema_version": {
      "const": "scoutflow.egress.v1"
    },
    "handoff_id": {
      "type": "string",
      "pattern": "^sfh_[A-Za-z0-9_\\-]+$"
    },
    "target_downstream": {
      "enum": [
        "diloflow",
        "raw_vault",
        "obsidian",
        "hermes-agent"
      ]
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "write_enabled": {
      "const": false
    },
    "handoff_state": {
      "enum": [
        "prepared",
        "staged",
        "pending_user_manual_transfer",
        "accepted",
        "needs_edit",
        "rejected",
        "superseded"
      ]
    },
    "assets": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/asset"
      }
    },
    "redaction_summary": {
      "$ref": "#/$defs/redaction_summary"
    },
    "supersede_summary": {
      "type": "object"
    },
    "manual_steps_required": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "audit_notes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "$defs": {
    "asset": {
      "type": "object",
      "required": [
        "asset_id",
        "kind",
        "relative_path",
        "checksums",
        "redaction",
        "supersede"
      ],
      "properties": {
        "asset_id": {
          "type": "string",
          "pattern": "^sfa_[A-Za-z0-9_.\\-]+$"
        },
        "kind": {
          "type": "string"
        },
        "relative_path": {
          "type": "string",
          "not": {
            "pattern": "(^/|\\.\\.)"
          }
        },
        "checksums": {
          "type": "object",
          "required": [
            "sha256",
            "size_bytes"
          ],
          "properties": {
            "sha256": {
              "type": "string",
              "pattern": "^[a-f0-9]{64}$"
            },
            "size_bytes": {
              "type": "integer",
              "minimum": 0
            }
          }
        },
        "redaction": {
          "type": "object",
          "required": [
            "applied",
            "ruleset_version"
          ],
          "properties": {
            "applied": {
              "const": true
            },
            "ruleset_version": {
              "type": "string"
            }
          }
        },
        "supersede": {
          "type": "object",
          "required": [
            "status",
            "supersedes",
            "superseded_by"
          ],
          "properties": {
            "status": {
              "enum": [
                "active",
                "deprecated",
                "superseded",
                "retracted",
                "archived",
                "duplicate"
              ]
            },
            "supersedes": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "superseded_by": {
              "anyOf": [
                {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                {
                  "type": "null"
                }
              ]
            }
          }
        }
      }
    },
    "redaction_summary": {
      "type": "object",
      "required": [
        "applied",
        "ruleset_version",
        "findings_count"
      ],
      "properties": {
        "applied": {
          "const": true
        },
        "ruleset_version": {
          "type": "string"
        },
        "findings_count": {
          "type": "integer",
          "minimum": 0
        }
      }
    }
  }
}
```

## 4. DiloFlow variant schema

```json
{
  "allOf": [
    {
      "$ref": "manifest-v1.json"
    }
  ],
  "properties": {
    "target_downstream": {
      "const": "diloflow"
    },
    "assets": {
      "items": {
        "properties": {
          "kind": {
            "enum": [
              "diloflow_capture",
              "topic_card",
              "signal",
              "receipt_summary"
            ]
          },
          "channel": {
            "type": "string"
          },
          "next_action": {
            "enum": [
              "follow",
              "park",
              "reject",
              "need_more_evidence"
            ]
          }
        }
      }
    }
  }
}
```

## 5. RAW vault variant schema

```json
{
  "allOf": [
    {
      "$ref": "manifest-v1.json"
    }
  ],
  "properties": {
    "target_downstream": {
      "const": "raw_vault"
    },
    "write_enabled": {
      "const": false
    },
    "handoff_state": {
      "enum": [
        "staged",
        "pending_user_manual_transfer",
        "accepted",
        "needs_edit",
        "rejected"
      ]
    },
    "assets": {
      "items": {
        "properties": {
          "kind": {
            "enum": [
              "raw_note_candidate",
              "script_seed_candidate",
              "receipt_summary"
            ]
          },
          "target_hint": {
            "const": "~/workspace/raw/00-Inbox/"
          }
        }
      }
    }
  }
}
```

## 6. Obsidian variant schema

```json
{
  "allOf": [
    {
      "$ref": "manifest-v1.json"
    }
  ],
  "properties": {
    "target_downstream": {
      "const": "obsidian"
    },
    "assets": {
      "items": {
        "properties": {
          "kind": {
            "enum": [
              "obsidian_note",
              "topic_card",
              "source_index"
            ]
          },
          "frontmatter_namespace": {
            "const": "scoutflow_"
          },
          "wikilink_hints": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}
```

## 7. hermes-agent variant schema

```json
{
  "allOf": [
    {
      "$ref": "manifest-v1.json"
    }
  ],
  "properties": {
    "target_downstream": {
      "const": "hermes-agent"
    },
    "execution_approval": {
      "const": false
    },
    "runtime_approval": {
      "const": false
    },
    "allowed_operations": {
      "type": "array",
      "items": {
        "enum": [
          "read_manifest",
          "read_redacted_markdown",
          "produce_audit_report"
        ]
      }
    },
    "forbidden_operations": {
      "type": "array",
      "minItems": 1
    }
  }
}
```

## 8. 示例 manifest

```json
{
  "schema_version": "scoutflow.egress.v1",
  "handoff_id": "sfh_20260507_raw_01",
  "target_downstream": "raw_vault",
  "created_at": "2026-05-07T00:00:00Z",
  "created_by": "ScoutFlow egress generator",
  "write_enabled": false,
  "handoff_state": "pending_user_manual_transfer",
  "source_baseline": {
    "prd": "PRD-v2-2026-05-04",
    "srd": "SRD-v2-2026-05-04",
    "run_evidence": "Run-3+4 C2 partial"
  },
  "manual_steps_required": ["User copies note files into RAW 00-Inbox"],
  "assets": [
    {
      "asset_id": "sfa_01KQYY9KP26SSZA6285MAY706S_raw_note_candidate_r001",
      "kind": "raw_note_candidate",
      "relative_path": "assets/sfa_01KQYY9KP26SSZA6285MAY706S_raw_note_candidate_r001.md",
      "checksums": {
        "sha256": "0000000000000000000000000000000000000000000000000000000000000000",
        "size_bytes": 1000,
        "content_encoding": "utf-8"
      },
      "redaction": {"applied": true, "ruleset_version": "scoutflow-redaction-v1", "masked_fields": []},
      "supersede": {"status": "active", "revision": 1, "supersedes": [], "superseded_by": null}
    }
  ],
  "redaction_summary": {"applied": true, "ruleset_version": "scoutflow-redaction-v1", "findings_count": 0},
  "supersede_summary": {"has_supersede_events": false, "events": []},
  "forbidden_fields_checked": ["cookie", "token", "qrcode", "browser_profile_path", "signed_url"],
  "audit_notes": ["No direct RAW write. Acceptance remains pending."]
}
```

## 9. 校验顺序

1. JSON parse。
2. JSON Schema validate。
3. `write_enabled == false` 硬检查。
4. 所有 `relative_path` resolve 后仍在 handoff 目录内。
5. 资产存在。
6. checksum 匹配。
7. frontmatter 与 manifest 的 `asset_id/kind/handoff_id` 一致。
8. redaction report 存在且 `applied=true`。
9. supersede graph 无循环。
10. downstream-specific enum 合法。
11. 若 target 是 RAW，handoff_state 默认不得是 `accepted`。
12. 若 target 是 hermes，execution/runtime approval 必须 false。

## 10. 为什么不单独放 4 个 JSON 文件

U8 prompt 同时要求“10 个文件”与“4 个 JSON schema 文件”。为保持 file count=10，本交付把四个下游 schema 以内嵌 JSON code block 放入本 Markdown。未来实际 repo 实现时可拆成：`manifest.schema.json`, `diloflow.schema.json`, `raw-vault.schema.json`, `obsidian.schema.json`, `hermes-agent.schema.json`。拆分不改变合同语义。

## 自检清单

| # | 检查项 | 结论 |
|---:|---|---|
| 1 | 是否漂移成 SDK / OpenAPI / broker | 否，仅文件级 frontmatter、目录、manifest |
| 2 | 是否把 RAW / Obsidian / DiloFlow 当 ScoutFlow 子模块 | 否，全部是 downstream candidate |
| 3 | 是否暗示 ScoutFlow 直写 `~/workspace/raw/` | 否，RAW 仅 staging + manual transfer |
| 4 | 是否把 C2 partial 写成 pass | 否，保留 pending_user_manual_transfer |
| 5 | 是否把 vault preview 当 true write | 否，preview_only / write_enabled=false |
| 6 | 是否解锁 media / ffmpeg / ASR / browser automation | 否，blocked lanes 原样保留 |
| 7 | 是否包含凭据、cookie、token、QR 图片 | 规范中禁止，实际未导出此类文件 |
| 8 | 是否覆盖 supersede | 是，软标记 + manifest 索引 + 下游 prune 触发 |
| 9 | 是否覆盖 redaction | 是，字段级 omit/mask/hash + 自动检查建议 |
| 10 | 是否声称 live web 已完成 | 否，明确 blocked / not live verified |
| 11 | 是否声称本地 DiloFlow/hermes repo 已验证 | 否，当前容器未发现 sibling repo |
| 12 | 是否污染 Obsidian template | 否，仅给兼容字段，不要求替换用户模板 |
| 13 | 是否让下游必须遵守 | 否，单方声明，建议遵守 |
| 14 | 是否可由单人实现 | 是，建议 ≤400 LOC + 4 schema 文件 |
| 15 | 是否与 U1-U7 基线冲突 | 未发现直接冲突；保持 v2 boundaries |
| 16 | 是否允许旧资产静默失效 | 否，必须写 superseded_by / manifest supersede_summary |
| 17 | 是否混淆 source_url 与 signed URL | 否，signed URL 需去签名或 omit |
| 18 | 是否把 PII redaction 当真实已跑 | 否，本文是 spec，非执行日志 |
## 11. Schema 设计取舍

本 schema 故意没有把所有业务字段都塞进通用 asset。原因是四个 downstream 的最小消费字段不同：RAW 只需要四字段 note 和 manual transfer；Obsidian 需要 namespace 和 tags/aliases；DiloFlow 需要 channel/next_action；hermes-agent 需要 allowed/forbidden operations。通用层只约束安全与生命周期不变量，下游层约束消费语义。这样可以避免一改 DiloFlow routing 就破坏 RAW parser，也避免 RAW 四字段模板被 Obsidian/Dataview 字段污染。

## 12. Schema validator 最小实现

验证器不需要复杂依赖；Python 标准库可做大部分硬检查：JSON parse、relative path containment、checksum、`write_enabled=false`。JSON Schema 校验可作为可选依赖；如果没有 `jsonschema` 包，也必须执行硬检查。硬检查失败优先级高于 schema 通过。例如 schema 没能表达某个绝对路径边界时，path containment 函数仍必须拒绝。validator 输出应是结构化 `validation-report.json`，字段包括 `passed`, `errors`, `warnings`, `assets_checked`, `checksum_failures`, `redaction_failures`, `supersede_failures`。

## 13. 向后兼容策略

`scoutflow.egress.v1` 的下游 parser 应忽略未知字段，但不得忽略安全字段。未知字段可以 warning；`write_enabled=true`、`redaction.applied=false`、checksum mismatch、path escape、unsupported supersede status 必须 hard fail。这样未来 v1.1 添加字段时不会破坏旧 importer，同时仍保持安全红线。
