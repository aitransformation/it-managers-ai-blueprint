# Section 4: OpenBrain — Central Agent Memory

> **Journey Step:** Step 4 — Build

---

## What OpenBrain is

OpenBrain is the central memory and knowledge layer for the entire agent network. It is a self-hosted PostgreSQL database with the pgvector extension installed, providing both structured SQL storage and semantic vector search.

Every agent reads from and writes to OpenBrain. It is the single source of truth for agent memory, task history, governance records, and organisational knowledge. No agent maintains its own isolated memory — all persistent state lives in OpenBrain.

OpenBrain exposes an MCP interface, allowing it to be queried by Claude Code CLI, Codex CLI, OpenClaw, and any other MCP-compatible client. The IT Manager can query the organisation's operational memory directly from their coding or agent interface.

> For the session context pattern — what to retrieve from OpenBrain at the start of every session — see [`CONTEXT.md`](../CONTEXT.md).

---

## Architecture

```
┌──────────────────────────────────────────────────────┐
│                      CLIENTS                          │
│    OpenClaw  │  Claude Code CLI  │  Codex CLI  │ ... │
└──────────────────────┬───────────────────────────────┘
                       │  MCP / HTTP / CLI
                       ▼
┌──────────────────────────────────────────────────────┐
│                    OPENBRAIN                          │
│  ┌──────────────┐        ┌────────────────┐          │
│  │  MCP Server  │        │   REST API     │          │
│  └──────────────┘        └────────────────┘          │
│  ┌────────────────────────────────────────────────┐  │
│  │           PostgreSQL + pgvector                │  │
│  │  ┌──────────────┐  ┌────────────────────────┐ │  │
│  │  │  SQL Tables  │  │    Vector Store        │ │  │
│  │  │ (structured) │  │  (semantic search)     │ │  │
│  │  └──────────────┘  └────────────────────────┘ │  │
│  └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

---

## SQL schema — core tables

### Agent task log
```sql
CREATE TABLE agent_tasks (
  id             SERIAL PRIMARY KEY,
  agent_role     VARCHAR(50)  NOT NULL,  -- 'head', 'coding', 'qa', 'monitoring', 'security', 'governance', 'reporting'
  task_type      VARCHAR(100) NOT NULL,
  initiated_by   VARCHAR(100),           -- 'it_manager', 'head_agent', 'scheduled'
  status         VARCHAR(20)  NOT NULL,  -- 'pending', 'running', 'complete', 'failed', 'escalated'
  input_summary  TEXT,
  output_summary TEXT,
  model_used     VARCHAR(100),
  data_accessed  TEXT[],                 -- array of data sources accessed
  started_at     TIMESTAMP NOT NULL DEFAULT NOW(),
  completed_at   TIMESTAMP,
  escalated      BOOLEAN DEFAULT FALSE,
  escalation_reason TEXT
);
```

### Monitoring events
```sql
CREATE TABLE monitoring_events (
  id             SERIAL PRIMARY KEY,
  source         VARCHAR(100) NOT NULL,  -- 'firewall', 'windows_event', 'backup', 'ssl', etc.
  severity       VARCHAR(20)  NOT NULL,  -- 'critical', 'high', 'medium', 'low', 'info'
  raw_alert      TEXT,
  triage_summary TEXT,
  likely_cause   TEXT,
  confidence     DECIMAL(3,2),
  status         VARCHAR(20)  NOT NULL,  -- 'new', 'triaged', 'resolved', 'escalated'
  resolved_by    VARCHAR(50),            -- 'monitoring_agent', 'it_manager', 'auto'
  received_at    TIMESTAMP NOT NULL DEFAULT NOW(),
  resolved_at    TIMESTAMP
);
```

### Governance register
```sql
CREATE TABLE governance_register (
  id             SERIAL PRIMARY KEY,
  register_type  VARCHAR(50)  NOT NULL,  -- 'ai_deployment', 'data_asset', 'policy', 'sop', 'vendor'
  name           VARCHAR(200) NOT NULL,
  owner          VARCHAR(100),
  classification VARCHAR(20),
  status         VARCHAR(20)  NOT NULL,  -- 'active', 'under_review', 'deprecated'
  next_review    DATE,
  last_reviewed  DATE,
  notes          TEXT,
  created_at     TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at     TIMESTAMP NOT NULL DEFAULT NOW()
);
```

### Vector memory (semantic knowledge store)
```sql
CREATE TABLE memories (
  id           SERIAL PRIMARY KEY,
  content      TEXT NOT NULL,
  source       VARCHAR(100),   -- 'agent_output', 'it_manager', 'document', 'incident'
  agent_role   VARCHAR(50),
  tags         TEXT[],
  embedding    VECTOR(768),    -- dimension matches local embedding model
  created_at   TIMESTAMP NOT NULL DEFAULT NOW(),
  last_accessed TIMESTAMP
);
```

### Script library
```sql
CREATE TABLE script_library (
  id             SERIAL PRIMARY KEY,
  script_name    VARCHAR(200) NOT NULL,
  description    TEXT,
  task_category  VARCHAR(100),
  file_path      VARCHAR(500),  -- path in local Gitea
  last_tested    DATE,
  test_status    VARCHAR(20),   -- 'passing', 'failing', 'untested'
  embedding      VECTOR(768),   -- semantic search on description
  created_at     TIMESTAMP NOT NULL DEFAULT NOW()
);
```

---

## MCP tools exposed

| MCP Tool | Description | Access |
|----------|-------------|--------|
| `memory_search` | Semantic search across all memories | All agents (read) |
| `memory_store` | Write a new memory with embedding | All agents (write) |
| `task_log` | Write a task event to the task log | All agents (write) |
| `task_query` | Query the task log by agent, status, or date range | All agents (read) |
| `script_search` | Semantic search of the script library | All agents (read) |
| `script_register` | Register a new script in the library | Coding Agent (write) |
| `governance_check` | Query governance register for upcoming reviews | Governance Agent (read) |
| `monitoring_log` | Write a monitoring event | Monitoring Agent (write) |
| `monitoring_query` | Query monitoring events by source, severity, status | All agents (read) |

---

## Installation

```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib

