# PASS Doctrine

## Street Definition

"We PASS." — the sr broker says · cleanly · without apology · when a deal doesn't pencil.

The **PASS Doctrine** is the explicit stance that DefendableOS refuses fantasy mandates. We turn down engagements we can't make defendable · even when the fee is real · even when the principal is influential · even when the prospect wants us specifically.

Founder's locked phrase: *"If seller wanted 100M strike price and the deal penciled at 75M · I would PASS on the 2M fee and wait until the seller went through enough pain with the other broker that sold him on fantasy · then they would call me · want to list WITH ME on MY guidance."*

PASS is the discipline that earns the next decade. Taking the wrong deal loses 3 future deals · so the PASS calculus is always net-positive over the long run.

## CRE Operator Meaning

In CRE · every broker faces fantasy mandates monthly. Sellers who want 100M for a 75M asset. Buyers who want 5cap on a 7cap deal. Sponsors who promise IRRs the asset class doesn't support. The bad brokers take all of those · run them through the apparatus · burn the seller's time and the buyer pool's patience · and book maybe 1 in 10 at re-traded numbers far below the original ask.

The top 1% brokers PASS on those. They walk. They tell the seller the truth (the asset prices at 75M · here's the comp set · we'd be happy to list at 75M but not at 100M). Then they go work other listings. 90 days later · the seller calls back · having burned through two other brokers on the fantasy mandate · ready to list at 75M with the broker who told them the truth on day one.

The patience IS the moat. The top brokers earn $20M/yr because they say no to $2M of fantasy fees per quarter.

## DefendableOS Definition

The **PASS Doctrine** in DefendableOS is the formal intake-filter discipline · documented at every stage of the MAGIC funnel · enforced by sr brokers · escalated to founder for any close calls.

PASS comes in two flavors:

1. **PASS_PIVOT** · we walk this engagement · we offer to revisit in 6-12 months · we may refer to a different provider in the interim · doors stay open
2. **PASS_TERMINAL** · we walk this engagement · we don't intend to revisit · the structural fit isn't there

