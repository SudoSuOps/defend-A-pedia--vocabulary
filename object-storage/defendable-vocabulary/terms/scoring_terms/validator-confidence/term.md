# Validator Confidence

## Street Definition

"What's the validator confidence?" That's the second question after the lift. **Validator Confidence** is the 0-1 dial showing how much trust the validator chain places in a given verdict. Computed from the 12-check pass rate weighted by the source quality. A pair with a great lift but low validator confidence doesn't promote · the chain doesn't believe in the math.

## CRE Operator Meaning

In CRE this is the **lender's confidence score** on a deal package. The numbers might pencil · the comps might support · but if the lender's underwriter has questions about the rent roll, the tenant credit, the title report, the appraisal date · the confidence score drops · the LTV gets capped · the rate goes up. The number alone isn't enough · the EVIDENCE behind the number matters. Validator Confidence is the lender's read on whether the receipts support the verdict.

## DefendableOS Definition

Validator Confidence is a 0-1 dial computed from two inputs: the 12-check validator chain pass rate (7 critical + 5 advisory) and the mean source weight of the evidence backing the verdict. The formula is:

```
validator_confidence = (critical_pass_rate × 0.7) + (advisory_pass_rate × 0.2) + (mean_source_weight × 0.1)
```

The threshold for `jelly-repaired/` promotion is `validator_confidence ≥ 0.6` (paired with `repair_lift ≥ 0.10`). Both must clear · neither is sufficient alone.

## Backend Representation

```json
{
  "validator_confidence.value": {"type": "float", "range": [0.0, 1.0]},
  "validator_confidence.formula_components": {
    "type": "object",
    "required": ["critical_pass_rate", "advisory_pass_rate", "mean_source_weight"],
    "properties": {
      "critical_pass_rate": {"type": "float", "range": [0.0, 1.0]},
      "advisory_pass_rate": {"type": "float", "range": [0.0, 1.0]},
      "mean_source_weight": {"type": "float", "range": [0.0, 1.0]}
    }
  },
  "validator_confidence.weights": {
    "type": "object",
    "const": {
      "critical": 0.7,
      "advisory": 0.2,
      "source_weight": 0.1
    }
  },
  "validator_confidence.promotion_threshold": {"type": "float", "const": 0.6},
  "validator_confidence.validator_chain_run_id": {"type": "string"}
}
```

Schema files: `docs/schemas/validator_chain.schema.json` · `docs/schemas/ui_dial.schema.json`

## Client Explanation

Validator Confidence is the trust score on a verdict. We don't just take the model's word · we run a 12-check chain on every verdict (7 must-pass · 5 advisory) and we weight the evidence quality. The dial shows you whether we're confident in the call. Below 0.6 · we don't promote · even if the lift number looks great. The dial protects you from over-confident wrong answers.

## Jr Broker Use

The Jr Hack reads Validator Confidence alongside Repair Lift · NEVER alone. A pair with lift +0.20 but confidence 0.45 does NOT promote · the chain is signaling something's off with the evidence. The Jr Hack investigates · usually it's a stale source (color > 30 days) or a single-source citation that should have been triangulated.

## Sr Broker Use

The Sr Hack monitors the distribution of validator confidence across the daily batch · a healthy day shows mean confidence ~0.75-0.85 with tails distributed normally. A bimodal distribution (cluster at 0.4 + cluster at 0.85) indicates two different qualities of evidence flowing in · the Sr Hack tracks which agent ENS or which model provider is sourcing the low-confidence cluster and triages upstream.

## Tribunal Use

- **Rule layer**: Validator Confidence MUST be computed from anchored validator chain run · not synthesized
- **Rule layer**: Promotion to `jelly-repaired/` requires confidence ≥ 0.6 AND lift ≥ 0.10 · both gates
- **Rule layer**: Weights MUST match the locked formula (0.7 / 0.2 / 0.1) · custom weights rejected
- **Judge layer**: Tribunal doesn't grade Validator Confidence · the validator chain produces it · Tribunal consumes it
- **Classification impact**: Low confidence (< 0.6) blocks Royal Jelly promotion · pair holds in JELLY or routes to quarantine

## Evidence Required

