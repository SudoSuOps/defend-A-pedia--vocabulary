# DefendableCloud.com

## Street Definition

"Run the cloud rail." That's the Sr Hack at standup when a SaaS-native customer signs. **DefendableCloud.com** is the hosted-inference rail · 128 RTX 6000 Blackwell GPUs in the operator-owned data center · 13+ open-weights models on tap · privacy-native · contractual no-logging · 90%+ inference margin. It's the SIXTH domain in the brand stack and the sister rail to DefendableRouter.

## CRE Operator Meaning

In CRE this is the **owned trophy asset**. Class A datacenter. Owned, not leased. Operator-controlled HVAC, power, security. Sub-leasable to anchor tenants with custom buildouts. The owner has the moat because they hold the dirt · they don't pay rent · they collect rent. DefendableCloud is the dirt. 128 RTX 6000s sitting in racks the operator owns, in a facility the operator controls. The margin profile reflects ownership · not tenancy.

## DefendableOS Definition

DefendableCloud.com is the hosted-inference rail of DefendableOS. It runs the open-weights model fleet (Qwen32B · Llama70B · DeepSeek · Mixtral · SwarmJelly-4B · 8+ more) on 128 RTX 6000 Blackwell GPUs in the operator-owned datacenter. It serves as the CLOUD-mode and HYBRID-mode endpoint for DefendableRouter customers. Contractual no-logging on raw payloads · only graded verdicts and receipts persist. KPMG-style attestable. 90%+ gross margin on inference (owned compute · no hyperscaler markup).

## Backend Representation

```json
{
  "defendablecloud.domain": {"type": "string", "const": "defendablecloud.com"},
  "defendablecloud.gpu_fleet_size": {"type": "integer", "const": 128},
  "defendablecloud.gpu_model": {"type": "string", "const": "NVIDIA RTX PRO 6000 Blackwell Workstation Edition"},
  "defendablecloud.gpu_vram_per": {"type": "string", "const": "95 GB"},
  "defendablecloud.deployment_topology": {"type": "string", "const": "operator_owned_dc"},
  "defendablecloud.models_served": {
    "type": "array",
    "default": ["qwen32b", "llama70b", "deepseek-coder", "mixtral-8x22b", "swarmjelly-4b"]
  },
  "defendablecloud.no_logging_clause": {"type": "boolean", "const": true},
  "defendablecloud.gross_margin_target": {"type": "float", "min": 0.90},
  "defendablecloud.audit_attestation": {"type": "string", "const": "KPMG_style"}
}
```

Schema files: `docs/schemas/inference_provider.schema.json` · `docs/schemas/deployment_topology.schema.json`

## Client Explanation

DefendableCloud is our hosted-inference service. 128 high-end GPUs we own in a datacenter we control. We run 13+ open-weights models · Qwen, Llama, DeepSeek, Mixtral, our in-house SwarmJelly. Your raw prompts and responses never get logged · only the graded verdicts and the receipts. Contractually. Auditable to KPMG standards. It's the choice for customers who want the privacy of self-host without the operational lift of standing up GPU servers themselves.

## Jr Broker Use

When the customer is CLOUD-mode or HYBRID-mode on DefendableRouter, the inference endpoint is DefendableCloud. Verify the customer's payload class against the no-logging clause. Even though we don't log raw payloads, some compliance regimes require the data to never CROSS a border · in that case route to EDGE mode (HoneyBox) instead.

## Sr Broker Use

The Sr Hack monitors GPU utilization across the 128-card fleet · target steady-state 60-75% · spikes to 90%+ should auto-trigger model-routing to spread load across the fleet. The Sr Hack also reviews the no-logging clause compliance quarterly · pen-tests the storage layer to verify no raw payloads persist · this is what backs the KPMG attestation.

## Tribunal Use

- **Rule layer**: All Tribunal grading runs that use DefendableCloud MUST cite the model tag and the GPU pool ID · `model_provider: defendablecloud` is the discriminator
- **Rule layer**: No-logging clause violation (raw payload found in storage) = PROPOLIS · platform-level governance failure
- **Judge layer**: Tribunal verdicts on DefendableCloud-graded pairs are first-class · same status as customer-self-hosted inference
- **Classification impact**: DefendableCloud inference is treated identically to other providers for grading purposes · the cloud just provides cheaper, faster compute

