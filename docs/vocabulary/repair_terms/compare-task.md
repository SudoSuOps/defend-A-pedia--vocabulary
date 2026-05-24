# Compare Task

## Street Definition

"Did the fix actually move the number?" That's the question that decides the bucket. **Compare Task** is RJ task #5 · the ranked outputs scored on 4 dimensions. It's the appraisal · the before-and-after comp · the proof that the rehab actually lifted the cap rate. The compare IS the receipt for the lift.

## CRE Operator Meaning

In CRE the Compare Task is the **appraisal report**. The asset was worth $X before the rehab. After the rehab, it's worth $Y. The appraiser doesn't take your word for it · they pull the comp set, they walk the building, they cross-reference recent sales, they score the asset on 4-5 dimensions (income · expenses · NOI · cap rate · physical condition), and they sign the report. The appraisal is what the lender funds against, what the buyer wires against, what the IRS audits against. Compare is the appraisal of the agent economy.

## DefendableOS Definition

The Compare Task is the fifth of the 5 Royal Jelly tasks SwarmFixer emits. It generates a ranked comparison of multiple candidate outputs (typically the original failed output, the repaired output, and 1-2 alternative repair candidates) scored on 4 dimensions: **correctness · completeness · format_compliance · reasoning_depth**. The compare IS the deterministic evidence behind the Repair Lift number. Without compare, the lift is a model opinion · with compare, the lift is a defensible measurement.

## Backend Representation

```json
{
  "compare.task_id": {"type": "string", "format": "rj-comp-<run_id>"},
  "compare.candidates": {
    "type": "array",
    "minItems": 2,
    "items": {
      "type": "object",
      "required": ["candidate_id", "source", "output"],
      "properties": {
        "candidate_id": {"type": "string"},
        "source": {"type": "enum", "values": ["ORIGINAL_AGENT", "SWARMFIXER_REPAIR", "ALTERNATIVE_REPAIR_A", "ALTERNATIVE_REPAIR_B"]},
        "output": {"type": "string"}
      }
    }
  },
  "compare.scoring_matrix": {
    "type": "object",
    "required": ["correctness", "completeness", "format_compliance", "reasoning_depth"],
    "patternProperties": {
      "^(correctness|completeness|format_compliance|reasoning_depth)$": {
        "type": "object",
        "additionalProperties": {"type": "number", "minimum": 0.0, "maximum": 1.0}
      }
    }
  },
  "compare.ranking": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "rank": {"type": "integer", "min": 1},
        "candidate_id": {"type": "string"},
        "composite_score": {"type": "number"}
      }
    }
  },
  "compare.confidence": {"type": "float", "range": [0.0, 1.0]},
  "compare.tiebreaker_rationale": {"type": "string", "nullable": true}
}
```

Schema files: `docs/schemas/royal_jelly_record.schema.json` · `docs/schemas/compare_task.schema.json`

## Client Explanation

The Compare Task is the proof line on your invoice. We don't just say "we fixed it." We ship a ranked comparison · the original agent's output · the repair we shipped · two alternative repairs we considered · all four scored on the same four dimensions. You can read the matrix, you can verify the ranking, you can re-derive the score yourself. That's why the receipts are anchored on a public chain · not because we're trying to be cute, but because audit is the asset.

## Jr Broker Use

The Jr Hack verifies the Compare Task includes at least 2 candidates · MINIMUM the original agent output and the repaired output. If only one candidate is present, there's nothing to compare · the lift is undefined. Re-route. Also verify all 4 dimensions are scored for every candidate · partial matrices are schema violations.

## Sr Broker Use

The Sr Hack reads the Compare Task for **rank stability**. If the same comparison run twice produces different rankings, the underlying scoring is non-deterministic · TEMP isn't locked or the prompt has variance. The Sr Hack triggers a refinery health check · because rank-instability poisons the Repair Lift number downstream.

## Tribunal Use

- **Rule layer**: Compare Task MUST have ≥ 2 candidates · MUST score all 4 dimensions for every candidate · MUST produce a ranking (C05 format compliance)
- **Rule layer**: The 4 dimensions are fixed: correctness · completeness · format_compliance · reasoning_depth · no substitutes accepted
- **Judge layer**: Tribunal re-runs the comparison at TEMP=0.05 · rank drift > 1 position between runs flags low-confidence
- **Classification impact**: Compare Task with rank instability blocks Royal Jelly promotion · the record drops to JELLY for re-run

## Evidence Required

