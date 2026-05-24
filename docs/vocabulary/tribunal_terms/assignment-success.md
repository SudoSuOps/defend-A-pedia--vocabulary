# Assignment Success

> *"Did the assignment close · or didn't it. That's the boolean. The five-grade rubric is how you EARN the boolean. No shortcuts."*
> — Founder · operator framing of when AI work actually finishes the job

## Street Definition

"Did the assignment close?" Assignment success is the boolean answer · TRUE if the AI work product fulfilled the engagement scope to production-safe standard · FALSE if it did not. Underneath the boolean sits the 5-grade rubric (Capability · Truth · Safety · Numeric/Structural · Efficiency · with Reproducibility as a separate hygiene gate) · each scored independently · with a composite that determines whether the boolean is earned.

In CRE language · assignment success is "did the deal close" · the binary that gates commission · gates the next referral · gates the broker's reputation. Underneath the close-binary sits the diligence rubric · did the comps tie · did the title clear · did the financing fund · did the LOI hold to PSA. Same exact pattern. The binary at the top · the rubric underneath · earn the boolean by clearing the rubric.

## CRE Operator Meaning

In CRE · assignment success is the closing event · the wire hits · the deed records · the LOU obligations are met · the commission earns. A broker's career is the sum of assignment successes · not the sum of engagements opened. A 30-year broker who closes 1 in 4 engagements has a stronger book than a broker who opens 4x as many but closes 1 in 12. Same here. AI engagement open is cheap · assignment success is the asset.

The 5-grade rubric inside is the rigor that distinguishes a closing-grade work product from a presentation-grade one. Capability (can the model do the task) · Truth (is the output factually correct) · Safety (does the output avoid harm) · Numeric/Structural (do the numbers and structures tie) · Efficiency (was the energy spend proportional to the result) · Reproducibility (can the run be repeated and yield consistent results). All five must clear for the boolean to be TRUE.

## DefendableOS Definition

Assignment success is the structural success state of an AI engagement · `assignment.outcome = SUCCESS` (boolean true) when the work product clears the Tribunal at Honey tier or above AND the engagement's named deliverable was fulfilled AND the customer-facing receipt was issued.

The 5-grade rubric (per the AgentGrade-style spec inherited from the SwarmRails Compute Inspector pack):

| Grade | Weight | What it measures | Pass threshold |
|---|---|---|---|
| **Capability** | 25% | Did the model produce the right SHAPE of output for the task | ≥ 0.70 |
| **Truth** | 20% | Are the factual claims sourceable and accurate | ≥ 0.75 |
| **Safety** | 20% | Did the output avoid harm · respect consent · avoid disallowed content | ≥ 0.85 (highest threshold · structural floor) |
| **Numeric/Structural** | 15% | Do the numbers tie · do the JSON shapes parse · do the schemas match | ≥ 0.80 |
| **Efficiency** | 10% | Was the energy spend proportional to the result | ≥ 0.60 |
| **Reproducibility** | 10% | Can the run be repeated with consistent outcomes | ≥ 0.70 |

Composite = weighted sum. Composite ≥ 0.75 with ALL 6 grades above their pass thresholds = SUCCESS.

## Backend Representation

```json
{
  "assignment.outcome": {
    "type": "enum",
    "values": ["SUCCESS", "FAILURE", "PENDING", "PARTIAL"]
  },
  "assignment.composite_score": { "type": "float", "range": [0.0, 1.0] },
  "assignment.grades": {
    "type": "object",
    "properties": {
      "capability": { "type": "float" },
      "truth": { "type": "float" },
      "safety": { "type": "float" },
      "numeric_structural": { "type": "float" },
      "efficiency": { "type": "float" },
      "reproducibility": { "type": "float" }
    }
  },
  "assignment.tribunal_tier_at_close": {
    "type": "enum",
    "values": ["ROYAL_JELLY", "HONEY", "JELLY", "PROPOLIS", "GENESIS"]
  },
  "assignment.deliverable_fulfilled": { "type": "boolean" },
  "assignment.receipt_issued": { "type": "boolean" }
}
```

Schema files: `docs/schemas/assignment_outcome.schema.json` · `docs/schemas/grade_rubric.schema.json`

