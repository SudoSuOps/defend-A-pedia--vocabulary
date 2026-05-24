# DefendableRouter

## Street Definition

"Flash the cracked router on the box." That's how a Sr Hack rolls out DefendableRouter to a new customer. **DefendableRouter** is the cracked-router middleware that captures every agent call · hashes it · receipts it · forwards it · all in under 5 milliseconds. Write-only. OpenWrt-energy. You own it · you flash it · the receipts anchor on a chain you can verify.

## CRE Operator Meaning

In CRE the Router is the **electronic security system** in a Class A building. Cameras at every door. Badge readers logging every swing. Alarm armed 24/7. But the tenants don't see any of it · they walk in and out at full speed · the security is invisible to them and obvious to the insurance carrier. That's DefendableRouter. The customer's agents run free. The receipts pile up. The defense lives in the shadows.

## DefendableOS Definition

DefendableRouter is the thin write-only middleware that sits between an AI agent and its model/tool endpoints. Every request and every response is captured, SHA-256 hashed, queued for overnight Tribunal grading, and forwarded with sub-5ms p99 added latency. The Router NEVER sits in the customer's call path · NEVER gates · NEVER scores in real-time. It ships in 3 deployment modes (EDGE · CLOUD · HYBRID), binds every agent to an ENS identity (`<agent>.<operator>.defendable.eth`), and emits 5-Proof receipts that anchor to Hedera HCS. License: MIT-with-receipt-clause.

## Backend Representation

```json
{
  "defendablerouter.deployment_mode": {"type": "enum", "values": ["EDGE", "CLOUD", "HYBRID"]},
  "defendablerouter.firmware_version": {"type": "string", "pattern": "^v[0-9]+\\.[0-9]+\\.[0-9]+$"},
  "defendablerouter.p99_added_latency_ms": {"type": "integer", "max": 5},
  "defendablerouter.capture_mode": {"type": "enum", "values": ["WRITE_ONLY"], "const": "WRITE_ONLY"},
  "defendablerouter.queue_backend": {"type": "enum", "values": ["NATS", "REDIS_STREAMS", "LOCAL_DISK_OVERFLOW"]},
  "defendablerouter.agent_ens_required": {"type": "boolean", "const": true},
  "defendablerouter.receipt_anchor_chain": {"type": "string", "default": "hedera_hcs"},
  "defendablerouter.license": {"type": "string", "const": "MIT-with-receipt-clause"},
  "defendablerouter.degraded_mode_disk_overflow_enabled": {"type": "boolean", "default": true}
}
```

Schema files: `docs/schemas/router_receipt.schema.json` · `docs/schemas/deployment_mode.schema.json`

## Client Explanation

DefendableRouter is the cracked router for your AI fleet. It sits in front of your agents · captures every call · hashes the receipts · runs in under 5 milliseconds · doesn't slow you down · doesn't gate anything. We don't sit in your call path. You can self-host the source if you want. You can flash it onto a HoneyBox on your premises if your data can't leave. You can run it in our cloud if it can. Three modes. One firmware. Same defense.

## Jr Broker Use

When you wire DefendableRouter for a customer, verify the deployment mode against the customer's data-residency posture. Healthcare · finance · legal · gov · defense → EDGE only. SaaS-native with no constraints → CLOUD is fine. Mixed data classes → HYBRID. NEVER ship a customer in CLOUD mode if their compliance officer hasn't signed off · the residency mismatch is a Tribunal-grade governance violation.

## Sr Broker Use

The Sr Hack monitors the p99 latency dashboard. The 5ms wall is the SLA. If p99 drifts to 7ms · the Sr Hack triggers a Router health check before the customer notices. The Sr Hack also monitors the degraded-mode disk overflow rate · if disk overflow fires > 0.1% of captures, the async drain is backlogged · scale up the drain workers before the customer's receipt completeness drops.

## Tribunal Use

- **Rule layer**: Every Tribunal-graded pair MUST come from a Router receipt · synthesized pairs are rejected
- **Rule layer**: Router receipts MUST be < 5ms p99 latency · receipts from over-budget Routers are flagged
- **Rule layer**: Router MUST be in write-only mode · any synchronous-gating behavior is a governance violation
- **Judge layer**: Tribunal doesn't grade the Router · it grades the pairs the Router produced · Router quality is measured by receipt completeness rate

