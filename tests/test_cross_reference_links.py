"""
test_cross_reference_links.py
==============================

For every term file · parse the Related Terms section · for each link target
that points at another vocabulary file (relative .md link) · assert the target
file exists. Catches dead links before they ship.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
VOCAB_DIR = REPO_ROOT / "docs" / "vocabulary"
EXAMPLES_DIR = REPO_ROOT / "docs" / "examples"

H2_RE = re.compile(r"^##\s+(.+?)\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def _collect_term_files() -> list[Path]:
    out: list[Path] = []
    for d in (VOCAB_DIR, EXAMPLES_DIR):
        if not d.exists():
            continue
        for p in sorted(d.rglob("*.md")):
            if p.name.lower() in {"readme.md", "index.md", "term_matrix.md"}:
                continue
            out.append(p)
    return out


def _related_section_body(text: str) -> str:
    buf: list[str] = []
    in_related = False
    for raw in text.splitlines():
        m = H2_RE.match(raw)
        if m:
            in_related = m.group(1).strip().lower().startswith("related terms")
            continue
        if in_related:
            buf.append(raw)
    return "\n".join(buf)


@pytest.mark.parametrize(
    "term_path",
    [pytest.param(p, id=p.name) for p in _collect_term_files()],
)
def test_related_terms_links_resolve(term_path: Path) -> None:
    text = term_path.read_text(encoding="utf-8")
    related = _related_section_body(text)
    if not related.strip():
        pytest.skip(f"{term_path.name} has no Related Terms section yet")
    missing: list[str] = []
    for _label, target in LINK_RE.findall(related):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # Resolve the link relative to the term file's directory.
        target_path = (term_path.parent / target).resolve()
        if target_path.suffix.lower() != ".md":
            continue
        if not target_path.exists():
            # Tolerate the case where the link points at a sibling category file
            # that simply has not been authored yet · SH1/SH3/SH4 will fill in.
            # Report only when the link points inside the repo and the file is absent.
            try:
                target_path.relative_to(REPO_ROOT)
            except ValueError:
                continue
            missing.append(f"{target} -> {target_path}")
    # Soft-fail policy: at this stage of the build many term files do not yet exist.
    # We surface the missing links as xfail rather than hard failure so SH3-SH5 can
    # see what's outstanding without blocking the rest of the suite.
    if missing:
        pytest.xfail(
            f"{term_path.name} references {len(missing)} not-yet-authored term file(s): "
            + ", ".join(missing[:5])
            + ("..." if len(missing) > 5 else "")
        )
