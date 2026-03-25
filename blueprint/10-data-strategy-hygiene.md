# Section 10: Data Strategy & Hygiene

> **Journey Step:** Step 2 — Foundations

---

## Why data quality is not optional

The quality of AI outputs is directly and unavoidably dependent on the quality of the data from which they are derived. Data strategy is not a separate workstream from AI deployment. It is a prerequisite for it.

An agent querying a knowledge base full of outdated, inconsistent, or incomplete data will produce unreliable outputs. The problem is not the agent. The problem is the data. Fix the data first.

---

## Data quality assessment

For each data asset connected to planned AI processing, assess and document quality against five dimensions.

| Dimension | Assessment Question |
|-----------|-------------------|
| **Completeness** | Are all required fields populated? What is the rate of missing values? |
| **Accuracy** | Does the data correctly represent the real-world entities and events it describes? |
| **Consistency** | Is the same entity represented consistently across systems? |
| **Timeliness** | How current is the data? Does the AI task require real-time or periodic data? |
| **Accessibility** | Can the agent access the data in the format required, without manual transformation? |

Any data asset materially deficient on any dimension shall be subject to a data improvement plan before AI processing is enabled. The named data owner is accountable for the improvement plan.

---

## Schema standardisation

Schema consistency deserves specific attention: the degree to which data describing the same entities uses consistent field names, formats, types, and value ranges across systems.

AI agents processing data from multiple systems will produce unreliable outputs where the same concept is represented differently across sources. A customer is "cust_id" in one system and "customer_number" in another. A date is ISO format in one system and DD/MM/YYYY in another. The agent cannot bridge this gap reliably.

The IT Manager shall:
1. Identify all cases where AI processing draws from multiple systems representing the same entities
2. Assess the degree of schema divergence
3. Produce a standardisation plan

Where standardisation at the source is not feasible, implement a transformation layer that normalises the schema before the data reaches the agent.

---

## Data pipeline visibility

Maintain current documentation of all data pipelines feeding AI systems. For each pipeline, capture:
- Source system
- Destination
- Transformation steps applied
- Frequency
- Data classification
- The owner responsible for its reliability

Pipeline documentation shall be reviewed and verified quarterly as part of the data register review.

---

## Local RAG architecture

Retrieval-Augmented Generation (RAG) is the mechanism by which local AI agents are connected to organisational knowledge bases — enabling outputs grounded in the organisation's own data rather than the model's training data alone.

A local RAG implementation requires three self-hosted components:

**1. Document store** — the organisation's knowledge base  
Policies, procedures, technical documentation, historical records. All subject to the data sovereignty standard.

**2. Vector database** — semantic search capability  
ChromaDB or Weaviate, self-hosted. The vector database holds embeddings for all knowledge base content and enables the agent to retrieve relevant chunks by meaning rather than keyword.

**3. Embedding model** — converts documents and queries to vector representations  
`nomic-embed-text` or `mxbai-embed-large` via Ollama. All embeddings generated locally — no content is sent to an external embedding API.

The quality of the knowledge base directly determines the quality of agent outputs. A RAG architecture is only as good as what you put in it.

---

## Building the initial knowledge base

Prioritise the content that your agents will actually use. Start with:

1. IT policies and SOPs (already created as part of Section 9)
2. Common service desk resolution guides — top ten request types with verified procedures
3. Business outcome register (from Section 1)
4. Asset register — current systems, owners, and classifications
5. Network diagram and infrastructure documentation

Do not ingest everything at once. Start small, verify quality, then expand. Inaccurate knowledge base content is worse than no knowledge base content — the agent will act on it.

---

## Implementation checklist

- [ ] Complete data quality assessments for all data assets connected to planned AI processing
- [ ] Assign named data owners for all critical data assets — confirm in the data register
- [ ] Build data improvement plans for any asset with a material quality deficiency
- [ ] Identify all schema inconsistencies across data sources used in AI processing — produce standardisation plan
- [ ] Document all data pipelines feeding AI systems — review quarterly
- [ ] Deploy local RAG infrastructure — ChromaDB or Weaviate, self-hosted
- [ ] Build the initial knowledge base: IT policies, SOPs, top ten service desk resolution guides
- [ ] Establish a knowledge base document review cycle — ownership and review dates assigned
- [ ] Integrate data quality checks into the agent monitoring task board

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/estate-discovery.md`](../tools/estate-discovery.md) | Map data sources, ownership, and quality gaps |
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | OpenBrain is the RAG store — see Section 4 for the full schema |

**Related sections:** [Section 2 — Data Sovereignty](02-data-sovereignty.md) · [Section 4 — OpenBrain Memory](04-open-brain-memory.md) · [Section 5 — Document Ingestion](05-document-ingestion.md)
