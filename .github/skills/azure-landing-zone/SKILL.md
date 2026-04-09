---
name: azure-landing-zone
description: "Generate Azure infrastructure templates for modernised applications. Use when: creating Bicep or Terraform modules, setting up Container Apps or App Service, configuring networking and monitoring, generating azure.yaml for azd, building Azure landing zones for migrated apps."
---

# Azure Landing Zone Generation Workflow

Step-by-step workflow for generating modular Azure IaC templates tailored to the target architecture.

## When to Use

- Generating Azure infrastructure for a modernised application
- Creating Bicep and/or Terraform modules for Azure services
- Setting up Container Apps, App Service, or Functions hosting
- Configuring networking (VNet, private endpoints) and monitoring

## Prerequisites

- Architecture design and service map from @architect
- Decision on hosting model: Container Apps (default) vs App Service vs Functions

## Procedure

### Step 1: Review Architecture

Read the service map from @architect and identify:
- Number of services and their hosting requirements
- Data stores needed (Azure SQL, Cosmos DB, Storage)
- Networking requirements (VNet, private endpoints, NSGs)
- Monitoring requirements (Application Insights, Log Analytics)
- Security requirements (Key Vault, managed identity, RBAC)

### Step 2: Select Azure Services

| Application Pattern | Recommended Azure Service |
|--------------------|--------------------------|
| Containerised microservice | Azure Container Apps |
| Traditional web app | Azure App Service |
| Event-driven / triggers | Azure Functions |
| Relational data | Azure SQL Database |
| Document/NoSQL data | Azure Cosmos DB |
| File/blob storage | Azure Storage Account |
| Secrets management | Azure Key Vault |
| API management | Azure API Management |
| Message broker | Azure Service Bus |
| Caching | Azure Cache for Redis |

### Step 3: Generate Bicep Modules

For each Azure resource type, generate a standalone Bicep module:

**Module template:**
```bicep
@description('Required. Name of the resource.')
param name string

@description('Required. Location for the resource.')
param location string = resourceGroup().location

@description('Optional. Tags for the resource.')
param tags object = {}

// Resource-specific parameters...

resource myResource 'Microsoft.Xxx/yyy@2024-01-01' = {
  name: name
  location: location
  tags: tags
  properties: {
    // ...
  }
}

output id string = myResource.id
output name string = myResource.name
```

Generate modules for:
1. `network.bicep` — VNet, subnets, NSGs, private endpoints
2. `container-apps.bicep` — Container Apps Environment + apps
3. `app-service.bicep` — App Service Plan + Web Apps
4. `sql.bicep` — Azure SQL Server + Database
5. `cosmos.bicep` — Cosmos DB account + database + containers
6. `key-vault.bicep` — Key Vault with access policies
7. `monitoring.bicep` — Log Analytics + Application Insights

### Step 4: Generate Terraform Modules

Mirror each Bicep module as a Terraform module:

**Module template:**
```hcl
variable "name" {
  description = "Name of the resource"
  type        = string
}

variable "location" {
  description = "Azure region"
  type        = string
}

variable "tags" {
  description = "Tags for the resource"
  type        = map(string)
  default     = {}
}

# Resource-specific variables...

resource "azurerm_xxx" "main" {
  name                = var.name
  location            = var.location
  resource_group_name = var.resource_group_name
  tags                = var.tags
}

output "id" {
  value = azurerm_xxx.main.id
}
```

### Step 5: Generate Main Orchestrator

**Bicep** (`main.bicep`):
- Call each module with parameters
- Wire outputs between modules (e.g., VNet ID → Container Apps)
- Set up RBAC role assignments

**Terraform** (`main.tf`):
- Call each module
- Configure provider and backend
- Wire outputs between modules

### Step 6: Generate azure.yaml

```yaml
name: <app-name>
metadata:
  template: arcshift-landing-zone
services:
  <service-name>:
    project: ./src/<service-name>
    host: containerapp
    language: dotnet | python
```

### Step 7: Generate Deployment Docs

Create `DEPLOY.md` with:
1. Prerequisites (Azure CLI, azd, Terraform)
2. Environment setup instructions
3. `azd up` or `terraform apply` commands
4. Post-deployment verification steps
5. Monitoring and troubleshooting links
