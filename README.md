# Bicep Overview

Atlanta, USA

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/brown9804)
[brown9804](https://github.com/brown9804)
[![Validation and Pages](https://github.com/brown9804/Bicep-Overview/actions/workflows/validate-and-deploy.yml/badge.svg)](https://github.com/brown9804/Bicep-Overview/actions/workflows/validate-and-deploy.yml)

Last updated: 2026-11-22

A practical introduction to Microsoft Bicep and Azure Infrastructure as Code.
Learn the language, resource scopes, dependencies, reusable modules, and safe
deployment workflow through small original examples before adapting larger
Azure solutions.

[Read the website](https://brown9804.github.io/Bicep-Overview/) |
[Start learning](docs/getting-started.md) |
[Example catalog](docs/catalog.md) |
[Bicep for Everyone](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone)

<details>
<summary><b>Table of contents</b></summary>

- [Learning sequence](#learning-sequence)
- [Companion Bicep library](#companion-bicep-library)
- [Repository structure](#repository-structure)
- [First compilation](#first-compilation)
- [Validation and website](#validation-and-website)
- [Safety and community](#safety-and-community)

</details>

## Learning sequence

| Goal | Read |
| --- | --- |
| Understand IaC, ARM, Bicep, and Terraform | [Fundamentals](docs/fundamentals.md) |
| Install tools and compile a resource group | [Getting started](docs/getting-started.md) |
| Use parameters, decorators, loops, and outputs | [Language](docs/language.md) |
| Understand resource groups and deployment scopes | [Resources/scopes](docs/resources-scopes.md) |
| Compose typed local modules and dependencies | [Modules](docs/modules.md) |
| Validate, preview changes, deploy, and clean up | [Deployment](docs/deployment.md) |
| Build a complete foundation lab | [Project](docs/project.md) |
| Resolve errors and review security/costs | [Troubleshooting](docs/troubleshooting.md), [safety](docs/security-costs.md) |

## Companion Bicep library

**[Cloud2BR-MSFTLearningHub/Bicep-For-Everyone](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone)**
is the complementary, service-organized Bicep learning and module library.
Use this overview for the learning sequence and small examples; use that
repository for broader networking, compute, storage/databases, identity,
monitoring, analytics, AI, integration, and architecture implementations.

[Browse its website](https://cloud2br-msftlearninghub.github.io/Bicep-For-Everyone/) |
[Review its module catalog](https://cloud2br-msftlearninghub.github.io/Bicep-For-Everyone/catalog.html) |
[How to select modules safely](docs/companion-library.md)

The reference shaped this project's documentation and visual format.
The examples here are original teaching implementations, not a mirrored
copy of its catalog. Each repository retains its own license, validation
history, and limitations. Neither is a production certification.

## Repository structure

```text
docs/                           Progressive Markdown lessons and Material styling
examples/01-resource-group/      First subscription-scoped resource
examples/02-language/            Expressions without workload resources
examples/03-modular-foundation/  Composed project with dev/prod parameter files
modules/private-storage/        TLS/Entra/private-only storage foundation
modules/isolated-network/       VNet, subnet, attached deny-inbound NSG
.github/                        Validation, Pages, issues, and pull request template
```

Every entry point has a README explaining inputs, prerequisites, commands,
expected results, cleanup, costs, and limits. Website source views include
canonical files at build time rather than maintaining pasted copies.

## First compilation

Install [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)
and the [Bicep VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-bicep).
From the cloned/downloaded repository root:

```shell
az bicep install
az bicep version
az bicep build --file examples/01-resource-group/main.bicep --stdout
```

Expected: subscription-scoped ARM JSON with one resource-group declaration.
No Azure login or resource creation is involved. Compilation is not a live
validation or deployment test.

## Validation and website

The MkDocs Material site matches
[LaTeX for Everyone](https://brown9804.github.io/LaTeX-For-Everyone/),
[Terraform Overview](https://brown9804.github.io/Terraform-Overview/), and the
companion Bicep platform: full-width navy headers/buttons, light/dark themes,
search, breadcrumbs, responsive navigation, copy-code, architecture diagrams,
and the Cloud2BR organization logo/favicon. No generator footer is displayed.

GitHub Actions installs Bicep, records its version, compiles/lints all five
entry points and both parameter files, tests security/scope contracts in
generated ARM JSON, checks synchronized source views, builds strict MkDocs,
checks local links/assets, and deploys Pages only after successful main
validation. No Azure login, live validation, what-if, or resource deployment
is part of routine CI.

See [maintenance](docs/maintaining.md) for reproduction commands and test limits.

## Safety and community

Most live samples create resources if you choose to run their deployment
commands. Review subscription, scopes, what-if, permissions, policy, costs,
and cleanup before creating anything. The private storage module requires
later endpoints, DNS, and data roles to support clients.

Do not commit credentials, private keys, real subscription identifiers,
sensitive parameters, or deployment/what-if output.
Read [CONTRIBUTING](CONTRIBUTING.md), [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md),
[CHANGELOG](CHANGELOG.md), and [CITATION](CITATION.cff).
The existing [GPL-3.0 license](LICENSE) is preserved; external tools, modules,
documentation, and organization branding retain their own licenses/ownership.
