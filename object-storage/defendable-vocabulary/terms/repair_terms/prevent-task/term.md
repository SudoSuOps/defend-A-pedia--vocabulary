# Prevent Task

## Street Definition

"How do we keep this from happening again?" That's the customer's first question after the dust settles. **Prevent Task** is RJ task #3 · the trigger condition + the check logic + the remediation. It's not the fix · it's the policy that stops the same failure shape from shipping a second time.

## CRE Operator Meaning

In CRE the Prevent Task is the **title insurance policy**. The original closing had a defect · easement claim · undisclosed lien · permit irregularity. You cured it for this transaction. The title policy is what protects the NEXT owner from the same defect re-appearing at the next closing. The policy doesn't fix what's already broken · it prevents the recurrence. That's the prevent layer.

## DefendableOS Definition

The Prevent Task is the third of the 5 Royal Jelly tasks SwarmFixer emits. It generates a deterministic rule that, if it had existed before today's failure, would have prevented it. The rule has three parts: the trigger condition (pattern to watch for), the check logic (deterministic evaluation), and the remediation (what the agent should do when the trigger fires). Prevent rules feed both the customer's runtime guardrails AND the AdversarialPack v.next as positive defense cases.

## Backend Representation

```json
{
  "prevent.task_id": {"type": "string", "format": "rj-prev-<run_id>"},
  "prevent.trigger_condition": {
    "type": "object",
    "required": ["pattern_type", "pattern_definition"],
    "properties": {
      "pattern_type": {"type": "enum", "values": ["INPUT_SHAPE", "TOOL_OUTPUT_SHAPE", "REASONING_TRACE", "OUTPUT_FORMAT"]},
      "pattern_definition": {"type": "string"}
    }
  },
  "prevent.check_logic": {
    "type": "object",
    "required": ["check_type", "check_definition"],
    "properties": {
      "check_type": {"type": "enum", "values": ["REGEX", "JSONPATH", "TOOL_CALL_GUARD", "INVARIANT_ASSERTION"]},
      "check_definition": {"type": "string"}
    }
  },
  "prevent.remediation": {
    "type": "object",
    "required": ["action_class", "action_detail"],
    "properties": {
      "action_class": {"type": "enum", "values": ["BLOCK_AND_REPROMPT", "FALLBACK_PATH", "ESCALATE_HUMAN", "AUGMENT_CONTEXT", "ABORT_SAFE"]},
      "action_detail": {"type": "string"}
    }
  },
  "prevent.confidence": {"type": "float", "range": [0.0, 1.0]},
  "prevent.proposed_pack_version": {"type": "string", "default": "v.next"}
}
```

Schema files: `docs/schemas/royal_jelly_record.schema.json` · `docs/schemas/prevent_task.schema.json` · `docs/schemas/adversarial_pack.schema.json`

## Client Explanation

The Prevent Task is the insurance policy on the fix. We tell you what to watch for, how to check it deterministically, and what your agent should do when the check fires. You wire the rule into your runtime guardrails. The same failure stops shipping. The rule also feeds our AdversarialPack so EVERY customer benefits from your one bad day.

## Jr Broker Use

The Jr Hack verifies the Prevent Task is DETERMINISTIC · not "ask the LLM if this looks bad." Deterministic means regex · JSONPath · tool-call assertions · invariant checks. If the check logic requires another LLM call, it's not a prevent rule · it's another agent, and that doesn't compound the same way. Re-route for re-generation with a deterministic check.

## Sr Broker Use

The Sr Hack reviews the Prevent Task for **breadth vs depth tradeoff**. A rule that's too narrow only catches the exact pair that failed today. A rule that's too broad catches false positives and degrades the customer's agent throughput. The sweet spot is the rule that catches the failure SHAPE · the 5-10 next pairs that will look similar but not identical. The Sr Hack signs off on the breadth.

## Tribunal Use

- **Rule layer**: Prevent Task MUST be deterministic · MUST have all 3 parts (trigger · check · remediation) · LLM-only checks rejected
- **Rule layer**: The check logic MUST be testable · the rule must be runnable against the source pair AND produce a positive trigger
- **Judge layer**: Tribunal evaluates whether the prevent rule would have stopped the original failure · this is a deterministic re-run · binary pass/fail
- **Classification impact**: Prevent Task that fails the self-test (would NOT have caught its own source failure) drops the whole RJ record to JELLY

