# Practice environment — CloudNote dummy SaaS

Use this folder for **hands-on labs** aligned with `TPM-PM-AI-Technical-Learning-Plan.md`: SQL validation, plots, text-to-SQL drills (with an LLM later), RAG over `corpus/`, and chatbot prototypes.

Treat all data as **synthetic**; do not paste real employer customer data here without clearance.

---

## What’s included

| Path | Purpose |
|------|---------|
| **`data/cloudnote.db`** | SQLite database file (created by the build script; listed in `.gitignore` if absent until you build) |
| **`scripts/build_dummy_db.py`** | Creates/regenerates the DB with fixed **`RNG_SEED=42`** so numbers stay reproducible |
| **`sql/faang_style_drills.sql`** | Prompt ideas for analytical SQL (metrics, experiments, support)—you write the queries |
| **`corpus/*.md`** | Short Markdown “policy” docs for **RAG** labs |
| **`labs/explore_metrics.py`** | Minimal Python: connects to SQLite and prints one rollup |
| **`requirements.txt`** | Python deps for labs/plots (pandas, matplotlib, jupyter, …) |
| **`.env.example`** | Template for API keys when you add LLM-based labs later |

**Scenario:** fictional B2B **CloudNote** — users, subscriptions (MRR), product events, A/B experiments, support tickets.

---

## Directory layout (where things live)

```
practice-env/
├── README.md                 ← this file
├── requirements.txt
├── .env.example
├── scripts/
│   └── build_dummy_db.py    ← run from practice-env (see below)
├── data/
│   └── cloudnote.db          ← produced by build script
├── sql/
│   └── faang_style_drills.sql
├── corpus/
│   ├── product_faq.md
│   └── internal_rfc_ai_sidebar.md
└── labs/
    └── explore_metrics.py
```

Always run terminal commands with your **current working directory** set to `practice-env` unless a lab tells you otherwise (`cd practice-env`).

---

## Prerequisites

| Requirement | Notes |
|-------------|--------|
| **Python 3.10+** (3.11+ recommended) | `python3 --version` |
| **`sqlite3` CLI** (optional but useful) | macOS/Linux often preinstalled; Windows: install SQLite or use Python only |
| **pip / venv** | Standard Python tooling |

---

## End-to-end setup (first time)

Do these steps once per machine (or once per clean clone).

### 1. Go to the practice folder

```bash
cd path/to/AI_PM_course/practice-env
```

### 2. Create a virtual environment

Isolates packages so this course does not clash with other Python projects.

```bash
python3 -m venv venv
```

**Activate:**

- **macOS / Linux:** `source venv/bin/activate`
- **Windows (cmd):** `venv\Scripts\activate.bat`
- **Windows (PowerShell):** `venv\Scripts\Activate.ps1`

Your prompt should usually show `(venv)`.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

This pulls in **pandas**, **matplotlib**, **jupyter**, etc., for later weeks. SQL-only practice does not strictly need everything, but installing once avoids errors when you extend labs.

### 4. Build the database

```bash
python scripts/build_dummy_db.py
```

Expected: a message like `Wrote .../data/cloudnote.db (users=800, events=..., tickets=...)`.

If **`data/`** did not exist, the script creates it.

### 5. Sanity checks

**SQLite CLI** — lists tables:

```bash
sqlite3 data/cloudnote.db "SELECT name FROM sqlite_master WHERE type='table' ORDER BY 1;"
```

**Python lab:**

```bash
python labs/explore_metrics.py
```

You should see a small **MRR roll-up by segment** printed as text.

---

## How to use each piece

### A. SQLite database (`data/cloudnote.db`)

**When:** Weeks focused on SQL, metrics, plots, text-to-SQL, or any “validate with data” exercise.

**Rules of thumb**

1. Treat the DB as **source of truth**—if an LLM suggests SQL, **you** review and run it (read-only mindset).
2. Prefer **`LIMIT`** while exploring row shape.
3. `event_ts` and dates are stored as **TEXT** (ISO-like strings); compare with string ranges or use SQLite date functions consistently.

**Open an interactive shell:**

```bash
sqlite3 data/cloudnote.db
```

Useful inside the shell:

```sql
.tables
.schema dim_user
.headers on
.mode column
```

**Exit:** `.quit`

### B. Drill prompts (`sql/faang_style_drills.sql`)

**When:** You practice turning vague PM questions into **metric definitions** + SQL.

**How**

1. Read a bullet in the file **without** looking at answers (there are none—prompts only).
2. Write the metric in **English** (numerator, denominator, time window).
3. Write SQL against `cloudnote.db`.
4. Run it; if rows look wrong, fix joins/filters before trusting narrative.

### C. Corpus (`corpus/`)

**When:** RAG labs (chunking, retrieval, citations).

**How**

1. Point your RAG tutorial/script at these `.md` files as the **knowledge base**.
2. Ask questions whose answers appear in the FAQ vs the RFC (test retrieval vs hallucination).
3. Optionally duplicate files into `corpus/` and edit—keep copies separate from the originals if you want a clean baseline.

