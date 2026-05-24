# Jelly

> *"Jelly is where the value is. The deal didn't close · but it's a workout · and the workout is the school. Every Jelly pair is a SwarmFixer paycheck waiting to be earned."*
> — Founder · on why he wouldn't trade the Jelly tier for a higher Honey rate

## Street Definition

"That one came back Jelly · route it." Jelly is the recoverable-failure tier. The pair scored too low to ship · failed a fixable check · or showed a workout angle the auto-judges flagged · and now it sits in `pair-candidates/jelly-repaired/` waiting for SwarmFixer to take a swing. After repair · the pair gets re-Scouted into the Tribunal as a fresh PairCandidate (with a `repair_lineage` pointer back to the original) · re-graded · and most of the time it lands Honey on the second pass.

In CRE language · Jelly is the Class C asset with a workout angle. Deferred maintenance. Below-market rents. Tenant vacancy. Whatever the problem is · the problem is FIXABLE · and the lift from the fix is what the value-add buyer pool pays for. Same here. Jelly is the workout pile. The most valuable training data the Hive produces · because the BEFORE / AFTER pair is the gold for the next SwarmFixer cohort.

## CRE Operator Meaning

In CRE · Jelly is the value-add play · the Class C-with-an-angle · the building with deferred maintenance that a sponsor can take down at a 7-cap · pump $4M into the roof and the HVAC · re-tenant at market · and exit at a 6-cap on the trended NOI. The deal doesn't pencil on day one · it pencils on the workout. The buyer pool is different (value-add funds · not core institutional) but the buyer pool exists · and the cap rate spread between Class C entry and Class B exit is the broker's value-add.

Inside DefendableOS · Jelly is identically structured. The AI work product didn't clear the Honey threshold · but the failure mode is named · the failure is recoverable · SwarmFixer (the 5-task RJ pipeline · DIAGNOSE / REPAIR / PREVENT / DETECT / COMPARE) takes the pair · produces a repair · the repaired pair re-enters the Tribunal · and the lift gets MEASURED.

The repair lift is the dial. The dial is the asset. Jelly is what makes the dial move.

## DefendableOS Definition

Jelly is the third Tribunal tier · `tribunal_label = JELLY` · typically JellyScore 0.50-0.69 with a NAMED recoverable failure mode. The pair did not clear Honey but did not trip a critical-fail that would force it to Propolis. The failure mode falls into one of the 7 SwarmJelly failure-class buckets:

- missing_step (reasoning)
- false_assumption (reasoning)
- hallucination (knowledge · NOT the catastrophic kind · the recoverable kind where the fact CAN be sourced)
- overgeneralization (knowledge)
- drift (instruction-following)
- schema_break (instruction-following · NOT the catastrophic C12 secret-leak kind · the recoverable JSON-format kind)
- tool_misuse (agent)

Jelly is the EXPLICIT repair lane. It is what feeds SwarmFixer. It is what produces the BEFORE / AFTER training pairs that train the NEXT SwarmFixer cohort. Jelly is the flywheel.

## Backend Representation

```json
{
  "tribunal_verdict.tier": {
    "type": "enum",
    "values": ["ROYAL_JELLY", "HONEY", "JELLY", "PROPOLIS"]
  },
  "tribunal_verdict.failure_mode": {
    "type": "enum",
    "values": ["missing_step", "false_assumption", "hallucination", "overgeneralization", "drift", "schema_break", "tool_misuse"],
    "nullable_when": "tier != JELLY"
  },
  "pair_candidate.repair_lineage": {
    "type": "string",
    "description": "pointer to the original pair this is a repair of (null for first-pass)"
  },
  "repair_lift.delta_score": {
    "type": "float",
    "range": [-1.0, 1.0],
    "scoring_hook": "repair_lift_v1"
  },
  "repair_lift.from_tier": { "type": "enum" },
  "repair_lift.to_tier": { "type": "enum" }
}
```

Schema files: `docs/schemas/tribunal_verdict.schema.json` · `docs/schemas/pair_candidate.schema.json` · `docs/schemas/repair_lift.schema.json`

## Client Explanation

"Jelly" is our recoverable-failure tier · the AI work product that did not clear our production-safe threshold but showed a named failure mode that our SwarmFixer pipeline can repair. We do not ship Jelly to you. We route it to repair · re-grade the repaired output · and ship the result (usually as Honey · sometimes as Royal Jelly) along with the lift report showing the repair worked. The lift report is your audit trail that says "we caught the problem · we fixed it · here's the before-and-after." Most AI vendors throw away their failures. We make a flywheel out of them.

## Jr Broker Use

When a pair comes back tagged JELLY:

