# Probability of Close

> *Second canonical example of the 13-section structure. Use alongside [`sample_term_color.md`](sample_term_color.md) as a reference shape for any scoring or dial term.*

## Street Definition

"Where's the dial on this one?" — a sr broker asks at the Monday morning huddle.

**Probability of Close** is the broker's gut-plus-math number that says how likely a given deal is to close. In CRE it's a percentage · a band · a color · whatever shorthand the desk uses. Greenshore broker says "85% locked." Distressed-asset broker says "this one's in the freezer." Either way · the number drives the calendar · the calls · and the escalation.

If you don't have a dial on the deal · you don't have the deal.

## CRE Operator Meaning

A sr broker reads a CRE Probability of Close off six signals:

- **Color strength** · what's verifiably true about the asset
- **Seller motivation** · 1031 clock · refi expiring · partnership dispute · age-out
- **Asset condition** · physical · financial · legal
- **Buyer pool fit** · who's in the market · who's funded · who's ready
- **Comp quality** · how many recent comps support the asking
- **Operator hygiene** · whether the listing team is running the deal clean

A new dial is a guess. A 30-day dial is a forecast. A 90-day dial · backed by 90 days of weekly evidence · is a number the firm books to. The discipline is the regular refresh · the cadence · the willingness to revise downward when the evidence demands it.

## DefendableOS Definition

In DefendableOS · **Probability of Close** is the modeled likelihood that an open engagement assignment lands in CLOSED · HONEY or CLOSED · CONDITIONED per the Assignment Success Doctrine. It is a float between 0.00 and 1.00 · bucketed into 5 UI bands · refreshed nightly by the Tribunal during the 2am reconciliation cron · and surfaced to the principal in the daily 06:00 Morning Brief.

The dial maps to the 5 Proofs by drawing inputs from all of them: Origin (which agent · which model · which strategy) · Quality (Tribunal pass rate) · Process (color file maturity) · Economics (cost-to-mint hygiene) · Trust (validator confidence). It is the single most important operating number in any active engagement.

## Backend Representation

```json
{
  "engagement.probability_of_close": {
    "type": "float",
    "range": [0.0, 1.0],
    "precision": 2,
    "scoring_hook": "primary_dial"
  },
  "engagement.probability_of_close_band": {
    "type": "enum",
    "values": ["GREEN_LOCKED", "AMBER_TRACKING", "YELLOW_WATCHLIST", "ORANGE_ESCALATION", "RED_DARK"],
    "derived_from": "probability_of_close"
  },
  "engagement.probability_of_close_drivers": {
    "type": "jsonb",
    "shape": {
      "color_strength": "float 0-1 · weight 0.25",
      "principal_motivation": "float 0-1 · weight 0.20",
      "asset_condition": "float 0-1 · weight 0.20",
      "buyer_pool_fit": "float 0-1 · weight 0.15",
      "comp_quality": "float 0-1 · weight 0.10",
      "operator_hygiene": "float 0-1 · weight 0.10"
    }
  },
  "engagement.probability_of_close_history": {
    "type": "jsonb_array",
    "schema": "timestamped daily snapshots · 365 day rolling retention"
  },
  "engagement.probability_of_close_last_refresh_at": {
    "type": "timestamp"
  },
  "engagement.probability_of_close_escalation_status": {
    "type": "enum",
    "values": ["NONE", "SR_BROKER_NOTIFIED", "FOUNDER_NOTIFIED", "FOUNDER_ENGAGED"],
    "auto_set_by": "rule_layer"
  }
}
```

Schema files: `docs/schemas/engagement.schema.json` · `docs/schemas/dial_history.schema.json`

## Client Explanation

The **Probability of Close** is our broker's-honest read on how likely your assignment is to land successfully. It's a number between 0 and 1 · refreshed every night · shown to you in your 06:00 Morning Brief.

We treat it like a CRE listing dial: 0.85-1.00 means we're locked in · 0.65-0.84 means we're tracking but watching specific drivers · 0.45-0.64 means we're on the watchlist and your sr broker is on the desk daily · 0.25-0.44 means we need to talk with the founder · below 0.25 means we go dark and we tell you same-day.

The dial isn't a guess. It's six drivers · weighted · audit-trail behind every one of them. If the dial moves · we tell you why · we tell you what we're doing about it · and we tell you the expected timeline back. No spin. No hedge.

## Jr Broker Use

When you're on an active engagement:

