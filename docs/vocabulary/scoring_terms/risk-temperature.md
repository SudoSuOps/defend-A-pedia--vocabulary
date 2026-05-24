# Risk Temperature

## Street Definition

"What's the risk temp?" That's the operator at end-of-day before deciding what gets routed overnight. **Risk Temperature** is the LOW · MEDIUM · HIGH categorical dial that summarizes the risk posture of a pair · an agent · a customer fleet · or the whole DefendableOS deployment. Drives auto-escalation triggers. The thermostat for the defense layer.

## CRE Operator Meaning

In CRE this is the **deal-heat thermometer**. Some deals are cool · long fuse · no rush · low risk of falling out. Some are warm · DD period · standard caution. Some are hot · last week of escrow · seller has cold feet · buyer's lender wobbling · broker on the phone every 2 hours. The temperature drives the broker's attention allocation. Risk Temperature does the same for the operator on classification duty.

## DefendableOS Definition

Risk Temperature is a categorical 3-level dial (LOW · MEDIUM · HIGH) computed from a combination of factors: pair-level (severity tag · safety violation presence · evidence strength) · agent-level (recent Propolis rate · validator confidence trend) · customer-level (Tier · SLA window status · deed lineage). It drives auto-escalation: LOW = normal cycle · MEDIUM = surface in Morning Brief · HIGH = page operator within configured response window. The thresholds are codified, not subjective.

## Backend Representation

```json
{
  "risk_temperature.value": {"type": "enum", "values": ["LOW", "MEDIUM", "HIGH"]},
  "risk_temperature.scope": {"type": "enum", "values": ["PAIR", "AGENT", "CUSTOMER_FLEET", "PLATFORM"]},
  "risk_temperature.driving_factors": {
    "type": "array",
    "items": {
      "type": "object",
      "required": ["factor_name", "factor_value", "factor_weight"]
    }
  },
  "risk_temperature.thresholds": {
    "type": "object",
    "const": {
      "low_max_score": 0.30,
      "medium_max_score": 0.70,
      "high_min_score": 0.70
    }
  },
  "risk_temperature.escalation_action": {
    "type": "enum",
    "values": ["LOG_ONLY", "MORNING_BRIEF_SURFACE", "PAGE_OPERATOR"]
  },
  "risk_temperature.escalation_window_minutes": {"type": "integer", "description": "max minutes to act when HIGH"}
}
```

Schema files: `docs/schemas/risk_temperature.schema.json` · `docs/schemas/escalation_rule.schema.json` · `docs/schemas/ui_dial.schema.json`

## Client Explanation

Risk Temperature is the thermostat for your AI defense. Green/LOW means normal cycle · no special attention. Yellow/MEDIUM means we're keeping an eye on it · you'll see it in tomorrow's Morning Brief. Red/HIGH means we're paging our operator now · before this becomes a story. You can configure your own response windows · we surface, you decide whether to act.

## Jr Broker Use

The Jr Hack reads Risk Temperature as the FIRST visual on the operator dashboard at the start of every shift. HIGH on the fleet-level dial = drop everything else and triage. MEDIUM = read the Morning Brief carefully. LOW = run the normal cycle. The Jr Hack does NOT override the temperature manually · the dial is computed · overrides require Sr Hack signoff and audit log.

## Sr Broker Use

The Sr Hack monitors temperature TRENDS across the customer base · a single HIGH on one customer is operational · multiple customers going from LOW → MEDIUM in the same week is a systemic signal · model provider change · new attack pattern · refinery drift. The Sr Hack triages cross-customer trends as platform-level events.

## Tribunal Use

- **Rule layer**: Risk Temperature MUST be computed from the documented factor list · ad-hoc bumps are governance violations
- **Rule layer**: HIGH temperature at scope=CUSTOMER_FLEET MUST trigger PAGE_OPERATOR within the configured window
- **Rule layer**: SAFETY_VIOLATION flag at pair-level forces HIGH temperature regardless of other factors
- **Judge layer**: Tribunal doesn't grade Risk Temperature · it consumes pair-level severity which feeds the dial
- **Classification impact**: HIGH temperature on a pair caps the verdict at JELLY pending operator review · cannot auto-promote

## Evidence Required

