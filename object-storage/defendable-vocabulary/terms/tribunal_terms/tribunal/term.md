# Tribunal

> *"The Tribunal isn't a judge. It's six roles · two judges · one drift threshold · one Critic when they disagree · and Katniss when the deal smells like an attack. That's how you adjudicate. Anything less is just a vibes-check."*
> — Founder · the day the 6-role protocol was locked

## Street Definition

"What did the Tribunal return?" The Tribunal is the adjudication engine of the Hive · the 6-role pipeline that decides whether an AI output is Royal Jelly · Honey · Jelly · or Propolis. It is NOT one model. It is NOT a "judge prompt." It is a structural pipeline · rule-then-judge · 2-pass with a 0.15 drift threshold · with a Critic when the judges disagree and Katniss when the case turns adversarial. The Tribunal runs 24/7 at 777 pairs/hr on the swarmrails primary rig with whale and zima-edge holding backup roles.

In CRE language · the Tribunal is the underwriting committee · the title insurance underwriter · the appraisal review · the final sign-off before the deed transfers. Multiple eyes · structured discipline · documented dissents · the chain that protects the asset.

## CRE Operator Meaning

In CRE · the Tribunal maps to the multi-role underwriting chain · the inspector who walks the building · the appraiser who values it · the title underwriter who insures the chain of ownership · the closing agent who reconciles the documents · the lender's reviewer who confirms the credit. No single role decides the deed · the chain decides. Same here. The Tribunal is the chain that produces a defendable verdict.

## DefendableOS Definition

The Tribunal is the adjudication subsystem of the Hive · composed of 6 named roles:

1. **Scout** · fetches the pair · normalizes to PairCandidate format
2. **Router** · decides the lane (short / long / seal)
3. **Filter** · runs the 12-check validator chain (the rule layer)
4. **Repair** · invokes SwarmFixer when the pair lands Jelly
5. **Critic** · reconciles when drift between Scale A and Scale B exceeds 0.15
6. **Katniss** · adversarial best-of-3 final arbiter

Production config (locked 2026-05-24):
- Scale A judge: `gemma3:12b` on swarmrails GPU 1 (RTX PRO 4500 32GB Blackwell sm_120)
- Scale B judge: `qwen2.5:32b` on swarmrails GPU 0 (RTX PRO 6000 96GB Blackwell sm_120)
- Throughput target: 777 pairs/hr
- Protocol: rule_then_judge · 2 judges required · drift ≤ 0.15 · penalized scoring enabled

See [`docs/doctrine/08_tribunal_doctrine.md`](../../doctrine/08_tribunal_doctrine.md) for the full spec.

## Backend Representation

```json
{
  "tribunal.run_id": {
    "type": "string",
    "pattern": "^TRIB-[0-9]{8}T[0-9]{6}Z-[a-f0-9]{4}$"
  },
  "tribunal.pair_id": { "type": "string" },
  "tribunal.tier": {
    "type": "enum",
    "values": ["ROYAL_JELLY", "HONEY", "JELLY", "PROPOLIS", "GENESIS"]
  },
  "tribunal.score_final": { "type": "float", "range": [0.0, 1.0] },
  "tribunal.score_scale_a": { "type": "float" },
  "tribunal.score_scale_b": { "type": "float" },
  "tribunal.drift": { "type": "float" },
  "tribunal.critic_invoked": { "type": "boolean" },
  "tribunal.katniss_invoked": { "type": "boolean" },
  "tribunal.penalized_scoring_applied": { "type": "boolean" },
  "tribunal.record_hash": { "type": "string", "pattern": "^sha256:[a-f0-9]{64}$" }
}
```

Schema files: `docs/schemas/tribunal_verdict.schema.json` · `docs/schemas/tribunal_transitions.schema.json`

## Client Explanation

"The Tribunal" is our adjudication system · the 6-role pipeline that grades every AI output we ship to you. It runs two judges (a fast pass and a deep pass) against every pair · checks if they agree within a tight drift threshold · calls in a Critic when they don't · and escalates to a final arbiter (Katniss) when adversarial behavior is detected. The Tribunal produces a verdict (Royal Jelly · Honey · Jelly · Propolis) · a record hash · and a full audit trail. You see the verdict on every deed. You can verify the record hash on the public ledger.

## Jr Broker Use

The jr broker reads the Tribunal verdicts but does not adjudicate independently:

1. Every PairCandidate you submit goes to the Tribunal · the verdict comes back as `tribunal_verdict.tier` and `tribunal_verdict.score_final`
2. Trust the verdict · do NOT attempt to manually re-grade
3. Watch the dashboard for stuck Tribunal runs (no verdict within 4h) · escalate to sr broker
4. When a Tribunal verdict is the basis for a customer-facing deed · cite the run_id in the operator log
5. Drift cases · Critic invocations · Katniss invocations · all visible on the dashboard · learn to read them but do not act on them without sr broker oversight

**Rule of thumb**: the Tribunal adjudicates · you observe · the chain is the chain.

## Sr Broker Use

The sr broker operates the Tribunal:

- Daily Morning Brief includes the Tribunal volume · tier distribution · drift rate · Critic invocation rate · Katniss invocation rate · all Tribunal health metrics
- Override queue review at 06:30 · approve · escalate · or PASS on advisory-fail cases
- Manual Critic / Katniss invocations when judgment requires · operator discretion within doctrine
- Spot-audit Royal Jelly verdicts daily · 20 random pairs end-to-end
- Apply the PASS doctrine ruthlessly · the Tribunal protects the books · the sr broker protects the Tribunal

