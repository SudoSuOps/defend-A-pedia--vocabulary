#!/usr/bin/env python3
"""
validate_terms.py
==================

Validate every vocabulary term .md file under docs/vocabulary/.

Each term file MUST contain all 13 mandatory H2 sections enforced by the
vocabulary_term.schema.json contract. The check is structural: we read the
markdown, scan for '## ' headings, and verify the canonical 13 are present.

Optional YAML frontmatter (between '---' fences at the top of the file) is
parsed if present but not required for the structural pass.

Exit codes:
    0  all term files pass
    1  one or more files failed (details printed)

Usage:
    python scripts/validate_terms.py
    python scripts/validate_terms.py --vocab-dir docs/vocabulary
    python scripts/validate_terms.py --quiet         # only print failures
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable

import click
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VOCAB_DIR = REPO_ROOT / "docs" / "vocabulary"
EXAMPLES_DIR = REPO_ROOT / "docs" / "examples"

# The 13 mandatory H2 sections · matched case-insensitively · "/" tolerated.
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


def _normalize(heading: str) -> str:
    return heading.strip().lower().replace(" ", "").replace("/", "")


REQUIRED_NORMALIZED = {_normalize(s) for s in REQUIRED_SECTIONS}


def _extract_frontmatter(text: str) -> tuple[dict | None, str]:
    """Pull YAML frontmatter if present · returns (data, body)."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None, text
    return data if isinstance(data, dict) else None, text[end + 5 :]


def _collect_h2_headings(body: str) -> list[str]:
    headings: list[str] = []
    for raw in body.splitlines():
        line = raw.rstrip()
        if line.startswith("## ") and not line.startswith("### "):
            headings.append(line[3:].strip())
    return headings


def _iter_term_files(vocab_dir: Path) -> Iterable[Path]:
    for path in sorted(vocab_dir.rglob("*.md")):
        name = path.name.lower()
        if name in {"readme.md", "index.md", "term_matrix.md"}:
            continue
        yield path


def check_term_file(path: Path) -> list[str]:
    """Return a list of error strings · empty list == pass."""
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"unreadable: {exc}"]

    _frontmatter, body = _extract_frontmatter(text)
    headings = _collect_h2_headings(body)
    if not headings:
        errors.append("no H2 sections found")
        return errors

    present = {_normalize(h) for h in headings}
    missing = REQUIRED_NORMALIZED - present
    if missing:
        # Map back to canonical names for the operator-facing message.
        missing_names = sorted(
            s for s in REQUIRED_SECTIONS if _normalize(s) in missing
        )
        errors.append(f"missing required H2 sections: {', '.join(missing_names)}")
    return errors


@click.command()
@click.option(
    "--vocab-dir",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=DEFAULT_VOCAB_DIR,
    show_default=True,
    help="Vocabulary directory to scan",
)
@click.option(
    "--include-examples/--no-include-examples",
    default=False,
    help="Also validate docs/examples/ (sample_term_color.md etc.)",
)
@click.option("--quiet", is_flag=True, help="Only print failures")
def main(vocab_dir: Path, include_examples: bool, quiet: bool) -> None:
    paths: list[Path] = list(_iter_term_files(vocab_dir))
    if include_examples and EXAMPLES_DIR.exists():
        paths.extend(_iter_term_files(EXAMPLES_DIR))

    if not paths:
        click.echo(f"[validate_terms] no term files found under {vocab_dir}")
        # No files means nothing to validate · that's not a failure.
        sys.exit(0)

    failures = 0
    passes = 0
    for path in paths:
        errors = check_term_file(path)
        rel = path.relative_to(REPO_ROOT)
        if errors:
            failures += 1
            click.echo(f"[FAIL] {rel}")
            for err in errors:
                click.echo(f"       · {err}")
        else:
            passes += 1
            if not quiet:
                click.echo(f"[ OK ] {rel}")

    click.echo("")
    click.echo(f"[validate_terms] {passes} passed · {failures} failed · {len(paths)} total")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