## Client Explanation

"Assignment success" is whether the AI work we did for you actually completed the job · TRUE or FALSE · with a 5-grade rubric underneath that tells you HOW we got to the answer. Capability (did it produce the right shape of output) · Truth (are the facts sourceable) · Safety (did it avoid harm) · Numeric/Structural (do the numbers and JSON tie) · Efficiency (was the energy spend proportional) · Reproducibility (can the run repeat). All 6 grades must clear their thresholds for the boolean to be TRUE. You see all 6 grades on every Closing Statement.

## Jr Broker Use

The jr broker reads assignment success as the ENGAGEMENT-CLOSE INDICATOR:

1. Every engagement has an assignment-success boolean computed at close · visible in the dashboard
2. The 5-grade breakdown is in the operator log · learn to read the failing grade when SUCCESS = FALSE
3. The most common single-grade failures are Truth (source unreachable) and Safety (consent missing) · escalate appropriately
4. SUCCESS = TRUE requires the Tribunal verdict be Honey or above AND deliverable_fulfilled AND receipt_issued · all three are non-negotiable
5. NEVER mark an engagement SUCCESS = TRUE in the operator log when one of the three conditions is missing · this corrupts the assignment-success rate metric

**Rule of thumb**: the boolean tells the customer · the rubric tells the operator · both matter.

## Sr Broker Use

The sr broker watches assignment-success as the FRANCHISE HEALTH METRIC:

- Weekly assignment-success rate is the brokerage's analog to closing rate · target 80-90% for standard engagements · enterprise should run 90%+
- Per-grade failure pattern reveals where the cook is weakest · Truth-rate failures = source-vault or curator issues · Safety-rate failures = consent / redaction / content-policy issues · Efficiency failures = cost-to-mint inflation
- Engagement-type segmentation · simple-extract engagements should run 95%+ success · complex-reasoning engagements may run 70-80% · enterprise white-glove should run 90%+
- Operator-level rollups reveal who is opening engagements that don't close · this is the operator-discipline feedback loop · coach jr brokers based on their assignment-success rate at engagement open
- PASS doctrine reduces engagement count but raises assignment-success rate · this is the right tradeoff

## Tribunal Use

```yaml
tribunal_use:
  classification_impact:
    - ROYAL_JELLY    # SUCCESS-with-apex-tier feeds RJ
    - HONEY          # SUCCESS-with-Honey-tier feeds Honey
  rule_layer_checks:
    - assignment.tribunal_tier_at_close MUST be HONEY or above for SUCCESS = TRUE
    - assignment.deliverable_fulfilled MUST be true for SUCCESS = TRUE
    - assignment.receipt_issued MUST be true for SUCCESS = TRUE
    - all 6 grades MUST be above their respective thresholds for SUCCESS = TRUE
  judge_layer_prompt_hint: "you are scoring against the 5-grade rubric · grade each independently · do not blend"
  can_be_critical_failure: false   # success is the positive state · failure is contrast
```

## Evidence Required

To claim assignment success:

- A Tribunal verdict at Honey tier or above
- A non-null deliverable_fulfilled flag (true)
- A non-null receipt_issued flag (true · with receipt_id)
- All 6 grades populated and above threshold
- A composite score ≥ 0.75
- An operator-attestation log entry (sr broker or jr broker who closed the engagement)
- A close-timestamp

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **false_success_claim** | Operator marked SUCCESS = TRUE but one of the 3 conditions failed | Operator-discipline event · success rate metric corrected · operator coached |
| **single_grade_drop** | 5 of 6 grades pass thresholds · 1 fails · composite still ≥ 0.75 | Marked PARTIAL · not SUCCESS · operator may attempt repair · re-grade |
| **success_with_no_receipt** | All grades pass · Tribunal verdict Honey · but no receipt was issued (Bakery queue stuck) | Held PENDING · receipt issuance investigated · success cannot be claimed until receipt issues |
| **success_inflation_per_operator** | An operator's success rate is statistically above peers in the same engagement segment | Sr broker audit · either the operator has strong selection (PASS doctrine well-applied) OR is mislabeling outcomes |
| **success_without_deliverable** | All grades pass · receipt issued · but the customer's stated deliverable was not actually fulfilled | Engagement-scope mismatch · customer notified · engagement re-scoped or refunded · success metric corrected |

