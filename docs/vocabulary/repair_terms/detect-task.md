# Detect Task

## Street Definition

"Does this LOOK like the same failure?" That's the question every operator asks when a flagged pair comes in. **Detect Task** is RJ task #4 · the positive/negative classifier with evidence. Given a new input · does it match THIS failure class · yes or no · with the evidence that proves the call.

## CRE Operator Meaning

In CRE the Detect Task is the **smoke alarm in every unit**. Each alarm is calibrated to a specific signal (smoke · CO · heat). Cheap to install · loud when it fires · zero false-positive tolerance. The alarm doesn't put out the fire · it just calls it early. Detect doesn't fix the agent · it just calls the failure early. The earlier you call it · the smaller the loss.

## DefendableOS Definition

The Detect Task is the fourth of the 5 Royal Jelly tasks SwarmFixer emits. It produces a binary classifier (positive/negative) for the specific failure pattern identified in the Diagnose Task. It runs in two modes: in-line (live agent traffic) and offline (sweep historic logs). The classifier carries the evidence it used to make the call · the operator can audit any classification by reading the evidence chain.

## Backend Representation

```json
{
  "detect.task_id": {"type": "string", "format": "rj-det-<run_id>"},
  "detect.classifier_type": {"type": "enum", "values": ["DETERMINISTIC", "ML_LIGHTWEIGHT", "HYBRID"]},
  "detect.classifier_definition": {"type": "string"},
  "detect.input_signature": {
    "type": "object",
    "required": ["fields_required"],
    "properties": {
      "fields_required": {"type": "array", "items": {"type": "string"}},
      "fields_optional": {"type": "array", "items": {"type": "string"}}
    }
  },
  "detect.output_class": {"type": "enum", "values": ["POSITIVE", "NEGATIVE"]},
  "detect.evidence_chain": {
    "type": "array",
    "items": {
      "type": "object",
      "required": ["evidence_type", "evidence_value"],
      "properties": {
        "evidence_type": {"type": "string"},
        "evidence_value": {"type": "string"},
        "weight": {"type": "float", "range": [0.0, 1.0]}
      }
    }
  },
  "detect.confidence": {"type": "float", "range": [0.0, 1.0]},
  "detect.false_positive_rate_estimated": {"type": "float", "range": [0.0, 1.0]},
  "detect.runtime_budget_ms": {"type": "integer", "max": 50}
}
```

Schema files: `docs/schemas/royal_jelly_record.schema.json` · `docs/schemas/detect_task.schema.json`

## Client Explanation

The Detect Task is the smoke alarm for your AI fleet. Once we identify a failure pattern, we ship you a lightweight classifier you can wire into your runtime · it runs in under 50ms per check · it doesn't slow your agent down · and it surfaces the failure pattern the moment it appears in the wild. Plus the evidence behind every classification, so you can audit.

## Jr Broker Use

The Jr Hack verifies the Detect Task's runtime budget · MUST be ≤ 50ms per check · because the customer wires this into their hot path. A 200ms classifier is useless · the customer rips it out. The Jr Hack also verifies the estimated false-positive rate is bounded · typically < 5% · because a noisy detector erodes operator trust faster than a missed detection.

## Sr Broker Use

The Sr Hack monitors the production false-positive rate vs the estimated rate · if production FP rate exceeds 2× the estimate, the detector is over-eager and needs re-tuning. The Sr Hack also tracks the detector's true-positive lift in the customer's actual traffic · a detector that fires 0 times in 30 days is either dead code or the prevent rule worked too well · either way, it gets reviewed.

## Tribunal Use

- **Rule layer**: Detect Task MUST have a runtime_budget_ms ≤ 50 · MUST be one of the 3 classifier types · MUST have an evidence_chain (no opaque classifications)
- **Rule layer**: Estimated false_positive_rate MUST be ≤ 0.05 · higher rates auto-reject
- **Judge layer**: Tribunal evaluates the detector by running it against the original failed pair (must POSITIVE) AND a set of known-Honey pairs (should be NEGATIVE) · selectivity score is a Tribunal axis
- **Classification impact**: A detector with > 10% false-positive on the Honey test set blocks RJ promotion · the whole record drops to JELLY

## Evidence Required

