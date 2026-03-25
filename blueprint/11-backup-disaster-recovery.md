# Section 11: Backup, Disaster Recovery & AI Resilience

> **Journey Step:** Step 2 — Foundations / Step 4 — Build

---

## AI agents are system assets

AI agents that have become operationally critical shall be managed as system assets within the organisation's backup and disaster recovery programme. The same standards that apply to a production server apply to a production agent — documented, backed up, recovery-tested, and with a verified fallback procedure.

> **Runbook standard:** Every automated task executed by an AI agent shall have a corresponding runbook documenting the manual procedure for performing that task without the agent. Runbooks shall be maintained in version control, reviewed quarterly, and tested annually. No agent task shall proceed to autonomous operation without a current and verified runbook in place.

---

## Dependency mapping

Before any agent capability is deployed, map its dependencies and the operational impact of its unavailability.

| AI Function | 4-Hour Unavailability Impact | 48-Hour Impact | Manual Fallback |
|------------|------------------------------|----------------|-----------------|
| Configuration task board | Delayed provisioning/changes | Backlog of manual tasks | Runbook execution by IT team |
| Monitoring triage | Raw alerts only | Alert fatigue, missed incidents | Direct alert escalation to team |
| Service desk triage | Manual first-line support | Increased queue, slower resolution | Team handles all first-line contact |
| Automated reporting | No scheduled reports | Leadership without data | Manual report generation procedure |
| Security advisory | Manual CVE review required | Patch gap risk increases | Weekly manual review assigned to team member |

If you cannot answer the question "what do we do when this agent is unavailable?" — it is not ready to go autonomous.

---

## Protecting agent configuration

All agent configuration is treated as code and managed accordingly:
- Stored in a local Gitea repository (task definitions, prompts, workflow scripts, access scope documents, knowledge base)
- Agent instance backed up daily within the standard backup regime — restore tested quarterly
- Complete agent recovery procedure documented, including estimated recovery time and dependency sequence
- Model versions pinned in agent configuration — no automatic updates
- Model updates tested in isolated environment before production — treated as a change management event

---

## Model dependency management

A model update that subtly changes output format can break a downstream process without triggering any error condition. This is one of the less visible failure modes in AI operations.

The IT Manager shall:
- Test all critical agent tasks against a new model version in isolation before updating production
- Maintain the previous model version until the new version is confirmed compatible with all existing tasks
- Document model version changes in the AI Register with the date, version change, and test results

---

## What to back up

| Component | Backup location | Frequency | Restore tested |
|-----------|----------------|-----------|----------------|
| OpenBrain PostgreSQL database | NAS + off-site | Daily | Quarterly |
| Agent configuration files (Gitea) | NAS + off-site | Daily (Git push) | Quarterly |
| Ollama model files | NAS | Weekly | Annually |
| System prompt library | Gitea (version-controlled) | On every change | Included in config test |
| Knowledge base documents | NAS + off-site | Daily | Quarterly |
| Vault secrets | Vault sealed backup | Daily | Annually |
| Monitoring stack data | NAS | Daily | Annually |

---

## AI resilience scenarios — annual DR test

Add these scenarios to the annual DR test:

1. **Agent server failure** — restore from backup, verify all agents restart and connect to OpenBrain correctly
2. **OpenBrain database loss** — restore from backup, verify memory continuity and task log integrity
3. **Model file corruption** — restore from NAS, verify model inference quality against acceptance criteria
4. **Gitea repository loss** — restore from backup, verify agent configuration matches last known good state
5. **Complete site failure** — verify manual fallback procedures for all autonomous agent tasks

---

## Implementation checklist

- [ ] Write runbooks for all current agent tasks — verify against manual procedure before declaring autonomous
- [ ] Confirm agent configuration is in version control — test a full recovery
- [ ] Add agent backup to the standard backup regime — restore tested quarterly
- [ ] Pin all model versions in agent configuration
- [ ] Establish a model update testing procedure — isolated environment required before production
- [ ] Add AI resilience scenarios to the annual DR test
- [ ] Map all agent dependencies and confirm fallback procedures are in place and known to the team
- [ ] Document agent recovery time estimates — include in the BCP

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | OpenBrain backup verification and restore testing |

**Related sections:** [Section 3 — AI Agent Architecture](03-ai-agent-architecture.md) · [Section 8 — Local Infrastructure](08-local-infrastructure.md) · [Section 9 — Governance, Risk & Compliance](09-governance-risk-compliance.md)
