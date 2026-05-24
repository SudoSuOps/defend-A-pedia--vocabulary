# TEMP 0.05 Rule (the Temp Five-Cent Rule)

## Street Definition

"TEMP equals five cents." That's the locked production rule. **The TEMP 0.05 Rule** is the constitutional setting for every SwarmJelly inference call · every SwarmFixer refinery run · every cook script · every runtime config. 0.05. No exceptions. No tuning preference. No "let's try 0.1 for diversity." Read the env. Read the config. Read the request payload. If any of the three reads ≠ 0.05, ABORT.

## CRE Operator Meaning

In CRE the TEMP 0.05 Rule is the **rate-lock at signing**. The lender locks the rate at the commitment letter · not at closing · not "we'll lock when rates look good" · at signing. Why? Because the deal pencils against a specific rate · the entire underwriting depends on it · if the rate moves, the deal stops penciling. Locking is the discipline that makes the deal close. TEMP 0.05 is the rate lock for the refinery. Move it, the deal stops penciling.

## DefendableOS Definition

The TEMP 0.05 Rule is the locked operational doctrine for ALL SwarmJelly model inference. The temperature parameter passed to the SwarmJelly endpoint MUST be 0.05 for any inference call participating in a SwarmFixer Royal Jelly Record. Production evidence backs the rule: at TEMP=0.7, the Honey rate is 0.7% (catastrophic). At TEMP=0.05, the Honey rate is 93.9% (production-grade). The rule is enforced at three layers: env var, runtime config, request payload. The validator chain Check C02 rejects any inference receipt with TEMP ≠ 0.05.

## Backend Representation

```json
{
  "temp_five_cent_rule.locked_value": {"type": "float", "const": 0.05},
  "temp_five_cent_rule.enforcement_layers": {
    "type": "array",
    "const": ["env_var", "runtime_config", "request_payload"]
  },
  "temp_five_cent_rule.validator_check_id": {"type": "string", "const": "C02"},
  "temp_five_cent_rule.production_evidence": {
    "type": "object",
    "fields": {
      "temp_0_7_honey_rate": {"type": "float", "const": 0.007},
      "temp_0_3_honey_rate": {"type": "float", "const": 0.11},
      "temp_0_1_honey_rate": {"type": "float", "const": 0.71},
      "temp_0_05_honey_rate": {"type": "float", "const": 0.939},
      "temp_0_0_honey_rate": {"type": "float", "const": 0.92}
    }
  },
  "temp_five_cent_rule.exception_path": {"type": "boolean", "const": false},
  "temp_five_cent_rule.waiver_authority": {"type": "string", "const": "doctrine_pr_only"}
}
```

Schema files: `docs/schemas/model_config.schema.json` · `docs/schemas/validator_chain.schema.json` · `docs/schemas/repair_run.schema.json`

## Client Explanation

The TEMP 0.05 Rule is the locked setting on our refinery model. Temperature is a knob that controls how random a language model is · higher temperature, more creative, more wrong. Lower temperature, more boring, more correct. For refinery work, we want correct. We tested · at the default 0.7, we got it right 0.7% of the time. At 0.05, we get it right 93.9% of the time. So we lock it. Every receipt cites the temperature · you can verify · we can't fake it.

## Jr Broker Use

The Jr Hack triple-checks TEMP before every refinery batch:

1. `echo $SWARMJELLY_TEMP` → must show `0.05`
2. `cat /etc/swarmjelly/config.yaml | grep temperature` → must show `temperature: 0.05`
3. The actual request payload (curl with verbose logging) → must show `"temperature": 0.05`

If any of the three reads ≠ 0.05, ABORT the batch and escalate. Don't "just override and proceed." The whole batch will fail validator chain Check C02 and the receipts won't anchor.

## Sr Broker Use

The Sr Hack reviews the weekly Cook Flightsheet · every cook script that touches SwarmJelly must explicitly declare TEMP=0.05 in the documented config. The Sr Hack also reviews any waiver requests · waivers require a doctrine PR · NOT a config flip · NOT a Slack approval. A waiver hasn't been granted yet and isn't planned. The rule is locked.

## Tribunal Use

- **Rule layer C02**: Inference receipts MUST cite TEMP=0.05 · any other value triggers automatic verdict downgrade to PROPOLIS for the refinery output
- **Rule layer**: TEMP override at runtime without explicit doctrine waiver = governance violation · the operator who flipped the flag gets escalated
- **Judge layer**: Tribunal doesn't grade the TEMP itself · it relies on the rule layer to enforce
- **Classification impact**: A SwarmFixer run at TEMP ≠ 0.05 cannot produce a Royal Jelly Record · the whole 5-task output is discarded

