---
status: candidate / not-authority / not-runtime-approval
created_for: Cloud Prompt U4 Visual Asset Spine
requested_date: 2026-05-07
generated_in_session_date: 2026-05-06
write_enabled: false
claim_scope: spec-only; no production code modification; no dispatch authorization
---

# LIVE-WEB-EVIDENCE — U4 external evidence matrix

> truthful claim label: live web browsing was **not available** in this run. Vendor rows below are URL seeds and evaluation targets, not verified 2026 facts. `live_verified_vendor_count=0`.

## 1. Truthful browsing status

The cloud prompt requested ≥20 live web searches across prosumer DAM, prompt registries, design tokens, pattern libraries, image-to-code, single-creator workflow tools, Apple HIG, and Material 3. In this execution environment, the `web.run` browser is disabled. I did not access live vendor pages, did not compare current pricing, did not verify 2026 product claims, and did not inspect current docs. This file therefore provides a **verification matrix** that can be used in a future browse-enabled run.

This is deliberately conservative. The U4 core spec does not depend on unverified vendor claims; it uses local ScoutFlow facts and generic local-first design principles. External tools are treated as inspiration categories only.


## Source Register / 证据边界

- PRD-v2/SRD-v2 的稳定事实：ScoutFlow 是 single-user、local-first、SQLite + FS + state words 的 authority-first 工作台；当前不得自动批准 SaaS、多用户、runtime 扩张、media/ASR、browser automation、vault true write 或 migration。
- Capture Station 的已读事实：`apps/capture-station/package.json` 是 React 18 + Vite 5，未把 Tailwind/shadcn/Panda/Radix/React Flow/TanStack/Lucide 写成已批准依赖；现有 H5 代码使用深海蓝 palette、inline style、URL Bar + Vault Preview/Dry Run + Live Metadata + Capture Scope + Trust Trace 的工作台结构。
- Visual docs 的已读事实：`design-brief.md` 固定 4 面板扫描顺序；`five-gate-checklist.md` 要求 5 gate 全过才可称 visual pass；`trust-trace-graph-spec.md` 固定 `capture -> capture_state -> metadata_job -> probe_evidence -> receipt_ledger -> media_audio -> audit` 节点链。
- 本地缺口：容器内没有 `~/workspace/ScoutFlow`、没有 `~/.claude/rules/aesthetic-first-principles.md`、没有 PF-V 实际 `INDEX.csv`，因此相关内容均标为 `needs_local_refresh`。
- Live web 缺口：本运行环境禁用实时网页浏览；任何 vendor / 2026 工具状态只能列为待验证 URL 种子，不得写成已访问事实。

## 2. Vendor / pattern URL seeds requiring future verification

