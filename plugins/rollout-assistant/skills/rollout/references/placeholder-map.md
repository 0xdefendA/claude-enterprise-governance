# Placeholder Map

Every placeholder across the governance plugins, the interview question to ask, and
where it is used. Shared placeholders (used by 2+ plugins) are collected once in Phase 1
and applied everywhere.

## Shared (Phase 1 — ask once)

| Placeholder | Interview question | Used by |
|---|---|---|
| `{{ORG_NAME}}` | What's the organization's name? | all |
| `{{COMPLIANCE_REGIME}}` | Which compliance framework(s) govern you? (HIPAA, PCI-DSS, SOC 2, GDPR, FedRAMP/CMMC, GLBA, etc.) | org-security-context (acceptable-use/incident reference it indirectly) |
| `{{REGULATED_DATA_TYPE}}` | What's your most sensitive/regulated data type? (PHI, cardholder data, PII, CUI) | org-security-context, acceptable-use, incident-escalation |
| `{{APPROVED_SYSTEMS}}` | Which systems are sanctioned to hold that data? | org-security-context, data-handling |
| `{{APPROVED_SECRET_CHANNELS}}` | Where do secrets live / move? (vault, 1Password, etc.) | org-security-context, data-handling |
| `{{SECURITY_CONTACT}}` | Security/SOC contact? | org-security-context, incident-escalation |
| `{{PRIVACY_CONTACT}}` | Privacy/compliance officer contact? | org-security-context, incident-escalation |
| `{{IT_CONTACT}}` | IT help desk contact? | org-security-context, incident-escalation |
| `{{PHISHING_REPORT_CHANNEL}}` | How do users report phishing? | org-security-context, incident-escalation |
| `{{INCIDENT_HOTLINE}}` | After-hours/urgent incident number? | org-security-context, incident-escalation |

Note: the classification scheme appears as `{{DATA_CLASSES}}` (org-security-context) and
as `{{TIER_n_NAME/DEF/EXAMPLES}}` (data-handling). Collect the scheme once and keep both
representations consistent.

## org-security-context (plugin-specific)

| Placeholder | Interview question |
|---|---|
| `{{ORG_DESCRIPTION}}` | One line: what is the org? (e.g. "regional health system") |
| `{{PRIMARY_DOMAINS}}` | Your owned email/web domains? |
| `{{AFFILIATED_DOMAINS}}` | Subsidiary/affiliate domains? |
| `{{VENDOR_DOMAINS}}` | Legitimate external partner domains agents will routinely see? |
| `{{LOOKALIKE_TLD}}` | A plausible lookalike TLD for the spoofing example (e.g. `.co`) |
| `{{DATA_CLASSES}}` | Your classification tiers (list) |
| `{{REGULATED_DATA_EXAMPLES}}` | Concrete examples of the regulated data type |
| `{{PROHIBITED_SYSTEMS}}` | Systems explicitly off-limits for sensitive data |
| `{{REGULATED_HANDLING_RULE_1/2}}` | Two regime-specific handling rules (encryption, minimum-necessary, retention) |
| `{{COMPLIANCE_OBLIGATION_1/2/3}}` | Three obligations that change agent behavior |
| `{{BREACH_NOTIFICATION_WINDOW}}` | Breach reporting window (e.g. "60-day", "without undue delay") |

## data-handling (plugin-specific)

| Placeholder | Interview question |
|---|---|
| `{{TIER_1..4_NAME}}` | Names of your classification tiers (least→most sensitive) |
| `{{TIER_1..4_DEF}}` | One-line definition of each tier |
| `{{TIER_1..4_EXAMPLES}}` | Examples for each tier |
| `{{LOW_TIER_RULE_1}}` | Any handling rule for the lower tiers |
| `{{HIGH_TIER_RULE_1/2}}` | Extra rules for sensitive tiers (encryption-at-rest, access logging) |
| `{{APPROVED_CHANNELS}}` | Approved transmission channels |
| `{{RESTRICTED_IDENTIFIERS}}` | Identifiers that force top-tier handling (PHI elements, PAN, SSN, PII) |
| `{{EXTERNAL_SHARING_APPROVAL}}` | What's required to share externally (NDA/DPA, sign-off) |
| `{{SECURE_SHARE_METHOD}}` | Approved secure-share mechanism |
| `{{RETENTION_RULE}}` | Retention/disposal policy summary |

If the org has fewer/more than four tiers, add or remove rows in the SKILL.md table to
match before rendering.

## acceptable-use (plugin-specific)

| Placeholder | Interview question |
|---|---|
| `{{ENCOURAGED_USE_1/2}}` | Concrete encouraged use cases |
| `{{REGULATED_ADVICE_ROLES}}` | Who real advice must come from (licensed counsel, CPA, clinician) |
| `{{COMMS_APPROVER}}` | Who approves external/official comms |
| `{{PEOPLE_DECISION_RULE}}` | Your rule on AI in people-decisions (note EU AI Act / local law) |
| `{{COMMITMENT_APPROVER}}` | Who can authorize binding commitments |
| `{{PROHIBITED_USE_1/2}}` | Org-specific prohibited uses |
| `{{RECORDKEEPING_RULE}}` | Record-keeping standard for AI-assisted official records |
| `{{AI_DISCLOSURE_RULE}}` | Whether/when AI assistance must be disclosed |
| `{{POLICY_CONTACT}}` | Who owns the AUP / answers policy questions |

## incident-escalation (plugin-specific)

| Placeholder | Interview question |
|---|---|
| `{{SAFETY_CONCERN_EXAMPLES}}` | What safety/conduct issues should route here |
| `{{PRESERVATION_RULE}}` | Evidence-preservation guidance from your IR plan |
| `{{REPORTING_MECHANISM}}` | The standard report path (ticket queue, button, address) |
| `{{URGENT_CRITERIA}}` | What makes something hotline-urgent |
| `{{SAFETY_CONTACT}}` | Safety/conduct/HR contact |

## Regime quick-pick

When the user names a regime, suggest the closest worked example as a drafting base:

- **HIPAA / PHI** → `org-security-context/examples/org-context-phi.md`
- **PCI-DSS** → `org-security-context/examples/org-context-pci.md`
- **PII / GDPR**, **CUI / CMMC**, **GLBA**, etc. → start from whichever example is
  structurally closest and adjust the regime-specific rules and breach window.
