# Weekly folders — AI for TPM / Technical PM

This directory maps **[TPM-PM-AI-Technical-Learning-Plan.md](../TPM-PM-AI-Technical-Learning-Plan.md)** to **14 consecutive weeks** of hands-on work. **Concepts and resource lists** are in **[`../learn/`](../learn/README.md)** (topic path). Each week folder is self-contained:

| File | Purpose |
|------|---------|
| **`README.md`** | **Start here each week:** problem statement, scenario, deliverables |
| **`TOPICS.md`** | **Practice lab sheet** — extra drills + checklist; links to the matching Learn chapter |
| **`READINGS.md`** | What to read or skim before practice (docs, concepts) |
| **`PRACTICE.md`** | Hands-on assignments (“learn by doing”) |
| **`EXAM.md`** | End-of-week check—redo **without** peeking at notes until you’ve answered |

**Shared environment:** [`../practice-env/`](../practice-env/README.md) — SQLite `cloudnote.db`, `corpus/` for RAG weeks, SQL drills.

**Graduate-style detail:** **[TPM-PM-AI-Graduate-Course.md](../TPM-PM-AI-Graduate-Course.md)**

**Where to put your work:** create `my-submissions/week-XX/` at the repo root (or inside each `week-XX/` folder) so your prompts, SQL, and exports stay organized.

---

## Week index

| Folder | Focus | Phase (plan) |
|--------|--------|----------------|
| [week-01](week-01/README.md) | LLM fundamentals, jargon, context limits; setup `practice-env` | Phase 0 |
| [week-02](week-02/README.md) | Prompt patterns: role/constraints, few-shot, decomposition | Phase 1 |
| [week-03](week-03/README.md) | CoT, self-critique, tool-use framing; **10-Q eval sheet** | Phase 1 |
| [week-04](week-04/README.md) | SQL as source of truth; natural language → SQL | Phase 2 |
| [week-05](week-05/README.md) | Text-to-SQL safety; threat model; drills | Phase 2 |
| [week-06](week-06/README.md) | Plots + quantitative validation | Phase 3 |
| [week-07](week-07/README.md) | RAG pipeline (ingest → retrieve → cite) | Phase 4 |
| [week-08](week-08/README.md) | RAG failure modes; **midterm** | Phase 4 |
| [week-09](week-09/README.md) | Chatbot UX, logging, rate limits | Phase 5 |
| [week-10](week-10/README.md) | Minimal chat UI; incident playbook | Phase 5 |
| [week-11](week-11/README.md) | Prototypes: reproducibility, Streamlit/Gradio path | Phase 6 |
| [week-12](week-12/README.md) | Demo script; cost/latency; **capstone kickoff** | Phase 6 |
| [week-13](week-13/README.md) | Agentic loops; human-in-the-loop; idempotency | Phase 7 |
| [week-14](week-14/README.md) | Capstone integration; extras review; **final review** | Phase 7 + Capstone |

---

## How to consume each week (recommended order)

1. **Learn chapter** (from [`../learn/README.md`](../learn/README.md)) — study the topic that matches this week when you need concepts or links.
2. **`README.md`** → **`READINGS.md`** → **`PRACTICE.md`** — course assignments in full.
3. **`TOPICS.md`** — practice bank rows (problem / data / outcome) as extra drills.
4. **`EXAM.md`** — self-test before checking solutions or notes.

## Note on “Week 1” vs prompt engineering

**Week 1** is **fundamentals and setup** (tokens, context window, jargon)—not full prompt-engineering patterns. **Prompt engineering patterns** start in **Weeks 2–3**, aligned with **Phase 1** in the master plan.
