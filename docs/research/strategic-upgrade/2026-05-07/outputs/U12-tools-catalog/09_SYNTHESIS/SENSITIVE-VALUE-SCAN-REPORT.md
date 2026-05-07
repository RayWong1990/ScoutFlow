---
title: Sensitive Value Scan Report
status: candidate / evidence-bounded / not-authority
created_at: 2026-05-06
---

# Sensitive Value Scan Report

本包没有复制用户真实 settings、CLAUDE 私有文件或插件缓存正文，只保存上传输入的 manifest、候选 catalog 与审计说明。扫描策略关注 credential-shaped value，而不是普通安全词汇本身。命中数量：0。

| File | Credential-shaped hits |
|---|---:|
| none | 0 |

结论：未发现需要掩码的真实凭据形态值。升级版读取真实本地 settings 时，必须只记录 server 名、事件名、脚本路径和 key 名，不输出任何 credential value。
