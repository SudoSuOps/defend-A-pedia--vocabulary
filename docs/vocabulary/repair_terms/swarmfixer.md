# SwarmFixer

## Street Definition

"Push it to the fixer." That's the line a Sr Hack uses when a Tribunal verdict comes back JELLY and the pair needs work. SwarmFixer is the **agent refinery** · the production layer that takes a low-grade agent output and turns it into a defendable Royal Jelly Record. Not a chatbot. Not a model wrapper. A refinery.

## CRE Operator Meaning

In CRE you have the **listing broker** and you have the **rehab crew**. The listing broker brings the deal in. The rehab crew makes the asset rentable. SwarmFixer is the rehab crew of the agent economy. Tenant moved out · roof leaking · rent roll thin · the building doesn't pencil. The rehab crew comes in · scopes the work · executes the repair · the building re-leases at a higher cap-rate-compressed comp. The lift is what makes the deal. **Repair Lift is NOI for agents.**

## DefendableOS Definition

SwarmFixer is the in-house repair service that consumes Jelly-tier pair candidates and produces Royal Jelly Records via a strict 5-task output: DIAGNOSE · REPAIR · PREVENT · DETECT · COMPARE. It runs on **SwarmJelly-4B** at `whale:11434` with TEMP locked at 0.05. It ships in three commercial tiers · Self-serve ($99-$499/mo) · Managed ($2K-$10K/mo) · Embedded ($50K-$250K ARR with 90-day Fix-or-Refund). Every successful refinery run produces a DDEED-DOV-REPAIR anchored on Hedera HCS.

## Backend Representation

```json
{
  "swarmfixer.run_id": {"type": "string", "format": "ag-fix-<utc-ts>-<short-hash>"},
  "swarmfixer.model_id": {"type": "string", "enum": ["swarmjelly-4b:v1.2"]},
  "swarmfixer.endpoint": {"type": "string", "default": "whale:11434"},
  "swarmfixer.temperature": {"type": "float", "const": 0.05},
  "swarmfixer.tier": {"type": "enum", "values": ["SELF_SERVE", "MANAGED", "EMBEDDED"]},
  "swarmfixer.task_outputs": {"type": "object", "required": ["diagnose","repair","prevent","detect","compare"]},
  "swarmfixer.repair_lift": {"type": "float", "range": [-1.0, 1.0]},
  "swarmfixer.validator_confidence": {"type": "float", "range": [0.0, 1.0]},
  "swarmfixer.bucket_destination": {"type": "enum", "values": ["jelly-repaired","pending","quarantined","propolis-failures"]}
}
```

Schema files: `docs/schemas/royal_jelly_record.schema.json` · `docs/schemas/repair_run.schema.json`

Scoring hooks: `repair_lift` · `jelly_score` · `royal_jelly_promotion`

## Client Explanation

SwarmFixer is the part of DefendableOS that fixes the agents you're already running. When your AI agent ships a low-quality answer · or a borderline one · we don't throw it away and we don't ship it. We refine it. Five outputs come back: what went wrong · how to fix it · how to prevent the next one · how to detect it next time · and how the fix compares to the original. You pay for the lift · not the diagnosis. If we don't move the number · the embedded tier refunds.

## Jr Broker Use

Don't run SwarmFixer on Honey-tier pairs (waste of compute). Don't run it on Propolis pairs directly (they need the AdversarialPack pipeline first). Do run it on Jelly-tier pairs once they're tagged with an AgentHash bucket and have evidence strength ≥ 0.4. Always verify TEMP=0.05 before triggering · read the env, read the config, read the request payload. If any of the three reads ≠ 0.05, ABORT.

## Sr Broker Use

The Sr Hack reads the 5-task output as a unit · not piece by piece. The DIAGNOSE without the COMPARE is half a story. The REPAIR without the PREVENT is a one-time fix. The DETECT without the AgentHash tag is a smoke alarm with no zone map. Sr Hacks adjudicate on the COMPLETENESS of the 5-task record · then on the Repair Lift · then on the validator chain pass rate. Three reads. One verdict.

## Tribunal Use

- **Rule layer**: SwarmFixer outputs MUST contain all 5 tasks (C01) · MUST be generated at TEMP=0.05 (C02) · MUST tag the 7-mode taxonomy + AgentHash bucket (C03)
- **Critical failure**: missing task, wrong TEMP, or untagged taxonomy = PROPOLIS verdict on the refinery run · the repair doesn't count
- **Judge layer**: Tribunal grades the REPAIR task output as if it were a fresh agent submission · the lift is the delta between original and repaired composite score
- **Classification impact**: A successful refinery run can promote a JELLY pair to ROYAL JELLY · but the original failure is never erased · the lineage is preserved on the deed

## Evidence Required

