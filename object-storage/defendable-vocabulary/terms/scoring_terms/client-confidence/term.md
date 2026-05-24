# Client Confidence

## Street Definition

"How confident is the principal?" — the founder asks the sr broker before scheduling any QBR.

**Client Confidence** is the symmetric dial · measuring how confident the PRINCIPAL is in OUR engagement · separate from how confident WE are in the validator chain. The validator-confidence dial measures the apparatus. The client-confidence dial measures the relationship.

Both dials matter. A high validator-confidence + low client-confidence engagement is a relationship at risk · regardless of how well the work is grading. A healthy engagement carries both dials above 0.70.

## CRE Operator Meaning

A sr broker in CRE knows the deal can pencil mathematically AND still die from low client confidence. The seller can be right · the comps can support · the buyer pool can be deep · and the seller can still pull the listing because they lost confidence in the broker.

The healthy CRE broker tracks both metrics implicitly: the deal-math (is this trade close-able) AND the client-pulse (does the principal still believe in me · in my team · in my recommendation). When the client-pulse dies · the deal-math doesn't matter. The relationship is the moat.

We mirror this exactly. Client Confidence is the relationship-pulse dial · tracked separately from Probability of Close (which is the deal-math dial).

## DefendableOS Definition

**Client Confidence** in DefendableOS is the modeled relationship-pulse number (float 0-1) for a given engagement · measuring the principal's confidence in the Defender as a counterparty. Computed weekly · refreshed on-demand on material relationship events · surfaced privately to the sr broker (NOT to the principal · principal pulse is operator information).

Computed as a 5-driver weighted composite:
- `responsiveness` · 25% (avg response time to sr broker outreach · last 30 days)
- `morning_brief_engagement` · 20% (open rate · reply rate · acknowledgment rate)
- `walk_attendance` · 20% (showed for scheduled walks · scheduled walks promptly · principal-acknowledgments captured within SLA)
- `escalation_tone` · 15% (qualitative · sr broker scores after each escalation · "principal trusted our framing" / "principal pushed back hard" / "principal seemed skeptical")
- `referral_signal` · 10% (did the principal refer anyone to us · did they mention us positively in industry contexts)
- `expansion_signal` · 10% (did the principal upgrade tier · expand fleet coverage · add assignments)

Bucketed into 5 bands using the same thresholds as Probability of Close (GREEN_LOCKED · AMBER_TRACKING · YELLOW_WATCHLIST · ORANGE_ESCALATION · RED_DARK). The bands are operator-internal · NEVER surfaced to the principal directly.

## Backend Representation

```json
{
  "scoring.client_confidence": {
    "type": "float",
    "range": [0.0, 1.0],
    "precision": 2,
    "visibility": "OPERATOR_ONLY",
    "scoring_hook": "relationship_pulse",
    "refresh_cadence": "weekly_friday_plus_on_demand"
  },
  "scoring.client_confidence_band": {
    "type": "enum",
    "values": ["GREEN_LOCKED", "AMBER_TRACKING", "YELLOW_WATCHLIST", "ORANGE_ESCALATION", "RED_DARK"]
  },
  "scoring.client_confidence_drivers": {
    "type": "jsonb",
    "shape": {
      "responsiveness": "float 0-1 · weight 0.25",
      "morning_brief_engagement": "float 0-1 · weight 0.20",
      "walk_attendance": "float 0-1 · weight 0.20",
      "escalation_tone": "float 0-1 · weight 0.15",
      "referral_signal": "float 0-1 · weight 0.10",
      "expansion_signal": "float 0-1 · weight 0.10"
    }
  },
  "scoring.client_confidence_trajectory_30d": {"type": "float"},
  "scoring.client_confidence_last_refresh_at": {"type": "timestamp"},
  "scoring.client_confidence_recovery_plan_active": {"type": "boolean"}
}
```

