# RAG — retrieval, chunking, evaluation

*Estimated study: 5–8 hours · aligns with Weeks 7–8 (includes midterm window).*

---

## Outcomes

- Explain **embeddings**, **vector stores**, **chunking**, **top‑k**, **hybrid search**.  
- Know **tradeoffs** — latency, freshness, cost, permissions.  
- Run an **RAG eval loop**: retrieval hits + answer faithfulness + failure buckets.  

---

## Topic map

| Topic | Core idea |
|-------|-----------|
| **Embeddings** | Dense vectors for semantic similarity. |
| **Chunking** | Unit of retrieval — wrong chunk size breaks answers. |
| **Vector store** | Index + filters + metadata (tenant, doc type). |
| **Hybrid** | Keyword + vector — often beats pure semantic for IDs & symbols. |
| **Grounding / citations** | Show sources; measure citation correctness. |
| **Guardrails** | Off-topic, toxic, PII — retrieval doesn’t fix policy. |

---

## Resources

### Core

- [Google — Embeddings](https://ai.google.dev/docs/embeddings_guide)
- [Google Cloud — RAG](https://cloud.google.com/use-cases/retrieval-augmented-generation)
- [LangChain — RAG](https://python.langchain.com/docs/tutorials/rag/) (or LlamaIndex equivalent)

### Chunking & hybrid

- Search **“chunking strategies RAG”** — one vendor blog + one paper summary.

### Eval

- Search **“RAG evaluation retrieval metrics”** — nDCG, hit rate, faithfulness.

### OWASP

- [LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

---

## Apply → weekly practice

**[Week 7](../course-weeks/week-07/README.md)** — design + stub pipeline on course corpus.  
**[Week 8](../course-weeks/week-08/README.md)** — **MIDTERM**: deeper build + write-up.
