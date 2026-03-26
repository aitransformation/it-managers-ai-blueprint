# Step 3: Skill Up

**Understand what you're deploying. Then teach it to your team.**

Before the agents go live, you and your team need to understand what they actually are, how they work, where they fail, and how to use them safely. This step builds that foundation.

This is not education for its own sake. Every section here connects directly to decisions you will make in Step 4 (Build) and to risks you will manage every month in Step 5 (Feedback Loop). If you skip this step and deploy anyway, the first time something goes wrong you will not know what you're looking at.

---

## What this step covers

- What GenAI actually is, in practical terms
- How to use it safely at work
- Why models differ and what that means for decision-making
- What agents are and how they behave
- The different types of agents and deployment models
- How to choose the right tools for your organisation
- How to teach this to your team

---

## Part 1: What GenAI actually is

### The honest explanation

A large language model (LLM) predicts the next most likely token — a word fragment — based on patterns in its training data. It is not thinking. It is not reasoning in the way humans reason. It is doing extremely sophisticated pattern completion at scale.

This matters because it explains every category of failure:

**Hallucination** — The model produces something that sounds correct but is not. This happens because it is completing a pattern, not retrieving a verified fact. The model has no mechanism to distinguish "I know this" from "I am plausibly completing this sentence." Both arrive in the same confident tone.

**Confidence without accuracy** — There is no "I'm guessing" mode. A model is equally confident when it is right and when it is fabricating. You cannot tell from tone or fluency whether an output is accurate.

**Training cutoff drift** — The model's knowledge stops at its training cutoff date. Anything after that is absent or guessed from pre-cutoff patterns. A model trained to early 2024 does not know what happened in late 2024.

**Prompt sensitivity** — Small changes in how you phrase a question can produce substantially different outputs. This is a direct consequence of the statistical prediction mechanism. It is why structured prompting matters and why copying prompts from the internet and running them unchanged is not a strategy.

### The difference between a model and a product

A **foundation model** is the trained set of weights — GPT-4, Claude 3.5, Llama 3, Gemini. This is what the capability actually is.

A **product** wraps a foundation model in an interface, often with a system prompt and added safeguards. ChatGPT is a product built on GPT-4. Claude.ai is a product built on Claude models. The product shapes the experience. The foundation model determines what the product can and cannot do.

A **fine-tuned model** is a foundation model further trained on a specific dataset. Better on targeted tasks, weaker on general ones.

A **RAG system** (Retrieval-Augmented Generation) connects a model to an external knowledge base. When you ask a question, relevant documents are retrieved and included in the prompt. The model answers from that context. This is the pattern OpenBrain uses. It reduces hallucination on known information because the model has the actual source in front of it — but it does not eliminate hallucination, and it depends entirely on the quality of what's in the knowledge base.

### Why "just ask it" is not a strategy

The model will produce an answer. The answer may be correct, partially correct, or entirely wrong — and it will arrive with equal confidence in all three cases. Without a structured approach to prompting and verification, you cannot know which category you're in.

A structured approach means: clear task, specific context, defined output format, and explicit acceptance criteria. Then verify the output against an independent source before acting on it.

This is the minimum requirement for professional use. It is not optional extra work.

---

## Part 2: How to use it safely at work

### The data rule, stated simply

Before you paste anything into an AI tool, ask: would I be comfortable sending this to a stranger on the internet?

If the answer is no, it stays local or stays off AI altogether.

More formally: classify the data first (Restricted / Confidential / Internal / Public), then check which tools are permitted for that classification in your organisation's AUP addendum.

Restricted data never leaves your organisation. Full stop.

### The verification rule

AI output is draft material. Never act on it without checking it.

What checking looks like depends on the output type:

| Output type | Verification approach |
|-------------|----------------------|
| Factual claims | Cross-reference two independent sources |
| Code | Run in a test environment; review logic before production |
| Documents | Read for accuracy, specifics, and tone before distributing |
| Data analysis | Verify methodology; spot-check the calculations |
| Recommendations | Apply your own professional judgement; do not outsource the decision |

The model does not know your environment, your constraints, or your history. You do. Apply that knowledge before acting.

### The five rules for your team

These cover most of what goes wrong:

1. **Don't paste in what you wouldn't email out.** Customer data, financial records, passwords, internal strategy documents — none of this goes into a public AI tool.