PASS is documented in writing every time it's invoked · in the engagement's PASS verdict log. The rationale is captured. The founder is briefed on any PASS at the Appraisals stage or later (early-Meetings PASS doesn't require founder briefing · just sr-broker discretion).

PASS is the doctrine equivalent of the LOU's §8 PASS Doctrine clause · which gives Defender the contractual right to invoke PASS even mid-engagement if the structure drifts.

## Backend Representation

```json
{
  "pass_verdict.verdict_id": {"type": "string", "primary_key": true},
  "pass_verdict.engagement_id": {"type": "string", "fk": "engagement.engagement_id", "nullable": true},
  "pass_verdict.lead_id": {"type": "string", "fk": "lead.lead_id"},
  "pass_verdict.invoked_at": {"type": "timestamp"},
  "pass_verdict.invoked_by_sr_broker_id": {"type": "string"},
  "pass_verdict.founder_briefed": {"type": "boolean"},
  "pass_verdict.verdict": {
    "type": "enum",
    "values": ["GO", "PASS_PIVOT", "PASS_TERMINAL"]
  },
  "pass_verdict.rationale_categories": {
    "type": "string_array",
    "enum_values": [
      "FANTASY_PROMISES_REQUIRED",
      "STRUCTURAL_INFEASIBILITY",
      "PRINCIPAL_NOT_REACHABLE",
      "VENDOR_FIT_MISMATCH",
      "ECONOMICS_BELOW_FLOOR",
      "ETHICAL_CONCERN",
      "REGULATORY_RISK",
      "TIMING_MISMATCH"
    ]
  },
  "pass_verdict.rationale_narrative": {"type": "text"},
  "pass_verdict.principal_notified_at": {"type": "timestamp", "nullable": true},
  "pass_verdict.principal_notified_by": {"type": "enum", "values": ["EMAIL", "PHONE", "IN_PERSON"]},
  "pass_verdict.referral_provided": {"type": "boolean"},
  "pass_verdict.referral_target": {"type": "string", "nullable": true},
  "pass_verdict.revisit_date": {"type": "date", "nullable": true},
  "pass_verdict.tags": {"type": "string_array"}
}
```

Schema files: `docs/schemas/pass_verdict.schema.json`

## Client Explanation

DefendableOS operates under a published **PASS Doctrine**. We refuse engagements we can't make defendable.

That means:

- If you ask us to certify an agent that we can't actually grade · we'll say so · and walk.
- If your success criteria require us to make claims we can't back with evidence · we'll say so · and walk.
- If your economics don't support our apparatus cost · we'll say so · and walk.
- If your timing requires us to skip the discipline that makes our work defendable · we'll say so · and walk.

We don't pretend. We don't over-promise. We don't sign LOUs we can't deliver against.

The PASS doctrine cuts both ways. You can PASS on us too · for any reason · at any time per the LOU termination clauses. The relationship is voluntary on both sides · which is part of what makes it trustworthy.

When we PASS · we tell you honestly. If we know a provider who is a better fit · we'll tell you that too. We'd rather lose this engagement and keep your respect than win this engagement and burn it.

## Jr Broker Use

The jr broker doesn't invoke PASS · but supports the verdict:

- **Capture the signals early** that might lead to PASS (vague pain · principal unreachable · success criteria fantasy)
- **Document principal motivation honestly** even when it's negative (don't sugar-coat to keep the deal alive · the sr broker needs the truth)
- **Flag economics that don't pencil** as soon as the rough math shows below the walk-away floor
- **Escalate any fantasy promise request** to sr broker same-day (don't try to negotiate it down yourself · let the sr broker handle)
- **Never argue against a PASS verdict** in front of the principal · take it back to the sr broker if you disagree internally

PASS is one of the highest-trust skills the jr broker develops. Learning to recognize when to escalate-for-PASS is what separates a 6-month jr from an 18-month jr.

## Sr Broker Use

The sr broker:

- **Invokes PASS authoritatively** at the Appraisals stage · with documented rationale
- **Briefs the founder on any PASS** at Ink stage or later (early PASS at Meetings/Appraisals is sr-broker discretion)
- **Authors the PASS notification to the principal** · gracefully · with respect · with referral if possible
- **Logs the PASS verdict** in the engagement folder · with revisit date if PIVOT
- **Reviews PASS verdicts in aggregate quarterly** · looks for pattern signals (are we PASSING too often on a specific vertical · is the intake apparatus filtering too tight · etc)

The sr broker also handles mid-engagement PASS pivots · invoking LOU §8 if the structure has drifted. Mid-engagement PASS is rare but documented · principal-notified within 24 hours · graceful exit per the LOU §9.3 termination-for-convenience clause.

## Tribunal Use

The Tribunal doesn't make PASS verdicts (that's a human-broker call) · but the Tribunal supports them:

- The Tribunal's color grading on the engagement's evidence backstops the PASS rationale
- The Tribunal's competitor-landscape data feeds the PASS-vs-PIVOT calculus
- The Tribunal flags engagements during in-flight if they drift toward structural infeasibility (early warning for sr broker PASS-pivot consideration)
- Aggregated PASS verdicts feed the calibration corpus for future intake screening

PASS verdicts are themselves audit-able · the QA validator (SH6) reviews quarterly for verdict consistency.

## Evidence Required

For a PASS verdict to be defensible:

- Rationale documented in writing (categorical + narrative)
- Sr broker signature captured
- Founder briefing captured (for any PASS at Appraisals stage or later)
- Principal-notification captured (date · channel · content)
- Referral (if provided) documented with the referred provider's name
- Revisit date set (if PIVOT) or explicit "no revisit planned" (if TERMINAL)
- Filed in the lead/engagement folder · permanent record · INTERNAL_ONLY visibility

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **fantasy_acceptance** | Deal taken that should have been PASSed · principal pressured the broker into accepting | PROPOLIS · founder review · likely engagement-level damage |
| **vague_pass_rationale** | PASS invoked without documented rationale | JELLY · rationale captured retroactively · audit flag |
| **principal_ghosted_on_pass** | PASS verdict made internally · principal never formally notified | PROPOLIS · trust breach · principal notified late |
| **silent_pivot** | PASS_PIVOT logged but no revisit date set · re-engagement window forgotten | JELLY · operator hygiene · revisit scheduled retroactively |
| **referral_blind** | PASS invoked · no referral attempted even though obvious alternative exists | JELLY · post-PASS courtesy lost · captured in coaching |
| **founder_skipped** | Material PASS made at Ink stage without founder briefing | JELLY · founder briefed retroactively · sr-broker coaching |

