# Contributing

Help make Azure infrastructure learning accurate, practical, and welcoming.
Small corrections, tested examples, diagrams, accessibility fixes, and
reproducible bug reports are welcome.

## Before changing anything

Inspect the current structure, relevant README/source, and tests.
Discuss substantial architecture or scope changes first.
Keep this overview focused on progressive learning; link the
[Bicep for Everyone library](https://github.com/Cloud2BR-MSFTLearningHub/Bicep-For-Everyone)
rather than copying its entire service catalog.

## Good contributions

- Original licensed Markdown and real compilable Bicep.
- Typed, described parameters, appropriate decorators, minimal non-secret outputs.
- Secure defaults and explicit prerequisites, scope, cost, and cleanup.
- Focused tests that fail when the protected behavior changes.
- Updated canonical README and generated source-view/catalog metadata.
- No empty placeholders, credentials, private identifiers, or sensitive artifacts.

## Validate

Compile/lint affected examples, run the compiled-template tests, check generated
documentation, and build MkDocs strictly with internal-link checks.
Commands and test boundaries are in the
[maintenance guide](https://brown9804.github.io/Bicep-Overview/maintaining.html).
Routine CI must not authenticate to Azure or deploy paid resources.

## Pull requests

Explain the learning problem, change, checks actually run, limitations,
and live deployment implications. Provide screenshots for layout changes.
Keep unrelated cleanup separate and never claim unrun tests succeeded.

Contributions use this repository's existing GPL-3.0 license.
Respect external projects' separate licenses and branding ownership.
