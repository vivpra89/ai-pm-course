# Prototypes — ship thin slices safely

*Estimated study: 3–5 hours · aligns with Weeks 11–12.*

---

## Outcomes

- **Scope** a demo that proves one hypothesis — not a science fair.  
- Use **gradio / streamlit / fastapi** for internal prototypes — secrets & env hygiene.  
- **Threat model** before exposing even an internal URL.  

---

## Topic map

| Topic | Core idea |
|-------|-----------|
| **Scope** | One user journey, one dataset, one success metric. |
| **gradio / streamlit** | Fast UI; don’t promote to prod without review. |
| **Secrets** | API keys in env, not repo; rotation story. |
| **Observability** | Log prompts? PII? redaction before any shared logging. |

---

## Resources

- [Gradio quickstart](https://www.gradio.app/guides/quickstart)
- [Streamlit](https://docs.streamlit.io/)
- [12-factor app — config](https://12factor.net/config)

---

## Apply → weekly practice

**[Week 11](../course-weeks/week-11/README.md)** — prototype spec + risk list.  
**[Week 12](../course-weeks/week-12/README.md)** — build or script-mock + demo notes.
