# Section 3: AI Agent Architecture — Multi-Agent System

> **Journey Step:** Step 4 — Build

---

## From single agent to agent network

The initial deployment of a single AI agent handling all IT operations tasks is the correct starting point. It is not the destination.

A single agent with broad responsibilities, access to multiple systems, and a growing task backlog quickly becomes a bottleneck and a governance challenge. As capability expands, the correct architecture is a network of specialist agents operating under the direction of a coordinating Head Agent.

This architecture should be planned from the first deployment, even if only the Head Agent and one specialist are initially active. The infrastructure, data architecture, and governance framework in this section are designed to support the full network from day one.

---

## The agent hierarchy

```
┌─────────────────────────────────────────────────────────┐
│                       HEAD AGENT                        │
│           Orchestration, task routing, escalation        │
│       Model: Mid-range (Llama 3 70B / Mistral Large)    │
└──────┬──────────┬──────────┬──────────┬────────┬────────┘
       │          │          │          │        │
       ▼          ▼          ▼          ▼        ▼
┌──────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌──────────┐
│  CODING  │ │   QA   │ │MONITOR │ │SECURITY│ │GOVERNANCE│
│  AGENT   │ │ AGENT  │ │ AGENT  │ │ AGENT  │ │  AGENT   │
└──────────┘ └────────┘ └────────┘ └────────┘ └──────────┘
                                                     │
                                                     ▼
                                             ┌──────────────┐
                                             │  REPORTING   │
                                             │    AGENT     │
                                             └──────────────┘
```

All agents read from and write to OpenBrain (PostgreSQL + pgvector).  
All agent task flows, outputs, and decisions are logged to SQL.

---

## Agent communication protocol

```
IT Manager request
        ↓
  Head Agent (interprets, routes)
        ↓
  Specialist Agent (executes, writes result to OpenBrain)
        ↓
  Head Agent (assembles, quality-checks, escalates if needed)
        ↓
  IT Manager response
```

All steps in this flow are written to the OpenBrain SQL task log with timestamps, agent identity, action taken, data accessed, and output produced. Direct agent-to-agent communication does not occur without the Head Agent as intermediary.

---

## Agent role definitions

### Head Agent

The orchestration layer. Receives tasks from the IT Manager, routes them to appropriate specialist agents, monitors progress, assembles outputs, and escalates when human decision is required. Does not execute specialist tasks directly.

| Attribute | Value |
|-----------|-------|
| Primary model | Mid-range local (Llama 3 70B or Mistral Large) |
| Frontier fallback | OpenRouter → Claude Sonnet (Internal/Public data only) |
| Tool access | OpenBrain read/write, all agent APIs, IT Manager notification channel |
| Data scope | Metadata and task routing only — does not handle raw operational data |
| Deployment stage | Day 1 (Week 5) |

**Head Agent responsibilities:**
- Receive and interpret task requests from the IT Manager
- Decompose complex tasks into sub-tasks and route to specialist agents
- Monitor specialist agent progress and assemble final outputs
- Maintain a task log in OpenBrain for all delegated work
- Escalate to the IT Manager when specialist agents return low-confidence outputs or encounter out-of-scope conditions
- Apply the **local-script-first rule**: always attempt to resolve a task via a local script before invoking a frontier model

---

### Coding Agent

Designs, writes, tests, and documents internal tools and automation scripts. The primary consumer of frontier model capability — complex code generation is the task type most likely to require a frontier model and least likely to involve sensitive data.

| Attribute | Value |
|-----------|-------|
| Primary model | DeepSeek Coder 33B (local) via Ollama |
| Frontier fallback | OpenRouter → Claude Opus or Codex (Internal/Public data only) |
| Coding interface | Claude Code CLI or OpenAI Codex CLI, running locally |
| Tool access | Local Git (Gitea), LAMP/ISPConfig API, OpenBrain read/write |
| Data scope | Internal and Public only — no Restricted or Confidential data in coding tasks |
| Deployment stage | Week 6 |

**Local-script-first rule:** The Coding Agent shall always attempt to resolve a task using an existing local script before generating new code or invoking a frontier model. The local script library (stored in Gitea and indexed in OpenBrain) is checked first on every task.

