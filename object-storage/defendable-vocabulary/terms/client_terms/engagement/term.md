# Engagement

## Street Definition

"Who's the engagement with?" — the founder asks before reviewing any new file.

An **Engagement** is the formal relationship between DefendableOS (acting as Defender) and a customer (acting as Principal). It's the umbrella · the contract envelope · the named relationship. Underneath the engagement live one-or-many Assignments · which are the specific work orders.

In CRE terms: an engagement is the listing-broker agreement (sometimes the exclusive-rep agreement) · the contract that names the broker as the principal's representative for a defined scope · period · and economics. Assignments under an engagement are the individual trades · listings · or transactions executed during that period. The engagement is the canopy · the assignments are the leaves.

If a customer hasn't signed a Letter of Understanding · we don't have an engagement. We have a conversation. That's a meaningful distinction.

## CRE Operator Meaning

A sr broker in CRE knows the difference between a relationship and a transaction. A transaction closes once and the parties walk. A relationship produces 10 transactions over 5 years · plus 4 referrals · plus 1 keynote · plus the call you get when their partner's brother needs a 1031.

An engagement is the relationship in writing. The LOU formalizes the scope · the term · the economics · the SLAs · the escalation pyramid · the conflict-of-interest stipulations. Everything material is named. Nothing material is implicit.

The discipline: every engagement has a named principal · a named broker · a defined economics structure · a defined term · and an exit ramp. If any of those five are missing · you have a vendor pitch · not an engagement.

## DefendableOS Definition

An **Engagement** in DefendableOS is the LOU-bound relationship between Defender and Principal · uniquely identified by `engagement_id` of shape `ENG-{org}-{vertical}-{customer}-{seq}`. Every engagement is itself a deed at issuance (`DDEED-{org}-LOU-{slug}-v1`) · anchored on Hedera HCS · resolvable via ENS.

An engagement contains:
- Exactly one signed LOU (with versioning if amended)
- One-or-many Assignments (each with its own brief)
- A continuous dial of Probability of Close (rolled up across active assignments)
- A continuous Morning Brief cadence (06:00 daily)
- A continuous books-and-records contribution stream (every deed under any assignment under the engagement)
- A defined service tier (T1 / T2 / T3 / T4)
- A defined principal contact list

Closure of all assignments does NOT close the engagement. The engagement persists until the LOU is formally terminated per §9 of the LOU template.

## Backend Representation

```json
{
  "engagement.engagement_id": {
    "type": "string",
    "pattern": "ENG-[A-Z]+-[A-Z]+-[A-Z]+-[0-9]{4}",
    "primary_key": true
  },
  "engagement.lou_deed_id": {
    "type": "string",
    "pattern": "DDEED-.+-LOU-v[0-9]+",
    "required": true
  },
  "engagement.tier": {
    "type": "enum",
    "values": ["T1_PILOT", "T2_PRODUCTION", "T3_WHITE_GLOVE", "T4_EMBEDDED"]
  },
  "engagement.effective_date": {"type": "date"},
  "engagement.term_months": {"type": "integer", "default": 12},
  "engagement.auto_renew": {"type": "boolean", "default": true},
  "engagement.status": {
    "type": "enum",
    "values": ["DISCOVERY", "APPRAISALS", "INK_PENDING", "ACTIVE", "PAUSED", "TERMINATING", "CLOSED"]
  },
  "engagement.principal_contacts": {
    "type": "jsonb_array",
    "shape": "[{role, name, email, escalation_tier}]"
  },
  "engagement.sr_broker_id": {"type": "string"},
  "engagement.founder_engagement_required": {"type": "boolean"},
  "engagement.assignment_ids": {"type": "string_array"},
  "engagement.dial_current": {"type": "float", "range": [0,1]},
  "engagement.cost_to_mint_ceiling_per_deed_usd": {"type": "float"},
  "engagement.monthly_floor_usd": {"type": "float"}
}
```

Schema files: `docs/schemas/engagement.schema.json` · `docs/schemas/lou.schema.json`

## Client Explanation

An **engagement** is our formal relationship with you · the contract envelope. It starts the day you sign the Letter of Understanding. It covers your service tier · your fee structure · your escalation pyramid · your books-and-records retention · everything that governs how we work together.

Inside an engagement we run one-or-many **assignments** · which are the specific projects with specific success criteria. Think of the engagement as your listing agreement · and the assignments as the individual trades we execute under it.

The engagement persists for as long as the LOU is in force (typically 12 months · auto-renewing). You can pause it · terminate it for cause · or terminate it for convenience on 60 days notice. We treat the engagement as the relationship · which means it survives any single assignment closing successfully or unsuccessfully.

## Jr Broker Use

When you open a new file:

- Confirm the engagement exists. If there's no signed LOU · there's no engagement · we have a discovery conversation · NOT an engagement-level workflow.
- Check the `engagement.status`. Most workflows ONLY apply to ACTIVE engagements. Don't run a Morning Brief generation against a DISCOVERY-stage record.
- Reference the `engagement_id` in every artifact you produce. Color files · digests · pre-market flight sheets · all of them carry the engagement_id in metadata.
- Don't add an assignment to an engagement without sr broker sign-off. Assignment creep is how engagements lose their dial calibration.
- If the principal asks for something that's outside the LOU scope · escalate to sr broker. Don't promise scope expansion verbally.

## Sr Broker Use

The sr broker is the named engagement lead. The sr broker:

- Drafts and walks the LOU at engagement open
- Approves every new assignment brief under the engagement
- Owns the weekly engagement review (Friday cadence · across the full book of engagements)
- Authorizes engagement-level escalations (founder cc decisions · PASS-pivot conversations)
- Signs every closing statement
- Owns the relationship continuity · across multiple assignments · across multiple closings · across renewal cycles

