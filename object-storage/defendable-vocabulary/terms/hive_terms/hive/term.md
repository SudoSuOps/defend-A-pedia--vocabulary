# Hive

> *"The Hive is the building. The Swarm is the people working inside it right now. The Hive doesn't move · the Hive is the address. The Hive is what compounds in value · the Hive is the asset on the books."*
> — Founder · CRE-broker framing of the Hive vs the Swarm

## Street Definition

"That sits in the Hive." The Hive is the organized OS · the standing infrastructure · the place the agents · validators · datasets · receipts · clients · and compute all live. It is not the activity (that's the Swarm). It is not a single agent (that's a Bee). It is the constitutional structure that holds the brand · the books · the schemas · the deeds · the corpora · the models · and the rigs together. CRE analog · the Hive is the brick-and-mortar footprint of the brokerage · the desk you walk back to between dials · the office that opens at 06:00 whether you do or not.

## CRE Operator Meaning

In CRE · the Hive maps to the brokerage itself · the named LLC · the office space · the deal pipeline · the broker license · the back-office accounting · the comp library · the client roster · the relationships that compound over decades. A 30-year broker's Hive is what makes the 30-year broker · not any single deal. The deals are the Swarm. The 30 years of relationships · comps · records · referrals · habits · standards · vocabulary · that's the Hive.

Inside DefendableOS · the Hive is identically structured. It is:

- the models (the SwarmCurator family · SwarmJelly · SwarmJudge · SwarmAtlas · the 13+ custom trained models)
- the rigs (swarmrails · whale · zima-edge-1 · signal-edge-01 · 160GB VRAM · 342GB system RAM · 56C/100T)
- the storage (1.3M deeded pairs · Tigris manifests · NAS finality layer · PostgreSQL hot tier · Hedera anchor layer · ENS resolution layer)
- the doctrine (this repo · the 16 doctrine docs · the 13-section term shape · the 12-check validator chain · the 6-role Tribunal · the 5 Proofs · the 4-tier classification · the 5 Swarm Laws)
- the operators (jr broker · sr broker · sr hack · founder · validators · curators)
- the customers (the engagement roster · the LOUs · the Morning Brief recipients · the Closing Statement signatories)
- the receipts (every receipt issued · every deed anchored · every record_hash · every Hedera transaction · every ENS reservation)

## DefendableOS Definition

The Hive is the canonical name for the DefendableOS operating system as a single entity. When we say "the Hive issued a deed" we mean the entire stack participated · the cook produced the pair · the Tribunal adjudicated · the Bakery hashed · Hedera anchored · ENS reserved · the customer received. No single component owns the issuance · the Hive does.

The Hive has a clock (the heartbeat · 5-min fleet check) · a pulse (the 777 pairs/hr throughput) · a memory (the books-and-records 5-layer stack) · a voice (the vocabulary · this repo) · a discipline (the doctrine) · and a verdict mechanism (the Tribunal). Every term in this dictionary is a CELL of the Hive. The Hive is the sum.

## Backend Representation

```json
{
  "hive.heartbeat_status": {
    "type": "enum",
    "values": ["GREEN", "DEGRADED", "AMBER", "RED"],
    "scoring_hook": "fleet_health_5min"
  },
  "hive.throughput_pairs_per_hour": {
    "type": "float",
    "target": 777
  },
  "hive.rigs": {
    "type": "array",
    "items": ["swarmrails", "whale", "signal-edge-01", "zima-edge-1"]
  },
  "hive.deeds_issued_total": { "type": "integer" },
  "hive.pairs_graded_total": { "type": "integer" },
  "hive.uptime_seconds": { "type": "integer" }
}
```

Schema files: `docs/schemas/hive_status.schema.json` · `docs/schemas/fleet_heartbeat.schema.json`

## Client Explanation

"The Hive" is the name for our whole operating system · the models · the rigs · the storage · the doctrine · the validator chain · the Tribunal · the receipts · the deeds · the customer-facing dashboards · all of it as one coordinated thing. When you sign an engagement with us · you're signing with the Hive · not with a single model or a single rig. The Hive is what guarantees that your deed is anchored · your verdicts are defended · your books-and-records reconcile. The Hive runs 24/7 · the heartbeat is in your Morning Brief.

