# Validate, preview, deploy, and clean up

## Distinct validation layers

| Check | Needs Azure login? | Establishes |
| --- | --- | --- |
| Bicep build/lint | No for local modules | Syntax/types, supported schema diagnostics, linter results |
| Compiled-template tests | No | Specific security/scope/output contracts in generated JSON |
| ARM validate | Yes | Deployment validation in the selected context |
| What-if | Yes | Predicted changes; some values may be unresolved |
| Create and management checks | Yes | Actual deployment result and observed resources |
| Runtime/data checks | Yes | Application behavior and private/data access |

Compilation cannot prove RBAC, policies, quotas, regional availability,
private connectivity, costs, or runtime success.
What-if can report uncertainty; read its limitations rather than interpreting
it as a guaranteed simulation.

```mermaid
flowchart LR
  Code["Review source and inputs"] --> Build["Compile + tests"]
  Build --> Context["Confirm subscription/scope"]
  Context --> Preview["Validate + what-if"]
  Preview --> Approval["Review and approve"]
  Approval --> Deploy["Create"]
  Deploy --> Verify["Verify + cleanup"]
```

## Optional live workflow

Use a dedicated approved environment and review every template/module.
The [project README](examples/examples--03-modular-foundation.md) includes
complete commands. The command family must match `targetScope`.
Authentication is an explicit step; routine CI does not authenticate.

For automation, use approved workload identity federation/OIDC and scoped
permissions instead of stored client secrets. Separate template checks from
privileged resource deployment. Never expose credentials to untrusted PR code.

## Parameters and deployment records

Protect local parameters and outputs. `@secure()` prevents ordinary parameter
logging in deployment records but is not permission to commit a secret.
Avoid secrets in outputs and do not use a parameter compilation artifact as
a general-purpose secret distribution mechanism.

Subscription deployment `--location` places deployment metadata.
It need not match every resource's region, and reusing a deployment name
with a different metadata region can fail.

## Failure and retry

ARM deployments are not universally transactional rollbacks. Earlier resources
may already exist after a later failure. Inspect deployment operations,
correct the cause, rerun validation/what-if, and review the new proposed changes.
Do not start deleting unrelated objects to clear an error.

## Incremental mode and intentional deletion

These samples use default incremental behavior. Removing a resource from
the file does not remove the existing Azure object. Do not switch casually
to complete mode, especially for an empty or partial template.
Review [deployment stacks](https://learn.microsoft.com/azure/azure-resource-manager/bicep/deployment-stacks)
when explicit lifecycle ownership is required; they are not enabled by this lab.

For disposable examples, the README lists reviewed resource/group deletions.
Deleting deployment history removes the record, not infrastructure.
Inspect all group contents before group deletion, respect locks/retention,
verify cleanup, and review lingering costs.
