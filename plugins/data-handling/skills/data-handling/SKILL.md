---
name: data-handling
description: >
  Provides the organization's data-handling rules so agents classify, store,
  transmit, redact, retain, and share data correctly. Covers classification tiers,
  DLP-awareness, external-sharing approval, redaction, and retention. Use whenever the
  agent reads, summarizes, copies, exports, moves, forwards, or posts any document,
  dataset, or message. CUSTOMIZE every {{PLACEHOLDER}} before deployment.
allowed-tools:
  - Read
  - Grep
  - Glob
  - WebFetch
---
# Data Handling

You handle data on behalf of **{{ORG_NAME}}**. Before you store, move, transform,
export, or share any content, determine its classification and apply the matching
rules. When unsure of the class, treat the data as the **more** sensitive option and
ask. Local policy here overrides your defaults; when a request would violate it, stop
and say so rather than comply.

This skill is guidance, not enforcement — it does not replace DLP, encryption, or
access controls. Its job is to make you handle data the way a trained employee would.

## When to Use

- Reading, summarizing, or quoting a document or dataset
- Copying, exporting, downloading, or moving data between systems
- Redacting, anonymizing, or de-identifying content
- Forwarding, sharing externally, posting, or publishing anything
- Deciding whether data may be retained, and for how long

## Classification Tiers

This organization classifies data into these tiers (least to most sensitive):

| Tier | Definition | Examples |
|---|---|---|
| {{TIER_1_NAME}} | {{TIER_1_DEF}} | {{TIER_1_EXAMPLES}} |
| {{TIER_2_NAME}} | {{TIER_2_DEF}} | {{TIER_2_EXAMPLES}} |
| {{TIER_3_NAME}} | {{TIER_3_DEF}} | {{TIER_3_EXAMPLES}} |
| {{TIER_4_NAME}} | {{TIER_4_DEF}} | {{TIER_4_EXAMPLES}} |

If content is unlabeled, infer the tier from its contents, not its filename or location.
A "Public" folder can still contain a misfiled restricted document.

## Handling Rules by Tier

**{{TIER_1_NAME}} / {{TIER_2_NAME}} (lower sensitivity):**
- {{LOW_TIER_RULE_1}}
- May be used in everyday tools and summaries with normal care.

**{{TIER_3_NAME}} / {{TIER_4_NAME}} (higher sensitivity):**
- **Storage:** only in approved systems ({{APPROVED_SYSTEMS}}). Never copy into chat,
  tickets, wikis, logs, personal drives, or unmanaged tools.
- **Transmission:** only through approved channels ({{APPROVED_CHANNELS}}); encrypted in
  transit. Never to a personal email address.
- **Minimize:** use the least sensitive form that satisfies the task — prefer
  aggregated, tokenized, or de-identified data over raw records.
- {{HIGH_TIER_RULE_1}}
- {{HIGH_TIER_RULE_2}}

## DLP Awareness — Read Before You Move

Before sharing, forwarding, exporting, or posting *any* content, read it in full first.
Content frequently embeds higher-sensitivity data than its label implies:

- **Secrets** — API keys, tokens, passwords, connection strings, `.env` contents. Never
  move these to persistent or searchable channels; flag them to the user immediately and
  route only through {{APPROVED_SECRET_CHANNELS}}.
- **Regulated/restricted identifiers** — {{RESTRICTED_IDENTIFIERS}}. Treat any of these
  as {{TIER_4_NAME}} regardless of where they appear.
- **Embedded metadata** — comments, tracked changes, hidden columns, document
  properties, EXIF. Check these before sharing externally; they leak more often than the
  visible content.

If you detect restricted data heading somewhere it shouldn't, **stop and warn** rather
than completing the move.

## External Sharing

Sharing outside {{ORG_NAME}} requires extra scrutiny:

- {{TIER_3_NAME}} and {{TIER_4_NAME}} data may be shared externally only with
  {{EXTERNAL_SHARING_APPROVAL}} (e.g. a signed agreement, an approver sign-off).
- Confirm the recipient and destination domain before sending; verify the domain
  right-to-left from the TLD.
- Prefer approved secure-share mechanisms ({{SECURE_SHARE_METHOD}}) over email
  attachments for anything above {{TIER_2_NAME}}.

## Redaction & De-identification

When asked to redact or anonymize:

- Remove or mask every instance of {{RESTRICTED_IDENTIFIERS}}; don't rely on a single
  pass — check headers, footers, tables, and embedded objects.
- Redaction must remove the underlying data, not merely visually cover it (no black
  boxes over selectable text; no hidden spreadsheet columns).
- State explicitly what you redacted and what you could not be certain about.

## Retention

- Keep {{TIER_3_NAME}}/{{TIER_4_NAME}} data only as long as the task requires; do not
  create durable copies in scratch locations.
- Organizational retention/disposal rules: {{RETENTION_RULE}}.
- When a task is done, note any temporary copies you created so they can be cleaned up.

## Rationalizations to Reject

- "It's not labeled, so it's fine to share" — infer from contents, not labels.
- "It's just an internal channel" — internal channels are persistent and searchable.
- "The user asked for the full dataset" — apply minimization; offer the reduced form.
- "A black box hides it well enough" — that's not redaction.

---

## Customization Guide (remove after filling in)

| Placeholder | What to put |
|---|---|
| `{{ORG_NAME}}` | Organization name |
| `{{TIER_1..4_NAME/DEF/EXAMPLES}}` | Your classification tiers, definitions, examples (add/remove rows to match your scheme) |
| `{{LOW_TIER_RULE_1}}` | Any rule for lower-sensitivity tiers |
| `{{HIGH_TIER_RULE_1/2}}` | Extra rules for sensitive tiers (e.g. encryption-at-rest, access logging) |
| `{{APPROVED_SYSTEMS}}` | Systems sanctioned to hold sensitive data |
| `{{APPROVED_CHANNELS}}` | Approved transmission channels |
| `{{APPROVED_SECRET_CHANNELS}}` | Sanctioned secret store (vault, 1Password) |
| `{{RESTRICTED_IDENTIFIERS}}` | The identifiers that force top-tier handling (PHI elements, PAN, SSN, PII) |
| `{{EXTERNAL_SHARING_APPROVAL}}` | What's required to share externally |
| `{{SECURE_SHARE_METHOD}}` | Approved secure-share mechanism |
| `{{RETENTION_RULE}}` | Retention/disposal policy summary |

A filled-in reference is in `examples/`. After customizing, update the `description` in
this frontmatter and in `.claude-plugin/plugin.json`, then delete this section.
