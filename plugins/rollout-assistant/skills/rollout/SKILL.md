---
name: rollout
description: >
  Interview-driven rollout of the Claude Enterprise governance starter kit. Collects an
  organization's details, fills every placeholder across the governance plugins,
  replaces the worked examples with real values, validates the result, and packages a
  deployment-ready copy. Use when a user wants to set up, customize, configure, tailor,
  or roll out the governance starter kit for an organization or client, or says things
  like "interview me to fill in the placeholders" or "customize this kit for my company."
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
---
# Rollout Assistant

Take an administrator from a freshly discovered starter kit to a deployment-ready,
customized governance bundle. Conduct a structured interview, capture answers in a
single reusable profile, render the templates, validate, and package — without ever
overwriting the pristine templates.

This skill operates ON the starter kit's files. Drive the conversation in plain
language; do not expose file paths or internal structure unless asked.

## Operating Principles

- **Never modify the templates in place.** Render into a fresh per-organization copy so
  the kit stays reusable for the next rollout (important for consultants serving multiple
  clients). Work in a directory named for the org, e.g. `dist/<org-slug>/`.
- **One source of truth.** Capture all answers in an `org-profile.yaml` (see
  `references/org-profile.template.yaml`). Render everything from it. This gives the admin
  a reviewable artifact and makes future updates a re-render, not a re-interview.
- **Shared answers asked once.** Many placeholders repeat across plugins (org name,
  compliance regime, regulated data type, approved systems, contacts). Collect these
  once in the profile and apply everywhere.
- **Confirm before writing.** Summarize the captured profile and get explicit sign-off
  before rendering files.
- **Validate before declaring done.** No placeholder may remain; all JSON must parse.

## Workflow

### Phase 0: Locate and orient

Find the starter kit root (the directory containing `.claude-plugin/marketplace.json`
and `plugins/`). Confirm with the user which plugins they want to roll out — default to
all governance plugins (`org-security-context`, `data-handling`, `acceptable-use`,
`incident-escalation`). Do **not** include `rollout-assistant` in the deployed output;
it is an admin tool.

Read `references/placeholder-map.md` for the complete list of placeholders, which plugin
each belongs to, and the interview question for each.

### Phase 1: Organization profile (shared answers)

Interview the user for the shared values first. Use AskUserQuestion for choices with
clear options (e.g. compliance regime, whether examples lean PHI/PCI/PII/CUI); use plain
questions for free-text values (domains, contacts). Group questions; don't ask one at a
time where you can batch.

Collect at minimum:

- Organization name and one-line description
- Controlling compliance regime(s)
- The regulated/restricted data type and concrete examples
- Owned domains, affiliated domains, known vendor domains
- Data classification tiers (names + definitions)
- Approved systems for sensitive data; approved channels; prohibited systems
- Approved secret store/exchange
- Key contacts: security/SOC, privacy/compliance, IT, safety/HR
- Report channels: phishing reporting, incident hotline, standard reporting mechanism

Write answers into `org-profile.yaml` as you go.

### Phase 2: Plugin-specific answers

For each selected plugin, collect the remaining placeholders that aren't covered by the
shared profile (see `references/placeholder-map.md` for the per-plugin lists):

- **org-security-context**: lookalike TLD example, breach-notification window, three
  compliance obligations, two regulated-handling rules
- **data-handling**: per-tier examples, low/high-tier rules, restricted identifiers,
  external-sharing approval, secure-share method, retention rule
- **acceptable-use**: encouraged uses, regulated-advice roles, comms/commitment/people-
  decision approvers and rules, prohibited uses, record-keeping and AI-disclosure rules,
  policy contact
- **incident-escalation**: safety-concern examples, preservation rule, urgent criteria

Offer the matching worked example as a starting point ("Your regime is HIPAA — want me
to base the security-context wording on the PHI example and adjust?"). Use the examples
in each plugin's `examples/` folder as drafting aids, but replace their illustrative
names/contacts with the real profile values.

### Phase 3: Confirm

Present the completed `org-profile.yaml` back to the user as a readable summary. Flag any
field left blank or marked "TBD." Get explicit confirmation before rendering.

### Phase 4: Render

For each selected plugin, into `dist/<org-slug>/plugins/<plugin>/`:

1. Copy the plugin's template files.
2. In each `SKILL.md`, replace every `{{PLACEHOLDER}}` with the profile value.
3. Replace the frontmatter `description` with an org-specific version (name + regime +
   triggers).
4. **Delete the entire "Customization Guide" section** (from its heading to end of file).
5. Remove the `examples/` directory from the rendered copy, or replace its contents with
   the now-real org wording — the deployed skill should not ship illustrative examples.
6. Update `.claude-plugin/plugin.json`: rewrite `description` to match, set `author` to
   the org, remove the `version_note`, and bump `version`.

Then render `dist/<org-slug>/.claude-plugin/marketplace.json` listing only the deployed
plugins, with `owner` set to the organization.

### Phase 5: Validate and package

Run the repo's backstop validator against the rendered copy in **deployment** mode:

```bash
python3 scripts/validate_kit.py dist/<org-slug> --mode deployment
```

It exits non-zero with a readable list on any failure and checks: no leftover
`{{placeholders}}`, no "Customization Guide" sections, no `examples/` directories, no
`rollout-assistant` plugin, valid JSON manifests, skill `name` matches its directory,
marketplace names match plugin directories, and no empty/`TBD` fields in
`org-profile.yaml`. Fix every failure and re-run until it passes before packaging.

Then package:

```bash
cd dist && zip -r /tmp/<org-slug>-governance.zip <org-slug> -x "*.DS_Store"
cp /tmp/<org-slug>-governance.zip <outputs>/<org-slug>-governance.zip
```

Present the zip and the `org-profile.yaml`. Summarize what was produced and the
remaining human step: review by the org's security/compliance owner before publishing to
their managed plugin source.

## Re-running and updates

To update a deployed kit (new contact, changed system, policy revision), edit the saved
`org-profile.yaml` and re-render rather than re-interviewing. Bump plugin versions on
each change so admins can track what's deployed.

## Guardrails

- This skill produces a **policy/behavior layer**, not technical enforcement. Remind the
  user at the end that it complements DLP, secret scanning, and access controls.
- Do not invent contacts, domains, or obligations. If the user doesn't know a value,
  record it as "TBD" and list it as a blocker rather than guessing.
- Keep the deployed output free of the rollout-assistant plugin and of any leftover
  template scaffolding (Customization Guides, examples).
