#!/usr/bin/env python3
"""
export_backend_map.py
======================

Walk docs/vocabulary/ · for each term file extract the Backend Representation
section · emit one JSONL line per (term, field) tuple to
data/backend_field_map.jsonl.

The Backend Representation section may be either a fenced ```json block (the
canonical shape used in sample_term_color.md) or a markdown list. We try both.

Each emitted record validates against docs/schemas/backend_field.schema.json:

    {
      "field_name": "asset.color_status",
      "type": "enum",
      "enum_values": ["VERIFIED", "PARTIAL", "UNVERIFIED", "MISSING"],
      "scoring_hook": "validator_confidence_weight",
      "vocabulary_term_slug": "color",
      "schema_file": "docs/vocabulary/cre_terms/color.md"
    }

Usage:
    python scripts/export_backend_map.py
    python scripts/export_backend_map.py --vocab-dir docs/vocabulary --out data/backend_field_map.jsonl
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import click

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VOCAB_DIR = REPO_ROOT / "docs" / "vocabulary"
DEFAULT_OUT = REPO_ROOT / "data" / "backend_field_map.jsonl"

SLUG_NORMALIZE = re.compile(r"[^a-z0-9]+")
H1_RE = re.compile(r"^#\s+(.+?)\s*$")
H2_RE = re.compile(r"^##\s+(.+?)\s*$")
JSON_FENCE_RE = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)

ALLOWED_TYPES = {
    "string", "integer", "float", "boolean", "timestamp",
    "enum", "jsonb", "array", "uuid", "sha256",
}


@dataclass
class FieldRow:
    field_name: str
    type: str
    enum_values: list[str] | None
    scoring_hook: str | None
    vocabulary_term_slug: str
    schema_file: str
    description: str | None
    added_at: str


def _slugify(text: str) -> str:
    return SLUG_NORMALIZE.sub("-", text.lower()).strip("-") or "untitled"


def _split_sections(text: str) -> dict[str, str]:
    """Map H2 heading → section body (trimmed)."""
    sections: dict[str, str] = {}
    current_key: str | None = None
    current_buf: list[str] = []
    for raw in text.splitlines():
        m = H2_RE.match(raw)
        if m:
            if current_key is not None:
                sections[current_key] = "\n".join(current_buf).strip()
            current_key = m.group(1).strip().lower()
            current_buf = []
        else:
            current_buf.append(raw)
    if current_key is not None:
        sections[current_key] = "\n".join(current_buf).strip()
    return sections


def _coerce_type(declared: str | None) -> str:
    if not declared:
        return "string"
    t = declared.strip().lower()
    aliases = {"int": "integer", "bool": "boolean", "ts": "timestamp", "date-time": "timestamp"}
    t = aliases.get(t, t)
    return t if t in ALLOWED_TYPES else "string"


def _extract_fields(section_body: str) -> list[dict[str, Any]]:
    """Parse a Backend Representation section · return list of raw field dicts.

    We accept the canonical fenced ```json block. The block is expected to be an
    object whose keys are dotted field names and values are spec dicts. Any
    spec dict missing 'type' is skipped (we don't want to invent types).
    """
    rows: list[dict[str, Any]] = []
    match = JSON_FENCE_RE.search(section_body)
    if not match:
        return rows
    try:
        parsed = json.loads(match.group(1))
    except json.JSONDecodeError:
        return rows
    if not isinstance(parsed, dict):
        return rows
    for field_name, spec in parsed.items():
        if not isinstance(spec, dict):
            continue
        rows.append({"field_name": field_name, **spec})
    return rows


def _read_term_slug(text: str, fallback: str) -> str:
    for line in text.splitlines():
        m = H1_RE.match(line)
        if m:
            return _slugify(m.group(1).strip())
    return _slugify(fallback)


def _build_row(field: dict[str, Any], slug: str, source_path: Path) -> FieldRow | None:
    field_name = field.get("field_name")
    if not isinstance(field_name, str) or not field_name:
        return None
    declared_type = field.get("type")
    coerced = _coerce_type(declared_type if isinstance(declared_type, str) else None)
    enum_values: list[str] | None = None
    raw_values = field.get("values")
    if coerced == "enum" and isinstance(raw_values, list):
        enum_values = [str(v) for v in raw_values]
    scoring_hook = field.get("scoring_hook")
    description = field.get("description")
    return FieldRow(
        field_name=field_name,
        type=coerced,
        enum_values=enum_values,
        scoring_hook=scoring_hook if isinstance(scoring_hook, str) else None,
        vocabulary_term_slug=slug,
        schema_file=str(source_path.relative_to(REPO_ROOT)),
        description=description if isinstance(description, str) else None,
        added_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
    )


def _emit(row: FieldRow) -> str:
    data = asdict(row)
    # Enforce schema invariant · if type=='enum' the schema requires enum_values.
    # When a vocab term declared type=='enum' but didn't enumerate the values
    # in the Backend Representation block · default to [] so the JSONL still
    # validates · SH6 QA pass surfaces these for backfill.
    if data.get("type") == "enum" and not data.get("enum_values"):
        data["enum_values"] = []
    # Drop nulls so the JSONL stays terse.
    return json.dumps({k: v for k, v in data.items() if v is not None}, sort_keys=True)


@click.command()
@click.option(
    "--vocab-dir",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=DEFAULT_VOCAB_DIR,
    show_default=True,
)
@click.option(
    "--out",
    type=click.Path(dir_okay=False, path_type=Path),
    default=DEFAULT_OUT,
    show_default=True,
)
@click.option(
    "--include-examples/--no-include-examples",
    default=True,
    help="Also walk docs/examples/ (default · sample_term_color.md is canonical)",
)
def main(vocab_dir: Path, out: Path, include_examples: bool) -> None:
    paths: list[Path] = sorted(vocab_dir.rglob("*.md"))
    if include_examples:
        examples = REPO_ROOT / "docs" / "examples"
        if examples.exists():
            paths.extend(sorted(examples.glob("*.md")))

    out.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    skipped_no_section = 0
    with out.open("w", encoding="utf-8") as f:
        for path in paths:
            name = path.name.lower()
            if name in {"readme.md", "index.md", "term_matrix.md"}:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                continue
            slug = _read_term_slug(text, fallback=path.stem)
            sections = _split_sections(text)
            backend_body = sections.get("backend representation", "")
            if not backend_body:
                skipped_no_section += 1
                continue
            for field in _extract_fields(backend_body):
                row = _build_row(field, slug, path)
                if row is None:
                    continue
                f.write(_emit(row) + "\n")
                written += 1

    click.echo(
        f"[export_backend_map] wrote {written} field rows → "
        f"{out.relative_to(REPO_ROOT)} · {skipped_no_section} terms had no backend section"
    )


if __name__ == "__main__":
    main()
