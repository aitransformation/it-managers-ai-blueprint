# Section 14: Skills Framework

> **Journey Step:** Step 3 — Skill Up

---

## Skills matter more than tools

The IT Manager who deploys capable AI agents but lacks the skills to govern, verify, and extend them is in a more precarious position than the IT Manager who has not yet deployed any.

Tools can be replaced. Skills compound. The skills described here become more valuable as AI capability increases, because they are the skills required to direct and govern that capability responsibly.

---

## IT Manager competency standard

### Prompt engineering

The IT Manager shall be capable of writing structured prompts that produce reliable and verifiable outputs. This includes:
- Specifying task, context, format, and acceptance criteria within the prompt
- Using system prompts to constrain model behaviour
- Iterating prompts based on output analysis
- Maintaining the prompt library to the required standard

Competency is demonstrated through maintained, verified prompts in the production library — not through ability to get a convincing response from ChatGPT.

### System architecture

The IT Manager shall be capable of:
- Evaluating the architecture of agent-built tools
- Assessing data flows for sovereignty compliance
- Identifying security boundary requirements
- Specifying integration points

This means being able to read, understand, and critically evaluate technical designs — and to instruct the agent to produce alternatives where the initial design does not meet the required standard.

### AI output verification

**AI output shall always be treated as draft material requiring validation, not as confirmed fact.**

The IT Manager shall apply a systematic verification discipline to all AI outputs before they are acted upon:

| Output type | Verification approach |
|------------|----------------------|
| Code | Sandbox testing, edge case testing, security review |
| Reports | Cross-reference key figures against source systems |
| Recommendations | Validate against primary sources, not solely AI output |
| Anything actioned | Human review before production |

The verification standard for each output type is documented in the relevant prompt library entry.

### Data literacy

The IT Manager shall maintain a current and accurate understanding of the organisation's full data landscape:
- Every significant data asset, its classification, its owner, its quality status, and its sovereignty requirements

This is the foundation for every data-adjacent decision — from AI capability deployment to vendor evaluation to incident response. Without it, you cannot govern an AI system safely.

### AI security awareness

The IT Manager shall understand the AI-specific threat vectors described in Section 7 and shall be capable of assessing new agent deployments for exposure to:
- Prompt injection
- Data leakage
- Privilege escalation

This understanding is applied at the design stage of every new capability — not retrospectively after something goes wrong.

---

## User training standard

Three tiers. The tier delivered depends on the role and the level of agent access.

| Tier | Audience | Content | Minimum Duration |
|------|----------|---------|-----------------|
| **Tier 1** | All staff | AI capability and limitations; identifying errors; data safety rules; escalation paths | 30 minutes |
| **Tier 2** | IT team | Deployed tools hands-on; prompt writing standards; output verification requirements; incident response | 2 hours |
| **Tier 3** | IT Manager and champions | Prompt engineering depth; agent operations; governance; emerging capabilities | 2+ hours/week ongoing |

**Tier 2 competency must be demonstrated before unsupervised agent use is permitted.**

**Tier 3 development is a core performance requirement of the IT Manager role** — not an optional extra.

---

## Internal champions

Identify individuals who engage readily with new technology. Brief them before the wider team. Give them access to test environments. Formally recognise them as champions.

Champions are the most effective channel for peer-level adoption support. They will also surface practical issues that formal feedback mechanisms miss.

---

## Implementation checklist

- [ ] Assess IT Manager competency against the five defined standards — build a personal development plan
- [ ] Dedicate a minimum of two hours per week to deliberate skills development — calendar protected
- [ ] Deliver Tier 1 training to all staff before AI-affected tools go live
- [ ] Deliver Tier 2 training to all IT team members before agent capabilities are accessible
- [ ] Identify two internal champions — brief before the wider team, involve in testing
- [ ] Build a competency sign-off process for Tier 2 — no unsupervised agent use without demonstration
- [ ] Include skills development update in the monthly governance review

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/anti-ai-writing.md`](../tools/anti-ai-writing.md) | Practical skills training — analysing and improving AI outputs |
| [`tools/prompt-injection-defence.md`](../tools/prompt-injection-defence.md) | Practical security awareness — understanding injection patterns |

**Related sections:** [Section 7 — AI Security](07-ai-security.md) · [Section 12 — Prompt Library](12-prompt-library.md) · [Section 16 — Change Management](16-change-management.md)