## Evidence Required

- Router firmware version (must be on approved list)
- Deployment mode declaration (EDGE/CLOUD/HYBRID)
- Customer compliance signoff for chosen mode
- p99 latency benchmark (proven ≤ 5ms)
- Receipt completeness rate (target ≥ 99.9%)
- Agent ENS registration (every agent behind the Router has an ENS identity)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `synchronous_gating` | Router gates calls in real-time · violates write-only doctrine | PROPOLIS · governance violation |
| `latency_breach` | p99 > 5ms · customer latency budget compromised | JELLY · operational alert |
| `mode_mismatch` | Customer in CLOUD mode without compliance signoff for residency | PROPOLIS · governance violation |
| `receipt_drop` | Receipt completeness < 99.9% · pair drift | JELLY · drain backlog escalation |
| `firmware_drift` | Router running unapproved firmware version | JELLY · upgrade required |
| `stripped_receipt_emitter` | Fork removed receipt-emit code · license violation | n/a · legal escalation |

## Scoring Impact

- **assignment_success**: HIGH · Router is the precondition for every receipt
- **repair_lift**: INDIRECT · no Router, no pair, no lift
- **validator_confidence**: HIGH · Router uptime IS the receipt-chain integrity
- **risk_temperature**: INVERSE · clean Router operation lowers risk
- **probability_of_close**: HIGH · the 5-minute install is the killer sales line vs synchronous competitors
- **evidence_strength**: HIGH · every receipt carries Router-captured raw evidence
- **cost_to_mint**: LOW · Router itself is open-source · cost is the deed mint downstream

## Deed / Receipt Impact

- **Receipt fields touched**: `router_receipt_id` · `deployment_mode` · `firmware_version` · `p99_latency_observed` · `agent_ens`
- **DDEED class impact**: Every DDEED references its source Router receipt · Router receipts are the parent of all deeds
- **Books and records layer**: L1 PostgreSQL → L2 Merkle → L3 NAS (raw capture) → L4 Hedera HCS (receipt hash) → L5 ENS (per-agent rollup)
- **5 Proofs touched**: ORIGIN (which Router, which firmware, which agent ENS) · PROCESS (the full capture lineage) · TRUST (anchor on Hedera + ENS pointer)

## Related Terms

- [defendableos](defendableos.md) · the parent platform
- [defendablecloud-com](defendablecloud-com.md) · the cloud-mode host
- [honeybox](honeybox.md) · the edge-mode appliance
- [clawcheck](clawcheck.md) · the intake form for new agents behind the Router
- [pair-candidate](../repair_terms/pair-candidate.md) · the Router's output
- [swarmfixer](../repair_terms/swarmfixer.md) · downstream consumer of Router receipts

## Example

> **Customer**: RegionalInsurer · 40-agent claims-triage fleet
>
> **Deployment**: HYBRID mode · Router at the edge in customer's AWS VPC · graded captures stream to DefendableCloud for Tribunal · raw PII payloads stay in customer VPC
>
> **Firmware**: defendablerouter:v1.4.2
>
> **Per-agent ENS**: 40 agents registered · all at `*.regional-insurer.defendable.eth`
>
> **Production stats (7-day)**: 1,247,883 captures · p99 latency 3.8ms · receipt completeness 99.98% · disk overflow fired 0.02% of captures (within tolerance)
>
> **Receipt**: every capture produces a router_receipt anchored to Hedera HCS topic 0.0.10291838 · receipts resolvable via `regional-insurer.defendable.eth/receipts/<id>`

## DefendableOS Notes

- The "DefendableHQ never sits in the call path" rule is constitutional · violating it makes us a SPOF · violating SPOF makes us another vendor on the customer's pager · which is the OPPOSITE of the trade
- The OpenWrt framing is what kills the procurement objection · customers can self-host · most don't · but the option signs the contract
- MIT-with-receipt-clause is the license model · stripping the receipt emitter is the one thing not allowed · we keep the network's defense intact even on forks
- DefendableRouter may ship before SwarmFixer as the commercial wedge · CFO-level pain (insurance angle) · easier demo than the refinery · simpler to deploy

🐝 *Write-only. Sub-5ms. You own it. The Hive verifies the receipts.*
