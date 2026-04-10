---
mode: "agent"
description: "Generate comprehensive test suites for modernised code ensuring functional parity"
---

# Generate Test Suite

Generate a comprehensive test suite for the modernised **{{component_name}}** to ensure functional parity with the legacy implementation.

## Analysis

1. Read the legacy implementation and identify all behaviours
2. Read the modernised implementation and map corresponding behaviours
3. Identify any behaviour gaps or new capabilities

## Test Categories

### Unit Tests
For each public method/endpoint in `{{component_name}}`:
- Happy path with valid inputs
- Edge cases (null, empty, boundary values)
- Error handling and exception paths
- Input validation

### Integration Tests
- Database operations (CRUD, transactions, concurrency)
- External service calls (with mocks/stubs)
- Authentication and authorisation flows
- Message/event handling

### Parity Tests
For each legacy behaviour:

| Legacy Behaviour | Legacy Input | Expected Output | Parity Status |
|-----------------|-------------|-----------------|---------------|
| _description_ | _sample input_ | _expected result_ | pass/fail/skip |

## Conventions

- Use the target stack's standard test framework
- Follow AAA pattern (Arrange, Act, Assert)
- Name tests descriptively: `test_{method}_{scenario}_{expected_result}`
- Include test data factories, not inline magic values
- Mark parity tests with `@pytest.mark.parity` or `[Trait("Category", "Parity")]`

## Output

Deliver:
- Unit test files per component
- Integration test files per boundary
- Parity test report (markdown table)
- Test coverage summary
