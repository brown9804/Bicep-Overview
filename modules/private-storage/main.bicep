targetScope = 'resourceGroup'

@description('Globally unique lowercase alphanumeric storage name, 3-24 characters.')
@minLength(3)
@maxLength(24)
param storageAccountName string

@description('Approved Azure region for storage.')
param location string = resourceGroup().location

@description('Non-sensitive resource tags.')
param tags object = {}

resource storage 'Microsoft.Storage/storageAccounts@2025-06-01' = {
  name: storageAccountName
  location: location
  tags: tags
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    minimumTlsVersion: 'TLS1_2'
    supportsHttpsTrafficOnly: true
    allowBlobPublicAccess: false
    allowSharedKeyAccess: false
    publicNetworkAccess: 'Disabled'
    defaultToOAuthAuthentication: true
  }
}

@description('Management-plane ID; no keys or data-plane permissions are returned.')
output storageAccountId string = storage.id
