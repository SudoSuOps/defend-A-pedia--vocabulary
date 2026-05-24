# Diagnose Task

## Street Definition

"What's the diagnosis?" That's how a Sr Hack opens the morning standup when there's a Propolis spike. **Diagnose Task** is RJ task #1 · the first output SwarmFixer emits on every refinery run. Root cause · severity 1-5 · recommended action. Three fields. No prose. The diagnosis is the receipt's first line.

## CRE Operator Meaning

In CRE the diagnose is the **pre-listing inspection**. The broker walks the building before he writes the OM · checks the roof · the HVAC · the parking · the elevators · the rent roll · the deferred maintenance. The inspection produces a punch list with a severity tag per item. The punch list IS the diagnosis. Without it · the OM is a fiction · the deal blows up in DD when the buyer finds what you missed.

## DefendableOS Definition

The Diagnose Task is the first of the 5 Royal Jelly tasks SwarmFixer emits. It identifies the failure mode from the 7-mode taxonomy (HALLUCINATION · SCHEMA_DRIFT · TOOL_MISUSE · INSTRUCTION_FAILURE · REASONING_GAP · SAFETY_VIOLATION · LATENCY_REGRESSION), the AgentHash bucket (STOP · CALL · READ · RECOVER · LOOP), assigns a severity score 1-5, and recommends an action class. It runs first because the other 4 tasks depend on it. No diagnose, no refinery.

## Backend Representation

```json
{
  "diagnose.task_id": {"type": "string", "format": "rj-diag-<run_id>"},
  "diagnose.failure_mode": {
    "type": "enum",
    "values": ["HALLUCINATION","SCHEMA_DRIFT","TOOL_MISUSE","INSTRUCTION_FAILURE","REASONING_GAP","SAFETY_VIOLATION","LATENCY_REGRESSION"]
  },
  "diagnose.agenthash_bucket": {
    "type": "enum",
    "values": ["STOP","CALL","READ","RECOVER","LOOP"]
  },
  "diagnose.clawhash_sub_algorithm": {
    "type": "enum",
    "values": ["injection","toolpoison","rce","supply","sandbox","audit","null"]
  },
  "diagnose.severity": {"type": "integer", "range": [1, 5]},
  "diagnose.recommended_action": {"type": "string", "enum": ["RETRY","RETRAIN","PATCH_PROMPT","ESCALATE_HUMAN","QUARANTINE"]},
  "diagnose.confidence": {"type": "float", "range": [0.0, 1.0]},
  "diagnose.evidence_citations": {"type": "array", "items": {"type": "string"}}
}
```

Schema files: `docs/schemas/royal_jelly_record.schema.json` · `docs/schemas/diagnose_task.schema.json`

## Client Explanation

The Diagnose Task is the doctor's chart. When your AI agent makes a mistake, the first thing we ship back is the root cause. Why did it fail · how bad was it · what should you do about it. Three answers in plain machine-readable form, so your engineers can wire it into their on-call · or your operator can read it and route to a fix.

## Jr Broker Use

The Jr Hack reads the Diagnose Task before reading anything else in the Royal Jelly Record. The diagnosis determines whether the rest of the record is worth reading. If the diagnosis severity is 5 and the AgentHash is STOP · the customer's agent is hanging on benign inputs · the rest of the record might say "RETRAIN" but the operator should escalate immediately.

## Sr Broker Use

The Sr Hack challenges the Diagnose Task. If the failure mode is tagged HALLUCINATION but the input looks like SCHEMA_DRIFT, the Sr Hack re-tags and re-runs. Wrong taxonomy at intake compounds into wrong PREVENT and wrong DETECT downstream. The diagnose is the load-bearing first decision · every other task inherits its frame.

## Tribunal Use

- **Rule layer**: Diagnose Task MUST tag both the 7-mode taxonomy AND the AgentHash bucket (C03)
- **Rule layer**: Severity MUST be ∈ {1,2,3,4,5} · floats or strings rejected
- **Rule layer**: Recommended action MUST be one of the 5 enum values · free-text rejected
- **Judge layer**: Tribunal scores the diagnose accuracy by re-running it through a second SwarmJelly inference at TEMP=0.05 · drift > 0.20 on taxonomy assignment flags the diagnose as low-confidence
- **Classification impact**: A misdiagnosed pair cannot reach Royal Jelly even if the REPAIR task is correct · because the receipt would carry a wrong cause-of-action

