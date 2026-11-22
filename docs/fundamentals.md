# Bicep and Infrastructure as Code

## Desired infrastructure in reviewable text

Infrastructure as Code records intended resources and relationships in files.
Version control supports review and change history; reproducible templates
reduce manual setup drift. None of this makes every change safe or reversible.

Bicep is a declarative language for Azure Resource Manager (ARM).
The compiler translates it into ARM JSON, and ARM evaluates/executes
the deployment against Azure management APIs.
Compilation is not cloud execution.

```mermaid
flowchart LR
  Source["Bicep + parameters"] --> Compiler["Bicep compiler"]
  Compiler --> JSON["ARM JSON"]
  JSON --> Review["Validate + what-if"]
  Review --> ARM["Approved ARM deployment"]
```

## Building blocks

- **Parameter:** typed external input; defaults are optional.
- **Variable:** named expression computed from other values.
- **Resource:** Azure object declaration with a symbolic name, type, and API version.
- **Existing resource:** a reference to an object already present, not ownership/import.
- **Module:** a separately compiled template with parameters, outputs, and scope.
- **Output:** result exposed to the caller; avoid secrets.
- **Scope:** tenant, management group, subscription, or resource group.

## Bicep, ARM JSON, and Terraform

| Aspect | Bicep | ARM JSON | Terraform |
| --- | --- | --- | --- |
| Authoring | Azure-focused typed DSL | Deployment template JSON | HCL with provider schemas |
| Execution | Compiles to ARM deployments | ARM deployments | Terraform graph/provider operations |
| Reuse | Local/registry modules | Nested/linked templates | Modules/registries |
| State model | Azure resource/deployment information | Azure resource/deployment information | Explicit Terraform state/backends |
| Primary scope | Azure management plane | Azure management plane | Multiple provider ecosystems |

Bicep does not maintain a Terraform-style local state file.
That does not mean resource lifecycle, deployment history, or drift disappear.
Deleting a deployment record deletes history, not its deployed resources.
Incremental deployments do not remove a resource simply because you removed
its declaration from the file.

Choose based on team operating model, service coverage, and lifecycle needs.
See [Terraform Overview](https://brown9804.github.io/Terraform-Overview/)
for the complementary workflow.
