# Prompting — specs, patterns, evals

*Estimated study: 4–6 hours · aligns with Weeks 2–3 practice.*

---

## Outcomes

- Treat prompts as **product interfaces** — version them like requirements.  
- Use **role + constraints + format**, **few-shot**, **decomposition**, **chain-of-thought**, **tool framing**.  
- Define **eval sets** with checkable pass/fail rules (including refusal cases).  
- Use **JSON / structured outputs** when downstream is code or UI.  

---

## Topic map

| Topic | Core idea |
|-------|-----------|
| **Role + constraints + format** | Audience, length, tone, schema — vague prompts → vague failures. |
| **Few-shot** | 2–5 examples lock output shape. |
| **Decomposition** | Split PM-sized asks into steps; merge results. |
| **Chain-of-thought** | Explicit reasoning step — auditability (may hide raw chain from users). |
| **Self-critique** | List assumptions → challenge → revise. |
| **Tool / function calling** | Model proposes actions; your code executes — own failures. |
| **Eval sets** | Golden questions + expected properties + safety rows. |

---

## Resources

### Core guides

- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic — Prompt engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- **Few-shot intuition:** skim abstract of **“Language Models are Few-Shot Learners”** (GPT-3 paper).

### Chain-of-thought & verification

- Search **“Chain-of-Thought prompting Wei”** — skim one summary.
- Search **“LLM eval golden set”** — Hugging Face / LangChain / Anthropic articles.

### Tools & JSON

- [OpenAI — Function calling](https://platform.openai.com/docs/guides/function-calling)
- [OpenAI — Structured outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [Anthropic — Tool use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)

---

## Apply → weekly practice

**[Week 2](../course-weeks/week-02/README.md)** — patterns on an incident narrative.  
**[Week 3](../course-weeks/week-03/README.md)** — CoT, eval sheet, tool policy.