## Evidence Required

- The original failed pair (input + agent output + Tribunal verdict)
- The 7-mode taxonomy tag with cited evidence in the pair
- The AgentHash bucket tag with cited evidence
- ClawHash sub-algorithm tag if the failure is adversarial (else null)
- Severity rationale (which fields of the pair drove the score)
- Recommended action with a doctrine pointer

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `wrong_taxonomy_tag` | Diagnose chose a failure mode not supported by the pair evidence | JELLY · re-run |
| `missing_agenthash` | AgentHash bucket not populated | JELLY · re-run |
| `severity_out_of_range` | Severity is 0 or 6 or a float | PROPOLIS · schema violation |
| `free_text_action` | Recommended action is prose · not one of the 5 enums | PROPOLIS · schema violation |
| `unfounded_severity` | Severity 5 on a pair with no evidence of catastrophic impact | JELLY · validator review |
| `missed_safety_signal` | Pair contained safety-violation signals · diagnose tagged something else | PROPOLIS · auto-escalate |

## Scoring Impact

- **assignment_success**: HIGH · wrong diagnose = wrong fix = no lift = no deed
- **repair_lift**: INDIRECT · diagnose feeds the REPAIR task · bad diagnose ceilings the lift
- **validator_confidence**: HIGH · validators read diagnose first · low-confidence diagnose → low overall confidence
- **risk_temperature**: DIRECT · severity 5 = high risk · severity 1 = low risk
- **probability_of_close**: NEUTRAL · internal task · not customer-facing per-pair
- **evidence_strength**: HIGH · diagnose must cite evidence from the source pair
- **cost_to_mint**: LOW · diagnose is the cheapest of the 5 tasks (~1500 tokens output)

## Deed / Receipt Impact

- **Receipt fields touched**: `diagnose.failure_mode` · `diagnose.agenthash_bucket` · `diagnose.severity` · `diagnose.recommended_action` · `diagnose.confidence`
- **DDEED class impact**: diagnose is part of DDEED-DOV-REPAIR · the failure mode tag becomes a queryable index for the deed registry
- **Books and records layer**: L1 PostgreSQL (the diagnose record) → L4 Hedera HCS (the deed)
- **5 Proofs touched**: PROCESS (root-cause analysis IS process) · QUALITY (the diagnose's own confidence)

## Related Terms

- [swarmfixer](swarmfixer.md) · the refinery that emits the diagnose
- [repair-task](repair-task.md) · RJ task #2 · depends on diagnose
- [prevent-task](prevent-task.md) · RJ task #3 · uses diagnose to write the rule
- [detect-task](detect-task.md) · RJ task #4 · uses diagnose to build the classifier
- [compare-task](compare-task.md) · RJ task #5 · validates the diagnose by comparison
- [pair-candidate](pair-candidate.md) · the unit the diagnose is run on

## Example

> **Pair**: books-bot.acmecorp.defendable.eth · journal entry with reversed DR/CR
>
> **Diagnose Task output**:
> ```yaml
> failure_mode: REASONING_GAP
> agenthash_bucket: READ
> clawhash_sub_algorithm: null
> severity: 3
> recommended_action: PATCH_PROMPT
> confidence: 0.88
> evidence_citations:
>   - "input.invoice_direction = outbound · agent_output.dr_account = AR (should be revenue)"
>   - "no fabrication detected · math correct given the misread"
>   - "agent did NOT call the entity-direction lookup tool"
> ```
>
> **Severity rationale**: severity 3 because financial impact is bounded ($X within reversible ledger period) but pattern likely systemic across recent batch
>
> **Action**: PATCH_PROMPT to require entity-direction lookup before any DR/CR assignment

## DefendableOS Notes

- Diagnose Task is the FIRST CITIZEN of the 5-task contract · everything else depends on it
- The 7-mode × 5-AgentHash matrix produces 35 cells · the SwarmJelly training corpus has at least one pair per cell · this is what makes the diagnose reliable at TEMP=0.05
- A misdiagnosed pair routed downstream is worse than no refinery run at all · because the customer's PREVENT and DETECT logic ships against the wrong root cause

🐝 *No diagnose, no fix. The diagnose is the punch list.*
