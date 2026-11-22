# Bicep for Everyone: companion module library

**[Cloud2BR-MSFTLearningHub/Bicep-For-Everyone](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone)**
is the reference and complementary Azure Bicep learning platform.
Its service-organized modules and projects are the natural next step after
this overview's small language, scope, and foundation exercises.

[Open the learning website](https://cloud2br-msftlearninghub.github.io/Bicep-For-Everyone/){ .md-button .md-button--primary }
[Browse its module catalog](https://cloud2br-msftlearninghub.github.io/Bicep-For-Everyone/catalog.html){ .md-button }

## Different roles, consistent format

| Bicep Overview | Bicep for Everyone |
| --- | --- |
| Focused progressive introduction | Broader learning paths and service modules |
| Small original language/scope examples | Networking, compute, data, identity, monitoring, and other services |
| Understand compiler and deployment boundaries | Reuse/adapt architecture and project building blocks |
| Shared navy/full-width website format | Structural and visual reference |

This overview does not mirror its catalog or claim its deployment/validation
history as our own. Each repository retains its own license and maintenance.

## Explore by area

| Learning need | Reference source |
| --- | --- |
| Groups, VNet/subnets, NSGs, IPs/routes | [Core infrastructure](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/0_core-infrastructure) |
| Storage, SQL, Cosmos, PostgreSQL | [Storage/databases](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/1_storage-databases) |
| VM, VMSS, App Service, Functions, Container Apps, AKS | [Compute/containers](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/2_compute-containers) |
| Private endpoints and DNS | [Networking](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/3_networking) |
| Key Vault, identity, and RBAC | [Identity/security](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/4_identity-security) |
| Event Hubs ingestion | [Analytics](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/5_analytics-bigdata) |
| Logs, diagnostics, Insights, alerts | [Monitoring/management](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/6_monitoring-management) |
| AI Services foundation | [AI/ML](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/8_ai-ml) |
| Recovery Services foundation | [Migration/backup](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/9_migration-backup) |
| Service Bus | [Integration](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/11_integration-services) |
| Hub/spoke, secure web, multi-tier foundations | [Architectures](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/12_architecture-examples) |
| Environment-based composition | [Projects](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone/tree/main/13_projects) |

## Select and adapt responsibly

1. Read the chosen README and **all** source files; record the reviewed commit/version.
2. Check scope, inputs, output sensitivity, API versions, deployment identities,
   required services, regional availability, costs, and cleanup.
3. Decide resource ownership: avoid duplicate declarations of existing groups,
   networks, or storage. Inspect full arrays/properties, not just names.
4. Review private endpoints/DNS/data roles before assuming a private service is usable.
5. Compile with your approved toolchain and inspect warnings.
6. Run authorized validate/what-if with your own inputs and inspect the proposed changes.
7. Deploy only with approval, verify management and runtime/data behavior, and clean up.

The library contains learning building blocks, not universal production
guarantees. Compiling this overview does not validate every external module.
