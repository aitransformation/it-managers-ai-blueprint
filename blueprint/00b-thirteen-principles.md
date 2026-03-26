# The 13 Principles

> **Journey Step:** Applies to every step. Read this alongside [Principles](00-principles.md) before you start.

These 13 principles define the operating stance behind the blueprint. They are the practical rules that shape how the agent stack is designed, how data is handled, and how the IT Manager stays in control.

They are not marketing lines. They are the guardrails.

---

## 1. AI agents run locally, on their own hardware

The default operating model is local. Agents should run on hardware under the organisation's control, not as a black box in somebody else's environment.

This gives the IT Manager control over performance, data handling, logging, update timing, and failure recovery. It also means the organisation is not one vendor decision away from losing a critical capability.

Cloud can be used where needed, but local is the baseline, not the aspiration.

---

## 2. Agents sit on their own VLAN and are firewalled from the rest of the network

Agents are not just another application. They are active systems that can read, write, process, and in some cases take action. They need to be treated as a distinct security zone.

Placing them on their own VLAN with explicit firewall rules limits blast radius, reduces lateral movement risk, and makes traffic easier to reason about and monitor.

---

## 3. Data is stored locally

If the organisation is serious about sovereignty, the data store cannot live somewhere else by default.

Operational data, memory, embeddings, documents, logs, and outputs should be stored locally wherever practical. If something leaves the environment, there should be a clear reason, a clear record, and a clear approval basis.

---

## 4. All skills and tools are built from scratch by the agent. Nothing is imported blindly

Imported tools and copied skills create supply-chain risk, hidden assumptions, and prompt-injection exposure.

The default position is to build what is needed locally, for the task at hand, under the organisation's own rules. If something external is evaluated, it is screened first and treated as untrusted until proven otherwise.

This principle is about control, not ego.

---

## 5. Memory and context are stored in a database served by vector search

An agent without memory starts from scratch every time. That means repeated work, lost decisions, weak continuity, and shallow outputs.

Context should live in a proper database-backed memory layer, with retrieval designed to bring back relevant information when needed. In this blueprint, that means Open Brain and vector-backed retrieval rather than hoping a chat window remembers enough.

---

## 6. Agents must have a self-reflection and improvement mechanism

An agent stack that never reviews itself will drift, repeat mistakes, and quietly get worse.

There must be a deliberate mechanism for reflection, review, and improvement. That can include error review, output checks, prompt tuning, workflow adjustment, and periodic redesign of weak skills or bad habits.

Improvement is part of the system, not an optional extra.

---

## 7. Agents do not have admin access to firewall or switch configurations

This is a hard boundary.

Agents may assist with documentation, analysis, and recommendation, but they do not get admin-level control over core network infrastructure. Firewall and switch configuration remains under direct human control.

That line exists because the downside of getting it wrong is too high.

---

## 8. No user content is served from the AI servers

AI infrastructure is not a content hosting platform.

User-facing content, customer assets, files, or application payloads should not be served from the same systems running models, memory, or agent workflows. Keep those concerns separate. It reduces risk and keeps the AI environment easier to harden and reason about.

---

## 9. All ingest data is first passed through a prompt injection detection tool

Anything coming in from outside the trusted environment is treated as hostile until screened.

That includes PDFs, copied text, websites, emails, HTML, imported repositories, and vendor documentation. Prompt injection is not an edge case. It is part of the normal threat model.

The screen happens before the agent sees the content, not afterwards.

---

## 10. Chat interfaces must be secure and have MFA as a minimum

If people can access an agent through chat, that interface becomes a security boundary.

It must be authenticated, protected, and governed. MFA is the minimum acceptable control. Session security, access control, and auditability matter just as much as model quality.

A clever agent behind a weak chat interface is still a weak system.

---

## 11. AI must provide the truth in all communications

AI should not flatter, bluff, smooth over uncertainty, or pretend to know more than it does.

If something is unknown, it should say so. If an answer is inferred, that should be clear. If confidence is low, that should be stated plainly. The standard here is honesty, not polish.

Truthfulness matters because once the AI becomes comfortable sounding right without being right, trust starts to rot.

---

## 12. AI does not replace humans. It provides leverage for them to work better

This is the core operating belief behind the whole blueprint.

The purpose of the agent is to reduce drag, return time, improve quality, and increase the range of what a person can get done. It is there to make the IT Manager and the wider team more capable, not less necessary.

The human remains accountable. The agent increases their reach.

---

## 13. AI responses should be derived from data, not assumed

The best AI output comes from good context, good retrieval, and good source material.

Where the answer should come from actual business data, actual documents, actual configurations, or actual records, the agent should retrieve and work from that. It should not guess because it can form a plausible sentence.

That means better memory, better retrieval, and better habits around evidence.

---

## How to use these principles

Use these principles in three ways:

1. **As a design test** — does a proposed tool, workflow, or architecture fit these rules?
2. **As a review test** — if something feels off, which principle is being broken?
3. **As a teaching tool** — these principles explain the operating model to leadership, technical teams, and contributors.

If a decision conflicts with these principles, stop and review it before moving forward.
