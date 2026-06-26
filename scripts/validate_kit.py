#!/usr/bin/env python3
"""
validate_kit.py — backstop validator for the Claude Enterprise governance starter kit.

Two modes:

  template    (default) — validate the source repo. Manifests, structure, and
              name/directory consistency must be correct. Placeholders, examples,
              Customization Guides, and the rollout-assistant plugin are EXPECTED here.

  deployment  — validate a rendered, customized copy (e.g. dist/<org-slug>/) that is
              about to be published. Everything template mode checks, PLUS: no leftover
              {{placeholders}}, no Customization Guide sections, no examples/ directories,
              no rollout-assistant plugin, and (if an org-profile.yaml is present) no
              empty or TBD fields.

Stdlib only. Exits 0 on success, 1 on any failure, with a readable summary.

Usage:
  python3 scripts/validate_kit.py [PATH] [--mode template|deployment]

PATH defaults to the repo root inferred from this script's location (template mode) or
must be given explicitly for a deployment directory.
"""

import argparse
import json
import os
import re
import sys

PLACEHOLDER_RE = re.compile(r"\{\{[^}]+\}\}")
GUIDE_RE = re.compile(r"^#+\s*Customization Guide", re.IGNORECASE | re.MULTILINE)


class Report:
    def __init__(self):
        self.errors = []
        self.checks = 0

    def check(self, ok, msg):
        self.checks += 1
        if not ok:
            self.errors.append(msg)
        return ok

    def fail(self, msg):
        self.errors.append(msg)


def find_marketplace(root):
    p = os.path.join(root, ".claude-plugin", "marketplace.json")
    return p if os.path.isfile(p) else None


def load_json(path, rep):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:  # noqa: BLE001
        rep.fail(f"JSON parse error in {path}: {e}")
        return None


def frontmatter_name(skill_md):
    """Return the `name:` value from a SKILL.md YAML frontmatter block, or None."""
    try:
        with open(skill_md, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    block = text[3:end] if end != -1 else text
    for line in block.splitlines():
        m = re.match(r"\s*name:\s*(\S+)", line)
        if m:
            return m.group(1).strip().strip("\"'")
    return None


def iter_plugin_dirs(root):
    plugins_dir = os.path.join(root, "plugins")
    if not os.path.isdir(plugins_dir):
        return []
    return [
        os.path.join(plugins_dir, d)
        for d in sorted(os.listdir(plugins_dir))
        if os.path.isdir(os.path.join(plugins_dir, d)) and not d.startswith(".")
    ]


def validate_structure(root, rep):
    mk_path = find_marketplace(root)
    if not rep.check(mk_path is not None,
                     "missing .claude-plugin/marketplace.json"):
        return
    mk = load_json(mk_path, rep)
    listed = set()
    if mk is not None:
        rep.check("name" in mk, "marketplace.json missing 'name'")
        for entry in mk.get("plugins", []):
            if "name" in entry:
                listed.add(entry["name"])
            rep.check("source" in entry,
                      f"marketplace plugin '{entry.get('name','?')}' missing 'source'")

    plugin_dirs = iter_plugin_dirs(root)
    dir_names = {os.path.basename(p) for p in plugin_dirs}
    if mk is not None:
        rep.check(listed == dir_names,
                  f"marketplace plugins {sorted(listed)} != plugin dirs {sorted(dir_names)}")

    for pdir in plugin_dirs:
        name = os.path.basename(pdir)
        manifest = os.path.join(pdir, ".claude-plugin", "plugin.json")
        if rep.check(os.path.isfile(manifest), f"{name}: missing .claude-plugin/plugin.json"):
            pj = load_json(manifest, rep)
            if pj is not None:
                rep.check(pj.get("name") == name,
                          f"{name}: plugin.json name '{pj.get('name')}' != directory '{name}'")
        skills_dir = os.path.join(pdir, "skills")
        if not os.path.isdir(skills_dir):
            continue
        for sd in sorted(os.listdir(skills_dir)):
            sdir = os.path.join(skills_dir, sd)
            if not os.path.isdir(sdir):
                continue
            skill_md = os.path.join(sdir, "SKILL.md")
            if rep.check(os.path.isfile(skill_md), f"{name}/{sd}: missing SKILL.md"):
                fn = frontmatter_name(skill_md)
                rep.check(fn == sd,
                          f"{name}/{sd}: SKILL.md frontmatter name '{fn}' != skill dir '{sd}'")


def validate_deployment_extras(root, rep):
    # no rollout-assistant in deployed output
    rep.check(
        not os.path.isdir(os.path.join(root, "plugins", "rollout-assistant")),
        "deployment must not contain the 'rollout-assistant' plugin (admin tool only)",
    )
    # scan rendered SKILL.md files
    for pdir in iter_plugin_dirs(root):
        name = os.path.basename(pdir)
        skills_dir = os.path.join(pdir, "skills")
        if not os.path.isdir(skills_dir):
            continue
        for sd in sorted(os.listdir(skills_dir)):
            sdir = os.path.join(skills_dir, sd)
            if not os.path.isdir(sdir):
                continue
            # no examples/ in deployed skills
            rep.check(not os.path.isdir(os.path.join(sdir, "examples")),
                      f"{name}/{sd}: examples/ directory must be removed before deployment")
            skill_md = os.path.join(sdir, "SKILL.md")
            if not os.path.isfile(skill_md):
                continue
            with open(skill_md, encoding="utf-8") as f:
                text = f.read()
            ph = sorted(set(PLACEHOLDER_RE.findall(text)))
            rep.check(not ph, f"{name}/{sd}/SKILL.md: unfilled placeholders {ph}")
            rep.check(not GUIDE_RE.search(text),
                      f"{name}/{sd}/SKILL.md: 'Customization Guide' section must be removed")

    # any other stray {{ }} anywhere under root (READMEs, manifests)
    for dirpath, _dirs, files in os.walk(root):
        for fn in files:
            if not fn.endswith((".md", ".json", ".yaml", ".yml")):
                continue
            fpath = os.path.join(dirpath, fn)
            try:
                with open(fpath, encoding="utf-8") as f:
                    if PLACEHOLDER_RE.search(f.read()):
                        rel = os.path.relpath(fpath, root)
                        rep.check(False, f"leftover placeholder in {rel}")
            except (OSError, UnicodeDecodeError):
                pass

    # optional: org-profile completeness
    for cand in ("org-profile.yaml", "org-profile.yml"):
        p = os.path.join(root, cand)
        if os.path.isfile(p):
            with open(p, encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    s = line.split("#", 1)[0].rstrip()
                    if s.endswith(': ""') or re.search(r":\s*TBD\s*$", s):
                        rep.check(False, f"{cand}:{i}: unfilled field -> {line.strip()}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate the governance starter kit.")
    parser.add_argument("path", nargs="?", default=None,
                        help="kit root or rendered deployment dir")
    parser.add_argument("--mode", choices=("template", "deployment"), default="template")
    args = parser.parse_args(argv)

    root = args.path
    if root is None:
        # default: repo root = parent of this script's directory
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = os.path.abspath(root)

    rep = Report()
    if not os.path.isdir(root):
        print(f"FAIL: not a directory: {root}", file=sys.stderr)
        return 1

    validate_structure(root, rep)
    if args.mode == "deployment":
        validate_deployment_extras(root, rep)

    print(f"validate_kit.py [{args.mode}] {root}")
    print(f"  checks run: {rep.checks}")
    if rep.errors:
        print(f"  FAILURES ({len(rep.errors)}):")
        for e in rep.errors:
            print(f"    - {e}")
        return 1
    print("  PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
