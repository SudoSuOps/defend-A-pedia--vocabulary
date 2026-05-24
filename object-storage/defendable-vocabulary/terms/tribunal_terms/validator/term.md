# Validator

> *"The validator is the auditor bee. The one whose only job is to cross-check the worker · run the 12 checks · log the result · and have the receipts to prove what they saw. The brokerage that doesn't have a validator is the brokerage that loses the audit."*
> — Founder · day the auditor role was named

## Street Definition

"Validator's looking at it." The validator is the Auditor-class Bee whose lane is the 12-check validator chain · the rule-layer that runs on every pair BEFORE the LLM judges weigh in. A validator does not produce output · it cross-checks the output produced by Worker Bees. It runs C01-C12 · annotates the pair with critical and advisory results · and emits the verdict-record skeleton the judges populate.

In CRE language · the validator maps to the title-insurance underwriter and the closing-agent reviewer · the role whose only job is to confirm the chain is clean before the deed transfers. The validator does not produce the deed · the validator protects the deed · the validator's signature is what makes the closing defendable.

## CRE Operator Meaning

In CRE · the validator is the auditor inside the brokerage · the role that checks the appraiser's math · the title chain · the survey · the lender's instructions · the closing-statement reconciliation. The validator does not sell · does not list · does not negotiate · the validator audits. A brokerage without a strong validator function is a brokerage that produces deals it can't defend at audit.

Inside DefendableOS · the validator carries that exact discipline. A validator never produces customer-facing output · the validator's only output is the verdict-record annotation that gets attached to the worker's output. The validator is the structural integrity layer of the chain.

## DefendableOS Definition

A validator is an Auditor-class Bee instance that executes the 12-check validator chain (C01-C12 · see [`13_validator_chain_doctrine.md`](../../doctrine/13_validator_chain_doctrine.md)) on a PairCandidate before the judge layer runs. Validators come in two operational modes:

### Critical-check validator (C01-C07)
- Runs the 7 critical checks · ANY fail short-circuits the pair to Propolis (or Jelly in the C03 cached-source case)
- Typical model: deterministic Python validators (no LLM required for most) · with optional model-backed checks for content-sensitive verifications

### Advisory-check validator (C08-C12)
- Runs the 5 advisory checks · annotates the pair with confidence penalties but does not block
- Typical model: SwarmJudge-9B-CRE for advisory content-validity checks · deterministic Python for hash / log / secret-scan checks

Validators report their results to the Tribunal Filter role. Filter aggregates · enforces priorities (critical before advisory) · and emits the rule-layer-result block of the verdict record.

## Backend Representation

```json
{
  "validator.validator_id": {
    "type": "string",
    "pattern": "^BEE-AUDITOR-VAL-[a-z0-9]+$"
  },
  "validator.check_id": {
    "type": "enum",
    "values": ["C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12"]
  },
  "validator.is_critical": { "type": "boolean" },
  "validator.result": {
    "type": "enum",
    "values": ["PASS", "FAIL", "ADVISORY_FAIL", "ERROR"]
  },
  "validator.reason": { "type": "string" },
  "validator.confidence_weight": { "type": "float", "range": [0.0, 1.0] },
  "validator.run_at": { "type": "timestamp" }
}
```

Schema files: `docs/schemas/validator_chain.schema.json` · `docs/schemas/validator_result.schema.json`

## Client Explanation

A "validator" is one of our auditor agents · its only job is to run twelve structural checks on every AI output before the judges weigh in. Validators don't produce output · they protect the output. Twelve checks · seven critical (any fail stops the deed) · five advisory (annotates but doesn't block). The validator's results are part of the verdict record you receive with every deed.

## Jr Broker Use

The jr broker treats validator output as the GO / NO-GO SIGNAL:

1. Every PairCandidate gets a validator pass before the judges · the validator chain results are visible in the dashboard before the verdict
2. If you see C01-C07 critical-fail · the pair is going Propolis · do NOT attempt to push it through
3. If you see C08-C12 advisory-fail · the pair MAY still ship · annotate the operator log with why · escalate to sr broker if uncertain
4. Validator output is FAST (sub-100ms per check on most) · if you see a validator taking > 5 sec · the validator service is degraded · escalate
5. Never bypass a validator check · the chain is the chain · operator override of critical-fail is structurally rejected

**Rule of thumb**: the validator catches the structural problems the judge would miss · trust the chain · the chain is doctrine.

## Sr Broker Use

The sr broker watches validator output as the EARLIEST-WARNING signal:

- Validator critical-fail rates are the upstream-broken signal · any single critical check failing > 2% of volume for 24h = degraded mode · investigate cook OR data source
- Validator advisory-fail patterns reveal operator discipline · sustained C08 (consent missing) > 5% means the engagement-onboarding process is leaking consent capture
- Validator latency is the rig-health signal · slow validators mean a busy rig OR a starving network · investigate
- C07 (holdout contamination) validator firing is the HIGHEST severity event in the Tribunal · page immediately · do not wait for the next Morning Brief

## Tribunal Use

```yaml
tribunal_use:
  classification_impact: []   # validators don't get tiers · their checks DETERMINE tiers
  rule_layer_checks:
    - validator.validator_id MUST be populated
    - validator.result MUST be one of [PASS, FAIL, ADVISORY_FAIL, ERROR]
    - if validator.is_critical AND result != PASS · pair goes to PROPOLIS (or JELLY in C03 cache case)
    - if validator.result == ERROR · pair is held · validator service health audited · re-run
  judge_layer_prompt_hint: "validators run BEFORE you · respect their critical-fail decisions · you cannot promote past them"
  can_be_critical_failure: false   # validators don't fail · they DETECT failures
```

## Evidence Required

To consider a validator pass valid:

- A run_at timestamp
- A result enum value
- A reason string (mandatory on FAIL and ADVISORY_FAIL · optional on PASS but recommended)
- A confidence_weight (0.0-1.0 · typically 1.0 for deterministic validators · variable for model-backed)
- The validator_id (links back to the auditor-bee lineage)

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **validator_silent_pass** | Validator returned PASS but the underlying check did not actually run | Validator service integrity event · service restarted · all recent passes audited |
| **validator_timeout** | Validator did not respond within latency budget · pair stuck | Validator service health audited · pair re-routed · if recurring · rig audited |
| **validator_disagreement** | Two parallel validator instances on the same check return different results (PASS vs FAIL) | Service determinism failure · escalate · the FAIL is treated as authoritative · investigate the PASS source |
| **validator_advisory_creep** | Advisory checks start failing at increasing rates without root-cause | Sr broker investigates upstream data quality · curator settings · operator-onboarding discipline |
| **validator_bypass_attempt** | Operator attempts to manually override a critical-fail validator result | Operator-discipline event · attempt is structurally rejected · logged · escalated |

## Scoring Impact

- **assignment_success**: GATE · validators are the structural gate the assignment must clear
- **repair_lift**: GATE · repaired pairs go through the validator chain again · the lift is measured post-validator-clearance
- **validator_confidence**: SELF · the validator's confidence_weight aggregates into the overall validator_confidence dial
- **risk_temperature**: INVERSE · clean validator runs lower risk · critical-fail validators spike risk
- **probability_of_close**: GATE · close prob assumes the validator chain will clear · validator history is a predictor
- **evidence_strength**: VALIDATOR-PRODUCED · evidence strength is partially validated by the validator chain (C02 source-referenced · C03 source-retrievable)
- **cost_to_mint**: INCLUDED · validator compute is a line item in cost-to-mint

## Deed / Receipt Impact

- **Receipt fields touched**: `validator_chain_results` (array of 12 check outcomes) · `validator_advisory_annotations` (list of advisory annotations) · `validator_lineage` (which validator-bees ran)
- **DDEED class impact**: NO DDEED issues without a clean validator chain (all 7 critical PASS · advisory annotated but not blocking)
- **Books and records layer**: L1 PG (validator results stored hot) · L2 Merkle (validator results hashed into batch root) · L3 NAS (validator transition log archived)
- **5 Proofs touched**: QUALITY (validators ARE the quality rule layer) · PROCESS (validator chain IS the process)

## Related Terms

- [validator-chain](validator-chain.md) · the 12-check chain the validator executes
- [tribunal](tribunal.md) · the parent system the validator runs within
- [judge](judge.md) · the LLM layer that runs AFTER the validator
- [bee](../hive_terms/bee.md) · the Auditor-class Bee that IS the validator instance
- [confidence-weight](confidence-weight.md) · the dial the validator's per-check confidence aggregates into

## Example

> **Engagement**: STNL opinion · industrial cold storage.
>
> **PairCandidate**: SwarmCRE-9B-produced opinion · waiting for Tribunal.
>
> **Validator passes (all 12 checks · logged in order)**:
> - C01 pair record present · validator BEE-AUDITOR-VAL-7a01 · PASS (43ms · confidence 1.0)
> - C02 source artifact referenced · BEE-AUDITOR-VAL-7a02 · PASS (61ms · 5 sources cited · confidence 1.0)
> - C03 source retrievable · BEE-AUDITOR-VAL-7a03 · PASS (310ms · 5/5 sources retrieved · confidence 1.0)
> - C04 tribunal label assigned · BEE-AUDITOR-VAL-7a04 · PASS (5ms · pre-judge null is acceptable · confidence 1.0)
> - C05 no hard-fail flagged · BEE-AUDITOR-VAL-7a05 · PASS (28ms · no hallucination · no schema break · no tool misuse · confidence 1.0)
> - C06 PROPOLIS not promoted · BEE-AUDITOR-VAL-7a06 · PASS (trivially clears · confidence 1.0)
> - C07 holdout contamination guard · BEE-AUDITOR-VAL-7a07 · PASS (88ms · cross-referenced against 5-holdout manifest · confidence 1.0)
> - C08 operator consent · BEE-AUDITOR-VAL-7a08 · PASS (12ms · consent flag captured at engagement open · confidence 1.0)
> - C09 redaction status · BEE-AUDITOR-VAL-7a09 · PASS (147ms · PII scan clean · confidence 0.95)
> - C10 transition audit log · BEE-AUDITOR-VAL-7a10 · PASS (8ms · all transitions logged · confidence 1.0)
> - C11 SHA-256 recorded · BEE-AUDITOR-VAL-7a11 · PASS (3ms · hash computed · confidence 1.0)
> - C12 no secrets in pair · BEE-AUDITOR-VAL-7a12 · PASS (52ms · no AWS keys · no API tokens · no PANs · confidence 1.0)
>
> **Outcome**: Validator chain clean · pair proceeds to judges · validator total latency 766ms · within budget · annotations attached to verdict record.

## DefendableOS Notes

- Validators are deterministic-first · model-backed only when the check is content-sensitive · this keeps the chain fast and auditable
- Validators are auditor-class Bees · same lifecycle (FETCH-COOK-GATE-SCORE-STAMP-ANCHOR-EMIT) as Workers
- The validator's confidence_weight is a dial that can be tuned per-check based on production performance · but the binary PASS/FAIL decision is doctrine
- Operator override of validator critical-fail is structurally rejected · this is the founder-locked discipline
- The validator chain is what makes the Tribunal more than vibes · without the validator layer the judges would be unconstrained

🐝 *Validator is the auditor bee. Twelve checks. Seven critical. Five advisory. The chain is the chain. The judge cannot promote past it.*
