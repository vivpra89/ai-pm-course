#!/usr/bin/env python3
"""
Build a reproducible SQLite database for TPM/PM AI practice (FAANG-style drills).

Scenario: "CloudNote" — B2B collaboration SaaS with subscriptions, product events,
experiments, and support tickets. Seed is fixed (RNG seed=42).

Usage:
  python scripts/build_dummy_db.py
Output:
  ../data/cloudnote.db
"""

from __future__ import annotations

import argparse
import random
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

RNG_SEED = 42

COUNTRIES = ["US", "US", "US", "GB", "DE", "IN", "JP", "BR"]  # weighted US
SEGMENTS = ["smb", "mid", "enterprise"]
PLATFORMS = ["web", "ios", "android"]
EVENT_NAMES = [
    "page_view",
    "doc_open",
    "doc_share",
    "search_query",
    "upgrade_click",
    "checkout_start",
    "checkout_complete",
    "error_boundary",
]
EXP_NAMES = [("exp_onboarding_v3", "2025-01-15", "2025-04-01"), ("exp_ai_sidebar", "2025-02-01", "2025-05-01")]
TICKET_CATEGORIES = ["billing", "bugs", "how_to", "performance", "account"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data" / "cloudnote.db",
        help="Output SQLite path",
    )
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)

    random.seed(RNG_SEED)

    base = datetime(2024, 6, 1, 0, 0, 0)
    n_users = 800

    users = []
    for i in range(1, n_users + 1):
        signup_offset_days = random.randint(0, 300)
        signup = base + timedelta(days=signup_offset_days)
        seg_roll = random.random()
        if seg_roll < 0.72:
            segment = "smb"
        elif seg_roll < 0.92:
            segment = "mid"
        else:
            segment = "enterprise"
        users.append(
            {
                "user_id": f"u_{i:05d}",
                "signup_ts": signup.isoformat(sep=" "),
                "country": random.choice(COUNTRIES),
                "segment": segment,
            }
        )

    subscriptions = []
    for u in users:
        # MRR by segment + noise
        base_mrr = {"smb": 29, "mid": 99, "enterprise": 499}[u["segment"]]
        mrr = max(9, int(random.gauss(base_mrr, base_mrr * 0.15)))
        churn_prob = {"smb": 0.08, "mid": 0.05, "enterprise": 0.02}[u["segment"]]
        churned = random.random() < churn_prob
        churn_date = None
        start = datetime.fromisoformat(u["signup_ts"]) + timedelta(days=random.randint(0, 14))
        if churned:
            churn_date = start + timedelta(days=random.randint(30, 220))
        subscriptions.append(
            {
                "user_id": u["user_id"],
                "plan_tier": u["segment"],
                "mrr_usd": mrr,
                "period_start": start.date().isoformat(),
                "churn_date": churn_date.date().isoformat() if churn_date else None,
            }
        )

    events = []
    eid = 0
    for u in users:
        signup_dt = datetime.fromisoformat(u["signup_ts"])
        end_activity = datetime(2025, 5, 1)
        if signup_dt > end_activity:
            continue
        n_events = random.randint(5, 120)
        for _ in range(n_events):
            eid += 1
            ts = signup_dt + timedelta(
                minutes=random.randint(0, int((end_activity - signup_dt).total_seconds() // 60))
            )
            ev = random.choices(
                EVENT_NAMES,
                weights=[20, 25, 10, 15, 4, 3, 2, 1],
            )[0]
            events.append(
                {
                    "event_id": eid,
                    "user_id": u["user_id"],
                    "event_ts": ts.isoformat(sep=" "),
                    "event_name": ev,
                    "platform": random.choice(PLATFORMS),
                }
            )

    experiments = []
    exposures = []
    for exp_id, (name, s, e) in enumerate(EXP_NAMES, start=1):
        experiments.append({"experiment_id": exp_id, "name": name, "start_date": s, "end_date": e})
        start_dt = datetime.fromisoformat(s + "T00:00:00")
        end_dt = datetime.fromisoformat(e + "T00:00:00")
        for u in users:
            su = datetime.fromisoformat(u["signup_ts"])
            if su > end_dt or su < start_dt - timedelta(days=200):
                continue
            if random.random() < 0.4:
                exposures.append(
                    {
                        "user_id": u["user_id"],
                        "experiment_id": exp_id,
                        "variant": random.choice(["control", "treatment"]),
                        "first_seen_ts": (su + timedelta(days=random.randint(0, 30))).isoformat(sep=" "),
                    }
                )

    tickets = []
    for tid in range(1, 451):
        u = random.choice(users)
        created = datetime(2024, 8, 1) + timedelta(days=random.randint(0, 240), hours=random.randint(0, 23))
        cat = random.choice(TICKET_CATEGORIES)
        prio = random.choices(["p0", "p1", "p2", "p3"], weights=[2, 12, 35, 51])[0]
        resolution = None if random.random() < 0.06 else random.randint(15, 3600 * 48)
        enterprise_slow = u["segment"] == "enterprise" and random.random() < 0.15
        if resolution and enterprise_slow:
            resolution = int(resolution * random.uniform(1.2, 2.5))
        tickets.append(
            {
                "ticket_id": tid,
                "user_id": u["user_id"],
                "created_ts": created.isoformat(sep=" "),
                "category": cat,
                "priority": prio,
                "resolution_minutes": resolution,
            }
        )

    conn = sqlite3.connect(args.out)
    cur = conn.cursor()
    cur.executescript(
        """
        PRAGMA foreign_keys = ON;
        DROP TABLE IF EXISTS fct_support_ticket;
        DROP TABLE IF EXISTS fct_experiment_exposure;
        DROP TABLE IF EXISTS dim_experiment;
        DROP TABLE IF EXISTS fct_product_event;
        DROP TABLE IF EXISTS fct_subscription;
        DROP TABLE IF EXISTS dim_user;

        CREATE TABLE dim_user (
          user_id TEXT PRIMARY KEY,
          signup_ts TEXT NOT NULL,
          country TEXT NOT NULL,
          segment TEXT NOT NULL CHECK (segment IN ('smb','mid','enterprise'))
        );

        CREATE TABLE fct_subscription (
          user_id TEXT NOT NULL REFERENCES dim_user(user_id),
          plan_tier TEXT NOT NULL,
          mrr_usd INTEGER NOT NULL,
          period_start TEXT NOT NULL,
          churn_date TEXT,
          PRIMARY KEY (user_id, period_start)
        );

        CREATE TABLE fct_product_event (
          event_id INTEGER PRIMARY KEY,
          user_id TEXT NOT NULL REFERENCES dim_user(user_id),
          event_ts TEXT NOT NULL,
          event_name TEXT NOT NULL,
          platform TEXT NOT NULL
        );
        CREATE INDEX idx_event_user_ts ON fct_product_event(user_id, event_ts);
        CREATE INDEX idx_event_name ON fct_product_event(event_name);

        CREATE TABLE dim_experiment (
          experiment_id INTEGER PRIMARY KEY,
          name TEXT NOT NULL UNIQUE,
          start_date TEXT NOT NULL,
          end_date TEXT NOT NULL
        );

        CREATE TABLE fct_experiment_exposure (
          user_id TEXT NOT NULL REFERENCES dim_user(user_id),
          experiment_id INTEGER NOT NULL REFERENCES dim_experiment(experiment_id),
          variant TEXT NOT NULL CHECK (variant IN ('control','treatment')),
          first_seen_ts TEXT NOT NULL,
          PRIMARY KEY (user_id, experiment_id)
        );

        CREATE TABLE fct_support_ticket (
          ticket_id INTEGER PRIMARY KEY,
          user_id TEXT NOT NULL REFERENCES dim_user(user_id),
          created_ts TEXT NOT NULL,
          category TEXT NOT NULL,
          priority TEXT NOT NULL,
          resolution_minutes INTEGER
        );
        CREATE INDEX idx_ticket_created ON fct_support_ticket(created_ts);
        """
    )

    cur.executemany(
        "INSERT INTO dim_user VALUES (:user_id, :signup_ts, :country, :segment)",
        users,
    )
    cur.executemany(
        """
        INSERT INTO fct_subscription (user_id, plan_tier, mrr_usd, period_start, churn_date)
        VALUES (:user_id, :plan_tier, :mrr_usd, :period_start, :churn_date)
        """,
        subscriptions,
    )
    cur.executemany(
        """
        INSERT INTO fct_product_event (event_id, user_id, event_ts, event_name, platform)
        VALUES (:event_id, :user_id, :event_ts, :event_name, :platform)
        """,
        events,
    )
    cur.executemany(
        "INSERT INTO dim_experiment VALUES (:experiment_id, :name, :start_date, :end_date)",
        experiments,
    )
    cur.executemany(
        """
        INSERT INTO fct_experiment_exposure (user_id, experiment_id, variant, first_seen_ts)
        VALUES (:user_id, :experiment_id, :variant, :first_seen_ts)
        """,
        exposures,
    )
    cur.executemany(
        """
        INSERT INTO fct_support_ticket
        (ticket_id, user_id, created_ts, category, priority, resolution_minutes)
        VALUES (:ticket_id, :user_id, :created_ts, :category, :priority, :resolution_minutes)
        """,
        tickets,
    )

    conn.commit()
    conn.close()
    print(f"Wrote {args.out} (users={len(users)}, events={len(events)}, tickets={len(tickets)})")


if __name__ == "__main__":
    main()
