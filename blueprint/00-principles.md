# Principles

> **Journey Step:** Applies to all steps. Read before starting anything else.

---

## The founding principle

**AI amplifies people. It does not replace them.**

This is not a disclaimer or a reassurance added to settle anxious staff. It is a design decision that shapes every recommendation in this blueprint.

AI agents, local models, and automated workflows exist here to multiply the output of every person in the IT function and across the business. The IT Manager who deploys a monitoring agent gives an engineer back the hours previously consumed by manual log review, and redirects those hours toward work that requires human judgment, creativity, and accountability.

The question is never: *what can AI replace?*  
The question is always: *what can this person now achieve that was previously impossible or impractical?*

The skills this blueprint develops — outcome mapping, agent governance, prompt engineering, data sovereignty — are not going to be automated away. They become more valuable as AI capability increases, because they are the skills required to direct and govern that capability responsibly.

---

## The data principle

**Local-first. Always.**

All AI agents, language models, data stores, and processing pipelines shall, wherever operationally possible, be deployed on local infrastructure under the direct control of the organisation.

Cloud-based AI services shall be used only where a local equivalent is not operationally viable, and only for data classified as Internal or Public.

**Restricted and Confidential data shall never be processed by external AI services or transmitted to third-party model providers.**

The default answer to "where shall this data be processed?" is always: locally. The burden of proof is on moving processing off local infrastructure, not on keeping it there.

---

## The four core business drivers

Every business outcome maps to one or more of four universal operational drivers. These are not IT categories. They are business categories, and they are the lens through which the IT Manager evaluates every system, process, and data flow.

| Driver | What it means | Examples |
|--------|--------------|---------|
| **Make** | Create something new — a product, service, report, or piece of intellectual property | Manufacturing, software development, report production, design work, content creation |
| **Change** | Transform something from one state to a more valuable state | Accountants turning raw numbers into financial insight; repair companies turning broken things into working ones; analysts turning data into decisions |
| **Communicate** | Move information between people, teams, or systems | Sales, marketing, customer support, internal coordination, reporting, notifications, knowledge sharing |
| **Deliver** | Move value to the customer or end recipient | Shipping goods, completing work, handing over services, fulfilling orders, deploying software |

When the IT Manager can map every system to one of these four verbs, they can justify every system they run and challenge every system that fails to map.

---

## The three non-negotiable standards

### 1. Business outcomes drive everything
IT systems exist to serve outcomes. They are evaluated from that starting point. Begin with a clear statement of what the business must achieve. Map it to the four core drivers. Only then assess whether the current systems are fit to serve it.

### 2. Governance precedes automation
Every capability requires verified outputs, documented rollback procedures, and human accountability before it operates autonomously. The answer to "can we make this autonomous?" is always "only after it has passed supervised operation."

### 3. AI output is draft material
It shall be verified, not trusted. The IT Manager's professional judgment remains the authoritative layer above every AI system in the environment. AI produces a candidate answer. The IT Manager confirms it.

---

## How this document is structured

This blueprint has 19 sections. Every section references the step of the 5-step journey it belongs to. If you're looking for the practical path through the blueprint, start at [`journey/README.md`](../journey/README.md).

Every section also lists relevant tools and skills at the end, pointing to the [`tools/`](../tools/) directory where applicable.
