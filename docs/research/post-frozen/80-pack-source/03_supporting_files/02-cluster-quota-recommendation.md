# 80 任务包组织裁决

## Verdict

Do not generate a flat executable `Dispatch177-256` pack.

Generate an 80-file cluster reservoir, with only 20-30 near-term mainline tasks.

## Cluster quota

| Cluster | Quota | Open now? |
|---|---:|---|
| PF-C0 authority/successor entry | 6 | yes |
| PF-O1 overflow | 6 | yes |
| PF-localhost-preview | 18 | yes, after C0/O1 |
| PF-C1 proof pair | 12 | gated after preview loop |
| PF-C2 RAW handoff | 12 | gated after C1 pass/partial |
| PF-C3 object compression | 6 | prep only |
| PF-C4 hardening | 8 | gated after proof |
| global audit/repair/resume | 12 | reservoir |

## Why this is better

- maximizes authoring horsepower without opening all work at once
- prevents C4 hardening from outrunning C1/C2 proof
- keeps overflow in front of runtime/migration/true write temptation
