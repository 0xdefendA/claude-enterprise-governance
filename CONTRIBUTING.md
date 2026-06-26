# Contributing

Thanks for helping improve the governance kit. This repo is a set of **customizable
template skills** for organizations rolling out Claude Enterprise. Contributions should
preserve that template nature and the conventions below.

## Ground rules

- **Skills are guidance, not enforcement.** Don't write a skill that claims to *block* or
  *guarantee* anything technical. Skills shape agent behavior and complement controls
  (DLP, secret scanning, access management) — say so where relevant.
- **No real org data.** Never commit real domains, contacts, secrets, or a filled-in
  `org-profile.yaml`. The `.gitignore` excludes `dist/` and working profiles; keep it
  that way.
- **Keep it tool-agnostic in templates.** Templates describe *categories* of system
  ("approved secret store"), not specific products, except inside `examples/`.

## Conventions

A governance plugin lives at `plugins/<name>/` and contains:

```
plugins/<name>/
├── .claude-plugin/plugin.json     # name == directory; kebab-case
└── skills/<name>/
    ├── SKILL.md                   # template body
    └── examples/<name>-example.md # at least one filled-in worked example
```

`SKILL.md` rules:

- YAML frontmatter with `name` (must equal the skill directory), a third-person
  `description` with concrete trigger phrases, and a least-privilege `allowed-tools`.
- Org-specific values are `{{PLACEHOLDER}}` tokens in UPPER_SNAKE_CASE.
- End the body with a `## Customization Guide` section: a table mapping every
  placeholder to what to put. The rollout assistant and validator rely on this heading.
- Every placeholder you introduce must be listed in
  `plugins/rollout-assistant/skills/rollout/references/placeholder-map.md` and added to
  `references/org-profile.template.yaml`, so the interview can collect it.

`examples/` rules:

- Worked examples are illustrative and use clearly fake names/contacts.
- Examples must **not** contain `{{placeholders}}` — they are fully filled in.

## Adding a plugin

1. Create the structure above.
2. Register it in `.claude-plugin/marketplace.json` (name + `source` path).
3. Update `placeholder-map.md` and `org-profile.template.yaml` for any new placeholders.
4. Run the validator (below). Open a PR.

## Validate before you push

```bash
python3 scripts/validate_kit.py . --mode template
```

CI runs this on every push and pull request via `.github/workflows/validate.yml`. A PR
that fails the validator won't be merged. To check a rendered deployment locally:

```bash
python3 scripts/validate_kit.py dist/<org-slug> --mode deployment
```

## What not to put here

- The `rollout-assistant` plugin is an **admin tool** and must never be included in a
  deployed/customized output (the validator enforces this in deployment mode).
- Enablement-tier skills (org glossary, comms voice, approved-tools map) are out of scope
  for this governance repo unless a maintainer decides to add a separate tier.
