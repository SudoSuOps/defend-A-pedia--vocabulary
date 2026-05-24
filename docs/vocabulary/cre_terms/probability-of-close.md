# Probability of Close

## Street Definition

"What's our probability of close on this one?" — sr broker, dialing into the Friday listing walk.

**Probability of close** (PoC) is the close-probability dial. The single number, between 0 and 1, that captures the firm's expected likelihood that an engagement will reach signed PSA from its current pipeline stage. It's the dial on every UI surface that matters · the operator's compass, the sr broker's reading, the board's leading indicator.

In CRE, the sr broker calculates PoC in their head from 30 years of patterns. In DefendableOS, PoC is a numeric dial computed from receipts · color score, validator status, stage history, customer engagement signals, comparable deal physics · and updated continuously. The math doesn't replace the broker instinct · it makes the instinct legible to the dashboard.

## CRE Operator Meaning

CRE sr brokers carry a running estimate of PoC for every active listing. The estimate is informed by:

- **Stage of negotiation** · pre-LOI vs post-LOI vs in-diligence vs in-PSA
- **Counterparty motivation** · 1031 deadline · partnership dispute · refi expiring · etc.
- **Counterparty financial capacity** · funded vs not · approved vs pending
- **Color depth** · how well we understand the asset · the seller · the buyer pool
- **Re-trade history** · clean vs re-priced vs re-papered
- **Comp pattern** · how similar deals at similar stage closed historically
- **Broker relationship depth** · 30-year relationship vs first deal together
- **Market state** · capital availability · cap rate trajectory · supply pipeline

A sr broker reading a $40M industrial NNN deal at LOI stage might say "67% probability of close · with the seller's 1031 deadline 73 days out, color built clean, buyer's lender pre-approved, no re-trades to date, comp pattern says we close at 71% from this configuration." That's the kind of reading PoC captures · numerically · with the math behind every input traceable.

## DefendableOS Definition

In DefendableOS, **Probability of Close** is the canonical engagement-level dial computed from receipt-anchored inputs. PoC is updated continuously as the underlying inputs change · color score refresh · validator chain run · re-trade events · sit-signal updates · vendor changelog drops · customer-engagement signal shifts.

The dial appears on every operator-facing surface and on selected customer-facing surfaces (with appropriate framing). The math behind the dial is open · any operator can drill into any PoC value and see the inputs that produced it. Auditors can verify PoC via the same drill-down.

### Deal physics: the inputs that drive PoC

PoC is a function of multiple receipt-anchored inputs · the "physics" of the deal. The weighting evolves as the firm learns from closed engagements, but the canonical input set is:

1. **Stage base rate** · the historical close rate from this stage to PSA (e.g., LOU signed → PSA = 88% baseline, Appraisal delivered → PSA = 33% baseline)
2. **Color score** · `color_score` from the engagement's color file (range 0.0-1.0, weighted 0.85+ as healthy)
3. **Validator chain status** · 7 critical checks pass count · 5 advisory checks status
4. **Counterparty motivation score** · explicit deadlines, prior pain events, regulatory triggers
5. **Counterparty financial capacity** · approved budget · CFO endorsement · funding source verified
6. **Re-trade count** · 0 is healthy · 1 is yellow · 2+ is red
7. **Dwell time vs expected** · stage dwell within p50 is healthy · approaching p90 is yellow · beyond p90 is red
8. **Sit-signal strength** · last sit attendance · principal vs delegate · post-sit reply velocity
9. **Vertical pattern match** · how this engagement compares to recent closed engagements in same vertical
10. **Walk-away risk** · how close current dynamics are to known PASS triggers

### How the math composes

PoC = `stage_base_rate × color_multiplier × validator_multiplier × motivation_multiplier × capacity_multiplier × retrade_multiplier × dwell_multiplier × sit_signal_multiplier × pattern_match_multiplier × (1 - walk_away_risk)`

