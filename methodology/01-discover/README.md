# Phase 01: Discover & Assess

**Agent:** `@assess`
**Tools:** `read`, `search` (read-only)
**Skill:** [assess-codebase](../../.github/skills/assess-codebase/SKILL.md)

## Objective

Produce a comprehensive assessment of the legacy codebase that quantifies migration complexity, identifies blockers, and recommends a modernisation approach.

## Activities

### 1. Codebase Inventory
- Enumerate all projects, modules, and entry points
- Identify frameworks, languages, and runtime versions
- Map build systems and deployment mechanisms

### 2. Dependency Analysis
- Catalogue all NuGet packages, pip packages, and system dependencies
- Flag deprecated, unsupported, or vulnerable packages
- Identify packages with no modern equivalent (migration blockers)

### 3. Architecture Mapping
- Identify application layers (presentation, business logic, data access)
- Map inter-component dependencies and coupling hotspots
- Document external integrations (APIs, databases, message queues, file shares)

### 4. Complexity Scoring
Each component receives a complexity score (1-5):

| Score | Label | Criteria |
|-------|-------|---------|
| 1 | Trivial | Pure library, no state, no external deps |
| 2 | Simple | Single dependency, stateless |
| 3 | Moderate | Multiple deps, some state, standard patterns |
| 4 | Complex | Heavy coupling, custom frameworks, shared state |
| 5 | Critical | Deeply embedded, undocumented, high-risk |

### 5. Risk Assessment
- Identify migration blockers (binary dependencies, COM interop, proprietary protocols)
- Flag compliance and security concerns
- Estimate effort range per component

## Deliverables

| Artefact | Format | Description |
|----------|--------|-------------|
| Assessment Report | JSON | Machine-readable component inventory with scores |
| Executive Summary | Markdown | High-level findings for stakeholders |
| Dependency Matrix | Table | Package-by-package migration status |
| Risk Register | Table | Blockers with severity and mitigation options |

## Copilot Usage

```
@assess Analyse this codebase and produce an assessment report.
Focus on migration complexity from .NET Framework 4.8 to .NET 8.
```

## Exit Criteria

- [ ] All components inventoried with complexity scores
- [ ] All dependencies catalogued with migration status
- [ ] Blockers identified with proposed mitigations
- [ ] Assessment report generated and reviewed by team