### D. Lab script (`labs/explore_metrics.py`)

**When:** First pandas/SQL connection smoke test; starting point for plotting weeks.

**How**

```bash
python labs/explore_metrics.py
```

**Extend:** copy the file or import patterns into a Jupyter notebook; swap in your own SQL and add matplotlib/plotly charts.

### E. API keys (later)

**When:** Text-to-SQL via API, embeddings for RAG, chatbot demos.

**How**

```bash
cp .env.example .env
# Edit .env — uncomment and set OPENAI_API_KEY or ANTHROPIC_API_KEY as needed
```

Load `.env` from Python only if your lab script uses `python-dotenv` (add it to requirements when you need it). SQL-only weeks skip this entirely.

---

## Example: SQL session from scratch

After setup and build:

```bash
cd practice-env
source venv/bin/activate   # if not already active
sqlite3 data/cloudnote.db
```

```sql
SELECT segment, COUNT(*) AS n_users
FROM dim_user
GROUP BY segment;
```

```sql
SELECT event_name, COUNT(*) AS n
FROM fct_product_event
GROUP BY event_name
ORDER BY n DESC
LIMIT 10;
```

Adjust filters as your weekly assignments require.

---

## Example: text-to-SQL workflow with an LLM (when ready)

1. Export a **small schema cheat-sheet** (you can start from the schema one-liner below).
2. In your LLM chat, paste **only** schema + your question; ask for **SELECT-only** SQL with **`LIMIT`**.
3. **Review** the SQL—watch for wrong joins, cartesian products, or leaking columns you did not intend.
4. Run in `sqlite3` or pandas **yourself**; never treat model output as audited facts until executed.

---

## Schema cheat-sheet (paste into LLM prompts)

```
Tables:
- dim_user(user_id, signup_ts, country, segment)  -- segment: smb | mid | enterprise
- fct_subscription(user_id, plan_tier, mrr_usd, period_start, churn_date)
- fct_product_event(event_id, user_id, event_ts, event_name, platform)
- dim_experiment(experiment_id, name, start_date, end_date)
- fct_experiment_exposure(user_id, experiment_id, variant, first_seen_ts)  -- variant: control | treatment
- fct_support_ticket(ticket_id, user_id, created_ts, category, priority, resolution_minutes)

Events examples: page_view, doc_open, checkout_complete, error_boundary, ...
Platforms: web, ios, android
```

---

## Rebuilding the database

Run again anytime you want a **clean** copy:

```bash
python scripts/build_dummy_db.py
```

Optional custom output path:

```bash
python scripts/build_dummy_db.py --out data/cloudnote.db
```

Same seed ⇒ **same data** each time (good for comparing notebooks across machines).

---

## Troubleshooting

| Problem | What to try |
|---------|-------------|
| **`No module named pandas`** | Activate `venv` and run `pip install -r requirements.txt` |
| **`cloudnote.db` missing or old** | Run `python scripts/build_dummy_db.py` from `practice-env` |
| **`sqlite3: command not found`** | Install SQLite tools or use Python only: `python -c "import sqlite3; print(sqlite3.connect('data/cloudnote.db').execute('select 1').fetchone())"` from `practice-env` |
| **Wrong results / empty joins** | Print `COUNT(*)`, check join keys (`user_id`), verify date filters on `event_ts` |
| **Script can’t find `data/cloudnote.db`** | Your shell might not be in `practice-env`; `cd` there or use absolute paths |
| **Permission errors on Windows venv** | Run terminal as normal user; try `python -m venv venv` again from `practice-env` |

---

## Jupyter (optional)

```bash
source venv/bin/activate
jupyter lab
```

Create a notebook in `labs/` or elsewhere; use:

```python
import sqlite3
import pandas as pd
conn = sqlite3.connect("data/cloudnote.db")
pd.read_sql_query("SELECT * FROM dim_user LIMIT 5", conn)
```

Paths are relative to the notebook’s working directory—often easiest to **change Jupyter’s cwd** to `practice-env` or use absolute paths.

---

## How this maps to the course

| Course topic | What to do here |
|--------------|-----------------|
| **SQL + validation** | Answer prompts in `sql/faang_style_drills.sql`; define metrics before coding |
| **Plots** | Extend `labs/explore_metrics.py` or a notebook; chart from query results |
| **RAG** | Chunk/embed/search `corpus/`; compare with vs without retrieval |
| **Text-to-SQL** | Schema cheat-sheet + LLM proposal + **your** execution |
| **Chatbot** | Thin Streamlit/Gradio app: optional read-only SQL + optional RAG over `corpus/` |

---

## Quick reference commands

```bash
cd practice-env && source venv/bin/activate
python scripts/build_dummy_db.py
python labs/explore_metrics.py
sqlite3 data/cloudnote.db
```

---

For the interactive course hub (browser), rebuild static HTML after README changes: `python3 scripts/build_static_site.py` from the repo root.