Each multiplier is in [0.5, 1.2] range · meaning any single input can knock PoC down by half (catastrophic) or boost it modestly (no single input can overstate PoC). The PoC is bounded by `[0.05, 0.97]` · we never claim certainty.

## Backend Representation

```json
{
  "engagement.probability_of_close": {
    "type": "float",
    "range": [0.0, 1.0],
    "scoring_hook": "engagement_poc_v1",
    "ui_dial": true
  },
  "engagement.poc_inputs_v1": {
    "type": "jsonb",
    "fields": {
      "stage_base_rate": "float",
      "color_multiplier": "float",
      "validator_multiplier": "float",
      "motivation_multiplier": "float",
      "capacity_multiplier": "float",
      "retrade_multiplier": "float",
      "dwell_multiplier": "float",
      "sit_signal_multiplier": "float",
      "pattern_match_multiplier": "float",
      "walk_away_risk": "float"
    }
  },
  "engagement.poc_last_recomputed_at": {
    "type": "timestamp"
  },
  "engagement.poc_history": {
    "type": "jsonb_array",
    "comment": "Time-series for trend analysis"
  }
}
```

Schema files: `docs/schemas/probability_of_close.schema.json` · `docs/schemas/engagement.schema.json` · `docs/ui_dials/probability_of_close.md`

## Client Explanation

