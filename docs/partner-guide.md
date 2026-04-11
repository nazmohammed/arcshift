# Partner Guide

A guide for System Integrators (SIs) and Microsoft Partners using Arcshift to deliver application modernisation engagements.

## Overview

Arcshift provides a structured, Copilot-driven methodology for modernising legacy applications to Azure. This guide walks you through how to use the accelerator with your clients.

## Prerequisites

### Tools
- GitHub Copilot Business or Enterprise license
- VS Code with GitHub Copilot extension
- Azure CLI (`az`) and Azure Developer CLI (`azd`)
- .NET 8 SDK and/or Python 3.11+

### Azure
- Azure subscription with Contributor access
- Resource group for the target environment
- Entra ID tenant for authentication

### Knowledge
- Familiarity with the client's legacy technology stack
- Understanding of target Azure services
- Basic experience with Infrastructure as Code (Bicep or Terraform)

## Engagement Workflow

### 1. Fork and Customise

```bash
# Fork the repository for the client engagement
gh repo fork nazmohammed/arcshift --clone --remote

# Create a client-specific branch
git checkout -b client/{client-name}
```

### 2. Add Client Codebase

```
samples/
  {client-name}/
    before/           ← Copy legacy codebase here
    after/            ← Modernised code will be generated here
    docs/
      assessment.json ← Phase 01 output
      adrs/           ← Phase 02 ADRs
      migration-log/  ← Phase 03 tracking
      parity-report/  ← Phase 04 results
```

### 3. Customise Agents (Optional)

If the client uses a stack not covered by default:

- Add new `.instructions.md` files for client-specific frameworks
- Add new `SKILL.md` files for client-specific migration patterns
- Modify agent definitions if the workflow differs

### 4. Execute the Methodology

Walk through each phase sequentially:

| Phase | Agent Command | Duration | Client Involvement |
|-------|-------------|----------|-------------------|
| 01 Discover | `@assess` | 1-2 days | Review assessment report |
| 02 Design | `@architect` | 2-3 days | Approve ADRs |
| 03 Migrate | `@migrate` | 1-4 weeks | Code review |
| 04 Validate | `@validate` | 3-5 days | Accept parity report |
| 05 Deploy | `@deploy` | 2-3 days | Verify deployment |

### 5. Deliver Artefacts

At the end of the engagement, deliver:
- Modernised application source code
- Infrastructure-as-code templates
- CI/CD pipeline configuration
- Architecture Decision Records
- Migration report and lessons learned

## Customisation Points

### Adding a New Target Stack

1. Create a new skill: `.github/skills/{skill-name}/SKILL.md`
2. Create instruction files: `.github/instructions/{stack}-modernise.instructions.md`
3. Add prompts: `.github/prompts/{task}.prompt.md`
4. Update the migrate agent to reference the new skill

### Adding a New Pattern

1. Create a pattern doc: `patterns/{pattern-name}/README.md`
2. Reference it from the decompose-monolith skill
3. Add code examples for the client's technology stack

### Client-Specific Agents

For complex engagements, create client-specific agents:

```yaml
# .github/agents/client-{name}.agent.md
---
description: "Migration agent customised for {client} technology stack"
tools: [read, edit, search, execute]
---
```

## Pricing Guidance

| Engagement Size | Components | Typical Duration |
|----------------|-----------|-----------------|
| Small | 1-5 services, single stack | 4-6 weeks |
| Medium | 5-15 services, mixed stacks | 8-12 weeks |
| Large | 15+ services, complex integrations | 12-24 weeks |

Arcshift typically reduces modernisation effort by 30-50% compared to manual migration through AI-assisted code generation, automated assessment, and structured methodology.

## Support

- **Issues**: File issues on the GitHub repository
- **Discussions**: Use GitHub Discussions for questions
- **Contributions**: See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines
