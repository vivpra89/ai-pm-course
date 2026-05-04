# Week 1 — Practice lab sheet

**Concepts & curated links:** read the Learn chapter **[Foundations](../../learn/foundations.md)** first (topic path, not calendar-only). This file is the **weekly practice bank** — extra drills and a checklist on top of **Readings** → **Practice** → **Exam**.

---

## 1. Practice bank

Use **`practice-env`** for anything marked with data below. Paths are relative to the **`practice-env/`** folder in this repo.

| # | Problem | Data / materials | Expected outcome |
|---|---------|-------------------|------------------|
| P1 | Explain in **≤ 5 sentences** why “paste the whole wiki into the prompt” fails at scale. | Concept only | Written answer you could give in a design review |
| P2 | Run the tokenizer or provider docs: approximate token count for **200 words** of English. | Tokenizer link in T1 | Screenshot or number + one-line interpretation |
| P3 | List **3 risks** of relying on model prose for **revenue numbers** without a database. | None | Bullet list in your notes |
| P4 | Complete **`practice-env` setup**: venv, `pip install`, `build_dummy_db.py`, `explore_metrics.py`. | `practice-env/README.md` | Terminal output saved + one sentence on what the rollup shows |
| P5 | Open `data/long_briefing_stub.txt` (in **`course-weeks/week-01/data/`**). Summarize to **≤ 120 words** for a VP yourself (no LLM), then optionally compare with one LLM summary. | `course-weeks/week-01/data/long_briefing_stub.txt` | Two short paragraphs: yours vs what you’d change after comparing |

### Expanded (same as table)

**P4 — Environment**

- **Problem:** Prove the practice database runs end-to-end.
- **Data:** SQLite `cloudnote.db`, script output.
- **Outcome:** Reproducible proof you can load metrics locally (foundation for Weeks 4–6).

**P5 — Context / summarization**

- **Problem:** Practice aggressive summarization tradeoffs.
- **Data:** Long stub briefing.
- **Outcome:** Explicit list of what you dropped and why (ties to context limits).

---

## 2. Week checklist

- [ ] Watched/read at least **one** resource per topic row (T1–T6)
- [ ] Finished **P4** (practice env)
- [ ] Finished **P5** or **P1–P3** written prompts
- [ ] Completed **`READINGS.md`** and **`PRACTICE.md`** for the formal week assignment
- [ ] **`EXAM.md`** without peeking at notes first
