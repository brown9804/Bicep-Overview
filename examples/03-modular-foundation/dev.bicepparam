using './main.bicep'

param prefix = 'learn'
param environment = 'dev'
param location = 'eastus2'
param storageAccountName = readEnvironmentVariable('BICEP_STORAGE_NAME')
