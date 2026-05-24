# DefendableRouter Doctrine · The Middleware

> *"DefendableHQ NEVER sits in the call path."*
>
> — Founder charter

---

## What DefendableRouter is

DefendableRouter is the **cracked router for AI agents**. OpenWrt-energy positioning · ship the firmware · own the hardware · open the source · the operator runs it · we get paid on the receipts and the deeds · not on a per-call fee.

Mechanically: it's a thin write-only middleware that sits between the customer's agent and the customer's model provider. Every request and every response gets captured · hashed · receipted · queued for overnight Tribunal grading. Then the call returns to the agent · untouched · sub-5-millisecond pass-through. The agent doesn't know we're there. The customer's latency budget doesn't move. The receipts pile up. The defense lives in the shadows.

In CRE terms: DefendableRouter is the **building's electronic security system**. The cameras are recording every entry and exit · the badge readers are logging every door swing · the alarm system is armed · but the tenants and the customers walk in and out at full speed. They don't see the security. They see the building. The owner sees the audit trail. The insurance carrier accepts the policy. **The defense is invisible to the offense · and that's the point.**

---

## Why write-only

There is one cardinal rule:

> **DefendableHQ NEVER sits in the call path.**

Write-only means: we capture · we hash · we forward · we acknowledge · we move on. We do NOT gate. We do NOT score in real-time. We do NOT block a model response on validator output. We do NOT introduce a synchronous dependency on anything we control.

Why? Because the moment we're synchronous, we own the customer's uptime. The moment we own their uptime, we own their pager. The moment we own their pager, we're not a defense vendor anymore · we're a single point of failure. That's not the trade. That's the opposite of the trade.

The trade is:

- **Real-time** · the customer's offense agent runs free · uninterrupted · at its native latency
- **Shadows** · DefendableRouter writes the capture to the local queue · nothing blocks
- **Overnight** · at 2am cron the Tribunal grades the day's pairs · pattern-flags · surfaces lifts
- **6am** · the Morning Reconciliation Brief lands · the owner sees what shipped · what flagged · what got refined

Write-only is what makes the defense layer adoptable. A CTO will install a write-only middleware in 5 minutes. A CTO will spend 6 months evaluating a synchronous one. We chose the 5-minute install.

---

## The <5ms POST budget

The Router has a hard wall: every capture POST must complete in under 5 milliseconds at p99. Not p50. p99. That's the SLA we sell. That's the SLA we engineer to. That's the SLA the customer can put on their internal latency dashboard without flinching.

The 5ms wall is held by:

- **Local queue write** · the receipt drops into a NATS or Redis-streams local queue · no network hop on the hot path
- **Async hash compute** · SHA-256 is computed off the hot path · the hot path just writes the raw bytes
- **No HTTP egress in-line** · all outbound traffic to DefendableHQ goes through the async drain · on a separate process · on a separate budget
- **No model inference in-line** · zero · the model graders run on whale:11434 on a completely different schedule
- **Zero gating** · the Router cannot refuse a call · it can only annotate · gating is the customer's job (and it's the customer's pager when it fires)

If the Router can't hit the budget, it ships in **degraded mode** · captures get dropped to a local-disk overflow log · the agent still runs · the receipt deficit gets reconciled on the next drain cycle. **Customer uptime > our receipt completeness · always.**

---

## OpenWrt-energy positioning

The marketing surface is not "AI gateway" or "agent firewall" or "observability stack." Those words are already debased.

The surface is **OpenWrt for AI agents**. Cracked router. You flash it. You own it. You configure it. The source is open. The receipts are anchored on a chain you can verify. The license is **MIT-with-receipt-clause** · you can fork the code · you can sell the fork · we ask only that you don't strip the receipt-emit code · because the receipts are what make the network defendable for everyone running it.

Why OpenWrt? Because the audience knows what OpenWrt is. They flashed a $40 router with it in college. They run it on their home network now. They trust it because they can read the source and because their friends run it. They will trust DefendableRouter for the same reason. The brand is the cracked router · not the SaaS dashboard.

The cracked-router framing also kills the procurement objection. Procurement doesn't buy infrastructure-they-can't-self-host. With DefendableRouter, they CAN self-host. They don't have to. Most won't. But the option is what gets the contract signed.

---

## The 3 deployment modes

Same firmware. Three deployment modes. Customer picks based on data-residency posture.

### Mode 1 · EDGE