## Evidence Required

- The Diagnose Task output (failure mode + AgentHash bucket)
- The Repair Task output (corrected behavior)
- The trigger condition with concrete pattern definition
- The check logic (runnable code or expression)
- The remediation action with detail
- A self-test proving the rule catches the source failure

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `non_deterministic_check` | Check logic requires LLM inference · not a rule | JELLY · re-route |
| `over_narrow_rule` | Rule only catches exact-match pairs · no breadth | JELLY · Sr review |
| `over_broad_rule` | Rule catches many false positives in the test corpus | JELLY · Sr review |
| `missing_remediation` | Trigger + check defined but no remediation action | PROPOLIS · schema violation |
| `self_test_fail` | Rule doesn't trigger on its own source pair | PROPOLIS · refinery failure |
| `infra_dependency_unmet` | Remediation requires infra the customer doesn't have | JELLY · escalate |

## Scoring Impact

- **assignment_success**: MEDIUM · prevention is long-term value · doesn't move today's lift
- **repair_lift**: NEUTRAL · prevent doesn't change the source pair's score
- **validator_confidence**: MEDIUM · validators verify the self-test
- **risk_temperature**: INVERSE · good prevent rule lowers customer's ongoing risk
- **probability_of_close**: HIGH · the prevent layer is the long-term retention story
- **evidence_strength**: HIGH · the rule is deterministic and re-testable
- **cost_to_mint**: LOW · prevent is short-output (~1000-2000 tokens)

## Deed / Receipt Impact

- **Receipt fields touched**: `prevent.trigger_condition` · `prevent.check_logic` · `prevent.remediation` · `prevent.self_test_pass`
- **DDEED class impact**: prevent rules accumulate into a per-customer guardrail registry · referenced from DDEED-DOV-REPAIR
- **Books and records layer**: L1 PostgreSQL (rule registry) → L4 Hedera HCS (rule hash anchor)
- **5 Proofs touched**: PROCESS (the rule's lineage from a real failure) · QUALITY (the self-test verdict) · TRUST (deterministic and verifiable)

## Related Terms

- [diagnose-task](diagnose-task.md) · RJ task #1 · feeds the trigger
- [repair-task](repair-task.md) · RJ task #2 · informs the remediation
- [detect-task](detect-task.md) · RJ task #4 · partner classifier
- [compare-task](compare-task.md) · RJ task #5
- [swarmfixer](swarmfixer.md) · the refinery
- [pair-candidate](pair-candidate.md) · the unit prevent rules are derived from

## Example

> **Diagnose**: REASONING_GAP · READ bucket · severity 3 (journal-entry DR/CR reversal)
>
> **Repair**: corrected output + entity_direction_lookup tool call
>
> **Prevent Task output**:
> ```yaml
> trigger_condition:
>   pattern_type: INPUT_SHAPE
>   pattern_definition: "Any journal-entry input where vendor_id is present AND entity_direction_lookup was NOT called"
> check_logic:
>   check_type: TOOL_CALL_GUARD
>   check_definition: "if input.vendor_id and 'entity_direction_lookup' not in tool_calls: BLOCK"
> remediation:
>   action_class: BLOCK_AND_REPROMPT
>   action_detail: "Refuse the journal entry · re-prompt the agent to call entity_direction_lookup(vendor_id) first · then resume"
> confidence: 0.94
> proposed_pack_version: v.next
> self_test:
>   ran_against: "<source_pair_id>"
>   triggered: true
>   would_have_blocked: true
> ```

## DefendableOS Notes

- The Prevent Task is what compounds across customers · one customer's bad day becomes every customer's defense
- Deterministic-only is non-negotiable · LLM-checks-on-LLM-outputs is a regression to opinion · the whole point of the rule layer is to escape opinion
- Prevent rules with self_test_pass = true and customer-adoption = true become CANONICAL guardrails published in the next AdversarialPack release

🐝 *The prevent is the title insurance. Deterministic. Testable. Compounds.*
