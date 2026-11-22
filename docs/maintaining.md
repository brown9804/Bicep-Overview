# Maintaining this platform

## Canonical sources

Educational Markdown lives in `docs/`, actual templates in `examples/` and
`modules/`, and each entry point's deployment/cleanup instructions in its README.
The catalog and source-view wrappers are generated from
`.github/scripts/generate_catalog.py`.
MkDocs snippets read the canonical code/README at build time.

```shell
python .github/scripts/generate_catalog.py
python .github/scripts/generate_catalog.py --check
```

Update catalog metadata when adding an example. Do not create a mirrored
service catalog; link Bicep for Everyone for broader modules.

## Reproduce CI checks

Install `requirements.txt` in an isolated Python environment and install
Azure CLI/Bicep first. From the repository root, Bash:

```bash
python -m pip install -r requirements.txt
az bicep install
az bicep version
export BICEP_STORAGE_NAME=stbicepoverviewci
python .github/scripts/validate_bicep.py
python .github/scripts/generate_catalog.py --check
python -m unittest discover -s .github/scripts -p 'test_*.py'
python -m mkdocs build --strict
python .github/scripts/check_site.py
```

The name above is artificial compile-time data, not a globally unique live
deployment input. PowerShell users can set
`$env:BICEP_STORAGE_NAME = 'stbicepoverviewci'` instead.
Compiled JSON goes under ignored `build/`.

## What tests protect

The validator compiles/lints five template entry points and two parameter
files, failing on compiler errors or warnings. It checks generated JSON parses.
Six focused tests protect storage restrictions/TLS, NSG association/default
deny, module group scope/dependency, resource-free language behavior,
dev/prod parameter selection, and one real catalog row per source.

These are offline contracts, not live ARM deployments. They do not certify
quota, regional availability, RBAC, policy, APIs, private DNS/routes,
application readiness, or production security.

## Toolchain and publication

Actions installs the current Bicep CLI and logs its actual version; schema or
linter drift fails validation instead of being hidden. Review compiler/API
changes together with examples/tests and official references.
Python website dependency versions are pinned in `requirements.txt`.

The validation workflow runs on main pushes, pull requests, and manual dispatch.
Only validated main builds deploy to Pages; configure Pages to use GitHub Actions.
No Azure credentials or resource deployment belong in routine CI.
The compiled artifact uses artificial non-sensitive parameters only; do not
upload private parameters, real what-if output, or deployment logs.

## Shared visual format

Preserve full-width navy Material styling, light/dark themes, accessible focus
indicators, search, breadcrumbs, responsive navigation, copy buttons,
Cloud2BR logo/favicon, Atlanta identity, and removed generator footer.
Check desktop and mobile widths without hiding document overflow.
The checker uses `/Bicep-Overview/`; page URLs use `.html`.

## Completion checklist

Require green compiler/tests/strict build/link checks. Verify Pages actually
deployed and inspect the live catalog, search, diagrams, logo, themes, and
narrow-screen layout before claiming publication succeeded.
