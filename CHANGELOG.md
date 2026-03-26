# Changelog

All notable changes to the IT Manager's AI Blueprint are documented here.

## Release pattern

- `main` — current stable edition
- GitHub releases tagged as `vYYYY.MM` (e.g. `v2026.03`)
- One release per month, aligned to the monthly review cadence

Editions older than three months should be reviewed against the current version before acting on them.

---

## v2026.03 — 2026-03-26

### Added

- `journey/00-setup.md` — New Step 0: stand up the agent safely before anything else. Covers Path A (minimum viable cloud setup) and Path B (full local stack), with all six safety rules: local-first, OpenBrain context retrieval, prompt injection protection, anti-AI quality gate, trust boundaries, and local tool build preference.
- `CHANGELOG.md` — this file

### Changed

- `README.md` — Full rewrite. Hero section opens with the real IT Manager pressure (founder expects AI, guidance is thin). Journey table now shows all six steps starting from Step 0. Clear "start here" direction to `journey/00-setup.md`.
- `AGENT.md` — Updated to reflect 6-step journey. Step 0 added. Applying-the-blueprint sequence now includes a Step 0 confirmation check before anything else.
- `journey/README.md` — Simplified to an index that directs readers to the main README as the primary entry point.
- `journey/01-audit.md` — Added Step 0 as a prerequisite. Added note that the agent can assist with audit work. Added previous/next navigation.
- `journey/02-foundations.md` — Removed agent setup section (moved to Step 0). Renumbered remaining steps. Updated prerequisites. Added previous/next navigation.
- `journey/03-skill-up.md` — Major expansion. Added seven-part structure: what GenAI is, safe use at work, why models differ, what agents are, types of agents and deployment models, how to choose, how to teach. Added deployment model comparison table covering consumer tools, M365 Copilot, coding tools, local desktop tools, server-based tools, and full agent stack. Added previous/next navigation.
- `journey/04-build.md` — Added note that Step 0 working agent stays in place through the build. Added previous/next navigation.
- `journey/05-feedback-loop.md` — Added previous/next navigation.

---

## v2026.02 — prior release

Initial open source edition. Five-step journey (Audit, Foundations, Skill Up, Build, Feedback Loop). See git history for full content at this point.
