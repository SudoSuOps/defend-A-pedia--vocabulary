# Deal Flow

## Street Definition

"What's the deal flow look like this week?" — sr broker, every Monday morning, on the pipeline review.

**Deal flow** is the pipeline metric. The volume and velocity of opportunities moving through the funnel · stage by stage · with conversion rates calculated at each stage transition. Strong deal flow doesn't mean lots of prospects; it means high-quality prospects moving through stages at predictable rates with clean attribution back to source.

In CRE, deal flow IS the broker's business. Without flow there are no listings, no closes, no fees. In DefendableOS, deal flow is the leading indicator of every other metric · pipeline today is revenue six months out · pipeline quality today is retention three years out.

## CRE Operator Meaning

A CRE broker's deal flow is a structured pipeline view across multiple stages. Standard CRE pipeline stages:

- **Prospecting** · names on a list · being researched · no contact yet
- **Outreach** · first contact made · call placed · email sent · reply pending
- **Engaged** · two-way conversation established · qualifying ongoing
- **Pitch** · the OM presented or the pitch deck delivered · response pending
- **LOI prep** · prospect interested · negotiating terms in principle
- **LOI signed** · soft commitment · diligence triggered
- **Diligence** · active verification phase
- **PSA prep** · diligence concluded · binding contract being papered
- **Closing** · documents in escrow · funds in flight
- **Closed / To the shed** · deed recorded · fee earned

Each stage has a conversion rate to the next stage. Each stage has an expected dwell time. Each stage has typical drop-off causes. A sr broker reads their pipeline like a CFO reads a cash-flow forecast · drops where expected, holding where expected, accelerating where expected. Anomalies trigger investigation.

Healthy deal flow has shape: pipeline value at each stage should follow a known distribution. If your prospecting stage is empty, you'll have no LOIs in 90 days · investigate now, not in 90 days. If your LOI stage is congested, your diligence team is bottlenecked · re-allocate.

## DefendableOS Definition

In DefendableOS, **deal flow** is the structured pipeline of defense engagements at every stage from prospecting to live-engagement closing-statement. Same stages as CRE, with adjusted vocabulary:

- **Sourced** · prospect identified · ICP-fit verified · researcher assigned
- **Outreach** · first dial / email / warm intro made
- **Engaged** · two-way conversation · pain hypothesis tested
- **OM delivered** · canonical Offering Memorandum sent · view signals tracked
- **Sit booked** · meeting scheduled · digest in flight
- **Sit delivered** · meeting happened · post-meeting receipt logged
- **Appraisal delivered** · flight sheet delivered · pricing scenarios presented
- **LOU signed** · soft commitment · diligence triggered
- **Diligence active** · verification phase running
- **PSA signed** · binding contract · live engagement
- **Live · day 1-30** · onboarding phase · service delivery starts
- **Live · day 30-90** · stabilization phase · title insurance commitment ramping
- **Live · day 90+** · stable engagement · monthly Brief cadence
- **Renewal review** · approaching term-end · renewal discussion active
- **Renewed** · new term locked · pipeline cycles back
- **Disposition** · engagement wound down · orderly exit

The DefendableOS pipeline differs from CRE in that the engagement persists post-PSA · CRE pipeline ends at closing, but DefendableOS pipeline continues through retention. Retention is part of deal flow · because the brand depends on the renewal as much as the original close.

## Backend Representation

```json
{
  "pipeline.engagements": {
    "type": "view",
    "schema": "docs/schemas/pipeline_view.schema.json",
    "fields": {
      "engagement_id": "uuid",
      "stage": "enum",
      "stage_entered_at": "timestamp",
      "stage_target_exit_at": "timestamp",
      "stage_dwell_days": "integer",
      "stage_value_usd_annualized": "decimal",
      "stage_probability_of_close": "float",
      "source_attribution": "enum",
      "owning_jr_broker_id": "uuid",
      "owning_sr_broker_id": "uuid"
    }
  },
  "pipeline.conversion_rates_v1": {
    "type": "view",
    "fields": {
      "from_stage": "enum",
      "to_stage": "enum",
      "rolling_30d_rate": "float",
      "rolling_90d_rate": "float",
      "trailing_year_rate": "float"
    }
  },
  "pipeline.stage_dwell_metrics": {
    "type": "view",
    "fields": {
      "stage": "enum",
      "median_dwell_days": "float",
      "p90_dwell_days": "float",
      "expected_dwell_days": "float"
    }
  }
}
```

