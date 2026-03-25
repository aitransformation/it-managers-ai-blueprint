# Tools

These are the operational tools that make the blueprint work in practice. Each tool has a corresponding skill in the workspace that an AI agent can use directly.

---

## Available tools

| Tool | What it does |
|------|-------------|
| [`prompt-injection-defence.md`](prompt-injection-defence.md) | Screen inbound content for injection attempts before it reaches an agent |
| [`security-skill-checker.md`](security-skill-checker.md) | Security screening for agent skills and tools before installation or use |
| [`anti-ai-writing.md`](anti-ai-writing.md) | Detect and rewrite AI-sounding patterns in prompts and content |
| [`open-brain-context.md`](open-brain-context.md) | Query and write to the agent memory store (OpenBrain) |
| [`estate-discovery.md`](estate-discovery.md) | Map the current IT estate — systems, data, ownership, gaps |

---

## How tools relate to the journey

| Journey Step | Tools most relevant |
|-------------|---------------------|
| Step 1 — Audit | Estate Discovery |
| Step 2 — Foundations | Open Brain Context, Estate Discovery |
| Step 3 — Skill Up | Anti-AI Writing, Prompt Injection Defence |
| Step 4 — Build | All tools |
| Step 5 — Feedback Loop | Open Brain Context, Security Skill Checker |

---

## Using tools with an AI agent

Each tool file includes the workspace skill path. When you ask an AI agent to use a tool, it can load the skill and apply it. See [`AGENT.md`](../AGENT.md) for the full session initialisation sequence.
