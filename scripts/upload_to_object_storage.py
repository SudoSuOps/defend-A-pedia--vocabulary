#!/usr/bin/env python3
"""
upload_to_object_storage.py
============================

Multi-target sync from the local object-storage/defendable-vocabulary/
tree to operator-controlled storage:

  - NAS    · rsync to /mnt/swarm/defendable-vocabulary/  (Synology DS1525+ · 192.168.0.102)
  - Tigris · S3-compatible · boto3 push to bucket=defendable-vocabulary
  - Local  · default · no-op (already on disk)

v0.3.0 ships this as a SAFE-BY-DEFAULT script that prints what it would do.
Pass --confirm to actually upload.

Usage:
    python3 scripts/upload_to_object_storage.py --target nas    --dry-run
    python3 scripts/upload_to_object_storage.py --target tigris --confirm
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import click

REPO_ROOT = Path(__file__).resolve().parents[1]
OBJ_STORAGE = REPO_ROOT / "object-storage" / "defendable-vocabulary"

NAS_PATH = "/mnt/swarm/defendable-vocabulary/"
TIGRIS_BUCKET = "defendable-vocabulary"


def _nas_push(dry_run: bool) -> int:
    """rsync to the NFS-mounted NAS path · idempotent · safe."""
    if not Path(NAS_PATH).parent.exists():
        click.echo(f"[nas] mount {Path(NAS_PATH).parent} not present · is /mnt/swarm/ NFS-mounted?")
        if not dry_run:
            return 1
    cmd = ["rsync", "-aHv", "--checksum", str(OBJ_STORAGE) + "/", NAS_PATH]
    if dry_run:
        cmd.insert(1, "--dry-run")
    click.echo(f"[nas] running · {' '.join(cmd)}")
    if dry_run:
        click.echo("[nas] dry-run · no actual transfer")
        return 0
    try:
        return subprocess.call(cmd)
    except FileNotFoundError:
        click.echo("[nas] rsync not installed · `apt install rsync` and retry")
        return 1


def _tigris_push(dry_run: bool) -> int:
    """S3-compatible push to Tigris via boto3."""
    try:
        import boto3  # type: ignore[import-not-found]
    except ImportError:
        click.echo("[tigris] boto3 not installed · `pip install boto3` and retry")
        return 1

    endpoint = os.environ.get("AWS_ENDPOINT_URL_S3") or os.environ.get("TIGRIS_ENDPOINT_URL")
    if not endpoint:
        click.echo("[tigris] AWS_ENDPOINT_URL_S3 not set · point at Tigris endpoint and retry")
        return 1

    if dry_run:
        # Just count files we'd upload
        files = list(OBJ_STORAGE.rglob("*"))
        files = [f for f in files if f.is_file()]
        click.echo(f"[tigris] dry-run · would upload {len(files)} objects to bucket {TIGRIS_BUCKET} at {endpoint}")
        return 0

    s3 = boto3.client("s3", endpoint_url=endpoint)
    count = 0
    for path in OBJ_STORAGE.rglob("*"):
        if not path.is_file():
            continue
        key = str(path.relative_to(OBJ_STORAGE))
        s3.upload_file(str(path), TIGRIS_BUCKET, key)
        count += 1
    click.echo(f"[tigris] uploaded {count} objects to s3://{TIGRIS_BUCKET}/")
    return 0


@click.command()
@click.option(
    "--target",
    type=click.Choice(["nas", "tigris", "all"], case_sensitive=False),
    default="nas",
    show_default=True,
)
@click.option("--confirm", is_flag=True, help="Actually upload (default is dry-run)")
@click.option("--dry-run/--no-dry-run", default=True, show_default=True)
def main(target: str, confirm: bool, dry_run: bool) -> None:
    if not OBJ_STORAGE.exists():
        raise click.ClickException("no object storage tree · run mint + manifest first")

    effective_dry = dry_run and not confirm

    target = target.lower()
    rc = 0
    if target in ("nas", "all"):
        rc |= _nas_push(effective_dry)
    if target in ("tigris", "all"):
        rc |= _tigris_push(effective_dry)

    if rc:
        raise SystemExit(rc)


if __name__ == "__main__":
    main()
