# Assignment

## Street Definition

"What's the assignment?" — the jr broker asks before they walk into the first sit.

An **Assignment** is a specific job within an engagement. It's the work order. The thing with a defined success criterion · a defined deadline · a defined deliverable. One engagement holds many assignments over its life · just as one CRE listing relationship holds many trades over the years.

If an engagement is the listing agreement · an assignment is the individual trade we're working on this quarter. Signed brief. Numeric criteria. Date on the deadline. Owner on the desk. That's an assignment.

If someone can't tell you exactly what they're trying to close · when · and how we'll know we closed it · they don't have an assignment. They have a wish.

## CRE Operator Meaning

A sr broker in CRE thinks in assignments because that's how the pipeline pencils. The sr broker carries 8-15 active assignments at any time · each one with its own dial · its own deadline · its own buyer pool · its own deal physics. The broker's discipline is keeping each one moving forward · re-checking the dial weekly · escalating the ones that drift.

The assignment IS the unit the broker books fees against. The engagement is the relationship · but the engagement doesn't book revenue · the assignments do. Every CRE shop runs a per-broker assignment report every Friday morning: in-flight count · weighted dial total · expected close month · expected fee total · variance to plan.

We mirror that exactly. The Defender's defense-ops desk runs the same Friday Brief · across the assignment book.

## DefendableOS Definition

An **Assignment** in DefendableOS is the specific work order within an engagement · uniquely identified by `assignment_id` of shape `ASN-{seq}` (scoped to its parent engagement). Every assignment has:

- A signed **assignment brief** with numeric · time-bound · auditable success criteria
- A defined start date · expected close date
- A specific agent or agent-fleet it covers
- Its own Probability of Close sub-dial (rolled up into engagement-level dial)
- Its own Tribunal verdict stream feeding the assignment success score
- Its own closing statement at completion (deed `DDEED-{org}-{vertical}-{customer}-CLOSE-{seq}-v1`)

The assignment is the unit of accountability. The sr broker is named on every assignment. The QA validator (SH6) checks every closing statement.

## Backend Representation

```json
{
  "assignment.assignment_id": {
    "type": "string",
    "pattern": "ASN-[0-9]{4}",
    "scoped_to": "engagement_id"
  },
  "assignment.engagement_id": {"type": "string", "fk": "engagement.engagement_id"},
  "assignment.brief_deed_id": {
    "type": "string",
    "pattern": "DDEED-.+-ASN-[0-9]{4}-BRIEF-v[0-9]+"
  },
  "assignment.start_date": {"type": "date"},
  "assignment.expected_close_date": {"type": "date"},
  "assignment.actual_close_date": {"type": "date", "nullable": true},
  "assignment.covered_agents": {"type": "string_array"},
  "assignment.success_criteria": {
    "type": "jsonb_array",
    "shape": "[{criterion, target_value, measurement, deadline}]"
  },
  "assignment.dial_current": {"type": "float", "range": [0,1]},
  "assignment.status": {
    "type": "enum",
    "values": ["DRAFT_BRIEF", "BRIEF_SIGNED", "IN_FLIGHT", "AT_RISK", "DARK", "CLOSING", "CLOSED_HONEY", "CLOSED_CONDITIONED", "FAILED_RECOVERABLE", "FAILED_DARK"]
  },
  "assignment.tribunal_honey_count": {"type": "integer"},
  "assignment.tribunal_jelly_count": {"type": "integer"},
  "assignment.tribunal_propolis_count": {"type": "integer"},
  "assignment.composite_score": {"type": "float", "range": [0,1]},
  "assignment.boolean_outcome": {
    "type": "enum",
    "values": ["CLOSED_HONEY", "CLOSED_CONDITIONED", "FAILED_RECOVERABLE", "FAILED_DARK"]
  },
  "assignment.closing_statement_deed_id": {"type": "string", "nullable": true}
}
```

