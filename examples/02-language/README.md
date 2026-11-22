# Expressions without workload resources

## Purpose

Practice allowed values, typed arrays, string interpolation, normalization,
conditional expressions, and loops before managing a workload.
This example declares no resources. Retention is learning metadata, not an
Azure policy or storage retention configuration.

## Inputs and expected output

Defaults produce names `learn-dev-web` and `learn-dev-worker`, with a
`retentionDays` output of 30. Choosing `prod` changes the derived names and
returns 90. `environment` accepts only `dev`, `test`, or `prod`.
`prefix` has length bounds, not a universal Azure service naming validator.

## Source and offline validation

Read [main.bicep](https://github.com/brown9804/Bicep-Overview/blob/main/examples/02-language/main.bicep). From the repository root:

```shell
az bicep build --file examples/02-language/main.bicep --stdout
```

Expected: resource-group-scoped ARM JSON, an empty resources list, parameter
constraints, and output expressions. Expressions involving parameters are
evaluated by ARM at deployment time, not printed as final values by compilation.

## Optional evaluation in Azure

If you already have an approved dedicated learning resource group:

```bash
az deployment group what-if --resource-group "$RESOURCE_GROUP" \
  --template-file examples/02-language/main.bicep --parameters environment=prod
az deployment group create --name bicep-overview-language \
  --resource-group "$RESOURCE_GROUP" --template-file examples/02-language/main.bicep \
  --parameters environment=prod --query properties.outputs
```

Expected after successful evaluation: prod names and retention 90, but no
workload resources. Incremental deployment is used; **never switch this
empty-resource example to complete mode**, which can delete unrelated objects.

## Cleanup and limitations

Offline compilation needs no cloud cleanup. Optional live evaluation creates
deployment history that can be removed with `az deployment group delete`
using the same group/name; that command removes history only.
Do not delete an existing shared group to clean up this exercise.
Protect real deployment outputs if you adapt the example to sensitive data.

**Exercise:** add a third non-sensitive workload name and predict the loop's
output before evaluating it.
