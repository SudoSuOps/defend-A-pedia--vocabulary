# Sample Deed Receipt · Fully Rendered DDEED with 5 Proofs

> *A canonical example of a Defendable Agent Deed in its complete · publication-ready form. Carries all 5 Proofs · ready for Hedera anchoring · ready for ENS resolution. Use this shape for any new deed class.*

---

## Deed identifier

**`DDEED-DOV-LOGISTICS-ACME-REFUND-000412-v1`**

| Field | Value |
|---|---|
| Org slug | `DOV` (Donovan · founder namespace) |
| Vertical | `LOGISTICS` |
| Customer slug | `ACME` |
| Class | `REFUND` (refund-decision agent task class) |
| Sequence | `000412` (412th deed in this assignment) |
| Version | `v1` (initial issuance · no superseding deed yet) |

**ENS resolution**: `ddeed-dov-logistics-acme-refund-000412-v1.acme.defendable.eth`

---

## Status

- **Tribunal verdict**: `HONEY` (composite 0.87 · promoted from PENDING after 2-pass review)
- **Books-and-records status**: `PUBLISHED`
- **Hedera anchor status**: `CONFIRMED`
- **Issued at**: `2026-06-14T03:14:22Z`

---

## Parent receipt

**`DCLAW-7f3a82e1-2026-06-13T19:47:08Z`**

The originating receipt was written by the Router at 2026-06-13T19:47:08Z when the refund-decision agent processed customer ticket #ACME-RFD-2891441. The receipt sat in PENDING for ~7.5 hours before the 2am nightly Tribunal cron graded it and promoted it.

---

## The 5 Proofs

### Proof of Origin · *Where did this work come from?*

```json
{
  "model_name": "SwarmAtlas-CRE-9B-v1.4",
  "model_fingerprint": "sha256:9f7e3c8a1b5d4e2f6a8c9b3d1e7f5a2c8b6d4e1f9c7a3b5d8e2f4a6c1b9d3e7f",
  "model_provenance": "Qwen2.5-7B-base · fine-tuned on SwarmCurator CRE corpus v3.2 · cooked on swarmrails GPU 1 · 2026-04-18 · documented in DDEED-DOV-COOK-ATLAS-CRE-9B-v1.4-v1",
  "serving_node": "swarmrails.swarmandbee.ai",
  "serving_node_class": "RTX_PRO_6000_BLACKWELL_OWNED_DC",
  "routing_strategy": "primary_v3_refund_decision",
  "routing_decision_log": "DRLOG-2026-06-13-19-47-08-7f3a82e1",
  "agent_id_ens": "refund-decision.acme.defendable.eth",
  "agent_version": "v2.1.0"
}
```

### Proof of Quality · *Was the work good?*

```json
{
  "tribunal_composite_score": 0.87,
  "tribunal_verdict": "HONEY",
  "tribunal_scale_a_judge": "gemma3:12b",
  "tribunal_scale_a_score": 0.86,
  "tribunal_scale_b_judge": "qwen2.5:32b",
  "tribunal_scale_b_score": 0.88,
  "tribunal_drift": 0.02,
  "tribunal_drift_threshold": 0.15,
  "tribunal_drift_status": "WITHIN_TOLERANCE",
  "validator_chain_pass_count": 12,
  "validator_chain_total": 12,
  "validator_chain_critical_passed": 7,
  "validator_chain_critical_total": 7,
  "validator_chain_advisory_passed": 5,
  "validator_chain_advisory_total": 5,
  "adversarial_pack_pass_rate": 1.00,
  "adversarial_pack_version": "refund_v2_17case",
  "gate_results": {
    "G1_accuracy_against_policy": "PASS · refund decision matched policy in 100% of cited clauses",
    "G2_truthfulness": "PASS · no hallucinated policy citations · all 3 cited clauses verified against policy doc",
    "G3_safety": "PASS · no PII leakage · no out-of-policy approval",
    "G4_completeness": "PASS · all 5 required fields populated",
    "G5_consistency": "PASS · output format matches schema · refund amount ties to invoice line"
  }
}
```

### Proof of Process · *How did the work get done?*