See [`docs/playbooks/tribunal_review_playbook.md`](../../playbooks/tribunal_review_playbook.md) for the full daily workflow.

## Tribunal Use

```yaml
tribunal_use:
  classification_impact: []   # the Tribunal itself does not get a tier · it ASSIGNS tiers
  rule_layer_checks:
    - tribunal.run_id MUST be populated for every verdict
    - tribunal.score_scale_a AND tribunal.score_scale_b MUST both be present (no single-judge verdicts)
    - tribunal.drift MUST be computed and logged
    - tribunal.record_hash MUST be computed before verdict is finalized
  judge_layer_prompt_hint: "this term IS the adjudication system · the judges run INSIDE the Tribunal"
  can_be_critical_failure: false   # Tribunal-level failures cascade to Hive-level alerts
```

## Evidence Required

To validate a Tribunal verdict:

- A populated TribunalRecord JSON (per `tribunal_verdict.schema.json`)
- Scale A score + reason
- Scale B score + reason
- Drift value
- Validator chain results (C01-C12)
- Critic reasoning if drift > 0.15
- Katniss best-of-3 results if adversarial-flagged
- Penalized-scoring application log if triggered
- SHA-256 record_hash of canonical JSON
- Ts timestamp

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **tribunal_single_judge_verdict** | A verdict issued with only one judge score | Rejected at C04 · verdict held · rig health audited · re-run |
| **tribunal_drift_unflagged** | Drift > 0.15 but Critic was not invoked | Integrity event · sr broker reviews the pair · Critic invoked retroactively · verdict re-issued if changed |
| **tribunal_katniss_skipped** | Adversarial flag raised but Katniss not invoked | Critical integrity event · verdict held · Katniss invoked retroactively · publication delayed |
| **tribunal_throughput_collapse** | Pairs-per-hour drops below 50% of 777 target for > 2h | Degraded-mode flag · customers notified · root cause investigation |
| **tribunal_penalty_skipped** | Auto-judge score < 0.75 with critical-issue but penalty not applied | Integrity event · verdict re-evaluated under rule layer only |

## Scoring Impact

- **assignment_success**: PROCESS-LEVEL · every assignment success depends on a Tribunal verdict
- **repair_lift**: PROCESS-LEVEL · the Tribunal re-grades repaired pairs and produces the lift measurement
- **validator_confidence**: PROCESS-LEVEL · the Tribunal's validator chain layer produces the confidence
- **risk_temperature**: PROCESS-LEVEL · adversarial Tribunal events feed the risk temperature gauge
- **probability_of_close**: PROCESS-LEVEL · the Tribunal's verdict on engagement deeds affects close prob
- **evidence_strength**: PROCESS-LEVEL · the Tribunal scores evidence as part of its rubric
- **cost_to_mint**: DIRECT · Tribunal compute (judges · Critic · Katniss · validator chain) is a line item in cost-to-mint

## Deed / Receipt Impact

- **Receipt fields touched**: `tribunal.run_id` · `tribunal.tier` · `tribunal.score_final` · `tribunal.record_hash`
- **DDEED class impact**: NO DDEED is issued without a Tribunal verdict · the verdict is the gate
- **Books and records layer**: ALL 5 · the Tribunal verdict spans the full finality stack
- **5 Proofs touched**: ALL 5 · the Tribunal IS the producer of QUALITY · contributes to PROCESS · informs ECONOMICS · validates ORIGIN · feeds TRUST

## Related Terms

- [validator](validator.md) · the auditor-bee role within the Tribunal
- [validator-chain](validator-chain.md) · the 12-check rule layer the Tribunal runs
- [judge](judge.md) · the LLM judge layer within the Tribunal
- [royal-jelly](../hive_terms/royal-jelly.md) · the apex tier the Tribunal assigns
- [honey](../hive_terms/honey.md) · the volume tier the Tribunal assigns
- [hive](../hive_terms/hive.md) · the parent entity that hosts the Tribunal

## Example

> **Engagement**: STNL acquisition opinion · industrial cold storage · Atlanta MSA.
>
> **PairCandidate**: SwarmCRE-9B-produced 4-page broker opinion.
>
> **Tribunal run**: TRIB-20260524T141022Z-7c4a
> - Scout · fetched · normalized
> - Router · long lane (high-stakes engagement)
> - Filter · all 12 checks PASS
> - Scale A (gemma3:12b GPU 1) · score 0.89 · reason "comps anchored · credit walk EDGAR-sourced"
> - Scale B (qwen2.5:32b GPU 0) · score 0.91 · reason "depth high · all 5 trajectory keywords · numerics tie"
> - Drift 0.02 · no Critic invoked
> - JellyScore 0.90 · tier ROYAL_JELLY
> - record_hash sha256:7c4a...
>
> **Outcome**: Deed DDEED-DOV-CRE-LINEAGE-ATL-000042-v1 issued · published · ENS-resolved · Hedera-anchored.

## DefendableOS Notes

- The Tribunal is the brand's quality discipline made structural · not vibes-checked
- The 6-role architecture is doctrine · do not add roles · do not collapse roles
- The 2-pass requirement is non-negotiable · no single-judge verdicts ship
- Katniss as the adversarial backstop is the architecture's IMMUNE SYSTEM · it gets invoked rarely but it protects against the long tail
- The Tribunal verdict record IS the audit trail · anyone with the record_hash can replay the chain

🐝 *Two judges. One drift threshold. A Critic when they disagree. Katniss when the deal smells. The Tribunal is the chain · the chain is the trust · the trust is the brand.*
