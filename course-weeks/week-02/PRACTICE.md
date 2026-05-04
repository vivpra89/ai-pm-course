# Week 02 — Learning by practice

Use `data/incident_sample.md` as the **single source incident** for all tasks.

## Task A — Role + constraints + format

Write **one system prompt** and **one user prompt** that produce:

- Executive audience, neutral tone.
- **≤ 120 words** total output.
- Sections: **Summary**, **Customer impact**, **Next steps**.

Save as `prompts_v1.md`.

## Task B — Few-shot

Add **two** input/output examples (synthetic is fine) showing “good” summaries for smaller incidents. Keep examples **short**. Save as `prompts_v2_fewshot.md`.

## Task C — Decomposition

Before summarizing, ask the model (or write yourself) a **3-step decomposition**:

1. Extract facts vs hypotheses.  
2. Rank severity.  
3. Then summarize.

Implement this either as **three chained prompts** or **one prompt with explicit steps**. Save as `prompts_v3_decompose.md`.

## Task D — Compare outputs

Run **A, B, C** against `incident_sample.md` (use any chat UI or API). Paste outputs side-by-side in `comparison.md` (≤ 400 words) with:

- Which output you’d ship first.
- One **failure mode** you still see (missed P0, vague impact, etc.).

---

**Submit:** `my-submissions/week-02/` with all markdown files.