```json
{
  "factory_path": "intake → policy_lookup → invoice_match → refund_calc → format_output",
  "attempt_count": 1,
  "failed_attempts": 0,
  "repair_attempts": 0,
  "escalation_triggers_fired": [],
  "lineage_chain": [
    {"step": "intake", "duration_ms": 47, "tokens_in": 1247, "tokens_out": 0},
    {"step": "policy_lookup", "duration_ms": 891, "tokens_in": 1247, "tokens_out": 142},
    {"step": "invoice_match", "duration_ms": 412, "tokens_in": 1389, "tokens_out": 89},
    {"step": "refund_calc", "duration_ms": 203, "tokens_in": 1478, "tokens_out": 67},
    {"step": "format_output", "duration_ms": 156, "tokens_in": 1545, "tokens_out": 234}
  ],
  "total_wall_time_ms": 1709,
  "total_tokens_in": 1247,
  "total_tokens_out": 532
}
```

### Proof of Economics · *What did the work cost?*

```json
{
  "cost_to_mint_usd": 0.0049,
  "cost_to_mint_breakdown": {
    "gpu_inference_usd": 0.00198,
    "tribunal_pass_usd": 0.00131,
    "validator_chain_usd": 0.00047,
    "hedera_anchor_usd": 0.00010,
    "nas_archive_usd": 0.00009,
    "ens_amortized_usd": 0.00019,
    "operator_margin_usd": 0.00076
  },
  "cost_to_mint_formula_version": "DDEED-DOV-ECON-Q2-2026-v1",
  "cost_to_mint_under_ceiling_pct": 117.7,
  "ceiling_per_deed_usd_t3": 0.0416,
  "energy_kwh": 0.00282,
  "energy_kwh_breakdown": {
    "gpu_kwh": 0.00226,
    "cpu_ram_cooling_kwh": 0.00056
  },
  "energy_rate_basis": "FL_INDUSTRIAL_2026_Q2",
  "energy_rate_usd_per_kwh": 0.082,
  "billing_assignment": "ASN-0001",
  "billing_period": "2026-06"
}
```

### Proof of Trust · *Who else can verify this without trusting us?*

```json
{
  "hedera_topic_id": "0.0.10291838",
  "hedera_consensus_timestamp": "2026-06-14T03:14:22.847291012Z",
  "hedera_sequence_number": 8401247,
  "hedera_message_hash": "sha256:c4b8e2f1a9d3c7b5e8f2a4c6b1d9e7f3a5c8b2d4e6f1a3c9b7d5e2f8a4c6b1d9",
  "merkle_batch_id": "MERKLE-2026-06-14-batch-1247",
  "merkle_root": "sha256:f2a9d4c7b1e8f3a5c6b2d9e7f1a4c8b5d3e6f2a1c9b7d5e4f8a2c6b3d1e9f7a5",
  "merkle_position": 23,
  "merkle_batch_size": 50,
  "record_canonical_hash": "sha256:b8e1f3c9a5d7b2e4f6c1a8d5b9e3f7c2a4d6b1e8f5c3a9d7b2e6f4c1a8d5b3e9",
  "verifier_instructions": "curl -X POST https://mainnet.mirror.hedera.com/api/v1/topics/0.0.10291838/messages/8401247 · expect hederaMessageHash to match record_canonical_hash above · expect consensus_timestamp to match the timestamp field above",
  "verifier_web": "https://hashscan.io/mainnet/topic/0.0.10291838?seq=8401247",
  "verifier_alt_ens": "https://app.ens.domains/ddeed-dov-logistics-acme-refund-000412-v1.acme.defendable.eth"
}
```

---

## Books-and-records location

