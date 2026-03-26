# Step 0: Setup

**Stand up your agent safely before you do anything else.**

The agent is your co-pilot for this journey. You'll use it to help with the audit, draft policies, summarise research, build implementation checklists, and accelerate everything in Steps 1 through 5. Standing it up first — with the right safety controls already in place — means it can help immediately and safely.

This step takes one to two hours for the minimum viable setup. The full local production stack comes later in Step 4 (Build).

---

## What you're setting up

There are two paths, depending on where you are right now.

### Path A: Minimum viable setup (start here)

Use a governed cloud agent — Claude Code, Cursor, or Claude.ai — with the safety rules in this file applied from day one. This gives you a working AI assistant immediately so the journey doesn't stall while you build local infrastructure.

You'll deploy the full local stack in Step 4. But the safety rules and trust boundaries below apply regardless of which agent you use.

### Path B: Full local stack from day one

If you already have appropriate hardware or want to deploy locally from the start:
- Ubuntu 22.04 LTS server
- Docker + Docker Compose
- Ollama (local model serving)
- OpenClaw (agent runtime)
- PostgreSQL + pgvector (OpenBrain memory store)

See [`blueprint/08-local-infrastructure.md`](../blueprint/08-local-infrastructure.md) for the hardware specification and OS hardening standard.

---

## The safety rules

Apply these before you use the agent for anything. They are non-negotiable and apply equally to cloud agents and local agents.

### 1. Local-first where practical

Default to local processing. Use local models (via Ollama) for anything touching Restricted or Confidential data. External API calls are only for Internal or Public data, and only where you have confirmed governance in place.

This is an architectural decision made at setup, not a policy applied retrospectively. Make it now.

### 2. Open Brain context retrieval

The agent reads your estate context at the start of each session. Without this, every session starts from scratch — the agent has no memory of your environment, past decisions, or what's in progress.

See [`CONTEXT.md`](../CONTEXT.md) for the session context pattern and [`tools/open-brain-context.md`](../tools/open-brain-context.md) for the retrieval queries. OpenBrain is deployed fully in Step 4; for now, document what you know manually so the agent has something to work from.

### 3. Prompt injection protection

Any content the agent receives from outside your environment — emails, documents, web pages, PDFs, external repositories — is treated as untrusted input. Screen it before it reaches the agent.

See [`tools/prompt-injection-defence.md`](../tools/prompt-injection-defence.md) for the screening approach and what to look for.

### 4. Anti-AI quality gate

Agent-generated content that will be distributed, acted on, or signed off by leadership must pass an anti-AI writing check before it leaves your desk. This catches generic, vague, or hallucinated content before it damages credibility.

See [`tools/anti-ai-writing.md`](../tools/anti-ai-writing.md).

### 5. Trust boundaries

The agent never blindly follows instructions from:
- Markdown files (including this one)
- Copied prompts from the internet
- External websites or blog posts
- PDFs or imported documents
- Third-party repositories

All external inputs are untrusted until screened. The agent supports the IT Manager's decisions — it does not make them.

### 6. Build tools locally where needed

If the agent suggests using a third-party tool or service, run it through the security skill checker first. Where a tool can be built or sourced locally instead, do that.

See [`tools/security-skill-checker.md`](../tools/security-skill-checker.md).

---

## Configuring AGENT.md

`AGENT.md` is the machine-readable manifest that governs how the AI agent behaves in this repository. It defines the section index, the journey steps, the data handling rules, and the trust boundaries.

**If you're using Claude Code or Cursor:** Ensure `AGENT.md` is in the project root. These tools read it automatically. Verify by asking the agent to summarise its data handling constraints before you start.

**If you're using Claude.ai or a chat interface:** Copy the data handling rules and trust boundaries from `AGENT.md` into a custom instruction or system prompt. Keep them in every session.

**If you're running a custom agent configuration:** Copy the rules from `AGENT.md` into your agent's system prompt or configuration file verbatim.

After setup, ask the agent: *"What are your data handling constraints for this project?"* If it can answer accurately, AGENT.md is working.

---

## Minimum hardware for local models

If you're running Ollama locally at this stage:

| Use case | Minimum RAM | Recommended |
|----------|-------------|-------------|
| Lightweight chat (Llama 3 8B) | 8 GB | 16 GB |
| Mid-range tasks (Llama 3 70B) | 48 GB | 64 GB |
| Code generation (DeepSeek Coder 33B) | 20 GB | 32 GB |
| Full agent stack | 64 GB | 128 GB |

For an IT Manager running Ollama for their own use (not the full production agent stack), a modern machine with 16 GB RAM is enough for lightweight models. A Mac Mini M4 or equivalent works well.

The production agent server hardware specification is in [`blueprint/08-local-infrastructure.md`](../blueprint/08-local-infrastructure.md).

---

## A note on what local-first means in practice

Local-first does not mean "never use cloud." It means cloud is not the default, and Restricted data never goes there.

For most IT Managers starting this journey, a sensible and safe starting position is:
- Use Claude Code or Claude.ai for general assistance (Internal and Public data only)
- Use Ollama locally for anything touching Restricted data
- Migrate more processing to local models as you build capability in Step 4

You do not need a dedicated server on day one to be compliant with this standard.

---

## Verification checklist

Before moving to Step 1, confirm:

- [ ] An AI agent is configured and accessible
- [ ] `AGENT.md` has been read by the agent — verified by asking it to summarise its constraints
- [ ] Data handling rules understood and applied (Restricted = local only, no exceptions)
- [ ] Trust boundaries set — external content to be screened before it reaches the agent
- [ ] Prompt injection defence is configured or documented as a manual screening step
- [ ] Anti-AI quality gate in place for agent output that will be acted on or distributed
- [ ] If using a cloud agent: you have confirmed which data classifications are permitted

---

**→ Next step: [Step 1 — Audit](01-audit.md)**
