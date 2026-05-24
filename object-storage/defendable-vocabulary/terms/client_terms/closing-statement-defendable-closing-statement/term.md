# Closing Statement (Defendable Closing Statement)

## Street Definition

"Did the closing statement land?" — the founder asks the sr broker on the Friday after any assignment milestone.

A **Defendable Closing Statement** is the formal post-assignment report · the HUD-1 equivalent for an AI defense engagement. It states the boolean outcome · the 5-grade breakdown · the variance vs contract · the cost-to-mint actual vs ceiling · the deed list · the Hedera proofs. One document. All the math. Walked with the principal in person.

If the principal didn't get a Defendable Closing Statement at the end of an assignment · the assignment didn't close. The statement IS the close.

## CRE Operator Meaning

In CRE · the HUD-1 (now the ALTA Settlement Statement) is the document that records every dollar that changed hands at the closing table. Buyer credits · seller credits · proration of taxes · title insurance · escrow · transfer tax · brokerage commission · everything. It's signed by both sides. It's filed with the closing agent. It's archived for 7+ years.

The HUD-1 is the only artifact that survives the closing table. The closing agreement gets filed. The deed gets recorded. But the HUD-1 is the line-item truth · the document a CFO can pull 5 years later when the auditor asks "exactly how was this trade economically structured?"

We mirror that exactly. The Defendable Closing Statement is the HUD-1 of an AI assignment. Same discipline. Same archival standard. Same survivability.

## DefendableOS Definition

A **Defendable Closing Statement** in DefendableOS is the formal closing artifact issued at the conclusion of every assignment (regardless of outcome · including FAILED · DARK). It is:

- A deed of its own (`DDEED-{org}-{vertical}-{customer}-CLOSE-{seq}-v1`)
- Anchored on Hedera HCS · ENS-resolvable
- Signed by sr broker · countersigned by founder on T3/T4 tiers
- Walked with the principal in a scheduled 30-minute session (NEVER emailed-and-ghosted)
- Permanently filed in books-and-records · 7-year retention beyond engagement termination

The closing statement has 8 mandatory sections:

1. Boolean outcome (CLOSED · HONEY / CONDITIONED / FAILED · RECOVERABLE / FAILED · DARK)
2. 5-grade breakdown (G1-G5 with weights and composite)
3. Variance vs success criteria (per criterion · numeric)
4. Cost-to-mint actual vs ceiling (per-deed average · monthly total · variance)
5. Deed inventory (count by tier · with sample Hedera anchors)
6. Repair history (if any · with repair-lift evidence)
7. Failure deeds (if any · with root-cause + remediation status)
8. Next-step recommendation (next-assignment proposal OR graceful-exit doc)

## Backend Representation

```json
{
  "closing_statement.closing_id": {"type": "string", "primary_key": true},
  "closing_statement.assignment_id": {"type": "string", "fk": "assignment.assignment_id"},
  "closing_statement.engagement_id": {"type": "string", "fk": "engagement.engagement_id"},
  "closing_statement.deed_id": {
    "type": "string",
    "pattern": "DDEED-.+-CLOSE-[0-9]+-v[0-9]+"
  },
  "closing_statement.boolean_outcome": {
    "type": "enum",
    "values": ["CLOSED_HONEY", "CLOSED_CONDITIONED", "FAILED_RECOVERABLE", "FAILED_DARK"]
  },
  "closing_statement.composite_score": {"type": "float", "range": [0,1]},
  "closing_statement.g1_outcome": {"type": "float", "range": [0,1]},
  "closing_statement.g2_truth": {"type": "float", "range": [0,1]},
  "closing_statement.g3_safety": {"type": "float", "range": [0,1]},
  "closing_statement.g4_economics": {"type": "float", "range": [0,1]},
  "closing_statement.g5_defensibility": {"type": "float", "range": [0,1]},
  "closing_statement.criteria_variance": {
    "type": "jsonb_array",
    "shape": "[{criterion, target_value, actual_value, variance_pct, passed}]"
  },
  "closing_statement.cost_actual_per_deed_usd": {"type": "float"},
  "closing_statement.cost_ceiling_per_deed_usd": {"type": "float"},
  "closing_statement.cost_variance_pct": {"type": "float"},
  "closing_statement.deed_count_honey": {"type": "integer"},
  "closing_statement.deed_count_jelly": {"type": "integer"},
  "closing_statement.deed_count_propolis": {"type": "integer"},
  "closing_statement.failure_deed_ids": {"type": "string_array", "nullable": true},
  "closing_statement.principal_walk_scheduled_at": {"type": "timestamp"},
  "closing_statement.principal_walk_completed_at": {"type": "timestamp", "nullable": true},
  "closing_statement.principal_acknowledged": {"type": "boolean"},
  "closing_statement.next_step_recommendation": {
    "type": "enum",
    "values": ["RENEW_SAME_TIER", "UPGRADE_TIER", "DOWNGRADE_TIER", "GRACEFUL_EXIT", "PAUSE_60D"]
  }
}
```

