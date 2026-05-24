# Energy

> *"Energy is the line item. Electricity. GPU time. Human review. If you can't price it · you can't sell it. If you can't measure it · you can't manage it. The math layer is non-optional."*
> — Founder · on the day cost-to-mint became a customer-facing dial

## Street Definition

"What's the energy on that cook?" Energy is the real-world operational cost of producing AI intelligence · the electricity the rigs metabolize · the GPU-hours the cooks burn · the human-review time the sr brokers spend · the back-office cost of running the books-and-records. It is the math layer that turns AI from a vibes-economy into an actual unit economic with a cost · a margin · a return. Without an energy line item · you can't write an OM · can't price the deed · can't prove the Hive pencils.

In CRE language · energy is the operating expense column on the rent roll · the property tax · the insurance · the management fee · the CAM reconciliation · the things that pencil the NOI. A broker who doesn't know the OpEx doesn't know the deal. A Hive that doesn't measure its energy doesn't know its books.

## CRE Operator Meaning

In CRE · energy is the building's actual operating cost · expressed per square foot · benchmarked against comps · disclosed in the OM · reconciled at year-end in the CAM. A broker quotes a 6-cap on a $50M industrial facility and the buyer asks "what's the OpEx" because the OpEx is what proves the NOI is real. If OpEx ratio is double the market · the building has a real problem and the cap rate is wrong. Same way in the Hive · if the cost-to-mint is double the benchmark · the cook has a real problem and the deed price is wrong.

The CRE-trained founder treats energy as the FIRST honesty test. Show me the OpEx. Show me the energy. Show me the math. Then we'll talk about the cap rate.

## DefendableOS Definition

Energy is the metabolic cost of producing intelligence inside the Hive · the aggregate of:

- **Electrical energy** · the watts the rigs draw (swarmrails ~1000W peak · whale ~400W peak · zima-edge ~15W · signal-edge ~10W) measured at the wall via per-rig PDUs and rolled up to per-cook · per-pair · per-deed costs
- **Compute energy** · the GPU-seconds spent per pair (9B Worker Bees ~3-5 GPU-sec · 27B Worker Bees ~10-15 GPU-sec · Auditor Bees ~1-2 GPU-sec · Katniss invocations ~5 GPU-sec each)
- **Human energy** · the operator-minutes spent on override review · adversarial-event escalation · weekly check sessions · pattern audit · doctrine maintenance
- **Anchor energy** · the Hedera HCS posting cost (~$0.0008 per cell certificate · ~$0.0001 per batch Merkle root) · the ENS reservation cost (one-time per deed)
- **Storage energy** · the cumulative cost of holding receipts on Tigris · NAS · PostgreSQL · ENS over the deed's lifetime

Energy aggregates into the **cost-to-mint** dial (the per-deed dollar cost) and the **margin** dial (the per-deed economic surplus over cost). Both are surfaced to customers in the Morning Brief and the Closing Statement.

## Backend Representation

```json
{
  "energy.electrical_watt_hours": { "type": "float" },
  "energy.gpu_seconds": { "type": "float" },
  "energy.operator_minutes": { "type": "float" },
  "energy.anchor_cost_usd": { "type": "float" },
  "energy.storage_cost_usd": { "type": "float" },
  "energy.total_cost_usd": {
    "type": "float",
    "scoring_hook": "cost_to_mint_v1"
  },
  "energy.per_rig_breakdown": {
    "type": "object",
    "additionalProperties": { "type": "float" }
  }
}
```

Schema files: `docs/schemas/cost_to_mint.schema.json` · `docs/schemas/energy_ledger.schema.json`

## Client Explanation

"Energy" is the math layer · the actual operating cost of every deed and every pair we produce. We measure it · we publish it · we price against it. Every deed in your Closing Statement includes the energy line · how much electricity · how much GPU time · how much operator time went into producing it. That's not industry standard · most AI vendors hide their unit economics behind "monthly subscription" pricing. We show the math because the math is the proof we can sustain the service · the proof your deed is real inventory · the proof we are a defendable economic entity · not a venture-funded loss-leader.

