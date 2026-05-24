# Assignment Failure

> *"Failure is the entry point to the SwarmFixer. The named failure mode is the lesson. The repaired output is the school. The lift is the asset. Don't throw failure away · operationalize it."*
> — Founder · why we treat failure as inventory

## Street Definition

"That assignment failed · route it." Assignment failure is the inverse of assignment success · the boolean is FALSE · one or more of the 6 rubric grades fell below threshold · the deliverable did not fulfill OR the receipt did not issue OR the Tribunal verdict landed Jelly or Propolis. Failure is NOT the end of the engagement · failure is the entry point to the SwarmFixer repair pipeline · failure is the inventory the next-gen training cohort runs on.

In CRE language · assignment failure is the deal that did not close · the LOI that did not convert to PSA · the engagement that died at the diligence stage. A 30-year broker has more failures than successes · the discipline is what you LEARN from each failure · which broker takes the call back · which customer earns a re-engagement · which seller is on the never-call list. Same here. AI failure is data · IF you operationalize it.

## CRE Operator Meaning

In CRE · assignment failure is the deal-died event · documented · post-mortemed · added to the brokerage's pattern library. A broker who never has a failure is a broker who only takes layups (or who is lying about their pipeline). The discipline is in WHY did it fail · WAS the failure preventable · WHAT do we change going forward. The CRE practice that survives a 30-year career is the one that codifies failure into the next cohort's training.

Inside DefendableOS · assignment failure is identically structured. The failure mode is NAMED (one of 7 SwarmJelly classes when recoverable) · the failure is ROUTED (to repair or seal) · the failure is MEASURED (repair lift if applicable) · the failure is OPERATIONALIZED (feeds the next SwarmFixer cohort training).

## DefendableOS Definition

Assignment failure is `assignment.outcome = FAILURE` when ANY of:

- the Tribunal verdict landed Propolis at close
- one or more of the 6 rubric grades fell below threshold
- the deliverable_fulfilled flag is false
- the receipt_issued flag is false (after a timely retry attempt)
- the operator-applied PASS doctrine sealed the engagement

Assignment failure is the explicit entry point to:

1. **SwarmFixer repair pipeline** · for Jelly-tier failures with named failure modes (the 5-task RJ output · DIAGNOSE / REPAIR / PREVENT / DETECT / COMPARE)
2. **Propolis vault** · for Propolis-tier failures · sealed with full lineage · feeds DETECT-task training for next SwarmFixer cohort
3. **Operator-discipline review** · for failures caused by upstream operator mistakes (engagement-scope drift · onboarding leak)
4. **Cook-audit cycle** · for failures suggesting upstream cook quality problems (judge temp drift · curator setting issues · prompt-domain degradation)

## Backend Representation

```json
{
  "assignment.outcome": {
    "type": "enum",
    "values": ["SUCCESS", "FAILURE", "PENDING", "PARTIAL"]
  },
  "assignment.failure_reason": {
    "type": "enum",
    "values": [
      "tribunal_propolis",
      "tribunal_jelly_repair_failed",
      "grade_below_threshold",
      "deliverable_not_fulfilled",
      "receipt_not_issued",
      "operator_pass_doctrine"
    ]
  },
  "assignment.failure_mode": {
    "type": "enum",
    "values": ["missing_step", "false_assumption", "hallucination", "overgeneralization", "drift", "schema_break", "tool_misuse", "n/a"]
  },
  "assignment.route_to": {
    "type": "enum",
    "values": ["swarmfixer_repair", "propolis_vault", "operator_discipline_review", "cook_audit_cycle"]
  }
}
```

Schema files: `docs/schemas/assignment_outcome.schema.json` · `docs/schemas/failure_routing.schema.json`

## Client Explanation

