# Pair Candidate

## Street Definition

"What's in the pipeline?" That's the Sr Hack at standup. **Pair Candidate** is the unit that flows through DefendableOS · the (input, output) pair captured by DefendableRouter · graded by the Tribunal · routed through the buckets · refined by SwarmFixer · deeded by the minter. One unit. One lifecycle. Six possible buckets.

## CRE Operator Meaning

In CRE the Pair Candidate is the **deal in the pipeline**. Some deals are still in discovery (pending) · some are signed and producing (Honey) · some are stuck in DD (Jelly) · some need workout (jelly-repaired) · some blew up (Propolis) · some are quarantined for fraud review. The pipeline isn't a list · it's a stack of folders · each folder has a label · the label IS the state. No separate state machine · the folder is the truth.

## DefendableOS Definition

A Pair Candidate is the canonical unit of work in DefendableOS. It binds an input (the prompt/context the agent received) with an output (the agent's response) plus all the metadata captured by DefendableRouter at the moment of the call. Pair Candidates flow through 6 mutually-exclusive buckets that represent their lifecycle state. The bucket IS the state · there is no separate state machine.

## Backend Representation

```json
{
  "pair_candidate.id": {"type": "string", "format": "pair-<utc-ts>-<short-hash>"},
  "pair_candidate.agent_ens": {"type": "string", "format": "<agent>.<operator>.defendable.eth"},
  "pair_candidate.input": {"type": "string"},
  "pair_candidate.output": {"type": "string"},
  "pair_candidate.model_used": {"type": "string"},
  "pair_candidate.timestamp": {"type": "string", "format": "date-time"},
  "pair_candidate.router_receipt_id": {"type": "string"},
  "pair_candidate.bucket": {
    "type": "enum",
    "values": ["pending", "honey", "jelly", "jelly-repaired", "propolis-failures", "quarantined"]
  },
  "pair_candidate.tribunal_verdict_id": {"type": "string", "nullable": true},
  "pair_candidate.agenthash_bucket": {"type": "string", "nullable": true},
  "pair_candidate.failure_mode_tag": {"type": "string", "nullable": true},
  "pair_candidate.evidence_strength": {"type": "float", "range": [0.0, 1.0]},
  "pair_candidate.created_at": {"type": "string", "format": "date-time"},
  "pair_candidate.bucket_changed_at": {"type": "string", "format": "date-time"}
}
```

Schema files: `docs/schemas/pair_candidate.schema.json` · `docs/schemas/router_receipt.schema.json`

## Client Explanation

A Pair Candidate is one of your AI agent's calls · with our metadata around it. We capture every call your agent makes (we don't slow it down · sub-5ms · invisible to the agent). Then overnight we grade it, route it to one of 6 buckets based on quality, and either ship a deed (Honey) · refine it (Jelly) · or flag it for the AdversarialPack (Propolis). Your morning brief shows the bucket flow from the prior 24 hours.

## Jr Broker Use

The Jr Hack reads the bucket flow every morning. The bucket counts ARE the dashboard · pending/honey/jelly/jelly-repaired/propolis-failures/quarantined. A pair that's been in `pending/` for > 24h is a stuck pair · escalate. A spike in `quarantined/` is a model regression signal · escalate. The Jr Hack doesn't re-classify pairs on their own · they route per the Tribunal verdict + playbook.

## Sr Broker Use

The Sr Hack monitors bucket-flow ratios. A healthy week shows ~70-85% Honey · 10-20% Jelly · 5-10% Jelly-Repaired · < 5% Propolis · < 1% Quarantined. Drift from these ratios is the first sign of a system change · customer's agent regression · model provider change · prompt drift · or refinery degradation. The Sr Hack triages the cause before the daily flow stabilizes against the new baseline.

## Tribunal Use

- **Rule layer**: Every Pair Candidate MUST have a router_receipt_id · no orphan pairs · the receipt anchors the pair to a real-world capture
- **Rule layer**: Bucket transitions MUST be logged · any pair changing bucket without an associated decision receipt is rejected and re-quarantined
- **Judge layer**: Tribunal grades the pair to produce a verdict · the verdict drives the initial bucket assignment
- **Classification impact**: The bucket field IS the Tribunal's externally visible decision · downstream systems read the bucket, not the verdict directly

## Evidence Required

