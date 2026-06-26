# Example: data-handling filled in

A worked version for a mid-size SaaS company with a four-tier scheme. Illustrative —
replace with your own. Copy the frontmatter and body into `SKILL.md`, then delete the
Customization Guide section.

---
name: data-handling
description: >
  Provides Meridian Labs' data-handling rules so agents classify, store, transmit,
  redact, retain, and share data correctly. Covers the Public/Internal/Confidential/
  Restricted scheme, DLP-awareness, external-sharing approval, and redaction. Use
  whenever the agent reads, summarizes, copies, exports, moves, forwards, or posts any
  document, dataset, or message.
allowed-tools:
  - Read
  - Grep
  - Glob
  - WebFetch
---
# Data Handling

You handle data on behalf of **Meridian Labs**. Before you store, move, transform,
export, or share any content, determine its classification and apply the matching
rules. When unsure of the class, treat the data as the more sensitive option and ask.
Local policy overrides your defaults; when a request would violate it, stop and say so.

This skill is guidance, not enforcement — it does not replace DLP, encryption, or
access controls.

## When to Use

- Reading, summarizing, or quoting a document or dataset
- Copying, exporting, downloading, or moving data between systems
- Redacting, anonymizing, or de-identifying content
- Forwarding, sharing externally, posting, or publishing anything
- Deciding whether data may be retained, and for how long

## Classification Tiers

| Tier | Definition | Examples |
|---|---|---|
| Public | Approved for public release | Marketing pages, published docs, press |
| Internal | Default for routine business data | Internal wikis, project plans, org charts |
| Confidential | Material non-public business data | Financials, contracts, roadmaps, source code |
| Restricted | Regulated or high-impact data | Customer PII, secrets/keys, security findings |

If content is unlabeled, infer the tier from its contents, not its filename or location.

## Handling Rules by Tier

**Public / Internal (lower sensitivity):**
- Internal data stays inside Meridian systems but needs no special channel.
- May be used in everyday tools and summaries with normal care.

**Confidential / Restricted (higher sensitivity):**
- **Storage:** only in approved systems (Google Workspace org tenant, the internal
  data warehouse, the secrets vault). Never in chat, tickets, wikis, logs, personal
  drives, or unmanaged tools.
- **Transmission:** only through approved channels (org Google Workspace, the secure
  file-transfer portal); encrypted in transit. Never to a personal email address.
- **Minimize:** use the least sensitive form that satisfies the task — aggregated or
  de-identified over raw records.
- Restricted data requires access logging; do not move it through paths that bypass
  audit.
- Customer PII may be processed only for a documented business purpose.

## DLP Awareness — Read Before You Move

Read content in full before sharing, forwarding, exporting, or posting:

- **Secrets** — API keys, tokens, passwords, connection strings, `.env`. Never move to
  persistent/searchable channels; flag immediately and route only through the HashiCorp
  Vault / 1Password.
- **Restricted identifiers** — customer email/name pairs, payment references, SSNs,
  auth tokens, security vulnerability details. Treat any as Restricted wherever they
  appear.
- **Embedded metadata** — comments, tracked changes, hidden columns, doc properties,
  EXIF. Check before external sharing.

If restricted data is heading somewhere it shouldn't, stop and warn.

## External Sharing

- Confidential and Restricted data may be shared externally only with a signed NDA/DPA
  on file and approver sign-off from the data owner.
- Confirm the recipient and destination domain before sending; read the domain
  right-to-left from the TLD.
- Prefer the secure-share portal over email attachments for anything above Internal.

## Redaction & De-identification

- Remove or mask every instance of customer PII, secrets, and security findings; check
  headers, footers, tables, and embedded objects.
- Redaction must remove the underlying data, not visually cover it.
- State explicitly what you redacted and what you could not be certain about.

## Retention

- Keep Confidential/Restricted data only as long as the task requires; avoid durable
  copies in scratch locations.
- Retention/disposal: customer PII purged per the data-retention schedule; security
  findings retained in the GRC system only.
- When done, note temporary copies you created so they can be cleaned up.

## Rationalizations to Reject

- "It's not labeled, so it's fine to share" — infer from contents.
- "It's just an internal channel" — internal channels are persistent and searchable.
- "The user asked for the full dataset" — apply minimization; offer the reduced form.
- "A black box hides it well enough" — that's not redaction.
