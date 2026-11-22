# Troubleshooting

| Symptom | Investigate | Safe next step |
| --- | --- | --- |
| `az` missing | Azure CLI install/PATH | Reopen terminal and run `az version` |
| Bicep missing/outdated | CLI-managed Bicep installation | Install/upgrade through Azure CLI; record the version |
| Unknown property/API | Resource reference and compiler types | Check supported API/schema; do not cast errors away |
| Module cannot be found | Relative path/registry reference | Resolve from the calling Bicep file; inspect restore authorization |
| Storage name env variable missing | Parameter compile-time inputs | Set `BICEP_STORAGE_NAME` explicitly |
| Scope mismatch | `targetScope` versus CLI/module scope | Use the correct command family or scoped module |
| Authorization failure | Tenant/subscription and scoped roles | Confirm identity/scope; request only needed permissions |
| Invalid deployment location | Reused subscription deployment name/location | Keep metadata region consistent or use an intentional new name |
| Storage name rejected | Character rules/global uniqueness | Choose your own lowercase alphanumeric 3-24-character name |
| Subnet rejected | CIDR containment/overlap/policies | Review design; string typing cannot prove address correctness |
| Private storage unreachable | Endpoint/DNS/routes/data roles | Verify the missing data-access dependencies |
| Unexpected what-if changes | Name/property changes or unresolved expressions | Stop and inspect source, inputs, ownership, and what-if limits |
| Partial deployment failure | Completed operations and remaining resources | Inspect operations, fix cause, validate/preview again |
| Resource remains after removing code | Incremental lifecycle semantics | Plan deliberate deletion; do not switch blindly to complete mode |
| Website source missing | Generated source views/snippet paths | Regenerate catalog and rebuild strictly |

## Reproduce without exposing data

Report the affected example/page, Azure CLI/Bicep versions, sanitized error,
command, expected result, and whether the check was offline or live.
Do not attach credentials, personal identifiers, real subscription IDs,
private parameters, whole deployment outputs, or environment dumps.

## Compile versus live failures

Offline structural tests cannot prove permissions, policy, quota,
regional availability, API execution, DNS, or runtime behavior.
For live issues use an approved isolated environment; inspect deployment
operations and actual resource state before retrying or deleting anything.