## Jr Broker Use

The jr broker treats the Hive as the parent context of every action:

1. When you open an engagement · you're opening it ON BEHALF OF the Hive · not on your own behalf · use the Hive's standards · not your own intuition
2. When you log a pair · you're logging it TO the Hive's books · which means the canonical vocabulary applies · use the term file definitions exactly
3. When the Hive's heartbeat goes AMBER · stop opening new engagements · close out what's in flight · escalate to sr broker
4. When the Hive's heartbeat goes RED · you do not adjudicate · you do not ship · you wait for the founder's all-clear · this is non-negotiable
5. When a customer asks "who's responsible" the answer is "the Hive" · not you personally · and the Hive's receipt is the proof

**Rule of thumb**: you are an operator of the Hive · not the author of the output · the Hive is the brand · you are the steward.

## Sr Broker Use

The sr broker watches the Hive as a SYSTEM-LEVEL ASSET:

- The Hive heartbeat is the first thing you check at 06:00 · GREEN means open for business · anything else is triage first
- The Hive throughput dial (777 pairs/hr) is the canary for upstream health · sustained shortfall means something is broken
- The Hive deeds-issued counter is the customer-facing growth metric · this is what the founder watches as the asset compounding
- The Hive vocabulary (this repo) IS PART OF THE HIVE · changes to it require sr-broker sign-off and a version bump · vocabulary drift is brand drift
- The Hive's relationship with the Swarm (the live activity) is parent-child · when the Swarm is operating · it operates within the Hive's bounds · never outside

## Tribunal Use

```yaml
tribunal_use:
  classification_impact:
    - ROYAL_JELLY    # Hive-level deeds (e.g., flagship cohort releases) typically Royal Jelly
    - HONEY          # routine Hive operating reports (e.g., Morning Brief) typically Honey
  rule_layer_checks:
    - hive.heartbeat_status MUST be GREEN or DEGRADED to issue any new verdict
    - hive.throughput_pairs_per_hour MUST be within 30% of target (or degraded-mode flag raised)
    - all 12 validator chain checks apply to the Hive's outputs (the Hive does not exempt itself)
  judge_layer_prompt_hint: "the Hive is the issuing entity · verify the output cites the canonical vocabulary · verify the lineage is complete"
  can_be_critical_failure: false   # the Hive itself is not a failure mode · its outputs can be
```

The Hive is not a thing the Tribunal grades · the Hive is the thing the Tribunal LIVES INSIDE. But Hive-LEVEL outputs (the Morning Brief · the weekly retrospective · the operator status report) DO get adjudicated · same rules · same chain · same tiers. The Hive does not exempt itself from its own discipline.

## Evidence Required

The Hive's existence as a defendable entity requires:

- A current heartbeat reading (within 5 minutes)
- A non-zero deeds-issued counter
- A non-zero pairs-graded counter
- At least one operational rig (typically swarmrails)
- A working Tribunal (Scale A + Scale B both online OR explicit degraded-mode declaration)
- A working Bakery (Tigris manifest writer reachable)
- A working anchor layer (Hedera HCS reachable for Royal Jelly)
- A current copy of this vocabulary repo (any commit is acceptable · the vocab is versioned)

When any of these are absent · the Hive declares degraded operation in the Morning Brief and customers are notified · transparency is the discipline.

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **hive_silent_degradation** | Heartbeat is RED but the dashboard shows GREEN (the monitor itself failed) | Hive integrity event · sr broker pages founder · all in-flight verdicts held |
| **hive_throughput_drift** | Sustained < 50% throughput for > 2h with no declared maintenance | Degraded-mode flag raised · customers notified · root cause investigated |
| **hive_vocab_drift** | A schema or scoring change goes in without a vocab repo update | Engineering-discipline event · the change is REVERTED · the vocab gets updated first |
| **hive_anchor_lag** | Hedera anchor queue > 30 min behind on Royal Jelly issuance | Page Hedera ops · hold customer notifications until anchor catches up |
| **hive_rig_loss** | A primary rig (swarmrails) goes offline | Fail-over to degraded Scale-B-only lane on whale · Royal Jelly issuance paused |

