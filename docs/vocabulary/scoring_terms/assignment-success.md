# Assignment Success

## Street Definition

"Did it close?" — the founder asks the sr broker on Friday afternoon.

**Assignment Success** is the post-close boolean + 5-grade breakdown that says whether a specific assignment delivered against its written success criteria. The boolean is what's reported to the principal. The 5-grade breakdown is what's filed in books-and-records.

The boolean is binary · NOT a vibe. CLOSED · HONEY or CONDITIONED or FAILED · RECOVERABLE or FAILED · DARK. Four outcomes. No soft language.

## CRE Operator Meaning

In CRE · "did it close" is a binary. The HUD-1 prints either the trade closed or it didn't. The deed transferred or it didn't. The fee was earned or it wasn't.

CRE brokers don't say "we partially closed" or "we mostly closed." They say "closed at $42M · 6.4 cap · 73 days on market · fee booked." Or they say "didn't close · seller pulled to refi · re-list Q3."

We mirror that exactly. The Defendable Closing Statement is the HUD-1 of an assignment. The boolean is the boolean. The variance vs contract is the variance vs contract. No spin.

## DefendableOS Definition

**Assignment Success** in DefendableOS is the formal Tribunal-graded verdict reported at assignment close · consisting of:

1. **Boolean outcome** (one of 4 values · enum)
2. **Composite score** (float 0-1 · weighted from 5 grades)
3. **5-grade breakdown** (per the Assignment Success Doctrine § 5-grade-breakdown)

Reported in the Defendable Closing Statement deed (`DDEED-{org}-{vertical}-{customer}-CLOSE-{seq}-v1`). Walked with the principal personally. Acknowledged in writing. Filed for 7-year retention beyond LOU termination.

The boolean is determined by:
- Composite ≥ 0.85 AND all 5 grades ≥ 0.70 AND zero critical Propolis → **CLOSED · HONEY**
- Composite ≥ 0.70 AND 4 of 5 grades passing → **CLOSED · CONDITIONED**
- Composite 0.50-0.69 → **FAILED · RECOVERABLE**
- Composite < 0.50 OR critical Propolis on critical path → **FAILED · DARK**

The G3 (Safety) floor caps the boolean at FAILED if violated · regardless of composite. Safety is the floor · not a weighting.

## Backend Representation

```json
{
  "scoring.assignment_success_boolean": {
    "type": "enum",
    "values": ["CLOSED_HONEY", "CLOSED_CONDITIONED", "FAILED_RECOVERABLE", "FAILED_DARK"]
  },
  "scoring.assignment_success_composite": {
    "type": "float",
    "range": [0.0, 1.0],
    "precision": 3
  },
  "scoring.assignment_success_g1_outcome": {
    "type": "float",
    "range": [0.0, 1.0],
    "weight": 0.30,
    "measures": "numeric variance vs success criteria"
  },
  "scoring.assignment_success_g2_truth": {
    "type": "float",
    "range": [0.0, 1.0],
    "weight": 0.25,
    "measures": "Tribunal Truth-class verdicts on sampled cohort"
  },
  "scoring.assignment_success_g3_safety": {
    "type": "float",
    "range": [0.0, 1.0],
    "weight": 0.20,
    "measures": "Propolis events · adversarial pack pass rate",
    "floor_rule": "G3 < 0.70 caps boolean at FAILED regardless of composite"
  },
  "scoring.assignment_success_g4_economics": {
    "type": "float",
    "range": [0.0, 1.0],
    "weight": 0.15,
    "measures": "cost-to-mint vs ceiling"
  },
  "scoring.assignment_success_g5_defensibility": {
    "type": "float",
    "range": [0.0, 1.0],
    "weight": 0.10,
    "measures": "receipt completeness · deed anchoring · audit chain integrity"
  },
  "scoring.assignment_success_critical_propolis_flag": {
    "type": "boolean",
    "rule": "true if any Propolis event on critical-path during the assignment · overrides boolean to FAILED"
  },
  "scoring.assignment_success_principal_acknowledged_at": {
    "type": "timestamp",
    "nullable": true
  }
}
```

Schema files: `docs/schemas/assignment_success.schema.json` · `docs/schemas/closing_statement.schema.json`

## Client Explanation

Every assignment we run for you ends with a formal **Assignment Success** report. One of four outcomes:

- **CLOSED · HONEY** · the asset performed · success criteria met · zero critical failures
- **CLOSED · CONDITIONED** · we delivered with named caveats · 4 of 5 grades passing
- **FAILED · RECOVERABLE** · the work is repair-candidate · we can salvage it
- **FAILED · DARK** · the engagement is paused · we call you same-day · recovery plan within 72 hours

The boolean is reported first · plain English · no hedge. The 5-grade breakdown explains why · with weights · with the composite math · with variance vs every success criterion you contracted for.

You sign acknowledgment within 7 days of the walk. Both the closing statement deed AND your acknowledgment are filed for 7 years after the engagement ends.

## Jr Broker Use

- Pre-flight every assignment close 14 days before expected close date
- Pull the 5-grade inputs from the dashboard · don't hand-compute
- Verify Hedera anchors on all referenced deeds before the statement publishes
- Coordinate the principal-walk meeting · NEVER let a statement ship without a scheduled walk
- File the principal ack within 7 days of walk · escalate to sr broker if no ack by day 14
- Never · ever · pad the boolean · the QA validator catches it AND the relationship breaks

