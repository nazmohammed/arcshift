# Arcshift Agent Team

This workspace uses a 5-phase agent pipeline for app modernisation. Each agent specialises in one phase and produces artifacts consumed by the next.

## Pipeline Flow

```
@assess → @architect → @migrate → @validate → @deploy
```

## Agents

### @assess (Phase 1: Discover & Assess)
- **Role**: Read-only codebase analyst
- **Input**: Legacy source code
- **Output**: Assessment report (JSON) with complexity scores, dependency map, tech debt inventory, migration blockers
- **Hands off to**: @architect

### @architect (Phase 2: Design)
- **Role**: Target architecture designer
- **Input**: Assessment report from @assess
- **Output**: Architecture Decision Records (ADRs), target service map, Azure service selections, decomposition boundaries
- **Hands off to**: @migrate

### @migrate (Phase 3: Code Migration)
- **Role**: Code transformer
- **Input**: Architecture design from @architect + legacy source code
- **Output**: Transformed source code in target framework (.NET 8 / FastAPI), updated dependencies, new project structure
- **Hands off to**: @validate

### @validate (Phase 4: Test & Validate)
- **Role**: Test engineer
- **Input**: Migrated code from @migrate + original code for parity reference
- **Output**: Test suites, parity reports, migration coverage metrics, functional equivalence verification
- **Hands off to**: @deploy

### @deploy (Phase 5: Deploy to Azure)
- **Role**: Infrastructure and deployment engineer
- **Input**: Validated migrated code + architecture design from @architect
- **Output**: Bicep/Terraform templates, CI/CD pipeline configuration, deployed Azure infrastructure

## Conventions

- Each agent uses the minimum tool set needed for its phase
- Agents reference methodology docs in `methodology/` for detailed procedures
- Agents use skills from `.github/skills/` for deep workflow automation
- Assessment reports use the JSON schema defined in `methodology/01-discover/`
