#!/usr/bin/env python3
"""
generate_sha256_manifest.py
============================

Walk object-storage/defendable-vocabulary/ · hash every artifact ·
emit the canonical manifests:

  - manifests/SHA256SUMS.txt              · one line per file · sha256(file)  path
  - manifests/vocabulary_manifest_v1.json · structured per-deed manifest
  - manifests/vocabulary_manifest_latest.json · symlink-equivalent (copy)

The manifests are themselves hashable and can be Merkle-batched for a
single Hedera HCS anchor per release (v0.3.0 strategy locked by founder).

Usage:
    python3 scripts/generate_sha256_manifest.py
    python3 scripts/generate_sha256_manifest.py --release v0.3.0
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import click

REPO_ROOT = Path(__file__).resolve().parents[1]
OBJ_STORAGE = REPO_ROOT / "object-storage" / "defendable-vocabulary"
MANIFEST_DIR = OBJ_STORAGE / "manifests"


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _walk_objects() -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = []
    for path in sorted(OBJ_STORAGE.rglob("*")):
        if not path.is_file():
            continue
        # Skip the manifest dir itself (chicken-and-egg)
        if MANIFEST_DIR in path.parents:
            continue
        rel = path.relative_to(OBJ_STORAGE)
        files.append((rel, _sha256_file(path)))
    return files


def _merkle_root(hashes: list[str]) -> str:
    """Simple binary Merkle root · pairs concatenated · re-hashed until 1 root."""
    if not hashes:
        return ""
    layer = [bytes.fromhex(h) for h in hashes]
    while len(layer) > 1:
        if len(layer) % 2 == 1:
            layer.append(layer[-1])
        nxt = []
        for i in range(0, len(layer), 2):
            nxt.append(hashlib.sha256(layer[i] + layer[i + 1]).digest())
        layer = nxt
    return layer[0].hex()


@click.command()
@click.option(
    "--release",
    type=str,
    default="v0.3.0",
    show_default=True,
)
def main(release: str) -> None:
    if not OBJ_STORAGE.exists():
        raise click.ClickException(
            "object storage tree not found · run scripts/mint_vocabulary_object.py first"
        )

    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)

    files = _walk_objects()
    if not files:
        raise click.ClickException("no files to hash · run mint first")

    # SHA256SUMS.txt · standard shasum format
    sha_lines = [f"{h}  {p}" for p, h in files]
    sha_text = "\n".join(sha_lines) + "\n"
    (MANIFEST_DIR / "SHA256SUMS.txt").write_text(sha_text, encoding="utf-8")

    # Structured manifest
    now = datetime.now(timezone.utc).isoformat()
    merkle = _merkle_root([h for _, h in files])

    manifest = {
        "manifest_type": "DEFENDABLE_VOCABULARY_MANIFEST",
        "release_version": release,
        "generated_at": now,
        "ens_canon": "defendapedia.eth",
        "ens_books_record": "streetledger.eth",
        "file_count": len(files),
        "merkle_root_sha256": merkle,
        "hedera_topic_id": "0.0.10291838",
        "hedera_anchor_status": "PENDING · single-snapshot anchor for this release",
        "files": [
            {"path": str(p), "sha256": h} for p, h in files
        ],
    }

    versioned_path = MANIFEST_DIR / f"vocabulary_manifest_{release}.json"
    latest_path = MANIFEST_DIR / "vocabulary_manifest_latest.json"

    versioned_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    latest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    # Aliases for the v1 alias requested in spec
    if release != "v1":
        v1_alias = MANIFEST_DIR / "vocabulary_manifest_v1.json"
        v1_alias.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    click.echo(f"[manifest] {len(files)} files hashed")
    click.echo(f"[manifest] merkle_root sha256:{merkle}")
    click.echo(f"[manifest] wrote SHA256SUMS.txt · vocabulary_manifest_{release}.json · vocabulary_manifest_latest.json")
    if release != "v1":
        click.echo(f"[manifest] wrote alias vocabulary_manifest_v1.json")


if __name__ == "__main__":
    main()
