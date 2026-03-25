# Section 6: System Prompt Management and Anti-Bloat Housekeeping

> **Journey Step:** Step 4 — Build / Step 5 — Feedback Loop

---

## The problem of prompt bloat

Agent system prompts accumulate instructions over time. When a new edge case is encountered, a line is added. When a capability is expanded, the system prompt grows to accommodate it. When a bug is fixed by adding a corrective instruction rather than addressing the root cause, the prompt carries that correction indefinitely.

Over weeks and months, a system prompt that started as 200 words becomes 2,000 words, much of which is contradictory, redundant, or no longer relevant. This is prompt bloat, and it degrades agent performance.

Bloat is not only a system prompt problem. OpenBrain accumulates memories that are no longer accurate. The vector store fills with embeddings for documents that have been superseded. Task logs grow without archival. Each of these represents noise that the agent must work around when retrieving context.

The solution is a defined housekeeping cycle, executed by the agents themselves on a scheduled basis, governed by the Governance Agent.

---

## The system prompt structure

Each agent has a system prompt with three parts:

```
[Central shared context]              ← Same across all agents
- Organisation identity
- Four core drivers
- Data sovereignty rules
- Local-script-first rule
- Escalation principles

[Agent-specific role definition]      ← Unique per agent
- Role name and purpose
- Tool access scope
- Data classification limits
- Success criteria for this role

[Current operational context]         ← Updated by housekeeping
- Active tasks and their status
- Recent decisions and outcomes
- Known issues in the environment
```

The system prompt for each agent is stored as a versioned file in Gitea. Any change to a system prompt is a change management event: it requires a reason, is tested against the acceptance criteria in the prompt library, and is committed with a descriptive message.

---

## Prompt token limits

| Agent | Maximum tokens | Review trigger |
|-------|---------------|----------------|
| Head Agent | 4,000 | Alert at 3,200 |
| Coding Agent | 3,000 | Alert at 2,400 |
| QA Agent | 2,000 | Alert at 1,600 |
| Monitoring Agent | 2,500 | Alert at 2,000 |
| Security Agent | 3,000 | Alert at 2,400 |
| Governance Agent | 2,000 | Alert at 1,600 |
| Reporting Agent | 1,500 | Alert at 1,200 |
| Ingestion Agent | 1,500 | Alert at 1,200 |

When a prompt exceeds its review trigger threshold, the Governance Agent alerts the IT Manager and initiates a prompt review.

---

## Scheduled housekeeping tasks

All housekeeping tasks are logged to the `agent_tasks` table in OpenBrain. All run during off-peak hours (default: 02:00 local time).

| Task | Agent | Schedule | Description |
|------|-------|----------|-------------|
| Prompt size audit | Governance Agent | Weekly (Monday) | Checks all system prompt token counts against limits. Flags any over threshold. |
| Memory staleness review | Governance Agent | Monthly | Identifies memories in OpenBrain not accessed in 90+ days. Flags for IT Manager review. |
| Memory deduplication | Governance Agent | Monthly | Finds near-duplicate memories (cosine similarity > 0.97). Presents candidates for merge or deletion. |
| Task log archival | Reporting Agent | Monthly | Archives `agent_tasks` records older than 90 days. Maintains rolling 90-day active window. |
| Monitoring event archival | Monitoring Agent | Monthly | Archives resolved `monitoring_events` older than 60 days. |
| Script library validation | QA Agent | Weekly (Sunday) | Runs all scripts marked `test_status = 'passing'` against a test environment. Updates status if tests fail. |
| Document freshness check | Ingestion Agent | Weekly | Identifies documents in OpenBrain not re-ingested in 30+ days. Checks source for updates. |
| Prompt library review reminder | Governance Agent | Per review dates | Sends reminders 7 days before prompt review due dates. |
| Governance register sweep | Governance Agent | Weekly | Checks all governance register entries for upcoming review dates within 14 days. Alerts IT Manager. |
| OpenBrain index optimisation | Head Agent | Monthly | Runs `VACUUM ANALYZE` on the PostgreSQL database. Rebuilds vector indexes where fragmentation is detected. |

---

## Anti-bloat review process

When the Governance Agent flags a prompt for size review, the IT Manager follows this process:

1. Read the current prompt in full
2. For every instruction, ask: is this still necessary? Is it covered elsewhere? Is it addressing a root cause or papering over a bug?
3. Remove every redundant, contradictory, or obsolete instruction
4. Verify the reduced prompt against the acceptance criteria in the prompt library
5. Commit the revised prompt to Gitea with a message describing what was removed and why
6. Update the token count in the prompt library entry
7. Monitor agent performance for 48 hours after the change

The Coding Agent may assist with the review — given the current prompt and the acceptance criteria, it can identify candidate instructions for removal. The IT Manager makes all final decisions. A reduced prompt that passes its acceptance criteria is always preferred over a longer one.

---

## Writing prompts that stay clean

The most effective way to avoid bloat is to write prompts that address root causes rather than edge cases.

When you find yourself adding a new instruction to fix an unexpected output, ask first:
- Is the model fundamentally misunderstanding its role? Fix the role definition.
- Is this caused by an edge case in the data? Fix the data, not the prompt.
- Is this caused by a missing tool or capability? Build the tool, not a workaround in the prompt.

Only add instructions to the system prompt when the underlying issue genuinely cannot be resolved elsewhere.

> **Anti-AI writing:** When writing or reviewing system prompts, avoid the AI-sounding patterns that prompts themselves often exhibit — over-structured lists, vague instructions, and instructions that don't actually constrain anything. A well-written prompt reads like clear professional instructions, not a ChatGPT output. Use the [`tools/anti-ai-writing.md`](../tools/anti-ai-writing.md) tool to check prompt drafts for weak patterns before deploying them.

---

## Implementation checklist

- [ ] Create the Gitea repository for system prompts and agent configuration
- [ ] Write the initial system prompt for each agent following the three-part structure
- [ ] Set token limits in the Governance Agent configuration
- [ ] Configure the housekeeping schedule — all tasks set to run at 02:00
- [ ] Test: Governance Agent correctly identifies a prompt over its trigger threshold
- [ ] Test: Memory deduplication identifies near-duplicate entries correctly
- [ ] Document the anti-bloat review process as an SOP in the prompt library
- [ ] Include prompt size review in the monthly governance review agenda

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/anti-ai-writing.md`](../tools/anti-ai-writing.md) | Detect and remove weak, vague, or AI-sounding patterns in system prompts |
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | Store and retrieve system prompt versions |

**Related sections:** [Section 12 — Prompt Library](12-prompt-library.md) · [Section 18 — Monthly Review](18-monthly-review.md)
