# Parameters, expressions, and outputs

## Inputs and decorators

Bicep supports strings, integers, booleans, objects, arrays, and user-defined
types. Use the smallest meaningful interface. `@description` explains
intent; decorators such as `@allowed` and `@minLength` constrain values.

The language example uses a typed string array and a bounded environment:

```bicep title="examples/02-language/main.bicep"
--8<-- "examples/02-language/main.bicep"
```

## Follow the expression flow

1. `prefix` is normalized by `toLower`.
2. A conditional selects prod retention metadata of 90, otherwise 30.
3. A loop derives one name per workload.
4. Outputs expose the calculated names and integer.

No storage retention policy or workload resource is deployed. This distinction
matters: a descriptive output alone does not configure a service.
Compile with:

```shell
az bicep build --file examples/02-language/main.bicep --stdout
```

Expected JSON contains constraints, expressions, and an empty resource collection.
The compiler checks types; ARM evaluates parameter-dependent results.
With defaults, evaluation produces dev names and 30.

## Parameter files and evaluation time

`.bicepparam` files use `using` to bind an actual template, gaining typed
parameter checking. They are not JSON files and not secret stores.
Our foundation reads `BICEP_STORAGE_NAME` through `readEnvironmentVariable`
at **parameter compilation time**; ARM does not look up the local variable.
Set it explicitly before build/deployment.

## Validation boundaries

Storage-name length decorators do not enforce lowercase characters or global
uniqueness. A string CIDR is not proof of network containment or no overlap.
Type safety and live service validation complement, rather than replace, one another.

Use `@secure()` for sensitive parameters when needed; never emit secrets
through outputs or commit their values.

**Exercise:** predict the language output with `prefix = 'TEAM'`,
`environment = 'prod'`, and one workload. Explain which checks happen offline
and which values are evaluated by ARM.
