# Step 1: Audit

**Map your estate. Define your business outcomes. Classify your data.**

This is the foundation everything else is built on. Do not skip it or cut it short. An IT function that does not know what it has cannot govern or improve what it has.

---

## What this step covers

- Mapping business outcomes to the four core drivers (Make, Change, Communicate, Deliver)
- Auditing every IT system against those outcomes
- Building the data register — classifying every data asset
- Identifying shadow systems and undocumented processes
- Establishing baseline measurements for the top ROI candidates

---

## What you produce

| Output | Where it lives | Used in |
|--------|----------------|---------|
| Business outcome register | OpenBrain / Gitea | Everything |
| Data register | OpenBrain | Sections 2, 2b, 10 |
| Asset register | OpenBrain | Sections 8, 13 |
| Shadow system log | OpenBrain / improvement backlog | Section 1 |
| Baseline measurements | Spreadsheet | Section 15 |
| Leadership sponsorship document | Filed document | Section 1 |

---

## Before you start

You need:
- **Written senior leadership sponsorship.** Without it, you cannot challenge systems that don't serve business outcomes. Get this first. A confirmed email is sufficient.

---

## The work

### 1. Get leadership sponsorship
Explain the programme as a business improvement initiative. Ask for a written mandate to challenge systems and investments. The IT Manager cannot do this unilaterally.

### 2. Map business outcomes
Work with each function head. Ask: "What must this part of the business be able to do?" Write each answer as a plain-language outcome statement.

Map each outcome to one or more of the four core drivers:
- **Make** — creating something new
- **Change** — transforming something to a more valuable state
- **Communicate** — moving information between people, teams, or systems
- **Deliver** — moving value to the customer

### 3. Map processes
For each outcome, map the process. Do this with the people who actually execute it — not from documentation. The gap between documented process and actual practice is important information.

### 4. Map data
For each process step, identify every data element. Source, format, owner, location. Classify each one:
- **Restricted** — personal data, financial records, credentials, IP
- **Confidential** — commercially sensitive, strategic
- **Internal** — operational data
- **Public** — approved for external publication

No AI processing of any data element until it is classified.

### 5. Map systems
Identify every system involved in every process. Include the ones people do not talk about — spreadsheets on desktops, WhatsApp groups used for operations, personal Dropbox folders. These are all shadow systems. They all go in the asset register.

### 6. Assess fitness for purpose
For each system: does it reliably enable the process, handle data compliantly, integrate correctly, and remain governable? Document failures. Build the improvement backlog.

### 7. Establish baselines
For the top three ROI target capabilities, measure the current state. Time per week, error rate, time from request to completion. Track for a minimum of two weeks before you deploy anything.

---

## How long does this take?

Realistically: two to four weeks for an SME estate, working 8 hours per week on this alongside normal operations. Don't rush it. Inaccurate audit outputs create problems further down the journey.

---

## Blueprint sections for this step

| Section | What it covers |
|---------|---------------|
| [`blueprint/01-outcome-mapping.md`](../blueprint/01-outcome-mapping.md) | The full 8-step outcome mapping methodology |
| [`blueprint/02-data-sovereignty.md`](../blueprint/02-data-sovereignty.md) | Data classification framework and data register |
| [`blueprint/15-business-case-roi.md`](../blueprint/15-business-case-roi.md) | Baseline measurement approach |

---

## Tools for this step

| Tool | Use |
|------|-----|
| [`tools/estate-discovery.md`](../tools/estate-discovery.md) | Structured approach to inventorying systems and mapping to outcomes |

---

## Done when

- [ ] Leadership sponsorship document filed
- [ ] Outcome register created — minimum 5 outcomes, each mapped to drivers
- [ ] Data register created — minimum 10 entries, each classified and owner confirmed
- [ ] Asset register updated — shadow systems included
- [ ] Improvement backlog exists — fit-for-purpose failures listed and prioritised
- [ ] Baseline measurements established for top 3 ROI candidates

**→ Next step: [Step 2 — Foundations](02-foundations.md)**
