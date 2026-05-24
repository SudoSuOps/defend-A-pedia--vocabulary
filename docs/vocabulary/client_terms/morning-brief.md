# Morning Brief

## Street Definition

"Did the Morning Brief land?" — the sr broker asks at the 07:00 standup.

The **Morning Brief** is the daily 06:00 client-facing reconciliation email. One page. Three numbers. Today's dial · today's actions · today's anomalies. Lands in the principal's inbox before the coffee. Lands every day · including weekends and holidays unless explicitly paused.

If the Morning Brief doesn't land · the engagement is not running. The cadence is the discipline. The discipline is the trust.

## CRE Operator Meaning

A sr broker in CRE runs a Friday pipeline brief and a Monday huddle for the team · plus a per-client weekly call cadence. The discipline is constancy. You don't skip the Friday brief because nothing happened · you write "no material moves this week · holding the line" and you send it. The principal is reassured by the cadence · not by the content fluctuation.

The same discipline applies to a 24/7 defense engagement · but the cadence is daily · not weekly · because the apparatus runs daily. The Morning Brief is the operator's daily proof-of-life. It says "we're here · we ran last night · here's what we saw · here's what we're doing today." No principal is left to wonder.

## DefendableOS Definition

The **Morning Brief** in DefendableOS is the daily principal-facing email · sent automatically at **06:00 ET** (or principal's preferred timezone) to all designated recipients per LOU §11. It is composed by the Defense Ops desk · reviewed by the sr broker on T3/T4 tiers · and delivered via the engagement's confirmed channel.

The Morning Brief has a fixed 6-slot format:

1. **Dial slot** · current Probability of Close · band · 7-day trajectory
2. **Volume slot** · 24-hour deed count · Honey rate · Propolis count · variance to 30-day baseline
3. **Cost slot** · rolling 7-day cost-to-mint actual · vs ceiling
4. **Action slot** · today's named action · with owner and ETA
5. **Anomaly slot** · any unusual events from the overnight Tribunal cron
6. **Receipt slot** · 1-3 sample deed IDs · with Hedera anchor links for principal verification

Constancy is sacred. The brief lands every day · including weekends · with the format intact. "Nothing material" is a valid action slot · saying so is part of the discipline.

## Backend Representation

```json
{
  "morning_brief.brief_id": {"type": "string", "primary_key": true},
  "morning_brief.engagement_id": {"type": "string", "fk": "engagement.engagement_id"},
  "morning_brief.brief_date": {"type": "date"},
  "morning_brief.sent_at": {"type": "timestamp"},
  "morning_brief.recipients": {"type": "string_array"},
  "morning_brief.dial_value": {"type": "float", "range": [0,1]},
  "morning_brief.dial_band": {"type": "enum"},
  "morning_brief.dial_7d_trajectory": {"type": "float"},
  "morning_brief.deed_count_24h": {"type": "integer"},
  "morning_brief.honey_rate_24h": {"type": "float"},
  "morning_brief.propolis_count_24h": {"type": "integer"},
  "morning_brief.cost_to_mint_7d_rolling": {"type": "float"},
  "morning_brief.cost_variance_to_ceiling_pct": {"type": "float"},
  "morning_brief.action_today": {"type": "string"},
  "morning_brief.action_owner": {"type": "string"},
  "morning_brief.action_eta": {"type": "date", "nullable": true},
  "morning_brief.anomalies": {"type": "jsonb_array"},
  "morning_brief.sample_deed_ids": {"type": "string_array"},
  "morning_brief.principal_open_confirmed": {"type": "boolean", "nullable": true},
  "morning_brief.principal_reply_count": {"type": "integer", "default": 0},
  "morning_brief.sr_broker_reviewed": {"type": "boolean"}
}
```

Schema files: `docs/schemas/morning_brief.schema.json`

## Client Explanation

The **Morning Brief** is your daily reconciliation email · in your inbox at 06:00. Every day. Including weekends. Including holidays.

It's one page. Six slots: the dial · the overnight volume · the cost · today's action · any anomalies · sample deed IDs you can verify on Hedera.

The brief is how you stay informed without having to ask. You should never have to wonder "where are we?" — the answer is in your inbox · 30 seconds of reading.

If we miss a Morning Brief · that's an operational failure on our side · and we'll tell you why in the next-day's brief. Constancy is the discipline.

You can pause the Morning Brief temporarily (vacation · acquisition window · etc) by writing to your sr broker. We default to ON · pausing is opt-out.

## Jr Broker Use

When you're the operator on the Morning Brief desk:

- **Compose the brief by 04:30 ET** for 06:00 delivery
- **Pull dial · volume · cost from the dashboard** · don't hand-compute (introduces drift)
- **Compose action slot personally** · the action slot is the only narrative slot · everything else is data
- **Anomaly slot must be NAMED if non-empty** · "minor issues" is not a valid entry · be specific or omit
- **Sample deed IDs must include valid Hedera anchors** · do a 30-second spot-check before sending
- **Get sr broker sign-off on T3/T4 briefs** (T1/T2 can ship without · but log the sign-off skipped)

If you miss the 06:00 window: send the brief with the actual send-time clearly noted · plus a 1-line "delivered late · operational miss" disclosure. Don't hide the miss.

## Sr Broker Use

The sr broker:

- **Reviews and approves T3/T4 briefs** before they go out (a 5-min review · not a redraft)
- **Owns the Friday brief enhancement** · the Friday brief includes the weekly sr-broker review (a 2-paragraph addendum)
- **Authors briefs during escalations** · YELLOW or below means the sr broker writes the brief personally · NOT the desk
- **Owns the post-brief follow-up** if the principal replies asking questions · the sr broker is on the next reply

The sr broker also handles **brief pause requests** · captures the pause reason · sets a calendar reminder to re-confirm pause status weekly · resumes when the principal signals.

## Tribunal Use

The Tribunal feeds the brief but doesn't approve it:

- The dial value · band · drivers come from the 2am Tribunal cron
- The deed counts come from the Tribunal verdict log
- The cost numbers come from the cost-to-mint accumulator
- The anomalies come from the Tribunal's rule-layer flags from the overnight grading

A brief that ships with stale data (older than 12 hours) triggers an operator_hygiene flag. Cadence + freshness together.

## Evidence Required

For a Morning Brief to be defensible:

- Sent on time (within 30 min of 06:00 target window for the engagement's timezone)
- All 6 slots populated (with valid "no material change" entries if applicable)
- Dial values match the dashboard at composition time
- Sample deed IDs resolve on Hedera within 60 seconds of spot-check
- Sr broker reviewed (T3/T4) · log entry captured
- Sent successfully to all recipients per LOU §11

A brief missing any of the above is logged as `OPERATIONAL_MISS` · counts against the monthly delivery SLA · disclosed in the next-day brief.

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **missed_send** | Brief not sent for a given calendar day | JELLY · operational miss · disclosed next day |
| **stale_data** | Brief composed with data older than 12 hours | JELLY · re-derive · re-issue with corrected numbers |
| **broken_anchor** | Sample deed ID cited but Hedera anchor doesn't resolve | PROPOLIS · trust breach · re-issue + investigate |
| **silent_anomaly** | Material event happened overnight · not surfaced in anomaly slot | PROPOLIS · trust breach · sr broker review |
| **format_drift** | Brief shipped without one or more required slots | JELLY · format restored next day · sr broker review |
| **principal_unsubscribed_quietly** | Principal removed from recipients without LOU §11 amendment | JELLY · audit failure · LOU amendment captured |

## Scoring Impact

- **assignment_success**: HIGH (cadence discipline is a strong predictor of engagement success rates)
- **repair_lift**: MEDIUM (the brief surfaces issues early → faster repair)
- **validator_confidence**: HIGH (the brief is the daily evidence trail of operator hygiene)
- **risk_temperature**: INVERSE (consistent briefs = low risk · missed briefs = elevated risk)
- **probability_of_close**: HIGH (cadence drives `operator_hygiene` driver = 10% of dial)
- **evidence_strength**: HIGH (the brief is a daily evidence artifact · audit-friendly)
- **cost_to_mint**: LOW (the brief is operator margin · amortized · negligible per-deed impact)

## Deed / Receipt Impact

- **Receipt fields touched**: every brief references 1-3 sample deeds for verification (those deeds are highlighted but not modified)
- **DDEED class impact**: the brief itself is NOT a DDEED (it's an operational artifact · not an attested output)
- **Books and records layer**: briefs are stored in L1 PostgreSQL + L3 NAS · 7-year retention · NOT anchored on Hedera (cost-prohibitive per-day)
- **5 Proofs touched**: indirectly · the brief surfaces evidence touching all 5 Proofs but doesn't itself carry them (it's the digest · not the deed)

## Related Terms

- [engagement](engagement.md) · the relationship the brief services
- [assignment](assignment.md) · the work surfaced in the brief
- [closing-statement](closing-statement.md) · the per-assignment artifact that closes the brief loop
- [principal](principal.md) · the brief recipient
- [probability-of-close](../scoring_terms/probability-of-close.md) · the dial in the brief's slot 1
- [pre-market-flight-sheet](pre-market-flight-sheet.md) · the pre-engagement document the brief operationalizes daily
- [letter-of-understanding](letter-of-understanding.md) · the contract that defines the brief cadence

## Example

> **Morning Brief · 2026-06-15 · 06:00 ET**
>
> To: Jane Smith (COO) · Mike Chen (CFO) · Dana Park (VP Eng) · ops-leadership@acmelogistics.com
>
> Engagement: ENG-DOV-LOGISTICS-ACME-0001 · T3 White-Glove
>
> ---
>
> **DIAL**: 0.78 · AMBER · TRACKING · trajectory -0.03 over 7 days
>
> **VOLUME**: 1,247 deeds in last 24h · Honey rate 89.7% · Propolis 0 · -1.2% vs 30-day baseline
>
> **COST**: $0.0049/deed rolling 7d · 88.2% under T3 ceiling
>
> **ACTION**: Sr broker (J. Reyes) deploying routing-tune on refund-decision path 2026-06-22 · projected to lift Honey rate back to 93% within 7 days post-deploy
>
> **ANOMALIES**: None overnight. One vendor-rubric reconciliation in flight (closes 2026-06-20).
>
> **RECEIPTS** (sample · verify on Hedera topic 0.0.10291838):
> - `DDEED-DOV-LOGISTICS-ACME-REFUND-000412-v1` · seq 8401247
> - `DDEED-DOV-LOGISTICS-ACME-INVOICE-000891-v1` · seq 8401249
> - `DDEED-DOV-LOGISTICS-ACME-REFUND-000413-v1` · seq 8401253
>
> ---
>
> Sr broker (J. Reyes) reviewed and approved at 04:47 ET. Founder cc · no action requested.
>
> Reply to ops@swarmandbee.ai for any questions · J. Reyes for relationship matters.

## DefendableOS Notes

- The brief is the daily proof-of-life. It's the operating discipline that makes the engagement feel managed · not "vendor-y." A principal who reads the brief feels in control.
- Constancy beats cleverness. Don't redesign the format every quarter · the principal's eye learns the layout · variance creates friction.
- A perfect brief is one the principal can scan in 30 seconds and feel updated. Anything that requires more than 30 seconds is too much. Push depth into the dashboard · keep the brief tight.
- The 06:00 ET ship time is calibrated to the founder's CRE-broker discipline · principals like to read with coffee · we mirror that. Adjust per principal's preferred timezone · don't force ours.

🐝 *Cadence is the discipline · discipline is the trust · trust is the engagement.*
