targetScope = 'resourceGroup'

@description('Short lowercase naming prefix; callers should also follow service-specific naming rules.')
@minLength(2)
@maxLength(12)
param prefix string = 'learn'

@description('Environment controls sample naming and retention metadata.')
@allowed([
  'dev'
  'test'
  'prod'
])
param environment string = 'dev'

@description('Non-sensitive names used to practice typed arrays and loop expressions.')
param workloads string[] = [
  'web'
  'worker'
]

var normalizedPrefix = toLower(prefix)
var retentionDays = environment == 'prod' ? 90 : 30
var workloadNames = [for workload in workloads: '${normalizedPrefix}-${environment}-${workload}']

@description('Calculated names; this example does not create Azure workloads.')
output workloadNames array = workloadNames

@description('Learning metadata only, not a deployed retention policy.')
output retentionDays int = retentionDays
