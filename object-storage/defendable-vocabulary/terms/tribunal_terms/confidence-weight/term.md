# Confidence Weight

> *"Confidence weight is the dial · 0 to 1 · how sure are we that this verdict is right. Not the score · the score is the verdict · the confidence is HOW SURE we are of the score."*
> — Founder · why we measure certainty separately from quality

## Street Definition

"What's the confidence weight?" Confidence weight is the validator-and-Tribunal-produced 0-to-1 dial that says HOW SURE we are that the verdict on a pair is correct. It is distinct from the JellyScore (which is the verdict itself) · the confidence weight measures the certainty of the verdict. A pair can be Royal Jelly with low confidence weight (the chain cleared but barely · the judges agreed but at the threshold) · or Honey with high confidence weight (the chain cleared cleanly · the judges agreed strongly · the evidence was deep).

In CRE language · confidence weight maps to the appraiser's reconciliation comment · the underwriter's confidence-in-the-deal · the closing agent's degree-of-comfort with the chain. An appraiser can produce a high value with low confidence (extrapolated comps · thin data) or a moderate value with high confidence (rich comp set · sourced cleanly · no triangulation gaps). Same here. The score is the answer · the confidence weight is the certainty of the answer.

## CRE Operator Meaning

In CRE · the confidence weight is the operator-discipline dial · the broker who knows their numbers AND knows how solid their numbers are. A 6.0% cap rate quote backed by 12 comps in the submarket within 30 days is high-confidence. The SAME 6.0% cap rate backed by 2 comps from 18 months ago in adjacent submarkets is low-confidence. Both quotes are 6.0% caps · the confidence is what tells the buyer how much weight to put on each.

DefendableOS inherits the discipline directly. Confidence weight is published on every verdict · low-confidence Royal Jelly is still Royal Jelly · but the customer sees the certainty alongside the verdict and makes the appropriately-weighted use of the output.

## DefendableOS Definition

Confidence weight is a per-pair float (0.0-1.0) computed by aggregating:

