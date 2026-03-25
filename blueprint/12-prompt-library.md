# Section 12: Prompt Library & AI Asset Management

> **Journey Step:** Step 4 — Build / Step 5 — Feedback Loop

---

## Prompts are organisational assets

Prompts that produce reliable, verified outputs represent invested development effort, domain knowledge, and confirmed alignment between instruction and desired output. They shall be managed as assets: stored, versioned, owned, and maintained.

> **Prompt Library Standard:** All prompts used in production agent operations shall be documented in the organisational prompt library, stored in version control, assigned to a named owner, and subject to a defined review cycle. No prompt shall be deployed to production without verification against defined acceptance criteria. Changes to production prompts are change management events and shall be tested before deployment.

---

## Library structure

The prompt library is maintained in the same version-controlled repository as agent configuration. For each prompt, the library records:

| Field | Description |
|-------|-------------|
| Prompt name | Short, descriptive name |
| Purpose | What this prompt is for and when to use it |
| Full prompt text | The complete prompt as deployed |
| Model and tier | The model this was developed for |
| Verification criteria | What a passing output looks like — specific and testable |
| Test results | Date tested, pass/fail, notes |
| Date of last review | When the prompt was last assessed |
| Named owner | Who is accountable for this prompt |
| Review cadence | Quarterly (operational) or monthly (high-impact) |

---

## Review cadence

- **Core operational prompts:** reviewed quarterly
- **High-impact or time-sensitive prompts:** reviewed monthly
- **Any prompt that fails its acceptance criteria:** reviewed immediately

---

## Prompt decay

Prompts developed for one model version may not perform identically on a subsequent version. When a model update is being tested:
1. Run each prompt in the library against the new model version
2. Compare outputs to the acceptance criteria
3. Any prompt not meeting its criteria on the new version is updated and re-verified before the model update goes to production

Model updates and prompt retesting are linked — you cannot update a model without retesting the prompts that depend on it.

---

## Starting the library

Do not wait until you have dozens of prompts. Start the library when you deploy the first agent. Seed it with:

1. The Head Agent system prompt
2. The standard task request format
3. The monitoring triage prompt
4. The incident summary format
5. The weekly IT health report template

Each entry should take ten minutes to document properly. The investment pays back every time you update a model or onboard a new team member.

---

## Implementation checklist

- [ ] Create the prompt library repository in version control — local, self-hosted in Gitea
- [ ] Document all current production prompts — include verification criteria and test results
- [ ] Assign owners to all prompts
- [ ] Set review dates — quarterly for operational, monthly for high-impact
- [ ] Include prompt performance testing in the model update testing procedure
- [ ] Share the library location with all team members using agent capabilities
- [ ] Review and cull the library quarterly — remove prompts that are no longer in use

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/anti-ai-writing.md`](../tools/anti-ai-writing.md) | Review prompt text for weak, vague, or AI-sounding patterns before deploying |

**Related sections:** [Section 6 — System Prompt Management](06-system-prompt-management.md) · [Section 14 — Skills Framework](14-skills-framework.md)