Probability of Close is the dial on our operator dashboard that tells us how likely an engagement is to reach signed PSA from its current state. It is not a marketing number · it is a computed value from a set of receipt-anchored inputs (color quality, validator status, your team's signaled engagement, counterparty financial readiness, and how similar engagements have progressed in our prior experience). We share PoC with you on selected surfaces · the Morning Brief for active engagements, the renewal-review dashboard for renewing customers · because we want you to see how we're reading the relationship in real time. Anytime PoC moves materially, you'll see the inputs that drove the move · we don't hide the math behind the dial.

## Jr Broker Use

You feed PoC. Every receipt you log, every color refresh you run, every re-trade event you document · updates the dial. The dial is your daily scoreboard.

- **Read your dial every morning.** First thing. Engagements where PoC dropped overnight get diagnosed before the day's dial block starts.
- **Diagnose PoC drops same-day.** If PoC dropped from 0.62 to 0.41 overnight, drill into which input multiplier moved. Did the customer's CFO leave? Did the vendor drop a changelog? Did a re-trade get logged you forgot to mention to sr broker? Same-day diagnosis.
- **Never game the dial.** Stage-stuffing to inflate stage_base_rate, fabricating color sources to inflate color_multiplier, hiding re-trades to inflate retrade_multiplier · these are all PROPOLIS-tier doctrine violations. The PoC is only useful if the inputs are clean.
- **Use PoC to prioritize.** When you have 12 active prospects and 6 hours of working time, you prioritize the ones where PoC is high-and-rising (real opportunity) or low-and-droppable (PASS candidates · close them out so they stop bloating the pipeline). You don't waste hours on flat middling PoCs unless there's a specific reason.

## Sr Broker Use

You read PoC as a portfolio. Same way a CRE sr broker reads a 12-asset listing book · which engagements are close to closing, which are stalled, which are below the PASS threshold and should be walked.

- **Friday walk PoC review.** Every active engagement walked. PoC trajectory over the week noted. Anything trending down hard gets a workout-plan discussion.
- **Walk-away threshold enforcement.** Any engagement with PoC < 0.20 sustained for 14+ days · candidate for PASS · sr broker decides cull or invest. The PASS doctrine is what protects pipeline-conversion math from being eaten by long-tail wishful prospects.
- **PoC outlier investigation.** Engagements with PoC > 0.85 deserve attention too · is the dial right? Anything that would be a surprise PASS? Pre-close discipline.
- **PoC math audit quarterly.** The multiplier weights evolve as the firm learns from closed engagements. SH3 (Tribunal Architect) and SH5 (Client Language Specialist) own the weight-update cycle · sr brokers participate in quarterly review of the math.

## Tribunal Use

PoC itself is Tribunal-scored · because the dial only works if the inputs feeding it are clean.

- **Rule layer**: PoC inputs missing or stale → critical_failure → dial value invalid until refreshed
- **Rule layer**: any input multiplier outside [0.5, 1.2] range → critical_failure → math anomaly · investigate
- **Rule layer**: PoC value outside [0.05, 0.97] bound → critical_failure → math broken · halt and audit
- **Judge layer**: PoC accuracy retroactively scored against actual close outcomes · the firm's overall PoC calibration tracked as a leading indicator of operational discipline
- **Classification impact**: well-calibrated PoC dials (predicted close-rate matches actual close-rate within ±5%) → Honey · poorly calibrated dials → Jelly · gamed dials (inputs fabricated to bias outputs) → Propolis

```yaml
classification_impact: [HONEY, ROYAL_JELLY, JELLY, PROPOLIS]
can_be_critical_failure: true
rule_layer_checks:
  - all PoC input multipliers present and in range
  - PoC value in [0.05, 0.97] bound
  - PoC last-recomputed timestamp within 24h for active engagements
  - input source receipts resolve and validate
```

## Evidence Required

- All input multiplier source receipts present and validate
- PoC history time-series persisted (for retroactive calibration analysis)
- Recompute trigger events logged (which event triggered the most recent recompute)
- Calibration reports persisted quarterly (predicted vs actual close-rates by stage)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **stage_stuffing_inflation** | Engagement moved to higher stage without trigger event → inflated stage_base_rate | PROPOLIS |
| **fabricated_color** | Color sources fabricated → inflated color_multiplier | PROPOLIS |
| **hidden_retrade** | Re-trade event not receipted → retrade_multiplier stays unjustifiably high | PROPOLIS |
| **stale_inputs** | PoC computed from inputs > 7 days old | JELLY |
| **broken_multiplier_bounds** | Multiplier value outside [0.5, 1.2] range | JELLY (PROPOLIS if persistent) |
| **mis_calibrated_baseline** | Stage base rate not updated against actual close-rates quarterly | JELLY |
| **overconfident_ceiling** | PoC reported > 0.97 (claiming near-certainty) | JELLY |
| **fatalistic_floor** | PoC reported < 0.05 on engagement still in active dialog | JELLY (PASS candidate · not zero) |

## Scoring Impact

- **assignment_success**: TERMINAL · PoC IS the engagement-success leading indicator
- **repair_lift**: HIGH · workout plans aimed at lifting specific input multipliers can materially lift PoC
- **validator_confidence**: HIGH · PoC inputs are validator-chain-anchored
- **risk_temperature**: INVERSE-CORRELATED · low PoC = elevated risk profile, by design
- **probability_of_close**: SELF · this term IS the dial
- **evidence_strength**: HIGH · PoC math is one of the most-cited receipt artifacts at the engagement level
- **cost_to_mint**: LOW · PoC computation is cheap · gaming the dial is catastrophically expensive in trust damage when caught

## Deed / Receipt Impact

- **Receipt fields touched**: `poc_value`, `poc_inputs_v1`, `poc_recomputed_at`, `poc_history` (trend); deed-level: `poc_at_lou`, `poc_at_psa`, `poc_actual_close_outcome`
- **DDEED class impact**: deeds include the PoC at LOU and at PSA as part of the engagement-origination provenance · enables retrospective calibration analysis
- **Books and records layer**: L1_PG (live dial) → L2_MERKLE (snapshot at stage transitions) → L3_NAS (full history archive) → L4_HEDERA (calibration reports anchored quarterly)
- **5 Proofs touched**: PROCESS (engagement physics) · QUALITY (input integrity) · ECONOMICS (forward revenue) · TRUST (open math to customer)

## Related Terms

- [deal-flow](deal-flow.md) · pipeline rolls up PoC across all active engagements
- [color](color.md) · color score is one of the input multipliers
- [digest](digest.md) · digests cite current PoC for the engagement
- [loi](loi.md) · LOU sign is a major PoC inflection event
- [psa](psa.md) · PSA sign is the terminal close event PoC predicts
- [due-diligence](due-diligence.md) · diligence outputs update multiple PoC multipliers
- [underwriting](underwriting.md) · underwriting math interacts with PoC scoring
- [books-and-records](books-and-records.md) · PoC history is anchored alongside engagement deeds

## Example

> **Engagement**: cold-storage operator · prior PASS (2025-11) · returned hurt (2026-05) · currently at LOU signed stage (LOU executed 2026-05-22).
>
> **PoC at LOU signed (2026-05-22 16:00 ET)**: 0.83
>
> **Input multipliers at LOU sign**:
> - `stage_base_rate`: 0.88 (LOU → PSA historical rate)
> - `color_multiplier`: 1.10 (color score 0.91 · top decile)
> - `validator_multiplier`: 1.05 (first-pass clean on 13/14 agents)
> - `motivation_multiplier`: 1.15 (hurt-customer return · documented prior PASS · clear pain)
> - `capacity_multiplier`: 1.05 (CFO endorsement · budget approved)
> - `retrade_multiplier`: 1.00 (no re-trades during LOU draft)
> - `dwell_multiplier`: 1.00 (median dwell for the stage)
> - `sit_signal_multiplier`: 1.10 (principal-led conversations · fast reply velocity)
> - `pattern_match_multiplier`: 1.00 (typical for vertical and size)
> - `walk_away_risk`: 0.05 (low · the disclosure clause and PASS clause are signed · risk is residual)
>
> **PoC during diligence (2026-06-08, mid-diligence)**: 0.79
>
> **Why the drop**: agent-09 logging-tooling vendor drift surfaced. `validator_multiplier` dropped from 1.05 to 0.95. `walk_away_risk` rose from 0.05 to 0.09. PoC dropped accordingly. Sr broker reviewed · workout plan added · PoC stabilized at 0.79 with workout-plan-clause baked into PSA.
>
> **PoC at PSA signed (2026-06-12 16:00 ET)**: 1.00 (terminal · close event reached)
>
> **Actual outcome**: PSA signed on schedule. Calibration data point logged: at LOU PoC of 0.83 with the input profile above, this engagement closed. Will inform future weight updates for hurt-customer-return engagement pattern.
>
> **Receipt ID for PoC history**: `POC-HISTORY-COLD-ATL-000088-2026-05-22-to-2026-06-12` · anchored to Hedera within the engagement's PSA-anchor batch.

## DefendableOS Notes

- PoC is the most-watched dial in the firm. Sr brokers refresh it mentally throughout the day; jr brokers refresh it operationally every morning. The discipline is what makes the dial meaningful.
- Customer-facing PoC display is selective · we don't expose it on prospect-facing surfaces (avoid creating PoC-as-pressure-tactic on engaged prospects), but we do expose it on active and renewal engagements where it serves the trust layer.
- PoC calibration analysis quarterly is the firm's self-audit · we hold ourselves to the same evidence discipline we apply to customer deeds. If our PoC math has drifted, we publish the calibration report and update the weights · same transparency we ask of our customers.
- Gaming the PoC dial is the single fastest way off the ladder. The firm's pipeline math depends on PoC integrity · any input fabrication is a PROPOLIS-tier event with immediate consequences.
- The PoC dial is the working example of how vocabulary, schema, scoring, and UI converge in DefendableOS · same word that's in the broker's head is the field in the database is the value on the dashboard. No translation. No drift.

🐝 *The dial is the truth · only if the inputs are clean. Read it. Diagnose it. Walk when it tells you to walk.*
