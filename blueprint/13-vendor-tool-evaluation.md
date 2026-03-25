# Section 13: Vendor & Tool Evaluation

> **Journey Step:** Step 2 — Foundations / Step 3 — Skill Up

---

## The problem with AI tooling

The AI tooling market is characterised by rapid development, aggressive marketing, and products that frequently fail to meet the governance and data sovereignty standards required for professional IT deployment.

The IT Manager's job is not to evaluate every new tool that appears. It is to apply a consistent evaluation framework so that decisions are made on evidence rather than on marketing, and so that the organisation's data sovereignty standard is not compromised by convenience.

---

## Build vs buy

With local AI agents capable of generating functional internal tools, an agent-built internal tool shall routinely be assessed as the preferred option — particularly where the commercial alternative would require Restricted or Confidential data to be transmitted to a third-party service.

| Assessment Criterion | Build | Buy |
|---------------------|-------|-----|
| Function can be fully specified with written acceptance criteria | Preferred | Consider |
| Data involved is Restricted or Confidential | Strongly preferred | Requires data sovereignty assessment |
| Team has capacity to maintain the built tool | Viable | Consider support model |
| Extensive pre-built integration with external systems required | May be less efficient | May be more efficient |
| Complex, multi-feature platform requirements | May be insufficient | Preferred |

---

## Vendor evaluation scorecard

Score on a three-point scale: **1** = does not meet standard, **2** = partially meets, **3** = fully meets.

Tools scoring below 18 of 24 shall not proceed to procurement without documented exception and senior leadership approval.

| Criterion | Assessment Standard |
|-----------|-------------------|
| **Data handling transparency** | Clear, contractually binding statement of where data is processed and stored. DPA available. |
| **Data sovereignty compliance** | Data handling complies with the organisation's sovereignty standard for the relevant classification. |
| **MCP / API compatibility** | Exposes a compatible integration surface for connection to the local agent architecture. |
| **Data portability and exit** | All data exportable in standard format. Process documented and tested by the vendor. |
| **Pricing clarity** | Transparent and predictable at the organisation's scale of use. |
| **Security certification** | ISO 27001 and SOC 2 Type II minimum for products handling Internal or Confidential data. |
| **Vendor stability** | Demonstrably funded, growing, with a track record of product continuity. |
| **Support quality** | Documented SLA support available from qualified personnel. Escalation paths defined. |

---

## Using the local agent for vendor research

The Coding Agent and Head Agent can assist with vendor evaluation research. Useful tasks:
- Summarise publicly available documentation on data handling policies
- Compare feature claims against the scorecard criteria
- Identify missing DPA or compliance information

**Verify all agent research outputs against primary sources.** Do not submit vendor evaluation decisions to leadership based solely on AI-generated research.

---

## The vendor register

Maintain a vendor register with, at minimum:
- Vendor name and product
- Current DPA status and expiry date
- Data classification permitted under the DPA
- Security certification expiry dates
- Contract renewal date
- Last evaluation date and score

Review the vendor register quarterly as part of the governance review.

---

## Implementation checklist

- [ ] Build the vendor scorecard — adapt criteria to the organisation's sovereignty and governance standards
- [ ] Apply the scorecard to all current SaaS tools at next renewal
- [ ] Conduct build vs buy assessment for every new internal tooling requirement
- [ ] Use the local agent to pre-research vendor evaluations — verify outputs against primary sources
- [ ] Maintain a vendor register with current DPA status, data classification permitted, and review dates
- [ ] Apply the scorecard as a procurement criterion — document exceptions with justification

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/security-skill-checker.md`](../tools/security-skill-checker.md) | Security screening for any skill or tool before installation |

**Related sections:** [Section 2 — Data Sovereignty](02-data-sovereignty.md) · [Section 9 — Governance, Risk & Compliance](09-governance-risk-compliance.md)