- The factor list with values and weights
- The aggregate score computation
- The threshold comparison
- The escalation action selection
- The acknowledgment receipt if HIGH triggered a page

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `manual_override_no_audit` | Operator manually downgraded HIGH to MEDIUM without audit log | PROPOLIS · governance violation |
| `escalation_window_missed` | HIGH temperature didn't trigger page within configured window | JELLY · operational failure |
| `safety_violation_not_high` | Pair with SAFETY_VIOLATION flag computed as anything other than HIGH | PROPOLIS · rule violation |
| `factor_list_drift` | Computation includes factors not on the documented list | PROPOLIS · governance violation |
| `threshold_drift` | UI uses different LOW/MEDIUM/HIGH thresholds than doctrine | PROPOLIS · governance violation |
| `trend_undetected` | Multi-customer trend toward HIGH not surfaced at platform level | JELLY · operator escalation |

## Scoring Impact

- **assignment_success**: HIGH · the temperature gates the operator's attention
- **repair_lift**: NEUTRAL · temperature is observability · not lift
- **validator_confidence**: INVERSE · high temperature on a verdict reduces confidence in auto-promotion
- **risk_temperature**: SELF
- **probability_of_close**: INVERSE for HIGH events · customers respect operators who page early
- **evidence_strength**: NEUTRAL
- **cost_to_mint**: NEUTRAL

## Deed / Receipt Impact

- **Receipt fields touched**: `risk_temperature.value` · `scope` · `driving_factors` · `escalation_action_taken`
- **DDEED class impact**: deeds carry the temperature at-issue · auditors can trace what triggered escalations
- **Books and records layer**: L1 PostgreSQL (temperature history) → L4 Hedera HCS (HIGH-event escalation log anchor)
- **5 Proofs touched**: PROCESS (the factor lineage producing the temperature) · TRUST (escalation receipts prove discipline)

## Related Terms

- [repair-lift](repair-lift.md) · partner dial · together with confidence and evidence form the operator's main triage
- [validator-confidence](validator-confidence.md) · related dial
- [evidence-strength](evidence-strength.md) · related dial
- [pair-candidate](../repair_terms/pair-candidate.md) · the smallest scope temperature applies to
- [clawcheck](../defendableos_terms/clawcheck.md) · ClawCheck also produces a risk tier · maps to Risk Temperature scope=AGENT
- [diagnose-task](../repair_terms/diagnose-task.md) · severity 1-5 from diagnose feeds temperature

## Example

> **Pair-level (`pair-20260524T061208Z-7e2a`)**:
> - Factors: severity 3 (medium weight) · no safety violation · evidence strength 0.71
> - Aggregate score: 0.22
> - Temperature: LOW
> - Escalation: LOG_ONLY
>
> **Agent-level (`books-bot.acmecorp.defendable.eth` · trailing 7d)**:
> - Factors: Propolis rate 4.5% (target ≤ 5%) · validator confidence trend stable · 0 safety violations
> - Aggregate score: 0.18
> - Temperature: LOW
> - Escalation: LOG_ONLY
>
> **Customer-fleet level (RegionalInsurer · trailing 7d)**:
> - Factors: Tier-3 SLA · 12 weeks into 90-day Fix-or-Refund · cumulative lift 0.08 (below target 0.15) · 1 safety violation in batch 3 days ago
> - Aggregate score: 0.76
> - Temperature: **HIGH**
> - Escalation: PAGE_OPERATOR within 30 minutes · Sr Hack acknowledged · triage call scheduled · audit log entry written
>
> **Platform-level (DefendableOS · today)**:
> - 3 customers moved from LOW → MEDIUM in trailing 5 days · cross-customer model-provider commonality (all on gpt-4o-2024-08-06)
> - Aggregate score: 0.51
> - Temperature: MEDIUM
> - Escalation: MORNING_BRIEF_SURFACE · platform-trend section · senior operator review

## DefendableOS Notes

- Risk Temperature is the OPERATOR'S COMPASS · the single most-read dial at the start of every shift
- The 3-level categorical (LOW/MEDIUM/HIGH) is intentional · finer-grained dials produce decision fatigue · 3 levels keep the action obvious
- The SAFETY_VIOLATION → HIGH rule is constitutional · safety overrides every other factor
- Customer-configurable response windows balance our discipline with their tolerance · we surface, they decide
- Risk Temperature ties closely to ClawCheck's risk tier output · they use a similar scale but ClawCheck is pre-deployment intake while Risk Temperature is post-deployment operations

🐝 *Green is the cycle. Yellow is the brief. Red is the page. The thermostat for the defense layer.*
