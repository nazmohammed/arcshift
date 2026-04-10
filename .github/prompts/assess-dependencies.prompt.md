---
description: "Analyse project dependencies and identify outdated, deprecated, or risky packages."
---

# Dependency Analysis

Analyse the dependencies in `{{file}}` and produce a report covering:

## Tasks

1. **List all dependencies** with current versions
2. **Flag outdated packages** — identify packages with major version updates available
3. **Flag deprecated packages** — identify packages that have been superseded or abandoned
4. **Identify security vulnerabilities** — check for known CVEs or security advisories
5. **Map transitive dependencies** — identify heavy dependency trees that increase attack surface
6. **Recommend replacements** — for each deprecated/outdated package, suggest the modern equivalent

## Output Format

| Package | Current Version | Latest Version | Status | Replacement | Notes |
|---------|----------------|----------------|--------|-------------|-------|
| ... | ... | ... | OK / Outdated / Deprecated / Vulnerable | ... | ... |
