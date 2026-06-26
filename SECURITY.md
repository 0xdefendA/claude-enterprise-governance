# Security Policy

## About this project

`claude-enterprise-governance` is a collection of **template skills** (Markdown +
manifests) plus a Python validation script. It contains no runtime service and processes
no data on its own. The skills are *guidance* that shapes AI-agent behavior; they are not
a technical control and do not enforce anything by themselves. Organizations that adopt
the kit must pair it with real controls (DLP, secret scanning, access management).

## What counts as a vulnerability here

Because there is no running service, the relevant security concerns are:

- **Guidance that could lead an agent to unsafe behavior** — e.g. a template that, as
  written, would steer an agent toward leaking data, mishandling secrets, or skipping
  escalation.
- **A defect in `scripts/validate_kit.py`** that causes it to pass output it should fail
  (e.g. missing leftover placeholders or secrets in a rendered deployment).
- **Sensitive data committed to the repo** — a real organization's domains, contacts, or
  a filled-in `org-profile.yaml` that should have been git-ignored.

## Reporting

Please report suspected issues privately rather than opening a public issue:

- Preferred: GitHub **private vulnerability reporting** for this repo
  (Security tab → "Report a vulnerability").
- Or email: **security@defenda.systems**.

Include the affected file(s), a description of the risk, and a suggested fix if you have
one. We aim to acknowledge reports within a reasonable time and will credit reporters who
wish to be named.

## Handling secrets in contributions

Never include real credentials, customer data, or filled-in organization profiles in a
pull request. Worked examples under `examples/` must use clearly fictional names and
contacts. The `.gitignore` excludes `dist/` and working `org-profile.yaml` files — keep
it that way.

## Supported versions

This kit is versioned per the marketplace and per-plugin `version` fields. Fixes are
applied to the latest released version; pin a tag if you need stability for a rollout.
