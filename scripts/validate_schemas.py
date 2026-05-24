#!/usr/bin/env python3
"""
validate_schemas.py
====================

Load every .schema.json under docs/schemas/ and verify:

    1. The file is valid JSON
    2. The JSON is a valid JSON Schema Draft 2020-12 document
    3. The schema declares a non-empty $id

These three checks guarantee every schema in the repo is loadable by
validate_jsonl.py and any downstream consumer (backend ORMs · LLM
training corpora · external auditors).

Exit codes:
    0  all schemas valid
    1  any schema failed any check

Usage:
    python scripts/validate_schemas.py
    python scripts/validate_schemas.py --schema-dir docs/schemas
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA_DIR = REPO_ROOT / "docs" / "schemas"


def check_schema_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"unreadable: {exc}"]

    try:
        schema = json.loads(text)
    except json.JSONDecodeError as exc:
        return [f"invalid JSON · {exc.msg} at line {exc.lineno} col {exc.colno}"]

    if not isinstance(schema, dict):
        return ["root must be a JSON object"]

    if not schema.get("$id"):
        errors.append("missing or empty $id")

    if not schema.get("$schema"):
        errors.append("missing $schema declaration")
    elif "2020-12" not in str(schema.get("$schema")):
        errors.append(
            f"unexpected $schema · expected JSON Schema 2020-12 · got {schema.get('$schema')}"
        )

    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        loc = ".".join(str(p) for p in exc.absolute_path) or "<root>"
        errors.append(f"not a valid Draft 2020-12 schema at {loc} · {exc.message}")

    return errors


@click.command()
@click.option(
    "--schema-dir",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=DEFAULT_SCHEMA_DIR,
    show_default=True,
)
@click.option("--quiet", is_flag=True, help="Only print failures")
def main(schema_dir: Path, quiet: bool) -> None:
    schemas = sorted(schema_dir.glob("*.schema.json"))
    if not schemas:
        click.echo(f"[validate_schemas] no .schema.json files under {schema_dir}")
        sys.exit(0)

    failures = 0
    for path in schemas:
        rel = path.relative_to(REPO_ROOT)
        errors = check_schema_file(path)
        if errors:
            failures += 1
            click.echo(f"[FAIL] {rel}")
            for err in errors:
                click.echo(f"       · {err}")
        elif not quiet:
            click.echo(f"[ OK ] {rel}")

    click.echo("")
    click.echo(f"[validate_schemas] {len(schemas) - failures}/{len(schemas)} schemas valid")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
