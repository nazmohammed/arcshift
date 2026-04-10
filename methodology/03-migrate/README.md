# Phase 03: Migrate Code

**Agent:** `@migrate`
**Tools:** `read`, `edit`, `search`, `execute`
**Skills:** [migrate-dotnet](../../.github/skills/migrate-dotnet/SKILL.md), [migrate-python](../../.github/skills/migrate-python/SKILL.md)

## Objective

Execute the code migration from legacy stack to target stack, following the architecture decisions and migration sequence from Phase 02.

## Activities

### 1. Set Up Target Project
- Scaffold the target project structure using modern templates
- Configure build system (SDK-style csproj / pyproject.toml)
- Set up dependency injection and configuration

### 2. Migrate Component by Component
Follow the migration sequence defined in Phase 02. For each component:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Read Legacy  │────▶│  Transform   │────▶│Write Modern  │
│    Code      │     │   with AI    │     │    Code      │
└──────────────┘     └──────────────┘     └──────────────┘
       │                    │                     │
   Understand          Apply skill           Verify builds
   patterns            patterns              and runs
```

### 3. .NET Migration Path
1. Convert `.csproj` from legacy format to SDK-style
2. Update NuGet packages to modern equivalents
3. Migrate `Global.asax` → `Program.cs` with builder pattern
4. Convert controllers to modern ASP.NET Core patterns
5. Update Entity Framework to EF Core with async patterns
6. Migrate `web.config` / `app.config` to `appsettings.json`
7. Replace `System.Web` dependencies with `Microsoft.AspNetCore`
8. Update authentication from Forms/Windows to modern identity

### 4. Python Migration Path
1. Convert `requirements.txt` to `pyproject.toml`
2. Migrate Flask routes to FastAPI router with type hints
3. Replace dictionaries with Pydantic models
4. Update SQLAlchemy to 2.0 patterns with async sessions
5. Add dependency injection for services
6. Migrate configuration to Pydantic Settings
7. Update entry point for ASGI (uvicorn)
8. Replace synchronous calls with async/await

### 5. Handle Cross-Cutting Concerns
- Logging: Migrate to structured logging (Serilog / structlog)
- Configuration: Centralise with Azure App Configuration
- Secrets: Move to Azure Key Vault references
- Health checks: Add standard health endpoints

## Deliverables

| Artefact | Format | Description |
|----------|--------|-------------|
| Modernised Source | Code | Target stack implementation |
| Migration Log | Markdown | Component-by-component changes |
| Build Verification | CLI output | Proof that the code compiles/runs |
| Known Issues | Markdown | Items deferred or requiring manual review |

## Copilot Usage

```
@migrate Migrate the OrderService from .NET Framework 4.8 to .NET 8.
Follow ADR-001 and ADR-002 from docs/adrs/.
Start with the data access layer.
```

## Exit Criteria

- [ ] All prioritised components migrated to target stack
- [ ] Code compiles and starts without errors
- [ ] No deprecated API usage in migrated code
- [ ] Migration log documents every transformation applied