- All candidate outputs (original + repaired + any alternatives)
- The 4-dimension scoring matrix · one row per candidate
- The composite scores per candidate (typically equal-weighted average)
- The final ranking with rank stability check
- A tiebreaker rationale if any candidates tie on composite

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `single_candidate` | Only 1 candidate · nothing to compare | PROPOLIS · schema violation |
| `partial_matrix` | One or more candidates missing scores on ≥ 1 dimension | PROPOLIS · schema violation |
| `non_4_dimensions` | Scoring uses a different dimension set | JELLY · re-route |
| `rank_instability` | Two runs produce different rankings · TEMP not locked | JELLY · health check |
| `tied_no_rationale` | Two candidates tie on composite · no tiebreaker explanation | JELLY · re-route |
| `repaired_loses` | Repaired output ranks BELOW original | PROPOLIS · refinery failure |

## Scoring Impact

- **assignment_success**: HIGH · compare IS the defensible evidence for the lift
- **repair_lift**: DIRECT · the compare scoring is the source-of-truth for the Repair Lift dial
- **validator_confidence**: HIGH · validators read compare to verify the lift number
- **risk_temperature**: NEUTRAL
- **probability_of_close**: HIGH · the compare matrix is what skeptical customers ask for in proof-of-value calls
- **evidence_strength**: HIGH · the matrix IS the evidence
- **cost_to_mint**: MEDIUM · compare is moderate tokens (~2000-3500) because it must score multiple candidates

## Deed / Receipt Impact

- **Receipt fields touched**: `compare.scoring_matrix` · `compare.ranking` · `compare.confidence` · `compare.tiebreaker_rationale`
- **DDEED class impact**: compare matrix is embedded in DDEED-DOV-REPAIR · queryable by dimension (e.g., "show all deeds where reasoning_depth lift > 0.2")
- **Books and records layer**: L1 PostgreSQL → L2 Merkle (scoring matrix as Merkle leaf) → L4 Hedera HCS
- **5 Proofs touched**: QUALITY (the dimensional scoring) · PROCESS (the multi-candidate evaluation) · TRUST (re-derivable from anchored matrix)

## Related Terms

- [diagnose-task](diagnose-task.md) · RJ task #1
- [repair-task](repair-task.md) · RJ task #2 · produces a candidate compared here
- [prevent-task](prevent-task.md) · RJ task #3
- [detect-task](detect-task.md) · RJ task #4
- [repair-lift](repair-lift.md) · the dial compare feeds
- [swarmfixer](swarmfixer.md) · the refinery

## Example

> **Compare Task output**:
> ```yaml
> candidates:
>   - candidate_id: cand-001
>     source: ORIGINAL_AGENT
>     output: '{"dr": "Accounts Receivable", "cr": "Revenue", "amount": 12500}'
>   - candidate_id: cand-002
>     source: SWARMFIXER_REPAIR
>     output: '{"dr": "COGS", "cr": "Accounts Payable", "amount": 12500, "memo": "Vendor invoice INV-2026-0142"}'
>   - candidate_id: cand-003
>     source: ALTERNATIVE_REPAIR_A
>     output: '{"dr": "COGS", "cr": "Accounts Payable", "amount": 12500}'
> scoring_matrix:
>   correctness:    {cand-001: 0.30, cand-002: 0.98, cand-003: 0.95}
>   completeness:   {cand-001: 0.85, cand-002: 0.95, cand-003: 0.80}
>   format_compliance: {cand-001: 0.95, cand-002: 0.95, cand-003: 0.90}
>   reasoning_depth: {cand-001: 0.40, cand-002: 0.88, cand-003: 0.75}
> ranking:
>   - {rank: 1, candidate_id: cand-002, composite_score: 0.940}
>   - {rank: 2, candidate_id: cand-003, composite_score: 0.850}
>   - {rank: 3, candidate_id: cand-001, composite_score: 0.625}
> confidence: 0.93
> tiebreaker_rationale: null
> ```

## DefendableOS Notes

- The 4 dimensions are constitutional · changing them changes every downstream lift calculation · changes require a doctrine PR · NOT a config flip
- Compare is what makes the Repair Lift number defensible to a third-party auditor · the auditor can re-run the comparison at TEMP=0.05 and re-derive the lift
- A "repaired_loses" outcome is one of the few PROPOLIS routes that auto-triggers a refinery diagnostic · because a refinery that ships regressions is broken

🐝 *The compare is the appraisal. Four dimensions. Ranked candidates. Defensible lift.*
