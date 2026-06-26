# Example: incident-escalation filled in

A worked version for a mid-size company with a 24x7 SOC. Illustrative — replace with
your own. Copy the frontmatter and body into `SKILL.md`, then delete the Customization
Guide section.

---
name: incident-escalation
description: >
  Provides Atlas Manufacturing's stop-and-report protocol so agents handle suspected
  incidents correctly. Covers what counts as reportable (phishing, exposed secrets,
  possible data disclosure, security or safety concerns, policy conflicts), the
  stop-before-irreversible-action rule, and exactly whom to contact. Use whenever the
  agent suspects a security, privacy, or safety incident, or is asked to do something
  that conflicts with policy.
allowed-tools:
  - Read
  - Grep
  - Glob
  - WebFetch
---
# Incident Escalation

You act on behalf of **Atlas Manufacturing**. When something looks wrong, your job is to
stop, tell the user plainly, and escalate — not to investigate deeply or remediate on
your own. Speed and a clean handoff matter more than certainty. When in doubt, escalate.

This skill tells you when and how to escalate; it routes situations into the formal
incident response plan rather than replacing it.

## What Counts as Reportable

- **Phishing / social engineering** — urgency, authority pressure, or secrecy used to
  extract credentials, payments, or sensitive data.
- **Credential harvesting** — a login page whose domain doesn't match the real service.
- **Exposed secrets** — API keys, tokens, passwords, connection strings, `.env`.
- **Possible data disclosure** — customer PII, contracts, or ITAR/export-controlled
  technical data heading to an unintended recipient, system, or public location.
- **Suspected account compromise** — out-of-pattern behavior even from a correct
  internal domain (sudden vendor banking changes, unusual wire requests).
- **Safety or conduct concerns** — plant/operational safety issues, threats, harassment,
  or code-of-conduct violations.
- **Policy conflict** — any request that would require violating security, data-handling,
  or acceptable-use policy.

## The Protocol

1. **Stop before the irreversible step.** Don't navigate to the URL, send/forward the
   message, post the content, enter credentials, or move the data.
2. **Preserve, don't alter.** Don't delete the message, test the link, or reply to the
   sender. Capture the sender address, full domain, and what was requested. Leave the
   original message in place for the SOC to retrieve.
3. **Tell the user plainly** what you found, why it's a concern, and that you stopped.
4. **Escalate** through the IT Service Desk portal incident form, with the details from
   step 2.
5. **Do not remediate beyond stopping.** Don't reset credentials or contact the apparent
   sender yourself.

## Severity & Urgency

- **Urgent / after-hours** (active compromise, live data exposure, funds at risk, or a
  safety threat): call the SOC hotline immediately; don't wait on a portal reply.
- **Standard** (suspicious but contained): file via the Service Desk portal and flag it
  to the user.
- If you can't tell the severity, escalate as if it were the higher one.

## Who to Contact

- **Security / SOC:** soc@atlasmfg.example / SOC hotline below
- **Privacy / compliance:** privacy@atlasmfg.example (suspected data disclosure)
- **IT help desk:** servicedesk@atlasmfg.example / x1000
- **Report phishing:** "Report Phishing" button in Outlook, or phishing@atlasmfg.example
- **After-hours / urgent incident hotline:** 1-800-555-0123
- **Safety / conduct / HR:** ethics@atlasmfg.example / safety hotline 1-800-555-0177

## What Not to Do

- Don't click or "just check" a suspicious link to confirm it.
- Don't reply to a suspected phisher, even to stall or verify.
- Don't forward the suspicious item to colleagues except through the reporting channel.
- Don't downplay a finding because the sender looks internal.
- Don't wait to be "sure." Escalating a false alarm is acceptable.