## Jr Broker Use

The jr broker treats energy as a TRANSPARENCY DIAL:

1. Every engagement has a real-time cost-to-mint readout in the dashboard · know what your engagement is costing while it's in flight
2. If a cook crosses 2x the per-pair energy benchmark without producing Royal Jelly · escalate · the cook is wasting energy
3. When a customer asks "what does this cost you" · the answer is the energy ledger · pull the numbers · be transparent
4. Don't promise energy-free repairs · every Jelly-to-Honey repair has a SwarmFixer compute cost · which is logged · which is real
5. Don't run shadow cooks · personal experiments · undocumented batches · they consume Hive energy without producing Hive deeds · they are wage theft against the books

**Rule of thumb**: energy is on the books · what you cook costs · what costs is logged · what is logged is accountable.

## Sr Broker Use

The sr broker watches energy as the OPERATING-MARGIN GAUGE:

- The Hive's per-rig energy efficiency is a daily metric · trending down means the cook discipline is slipping
- The Royal Jelly cost-to-mint should hold steady around 1.3-1.5x the Honey cost-to-mint · ratios outside that range mean the apex tier is either too cheap (corner-cutting) or too expensive (over-engineering)
- The Propolis cost-to-mint is the COST OF QUALITY DISCIPLINE · we publish it · we own it · it should be 5-15% of total cook energy
- The human-review minutes per deed should trend DOWN over time · this is the SwarmFixer flywheel paying off · the next cohort catches earlier · the operator spends less
- When energy spikes without throughput gain · the cook is misconfigured · the most common cause is temp drift (must be 0.05 · not 0.7)
- The weekly check reviews per-rig energy efficiency and identifies underperforming nodes for re-tuning OR re-deployment

## Tribunal Use

```yaml
tribunal_use:
  classification_impact: []   # energy is not a tier · it is the cost of producing the tiers
  rule_layer_checks:
    - energy.total_cost_usd MUST be logged for every pair (no untracked compute)
    - energy.per_rig_breakdown MUST sum to total (accounting integrity)
    - energy.anchor_cost_usd MUST be logged when tier == ROYAL_JELLY (the cell certificate carries its own cost)
  judge_layer_prompt_hint: "energy is not a judgment input · the judge does not grade energy · the auditor logs it"
  can_be_critical_failure: false   # energy is an economic metric · not a quality verdict
```

Energy is not adjudicated by the Tribunal · but the Tribunal's verdict records carry the energy line · because every defendable claim includes its cost.

## Evidence Required

To make an energy claim:

- A per-rig PDU reading (watts at the wall) for every active cook period
- A per-Bee GPU-second log (from the vLLM telemetry layer)
- An operator-minute log (from the dashboard activity log)
- Anchor and storage cost line items (from Hedera HCS and Tigris billing APIs)
- A reconciled total (per-rig + Bee + operator + anchor + storage) for every deed

Without these · the cost-to-mint is unverifiable and the deed's economic claim is theater.

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **untracked_compute** | A cook ran on a rig without logging GPU-seconds | The cook's deeds are held · the rig is audited · the missing logs are reconstructed from PDU readings if possible |
| **energy_spike_no_lift** | Cook energy 3x benchmark with no Royal Jelly produced | The cook is throttled · the config is audited · the most common cause is temp drift |
| **anchor_cost_drift** | Hedera per-cell cost climbs > 25% above benchmark | Investigate · usually a Hedera-network fee shift · update the per-deed pricing if sustained |
| **operator_overcount** | Operator-review time logged that exceeds actual operator activity | Operator-discipline event · the log is reconciled against dashboard activity · gap investigated |
| **shadow_cook** | Compute consumed without a corresponding cook record | Operator-discipline event · the rig is locked · all unattributed deeds are held |

## Scoring Impact

