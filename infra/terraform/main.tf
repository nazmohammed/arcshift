terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.100"
    }
  }
}

provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy = false
    }
  }
}

variable "app_name" {
  description = "Application name used for resource naming"
  type        = string
}

variable "location" {
  description = "Azure region for all resources"
  type        = string
  default     = "australiaeast"
}

variable "environment" {
  description = "Environment (dev, staging, prod)"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

locals {
  resource_group_name = "rg-${var.app_name}-${var.environment}"
  tags = {
    application = var.app_name
    environment = var.environment
    managed_by  = "arcshift"
  }
}

resource "azurerm_resource_group" "main" {
  name     = local.resource_group_name
  location = var.location
  tags     = local.tags
}

module "identity" {
  source   = "./modules/identity"
  app_name = var.app_name
  location = var.location
  tags     = local.tags
  resource_group_name = azurerm_resource_group.main.name
}

module "network" {
  source   = "./modules/network"
  app_name = var.app_name
  location = var.location
  tags     = local.tags
  resource_group_name = azurerm_resource_group.main.name
}

module "monitoring" {
  source   = "./modules/monitoring"
  app_name = var.app_name
  location = var.location
  tags     = local.tags
  resource_group_name = azurerm_resource_group.main.name
}

output "resource_group_name" {
  value = azurerm_resource_group.main.name
}