| # | category | target | URL seed | status in this run | why it matters |
|---:|---|---|---|---|---|
| 1 | prosumer DAM | Air | https://air.inc/ | not accessed | lightweight visual asset organization patterns |
| 2 | enterprise/prosumer DAM | Brandfolder | https://brandfolder.com/ | not accessed | contrast with overbuilt DAM features |
| 3 | creative asset browser | Eagle | https://eagle.cool/ | not accessed | local image library UX inspiration |
| 4 | photo library | Mylio | https://mylio.com/ | not accessed | local-first media catalog ideas |
| 5 | launcher/workflow | Raycast | https://www.raycast.com/ | not accessed | single-user command palette / extension style |
| 6 | image editing | Pixelmator Pro | https://www.pixelmator.com/pro/ | not accessed | prosumer image workflow boundary |
| 7 | notes/assets | Bear | https://bear.app/ | not accessed | single-user tagging and writing workflow |
| 8 | design tokens | Style Dictionary | https://styledictionary.com/ | not accessed | token transform conventions |
| 9 | design tokens | Tokens Studio | https://tokens.studio/ | not accessed | Figma token workflow comparison |
| 10 | design tokens | Theo | https://github.com/salesforce-ux/theo | not accessed | historical token transformer reference |
| 11 | design tokens | Specify | https://specifyapp.com/ | not accessed | token pipeline/product comparison |
| 12 | image-to-code | Anima | https://www.animaapp.com/ | not accessed | design-to-code boundary risks |
| 13 | image-to-code | Locofy | https://www.locofy.ai/ | not accessed | screenshot/design-to-code positioning |
| 14 | image-to-code | Builder.io Visual Copilot | https://www.builder.io/ | not accessed | AI visual/code conversion patterns |
| 15 | code gen | v0.dev | https://v0.dev/ | not accessed | prompt-to-UI flow and cautionary boundary |
| 16 | OSS screenshot-to-code | screenshot-to-code | https://github.com/abi/screenshot-to-code | not accessed | local/open image-to-code prototype risk |
| 17 | prompt registry | PromptLayer | https://promptlayer.com/ | not accessed | prompt registry concepts |
| 18 | prompt registry | LangSmith / Hub | https://smith.langchain.com/ | not accessed | prompt/version/trace concepts |
| 19 | prompt observability | Helicone | https://www.helicone.ai/ | not accessed | run/cost metadata pattern |
| 20 | pattern library | Storybook | https://storybook.js.org/ | not accessed | component story/pattern documentation |
| 21 | component/pattern | Bit Cloud | https://bit.cloud/ | not accessed | reusable component workspace comparison |
| 22 | pattern library | Pattern Lab | https://patternlab.io/ | not accessed | pattern language structure |
| 23 | AI visual workflow | Krea | https://www.krea.ai/ | not accessed | image generation workflow comparison |
| 24 | AI visual workflow | Freepik Spaces | https://www.freepik.com/ | not accessed | creative asset generation ecosystem |
| 25 | AI site/prototype | Raelume | https://www.relume.io/ | not accessed | prompt-to-site workflow comparison |
| 26 | AI app workflow | MindStudio | https://www.mindstudio.ai/ | not accessed | single-creator AI workflow packaging |
| 27 | design guideline | Apple HIG | https://developer.apple.com/design/human-interface-guidelines/ | not accessed | 5-Gate visual quality context |
| 28 | design guideline | Material 3 | https://m3.material.io/ | not accessed | current Material guidance context |

## 3. Verification template for future browse-enabled run

```yaml
vendor: <name>
url: <actual page>
accessed_at: <ISO timestamp>
page_status: reachable|redirect|blocked|not_found
claim_used: <specific current claim>
claim_quote: <verbatim quote>
single_user_fit: high|medium|low
enterprise_drift_risk: high|medium|low
u4_relevance:
  visual_asset: <yes/no + reason>
  prompt_template: <yes/no + reason>
  design_token: <yes/no + reason>
  pattern_library: <yes/no + reason>
notes: <what should or should not influence U4>
```

## 4. Expected evidence questions

### Prosumer DAM

The question is not “what features do DAM tools have?” but “which features should a single-user local-first visual spine deliberately avoid?” Likely avoid: multi-user permissions, brand portals, public share links, SSO, asset approval workflows, rights management, CDN delivery, usage analytics, and enterprise taxonomy. Likely keep: tags, thumbnails, duplicate detection, lightweight metadata, collections/phase reuse, search, and local file integrity.

### Prompt registry

The U4 prompt registry needs lineage, version, parameter schema, run cost, and quality score. It does not need hosted traces, collaborative prompt hub, production deployment, or API observability unless later promoted.

### Design tokens

The immediate need is a single JSON file and optional CSS variable generator. A future verification run should compare current token standards and tools, but U4 should not install token pipelines until Capture Station implementation gate opens.

### Pattern library

Storybook/Bit/Pattern Lab may inspire pattern documentation shape, but U4 patterns are workflow patterns across image/code/copy/data/dispatch, not only UI components.

### Image-to-code

Image-to-code tools are useful cautionary references. U4 should record generated assets and prompts, but not allow screenshot-to-code output to mutate production app without explicit code lane approval.

## 5. Current conclusion without live web

The absence of live web reduces external-evidence confidence, but it does not invalidate the local sidecar spine. The four-module architecture is driven by observed ScoutFlow/PF-V needs: visual files need lineage, prompts need registry, tokens need a single candidate source, and patterns need reusable definitions. External tools should be used only to sharpen vocabulary and prevent overbuilding, not to justify SaaS-like scope.

## 6. Acceptance checklist for future refresh

- Visit at least 20 URLs and record access date/time.
- Quote only claims visible on the page or official docs.
- Separate vendor marketing from U4 design decisions.
- Update this file with `live_verified_vendor_count`.
- Do not change core U4 boundaries merely because a vendor offers a feature.


## 7. Future live-search query plan

A browse-enabled run should use at least these searches and record dates:

| # | query |
|---:|---|
| 1 | `Air digital asset management 2026 features visual assets` |
| 2 | `Brandfolder DAM features 2026 brand asset management` |
| 3 | `Eagle app visual asset management local library` |
| 4 | `Mylio local photo library 2026` |
| 5 | `Raycast extensions workflow single user 2026` |
| 6 | `Pixelmator Pro 2026 image editing workflow` |
| 7 | `Style Dictionary v4 design tokens documentation` |
| 8 | `Tokens Studio design tokens Figma 2026` |
| 9 | `Specify design token platform documentation` |
| 10 | `Anima AI design to code 2026` |
| 11 | `Locofy AI design to code 2026` |
| 12 | `Builder.io Visual Copilot documentation` |
| 13 | `v0.dev UI generation documentation 2026` |
| 14 | `PromptLayer prompt registry versions` |
| 15 | `LangSmith prompt hub prompt versioning` |
| 16 | `Helicone prompt management cost observability` |
| 17 | `Storybook 8 documentation component library` |
| 18 | `Bit Cloud component platform 2026` |
| 19 | `Pattern Lab atomic design documentation` |
| 20 | `Krea AI image generation workflow 2026` |
| 21 | `Freepik Spaces AI workflow` |
| 22 | `Relume AI website builder workflow` |
| 23 | `MindStudio AI app workflow` |
| 24 | `Apple Human Interface Guidelines visual hierarchy accessibility 2026` |
| 25 | `Material 3 Expressive design 2026 accessibility` |

## 8. Evidence scoring rubric

For each verified source, score it against U4 instead of copying its feature list.

| score | interpretation |
|---:|---|
| 0 | irrelevant or harmful to local-first scope |
| 1 | interesting vocabulary only |
| 2 | useful UX pattern, not a schema driver |
| 3 | supports one U4 module decision |
| 4 | supports multiple U4 module decisions |
| 5 | should materially change U4 spec |

Any score 5 must include a direct quote, access date, and explanation of why it does not violate hard boundaries.

## 9. Expected anti-patterns to catch

- A DAM vendor may make collaboration look essential; U4 must remember single-user scope.
- A prompt observability vendor may imply hosted tracing; U4 only needs local registry fields.
- A token platform may imply full pipeline adoption; U4 only needs JSON + optional CSS generator.
- Image-to-code marketing may imply production-ready code; U4 keeps code changes in a separate lane.
- Design guideline pages may change wording; U4 should cite exact current pages after browsing.

## 10. How to update this file after browsing

Replace each `not accessed` status with:

```text
accessed 2026-05-07, official docs page, claim quoted, U4 relevance score N
```

Then update the README stdout:

```yaml
live_web_browsing_used: true
live_verified_vendor_count: <count>
multi_pass_completed: "10/10"  # only if PF-V/local gaps are also resolved or separately noted
```

Do not update `CLOUD_U4_VISUAL_ASSET_SPINE_COMPLETE` to true unless the PF-V CSV and canonical 5-Gate file are also actually read, or unless the stdout explicitly defines complete as “web-only refresh complete.”


## 11. How live evidence could change U4

A future web refresh may change details, but only specific findings should change core spec:

| possible finding | change allowed |
|---|---|
| Style Dictionary current format differs | adjust JSON compatibility notes |
| Tokens Studio has useful naming convention | add optional naming note, no package requirement |
| Eagle/Mylio show strong local tagging pattern | refine visual_asset tag/search ideas |
| PromptLayer/LangSmith expose lineage terminology | refine prompt_template field names |
| Storybook/Pattern Lab show better pattern card structure | refine markdown export format |
| Apple/Material/WCAG current guidance updates gate wording | update 5-Gate table after citation |
| Image-to-code tools claim production output | no automatic scope expansion; keep boundary |
| DAM tools emphasize collaboration | no change unless single-user local value is clear |

## 12. Citation discipline for future update

Every future vendor claim should have:

```text
source name
official URL
access date
one-sentence claim
quoted phrase or exact doc section
U4 decision influenced
```

Avoid citing third-party summaries for product features unless official pages are unreachable. For open-source projects, cite the repository and README commit/date if possible.

## 13. Current no-web replacement evidence

Instead of live web, this run used three available evidence classes:

1. Uploaded U4 prompt and post176 audit pack.
2. GitHub connector fetches for ScoutFlow PRD/SRD and Capture Station files.
3. Local container checks for unavailable workspace and canonical 5-Gate file.

This evidence is enough to build a candidate local-first spec. It is not enough to claim current vendor comparisons. That distinction is preserved across the ZIP.

## 14. Vendor categories most likely to matter

The most relevant external category is not enterprise DAM; it is local creative asset browsers like Eagle/Mylio-style workflows, because they show how a single creator can search and tag images without SaaS governance. The second most relevant category is prompt registry/observability, but only for field vocabulary. The third is token tools, but only for JSON compatibility. Image-to-code tools are mostly cautionary because ScoutFlow production code remains gated.


## 15. Future evidence downgrade policy

If a vendor page cannot be reached, do not use cached memory as a verified claim. Mark it `unreachable` and use another official source or skip it. If a tool has changed names, record the redirect and new name. If pricing or features are hidden behind login, do not infer them. The goal is not to force 20 favorable citations; the goal is to avoid ungrounded decisions.

## 16. Expected final live-web summary shape

```yaml
LIVE_WEB_REFRESH_COMPLETE: true
access_date: 2026-05-07
verified_sources: 24
unreachable_sources: 2
sources_affecting_spec: 5
sources_reference_only: 19
core_boundary_changed: false
notable_updates:
  - "token format note updated after Style Dictionary docs"
  - "pattern card export refined after Storybook/Pattern Lab review"
```

This shape keeps future web work focused. Most external research should refine vocabulary, not expand scope.

## 17. Web evidence and claim labels

After browsing, each module can keep a high structural claim while external claims get their own labels. For example, `design_token` may be ≥95% for local JSON structure and 80% for current tool comparison. Mixing those numbers into one confidence score would be misleading. The README should preserve this separation.


## Appendix B — exact refresh protocol for next browser-enabled pass

下一次可用浏览器时，不要只打开厂商首页。每个 vendor 至少记录四项：访问日期、产品页 URL、与 U4 相关的能力点、与 ScoutFlow 不采用的企业化能力。对于 design token 工具，优先查 release notes、schema docs、CLI docs；对于 image-to-code 工具，优先查是否支持 React、Tailwind/CSS variables、Figma/screenshot 输入、export ownership；对于 prompt registry，优先查 versioning、lineage、cost/quality metadata；对于 DAM，优先查 tagging、dedupe、thumbnail、local/offline 能力。

建议验证表头：

```csv
category,vendor,url,access_date,verified,capability_relevant_to_U4,enterprise_features_to_avoid,notes
prompt_registry,LangSmith Hub,https://...,2026-05-07,false,prompt version lineage,team sharing/RBAC,needs browser refresh
```

### No-claim rule

在 live refresh 完成前，本文件中的 vendor 名只能作为“待查对象”，不能写成“已证明 2026 行业趋势”。最终 U4 spec 可引用这些工具的模式语言，但不得把未访问页面当成 evidence。若 refresh 发现某产品已停服、改名或功能变化，应直接更新本文件并保留旧条目为 `superseded`，不要为了满足 20 条数量而保留假阳性。

### Minimum 20 target grouping

建议浏览顺序：DAM 6 条、design token 4 条、image-to-code 5 条、prompt registry 4 条、pattern library 3 条、single-creator workflow 4 条、platform guidelines 2 条。这样即使部分 URL 不可访问，也能保留超过 20 条候选，并区分“已访问可引用”和“仅候选待查”。


## Appendix C — source acceptance thresholds

浏览器补证时，接受证据分三档。A 档是官方文档、release note、pricing/feature page，可直接引用；B 档是官方 blog、help center、GitHub repo，可作为功能趋势证据但需标明口径；C 档是第三方评测、社区帖子、截图，只能作为线索，不作为规格依据。若一个 vendor 只有 C 档材料，本 U4 spec 不应把它列为 verified vendor。对于 Apple HIG / Material 3 这类平台规则，只接受官方 guideline 或官方设计 blog，不接受二手摘要替代 canonical。

证据刷新后应重写本文件的 stdout 摘要：`live_web_browsing_used=true`、`live_verified_vendor_count=<A+B档数量>`，并把未通过项留在 `rejected_or_unverified` 表里。这样后续审计能看到数量达标和事实可信度，而不是只有 vendor 名单。
