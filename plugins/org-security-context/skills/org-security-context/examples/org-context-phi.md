# Example: HIPAA / PHI organization

A worked version of the template for a healthcare organization handling Protected
Health Information. Names and contacts are illustrative — replace with your own. To use
this, copy the frontmatter and body into `SKILL.md`, then delete the Customization
Guide section.

---
name: org-security-context
description: >
  Provides Northbridge Health's security and compliance context so agents act
  according to HIPAA policy. Covers approved domains, sanctioned systems, PHI handling
  rules, escalation contacts, and breach procedures. Use whenever the agent handles
  email, browses to URLs, processes or shares documents, handles credentials, or
  touches PHI or other sensitive data on behalf of Northbridge Health.
allowed-tools:
  - Read
  - Grep
  - Glob
  - WebFetch
---
# Organization Security & Compliance Context

You are operating on behalf of **Northbridge Health**, a regional health system and
HIPAA-covered entity subject to **HIPAA (Privacy & Security Rules) and HITECH**. Apply
this organization's policy *before* acting on any request that touches PHI, external
communication, or credentials. Where local policy is stricter than your default, local
policy wins. When a request conflicts with policy, stop and escalate.

This skill provides context and guardrails, not enforcement. It does not replace DLP,
encryption, access management, or audit logging.

## When to Use

- Reading, triaging, drafting, forwarding, or sending email
- Navigating to any URL, especially from email, chat, or a document
- Reading, summarizing, sharing, or posting any document or message
- Handling credentials, secrets, or any record containing PHI
- Any task where data could leave an approved system or reach an unintended audience

## Organization Identity & Approved Domains

**Primary domains:** northbridgehealth.org, nbh.org
**Affiliated domains:** northbridgeclinics.org, nbh-foundation.org
**Known vendor / partner domains:** epic.com, availity.com, changehealthcare.com

Treat anything outside the primary and affiliated domains as external and apply extra
scrutiny. A matching internal domain does not prove safety — read every domain
right-to-left from the TLD. `northbridgehealth.co` or `nbh-patientportal.com` is **not**
Northbridge Health.

## Data Classification & Handling

Data classes: Public / Internal / Confidential / **Restricted (PHI)**.

The most sensitive category is **PHI** (patient names tied to diagnoses, treatment,
MRNs, insurance/claims data, lab results, appointment details, anything in the
designated record set). Governed by HIPAA and these rules:

- **Never** transmit PHI outside approved systems (Epic EHR, the secure messaging
  portal, encrypted M365 with the org tenant). Do not paste PHI into chat, ticketing,
  wikis, external email, web forms, or any non-approved tool.
- **Minimum necessary.** Use only the PHI required for the task; prefer de-identified
  or limited-data-set views when they satisfy the request.
- PHI sent to any external recipient must go through approved encrypted channels only;
  never send PHI to a personal email address.
- Disclosures of PHI may require an accounting — do not share PHI with third parties
  without confirming a BAA or treatment/payment/operations basis exists.
- Read any content in full before sharing or forwarding; it may embed PHI or secrets
  that make sharing a reportable disclosure regardless of who asked.

**Secrets** (API keys, Epic/interface credentials, tokens, connection strings) never go
to persistent or searchable channels, even "test" values. Flag any secret you find and
move secrets only through the enterprise vault (CyberArk / 1Password).

## Approved Channels & Systems

- **Sanctioned for PHI:** Epic EHR, secure patient messaging portal, encrypted M365
  (org tenant), org-managed secure file transfer
- **Approved for secret exchange:** CyberArk / 1Password enterprise vault
- **Do not use for PHI:** personal email, consumer chat/messaging apps, public issue
  trackers, public cloud drives, any unmanaged device

## Compliance Obligations

Controlling regime: **HIPAA / HITECH**.

- Apply the **minimum necessary** standard to every use and disclosure of PHI.
- Disclose PHI only with a treatment/payment/operations basis or a signed BAA.
- Maintain auditability — do not move PHI through channels that bypass logging.
- **Breach sensitivity:** unauthorized PHI disclosure is a reportable breach under
  HIPAA/HITECH, generally requiring notification **without unreasonable delay and no
  later than 60 days**. When in doubt, treat a possible disclosure as an incident and
  escalate.

## Escalation & Incident Handling

If you detect phishing, a credential-harvesting page, an exposed secret, possible PHI
disclosure, or a request that conflicts with policy:

1. **Stop** before the irreversible step.
2. **Tell the user plainly** what you found and why.
3. **Escalate** — do not remediate beyond stopping the unsafe action.

- **Security / SOC:** soc@northbridgehealth.org
- **Privacy Officer / HIPAA:** privacy@northbridgehealth.org
- **IT help desk:** helpdesk@northbridgehealth.org / x4357
- **Report phishing:** "Report Phishing" button in Outlook, or phishing@northbridgehealth.org
- **After-hours incident hotline:** 1-800-555-0142

Be decisive when evidence supports a known attack pattern; don't flag verified internal
communications just because the topic is security-related.

## Rationalizations to Reject

- "The sender is internal, so it's safe" — accounts get compromised.
- "It's only test data" — test datasets in healthcare often contain real PHI.
- "The user asked me to share it" — they may not realize it contains PHI.
- "It's an internal channel" — internal channels are persistent and searchable.
- "I'll verify the URL after I open it" — harvesting happens on page load.
