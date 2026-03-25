# Section 2b: Data Access Governance — Approved Access Policy

> **Journey Step:** Step 2 — Foundations

---

## The access approval standard

No person and no system may connect to, query, or transmit organisational data through any AI tool, API, or automated process without explicit approval. This applies to all data at all classification levels.

**The default position is denied. Access is granted, not assumed.**

This standard exists because the most common data sovereignty breach in SME environments is not a sophisticated attack. It is a well-intentioned employee who opens a cloud AI tool, pastes in a customer document, and asks it a question. The tool processes that data on servers the organisation does not control. The data may be retained. The employee had no idea this was a problem.

---

## What requires approval — worked examples

| Scenario | Approval Required? |
|----------|-------------------|
| IT Manager uses Claude Code CLI on the local agent server to generate a script | No — local processing, approved tool |
| Team member opens ChatGPT in their browser and pastes in an internal report | Yes — external AI, Internal data |
| Team member opens ChatGPT and asks a general question with no company data | Context-dependent — see AUP |
| Coding Agent calls OpenRouter API with Internal-classified code | Yes — documented in AI Register, frontier model exception approval in place |
| Monitoring Agent processes firewall logs (Confidential) | Yes — recorded in AI Register as local processing |
| Finance team member pastes customer financial data into any AI tool | Never permitted — Restricted data |

---

## The access register

Every approved AI data access — whether by a person or a system — is recorded in the governance register in OpenBrain:

```sql
register_type = 'ai_deployment'
```

Each record includes:
- Who or what is accessing the data (person name / agent role)
- What data they are permitted to access (classification and specific sources)
- What AI tool they are permitted to use with that data
- Whether processing is local or via an approved frontier model
- The approval date and approving authority
- The review date

---

## Acceptable Use Policy — AI addendum

The organisation's Acceptable Use Policy shall include an AI-specific addendum covering:

**1. Approved AI tools**  
A named list of AI tools approved for use. Any tool not on the list is not approved. The list is maintained by the IT Manager and reviewed quarterly.

**2. Data rules by classification**  
Plain-language statement of what data can and cannot be used with each approved tool tier. Not a policy document people need to interpret — a table they can check.

**3. Prohibition on shadow AI**  
Explicit prohibition on connecting organisational data to any unapproved AI service, including browser-based AI tools, mobile AI applications, and AI features embedded in unapproved SaaS products.

**4. Reporting obligation**  
Employees must report any accidental or uncertain AI data sharing to the IT Manager within 24 hours.

**5. Consequences**  
Clear statement that violation of these rules is treated as a data breach under the organisation's disciplinary policy.

---

## Implementation checklist

- [ ] Draft the AI addendum to the AUP — get leadership approval before distributing
- [ ] Build and publish the approved AI tools list — keep it short and specific
- [ ] Create the data rules table — one row per classification tier, one column per approved tool tier
- [ ] Brief all staff on the AUP addendum in person — email alone is not sufficient
- [ ] Collect written acknowledgement from all staff
- [ ] Set up the AI Register in OpenBrain — first entries are human users, then agents
- [ ] Review the AI Register and approved tools list quarterly

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | Maintain the AI Register in OpenBrain governance_register table |

**Related sections:** [Section 2 — Data Sovereignty](02-data-sovereignty.md) · [Section 9 — Governance, Risk & Compliance](09-governance-risk-compliance.md)
