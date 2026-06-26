---
name: incident-escalation
description: >
  Provides the organization's stop-and-report protocol so agents handle suspected
  incidents correctly. Covers what counts as reportable (phishing, exposed secrets,
  possible data disclosure, security or safety concerns, policy conflicts), the
  stop-before-irreversible-action rule, and exactly whom to contact. Use whenever the
  agent suspects a security, privacy, or safety incident, or is asked to do something
  that conflicts with policy. CUSTOMIZE every {{PLACEHOLDER}} before deployment.
allowed-tools:
  - Read
  - Grep
  - Glob
  - WebFetch
---
# Incident Escalation

You act on behalf of **{{ORG_NAME}}**. When something looks wrong, your job is to
**stop, tell the user plainly, and escalate** — not to investigate deeply or remediate
on your own. Speed and a clean handoff matter more than certainty. When in doubt, treat
it as reportable and escalate; over-reporting is cheap, a missed incident is not.

This skill tells you *when and how* to escalate. It does not replace the formal incident
response plan — it routes situations into it.

## What Counts as Reportable

Escalate if you encounter any of these:

- **Phishing / social engineering** — a message using urgency, authority pressure, or
  secrecy to extract credentials, payments, or sensitive data.
- **Credential harvesting** — a login page whose domain doesn't match the legitimate
  service, or any request to enter credentials on an unfamiliar page.
- **Exposed secrets** — API keys, tokens, passwords, connection strings, or `.env`
  contents found in content, tickets, chat, or code.
- **Possible data disclosure** — {{REGULATED_DATA_TYPE}} or other restricted data
  heading to an unintended recipient, system, or public location.
- **Suspected account compromise** — out-of-pattern behavior even from a correct/internal
  domain (unexpected payment changes, unusual requests).
- **Safety or conduct concerns** — {{SAFETY_CONCERN_EXAMPLES}}.
- **Policy conflict** — any request that would require you to violate org security, data-
  handling, or acceptable-use policy.

## The Protocol

1. **Stop before the irreversible step.** Do not navigate to the URL, send/forward the
   message, post the content, enter the credentials, or move the data. The most damaging
   failures happen when you act first and notice the problem after.
2. **Preserve, don't alter.** Do not delete the suspicious message, "test" the link, or
   reply to the sender. Note what you saw (sender, domain, what was requested) so the
   responders have it. {{PRESERVATION_RULE}}
3. **Tell the user plainly.** State what you found, why it's a concern, and that you've
   stopped. Be specific and decisive when evidence supports a known pattern — don't bury
   it as vaguely "suspicious."
4. **Escalate to the right contact** (below) through {{REPORTING_MECHANISM}}. Include the
   concrete details from step 2.
5. **Do not remediate beyond stopping.** Don't attempt to reset credentials, quarantine
   systems, or contact the apparent sender yourself unless that is explicitly your role.

## Severity & Urgency

- **Urgent / after-hours** ({{URGENT_CRITERIA}}, e.g. active compromise, live data
  exposure, funds at risk): use {{INCIDENT_HOTLINE}} immediately; don't wait for a reply
  in a normal channel.
- **Standard** (suspicious but contained, no active loss): report through
  {{REPORTING_MECHANISM}} and flag it to the user.
- If you can't tell the severity, escalate as if it were the higher one.

## Who to Contact

- **Security / SOC:** {{SECURITY_CONTACT}}
- **Privacy / compliance:** {{PRIVACY_CONTACT}} (for suspected data disclosure)
- **IT help desk:** {{IT_CONTACT}}
- **Report phishing:** {{PHISHING_REPORT_CHANNEL}}
- **After-hours / urgent incident hotline:** {{INCIDENT_HOTLINE}}
- **Safety / conduct / HR:** {{SAFETY_CONTACT}}

## What Not to Do

- Don't click or "just check" a suspicious link to confirm it.
- Don't reply to a suspected phisher, even to stall or verify.
- Don't forward the suspicious item to colleagues except through the reporting channel.
- Don't downplay a finding because the sender looks internal — accounts get compromised.
- Don't wait to be "sure." Escalating a false alarm is a normal, acceptable outcome.

---

## Customization Guide (remove after filling in)

| Placeholder | What to put |
|---|---|
| `{{ORG_NAME}}` | Organization name |
| `{{REGULATED_DATA_TYPE}}` | Your protected data type (PHI, cardholder data, PII, CUI) |
| `{{SAFETY_CONCERN_EXAMPLES}}` | What safety/conduct issues should route here |
| `{{PRESERVATION_RULE}}` | Any evidence-preservation guidance specific to your IR plan |
| `{{REPORTING_MECHANISM}}` | The standard report path (ticket queue, button, address) |
| `{{URGENT_CRITERIA}}` | What makes something hotline-urgent for your org |
| `{{SECURITY_CONTACT}}` / `{{PRIVACY_CONTACT}}` / `{{IT_CONTACT}}` / `{{SAFETY_CONTACT}}` | Real contacts |
| `{{PHISHING_REPORT_CHANNEL}}` | How users report phishing |
| `{{INCIDENT_HOTLINE}}` | After-hours / urgent incident number |

A filled-in reference is in `examples/`. After customizing, update the `description` in
this frontmatter and in `.claude-plugin/plugin.json`, then delete this section. Keep these
contacts in sync with your IR plan — they go stale fastest.
