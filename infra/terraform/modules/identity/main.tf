variable "app_name" {
  type = string
}

variable "location" {
  type = string
}

variable "tags" {
  type = map(string)
}

variable "resource_group_name" {
  type = string
}

resource "azurerm_user_assigned_identity" "main" {
  name                = "id-${var.app_name}"
  location            = var.location
  resource_group_name = var.resource_group_name
  tags                = var.tags
}

output "identity_id" {
  value = azurerm_user_assigned_identity.main.id
}

output "principal_id" {
  value = azurerm_user_assigned_identity.main.principal_id
}

output "client_id" {
  value = azurerm_user_assigned_identity.main.client_id
}
