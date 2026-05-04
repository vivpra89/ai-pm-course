# Week 03 — Learning by practice

Use incident text from **[week-02/data/incident_sample.md](../week-02/data/incident_sample.md)**.

## Task A — Chain-of-thought (design only)

Write a prompt that forces **explicit reasoning steps** before the final executive summary. Optionally hide raw chain from end users in your product note. Save `prompt_cot.md`.

## Task B — Self-critique

Same incident: add a second stage— “List assumptions, then challenge them; revise summary if needed.” Save `prompt_selfcritique.md` + paste **before/after** summary if different.

## Task C — Tool-use framing

Write `tool_policy.md` answering:

- When should the assistant **refuse** numeric claims without querying **`practice-env` DB**?
- When is “read Support queue +22%” acceptable without SQL?

Include **one** example user question routed to **SQL** and one routed to **no SQL**.

## Task D — Eval sheet (required)

Create **`eval_sheet_10.md`** with **10** rows:

| # | User question or stress case | Expected property | Pass/Fail rule |

Include:

- At least **2** safety/refusal cases (e.g. exfiltration, medical/legal).
- At least **2** format/check cases (JSON keys present, word limit).
- At least **1** “must cite or qualify uncertainty” case tied to the incident.

---

**Submit:** `my-submissions/week-03/`.