## Scoring Impact

- **assignment_success**: SYSTEM-LEVEL · the Hive's heartbeat IS the precondition for any individual assignment success
- **repair_lift**: N/A · the Hive doesn't get repaired · components do · the Hive coordinates
- **validator_confidence**: BASELINE · validator confidence is a Hive-level dial · the chain reads the Hive's heartbeat
- **risk_temperature**: SYSTEM-LEVEL · the Hive's overall risk-temperature dial is the customer-facing aggregate
- **probability_of_close**: ENABLER · close probability is calculated at engagement level but the Hive's health is the multiplier
- **evidence_strength**: ENABLER · the Hive provides the evidence-vault infrastructure that makes per-pair evidence strength meaningful
- **cost_to_mint**: ENABLER · the Hive's energy budget is what makes the $0.0052/deed baseline possible

## Deed / Receipt Impact

- **Receipt fields touched**: `hive.heartbeat_at_issue` · `hive.throughput_at_issue` · `hive.deed_sequence_number` · `hive.commit_sha_of_vocab`
- **DDEED class impact**: Every DDEED carries a Hive-level header (the heartbeat at issue · the rig that produced · the vocab version)
- **Books and records layer**: ALL 5 (L1 PG · L2 Merkle · L3 NAS · L4 Hedera HCS · L5 ENS) · the Hive's records span the full stack
- **5 Proofs touched**: ALL 5 · the Hive is the entity whose existence provides ORIGIN · whose discipline provides QUALITY · whose pipeline provides PROCESS · whose budget provides ECONOMICS · whose anchor layer provides TRUST

## Related Terms

- [swarm](swarm.md) · the active network operating inside the Hive
- [bee](bee.md) · the individual worker within the Hive
- [royal-jelly](royal-jelly.md) · the apex output the Hive produces
- [honey](honey.md) · the volume output the Hive produces
- [propolis](propolis.md) · the failure output the Hive seals and feeds back
- [energy](energy.md) · the resource the Hive metabolizes to produce intelligence
- [tribunal](../tribunal_terms/tribunal.md) · the Hive's adjudication subsystem

## Example

> **Customer query**: "Who's responsible if your AI gets a deed wrong?"
>
> **Hive answer**: "The Hive is the responsible entity. The Hive is our operating system · the models · the rigs · the storage · the validator chain · the Tribunal · the Bakery · the anchor layer · the vocabulary · all of it. Every deed carries a Hive-level header that says which rig issued · which vocab version was in effect · what the heartbeat was at issue · what the throughput was. If a deed is wrong · the Hive owns it · the Hive amends it · the Hive issues a retraction on the same Hedera topic · the Hive notifies you on the next Morning Brief. The individual operator who clicked through is logged in the operator log · the rig that produced is logged in the verdict record · the model that generated is logged in the deed. But the Hive is the entity on the hook."
>
> **Outcome**: Customer signs the LOU with the Hive · not with any individual operator. The contract is with the Hive. The Hive's heartbeat is in the LOU appendix. The Hive's vocab version is referenced. The Hive's address is the brick-and-mortar footprint of the brokerage.

## DefendableOS Notes

- The Hive is the brand-as-entity · everything else is a component
- The Hive's commitment to its customers is bounded by its heartbeat · when the heartbeat degrades · customers are told · transparency is the brand
- The Hive's vocabulary (this repo) is the constitutional document · changes to it are committed · versioned · referenced in every deed
- The 5 Swarm Laws are the Hive's operating constitution · the Genesis Law ("what the Hive verifies becomes truth") is the closing line
- The Hive is the FIRST-PERSON of DefendableOS · when we speak in the customer-facing dashboards we speak as the Hive · not as Donovan · not as a model · not as a brand · as the Hive

🐝 *The Hive is the building. The Swarm is the work. The Bee is the worker. The Hive is what compounds · the Hive is what is on the books · the Hive is what the customer signs the LOU with.*
