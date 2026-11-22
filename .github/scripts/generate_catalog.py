"""Synchronize the catalog and source views with canonical example READMEs."""
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = [
    ("examples/01-resource-group", "First resource group", "Beginner", "Subscription"),
    ("examples/02-language", "Expressions without workload resources", "Beginner", "Resource group"),
    ("modules/private-storage", "Private storage module", "Intermediate", "Resource group"),
    ("modules/isolated-network", "Isolated network module", "Intermediate", "Resource group"),
    ("examples/03-modular-foundation", "Modular environment foundation", "Advanced", "Subscription"),
]


def generated_files():
    discovered = {
        path.parent.relative_to(ROOT).as_posix()
        for folder in ("examples", "modules")
        for path in (ROOT / folder).rglob("main.bicep")
    }
    if discovered != {row[0] for row in EXAMPLES}:
        raise ValueError("Every entry point must have exactly one catalog entry.")
    files = {}
    rows = [
        "# Example catalog\n\n",
        "Start with compilation, which needs no login. Live commands in the READMEs "
        "are optional and can create paid resources.\n\n",
        "| Example | Level | Deployment scope |\n| --- | --- | --- |\n",
    ]
    for path, title, level, scope in EXAMPLES:
        if not (ROOT / path / "README.md").is_file():
            raise ValueError(f"Missing example README: {path}")
        slug = path.replace("/", "--")
        rows.append(f"| [{title}](examples/{slug}.md) | {level} | {scope} |\n")
        content = (
            f'--8<-- "{path}/README.md"\n\n## Canonical Bicep source\n\n'
            f'```bicep title="{path}/main.bicep"\n--8<-- "{path}/main.bicep"\n```\n'
        )
        for parameters in sorted((ROOT / path).glob("*.bicepparam")):
            source = parameters.relative_to(ROOT).as_posix()
            content += f'\n## {parameters.stem.title()} parameters\n\n```bicep title="{source}"\n--8<-- "{source}"\n```\n'
        files[Path("docs/examples") / f"{slug}.md"] = content
    files[Path("docs/catalog.md")] = "".join(rows)
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for relative, content in generated_files().items():
        target = ROOT / relative
        if args.check:
            if not target.is_file() or target.read_text(encoding="utf-8") != content:
                stale.append(str(relative))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
    if stale:
        raise SystemExit("Regenerate catalog: " + ", ".join(stale))
    print(f"Synchronized {len(EXAMPLES)} canonical example source views.")
