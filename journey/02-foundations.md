# Step 2: Foundations

**Simplify first. Build policy and data hygiene before you build anything else.**

Deploying AI on a messy, ungoverned IT estate is how you get messy, ungoverned AI. This step builds the foundations that make everything in Step 4 work reliably and safely.

---

## What this step covers

- Drafting and approving the core policy set
- Building data hygiene and quality foundations
- Setting up governance frameworks
- Ensuring backup and DR cover AI-adjacent systems
- Simplifying the estate where the audit identified clear improvement opportunities

---

## The principle

**Simplify before you automate.**

If a process is broken, automating it gives you a broken process that runs faster. Fix the process first. Automate what works. This is not a technology rule — it is a basic operations rule.

---

## What you produce

| Output | Where it lives | Used in |
|--------|----------------|---------|
| Acceptable Use Policy — AI Addendum | Filed / Gitea | Sections 2b, 9 |
| AI Governance Policy | Gitea | Section 9 |
| Data Classification Policy | Gitea | Section 2 |
| Data quality assessments | OpenBrain | Section 10 |
| Backup schedule including AI assets | Runbook / documentation | Section 11 |
| Vendor register with DPA status | OpenBrain | Section 13 |

---

## Before you start

You need:
- Step 1 complete — outcome register, data register, and asset register all exist
- Leadership sponsorship in place — you need their approval for the AUP addendum

---

## The work

### 1. Draft and approve the policies
Start with the Acceptable Use Policy AI Addendum. This is the single most important document for data safety. It tells every person in the organisation what they can and cannot do with AI tools. It needs leadership approval and a staff briefing before any AI capability goes live.

Then draft:
- AI Governance Policy
- Data Classification Policy (may already exist — update it if so)
- AI Data Processing Policy

These do not need to be long. They need to be clear and specific.

### 2. Brief all staff on the AUP addendum
In person. Not by email. The IT Manager or a senior sponsor explains the rules, why they exist, and what happens if they are breached. Allow genuine questions.

### 3. Build data quality foundations
For every data asset connected to planned AI processing: assess completeness, accuracy, consistency, timeliness, and accessibility. Any data asset with a material deficiency gets a data improvement plan before AI processing is enabled.

### 4. Identify schema inconsistencies
Where the same entities appear in multiple systems with different field names, formats, or values — document it and build a standardisation plan. Agents processing this data will produce unreliable outputs without it.

### 5. Verify backup coverage
Every system that will be connected to AI processing needs to be backed up. This includes OpenBrain when it is deployed. Check the backup schedule, confirm restore testing is happening, and document the DR procedure for any system that does not yet have one.

### 6. Simplify where the audit identified clear wins
Not every simplification opportunity needs to be addressed now. Pick the ones that directly reduce complexity for the systems you are planning to connect to AI. Simplification at this stage pays back in the build step.

---

## Blueprint sections for this step

| Section | What it covers |
|---------|---------------|
| [`blueprint/02-data-sovereignty.md`](../blueprint/02-data-sovereignty.md) | Data classification, local-first architecture |
| [`blueprint/02b-data-access-governance.md`](../blueprint/02b-data-access-governance.md) | AUP addendum, access approval standard |
| [`blueprint/09-governance-risk-compliance.md`](../blueprint/09-governance-risk-compliance.md) | Full policy framework, SOPs |
| [`blueprint/10-data-strategy-hygiene.md`](../blueprint/10-data-strategy-hygiene.md) | Data quality assessment, local RAG |
| [`blueprint/11-backup-disaster-recovery.md`](../blueprint/11-backup-disaster-recovery.md) | Backup, runbooks, AI resilience |
| [`blueprint/13-vendor-tool-evaluation.md`](../blueprint/13-vendor-tool-evaluation.md) | Vendor scorecard, DPA verification |

---

## Done when

- [ ] AUP AI Addendum approved by leadership and distributed to all staff
- [ ] AI Governance Policy and Data Classification Policy drafted and filed
- [ ] Staff briefed in person on AI data rules
- [ ] Data quality assessments complete for all AI-connected data assets
- [ ] Backup schedule updated to include all systems that will connect to AI
- [ ] Vendor register created with current DPA status for all relevant tools

**→ Next step: [Step 3 — Skill Up](03-skill-up.md)**
