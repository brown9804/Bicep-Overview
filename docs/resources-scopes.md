# Resources and deployment scopes

## Symbolic name versus Azure name

In `resource group 'Microsoft.Resources/resourceGroups@2025-04-01'`,
`group` is a local code symbol. The `name` property supplies the Azure name.
The type/API version determine the available properties and scope rules.
Choose a supported API and read its official resource reference.

## Match scope to the deployment command

| `targetScope` | CLI family | Typical use |
| --- | --- | --- |
| `resourceGroup` | `az deployment group` | Most workload resources |
| `subscription` | `az deployment sub` | Create resource groups and subscription-scoped objects |
| `managementGroup` | `az deployment mg` | Organization-level deployments/policy |
| `tenant` | `az deployment tenant` | Tenant-scoped deployment operations |

Creating a resource group is subscription-scoped. Creating a storage account
inside it is resource-group-scoped. Merely passing a group name to a
parameter does not change a template's target scope.
Our foundation uses scoped modules to bridge those boundaries.

## Existing resources and extensions

Use `existing` when referencing a resource already deployed.
It does not create the resource or adopt a lifecycle state mapping.
The identity still needs permissions for any reads such as properties or keys.
Cross-scope existing references can use supported scope functions.

Extension resources such as role assignments attach to a specific scope.
Plan least privilege; a management-plane owner role is not a substitute for
carefully scoped workload/data roles.

## Dependencies

`securityGroup.id` in the VNet subnet's NSG association tells Bicep that the
network needs the NSG. The compiled template includes the appropriate dependency.
Prefer these references over unnecessary `dependsOn`.
Use explicit dependencies only for real relationships not captured by data flow.

## Lifecycle is not source-file deletion

Incremental deployments keep resources not declared in the current template.
Do not expect deleting a line to delete infrastructure. Review the
[deployment and cleanup guide](deployment.md) for deliberate lifecycle actions.
The empty language example must never be used in complete mode against a
group containing unrelated resources.

**Exercise:** trace the scope of the foundation root, group declaration, and
both modules. Identify the correct CLI family for the root and for standalone storage.
