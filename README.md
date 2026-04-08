# Arcshift

**Copilot-Driven App Modernisation Accelerator**

Arcshift provides SI/Partners with a repeatable, GitHub Copilot-first methodology for modernising legacy applications. It combines custom Copilot agents, skills, and prompts with a documented 5-phase methodology, before/after sample apps, and modular Azure IaC templates.

## What's Included

| Component | Description |
|-----------|-------------|
| **5 Copilot Agents** | Custom agents for each modernisation phase (Assess → Architect → Migrate → Validate → Deploy) |
| **5 Copilot Skills** | Deep workflow automation: codebase assessment, .NET migration, Python migration, monolith decomposition, Azure landing zone |
| **6 Prompt Templates** | Reusable prompts for dependency analysis, migration planning, service extraction, test generation, DB schema analysis, API modernisation |
| **File Instructions** | Context-aware guidance for .NET, Python, and IaC files |
| **5-Phase Methodology** | Documented process with checklists, decision trees, and Copilot integration points |
| **Sample Apps** | Before/after skeleton apps in .NET (Acme Retail) and Python (Atlas Inventory) |
| **Azure IaC** | Modular Bicep and Terraform templates for target infrastructure |
| **Pattern Catalogue** | 6 proven modernisation patterns with implementation guidance |

## Quick Start

1. **Clone this repo** into your workspace:
   ```bash
   git clone https://github.com/nazmohammed/arcshift.git
   cd arcshift
   ```

2. **Open in VS Code** with GitHub Copilot installed

3. **Use the agents** — Open the Copilot Chat agent picker and select:
   - `@assess` — Analyse a legacy codebase
   - `@architect` — Design the target architecture
   - `@migrate` — Transform code to modern stack
   - `@validate` — Generate tests and verify parity
   - `@deploy` — Generate IaC and deploy to Azure

4. **Use the skills** — Type `/` in Copilot Chat:
   - `/assess-codebase` — Full assessment workflow
   - `/migrate-dotnet` — .NET Framework → .NET 8
   - `/migrate-python` — Flask → FastAPI
   - `/decompose-monolith` — Monolith → microservices
   - `/azure-landing-zone` — Generate Azure IaC

## 5-Phase Methodology

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  1. Discover │───▶│  2. Design  │───▶│  3. Migrate │───▶│ 4. Validate │───▶│  5. Deploy  │
│   & Assess   │    │ Architecture│    │    Code     │    │   & Test    │    │  to Azure   │
│              │    │             │    │             │    │             │    │             │
│ @assess      │    │ @architect  │    │ @migrate    │    │ @validate   │    │ @deploy     │
│ /assess-     │    │             │    │ /migrate-*  │    │ /generate-  │    │ /azure-     │
│  codebase    │    │             │    │ /decompose- │    │  tests      │    │  landing-   │
│              │    │             │    │  monolith   │    │             │    │  zone       │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

Each phase produces artifacts consumed by the next:
- **Discover** → Assessment Report (JSON) with complexity scores, dependency map, blockers
- **Design** → Architecture Decision Records (ADRs), target service map, Azure service selections
- **Migrate** → Transformed source code, updated dependencies, new project structure
- **Validate** → Test suites, parity reports, migration coverage metrics
- **Deploy** → Bicep/Terraform templates, CI/CD pipelines, deployed infrastructure

## Modernisation Patterns Supported

| Pattern | Use When |
|---------|----------|
| **Legacy Language Migration** | COBOL/VB6/Java → modern stack |
| **Monolith to Microservices** | Breaking apart large coupled applications |
| **On-Prem to Cloud** | Lift-and-shift or re-platform to Azure |
| **Framework Upgrade** | .NET Framework → .NET 8, Flask → FastAPI |
| **Strangler Fig** | Incremental migration wrapping legacy |
| **Database Per Service** | Decomposing shared databases |

## Target Stacks

- **.NET**: .NET Framework 4.x → .NET 8 on Azure Container Apps / App Service
- **Python**: Flask/Django → FastAPI on Azure Container Apps

## Project Structure

```
arcshift/
├── .github/
│   ├── copilot-instructions.md       # Global Copilot workspace instructions
│   ├── AGENTS.md                      # Agent team orchestration description
│   ├── agents/                        # 5 custom Copilot agents
│   ├── skills/                        # 5 Copilot skills with workflows
│   ├── instructions/                  # File-scoped Copilot instructions
│   └── prompts/                       # Reusable prompt templates
├── methodology/                       # 5-phase methodology documentation
├── samples/                           # Before/after sample applications
│   ├── acme-retail-dotnet/            # .NET modernisation sample
│   └── atlas-inventory-python/        # Python modernisation sample
├── infra/                             # Azure IaC templates
│   ├── bicep/                         # Bicep modules
│   └── terraform/                     # Terraform modules
├── patterns/                          # Modernisation pattern catalogue
└── docs/                              # Partner guide and ADR templates
```

## For SI/Partners

See the [Partner Guide](docs/partner-guide.md) for:
- How to adopt Arcshift for customer engagements
- Customising agents and skills for specific scenarios
- Running assessments and generating proposals
- Estimating modernisation effort from assessment reports

## License

[MIT](LICENSE)
