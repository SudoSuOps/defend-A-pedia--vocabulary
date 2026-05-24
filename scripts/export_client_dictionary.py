#!/usr/bin/env python3
"""
export_client_dictionary.py
============================

Walk docs/vocabulary/ · for each term file extract the Client Explanation and
Related Terms sections · emit one JSONL line per term to
data/client_language_map.jsonl.

This is the dictionary sales · marketing · and client-success use when
translating operator/CRE language into boardroom English. NO engineer jargon
leaks · NO backend field names · only what the principal will read.

Record shape:
    {
      "term": "Color",
      "slug": "color",
      "category": "cre_terms",
      "client_explanation": "...",
      "related_terms": ["digest", "probability-of-close", ...]
    }

Usage:
    python scripts/export_client_dictionary.py
    python scripts/export_client_dictionary.py --out data/client_language_map.jsonl
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import click

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VOCAB_DIR = REPO_ROOT / "docs" / "vocabulary"
DEFAULT_OUT = REPO_ROOT / "data" / "client_language_map.jsonl"

H1_RE = re.compile(r"^#\s+(.+?)\s*$")
H2_RE = re.compile(r"^##\s+(.+?)\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
SLUG_NORMALIZE = re.compile(r"[^a-z0-9]+")


def _slugify(text: str) -> str:
    return SLUG_NORMALIZE.sub("-", text.lower()).strip("-") or "untitled"


def _split_sections(text: str) -> tuple[str, dict[str, str]]:
    """Return (h1_title, {h2_heading_lower: body})."""
    title = ""
    sections: dict[str, str] = {}
    current_key: str | None = None
    current_buf: list[str] = []
    for raw in text.splitlines():
        if not title:
            m1 = H1_RE.match(raw)
            if m1:
                title = m1.group(1).strip()
                continue
        m2 = H2_RE.match(raw)
        if m2:
            if current_key is not None:
                sections[current_key] = "\n".join(current_buf).strip()
            current_key = m2.group(1).strip().lower()
            current_buf = []
        else:
            current_buf.append(raw)
    if current_key is not None:
        sections[current_key] = "\n".join(current_buf).strip()
    return title, sections


def _extract_related(body: str) -> list[str]:
    """Pull every markdown link target's basename (without .md) from the section."""
    slugs: list[str] = []
    seen: set[str] = set()
    for line in body.splitlines():
        for label, target in LINK_RE.findall(line):
            base = Path(target).stem
            slug = _slugify(base) if base else _slugify(label)
            if slug and slug not in seen:
                seen.add(slug)
                slugs.append(slug)
        # If the line is a bullet with no link, try the leading token as a slug.
        stripped = line.strip().lstrip("-*+ ").strip()
        if stripped and not LINK_RE.search(line):
            token = stripped.split("·")[0].split("·")[0].split(":")[0].strip("` ")
            if token and " " not in token and token.lower() == token:
                slug = _slugify(token)
                if slug and slug not in seen:
                    seen.add(slug)
                    slugs.append(slug)
    return slugs


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
)
def main(vocab_dir: Path, out: Path, include_examples: bool) -> None:
    paths: list[Path] = sorted(vocab_dir.rglob("*.md"))
    if include_examples:
        examples = REPO_ROOT / "docs" / "examples"
        if examples.exists():
            paths.extend(sorted(examples.glob("*.md")))

    out.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    skipped = 0
    with out.open("w", encoding="utf-8") as f:
        for path in paths:
            name = path.name.lower()
            if name in {"readme.md", "index.md", "term_matrix.md"}:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                continue
            title, sections = _split_sections(text)
            client_body = sections.get("client explanation", "")
            if not client_body:
                skipped += 1
                continue
            related = _extract_related(sections.get("related terms", ""))
            slug = _slugify(title) if title else _slugify(path.stem)
            category = (
                path.relative_to(vocab_dir).parts[0]
                if path.parent != vocab_dir and vocab_dir in path.parents
                else "example"
            )
            record = {
                "term": title or path.stem,
                "slug": slug,
                "category": category,
                "client_explanation": client_body,
                "related_terms": related,
                "source": str(path.relative_to(REPO_ROOT)),
            }
            f.write(json.dumps(record, sort_keys=True) + "\n")
            written += 1

    click.echo(
        f"[export_client_dictionary] wrote {written} entries → "
        f"{out.relative_to(REPO_ROOT)} · {skipped} terms had no Client Explanation"
    )


if __name__ == "__main__":
    main()