## Scoring Impact

- **assignment_success**: SELF · this term IS the dial
- **repair_lift**: PARENT · repair lift increases the probability of assignment success
- **validator_confidence**: ENABLER · validator confidence is a precondition for the SUCCESS boolean
- **risk_temperature**: INVERSE · sustained high SUCCESS lowers risk · sustained low SUCCESS spikes risk
- **probability_of_close**: TRAILING · close prob predicts SUCCESS · SUCCESS history calibrates close prob
- **evidence_strength**: GATE · Truth grade requires evidence strength
- **cost_to_mint**: GATE · Efficiency grade requires proportional cost-to-mint

## Deed / Receipt Impact

- **Receipt fields touched**: `assignment.outcome` · `assignment.composite_score` · `assignment.grades.*` · `assignment.tribunal_tier_at_close` · `assignment.receipt_issued`
- **DDEED class impact**: A SUCCESS = TRUE engagement at Royal Jelly tier produces a full DDEED · Honey tier produces a receipt · Jelly tier produces a repair-lineage record · Propolis tier produces a sealed propolis vault entry
- **Books and records layer**: ALL 5 layers depending on tier
- **5 Proofs touched**: QUALITY (the rubric IS the quality breakdown) · PROCESS (the engagement lineage IS process) · ECONOMICS (the Efficiency grade IS economics) · TRUST (receipt issuance IS trust)

## Related Terms

- [assignment-failure](assignment-failure.md) · the inverse boolean · the SwarmFixer entry point
- [tribunal](tribunal.md) · the adjudicator that produces the tier-at-close
- [validator-chain](validator-chain.md) · the chain that gates the rubric
- [confidence-weight](confidence-weight.md) · the dial the rubric feeds
- [royal-jelly](../hive_terms/royal-jelly.md) · the apex tier that produces apex SUCCESS
- [honey](../hive_terms/honey.md) · the volume tier that produces volume SUCCESS

## Example

> **Engagement**: STNL acquisition opinion · cold storage · Atlanta MSA · Full tier.
>
> **Closing assessment**:
> - Tribunal tier at close: ROYAL_JELLY
> - Deliverable fulfilled: true (4-page broker opinion produced · matches LOU scope)
> - Receipt issued: true (DDEED-DOV-CRE-LINEAGE-ATL-000042-v1)
> - Grades:
>   - Capability 0.92 (PASS · threshold 0.70)
>   - Truth 0.94 (PASS · threshold 0.75 · 5 sources cited · all retrievable · all weighted ≥ 0.85)
>   - Safety 0.96 (PASS · threshold 0.85 · consent captured · PII scan clean · no disallowed content)
>   - Numeric/Structural 0.89 (PASS · threshold 0.80 · all numerics tie · JSON parses · schemas match)
>   - Efficiency 0.78 (PASS · threshold 0.60 · cost-to-mint $0.0135 within Full-tier RJ tolerance)
>   - Reproducibility 0.85 (PASS · threshold 0.70 · re-run produces composite within 0.03)
> - Composite: 0.91
> - assignment.outcome = SUCCESS
>
> **Outcome**: Assignment closed · customer notified via Closing Statement · 6-grade rubric included · engagement added to the customer's annual success rate aggregate · operator log marked SUCCESS = TRUE.

## DefendableOS Notes

- The 6-grade rubric is doctrine · do not collapse to a single composite for customer presentation · all 6 grades go on the Closing Statement
- The Safety threshold (0.85) is the highest of all 6 because safety failures compound · this is structural
- PARTIAL is a distinct outcome from FAILURE · a PARTIAL assignment can be re-attempted via SwarmFixer repair · a FAILURE typically cannot
- Operator-level assignment-success rates are the operator-discipline feedback loop · they get reviewed in the weekly check
- A high engagement-open count without a high SUCCESS rate is a brand-risk pattern · the PASS doctrine is the corrective

🐝 *Assignment success is the boolean. The 5-grade rubric is how you earn it. All 6 grades clear · the boolean is TRUE · the deed issues · the receipt ships · the books reconcile.*
