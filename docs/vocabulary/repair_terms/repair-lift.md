# Repair Lift

## Street Definition

"What's the lift?" That's the only question the operator cares about after a refinery run. **Repair Lift** is the measured delta · the before-score vs the after-score · the number that proves the fix worked. No lift, no deed. Negative lift, you blew it. ≥ 0.10 lift, you get the bucket transition.

## CRE Operator Meaning

In CRE Repair Lift is the **NOI lift on a value-add deal**. You buy the building at a 6-cap. You do the rehab. You re-lease at higher rents. The NOI goes from $1.2M to $1.6M. That's a $400K NOI lift · at a 5-cap exit, that's $8M of additional asset value. The rehab IS the deal. No NOI lift, you overpaid on a Class B that thinks it's a Class A. **Repair Lift is NOI for agents.**

## DefendableOS Definition

Repair Lift is the numeric delta between a pair candidate's original Tribunal composite score and the same pair's score AFTER SwarmFixer refinery. The formula is locked:

```
repair_lift = repaired_composite_score - original_composite_score
```

Range: [-1.0, +1.0] (in practice typically -0.20 to +0.40). The threshold for `jelly-repaired/` bucket transition is **≥ 0.10 AND validator_confidence ≥ 0.6**. Below 0.10, the pair re-routes to `pending/` for up to 2 retries. Negative lift routes to `propolis-failures/` and feeds the AdversarialPack.

## Backend Representation

```json
{
  "repair_lift.value": {"type": "float", "range": [-1.0, 1.0]},
  "repair_lift.original_score": {"type": "float", "range": [0.0, 1.0]},
  "repair_lift.repaired_score": {"type": "float", "range": [0.0, 1.0]},
  "repair_lift.threshold_for_promotion": {"type": "float", "const": 0.10},
  "repair_lift.validator_confidence_required": {"type": "float", "const": 0.6},
  "repair_lift.axes_breakdown": {
    "type": "object",
    "fields": ["correctness","completeness","format_compliance","reasoning_depth"]
  },
  "repair_lift.tribunal_run_id_original": {"type": "string"},
  "repair_lift.tribunal_run_id_repaired": {"type": "string"}
}
```

Schema files: `docs/schemas/royal_jelly_record.schema.json` · `docs/schemas/repair_run.schema.json` · `docs/schemas/ui_dial.schema.json`

Scoring hooks: `bucket_transition_decision` · `customer_weekly_sla_aggregate` · `dashboard_repair_lift_dial`

## Client Explanation

Repair Lift is the number on your invoice that proves we earned it. Your AI agent shipped an answer scoring 76 · we refined it to 91 · the lift is +0.15 · the threshold for production promotion is +0.10 · we cleared it. On your Embedded tier, the weekly aggregate lift number is what backs your renewal · it's what we'd refund against if we missed.

## Jr Broker Use

The Jr Hack on classifier duty calculates Repair Lift on every refinery run · NOT optional · NOT estimated. The two Tribunal verdicts (original + repaired) both anchor to receipts before the lift number is computed. The lift gets logged with both verdict run_ids so the customer or auditor can re-derive it independently.

Don't round the lift. Don't bucket it into "good" / "bad" categories. The number is the number. Three decimal places. Logged as-is.

## Sr Broker Use

The Sr Hack reads the lift distribution weekly · not just the mean. A mean lift of +0.18 with p10 of -0.05 is a different reality than a mean of +0.18 with p10 of +0.04. The first has tail risk · the second is a refinery that's behaving. Sr Hacks set distribution-shape alerts · not just mean alerts.

When the lift drifts down 2 weeks in a row · the Sr Hack triggers a refinery tuning review BEFORE the customer dashboard reflects it. The customer's KPI is downstream of the lift · the Sr Hack manages upstream.

## Tribunal Use

- **Rule layer**: Repair Lift MUST be computed from two anchored Tribunal verdicts · synthesized lift numbers are rejected (C04 evidence binding)
- **Rule layer**: `validator_confidence < 0.6` blocks promotion even if lift ≥ 0.10
- **Judge layer**: Tribunal grades the repaired output as a fresh submission · doesn't carry forward the original score · the lift is purely the math of two independent verdicts
- **Classification impact**: lift ≥ 0.10 → ROYAL JELLY promotion · 0 ≤ lift < 0.10 → JELLY hold · lift < 0 → PROPOLIS regression

## Evidence Required