- **Check the dial every morning** before you open the Morning Brief. If you don't know the number off the top of your head by 07:00 · you're not running your book.
- **Log every driver change** to the dial. If a color source got added or downgraded · you update the driver score. If the principal went quiet · you flag motivation. The dial is only as good as the inputs.
- **Watch for 5-point movements**. Any change > 0.05 in a 24-hour window triggers a same-day sr broker review.
- **Don't try to "save" the dial** by withholding bad inputs. Honest down-movements are how the system stays calibrated. Spin breaks the calibration · which breaks the principal's trust.
- **If the dial drops two bands**, you don't wait for the sr broker · you escalate within 4 hours.

## Sr Broker Use

The sr broker owns the dial. Specifically:

- **Weekly dial review** every Friday · across the entire book
- **Cross-engagement comp analysis** · if 3 engagements drop the dial in the same week with the same driver underwater · we look at our own apparatus · not the client's
- **Calibration discipline** · the annual calibration report compares dial predictions to actual outcomes · the sr broker authors the analysis · the formula gets revised if needed
- **Principal-call discretion** · the sr broker decides when to escalate from email to voice · when to escalate to founder · when to call a PASS-pivot conversation
- **Override authority** · the sr broker can manually pin a dial value if they have signal the model isn't capturing · but every override is logged with a justification deed

The sr broker also handles disagreements. When a principal says "your dial is too low · here's why I think we're locked" · the sr broker LISTENS · captures the signal · and either revises the dial or explains why the model holds.

## Tribunal Use

The Tribunal treats the dial as a derived output · not a primary classification. Specifically:

- **Rule layer**: any single-day drop > 0.20 triggers a `dial_anomaly_flag` for QA validator review
- **Rule layer**: any dial sitting below 0.50 for > 7 consecutive days triggers an automatic `engagement_health_check` deed
- **Judge layer**: NOT graded by the Tribunal directly (the Tribunal grades the inputs · the dial composes them)
- **Drift check**: Scale A vs Scale B judges drift > 0.15 on the underlying Tribunal verdicts feeding `asset_condition` driver → flag for manual review
- **Classification impact**: A dial < 0.25 (RED · DARK) caps any new deed at JELLY tier · cannot issue HONEY or Royal Jelly while the engagement is dark

The Tribunal never publishes the dial publicly. The dial is operator + principal information only.

## Evidence Required

For a dial to be defensible · the engagement record must include:

- A `color_file` referenced via `color_file_id` · with ≥ 5 independent sources (per the color doctrine)
- A `cost_to_mint_history` with ≥ 14 days of per-deed cost data
- An `assignment_brief` with numeric · time-bound success criteria
- A `principal_engagement_log` capturing every principal touch (date · channel · outcome)
- ≥ 3 daily snapshots before the dial is considered "stabilized" (newer than 3 days = `provisional`)
- Validator chain pass results from the last 7 days (≥ 7 of 12 critical checks passing)

A dial with missing evidence is rendered as `--` in the UI (NEVER as a number) and flagged in the Morning Brief.

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **inflated_dial** | Driver scores manually boosted without evidence | PROPOLIS · sr broker authority revoked pending review |
| **stale_dial** | Last refresh > 72 hours · UI still showing old number | JELLY · auto-flagged · refresh forced |
| **silent_drop** | Dial moved > 0.10 but no driver explanation captured | JELLY · escalation auto-triggered |
| **principal_blindside** | Dial moved 2+ bands and principal was not notified within escalation window | PROPOLIS · trust breach · sr broker review |
| **spin_dial** | Dial briefed to principal with language that doesn't match the band (e.g., "we're locked" at 0.71 amber) | PROPOLIS · relationship-level severity |
| **comp_starved_dial** | Dial reported with comp_quality driver < 0.30 but the band shown is GREEN | JELLY · forced amber until comps improve |

## Scoring Impact

- **assignment_success**: HIGH · the dial is the leading indicator of the boolean
- **repair_lift**: LOW · the dial is a measurement · not a thing to be repaired (its inputs are repaired separately)
- **validator_confidence**: HIGH · validator-pending dials are flagged provisional · the dashboard surfaces this
- **risk_temperature**: INVERSE · low dial = high risk temp · feeds the escalation pyramid
- **probability_of_close**: SELF · the dial IS probability of close · referenced reflexively
- **evidence_strength**: HIGH · the dial cannot pencil without strong evidence stacks across drivers
- **cost_to_mint**: MEDIUM · running the apparatus to compute the dial costs energy · but a missing dial costs more (relationship breaks · principal trust erodes · rework escalates)

