# org-security-context

A **template plugin** that gives Claude agents organization-specific security and
compliance context — approved domains, sanctioned systems, data-classification and
handling rules, the controlling compliance regime, escalation contacts, and incident
procedures.

It is designed to be **customized per organization** and rolled out as part of a Claude
enterprise deployment. It pairs well with a generic security-awareness skill (which
teaches *how* to recognize threats); this plugin supplies the *org-specific facts* an
agent needs to apply those instincts correctly.

> **This is guidance, not enforcement.** A skill raises the floor on agent behavior; it
> does not replace technical controls (DLP, egress filtering, secret scanning, access
> management, network segmentation). Deploy it alongside real controls, not instead of
> them. Also note: skills load *on demand* when the model judges them relevant to a
> task — they are not an always-on guardrail that runs on every action.

## What's inside

```
org-security-context/
├── .claude-plugin/plugin.json
├── skills/
│   └── org-security-context/
│       ├── SKILL.md                  # generic template with {{PLACEHOLDER}}s
│       └── examples/
│           ├── org-context-phi.md    # filled in for a HIPAA/PHI org
│           └── org-context-pci.md    # filled in for a PCI-DSS org
└── README.md
```

## How to customize before rollout

1. Open `skills/org-security-context/SKILL.md`.
2. Replace every `{{PLACEHOLDER}}` using the table in its Customization Guide. The two
   files in `examples/` show the same skeleton filled in for different regimes — copy
   whichever is closest and adjust.
3. Update the `description` in the SKILL.md frontmatter and in
   `.claude-plugin/plugin.json` so the skill triggers and identifies for *your* org.
4. Delete the Customization Guide section from SKILL.md.
5. Repackage and publish to your internal/managed plugin source.

## Rollout notes for administrators

- **Distribute centrally.** Publish through a managed/internal plugin source rather than
  asking each user to install ad hoc, so versions stay consistent and updatable.
- **Version it.** Bump the `version` in `plugin.json` on every policy change so you can
  track which agents have which guidance.
- **One per regime, or one per business unit.** Orgs with multiple data types (e.g. both
  PHI and PCI) can maintain separate customized copies, or combine the relevant sections
  into a single skill — keep it specific enough that the guidance is actionable.
- **Pilot first.** Run it with a small group and watch for over-triggering (flagging
  legitimate internal mail) before a broad push.
- **Keep contacts current.** Escalation contacts and report channels are the parts most
  likely to go stale; review them on the same cadence as your IR plan.
- **Pair with controls.** This skill is the human-readable policy layer; keep DLP, secret
  scanning, and access controls doing the enforcement.

## Credits / inspiration

Threat-recognition framing draws on the structure of Trail of Bits' curated
`security-awareness` skill. This plugin focuses on the complementary, org-specific
context layer.
