# Step 4: Build

**Deploy your agents, OpenBrain, and local infrastructure.**

This is the longest step. It takes roughly 8 weeks to go from a blank server to seven agents running in supervised mode. Follow the week-by-week plan in Section 17. Do not try to compress it significantly — the supervised operation phases exist because you need time to verify behaviour before you trust it.

Your working agent from Step 0 stays in place throughout the build. This step deploys the full production local stack — dedicated server, Ollama, OpenBrain, and the 7-agent hierarchy. Once complete, you will have local infrastructure that can replace your Step 0 cloud setup for anything touching Restricted or Confidential data.

---

## What this step covers

- Deploying the hardware and OS
- Installing Ollama and local models
- Deploying OpenBrain (PostgreSQL + pgvector)
- Installing OpenClaw and deploying the Head Agent
- Deploying each specialist agent in sequence
- Building the script library and prompt library
- Connecting monitoring inputs
- Getting the first supervised autonomous tasks running

---

## The order matters

Deploy in this sequence:

1. **Hardware and OS** — Week 3
2. **OpenBrain and model routing** — Week 4
3. **Head Agent** — Week 5
4. **Coding Agent + QA Agent** — Week 6
5. **Monitoring Agent** — Week 7
6. **Security Agent + Governance Agent** — Week 8
7. **Reporting Agent** — Week 8
8. **Supervised operation** — Weeks 9–11
9. **First autonomous tasks** — Week 12+

Do not deploy agents before OpenBrain is running. All agent task logging depends on it.

---

## The data sovereignty rule during the build

Every deployment decision has a data sovereignty dimension. When you are wiring up a new agent capability, ask:
- What data will this agent access?
- What is that data's classification?
- Is the processing local or external?
- Is the local-first standard being met?

If the answers are not satisfactory, do not proceed with the deployment until they are.

---

## Supervised operation is not optional

Before any agent capability operates autonomously, it runs in supervised mode:
- IT Manager reviews all outputs before any action is taken
- Outputs are logged to OpenBrain
- A minimum of 10 consecutive supervised runs with zero failures before autonomous approval

The temptation is to skip supervised operation because the agent seems to be working. Resist this. Supervised operation is where you discover the edge cases. Edge cases discovered before autonomy are learning opportunities. Discovered after autonomy, they are incidents.

---

## Runbooks before autonomy

Every agent task that will eventually run autonomously requires a runbook documenting the manual procedure for performing that task without the agent. Write the runbook before you deploy, not after.

The question to answer in each runbook: "If the agent goes down at 3pm on a Thursday, what do we do?"

---

## Blueprint sections for this step

| Section | What it covers |
|---------|---------------|
| [`blueprint/03-ai-agent-architecture.md`](../blueprint/03-ai-agent-architecture.md) | The 7-agent hierarchy and communication protocol |
| [`blueprint/04-open-brain-memory.md`](../blueprint/04-open-brain-memory.md) | OpenBrain installation, schema, MCP tools |
| [`blueprint/05-document-ingestion.md`](../blueprint/05-document-ingestion.md) | Document ingestion pipeline |
| [`blueprint/06-system-prompt-management.md`](../blueprint/06-system-prompt-management.md) | Prompt structure, token limits, housekeeping |
| [`blueprint/07-ai-security.md`](../blueprint/07-ai-security.md) | Security controls — apply during build |
| [`blueprint/08-local-infrastructure.md`](../blueprint/08-local-infrastructure.md) | Hardware, OS, network, physical security |
| [`blueprint/11-backup-disaster-recovery.md`](../blueprint/11-backup-disaster-recovery.md) | Backup configuration for the agent stack |
| [`blueprint/12-prompt-library.md`](../blueprint/12-prompt-library.md) | Building the prompt library as you deploy |
| [`blueprint/17-30-60-90-day-plan.md`](../blueprint/17-30-60-90-day-plan.md) | Week-by-week plan with definitions of done |

---

## Tools for this step

| Tool | Use |
|------|-----|
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | Setting up session context for agent sessions |
| [`tools/prompt-injection-defence.md`](../tools/prompt-injection-defence.md) | Configure for all document ingestion paths |
| [`tools/security-skill-checker.md`](../tools/security-skill-checker.md) | Screen all skills and tools before deployment |
| [`tools/estate-discovery.md`](../tools/estate-discovery.md) | Map system integrations as you build |

---

## Done when

- [ ] Dedicated agent server deployed, hardened, on its own VLAN
- [ ] Ollama running — three model tiers available locally
- [ ] OpenBrain running — all SQL tables populated, MCP responding
- [ ] All 7 agents deployed and logging to OpenBrain
- [ ] Script library seeded with existing automation scripts
- [ ] Prompt library contains minimum 15 entries, all owned and reviewed
- [ ] Monitoring inputs connected from all major sources
- [ ] Minimum 5 tasks in supervised operation
- [ ] Runbooks written for all supervised tasks
- [ ] All agents documented in the AI Register

**→ Previous step: [Step 3 — Skill Up](03-skill-up.md)** | **Next step: [Step 5 — Feedback Loop](05-feedback-loop.md)**
