---
name: anti-ai-writing
description: Detect AI-sounding writing patterns and rewrite drafts to avoid them. Use when asked to humanize text, make writing sound less AI-generated, score a draft for AI tells, remove robotic/corporate phrasing, or produce content that avoids common Wikipedia-style signs of AI writing while staying specific, credible, and human.
---

# Anti-AI Writing

Use this skill to do two things well:

1. **Detect** drafts that sound synthetic, over-structured, vague, or LLM-shaped.
2. **Rewrite** them so they sound more human without becoming sloppy, gimmicky, or fake-casual.

## Default goal

Aim for writing that is:
- specific
- grounded
- readable aloud
- willing to sound like a person
- not stuffed with filler, hype, or fake polish

Do **not** overcorrect into deliberate messiness, fake typos, or forced quirk unless the user explicitly asks.

## Workflow

### 1) Detect the problem

Scan for the common tells in `references/patterns.md`.

Look especially for:
- significance inflation
- vague attribution
- generic conclusions
- AI-favorite vocabulary
- filler transitions
- overuse of em dashes / bold / list structures
- chatbot phrases and sycophancy
- uniform sentence rhythm
- abstract claims without concrete detail

If helpful, summarize the result in this format:

- **Risk level:** low / medium / high
- **Main issues:** 3-6 bullets
- **Examples:** short quoted snippets
- **Fix direction:** what to change first

### 2) Choose the mode

#### Detector mode
Use when the user wants analysis, scoring, or diagnosis.

Output:
- short verdict
- key flagged traits
- evidence snippets
- practical rewrite advice

#### Editor mode
Use when the user wants a rewrite.

Process:
- keep the meaning
- remove inflated or robotic phrasing
- replace abstractions with specifics where available
- tighten rhythm
- remove filler and templated transitions
- preserve the intended tone

#### Writer mode
Use when the user wants fresh copy that avoids AI tells from the start.

Before drafting:
- choose a clear point of view
- prefer concrete nouns and verbs
- avoid generic intro/outro filler
- end with a specific point, not a vague flourish

## House style rules

Read `references/style-rules.md` when the user has a clear voice, audience, or brand context.

If no other style is specified, default to:
- natural, not performatively casual
- no corporate sludge
- no empty hype
- no “Great question” style padding
- no press-release grandiosity

## Rewrite rules

### Always do
- prefer plain verbs over inflated ones
- cut throat-clearing
- name specifics if they exist
- vary sentence length naturally
- allow opinion when appropriate
- make conclusions concrete

### Avoid by default
- strategic typos
- fake tangents
- forced slang
- random emoji
- trying too hard to sound “human”

## Output patterns

### If asked to assess text
Return:
- one-line verdict
- top issues
- short examples
- optional revised paragraph

### If asked to rewrite text
Return:
- revised version first
- then a brief note on what changed

### If asked to draft from scratch
Return clean copy only, unless the user asks for commentary.

## References

- Read `references/patterns.md` for the anti-pattern checklist.
- Read `references/style-rules.md` for rewrite heuristics and tone guardrails.

## Final check

Before sending writing, ask:
- Does this say anything specific?
- Does it sound like a person with a point of view?
- Could any sentence be cut because it only sounds nice?
- Does the ending actually land, or just fade out politely?