## Scoring Impact

- **assignment_success**: HIGH (PASS discipline keeps the in-flight book healthy · the engagements we DO take close at high HONEY rates)
- **repair_lift**: HIGH (PASS prevents engagements that would have required heavy ongoing repair · upfront filtering > downstream fixing)
- **validator_confidence**: HIGH (clean PASS logs prove the intake filter works · audit-clean intake → audit-clean book)
- **risk_temperature**: INVERSE (PASS discipline = lower portfolio risk · skipping PASS = elevated risk)
- **probability_of_close**: HIGH (filtered intake produces higher-dial engagements on average)
- **evidence_strength**: HIGH (PASS verdicts are evidence the apparatus is disciplined · not just permissive)
- **cost_to_mint**: NEUTRAL (PASS doesn't directly affect per-deed cost · but reduces rework cost downstream)

## Deed / Receipt Impact

- **Receipt fields touched**: PASS verdicts are not receipted (no work was done) but the verdict itself is logged
- **DDEED class impact**: PASS verdicts are NOT issued as DDEEDs (they're internal · pre-engagement · not principal-facing in the deed sense)
- **Books and records layer**: L1 PostgreSQL + L3 NAS · 7-year retention · INTERNAL_ONLY visibility
- **5 Proofs touched**: indirectly · the PASS verdict protects the books-and-records integrity downstream by filtering at intake

## Related Terms

- [engagement](engagement.md) · the relationship PASS filters at intake
- [letter-of-understanding](letter-of-understanding.md) · contains the §8 PASS clause that authorizes mid-engagement PASS
- [pre-market-flight-sheet](pre-market-flight-sheet.md) · the artifact that renders the PASS verdict
- [principal](principal.md) · the human notified of PASS
- [closing-statement](closing-statement.md) · the post-engagement artifact that calibrates against PASS verdicts (did the engagements we said YES to close at the expected rates)
- [morning-brief](morning-brief.md) · the cadence that surfaces in-flight drift toward mid-engagement PASS

## Example

> **PASS Verdict**: `PV-2026-OMICRON-RETAIL-001`
>
> **Lead**: Omicron Retail Holdings · introduction via referral 2026-04-08
>
> **Sr Broker**: Jenny Reyes · Founder briefed 2026-04-22
>
> **Verdict**: **PASS_PIVOT**
>
> **Rationale Categories**: FANTASY_PROMISES_REQUIRED · ECONOMICS_BELOW_FLOOR
>
> **Narrative**:
> > Omicron's CEO wants us to certify their customer-service agent for SOC2 in 60 days. Color file shows their agent has not been instrumented for receipts · is running on a vendor stack we don't have access to · and the SOC2 audit is on a fixed timeline that doesn't allow our standard 90-day color-build + 60-day stabilization. They also want a $3,500/mo all-in price that's below our T1 pilot floor of $4,200.
> >
> > We could PASS_TERMINAL but the founder has a 30-year industry-vertical fit and Omicron is well-positioned in retail. Likely they go to a competitor who promises the timeline · burns through the SOC2 audit on shaky receipts · and comes back to us in 12-18 months ready to do this right. We want to be available when that call comes.
>
> **Principal Notified**: 2026-04-23 · phone call with CEO + email follow-up · graceful framing · referred to Competitor A (better timeline-fit at a lower discipline bar · honest about the tradeoff)
>
> **Revisit Date**: 2027-04-23 (12 months · re-introduce if SOC2 audit reveals receipt gaps)
>
> **Tags**: `retail` · `soc2_timeline_mismatch` · `founder_vertical_match` · `revisit_q2_2027`

## DefendableOS Notes

- PASS is one of the most important brand-defining disciplines we have. Every PASS is a vote for the integrity of the book. Every fantasy-deal-accepted is a vote against it.
- We track PASS quarterly. A healthy book sees 30-50% PASS at the Appraisals stage (intake filter doing its job). A book with < 10% PASS is suspicious (filter too loose · likely taking deals that will fail downstream).
- The founder PASS-walked $2M in fee revenue per quarter in his CRE career to earn $20M/yr. The math compounds in our favor over time · same as it did for him.
- A graceful PASS notification can convert into a referral 18 months later. The relationship survives the no.

🐝 *PASS is the moat · the patience is the math · the next listing comes from the discipline.*
