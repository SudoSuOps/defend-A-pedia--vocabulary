# Evidence Strength

## Street Definition

"How strong is the evidence?" That's the discriminator question on every Tribunal verdict review. **Evidence Strength** is the 0-1 dial that measures how well-supported a pair candidate's evidence base is · count of independent citations × mean source quality × freshness. Thin evidence cap-rates the verdict. Strong evidence unlocks promotion.

## CRE Operator Meaning

In CRE this is the **comp set quality**. A deal pencils on the strength of its comp set · 5 same-submarket recent sales is strong · 1 stale out-of-state comp is thin · the broker who pencils against thin comps eats the failed listing. Evidence Strength is the comp-set quality score for the agent economy. Strong evidence backs the verdict the way 5 fresh comps back a cap rate.

## DefendableOS Definition

Evidence Strength is a 0-1 dial computed from three multiplicative factors:

```
evidence_strength = color_evidence_count_normalized × mean_source_weight × (1 - staleness_penalty)
```

Where:
- `color_evidence_count_normalized` = min(evidence_count / 5, 1.0) (5 is the canonical baseline)
- `mean_source_weight` = the average of source weights (EDGAR 0.90 · OpenAlex 0.85 · CRE News 0.65 · Reddit 0.50 · etc.)
- `staleness_penalty` = (days_since_oldest_source / 30) * 0.4 capped at 0.4

The threshold for refinery eligibility is `evidence_strength ≥ 0.4` (below 0.4, SwarmFixer cannot run on the pair).

## Backend Representation

```json
{
  "evidence_strength.value": {"type": "float", "range": [0.0, 1.0]},
  "evidence_strength.formula_inputs": {
    "type": "object",
    "required": ["evidence_count", "mean_source_weight", "oldest_source_days_old"],
    "properties": {
      "evidence_count": {"type": "integer", "min": 0},
      "mean_source_weight": {"type": "float", "range": [0.0, 1.0]},
      "oldest_source_days_old": {"type": "integer", "min": 0}
    }
  },
  "evidence_strength.normalization_baseline": {"type": "integer", "const": 5},
  "evidence_strength.staleness_penalty_max": {"type": "float", "const": 0.4},
  "evidence_strength.refinery_eligibility_threshold": {"type": "float", "const": 0.4},
  "evidence_strength.source_weights_reference": {"type": "string", "const": "EntityScorer table"}
}
```

Schema files: `docs/schemas/evidence_record.schema.json` · `docs/schemas/ui_dial.schema.json` · `docs/schemas/entity_scorer.schema.json`

## Client Explanation

Evidence Strength is how strong the evidence is behind every verdict. We count the citations · weight them by source quality (EDGAR > Wikipedia > Reddit) · and apply a freshness penalty (stale evidence loses weight). The dial shows you whether your verdict is backed by gold-standard receipts or by thin air. Anything below 0.4 doesn't even qualify for our refinery · we'd be building on sand.

## Jr Broker Use

The Jr Hack pre-screens every incoming pair on Evidence Strength BEFORE routing to SwarmFixer. Below 0.4 = route to evidence-gathering · not to refinery. The Jr Hack also documents the source citations explicitly · "EDGAR 10-K filing for entity X dated 2026-04-15" not "Wikipedia entry for X" · the EntityScorer table caps Wikipedia at 0.65 while EDGAR sits at 0.90.

## Sr Broker Use

The Sr Hack monitors the distribution of Evidence Strength across incoming pairs · a drift down (mean falling from 0.7 to 0.55 over 4 weeks) signals an upstream change · customer's agent dropped a high-weight source · or model provider stopped including citations · or the routing changed. The Sr Hack escalates upstream before the refinery throughput collapses.

## Tribunal Use

- **Rule layer**: Evidence Strength MUST be computed from the documented formula with the documented EntityScorer weights
- **Rule layer**: Below 0.4, the pair cannot enter SwarmFixer · it routes to evidence-gathering instead
- **Rule layer**: A pair claiming 5 sources but all single-source-class (e.g., 5 Reddit) gets capped at the source-class weight (0.50) not boosted by count
- **Judge layer**: Tribunal doesn't grade Evidence Strength directly · it consumes the dial value · low evidence strength caps the verdict tier
- **Classification impact**: Evidence Strength < 0.4 caps the verdict at JELLY · cannot reach ROYAL JELLY no matter the lift

