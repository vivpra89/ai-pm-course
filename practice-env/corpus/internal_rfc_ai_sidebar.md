# RFC-1842 — AI Sidebar retrieval (internal excerpt, dummy)

## Problem

Users expect answers grounded in their workspace. A naive LLM will hallucinate policies and invented ticket IDs.

## Proposed architecture

1. **Query understanding**: classify intent (summarize, Q&A, draft email).
2. **Retrieval**: hybrid search (BM25 + embeddings) over permitted doc chunks; filter by ACL before ranking.
3. **Generation**: LLM must cite chunk IDs in its trace; UI shows citations only from retrieved set.

## Risks

- **Indirect prompt injection**: malicious text inside a shared doc could steer the model. Mitigation: strip HTML, sandbox rendering, and retrieval-level scoring penalties for known injection patterns (heuristic).
- **Cost**: average 4 retrieved chunks × 800 tokens + 500 output; target P95 latency 2.5s warm.

## Launch criteria

Offline eval: 200 golden Q&A pairs; citation accuracy ≥ 92%; refusal rate on policy violations ≥ 99%.
