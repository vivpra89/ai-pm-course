# TPM / PM: AI Technical Learning Plan

A self-paced course for program and product managers who need **technical depth and current AI jargon**—not generic PM skills. Target: **10–14 weeks** at **6–10 hours/week** (adjust as needed).

**Graduate-style syllabus (readings, problem sets, labs, midterm, capstone rubrics):** **[TPM-PM-AI-Graduate-Course.md](TPM-PM-AI-Graduate-Course.md)**

**Weekly folders (problem statement, readings, practice, exam per week):** **[course-weeks/README.md](course-weeks/README.md)**

**Course hub (browser UI):** **[site/README.md](site/README.md)** — **fully static pages:** open **`site/static/index.html`** (no server), or use the dynamic hub with `python3 -m http.server` from the repo root → `http://localhost:8080/site/`.

---

## How each phase helps you at work

Use this table to see **why** a week matters for a **TPM / technical PM / program manager** job—not just interview prep. Prioritize phases that match your next quarter (e.g. skip ahead to RAG if you are shipping a copilot soon), but keep **Phase 0** first so vocabulary in meetings stays precise.

| Phase | Weeks (typical) | How this shows up on the job |
|-------|-----------------|-------------------------------|
| **Phase 0** — Fundamentals & jargon | 1 | You can **follow engineering and ML conversations** (tokens, latency, context limits, hallucination vs grounding), push back on vague timelines, and ask for **SLOs** and cost drivers instead of accepting “the model will figure it out.” You sound credible in **roadmap and staffing** discussions. |
| **Phase 1** — Prompt engineering | 2–3 | You turn fuzzy asks into **repeatable specs**: system vs user prompts, output schema, eval criteria. That improves **PRDs, AI feature readiness gates**, and vendor POCs—you define **what “good” means** before eng burns cycles. |
| **Phase 2** — LLMs + databases | 4–5 | You connect product questions to **data the company already trusts**: metrics definitions, SQL/text-to-SQL workflows, and **safe** exploration (read-only, approved tables). You validate hypotheses in **reviews with analytics**, not only slides. |
| **Phase 3** — Plots & quantitative validation | 5–6 | You drive decisions with **charts tied to a hypothesis**—exec updates, experiment readouts, incident narratives. You catch **bad denominators** and cherry-picked windows before they reach leadership. |
| **Phase 4** — RAG | 7–8 | You specify **doc-grounded** features (support copilots, internal Q&A), spot **retrieval** failure modes (stale docs, ACL leaks), and align **legal/compliance** asks with how retrieval actually works. |
| **Phase 5** — Chatbot | 9–10 | You own the **product surface**: streaming UX, logging for debugging, rate limits, fallbacks. You write sensible **launch criteria and incident playbooks**—what ops does when the model or DB misbehaves. |
| **Phase 6** — Prototypes | 11–12 | You ship **credible demos** to leadership and XFN fast—reproducible prompts, traces, cost awareness—so decisions are based on **evidence**, not one-off lucky prompts. |
| **Phase 7** — Agentic patterns | 12–14 | You design and review **multi-step automations** (tools, approvals, retries): what must stay **human-in-the-loop**, where **audit logs** go, and how to avoid runaway cost—critical for **internal agents** and integrations. |
| **Extras** — Evals, security, observability, MCP | Ongoing | You run **launch reviews** with the right questions: offline/online eval, prompt injection, residency, observability. You engage **security/legal** with specifics instead of generic “we’ll monitor it.” |
| **Capstone** | Near end | You practice telling a **single end-to-end story** (data → retrieval → UI → metrics)—how you’d justify headcount, vendor spend, and **phase rollout** on a real program. |

**Tip:** In **program management**, Phases **0–2–3** plus **Extras** pay off first for **cross-team alignment** and **milestone reviews**. In **product-facing AI**, weight **1, 4, 5, 7** and **Extras** (safety, eval).

---

## FAANG-level prep (what to optimize for)

FAANG-style TPM and technical PM loops stress **structured ambiguity**, **metric rigor**, **tradeoffs**, and **execution mechanics**. Use this plan together with the hands-on environment in [`practice-env/README.md`](practice-env/README.md) for timed drills.

### What interviewers often probe

