# Foundations — LLM literacy for PMs / TPMs

*Estimated study: 3–5 hours before Week 1 practice.*

---

## What you’ll know after this chapter

- Why **tokens** and **context windows** drive cost, latency, and architecture choices  
- **Inference vs training** — what product teams ship day to day  
- **Hallucination vs grounding** — where trust comes from  
- **Embeddings** at a high level (detail in [RAG](rag.md))  
- When **RAG vs fine-tuning** is the right class of bet  

---

## 1. Topic map

| Topic | One-line job |
|-------|----------------|
| **Tokens** | Billing and limits are counted in tokens — not “words.” |
| **Context window** | Hard cap on text in one request → summarization, chunking, retrieval. |
| **Inference vs training** | You ship features on **inference**; full training is rarely the PM lever. |
| **Hallucination vs grounding** | Fluency ≠ truth; tie answers to sources or tools. |
| **Embeddings** | Dense vectors for “similar meaning” — powers search/RAG. |
| **RAG vs fine-tuning** | RAG = fresh facts at query time; fine-tuning often = style/tasks — different tradeoffs. |

---

## 2. Resources by topic

### Tokens

- **Docs:** [OpenAI — Understanding tokens](https://platform.openai.com/docs/concepts/tokens)
- **Interactive:** [OpenAI tokenizer](https://platform.openai.com/tokenizer)
- **Models / limits:** [Anthropic model docs](https://docs.anthropic.com/en/docs/about-claude/models) or [OpenAI models](https://platform.openai.com/docs/models)

### Context window

- Read “context” / “window” in your provider’s model guide — same links as above.
- **Idea:** Anything that doesn’t fit must be summarized, chunked, or retrieved — there is no magic “read my whole drive.”

### Inference vs training

- **Overview:** [Google Cloud — What is generative AI?](https://cloud.google.com/learn/what-is-generative-ai)
- **Video (search):** YouTube — **“Andrej Karpathy intro large language models”** or **“State of GPT”** — big-picture stack only.

### Hallucination & grounding

- **Safety:** [OWASP LLM Top 10 — overview](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- **Product:** Search **“grounded generation LLM”** + your cloud vendor’s grounding docs.

### Embeddings

- [Google — Embeddings guide](https://ai.google.dev/docs/embeddings_guide) or [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings)
- **Optional deep dive:** Search **“Jay Alammar illustrated transformer”** (intuition only).

### RAG vs fine-tuning

- [Google Cloud — RAG](https://cloud.google.com/use-cases/retrieval-augmented-generation)
- **PM takeaway:** RAG answers “what’s true *today* in our corpus”; fine-tuning often teaches *behavior* — combine thoughtfully.

---

## 3. Apply → weekly practice

When this chapter feels solid, do **[Week 1](../course-weeks/week-01/README.md)** (Overview → Readings → Practice → Exam). Extra drills live in that week’s **`TOPICS.md`** (practice lab sheet).
