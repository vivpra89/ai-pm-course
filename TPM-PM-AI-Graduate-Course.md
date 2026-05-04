# Graduate-style course: AI for TPM / Technical PM

This document turns **[TPM-PM-AI-Technical-Learning-Plan.md](TPM-PM-AI-Technical-Learning-Plan.md)** into a **structured seminar**: readings, **graded-style assignments** (you self-grade with rubrics), milestones, and a capstone. Treat each week like **8–12 hours** of graduate coursework (readings + problem sets + labs).

**Companion artifacts**

- Learning roadmap and topic index: **[TPM-PM-AI-Technical-Learning-Plan.md](TPM-PM-AI-Technical-Learning-Plan.md)**
- Hands-on data and corpus: **[practice-env/README.md](practice-env/README.md)**

---

## 1. Course information

| Field | Detail |
|-------|--------|
| **Audience** | Program managers, TPMs, and PMs preparing for **technical + AI** depth (including FAANG-style loops). |
| **Prerequisites** | Comfort with spreadsheets; willingness to run Python in a virtualenv; basic SQL helpful but teachable inside the course. |
| **Duration** | **14 weeks** (one module per week); compress or extend as needed. |
| **Materials** | Open documentation from major model providers, OWASP LLM materials, optional survey papers; local **`practice-env`** SQLite + Markdown corpus. |

### Learning outcomes (what you should be able to do)

By the end you should be able to:

1. **Define** core LLM concepts (tokens, context window, inference vs training, grounding, embeddings) and use vocabulary correctly in design discussions.
2. **Draft** prompts using reusable **patterns** (role/constraints, few-shot, tool-use framing) and an **eval rubric** for a feature.
3. **Translate** product questions into **metric definitions** and **SQL or pandas** queries; critique ambiguous analytics.
4. **Produce** charts tied to a hypothesis and explain **one weakness** of each metric.
5. **Explain** the RAG pipeline, common failure modes, and mitigations at a **system** level.
6. **Specify** a minimal chatbot/RAG product: UX, logging, safety, and incident response.
7. **Diagram** an agentic workflow with **human gates**, idempotency, and auditability.

---

## 2. How to actually learn this (graduate habits)

| Habit | What to do |
|-------|------------|
| **Active recall** | After each reading, close the tab and write **5 bullet notes** from memory. |
| **Explain aloud** | 10-minute “lecture to the wall” on one topic (tokens, RAG, eval). |
| **One artifact per week** | Never finish a module with only passive reading—always submit the **lab deliverable**. |
| **Timed practice** | Use a **45-minute** block for SQL drills and **90 minutes** for system-design outlines. |
| **LLM use policy** | You may use AI assistants for drafts **if** you (a) paste your final reasoning in your own words, (b) verify anything that touches **numbers or SQL** against the DB, (c) note in the assignment where the assistant helped. |

---

## 3. Grading map (self-assessment)

There are no external graders. Use the rubrics below; aim for **“meets” or “exceeds”** on every criterion before moving on.

| Component | Weight (suggested) | What it is |
|-----------|-------------------|------------|
| **Problem sets (PS1–PS7)** | 35% | Written + short analytical tasks |
| **Labs (L0–L7)** | 35% | Code/SQL/notebook deliverables |
| **Midterm** | 10% | Timed SQL + metric-definition exam (self-proctored) |
| **Capstone** | 20% | Integrated project + written report |

Adjust weights if you skip optional sections.

---

## 4. Weekly modules: readings + assignments

Each **Module *n*** lists: objectives, readings (complete **before** the problem set), **Problem Set *n***, and **Lab *n***. Solution discipline: store work in a folder like `my-submissions/module-03/` (you create it).

### Module 0 — Foundations and jargon (Week 1)

**Objectives:** Explain tokens, context window, inference vs training, hallucination vs grounding, embeddings at a high level; list 10 jargon terms you did not know before.

**Readings (pick depth)**

- *Required:* Skim your chosen provider’s docs on **models**, **tokens**, **chat vs completions**, **JSON / structured output** (e.g. OpenAI, Anthropic, or Google AI Studio documentation—one ecosystem is enough).
- *Recommended:* OWASP **LLM Top 10** overview (conceptual, not memorization of every item).

