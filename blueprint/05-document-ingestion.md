# Section 5: Document Ingestion Agent

> **Journey Step:** Step 4 — Build

---

## Purpose

The organisation holds its purpose, processes, and operating knowledge in documents. Policy files, SOPs, contracts, meeting notes, board papers, product documentation, customer records, and operational guides are scattered across shared drives, email archives, and local file stores.

For AI agents to serve the organisation well, they must be able to reason over this material. For that to happen, it must be ingested, classified, chunked, embedded, and stored in OpenBrain where agents can retrieve it semantically.

The Document Ingestion Agent handles this process. It watches defined source locations, processes incoming documents, classifies them, generates local embeddings using the locally-hosted embedding model, and writes the resulting vectors and structured metadata to OpenBrain.

**Every step in this pipeline runs locally. No document content is transmitted to any external service regardless of the document's classification tier.** Company documents, operating procedures, customer records, and business outcome descriptions are among the most sensitive assets the organisation holds. Local processing is not a preference here. It is a hard requirement.

---

## What the ingestion agent processes

| Source Type | Format | Schedule | Notes |
|-------------|--------|----------|-------|
| Shared folder / NAS | PDF, DOCX, TXT, MD | Every 15 minutes | Primary source for policies, SOPs, reports |
| Email attachments | PDF, DOCX, XLSX | Hourly | Filtered by sender domain and subject rules |
| Structured exports | CSV, JSON, XLSX | On demand / scheduled | Financial data, asset registers, system exports |
| Web pages and internal wikis | HTML | Daily | Internal Gitea wiki, ISPConfig-hosted internal sites |

---

## Ingestion pipeline

```
Source document
    │
    ▼
[1] File watcher / email listener detects new document
    │
    ▼
[2] Format extraction
    PDF    → text via pdfminer.six (local)
    DOCX   → text via python-docx (local)
    XLSX/CSV → structured text via pandas (local)
    HTML   → clean text via trafilatura (local)
    │
    ▼
[3] Classification check
    Agent queries the data register for the source path
    Assigns classification tier from the register entry
    If source path is unregistered → document held in quarantine
    IT Manager notified for classification decision
    │
    ▼
[4] Chunking
    Documents split into chunks of 512 tokens with 64-token overlap
    Chunk boundaries respect paragraph and heading structure
    Each chunk tagged with: source file, page/section, document date,
    classification tier, document type
    │
    ▼
[5] Embedding (LOCAL ONLY)
    nomic-embed-text via Ollama generates 768-dimension embeddings
    No content leaves the agent server at this stage
    │
    ▼
[6] Storage in OpenBrain
    Chunks and embeddings written to the memories table
    Metadata written to the documents table
    Duplicate detection: if a document with identical hash already exists,
    only the updated chunks are reprocessed
    │
    ▼
[7] Index update
    script_library semantic index refreshed if the document is a procedure or SOP type
    governance_register updated if the document is a policy
```

---

## OpenBrain documents table

```sql
CREATE TABLE documents (
  id               SERIAL PRIMARY KEY,
  file_name        VARCHAR(500) NOT NULL,
  file_path        VARCHAR(1000),
  source_type      VARCHAR(50),           -- 'nas', 'email', 'export', 'wiki'
  document_type    VARCHAR(100),          -- 'policy', 'sop', 'contract', 'report', 'procedure', ...
  classification   VARCHAR(20) NOT NULL,
  file_hash        VARCHAR(64),           -- SHA-256 for duplicate detection
  chunk_count      INTEGER,
  ingested_at      TIMESTAMP NOT NULL DEFAULT NOW(),
  last_updated     TIMESTAMP,
  ingestion_status VARCHAR(20),           -- 'complete', 'quarantine', 'failed', 'reprocessing'
  notes            TEXT
);
```

---

## Document quarantine

Any document arriving from an unregistered source path is placed in quarantine. The Ingestion Agent:
1. Writes the file metadata to the documents table with `ingestion_status = 'quarantine'`
2. Sends an alert to the IT Manager via the Head Agent

The IT Manager:
1. Reviews the document
2. Assigns a classification and document type
3. Updates the data register
4. Instructs the Ingestion Agent to process it

**Documents in quarantine are never embedded or made available to other agents until the IT Manager has approved their classification.**

---

## Keeping the knowledge base current

Ingestion is not a one-time exercise. Documents change. When a document is re-ingested, the hash is compared to the stored value. If the document has changed:
1. All previous chunks for that document are marked stale
2. The document is re-chunked and re-embedded
3. Stale entries are removed
4. The document table record is updated with the new ingestion timestamp

The IT Manager reviews the ingestion log monthly as part of the governance review, checking for documents in quarantine, failed ingestion jobs, and any documents that have not been updated in an unexpectedly long time.

---

## Ingestion agent specification

| Attribute | Value |
|-----------|-------|
| Primary model | Lightweight local (Phi-3 Mini) for classification and routing |
| Embedding model | nomic-embed-text via Ollama — fixed local, no model choice |
| Tool access | NAS/shared folder (read), email listener (read), OpenBrain (write), IT Manager notification |
| Data scope | All classification tiers — local processing only, no frontier model access |
| Deployment stage | Week 5 (alongside Head Agent) |

---

## Implementation checklist

- [ ] Define source paths for the ingestion agent — all shared folders, email accounts, export locations
- [ ] Register all source paths in the data register with classification assignments before the agent starts
- [ ] Deploy the ingestion pipeline — format extraction, chunking, embedding, storage
- [ ] Test quarantine: introduce a document from an unregistered path and verify it is held
- [ ] Test duplicate detection: re-ingest an updated document and verify stale chunks are replaced
- [ ] Seed the knowledge base with policies, SOPs, and top-ten service desk resolution guides
- [ ] Set the ingestion schedule — 15-minute interval for NAS, hourly for email
- [ ] Include ingestion log review in the monthly governance review agenda

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/prompt-injection-defence.md`](../tools/prompt-injection-defence.md) | Screen all inbound documents before ingestion |
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | Query and verify ingested knowledge base content |

**Related sections:** [Section 4 — OpenBrain Memory](04-open-brain-memory.md) · [Section 2 — Data Sovereignty](02-data-sovereignty.md) · [Section 10 — Data Strategy & Hygiene](10-data-strategy-hygiene.md)
