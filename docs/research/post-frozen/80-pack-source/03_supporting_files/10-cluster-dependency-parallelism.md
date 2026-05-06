# Cluster Dependency And Parallelism

```mermaid
flowchart LR
  C0[PF-C0 successor entry] --> LP[PF-localhost-preview]
  O1[PF-O1 overflow] --> LP
  LP --> C1[PF-C1 proof pair]
  C1 --> C2[PF-C2 RAW handoff]
  C1 -. prep .-> C3[PF-C3 object compression]
  C2 --> C4[PF-C4 hardening]
  C3 -. guides .-> C1
  C3 -. guides .-> C2
  RES[global reservoir] -. supports .-> C0
  RES -. supports .-> LP
```

| Work | Parallel? | Notes |
|---|---|---|
| C0 + O1 | yes | Thin docs/gates, no code. |
| localhost backend + frontend prep | partial | API client and router tests can parallelize; final wiring serial. |
| C1 contract + C2 contract | yes | Preparation only; real C2 waits for C1 verdict. |
| C4 prep | limited | Can prepare rubric; cannot harden before proof. |
