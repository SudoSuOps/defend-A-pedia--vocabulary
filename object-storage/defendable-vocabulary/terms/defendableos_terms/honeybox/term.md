# HoneyBox

## Street Definition

"Ship them a HoneyBox." That's the Sr Hack at standup when a regulated-industry customer signs. **HoneyBox** is the $249 Jetson Orin Nano edge appliance · 8GB RAM · 40 TOPS · physical hardware that sits on the customer's premises and holds the per-agent ledger locally. Raw data NEVER leaves the building. Compliance officer sleeps. Auditor verifies. The defense lives on-prem.

## CRE Operator Meaning

In CRE this is the **on-site property manager's office**. Class A asset can't run on remote management alone · the tenants need a physical desk, a physical face, a physical phone number. The office costs money but the office is what makes the building rentable to anchor tenants who require on-prem ops. HoneyBox is the on-site office for the AI defense layer. $249 of hardware is the price of admission to regulated industries that won't touch cloud-only competitors.

## DefendableOS Definition

HoneyBox is the edge-deployment appliance of DefendableOS. It's a productized Jetson Orin Nano (8GB · 40 TOPS) preloaded with DefendableRouter firmware, SwarmJelly-4B inference (quantized for the device), the local per-agent ledger storage, and the signed-metadata-only egress channel. It enables EDGE-mode DefendableRouter deployment for customers with data-residency constraints. Raw payloads stay local · only signed metadata pings leave the building. Acquisition price $249-499 · subscription $99/mo · 5-min credit-card swipe vs 9-month enterprise procurement cycle.

## Backend Representation

```json
{
  "honeybox.device_id": {"type": "string", "format": "HB-<utc-date>-<serial>"},
  "honeybox.hardware_class": {"type": "string", "const": "NVIDIA_JETSON_ORIN_NANO_8GB"},
  "honeybox.compute_tops": {"type": "integer", "const": 40},
  "honeybox.firmware_version": {"type": "string", "pattern": "^v[0-9]+\\.[0-9]+\\.[0-9]+$"},
  "honeybox.deployment_address": {"type": "string", "description": "physical site address"},
  "honeybox.customer_id": {"type": "string"},
  "honeybox.acquisition_price_usd": {"type": "integer", "enum": [249, 399, 499]},
  "honeybox.subscription_usd_mo": {"type": "integer", "default": 99},
  "honeybox.raw_data_egress_disabled": {"type": "boolean", "const": true},
  "honeybox.signed_metadata_egress_enabled": {"type": "boolean", "const": true},
  "honeybox.ens_compliance_inbox": {"type": "string", "format": "compliance.<customer>.defendable.eth"}
}
```

Schema files: `docs/schemas/honeybox_device.schema.json` · `docs/schemas/edge_deployment.schema.json`

## Client Explanation

HoneyBox is a small physical appliance · about the size of a paperback book · that sits on your premises. It runs DefendableOS locally. Your AI agents' raw data NEVER leaves your building · we only send signed metadata pings (a "you got mail" notification with the hash · not the content). $249-499 to buy · $99/month to keep current. Compliance teams in healthcare · finance · law · gov can sign off in days instead of months because the data residency story is bulletproof.

## Jr Broker Use

HoneyBox is the wedge product for regulated industries. When the customer's first question is "where does our data go", the answer is "nowhere · it stays on the HoneyBox on your desk." That answer closes the call. Jr Hack ships the device, sets up the ENS compliance inbox (`compliance.<customer>.defendable.eth`), and walks the customer through the 5-minute setup on a screen-share. Don't over-engineer the install · the box is designed to be plug-and-play.

## Sr Broker Use

The Sr Hack monitors the per-device fleet health · firmware version drift · subscription renewal rate · device-down events. A HoneyBox that goes offline is a customer's defense layer down · escalate within 1 hour. The Sr Hack also coordinates the per-customer ENS rollout · `<agent>.<operator>.defendable.eth` for each agent on the box · compliance inbox always at `compliance.<customer>.defendable.eth`.

## Tribunal Use

- **Rule layer**: HoneyBox MUST have raw_data_egress_disabled=true · any flag flip is a governance violation
- **Rule layer**: Signed metadata pings MUST be hash-only · embedding raw payload in the ping is a privacy breach
- **Rule layer**: Firmware MUST be on the approved version list
- **Judge layer**: Tribunal doesn't grade HoneyBox per-device · it grades the metadata pings the box emits
- **Classification impact**: HoneyBox-graded pairs carry the same classification as cloud-graded pairs · the topology doesn't affect the verdict

## Evidence Required

