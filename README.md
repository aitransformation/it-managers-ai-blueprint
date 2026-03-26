# IT Manager's AI Blueprint

You've been asked to do something with AI.

Maybe the founder saw a demo. Maybe a competitor is already using it. Maybe a board member forwarded an article with "thoughts?" in the subject line. Whatever triggered it, the expectation has landed on your desk: get this working, do it safely, and don't break anything.

The gap between that expectation and knowing how to actually deliver is real. How do you deploy AI when you don't have a dedicated data science team? How do you keep sensitive data in-house? How do you explain the governance to leadership when leadership barely knows what an LLM is? How do you stop your team from pasting customer records into ChatGPT?

This blueprint is the practical path through that gap.

It's a working standard for IT Managers in SMEs — not a vision document, not a vendor pitch, not an academic framework. A concrete, ordered guide to what you do, when you do it, and how you do it safely. Built from real deployments in live SME environments. Updated monthly.

---

## Who it's for

You're an IT Manager, head of IT, or technology lead in a small or medium-sized business. You probably run a small team or work solo. You have real systems to keep running, real users to support, limited time, and no appetite for unnecessary risk.

You want to use AI in a way you can defend to your leadership, your board, and yourself.

---

## The journey

This blueprint is structured as a six-step journey. Follow it in order.

| Step | File | What you're doing |
|------|------|-------------------|
| 0 | [Setup](journey/00-setup.md) | Stand up your agent safely before anything else |
| 1 | [Audit](journey/01-audit.md) | Map your estate, define outcomes, classify your data |
| 2 | [Foundations](journey/02-foundations.md) | Policies, data hygiene, and governance — before automation |
| 3 | [Skill Up](journey/03-skill-up.md) | Understand what you're deploying and teach it to your team |
| 4 | [Build](journey/04-build.md) | Deploy agents, memory, and local infrastructure |
| 5 | [Feedback Loop](journey/05-feedback-loop.md) | Monthly review and continuous improvement |

**Start here: [Step 0 — Setup](journey/00-setup.md)**

---

## Why Setup comes first

Standing up a governed AI agent at the start of the journey means you have a practical assistant for the rest of it. Your agent helps with the audit, with drafting policies, with research summaries, with implementation checklists — from the very first step. But it only helps safely if you set the boundaries before you use it.

That's what Step 0 does.

---

## What's in the repo

**`journey/`** — The six-step path. This is the primary reading experience. Start here and follow the steps in order.

**`blueprint/`** — The reference standard. Detailed guidance on every topic: data sovereignty, agent architecture, security, governance, infrastructure, skills, change management, and more. The journey steps link to the right sections as you go.

**`tools/`** — Operational tools: prompt injection defence, security skill checker, anti-AI writing detection, estate discovery.

**`AGENT.md`** — Read this if you're using an AI agent to apply the blueprint. It defines how the agent should behave, what data rules apply, and which sections to read for each step.

---

## The founding principle

**AI amplifies people. It does not replace them.**

Every recommendation in this blueprint builds on this. Agents, local models, and automated workflows exist to multiply what you can do — not to remove people from the equation. The question is never "what can AI replace?" It is always "what can this person now achieve that was previously impossible or impractical?"

---

## Update cadence

This blueprint updates monthly. The AI landscape moves fast. Each edition reflects verified, deployable practice at the time of publication. Check [CHANGELOG.md](CHANGELOG.md) for the release history. Editions older than three months should be reviewed against the current version before you act on them.

---

## Community

- **The Forge** — community for IT Managers applying this blueprint: [link coming]
- **The Furnace** — 1:1 coaching and support: [link coming]

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The bar is high: everything must be verified and deployable, not theoretical.

---

*Published monthly. Built for SME IT Managers. Grounded in real deployments.*