| Area | What “good” sounds like |
|------|-------------------------|
| **Problem framing** | You restate goals, constraints, and success criteria before solutions. |
| **Metric definition** | You define numerators/denominators, windows (e.g. 7d vs 28d), and segment cuts when comparing cohorts. |
| **System thinking** | For AI features: data → retrieval/tools → model → eval → safety → cost/latency → rollback; you name single points of failure. |
| **Tradeoffs** | RAG vs fine-tuning; streaming vs batch eval; human review gates; when **not** to use an LLM. |
| **Execution** | Phased rollout, shadow mode, guardrails, dashboards, incident response; **idempotency** and **audit logs** for agents. |

### AI / ML system design (common arc)

1. **Requirements**: who is the user, latency budget, offline vs online freshness, compliance (PII, residency).
2. **Baseline**: rules, search, or smaller model before “big LLM everywhere.”
3. **Eval**: golden sets, regression suites, online A/B; human rubric for subjective quality.
4. **Observability**: traces, prompt/version IDs, token/cost attribution.
5. **Safety**: prompt injection (including via retrieved docs), harmful outputs, unsafe tool calls.
6. **Launch**: progressive exposure, kill switch, fallback UX.

### Behavioral stories (short structure)

Use **STAR** but include **one technical anchor** per story: e.g. “P95 latency moved from X to Y,” “eval gate blocked release until citation accuracy ≥ Z%.” Practice aloud with the [`practice-env`](practice-env/README.md) dataset as the subject (“how I’d validate an AI sidebar hypothesis with events + tickets”).

### Timed drill idea (45–60 min)

Open [`practice-env/sql/faang_style_drills.sql`](practice-env/sql/faang_style_drills.sql). Pick two prompts: write the **metric definition in English**, then **SQL or pandas**, then **one chart type** you’d show to leadership and **one risk** with the metric.

---

## Practice environment (dummy data)

The **`practice-env/`** folder contains:

- **`data/cloudnote.db`** — SQLite (“CloudNote” B2B SaaS: users, subscriptions, events, experiments, support tickets); rebuild with `python scripts/build_dummy_db.py`.
- **`corpus/`** — Markdown files for **RAG** labs.
- **`sql/faang_style_drills.sql`** — Analytical prompts.
- **`labs/explore_metrics.py`** — Sample Python + pandas.

See **[practice-env/README.md](practice-env/README.md)** for setup (`venv`, `pip install -r requirements.txt`).

---

## How to use this plan

- **Concepts & curated links** live in **`learn/`** (topic chapters — read in order or jump to what your job needs). **Each week**, use **`README.md` → `READINGS.md` → `PRACTICE.md` → `EXAM.md`** for rhythm; **`TOPICS.md`** is the extra **practice lab sheet** (drills + checklist) with pointers back to the matching Learn chapter.
- **Outcome per week**: read concepts → **one hands-on artifact** (notebook, small app, or diagram you could explain in an interview).
- **Language for prototypes**: Python is the default for data/LLM tooling; TypeScript is fine for product-shaped demos. Pick one stack and stay consistent.
- **Interview artifact**: keep a **one-page “system diagram + tradeoffs”** for each major project (chatbot, RAG, SQL agent).

---

## Concepts & intuitions checklist (end of each phase)

Use this when you **finish a phase** (or the listed week range). If an item feels fuzzy, stay on that phase until you can explain it **without notes** in **2–3 sentences**.

**Legend:** *Concepts* = vocabulary and facts you recognize and use correctly. *Intuitions* = mental models—what “good” feels like, what usually breaks, what to ask next.

### Phase 0 — End of Week 1