Schema files: `docs/schemas/pipeline_view.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

Deal flow is the term we use for the structured pipeline of potential engagements moving through our firm. You may hear it referenced in our Morning Briefs or annual reports as a measure of the firm's health · strong deal flow means high-quality prospects moving through stages at predictable rates, which is the leading indicator of our ability to serve you well over multi-year relationships. We monitor deal flow with the same discipline a CFO monitors cash flow · stage-by-stage, with conversion rates, dwell-time targets, and source attribution. It is one of the metrics that earned us KPMG-grade audit positioning and the basis of our retention math.

## Jr Broker Use

You ARE the deal flow. The dials you make, the meetings you book, the appraisals you deliver, the LOUs you prep · they ARE the pipeline. Your pipeline view is your scoreboard · checked daily, rebuilt every Monday, walked with sr broker every Friday.

Discipline:

- **Daily rebuild.** Every morning, your pipeline view reflects yesterday's receipts. Receipts that didn't land in the books don't count · they don't exist for pipeline math purposes.
- **Stage discipline.** A prospect doesn't advance stages just because you want them to. They advance when they take the next action that defines the next stage (responded to outreach · booked the sit · signed the LOU). Stage-stuffing is a doctrine violation · the math punishes it later.
- **Source attribution.** Every prospect tagged with source · cold outreach / founder network referral / inbound from `defendableos.com` / sample-pack download / partner referral / customer referral. Source attribution is what tells the firm where to invest next quarter.
- **Conversion math weekly.** Every Monday, compute your own dial-to-connect, connect-to-sit, sit-to-appraisal, appraisal-to-LOU, LOU-to-PSA conversion rates from your own receipts. Compare to firm benchmarks. Note where you're above range, where below, and why.
- **Stale-prospect cleanup.** Anyone who hasn't moved stages in 30 days gets reviewed. Either you have a real reason to keep them in the pipeline (named hold reason, expected next-action date) or they get culled. Bloat is the enemy of conversion math accuracy.

## Sr Broker Use

You read the pipeline as a portfolio. Same way you'd read a 12-asset CRE listing book · which assets are about to close, which are mid-marketing, which are pre-marketing, which are PASS candidates, which need re-pricing.

- **Friday walk includes pipeline walk.** End-of-week pipeline review. Conversion rates by jr broker. Stage dwell times by stage. Any anomalies investigated same Friday.
- **Source-mix review monthly.** Which sources are producing the highest-quality engagements? Which are producing high-volume low-quality? Re-allocate research and outreach investment accordingly.
- **Vertical concentration check.** Pipeline shouldn't be concentrated in one vertical · if 80% of pipeline is medical, a regulatory event in medical takes down the firm. Diversification is risk management for the brand · sr broker enforces.
- **Stage-imbalance escalation.** If LOI stage is bloated (lots of soft commitments, no progressions), diligence team may be bottlenecked or sr broker bandwidth on signatures may be the constraint. Investigate · re-allocate.
- **Pipeline-as-leading-indicator.** Pipeline today predicts revenue 6 months out. Sr broker sets quarterly targets backwards from pipeline math · not forward from wishful targets.

## Tribunal Use

The pipeline view itself is a Tribunal-scored artifact · it's not just a CRM dashboard, it's an underwriting input for the firm's own forward-looking commitments.

- **Rule layer**: any stage with a single-prospect concentration >40% of pipeline value → critical_failure → escalate (single-deal risk too high)
- **Rule layer**: source attribution missing on any active engagement → critical_failure → jr broker remediation
- **Rule layer**: stage dwell time >2x p90 with no documented hold reason → critical_failure → cleanup or status update required
- **Judge layer**: pipeline quality scored on diversification (1-5), source-mix balance (1-5), conversion-rate consistency (1-5), stage-velocity health (1-5)
- **Classification impact**: clean disciplined pipeline → Honey · pipeline with chronic single-deal concentration or skipped attribution → Jelly · pipeline gamed with stage-stuffing or fabricated source attribution → Propolis

```yaml
classification_impact: [HONEY, ROYAL_JELLY, JELLY, PROPOLIS]
can_be_critical_failure: true
rule_layer_checks:
  - no single prospect > 40% of pipeline stage value
  - all engagements have source attribution
  - stage dwell times within tolerance or hold reason documented
  - conversion rates calculable from receipts (not CRM gut feel)
