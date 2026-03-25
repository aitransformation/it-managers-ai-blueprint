# Section 1: Business Outcome Mapping & IT Alignment

> **Journey Step:** Step 1 — Audit

---

## The core error to avoid

A fundamental error in IT management is to begin simplification and improvement programmes by auditing IT systems. IT systems are not the subject of the exercise. They are an output of it.

The correct starting point is the business outcomes the organisation must deliver. The IT estate is evaluated last, not first. This order is not optional.

---

## The four core business drivers

Every business outcome maps to one or more of four universal operational drivers. See [`00-principles.md`](00-principles.md) for the full definition. In brief:

- **Make** — Create something new
- **Change** — Transform something to a more valuable state
- **Communicate** — Move information between people, teams, or systems
- **Deliver** — Move value to the customer

Every IT system, process, and data flow shall be traceable to at least one business outcome. That outcome shall in turn map to one or more of the four core drivers. Any system that cannot be traced to a business outcome through this mapping shall be placed under formal review and decommissioned unless a justified exception is approved by senior leadership.

---

## Prerequisites

**Senior leadership alignment is required before you start.** Present outcome mapping as a business improvement initiative, not a technology project. Without leadership sponsorship, the IT Manager cannot challenge systems and investments that don't serve defined outcomes.

Get the sponsorship in writing, however simple. A confirmed email is enough.

---

## The outcome mapping methodology

Eight steps, applied to each business outcome in sequence, repeated until all outcomes are mapped.

### Step 1 — Define the business outcome

State in plain, non-technical language what the business must be able to do. Not how. What.

**Well-stated examples:**
- "A new customer account must be created and fully provisioned within four hours of contract signature."
- "Monthly management accounts must be produced and distributed by the fifth working day of the following month."
- "A field engineer must be able to access job information and submit completion reports from any location without network connectivity."

**Poorly-stated (reframe it):**  
"The CRM must be available to the sales team." — This is a system availability requirement. Restate it as the outcome the system serves.

### Step 2 — Map to core drivers

Most outcomes have one primary driver with secondary connections. A customer onboarding outcome primarily serves **Deliver**, with connections to **Communicate** and **Make**. Document all connections. This ensures a system is evaluated against all the outcomes it must serve, not just the obvious primary one.

### Step 3 — Process map

Document every step required to deliver the outcome. Inputs, outputs, decision points, dependencies. Produce this collaboratively with the people who actually execute the process — not from documentation that may have drifted from practice.

The gap between documented process and actual practice is almost always present. It surfaces workarounds, risks, and inefficiencies that IT solutions alone cannot fix. Document divergences and escalate to the relevant process owner.

### Step 4 — Data map

For each process step, identify every data element consumed or produced. Source, format, owner, classification, location, flows.

This step is the foundation of the data sovereignty posture. It will surface data held in inappropriate locations, transmitted insecurely, or subject to regulatory obligations not currently met.

**No AI processing of any data element shall be approved until that element has been classified and its sovereignty requirements confirmed.**

The data map produced here feeds directly into the data register in Section 2.

### Step 5 — People and system map

Identify every person, team, and system involved. This step routinely surfaces shadow systems, spreadsheets, personal cloud storage, messaging tools, and manual workarounds that are undocumented but operationally critical.

All identified shadow systems shall be brought into the asset register, assessed for data sovereignty and security risk, and included in the improvement backlog.

### Step 6 — Fit-for-purpose assessment

A system is fit for purpose if it:
- Reliably enables the process steps it supports
- Handles data in compliance with sovereignty requirements
- Integrates correctly with dependent systems
- Can be adequately governed and monitored
- Is likely to continue meeting these requirements over a reasonable planning horizon

A system that fails any of these criteria on any outcome it is mapped to shall be documented as a candidate for remediation or replacement.

### Step 7 — Remediate or replace

The decision is made on evidence: the cost and reliability of remediation, the technical debt of the existing system, and its likely longevity. A system requiring repeated remediation cycles is a replacement candidate regardless of the apparent low cost of any single round.

Where replacement is indicated, the requirement is derived from the outcome mapping, not from the features of the incumbent. Define what the replacement must do in outcome terms and evaluate candidates against those requirements.

### Step 8 — Repeat

Continue until every business outcome has been mapped, assessed, and confirmed as supported by fit-for-purpose systems. The outcome register is a live document, reviewed and updated at minimum quarterly.

---

## Implementation checklist

- [ ] Obtain written senior leadership sponsorship before commencing
- [ ] Convene outcome definition workshops with all operational function heads
- [ ] Build and maintain the outcome register — every outcome named, owned, and mapped to drivers
- [ ] Complete process maps collaboratively with the people who execute each process
- [ ] Complete data maps for all process steps — classify every data element
- [ ] Identify all shadow systems, bring into the asset register and assess for risk
- [ ] Conduct fit-for-purpose assessments for every identified system
- [ ] Build the improvement backlog from fit-for-purpose failures, prioritised by business impact
- [ ] Schedule a minimum quarterly review of the outcome register

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/estate-discovery.md`](../tools/estate-discovery.md) | Structured approach to inventorying systems and mapping them to outcomes |

**Related sections:** [Section 2 — Data Sovereignty](02-data-sovereignty.md) (the data map from Step 4 feeds the data register)
