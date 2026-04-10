---
description: "Generate a structured migration plan for modernising an application from legacy to modern stack."
---

# Migration Plan Generation

Generate a detailed migration plan for modernising `{{application_name}}` from `{{source_stack}}` to `{{target_stack}}`.

## Tasks

1. **Summarise current state** — Technology stack, architecture, key dependencies, known issues
2. **Define target state** — Target framework, hosting, data stores, architecture style
3. **Select migration strategy** — Strangler fig, big bang, parallel run, or branch by abstraction
4. **Break into work packages** — Ordered list of migration tasks with dependencies
5. **Identify risks** — Technical risks, data migration risks, integration risks
6. **Define success criteria** — How to measure migration completion and quality

## Output Format

```markdown
# Migration Plan: {{application_name}}

## Current State
- Stack: ...
- Architecture: ...
- Key Dependencies: ...

## Target State
- Stack: ...
- Architecture: ...
- Azure Services: ...

## Strategy: {{strategy_name}}
Justification: ...

## Work Packages (ordered)
1. [WP-01] {{task}} — Effort: S/M/L — Risk: Low/Med/High
2. [WP-02] {{task}} — Effort: S/M/L — Risk: Low/Med/High
...

## Risks & Mitigations
| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|------------|
| ... | ... | ... | ... |

## Success Criteria
- [ ] All tests pass
- [ ] API parity verified
- [ ] Performance within 10% of baseline
- [ ] Zero data loss during migration
```
