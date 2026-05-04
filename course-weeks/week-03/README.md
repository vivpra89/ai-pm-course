# Week 03 — Prompt patterns II: CoT, self-critique, tool-use framing + eval sheet (Phase 1)

## Problem statement

Same incident program as Week 02—now you must make reasoning **auditable**, catch **overconfidence**, and specify **when** the model should refuse or call tools. You also ship a **10-question eval sheet** so QA and PM agree what “pass” means.

## Outcomes

- Chain-of-thought **instruction** (raw chain may stay hidden from users).
- Self-critique / verification pattern.
- Tool-use framing: **when** to query SQL vs answer from chat.
- **Eval sheet** with pass/fail rules + **2 safety/refusal** rows.

## Deliverables

1. `eval_sheet_10.md` — ten rows: Question | Expected property | Pass/Fail rule.
2. Prompt pack using CoT + self-critique on `../week-02/data/incident_sample.md`.
3. One-page **tool-use policy**: which tools (SQL, search, calendar) for which user intents.

## Links

- [Phase 1 mini deliverable](../../TPM-PM-AI-Technical-Learning-Plan.md#phase-1--prompt-engineering-patterns-not-tricks-weeks-23)