- Original failed pair (input + agent output + Tribunal verdict)
- AgentHash bucket tag (one of STOP/CALL/READ/RECOVER/LOOP)
- ENS identity of the originating agent
- Evidence strength ≥ 0.4 on the source pair
- Model config snapshot proving TEMP=0.05
- Validator chain result (12 checks · 7 critical + 5 advisory)
- Re-bench Tribunal verdict on the repaired output

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `temp_drift` | SwarmFixer called at TEMP ≠ 0.05 (default 0.7 catastrophic: 0.7% Honey rate) | PROPOLIS |
| `partial_task_output` | Fewer than 5 tasks returned · the contract is broken | PROPOLIS |
| `untagged_taxonomy` | DIAGNOSE didn't tag the 7-mode failure or the AgentHash bucket | JELLY |
| `negative_lift` | Repaired output scored LOWER than original · regression | PROPOLIS (refinery failure) |
| `fabricated_evidence` | REPAIR task cites sources that don't exist in the input | PROPOLIS · auto-quarantine |
| `judge_drift_high` | Scale-A and Scale-B judges disagree > 0.15 on the repair | JELLY · contested · escalate |
| `low_confidence_task` | Any of the 5 tasks returns confidence < 0.50 | JELLY · re-route to pending |

## Scoring Impact

- **assignment_success**: HIGH · the refinery IS the assignment for any Tier-2/Tier-3 customer
- **repair_lift**: DIRECT · SwarmFixer is the engine that produces the lift
- **validator_confidence**: HIGH · validator chain runs on every refinery output · low pass rate = low confidence in the refinery itself
- **risk_temperature**: INVERSE · more refinery throughput = lower production risk
- **probability_of_close**: HIGH on Tier-3 · the Fix-or-Refund clause is what gets the contract signed
- **evidence_strength**: NEUTRAL · refinery doesn't manufacture evidence · it works with what's there
- **cost_to_mint**: MEDIUM · ~$0.05 per refinery run (SwarmJelly-4B inference cost) + $0.0052 deed mint

## Deed / Receipt Impact

- **Receipt fields touched**: `swarmfixer.run_id` · `repair_lift` · `validator_confidence` · `bucket_destination` · `5_task_hash`
- **DDEED class impact**: produces `DDEED-DOV-REPAIR-<agent>-<seq>-v<n>` on every `jelly-repaired/` transition
- **Books and records layer**: L1 PostgreSQL → L2 Merkle → L3 NAS → L4 Hedera HCS → L5 ENS (full 5-layer)
- **5 Proofs touched**: PROCESS (the refinery lineage) · QUALITY (the 5-task validator pass) · ECONOMICS (the inference + deed cost) · TRUST (the Hedera + ENS anchor)

## Related Terms

- [swarmjelly](swarmjelly.md) · the 4B model behind the refinery
- [defendablejelly](defendablejelly.md) · the public-facing brand for the repair layer
- [repair-lift](repair-lift.md) · the lift dial the refinery is measured on
- [pair-candidate](pair-candidate.md) · the unit that flows through
- [diagnose-task](diagnose-task.md) · RJ task #1
- [repair-task](repair-task.md) · RJ task #2
- [prevent-task](prevent-task.md) · RJ task #3
- [detect-task](detect-task.md) · RJ task #4
- [compare-task](compare-task.md) · RJ task #5
- [temp-five-cent-rule](../defendableos_terms/temp-five-cent-rule.md) · the LOCKED TEMP doctrine

## Example

> **Customer**: ACMECorp · Tier-3 embedded · books-bot.acmecorp.defendable.eth
>
> **Failure**: agent generated journal entry with debit/credit reversed · Tribunal verdict JELLY · composite 76 · taxonomy = REASONING_GAP · AgentHash = READ (misread the invoice direction)
>
> **SwarmFixer run**: `ag-fix-20260524T071200Z-9a3c` · SwarmJelly-4B v1.2 · TEMP=0.05
>
> **5-task output**:
> - DIAGNOSE · root cause = misclassified invoice as inbound when it was outbound · severity 3 · action = retrain on direction-tagged corpus
> - REPAIR · corrected journal entry · DR Accounts Receivable $X · CR Revenue $X
> - PREVENT · check that vendor/customer ID matches the expected direction before posting
> - DETECT · flag any journal entry where DR/CR sign matches the OPPOSITE of the entity-direction lookup
> - COMPARE · repaired output 91/100 vs original 76/100 · all 4 dims improved
>
> **Repair Lift**: 91 - 76 = **+0.15** (≥ 0.10 threshold)
>
> **Validator chain**: 7/7 critical pass · 4/5 advisory pass
>
> **Transition**: `jelly/` → `jelly-repaired/`
>
> **Deed minted**: `DDEED-DOV-REPAIR-ACMECORP-BOOKS-000142-v1` · anchored on Hedera HCS topic 0.0.10291838 · ENS at `ddeed-dov-repair-acmecorp-books-000142-v1.swarmbee.defendable.eth`

## DefendableOS Notes

- SwarmFixer NEVER sits in the customer's real-time call path · always overnight/shadow-mode
- The refinery is the moat · the lift is the receipt · the deed is the customer asset
- Tier-3 Fix-or-Refund is the killer clause that gets brokerage-class deals signed
- The refinery's training set is 125K pairs · 7-mode × 5-RJ-task taxonomy · 25% distribution cap enforced

🐝 *The refinery is the moat. Push it to the fixer.*