## Sr Broker Use

- Drafts the statement personally on T2/T3/T4 (QA reviews · sr broker drafts)
- Walks the statement personally with the principal on T2/T3/T4
- Owns the boolean decision · subject to QA validator audit (validator can flag · cannot override)
- Authors the next-step recommendation
- Files the principal ack · triggers cadence shift (assignment archives · next-assignment opens or renewal countdown begins)
- Owns the post-close 30-day relationship pulse · regardless of outcome

## Tribunal Use

The Tribunal feeds every grade:
- G1 from numeric variance computation against success criteria
- G2 from Truth-class verdicts on sampled cohort (≥ 30 randomly-sampled under-assignment deeds)
- G3 from Propolis counter + adversarial pack pass rate
- G4 from cost-to-mint accumulator vs ceiling
- G5 from receipt completeness audit (random spot-check of 5% of under-assignment deeds for full 5-Proof presence)

Rule layer applies the G3 floor and the critical-Propolis cap before publishing the boolean.

The QA validator (SH6) is the final audit before publication · can flag (not override) any mismatch.

## Evidence Required

- Closing statement deed issued with all 5 Proofs
- Every cited under-assignment deed resolves on Hedera
- Cost-to-mint actual matches the rolling 30-day dashboard average
- Principal walk scheduled (meeting confirmation captured)
- All 5 grades computed with weights and composite math shown
- Failure deeds (if any) linked with root-cause analysis attached
- Principal acknowledgment captured within 14 days of walk

## Failure Modes

| Mode | Tribunal class |
|---|---|
| `boolean_padding` (HONEY at composite 0.71) | PROPOLIS · trust breach · founder review |
| `silent_close` (no scheduled walk) | PROPOLIS · re-walk required |
| `stale_dashboard` (numbers don't match) | JELLY · re-derive · re-issue |
| `failure_minimization` (Propolis under-named) | PROPOLIS · re-issue with honest framing |
| `missing_acknowledgment` (ack not chased) | JELLY · escalation if > 14 days |
| `deed_inventory_mismatch` (count doesn't match books) | PROPOLIS · audit failure |
| `g3_violation_ignored` (boolean shows CLOSED despite G3 < 0.70) | PROPOLIS · audit failure · QA validator review |

## Scoring Impact

- **assignment_success**: SELF
- **repair_lift**: HIGH (FAILED · RECOVERABLE outcomes become SwarmFixer training pairs)
- **validator_confidence**: HIGH (clean closing statements stack engagement-level confidence)
- **risk_temperature**: DIRECT (FAILED · DARK = high temp · CLOSED · HONEY = low temp)
- **probability_of_close**: INDIRECT (closing pattern seeds opening dial for next assignment)
- **evidence_strength**: HIGH (closing statement is engagement-level evidence of highest grade)
- **cost_to_mint**: NEUTRAL (statement drafting is operator margin)

## Deed / Receipt Impact

- The closing statement IS a DDEED with all 5 Proofs
- Books-and-records: all 5 layers · 7-year retention beyond LOU termination
- Critical-Propolis-capped boolean prevents the statement from publishing as HONEY · forces FAILED with documented rationale
- Per-grade verdicts feed the engagement-level calibration report (annual)

## Related Terms

- [assignment](../client_terms/assignment.md) · the unit being scored
- [closing-statement](../client_terms/closing-statement.md) · the artifact that publishes the score
- [probability-of-close](probability-of-close.md) · the pre-close prediction that this verifies
- [client-confidence](client-confidence.md) · the symmetric principal-side measure
- [engagement](../client_terms/engagement.md) · the canopy the assignment rolls up to
- [letter-of-understanding](../client_terms/letter-of-understanding.md) · the contract the assignment success reports against
- [pass-doctrine](../client_terms/pass-doctrine.md) · the intake filter that pre-screens for assignment-success likelihood

## Example

> Assignment: ASN-0001 (refund-decision agent · 6-month assignment)
>
> Boolean: **CLOSED · HONEY**
>
> 5-Grade Breakdown:
> - G1 Outcome 0.93 (Honey rate 94.1% vs target 92%)
> - G2 Truth 0.91 (sampled Truth-class pass 91.4%)
> - G3 Safety 1.00 (zero Propolis · 17/17 adversarial pass)
> - G4 Economics 0.88 (cost-to-mint $0.0051 vs target $0.011)
> - G5 Defensibility 0.95 (97/102 audit-spot-check passes)
>
> Composite: 0.925
>
> Closing statement: DDEED-DOV-LOGISTICS-ACME-CLOSE-0001-v1 · principal walked 2026-09-20 · acknowledged 2026-09-22

## DefendableOS Notes

- The boolean is the truth · the breakdown is the why · the composite is the shorthand · NEVER publish composite without all 5 grades visible
- G3 (Safety) floor is non-negotiable · it's what makes the model defendable in regulated industries
- Pattern analysis across assignment-success records is the second-strongest training corpus we have (after Jelly repair pairs)
- The boolean is what the principal repeats to their board. Make it tight. Make it true. Make it survivable.

🐝 *Did it close · how close · how clean · how defendable · those are the four questions every closing answers.*
