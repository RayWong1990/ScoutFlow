# ScoutFlow Phase 0 Bootstrap Checklist v0.1

> 目标：用最小平台骨架启动 ScoutFlow，不让治理先膨胀，也不让代码裸跑。

---

## 0. 第一件事：git init

```bash
cd /Users/wanglei/workspace/ScoutFlow
git init
```

推荐直接建 GitHub 私库；如果暂时不用 GitHub，至少本地 commit checkpoint。

---

## 1. 首批文件

```text
README.md
AGENTS.md
CLAUDE.md
DESIGN.md
.env.example
.gitignore
pyproject.toml
package.json
pnpm-workspace.yaml
Makefile
```

```text
docs/project-context.md
docs/current.md
docs/decision-log.md
docs/product-design.md
docs/specs/locked-principles.md
docs/specs/architecture.md
docs/specs/fs-layout.md
docs/specs/schema-v1.1.md
docs/specs/api-routes-v1.1.md
docs/specs/worker-contract.md
docs/research/reference-repo-index.md
```

---

## 2. 首批目录

```bash
mkdir -p apps/console/src
mkdir -p services/api/scoutflow_api/{routes,middleware,schemas,models,db,services}
mkdir -p services/api/migrations
mkdir -p workers/{common,bili,media,asr,asr_postprocess,normalize,index,raw_linker,plan_estimator,recommender,reranker}
mkdir -p packages/shared-contracts/{openapi,generated/ts,generated/py}
mkdir -p tools
mkdir -p tests/{integration,fixtures,e2e}
mkdir -p data/{db,artifacts,exports,tmp,logs,backups}
mkdir -p referencerepo
```

---

## 3. .gitignore 必须包含

```gitignore
# runtime data
data/db/
data/artifacts/
data/exports/
data/tmp/
data/logs/
data/backups/

# credentials
.env
.env.*
!.env.example
*.cookie
credentials.json

# reference repos
referencerepo/

# python
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/

# node
node_modules/
dist/
.vite/

# OS
.DS_Store
```

---

## 4. .env.example

```env
SCOUTFLOW_DATA_DIR=./data
SCOUTFLOW_DB_PATH=./data/db/scoutflow.sqlite
SCOUTFLOW_ARTIFACTS_DIR=./data/artifacts
SCOUTFLOW_RAW_DIR=~/raw
SCOUTFLOW_OBSIDIAN_VAULT=~/Documents/Obsidian
SCOUTFLOW_LOG_LEVEL=INFO
SCOUTFLOW_WORKER_CONCURRENCY=2
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
WHISPER_MODEL=large-v3
HERMES_ENABLED=false
```

---

## 5. Phase 0 最小命令

```bash
make lint
make test
make build
make check-docs
make check-contracts
make check-fs
make check-banned-words
```

初期可以让这些命令先跑 stub，但必须存在。

---

## 6. 首个 commit

```bash
git add .
git commit -m "Phase 0 skeleton: docs + LP + gitignore"
```

---

## 7. 后续 commit 顺序

```text
Commit 2: repo skeleton: apps + services + workers + packages
Commit 3: API healthz/readyz + migration runner stub
Commit 4: Console shell + 9-page static mock
Commit 5: LP-001 scope gate test + implementation
Commit 6: FS layout checker + demo capture fixture
Commit 7: OpenAPI snapshot + generated TS client
```

---

## 8. Phase 0 验收

```text
[ ] git repo initialized
[ ] first commit exists
[ ] README / AGENTS / CLAUDE / DESIGN exist
[ ] docs/current.md says current phase and next action
[ ] API healthz returns 200
[ ] readyz checks DB path and artifacts path
[ ] Console 9-page shell builds
[ ] 001_init.sql can run against empty SQLite
[ ] tools/check-banned-words runs
[ ] tools/check-fs-layout runs
[ ] tools/lint-docs runs
[ ] tools/lint-contracts runs
```

---

## 9. Phase 0 不做

```text
不连 B 站
不跑 ASR
不跑 LLM
不接 XHS
不做 Hermes
不做 Signal Workbench 真业务
不做 Agent Dispatch UI
不做 Docker
不做 Redis/Celery
不做完整向量库
```
