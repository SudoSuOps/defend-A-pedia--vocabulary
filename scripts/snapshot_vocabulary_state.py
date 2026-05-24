#!/usr/bin/env python3
"""
snapshot_vocabulary_state.py
=============================

Capture the current vocabulary state into a dated snapshot directory.
Snapshots live under object-storage/defendable-vocabulary/snapshots/{daily,weekly,monthly}/
and are immutable · the books-and-records that anchor a point in time.

Each snapshot is a compressed tarball plus its own manifest + Merkle root.

Usage:
    python3 scripts/snapshot_vocabulary_state.py --cadence daily
    python3 scripts/snapshot_vocabulary_state.py --cadence weekly
    python3 scripts/snapshot_vocabulary_state.py --cadence monthly
"""

from __future__ import annotations

import hashlib
import json
import tarfile
from datetime import datetime, timezone
from pathlib import Path

import click

REPO_ROOT = Path(__file__).resolve().parents[1]
OBJ_STORAGE = REPO_ROOT / "object-storage" / "defendable-vocabulary"
SNAP_ROOT = OBJ_STORAGE / "snapshots"


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


@click.command()
@click.option(
    "--cadence",
    type=click.Choice(["daily", "weekly", "monthly"], case_sensitive=False),
    default="daily",
    show_default=True,
)
@click.option("--tag", type=str, default=None, help="Optional snapshot tag (e.g. release version)")
def main(cadence: str, tag: str) -> None:
    if not OBJ_STORAGE.exists():
        raise click.ClickException("no object storage tree · run mint first")

    cadence = cadence.lower()
    snap_dir = SNAP_ROOT / cadence
    snap_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    tag_part = f"-{tag}" if tag else ""
    snapshot_name = f"vocabulary-snapshot-{cadence}-{stamp}{tag_part}"

    archive_path = snap_dir / f"{snapshot_name}.tar.gz"
    manifest_path = snap_dir / f"{snapshot_name}.manifest.json"

    # Archive everything EXCEPT existing snapshots (avoid recursion)
    excluded_dir = SNAP_ROOT
    with tarfile.open(archive_path, "w:gz") as tar:
        for path in sorted(OBJ_STORAGE.rglob("*")):
            if not path.is_file():
                continue
            # Don't include the snapshots tree (chicken and egg)
            if excluded_dir in path.parents:
                continue
            arcname = path.relative_to(OBJ_STORAGE)
            tar.add(path, arcname=str(arcname))

    archive_sha = _sha256_file(archive_path)
    archive_size = archive_path.stat().st_size

    snap_manifest = {
        "snapshot_type": "DEFENDABLE_VOCABULARY_SNAPSHOT",
        "cadence": cadence,
        "snapshot_name": snapshot_name,
        "captured_at": now.isoformat(),
        "tag": tag,
        "archive_filename": archive_path.name,
        "archive_size_bytes": archive_size,
        "archive_sha256": archive_sha,
        "source_root": str(OBJ_STORAGE.relative_to(REPO_ROOT)),
        "ens_books_record": f"streetledger.eth/vocabulary/snapshots/{cadence}/{snapshot_name}",
        "hedera_anchor_status": "PENDING · single archive hash · ready for next batch",
    }

    manifest_path.write_text(
        json.dumps(snap_manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    click.echo(f"[snapshot] cadence={cadence} · captured at {now.isoformat()}")
    click.echo(f"[snapshot] archive · {archive_path.relative_to(REPO_ROOT)} ({archive_size} bytes)")
    click.echo(f"[snapshot] archive_sha256 · {archive_sha}")
    click.echo(f"[snapshot] manifest · {manifest_path.relative_to(REPO_ROOT)}")
    click.echo(f"[snapshot] ENS · {snap_manifest['ens_books_record']}")


if __name__ == "__main__":
    main()
