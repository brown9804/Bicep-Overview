# Private storage module

## Purpose and Azure services

Create a StorageV2 account with Standard LRS replication, TLS 1.2, HTTPS,
public networking disabled, public blobs disabled, and shared keys disabled.
Return only its management-plane ID. This is a private storage foundation,
not a usable application storage solution on its own.

## Prerequisites and input contract

- Offline: Azure CLI with Bicep installed.
- Live: an approved group/subscription, deployment permission, policy and
  region review, a globally unique storage name, and cost approval.
- Later data use: private endpoints, private DNS, routing, and Entra data roles.

`storageAccountName` is required; it must be lowercase alphanumeric and 3-24
characters. Decorators validate length, not character rules or global uniqueness.
`location` defaults to the target group's region. `tags` defaults to an empty object.

Read [main.bicep](https://github.com/brown9804/Bicep-Overview/blob/main/modules/private-storage/main.bicep). The
[modular foundation](https://github.com/brown9804/Bicep-Overview/blob/main/examples/03-modular-foundation/README.md) is the
working caller with actual module wiring.

## Compile and optionally deploy

From the repository root:

```shell
az bicep build --file modules/private-storage/main.bicep --stdout
```

Expected: ARM JSON with private-only account properties. This is not a live
connectivity test. For standalone use in an existing dedicated group, Bash:

```bash
az deployment group validate --resource-group "$RESOURCE_GROUP" \
  --template-file modules/private-storage/main.bicep \
  --parameters storageAccountName="$BICEP_STORAGE_NAME"
az deployment group what-if --resource-group "$RESOURCE_GROUP" \
  --template-file modules/private-storage/main.bicep \
  --parameters storageAccountName="$BICEP_STORAGE_NAME"
az deployment group create --name bicep-overview-storage --resource-group "$RESOURCE_GROUP" \
  --template-file modules/private-storage/main.bicep \
  --parameters storageAccountName="$BICEP_STORAGE_NAME"
```

Authenticate and select the intended subscription first; review what-if.
After successful deployment, verify the account's public network and
authentication settings through Azure's management plane.
No container, endpoint, DNS zone, data role, backup, or workload is included.

## Security, costs, and cleanup

Storage capacity/operations and follow-on network services can incur charges.
Successful management deployment does not mean a client can reach storage;
restricted access here is intentional. Use managed identity and scoped
Entra data roles for later workloads.

Delete only this account after reviewing its data and dependencies:

```bash
az storage account delete --name "$BICEP_STORAGE_NAME" --resource-group "$RESOURCE_GROUP"
```

Read the confirmation and verify removal. Do not delete a shared group.
For the composed disposable foundation, use its documented group cleanup instead.