## Deed / Receipt Impact

- **Receipt fields touched**: every Tribunal verdict feeds the `asset_condition` driver · so every receipt indirectly touches the dial
- **DDEED class impact**: dial < 0.25 (RED) caps any new deed at JELLY · cannot issue HONEY · cannot issue Royal Jelly
- **Calibration deed**: annual `DDEED-{org}-CALIB-{year}-v1` carries the dial vs outcome variance for the year
- **Books and records layer**: L1 PostgreSQL (live) · L3 NAS (daily snapshot) · L4 Hedera HCS (calibration deed only · NOT every daily snapshot · would be cost-prohibitive)
- **5 Proofs touched**: ECONOMICS (drives engagement-tier conversation) · PROCESS (the lineage of color + dial drivers) · TRUST (the validator confidence backing it)

## Related Terms

- [color](../vocabulary/cre_terms/color.md) · the 25% driver
- [assignment-success](../vocabulary/scoring_terms/assignment-success.md) · what the dial predicts
- [client-confidence](../vocabulary/scoring_terms/client-confidence.md) · the symmetric dial measuring the principal's confidence in US
- [morning-brief](../vocabulary/client_terms/morning-brief.md) · the daily surfacing channel
- [pre-market-flight-sheet](../vocabulary/client_terms/pre-market-flight-sheet.md) · the pre-engagement version of the dial story
- [pass-doctrine](../vocabulary/client_terms/pass-doctrine.md) · the intake filter that prevents low-dial engagements from opening in the first place
- [closing-statement](../vocabulary/client_terms/closing-statement.md) · the post-close artifact that verifies the dial

## Example

> **Engagement**: Acme Logistics · T3 White-Glove · invoice-reconciliation agent + refund-decision agent · LOU 2026-03-12 · 2 assignments in flight.
>
> **Dial trajectory** (last 14 days):
> 0.81 → 0.79 → 0.79 → 0.78 → 0.78 → 0.77 → 0.78 (today)
>
> **Band**: AMBER · TRACKING
>
> **Drivers**:
> - color_strength · 0.88 (UP · +2 EDGAR sources added)
> - principal_motivation · 0.85 (steady · principal answering same-day)
> - asset_condition · 0.79 (DOWN · 3 Propolis events on non-critical paths)
> - buyer_pool_fit · 0.86 (steady · workflow fit confirmed)
> - comp_quality · 0.72 (steady · 4 comp engagements available)
> - operator_hygiene · 0.62 (DOWN · cost-to-mint at 108% of ceiling 3 of last 4 weeks)
>
> **Composite**: (0.88 × 0.25) + (0.85 × 0.20) + (0.79 × 0.20) + (0.86 × 0.15) + (0.72 × 0.10) + (0.62 × 0.10) = 0.78
>
> **Morning Brief slot (verbatim)**:
> ```
> PROBABILITY OF CLOSE · 0.78 · AMBER · TRACKING
>
> UP: Color file added 2 EDGAR confirmations · principal completed all
>     diligence items same-day.
> DOWN: Cost-to-mint at 108% of ceiling 3 of last 4 weeks · driven by
>       a routing inefficiency on the refund-decision path.
> ACTION: Sr broker (J. Reyes) re-tuning routing strategy by 2026-06-22 ·
>         revised projection in Thursday Morning Brief.
> ```
>
> **Sr broker action**: scheduled 30-min call with principal Thursday to walk the cost variance + remediation. Founder cc'd but not on the call.
>
> **Outcome 7 days later**: routing tune deployed · cost-to-mint back to 99% of ceiling · operator_hygiene driver recovered to 0.81 · composite dial moved to 0.82 · still amber but trajectory positive.

## DefendableOS Notes

- The dial is the engagement's pulse. A flat dial for too long is suspicious · a healthy engagement breathes (movement within the band is normal · movement across bands is the signal).
- The dial maps directly to the M&M operator cadence · "make the dial · build the math · eat the fees." The dial IS the dial in that chant. The fees follow.
- Comps starvation is a structural risk for any new vertical we enter. We track this explicitly · and we widen the confidence interval on dials in low-comp domains rather than pretending we have signal we don't.
- The dial is what makes the engagement defendable. A no-dial engagement is a vendor relationship. A live-dial engagement is a broker relationship. The difference is everything.

🐝 *The dial is the pulse · the pulse is the deal · the deal is the receipt.*
