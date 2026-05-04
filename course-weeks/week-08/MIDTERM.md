# Week 08 — Midterm (timed)

**Total: 90 minutes.** Stop when time is up. Use only: SQLite + `practice-env/data/cloudnote.db`, schema from [practice-env README](../../practice-env/README.md), and blank paper/notes **you wrote yourself**.

## Part A — Metric precision (30 min)

Rewrite these **ambiguous** questions into **testable** metric definitions (numerator, denominator, window, segment if needed):

1. “Did the AI sidebar hurt retention?”  
2. “Are enterprise customers unhappy?”  
3. “Is the product getting slower?”

## Part B — SQL (45 min)

On `cloudnote.db`, write queries that:

1. Count **distinct users** with at least one `checkout_complete` event, **by segment**.  
2. List **top 3** `event_name` values by **count** in February 2025 (use `event_ts` text comparison `>= '2025-02-01' AND < '2025-03-01'` or equivalent).

Run queries and paste row counts or sample rows.

## Part C — Short concepts (15 min)

Define in **≤ 2 sentences** each: **embedding**, **RAG**, **prompt injection**, **temperature**.

---

**Afterward:** Grade using answer key you write **tomorrow** with references open; update weak topics.
