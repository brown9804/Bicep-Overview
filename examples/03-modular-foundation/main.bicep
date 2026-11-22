targetScope = 'subscription'

@description('Short naming prefix; no credentials or identifiers belong here.')
@minLength(2)
@maxLength(12)
param prefix string = 'learn'

@description('Environment label; use a dedicated group per environment.')
@allowed([
  'dev'
  'test'
  'prod'
])
param environment string = 'dev'

@description('Approved region; deployment metadata region is provided through Azure CLI.')
param location string = 'eastus2'

@description('Globally unique lowercase alphanumeric storage account name.')
@minLength(3)
@maxLength(24)
param storageAccountName string

var baseName = '${toLower(prefix)}-${environment}'
var commonTags = {
  environment: environment
  purpose: 'bicep-overview'
}

resource group 'Microsoft.Resources/resourceGroups@2025-04-01' = {
  name: 'rg-${baseName}'
  location: location
  tags: commonTags
}

module network '../../modules/isolated-network/main.bicep' = {
  name: 'network-${environment}'
  scope: group
  params: {
    virtualNetworkName: '${baseName}-vnet'
    location: location
    tags: commonTags
  }
}

module storage '../../modules/private-storage/main.bicep' = {
  name: 'storage-${environment}'
  scope: group
  params: {
    storageAccountName: storageAccountName
    location: location
    tags: commonTags
  }
}

@description('Group to inspect and, for a disposable lab, delete after verification.')
output resourceGroupName string = group.name

@description('Network module result.')
output virtualNetworkId string = network.outputs.virtualNetworkId

@description('Storage module result; not data access or a credential.')
output storageAccountId string = storage.outputs.storageAccountId