2. **Don't forward AI output without reading it.** If it has an error and you signed off on it, that's on you.

3. **Don't assume it's current.** If recency matters, verify separately.

4. **Report anything unusual.** If the tool says something alarming, unexpected, or asks for information it shouldn't need, tell IT.

5. **You are accountable for what you act on.** The AI tool is not.

---

## Part 3: Why models differ

You do not need to understand the technical details. You need to understand the practical implications.

### Scale and capability

Larger models (more parameters) generally produce better outputs on complex tasks, but they are slower and more expensive to run. A Llama 3 8B model runs on a capable laptop. A Llama 3 70B model needs a server with substantial RAM. GPT-4 and Claude Opus run in data centres you do not control.

The trade-off is capability versus cost and sovereignty.

### Context window

The context window is how much text the model can process at once — your question, background documents, and conversation history together. Larger windows let you include more material. Smaller ones require more careful task structuring.

This directly affects agent design. Agents with larger context windows can hold more operational history. Agents with smaller windows need structured memory management (which is part of why OpenBrain exists).

### Training data and cutoff

Every model has a training cutoff date. It also reflects the biases and gaps of whatever data it was trained on. A model trained primarily on English-language web content will be weaker on specialist technical domains, non-English content, and anything that emerged after its cutoff.

Understanding this helps you predict where a model will struggle and what verification is most important.

### Reasoning capability

Some models are explicitly trained for extended reasoning — they work through a problem step by step before producing a final answer. These are slower and more expensive, but substantially better on complex multi-step tasks. For straightforward tasks, a lighter model is usually sufficient and significantly faster. Match the model to the task.

### Local versus frontier models

| | Local models (via Ollama) | Frontier models (OpenAI, Anthropic) |
|--|--------------------------|-------------------------------------|
| Data sovereignty | Full — stays in your environment | Data leaves your organisation |
| Cost | Compute only, largely fixed | Per-token pricing |
| Capability | Good on common tasks | Better on complex or specialised tasks |
| Privacy | Guaranteed | Depends on contract and service terms |
| Internet connection | Not required | Required |
| Setup complexity | Medium–high | Low |

Blueprint default: local models for everything touching Restricted or Confidential data; frontier models as a governed exception for Internal and Public data where local capability is insufficient.

---

## Part 4: What agents are

### The honest definition

An agent is a model connected to tools, memory, and a task loop. It receives a task, plans how to approach it, uses tools (read files, run scripts, query databases, call APIs), checks its own output, and iterates until the task is complete or it needs human input.

The key difference between a chatbot and an agent is **autonomy over time**. A chatbot answers questions in a conversation and stops. An agent works on a task — potentially over minutes or hours, potentially making many tool calls and course corrections — until something is done or it fails.

### How agents fail

Agents fail in a small number of predictable ways:

**Tool misuse** — The agent calls the right tool in the wrong context, or calls a tool it shouldn't be using at all.

**Context drift** — Over a long task, the accumulated context fills the model's window and earlier instructions start to get lost or overridden.

**Cascading errors** — An error in step one of a multi-step task flows through to step four without being caught, because no checkpoint exists.

**Prompt injection** — Malicious content in a document, email, or web page hijacks the agent's instructions. See [`tools/prompt-injection-defence.md`](../tools/prompt-injection-defence.md).

**Hallucination in tool calls** — The agent invents a file path, function name, or parameter that does not exist, and then acts as if the result succeeded.

Understanding these failure modes is what makes supervised operation (Step 4) productive rather than bureaucratic. You know what you're watching for.

### The supervised → autonomous spectrum

No agent capability starts autonomous. Everything goes through supervised operation:
- The IT Manager reviews all outputs before any action is taken
- Minimum 10 consecutive runs with zero failures before autonomous approval
- A runbook exists before autonomy is granted

This is not extra process. It is the mechanism by which you discover failure modes before they cost you anything.

---

## Part 5: Types of agents and deployment models

### Cloud and app-based tools

**Consumer AI assistants (ChatGPT, Claude.ai, Gemini)**
Web-based interfaces on top of frontier models. Good for general-purpose tasks with Internal or Public data. Not appropriate for Restricted or Confidential data. No operational integration — copy and paste. Lowest barrier to entry.

**Microsoft 365 Copilot**
Microsoft's AI layer on top of Office 365. Deeply integrated with your existing M365 environment and data. Useful if you're already in the M365 ecosystem. Data handling follows your M365 tenant settings — verify these before using it with anything sensitive.

