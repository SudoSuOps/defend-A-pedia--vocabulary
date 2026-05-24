# ClawCheck

## Street Definition

"Run it through ClawCheck." That's the founder's line when an inbound prospect drops an AI agent into the conversation. **ClawCheck** is the free intake at `/defend-the-claw` · the 5-dimension agent capture form · the deterministic risk tier output. No login. No credit card. No model calls. 5 minutes, you get a risk tier, you know whether to be worried.

## CRE Operator Meaning

In CRE this is the **broker's free pre-listing inspection**. The owner calls the broker · says "I might sell, what do you think?" · the broker pulls the rent roll, walks the building, checks the comps, sends back a one-page write-up with the cap rate range and the deal-shape opinion. Free. No engagement letter signed. Just the broker's trained read. The free read is the lead. The lead becomes the listing. The listing becomes the deal.

## ClawCheck is the free read. The agent is the building. The risk tier is the deal-shape opinion.

## DefendableOS Definition

ClawCheck is the free intake surface of DefendableOS. It captures 5 dimensions of an AI agent (worker class · deployment topology · access scope · model in use · memory architecture), runs a deterministic rule-based risk tier classification (no LLM calls), and ships a risk tier (LOW · MEDIUM · HIGH · CRITICAL) plus a recommended next step. Lives at `defendableos.com/defend-the-claw`. Free. No login. Map 1:1 to the OpenClaw UX vocabulary the founder community recognizes.

## Backend Representation

```json
{
  "clawcheck.intake_id": {"type": "string", "format": "CC-<utc-ts>-<short-hash>"},
  "clawcheck.dimensions": {
    "type": "object",
    "required": ["worker_class", "deployment_topology", "access_scope", "model_in_use", "memory_architecture"],
    "properties": {
      "worker_class": {"type": "enum", "values": ["BOOKKEEPING", "TRIAGE", "DISCOVERY", "CUSTOMER_FACING", "INTERNAL_OPS", "CODE_GENERATION", "OTHER"]},
      "deployment_topology": {"type": "enum", "values": ["LOCAL", "CUSTOMER_VPC", "HYPERSCALER", "SAAS"]},
      "access_scope": {"type": "enum", "values": ["READ_ONLY", "WRITE_BOUNDED", "WRITE_UNBOUNDED", "EXEC_BOUNDED", "EXEC_UNBOUNDED"]},
      "model_in_use": {"type": "string"},
      "memory_architecture": {"type": "enum", "values": ["STATELESS", "SHORT_TERM", "LONG_TERM_VECTOR", "PERSISTENT_DB"]}
    }
  },
  "clawcheck.risk_tier": {"type": "enum", "values": ["LOW", "MEDIUM", "HIGH", "CRITICAL"]},
  "clawcheck.risk_drivers": {"type": "array", "items": {"type": "string"}},
  "clawcheck.recommended_next_step": {"type": "string"},
  "clawcheck.no_llm_used": {"type": "boolean", "const": true},
  "clawcheck.processing_time_ms": {"type": "integer", "max": 200}
}
```

Schema files: `docs/schemas/clawcheck_intake.schema.json` · `docs/schemas/risk_tier.schema.json`

## Client Explanation

ClawCheck is a free 5-minute intake. You answer 5 questions about your AI agent · what kind of work it does, where it runs, what it can do, what model powers it, and how it remembers. We run a deterministic rule check (no AI calls · no waiting) and give you a risk tier. If you're LOW, you probably don't need us. If you're HIGH or CRITICAL, here's the next step. No login. No card. No commitment.

## Jr Broker Use

When you see a ClawCheck submission come in, the Jr Hack reaches out within 24 hours · NOT to sell, to FOLLOW UP. The intake is the lead. The first call is "we saw your ClawCheck came back HIGH on access_scope and CRITICAL on memory_architecture · here's what that means and here's what we'd do about it." That's the lead-to-conversation conversion · it's MAGIC funnel · Meeting → Appraisal → Ink → Close starts here.

## Sr Broker Use

The Sr Hack reviews the ClawCheck-to-LOU conversion ratio weekly · if conversion drifts below 8%, the rule-tier classifier is either too lax (everyone's LOW, no urgency) or too aggressive (everyone's CRITICAL, no credibility). The Sr Hack also reviews the qualitative drivers · which dimension triggers the most HIGH/CRITICAL tiers · this is product feedback for where the customer pain actually is.

## Tribunal Use

