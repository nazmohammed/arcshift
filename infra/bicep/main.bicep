targetScope = 'subscription'

@description('Application name used for resource naming')
param appName string

@description('Azure region for all resources')
param location string = 'australiaeast'

@description('Environment (dev, staging, prod)')
@allowed(['dev', 'staging', 'prod'])
param environment string = 'dev'

var resourceGroupName = 'rg-${appName}-${environment}'
var tags = {
  application: appName
  environment: environment
  managedBy: 'arcshift'
}

resource rg 'Microsoft.Resources/resourceGroups@2023-07-01' = {
  name: resourceGroupName
  location: location
  tags: tags
}

module identity 'modules/identity.bicep' = {
  scope: rg
  name: 'identity'
  params: {
    appName: appName
    location: location
    tags: tags
  }
}

module network 'modules/network.bicep' = {
  scope: rg
  name: 'network'
  params: {
    appName: appName
    location: location
    tags: tags
  }
}

module monitoring 'modules/monitoring.bicep' = {
  scope: rg
  name: 'monitoring'
  params: {
    appName: appName
    location: location
    tags: tags
  }
}

module keyvault 'modules/keyvault.bicep' = {
  scope: rg
  name: 'keyvault'
  params: {
    appName: appName
    location: location
    tags: tags
    principalId: identity.outputs.principalId
  }
}

module sql 'modules/sql.bicep' = {
  scope: rg
  name: 'sql'
  params: {
    appName: appName
    location: location
    tags: tags
    subnetId: network.outputs.sqlSubnetId
  }
}

module containerApp 'modules/container-app.bicep' = {
  scope: rg
  name: 'containerApp'
  params: {
    appName: appName
    location: location
    tags: tags
    identityId: identity.outputs.identityId
    subnetId: network.outputs.appSubnetId
    appInsightsConnectionString: monitoring.outputs.appInsightsConnectionString
  }
}

output resourceGroupName string = rg.name
output containerAppFqdn string = containerApp.outputs.fqdn