**Google Workspace AI**
Similar to M365 Copilot for Google Workspace. Same data sovereignty caveat applies.

**Productivity tool integrations (Slack AI, Notion AI, and similar)**
AI features built into tools you may already use. Data stays within the tool's environment — verify the data processing terms for each before relying on them.

### Coding tools

**GitHub Copilot**
In-editor code completion and generation. Useful for the IT team's scripting and automation work. Code is sent to GitHub's servers for processing — check your enterprise plan settings for data handling, and ensure no secrets, credentials, or PII are in the context.

**Cursor**
AI-first code editor built on VS Code. Uses frontier models with your codebase as context. Powerful for code generation, refactoring, and explanation. Same data sovereignty consideration as Copilot — code leaves the machine. Good for Internal code. Not appropriate where the codebase handles Restricted data in ways that would expose it.

**Claude Code**
Terminal-based coding agent that works in your local repository. Used for complex, multi-step coding tasks. Operates in your local environment — API calls go to Anthropic's servers, but the agent itself runs where you run it. This blueprint is maintained with Claude Code.

For all coding tools: ensure secrets are properly managed (environment variables, not plain text), and think about what data the model sees before it sees it.

### Local agents and model serving

**Ollama**
Runs open-source language models locally. Supports Llama, Mistral, Phi, DeepSeek Coder, Qwen, and many others. Exposes a local API that agents and tools can call. Runs on Linux, Mac, and Windows. The foundation for local AI processing in this blueprint.

**OpenClaw**
Agent runtime that connects Ollama models to tools, memory (OpenBrain), and task workflows. Used for the IT Manager agent stack in Step 4. Designed for governed, logged, local agent operations.

**LM Studio**
Desktop application for running local models. Easier to set up than Ollama for desktop use. Good for testing and evaluation. Less suitable for production agent deployment.

**Jan.ai**
Open-source desktop AI assistant with local model support. Good for personal productivity. Less suitable for multi-agent deployment.

**Open WebUI**
Web interface that connects to Ollama. Gives you a ChatGPT-like experience over local models. Good for giving staff access to a governed local tool rather than directing them to cloud consumer tools.

### Self-hosted on a server or VPS

Running Ollama and an agent runtime on a dedicated server or VPS gives you:
- Better hardware than most laptops
- Always-on availability for agent tasks
- Network access within your environment
- Full control — no third-party processing

This is the pattern used in the Step 4 build. The server sits on its own VLAN within your infrastructure.

### Deployment model comparison

| Deployment | Best for | Data sovereignty | Complexity |
|------------|----------|-----------------|------------|
| Consumer AI (ChatGPT, Claude.ai) | General tasks, drafting | Low (data leaves org) | None |
| M365/Workspace Copilot | Productivity in existing stack | Medium (governed by tenant) | Low |
| Coding tools (Copilot, Cursor) | Code generation and editing | Low–medium (code leaves machine) | Low |
| Local desktop (LM Studio, Jan.ai) | Personal use, testing | High (local) | Low |
| Open WebUI on server | Staff access to governed local tool | High (local) | Medium |
| Ollama on server | Production local inference | High (local) | Medium |
| Full agent stack (OpenClaw + OpenBrain) | Governed IT automation | Highest (local, logged) | High |

---

## Part 6: How to choose

### Step one: classify the data

What data will this agent or tool touch? If the answer includes anything Restricted, the only options are local-only tools. No exceptions.

### Step two: define the use case

- General research and drafting → Claude.ai (Internal/Public data)
- Code generation → Cursor or Claude Code with appropriate data hygiene
- Automated IT operations → OpenClaw + Ollama
- Document summarisation of sensitive files → Ollama locally

Match the tool to the task. Do not pick a tool and then find tasks to justify it.

### Step three: assess the cost

Frontier API costs add up at volume. Local compute costs are largely fixed after hardware outlay. For high-volume tasks, local models are dramatically cheaper over six months. Run the numbers before committing.

### Step four: assess the maintenance burden

Local models need management — updates, storage, monitoring. Cloud tools need governance and DPA verification. Neither is free of operational overhead. Be honest about what your team can maintain before committing to a path.

### The decision in one rule

Restricted data? → Local only.
Everything else? → Local preferred, cloud with governance where necessary.

---