## Evidence Required

- Datacenter ownership/lease documentation (operator-owned, not hyperscaler tenant)
- GPU fleet inventory (128 cards · serial numbers in PRIVATE_EVIDENCE vault)
- Model registry (which open-weights models are served · checksums)
- No-logging architecture proof (storage audit logs, retention policies)
- KPMG-style attestation report (annual)
- Gross margin attestation (cost per inference vs revenue per inference)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `no_logging_breach` | Raw payload found persisted in storage · clause violation | PROPOLIS · governance failure |
| `gpu_oversubscription` | Steady-state utilization > 90% · customer latency degraded | JELLY · capacity escalation |
| `model_drift` | Served model checksum doesn't match registered version | PROPOLIS · supply chain |
| `cross_border_violation` | Customer with residency constraint routed to wrong region | PROPOLIS · governance |
| `margin_drift` | Gross margin falls below 90% target sustained · pricing or cost problem | JELLY · finance review |
| `attestation_lapse` | KPMG-style attestation expired without renewal | JELLY · audit escalation |

## Scoring Impact

- **assignment_success**: HIGH · cloud is the default delivery for SaaS-native customers
- **repair_lift**: INDIRECT · cloud hosts SwarmJelly · refinery quality depends on cloud uptime
- **validator_confidence**: HIGH · KPMG attestation IS a trust signal
- **risk_temperature**: INVERSE · owned-DC reduces hyperscaler-dependency risk
- **probability_of_close**: HIGH · privacy-native + KPMG attestation = enterprise-ready
- **evidence_strength**: HIGH · every inference receipt cites the GPU pool ID
- **cost_to_mint**: LOW · owned compute = lowest cost-per-inference in the stack

## Deed / Receipt Impact

- **Receipt fields touched**: `model_provider: defendablecloud` · `gpu_pool_id` · `model_tag` · `region` · `attestation_active`
- **DDEED class impact**: deeds issued for cloud-graded pairs cite DefendableCloud as the inference origin
- **Books and records layer**: L1 PostgreSQL (inference log · metadata only) → L4 Hedera HCS (per-batch anchor) → L5 ENS (`defendablecloud.eth` for fleet attestation)
- **5 Proofs touched**: ORIGIN (which GPU, which model, which region) · ECONOMICS (cost per inference is the CFO line) · TRUST (KPMG attestation + no-logging clause)

## Related Terms

- [defendableos](defendableos.md) · parent platform
- [defendablerouter](defendablerouter.md) · the capture rail that streams to DefendableCloud
- [honeybox](honeybox.md) · the edge-mode alternative
- [swarmjelly](../repair_terms/swarmjelly.md) · one of the models served on the cloud fleet
- [defendablejelly](../repair_terms/defendablejelly.md) · the product that uses cloud inference

## Example

> **Customer**: ACMECorp · SaaS-native · 14-agent fleet · no data-residency constraint
>
> **Deployment**: CLOUD mode · all inference routes to DefendableCloud
>
> **Fleet snapshot (Q2 2026)**: 128 RTX 6000 Blackwell cards · 12 PCIe pools · 4 NVLink pools · 60-72% steady-state utilization · ~140K inferences/day for ACMECorp
>
> **No-logging proof**: Q2 KPMG-style audit · zero raw payloads found in persisted storage · only verdicts and receipts retained
>
> **Margin**: cost/inference ~$0.0008 · revenue/inference ~$0.012 · gross margin 93%
>
> **Customer benefit**: 5-min provisioning vs 9-month GPU procurement · privacy-native (no logging) · receipted (anchored to chain)

## DefendableOS Notes

- DefendableCloud is the SIXTH domain in the brand quintet · brand stack now goes defendableos · defendablerouter · defendablecloud · defendablehack · opendefendable · defendthehive
- The 90%+ gross margin profile is what makes the SaaS-native expansion economic · we don't pay hyperscaler tax · the moat is the dirt
- The "no logging" clause is contractual + audited + technical · three layers · it's not a promise it's a posture
- DefendableCloud and HoneyBox are SIBLING rails · same doctrine (write-only Router · sub-5ms · receipted) · different topology · customer picks based on data class

🐝 *Owned dirt. Privacy-native. 90% margin. The sister rail of the cracked router.*