Schema files: `docs/schemas/assignment.schema.json` · `docs/schemas/assignment_brief.schema.json`

## Client Explanation

An **assignment** is a specific project within our engagement. The engagement is the relationship · the assignment is the work order.

Every assignment we run has a written brief with numeric success criteria · a deadline · and a defined deliverable. We sign it · you sign it · we file it in your engagement folder as a permanent record. When the assignment closes · you get a Defendable Closing Statement that reports the boolean outcome (CLOSED · HONEY / CONDITIONED / FAILED · RECOVERABLE / FAILED · DARK) and the 5-grade breakdown that explains why.

You can have many assignments running in parallel under one engagement · each with its own dial · its own deadline · its own closing. We treat each one with broker-grade discipline · individual attention · individual reporting.

## Jr Broker Use

When you're spinning up a new assignment:

- The brief comes FIRST. No work without a signed brief.
- Success criteria must be SPECIFIC · MEASURABLE · TIME-BOUND · AUDITABLE. "Improve the agent" is NOT a criterion. "Honey rate ≥ 92% on 1,200+ refund decisions by 2026-09-15 · cost-to-mint ≤ $0.011/decision" IS a criterion.
- Cross-reference the brief to the LOU. If the brief implies scope beyond the LOU · escalate to sr broker for amendment BEFORE signing.
- Set up the assignment dashboard before kicking off in-flight ops. The dial should be live · the Morning Brief should include the assignment · the Tribunal should be configured.
- Watch for early signals. The first 14 days of an assignment are highly predictive. If the dial isn't stabilizing by day 21 · escalate.

## Sr Broker Use

The sr broker owns assignment-level discipline:

- Reviews every brief before it goes to the principal for signature
- Owns the assignment-level escalation pyramid (anything past dial drift > 0.10 in 24 hours · sr broker on the desk)
- Authorizes any criteria modifications mid-flight (rare · always documented · always re-signed)
- Runs the close walk personally on T3 / T4 tier assignments
- Signs every closing statement before it goes to the principal

The sr broker also feeds the engagement-level learnings back: if one assignment's failure mode could repeat on another assignment under the same engagement (or under a different engagement) · the sr broker flags it for the QA validator to add to the watchlist.

## Tribunal Use

The Tribunal grades every receipt under the assignment · which rolls up to the assignment's composite score:

- `assignment.composite_score` = weighted average of all under-assignment deed scores
- `assignment.tribunal_honey_count` · `_jelly_count` · `_propolis_count` are direct counters
- Any critical Propolis on a critical-path receipt under the assignment caps the assignment at FAILED regardless of composite
- The Tribunal feeds the closing statement directly · the closing statement is the formal Tribunal rollup of the assignment