A sr broker should be able to answer · for any engagement they lead: current dial · current tier · current cost-to-mint trajectory · open escalation status · time-to-renewal. If they can't answer those 5 things in 30 seconds · the engagement isn't being run well.

## Tribunal Use

The Tribunal doesn't grade engagements directly · it grades the receipts and deeds under each assignment. But the Tribunal feeds the engagement-level rollups:

- `engagement.dial_current` is derived from across all in-flight assignments
- `engagement.health_score` is computed nightly from the 7-day rollup of all under-engagement deeds
- Critical Propolis on ANY assignment under an engagement triggers an engagement-level escalation (NOT just an assignment-level one)
- `engagement.calibration_report` is the annual rollup (deed `DDEED-{org}-CALIB-{slug}-{year}-v1`)

The Tribunal also produces the data feeding the annual engagement-level renewal recommendation (continue · upgrade-tier · downgrade-tier · graceful-exit).

## Evidence Required

For an engagement to be defensible:

- Signed LOU on file · referenced by `lou_deed_id`
- Initial assignment brief signed (so the engagement has at least one work order)
- Designated recipients confirmed in writing (per LOU §11)
- Service tier explicitly chosen and acknowledged
- Cost-to-mint ceiling acknowledged in writing
- First Morning Brief delivered (so the cadence is live)

An engagement record missing any of the above is in `INK_PENDING` status · NOT ACTIVE. The dial doesn't spin up until ACTIVE.

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **ghost_engagement** | Engagement record exists but no signed LOU referenced | PROPOLIS · audit failure · sr broker review |
| **scope_creep** | Assignments added outside LOU scope without amendment | JELLY · engagement health flag · re-paper |
| **tier_mismatch** | Service delivered exceeds contracted tier (giving away the apparatus) | JELLY · operator hygiene · re-tier discussion |
| **silent_renewal** | LOU auto-renewed without principal acknowledgment of any material change | PROPOLIS · trust risk · re-walk required |
| **orphaned_engagement** | Sr broker left · engagement not reassigned · principal goes 30+ days without a named contact | PROPOLIS · founder takes the lead |

## Scoring Impact

- **assignment_success**: HIGH (engagement health correlates strongly with assignment success rates)
- **repair_lift**: MEDIUM (engagement-level fixes lift many assignments)
- **validator_confidence**: HIGH (engagement-level audit-trail completeness feeds every assignment's validator confidence)
- **risk_temperature**: INVERSE (healthy engagement = lower per-assignment risk)
- **probability_of_close**: HIGH (the dial IS engagement-level)
- **evidence_strength**: HIGH (engagement-level evidence stacks feed every under-engagement deed)
- **cost_to_mint**: LOW (engagement-level costs are amortized · the per-deed cost is what matters)

## Deed / Receipt Impact

- **Receipt fields touched**: every receipt under any assignment carries `engagement_id` for rollup
- **DDEED class impact**: engagement-level deeds (LOU · calibration · termination) are themselves DDEEDs
- **Books and records layer**: all 5 layers · engagement_id is the primary join key for any cross-deed query
- **5 Proofs touched**: ORIGIN (the engagement defines the routing universe) · PROCESS (the LOU is part of the lineage) · TRUST (the LOU deed is the trust anchor for the engagement)

## Related Terms

- [assignment](assignment.md) · the work order within the engagement
- [letter-of-understanding](letter-of-understanding.md) · the contract that opens the engagement
- [principal](principal.md) · the decision-maker on the engagement
- [closing-statement](closing-statement.md) · the per-assignment artifact that rolls up to engagement health
- [morning-brief](morning-brief.md) · the daily engagement-level surfacing
- [probability-of-close](../scoring_terms/probability-of-close.md) · the engagement-level dial
- [pass-doctrine](pass-doctrine.md) · the intake filter for new engagements

## Example

> **Engagement**: `ENG-DOV-LOGISTICS-ACME-0001`
>
> **LOU**: `DDEED-DOV-LOGISTICS-ACME-LOU-v1` · signed 2026-03-12 · 12-month initial term · auto-renew enabled.
>
> **Tier**: T3 · White-Glove · effective rate $0.0416/deed · monthly floor $8,500.
>
> **Assignments under this engagement**: ASN-0000 (pilot · CLOSED · HONEY) · ASN-0001 (refund-decision · in flight) · ASN-0002 (invoice-reconciliation · in flight).
>
> **Status**: ACTIVE · Q3 QBR scheduled 2026-06-15.
>
> **Sr broker**: Jenny Reyes · Founder cc on material events.
>
> **Year-1 trajectory**: started at dial 0.71 (first 30 days · normal pilot ramp) · climbed to 0.84 by month 4 · drifted to 0.78 in month 6 (operator hygiene driver · routing inefficiency · fixed by 2026-06-22). Year-1 forecast: renewal probability 0.85 · likely upgrade to T3+ with custom validator chain for Q4.

## DefendableOS Notes

- An engagement is the unit of relationship · NOT the unit of work. Assignments are the work. Receipts are the proof. Engagements are the canopy.
- The engagement record persists across team rotations · across model upgrades · across customer org changes. It's designed to outlast every party that touched it.
- The 7-year retention on books-and-records is engagement-level · not assignment-level. The engagement folder is what survives the relationship.
- An engagement is a Class A 5-cap asset on our side. The founder treats every engagement like a listed building. The discipline is the same.

🐝 *The engagement is the canopy · the assignments are the leaves · the deeds are the soil.*