"Assignment failure" is when the AI work we did for you did not clear our production-safe threshold · we do NOT ship failure to you · we route it to repair · re-grade the repaired output · and ship the result (or, for unrecoverable failures, we acknowledge the failure transparently in the Morning Brief). Every failure has a named failure mode (1 of 7 classes) · the failure mode feeds our SwarmFixer training so the NEXT version of the model catches that failure earlier. Most AI vendors hide their failure rates. We publish ours · because that is the trust signal.

## Jr Broker Use

The jr broker reads assignment failure as the REPAIR-LANE INDICATOR:

1. When an engagement closes with FAILURE · check the `failure_reason` field · the routing decision follows from it
2. Failures with `failure_reason = tribunal_jelly_repair_failed` AND a named `failure_mode` route to SwarmFixer (most common path)
3. Failures with `failure_reason = tribunal_propolis` route to the Propolis vault (no repair attempt)
4. Failures with `failure_reason = operator_pass_doctrine` are operator-sealed · log the reason · respect the seal
5. NEVER · ever · ship a FAILURE output to a customer · this is the brand-protection floor · escalate if uncertain

**Rule of thumb**: failure is inventory · not waste · route it correctly · let the system metabolize it.

## Sr Broker Use

The sr broker watches assignment failure as the SYSTEM HEALTH and FRANCHISE INTEGRITY signal:

- Weekly assignment-failure rate is the inverse of success rate · use both views (success up · failure down OR failure pattern shifts)
- Per-failure-mode distribution reveals upstream issues · sustained `hallucination` failure spike = curator OR judge calibration issue · sustained `schema_break` = prompt-domain or output-parsing issue · sustained `tool_misuse` = agent-design issue
- `failure_reason = receipt_not_issued` failures are operationally distinct · the Tribunal cleared · the Bakery did not · investigate the Bakery write queue
- `failure_reason = operator_pass_doctrine` rate is the OPERATOR DISCRIMINATION dial · should be 2-5% · above 8% means operators are over-PASSing (or under-PASSing if too low)
- A failure that survives 2 repair attempts becomes a Propolis seal with high DETECT-corpus weight · this is the natural escalation

## Tribunal Use

```yaml
tribunal_use:
  classification_impact:
    - JELLY      # most failures land Jelly first · route to repair
    - PROPOLIS   # critical failures or twice-failed repairs land Propolis
  rule_layer_checks:
    - assignment.failure_reason MUST be populated when assignment.outcome == FAILURE
    - assignment.failure_mode MUST be populated when assignment.failure_reason == tribunal_jelly_repair_failed
    - assignment.route_to MUST be populated and consistent with failure_reason
  judge_layer_prompt_hint: "you are scoring against the 5-grade rubric · if any grade falls below threshold · flag the failure mode and the reason"
  can_be_critical_failure: false   # failure is the state · not the cause
```

## Evidence Required

To assign assignment failure:

- A Tribunal verdict (any tier)
- A populated failure_reason
- A populated failure_mode (if recoverable failure)
- A populated route_to
- A grade breakdown showing which grade(s) fell below threshold
- An operator log entry (who closed the engagement with FAILURE · why)
- A close-timestamp

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **failure_unnamed** | Assignment marked FAILURE but no failure_reason set | Operator-discipline event · the failure must be classified to be routable · returned for classification |
| **failure_routed_to_wrong_lane** | failure_reason and route_to don't match doctrine | Operator-discipline event · corrected · operator coached |
| **failure_hidden** | An engagement closed FAILURE but not reported in the failure-rate metric | Integrity event · investigate operator log · escalate to founder |
| **failure_repeat_no_lift** | Engagement re-attempted via SwarmFixer · second attempt also FAILURE with no lift | Promote to Propolis seal · the failure mode is structurally hard for current SwarmFixer · feeds next cohort training with high weight |
| **failure_reported_as_success** | Operator marked SUCCESS but Tribunal verdict was Propolis | Operator-discipline event · success rate corrected · operator coached or removed |

## Scoring Impact

