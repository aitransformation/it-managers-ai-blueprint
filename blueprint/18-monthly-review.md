# Section 18: Monthly Review Cadence

> **Journey Step:** Step 5 — Feedback Loop

---

## The review is not optional

The monthly review is the mechanism by which the IT Manager maintains operational control, meets governance obligations, and sustains leadership visibility. It is a protected, recurring commitment.

> **Monthly Review Standard:** The IT Manager shall conduct a structured monthly review of all AI deployments, governance documentation, performance metrics, and programme priorities. The review shall be documented in a one-page summary shared with the nominated senior sponsor within 48 hours. The review shall not be cancelled without the explicit agreement of the senior sponsor.

If the review keeps slipping, something is wrong — either with the calendar discipline or with the programme itself. Both are worth investigating.

---

## Review structure — 90 minutes

| # | Agenda item | Duration |
|---|-------------|----------|
| 1 | AI Register review — new deployments, decommissions, incidents | 10 min |
| 2 | Data register review — new assets, classification changes, quality issues | 10 min |
| 3 | ROI tracking update — metrics moving as expected; anomalies | 15 min |
| 4 | Prompt library review — prompts due; decay issues; new verified prompts | 15 min |
| 5 | Agent performance review — failures, unexpected outputs, access scope issues | 15 min |
| 6 | Security and compliance check — AI stack CVEs; compliance items due; DPA renewals | 10 min |
| 7 | Team feedback — what is and is not working | 10 min |
| 8 | Next month priorities — top three focus areas | 5 min |

---

## The one-page monthly summary

The summary is a single page, distributed to the senior sponsor within 48 hours of the review. It covers:

- AI Register: changes since last review
- Data register: changes since last review
- ROI metrics: current vs baseline, trend
- Agent performance: key outputs, any failures or escalations
- Prompt library: prompts reviewed, any decay issues
- Security: items addressed, items open
- Top three priorities for next month

It is not a detailed technical report. It is a governance summary written for a senior leader who is not in the weeds of the AI programme. Plain language. No jargon.

---

## Annual blueprint reset

Once per year, the IT Manager conducts a full programme reset:
- Re-runs the outcome mapping process against the current business
- Reassesses all deployed systems for continued fit for purpose
- Reviews the full AI Register
- Verifies that all governance documentation remains current

The annual reset prevents the accumulation of new technical debt and ensures the IT programme continues to serve current business outcomes.

Set the annual reset date before the end of Q1. Put it in the calendar the same day you set up the monthly review.

---

## Implementation checklist

- [ ] Set a recurring 90-minute protected calendar entry — same day each month
- [ ] Build the one-page monthly summary template
- [ ] Set the annual blueprint reset date — calendar entry placed before end of Q1
- [ ] Distribute the first monthly summary to the senior sponsor within 48 hours of the first review
- [ ] Review the monthly summary template every six months — adjust format if needed

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | Governance Agent pulls review agenda items from OpenBrain |

**Related sections:** [Section 9 — Governance, Risk & Compliance](09-governance-risk-compliance.md) · [Section 12 — Prompt Library](12-prompt-library.md) · [Section 19 — Research Watchlist](19-research-watchlist.md)
