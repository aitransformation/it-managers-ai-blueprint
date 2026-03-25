# Section 9: Governance, Risk & Compliance

> **Journey Step:** Step 2 — Foundations

---

## IT policy framework — complete set

Every professionally managed IT function operates under a set of defined policies. AI deployment does not create the need for IT policies — it adds to an existing requirement.

Policies marked **AI-Updated** require specific additions to address AI tools and agents. All other policies apply as standard but should be reviewed to ensure AI use cases are not inadvertently out of scope.

### Core IT policies

| Policy | Description | AI-Updated |
|--------|-------------|-----------|
| Acceptable Use Policy (AUP) | Defines permitted and prohibited use of IT systems and data by all users | Yes — AI tool addendum required |
| Information Security Policy | Overarching security posture, risk appetite, and control framework | Yes — AI security controls and threat vectors |
| Data Classification Policy | Defines classification tiers and handling requirements | Yes — AI processing rules per tier |
| Data Protection Policy | GDPR and applicable data protection obligations | Yes — Article 22, AI processing disclosure |
| Access Control Policy | Principles governing user, system, and agent access to systems and data | Yes — agent access scope requirements |
| Password and Credential Policy | Standards for credential creation, storage, and rotation | Yes — Vault requirement, service account rules |
| Network Security Policy | Network segmentation, firewall rules, permitted traffic | Yes — agent server network position |
| Incident Response Policy | Classification, escalation, and resolution of security and operational incidents | Yes — AI-specific incident response procedure |
| Change Management Policy | Approval and testing requirements for changes to IT systems | Yes — model updates, agent configuration changes |
| Asset Management Policy | Registration and lifecycle management of IT assets | Yes — AI Register as asset sub-register |
| Backup and Recovery Policy | Backup schedules, retention, and recovery testing | Yes — agent configuration backup requirements |
| Remote Access Policy | Controls governing remote access to internal systems | Standard |
| Third-Party and Vendor Policy | Requirements for suppliers, SaaS providers, and service providers | Yes — DPA requirements, vendor scorecard |
| Bring Your Own Device Policy | Where applicable | Standard |
| Business Continuity Policy | Plans for continued operation during significant disruptions | Yes — AI runbook requirements |

### AI-specific policies (new)

| Policy | Description |
|--------|-------------|
| AI Governance Policy | Overarching policy covering AI Register, risk classification, deployment standards, and governance cadence |
| AI Data Processing Policy | Defines which AI tools may process which data classifications, local vs frontier rules, and the approval process |
| AI Agent Access Policy | Defines agent access scopes, the least-privilege standard, and technical enforcement requirements |
| Prompt Library Policy | Ownership, review cadence, change management, and version control requirements for the prompt library |
| Model Management Policy | Version pinning, update testing, frontier model exception process, OpenRouter usage rules |

---

## Standard Operating Procedures — framework

A Standard Operating Procedure (SOP) documents a process in sufficient detail that a competent person can execute it consistently without relying on institutional knowledge. Every IT process — whether executed manually, by an agent, or as a human-agent collaboration — shall have an SOP.

### Infrastructure SOPs

| SOP | Purpose | Agent-Assisted? |
|-----|---------|-----------------|
| New starter provisioning | End-to-end process for provisioning a new employee | Yes — Configuration Agent automates steps 3–8 |
| Leaver offboarding | Secure removal of access, data handling, asset return | Yes — Configuration Agent handles access revocation |
| Server build and baseline | Standard build process for new servers | Yes — Coding Agent generates build scripts |
| Network device configuration | Standard configuration for new/changed network devices | Partial |
| SSL certificate renewal | Process for identifying, ordering, and deploying SSL renewals | Yes — Monitoring Agent identifies, IT Manager approves |
| Firewall rule change | Request, approval, implementation, and verification of firewall rule changes | Partial — Security Agent drafts, IT Manager approves |
| Backup verification | Monthly backup restore test procedure | No — manual IT Manager action |
| DR invocation | Steps to invoke disaster recovery for each critical system | No — manual only |

### AI-specific SOPs

| SOP | Purpose |
|-----|---------|
| Agent task request | How the IT Manager requests a task from the Head Agent |
| New agent capability deployment | End-to-end process from requirements to supervised testing to autonomous operation |
| Agent incident response | Step-by-step response to an agent producing incorrect outputs or taking unintended actions |
| Frontier model exception request | Process for requesting and approving use of a frontier model for a specific task |
| Prompt library update | Process for creating, testing, reviewing, and retiring prompts |
| OpenBrain memory review | Process for reviewing and curating OpenBrain memory content quarterly |
| AI Register update | Process for adding, updating, and reviewing AI Register entries |
| Data classification review | Process for reviewing and updating data asset classifications |
| AI security incident | Specific response process for AI-related security incidents (prompt injection, data leakage, privilege escalation) |

### Security and compliance SOPs

| SOP | Purpose | Agent-Assisted? |
|-----|---------|-----------------|
| Vulnerability management | Receiving, prioritising, and remediating vulnerability findings | Yes — Security Agent generates recommendations |
| Patch deployment | Testing and deployment of patches to production systems | Partial |
| Security incident response | End-to-end response to a security incident | Partial — Security Agent provides analysis |
| Access review | Periodic review of user and system access rights | Yes — Governance Agent schedules and tracks |
| DMARC report review | Reviewing and acting on DMARC aggregate and forensic reports | Yes — Monitoring Agent summarises |
| Data breach response | Response to actual or suspected data breach | No — manual only, legal involvement |

---

## Implementation checklist

- [ ] Audit existing policies against the core set — identify gaps
- [ ] Update all existing policies to include AI-specific additions where marked
- [ ] Draft the five AI-specific policies — get leadership approval before distributing
- [ ] Document all current IT processes as SOPs — start with the top ten by frequency
- [ ] Create the AI-specific SOP set — at minimum the nine listed above
- [ ] Store all policies and SOPs in version control (Gitea) — reviewed annually minimum
- [ ] Set review dates for all policies and SOPs — enter in the governance register
- [ ] Assign a named owner to every policy and SOP
- [ ] Brief all staff on policy changes before they take effect

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | Store policies, SOPs, and governance register in OpenBrain |

**Related sections:** [Section 2b — Data Access Governance](02b-data-access-governance.md) · [Section 12 — Prompt Library](12-prompt-library.md) · [Section 18 — Monthly Review](18-monthly-review.md)