## Evidence Required

- The count of distinct citations
- The list of sources with EntityScorer weights
- The date of the oldest source (drives staleness)
- The formula application showing the three factors and the product
- The threshold check (≥ 0.4 for refinery eligibility)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `single_source_padding` | Pair cites 5 quotes from one source counted as 5 evidence | JELLY · de-dup required |
| `wrong_source_weights` | Formula applied with weights not from EntityScorer | PROPOLIS · governance violation |
| `staleness_not_applied` | Old sources used at full weight without penalty | JELLY · re-compute |
| `fabricated_source` | Source cited doesn't exist · count inflated | PROPOLIS · auto-quarantine |
| `below_threshold_refinery_run` | SwarmFixer ran on pair with evidence_strength < 0.4 | PROPOLIS · refinery governance |
| `evidence_count_only` | Dial computed as count only · ignoring source weights and staleness | PROPOLIS · governance violation |

## Scoring Impact

- **assignment_success**: HIGH · evidence strength is the precondition for refinery work
- **repair_lift**: GATING · below 0.4, no refinery, no lift
- **validator_confidence**: INPUT · evidence strength feeds the validator confidence formula
- **risk_temperature**: INVERSE · strong evidence = low risk
- **probability_of_close**: HIGH · customers trust verdicts backed by strong evidence
- **evidence_strength**: SELF
- **cost_to_mint**: NEUTRAL · evidence computation is part of standard pipeline

## Deed / Receipt Impact

- **Receipt fields touched**: `evidence_strength.value` · formula inputs · source weights table reference
- **DDEED class impact**: deeds embed evidence strength · auditors can re-derive
- **Books and records layer**: L1 PostgreSQL (per-pair evidence record) → L2 Merkle (source citations as leaves) → L4 Hedera HCS (anchored)
- **5 Proofs touched**: QUALITY (source weights ARE quality) · PROCESS (evidence-gathering lineage) · TRUST (re-derivable formula)

## Related Terms

- [repair-lift](repair-lift.md) · partner dial · evidence gates whether refinery can produce lift
- [validator-confidence](validator-confidence.md) · evidence strength is an input
- [risk-temperature](risk-temperature.md) · partner dial · evidence inversely correlates with risk
- [pair-candidate](../repair_terms/pair-candidate.md) · the unit evidence is measured on
- [swarmfixer](../repair_terms/swarmfixer.md) · refinery requires evidence_strength ≥ 0.4

## Example

> **Pair with strong evidence (`pair-20260524T061208Z-7e2a`)**:
> - evidence_count: 5
> - sources: EDGAR 10-K (0.90) · CompStak (0.85) · ATTOM (0.85) · broker phone log (0.90) · SwarmCurator CRE corpus (0.85)
> - mean_source_weight: 0.870
> - oldest_source_days_old: 14
> - staleness_penalty: (14/30) × 0.4 = 0.187
> - Formula: min(5/5, 1.0) × 0.870 × (1 - 0.187) = 1.0 × 0.870 × 0.813 = **0.707**
> - Refinery eligible: YES (0.707 ≥ 0.4)
>
> **Pair with weak evidence (`pair-20260524T071800Z-x9k1`)**:
> - evidence_count: 2 (both Reddit threads)
> - mean_source_weight: 0.50 (Reddit cap)
> - oldest_source_days_old: 45
> - staleness_penalty: capped at 0.4
> - Formula: min(2/5, 1.0) × 0.50 × (1 - 0.4) = 0.4 × 0.50 × 0.6 = **0.120**
> - Refinery eligible: NO (0.120 < 0.4)
> - Routes to evidence-gathering queue instead

## DefendableOS Notes

- Evidence Strength is what separates the refinery from a guessing engine · without strong evidence, the diagnose and repair are speculation
- The EntityScorer source weights table is the canonical reference · it lives at `docs/schemas/entity_scorer.schema.json` · changes require a doctrine PR
- The 0.4 threshold is the floor for refinery eligibility · the 5-evidence baseline is the normalization point · both are constitutional
- Evidence Strength × Validator Confidence × Repair Lift = the trinity of dials that gate every Royal Jelly promotion · all three must clear

🐝 *Five comps backed by EDGAR vs one stale Reddit thread. The dial tells you which deal is real.*