# Install pgvector extension
sudo apt install postgresql-16-pgvector  # adjust version to match

# Create OpenBrain database and user
sudo -u postgres psql << EOF
CREATE DATABASE openbrain;
CREATE USER openbrain_agent WITH ENCRYPTED PASSWORD 'your-strong-password';
GRANT ALL PRIVILEGES ON DATABASE openbrain TO openbrain_agent;
\c openbrain
CREATE EXTENSION IF NOT EXISTS vector;
GRANT ALL ON SCHEMA public TO openbrain_agent;
EOF

# Clone OpenBrain MCP server (from local Gitea mirror)
cd /opt
git clone https://gitea.internal/mirrors/open-brain.git
cd open-brain
pip install -e .

# Configure
cp .env.example .env
# Edit .env: set DATABASE_URL, embedding model endpoint (local Ollama)

# Start the MCP server
openbrain serve --host 127.0.0.1 --port 8000
```

> **Local Git only:** OpenBrain and all other software is cloned from a local Gitea mirror of the upstream repository. Public Git repositories are never accessed directly from the agent server.

---

## Embedding model

OpenBrain uses a locally-hosted embedding model to generate vector representations for all stored memories and script descriptions:

```bash
ollama pull nomic-embed-text
# Configure OpenBrain to use: http://localhost:11434/api/embeddings
```

All embeddings are generated locally. No content is sent to an external embedding API.

---

## Implementation checklist

- [ ] Install PostgreSQL with pgvector extension
- [ ] Deploy the full SQL schema — all five tables
- [ ] Install and start the OpenBrain MCP server
- [ ] Pull nomic-embed-text via Ollama and configure OpenBrain to use it
- [ ] Test: `memory_store` writes and `memory_search` retrieves correctly
- [ ] Test: `task_log` writes and `task_query` retrieves correctly
- [ ] Confirm all agents write to the correct tables
- [ ] Mirror the OpenBrain repository to local Gitea — never pull directly from public Git
- [ ] Set up daily backups of the OpenBrain database

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | Session context pattern — what to query at session start |

**Related sections:** [Section 3 — AI Agent Architecture](03-ai-agent-architecture.md) · [Section 5 — Document Ingestion](05-document-ingestion.md) · [CONTEXT.md](../CONTEXT.md)
