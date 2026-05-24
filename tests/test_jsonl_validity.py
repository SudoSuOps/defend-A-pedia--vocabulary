"""
test_jsonl_validity.py
=======================

For every .jsonl file under data/ · every non-blank line must parse as JSON.
This is the cheap, fast, structural guard that runs before the schema tests.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest


def test_data_dir_exists(data_dir: Path) -> None:
    assert data_dir.exists(), f"data dir missing: {data_dir}"


def test_at_least_one_jsonl_file_present(jsonl_files: list[Path]) -> None:
    assert jsonl_files, "expected at least one seed .jsonl under data/"


@pytest.mark.parametrize(
    "jsonl_path",
    [pytest.param(p, id=p.name) for p in
     sorted((Path(__file__).resolve().parents[1] / "data").rglob("*.jsonl"))],
)
def test_every_line_is_valid_json(jsonl_path: Path) -> None:
    errors: list[str] = []
    for lineno, raw in enumerate(jsonl_path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = raw.strip()
        if not stripped:
            continue
        try:
            json.loads(stripped)
        except json.JSONDecodeError as exc:
            errors.append(f"line {lineno}: {exc.msg} at col {exc.colno}")
    assert not errors, f"{jsonl_path.name} has invalid JSON lines:\n  " + "\n  ".join(errors)
