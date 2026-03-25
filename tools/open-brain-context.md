# Tool: Open Brain Context

## What it does

Manages the session context layer for AI agent sessions. At session start, retrieves the current estate profile, active tasks, governance state, and recent decisions from OpenBrain (PostgreSQL + pgvector). After meaningful work, writes updated context back so the next session picks up where this one left off.

This is what prevents an AI agent from starting from scratch every session.

---

## When to use it in the journey

| Journey Step | Use case |
|-------------|----------|
| Step 4 — Build | Set up OpenBrain and the session context pattern when deploying the Head Agent |
| Step 4 — Build | Verify that all agents are correctly writing task results to OpenBrain |
| Step 5 — Feedback Loop | At the start of every monthly review session |
| Any step | At the start of any session where an AI agent is helping you apply the blueprint |

---

## Workspace reference

The full query pattern is defined in [`CONTEXT.md`](../CONTEXT.md) at the repository root. Read that file for the complete SQL queries and the graceful fallback procedure when Open Brain is unavailable.

OpenBrain installation and schema are defined in [`blueprint/04-open-brain-memory.md`](../blueprint/04-open-brain-memory.md).

---

## Session start queries

Run these at the start of every agent session (abbreviated — see `CONTEXT.md` for full SQL):

| Query | What it retrieves |
|-------|-------------------|
| Estate profile | Current snapshot of IT estate |
| Active tasks | All in-progress work from agent_tasks |
| Last review date | Last governance review from governance_register |
| Data register summary | Count of assets by classification tier |
| AI register summary | All deployed AI capabilities and next review dates |
| Journey step | Current position in the 5-step journey |
| Recent decisions | Last 5 recorded decisions |

---

## Writing context back

After every meaningful session, write to OpenBrain:

```sql
-- Update estate profile
INSERT INTO memories (content, source, tags, embedding)
VALUES ('<updated estate description>', 'it_manager', ARRAY['estate-profile'], <embedding>);

-- Record a decision
INSERT INTO memories (content, source, tags, embedding)
VALUES ('<decision and rationale>', 'it_manager', ARRAY['decision', '<topic>'], <embedding>);

-- Update journey step
INSERT INTO memories (content, source, tags, embedding)
VALUES ('Current journey step: <N — name>. Status: <note>.', 'it_manager', ARRAY['journey-step'], <embedding>);
```

All embeddings are generated locally via `nomic-embed-text` through Ollama.

---

## When Open Brain is unavailable

Do not invent context. State clearly that no stored context is available. Ask for the minimum needed to complete the current task. Offer to write an estate profile once the session produces enough information.

All outputs during a no-context session are advisory only. Flag this explicitly in any outputs produced.

---

## Example use case

**Scenario:** The IT Manager starts a session to plan the deployment of the Security Agent (Week 8 in the 13-week plan). The agent queries OpenBrain at session start. It retrieves: the estate profile (describing the current server setup), active tasks (one in-progress monitoring configuration), the current journey step (Step 4, Build — Week 7 complete), and the three most recent decisions (including the model tier chosen for the Security Agent).

The agent has enough context to immediately pick up where Week 7 left off, without the IT Manager needing to re-explain the environment.

---

## Blueprint reference

[Section 4 — OpenBrain Memory](../blueprint/04-open-brain-memory.md) covers the full architecture, schema, and installation. [`CONTEXT.md`](../CONTEXT.md) defines the complete session context pattern.
