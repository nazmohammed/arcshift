# Phase 05: Deploy to Azure

**Agent:** `@deploy`
**Tools:** `read`, `edit`, `search`, `execute`
**Skill:** [azure-landing-zone](../../.github/skills/azure-landing-zone/SKILL.md)

## Objective

Generate infrastructure-as-code, CI/CD pipelines, and deployment documentation to ship the modernised application to Azure.

## Activities

### 1. Select Azure Services
Based on the architecture decisions (ADRs):

| Requirement | Azure Service | SKU/Tier |
|------------|--------------|----------|
| Web hosting | Container Apps / App Service | Consumption / B1 |
| Database | Azure SQL / PostgreSQL Flexible | Basic / Burstable |
| Caching | Azure Cache for Redis | Basic C0 |
| Messaging | Service Bus / Event Grid | Basic |
| Identity | Entra ID | N/A |
| Secrets | Key Vault | Standard |
| Monitoring | Application Insights | Pay-as-you-go |

### 2. Generate Infrastructure as Code

#### Bicep Modules
Generate modular Bicep files in `infra/bicep/`:
- `main.bicep` — Orchestrator with parameters
- `modules/container-app.bicep` — Container Apps environment and apps
- `modules/sql.bicep` — Database with firewall rules
- `modules/keyvault.bicep` — Key Vault with access policies
- `modules/monitoring.bicep` — Log Analytics + App Insights
- `modules/network.bicep` — VNet, subnets, private endpoints
- `modules/identity.bicep` — Managed identities and role assignments

#### Terraform Modules
Generate equivalent Terraform in `infra/terraform/`:
- `main.tf`, `variables.tf`, `outputs.tf` — Root module
- `modules/` — One module per resource type

### 3. Configure Azure Developer CLI
Generate `azure.yaml` for `azd up` deployment:
```yaml
name: {application-name}
services:
  api:
    host: containerapp
    project: ./src/api
  web:
    host: containerapp
    project: ./src/web
```

### 4. Create CI/CD Pipeline
Generate GitHub Actions workflow:
- Build and test on PR
- Deploy to staging on merge to `main`
- Promote to production with manual approval
- Include infrastructure provisioning step

### 5. Write Deployment Runbook
Document the deployment process:
- Prerequisites (Azure subscription, CLI tools, permissions)
- Environment setup (dev, staging, production)
- Deployment commands
- Rollback procedure
- Monitoring and alerting setup

## Deliverables

| Artefact | Format | Description |
|----------|--------|-------------|
| Bicep Modules | `.bicep` | Modular infrastructure templates |
| Terraform Modules | `.tf` | Alternative IaC option |
| azure.yaml | YAML | Azure Developer CLI configuration |
| CI/CD Pipeline | YAML | GitHub Actions workflow |
| Deployment Runbook | Markdown | Step-by-step deployment guide |

## Copilot Usage

```
@deploy Generate Azure infrastructure for this application.
Target: Azure Container Apps with Azure SQL Database.
Include VNet integration, Key Vault, and Application Insights.
Use Bicep modules following the azure-landing-zone skill.
```

## Exit Criteria

- [ ] IaC templates generate valid infrastructure (lint + what-if pass)
- [ ] `azd up` deploys successfully to a dev environment
- [ ] CI/CD pipeline triggers on PR and merge
- [ ] Application health checks pass post-deployment
- [ ] Deployment runbook reviewed and tested
