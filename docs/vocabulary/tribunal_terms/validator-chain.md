# Validator Chain

> *"Twelve checks. Seven critical. Five advisory. Run them in order · log every result · do NOT skip. The chain is title insurance for AI output."*
> — Founder · the day C01-C12 were locked

## Street Definition

"What's the chain look like?" The validator chain is the C01-C12 sequence · the 12-check rule layer the Tribunal Filter runs on every pair BEFORE the LLM judges weigh in. Seven critical (C01-C07) can stop a deed cold. Five advisory (C08-C12) can downgrade confidence but cannot block. The chain runs in deterministic order · every result is logged · every decision is auditable from the record_hash.

In CRE language · the validator chain is the full title-insurance underwriting checklist · the survey · the chain-of-title walk · the lien search · the encumbrance disclosure · the entitlement transfer · the holdout-buyer protection · plus the SOC2-grade operator discipline (consent · redaction · audit log · hash · secret-scan). Twelve items the closing agent checks before the title insurance writes.

## CRE Operator Meaning

In CRE · the validator chain maps to the full title-insurance checklist · the items that have to be cleared before the closing agent writes the title policy. Survey current? Chain of title clean? Liens released? Easements disclosed? Tax-cert clean? Holdout deed identified? Twelve items more or less · seven of them stop-the-deal · five of them disclosure items that get into the title insurance addendum without blocking the close.

Same here. The validator chain is what the Tribunal runs before any judge can issue a verdict. The chain is the structural protection that keeps the Hive's deeds defendable in audit.

## DefendableOS Definition

The validator chain is the ordered sequence of 12 named checks (C01-C12) executed by Auditor-class Bee validators inside the Tribunal Filter role:

| # | Check | Type | Trigger |
|---|---|---|---|
| **C01** | pair record present | CRITICAL | PairCandidate JSON exists · parses |
| **C02** | source artifact referenced | CRITICAL | Every claim cites at least one source |
| **C03** | source retrievable | CRITICAL | At least one source resolves (HTTP 200) within 30-day cache |
| **C04** | tribunal label assigned | CRITICAL | tribunal_label or judges_pending flag present |
| **C05** | no hard-fail flagged | CRITICAL | No hallucination_event · schema_break · tool_misuse |
| **C06** | PROPOLIS not promoted | CRITICAL | Propolis-flagged pairs cannot reach deed pipeline |
| **C07** | holdout contamination guard | CRITICAL | Pair NOT in holdout_manifest.jsonl (5 holdouts as of 2026-05-24) |
| **C08** | operator consent | ADVISORY | Engagement consent flag captured |
| **C09** | redaction status | ADVISORY | PII / secrets / PAN scan result logged |
| **C10** | transition audit log | ADVISORY | All Tribunal state changes logged |
| **C11** | SHA-256 recorded | ADVISORY | Canonical JSON record_hash computed |
| **C12** | no secrets in pair | ADVISORY · also SAFETY GATE | Regex + entropy scan for AWS keys · tokens · PANs |

Full spec in [`docs/doctrine/13_validator_chain_doctrine.md`](../../doctrine/13_validator_chain_doctrine.md).

## Backend Representation

```json
{
  "validator_chain.results": {
    "type": "array",
    "items": {
      "type": "object",
      "required": ["check_id", "result", "reason", "is_critical"],
      "properties": {
        "check_id": {
          "type": "string",
          "enum": ["C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12"]
        },
        "result": {
          "type": "string",
          "enum": ["PASS", "FAIL", "ADVISORY_FAIL", "ERROR"]
        },
        "is_critical": { "type": "boolean" },
        "reason": { "type": "string" },
        "confidence_weight": { "type": "float" }
      }
    }
  },
  "validator_chain.all_critical_pass": { "type": "boolean" },
  "validator_chain.advisory_count_failed": { "type": "integer" },
  "validator_chain.total_latency_ms": { "type": "integer" }
}
```

Schema files: `docs/schemas/validator_chain.schema.json` · `docs/schemas/validator_result.schema.json`

## Client Explanation

"The validator chain" is our 12-check rule layer · the structural checklist our Tribunal runs on every AI output before the judges weigh in. Seven of the checks are critical · any fail stops the deed cold. Five are advisory · they downgrade confidence but don't block. Every deed you receive carries the full chain results in its record. You can audit any deed by running its record_hash against the chain results · the chain is the chain · the audit trail is verifiable.

## Jr Broker Use

The jr broker reads the chain results but does not interpret independently:

1. Every PairCandidate produces a validator chain result block · visible in the dashboard within seconds of submission
2. All 7 critical PASS → pair proceeds to judges (the normal path)
3. ANY critical FAIL → pair short-circuits to Propolis or Jelly (depending on which check · per the doctrine)
4. Any advisory FAIL → annotated but pair proceeds · escalate to sr broker for sign-off
5. NEVER modify the chain · NEVER skip a check · NEVER attempt to override a critical-fail · the chain is doctrine

**Rule of thumb**: clean chain = green light · any critical fail = stop · advisory fails = ask the sr broker.

## Sr Broker Use

The sr broker monitors the chain as the SYSTEM HEALTH GAUGE:

- Daily Morning Brief shows per-check fail rates · any critical check > 2% fail rate triggers degraded mode
- The C07 holdout-contamination check is the highest-severity event · pages immediately · holds the entire cook batch pending audit
- Advisory check patterns reveal upstream discipline issues · C08 (consent) creep means engagement-onboarding is leaking · C09 (redaction) creep means PII-scan service is degraded · C10 (audit log) creep means transition logging is dropping events
- Manual override of advisory checks is permitted with logged reason · manual override of critical checks is structurally rejected (the chain rejects the override at C06)
- The 12-check budget per pair is ~80ms · the full chain budget is ~1000ms · sustained chain latency > 2000ms means a validator service is degraded

