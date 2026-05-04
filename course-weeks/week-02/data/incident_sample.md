# Synthetic incident — Week 02–03 prompt practice

**Status:** ACTIVE — internal bridge  
**Opened:** 2025-04-12 09:10 UTC  
**Reporter:** NOC — synthetic  

## Summary (raw)

Search latency P95 increased from 180ms to 940ms in `us-west-2` for enterprise tenants only. Mobile web worse than desktop. Initial suspicion: index shard hot-spot after a config deploy at 08:40 UTC. A Redis cluster showed elevated CPU but not saturation. One hypothesis is a bad rollout of feature flag `exp_ai_sidebar` causing extra retrieval calls on doc open events.

## Customer impact

No confirmed data loss. Support queue +22% vs prior week; three accounts threatened downgrade in chat (unverified severity). SMB tenants largely unaffected.

## Hypotheses / unknowns

- Correlation vs causation: AI sidebar experiment may be coincident with index issues.
- Sample size: enterprise-only pattern might reflect traffic skew not root cause.

## Actions taken

- Rolled back config deploy at 09:55 UTC — partial improvement (P95 ~410ms).
- Increased replica count for search tier — monitoring overnight.

## Links

- Synthetic dashboard ID `dash_90210` (not real).
