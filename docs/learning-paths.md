# Learning paths

## Beginner: understand before deploying

1. Read [fundamentals](fundamentals.md) and explain the role of ARM.
2. [Install tools](getting-started.md) and compile the resource group offline.
3. Read [language](language.md), then inspect the resource-free expression example.
4. Learn [scopes](resources-scopes.md) and match each example to its CLI command.
5. Explain why compilation does not authorize or create a cloud resource.

**Outcome:** you can read a small template and identify its inputs, scope,
resources, outputs, and limits. No Azure subscription is needed for these steps.

## Practitioner: compose and review

1. Inspect the private-storage and isolated-network [source views](catalog.md).
2. Read [modules](modules.md) and trace references/dependencies in the root.
3. Compile [dev/prod parameter files](project.md) with an artificial storage name.
4. Review [deployment](deployment.md), [security/costs](security-costs.md),
   and the cleanup procedure before optionally using an approved lab subscription.
5. Compare what-if with your intended changes; verify management and data planes separately.

**Outcome:** you can compose a scoped foundation and explain why it does not
yet provide application runtime or private data access.

## Expand: choose service modules responsibly

Use [Bicep for Everyone](companion-library.md) for more Azure services.
Read the chosen module's source and README, pin your source version,
design resource ownership/scope, and review permissions, dependencies,
API versions, cost, private access, and cleanup.
Do not turn this overview into a second mirrored service catalog.

**Outcome:** you can adapt a module deliberately instead of combining
unrelated templates and hoping the deployment works.