1. Confirm the `failure_mode` field is populated (one of the 7 SwarmJelly classes) · if it is null · the Tribunal verdict is incomplete · escalate
2. Confirm the pair routed into the `pair-candidates/jelly-repaired/` queue within 5 minutes
3. Watch the repair queue depth · if it climbs above 500 · escalate to the rig owner (SwarmFixer is on whale:11434 · check it is alive)
4. When the repaired pair comes back with a fresh verdict · log the BEFORE / AFTER scores in the repair_lift report
5. If the repair lift is < 0.05 (basically no improvement) · the repair failed · the pair should be re-routed to a second repair attempt OR sealed as Propolis after the second failure
6. Do NOT ship Jelly to customers · the customer sees the repaired output (Honey or Royal Jelly) with the lift report attached

**Rule of thumb**: Jelly is in-process inventory · not finished goods. It gets repaired before it ships.

## Sr Broker Use

The sr broker watches Jelly as a HEALTH METRIC for the cook upstream:

- Healthy Jelly % is 10-20% of total volume · this is the repair flywheel running normally
- If Jelly is over 25% · the cook is producing systematic failures · audit the curator settings · check temperature (should be 0.05) · check the prompt domain pack
- If Jelly is under 5% · either the cook is exceptional OR the judges are being too lenient (Jelly that should have been Propolis is leaking into Honey) · run a sample audit
- Track repair lift over time · the WEEKLY MEAN repair lift across all Jelly-to-Honey transitions is the SwarmFixer health score · trending down means SwarmFixer is degrading and needs a re-cook
- Apply the PASS doctrine · if a Jelly pair is from an engagement we should not have opened · do NOT route to repair · seal as Propolis with `operator_pass_doctrine` annotation
- The most valuable Jelly pairs are the ones with the LARGEST repair lift · those are the ones that go into the NEXT SwarmFixer training cohort with the highest weight

## Tribunal Use

```yaml
tribunal_use:
  classification_impact:
    - JELLY      # this term IS the Jelly tier
  rule_layer_checks:
    - C01: pair record present (MUST PASS · else PROPOLIS)
    - C02: source artifact referenced (MUST PASS · else PROPOLIS)
    - C03: source retrievable (MAY FAIL · routes to source-refresh repair within Jelly · does NOT force Propolis)
    - C04: tribunal label assigned (MUST be JELLY)
    - C05: no hard-fail flagged (MUST PASS · the recoverable hallucination class is C05-clear · catastrophic hallucination is C05-fail and that is PROPOLIS)
    - C06: trivially clears (Jelly is not promotion)
    - C07: holdout contamination guard (MUST PASS · zero tolerance same as all tiers)
  judge_layer_prompt_hint: "score this pair on the 5-component JellyScore · identify the named failure mode · this pair will be routed to repair"
  can_be_critical_failure: false   # Jelly is recoverable · contrast Propolis which is critical
```

The Tribunal assigns Jelly when the score lands in the 0.50-0.69 range AND a named SwarmJelly failure mode is identified AND no critical-fail (C01, C02, C04, C05 hard-fail variant, C06, C07) fires. The judge layer is allowed to flag a failure mode based on its reasoning · the rule layer then confirms the mode is in the 7-class taxonomy and routes accordingly.

## Evidence Required

To assign Jelly · the verdict record must include:

- The original PairCandidate (well-formed)
- A NAMED `failure_mode` field (one of 7 SwarmJelly classes)
- Both judge reasons (Scale A AND Scale B) with raw scores in the 0.50-0.69 band (with allowance for one judge slightly higher if drift ≤ 0.15)
- SHA-256 record_hash
- A routing decision (which `pair-candidates/jelly-repaired/` lane the pair was placed in)
- After repair · the `repair_lift.delta_score` must be computed and logged

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **unnamed_failure_jelly** | Pair lands Jelly score but no failure_mode named · cannot route to repair | Held for sr broker to name the mode OR force to Propolis |
| **repair_lift_negative** | SwarmFixer produced a repair that scored LOWER than the original · the repair made it worse | Pair sealed as Propolis after second attempt · the failure mode added to next SwarmFixer training corpus with high weight |
| **two_failed_repairs_jelly** | Same pair routed to repair twice · both repairs failed to lift to Honey | Sealed as Propolis · the failure mode is structurally hard for the current SwarmFixer cohort · feeds next cohort training |
| **jelly_promoted_without_repair** | Operator tries to promote Jelly to Honey without an actual repair lift | Operator-discipline event · pair stays Jelly · misrep logged · escalated |
| **stale_jelly_in_queue** | Jelly pair sits in repair queue > 24h without a repair attempt | Operator alert · investigate SwarmFixer rig health · sometimes the queue is healthy and just deep |

## Scoring Impact

