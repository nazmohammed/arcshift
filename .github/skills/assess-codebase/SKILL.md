---
name: assess-codebase
description: "Full codebase assessment workflow for legacy application modernisation. Use when: running a complete assessment, analysing dependencies, scanning for anti-patterns, generating assessment reports, evaluating migration readiness."
---

# Codebase Assessment Workflow

Automated workflow that scans a legacy codebase and produces a structured assessment report for modernisation planning.

## When to Use

- Starting a new modernisation engagement
- Evaluating a legacy application for migration readiness
- Generating an assessment report for stakeholder review
- Running dependency analysis before architecture design

## Procedure

### Step 1: Identify the Target Codebase

Ask the user which directory contains the legacy application. Look for:
- Solution files (`.sln`) for .NET projects
- `requirements.txt` or `setup.py` or `pyproject.toml` for Python projects
- `package.json` for Node.js projects
- `pom.xml` or `build.gradle` for Java projects

### Step 2: Scan Project Structure

1. List all directories and files recursively
2. Identify entry points: `Program.cs`, `Startup.cs`, `Global.asax`, `app.py`, `main.py`
3. Count files by extension to determine language distribution
4. Identify configuration files: `web.config`, `appsettings.json`, `config.py`, `.env`
5. Check for containerisation: `Dockerfile`, `docker-compose.yml`
6. Check for CI/CD: `.github/workflows/`, `azure-pipelines.yml`, `Jenkinsfile`

### Step 3: Analyse Dependencies

**For .NET:**
- Parse `packages.config` or `<PackageReference>` elements in `.csproj` files
- Flag deprecated packages (e.g., `Microsoft.AspNet.WebApi`, `EntityFramework` < 7)
- Check target framework: `net48`, `net472`, `netcoreapp3.1` etc.

**For Python:**
- Parse `requirements.txt` or `pyproject.toml`
- Flag outdated packages (e.g., `Flask` < 2.0, `SQLAlchemy` < 2.0)
- Check Python version constraints

### Step 4: Identify Anti-Patterns

Search the codebase for common legacy anti-patterns:

| Anti-Pattern | .NET Indicators | Python Indicators |
|-------------|----------------|-------------------|
| God classes | Classes > 500 lines, > 20 methods | Classes > 300 lines, > 15 methods |
| Tight coupling | `new` keyword everywhere, no DI | Global singletons, import coupling |
| Hardcoded config | Connection strings in code | Credentials in source |
| No separation of concerns | Business logic in controllers | Logic in route handlers |
| Shared mutable state | `static` fields, `HttpContext.Current` | Module-level mutable variables |
| Circular dependencies | A → B → A project references | Circular imports |

### Step 5: Score Components

Rate each component on two axes (1-5 scale):

**Complexity Score:**
1. Simple — Few dependencies, clear boundaries
2. Low — Some coupling, manageable size
3. Medium — Moderate coupling, multiple responsibilities
4. High — Significant coupling, complex logic
5. Very High — Deep coupling, undocumented behaviour, platform-specific

**Migration Difficulty:**
1. Drop-in — Direct API equivalents exist
2. Low — Minor changes needed
3. Medium — Significant refactoring required
4. High — Architectural changes needed
5. Very High — Custom solutions required, potential blockers

### Step 6: Generate Assessment Report

Produce the JSON assessment report following the schema in the @assess agent definition.

### Step 7: Summarise Findings

Present a human-readable summary:
1. **Executive Summary** — One paragraph overview
2. **Key Metrics** — File count, LOC, dependencies, test coverage
3. **Top Risks** — 3-5 highest severity blockers
4. **Recommended Strategy** — Strangler fig, big bang, or branch by abstraction
5. **Next Steps** — Hand off to @architect with the assessment report