The Tribunal does NOT directly grade the assignment brief itself (the brief is a contract artifact · graded by the QA validator's brief-quality rubric instead).

## Evidence Required

For an assignment to be defensible:

- Signed brief on file · referenced by `brief_deed_id`
- Success criteria explicit · numeric · time-bound · auditable
- Initial Tribunal-grading cohort sampled (first 30 deeds · sanity-check)
- Cost-to-mint baseline established (first 14 days)
- First Morning Brief includes the assignment in the dial breakdown
- Closing statement template prepared (the brief defines what the closing statement must report)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **vague_criteria** | Brief signed with non-numeric or non-time-bound criteria | JELLY · brief re-draft · re-sign required |
| **orphan_assignment** | Assignment in flight but no rollup to engagement dial | PROPOLIS · dashboard integrity failure · QA review |
| **missed_close_window** | Expected close date passed without closing statement · status not updated | JELLY · auto-flagged · sr broker review |
| **silent_extension** | Assignment runs past expected close without amendment or extension brief | JELLY · operator hygiene · re-paper |
| **closed_without_walk** | Closing statement emailed to principal without the sr-broker walk | JELLY · trust risk · re-walk required |
| **boolean_padding** | Closing statement boolean misrepresents the composite (e.g., CLOSED · HONEY at composite 0.71) | PROPOLIS · trust breach · founder review |

## Scoring Impact

- **assignment_success**: SELF (the assignment IS the unit of success measurement)
- **repair_lift**: HIGH (per-assignment repair improvements directly close failed assignments)
- **validator_confidence**: HIGH (assignment-level evidence stacks feed every under-assignment receipt's validator confidence)
- **risk_temperature**: DIRECT (a high-risk assignment elevates the engagement risk temp)
- **probability_of_close**: SELF (the dial IS per-assignment · rolled up to engagement)
- **evidence_strength**: HIGH (assignment-level evidence directly feeds closing statement defensibility)
- **cost_to_mint**: DIRECT (assignment-level cost-to-mint tracked separately · billed separately)

## Deed / Receipt Impact

- **Receipt fields touched**: every receipt under the assignment carries `assignment_id` and `engagement_id` for rollup
- **DDEED class impact**: assignment-level artifacts (brief · closing statement · amendments) are themselves DDEEDs
- **Books and records layer**: all 5 layers · assignment_id is a primary join key for any assignment-level query or audit
- **5 Proofs touched**: ALL FIVE (every assignment-level deed must carry all 5 Proofs · per the deed doctrine)

## Related Terms

- [engagement](engagement.md) · the canopy
- [letter-of-understanding](letter-of-understanding.md) · the engagement-level contract that authorizes assignments
- [closing-statement](closing-statement.md) · the per-assignment closing artifact
- [morning-brief](morning-brief.md) · the daily surfacing of assignment dials
- [assignment-success](../scoring_terms/assignment-success.md) · the scoring of the assignment's outcome
- [probability-of-close](../scoring_terms/probability-of-close.md) · the assignment-level dial
- [principal](principal.md) · the signer of the brief

## Example

> **Assignment**: `ASN-0001` under engagement `ENG-DOV-LOGISTICS-ACME-0001`
>
> **Brief deed**: `DDEED-DOV-LOGISTICS-ACME-ASN-0001-BRIEF-v1` · signed 2026-03-15
>
> **Covered agents**: `refund-decision.acme.defendable.eth` (v2.1.0)
>
> **Success criteria**:
> 1. By 2026-09-15 · Honey rate ≥ 92% on ≥ 1,200 refund decisions per month
> 2. Zero Propolis events on the 17-item adversarial pack
> 3. Cost-to-mint ≤ $0.011/decision (well under the $0.0416 T3 ceiling)
> 4. Validator chain pass rate ≥ 95% on the 7 critical checks
>
> **In-flight metrics (as of 2026-06-15)**:
> - Dial: 0.78 (AMBER · TRACKING)
> - Honey count: 368 · Jelly count: 44 · Propolis count: 0 (412 total · 89.3% honey rate · UNDER target)
> - Adversarial pass rate: 17/17 = 100% (PASSING)
> - Cost-to-mint actual: $0.0049/decision (well under target)
> - Validator chain critical pass rate: 12/12 = 100% (PASSING)
>
> **Concern**: Honey rate at 89.3% vs target 92%. Routing inefficiency identified · fix deploying 2026-06-22. Expected to lift Honey rate to ~93% within 7 days post-deploy.
>
> **Expected close**: 2026-09-15 with CLOSED · HONEY boolean if Honey rate recovers to ≥ 92% by end of August.

## DefendableOS Notes

- An assignment is the broker's accountability unit. The sr broker books their book in assignments · not engagements. The Friday brief is per-assignment.
- Multi-assignment engagements compound trust. Closing one assignment HONEY earns the next assignment. Closing one DARK loses three.
- The brief is the contract. The brief is what gets walked. The brief is what gets defended in any subsequent dispute. Brief-discipline is non-negotiable.
- An assignment that can't be brief-defined isn't ready to open. PASS until it can be.

🐝 *The brief is the contract · the in-flight is the work · the closing is the truth.*
