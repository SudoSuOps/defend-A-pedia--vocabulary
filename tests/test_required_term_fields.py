"""
test_required_term_fields.py
=============================

For every .md file under docs/vocabulary/ (and docs/examples/) assert the 13
mandatory H2 sections are present. Mirrors scripts/validate_terms.py · the
test suite is the executable spec.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

H2_RE = re.compile(r"^##\s+(.+?)\s*$")

REQUIRED_SECTIONS = [
    "Street Definition",
    "CRE Operator Meaning",
    "DefendableOS Definition",
    "Backend Representation",
    "Client Explanation",
    "Jr Broker Use",
    "Sr Broker Use",
    "Tribunal Use",
    "Evidence Required",
    "Failure Modes",
    "Scoring Impact",
    "Deed / Receipt Impact",
    "Related Terms",
]


def _normalize(s: str) -> str:
    return s.strip().lower().replace(" ", "").replace("/", "")


REQUIRED_NORMALIZED = {_normalize(s) for s in REQUIRED_SECTIONS}


def _collect_h2(text: str) -> set[str]:
    return {_normalize(m.group(1)) for line in text.splitlines() if (m := H2_RE.match(line))}


def test_at_least_one_term_file_exists(term_files: list[Path]) -> None:
    assert term_files, "expected at least one vocabulary term file under docs/vocabulary/ or docs/examples/"


# docs/examples/ holds reference documents (sample_letter_of_understanding.md ·
# sample_deed_receipt.md · sample_deal_digest.md · etc.) that follow other
# document templates · not the 13-section vocabulary term shape. Only files
# starting with `sample_term_` in examples/ are vocabulary-term exemplars.
_VOCAB_TERM_PATHS = sorted(
    (Path(__file__).resolve().parents[1] / "docs" / "vocabulary").rglob("*.md")
)
_EXAMPLE_TERM_PATHS = [
    p for p in sorted((Path(__file__).resolve().parents[1] / "docs" / "examples").rglob("*.md"))
    if p.name.startswith("sample_term_")
]


@pytest.mark.parametrize(
    "term_path",
    [pytest.param(p, id=str(p.name)) for p in (_VOCAB_TERM_PATHS + _EXAMPLE_TERM_PATHS)
     if p.name.lower() not in {"readme.md", "index.md", "term_matrix.md"}],
)
def test_term_file_has_all_required_sections(term_path: Path) -> None:
    text = term_path.read_text(encoding="utf-8")
    present = _collect_h2(text)
    missing = REQUIRED_NORMALIZED - present
    canonical_missing = sorted(s for s in REQUIRED_SECTIONS if _normalize(s) in missing)
    assert not missing, (
        f"{term_path.name} is missing required H2 sections: {canonical_missing}"
    )