- **assignment_success**: PENDING · Jelly is in-process · success is measured AFTER repair
- **repair_lift**: PRIMARY DRIVER · this is where the repair lift metric LIVES · the BEFORE-AFTER delta is the dial
- **validator_confidence**: MEDIUM · the chain cleared the critical checks but the score is below production-safe
- **risk_temperature**: MEDIUM-HIGH · Jelly carries risk that the repair will not lift OR will leak Propolis-quality output into Honey if operators get sloppy
- **probability_of_close**: TBD until repair · post-repair behaves as Honey or Royal Jelly · pre-repair is not closeable
- **evidence_strength**: PRESENT but insufficient for Honey · usually a missing source · a recoverable schema break · a fixable reasoning gap
- **cost_to_mint**: ELEVATED · Jelly carries the cost of the original pair PLUS the SwarmFixer repair compute · ~$0.01-$0.015/pair before the repaired output ships as Honey or Royal Jelly

## Deed / Receipt Impact

- **Receipt fields touched**: `tier=JELLY` · `failure_mode` · `repair_lineage` (when repaired) · `repair_lift.delta_score` (when repaired) · `repair_lift.from_tier` · `repair_lift.to_tier`
- **DDEED class impact**: Jelly does NOT issue a deed directly · the REPAIRED pair (now Honey or Royal Jelly) issues the deed · with the original Jelly pair referenced in `repair_lineage` for full lift audit
- **Books and records layer**: L1 PG · L2 Merkle (the failure pair is logged in batch Merkle even pre-repair · the repair lift is also logged) · L3 NAS
- **5 Proofs touched**: PROCESS (the failure lineage is the asset) · QUALITY (the named failure mode IS the quality signal) · ECONOMICS (the repair cost is logged)

## Related Terms

- [honey](honey.md) · the tier Jelly aspires to via repair lift
- [royal-jelly](royal-jelly.md) · the apex tier Jelly occasionally lifts to (rare but documented)
- [propolis](propolis.md) · the tier Jelly falls to after a failed repair · the lineage continuation
- [hive](hive.md) · the system that grades Jelly
- [tribunal](../tribunal_terms/tribunal.md) · the adjudicator that assigns the Jelly verdict and the failure mode

## Example

> **Engagement**: AVO opinion request on a small office portfolio (3 properties · suburban Atlanta).
>
> **AI work product (first pass)**: SwarmCRE-9B produced a 3-page opinion · the cap-rate analysis was solid · but the tenant-credit walk cited a 10-K that was from the WRONG fiscal year (drift failure mode · the model used the FY2024 10-K when the FY2025 was available).
>
> **Tribunal run**: TRIB-20260524T103044Z-9b21
> - Validator chain · all 7 critical PASS · C03 source-retrievable PASS (the wrong-year 10-K WAS retrievable · the issue is staleness · advisory)
> - Scale A score 0.62 · reason "cap rate analysis solid · tenant credit walk used stale FY2024 10-K · FY2025 available · drift failure"
> - Scale B score 0.65 · reason "structure clean · drift on the tenant credit source · recoverable"
> - JellyScore 0.635 · tier JELLY · failure_mode = drift
>
> **Routed**: `pair-candidates/jelly-repaired/drift/` · SwarmFixer queue
>
> **SwarmFixer repair** (whale:11434 · SwarmJelly-4B):
> - DIAGNOSE · "tenant credit source cites FY2024 10-K · FY2025 filed 2026-03-12 · source drift"
> - REPAIR · "re-fetch FY2025 10-K · re-run tenant credit walk with current debt schedule"
> - PREVENT · "add validator check · 10-K citation must be within 12 months of engagement open date"
> - DETECT · "POSITIVE · drift present · confidence 92"
> - COMPARE · "repaired output scored higher on numeric_verify and source_confidence"
>
> **Re-grade**: TRIB-20260524T104511Z-9b22 · Scale A 0.81 · Scale B 0.83 · JellyScore 0.82 · tier HONEY · `repair_lift.delta_score = +0.185`
>
> **Outcome**: Honey opinion shipped to the customer with repair lift report attached. The original Jelly pair · the 5-task RJ output · and the repaired Honey pair all entered the SwarmFixer v3 training corpus · weighted by the +0.185 lift.

## DefendableOS Notes

- Jelly is the most valuable training tier in the Hive · the BEFORE/AFTER pair is what trains the next SwarmFixer to be better than the current one · this is the flywheel
- The "where most valuable data exists" framing is correct · success doesn't teach the model · failure does · but only when the failure is NAMED and the REPAIR is captured · that combination is uniquely produced in the Jelly tier
- A Jelly pair that does not get repaired within 24h is a Hive failure · not a Jelly failure · escalate to rig ops
- A Jelly pair that survives 2 failed repairs becomes Propolis · the failure mode IS the lesson · the next SwarmFixer cohort gets weighted on it
- The Jelly tier is also why we tell customers we have a FALSIFIABLE quality promise · we do not pretend failure didn't happen · we name it · we repair it · we measure the lift · we ship the result with the lift report attached

🐝 *Jelly is the workout pile. The most valuable training data in the Hive. Don't throw failure away · name it · repair it · measure the lift · ship the result. The flywheel runs on Jelly.*
