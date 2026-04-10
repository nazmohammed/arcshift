---
mode: "agent"
description: "Extract a bounded context from a monolith into an independent microservice"
---

# Extract Service from Monolith

Extract the **{{service_name}}** bounded context from the monolith codebase.

## Source Analysis

1. Identify all classes, modules, and functions belonging to `{{service_name}}`
2. Map inbound dependencies — what calls INTO this context
3. Map outbound dependencies — what this context calls OUT to
4. Identify shared database tables and data ownership
5. List shared utilities or cross-cutting concerns used

## Extraction Plan

For each dependency crossing the boundary:

| Dependency | Direction | Current Coupling | Decoupling Strategy |
|-----------|-----------|-----------------|-------------------|
| _class/function_ | inbound/outbound | direct call / shared DB / shared model | API call / event / ACL |

## Code Generation

Generate the extracted service with:
- **Project structure** following target stack conventions
- **API contracts** (OpenAPI spec) for all inbound interfaces
- **Anti-corruption layer** for outbound dependencies not yet migrated
- **Data migration script** for owned tables
- **Integration tests** validating the boundary

## Strangler Fig Routing

Provide a routing configuration that:
1. Routes `{{service_name}}` traffic to the new service
2. Falls back to the monolith on failure (circuit breaker)
3. Includes feature flags per endpoint for gradual cutover
4. Logs comparison metrics between old and new paths

## Output

Deliver:
- Extracted service project files
- API contract (OpenAPI YAML)
- Data migration script
- Integration test suite
- Routing/proxy configuration
- Rollback procedure