| Concepts you should have | Intuitions you should have |
|--------------------------|-----------------------------|
| **Tokens** as the unit of cost, latency, and context—not “characters” or “words” alone. | Long inputs and outputs **cost more** and **take longer**; huge prompts hit a **hard ceiling** (context window). |
| **Context window** as max simultaneous text the model can attend to. | If it doesn’t fit in context, you must **summarize**, **chunk**, **retrieve**, or **drop**—there is no “just read the whole drive.” |
| **Inference** vs **training**; you ship features on **inference**. | Training is rare for PM scope; your roadmap debates are almost always **serving, eval, data, and cost**—not retraining from scratch. |
| **Temperature / top-p** as randomness knobs. | Higher temperature → **more variance** run-to-run; for production you often want **low** for deterministic UX unless creativity is the goal. |
| **Hallucination** vs **grounding**; **structured output** (JSON/schema). | The model can sound certain and be wrong; **trust comes from tools, retrieval, and checks**—not from fluency. |
| **Embeddings** as “meaning-ish” vectors for similarity search. | Similar **words** ≠ similar **vectors** in every case; similarity is **approximate** and domain-sensitive. |
| **Fine-tuning** vs **RAG** at a decision level (when each is in play). | RAG answers “**what’s true today in our docs/DB**”; fine-tuning often answers “**behave in our style / task pattern**”—different bets. |
| Basic jargon: **tool/function calling**, **guardrails**, **prompt injection**, **eval**, **streaming**, **SLO/latency**. | You can ask engineers sensible questions: **what’s in context**, **what’s the fallback**, **what’s measured**, **what’s blocked**. |

### Phase 1 — End of Weeks 2–3

| Concepts you should have | Intuitions you should have |
|--------------------------|-----------------------------|
| **System vs user** prompts; **multi-turn** state. | The **system** prompt is the product contract; changing it is like changing **requirements**—version it. |
| Patterns: **role + constraints + format**, **few-shot**, **CoT**, **decomposition**, **tool-use framing**. | Prompts are **interfaces**: vague prompts → vague failure; **constraints and examples** reduce rework. |
| **Eval sets** and **pass/fail rubrics** (golden questions). | If you can’t say what “wrong” looks like, you can’t ship with confidence—**define checks before** debating model choice. |
| **JSON mode / schema** for machine-readable outputs. | When downstream is code or UI, **schema beats prose** for reliability. |

### Phase 2 — End of Weeks 4–5

| Concepts you should have | Intuitions you should have |
|--------------------------|-----------------------------|
| **SQL (or approved metrics)** as **source of truth**; LLM proposes, human/rules **validate**. | “The model said the number” is not evidence—**the query + table + filters** are. |
| **Text-to-SQL** pipeline: schema snippet → query → **sandbox execution** → summary. | Wrong **joins**, **date filters**, and **duplicates** are the default risks—**always sanity-check row counts**. |
| **Read-only** DB, **LIMIT**, **allowlisted** tables/columns, **PII** sensitivity. | Treat model-generated SQL like **untrusted code** until reviewed—especially with writes (often **disallowed**). |
| **Schema grounding**; **semantic layer** (approved metric definitions). | Ambiguous business language (“active user,” “revenue”) must map to **one** definition or metrics **won’t** align across teams. |

### Phase 3 — End of Weeks 5–6

| Concepts you should have | Intuitions you should have |
|--------------------------|-----------------------------|
| **Aggregation**, **grouping**, **time windows**, **segments**. | A chart without an explicit **denominator and window** is a **story**, not a metric. |
| When to use **line vs bar vs funnel**; axes, labels, titles. | The chart type encodes a **claim**—match it to the claim (trend vs comparison vs conversion). |
| **pandas/SQL** as the path from DB → plot; optional LLM for **plot code** only under review. | Generated code can **mis-filter** or **double-count**—the intuition is **mistrust until you verify** on real data. |
| Hypothesis → **falsifiable** view; **baseline** or comparison. | Ask: “What would **convince me I’m wrong**?”—if nothing, the metric isn’t ready. |

### Phase 4 — End of Weeks 7–8

| Concepts you should have | Intuitions you should have |
|--------------------------|-----------------------------|
| RAG pipeline: **ingest → chunk → embed → retrieve → augment → generate**; **metadata** (source, date, ACL). | Retrieval quality **caps** answer quality—bad chunks → confident nonsense. |
| **Chunking**, **overlap**, **embedding model**, **vector DB / pgvector**, **top-k**. | Smaller chunks ≠ always better; trade **precision vs recall** at chunk boundaries. |
| **Hybrid search**, **reranking**, **citation** to retrieved spans. | Keyword search finds **exact terms**; embeddings find **paraphrases**—many products need **both**. |
| Failure modes: **stale** docs, **duplicates**, **ACL leaks**, **low recall**. | RAG is not “upload PDF = truth”; **permissions** and **freshness** are product and legal requirements. |

### Phase 5 — End of Weeks 9–10

