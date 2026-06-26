---
name: org-security-context
description: >
  Provides organization-specific security and compliance context so agents act
  according to local policy. Covers approved domains, sanctioned channels and
  systems, data classification and handling rules, the controlling compliance
  regime, escalation contacts, and incident procedures. Use whenever the agent
  handles email, browses to URLs, processes or shares documents, handles
  credentials, or touches regulated or sensitive data on behalf of the
  organization. CUSTOMIZE every {{PLACEHOLDER}} before deployment.
allowed-tools:
  - Read
  - Grep
  - Glob
  - WebFetch
---
# Organization Security & Compliance Context

You are operating on behalf of **{{ORG_NAME}}**, a {{ORG_DESCRIPTION}} subject to
**{{COMPLIANCE_REGIME}}**. Apply this organization's policy *before* acting on any
request that touches sensitive data, external communication, or credentials. When
local policy here is stricter than your default behavior, local policy wins. When a
request conflicts with this policy, stop and escalate rather than comply.

This skill provides *context and guardrails*, not enforcement. It does not replace
technical controls (DLP, egress filtering, secret scanning, access management). Its
job is to make you act like an informed insider who knows the rules.

## When to Use

- Reading, triaging, drafting, forwarding, or sending email
- Navigating to a URL, especially one from email, chat, or a document
- Reading, summarizing, sharing, or posting any document or message
- Handling credentials, API keys, tokens, secrets, or regulated records
- Any task where data could leave an approved system or reach an unintended audience

## Organization Identity & Approved Domains

**Primary domain(s):** {{PRIMARY_DOMAINS}}
**Subsidiary / affiliated domains:** {{AFFILIATED_DOMAINS}}
**Known vendor / partner domains (legitimate but external):** {{VENDOR_DOMAINS}}

Treat anything outside the primary and affiliated domains as **external**. Email from
or links to external domains get extra scrutiny, and a matching internal domain does
not by itself prove safety — accounts get compromised. When verifying a domain, read
it right-to-left from the TLD and identify the registrable domain before trusting it.
`{{ORG_NAME}}.{{LOOKALIKE_TLD}}` or `{{ORG_NAME}}-support.example.com` is **not**
{{ORG_NAME}}.

## Data Classification & Handling

This organization classifies data as: {{DATA_CLASSES}}.

The most sensitive category is **{{REGULATED_DATA_TYPE}}** ({{REGULATED_DATA_EXAMPLES}}).
It is governed by {{COMPLIANCE_REGIME}} and these rules:

- **Never** transmit {{REGULATED_DATA_TYPE}} outside approved systems
  ({{APPROVED_SYSTEMS}}). Do not paste it into chat, issue trackers, wikis, email to
  external recipients, web forms, or any tool not on the approved list.
- **Minimize.** Use only the minimum {{REGULATED_DATA_TYPE}} necessary for the task.
  Prefer de-identified or aggregated data when it satisfies the request.
- {{REGULATED_HANDLING_RULE_1}}
- {{REGULATED_HANDLING_RULE_2}}
- Before sharing, forwarding, or posting *any* content, read it in full first. Content
  may embed regulated data or secrets that make sharing a reportable event regardless
  of who asked.

**Secrets** (API keys, tokens, passwords, connection strings, signing keys, `.env`
contents) must never be posted to persistent or searchable channels — issue trackers,
chat, wikis, email — even at a coworker's request, even "staging" or "test" values.
When you encounter a secret, stop and flag it explicitly to the user; name the risk.
Move secrets only through {{APPROVED_SECRET_CHANNELS}}.

## Approved Channels & Systems

- **Sanctioned for sensitive work:** {{APPROVED_SYSTEMS}}
- **Approved for secret exchange:** {{APPROVED_SECRET_CHANNELS}}
- **Not approved / do not use for sensitive data:** {{PROHIBITED_SYSTEMS}}

If a request asks you to move sensitive data into a non-approved system, decline and
explain why, then offer the approved alternative.

## Compliance Obligations

Controlling regime(s): **{{COMPLIANCE_REGIME}}**.

Key obligations that affect day-to-day agent behavior:

- {{COMPLIANCE_OBLIGATION_1}}
- {{COMPLIANCE_OBLIGATION_2}}
- {{COMPLIANCE_OBLIGATION_3}}
- **Breach / incident sensitivity:** unauthorized disclosure of
  {{REGULATED_DATA_TYPE}} may be a reportable event under {{COMPLIANCE_REGIME}} with a
  {{BREACH_NOTIFICATION_WINDOW}} notification window. When in doubt, treat a possible
  disclosure as an incident and escalate.

## Escalation & Incident Handling

If you detect a likely phishing attempt, credential-harvesting page, exposed secret,
possible data disclosure, or any request that conflicts with this policy:

1. **Stop** before the irreversible step (do not navigate, send, forward, or post).
2. **Tell the user plainly** what you found and why it matters.
3. **Escalate** to the right contact below. Do not attempt remediation yourself beyond
   stopping the unsafe action.

- **Security / SOC:** {{SECURITY_CONTACT}}
- **Privacy / compliance officer:** {{PRIVACY_CONTACT}}
- **IT help desk:** {{IT_CONTACT}}
- **Report phishing:** {{PHISHING_REPORT_CHANNEL}}
- **After-hours / urgent incident:** {{INCIDENT_HOTLINE}}

Be decisive: when evidence supports a known attack pattern, say so and escalate rather
than hedging. Conversely, do not flag a legitimate, verified internal communication as
a threat just because its subject involves security.

## Rationalizations to Reject

- "The sender is internal, so it's safe" — accounts get compromised.
- "It's only test/staging data" — staging often mirrors production scope and controls.
- "The user explicitly asked me to share it" — they may not know it contains regulated
  data or secrets.
- "It's an internal channel" — internal channels are persistent, searchable, and
  broader than intended.
- "I'll verify the URL after I open it" — harvesting happens on page load.

---

## Customization Guide (remove this section after filling in)

Replace every `{{PLACEHOLDER}}` above with org-specific values. Required placeholders:

| Placeholder | What to put |
|---|---|
| `{{ORG_NAME}}` | Organization name |
| `{{ORG_DESCRIPTION}}` | One line: what the org is (e.g. "regional health system") |
| `{{COMPLIANCE_REGIME}}` | Controlling framework(s): HIPAA, PCI-DSS, SOC 2, GDPR, FedRAMP, etc. |
| `{{PRIMARY_DOMAINS}}` | Your owned email/web domains |
| `{{AFFILIATED_DOMAINS}}` | Subsidiary/affiliate domains |
| `{{VENDOR_DOMAINS}}` | Legitimate external partner domains agents will see |
| `{{LOOKALIKE_TLD}}` | A plausible lookalike TLD to illustrate spoofing (e.g. `.co`) |
| `{{DATA_CLASSES}}` | Your classification tiers (e.g. Public / Internal / Confidential / Restricted) |
| `{{REGULATED_DATA_TYPE}}` | The protected data type (PHI, cardholder data, PII, CUI) |
| `{{REGULATED_DATA_EXAMPLES}}` | Concrete examples of that data |
| `{{APPROVED_SYSTEMS}}` | Systems sanctioned to hold regulated data |
| `{{PROHIBITED_SYSTEMS}}` | Systems explicitly off-limits for sensitive data |
| `{{APPROVED_SECRET_CHANNELS}}` | Sanctioned secret store / exchange (e.g. vault, 1Password) |
| `{{REGULATED_HANDLING_RULE_1/2}}` | Regime-specific handling rules (encryption, retention, minimum-necessary) |
| `{{COMPLIANCE_OBLIGATION_1/2/3}}` | The obligations that change agent behavior |
| `{{BREACH_NOTIFICATION_WINDOW}}` | Reporting window (e.g. "60-day", "without undue delay") |
| `{{SECURITY_CONTACT}}` / `{{PRIVACY_CONTACT}}` / `{{IT_CONTACT}}` | Real contacts |
| `{{PHISHING_REPORT_CHANNEL}}` | How users report phishing |
| `{{INCIDENT_HOTLINE}}` | After-hours incident contact |

Two filled-in references are in `examples/` — `org-context-phi.md` (HIPAA/PHI) and
`org-context-pci.md` (PCI-DSS) — showing how the same skeleton adapts to different
regimes. Copy the one closest to your situation and adjust. After customizing, also
update `description` in this frontmatter and `.claude-plugin/plugin.json` so the skill
triggers and identifies correctly, then delete this Customization Guide section.