1. **Validator chain confidence** · the mean of per-check confidence_weights from the 12 validators (deterministic checks contribute 1.0 · model-backed checks contribute the model's reported confidence)
2. **Judge drift confidence** · `1 - (drift / 0.15)` · clean-agreement judges produce 1.0 · drift at threshold produces 0.0 · drift beyond threshold (Critic-reconciled) produces a reduced confidence
3. **Evidence source confidence** · the mean of source-weight values across cited sources (per the EntityScorer 0.30-0.90 weight ladder)
4. **Reproducibility confidence** · the rerun-consistency value from the Reproducibility rubric grade

The composite formula:

```python
confidence_weight = (
    validator_chain_confidence  * 0.30
  + judge_drift_confidence      * 0.25
  + evidence_source_confidence  * 0.25
  + reproducibility_confidence  * 0.20
)
```

Output is clamped to [0.0, 1.0].

## Backend Representation

```json
{
  "confidence_weight.composite": { "type": "float", "range": [0.0, 1.0] },
  "confidence_weight.components": {
    "type": "object",
    "properties": {
      "validator_chain_confidence": { "type": "float" },
      "judge_drift_confidence": { "type": "float" },
      "evidence_source_confidence": { "type": "float" },
      "reproducibility_confidence": { "type": "float" }
    }
  },
  "confidence_weight.band": {
    "type": "enum",
    "values": ["HIGH", "MEDIUM", "LOW", "INSUFFICIENT"]
  }
}
```

Bands:
- HIGH: ≥ 0.85
- MEDIUM: 0.65-0.84
- LOW: 0.45-0.64
- INSUFFICIENT: < 0.45 (verdict is held pending review · sr broker decision required)

Schema files: `docs/schemas/confidence_weight.schema.json` · `docs/schemas/tribunal_verdict.schema.json`

## Client Explanation

"Confidence weight" is our 0-to-1 dial that tells you how SURE we are about the verdict on every output we ship. The verdict is one thing · the confidence is another. A Royal Jelly verdict with HIGH confidence means strong agreement across our chain · deep evidence · clean reproducibility. The SAME verdict with LOW confidence means we cleared the bar but barely · use the output with appropriate weighting. We publish the confidence on every deed so you know how much weight to put on each output in your downstream decisions.

## Jr Broker Use

The jr broker reads confidence weight as the SECOND DIMENSION of every verdict:

1. Every Tribunal verdict has both a JellyScore AND a confidence_weight · know both before reporting to the customer
2. HIGH confidence (≥ 0.85) is the typical green-light state · customer-facing language can be assertive
3. MEDIUM confidence (0.65-0.84) is the typical state for routine production · customer-facing language should be appropriately calibrated
4. LOW confidence (0.45-0.64) means escalate to sr broker · the verdict cleared but the certainty is thin · the customer may want a re-run or additional sourcing
5. INSUFFICIENT confidence (< 0.45) is held automatically · do NOT manually push through · sr broker review required

**Rule of thumb**: score answers "is it good" · confidence answers "how sure are we" · both go on the deed.

## Sr Broker Use

The sr broker watches confidence weight as the QUALITY-OF-CERTAINTY signal:

- Aggregate confidence weight per cook is a meta-quality dial · cooks producing high-score but low-confidence verdicts are over-fitting to a narrow source set · audit
- Confidence weight per engagement type reveals which engagement classes have natural certainty limits · medical regulatory engagements run higher confidence than speculative-comp engagements
- INSUFFICIENT confidence holds are the sr broker's queue · review with priority · either approve with sign-off (logged reason) OR re-run the engagement with stronger sourcing
- Component breakdowns reveal which dimension is weak · low validator_chain_confidence means a chain-validator is degraded · low judge_drift_confidence means the two judges are systematically diverging · low evidence_source_confidence means the source set is thin · low reproducibility_confidence means the cook is non-deterministic
- Confidence weight is what we publish to customers to demonstrate calibration discipline · most vendors only publish the score (and often inflated)

## Tribunal Use

```yaml
tribunal_use:
  classification_impact: []   # confidence is not a tier · it modulates the verdict
  rule_layer_checks:
    - confidence_weight.composite MUST be computed for every verdict
    - confidence_weight.band MUST be one of the 4 enum values
    - confidence_weight INSUFFICIENT MUST hold the verdict pending sr broker review
  judge_layer_prompt_hint: "your reasoning depth and source citation feed the confidence weight · be explicit about uncertainty"
  can_be_critical_failure: false   # confidence is a dial · not a critical-fail state
```

## Evidence Required

To claim a confidence weight:

- A computed composite value
- A populated components breakdown (all 4 sub-scores)
- An assigned band (one of 4 enum values)
- A reasoning log if the confidence was overridden by sr broker (rare)

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **confidence_inflation** | Composite confidence trending higher than peers in same engagement class | Audit the components · usually evidence_source_confidence is mis-weighted (source weight ladder is inflated) |
| **confidence_collapse** | Sudden drop in aggregate confidence weight · suggests upstream validator or judge degradation | Investigate · most common cause is judge temperature drift OR validator service degradation |
| **confidence_insufficient_unprocessed** | INSUFFICIENT-band verdict held for > 4h without sr broker review | Sr broker queue management failure · escalate · resolve same day |
| **confidence_overridden_silently** | Sr broker overrode INSUFFICIENT to approve without logged reason | Operator-discipline event · override is rolled back · operator coached |
| **confidence_decoupled_from_score** | High score (Royal Jelly) with persistently LOW confidence pattern | Cook is over-fitting to weak evidence · re-evaluate the curator settings · widen the source set |

## Scoring Impact

- **assignment_success**: MODULATES · low confidence may downgrade SUCCESS to PARTIAL pending review
- **repair_lift**: USED · repair lift = post-repair confidence - pre-repair confidence (in addition to score delta)
- **validator_confidence**: SELF · this term IS one of the components
- **risk_temperature**: INVERSE · higher confidence = lower risk
- **probability_of_close**: WEIGHTED · close prob is multiplied by confidence weight
- **evidence_strength**: COMPONENT · evidence_source_confidence is one of the 4 sub-scores
- **cost_to_mint**: NEUTRAL · we don't price differently by confidence · we publish the confidence

## Deed / Receipt Impact

- **Receipt fields touched**: `confidence_weight.composite` · `confidence_weight.components.*` · `confidence_weight.band`
- **DDEED class impact**: All DDEEDs carry the confidence weight as a published dial · LOW or INSUFFICIENT confidence DDEEDs receive a customer-facing advisory annotation
- **Books and records layer**: L1 PG (hot) · L2 Merkle (confidence in batch root)
- **5 Proofs touched**: QUALITY (confidence IS a quality refinement) · TRUST (publishing confidence IS the trust signal)

## Related Terms

- [validator](validator.md) · the role that produces per-check confidence
- [validator-chain](validator-chain.md) · the chain whose aggregate is one of the 4 components
- [judge](judge.md) · the role whose drift is the second component
- [tribunal](tribunal.md) · the parent system that publishes confidence
- [royal-jelly](../hive_terms/royal-jelly.md) · the apex tier that can carry variable confidence
- [honey](../hive_terms/honey.md) · the volume tier that can carry variable confidence

## Example

> **Engagement**: STNL opinion · cold storage · Atlanta MSA.
>
> **Confidence weight breakdown for the deed**:
> - validator_chain_confidence: 0.99 (all 12 checks PASS · 11 deterministic at 1.0 · 1 model-backed at 0.95)
> - judge_drift_confidence: 0.87 (drift 0.02 · well below threshold · `1 - (0.02/0.15) = 0.867`)
> - evidence_source_confidence: 0.91 (5 sources cited · weights mean 0.91 · EDGAR + CompStak + ATTOM + Local-Verified + SwarmCurator-CRE)
> - reproducibility_confidence: 0.85 (re-run produced composite within 0.03 · acceptable)
> - composite: `0.99*0.30 + 0.87*0.25 + 0.91*0.25 + 0.85*0.20 = 0.917`
> - band: HIGH
>
> **Customer-facing line on the deed**: "Confidence weight: HIGH (0.92). Components · validator chain 0.99 · judge drift 0.87 · evidence source 0.91 · reproducibility 0.85."
>
> **Outcome**: Customer reads both the JellyScore (0.90 Royal Jelly verdict) AND the confidence (0.92 HIGH) · knows the apex verdict is backed by strong certainty across all 4 dimensions · uses the deed in their compliance file with full assertive language.

## DefendableOS Notes

- Confidence weight is published on every deed · we do not show only the score · this is the calibration discipline
- The 4-component formula is doctrine · do not collapse to a single number for the customer · show all 4 on detailed deed views
- INSUFFICIENT band is the structural floor · these verdicts hold pending sr broker review · this is the founder-locked discipline
- The confidence weight is what distinguishes Defendable verdicts from leaderboard-style AI scores · we measure HOW SURE not just WHAT SCORE
- A high-score / low-confidence pattern is a known cook degradation signal · sr broker watches for it weekly

🐝 *Confidence weight is the dial · 0 to 1 · how sure we are. Score is the verdict · confidence is the certainty of the verdict. Both go on the deed. Both go in the books.*
