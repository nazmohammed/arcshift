# Phase 04: Validate & Test

**Agent:** `@validate`
**Tools:** `read`, `edit`, `search`, `execute`
**Prompt:** [generate-tests](../../.github/prompts/generate-tests.prompt.md)

## Objective

Verify that the modernised codebase maintains functional parity with the legacy system, generating comprehensive test suites and a parity report.

## Activities

### 1. Generate Test Suites
For each migrated component, generate:

- **Unit tests** — Validate individual methods and classes
- **Integration tests** — Validate component interactions and data access
- **Parity tests** — Compare legacy vs. modern behaviour for identical inputs

### 2. Run Parity Checks
Execute the same test scenarios against both legacy and modern code:

```
┌─────────────┐     ┌──────────────┐
│  Test Input  │────▶│ Legacy Code  │──▶ Expected Output
│             │     └──────────────┘
│             │     ┌──────────────┐
│             │────▶│ Modern Code  │──▶ Actual Output
└─────────────┘     └──────────────┘
                           │
                    Compare Results
                           │
                    ┌──────────────┐
                    │Parity Report │
                    └──────────────┘
```

### 3. Analyse Gaps
For each parity failure:

| Behaviour | Legacy Output | Modern Output | Gap Type | Resolution |
|-----------|-------------|---------------|----------|-----------|
| _description_ | _value_ | _value_ | intentional/bug/missing | fix/accept/defer |

### 4. Performance Baseline
- Measure response times for critical endpoints
- Compare memory usage between legacy and modern
- Identify performance regressions requiring optimisation

### 5. Security Scan
- Run dependency vulnerability scan (Dependabot / Safety)
- Check for common security anti-patterns in migrated code
- Verify authentication and authorisation flows

## Deliverables

| Artefact | Format | Description |
|----------|--------|-------------|
| Test Suite | Code | Unit + integration + parity tests |
| Parity Report | JSON | Pass/fail/skip counts with gap analysis |
| Coverage Report | HTML/JSON | Code coverage metrics |
| Performance Baseline | Table | Response times and resource usage |
| Security Scan | Report | Vulnerability findings |

## Copilot Usage

```
@validate Generate parity tests for the OrderService.
Compare the legacy .NET Framework implementation in samples/acme-retail-dotnet/before/
with the modern .NET 8 implementation in samples/acme-retail-dotnet/after/.
```

## Exit Criteria

- [ ] All parity tests pass or gaps are documented and accepted
- [ ] Code coverage meets minimum threshold (80%+)
- [ ] No critical or high severity vulnerabilities
- [ ] Performance baseline shows no regressions > 20%
- [ ] Parity report reviewed and signed off by team
