# Repair Task

## Street Definition

"Show me the fix." That's the operator's second read after the diagnose. **Repair Task** is RJ task #2 · the step-by-step recovery from the failed state to a Honey-grade answer. The diagnose says what's wrong · the repair says how it gets done. Step-by-step. With the corrected output. With the rationale.

## CRE Operator Meaning

In CRE the Repair Task is the **GC's scope of work**. The inspector wrote the punch list. The GC writes the actual scope · who does what · in what order · to what spec · with what materials · for how much. The scope is what gets bid. The scope is what gets built. The scope is what gets inspected at completion. No scope, no rehab.

## DefendableOS Definition

The Repair Task is the second of the 5 Royal Jelly tasks SwarmFixer emits. It produces the step-by-step recovery procedure AND the corrected output. The procedure is a numbered sequence of operations the agent should have performed. The corrected output is the answer the agent should have produced. The Tribunal grades the corrected output as a fresh submission · its composite score is the input to the Repair Lift calculation.

## Backend Representation

```json
{
  "repair.task_id": {"type": "string", "format": "rj-rep-<run_id>"},
  "repair.steps": {
    "type": "array",
    "items": {
      "type": "object",
      "required": ["step_number", "action", "rationale"],
      "properties": {
        "step_number": {"type": "integer", "min": 1},
        "action": {"type": "string"},
        "rationale": {"type": "string"},
        "tool_call": {"type": "string", "nullable": true}
      }
    },
    "minItems": 1
  },
  "repair.corrected_output": {"type": "string"},
  "repair.input_evidence_cited": {"type": "array", "items": {"type": "string"}},
  "repair.confidence": {"type": "float", "range": [0.0, 1.0]},
  "repair.tribunal_rebench_run_id": {"type": "string"}
}
```

Schema files: `docs/schemas/royal_jelly_record.schema.json` · `docs/schemas/repair_task.schema.json`

## Client Explanation

The Repair Task is the corrected answer. When your AI shipped the wrong journal entry · the wrong claim summary · the wrong contract clause · we ship back the right one, plus the step-by-step that produced it. You can read the steps and patch your prompt. Or you can ship the corrected output to the downstream system. Either way · you have the fix in hand.

## Jr Broker Use

The Jr Hack verifies the Repair Task cites evidence from the source pair · not fabricated sources. If the repair cites a "vendor master record" that wasn't in the input, that's a fabrication and the pair routes to `quarantined/`. The Jr Hack also verifies the corrected output runs through Tribunal re-bench before the lift is computed · skipping the re-bench is a process violation.

## Sr Broker Use