## Evidence Required

- Env var snapshot (proves shell environment)
- Runtime config file (proves the daemon's config)
- Request payload trace (proves the actual API call)
- Receipt with TEMP field embedded
- Validator chain C02 pass result

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `temp_drift_to_default` | Operator forgot to set TEMP · falls back to model default (often 0.7) | PROPOLIS · batch discard |
| `silent_override` | Code path overrides TEMP without logging | PROPOLIS · governance violation |
| `partial_enforcement` | TEMP correct in env var but wrong in runtime config | PROPOLIS · enforcement gap |
| `waiver_without_pr` | Someone applied a TEMP waiver via Slack approval · no doctrine PR | PROPOLIS · governance violation |
| `temp_in_receipt_missing` | Receipt doesn't include the TEMP field at all | PROPOLIS · evidence gap |
| `temp_documented_wrong` | Cook script documented as TEMP=0.05 but actually runs at different value | PROPOLIS · documentation violation |

## Scoring Impact

- **assignment_success**: CRITICAL · TEMP wrong = whole assignment void
- **repair_lift**: DIRECT · TEMP 0.05 IS what produces the 93.9% Honey rate
- **validator_confidence**: GATING · validator chain blocks on C02 failure
- **risk_temperature**: HIGH · TEMP drift is one of the highest-risk operational failures
- **probability_of_close**: HIGH · the TEMP receipt is a competitive differentiator (defensible setting)
- **evidence_strength**: HIGH · receipted TEMP value is the strongest possible attestation
- **cost_to_mint**: NEUTRAL · the cost is the same · the QUALITY is the difference

## Deed / Receipt Impact

- **Receipt fields touched**: every SwarmJelly receipt includes `model_config.temperature: 0.05`
- **DDEED class impact**: DDEED-DOV-REPAIR inherits TEMP from the receipt · auditor can verify TEMP across deed history
- **Books and records layer**: L1 PostgreSQL (model config registry) → L4 Hedera HCS (TEMP anchored per receipt) → L5 ENS (model config doctrine page)
- **5 Proofs touched**: ORIGIN (the model config in effect at inference time) · QUALITY (the TEMP IS the quality lever) · TRUST (defensible runtime setting · auditable end-to-end)

## Related Terms

- [swarmjelly](../repair_terms/swarmjelly.md) · the model the rule applies to
- [swarmfixer](../repair_terms/swarmfixer.md) · the refinery that enforces the rule
- [defendablejelly](../repair_terms/defendablejelly.md) · the product whose quality depends on the rule
- [repair-lift](../repair_terms/repair-lift.md) · the dial the TEMP rule protects

## Example

> **Production evidence (cook log from cook-20260510)**:
> - First cook with default TEMP=0.7: 1,000 refinery runs · 7 produced Honey-grade RJ Records · 880 produced Propolis · catastrophic
> - Re-cook with TEMP=0.3: 1,000 runs · 110 Honey · 640 Propolis · still unusable
> - Re-cook with TEMP=0.1: 1,000 runs · 710 Honey · 140 Propolis · good but inconsistent
> - **Re-cook with TEMP=0.05: 1,000 runs · 939 Honey · 30 Propolis · LOCKED · production**
> - Re-cook with TEMP=0.0: 1,000 runs · 920 Honey · 30 Propolis · loses tie-breaking diversity on COMPARE task
>
> **Production receipt sample** (`ag-fix-20260524T071200Z-9a3c`):
> ```json
> {"model_config": {"temperature": 0.05, "top_p": 0.95, "model_tag": "swarmjelly-4b:v1.2"}}
> ```
>
> **Validator chain C02 pass**: confirmed TEMP=0.05 in env, runtime config, AND request payload · receipt anchored

## DefendableOS Notes

- The TEMP 0.05 Rule is THE single most important locked operational setting in the entire DefendableOS stack
- Discovered through canary-then-cook discipline · prior cooks attempted TEMP=0.7 because that's the model default · the 0.7% Honey rate was the wake-up
- A waiver path EXISTS but has never been used · waiver requires a doctrine PR (not a Slack approval) · the bar is intentionally high
- The rule appears in every SwarmFixer doctrine doc, every refinery playbook, every cook flightsheet, every runtime config · redundant enforcement is intentional
- "Temp Five-Cent Rule" is the operator nickname · five cents = 0.05 in the broker's mental shorthand

🐝 *Five cents. Locked. Read three places. ABORT if drift. The rule that makes the refinery a refinery.*
