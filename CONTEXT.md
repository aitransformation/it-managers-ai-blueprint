# CONTEXT.md — Open Brain Context Anchor

This file defines what an AI agent should retrieve from Open Brain (PostgreSQL) at the start of a session to maintain operational continuity across conversations.

---

## Purpose

An AI agent without context is starting from scratch every time. Open Brain holds the organisation's estate profile, active tasks, governance state, and recent decisions. Retrieving the right context at session start means the agent can pick up where work left off rather than asking the IT Manager to re-explain the environment.

---

## What to query at session start

Run these queries in sequence. If Open Brain is unavailable, skip to the fallback section.

### 1. Estate profile
```sql
SELECT content, source, tags, created_at
FROM memories
WHERE tags @> ARRAY['estate-profile']
ORDER BY created_at DESC
LIMIT 1;
```
This gives the current snapshot of the IT estate: systems, infrastructure, data classification status, agent deployment stage. If it returns nothing, the estate has not yet been profiled — prompt the IT Manager to run the audit step.

### 2. Active tasks
```sql
SELECT agent_role, task_type, status, input_summary, started_at
FROM agent_tasks
WHERE status IN ('pending', 'running', 'escalated')
ORDER BY started_at ASC;
```
Returns all in-progress work. If there are escalated tasks, flag them immediately. If there are running tasks from a previous session, ask the IT Manager whether to resume or review.

### 3. Last review date
```sql
SELECT last_reviewed, next_review, name, notes
FROM governance_register
WHERE register_type = 'blueprint-review'
ORDER BY last_reviewed DESC
LIMIT 1;
```
If no review record exists, the monthly review has not yet been set up. Recommend Step 5 of the journey.

### 4. Data register summary
```sql
SELECT classification, COUNT(*) as count
FROM governance_register
WHERE register_type = 'data_asset'
GROUP BY classification;
```
Gives a quick read of how many assets exist at each classification tier. If the count is zero or very low, the data register is incomplete — this is a gap.

### 5. AI register summary
```sql
SELECT name, status, next_review
FROM governance_register
WHERE register_type = 'ai_deployment'
ORDER BY next_review ASC;
```
Lists all deployed AI capabilities and their next review dates. Flag any that are overdue.

### 6. Journey step (semantic search)
```sql
SELECT content, tags, created_at
FROM memories
WHERE tags @> ARRAY['journey-step']
ORDER BY created_at DESC
LIMIT 1;
```
Records which step of the 5-step journey the organisation is currently on. If absent, assume Step 1.

### 7. Recent decisions
```sql
SELECT content, source, created_at
FROM memories
WHERE tags @> ARRAY['decision']
ORDER BY created_at DESC
LIMIT 5;
```
Retrieves the last five recorded decisions. Use this to avoid re-litigating resolved questions.

---

## Graceful handling when context is missing

If Open Brain is unavailable or returns no results:

1. Do not invent context. State that you have no stored context for this estate.
2. Ask the IT Manager for the minimum needed: what step are they on, what's the immediate task.
3. Offer to write an estate profile to Open Brain once the session produces enough information to do so.
4. All outputs during a no-context session are advisory only. Flag this explicitly.

If partial context exists (some queries return results, others don't):

- Work with what's there.
- Note explicitly which context is absent.
- Recommend filling the gap as part of the session.

---

## Writing context back

After every meaningful session, write updated context to Open Brain so the next session has continuity.

### Update estate profile
```sql
INSERT INTO memories (content, source, tags, embedding)
VALUES (
  '<updated estate description>',
  'it_manager',
  ARRAY['estate-profile'],
  <embedding from local model>
);
```

### Record a decision
```sql
INSERT INTO memories (content, source, tags, embedding)
VALUES (
  '<description of what was decided and why>',
  'it_manager',
  ARRAY['decision', '<relevant-topic>'],
  <embedding from local model>
);
```

### Update journey step
```sql
INSERT INTO memories (content, source, tags, embedding)
VALUES (
  'Current journey step: <step number and name>. Status: <brief note>.',
  'it_manager',
  ARRAY['journey-step'],
  <embedding from local model>
);
```

---

## System prompt template — context anchor

Use this structure at the start of every agent system prompt to anchor session context:

```
[CONTEXT ANCHOR]
Organisation: <name>
Current journey step: <step 1–5>
Estate profile: <one-paragraph summary from memories table>
Active tasks: <list from agent_tasks>
Last governance review: <date>
Data assets classified: <count by tier>
Active AI deployments: <list from ai_deployment register>
Recent decisions: <last 3 from memories>
[END CONTEXT ANCHOR]
```

If any field is unavailable, replace with: `[not yet established]` — do not omit the field.

---

## Context review cadence

The context anchor should be refreshed:
- At the start of every session (pulled from Open Brain)
- After every monthly review (full refresh)
- Whenever the estate profile changes materially (new system, new agent, change of journey step)
- After a DR event (context may have been lost; verify and restore)

---

*This file is part of the IT Manager's AI Blueprint. See `AGENT.md` for the full session initialisation sequence.*
