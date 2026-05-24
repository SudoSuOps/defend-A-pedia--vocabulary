"""
test_schema_alignment.py
=========================

Every record in data/vocabulary_terms.jsonl must validate against
docs/schemas/vocabulary_term.schema.json. This is the structural guarantee
that the corpus is training-ready.

Also smoke-tests that every .schema.json in docs/schemas/ is a valid JSON
Schema 2020-12 document.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError, ValidationError

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = REPO_ROOT / "docs" / "schemas"
DATA_DIR = REPO_ROOT / "data"


def _load(schema_filename: str) -> Draft202012Validator:
    schema = json.loads((SCHEMAS_DIR / schema_filename).read_text(encoding="utf-8"))
    return Draft202012Validator(schema)


@pytest.mark.parametrize(
    "schema_path",
    [pytest.param(p, id=p.name) for p in sorted(SCHEMAS_DIR.glob("*.schema.json"))],
)
def test_schema_file_is_valid_draft_2020_12(schema_path: Path) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    assert schema.get("$id"), f"{schema_path.name} is missing $id"
    assert "2020-12" in str(schema.get("$schema", "")), (
        f"{schema_path.name} does not declare JSON Schema 2020-12"
    )
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        pytest.fail(f"{schema_path.name} is not a valid Draft 2020-12 schema: {exc.message}")


def test_vocabulary_terms_records_validate_against_schema() -> None:
    jsonl = DATA_DIR / "vocabulary_terms.jsonl"
    if not jsonl.exists():
        pytest.skip("data/vocabulary_terms.jsonl not present yet")
    validator = _load("vocabulary_term.schema.json")
    errors: list[str] = []
    for lineno, raw in enumerate(jsonl.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = raw.strip()
        if not stripped:
            continue
        record = json.loads(stripped)
        try:
            validator.validate(record)
        except ValidationError as exc:
            loc = ".".join(str(p) for p in exc.absolute_path) or "<root>"
            errors.append(f"line {lineno} at {loc}: {exc.message}")
    assert not errors, "vocabulary_terms.jsonl has schema violations:\n  " + "\n  ".join(errors)


def test_backend_field_map_records_validate_against_schema() -> None:
    jsonl = DATA_DIR / "backend_field_map.jsonl"
    if not jsonl.exists():
        pytest.skip("data/backend_field_map.jsonl not present yet")
    validator = _load("backend_field.schema.json")
    errors: list[str] = []
    for lineno, raw in enumerate(jsonl.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = raw.strip()
        if not stripped:
            continue
        record = json.loads(stripped)
        try:
            validator.validate(record)
        except ValidationError as exc:
            loc = ".".join(str(p) for p in exc.absolute_path) or "<root>"
            errors.append(f"line {lineno} at {loc}: {exc.message}")
    assert not errors, "backend_field_map.jsonl has schema violations:\n  " + "\n  ".join(errors)
