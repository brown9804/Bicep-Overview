targetScope = 'resourceGroup'

@description('Virtual network name.')
@minLength(1)
@maxLength(64)
param virtualNetworkName string

@description('Approved Azure region for network resources.')
param location string = resourceGroup().location

@description('VNet CIDR; review containment and overlap before deployment.')
param addressPrefix string = '10.40.0.0/16'

@description('Workload subnet CIDR contained in the VNet prefix.')
param subnetPrefix string = '10.40.1.0/24'

@description('Non-sensitive resource tags.')
param tags object = {}

resource securityGroup 'Microsoft.Network/networkSecurityGroups@2025-01-01' = {
  name: '${virtualNetworkName}-nsg'
  location: location
  tags: tags
  properties: {
    securityRules: [
      {
        name: 'deny-all-inbound'
        properties: {
          priority: 4096
          direction: 'Inbound'
          access: 'Deny'
          protocol: '*'
          sourcePortRange: '*'
          destinationPortRange: '*'
          sourceAddressPrefix: '*'
          destinationAddressPrefix: '*'
        }
      }
    ]
  }
}

resource network 'Microsoft.Network/virtualNetworks@2025-01-01' = {
  name: virtualNetworkName
  location: location
  tags: tags
  properties: {
    addressSpace: {
      addressPrefixes: [
        addressPrefix
      ]
    }
    subnets: [
      {
        name: 'workload'
        properties: {
          addressPrefix: subnetPrefix
          networkSecurityGroup: {
            id: securityGroup.id
          }
        }
      }
    ]
  }
}

@description('Management-plane ID of the VNet.')
output virtualNetworkId string = network.id