The Sr Hack reads the repair steps as if they were the playbook the customer's agent should adopt going forward. If the steps would require infrastructure the customer doesn't have (e.g., "call the entity-direction lookup tool" when the customer hasn't built that tool yet), the Sr Hack flags it for the PREVENT and DETECT tasks to compensate · or escalates to the customer for an infra discussion.

## Tribunal Use

- **Rule layer**: Repair Task MUST include at least 1 step · MUST include a corrected_output · MUST cite input evidence (no fabrication) (C04)
- **Rule layer**: The corrected_output MUST be re-benched through Tribunal · the rebench run_id MUST be populated
- **Judge layer**: The Tribunal grades the corrected_output as a fresh agent submission · uses the same 6-axis rubric as the original verdict
- **Classification impact**: The repaired score IS the input to Repair Lift · which gates the bucket transition

## Evidence Required

- The original failed pair (input + agent output)
- The Diagnose Task output (severity + failure mode)
- The repair steps with rationale per step
- The corrected output as runnable text/JSON/code
- Citations to specific fields in the source pair (no fabricated sources)
- The Tribunal re-bench verdict with run_id

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `fabricated_evidence` | Repair cites sources not in the source pair | PROPOLIS · auto-quarantine |
| `empty_steps` | Steps array is empty · no procedure documented | PROPOLIS · schema violation |
| `corrected_output_unrunnable` | Corrected output is malformed · won't parse or won't execute | JELLY · re-route |
| `no_rebench` | Tribunal re-bench skipped · lift cannot be computed | PROPOLIS · process violation |
| `infra_assumption` | Steps assume infra the customer doesn't have | JELLY · escalate to PREVENT/DETECT |
| `lower_than_original` | Re-bench scores LOWER than original · regression | PROPOLIS · refinery failure |

## Scoring Impact

- **assignment_success**: HIGH · the repair IS the assignment deliverable
- **repair_lift**: DIRECT · the corrected_output's re-bench score IS the lift input
- **validator_confidence**: HIGH · validators read the repair steps to verify reasoning
- **risk_temperature**: INVERSE · clean repair lowers risk · sloppy repair raises it
- **probability_of_close**: HIGH · customers judge the product on the quality of the corrected output
- **evidence_strength**: HIGH · the repair must cite source evidence (no fabrication)
- **cost_to_mint**: MEDIUM · repair is the most-token-intensive of the 5 tasks (~3000-5000 tokens)

## Deed / Receipt Impact

- **Receipt fields touched**: `repair.steps` (hashed) · `repair.corrected_output` (hashed) · `repair.tribunal_rebench_run_id` · `repair.confidence`
- **DDEED class impact**: repair is the BODY of DDEED-DOV-REPAIR · the corrected output is what the deed attests to
- **Books and records layer**: L1 PostgreSQL → L2 Merkle (corrected output as leaf) → L4 Hedera HCS
- **5 Proofs touched**: PROCESS (the step sequence) · QUALITY (the re-bench verdict) · ECONOMICS (token cost)

## Related Terms

- [diagnose-task](diagnose-task.md) · RJ task #1 · provides the root cause
- [prevent-task](prevent-task.md) · RJ task #3 · derived from the repair
- [detect-task](detect-task.md) · RJ task #4 · derived from the repair
- [compare-task](compare-task.md) · RJ task #5 · ranks the repair against alternatives
- [repair-lift](repair-lift.md) · the dial the repair produces
- [swarmfixer](swarmfixer.md) · the refinery that emits the repair

## Example

> **Pair**: books-bot.acmecorp.defendable.eth · journal entry with reversed DR/CR
>
> **Diagnose**: REASONING_GAP · severity 3 · AgentHash READ
>
> **Repair Task output**:
> ```yaml
> steps:
>   - step_number: 1
>     action: "Call entity_direction_lookup(vendor_id) to confirm direction"
>     rationale: "Misread root cause was not consulting the canonical direction source"
>     tool_call: "entity_direction_lookup"
>   - step_number: 2
>     action: "If lookup returns 'OUTBOUND' · set DR = COGS/Expense · CR = AP/Cash"
>     rationale: "Outbound invoice from vendor = expense recognition"
>     tool_call: null
>   - step_number: 3
>     action: "Re-emit journal entry with corrected DR/CR direction"
>     rationale: "Final output must match the inferred direction"
>     tool_call: null
> corrected_output: |
>   {"journal_entry": {"dr": {"account": "COGS", "amount": 12500}, "cr": {"account": "Accounts Payable", "amount": 12500}, "memo": "Vendor invoice INV-2026-0142"}}
> input_evidence_cited:
>   - "input.invoice.direction = outbound"
>   - "input.invoice.amount = 12500"
>   - "input.invoice.vendor_id = V-8801"
> confidence: 0.92
> tribunal_rebench_run_id: "tribunal-rebench-20260524T073000Z-acme-books-001"
> ```
>
> **Tribunal re-bench**: composite 0.910 (was 0.760)
>
> **Repair Lift**: +0.150

## DefendableOS Notes

- The Repair Task is what the customer ACTUALLY consumes · they read the steps · they patch their agent · they ship the corrected output to downstream
- The "no fabricated sources" rule is the bright line · violations auto-quarantine · because a refinery that hallucinates fixes is worse than no refinery
- The corrected_output gets re-benched independently · this is what makes the lift number defensible to an auditor

🐝 *The repair is the GC's scope. Numbered steps. Cited evidence. Runnable output.*
