"""Minimal lab: load CloudNote SQLite and print a simple rollup (pandas).

Run from practice-env root:
  python labs/explore_metrics.py

Requires: pip install pandas (see ../requirements.txt)
"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "cloudnote.db"


def main() -> None:
    if not DB.exists():
        raise SystemExit(f"Missing {DB}. Run: python scripts/build_dummy_db.py")

    import sqlite3

    conn = sqlite3.connect(DB)

    q = """
    SELECT u.segment,
           COUNT(DISTINCT u.user_id) AS users,
           ROUND(AVG(s.mrr_usd), 1) AS avg_mrr,
           SUM(CASE WHEN s.churn_date IS NOT NULL THEN 1 ELSE 0 END) AS churned_subs
    FROM dim_user u
    JOIN fct_subscription s ON s.user_id = u.user_id
    GROUP BY u.segment
    ORDER BY u.segment
    """
    df = pd.read_sql_query(q, conn)
    conn.close()
    print("MRR roll-up by segment (dummy CloudNote data)\n")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
