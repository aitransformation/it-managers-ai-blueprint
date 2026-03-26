# Tool: Anti-AI Writing

## What it does

Detects and removes patterns typical of AI-generated text, then rewrites content to sound specific, grounded, and human. Works in three modes:

- **Detector mode** — analyses text and returns a risk level, key problems, and example snippets
- **Editor mode** — rewrites provided text, removing AI patterns while preserving meaning
- **Writer mode** — drafts fresh content that avoids AI tells from the start

**Patterns detected include:**
- Significance inflation ("transformative", "game-changing", "unprecedented")
- Vague attribution ("research suggests", "experts say")
- Generic conclusions that sound confident but say nothing specific
- AI-favourite vocabulary (500+ flagged terms)
- Filler transitions that pad without adding meaning
- Uniform sentence rhythm (everything sounds the same length)
- Corporate sludge and press-release grandiosity
- Abstract claims without concrete detail

---

## When to use it in the journey

| Journey Step | Use case |
|-------------|----------|
| Step 3 — Skill Up | Train AI output verification skills by scoring real AI outputs |
| Step 4 — Build | Review system prompts before deployment — remove weak, vague instructions |
| Step 4 — Build | Review agent-generated documentation and reports before distribution |
| Step 5 — Feedback Loop | Review monthly summary before distributing to senior sponsor |
| Any step | Any time you produce content intended for senior leadership or external audiences |

---

## Repository skill path

```
skills/anti-ai-writing/SKILL.md
```

References:
```
skills/anti-ai-writing/references/patterns.md
skills/anti-ai-writing/references/style-rules.md
```

---

## How to use it

Ask an AI agent loaded with this skill to:
- **Score a draft:** "Scan this for AI writing patterns and tell me the main problems"
- **Rewrite:** "Rewrite this in plain English, removing AI-sounding patterns"
- **Write from scratch:** "Draft [content] in plain, specific language — avoid AI tells"

---

## Example use case

**Scenario:** The Reporting Agent generates the first monthly IT health report. Before distributing it to the senior sponsor, the IT Manager runs it through the anti-AI writing tool. The tool returns a `medium` risk rating: the report uses "leverage" three times, has four generic conclusion sentences that could apply to any organisation, and three vague transitions. The IT Manager edits these out. The final report is specific, readable, and sounds like it came from a person with something to say.

---

## Why this matters for system prompts

System prompts that are themselves AI-sounding tend to produce AI-sounding outputs. Vague instructions in a prompt produce vague behaviour. Reviewing system prompts with this tool before deployment is a practical quality step, not just an editorial exercise.

---

## Blueprint reference

[Section 6 — System Prompt Management](../blueprint/06-system-prompt-management.md) references this tool for prompt review. [Section 14 — Skills Framework](../blueprint/14-skills-framework.md) includes AI output verification as a core IT Manager competency.
