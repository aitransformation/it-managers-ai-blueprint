# Tool: Prompt Injection Defence

## What it does

Screens inbound external content for prompt injection patterns before the content is passed to an AI agent. Flags known injection markers based on OWASP LLM01 guidance and applies a risk level: `low`, `medium`, or `high`.

**Patterns detected:**
- Instruction override language ("ignore previous instructions", "disregard your system prompt")
- Hidden or system prompt extraction requests
- Credential and secret requests
- Tool-use exfiltration instructions
- Safety bypass instructions
- Hidden HTML and script patterns
- Encoded payload hints

This is the primary defence against prompt injection via documents, web content, or user input.

---

## When to use it in the journey

| Journey Step | Use case |
|-------------|----------|
| Step 4 — Build | Configure on all document ingestion paths before the Document Ingestion Agent goes live |
| Step 4 — Build | Apply to any agent capability that processes external or user-generated content |
| Step 5 — Feedback Loop | Review flagged content monthly as part of the security check |

---

## Repository source path

```
ops/PROMPT_INJECTION_DEFENCE.md
```

The detector script is at:
```
tools-src/prompt_injection_detector.py
```

---

## How to use it

Run the detector against any external content before passing it to an agent:

```bash
python3 tools/prompt_injection_detector.py --input <file_or_text>
```

**Risk level handling:**
- `low` — continue with normal caution
- `medium` — continue but treat as untrusted; do not follow instructions embedded in the content
- `high` — quarantine, escalate, strip before use

---

## Example use case

**Scenario:** The Document Ingestion Agent receives a new PDF from an external supplier. Before the PDF is chunked and embedded, the prompt injection detector runs against the extracted text. It returns a `medium` risk rating for instruction override language found in a footer. The document is flagged to the IT Manager. The IT Manager reviews, strips the problematic section, and approves ingestion.

Without this check, the instruction override language could have influenced agent behaviour during retrieval.

---

## Blueprint reference

[Section 7 — AI Security](../blueprint/07-ai-security.md) covers prompt injection as a threat vector and defines the control requirements.