- Validator chain run with 12-check results (7 critical + 5 advisory)
- Per-check pass/fail with rationale
- Source weight table for evidence cited in the pair
- Formula application showing the three components and the final dot product
- Threshold comparison (≥ 0.6 for promotion)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `synthesized_confidence` | Confidence value cited without an anchored validator chain run | PROPOLIS · evidence violation |
| `custom_weights` | Formula applied with weights other than (0.7, 0.2, 0.1) | PROPOLIS · governance violation |
| `partial_chain_run` | Validator chain didn't complete all 12 checks | JELLY · re-run required |
| `source_weight_missing` | Evidence cited without source weight assignment | JELLY · re-route |
| `confidence_promotion_below_threshold` | Pair promoted with confidence < 0.6 | PROPOLIS · governance violation |
| `chain_drift` | Validator chain ran a different check set than the 12-check spec | PROPOLIS · governance violation |

## Scoring Impact

- **assignment_success**: HIGH · confidence is one of the two promotion gates
- **repair_lift**: PARTNER · together with lift gates the bucket transition
- **validator_confidence**: SELF · this term defines the dial
- **risk_temperature**: INVERSE · high confidence lowers risk · low confidence raises it
- **probability_of_close**: HIGH · confidence trend correlates with renewal probability
- **evidence_strength**: HIGH · confidence IS partly a function of evidence strength
- **cost_to_mint**: NEUTRAL · validator chain runs are part of the standard mint cost

## Deed / Receipt Impact

- **Receipt fields touched**: `validator_confidence.value` · `validator_chain_run_id` · formula components
- **DDEED class impact**: every DDEED-DOV-REPAIR embeds the validator confidence value · auditors can verify the chain
- **Books and records layer**: L1 PostgreSQL (validator chain runs) → L2 Merkle (check results) → L4 Hedera HCS (anchored per receipt)
- **5 Proofs touched**: QUALITY (the chain pass rate IS quality) · PROCESS (the 12-check lineage) · TRUST (chain-backed numeric attestation)

## Related Terms

- [repair-lift](repair-lift.md) · partner dial · both gates required for promotion
- [evidence-strength](evidence-strength.md) · input to the formula
- [risk-temperature](risk-temperature.md) · partner dial
- [pair-candidate](../repair_terms/pair-candidate.md) · the unit confidence is computed on
- [swarmfixer](../repair_terms/swarmfixer.md) · the refinery that needs both lift and confidence to promote

## Example

> **Pair `pair-20260524T061208Z-7e2a`**:
> - Validator chain run: `vc-20260524T071730Z-bb3e`
> - Critical checks (7): 7/7 pass · critical_pass_rate = 1.00
> - Advisory checks (5): 4/5 pass · advisory_pass_rate = 0.80
> - Evidence sources cited: 5 sources · mean_source_weight = 0.83
> - Formula: (1.00 × 0.7) + (0.80 × 0.2) + (0.83 × 0.1) = 0.700 + 0.160 + 0.083 = **0.943**
> - Threshold check: 0.943 ≥ 0.6 · GATE CLEARED
> - Paired with repair_lift = +0.15 · BOTH gates clear · promotion to `jelly-repaired/` proceeds
>
> **Pair `pair-20260524T061745Z-8f3c` (failed gate)**:
> - Critical checks: 6/7 pass (C04 evidence binding failed)
> - Confidence formula: (0.857 × 0.7) + (0.80 × 0.2) + (0.61 × 0.1) = 0.600 + 0.160 + 0.061 = **0.821**
> - Even though confidence ≥ 0.6 numerically, the C04 critical FAIL is an absolute gate · pair routes to `quarantined/` for evidence-fabrication review

## DefendableOS Notes

- Validator Confidence is the SECOND gate alongside Repair Lift · together they're the promotion test
- The weights are locked · 0.7/0.2/0.1 is constitutional · waivers require a doctrine PR
- A critical-check FAIL is an absolute gate regardless of numerical confidence · the rule layer cannot be overridden by the formula
- Validator Confidence appears on the dashboard alongside Repair Lift · both dials together tell the complete story
- The 12-check chain doctrine lives at `docs/doctrine/13_validator_chain_doctrine.md` · this dial is the chain's numeric surface

🐝 *The chain's belief in the verdict. Two gates · one promotion. Numbers backed by evidence.*