- **assignment_success**: ENABLER · energy affordability is a precondition for any assignment to be commercially viable
- **repair_lift**: TRADE-OFF · repair adds energy · the lift must justify the additional cost · SwarmFixer is measured on energy-per-lift-point
- **validator_confidence**: NEUTRAL · validator confidence is independent of energy cost (we don't grade cheaper outputs more leniently)
- **risk_temperature**: NEUTRAL at the pair level · ELEVATED at the system level (high-energy cook means high burn rate · which is a business risk)
- **probability_of_close**: ENABLER · the per-deed margin must be positive for the engagement model to sustain
- **evidence_strength**: NEUTRAL · evidence weight is independent of how much energy produced the evidence
- **cost_to_mint**: DIRECT · energy IS the cost-to-mint numerator · this is the primary dial

## Deed / Receipt Impact

- **Receipt fields touched**: `energy.total_cost_usd` · `energy.per_rig_breakdown` · `energy.gpu_seconds` · `energy.operator_minutes` · `energy.anchor_cost_usd`
- **DDEED class impact**: Every DDEED carries an energy line · for customer transparency · for operator accountability · for sustainability claims
- **Books and records layer**: ALL 5 (L1 PG hot · L2 Merkle hashed · L3 NAS archived · L4 Hedera HCS receipted · L5 ENS resolution paid)
- **5 Proofs touched**: ECONOMICS (energy IS the economics proof) · PROCESS (energy lineage IS the process · what tried what failed what survived)

## Related Terms

- [cost-to-mint](cost-to-mint.md) · the dollar dial that aggregates energy into a per-deed price
- [hive](hive.md) · the entity that consumes energy and produces deeds
- [swarm](swarm.md) · the active network that metabolizes energy in real time
- [bee](bee.md) · the worker whose per-instance energy is logged
- [honey](honey.md) · the volume output the energy buys
- [royal-jelly](royal-jelly.md) · the apex output that costs ~1.3-1.5x Honey energy

## Example

> **Engagement**: Daily CRE morning digest · 14 industrial listings · standard scope.
>
> **Energy ledger for the engagement**:
>
> - Scout Bee · whale · SwarmCurator-2B · 14 source scans · GPU-sec 4.2 · electrical 0.0011 kWh
> - Worker Bee · swarmrails GPU 0 · SwarmCurator-9B · digest cook · GPU-sec 11.8 · electrical 0.0033 kWh
> - Auditor Bee · swarmrails GPU 1 · gemma3:12b Scale A · GPU-sec 2.1 · electrical 0.0006 kWh
> - Auditor Bee · swarmrails GPU 0 · qwen2.5:32b Scale B · GPU-sec 4.6 · electrical 0.0019 kWh
> - Operator review · 3 minutes (override queue) · ~0.05 operator-cost units
> - Bakery hash + Tigris write · 0.001 USD
> - Hedera batch anchor (shared across 50-pair batch) · this pair's share 0.0000016 USD
> - **Total cost-to-mint: 0.0058 USD** · 11% above the $0.0052 baseline · within tolerance · cook reported healthy
>
> **Customer disclosure (Closing Statement line)**: "This Honey deed cost 0.0058 USD to produce. Lineage: 4 Bees · 22.7 GPU-seconds · 0.0069 kWh · 3 operator-minutes. Hedera batch anchor 0.0000016 USD."
>
> **Why the customer sees this**: because it's the math · because the math is the trust · because the trust is the brand.

## DefendableOS Notes

- Energy is the brand's anti-fantasy mechanism · we publish the cost · we don't hide unit economics behind subscription fog
- The $0.0052/deed Honey baseline is the operator-tested number from production · variance up to 20% is healthy · sustained variance above 30% is a cook problem
- The energy ledger is what makes the Hive a defendable business · not just a defendable technology · the CFO can audit it · the auditor can sign off · the investor can model the unit economics
- Sustainability claims are made FROM the energy ledger · not adjacent to it · we don't say "green AI" · we say "$0.0058 of electrical input produced this deed · here's the kWh · here's the rig"
- The math layer is what separates Defendable from every AI vendor selling intelligence at a loss to capture growth · we don't run a loss-leader · we run a defendable economic entity

🐝 *Energy is the line item. Measure it. Publish it. Price against it. The math layer is what makes the Hive a defendable business · not just a defendable technology.*
