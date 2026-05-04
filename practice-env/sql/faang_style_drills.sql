-- CloudNote dummy DB — analytical drills (FAANG-style: clarify metric, then query)
-- Run: sqlite3 ../data/cloudnote.db < faang_style_drills.sql
-- Or paste queries one at a time.

-- ---------------------------------------------------------------------------
-- 1) North star sanity
-- "Define weekly active users (WAU) as distinct users with any event in the week."
-- Drill: last 4 full weeks of data in your DB window.

-- 2) Revenue risk
-- MRR by segment; count of subscribers churned in last 90 days vs active.

-- 3) Experiment readout (template — adjust dates to match dim_experiment)
-- Compare treatment vs control for conversion: users with checkout_complete
-- after first exposure, within 14 days, per experiment.

-- 4) Support load
-- Tickets created per week; p90 resolution time for enterprise vs smb (SQL percentile approx:
-- use subquery or export to pandas).

-- 5) Product quality proxy
-- Rate of error_boundary events per 1k doc_open by platform.

-- Example starter (uncomment to run):

-- SELECT segment, COUNT(*) AS users, SUM(mrr_usd) AS mrr
-- FROM dim_user u
-- JOIN fct_subscription s ON s.user_id = u.user_id
-- GROUP BY segment;
