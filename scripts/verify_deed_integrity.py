#!/usr/bin/env python3
"""
verify_deed_integrity.py
=========================

Re-hash every artifact in the object storage tree · compare against the
manifest · report any drift. This is the spot-check operators run when
they need to PROVE the books-and-records haven't been tampered with.

Usage:
    python3 scripts/verify_deed_integrity.py
    python3 scripts/verify_deed_integrity.py --deed DDEED-VOCAB-CRE_TERMS-COLOR-v1
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Optional

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


@click.command()
@click.option("--deed", type=str, default=None, help="Verify only a specific deed")
def main(deed: Optional[str]) -> None:
    latest = MANIFEST_DIR / "vocabulary_manifest_latest.json"
    if not latest.exists():
        raise click.ClickException(
            "no latest manifest · run scripts/generate_sha256_manifest.py first"
        )

    manifest = json.loads(latest.read_text(encoding="utf-8"))
    expected = {entry["path"]: entry["sha256"] for entry in manifest["files"]}

    if deed:
        filter_substr = deed
    else:
        filter_substr = None

    checked = 0
    mismatched: list[tuple[str, str, str]] = []
    missing: list[str] = []

    for rel_path, expected_hash in expected.items():
        if filter_substr and filter_substr not in rel_path:
            continue
        abs_path = OBJ_STORAGE / rel_path
        if not abs_path.exists():
            missing.append(rel_path)
            continue
        actual = _sha256_file(abs_path)
        if actual != expected_hash:
            mismatched.append((rel_path, expected_hash, actual))
        checked += 1

    click.echo(f"[verify] manifest release {manifest['release_version']}")
    click.echo(f"[verify] merkle root sha256:{manifest['merkle_root_sha256']}")
    click.echo(f"[verify] {checked} files checked · {len(missing)} missing · {len(mismatched)} mismatched")

    if missing:
        click.echo("")
        click.echo("MISSING:")
        for p in missing:
            click.echo(f"  · {p}")

    if mismatched:
        click.echo("")
        click.echo("MISMATCHED:")
        for p, exp, act in mismatched:
            click.echo(f"  · {p}")
            click.echo(f"      expected · sha256:{exp}")
            click.echo(f"      actual   · sha256:{act}")

    if missing or mismatched:
        raise SystemExit(1)

    click.echo("")
    click.echo("[verify] integrity confirmed · the books-and-records match the manifest")


if __name__ == "__main__":
    main()
