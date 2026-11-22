# Modules and dependencies

## A typed interface

A Bicep module is a reusable template with parameters, outputs, and deployment
scope. A local relative path resolves from the calling Bicep file, not from
your terminal's working directory.
Use small, meaningful contracts instead of a large collection of unrelated flags.

The foundation is an actual caller:

```bicep title="examples/03-modular-foundation/main.bicep"
--8<-- "examples/03-modular-foundation/main.bicep"
```

The root creates a group and sets `scope: group` on each module.
The group reference establishes the scope/dependency; module output
references let downstream callers consume results without duplicating names.
The caller supplies shared location/tags consistently.

## Included contracts

| Module | Responsibility | Not included |
| --- | --- | --- |
| [Private storage](examples/modules--private-storage.md) | Private-only StorageV2 account | Endpoint, DNS, data roles, containers, backup |
| [Isolated network](examples/modules--isolated-network.md) | VNet/subnet and attached deny-inbound NSG | Workload allows, egress policy, NAT, compute |

Both are resource-group-scoped and independently compilable.
Neither is certified production infrastructure.

## Registry modules

Bicep also supports registry module references. Pin a reviewed version/tag,
record provenance/license, and inspect inputs, outputs, API versions, source,
and permissions. Restoring a registry module may need network/authentication;
local examples here avoid those extra prerequisites.
Do not assume a tag is immutable unless the registry's policy guarantees it.

Consider [Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/)
and the [Bicep for Everyone catalog](companion-library.md) for broader
building blocks with their own maintenance/support policies.

## Scope and ownership review

Give each resource a clear owning template/team. Do not combine two modules
that both redefine the same VNet/subnets with different intended properties.
Review complete arrays and full resource declarations when composing network
templates; "incremental" does not mean every property list is merged safely.
Prefer references to existing shared resources where ownership lies elsewhere.

**Exercise:** add a non-sensitive ownership tag at the foundation root, trace
its propagation to both modules, then compile and inspect the generated templates.