Schema files: `docs/schemas/closing_statement.schema.json`

## Client Explanation

The **Defendable Closing Statement** is your formal report at the end of every assignment. Think of it as the HUD-1 of AI defense work. One document. All the math.

It reports:

- The boolean outcome (we either CLOSED · HONEY · CONDITIONED · FAILED · RECOVERABLE · or FAILED · DARK · no soft language)
- The 5-grade breakdown · why we landed where we landed
- Variance vs every success criterion you contracted for · numeric · per-criterion
- The cost-to-mint actual vs the ceiling in your LOU
- The deed inventory · how many we issued · at what tier · with verifiable Hedera anchors
- Any failures we recorded · with root cause and remediation status
- A recommendation for next steps (next assignment · upgrade · downgrade · or graceful exit)

The sr broker walks you through it in person · NEVER just emails the PDF. The walk is the close · not a courtesy.

You acknowledge the closing statement in writing. The signed acknowledgment is the proof you saw what we said happened. Both stay in your engagement folder for 7 years after the LOU terminates.

## Jr Broker Use

When an assignment is approaching its expected close date:

- **Pre-flight the closing statement 14 days before close-date**. The sr broker drafts · you support data-pull · QA validator reviews · founder reviews on T3/T4.
- **Verify the Hedera anchors for every deed referenced**. The statement cites them · they must resolve · or the statement is non-defensible.
- **Coordinate the principal-walk meeting** (60-min on T3/T4 · 30-min on T2 · written ack on T1).
- **Track the principal acknowledgment** within 7 days of the walk. If no ack within 14 days · escalate to sr broker · this is a relationship signal.
- **File the closing statement as a deed** · trigger the Hedera anchor pipeline · confirm the deed lands within 24 hours of last signature.

## Sr Broker Use

The sr broker:

- **Drafts the closing statement personally** · the QA validator reviews but does not draft (drafting is a relationship act · not a process act)
- **Walks the statement with the principal personally** · no delegation on T2/T3/T4 tiers
- **Owns the boolean outcome decision** · subject to QA validator audit (the QA validator can flag a misrepresented boolean but cannot override)
- **Authors the next-step recommendation** · with founder review on any RENEW_SAME_TIER → UPGRADE_TIER or any GRACEFUL_EXIT
- **Files the principal ack** in books-and-records · triggers the post-close cadence shift (assignment archives · next-assignment opens or engagement enters renewal countdown)

The sr broker also owns the **post-close relationship pulse** · a 30-day check-in after every close · regardless of outcome · to capture qualitative feedback and re-confirm the relationship trajectory.

## Tribunal Use

The Tribunal feeds the closing statement directly:

- `composite_score` is the rollup of all under-assignment Tribunal verdicts
- `g1` through `g5` are computed from the assignment's Tribunal verdict distribution
- `deed_count_honey/jelly/propolis` are direct Tribunal-classification counts
- The boolean outcome is RULE-LAYER applied (G3 < 0.70 OR critical Propolis → FAILED regardless of composite)

The QA validator (SH6) is the human audit on the Tribunal output before the statement publishes. The QA validator can FLAG (not override) any boolean that doesn't tie to the underlying math.

## Evidence Required

For a closing statement to be defensible:

- Every cited deed must resolve on Hedera HCS
- Every success criterion variance must be re-derivable from books-and-records
- Cost-to-mint actual must match the rolling 30-day average in the dashboard
- Principal walk must be scheduled (not just emailed) · meeting confirmation captured
- All 5 grades must be present with weights and composite math shown
- Failure deeds (if any) must be linked with root-cause analysis attached

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **boolean_padding** | Closing statement reports HONEY when composite is 0.71 (CONDITIONED territory) | PROPOLIS · trust breach · founder review |
| **silent_close** | Closing statement emailed without scheduled walk · principal-walk skipped | PROPOLIS · trust breach · re-walk required |
| **stale_dashboard** | Cost-to-mint reported on statement doesn't match rolling 30-day in dashboard | JELLY · re-derive · re-issue with corrected numbers |
| **failure_minimization** | Critical Propolis under-named · root cause downplayed | PROPOLIS · founder review · re-issue with honest framing |
| **missing_acknowledgment** | Statement issued · principal never acknowledged · cadence shift proceeded anyway | JELLY · ack chased · escalation if > 14 days |
| **deed_inventory_mismatch** | Statement cites deed count that doesn't match books-and-records | PROPOLIS · audit failure · QA validator review |

## Scoring Impact

