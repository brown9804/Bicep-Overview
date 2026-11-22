# Getting started

## Install and verify

Install [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli),
[VS Code](https://code.visualstudio.com/), and the
[Bicep extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-bicep).
The editor provides completion, resource types, diagnostics, and navigation.
Azure CLI's managed Bicep installation is separate from the editor.

```shell
az version
az bicep install
az bicep version
```

Compilation requires no login. Use the supported current CLI; this project's
workflow records the Bicep version it actually tested.

Download the repository ZIP or clone it:

```shell
git clone https://github.com/brown9804/Bicep-Overview.git
cd Bicep-Overview
```

## Inspect the first source

```bicep title="examples/01-resource-group/main.bicep"
--8<-- "examples/01-resource-group/main.bicep"
```

`targetScope` makes this a subscription deployment. Parameters describe caller
choices; decorators provide documentation and bounds. The resource declaration
specifies a type/API version, and outputs expose results.
The symbolic name `group` is a code reference, not the Azure resource name.

## Compile offline

```shell
az bicep build --file examples/01-resource-group/main.bicep --stdout
```

Expected: ARM JSON with a subscription deployment schema, parameter definitions,
one resource-group resource, and outputs. No resource has been created.
Without `--stdout`/`--outfile`, build writes a JSON file beside the source;
CI writes generated output under ignored `build/`.

## Next step

First read [fundamentals](fundamentals.md) and [language](language.md).
For optional live use, the [resource-group example](examples/examples--01-resource-group.md)
includes validation, what-if, creation, verification, and cleanup.
It requires explicit Azure authorization and may fail due to policies/permissions
that compilation cannot evaluate.

**Exercise:** change the group-name default and compile again. Identify the
changed parameter default in JSON, and explain why this has not renamed a real group.
