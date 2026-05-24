#!/usr/bin/env python3
"""
build_cross_reference_index.py
===============================

Walk object-storage/defendable-vocabulary/deeds/vocabulary/ · build the 5
canonical cross-reference indexes per spec:

  - indexes/vocabulary_index.json    · master term-by-slug index
  - indexes/backend_field_map.json   · backend field → term
  - indexes/client_dictionary.json   · term → client_explanation
  - indexes/tribunal_term_map.json   · tribunal-relevant terms
  - indexes/repair_term_map.json     · repair/SwarmFixer-relevant terms

Each index is JSON · sorted · deterministic for downstream consumers.

Usage:
    python3 scripts/build_cross_reference_index.py
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import click

REPO_ROOT = Path(__file__).resolve().parents[1]
OBJ_STORAGE = REPO_ROOT / "object-storage" / "defendable-vocabulary"
DEED_DIR = OBJ_STORAGE / "deeds" / "vocabulary"
TERMS_DIR = OBJ_STORAGE / "terms"
INDEX_DIR = OBJ_STORAGE / "indexes"


@click.command()
def main() -> None:
    if not DEED_DIR.exists():
        raise click.ClickException("no deeds found · run mint first")

    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    # Load all deeds + term JSONs
    deeds: list[dict] = []
    for path in sorted(DEED_DIR.glob("DDEED-VOCAB-*.json")):
        deeds.append(json.loads(path.read_text(encoding="utf-8")))

    terms: dict[str, dict] = {}
    for path in sorted(TERMS_DIR.rglob("term.json")):
        rec = json.loads(path.read_text(encoding="utf-8"))
        terms[rec["slug"]] = rec

    # ──────────────────────────────────────────────────────────────
    # 1 · vocabulary_index.json · master index keyed by slug
    # ──────────────────────────────────────────────────────────────
    by_category: dict[str, list[dict]] = defaultdict(list)
    for d in deeds:
        by_category[d["category"]].append({
            "deed_id": d["deed_id"],
            "term": d["term"],
            "slug": d["slug"],
            "record_status": d["record_status"],
            "ens_anchor": d["ens_anchor"],
            "record_hash": d["record_hash"],
        })

    vocab_index = {
        "index_type": "DEFENDABLE_VOCABULARY_INDEX",
        "term_count": len(deeds),
        "category_count": len(by_category),
        "categories": {
            cat: sorted(items, key=lambda x: x["slug"])
            for cat, items in sorted(by_category.items())
        },
    }
    (INDEX_DIR / "vocabulary_index.json").write_text(
        json.dumps(vocab_index, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    # ──────────────────────────────────────────────────────────────
    # 2 · backend_field_map.json · field → term mapping
    # ──────────────────────────────────────────────────────────────
    field_map: list[dict] = []
    for slug, t in terms.items():
        backend_raw = t.get("backend_representation", {}).get("raw_markdown", "")
        # Heuristic · pull any line that looks like a field name (contains . or _)
        for line in backend_raw.split("\n"):
            stripped = line.strip().strip("`'\"")
            if "." in stripped and ":" in stripped and len(stripped) < 200:
                field_map.append({
                    "field_hint": stripped[:120],
                    "term_slug": slug,
                    "term": t["term"],
                    "category": t["category"],
                })
    backend_index = {
        "index_type": "BACKEND_FIELD_MAP",
        "field_count": len(field_map),
        "term_count": len(terms),
        "fields": sorted(field_map, key=lambda x: x["term_slug"]),
    }
    (INDEX_DIR / "backend_field_map.json").write_text(
        json.dumps(backend_index, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    # ──────────────────────────────────────────────────────────────
    # 3 · client_dictionary.json · term → client_explanation
    # ──────────────────────────────────────────────────────────────
    client_dict = {
        "index_type": "CLIENT_DICTIONARY",
        "term_count": len([t for t in terms.values() if t.get("client_explanation")]),
        "entries": sorted([
            {
                "slug": t["slug"],
                "term": t["term"],
                "category": t["category"],
                "client_explanation": t.get("client_explanation", "").strip(),
            }
            for t in terms.values()
            if t.get("client_explanation", "").strip()
        ], key=lambda x: x["slug"]),
    }
    (INDEX_DIR / "client_dictionary.json").write_text(
        json.dumps(client_dict, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    # ──────────────────────────────────────────────────────────────
    # 4 · tribunal_term_map.json · tribunal-relevant terms
    # ──────────────────────────────────────────────────────────────
    tribunal_terms = []
    for slug, t in terms.items():
        if t["category"] == "tribunal_terms" or "tribunal" in t.get("tribunal_use", "").lower():
            tribunal_terms.append({
                "slug": slug,
                "term": t["term"],
                "category": t["category"],
                "tribunal_use": t.get("tribunal_use", "").strip()[:400],
            })
    tribunal_index = {
        "index_type": "TRIBUNAL_TERM_MAP",
        "term_count": len(tribunal_terms),
        "terms": sorted(tribunal_terms, key=lambda x: x["slug"]),
    }
    (INDEX_DIR / "tribunal_term_map.json").write_text(
        json.dumps(tribunal_index, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    # ──────────────────────────────────────────────────────────────
    # 5 · repair_term_map.json · repair/SwarmFixer-relevant terms
    # ──────────────────────────────────────────────────────────────
    repair_terms = []
    for slug, t in terms.items():
        keys = (t.get("defendableos_definition", "") + " " + t.get("tribunal_use", "")).lower()
        if t["category"] == "repair_terms" or any(k in keys for k in ["swarmfixer", "swarmjelly", "repair", "fixer", "jelly"]):
            repair_terms.append({
                "slug": slug,
                "term": t["term"],
                "category": t["category"],
            })
    repair_index = {
        "index_type": "REPAIR_TERM_MAP",
        "term_count": len(repair_terms),
        "terms": sorted(repair_terms, key=lambda x: x["slug"]),
    }
    (INDEX_DIR / "repair_term_map.json").write_text(
        json.dumps(repair_index, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    click.echo(f"[index] vocabulary_index.json   · {vocab_index['term_count']} terms · {vocab_index['category_count']} categories")
    click.echo(f"[index] backend_field_map.json  · {backend_index['field_count']} field hints · {backend_index['term_count']} terms")
    click.echo(f"[index] client_dictionary.json  · {client_dict['term_count']} client-facing entries")
    click.echo(f"[index] tribunal_term_map.json  · {tribunal_index['term_count']} tribunal-relevant terms")
    click.echo(f"[index] repair_term_map.json    · {repair_index['term_count']} repair-relevant terms")


if __name__ == "__main__":
    main()