- **assignment_success**: SELF (the closing statement IS the assignment success report)
- **repair_lift**: HIGH (clean closing statements with named failures + remediation become repair-training corpus)
- **validator_confidence**: HIGH (the statement is the validator's final artifact)
- **risk_temperature**: INVERSE (well-walked statement = low engagement risk · skipped walk = elevated risk)
- **probability_of_close**: INDIRECT (a series of clean HONEY closings raises the next assignment's opening dial · failure closings lower it)
- **evidence_strength**: HIGH (closing statement is engagement-level evidence stack of the highest grade)
- **cost_to_mint**: NEUTRAL (statement drafting cost is operator margin · amortized)

## Deed / Receipt Impact

- **Receipt fields touched**: every under-assignment receipt is referenced (or sampled) by the statement
- **DDEED class impact**: the closing statement IS a DDEED · with all 5 Proofs · same as any other deed
- **Books and records layer**: all 5 layers · 7-year retention beyond engagement termination
- **5 Proofs touched**: ALL FIVE · same as any other DDEED · with the additional Process-proof being the assignment lineage from brief to close

## Related Terms

- [assignment](assignment.md) · the unit the closing statement closes
- [engagement](engagement.md) · the canopy the closing statement rolls up to
- [letter-of-understanding](letter-of-understanding.md) · the contract the closing statement reports vs
- [principal](principal.md) · the audience for the walk
- [morning-brief](morning-brief.md) · the daily cadence that precedes and follows the closing
- [assignment-success](../scoring_terms/assignment-success.md) · the scoring framework the statement reports
- [pre-market-flight-sheet](pre-market-flight-sheet.md) · the pre-engagement document the closing statement closes the loop on

## Example

> **Closing Statement**: `DDEED-DOV-LOGISTICS-ACME-CLOSE-0001-v1`
>
> **Assignment**: `ASN-0001` (refund-decision agent · 6-month assignment)
>
> **Issued**: 2026-09-18 · walked with principal 2026-09-20 · acknowledged 2026-09-22
>
> **Boolean Outcome**: **CLOSED · HONEY**
>
> **5-Grade Breakdown**:
> - G1 Outcome (30%): 0.93 (Honey rate 94.1% · target 92% · 102% to plan)
> - G2 Truth (25%): 0.91 (Tribunal Truth-class pass 91.4% on sampled cohort)
> - G3 Safety (20%): 1.00 (zero Propolis · 17/17 adversarial pack passing)
> - G4 Economics (15%): 0.88 (cost-to-mint $0.0051/decision · target $0.011 · 46% under target)
> - G5 Defensibility (10%): 0.95 (all deeds Hedera-anchored · all 5 Proofs complete · 97 of 102 audit-spot-check passes)
> - **Composite**: 0.30·0.93 + 0.25·0.91 + 0.20·1.00 + 0.15·0.88 + 0.10·0.95 = **0.925**
>
> **Criteria variance**:
> - "Honey rate ≥ 92% on ≥ 1,200 decisions/mo by 2026-09-15": 94.1% on avg 1,387/mo → PASSED (+2.3% over target)
> - "Zero Propolis events on adversarial pack": 0 events / 17 cases → PASSED
> - "Cost-to-mint ≤ $0.011/decision": $0.0051 actual → PASSED (54% under target)
> - "Validator chain critical pass ≥ 95%": 100% actual → PASSED
>
> **Cost-to-mint summary**:
> - Actual avg: $0.0051/deed
> - Ceiling (T3): $0.0416/deed
> - Variance: 87.7% under ceiling
> - Monthly totals · 6 months: $42,180 total cost · $52,800 invoiced at floor · margin gap is operator margin
>
> **Deed inventory**:
> - HONEY: 7,832 · JELLY: 489 · PROPOLIS: 0 (8,321 total)
> - All deeds Hedera-anchored on topic 0.0.10291838 · ENS-resolvable
>
> **Failure deeds**: none issued
>
> **Next-step recommendation**: UPGRADE_TIER to T3+ with custom validator chain for Q4 · scoped at QBR · go-live 2026-09-25.

## DefendableOS Notes

- The closing statement is the relationship's report card · not the broker's. We name truth · including ours. CONDITIONED is CONDITIONED. FAILED is FAILED. Honesty earns the next decade · spin loses the next quarter.
- The walk is the close. Email-and-ghost on a closing statement is one of the highest-severity trust breaches in the operating model. The QA validator audits walk-discipline.
- Closing statements are also marketing artifacts (sanitized). Aggregated · they prove the apparatus. "47 closings · 39 HONEY · 6 CONDITIONED · 2 FAILED · 100% receipted · 100% Hedera-anchored" is the strongest competitive moat in the category.
- The 7-year retention beyond LOU termination is the difference between a vendor and an insurance company. We're building toward the insurance-company posture · because that's what ownership trusts.

🐝 *The closing statement is the truth. The truth is the receipt. The receipt is the next listing.*