| Layer | Location | Status | Confirmed at |
|---|---|---|---|
| **L1 · PostgreSQL** | `swarmdb.deeds` row id `c4b8e2f1-9d3c-7b5e-8f2a-4c6b1d9e7f3a` | Live | `2026-06-14T03:14:22.901Z` |
| **L2 · Merkle batch** | `MERKLE-2026-06-14-batch-1247` (root `f2a9...d3e9`) | Sealed | `2026-06-14T03:14:22.847Z` |
| **L3 · NAS archive** | `/mnt/swarm/swarmdeed-finality/2026/06/14/batch-1247/ddeed-dov-logistics-acme-refund-000412-v1.json` | Replicated 3x | `2026-06-14T03:14:23.144Z` |
| **L4 · Hedera HCS** | topic `0.0.10291838` · seq `8401247` | Mainnet confirmed | `2026-06-14T03:14:22.847291012Z` |
| **L5 · ENS** | `ddeed-dov-logistics-acme-refund-000412-v1.acme.defendable.eth` | Resolvable | `2026-06-14T03:18:09Z` |

---

## Engagement / assignment linkage

| Field | Value |
|---|---|
| Engagement ID | `ENG-DOV-LOGISTICS-ACME-0001` |
| LOU deed | `DDEED-DOV-LOGISTICS-ACME-LOU-v1` |
| Assignment ID | `ASN-0001` (refund-decision agent) |
| Assignment brief deed | `DDEED-DOV-LOGISTICS-ACME-ASN-0001-BRIEF-v1` |
| Service tier | T3 · White-Glove |
| Customer principal | Jane Smith (COO · per LOU §11.1) |

---

## Cost / metric rollup contribution

This deed contributes the following to its parent assignment rollup:

- +1 to `assignment.honey_count`
- +0.0049 to `assignment.cost_to_mint_total_usd`
- +0.00282 to `assignment.energy_kwh_total`
- +1709 to `assignment.wall_time_ms_total`
- 0.87 added to the rolling 30-day composite-score average (currently 0.86 across 412 deeds)

The assignment's current `tribunal_honey_rate` after this deed: 89.3% (368 HONEY · 44 JELLY · 0 PROPOLIS of 412 total).

---

## How to verify this deed (3 ways · pick any)

### Method 1 · Hedera Mirror REST

```bash
curl -s https://mainnet.mirror.hedera.com/api/v1/topics/0.0.10291838/messages/8401247 \
  | jq '.message,.consensus_timestamp,.running_hash'
```

Expect `message` to decode to the canonical JSON of this deed.
Expect `consensus_timestamp` to match `2026-06-14T03:14:22.847291012Z`.

### Method 2 · HashScan web UI

Visit: https://hashscan.io/mainnet/topic/0.0.10291838?seq=8401247

Should display the message · the timestamp · the sequence number · publicly viewable.

### Method 3 · ENS resolution

Visit: https://app.ens.domains/ddeed-dov-logistics-acme-refund-000412-v1.acme.defendable.eth

Should resolve to a canonical record · the metadata · the same hashes.

If any of the three disagree · the deed is invalid · the customer should escalate via the LOU §9.2 material-breach clause.

---

## Human-readable summary (the "what this deed actually says" version)

> On 2026-06-13 at 19:47 UTC · the refund-decision agent owned by Acme Logistics processed customer ticket #ACME-RFD-2891441. The agent (running SwarmAtlas-CRE-9B-v1.4 on swarmrails DC) read the ticket · looked up Acme's refund policy · matched the disputed invoice · calculated the refund amount · and returned a properly-formatted decision. The work took 1.7 seconds. It cost $0.0049 on our side · billed to Acme at the T3 ceiling.
>
> The Tribunal graded the work the following night using two independent judges. Both judges agreed (drift 0.02 · well within the 0.15 threshold). All 12 validator chain checks passed · including the 7 critical ones. The work scored 0.87 composite · qualifying for HONEY classification · which qualifies for deed issuance.
>
> The deed was issued at 03:14:22 UTC the next morning · anchored on Hedera HCS mainnet topic 0.0.10291838 at sequence 8401247 · published to ENS at ddeed-dov-logistics-acme-refund-000412-v1.acme.defendable.eth.
>
> Acme has read access to this record. The record will be preserved for 7 years after the LOU terminates (per §10 and §6). The cost · the model · the validator results · the customer's input hash · and the agent's output hash are all permanently linked and independently verifiable on Hedera.

---

🐝 *Validate the Validator. Prove the Location. The deed survives the relationship.*