- The Diagnose Task output (defines the failure pattern)
- The classifier definition (deterministic code OR ML-model artifact reference)
- The input signature (what fields the classifier needs)
- The runtime budget benchmark (proven ≤ 50ms)
- The selectivity test result (positive on source pair · negative on Honey set)
- The estimated false-positive rate with sample size

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `over_budget_runtime` | Classifier > 50ms per check · unusable in hot path | JELLY · re-route |
| `opaque_classification` | No evidence_chain · classifier emits verdict without justification | PROPOLIS · schema violation |
| `high_false_positive` | Estimated FP rate > 0.05 · or production FP > 2× estimate | JELLY · re-tune |
| `fails_self_test_positive` | Classifier returns NEGATIVE on its own source failure pair | PROPOLIS · refinery failure |
| `fails_honey_test_negative` | Classifier returns POSITIVE on > 10% of Honey test set | JELLY · re-route |
| `missing_input_signature` | Required fields not enumerated · customer can't wire it in | JELLY · schema gap |

## Scoring Impact

- **assignment_success**: HIGH · the detector is what scales the prevent layer to production traffic
- **repair_lift**: NEUTRAL · detector doesn't change the source pair score
- **validator_confidence**: MEDIUM · validators run the selectivity tests
- **risk_temperature**: INVERSE · detector lowers ongoing customer risk · false-positive detector raises operator trust risk
- **probability_of_close**: MEDIUM · detectors are part of the long-term retention story
- **evidence_strength**: HIGH · every classification carries its evidence chain
- **cost_to_mint**: LOW · detect is short-output and the runtime cost is the customer's, not ours

## Deed / Receipt Impact

- **Receipt fields touched**: `detect.classifier_definition` (hashed) · `detect.input_signature` · `detect.runtime_budget_ms` · `detect.false_positive_rate_estimated`
- **DDEED class impact**: detect classifiers accumulate into a per-customer detector registry · referenced from DDEED-DOV-REPAIR
- **Books and records layer**: L1 PostgreSQL (detector registry) → L4 Hedera HCS (classifier hash anchor)
- **5 Proofs touched**: QUALITY (the selectivity test) · PROCESS (lineage from source failure) · TRUST (evidence chain on every classification)

## Related Terms

- [diagnose-task](diagnose-task.md) · RJ task #1 · defines what to detect
- [repair-task](repair-task.md) · RJ task #2
- [prevent-task](prevent-task.md) · RJ task #3 · partner rule
- [compare-task](compare-task.md) · RJ task #5
- [swarmfixer](swarmfixer.md) · the refinery
- [pair-candidate](pair-candidate.md) · the unit detectors are derived from

## Example

> **Diagnose**: REASONING_GAP · READ bucket · severity 3 (journal-entry DR/CR reversal)
>
> **Detect Task output**:
> ```yaml
> classifier_type: DETERMINISTIC
> classifier_definition: |
>   def classify(pair):
>       if pair.task_type != "journal_entry": return ("NEGATIVE", [])
>       if "entity_direction_lookup" in pair.tool_calls: return ("NEGATIVE", [...])
>       if pair.vendor_id_present: return ("POSITIVE", [...])
>       return ("NEGATIVE", [...])
> input_signature:
>   fields_required: ["task_type", "tool_calls", "vendor_id_present"]
>   fields_optional: ["amount", "direction_hint"]
> runtime_budget_ms: 4
> false_positive_rate_estimated: 0.02
> selectivity_test:
>   source_pair_classification: POSITIVE
>   honey_test_set_size: 200
>   honey_test_false_positive_count: 3
>   honey_test_false_positive_rate: 0.015
> confidence: 0.91
> ```

## DefendableOS Notes

- The Detect Task scales the Prevent Task to production · prevent is the rule · detect is the rule's eyes
- 50ms budget is non-negotiable because the customer's hot path won't tolerate more · DefendableOS is write-only on the hot path · detect is the only piece that runs in-line for the customer · it MUST be cheap
- Detect + Prevent together = the customer's runtime guardrail set · this is the layer that grows over time and becomes the customer's moat
- Detectors are open-source under MIT-with-receipt-clause · customers can self-host and modify · we only ask the receipts keep flowing

🐝 *The detect is the smoke alarm. Cheap. Fast. Auditable. Calls the failure early.*