- Router capture receipt (proves the pair came from the wire, not synthesized)
- Agent ENS identity (proves the originating agent)
- Timestamp (proves temporal ordering)
- Tribunal verdict (proves the bucket assignment is justified)
- Bucket-change audit trail (proves the lifecycle is traceable)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `orphan_pair` | Pair Candidate present without a router_receipt_id | PROPOLIS · auto-quarantine |
| `unbacked_bucket_transition` | Bucket changed without an associated decision receipt | PROPOLIS · governance violation |
| `stuck_pending` | Pair in `pending/` > 24h with no refinery attempt | JELLY · operator escalation |
| `manual_promotion` | Pair manually moved to higher bucket without Tribunal pass | PROPOLIS · governance violation |
| `missing_ens` | Pair has no agent_ens · downstream deed can't anchor | JELLY · re-route to ENS-fix queue |
| `evidence_strength_zero` | Pair has zero evidence strength · refinery cannot work on it | JELLY · re-route to evidence-gathering |

## Scoring Impact

- **assignment_success**: HIGH · bucket flow IS the work product
- **repair_lift**: INDIRECT · pairs in jelly/ are the lift's denominator
- **validator_confidence**: HIGH · bucket discipline IS the validator's primary trust signal
- **risk_temperature**: DIRECT · quarantined/propolis spike = high risk
- **probability_of_close**: HIGH · customer dashboards show bucket-flow ratios · ratios drive renewal
- **evidence_strength**: SELF · the pair carries its own evidence strength score
- **cost_to_mint**: NEUTRAL · cost is per-deed, not per-pair

## Deed / Receipt Impact

- **Receipt fields touched**: `pair_candidate.id` · `pair_candidate.bucket` · `pair_candidate.tribunal_verdict_id` · `pair_candidate.router_receipt_id`
- **DDEED class impact**: every deed references the source pair_candidate.id · deeds are downstream of pairs · pairs are upstream of deeds
- **Books and records layer**: L1 PostgreSQL → L2 Merkle → L3 NAS (raw pair) → L4 Hedera HCS (pair_id + bucket transitions) → L5 ENS (per-agent rollup)
- **5 Proofs touched**: ORIGIN (the router receipt) · PROCESS (the bucket lifecycle) · QUALITY (the Tribunal verdict) · TRUST (the deed lineage)

## Related Terms

- [swarmfixer](swarmfixer.md) · refines pairs in `jelly/`
- [swarmjelly](swarmjelly.md) · the model used in refinery
- [defendablejelly](defendablejelly.md) · the customer-facing product
- [repair-lift](repair-lift.md) · the lift measured per-pair
- [defendablerouter](../defendableos_terms/defendablerouter.md) · captures pairs at <5ms
- [diagnose-task](diagnose-task.md) · pair input for refinery

## Example

> **Capture**: 2026-05-24T06:12:08Z · books-bot.acmecorp.defendable.eth · model gpt-4o-2024-08-06 · 1,142 tokens in · 318 tokens out · router latency 3ms
>
> **Pair created**: `pair-20260524T061208Z-7e2a`
>
> **Initial bucket**: `pending/` (awaiting overnight Tribunal grading)
>
> **Tribunal verdict 06:14**: JELLY · composite 0.760 · AgentHash READ · failure_mode REASONING_GAP · evidence_strength 0.68 · judge_drift 0.08
>
> **Bucket transition**: `pending/` → `jelly/` at 06:14:32Z · transition receipt `bt-20260524T061432Z-rt9`
>
> **SwarmFixer run 07:12**: refinery produces 5-task RJ Record · Repair Lift +0.15 · validator confidence 0.78
>
> **Bucket transition**: `jelly/` → `jelly-repaired/` at 07:18:00Z · transition receipt `bt-20260524T071800Z-q3k`
>
> **Deed minted 07:22**: `DDEED-DOV-REPAIR-ACMECORP-BOOKS-000142-v1`
>
> **Final state**: archived in `jelly-repaired/` · referenced by deed · resolvable on ENS

## DefendableOS Notes

- The 6-bucket model is constitutional · not configurable · adding a 7th bucket requires a doctrine PR
- The bucket IS the state · the file system IS the source of truth · this is intentional · it makes auditing trivial (`ls` is the verifier)
- A pair NEVER skips a bucket · transitions are always to an adjacent bucket per the playbook · no "manual promotions to honey" · no exceptions
- Pair Candidates are the atomic unit of every DefendableOS receipt · receipts are pair-derived · deeds are receipt-derived · everything starts here

🐝 *Six buckets. One unit. The folder is the truth.*
