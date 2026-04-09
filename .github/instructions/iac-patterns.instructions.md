---
description: "Best practices for writing Azure IaC templates. Loaded automatically when editing Bicep or Terraform files."
applyTo: "**/*.bicep,**/*.tf"
---

# IaC Authoring Patterns

When working with infrastructure-as-code in this repository, follow these patterns:

## General Principles
- One Azure resource type per module
- All modules must be parameterised with sensible defaults
- Always output `id` and `name` from every module
- Use consistent naming: `{prefix}-{resource-type}-{environment}`
- Tag all resources with at minimum: `environment`, `project`, `managedBy`

## Bicep Conventions
- Use `@description()` decorators on all parameters
- Use `@allowed()` for constrained values
- Use `param location string = resourceGroup().location` as default
- Use `existing` keyword for referencing pre-existing resources
- Use modules (`module x './modules/y.bicep'`) not inline resources in main

## Terraform Conventions
- Use `variable` blocks with `description`, `type`, and `default` where appropriate
- Use `locals` for computed values and naming conventions
- Use `output` blocks for resource IDs and connection info
- Use `for_each` instead of `count` for named resource collections
- Pin provider versions in `required_providers`

## Security
- Never hardcode secrets — use Key Vault references
- Use managed identity for service-to-service auth
- Enable private endpoints for all data services
- Configure NSGs to deny all inbound by default, allow only required ports
- Use RBAC role assignments instead of access keys

## Networking
- Always create a VNet with separate subnets for compute, data, and management
- Use private endpoints for SQL, Cosmos DB, Storage, Key Vault
- Configure private DNS zones for private endpoint resolution
- Use NSGs on all subnets

## Monitoring
- Always deploy Log Analytics workspace + Application Insights together
- Configure diagnostic settings on all resources to send to Log Analytics
- Set up alerts for critical metrics (CPU, memory, errors, latency)