**Problem Set 0 (PS0)**

1. In **≤ 250 words**, explain why **context limits** imply summarization, chunking, or RAG for large corpora.
2. Glossary: define **10 terms** from the learning plan’s jargon list in **your own words** (no copy-paste).

**Lab 0 (L0)**

- Set up **`practice-env`** per [README](practice-env/README.md): `venv`, `pip install -r requirements.txt`, run `scripts/build_dummy_db.py`, run `labs/explore_metrics.py`.
- Submit: screenshot or paste of terminal output + **one sentence** describing what the script computes.

**Rubric — PS0**

| Criterion | Meets | Exceeds |
|-----------|--------|---------|
| Context limits | Links limits to a **product** consequence (cost, truncation, recall). | Compares two mitigation strategies (e.g. RAG vs summarize) with a tradeoff. |
| Glossary | Definitions are accurate and plain-language. | Each term has a **tiny example** (one phrase). |

---

### Module 1 — Prompt engineering as engineering (Weeks 2–3)

**Objectives:** Use prompt **patterns** (not vibes); design a small **eval** with pass/fail rules.

**Readings**

- *Required:* Provider guide on **system prompts**, **multi-turn**, and **function calling** (or equivalent).
- *Recommended:* One industry write-up on **eval sets** for LLM features (blog or vendor-neutral summary).

**Problem Set 1 (PS1)**

1. Write **one system prompt** and **one user prompt** for: “Summarize a weekly incident report for executives; flag P0 risks.” Include **constraints** (length, tone) and **output format** (bullets vs JSON).
2. Build a **10-question eval sheet** for that feature: columns `Question | Expected property | Pass/Fail rule`. Include at least **2 safety/refusal** cases.

**Lab 1 (L1)**

- In a Markdown file, show **three variants** of the same task using: (a) role + constraints only, (b) **few-shot** with 2 examples, (c) **chain-of-thought** instruction with optional hidden reasoning note.
- For each variant, run the prompt against **one** real or synthetic incident paragraph (invented is fine) and paste outputs; write **3 sentences** on which variant you’d ship first and why.

**Rubric — PS1 / L1**

| Criterion | Meets | Exceeds |
|-----------|--------|---------|
| Eval sheet | Pass/fail is **checkable** without subjective vibes. | Includes **negative tests** (wrong format, missing P0). |
| Variant comparison | Chooses a variant with **stated tradeoffs** (latency, verbosity, control). | Discusses **eval maintenance** (when prompts change). |

---

### Module 2 — LLMs and databases (Weeks 4–5)

**Objectives:** Treat SQL as source of truth; specify **safe** text-to-SQL workflows; practice **`practice-env`**.

**Readings**

- *Required:* Documentation on **read-only** DB users / SQLite safety patterns (your choice); one article on **text-to-SQL** pitfalls (join errors, date filters).

**Problem Set 2 (PS2)**

1. From **`practice-env`**, write **5 business questions** in English and the **SQL** that answers each (run against `cloudnote.db`).
2. **Threat model:** In **≤ 200 words**, list **three** ways a text-to-SQL assistant could cause harm and **one** control per harm (allowlist, LIMIT, human approval, etc.).

**Lab 2 (L2)**

- Complete **at least 3** analytical prompts from [`practice-env/sql/faang_style_drills.sql`](practice-env/sql/faang_style_drills.sql): for each, submit (a) metric definition in English, (b) working SQL, (c) **one sentence** interpreting the result.

**Rubric — PS2 / L2**

| Criterion | Meets | Exceeds |
|-----------|--------|---------|
| SQL | Queries run without error; joins match intent. | Uses **clear aliases** and comments for non-obvious filters. |
| Safety | Controls map to realistic deployment. | Mentions **audit log** or **semantic layer** for metrics. |

---

### Module 3 — Visualization and narrative (Week 5–6)

**Objectives:** Tie plots to hypotheses; label and defend denominators.

**Readings**

- *Required:* Matplotlib or Plotly “getting started” (skim); one article on **metric hygiene** (cohorts, ratios).

**Problem Set 3 (PS3)**

1. For each plot type—**line**, **bar**, **funnel**—give **one** PM question it answers well and **one** misuse.
2. Hypothesis: “Enterprise users file more support tickets per active user than SMB.” Define **active user** and **normalize** the comparison; state what would **falsify** the hypothesis.

**Lab 3 (L3)**

- Extend [`labs/explore_metrics.py`](practice-env/labs/explore_metrics.py) or a notebook: produce **three** static plots for `cloudnote.db` that answer:
  - “Is the problem getting worse?”
  - “Who is affected?”
  - “What’s a simple baseline or comparison?”
- Submit plots (PNG or PDF) + **≤ 150 words** total interpretation.

**Rubric — L3**

| Criterion | Meets | Exceeds |
|-----------|--------|---------|
| Charts | Axes labeled; title states the takeaway. | Denominator or time window explicit in caption. |
| Narrative | Hypothesis linked to chart; caution noted. | Calls out **Simpson’s paradox** or segment confound if relevant. |

---

### Module 4 — RAG (Weeks 7–8)

**Objectives:** Describe ingest → chunk → embed → retrieve → generate; recognize failure modes.

**Readings**

- *Required:* One vendor-neutral explainer on **embeddings** and **vector search**; LlamaIndex or LangChain **RAG overview** (skim architecture diagrams only if short on time).
- *Recommended:* Survey **hybrid search** (BM25 + dense) at concept level.

**Problem Set 4 (PS4)**

1. Draw **RAG architecture** (boxes + arrows): ingestion, chunking, embedding store, retriever, generator, optional reranker.
2. List **four failure modes** (stale doc, bad chunk, ACL leak, low recall) and **one** mitigation each.

**Lab 4 (L4)**

- Minimum viable RAG: chunk [`practice-env/corpus/`](practice-env/corpus/) (by heading or fixed size), embed with a library/API of your choice **or** simulate retrieval with keyword overlap if you have no API key—**state which**.
- Ask **5 questions**; for each, show **retrieved chunks** and model answer with **citations** (or pseudo-citations if simulated).
- Write **two** observed failures and how you’d detect them in production.

**Rubric — L4**

| Criterion | Meets | Exceeds |
|-----------|--------|---------|
| Traceability | Answers tie to specific chunks. | Eval idea for **citation accuracy** sketched. |

---

### Module 5 — Chatbot product surface (Weeks 9–10)

**Objectives:** Specify UX, logging, rate limits, fallbacks; naive RAG vs tool-using agent—when each.

**Readings**

- *Required:* Your provider’s docs on **streaming** and **rate limits**.
- *Recommended:* One post on **prompt injection** in chat UIs.

**Problem Set 5 (PS5)**

1. **One-pager** spec: stakeholders, success metrics, **P95 latency** target (pick a number and defend order-of-magnitude), logging fields per turn.
2. **Incident playbook** (≤ 1 page): “model wrong,” “DB down,” “rate limit,” “retrieval returns empty.”

**Lab 5 (L5)**

- Minimal UI (Streamlit/Gradio/CLI): user asks a question; system retrieves from **corpus** and/or runs **one** read-only SQL template you approve.
- Log: timestamp, question, sources used, rough latency.
- Submit: short screen recording or transcript + `README` how to run.

**Rubric — L5**

| Criterion | Meets | Exceeds |
|-----------|--------|---------|
| Ops | Logs exist and are useful. | Redaction strategy for PII mentioned. |

---

### Module 6 — Prototypes and reproducibility (Weeks 11–12)

**Objectives:** Reproducible demos; versioned prompts; cost awareness.

**Readings**

- *Required:* Skim **Streamlit** or **Gradio** docs (your choice).
- *Recommended:* Notes on **token counting** and caching concepts.

**Problem Set 6 (PS6)**

1. Write a **5-minute demo script** (bullet outline) for leadership: setup, question, expected insight, fallback line if the model fails.
2. Estimate **order-of-magnitude** tokens for one session (show assumptions).

**Lab 6 (L6)**

- Package L5 into a **reproducible** run: `requirements.txt` or lockfile, **pinned** prompt text in a file, `README` with exact commands.
- Optional: add **one** chart from `cloudnote.db` in the same demo flow.

**Rubric — L6**

| Criterion | Meets | Exceeds |
|-----------|--------|---------|
| Repro | Fresh clone runs with documented steps. | Single command or Makefile target. |