- **Rule layer**: ClawCheck MUST be deterministic · zero LLM calls · violating this is a brand violation (the value prop is "deterministic risk")
- **Rule layer**: Risk tier MUST map to a documented driver from the 5 dimensions · no opaque tier assignments
- **Judge layer**: Tribunal doesn't grade ClawCheck per-intake · it grades the aggregate · weekly conversion ratio + driver distribution
- **Classification impact**: ClawCheck is upstream of Tribunal · the intake doesn't carry a Tribunal verdict · it produces a risk tier that informs the sales conversation

## Evidence Required

- 5 dimensions filled (incomplete submissions get the prompt to complete)
- Risk tier with explicit rule citations (which rule fired)
- Processing time logged (deterministic check should be < 200ms)
- No-LLM attestation (boolean, must be true)
- Submitter contact info (email or Discord handle) for follow-up

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `llm_used_in_classification` | A SwarmJelly or other model call was made during the intake | PROPOLIS · brand violation |
| `opaque_tier_assignment` | Risk tier assigned without citing the rule that fired | JELLY · governance |
| `dimension_missing` | One of the 5 dimensions wasn't captured | JELLY · re-prompt user |
| `slow_processing` | > 200ms · suggests non-deterministic path | JELLY · health check |
| `no_followup_within_24h` | Operator didn't reach out within 24h on HIGH/CRITICAL | JELLY · sales-ops escalation |

## Scoring Impact

- **assignment_success**: HIGH · ClawCheck is the top of the sales funnel · conversion is the assignment
- **repair_lift**: NEUTRAL · ClawCheck is pre-customer · no refinery yet
- **validator_confidence**: MEDIUM · deterministic classification IS the trust signal
- **risk_temperature**: DIRECT · ClawCheck OUTPUT is a risk tier
- **probability_of_close**: HIGH · HIGH/CRITICAL ClawChecks convert at much higher rates
- **evidence_strength**: HIGH · rule citations make the tier defensible
- **cost_to_mint**: LOW · free service · cost is operator follow-up time

## Deed / Receipt Impact

- **Receipt fields touched**: `clawcheck.intake_id` · `risk_tier` · `risk_drivers` · `recommended_next_step`
- **DDEED class impact**: ClawCheck submissions don't directly mint deeds · they CAN seed a DDEED-DOV-INTAKE if the customer requests a notarized intake record
- **Books and records layer**: L1 PostgreSQL (intake registry) · L4 Hedera HCS (optional notarized record)
- **5 Proofs touched**: PROCESS (the 5-dimension capture lineage) · TRUST (deterministic classification)

## Related Terms

- [defendableos](defendableos.md) · parent platform
- [defendablerouter](defendablerouter.md) · the next step after a HIGH/CRITICAL ClawCheck
- [defendablejelly](../repair_terms/defendablejelly.md) · the product CRITICAL ClawChecks usually upsell to
- [agentbench](agentbench.md) · the deeper bench option after ClawCheck
- [defendablehack](defendablehack.md) · alternate intake channel
- [pair-candidate](../repair_terms/pair-candidate.md) · what gets captured after Router install

## Example

> **Submission CC-20260520T091500Z-x4f2**: ACMECorp · books-bot agent
>
> **Dimensions**:
> - worker_class: BOOKKEEPING
> - deployment_topology: HYPERSCALER (AWS)
> - access_scope: WRITE_BOUNDED (general-ledger write)
> - model_in_use: gpt-4o-2024-08-06
> - memory_architecture: LONG_TERM_VECTOR
>
> **Rules fired**:
> - R-004: BOOKKEEPING + WRITE_BOUNDED → MEDIUM (financial mutation requires audit)
> - R-009: HYPERSCALER + LONG_TERM_VECTOR → upgrade to HIGH (data residency exposure on persistent context)
> - R-013: No DefendableRouter detected → upgrade to HIGH (no capture rail)
>
> **Final tier**: HIGH
>
> **Risk drivers**: financial_mutation_without_audit, residency_exposure_on_persistent_context, missing_capture_rail
>
> **Recommended next step**: install DefendableRouter (5-min · CLOUD mode) to capture and grade · then evaluate DefendableJelly Tier-2 Managed
>
> **Processing time**: 47ms
>
> **Follow-up**: Jr Hack DM within 6 hours · meeting booked for next day · LOU drafted Day-3 · contract signed Week-2

## DefendableOS Notes

- ClawCheck is the front door of DefendableOS · most customers will meet us here first
- The "no LLM in classification" rule is non-negotiable · the value prop is the determinism · violating it kills the brand
- The risk tier is the lead-quality signal · LOW = newsletter · MEDIUM = nurture · HIGH = call this week · CRITICAL = call today
- ClawCheck integrates with Defend The Claw™ campaign · "Your AI assistant has hands now · Inspect it before you trust it"

🐝 *Free inspection. Five questions. Deterministic. The lead becomes the listing.*