Schema files: `docs/schemas/client_confidence.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

We don't surface the **Client Confidence** dial to you directly · it's an internal operator metric · the way a CRE broker tracks "is the seller still happy" separately from "does the deal still pencil." Surfacing it raw would be like a CRE broker telling the seller "I'm scoring your engagement-mood at 0.62 this week" — useful internally · weird externally.

What you DO see is the OUTPUT of the client-confidence tracking:

- Your sr broker calls more often when client confidence drifts (it's a relationship signal · so the response is a relationship action)
- Your Morning Brief evolves to address concerns we sense before you raise them
- Founder gets cc'd on more events when the dial dips
- We proactively re-walk LOU sections or doctrine pieces if we sense gaps in alignment

The dial drives our cadence and our care. It doesn't drive a dashboard you watch. You watch your Probability of Close (the deal-math dial). We watch your Client Confidence (the relationship-pulse dial). Together they keep both sides of the engagement healthy.

## Jr Broker Use

- Capture relationship signals · responsiveness · brief-engagement · tone after every touch
- Log the `escalation_tone` score after every escalation call · honestly · including when it went poorly on our side
- Track referral and expansion signals when they happen · they're rare but high-weight
- Don't tell the principal about the dial · violation = JELLY at minimum · PROPOLIS if framed as a "scorecard"
- Escalate client-confidence drops to sr broker immediately · they often precede dial drops on PoC

The jr broker is the relationship-listening apparatus. You're the ones who catch the qualitative signals the dashboards can't.

## Sr Broker Use

- Reviews client-confidence weekly across the entire book (Friday cadence · same as PoC dial)
- Cross-references with Probability of Close · high-PoC + low-CC engagements are at risk
- Initiates **client-confidence recovery plans** when an engagement drops into YELLOW or worse:
  - Identifies the under-weight driver
  - Authors a relationship-action plan (more calls · founder-touch · re-walk · in-person visit)
  - Tracks recovery over 4-6 weeks
- Owns the principal-trust-recovery posture after any FAILED · DARK close
- Notifies founder on any RED · DARK CC dial · this is relationship-emergency territory

The sr broker uses CC as the early-warning system. CC typically drops 30-60 days before PoC drops · giving the sr broker a window to recover the relationship before the deal-math suffers.

## Tribunal Use

The Tribunal doesn't grade client-confidence directly · but supports it:
- Aggregated CC pattern analysis becomes calibration corpus for future intake screening (which signals predict high/low CC engagements)
- CC drops trigger Tribunal rule-layer to flag related deed-quality for QA validator review (sometimes CC drops because the work is actually slipping · sometimes because the relationship is independently souring)
- Quarterly CC trends across the book feed founder-level dashboard

## Evidence Required

- Responsiveness data captured from email/calendar system (no manual entry)
- Morning brief open/reply/ack data captured automatically
- Walk attendance + ack timestamp data captured automatically
- Escalation tone scored within 24 hours of every escalation by the sr broker on the call
- Referral and expansion signals logged in CRM with date · context · principal-quote (if any)
- ≥ 4 weekly snapshots before CC is considered stabilized for a new engagement

## Failure Modes

| Mode | Tribunal class |
|---|---|
| `cc_surfaced_to_principal` (raw dial shown to principal) | PROPOLIS · trust breach · sr broker review |
| `cc_inflated_by_sr_broker` (qualitative drivers boosted without evidence) | PROPOLIS · founder review |
| `cc_recovery_skipped` (CC dropped to YELLOW · no recovery plan authored within 7 days) | JELLY · sr broker coaching |
| `cc_red_silent` (CC dropped to RED · founder not notified) | PROPOLIS · founder review · likely relationship emergency |
| `cc_decoupled_from_poc` (CC high · PoC low · or vice versa · no cross-analysis done) | JELLY · sr broker cross-analysis required |

## Scoring Impact

- **assignment_success**: HIGH (low CC engagements close at lower HONEY rates regardless of validator-confidence)
- **repair_lift**: HIGH (CC-recovery interventions often lift PoC alongside)
- **validator_confidence**: ORTHOGONAL (CC and validator-confidence are independent metrics by design)
- **risk_temperature**: INVERSE (low CC = elevated relationship risk)
- **probability_of_close**: PREDICTIVE (CC drops typically precede PoC drops by 30-60 days)
- **evidence_strength**: HIGH (CC trajectory is a strong engagement-health evidence class)
- **cost_to_mint**: NEUTRAL (CC tracking is operator margin · amortized)

## Deed / Receipt Impact

- CC drops trigger rule-layer flags on under-engagement deeds for QA validator review
- CC trajectory is part of the annual engagement-calibration deed (`DDEED-{org}-CALIB-{slug}-{year}-v1`)
- Books-and-records: L1 + L3 weekly snapshots · L4 Hedera anchor only on calibration deed
- 5 Proofs touched: PROCESS (relationship lineage is part of engagement process) · TRUST (CC is the trust-side mirror of validator-confidence)

## Related Terms

- [probability-of-close](probability-of-close.md) · the deal-math dial (CC is the relationship-pulse dial · symmetric pair)
- [assignment-success](assignment-success.md) · the outcome CC predicts
- [engagement](../client_terms/engagement.md) · the unit CC measures
- [principal](../client_terms/principal.md) · the human whose confidence is being measured
- [morning-brief](../client_terms/morning-brief.md) · a major CC-driver input source
- [closing-statement](../client_terms/closing-statement.md) · CC scores typically drop after FAILED closes · recover over 60-90 days with discipline
- [pass-doctrine](../client_terms/pass-doctrine.md) · CC in low bands sometimes triggers PASS-pivot consideration

## Example

> Engagement: ENG-DOV-LOGISTICS-ACME-0001
>
> Current Client Confidence: **0.81** · AMBER · TRACKING (operator-internal · NOT surfaced to principal)
>
> Drivers:
> - `responsiveness` 0.91 (avg response 4.3 hrs · excellent)
> - `morning_brief_engagement` 0.88 (94% open rate · 23% reply rate over 90 days)
> - `walk_attendance` 1.00 (4 of 4 scheduled walks attended on time · all acks within 7 days)
> - `escalation_tone` 0.72 (last escalation: principal pushed back hard on cost variance · ultimately accepted our framing but the tone was edgier than prior)
> - `referral_signal` 0.40 (no referrals to date · neutral · not concerning for 6-mo engagement)
> - `expansion_signal` 0.65 (T3 → T3+ upgrade in active discussion · positive signal)
>
> Composite: 0.81
>
> 30-day trajectory: -0.04 (slight drift · attributable to single edgy escalation · not a recovery-plan trigger yet · sr broker noting)
>
> Cross-analysis with PoC dial (0.78 AMBER): CC slightly higher than PoC · consistent with the cost-variance being an operational issue we're actively fixing · principal's confidence is in the apparatus + relationship · the deal-math will recover with the routing tune.
>
> Sr broker action: continue weekly cadence · re-evaluate CC after next walk (post-routing-tune).

## DefendableOS Notes

- CC is the leading indicator. PoC is the lagging indicator. The sr broker who learns to read CC moves earlier than the sr broker who only watches PoC.
- The dial is INTERNAL by design. Surfacing it would distort it (principals would optimize for the score instead of just being themselves). It's the same reason a CRE broker doesn't tell the seller "I'm scoring your engagement-mood today."
- CC and PoC together are the engagement's two-sided pulse. High both = healthy. High PoC + low CC = relationship-at-risk. Low PoC + high CC = recoverable. Low both = consider PASS-pivot.
- The annual calibration of CC predictions vs actual relationship outcomes (renewal vs churn) is part of the engagement-level calibration deed. Long-run · CC accuracy compounds into the firm's institutional relationship-IQ.

🐝 *Two dials · one engagement · the relationship and the math both have to pencil.*