---

### QA Agent

Reviews all outputs from the Coding Agent before they are presented to the IT Manager for approval and deployment.

| Attribute | Value |
|-----------|-------|
| Primary model | Lightweight local (Llama 3 8B or Phi-3 Mini) for structural checks; mid-range for security review |
| Tool access | Gitea (read), isolated test environment, OpenBrain read/write |
| Data scope | Internal and Public only |
| Deployment stage | Week 6 |

**QA Agent responsibilities:**
- Run the defined test suite against all Coding Agent outputs
- Check for common security vulnerabilities (injection risks, hardcoded credentials, excessive permissions)
- Validate that code meets the documentation standard
- Check that no Restricted or Confidential data is referenced in code or configuration
- Produce a structured QA report — pass/fail with specific findings — written to OpenBrain

---

### Monitoring Agent

The continuous eyes of the IT operation. Consumes monitoring inputs, triages alerts, and produces structured incident summaries.

| Attribute | Value |
|-----------|-------|
| Primary model | Lightweight local (Llama 3 8B) for triage; mid-range for complex incident analysis |
| Tool access | Log aggregation stack (read), Prometheus API (read), OpenBrain read/write, IT Manager notification |
| Data scope | Internal and Confidential monitoring data — processed locally only |
| Deployment stage | Week 7 |

---

### Security Agent

Maintains a continuous picture of the organisation's security posture. Monitors vulnerability feeds, analyses security scan outputs, reviews access control configurations, and generates remediation recommendations.

| Attribute | Value |
|-----------|-------|
| Primary model | Mid-range local (Llama 3 70B) |
| Frontier fallback | OpenRouter → Claude Sonnet for complex threat analysis (Internal data only) |
| Tool access | CVE feeds (read), security scan API (read), firewall API (read), OpenBrain read/write |
| Data scope | Internal and Confidential — all processing local |
| Deployment stage | Week 8 |

> **Important:** The Security Agent shall never autonomously apply security changes. All recommendations require IT Manager approval.

---

### Governance Agent

Supports the IT Manager in maintaining the governance framework. Monitors the AI Register, tracks policy review dates, checks compliance posture, and generates the monthly governance summary.

| Attribute | Value |
|-----------|-------|
| Primary model | Lightweight local (Phi-3 Mini) for scheduling and tracking; mid-range for report generation |
| Tool access | OpenBrain read/write (AI Register, data register, prompt library), calendar integration |
| Data scope | Internal — governance documentation is Internal classification |
| Deployment stage | Week 8 |

---

### Reporting Agent

Generates scheduled and ad-hoc reports from approved data sources.

| Attribute | Value |
|-----------|-------|
| Primary model | Lightweight local (Llama 3 8B) |
| Tool access | MariaDB (read), OpenBrain (read), approved log sources (read) |
| Data scope | Internal — all reporting data processed locally |
| Deployment stage | Week 8 |

---

## Implementation checklist

- [ ] Plan the full 7-agent architecture before deploying anything — infrastructure from day one
- [ ] Deploy Head Agent first (Week 5), with task logging to OpenBrain confirmed
- [ ] Deploy Coding Agent and QA Agent as a pair (Week 6)
- [ ] Deploy Monitoring Agent (Week 7) — connect all monitoring inputs before deploying
- [ ] Deploy Security Agent and Governance Agent (Week 8)
- [ ] Deploy Reporting Agent (Week 8) — confirm report templates before deploying
- [ ] Document all agents in the AI Register with full permission and data scope entries
- [ ] Test the local-script-first rule — verify the script library is checked before Coding Agent is invoked
- [ ] Confirm all agent outputs are logged to OpenBrain before any autonomous operation

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | Central memory layer for all agent communication |
| [`tools/security-skill-checker.md`](../tools/security-skill-checker.md) | Screen agent tools before deployment |

**Related sections:** [Section 4 — OpenBrain Memory](04-open-brain-memory.md) · [Section 7 — AI Security](07-ai-security.md) · [Section 8 — Local Infrastructure](08-local-infrastructure.md)
