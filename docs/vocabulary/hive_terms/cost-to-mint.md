# Cost to Mint

> *"Cost to mint is the per-deed all-in. Electricity. Compute. Operator review. Anchor fees. Storage carry. You roll it up · you publish it · you price against it. That's the math layer. Without it · you're selling vibes."*
> — Founder · the day the $0.0052 baseline got locked

## Street Definition

"What's the cost to mint?" The cost-to-mint is the all-in per-deed dollar number · the unit economic that converts a Hive deed into a defendable line item on the books. It rolls up electricity + GPU-seconds + operator minutes + Hedera anchor fees + storage carry · per deed · published in the Closing Statement · auditable against the energy ledger.

The baseline is $0.0052/deed for a standard Honey deed. The four-tier fee schedule (Floor $0.008 · Standard $0.02 · Full $0.05 · Enterprise $0.10) is what we CHARGE customers · the difference between charge and cost is the margin · which is what makes the Hive a sustainable business · not a venture-funded loss leader.

In CRE language · cost-to-mint is the operating-cost-per-unit · the per-SF OpEx on an industrial facility · the per-key cost on a hospitality asset · the number that pencils whether the building cash-flows after debt service. Without it · the cap rate is theater.

## CRE Operator Meaning

In CRE · cost-to-mint maps to the per-unit operating cost · disclosed in the OM · reconciled at year-end in the CAM. A sr broker quoting a 6-cap on a cold-storage facility includes the OpEx per cubic foot · the energy cost (cold storage is energy-heavy · OpEx ratio runs 35-45% of revenue) · the labor cost · the maintenance reserve. The buyer's underwriter takes the disclosed cost-to-mint · stress-tests it against comps · and either confirms the NOI or re-trades the price.

Same here. Cost-to-mint is what makes the customer's underwriter able to model the engagement. Without it · the deed has no economic anchor.

## DefendableOS Definition

Cost-to-mint is the per-deed all-in dollar cost · computed as:

```
cost_to_mint_usd =
    electrical_energy_kwh * grid_price_per_kwh
  + gpu_seconds * gpu_amortized_dollar_per_second
  + operator_minutes * operator_dollar_per_minute
  + anchor_cost_usd            # Hedera HCS per-cell for RJ · per-batch for others
  + storage_carry_usd          # amortized Tigris + NAS + PostgreSQL + ENS
  + chain_overhead_usd         # Merkle assembly · validator chain compute · audit logging
```

The Honey-baseline `$0.0052/deed` is the operator-tested production number on the swarmrails primary rig with:

- grid price $0.085/kWh (Florida commercial rate · 2026)
- GPU amortized $0.0011/sec (RTX PRO 6000 96GB · 3-year amortization at 75% duty cycle)
- operator labor $1.20/min (sr broker rate amortized across review queue)
- Hedera HCS batch share $0.0000016/pair (50-pair batch · ~$0.0001 batch root)
- Tigris + NAS + PG amortized $0.0008/deed-year
- chain overhead $0.0011/deed (Merkle + validator chain compute)

Royal Jelly deeds add ~$0.0008 per-cell Hedera certificate · so RJ runs ~1.3-1.5x Honey baseline (~$0.007-0.008).

## The 4 fee tiers

The cost-to-mint is the COST. The fee tiers are what we CHARGE. The spread between cost and fee is the margin · the engineering · the brand · the warranty · the books-and-records discipline.

| Tier | Fee per deed | Use case | Margin over cost |
|---|---|---|---|
| **Floor** | $0.008 | High-volume internal cooks · scout-grade outputs · ML pipeline back-fill | ~$0.003 (60% over Honey baseline) |
| **Standard** | $0.02 | Standard customer engagements · routine production deeds · the volume tier of customer revenue | ~$0.015 (300% over baseline) |
| **Full** | $0.05 | Full-service engagement · Royal Jelly deeds · regulated-industry compliance · the bread-and-butter for STNL-style relationships | ~$0.045 (~600% over baseline · includes operator high-touch) |
| **Enterprise** | $0.10 | Enterprise engagement · audit-grade · KPMG-deliverable equivalent · custom doctrine extensions · dedicated sr broker | ~$0.092 (~1700% over baseline · includes white-glove SLAs · custom anchors · dedicated rigs) |

The fee tier IS NOT a quality tier. Quality is determined by the Tribunal verdict (Royal Jelly · Honey · Jelly · Propolis). Fee tier is determined by ENGAGEMENT TYPE (volume · standard · full-service · enterprise). A Floor-tier engagement can produce Royal Jelly outputs · an Enterprise-tier engagement can produce Honey outputs · the verdict and the fee are orthogonal axes.

## Backend Representation