---

### Module 7 — Agentic patterns (Weeks 12–14)

**Objectives:** Plan–act–observe loops; human gates; cost and audit.

**Readings**

- *Required:* One overview of **ReAct** or **tool use** (paper abstract + diagram ok).
- *Recommended:* MCP introduction (Anthropic or official MCP docs)—**conceptual**.

**Problem Set 7 (PS7)**

1. Compare **single agent with tools** vs **multi-agent** for **one** scenario (e.g. “investigate ticket + query metrics”): pros/cons in a table.
2. Design **human approval** for any action that sends email or refunds money—sequence diagram or numbered steps.

**Lab 7 (L7)**

- Diagram (Mermaid, draw.io export, or neat ASCII) an agent that **cannot** send external email without approval; include **retry/idempotency** note for tool calls.

**Rubric — PS7 / L7**

| Criterion | Meets | Exceeds |
|-----------|--------|---------|
| Governance | Approval boundary is explicit. | Discusses **duplicate execution** or **partial failure**. |

---

## 5. Midterm (Week 8 suggested)

**Duration:** 90 minutes, closed notes except **`practice-env`** schema sheet and SQLite CLI.

**Sections**

1. **Metric definitions (30 min):** Given three ambiguous questions (“Did AI improve retention?”), rewrite **precise definitions** (numerator/denominator/window).
2. **SQL (45 min):** Answer **two** prompts from [`faang_style_drills.sql`](practice-env/sql/faang_style_drills.sql) with working queries on `cloudnote.db`.
3. **Short concepts (15 min):** Define **four** of: embedding, temperature, RAG, prompt injection, eval set, P95 latency—in **2 sentences each**.

**Self-grade:** Use answer keys you write **after** the exam (prepare keys from your own solutions the next day); flag gaps and redo weak sections.

---

## 6. Capstone (Weeks 12–14)

Align with **[Capstone in learning plan](TPM-PM-AI-Technical-Learning-Plan.md)** — **Insight copilot** using `practice-env` corpus + DB.

### Deliverables

| Artifact | Requirement |
|----------|-------------|
| **Code/notebook** | RAG + at least **one** approved SQL path + **one** chart from DB |
| **Eval** | ≥ **15** golden questions with expected behaviors (correct refusal, citation, numeric sanity) |
| **Report (2000–3500 words)** | Problem, users, architecture, **tradeoffs**, risks, **launch plan**, metrics dashboard sketch |
| **Demo** | 8-minute recorded walkthrough or live checklist |

### Capstone rubric (summary)

| Dimension | Meets | Exceeds |
|-----------|--------|---------|
| Technical coherence | End-to-end flow works; limitations stated. | Clear comparison vs baseline without AI. |
| Product judgment | Metrics tied to decisions; rollout phased. | Explicit **rollback** and **kill switch**. |
| Risk | Safety and misuse discussed with mitigations. | **Red-team** two abuse scenarios. |

---

## 7. Suggested calendar (14 weeks)

| Week | Focus | Submit |
|------|--------|--------|
| 1 | Module 0 | PS0, L0 |
| 2–3 | Module 1 | PS1, L1 |
| 4–5 | Module 2 | PS2, L2 |
| 5–6 | Module 3 | PS3, L3 |
| 7–8 | Module 4 + **Midterm** | PS4, L4, midterm |
| 9–10 | Module 5 | PS5, L5 |
| 11–12 | Module 6 | PS6, L6 |
| 12–14 | Module 7 + **Capstone** | PS7, L7, capstone |

Overlap weeks intentionally combine lighter reading with heavier labs—adjust to your schedule.

---

## 8. Where this ties back

| Topic | Learning plan phase | This course |
|-------|---------------------|-------------|
| Jargon / fundamentals | Phase 0 | Module 0 |
| Prompting / eval | Phase 1 | Module 1 |
| SQL / validation | Phase 2 | Module 2 |
| Plots | Phase 3 | Module 3 |
| RAG | Phase 4 | Module 4 |
| Chatbot | Phase 5 | Module 5 |
| Prototypes | Phase 6 | Module 6 |
| Agents | Phase 7 | Module 7 |

---

*This syllabus is for independent study; adapt deadlines, readings, and rubrics to your goals.*
