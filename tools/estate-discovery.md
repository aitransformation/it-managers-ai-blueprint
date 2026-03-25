# Tool: Estate Discovery

## What it does

Maps the current IT estate: systems, data stores, integrations, identities, devices, key vendors, and ownership. Surfaces shadow IT, duplication, unclear ownership, and brittle dependencies. Produces a clear picture of what exists and where the estate is messy.

This tool drives Step 1 of the journey. It produces the inputs that everything else in the blueprint depends on.

---

## When to use it in the journey

| Journey Step | Use case |
|-------------|----------|
| Step 1 — Audit | Primary tool for mapping the estate against business outcomes |
| Step 1 — Audit | Shadow system discovery — find the undocumented but operationally critical |
| Step 2 — Foundations | Identify which systems need DPA verification before connecting to AI |
| Step 4 — Build | Map system integrations as you wire up agent capabilities |
| Step 5 — Feedback Loop | Annual blueprint reset — re-map the estate against current outcomes |

---

## Workspace skill path

```
/home/nick-butcher/.openclaw/workspace/skills/estate-discovery/SKILL.md
```

References:
```
/home/nick-butcher/.openclaw/workspace/skills/estate-discovery/references/discovery-checklist.md
```

---

## What good estate discovery produces

- Business-critical outcomes mapped (from Section 1 of the blueprint)
- Major business processes documented
- Systems supporting those processes — including shadow systems
- Data sources and stores — with owners and classification
- Ownership and support gaps — who is responsible for what
- Simplification opportunities — the smallest useful improvements

---

## How to use it

Ask an AI agent loaded with this skill to:

1. **Define scope** — what business areas or outcomes are being mapped?
2. **Inventory** — systems, data stores, integrations, identities, devices, key vendors
3. **Map to outcomes** — each system traced to a business outcome using the four core drivers
4. **Flag problems** — duplication, unclear ownership, shadow IT, brittle dependencies
5. **Recommend simplification** — the smallest useful moves that reduce complexity

---

## Example use case

**Scenario:** The IT Manager is beginning Step 1 of the journey. They ask an AI agent to help map the finance function's IT estate. The estate discovery skill guides the session: what outcomes does finance need to deliver, what processes serve those outcomes, what systems support those processes, and what data flows through them?

The session surfaces two shadow systems: a spreadsheet-based approval workflow that is operationally critical but undocumented, and a personal OneDrive folder used to share financial data externally. Both go into the asset register. Both are assessed for data sovereignty risk. The spreadsheet becomes a candidate for replacement. The OneDrive usage triggers an immediate data sovereignty remediation action.

---

## Blueprint reference

[Section 1 — Business Outcome Mapping](../blueprint/01-outcome-mapping.md) defines the full 8-step methodology this tool supports. [Section 2 — Data Sovereignty](../blueprint/02-data-sovereignty.md) describes how the data map produced here feeds the data register.
