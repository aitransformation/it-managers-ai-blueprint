# Section 15: Business Case & Return on Investment

> **Journey Step:** Step 1 — Audit / Step 5 — Feedback Loop

---

## The accountability requirement

The IT Manager is accountable for demonstrating the value of AI investments in terms meaningful to senior leadership. This requires:
- Quantifiable baselines **before** deployment
- Tracked outcomes **after** deployment
- Presentation in business language — outcomes, value, and risk

Technology features do not feature in a business case. Outcomes do.

---

## Baseline measurement

Before deployment commences, establish and document:

| Metric | Measurement approach | Minimum period |
|--------|---------------------|----------------|
| Time spent per week on tasks the AI will handle | Tracked manually, time log | 2 weeks |
| Error rate for the relevant manual process | Counted, logged | 4 weeks |
| Time from request to completion for the relevant process | Average and 90th percentile | 4 weeks |
| Current tooling cost where AI replaces commercial spend | Invoice/contract review | Current |

If you don't have baselines, you cannot demonstrate ROI. Establish them before any deployment starts, not after.

---

## ROI framework

Return on investment is calculated over a 90-day post-deployment period:

```
ROI = (Time recovered in hours × average fully-loaded IT staff cost per hour)
    + (Reduction in error-related remediation cost)
    + (Reduction in tooling cost)
    - (AI infrastructure and running cost)
```

**A positive 90-day ROI** confirms the deployment is delivering value. Record as a successful deployment in the AI Register.

**A negative 90-day ROI** triggers a review:
- Is the capability not yet delivering as designed? — That is a technical problem to solve.
- Did the baseline task have insufficient volume to justify the deployment cost? — That is a prioritisation lesson.

---

## Presenting to leadership

Business case presentations lead with outcomes, not technology. The structure is:

1. **The outcome that was improved** — in plain language, what is better now
2. **The before position** — time, cost, error rate (your baselines)
3. **The current position** — the measured change
4. **The value delivered** — calculated in money or time
5. **The cost of the capability** — infrastructure, running cost, time invested

The model, agent, and technical architecture are context. The outcome is the subject. If the first thing in your presentation is the name of a product or model, start again.

---

## Prioritising what to deploy

Not all candidate AI capabilities will show positive ROI at the same time. Prioritise based on:
- Volume: high-frequency tasks benefit more from automation
- Time cost: tasks that consume significant IT Manager time have higher ceiling ROI
- Error cost: tasks where errors are expensive to remediate
- Current tooling cost: tasks where AI replaces paid commercial tools

The top three ROI candidates are the first three deployments. Do not build a monitoring agent before you know what your top three are.

---

## Implementation checklist

- [ ] Identify the top three ROI target capabilities before deployment begins
- [ ] Establish baseline measurements for all three — time tracked for a minimum of two weeks
- [ ] Build the ROI tracking document — shared with senior sponsor from day one
- [ ] Set a 90-day review date from first deployment of each capability
- [ ] Prepare the first leadership presentation: outcomes first, technology second, costs third
- [ ] Record ROI outcomes in the AI Register for each deployment

---

## Tools & Skills

No specific tools for this section. The measurement discipline itself is the tool.

**Related sections:** [Section 1 — Business Outcome Mapping](01-outcome-mapping.md) · [Section 18 — Monthly Review](18-monthly-review.md)
