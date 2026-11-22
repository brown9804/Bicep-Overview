# Security and cost review

## Before creating resources

- Confirm tenant/subscription, scope, resource ownership, and cleanup owner.
- Review deployment identity and least-privilege management/data permissions.
- Inspect public access, key authentication, TLS, ingress, egress, and diagnostics.
- Check regional availability, policies, quotas, SKUs, and dependencies.
- Estimate costs with the [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/).
- Set approved budgets/alerts and a time-bounded cleanup plan.

A resource group/VNet/NSG has no direct compute charge, but storage use and
later network/workload services may incur charges. Budget alerts notify;
they are not universal spending caps.

## Secrets and identity

Never hardcode credentials, private keys, real environment identifiers, or
sensitive deployment parameters. Use secure parameters and approved Key Vault
references where appropriate; prefer managed identity or federation for
workload/automation access. Do not return secrets in outputs.

Our parameter files read a **non-secret storage name** from an environment
variable at compile time. That mechanism does not make parameter files or
compiled artifacts suitable secret stores.
Protect real logs, what-if output, deployment records, and local parameters.

## Private does not mean usable or complete

The storage module disables public networking, public blobs, and shared keys.
Data clients need private endpoints, DNS resolution, network access, and scoped
Entra data roles. A management-plane deployment can succeed while the service
remains intentionally inaccessible to clients.

The network denies inbound through its attached NSG, but does not implement
complete egress isolation. Review workload allow rules and outbound controls
before deploying an application.

## Supply chain

Review/pin module sources and APIs, inspect changes, and use trusted tool
installation paths. Registry module restore can need separate authorization.
Do not give privileged deployment credentials to untrusted pull-request code.
Routine CI here only compiles local modules and publishes documentation.

## Cleanup matters

Inspect the entire target group before deletion. Respect locks, retained
data, backups, policies, and shared dependencies. Confirm actual removal and
review lingering costs. Deleting deployment history or local compiled JSON
does not delete deployed infrastructure.