| Concepts you should have | Intuitions you should have |
|--------------------------|-----------------------------|
| Chat **UX**: streaming, errors, retries, **disclaimers**, **feedback**, “why this answer.” | Users need **progressive disclosure**—fast partial output beats blocking silence if latency is high. |
| **Session / memory**, **rate limits**, **logging** (query, sources, latency, version). | Without logs you cannot **debug** production AI—treat logging as **non-optional** for launched features. |
| **Naive RAG chat** vs **agent + tools** (when complexity warrants). | More autonomy → more **failure modes**; agents are for **multi-step** tasks with **clear stop conditions**. |
| **Prompt injection**, **PII**, **off-topic** handling at UX + backend. | Any user content can try to **override instructions**—assume **hostile** inputs in design reviews. |

### Phase 6 — End of Weeks 11–12

| Concepts you should have | Intuitions you should have |
|--------------------------|-----------------------------|
| Prototype stacks: **notebook**, **Streamlit/Gradio**, **Next.js** mock, **Figma** + API. | Choose fidelity to **the decision**—notebook for logic, Streamlit for **stakeholder demos**, prod-shaped when testing **integration**. |
| **Reproducibility**: seeds, **versioned prompts**, saved **traces**. | A demo that only works on one laptop is a **liability**—pin artifacts like any release candidate. |
| **Latency and cost per session** as product constraints. | Every extra token and round-trip is **money and time**—prototype under realistic caps. |

### Phase 7 — End of Weeks 12–14

| Concepts you should have | Intuitions you should have |
|--------------------------|-----------------------------|
| **Plan → act (tool) → observe → revise** loops; **ReAct-style** behavior. | Longer loops mean **more places to fail**—you need **stop rules**, **timeouts**, and **max iterations**. |
| **Single agent + tools** vs **multi-agent** / **supervisor** routing. | More agents ≠ smarter; often **harder to debug**—default to **simplicity** until proven insufficient. |
| **Human-in-the-loop** for high-impact actions; **idempotency**; **audit logs**. | Side effects (send money, email externally, delete data) need **gates** and **replay-safe** tool design. |
| **Cost explosion** on long runs; **non-determinism** across retries. | Same user input may **branch** differently—product UX must tolerate **variance** or constrain it. |

### Extras — Ongoing (layer across later phases)

| Concepts you should have | Intuitions you should have |
|--------------------------|-----------------------------|
| **Offline eval** vs **online** A/B; **LLM-as-judge** caveats. | Offline catches regressions; online catches **real distribution shift**—you need both for serious launches. |
| **Observability**: traces, prompt/model **version** tags, token accounting. | If you can’t slice failures by **version**, you can’t run a **blameless** postmortem. |
| **Prompt injection** vs **indirect** injection (via retrieved content); **residency**. | Untrusted text anywhere in context—including **RAG results**—can steer the model. |
| **MCP** as “tools/resources for agents” (conceptual). | Standard protocols reduce **one-off glue**; still need **authz** at the tool boundary. |
| When **not** to use LLMs: deterministic logic, regulated math, **tight latency**. | Use the cheapest **correct** tool: rules, classical search, small models, or human workflow. |

### Capstone — End of course

| Concepts you should have | Intuitions you should have |
|--------------------------|-----------------------------|
| One **end-to-end** story: data + retrieval + UI + **metrics** + **risk**. | Shipping AI is a **system** problem—model choice is one box in a larger diagram. |
| **Launch criteria**: eval thresholds, **fallbacks**, **rollback**, **kill switch**. | “GA” means **operational** readiness, not “demo worked once.” |

---

## Phase 0 — Mental model and jargon (Week 1)

### Fundamentals

| Concept | What PMs/TPMs need to know |
|--------|----------------------------|
| **Tokens** | Billing, latency, and context limits are measured in tokens (chunks of text), not “words.” |
| **Context window** | Max text the model can “see” at once; drives summarization, RAG chunking, and tool output size. |
| **Inference** | Running the model to get a completion; distinct from **training**. |
| **Temperature / top-p** | Sampling knobs: lower = more deterministic; higher = more creative/variance. |
| **Hallucination** | Confident wrong outputs; mitigated with retrieval, tools, and evaluation—not “prompt magic” alone. |
| **Grounding** | Tying answers to verifiable sources (docs, DB rows, APIs). |
| **Structured output** | JSON/schema-constrained answers for pipelines and UIs. |
| **Embeddings** | Vectors representing meaning for similarity search (core to RAG). |
| **Fine-tuning vs RAG** | Fine-tuning = teach style/tasks with examples; RAG = inject fresh facts at query time. Different cost/risk profiles. |

