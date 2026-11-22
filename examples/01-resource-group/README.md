# First resource group

## Purpose and architecture

Declare one Azure resource group from a subscription-scoped Bicep file.
A subscription deployment owns deployment history; the resource group
contains later workload resources. Creating a group alone creates no workload.

## Inputs and outputs

| Input | Meaning |
| --- | --- |
| `resourceGroupName` | Dedicated group name, default `rg-bicep-overview-dev` |
| `location` | Region for the group, default `eastus2` |
| `tags` | Non-sensitive purpose/environment metadata |

Outputs return the group name and management-plane ID, never credentials.
Read [main.bicep](https://github.com/brown9804/Bicep-Overview/blob/main/examples/01-resource-group/main.bicep) before running commands.

## Compile without Azure

From the repository root with Azure CLI/Bicep installed:

```shell
az bicep build --file examples/01-resource-group/main.bicep --stdout
```

Expected: subscription-scoped ARM JSON with one resource-group declaration.
No login or deployment is involved.

## Optional live validation and deployment

Requires an approved subscription, correct Azure CLI account, and scoped
resource-group/deployment permissions. The following is Bash syntax:

```bash
az login
az account set --subscription "$SUBSCRIPTION_ID"
az account show --output table
az deployment sub validate --location eastus2 \
  --template-file examples/01-resource-group/main.bicep
az deployment sub what-if --location eastus2 \
  --template-file examples/01-resource-group/main.bicep
az deployment sub create --name bicep-overview-group --location eastus2 \
  --template-file examples/01-resource-group/main.bicep
az group show --name rg-bicep-overview-dev --output table
```

Inspect every result and proposed action before create. `--location` identifies
deployment metadata placement; the Bicep `location` parameter places the group.
Use the same deployment metadata location when reusing a deployment name.

## Expected result, cleanup, costs, and limits

After an authorized successful deployment, inspect the group's region/tags.
A group itself has no direct service charge, but anything added later may.
Compilation alone does not verify RBAC, policy, regions, or runtime behavior.

For this dedicated disposable lab only, inspect its contents and then run:

```shell
az resource list --resource-group rg-bicep-overview-dev --output table
az group delete --name rg-bicep-overview-dev
```

Read the confirmation. Deletion includes **every resource in the group**.
Verify removal and account for locks/retention. Deleting a subscription
deployment record does not delete its deployed resources.
