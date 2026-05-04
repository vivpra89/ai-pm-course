# SQL & data validation — truth beats prose

*Estimated study: 4–6 hours · aligns with Weeks 4–5.*

---

## Outcomes

- Treat **SQL (or approved metrics)** as **source of truth** — LLM proposes, you validate.  
- Define **numerators / denominators / windows** before debating charts.  
- Run **text-to-SQL** with schema grounding, read-only roles, LIMIT, allowlists — treat generated SQL as untrusted code.  

---

## Topic map

| Topic | Core idea |
|-------|-----------|
| **Metric definitions** | Ambiguous KPIs (“active user”) destroy cross-team alignment. |
| **JOINs & filters** | Wrong joins = wrong narrative — always sanity-check row counts. |
| **Text-to-SQL workflow** | Schema snippet → query → sandbox execute → summarize. |
| **Governance** | PII, destructive queries, audit — controls before automation. |
| **Semantic layer** | Org-approved metric definitions the model must map to. |

---

## Resources

### SQL mechanics

- [SQLite SELECT / JOIN](https://www.sqlite.org/lang_select.html) (reference)
- YouTube: **“SQL joins explained”** — pick a short visual tutorial.

### PM analytics

- Search **“metric definition numerator denominator”** — one solid article on KPI hygiene.

### LLM + SQL risks

- Search **“text to SQL pitfalls”** — wrong joins, dates, leakage.
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — data exfiltration / excessive agency angles.

### Semantic layer (concept)

- Search **“semantic layer metrics dbt”** — why governed definitions matter.

---

## Apply → weekly practice

**[Week 4](../course-weeks/week-04/README.md)** — NL → SQL on CloudNote.  
**[Week 5](../course-weeks/week-05/README.md)** — threat model + drills.

**Data:** [`practice-env`](../practice-env/README.md) — `cloudnote.db`, `sql/faang_style_drills.sql`.
