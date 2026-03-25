# Section 2: Data Sovereignty — The Non-Negotiable Foundation

> **Journey Step:** Step 1 — Audit / Step 2 — Foundations

---

## Why this matters now

Data sovereignty has moved from a compliance consideration to a core operational standard. The proliferation of cloud services, AI platforms, and third-party integrations has resulted in organisational data being distributed across systems and jurisdictions that IT Managers may have limited visibility into and no meaningful control over.

The IT Manager is responsible for establishing and maintaining a clear, verified understanding of where every piece of organisational data resides, who can access it, under what legal framework it is held, and what controls protect it.

---

## The data classification framework

All organisational data shall be assigned to one of four classification tiers. Classification governs where data may be stored, how it may be transmitted, and whether and how it may be processed by AI systems.

| Classification | Definition | Permitted Location | AI Processing Rule |
|---------------|-----------|-------------------|--------------------|
| **Restricted** | Personal data, financial records, legal documents, credentials, IP | Local infrastructure only. No cloud storage or transmission. | Local models only. No external API under any circumstances. |
| **Confidential** | Operational data, commercially sensitive information, strategic plans | Local infrastructure. Cloud only with verified DPA and confirmed data residency. | Local models strongly preferred. External API only with anonymisation, verified DPA, and documented approval. |
| **Internal** | General operational data not approved for external disclosure | Local or approved cloud with access controls. | Local or external API permitted with standard governance. |
| **Public** | Information approved for external publication | Any location. | Any model, local or cloud. |

Classification is the responsibility of the named **data owner** — the individual accountable for the accuracy and appropriate handling of a given data asset. The IT Manager is responsible for ensuring classifications are made, documented, and that technical controls reflect classification requirements.

---

## The data register

The data register is the master record of all organisational data assets. It is maintained by the IT Manager and reviewed quarterly with data owners and a senior leadership sponsor.

For each entry, the register captures:
- The data asset name and description
- Its classification tier
- The named data owner
- The system or systems in which it resides
- The physical location of storage, including jurisdiction
- Access controls in place — who can read, write, and delete
- Applicable regulatory obligations (GDPR, sector-specific, contractual)
- Whether it is currently processed by any AI system, and which one
- Date of last classification review

> **Warning:** The data map produced during outcome mapping (Section 1, Step 4) is the primary input to the data register. These two documents must be kept in synchrony. A data element present in the outcome maps but absent from the data register is an unmanaged risk.

---

## Local-first data architecture

The local-first principle requires all data classified as Restricted or Confidential to be stored exclusively on infrastructure under the direct operational control of the organisation.

The default answer to "where shall this data be stored?" is always **local**. The burden of proof is on moving data off local infrastructure, not on keeping it there.

Any proposal to store Restricted or Confidential data in a third-party system shall be supported by:
1. A documented risk assessment
2. A verified Data Processing Agreement (DPA)
3. Explicit approval from both the IT Manager and a senior leadership sponsor

---

## The local AI stack

The AI era has changed the data sovereignty calculus. When an organisation connects to a cloud-based AI service, the default behaviour is to receive, process, and in many cases retain the data submitted. For Restricted and Confidential data, this is not a manageable risk — it is a standard violation.

The technology for a fully local AI stack is available and deployable by an SME IT Manager in 2026:

| Component | Local Standard | Verified Option (March 2026) |
|-----------|---------------|------------------------------|
| AI Agent Platform | Self-hosted, on-premises | OpenClaw / Clawdbot |
| Language Model — General | Locally-hosted via Ollama | Llama 3 70B or Mistral Large |
| Language Model — Lightweight | Locally-hosted via Ollama | Phi-3 Mini or Llama 3 8B |
| Language Model — Code | Local code-specialist model | DeepSeek Coder or CodeLlama via Ollama |
| Vector / RAG Store | Self-hosted vector database | OpenBrain / PostgreSQL + pgvector (self-hosted) |
| Embedding Model | Local embedding model | nomic-embed-text or mxbai-embed-large via Ollama |
| Data Storage | On-premises or self-hosted | Local database / NAS / self-hosted object store |
| Prompt Library | Version-controlled, local | Self-hosted Gitea or equivalent |
| Monitoring | On-premises stack | Grafana + Prometheus (self-hosted) |
| External API (exception only) | Isolated key, spend-capped | Anthropic API — Internal/Public data only, documented exception required |

> **AI Data Processing Standard:** No data classified as Restricted shall be transmitted to any external AI service under any circumstances. No data classified as Confidential shall be transmitted to any external AI service without a verified DPA, explicit data residency confirmation, anonymisation where feasible, and documented approval from the IT Manager and senior sponsor.

---

## Access control — principle of least privilege

Data sovereignty is not solely about where data is stored. It is equally about who and what can access it.

Every user, system, and AI agent receives access only to the data required to fulfil its defined function.

For AI agents specifically:
- Define the data access scope for each agent capability **before deployment**, in writing
- Implement access controls technically — do not rely on configuration or prompting to restrict agent access
- Audit agent data access quarterly — log what was accessed and compare against defined scope
- Revoke and redefine access when agent capabilities are changed or extended

---

## Implementation checklist

- [ ] Build the data register — complete an entry for every data asset identified in outcome mapping
- [ ] Confirm classification with the named data owner for every data asset
- [ ] Identify all data in third-party systems — verify DPAs are current and data residency confirmed
- [ ] Audit all current AI deployments against the classification framework — remediate non-compliant processing
- [ ] Deploy local model infrastructure — Ollama on local hardware with appropriate model tiers
- [ ] Migrate all Restricted and Confidential AI processing to local models
- [ ] Define and technically enforce access scopes for all agent deployments
- [ ] Update the Acceptable Use Policy — include AI data processing rules, brief all staff
- [ ] Schedule quarterly data register review — IT Manager, data owners, senior sponsor
- [ ] Document all approved exceptions to the local-first standard with full risk assessment and sign-off

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/estate-discovery.md`](../tools/estate-discovery.md) | Map data assets and their locations during the initial audit |
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | Store and retrieve the data register in Open Brain |

**Related sections:** [Section 2b — Data Access Governance](02b-data-access-governance.md) · [Section 10 — Data Strategy & Hygiene](10-data-strategy-hygiene.md)
