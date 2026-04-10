# Phase 02: Design Architecture

**Agent:** `@architect`
**Tools:** `read`, `search`, `web`
**Skill:** [decompose-monolith](../../.github/skills/decompose-monolith/SKILL.md)

## Objective

Design the target architecture based on the assessment report, producing Architecture Decision Records (ADRs) and a service map that guides the migration phase.

## Activities

### 1. Review Assessment
- Load the Phase 01 assessment report
- Identify high-complexity components requiring architectural decisions
- Group components into candidate bounded contexts

### 2. Define Bounded Contexts
- Map business capabilities to service boundaries
- Identify shared kernel vs. separate contexts
- Define data ownership per context

### 3. Select Target Architecture
Choose and document the target pattern:

| Pattern | When to Use |
|---------|------------|
| Modular monolith | Low complexity, tight timelines |
| Microservices | High team autonomy, independent scaling needs |
| Hybrid | Gradual migration with strangler fig |

### 4. Write Architecture Decision Records

Each ADR follows the format:
```markdown
# ADR-{number}: {title}
## Status: Proposed | Accepted | Deprecated
## Context: Why this decision is needed
## Decision: What we chose
## Consequences: Trade-offs and implications
```

Key ADRs to produce:
- ADR-001: Target runtime and framework
- ADR-002: Service decomposition strategy
- ADR-003: Data persistence approach
- ADR-004: Communication patterns (sync/async)
- ADR-005: Authentication and authorisation model
- ADR-006: Hosting and infrastructure

### 5. Generate Service Map
Produce a service map showing:
- Service boundaries and responsibilities
- Synchronous API calls (REST/gRPC)
- Asynchronous messaging (events/commands)
- Shared data stores vs. service-owned stores

## Deliverables

| Artefact | Format | Description |
|----------|--------|-------------|
| Architecture Decision Records | Markdown | One ADR per key decision |
| Service Map | JSON + Mermaid | Machine-readable + visual diagram |
| Migration Sequence | Ordered list | Service extraction order by risk/value |
| Technology Radar | Table | Adopt/trial/assess/hold per technology |

## Copilot Usage

```
@architect Design a target architecture for this application.
The assessment report is in docs/assessment-report.json.
Target platform is Azure Container Apps with .NET 8.
```

## Exit Criteria

- [ ] All bounded contexts defined with clear ownership
- [ ] ADRs written and reviewed for each key decision
- [ ] Service map generated with dependency graph
- [ ] Migration sequence prioritised by business value and risk