```json
{
  "cost_to_mint.usd": { "type": "float" },
  "cost_to_mint.baseline_honey_usd": { "type": "float", "default": 0.0052 },
  "cost_to_mint.fee_tier": {
    "type": "enum",
    "values": ["FLOOR", "STANDARD", "FULL", "ENTERPRISE"]
  },
  "cost_to_mint.fee_charged_usd": { "type": "float" },
  "cost_to_mint.margin_usd": { "type": "float" },
  "cost_to_mint.breakdown": {
    "type": "object",
    "properties": {
      "electrical_usd": { "type": "float" },
      "gpu_usd": { "type": "float" },
      "operator_usd": { "type": "float" },
      "anchor_usd": { "type": "float" },
      "storage_usd": { "type": "float" },
      "chain_overhead_usd": { "type": "float" }
    }
  }
}
```

Schema files: `docs/schemas/cost_to_mint.schema.json` · `docs/schemas/fee_tier.schema.json` · `docs/schemas/energy_ledger.schema.json`

## Client Explanation

"Cost to mint" is the per-deed dollar cost of producing your deed · we publish it on every Closing Statement so you can see the math. The baseline is $0.0052 per Honey deed at our current rig efficiency · Royal Jelly deeds run about 30-50% higher because they include a per-cell Hedera anchor. We bill against one of four fee tiers · Floor ($0.008) · Standard ($0.02) · Full ($0.05) · Enterprise ($0.10) · depending on the engagement type. The difference between cost and fee is our margin · which funds the rigs · the doctrine · the brand · the warranty · the people. We publish all of it because the math is the trust · and the trust is the brand.

## Jr Broker Use

The jr broker uses cost-to-mint as the ECONOMICS DIAL on every engagement:

