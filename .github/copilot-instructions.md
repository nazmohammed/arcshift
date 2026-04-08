# Arcshift Workspace Instructions

You are working in the **Arcshift** repository — a Copilot-driven app modernisation accelerator for SI/Partners.

## Project Context

Arcshift provides a 5-phase methodology for modernising legacy applications:
1. **Discover & Assess** — Analyse legacy codebases for complexity, dependencies, and migration blockers
2. **Design** — Propose target architecture with decomposition boundaries and Azure service selections
3. **Migrate** — Transform code from legacy frameworks to modern stacks (.NET 8, FastAPI)
4. **Validate** — Generate tests, run parity checks, verify functional equivalence
5. **Deploy** — Generate Azure IaC (Bicep/Terraform), configure CI/CD, deploy to Azure

## Vocabulary

Use these terms consistently:
- **Assessment report** — JSON output from Phase 1 with complexity scores and dependency maps
- **ADR** — Architecture Decision Record documenting a design choice with context and consequences
- **Strangler fig** — Incremental migration pattern that wraps legacy functionality
- **Branch by abstraction** — Introduce an abstraction layer, build new implementation behind it, switch over
- **Anti-corruption layer** — Adapter between legacy and modern systems preventing legacy patterns from leaking
- **Bounded context** — A logical boundary within a monolith that maps to a potential microservice
- **Parity check** — Automated comparison of legacy and migrated system behaviour

## Target Stacks

When modernising code, target these stacks:
- **.NET**: .NET 8+, minimal hosting, EF Core, Azure Container Apps or App Service
- **Python**: FastAPI, async/await, Pydantic v2, SQLAlchemy 2.0, Azure Container Apps

## Conventions

- Use conventional commit messages: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`
- Assessment reports follow the JSON schema in `methodology/01-discover/`
- ADRs use the template in `docs/architecture-decision-records/`
- IaC is modular — one Azure resource type per Bicep/Terraform module
- Sample apps in `samples/` are representative skeletons, not full production apps

## File Structure Awareness

- `.github/agents/` — Custom Copilot agents (one per modernisation phase)
- `.github/skills/` — Deep workflow skills with scripts and references
- `.github/prompts/` — Reusable prompt templates for common tasks
- `.github/instructions/` — File-scoped instructions for .NET, Python, and IaC
- `methodology/` — 5-phase methodology documentation
- `samples/` — Before/after sample applications
- `infra/` — Azure IaC templates (Bicep and Terraform)
- `patterns/` — Modernisation pattern catalogue
- `docs/` — Partner guide and ADR templates
