# Tool: Security Skill Checker

## What it does

Performs a pre-install and pre-run security review for every third-party skill or agent tool. Scans for risky patterns and returns a `PASS`, `WARN`, or `FAIL` decision with findings and required mitigations.

**Checks performed:**
- Prompt injection patterns in SKILL.md content (instructions to ignore safeguards, override system policy, exfiltrate secrets, hidden role redefinition)
- Destructive command patterns (`rm -rf`, mass delete, blind `chmod`/`chown`, unsafe `curl | bash`)
- Credential handling issues (hardcoded tokens, plaintext secrets, external posting of sensitive data)
- Privilege escalation signals (unnecessary root, sudo abuse, persistence changes without guardrails)
- External messaging or data exfiltration without user approval

---

## When to use it in the journey

| Journey Step | Use case |
|-------------|----------|
| Step 4 — Build | Run before installing any skill from ClawHub or a third-party source |
| Step 4 — Build | Run before deploying any agent-built tool that will have elevated permissions |
| Step 5 — Feedback Loop | Re-run quarterly for all third-party skills when reviewing the agent stack |
| Any step | Any time the vendor evaluation scorecard is applied to an agent tool |

---

## Repository skill path

```
skills/security-skill-checker/SKILL.md
```

The checker script is at:
```
skills/security-skill-checker/scripts/check_skills.py
```

---

## How to use it

Single skill:
```bash
python3 skills/security-skill-checker/scripts/check_skills.py --path <skill-dir>
```

Batch check a directory:
```bash
python3 skills/security-skill-checker/scripts/check_skills.py --path <skills-root> --recursive
```

Record the result in:
```
ops/SKILL_SECURITY_REGISTRY.json
```

**Decision policy:**
- `PASS` — no critical findings; proceed
- `WARN` — non-critical issues; require mitigation notes before use
- `FAIL` — critical risk; do not install or use

---

## Example use case

**Scenario:** The IT Manager wants to install a monitoring skill from ClawHub that integrates with a third-party security feed. Before installation, the security skill checker runs against the skill directory. It returns `WARN` — the skill makes outbound HTTPS calls but the destination is not clearly documented. The IT Manager reviews the skill's references, confirms the destination is the approved feed, documents the mitigation, and proceeds with installation.

---

## Blueprint reference

[Section 7 — AI Security](../blueprint/07-ai-security.md) defines the security review requirement for agent tools. [Section 13 — Vendor & Tool Evaluation](../blueprint/13-vendor-tool-evaluation.md) applies the vendor scorecard.
