targetScope = 'subscription'

@description('Name of the dedicated learning resource group.')
@minLength(1)
@maxLength(90)
param resourceGroupName string = 'rg-bicep-overview-dev'

@description('Approved Azure region for the group; deployment metadata has its own region.')
param location string = 'eastus2'

@description('Non-sensitive ownership and purpose tags.')
param tags object = {
  purpose: 'bicep-overview'
  environment: 'dev'
}

resource group 'Microsoft.Resources/resourceGroups@2025-04-01' = {
  name: resourceGroupName
  location: location
  tags: tags
}

@description('Management-plane ID of the group.')
output resourceGroupId string = group.id

@description('Resource group name for follow-on deployments.')
output resourceGroupName string = group.name
