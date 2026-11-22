"""Compile every learning entry point without Azure authentication or deployment."""
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def main():
    sources = sorted(
        path for folder in ("examples", "modules")
        for path in (ROOT / folder).rglob("*")
        if path.suffix in (".bicep", ".bicepparam")
    )
    if not sources:
        raise SystemExit("No Bicep sources found.")
    for source in sources:
        relative = source.relative_to(ROOT)
        output = ROOT / "build" / relative.with_suffix(".json")
        output.parent.mkdir(parents=True, exist_ok=True)
        command = "build-params" if source.suffix == ".bicepparam" else "build"
        result = subprocess.run(
            ["az", "bicep", command, "--file", str(source), "--outfile", str(output)],
            cwd=ROOT, text=True, capture_output=True, timeout=180,
        )
        print(f"{command}: {relative}", flush=True)
        if result.stdout:
            print(result.stdout, flush=True)
        if result.stderr:
            print(result.stderr, flush=True)
        if result.returncode or "warning" in result.stderr.lower():
            raise SystemExit(f"Compilation/lint failed: {relative}")
        document = json.loads(output.read_text(encoding="utf-8"))
        if "$schema" not in document:
            raise SystemExit(f"Missing compiled ARM schema: {relative}")
    print(f"Compiled and linted {len(sources)} Bicep and parameter files; no Azure deployment performed.")


if __name__ == "__main__":
    main()
