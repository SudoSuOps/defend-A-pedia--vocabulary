#!/usr/bin/env python3
"""Cost-to-Mint calculator for Pain in the Shed signature segment.

Generates the standardized 8-line readout that closes every Pain in the Shed
episode. Outputs both the formatted text (for reading aloud and publishing on
episode pages) and the structured JSON (for the cumulative ledger at
painintheshed.com/cost-to-mint).

Baselines pulled from SwarmOS operator-platform doctrine:
  - Electricity (US avg):    $0.10 / kWh
  - RTX 6000 power draw:     300W = 0.3 kWh / hour
  - RTX 6000 depreciation:   ~$0.005 / deed at 90 verdicts/min throughput
  - Hedera HCS message:      $0.0001 / message
  - Validator pass cost:     ~$0.0001 / pass on owned GPU (Qwen-9B equivalent)

Default hyperscaler comparison: AWS p4d.24xlarge ($32.77/hr) extrapolated per task
Default human-only comparison:  Senior analyst ($200/hr) extrapolated per task

Usage:
    python3 cost_to_mint.py --episode 1 --slug false-honey \\
        --compute-hours 2.5 --compute-rate 0.80 \\
        --review-min 90 --review-rate 200 \\
        --validator-passes 3 --storage-gb 12 --energy-kwh 0.75 \\
        --retries 1 --repair-count 0

Or from a YAML config:
    python3 cost_to_mint.py --config episode-001.yaml

License: MIT (Swarm and Bee LLC)
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path


# Default baselines from SwarmOS operator-platform doctrine
DEFAULT_ELECTRICITY_USD_PER_KWH = 0.10
DEFAULT_STORAGE_USD_PER_GB_MONTH = 0.023  # Tigris / S3-equivalent
DEFAULT_VALIDATOR_USD_PER_PASS = 0.0001
DEFAULT_HEDERA_USD_PER_MSG = 0.0001
DEFAULT_RETRY_AVG_USD = 0.05  # average compute+energy hit per retry

# Comparison baselines
DEFAULT_HYPERSCALER_USD_PER_HOUR = 32.77  # AWS p4d.24xlarge
DEFAULT_HUMAN_ONLY_USD_PER_HOUR = 200.00  # Senior analyst rate


@dataclass
class CostToMint:
    """Standardized Cost-to-Mint readout · the 8-line + comparison segment."""

    # Episode metadata
    episode_num: int
    slug: str
    topic: str = ""
    run_scope: str = ""

    # The 8-line readout (USD)
    compute_usd: float = 0.0
    human_review_usd: float = 0.0
    validator_usd: float = 0.0
    storage_usd: float = 0.0
    energy_usd: float = 0.0
    retries_usd: float = 0.0
    repair_usd: float = 0.0
    deed_issuance_usd: float = 0.0

    # Comparisons (USD)
    hyperscaler_equivalent_usd: float = 0.0
    human_only_equivalent_usd: float = 0.0

    # Computed at finalize()
    total_usd: float = 0.0
    hyperscaler_savings_multiple: float = 0.0
    human_only_savings_multiple: float = 0.0
    minted_at: str = ""

    def finalize(self) -> CostToMint:
        """Compute total + savings multiples + timestamp."""
        self.total_usd = round(
            self.compute_usd
            + self.human_review_usd
            + self.validator_usd
            + self.storage_usd
            + self.energy_usd
            + self.retries_usd
            + self.repair_usd
            + self.deed_issuance_usd,
            6,
        )

        if self.total_usd > 0:
            self.hyperscaler_savings_multiple = round(
                self.hyperscaler_equivalent_usd / self.total_usd, 2
            )
            self.human_only_savings_multiple = round(
                self.human_only_equivalent_usd / self.total_usd, 2
            )

        self.minted_at = datetime.now(timezone.utc).isoformat()
        return self

    def to_dict(self) -> dict:
        return asdict(self)

    def to_readout_text(self) -> str:
        """Render the standardized text readout for episode + ledger pages."""
        ep_label = f"Episode {self.episode_num}"
        if self.slug:
            ep_label += f" · {self.slug}"

        lines = []
        lines.append("═" * 60)
        lines.append(f"COST TO MINT · {ep_label}")
        lines.append("═" * 60)
        if self.topic:
            lines.append(f"Topic:            {self.topic}")
        if self.run_scope:
            lines.append(f"Run scope:        {self.run_scope}")
        lines.append("")
        lines.append(f"Compute           ${self.compute_usd:>10.4f}")
        lines.append(f"Human review      ${self.human_review_usd:>10.4f}")
        lines.append(f"Validator pass    ${self.validator_usd:>10.4f}")
        lines.append(f"Storage           ${self.storage_usd:>10.4f}")
        lines.append(f"Energy            ${self.energy_usd:>10.4f}")
        lines.append(f"Retries           ${self.retries_usd:>10.4f}")
        lines.append(f"Repair            ${self.repair_usd:>10.4f}")
        lines.append(f"Deed issuance     ${self.deed_issuance_usd:>10.4f}")
        lines.append("─" * 60)
        lines.append(f"Total             ${self.total_usd:>10.4f}  per minted artifact")
        lines.append("")
        lines.append("Comparison")
        lines.append(
            f"  Hyperscaler equivalent   ${self.hyperscaler_equivalent_usd:>10.4f}"
            f"  ({self.hyperscaler_savings_multiple}× ours)"
        )
        lines.append(
            f"  Human-only equivalent    ${self.human_only_equivalent_usd:>10.4f}"
            f"  ({self.human_only_savings_multiple}× ours)"
        )
        lines.append("═" * 60)
        return "\n".join(lines)


def compute_cost_to_mint(
    *,
    episode_num: int,
    slug: str,
    topic: str = "",
    run_scope: str = "",
    # Compute inputs
    compute_hours: float = 0.0,
    compute_rate_usd_per_hour: float = 0.80,  # owned RTX 6000 amortized
    # Human review inputs
    review_minutes: float = 0.0,
    review_rate_usd_per_hour: float = 200.0,
    # Validator inputs
    validator_passes: int = 0,
    validator_rate_usd_per_pass: float = DEFAULT_VALIDATOR_USD_PER_PASS,
    # Storage inputs
    storage_gb: float = 0.0,
    storage_rate_usd_per_gb_month: float = DEFAULT_STORAGE_USD_PER_GB_MONTH,
    storage_months: float = 1.0,
    # Energy inputs (kWh consumed for this artifact)
    energy_kwh: float = 0.0,
    electricity_rate_usd_per_kwh: float = DEFAULT_ELECTRICITY_USD_PER_KWH,
    # Retries
    retries: int = 0,
    retry_avg_usd: float = DEFAULT_RETRY_AVG_USD,
    # Repair (SwarmFixer interventions)
    repair_count: int = 0,
    repair_avg_usd: float = 0.02,
    # Deed issuance
    deed_messages: int = 1,
    deed_rate_usd_per_msg: float = DEFAULT_HEDERA_USD_PER_MSG,
    # Comparison inputs
    hyperscaler_rate_usd_per_hour: float = DEFAULT_HYPERSCALER_USD_PER_HOUR,
    human_only_hours: float | None = None,
    human_only_rate_usd_per_hour: float = DEFAULT_HUMAN_ONLY_USD_PER_HOUR,
) -> CostToMint:
    """Compute the Cost-to-Mint readout from operator-grade inputs."""

    ctm = CostToMint(
        episode_num=episode_num,
        slug=slug,
        topic=topic,
        run_scope=run_scope,
    )

    ctm.compute_usd = round(compute_hours * compute_rate_usd_per_hour, 6)
    ctm.human_review_usd = round((review_minutes / 60.0) * review_rate_usd_per_hour, 6)
    ctm.validator_usd = round(validator_passes * validator_rate_usd_per_pass, 6)
    ctm.storage_usd = round(storage_gb * storage_rate_usd_per_gb_month * storage_months, 6)
    ctm.energy_usd = round(energy_kwh * electricity_rate_usd_per_kwh, 6)
    ctm.retries_usd = round(retries * retry_avg_usd, 6)
    ctm.repair_usd = round(repair_count * repair_avg_usd, 6)
    ctm.deed_issuance_usd = round(deed_messages * deed_rate_usd_per_msg, 6)

    # Hyperscaler comparison · compute_hours equivalent on AWS-tier GPU
    ctm.hyperscaler_equivalent_usd = round(
        compute_hours * hyperscaler_rate_usd_per_hour, 6
    )

    # Human-only comparison · use explicit hours if provided, else use review_minutes
    if human_only_hours is None:
        human_only_hours = review_minutes / 60.0
    ctm.human_only_equivalent_usd = round(
        human_only_hours * human_only_rate_usd_per_hour, 6
    )

    return ctm.finalize()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--episode", type=int, required=True, help="Episode number")
    p.add_argument("--slug", required=True, help="URL slug (e.g., false-honey)")
    p.add_argument("--topic", default="", help="Lane / topic description")
    p.add_argument("--run-scope", default="", help="Specific artifact / run being measured")

    p.add_argument("--compute-hours", type=float, default=0.0)
    p.add_argument("--compute-rate", type=float, default=0.80, help="USD/hour (default: owned RTX 6000 amortized)")

    p.add_argument("--review-min", type=float, default=0.0)
    p.add_argument("--review-rate", type=float, default=200.0, help="USD/hour")

    p.add_argument("--validator-passes", type=int, default=0)
    p.add_argument("--validator-rate", type=float, default=DEFAULT_VALIDATOR_USD_PER_PASS)

    p.add_argument("--storage-gb", type=float, default=0.0)
    p.add_argument("--storage-rate", type=float, default=DEFAULT_STORAGE_USD_PER_GB_MONTH, help="USD/GB/month")
    p.add_argument("--storage-months", type=float, default=1.0)

    p.add_argument("--energy-kwh", type=float, default=0.0)
    p.add_argument("--electricity-rate", type=float, default=DEFAULT_ELECTRICITY_USD_PER_KWH)

    p.add_argument("--retries", type=int, default=0)
    p.add_argument("--retry-avg", type=float, default=DEFAULT_RETRY_AVG_USD)

    p.add_argument("--repair-count", type=int, default=0)
    p.add_argument("--repair-avg", type=float, default=0.02)

    p.add_argument("--deed-messages", type=int, default=1, help="Hedera HCS messages anchored")

    p.add_argument("--hyperscaler-rate", type=float, default=DEFAULT_HYPERSCALER_USD_PER_HOUR,
                   help="Hyperscaler USD/hour for comparison")
    p.add_argument("--human-only-hours", type=float, default=None,
                   help="Human-only hours (default: same as review-min)")
    p.add_argument("--human-rate", type=float, default=DEFAULT_HUMAN_ONLY_USD_PER_HOUR)

    p.add_argument("--out-json", type=Path, default=None, help="Write JSON output to file")
    p.add_argument("--json-only", action="store_true", help="Output JSON only, no readout text")

    return p.parse_args()


def main() -> int:
    args = parse_args()

    ctm = compute_cost_to_mint(
        episode_num=args.episode,
        slug=args.slug,
        topic=args.topic,
        run_scope=args.run_scope,
        compute_hours=args.compute_hours,
        compute_rate_usd_per_hour=args.compute_rate,
        review_minutes=args.review_min,
        review_rate_usd_per_hour=args.review_rate,
        validator_passes=args.validator_passes,
        validator_rate_usd_per_pass=args.validator_rate,
        storage_gb=args.storage_gb,
        storage_rate_usd_per_gb_month=args.storage_rate,
        storage_months=args.storage_months,
        energy_kwh=args.energy_kwh,
        electricity_rate_usd_per_kwh=args.electricity_rate,
        retries=args.retries,
        retry_avg_usd=args.retry_avg,
        repair_count=args.repair_count,
        repair_avg_usd=args.repair_avg,
        deed_messages=args.deed_messages,
        deed_rate_usd_per_msg=DEFAULT_HEDERA_USD_PER_MSG,
        hyperscaler_rate_usd_per_hour=args.hyperscaler_rate,
        human_only_hours=args.human_only_hours,
        human_only_rate_usd_per_hour=args.human_rate,
    )

    if args.json_only:
        print(json.dumps(ctm.to_dict(), indent=2))
    else:
        print(ctm.to_readout_text())
        print()
        print("# JSON for cumulative ledger:")
        print(json.dumps(ctm.to_dict(), indent=2))

    if args.out_json:
        args.out_json.write_text(json.dumps(ctm.to_dict(), indent=2))
        print(f"\n# wrote: {args.out_json}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