- Device serial + hardware class attestation
- Firmware version on the approved list
- Customer site address (for the on-prem ledger location)
- Compliance inbox ENS registration
- Raw-data-egress-disabled attestation (technical + contractual)
- Subscription billing record

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `raw_data_egress_enabled` | Flag flipped · raw payloads leaving the box | PROPOLIS · governance breach |
| `ping_contains_payload` | "You got mail" ping carries raw content instead of hash | PROPOLIS · privacy violation |
| `firmware_drift` | Box running unapproved firmware | JELLY · upgrade required |
| `device_offline` | Box unreachable > 1h · customer defense layer down | JELLY · operational alert |
| `ens_compliance_inbox_missing` | Customer doesn't have `compliance.<customer>.defendable.eth` registered | JELLY · provisioning gap |
| `subscription_lapsed` | Subscription expired · device falls behind on firmware/AdversarialPack | JELLY · billing escalation |

## Scoring Impact

- **assignment_success**: HIGH · HoneyBox IS the wedge for regulated industries
- **repair_lift**: INDIRECT · HoneyBox enables the refinery in EDGE mode
- **validator_confidence**: HIGH · on-prem topology IS a trust signal for regulated buyers
- **risk_temperature**: INVERSE · HoneyBox dramatically lowers data-residency risk
- **probability_of_close**: HIGH for regulated industries · MEDIUM for SaaS-native
- **evidence_strength**: HIGH · physical device with serial + ENS = strong evidence
- **cost_to_mint**: LOW · hardware is acquisition · ongoing cost is subscription

## Deed / Receipt Impact

- **Receipt fields touched**: `honeybox.device_id` · `firmware_version` · `customer_id` · `raw_data_egress_disabled`
- **DDEED class impact**: HoneyBox-graded pairs cite the device_id in the Proof of Origin · deeds resolvable per device
- **Books and records layer**: L1 PostgreSQL (device registry) → L3 NAS (local per-agent ledger ON DEVICE · not in cloud) → L4 Hedera HCS (metadata anchor) → L5 ENS (per-device pointer at `<device>.devices.defendable.eth`)
- **5 Proofs touched**: ORIGIN (device serial + firmware) · PROCESS (on-prem capture lineage) · TRUST (raw-data-egress-disabled attestation)

## Related Terms

- [defendableos](defendableos.md) · parent platform
- [defendablerouter](defendablerouter.md) · the firmware HoneyBox runs
- [defendablecloud-com](defendablecloud-com.md) · the cloud-mode alternative
- [clawcheck](clawcheck.md) · the intake that routes regulated customers to HoneyBox
- [swarmjelly](../repair_terms/swarmjelly.md) · the quantized model running on the device

## Example

> **Customer**: MRI imaging center · 12-radiologist practice · HIPAA-regulated · 4 AI agents (intake triage, report-draft, billing-code, follow-up)
>
> **Hardware shipped**: HoneyBox HB-20260520-7e3a · NVIDIA Jetson Orin Nano 8GB · 40 TOPS
>
> **Acquisition**: $399 (mid-tier · with extended warranty) · 5-min credit-card swipe by the practice manager · arrives 3-day FedEx
>
> **Setup**: practice plugs in · DefendableRouter firmware auto-configures · 4 agent ENS identities registered (`triage.mri-center-jupiter.defendable.eth` · etc.) · compliance inbox at `compliance.mri-center-jupiter.defendable.eth`
>
> **Subscription**: $99/mo · auto-renews · includes AdversarialPack updates · firmware updates · ENS hosting
>
> **Data flow**: agents call OpenAI · Router captures locally · Tribunal grading runs on the box at night · Morning Reconciliation Brief auto-emails to compliance inbox at 6am · raw PHI NEVER leaves the practice
>
> **HIPAA posture**: the box is a BAA-eligible asset · zero raw PHI in any cloud · compliance officer signed in 4 days · would have been 9 months for cloud-only solution

## DefendableOS Notes

- HoneyBox is the WEDGE BUYER unlock · regulated industries that are categorically closed to cloud-only competitors (healthcare · finance · gov · defense · legal)
- The hardware is acquisition channel · not profit · $249-499 covers the cost · the $99/mo subscription is the recurring economics
- 5-min credit-card swipe is the KILLER MOVE · it's tax-deductible · off-balance-sheet · founder-credit-card friendly · zero procurement overhead
- HoneyBox + DefendableRouter = Defendable Edge Stack · the on-prem twin of the cloud rail
- 5-year LTV per HoneyBox is $9K (SMB) to $62K (MRI center) · 86% gross margin

🐝 *On-prem defense. $249 of hardware. The wedge for regulated industries.*
