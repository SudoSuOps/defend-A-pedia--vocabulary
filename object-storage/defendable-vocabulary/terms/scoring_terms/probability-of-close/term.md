# Probability of Close

> *Schema-side definition for the dial. See [`sample_term_probability_of_close.md`](../../examples/sample_term_probability_of_close.md) for the full canonical 13-section example.*

## Street Definition

"What's the dial say?" — the sr broker asks at the Monday huddle.

**Probability of Close** is the operating dial · the broker's gut-plus-math number that says how likely the assignment is to land successfully. Number between 0 and 1. Updated nightly. Visible to the principal in the daily Morning Brief.

The dial is the engagement's pulse. A flat dial for too long is suspicious. A dial that moves but stays within the band is healthy breathing. A dial that crosses bands is a signal.

## CRE Operator Meaning

Every CRE shop runs a dial on every listing. Top brokers can call the dial within 10 minutes of touring a building. The discipline is the regular refresh · the cadence · the willingness to revise downward when the evidence demands it.

The dial drives the calendar. Green-band deals get weekly cadence. Amber-band deals get bi-weekly. Yellow-band deals get daily. Orange-band deals get founder-level attention. Red-band deals are workouts · open-line · same-day decisions.

In CRE the dial is the broker's accountability metric. We mirror that exactly · the dial is what the sr broker brings to the Friday brief.

## DefendableOS Definition

**Probability of Close** in DefendableOS is the modeled likelihood (float 0-1 · bucketed into 5 bands) that an active assignment lands in `CLOSED_HONEY` or `CLOSED_CONDITIONED` per the Assignment Success Doctrine. Updated nightly via the 2am Tribunal reconciliation cron · refreshed on-demand on material driver moves · surfaced in the Morning Brief and the dashboard.

Computed as a 6-driver weighted composite:
- `color_strength` · 25%
- `principal_motivation` · 20%
- `asset_condition` · 20%
- `buyer_pool_fit` · 15%
- `comp_quality` · 10%
- `operator_hygiene` · 10%

## Backend Representation

```json
{
  "scoring.probability_of_close": {
    "type": "float",
    "range": [0.0, 1.0],
    "precision": 2,
    "scoring_hook": "primary_dial",
    "refresh_cadence": "nightly_2am_cron_plus_on_demand"
  },
  "scoring.probability_of_close_band": {
    "type": "enum",
    "values": [
      "GREEN_LOCKED",      
      "AMBER_TRACKING",   
      "YELLOW_WATCHLIST", 
      "ORANGE_ESCALATION",
      "RED_DARK"          
    ],
    "derivation_rule": {
      "GREEN_LOCKED":      "0.85 <= value <= 1.00",
      "AMBER_TRACKING":    "0.65 <= value <  0.85",
      "YELLOW_WATCHLIST":  "0.45 <= value <  0.65",
      "ORANGE_ESCALATION": "0.25 <= value <  0.45",
      "RED_DARK":          "0.00 <= value <  0.25"
    }
  },
  "scoring.probability_of_close_drivers": {
    "type": "jsonb",
    "shape": "{driver_name: {value: float 0-1, weight: float, last_updated: timestamp, evidence_count: int}}"
  },
  "scoring.probability_of_close_escalation_status": {
    "type": "enum",
    "values": ["NONE", "SR_BROKER_NOTIFIED", "FOUNDER_NOTIFIED", "FOUNDER_ENGAGED"],
    "auto_set_by_rule_layer": true
  }
}
```