### Jargon cheat sheet (high leverage)

- **System prompt vs user prompt**, **multi-turn chat**, **tool calling / function calling**, **orchestration**, **agent**, **planner**, **eval / benchmark**, **guardrails**, **PII redaction**, **prompt injection**, **latency vs throughput**, **streaming**, **SLA/SLO** for AI features.

### Mini deliverable

Write a **half-page** explaining why **context limits** force RAG or summarization for long corpuses.

---

## Phase 1 — Prompt engineering: patterns, not tricks (Weeks 2–3)

### Patterns that map to real product work

1. **Role + constraints + format** (audience, tone, length, schema).
2. **Chain-of-thought (reasoning steps)** — use when you need auditability; hide raw chain from users if needed.
3. **Decomposition** — break PM questions into sub-questions and merge (PRDs, risks, test plans).
4. **Few-shot** — 2–5 examples of desired input/output for repeatable formats.
5. **Self-critique / verification** — “list assumptions, then challenge them.”
6. **Tool-use framing** — prompts that assume the model will call tools (SQL, search, calendar): specify **when** to use tools vs answer from chat.

### Tools and concepts to know exist

Prompt/version libraries (e.g. LangChain/LlamaIndex concepts), **JSON mode**, **eval sets** (golden questions with expected properties).

### Mini deliverable

A **10-question eval sheet** for a feature (correctness, safety, style) with pass/fail rubric.

---

## Phase 2 — LLMs + data: validate ideas with databases (Weeks 4–5)

### Core idea

Turn questions into **queryable truth** and **LLM-assisted exploration** without replacing the database as source of truth.

### Stack concept map

- **SQL** remains the contract; the model proposes queries, you **validate** (human or rules).
- **Text-to-SQL** flow: schema snippet → model generates SQL → execute in sandbox → summarize results.
- Risks: wrong joins, leaking PII, destructive queries → **read-only roles**, **LIMIT**, **allowlisted tables**.

### Patterns

- **Schema grounding**: feed column names, types, sample rows (small).
- **Iterative refinement**: run → error message → fix SQL (agent loop).
- **Semantic layer** (BI term): predefined metrics so the model maps to **approved** definitions.

### Mini deliverable

Connect to **SQLite** with a fake dataset; produce **5 natural-language questions** that resolve to SQL + a one-paragraph “what we learned.”

**Use [`practice-env`](practice-env/README.md):** run `python scripts/build_dummy_db.py`, query `data/cloudnote.db`, and try [`sql/faang_style_drills.sql`](practice-env/sql/faang_style_drills.sql).

---

## Phase 3 — Plots and quantitative validation (Weeks 5–6)

### Goal

From DB → **pandas/SQL** → **chart** → **narrative** tied to a hypothesis.

### Minimum skill path

- SQL aggregation → export or **pandas** → **matplotlib/plotly**.
- For exec-ready charts: know **when to use** bar vs line vs funnel; label axes; show denominators.

### LLM angle

Model drafts **plot code**; you run it locally and inspect the chart. Always verify **filters and time windows**.

### Mini deliverable

Three plots answering: “Is the problem getting worse?”, “Who is affected?”, “What’s the counterfactual baseline?”

Start from [`labs/explore_metrics.py`](practice-env/labs/explore_metrics.py) and extend.

---

## Phase 4 — RAG and related concepts (Weeks 7–8)

### Core pipeline

1. **Ingest** documents (PDF, HTML, tickets).
2. **Chunk** text with overlap; track metadata (source, date, ACL).
3. **Embed** chunks; store in **vector DB** (or pgvector).
4. **Retrieve** top-k similar chunks for a query.
5. **Augment** prompt: chunks + user question → answer with citations.

### Jargon

- **Chunking**, **embedding model**, **vector similarity**, **hybrid search** (keyword + vector), **reranking**, **reciprocal rank fusion**, **citation fidelity**, **ACL-aware retrieval**.

### Failure modes PMs should recognize

