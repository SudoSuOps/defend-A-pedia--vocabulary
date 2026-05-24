# Pre-Market Flight Sheet

## Street Definition

"What's the flight sheet say?" — the sr broker asks before the first sit-down with a prospect.

The **Pre-Market Flight Sheet** is the broker-grade internal operating doc that supersedes the pretty marketing OM. It captures the real numbers · the actual comps · the buyer pool · the deal physics · the area-of-specialization intel. It's the document the sr broker uses to actually win the deal · NOT the document the marketing team uses to get attention.

Founder's locked phrase: *"It's not the best OM · pretty booklet that wins the listing · it's the pre-market flight sheet · know your area of specialization · and dominate it."*

If the team only has the OM and not the flight sheet · they're a marketing team · not a brokerage. The flight sheet is what separates the two.

## CRE Operator Meaning

In CRE · the OM (Offering Memorandum) is the public-facing marketing document for a listing. It has renders · highlights · stats · cap-rate math · executive summary · property photos. It's polished for the broker's brand and for capturing buyer interest. Every shop ships one. They mostly look alike.

The pre-market flight sheet is what lives behind the OM. It's the document that has:

- The real comps (not the seller's pitched comps · the actual closed sales we verified)
- The real buyer pool (specific firms · specific allocations · specific recent activity)
- The deal physics (what the deal pencils at for a realistic buyer · NOT what it lists at)
- The seller's actual motivation (1031 clock · refi expiring · partnership dispute)
- The walk-away number (the price below which we PASS rather than re-trade)
- The area-of-specialization intel (the broker's edge · the things no other broker on the deal knows)

The flight sheet is INTERNAL. It never leaves the brokerage. It's the document that wins the deal because the broker can quote it from memory in any conversation.

## DefendableOS Definition

The **Pre-Market Flight Sheet** in DefendableOS is the broker-grade internal operating doc for a prospective engagement · prepared during the Appraisals stage of MAGIC · referenced through engagement open · and archived as part of the engagement folder. It mirrors the CRE flight sheet shape · adapted to AI defense:

- The principal's actual pain (not the pitch · the diagnosed reality)
- The agent fleet's actual condition (not vendor's claimed metrics · our color-built observations)
- The competitor landscape (who else is talking to this principal · what they're pitching · how we differentiate)
- The deal physics (what the engagement pencils at on T1 / T2 / T3 / T4 · which tier is right)
- The walk-away number (the floor below which we PASS · documented in writing)
- The area-of-specialization intel (which of our vertical playbooks applies · why we have an edge here)

The flight sheet is INTERNAL · NEVER shared with the principal. The principal sees the LOU (which is the OM-equivalent · the document we sign together). The flight sheet is what makes the LOU defendable from our side.

## Backend Representation

```json
{
  "flight_sheet.flight_sheet_id": {"type": "string", "primary_key": true},
  "flight_sheet.engagement_id": {"type": "string", "fk": "engagement.engagement_id", "nullable": true},
  "flight_sheet.lead_id": {"type": "string", "fk": "lead.lead_id"},
  "flight_sheet.prepared_at": {"type": "timestamp"},
  "flight_sheet.prepared_by_sr_broker_id": {"type": "string"},
  "flight_sheet.principal_pain_diagnosed": {"type": "text"},
  "flight_sheet.color_summary": {
    "type": "jsonb",
    "shape": "{source_count, source_weights_mean, contradictions, freshness_days}"
  },
  "flight_sheet.agent_fleet_observed_condition": {"type": "jsonb"},
  "flight_sheet.competitor_landscape": {
    "type": "jsonb_array",
    "shape": "[{competitor, pitch_summary, our_differentiation}]"
  },
  "flight_sheet.recommended_tier": {
    "type": "enum",
    "values": ["T1_PILOT", "T2_PRODUCTION", "T3_WHITE_GLOVE", "T4_EMBEDDED", "PASS"]
  },
  "flight_sheet.deal_physics_per_tier": {
    "type": "jsonb",
    "shape": "{tier: {projected_monthly_revenue, projected_deed_volume, projected_close_dial, expected_lifetime_months}}"
  },
  "flight_sheet.walk_away_floor_usd_per_month": {"type": "float"},
  "flight_sheet.area_of_specialization_match": {
    "type": "enum",
    "values": ["STRONG", "MODERATE", "WEAK", "NEW_VERTICAL"]
  },
  "flight_sheet.pass_verdict": {
    "type": "enum",
    "values": ["GO", "PASS_PIVOT", "PASS_TERMINAL"]
  },
  "flight_sheet.pass_verdict_rationale": {"type": "text"},
  "flight_sheet.visibility": {
    "type": "enum",
    "values": ["INTERNAL_ONLY"],
    "default": "INTERNAL_ONLY",
    "validation_rule": "must NEVER be set to client-visible"
  }
}
```

Schema files: `docs/schemas/flight_sheet.schema.json`

## Client Explanation

The principal never sees the flight sheet directly. The flight sheet is an internal artifact · the same way a CRE brokerage doesn't share their internal pre-listing pricing analysis with the seller (they share the listing recommendation · which derives from the analysis).

What the principal SEES:
- The result of the flight sheet (the LOU we recommend · the tier · the success criteria · the pricing)
- The summarized intelligence (the pain diagnosis · the area-of-specialization fit · the recommended path)
- The PASS decision (if we walk · we tell the principal honestly · including which competitor we'd refer them to if our tier doesn't fit)

What the principal DOESN'T see:
- The walk-away floor (that's negotiation strategy)
- The full competitor landscape analysis (we don't broadcast who else we know is in the conversation)
- The internal scoring on principal motivation (could damage the relationship if surfaced raw)

The principal earns trust by experiencing the OUTPUT of the flight sheet · not by reading it raw. The discipline behind the recommendation is the trust signal.

## Jr Broker Use

The jr broker doesn't draft the flight sheet · the sr broker does. But you support:

- **Build the color file** that feeds the flight sheet (≥ 5 independent sources)
- **Document the principal's pain in their own words** (verbatim · not paraphrased · the sr broker translates)
- **Surface any competitor signals you hear** (specific firm mentions · pricing references · pitch comparisons) → all go into the competitor landscape section
- **Track principal motivation signals** (responsiveness · diligence engagement · stakeholder alignment) → feeds the deal physics section
- **Coordinate the sr-broker prep session** for the flight sheet draft (typically 90-120 min focused work)

You also confirm the visibility lock: a flight sheet must NEVER be sent to the principal · even by accident. The schema enforces this · but the operator hygiene enforces it twice.

## Sr Broker Use

The sr broker:

- **Drafts the flight sheet personally** during Appraisals · references color file · diagnoses pain · scopes competitors
- **Reviews with founder on T3/T4 tier recommendations** (founder owns the area-of-specialization match call)
- **Updates the flight sheet through engagement open** (the flight sheet evolves until the LOU signs · then it freezes as a baseline)
- **Re-opens the flight sheet at annual renewal** (writes a v2 · documents what changed · captures learnings)
- **Files the final pre-LOU flight sheet as an engagement-folder artifact** · permanent record · INTERNAL ONLY tag enforced

The sr broker is also responsible for the **PASS verdict** documentation. If the flight sheet recommends PASS_PIVOT or PASS_TERMINAL · the rationale is documented · the founder is briefed · the principal is notified gracefully.

## Tribunal Use

The Tribunal doesn't grade flight sheets directly · but:

- The flight sheet's `color_summary` field is sourced from Tribunal-graded color evidence
- The flight sheet's `pass_verdict` becomes an intake gate · negative PASS verdicts prevent engagement creation
- The flight sheet's `recommended_tier` feeds the engagement-tier-fit scoring
- Aggregated flight-sheet data (over time) becomes calibration corpus for the area-of-specialization fit predictions

The Tribunal CANNOT view flight sheets in their full text (the visibility lock applies to internal automation too · only sr brokers + founder + QA validator have read access).

## Evidence Required

For a flight sheet to be defensible:

- Color file referenced with ≥ 5 independent sources · contradictions reconciled
- Principal pain captured in writing (verbatim if possible · diagnosed honestly)
- Competitor landscape includes ≥ 2 named competitor pitches (or explicit "no known competition" with rationale)
- Deal physics modeled for at least 3 of 4 tiers (so the tier recommendation is comparative · not isolated)
- Walk-away floor documented in USD/month
- PASS verdict explicit (GO · PASS_PIVOT · PASS_TERMINAL · NOT "TBD")
- Sr broker signature captured · founder sign-off on T3/T4 recommendations

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **client_leak** | Flight sheet shared with principal (even partial · even by accident) | PROPOLIS · trust breach · sr broker review · founder notification |
| **vague_pass_verdict** | PASS verdict missing or "TBD" · engagement opened anyway | PROPOLIS · audit failure · re-paper |
| **single_tier_only** | Only one tier modeled · no comparative pricing · recommendation isolated | JELLY · re-draft required |
| **competitor_blind** | No competitor landscape analysis · engagement opened in a vacuum | JELLY · re-draft required |
| **stale_flight_sheet** | Engagement open · flight sheet not updated at first renewal | JELLY · re-open + write v2 required |
| **walk_away_missing** | No walk-away floor documented · engagement renegotiated without a baseline | PROPOLIS · re-paper |

## Scoring Impact

- **assignment_success**: HIGH (engagements opened against solid flight sheets close at significantly higher HONEY rates)
- **repair_lift**: MEDIUM (flight sheet identifies upfront which engagements will need ongoing repair-style attention)
- **validator_confidence**: HIGH (the flight sheet is the engagement-level evidence backbone)
- **risk_temperature**: INVERSE (solid flight sheet = low engagement risk)
- **probability_of_close**: HIGH (the recommendation in the flight sheet seeds the opening dial)
- **evidence_strength**: HIGH (flight sheet is the strongest pre-engagement evidence class)
- **cost_to_mint**: NEUTRAL (flight sheet is operator-margin time · amortized)

## Deed / Receipt Impact

- **Receipt fields touched**: every under-engagement deed references back to the flight sheet for pre-engagement context (not displayed publicly · stored for audit)
- **DDEED class impact**: the flight sheet is NOT itself a DDEED (it's internal · not principal-facing · not appropriate for public anchoring)
- **Books and records layer**: L1 PostgreSQL + L3 NAS · 7-year retention · INTERNAL_ONLY visibility flag enforced
- **5 Proofs touched**: indirectly · the flight sheet is the seed for the engagement's process lineage · ORIGIN + PROCESS proofs reference it

## Related Terms

- [engagement](engagement.md) · the relationship the flight sheet seeds
- [letter-of-understanding](letter-of-understanding.md) · the OM-equivalent the flight sheet produces
- [principal](principal.md) · the subject of the flight sheet
- [pass-doctrine](pass-doctrine.md) · the verdict the flight sheet renders
- [closing-statement](closing-statement.md) · the post-engagement artifact the flight sheet's predictions get calibrated against
- [color](../cre_terms/color.md) · the input the flight sheet stands on

## Example

> **Flight Sheet**: `FLT-2026-ACME-LOGISTICS-001` (INTERNAL ONLY)
>
> **Prepared**: 2026-03-08 by Jenny Reyes · Sr Broker · founder reviewed 2026-03-09
>
> **Principal Pain Diagnosed**:
> > "We have 4 production AI agents (refund · invoice · CS · fraud-flag). The vendor dashboards say 94% accuracy but my team's internal sampling says ~89%. We have a SOC2 audit Q4 and zero audit-trail. We need a third party to actually grade these things and produce evidence we can show the auditor."
>
> **Color Summary**: 11 sources · weights mean 0.87 · 1 active contradiction (vendor claim vs internal sampling) · freshness 4 days
>
> **Agent Fleet Observed Condition**: 4 agents in production · refund + invoice are top priorities · CS + fraud-flag are stable but lower volume · estimated Honey rate range 85-92% across the fleet (consistent with internal sampling · NOT vendor claim)
>
> **Competitor Landscape**:
> - Competitor A · "AI Observability Vendor" · pitching log aggregation + APM-style metrics · NOT third-party grading · weak on audit-trail
> - Competitor B · Big-4 consulting · proposing a 12-week AI audit engagement at $180K fixed · one-shot · not ongoing
> - Our differentiation: ONGOING 24/7 defense + receipts + audit-trail by design · NOT a snapshot
>
> **Deal Physics per Tier**:
> - T1 Pilot: $4,200/mo · 24K deeds/mo · projected close dial 0.71 · lifetime 6 mo
> - T2 Production: $7,800/mo · 38K deeds/mo · projected close dial 0.78 · lifetime 18 mo
> - **T3 White-Glove: $11,200/mo · 38K deeds/mo · projected close dial 0.82 · lifetime 36+ mo [RECOMMENDED]**
> - T4 Embedded: $24K/mo · same deed volume · likely overkill at this engagement size
>
> **Walk-Away Floor**: $8,500/mo (the T3 monthly floor · we don't drop below the apparatus cost)
>
> **Area of Specialization Match**: STRONG (logistics · supply chain · CRE-rooted operator) · our vertical playbook is mature
>
> **PASS Verdict**: GO · proceed to LOU draft at T3 tier
>
> **Rationale**: Principal pain is real · pencils on T3 economics · area of specialization is strong · competitors are mis-positioned (logs vs grading · or one-shot vs ongoing) · SOC2 audit deadline creates time pressure that favors our cadence-based discipline. Founder approval captured 2026-03-09.

## DefendableOS Notes

- The flight sheet is the discipline that wins the deal. The LOU is the discipline that runs the relationship. The closing statement is the discipline that earns the next listing. The three discipline artifacts compound.
- Aggregated flight sheets (sanitized · stripped of competitive intel) become the strongest internal training corpus for future sr brokers. Every flight sheet is a curriculum.
- The "pretty OM beats pretty OM" reframe is one of the founder's most important locks. The marketing team owns the OM. The brokerage owns the flight sheet. The brokerage WINS the deal.
- The visibility lock (INTERNAL_ONLY) is enforced at schema level · at API level · at the audit layer. Any flight-sheet leak is the highest-severity trust breach in the operating model.

🐝 *The flight sheet is the discipline · the LOU is the signature · the closing is the truth.*