- **assignment_success**: INVERSE · failure is the negative state
- **repair_lift**: ENTRY · failures are the substrate repair lift is measured against
- **validator_confidence**: REDUCED · failure events lower aggregate validator confidence
- **risk_temperature**: ELEVATED · sustained failure rates elevate risk temperature
- **probability_of_close**: REDUCED · failure history lowers close prob for similar future engagements
- **evidence_strength**: VARIABLE · sometimes failure is from weak evidence · sometimes from fabricated-but-strong evidence (adversarial)
- **cost_to_mint**: INCLUDED · failed cooks still consume energy · the cost is logged as the cost of quality discipline

## Deed / Receipt Impact

- **Receipt fields touched**: `assignment.outcome=FAILURE` · `assignment.failure_reason` · `assignment.failure_mode` · `assignment.route_to`
- **DDEED class impact**: A FAILURE engagement does NOT produce a DDEED · it produces a sealed failure record (Propolis vault entry) OR a repair-lineage record (SwarmFixer routing)
- **Books and records layer**: L1 PG (hot) · L2 Merkle (failure hashed into batch root · audit trail preserved) · L3 NAS (propolis vault archive)
- **5 Proofs touched**: PROCESS (failure lineage IS process · what tried what failed what survived) · ECONOMICS (the cost of the failed cook IS published as cost of discipline)

## Related Terms

- [assignment-success](assignment-success.md) · the inverse boolean
- [jelly](../hive_terms/jelly.md) · the tier most failures land in for repair
- [propolis](../hive_terms/propolis.md) · the tier critical failures land in for sealing
- [hallucination-event](hallucination-event.md) · one of the named failure modes
- [tribunal](tribunal.md) · the adjudicator that assigns the failure tier
- [validator-chain](validator-chain.md) · the gate whose critical-fail produces Propolis failures

## Example

> **Engagement**: AVO opinion · 3-property suburban office portfolio · Standard tier.
>
> **First-pass close (FAILURE)**:
> - Tribunal verdict: JELLY
> - Grade breakdown: Capability 0.82 (PASS) · Truth 0.62 (FAIL · threshold 0.75) · Safety 0.91 (PASS) · Numeric/Structural 0.78 (PASS) · Efficiency 0.74 (PASS) · Reproducibility 0.81 (PASS)
> - failure_reason: tribunal_jelly_repair_failed (first attempt · routed to repair)
> - failure_mode: drift (the model cited a stale FY2024 10-K when FY2025 was available)
> - route_to: swarmfixer_repair
>
> **SwarmFixer repair completes · re-Scout · re-judge** · second pass:
> - Tribunal verdict: HONEY · all 6 grades clear
> - assignment.outcome flipped to SUCCESS (PARTIAL retroactively logged for audit)
> - repair_lift.delta_score = +0.185
>
> **Outcome**: First-pass failure produced a Jelly pair with named drift failure mode · SwarmFixer-repaired pair produced a Honey-tier success · the BEFORE/AFTER pair entered the next-generation SwarmFixer training cohort weighted by the +0.185 lift · the customer received the repaired output with a transparent repair-lift report attached.

## DefendableOS Notes

- Failure is inventory · the operating principle is "no waste in a Hive" · every failure has a route
- The 7-failure-mode taxonomy (from SwarmJelly) is the doctrine · do not invent new modes · expand only via Sr Hack 4 review
- Customer-facing failure reporting is in aggregate · we publish the failure rate · we do not ship individual failures
- Operator-PASS failures are distinct from quality-FAIL failures · both go on the failure-rate metric · only quality failures go to repair
- The willingness to publish failure rates is the brand's anti-fantasy mechanism · vendors who hide failure rates are selling vibes · we sell defendable inventory

🐝 *Assignment failure is the entry point to the SwarmFixer. Named the mode · route it · measure the lift. Failure is inventory · not waste · the Hive metabolizes everything.*