Stale docs, **duplicate chunks**, wrong chunk boundaries, **permission leaks** in retrieval, **low recall** (missed relevant passages).

### Mini deliverable

Small **RAG over your own notes/PDFs** with **citations**; document two failure cases you observed.

Starter corpus: [`practice-env/corpus/`](practice-env/corpus/) (`product_faq.md`, `internal_rfc_ai_sidebar.md`).

---

## Phase 5 — Building a chatbot (Weeks 9–10)

### Layers to specify like a TPM

- **UX**: streaming, disclaimers, retry, “why this answer,” feedback thumbs.
- **Backend**: session memory, rate limits, logging.
- **Knowledge**: RAG + optional tools (SQL, ticketing API).
- **Safety**: PII, prompt injection, **off-topic** handling.

### Architecture patterns

- **Naive RAG chat** (single retrieval step).
- **Agent** with tools (retrieve, SQL, HTTP)—**only** when you need multi-step reasoning with verification.

### Mini deliverable

A **minimal** chat UI + backend that logs questions, retrieved sources, and latency. Write a **one-page incident playbook**: “model wrong,” “DB down,” “rate limit hit.”

---

## Phase 6 — Prototypes (Weeks 11–12)

### Prototype types PMs should know

| Type | Good for |
|------|-----------|
| **Prompt + notebook** | Logic and eval before UI |
| **Streamlit / Gradio** | Internal demos fast |
| **Next.js + API route** | Closer to prod shape |
| **Figma + API mocks** | UX without backend |

### What “good prototype” means technically

Reproducible **seed**, versioned **prompt**, saved **traces**, simple **metrics** (latency, cost per session).

### Mini deliverable

One **demo script** (5 minutes) with a live query that hits your DB or RAG corpus and shows a chart.

---

## Phase 7 — Agentic patterns (Weeks 12–14)

### What “agentic” usually means in industry

- **Loop**: plan → act (tool) → observe → revise.
- **Multi-agent** (specialized sub-agents) vs **single agent with tools** (simpler to debug).

### Patterns

- **ReAct-style** reasoning + tool use.
- **Supervisor** routes to specialist tools.
- **Human-in-the-loop** for high-stakes actions (refunds, deletes, emails).

### TPM concerns

Non-determinism, **cost explosion**, **long-running tasks**, **idempotency**, **audit logs**.

### Mini deliverable

Diagram an agent that **must not** send email without approval—show where checks live.

---

## Extras — topics you might not know yet

- **Evaluation**: offline eval sets, online A/B, **LLM-as-judge** (with caveats), human rubrics.
- **Observability**: traces (Langfuse/OpenTelemetry-style concepts), prompt/version tagging.
- **Cost**: tokens in/out, caching, smaller models for routing.
- **Security**: **prompt injection**, **indirect injection** (malicious content inside retrieved docs), **data residency**.
- **Governance**: model cards, **bias/fairness** checkpoints for user-facing decisions.
- **MCP (Model Context Protocol)**: standard way to expose **tools/resources** to agents (worth a shallow pass for vendor conversations).
- **When not to use LLMs**: tight deterministic logic, regulated math, sub-ms latency—use traditional code.

---

## Capstone project

**“Insight copilot”** for a fake product:

1. Ingest FAQs/docs → **RAG** with citations (use [`practice-env/corpus`](practice-env/corpus/) or your own).
2. Add **read-only SQL** on [`practice-env/data/cloudnote.db`](practice-env/README.md).
3. Generate **plot code** + chart for one hypothesis.
4. **Chatbot** UI with logging and a basic **eval** set.
5. **Written reflection**: tradeoffs, failure modes, what you’d measure in production.

---

## Suggested weekly rhythm

| Activity | Time |
|----------|------|
| Concept deep dive (articles/docs) | 2–3 h |
| Hands-on lab | 3–5 h |
| Jargon flashcards + explain aloud | 1 h |

---

## Quick topic index

| Topic | Phase |
|-------|--------|
| LLM fundamentals & jargon | 0 |
| Prompt engineering patterns | 1 |
| AI + databases / validation | 2 |
| Plots from DB data | 3 |
| RAG | 4 |
| Chatbot | 5 |
| Prototypes | 6 |
| Agentic patterns | 7 |
| Evals, security, observability, MCP | Extras |