```

## Evidence Required

- Every engagement receipted at every stage transition
- Source attribution at engagement origination
- Stage entry/exit timestamps from receipts
- Conversion rates computed from L1 ledger data (not CRM tag data)
- Hold reasons documented in receipts for any stage-stuck engagement

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **stage_stuffing** | Engagements advanced stages without trigger event | JELLY (PROPOLIS on repeat) |
| **fabricated_source** | Source attribution falsified to bias mix metrics | PROPOLIS |
| **stale_pipeline** | Stage-stuck engagements not cleaned · pipeline bloat | JELLY |
| **vertical_concentration** | >70% of pipeline value in one vertical | JELLY |
| **single_prospect_risk** | One prospect >40% of stage value | JELLY |
| **gut_conversion_rates** | Conversion rates reported from CRM gut feel, not receipt math | JELLY |
| **missing_attribution** | Engagement origination lacks source tag | JELLY |
| **wishful_close_dates** | Stage-target-exit dates not informed by historical dwell math | JELLY |

## Scoring Impact

- **assignment_success**: HIGH · pipeline health is the strongest predictor of forward firm-level revenue
- **repair_lift**: MEDIUM · bad pipelines can be cleaned · but it takes time
- **validator_confidence**: HIGH · pipeline metrics anchor every quarterly board update
- **risk_temperature**: VARIABLE · concentration risk lives in pipeline metrics
- **probability_of_close**: STAGE-DEPENDENT · pipeline-level prob of close rolls up engagement-level probs
- **evidence_strength**: HIGH · pipeline is one of the most-cited firm-level evidence artifacts
- **cost_to_mint**: LOW · pipeline accounting is templated · poor pipeline discipline is expensive in wasted activity

## Deed / Receipt Impact

- **Receipt fields touched**: per-engagement: `pipeline_stage`, `stage_entered_at`, `stage_value_usd_annualized`; firm-level: `pipeline_conversion_rates_v1`, `pipeline_stage_dwell_v1`
- **DDEED class impact**: pipeline metrics inform firm-level quarterly deed of operations · deed of operations cites pipeline view IDs
- **Books and records layer**: L1_PG (live view) → L2_MERKLE (quarterly snapshots sealed) → L3_NAS (historical archive)
- **5 Proofs touched**: PROCESS (engagement lifecycle discipline) · ECONOMICS (forward revenue math) · TRUST (transparency to board and customers)

## Related Terms

- [probability-of-close](probability-of-close.md) · pipeline rolls up engagement-level prob of close
- [digest](digest.md) · every active engagement has digests at multiple stages
- [om](om.md) · OM delivery is a pipeline stage event
- [loi](loi.md) · LOI signed is a pipeline-stage transition
- [psa](psa.md) · PSA signed is the close event
- [books-and-records](books-and-records.md) · pipeline metrics anchored alongside deed metrics

## Example

> **Pipeline snapshot · 2026-05-24 06:00 ET · firm-wide view**:
>
> | Stage | Count | Annualized Value | Median Dwell | Conversion to Next |
> |---|---|---|---|---|
> | Sourced | 84 | n/a | 3 days | 32% |
> | Outreach | 71 | n/a | 5 days | 18% |
> | Engaged | 38 | $14.2M | 12 days | 41% |
> | OM delivered | 22 | $8.7M | 7 days | 64% |
> | Sit booked | 14 | $6.1M | 11 days | 86% |
> | Sit delivered | 12 | $5.3M | 4 days | 67% |
> | Appraisal delivered | 8 | $3.8M | 18 days | 38% |
> | LOU signed | 3 | $1.4M | 22 days | 100% |
> | Diligence active | 3 | $1.4M | 19 days | 100% |
> | PSA signed (this quarter) | 9 | $4.1M | n/a | n/a |
> | Live | 41 | $19.8M ARR | n/a | 94% renewed at 12mo |
>
> **Anomalies flagged this week**:
> - Appraisal-to-LOU conversion at 38% (below 25-40% healthy range top end → above the bottom · acceptable but worth watching)
> - Vertical concentration: 47% medical · 23% cold storage · 18% industrial · 12% other. Medical concentration approaching upper tolerance · diversification investment to be discussed at quarterly board.
> - Source mix: 38% inbound from `defendableos.com`, 31% founder network, 19% customer referral, 12% partner referral. Customer referral % growing quarter over quarter (good signal).
> - Single-prospect concentration in Appraisal stage: largest engagement = $1.1M annualized (29% of stage value) · within tolerance.
>
> **Sr broker decisions for the week**: re-allocate one jr broker from prospecting to LOU-prep support given diligence backlog. Begin pre-marketing in retail-defense vertical to start diversifying medical concentration.
>
> **Pipeline view receipt**: `PIPELINE-SNAPSHOT-2026-05-24-06_00-firm` · anchored to Hedera within the firm-level weekly seal.

## DefendableOS Notes

- Pipeline math is the leading indicator the firm runs on. Sr brokers who run a clean pipeline at scale earn the right to scale their own books · pipeline discipline is one of the senior-management promotion criteria.
- The pipeline view is the closest thing to a "marketing-ops" surface in DefendableOS · but it's not run by marketing-ops, it's run by sr brokers from receipt math. The doctrine deliberately keeps pipeline ownership with the operators · not with a separate ops team.
- Vertical concentration is the most-watched risk metric at the firm-wide level. The PASS doctrine helps · we walk over-concentrated mandates · but proactive vertical diversification investment is the structural answer.
- The pipeline is published quarterly to customers · in aggregate form · as part of the firm's transparency commitment. Customers like seeing that the firm is well-funded by diversified pipeline · it's part of the trust layer.

🐝 *Pipeline today is revenue six months out. Pipeline quality today is retention three years out.*