## Part 7: How to teach this inside a business

### What each tier needs

**Tier 1 — All staff (30 minutes)**

The goal is not expertise. It is safe behaviour.

- What AI tools can and cannot do (three bullet points, not a lecture)
- What data they can and cannot use with AI tools — your AUP addendum, summarised in plain English
- How to recognise when something has gone wrong
- Who to tell and what to do

Deliver in person. Not by email. Not a PDF. If people can ask questions, the session is worth ten times more than a document they'll skim.

**Tier 2 — IT team and champions (2 hours)**

- Hands-on time with the tools they will actually use
- How to write a prompt that works
- How to verify output before acting on it
- What to do when an agent behaves unexpectedly
- Incident response basics

Competency sign-off required before unsupervised use.

**Tier 3 — IT Manager and internal champions (ongoing)**

- Prompt engineering depth
- Agent architecture and governance
- Research and evaluation of new capabilities
- Minimum 2 hours per week, calendar-protected

### Running a session that actually works

Sessions that fail follow a predictable pattern: slides about AI transforming industries, five minutes on what people can't do, and no time for questions.

Sessions that work:

1. **Start with what people already use.** Most staff are already using AI tools personally. Acknowledge this. It reduces defensiveness and means the conversation starts from reality, not from a policy briefing.

2. **Show it working, then show it failing.** The best demonstration of why verification matters is watching a confident AI produce a plausible-sounding error about something the audience knows well.

3. **Get practical, not philosophical.** "Here is what you can and cannot paste into Claude.ai for your specific job role" is more useful than any amount of talk about AI transforming the workplace.

4. **Give them one rule they will actually remember under pressure.** "Would I be comfortable emailing this to a stranger?" is better than asking them to recall a four-tier classification policy at the moment they need to decide.

5. **Leave time for questions.** The questions are where you find out what people are already doing. You need to know this.

### Handling AI anxiety

Some people will be worried about job security. This is a reasonable response to the news coverage. The honest answer is direct: AI amplifies people, it does not replace them in this context. Your job as IT Manager is to help the organisation use AI safely and effectively — which means IT remains essential. Say this plainly. Do not promise what you cannot deliver, but do not amplify anxiety with non-answers either.

### Internal champions

Identify two people who engage readily with new technology. Brief them before the wider team. Give them access to a test environment. Formally recognise their role.

Champions find the practical problems before you go live. They are also the most credible channel for peer-to-peer reassurance when colleagues are uncertain — more credible than IT, because they do the same job as the person asking.

---

## Blueprint sections for this step

| Section | What it covers |
|---------|---------------|
| [`blueprint/14-skills-framework.md`](../blueprint/14-skills-framework.md) | Full competency standard and training tiers |
| [`blueprint/16-change-management.md`](../blueprint/16-change-management.md) | Staff communication, AI anxiety, champions |
| [`blueprint/07-ai-security.md`](../blueprint/07-ai-security.md) | AI-specific threat vectors — read before any deployment |
| [`blueprint/13-vendor-tool-evaluation.md`](../blueprint/13-vendor-tool-evaluation.md) | Evaluating tools against a consistent standard |

---

## Tools for this step

| Tool | Use |
|------|-----|
| [`tools/anti-ai-writing.md`](../tools/anti-ai-writing.md) | Practical exercise — spot and improve weak AI output |
| [`tools/prompt-injection-defence.md`](../tools/prompt-injection-defence.md) | Understand injection patterns before deploying agents |
| [`tools/security-skill-checker.md`](../tools/security-skill-checker.md) | Evaluate any new tool before using it |

---

## Done when

- [ ] IT Manager can explain what a language model is and why it hallucinates
- [ ] IT Manager can classify data and identify which tools are permitted for each classification
- [ ] IT Manager can describe the difference between a chatbot, a local model, and an agent
- [ ] IT Manager understands the main agent failure modes and how supervised operation addresses them
- [ ] IT Manager personal development plan exists and is in progress
- [ ] Tier 1 training delivered to all staff — attendance logged
- [ ] Tier 2 training delivered to IT team — competency sign-off recorded
- [ ] Two internal champions identified and briefed
- [ ] Monthly feedback session scheduled
- [ ] AI security threat vectors understood by IT Manager and champions

**→ Previous step: [Step 2 — Foundations](02-foundations.md)** | **Next step: [Step 4 — Build](04-build.md)**