## Tribunal Use

```yaml
tribunal_use:
  classification_impact: []   # the chain itself does not have a tier · it DETERMINES tiers
  rule_layer_checks:
    - validator_chain.results MUST contain all 12 check outcomes
    - validator_chain.all_critical_pass MUST be true for any tier above Propolis
    - validator_chain.advisory_count_failed feeds the confidence_weight adjustment
  judge_layer_prompt_hint: "the chain has run · respect its decisions · you cannot promote past a critical-fail"
  can_be_critical_failure: false   # the chain doesn't fail · it DETECTS failures
```

## Evidence Required

To consider a validator chain pass valid:

- All 12 check outcomes recorded
- The is_critical flag correct for each check (C01-C07 critical · C08-C12 advisory · C12 special safety-gate status)
- A reason string for any non-PASS result
- A total_latency_ms reading
- A canonical-JSON record_hash that includes the chain results

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **chain_short_run** | Chain results contain fewer than 12 entries (one or more checks did not execute) | Pair held · chain re-run · if recurring · validator service audited |
| **chain_out_of_order** | Checks executed in wrong order (e.g., C05 before C03) | Integrity event · check the Tribunal Filter implementation · re-run |
| **chain_silent_skip** | Check returned PASS but did not actually execute the underlying logic | Validator service integrity failure · all recent passes audited |
| **chain_latency_explosion** | Total chain latency > 2000ms sustained | Validator service health audited · likely a slow source-fetch or PII-scan dependency |
| **chain_override_attempt** | Operator attempted to manually override a critical-fail | Structurally rejected at C06 · operator coached · attempt logged · escalated |

## Scoring Impact

- **assignment_success**: GATE · success requires all 7 critical PASS
- **repair_lift**: GATE · repaired pairs go through the chain again · the lift is measured post-chain
- **validator_confidence**: PRIMARY DRIVER · the confidence_weight aggregates from per-check confidences
- **risk_temperature**: INVERSE · clean chain lowers risk · critical fails spike risk
- **probability_of_close**: GATE · close prob assumes chain clearance · chain failure history predicts re-fail
- **evidence_strength**: PARTIALLY GATED · C02 + C03 directly validate evidence
- **cost_to_mint**: INCLUDED · chain compute is in chain_overhead line of cost-to-mint

## Deed / Receipt Impact

- **Receipt fields touched**: `validator_chain.results` (full 12-item array) · `validator_chain.all_critical_pass` · `validator_chain.advisory_count_failed` · `validator_chain.total_latency_ms`
- **DDEED class impact**: NO DDEED issues without a clean critical chain (all C01-C07 PASS)
- **Books and records layer**: L1 PG (chain results stored hot) · L2 Merkle (chain results hashed into batch root) · L3 NAS (chain transition log archived) · L4 Hedera HCS (chain hash included in batch root)
- **5 Proofs touched**: QUALITY (chain IS the quality rule layer) · PROCESS (chain IS the process) · TRUST (chain results in the deed record are what's verifiable)

## Related Terms

- [validator](validator.md) · the auditor-bee role that executes the chain
- [tribunal](tribunal.md) · the parent adjudicator that runs the chain
- [judge](judge.md) · the LLM layer that runs AFTER the chain clears
- [confidence-weight](confidence-weight.md) · the dial the chain's per-check confidence aggregates into
- [hallucination-event](hallucination-event.md) · the named class of failure C05 detects
- [propolis](../hive_terms/propolis.md) · the tier the chain forces critical-fail pairs into

## Example

> **Engagement**: STNL opinion · cold storage · Atlanta MSA.
>
> **Validator chain results (in execution order)**:
> - C01 PASS (43ms · confidence 1.0)
> - C02 PASS (61ms · 5 sources cited · confidence 1.0)
> - C03 PASS (310ms · 5/5 sources retrieved · confidence 1.0)
> - C04 PASS (5ms · pre-judge null acceptable · confidence 1.0)
> - C05 PASS (28ms · no hard-fail flags · confidence 1.0)
> - C06 PASS (2ms · trivially clears for non-Propolis · confidence 1.0)
> - C07 PASS (88ms · cross-checked against 5-holdout manifest · confidence 1.0)
> - C08 PASS (12ms · consent flag captured · confidence 1.0)
> - C09 PASS (147ms · PII scan clean · confidence 0.95)
> - C10 PASS (8ms · all transitions logged · confidence 1.0)
> - C11 PASS (3ms · hash computed sha256:... · confidence 1.0)
> - C12 PASS (52ms · zero secret patterns matched · confidence 1.0)
> - Total latency 759ms
> - all_critical_pass = true · advisory_count_failed = 0
>
> **Outcome**: Chain clean · pair proceeds to Scale A + Scale B judges · verdict ROYAL_JELLY · deed issued · chain results included in DDEED record · audit trail verifiable.

## DefendableOS Notes

- The 12 checks are doctrine · do not add · do not remove · do not reorder
- The critical/advisory split is doctrine · C01-C07 critical · C08-C12 advisory (with C12 special safety-gate status)
- Operator override of critical checks is structurally rejected · this is the founder-locked discipline
- The chain budget is ~1000ms per pair · sustained latency above 2000ms = degraded mode
- The chain is what makes the Tribunal MORE than vibes · removing the chain reduces the Tribunal to LLM opinion · which is what we're replacing

🐝 *Twelve checks. Seven critical. Five advisory. Run them in order. Log every result. The chain is the chain · the chain is title insurance for AI output.*
