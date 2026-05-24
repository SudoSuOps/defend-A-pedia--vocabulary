"""Shared pytest fixtures and path constants for the Defend-A-Pedia test suite."""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
VOCAB_DIR = REPO_ROOT / "docs" / "vocabulary"
SCHEMAS_DIR = REPO_ROOT / "docs" / "schemas"
DATA_DIR = REPO_ROOT / "data"
EXAMPLES_DIR = REPO_ROOT / "docs" / "examples"


def _iter_term_files(*dirs: Path) -> list[Path]:
    out: list[Path] = []
    for d in dirs:
        if not d.exists():
            continue
        for path in sorted(d.rglob("*.md")):
            if path.name.lower() in {"readme.md", "index.md", "term_matrix.md"}:
                continue
            out.append(path)
    return out


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def vocab_dir() -> Path:
    return VOCAB_DIR


@pytest.fixture(scope="session")
def schemas_dir() -> Path:
    return SCHEMAS_DIR


@pytest.fixture(scope="session")
def data_dir() -> Path:
    return DATA_DIR


@pytest.fixture(scope="session")
def term_files() -> list[Path]:
    """All vocabulary term files (vocab + examples)."""
    return _iter_term_files(VOCAB_DIR, EXAMPLES_DIR)


@pytest.fixture(scope="session")
def jsonl_files() -> list[Path]:
    return sorted(DATA_DIR.rglob("*.jsonl")) if DATA_DIR.exists() else []
