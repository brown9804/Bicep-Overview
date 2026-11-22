# Bicep cheat sheet

## Language reminders

| Syntax | Meaning | Caution |
| --- | --- | --- |
| `param name string` | Required typed input | Do not embed secret defaults |
| `@allowed([...])` | Constrain input values | Not a live availability check |
| `@secure()` | Mark sensitive input | Do not output/commit its value |
| `var name = expression` | Named computed value | Not a resource |
| `resource symbol 'type@version'` | Resource declaration | Symbol is not the Azure name |
| `existing` | Reference an existing resource | Does not create or adopt ownership |
| `module symbol './main.bicep'` | Local module | Path is relative to the calling file |
| `scope: group` | Module deployment scope | Match identity and target scope |
| `output name string` | Expose a result | Avoid credentials or private data |
| `[for item in items: ...]` | Array/resource iteration | Review names and concurrency |
| `using './main.bicep'` | Bind a parameter file | Compiler needs the actual template |

## Commands from the repository root

```shell
az bicep install
az bicep version
az bicep build --file examples/01-resource-group/main.bicep --stdout
```

For parameter compilation, first set `BICEP_STORAGE_NAME` explicitly:

```shell
az bicep build-params --file examples/03-modular-foundation/dev.bicepparam --stdout
```

| Scope | Validate | Preview | Deploy |
| --- | --- | --- | --- |
| Resource group | `az deployment group validate` | `az deployment group what-if` | `az deployment group create` |
| Subscription | `az deployment sub validate` | `az deployment sub what-if` | `az deployment sub create` |

These are command families, not complete live commands: supply the correct
group or metadata location, template/parameters, approved identity, and values.
Use the [project](project.md) for a complete reviewed workflow.

## Pre-deployment checklist

Correct subscription/scope? Valid inputs? Unexpected replacements/deletions?
Public access? Identity/data roles? Price review? Private DNS/routes?
Cleanup owner? Compilation alone cannot answer all of these.
