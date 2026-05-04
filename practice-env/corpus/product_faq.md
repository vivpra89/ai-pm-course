# CloudNote — Product FAQ (dummy corpus for RAG practice)

## What is CloudNote?

CloudNote is a B2B workspace for documents, wikis, and lightweight project tracking. AI features are optional and governed by org-level policies.

## Plans and billing

- **SMB**: up to 25 seats, standard SSO, 100 GB pooled storage.
- **Mid-market**: up to 200 seats, SAML SSO, audit log export (CSV), 2 TB pooled storage.
- **Enterprise**: unlimited seats (fair-use), SCIM provisioning, regional data residency options, dedicated support SLAs.

Annual billing receives a 15% discount when prepaid. Downgrades take effect at the next renewal.

## AI Sidebar (beta)

The AI Sidebar can summarize threads, draft replies, and extract action items. It may retrieve **only** documents the user already has access to. Org admins can disable AI entirely or restrict summarization to internal docs.

## Rate limits (API)

REST API defaults: 300 requests per minute per OAuth client, burst up to 600. Heavy export jobs should use the async export endpoint which returns a job ID.

## Data retention

Trash is retained 30 days. Audit logs for enterprise are retained 7 years unless a shorter period is contracted.
