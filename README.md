# Claude Enterprise Governance Kit

A curated set of **customizable security governance template skills** for organizations rolling out Claude
Enterprise. Claude Enterprise ships the platform but no opinionated baseline of skills;
every org starts from a blank page. This repo gives you a governance floor to start
from — fill in the placeholders, pilot, and publish to your managed plugin source.

> **Guidance, not enforcement.** These skills shape agent *behavior*; they do not
> replace technical controls (DLP, egress filtering, secret scanning, access
> management). And skills load *on demand* when the model judges them relevant to a
> task — they are not always-on guardrails. Treat this kit as the human-readable policy
> layer that sits alongside your real controls.

## What's in the kit

This is a **plugin marketplace**: one repo, multiple plugins, each a self-contained
skill you can adopt independently.

| Plugin | What it gives an agent | Worked examples |
|---|---|---|
| `org-security-context` | Approved domains, sanctioned systems, controlling compliance regime, escalation contacts, incident procedures | HIPAA/PHI, PCI-DSS |
| `data-handling` | Classification tiers, DLP-awareness, redaction, retention, external-sharing rules | One generic example |
| `acceptable-use` | What to delegate vs. require human review; guardrails on regulated advice, confidential data, record-keeping | One generic example |
| `incident-escalation` | A stop-and-report protocol — recognize, halt before the irreversible step, escalate to the right contact | One generic example |

Each plugin contains a generic `SKILL.md` with `{{PLACEHOLDER}}`s plus at least one
filled-in example under `skills/<name>/examples/`.

A fifth plugin, **`rollout-assistant`**, is an *admin tool* — not deployed to end users.
It drives the fast path below.

## Fast path: let Claude roll it out for you

If you have this kit open in Claude (Cowork or Claude Code with the kit on disk), you can
go from discovery to deployment by interview instead of hand-editing files:

> "Use the rollout assistant to customize this kit for my organization."

The `rollout` skill will:

1. Interview you for your org's details (name, compliance regime, domains, approved
   systems, contacts, escalation paths) — asking shared values once.
2. Capture everything in a reusable `org-profile.yaml` (your single source of truth).
3. Render a **customized copy per organization** under `dist/<org-slug>/` — filling every
   placeholder, replacing the examples with your real values, and stripping the
   Customization Guides — while leaving these templates pristine for the next rollout.
4. Validate (no leftover placeholders, valid manifests) and package a deployable zip.

To update later, edit `org-profile.yaml` and re-render — no need to re-interview.
**Consultants:** run it once per client; the templates are never overwritten.

## How customization works (manual)

Every skill body uses `{{PLACEHOLDER}}` tokens for org-specific facts (domains,
systems, contacts, regime-specific rules). A Customization Guide table at the bottom of
each `SKILL.md` lists every placeholder and what to put. The `examples/` files show the
same skeleton filled in, so you can copy the closest one and adjust.

**Per-plugin steps:**

1. Open `plugins/<plugin>/skills/<plugin>/SKILL.md`.
2. Replace every `{{PLACEHOLDER}}` (use the Customization Guide table + the example).
3. Update the `description` in that SKILL.md frontmatter and in the plugin's
   `.claude-plugin/plugin.json` so it triggers and identifies for *your* org.
4. Delete the Customization Guide section.
5. Bump the version and repackage.

**Repo-level steps:**

- Set `owner` in `.claude-plugin/marketplace.json` to your org/team.
- Keep each plugin's `version` in sync between its `plugin.json` and the marketplace
  entry when you publish changes.

## Validation backstop

`scripts/validate_kit.py` (stdlib Python, no dependencies) is the consistency gate. It
runs in two modes:

```bash
# Validate the source repo — structure, manifests, name/dir consistency.
# Placeholders, examples, and the rollout-assistant are expected here.
python3 scripts/validate_kit.py . --mode template

# Validate a rendered, customized copy before publishing.
# Also requires: no leftover {{placeholders}}, no Customization Guides, no examples/,
# no rollout-assistant, and no empty/TBD fields in org-profile.yaml.
python3 scripts/validate_kit.py dist/<org-slug> --mode deployment
```

It exits non-zero with a readable failure list, so the same script the rollout skill
runs at the end of a customization also serves as a CI gate. A GitHub Actions workflow
(`.github/workflows/validate.yml`) runs the template-mode check on every push and PR.

## Rollout notes for administrators

- **Distribute centrally** through a managed/internal plugin source so versions stay
  consistent — don't have users install ad hoc.
- **Pilot first** with a small group and watch for over-triggering (flagging
  legitimate internal mail) before a broad push.
- **Keep contacts current.** Escalation contacts and report channels go stale fastest;
  review them on the same cadence as your IR plan.
- **One per regime or business unit.** Orgs with multiple data types (e.g. PHI *and*
  PCI) can maintain separate customized copies or merge the relevant sections.
- **Pair with controls.** Keep DLP, secret scanning, and access controls doing the
  enforcement; this kit is only the *policy/behavior layer*.

## Extending the kit

Add a new plugin under `plugins/`, follow the same `SKILL.md` + `examples/` +
`{{PLACEHOLDER}}` convention, and register it in `.claude-plugin/marketplace.json`.
Good candidates for a future tier: an org glossary/memory skill, comms/brand-voice
guidance, and an approved-tools/connector map.

## Credits / inspiration

Threat-recognition framing draws on the structure of curated community skills such as
Trail of Bits' `skills-curated` and 1Password's `security-awareness`. This kit focuses
on the complementary, org-specific governance layer to save you from having to create one from scratch, or omitting entirely. 

## Contributing & License

See `CONTRIBUTING.md` for the template/placeholder conventions and the validation gate.
Licensed under the MIT License (`LICENSE`)