The Router runs on the customer's premises · usually inside the HoneyBox ($249 Jetson Orin Nano appliance). All capture stays local. All Tribunal grading runs local-only on the HoneyBox's onboard model. The only thing that leaves the building is the SIGNED METADATA `you got mail` ping · zero raw data egress.

For: regulated industries (healthcare · finance · gov · defense · legal · attorney-client privilege). The compliance officer can sleep. The auditor can audit. The data never moves.

### Mode 2 · CLOUD

The Router runs as a container · captures stream to DefendableCloud (the 128-RTX-6000 fleet at the operator-owned DC) · Tribunal grading runs on the cloud fleet · receipts come back signed and anchored. Standard SaaS posture · familiar to most teams.

For: SaaS-native customers who already trust hyperscaler-class providers · don't have data-residency constraints · want the lowest setup friction.

### Mode 3 · HYBRID

The Router runs at the edge for capture · forwards metadata-only to DefendableCloud for Tribunal grading · raw payloads stay local · graded verdicts come back to the edge for archive. Best of both worlds for teams who want cloud-grade Tribunal throughput without sending raw prompts off-prem.

For: mid-market teams with mixed data classes · some raw payloads that can leave · some that cannot · they want one control plane to manage both.

---

## The ENS bridge · per-agent attestation

Every agent that flows through DefendableRouter gets an ENS identity:

```
<agent>.<operator>.defendable.eth
```

Examples:

- `books-bot.acmecorp.defendable.eth` · the bookkeeping agent at ACMECorp
- `claims-triage.regional-insurer.defendable.eth` · the insurance-claims triage agent
- `discovery.law-firm.defendable.eth` · the legal-discovery agent

This is not vanity. This is **attestable agent identity**. The ENS record carries:

- The agent's class (offense / defense / observer)
- The operator's controlled-domain proof
- The pointer to the latest DDEED-DOV-AGENT for that agent
- The compliance contact at `compliance.<operator>.defendable.eth`

When a receipt is issued, the receipt cites the ENS name. When the deed clears, the deed updates the ENS pointer. When the customer's auditor or insurance carrier wants to verify the agent's lineage, they resolve the ENS name. One name. One canonical pointer. One chain of receipts back to genesis.

The ENS bridge is what makes the Router defensible to a third-party auditor. Without it, "the agent" is a string in a log. With it, "the agent" is a named principal with a verifiable history.

---

## The 5 Proofs anchored per receipt

Every Router receipt anchors all 5 Proofs · not 4 · not "as many as we can" · all 5. If a Proof is missing, the receipt is provisional and cannot promote to a deed.

1. **Proof of Origin** · which model · which endpoint · which agent ENS · which operator
2. **Proof of Quality** · what Tribunal said · what the rule-layer flagged · what the judge scored
3. **Proof of Process** · the full lineage · what the agent tried · what it called · what came back
4. **Proof of Economics** · token count · wall time · energy cost · CFO line item
5. **Proof of Trust** · Hedera HCS topic · Merkle root · ENS pointer · validator-chain checksum

Five Proofs. One receipt. The receipt is the deed's parent record. The deed is the customer's audit asset. The chain holds.

---

## License · MIT-with-receipt-clause

The Router firmware ships under **MIT-with-receipt-clause**. Plain MIT for the code · with one constitutional addition:

> *Forks and derivatives MUST preserve the receipt-emit path. Stripping the receipt emitter is a license violation. Anchoring receipts to an alternate ledger is permitted · stripping them is not.*

Why? Because the receipt network is a public good. Every Router that emits receipts makes the next Router more defendable · because attack patterns surface faster · because the AdversarialPack grows faster · because the validator chain gets stronger with every anchored event. A stripped fork is a free-rider. We allow the source to be free. We don't allow the network's defense to be diluted.

---

## Read next

- [`11_swarmfixer_doctrine.md`](11_swarmfixer_doctrine.md) · the refinery the Router feeds
- [`../vocabulary/defendableos_terms/defendablerouter.md`](../vocabulary/defendableos_terms/defendablerouter.md) · the term file
- [`../vocabulary/defendableos_terms/honeybox.md`](../vocabulary/defendableos_terms/honeybox.md) · the edge appliance · Mode 1 host
- [`../vocabulary/defendableos_terms/defendablecloud-com.md`](../vocabulary/defendableos_terms/defendablecloud-com.md) · the cloud fleet · Mode 2 host

---

🐝 *Write-only. Sub-5ms. Owned by you. Receipted by the Hive. The defense lives in the shadows.*