1. When you open an engagement · the fee tier is set by the engagement type (use the routing matrix in the playbook · don't guess)
2. Watch the live cost-to-mint dial during the cook · if it crosses 2x baseline without producing Royal Jelly · flag it
3. The cost-to-mint goes on the Closing Statement · do NOT redact it · transparency is the brand
4. If a customer asks "is this expensive" · pull the comp · we publish our baseline · we compare against subscription vendors · we are typically 5-20x cheaper PER UNIT OF DEFENDABLE OUTPUT than $20/user/mo SaaS doing the same work
5. Never quote the FEE as if it were the COST · those are two different numbers · the customer is sophisticated · respect their underwriter

**Rule of thumb**: cost-to-mint is the OpEx · the fee is the rent · the margin is the cap rate · know all three.

## Sr Broker Use

The sr broker watches cost-to-mint as the OPERATING-MARGIN AUDIT:

- The weekly check includes a cost-to-mint efficiency review · per-rig · per-cook · per-engagement tier
- If a customer is consistently producing engagements that cost > 1.3x baseline · either the engagement type is wrong (should be a higher tier) OR the cook is mismatched to the customer's domain · adjust
- If the Royal Jelly cost ratio drifts above 1.6x Honey · investigate the Hedera anchor cost · sometimes network conditions push per-cell certificates up · re-quote enterprise customers
- The Floor tier is the LOSS-LEADER tier · margin is ~$0.003 · we run it for high-volume internal cooks AND for known-strategic customers · the founder approves Floor pricing personally
- Enterprise tier is where the white-glove margin lives · ensure the white-glove discipline matches the price · dedicated sr broker · custom anchors · SLAs honored

## Tribunal Use

```yaml
tribunal_use:
  classification_impact: []   # cost-to-mint is not a tier · it is the economic dial
  rule_layer_checks:
    - cost_to_mint.usd MUST be populated for every issued deed (no untracked economics)
    - cost_to_mint.breakdown MUST sum to cost_to_mint.usd (accounting integrity)
    - cost_to_mint.fee_charged_usd MUST be one of the 4 published tiers (no off-tier billing)
    - cost_to_mint.margin_usd MUST be non-negative for STANDARD/FULL/ENTERPRISE (Floor tier may be operator-discretion negative for strategic customers)
  judge_layer_prompt_hint: "cost-to-mint is not a judgment input · the judge does not score on cost"
  can_be_critical_failure: false   # economic metric · not a quality verdict
```

The Tribunal does not grade cost-to-mint · but the validator chain (C11 SHA-256 + audit hooks) ensures the cost-to-mint is logged and reconciled for every deed. Unreconciled economics = unverifiable deed.

## Evidence Required

To claim a cost-to-mint:

- An energy ledger entry covering all 6 line items (electrical · GPU · operator · anchor · storage · chain overhead)
- A per-rig PDU reading for the cook period
- A per-Bee GPU-second log
- An operator-activity log for review minutes
- A Hedera HCS transaction reference for anchor cost
- A reconciled total that matches the published cost-to-mint value
- The fee tier billed (with engagement-type justification)

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **cost_unreconciled** | Cost-to-mint reported but breakdown does not sum to total | Deed held · accounting integrity event · investigate before publishing |
| **fee_off_tier** | A custom fee charged outside the 4 published tiers | Operator-discipline event · the fee is revised to the nearest published tier · the operator is coached |
| **negative_margin_standard** | A STANDARD-tier deed produced a negative margin (cook cost > fee) | Engineering audit · either re-tier the customer or fix the cook efficiency |
| **cost_inflation_unmonitored** | Cost-to-mint trending up > 20% over 30 days with no operator review | Sr broker investigates · most common causes are temp drift · network fee shifts · rig amortization adjustments |
| **shadow_cost** | Compute consumed without contributing to a tracked cost-to-mint | Operator-discipline event · the rig is locked · all unattributed deeds are held |

## Scoring Impact

- **assignment_success**: ENABLER · cost-to-mint must be within margin tolerance for the engagement to be commercially viable
- **repair_lift**: TRADE-OFF · repair adds energy → adds cost · the lift must justify the additional cost · SwarmFixer is measured on energy-per-lift-point
- **validator_confidence**: NEUTRAL · we do not increase or decrease confidence based on cost
- **risk_temperature**: NEUTRAL at the pair level · ELEVATED at the system level when sustained cost spikes occur
- **probability_of_close**: ENABLER · per-deed margin enables the engagement model
- **evidence_strength**: NEUTRAL · evidence weight is independent of cost
- **cost_to_mint**: SELF · this term IS the cost-to-mint dial

## Deed / Receipt Impact

- **Receipt fields touched**: `cost_to_mint.usd` · `cost_to_mint.breakdown.*` · `cost_to_mint.fee_tier` · `cost_to_mint.fee_charged_usd` · `cost_to_mint.margin_usd`
- **DDEED class impact**: Every DDEED carries the full cost-to-mint line · for customer transparency · for operator accountability
- **Books and records layer**: ALL 5 (L1 hot · L2 hashed · L3 archived · L4 anchored · L5 ENS for Royal Jelly)
- **5 Proofs touched**: ECONOMICS (cost-to-mint IS the economics proof) · TRUST (publishing the math IS the trust signal)

## Related Terms

- [energy](energy.md) · the input that aggregates into cost-to-mint
- [royal-jelly](royal-jelly.md) · the apex tier that costs ~1.3-1.5x Honey baseline
- [honey](honey.md) · the tier whose baseline IS the cost-to-mint anchor
- [propolis](propolis.md) · the failure tier whose cost IS the cost of quality discipline · published transparently
- [hive](hive.md) · the entity whose cost-to-mint is the unit economic
- [bee](bee.md) · the worker whose per-instance compute is the cost-to-mint atomic unit

## Example

> **Engagement**: Industrial cold-storage AVO · STNL acquisition opinion · Full-tier customer · Royal Jelly target.
>
> **Cost-to-mint breakdown for the deed**:
>
> - Electrical: 0.0091 kWh × $0.085/kWh = $0.00077
> - GPU compute: 18.4 GPU-sec × $0.0011/sec = $0.00202
> - Operator review: 4 min × $1.20/min = $0.00800 (sr broker validated the apex)
> - Hedera per-cell certificate: $0.00080
> - Storage carry (amortized): $0.00080
> - Chain overhead: $0.00110
> - **Total cost-to-mint: $0.01349** (~2.6x Honey baseline · within Royal Jelly + Full-tier white-glove tolerance)
>
> **Fee charged**: $0.05 (Full tier)
> **Margin**: $0.03651 (~270% over cost)
>
> **Closing Statement disclosure**:
> "Deed DDEED-DOV-CRE-LINEAGE-ATL-000042-v1 · cost-to-mint $0.01349 · fee tier FULL · invoiced $0.05 · margin $0.03651. Cost breakdown · electrical $0.00077 · GPU $0.00202 · operator $0.00800 · anchor $0.00080 · storage $0.00080 · chain overhead $0.00110."
>
> **Outcome**: Customer's underwriter confirms the engagement-tier pricing is consistent with disclosed cost-to-mint · the deed is added to the customer's compliance file with the full economic line · the customer's annual operating budget accurately models DefendableOS as a $XXX-per-month line item rather than a fog-priced SaaS subscription.

## DefendableOS Notes

- The $0.0052/deed baseline is the production-tested number · it is publicly cited in our pricing page · it is the brand's anti-fantasy mechanism
- The 4 fee tiers (Floor · Standard · Full · Enterprise) are the published price list · we do not negotiate off-tier without founder approval
- Customers who want fixed monthly subscriptions are offered a tier-based per-deed model first · subscription is available but framed as a convenience · the unit economics remain visible underneath
- The margin in the Standard and Full tiers is what funds the Hive's R&D · the doctrine · the brand · the warranty · the people
- Publishing cost-to-mint is the brand's defensive moat against "AI is too expensive" narrative · our economics are auditable · most vendors' are not

🐝 *Cost-to-mint is the all-in dollar number per deed. Publish it. Price against it. The math is the trust. The trust is the brand. The brand is the asset on the books.*
