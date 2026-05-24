#!/usr/bin/env python3
"""
validate_jsonl.py
==================

Validate every .jsonl file under data/ · two passes per file:

    1. Every line is well-formed JSON
    2. Every line validates against the schema registered for that file

Schema registration table is below. Files not in the table get JSON-only
validation (a warning is printed so we know to register them when they grow up).

Exit codes:
    0  every line of every registered file validated cleanly
    1  any line failed JSON parse OR schema validation

Usage:
    python scripts/validate_jsonl.py
    python scripts/validate_jsonl.py --data-dir data
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import click
from jsonschema import Draft202012Validator, ValidationError

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DIR = REPO_ROOT / "data"
SCHEMA_DIR = REPO_ROOT / "docs" / "schemas"

# Maps data/<filename> → schema file under docs/schemas/.
# SH3-SH5 will extend this as new corpora land.
SCHEMA_FILES: dict[str, str] = {
    "vocabulary_terms.jsonl": "vocabulary_term.schema.json",
    "backend_field_map.jsonl": "backend_field.schema.json",
    "tribunal_verdicts.jsonl": "tribunal_verdict.schema.json",
    "deed_receipts.jsonl": "deed_receipt.schema.json",
    "evidence_records.jsonl": "evidence_record.schema.json",
    "risk_flags.jsonl": "risk_flag.schema.json",
    "repair_lifts.jsonl": "repair_lift.schema.json",
    "engagements.jsonl": "engagement.schema.json",
    "deal_stages.jsonl": "deal_stage.schema.json",
    "probability_of_close.jsonl": "probability_of_close.schema.json",
    "assignment_success.jsonl": "assignment_success.schema.json",
    "cost_to_mint.jsonl": "cost_to_mint.schema.json",
    "honey_jelly_propolis.jsonl": "honey_jelly_propolis.schema.json",
    "validator_chains.jsonl": "validator_chain.schema.json",
    # No schema yet · JSON-only:
    # "cre_to_defendableos_map.jsonl"
    # "scoring_dials.jsonl"
    # "client_language_map.jsonl"
}


def _load_validator(schema_filename: str) -> Draft202012Validator:
    schema_path = SCHEMA_DIR / schema_filename
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    return Draft202012Validator(schema)


def _validate_file(
    path: Path, validator: Draft202012Validator | None
) -> tuple[int, int, list[str]]:
    """Return (pass_count, fail_count, errors)."""
    passes = 0
    failures = 0
    errors: list[str] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return 0, 1, [f"unreadable: {exc}"]

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if not stripped:
            continue
        try:
            record: Any = json.loads(stripped)
        except json.JSONDecodeError as exc:
            failures += 1
            errors.append(f"line {lineno}: invalid JSON · {exc.msg} at col {exc.colno}")
            continue
        if validator is None:
            passes += 1
            continue
        try:
            validator.validate(record)
        except ValidationError as exc:
            failures += 1
            loc = ".".join(str(p) for p in exc.absolute_path) or "<root>"
            errors.append(f"line {lineno}: schema violation at {loc} · {exc.message}")
        else:
            passes += 1
    return passes, failures, errors


@click.command()
@click.option(
    "--data-dir",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=DEFAULT_DATA_DIR,
    show_default=True,
)
@click.option("--quiet", is_flag=True, help="Only print failures")
def main(data_dir: Path, quiet: bool) -> None:
    jsonl_files = sorted(data_dir.rglob("*.jsonl"))
    if not jsonl_files:
        click.echo(f"[validate_jsonl] no .jsonl files under {data_dir}")
        sys.exit(0)

    total_pass = 0
    total_fail = 0
    file_failures = 0

    for jpath in jsonl_files:
        rel = jpath.relative_to(REPO_ROOT)
        schema_filename = SCHEMA_FILES.get(jpath.name)
        validator: Draft202012Validator | None = None
        if schema_filename:
            try:
                validator = _load_validator(schema_filename)
            except (OSError, json.JSONDecodeError) as exc:
                click.echo(f"[FAIL] {rel} · could not load schema {schema_filename}: {exc}")
                file_failures += 1
                total_fail += 1
                continue
        else:
            if not quiet:
                click.echo(f"[WARN] {rel} · no schema registered · JSON-only validation")

        passes, failures, errors = _validate_file(jpath, validator)
        total_pass += passes
        total_fail += failures

        if failures:
            file_failures += 1
            click.echo(f"[FAIL] {rel} · {passes} ok · {failures} bad")
            for err in errors:
                click.echo(f"       · {err}")
        elif not quiet:
            label = "schema-validated" if validator else "json-only"
            click.echo(f"[ OK ] {rel} · {passes} records ({label})")

    click.echo("")
    click.echo(
        f"[validate_jsonl] {total_pass} records ok · {total_fail} bad · "
        f"{file_failures} files failed · {len(jsonl_files)} files scanned"
    )
    sys.exit(1 if total_fail else 0)


if __name__ == "__main__":
    main()
