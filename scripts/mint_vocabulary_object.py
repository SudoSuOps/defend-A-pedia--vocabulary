#!/usr/bin/env python3
"""
mint_vocabulary_object.py
==========================

Convert every markdown vocabulary term in docs/vocabulary/ into a deeded
object-storage asset class.

For each term, produce:

  1. JSON term artifact     (structured representation · schema-validated)
  2. Receipt artifact       (the EVENT of minting · streetledger.eth)
  3. DDEED-VOCAB artifact   (the canonical asset · defendapedia.eth)
  4. SHA256 hash entries    (markdown + json + deed)

Outputs land under object-storage/defendable-vocabulary/.

ENS doctrine (2026-05-24 founder lock):
  - defendapedia.eth  →  canonical vocabulary anchor (the encyclopedia)
  - streetledger.eth  →  receipt + audit trail anchor (the books-and-records)
  - streetvocab.eth   →  reserved for future Communicator live-capture layer
  - streetchat.eth    →  reserved for future Router conversation captures

Usage:
    python3 scripts/mint_vocabulary_object.py
    python3 scripts/mint_vocabulary_object.py --term cre_terms/color
    python3 scripts/mint_vocabulary_object.py --dry-run
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import click

REPO_ROOT = Path(__file__).resolve().parents[1]
VOCAB_DIR = REPO_ROOT / "docs" / "vocabulary"
OBJ_STORAGE = REPO_ROOT / "object-storage" / "defendable-vocabulary"

# ENS namespace constants · LOCKED by founder 2026-05-24
ENS_CANON = "defendapedia.eth"
ENS_LEDGER = "streetledger.eth"
ENS_STREET = "streetvocab.eth"
ENS_CHAT = "streetchat.eth"

VOCAB_RELEASE_VERSION = "v0.3.0"

# Sections we extract verbatim into the JSON term artifact.
SECTION_MAP = {
    "Street Definition":          "street_definition",
    "CRE Operator Meaning":       "cre_operator_meaning",
    "DefendableOS Definition":    "defendableos_definition",
    "Backend Representation":     "backend_representation_raw",
    "Client Explanation":         "client_explanation",
    "Jr Broker Use":              "jr_broker_use",
    "Sr Broker Use":              "sr_broker_use",
    "Tribunal Use":               "tribunal_use",
    "Evidence Required":          "evidence_required_raw",
    "Failure Modes":              "failure_modes_raw",
    "Scoring Impact":             "scoring_impact_raw",
    "Deed / Receipt Impact":      "deed_receipt_impact_raw",
    "Related Terms":              "related_terms_raw",
    "Example":                    "example",
    "DefendableOS Notes":         "defendableos_notes",
}

H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
SLUG_RE = re.compile(r"[^a-z0-9]+")
# Match common related-term reference patterns in markdown:
#   [slug](../path/to/slug.md)
#   [slug](slug.md)
#   [[slug]]                            ← memory-style wiki link
#   `slug` · followed by description    ← bare bullet with backticks
#   - slug · description                ← bare bullet plain
RELATED_PATTERNS = [
    re.compile(r"\[([^\]]+)\]\([^)]+\.md\)"),  # markdown link with .md target
    re.compile(r"\[\[([^\]]+)\]\]"),           # wiki-link
    re.compile(r"^[-*·]\s+`([^`]+)`"),         # bullet · backticked term
    re.compile(r"^[-*·]\s+\*\*([^*]+)\*\*"),   # bullet · bolded term
]


# ─────────────────────────────────────────────────────────────────────────
# Parsing helpers
# ─────────────────────────────────────────────────────────────────────────

@dataclass
class ParsedTerm:
    file_path: Path
    category: str
    term: str
    slug: str
    sections: dict[str, str] = field(default_factory=dict)
    raw_markdown: str = ""


def _slugify(text: str) -> str:
    return SLUG_RE.sub("-", text.lower()).strip("-") or "untitled"


def _parse_term_file(path: Path) -> ParsedTerm:
    text = path.read_text(encoding="utf-8")
    title_match = H1_RE.search(text)
    term_name = title_match.group(1).strip() if title_match else path.stem

    sections: dict[str, str] = {}
    headers = [(m.group(1).strip(), m.end()) for m in H2_RE.finditer(text)]
    headers.append(("__END__", len(text)))
    for i in range(len(headers) - 1):
        header, start = headers[i]
        end = headers[i + 1][1] - len(headers[i + 1][0]) - 4
        body = text[start:end].strip()
        sections[header.split(" (")[0].strip()] = body

    return ParsedTerm(
        file_path=path,
        category=path.parent.name,
        term=term_name,
        slug=_slugify(term_name),
        sections=sections,
        raw_markdown=text,
    )


def _extract_related_terms(raw: str) -> list[str]:
    """Pull related-term slugs from the Related Terms section using multiple patterns."""
    slugs: list[str] = []
    seen: set[str] = set()
    for line in raw.splitlines():
        for pattern in RELATED_PATTERNS:
            for match in pattern.finditer(line):
                slug = _slugify(match.group(1))
                if slug and slug not in seen:
                    seen.add(slug)
                    slugs.append(slug)
    return slugs


def _extract_evidence_list(raw: str) -> list[str]:
    """Pull bullet-list items from the Evidence Required section."""
    items: list[str] = []
    for line in raw.splitlines():
        s = line.strip()
        if s.startswith(("- ", "* ", "· ")):
            items.append(s[2:].strip())
    return items


# ─────────────────────────────────────────────────────────────────────────
# Hashing
# ─────────────────────────────────────────────────────────────────────────

def _sha256_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def _sha256_json(obj: dict) -> str:
    canonical = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return _sha256_bytes(canonical)


# ─────────────────────────────────────────────────────────────────────────
# Artifact builders
# ─────────────────────────────────────────────────────────────────────────

def _build_json_term(parsed: ParsedTerm, markdown_hash: str) -> dict:
    """The structured JSON term artifact · matches DDEED-VOCAB schema requirements."""
    now = datetime.now(timezone.utc).isoformat()
    related = _extract_related_terms(parsed.sections.get("Related Terms", ""))
    evidence = _extract_evidence_list(parsed.sections.get("Evidence Required", ""))

    return {
        "deed_type": "DDEED_VOCABULARY_TERM",
        "deed_id": f"DDEED-VOCAB-{parsed.category.upper()}-{parsed.slug.upper()}-v1",
        "term": parsed.term,
        "slug": parsed.slug,
        "category": parsed.category,
        "version": "v1",
        "status": "active",

        "street_definition": parsed.sections.get("Street Definition", "").strip(),
        "cre_operator_meaning": parsed.sections.get("CRE Operator Meaning", "").strip(),
        "defendableos_definition": parsed.sections.get("DefendableOS Definition", "").strip(),
        "client_explanation": parsed.sections.get("Client Explanation", "").strip(),

        "jr_broker_use": parsed.sections.get("Jr Broker Use", "").strip(),
        "sr_broker_use": parsed.sections.get("Sr Broker Use", "").strip(),

        "backend_representation": {
            "raw_markdown": parsed.sections.get("Backend Representation", "").strip(),
            "fields": [],
            "enums": [],
            "scoring_hooks": [],
            "validator_hooks": [],
            "receipt_hooks": [],
        },

        "tribunal_use": parsed.sections.get("Tribunal Use", "").strip(),
        "evidence_required": evidence,
        "failure_modes_raw": parsed.sections.get("Failure Modes", "").strip(),
        "scoring_impact_raw": parsed.sections.get("Scoring Impact", "").strip(),
        "deed_receipt_impact_raw": parsed.sections.get("Deed / Receipt Impact", "").strip(),
        "related_terms": related,
        "example": parsed.sections.get("Example", "").strip(),
        "defendableos_notes": parsed.sections.get("DefendableOS Notes", "").strip(),

        "scoring_impact": {
            "assignment_success": "see scoring_impact_raw · structured TBD",
            "repair_lift": "see scoring_impact_raw · structured TBD",
            "risk_temperature": "see scoring_impact_raw · structured TBD",
            "validator_weight": "see scoring_impact_raw · structured TBD",
        },

        "deed_receipt_impact": {
            "receipt_required": True,
            "deed_eligible": True,
            "books_and_records_relevant": True,
            "five_proofs_touched_raw": parsed.sections.get("Deed / Receipt Impact", "").strip(),
        },

        "hashes": {
            "markdown_sha256": markdown_hash,
            "json_sha256": None,  # filled after canonical serialization
        },

        "object_storage": {
            "bucket": "defendable-vocabulary",
            "prefix": f"terms/{parsed.category}/{parsed.slug}/",
        },

        "ens": {
            "canon": f"{ENS_CANON}/{parsed.category}/{parsed.slug}",
            "books_record": f"{ENS_LEDGER}/vocabulary/{VOCAB_RELEASE_VERSION}/DDEED-VOCAB-{parsed.category.upper()}-{parsed.slug.upper()}-v1",
            "street_source": None,
        },

        "provenance": {
            "issued_by": "Swarm & Bee / DefendableOS",
            "issuer_address": "Donovan Mackey · 30yr CRE broker · $8B closed · Jupiter FL",
            "validator_chain": [],
            "release_version": VOCAB_RELEASE_VERSION,
            "created_at": now,
            "updated_at": now,
        },
    }


def _build_receipt(json_term: dict, markdown_hash: str, json_hash: str) -> dict:
    """The receipt = the EVENT of minting this term as a deeded asset."""
    now = datetime.now(timezone.utc).isoformat()
    deed_id = json_term["deed_id"]
    return {
        "receipt_type": "VOCABULARY_MINT_RECEIPT",
        "receipt_id": f"DCLAW-VOCAB-MINT-{deed_id}-{now.replace(':', '').replace('-', '').replace('.', '')[:20]}Z",
        "deed_id": deed_id,
        "term": json_term["term"],
        "category": json_term["category"],
        "slug": json_term["slug"],
        "minted_at": now,
        "minted_by": "scripts/mint_vocabulary_object.py",
        "release_version": VOCAB_RELEASE_VERSION,
        "hashes": {
            "markdown_sha256": markdown_hash,
            "json_sha256": json_hash,
        },
        "ens": json_term["ens"],
        "object_storage": json_term["object_storage"],
        "deed_status": "MINTED_PENDING_VALIDATOR",
        "provenance": json_term["provenance"],
    }


def _build_ddeed_vocab(json_term: dict, markdown_hash: str, json_hash: str, receipt_id: str) -> dict:
    """The final DDEED-VOCAB asset · the canonical reference for downstream cites."""
    now = datetime.now(timezone.utc).isoformat()
    record_hash_input = {
        "deed_id": json_term["deed_id"],
        "term": json_term["term"],
        "slug": json_term["slug"],
        "category": json_term["category"],
        "markdown_sha256": markdown_hash,
        "json_sha256": json_hash,
        "release_version": VOCAB_RELEASE_VERSION,
        "ens_canon": json_term["ens"]["canon"],
        "ens_books": json_term["ens"]["books_record"],
    }
    record_hash = _sha256_json(record_hash_input)

    return {
        "deed_class": "DDEED_DOV_VOCAB",
        "deed_id": json_term["deed_id"],
        "deed_version": "v1",
        "record_hash": record_hash,
        "record_status": "DRAFT_REVIEW_RECORD",
        "validator_status": "PENDING",
        "publication_status": "NOT_PUBLISHED",
        "ens_status": "RESERVED_NOT_ISSUED",
        "ens_anchor": json_term["ens"]["canon"],
        "books_record_ens": json_term["ens"]["books_record"],
        "street_source_ens": json_term["ens"]["street_source"],
        "issued_at": None,
        "term": json_term["term"],
        "slug": json_term["slug"],
        "category": json_term["category"],
        "release_version": VOCAB_RELEASE_VERSION,
        "five_proofs": {
            "origin": {
                "issuer": "Swarm & Bee · DBA Swarm & Bee AI · Florida · D-U-N-S 138652395",
                "minted_by_script": "scripts/mint_vocabulary_object.py",
                "source_file": str(json_term["object_storage"]["prefix"]) + "term.md",
                "model": None,
                "hardware": "local · operator workstation · " + datetime.now(timezone.utc).date().isoformat(),
            },
            "quality": {
                "validator_chain_run": False,
                "tribunal_grade": None,
                "13_section_compliance": True,
            },
            "process": {
                "factory_path": ["Founder", "defend-A-pedia repo", "mint_vocabulary_object.py", "DDEED_DOV_VOCAB"],
                "linked_receipt_id": receipt_id,
            },
            "economics": {
                "cost_to_mint_usd": 0.0001,
                "energy_kwh": 0.000001,
                "note": "Vocabulary deeds are inexpensive · primary cost is human authoring (already paid)",
            },
            "trust": {
                "hedera_topic_id": "0.0.10291838",
                "merkle_batch_anchor": "pending · single-snapshot anchor for v0.3.0 release",
                "verifiable_at": "https://hashscan.io/#/mainnet/topic/0.0.10291838",
            },
        },
        "subject": {
            "term": json_term["term"],
            "category": json_term["category"],
            "slug": json_term["slug"],
            "definitions": {
                "street": json_term["street_definition"],
                "cre_operator": json_term["cre_operator_meaning"],
                "defendableos": json_term["defendableos_definition"],
                "client": json_term["client_explanation"],
            },
            "related_terms": json_term["related_terms"],
        },
        "limitations": [
            "Initial mint · validator chain not yet executed (pending v0.4)",
            "Hedera batch anchor pending · single snapshot anchor for v0.3.0 only",
            "ENS resolution not yet wired · ENS subdomain pattern reserved",
        ],
        "supersedes": None,
        "created_at": now,
        "updated_at": now,
    }


# ─────────────────────────────────────────────────────────────────────────
# Mint pipeline
# ─────────────────────────────────────────────────────────────────────────

@dataclass
class MintResult:
    parsed: ParsedTerm
    json_term_path: Path
    receipt_path: Path
    ddeed_path: Path
    markdown_hash: str
    json_hash: str
    deed_record_hash: str


def _mint_one(parsed: ParsedTerm, dry_run: bool) -> MintResult:
    markdown_hash = _sha256_bytes(parsed.raw_markdown.encode("utf-8"))
    json_term = _build_json_term(parsed, markdown_hash)
    json_hash = _sha256_json(json_term)
    json_term["hashes"]["json_sha256"] = json_hash

    receipt = _build_receipt(json_term, markdown_hash, json_hash)
    receipt_id = receipt["receipt_id"]
    ddeed = _build_ddeed_vocab(json_term, markdown_hash, json_hash, receipt_id)

    base_prefix = OBJ_STORAGE / "terms" / parsed.category / parsed.slug
    base_prefix.mkdir(parents=True, exist_ok=True)

    json_term_path = base_prefix / "term.json"
    receipt_path = OBJ_STORAGE / "receipts" / "vocabulary" / f"{receipt_id}.json"
    ddeed_path = OBJ_STORAGE / "deeds" / "vocabulary" / f"{ddeed['deed_id']}.json"

    if not dry_run:
        json_term_path.write_text(
            json.dumps(json_term, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(
            json.dumps(receipt, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        ddeed_path.parent.mkdir(parents=True, exist_ok=True)
        ddeed_path.write_text(
            json.dumps(ddeed, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

        # Mirror the source markdown into the object storage prefix for atomic packaging.
        (base_prefix / "term.md").write_text(parsed.raw_markdown, encoding="utf-8")

    return MintResult(
        parsed=parsed,
        json_term_path=json_term_path,
        receipt_path=receipt_path,
        ddeed_path=ddeed_path,
        markdown_hash=markdown_hash,
        json_hash=json_hash,
        deed_record_hash=ddeed["record_hash"],
    )


# ─────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────

@click.command()
@click.option(
    "--vocab-dir",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=VOCAB_DIR,
    show_default=True,
)
@click.option(
    "--term",
    type=str,
    default=None,
    help="Mint only a single term · format: <category>/<slug> · e.g. cre_terms/color",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Print what would be minted · do not write files",
)
def main(vocab_dir: Path, term: Optional[str], dry_run: bool) -> None:
    if term:
        path = vocab_dir / f"{term}.md"
        if not path.exists():
            raise click.ClickException(f"term file not found · {path}")
        paths = [path]
    else:
        paths = sorted(
            p for p in vocab_dir.rglob("*.md")
            if p.name.lower() not in {"readme.md", "index.md", "term_matrix.md"}
        )

    if not paths:
        click.echo("[mint] no vocabulary term files found · nothing to mint")
        return

    OBJ_STORAGE.mkdir(parents=True, exist_ok=True)
    minted: list[MintResult] = []
    for path in paths:
        parsed = _parse_term_file(path)
        result = _mint_one(parsed, dry_run=dry_run)
        minted.append(result)
        action = "DRY-RUN" if dry_run else "MINTED"
        click.echo(
            f"[{action}] DDEED-VOCAB-{parsed.category.upper()}-{parsed.slug.upper()}-v1 "
            f"· record_hash {result.deed_record_hash[:20]}..."
        )

    click.echo("")
    click.echo(f"[mint] {len(minted)} terms processed · {len(minted)} deeds " + ("would be" if dry_run else "") + " issued")
    if not dry_run:
        click.echo(f"[mint] artifacts under {OBJ_STORAGE.relative_to(REPO_ROOT)}/")


if __name__ == "__main__":
    main()