- Original pair Tribunal verdict (with run_id)
- Repaired pair Tribunal verdict (with run_id)
- Validator chain pass (≥ 0.6 confidence)
- Axes breakdown (correctness · completeness · format_compliance · reasoning_depth)
- Timestamp of refinery run between the two verdicts
- SwarmJelly model tag used for the refinery (proves TEMP=0.05 path)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `synthesized_lift` | Lift number cited without two anchored Tribunal verdicts | PROPOLIS · evidence violation |
| `rounded_lift` | Lift rounded or bucketed before logging | JELLY · data integrity |
| `axes_missing` | Lift reported without the 4-axis breakdown | JELLY · validator re-run |
| `judge_drift_high` | Repaired verdict has judge_drift_AB > 0.15 · lift is contested | JELLY · escalate to validator |
| `negative_lift_unlogged` | Negative lift not routed to propolis-failures | PROPOLIS · refinery governance |
| `weekly_aggregate_drift` | Weekly mean lift drifts down 2 weeks in row without tuning trigger | JELLY · operator-discipline failure |

## Scoring Impact

- **assignment_success**: DIRECT · lift IS the assignment success metric for the refinery
- **repair_lift**: SELF · this term defines the dial
- **validator_confidence**: GATED · promotion requires both lift ≥ 0.10 AND confidence ≥ 0.6
- **risk_temperature**: INVERSE · positive lift trend lowers risk · negative lift trend raises it
- **probability_of_close**: HIGH · customer-facing weekly aggregate is a renewal predictor
- **evidence_strength**: HIGH · lift is the strongest evidence of refinery value
- **cost_to_mint**: NEUTRAL · the deed cost is the same regardless of lift size

## Deed / Receipt Impact

- **Receipt fields touched**: `repair_lift.value` · `original_score` · `repaired_score` · `axes_breakdown` · `tribunal_run_id_original` · `tribunal_run_id_repaired`
- **DDEED class impact**: lift value embedded in every DDEED-DOV-REPAIR · used as the primary numeric attestation
- **Books and records layer**: L1 PostgreSQL → L2 Merkle (lift as Merkle leaf) → L4 Hedera HCS (anchored) → L5 ENS (resolvable per deed)
- **5 Proofs touched**: QUALITY (the lift IS the quality measurement) · PROCESS (the two-verdict lineage that produced it) · ECONOMICS (cost-per-lift is the unit economics)

## Related Terms

- [swarmfixer](swarmfixer.md) · the refinery that produces the lift
- [swarmjelly](swarmjelly.md) · the model that produces the lift
- [pair-candidate](pair-candidate.md) · the unit lift is measured on
- [compare-task](compare-task.md) · the RJ task that ranks repaired outputs feeding the lift
- [validator-confidence](../scoring_terms/validator-confidence.md) · the second gate alongside lift
- [evidence-strength](../scoring_terms/evidence-strength.md) · related dial

## Example

> **Original pair**: books-bot.acmecorp.defendable.eth · journal entry error · Tribunal verdict JELLY · composite 0.760 · axes: correctness 0.70 · completeness 0.85 · format 0.80 · reasoning 0.65
>
> **Refinery run**: `ag-fix-20260524T071200Z-9a3c` · SwarmJelly-4B v1.2 · TEMP=0.05
>
> **Repaired pair**: re-bench Tribunal verdict ROYAL_JELLY · composite 0.910 · axes: correctness 0.95 · completeness 0.92 · format 0.95 · reasoning 0.85
>
> **Repair Lift**: 0.910 - 0.760 = **+0.150** (clears 0.10 threshold)
>
> **Validator confidence**: 0.78 (clears 0.6 threshold)
>
> **Bucket transition**: `jelly/` → `jelly-repaired/`
>
> **Deed**: `DDEED-DOV-REPAIR-ACMECORP-BOOKS-000142-v1` · repair_lift field embedded · resolvable on ENS

## DefendableOS Notes

- Repair Lift is the unit economics of the refinery · cost-per-lift = (refinery inference cost + deed mint cost) / mean lift over period
- A refinery that ships at +0.15 mean lift at $0.055/run is a unit-economic winner · the customer pays for the lift · we pay for the inference
- The CRE analogy holds end-to-end · lift IS NOI for agents · the comp set is the customer's prior week · the asset value is the deed lineage
- See also the SCORING DIAL version of this term at [`../scoring_terms/repair-lift.md`](../scoring_terms/repair-lift.md) · same number · different UI surface

🐝 *No lift, no deed. The lift is the receipt.*
