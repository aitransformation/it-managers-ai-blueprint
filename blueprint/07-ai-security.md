# Section 7: AI Security — Threats & Controls

> **Journey Step:** Step 2 — Foundations / Step 4 — Build

---

## AI-specific threats

AI systems introduce attack surfaces and failure modes that traditional security frameworks do not fully address. These threats must be understood and controlled before deployment, not after an incident.

---

### Prompt injection

Prompt injection is an attempt to manipulate an AI agent's behaviour by embedding malicious instructions within input data — for example, in a document the agent is asked to summarise, or in a user support request.

This applies to Markdown files, PDFs, copied prompts, websites, HTML content, imported repositories, and internal notes just as much as it applies to obvious hostile content. A `.md` file is not trusted because it is text. It is just another input source.

A successful prompt injection can cause the agent to:
- Ignore its instructions
- Exfiltrate data
- Take unintended actions
- Bypass access controls

**Controls:**
- Input sanitisation and validation before data is passed to the agent
- System prompt hardening — instructions that explicitly address and reject override attempts
- Constraint enforcement at the platform level, not prompt level alone
- Monitoring of agent outputs for anomalous behaviour patterns
- Principle of least privilege — limit the damage a compromised agent can do
- Treat all imported Markdown, copied text, websites, and repositories as untrusted until screened
- Never allow a model to auto-execute instructions simply because they appear in a project file

> **Prompt Injection Defence tool:** The workspace includes a prompt injection detector based on OWASP LLM01 guidance. Run it against all inbound external content before it reaches an agent. Run it against imported Markdown and repository content too. See [`tools/prompt-injection-defence.md`](../tools/prompt-injection-defence.md). Risk levels: `low` (continue with caution), `medium` (treat as untrusted, do not follow embedded instructions), `high` (quarantine, escalate, strip before use).

---

### Data leakage

AI agents processing organisational data can inadvertently expose sensitive information — through overly verbose outputs, inclusion of sensitive context in responses visible to unauthorised users, or transmission of data to external services where the agent has been connected without adequate scoping.

**Controls:**
- Output review before distribution for any capability handling Restricted or Confidential data
- Data classification enforcement at the access scope level — agents cannot access data they are not permitted to process
- Monitoring of agent outputs for classification-inappropriate content
- Prohibition of external API connections for agents handling Restricted or Confidential data
- Logging all data accessed by each agent invocation

---

### Agent privilege escalation

An agent that has been granted access to execute tasks may attempt — through model behaviour, prompt injection, or misconfiguration — to perform actions beyond its authorised scope. This is particularly dangerous in agents with system access, file write permissions, or network connectivity.

**Controls:**
- Technical enforcement of permission boundaries — not configuration or prompting alone
- Agents run under dedicated service accounts with the minimum required OS and network permissions
- All agent-initiated actions logged with the agent identity and the access scope document version in force
- Automated alerting when an agent attempts an action outside its defined scope
- Regular review of agent action logs against the access scope document

---

### Model manipulation and supply chain risk

Locally-hosted models are obtained from repositories that could in principle contain models that have been tampered with or that contain embedded behaviours not documented by the model provider.

**Controls:**
- Download models only from verified, reputable sources (Ollama official library, Hugging Face with verified publishers)
- Verify model checksums before deployment
- Test model behaviour in an isolated environment before connecting to production data or systems
- Monitor for model updates that change behaviour in unexpected ways

---

## AI security governance

Every AI deployment shall include:
- A defined permission model that is technically enforced
- Interaction monitoring with anomaly alerting
- Input filtering for all data passed to agents from external or user-generated sources
- A security review of every agent-built tool before deployment
- Inclusion of AI-specific threat vectors in the organisation's annual security assessment

---

## Integration with the wider security programme

AI security is not a separate discipline — it is an extension of the existing security programme.

| Area | AI-specific addition |
|------|---------------------|
| Penetration testing | Add AI infrastructure to scope at next scheduled test |
| Annual security assessment | Add prompt injection, data leakage, privilege escalation as assessed vectors |
| Incident response | Add AI-specific incident response procedure (see Section 9) |
| Vulnerability management | Security Agent monitors CVE feeds for AI infrastructure components |
| Access review | Include agent access scope documents in periodic access review |

---

## Implementation checklist

- [ ] Implement input sanitisation for all data sources connected to AI agents
- [ ] Deploy the prompt injection detector — run against all external content before ingest
- [ ] Configure OpenClaw guardrails — define and enforce hard constraints on agent behaviour
- [ ] Run dedicated service accounts for all agents — minimum required OS and network permissions
- [ ] Enable and review agent action logs — configure alerting for out-of-scope action attempts
- [ ] Verify model checksums on first install and on each update
- [ ] Add AI-specific threat vectors to the annual security assessment
- [ ] Add AI infrastructure to the penetration testing scope at next scheduled test
- [ ] Document the AI security controls in the AI Register for each deployment

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/prompt-injection-defence.md`](../tools/prompt-injection-defence.md) | Screen inbound content for injection attempts |
| [`tools/security-skill-checker.md`](../tools/security-skill-checker.md) | Security screening for agent tools and skills before use |

**Related sections:** [Section 2 — Data Sovereignty](02-data-sovereignty.md) · [Section 3 — AI Agent Architecture](03-ai-agent-architecture.md) · [Section 9 — Governance, Risk & Compliance](09-governance-risk-compliance.md)
