---
title: Local Rescan Checklist
status: candidate / operator-runbook / not-authority
created_at: 2026-05-06
---

# Local Rescan Checklist

此清单用于把本包从“上传证据版”升级为“真实本机全量版”。它只读扫描，不修改配置，不调用 skill，不执行 hook 的业务动作。

```bash
set -euo pipefail
ROOTS=(
  "$HOME/.claude/skills"
  "$HOME/.claude/agents"
  "$HOME/.claude/rules"
  "$HOME/.claude/plugins"
  "$HOME/.claude/scripts"
  "$HOME/.codex"
  "$HOME/workspace/ScoutFlow/.claude"
  "$HOME/Library/Application Support/Claude"
)
for d in "${ROOTS[@]}"; do
  if [ -d "$d" ]; then
    printf 'FOUND	%s
' "$d"
    find "$d" -maxdepth 4 -type f       \( -name '*.md' -o -name '*.json' -o -name '*.sh' -o -name '*.py' -o -name '*.toml' -o -name '*.yaml' -o -name '*.yml' \)       -print | sed 's#^#FILE	#'
  else
    printf 'MISSING	%s
' "$d"
  fi
done
```

推荐把输出保存成 `local-inventory.tsv` 后再做下一步：按 frontmatter 聚合 `name`、`description`、`allowed_tools`、`activation`、`hooks`、`dependencies`；对 settings 类文件只记录 key 名、事件名、server 名、脚本路径，绝不输出 credential value。然后用本包的 `verification_status` 字段进行二次标注：真实存在的 source path 改为 `verified-local-path`，只在 prompt 中出现的仍保留 `specified-by-U12-prompt`。

## 升级验收

升级版至少需要满足四项：第一，所有 entry 的 `source` 都指向本地真实文件；第二，settings 中任何 credential 值均已掩码；第三，重复 skill/agent 名称能定位到具体路径；第四，hook/script 冲突能对应到实际事件或脚本，而不只是设计风险。