Schema files: `docs/schemas/dial.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

Your engagement carries a daily **Probability of Close** dial. It's a number between 0 and 1 · refreshed every night · surfaced in your 06:00 Morning Brief.

- 0.85+ means we're locked in
- 0.65-0.84 means we're tracking but watching specific drivers
- 0.45-0.64 means we're on the watchlist
- 0.25-0.44 means we escalate to founder
- Below 0.25 means we go dark and tell you same-day

The dial isn't a vibe · it's 6 weighted drivers · audit-trail behind each one. You see the dial · you see the band · you see the trajectory · you see what moved it · you see what we're doing about it. No spin.

## Jr Broker Use

- Check the dial every morning before reading the Morning Brief · know the number by 07:00
- Log every driver change · the dial is only as good as the inputs
- Watch for 5-point movements · any change > 0.05 in 24 hours triggers same-day sr broker review
- Don't try to "save" the dial by withholding bad inputs · honest down-movements keep the calibration honest
- If the dial drops two bands · escalate within 4 hours · don't wait

## Sr Broker Use

- Friday weekly dial review across the entire book
- Cross-engagement comp analysis when patterns emerge
- Annual calibration discipline (annual `DDEED-{org}-CALIB-{year}-v1` issued)
- Principal-call discretion (when to escalate from email to voice · when to involve founder · when to call a PASS-pivot)
- Override authority with logged justification (rare · always documented)

## Tribunal Use

The Tribunal grades the inputs · the dial composes them. Rule-layer flags:
- Single-day drop > 0.20 → `dial_anomaly_flag` for QA validator
- Dial below 0.50 for > 7 consecutive days → automatic `engagement_health_check` deed
- Drift > 0.15 between Scale A and Scale B judges on `asset_condition` inputs → manual review
- Dial < 0.25 caps any new deed at JELLY tier (cannot issue HONEY · cannot issue Royal Jelly while RED)

## Evidence Required

- Color file with ≥ 5 independent sources per the color doctrine
- ≥ 14 days of cost-to-mint history
- Assignment brief with numeric · time-bound criteria
- Principal engagement log (every touch · date · channel · outcome)
- ≥ 3 daily snapshots before the dial is considered stabilized (newer = `provisional`)
- Validator chain pass results from the last 7 days

## Failure Modes

| Mode | Tribunal class |
|---|---|
| `inflated_dial` (boosted without evidence) | PROPOLIS |
| `stale_dial` (> 72 hours since refresh) | JELLY |
| `silent_drop` (moved > 0.10 without explanation captured) | JELLY |
| `principal_blindside` (moved 2+ bands without principal notification per escalation pyramid) | PROPOLIS |
| `spin_dial` (briefed with language inconsistent with band) | PROPOLIS |
| `comp_starved_dial` (GREEN band shown with comp_quality < 0.30) | JELLY |

## Scoring Impact

- **assignment_success**: HIGH (leading indicator of the boolean)
- **repair_lift**: LOW (dial is a measurement · not a thing to be repaired)
- **validator_confidence**: HIGH (provisional dials flagged in dashboard)
- **risk_temperature**: INVERSE (low dial = high risk · feeds escalation pyramid)
- **probability_of_close**: SELF
- **evidence_strength**: HIGH (dial cannot pencil without strong evidence stacks)
- **cost_to_mint**: MEDIUM (running the apparatus costs energy · but missing dial costs more)

## Deed / Receipt Impact

- Every Tribunal verdict feeds `asset_condition` driver → indirectly touches every receipt
- Dial < 0.25 (RED) caps deed issuance at JELLY
- Annual calibration deed `DDEED-{org}-CALIB-{year}-v1` carries dial vs outcome variance
- Books-and-records: L1 + L3 daily snapshots · L4 Hedera only on calibration deed (not daily snapshots · cost-prohibitive)
- 5 Proofs touched: ECONOMICS · PROCESS · TRUST

## Related Terms

- [assignment-success](assignment-success.md) · what the dial predicts
- [client-confidence](client-confidence.md) · the symmetric principal-side dial
- [color](../cre_terms/color.md) · the 25% driver
- [morning-brief](../client_terms/morning-brief.md) · the daily surfacing
- [pre-market-flight-sheet](../client_terms/pre-market-flight-sheet.md) · the pre-engagement basis for the dial
- [pass-doctrine](../client_terms/pass-doctrine.md) · the intake filter that prevents low-dial engagements
- [closing-statement](../client_terms/closing-statement.md) · the post-close artifact that calibrates the dial

## Example

> Engagement: ENG-DOV-LOGISTICS-ACME-0001
>
> Dial trajectory last 14 days: 0.81 → 0.79 → 0.79 → 0.78 → 0.78 → 0.77 → 0.78
>
> Band: AMBER · TRACKING
>
> Drivers:
> - color_strength 0.88 (UP) · principal_motivation 0.85 · asset_condition 0.79 (DOWN) · buyer_pool_fit 0.86 · comp_quality 0.72 · operator_hygiene 0.62 (DOWN)
>
> Composite: 0.78
>
> See [`sample_term_probability_of_close.md`](../../examples/sample_term_probability_of_close.md) for the full worked example.

## DefendableOS Notes

- The dial is the engagement's pulse. Healthy engagements breathe (within-band movement); the cross-band move is the signal.
- The dial maps directly to "make the dial · build the math · eat the fees." It's the chant made operational.
- Never publish dials externally. Operator + principal information only.
- The annual calibration is what makes the dial credible · without it the dial is theater.

🐝 *The dial is the pulse · the pulse is the deal.*
