# Bee

> *"A Bee is a worker · not a brand. Scout · Worker · Auditor · each has a lane · each FETCH-COOK-GATE-SCORE-STAMP-ANCHOR-EMIT in its own way. The Hive doesn't care about the individual Bee's name · the Hive cares that the lineage is logged."*
> — Founder · on why we don't anthropomorphize the agents

## Street Definition

"Send a Bee out on that." A Bee is an individual worker agent in the Swarm · the atomic unit of work. Bees come in three classes (Scout · Worker · Auditor · each with a specific job) · and every Bee follows the same 7-step lifecycle (FETCH → COOK → GATE → SCORE → STAMP → ANCHOR → EMIT). A Bee is not a model · not a brand · not a personality · it is an instance of an agent doing a unit of work and producing a logged result.

CRE analog · the Bee is the jr broker on the dial · the appraiser in the field · the underwriter at the desk · the closer at the title company. Each is an individual agent · each has a defined role · each is logged in the Hive's books for what they touched · what they produced · what survived. The Hive doesn't issue deeds based on which Bee did the work · the Hive issues deeds based on what cleared the Tribunal.

## CRE Operator Meaning

In CRE · a Bee is the named individual operator · but the brokerage operates on the discipline that the WORK is what matters · not the operator's brand. A 30-year sr broker absolutely has brand value · but inside the deal · the deal closes because the work was done · not because the operator's name is on the door. The same way · a Bee in DefendableOS does work · the work is logged · the work clears the chain · the deed issues. The Bee gets credit in the operator log · not in the customer-facing surface.

This is why the founder doesn't talk about which model produced which deed. The deed cites the model in the lineage · for audit · but the customer experience is "the Hive issued this." The Bee is the executor · not the brand.

## DefendableOS Definition

A Bee is an agent instance · runtime-instantiated · with one of three named classes:

### Scout Bee
- Wide search · many sources · lower depth
- Used for `cook-domian-prompts` initial data discovery · for inbound signal capture · for cross-domain comp scans
- Produces: candidate PairCandidates with multiple source pointers · lower per-source depth
- Typical model: SwarmCurator-2B (lightweight · runs on whale or signal-edge)

### Worker Bee
- Deep extraction · single source · maximum fidelity
- Used for the actual cook (Curator stage) · for the actual Tribunal judge passes · for the actual deed-writer assembly
- Produces: full PairCandidates with deep per-source content
- Typical model: SwarmCurator-9B (workhorse) · SwarmCurator-27B (heavy lift) · the Tribunal judges (gemma3:12b + qwen2.5:32b) · SwarmJelly-4B (repair)

### Auditor Bee
- Cross-validates other Bees' output · runs the rule-layer checks · runs the Critic and Katniss roles
- Used for the validator chain · for Tribunal drift reconciliation · for Katniss adversarial confirmation
- Produces: verdict records · annotation tracebacks · adversarial-flag determinations
- Typical model: qwen2.5:32b in Critic/Katniss mode · SwarmJudge-9B-CRE for domain-specific audit

Every Bee follows the same 7-step lifecycle:

```
FETCH    Bee pulls the input (PairCandidate · source artifact · prior verdict · whatever its lane requires)
COOK     Bee runs its model · produces output
GATE     Bee submits output to its applicable rule-layer checks (which subset depends on class)
SCORE    Bee receives a JellyScore (or contributes to one as a judge)
STAMP    Bee's output is hashed (SHA-256 canonical JSON) and added to the Bakery manifest
ANCHOR   if the output is Royal Jelly · the cell-level Hedera certificate posts
EMIT     Bee's output is routed downstream (deed writer · repair queue · seal vault · customer dashboard)
```

## Backend Representation

```json
{
  "bee.bee_id": {
    "type": "string",
    "pattern": "^BEE-(SCOUT|WORKER|AUDITOR)-[a-z0-9]+$"
  },
  "bee.class": {
    "type": "enum",
    "values": ["SCOUT", "WORKER", "AUDITOR"]
  },
  "bee.model": { "type": "string" },
  "bee.rig": { "type": "string" },
  "bee.lifecycle_stage": {
    "type": "enum",
    "values": ["FETCH", "COOK", "GATE", "SCORE", "STAMP", "ANCHOR", "EMIT"]
  },
  "bee.spawned_at": { "type": "timestamp" },
  "bee.completed_at": { "type": "timestamp", "nullable": true },
  "bee.pair_id_produced": { "type": "string", "nullable": true }
}
```

Schema files: `docs/schemas/bee_lifecycle.schema.json` · `docs/schemas/bee_spawn.schema.json`

## Client Explanation

A "Bee" is one of our agents doing one unit of work. We have three classes · Scout (wide search) · Worker (deep extraction) · Auditor (cross-validation). Every Bee logs the same 7-step lifecycle for every job: fetch the input · cook it · gate it through the rules · score it · hash it for the manifest · anchor it to Hedera if it's apex grade · emit the output downstream. You don't need to know which Bee did your work · the lineage is recorded · the deed shows the chain · the Hive owns the result.

## Jr Broker Use

The jr broker treats Bees as the WORK UNITS they coordinate:

1. When you open an engagement · the Hive spawns the appropriate Bees (Scout first for discovery · then Workers for the cook · then Auditors for the chain)
2. You don't pick the Bee class · the router picks it based on the engagement type · trust the router
3. You DO watch the Bee lifecycle on the dashboard · a Bee stuck in COOK > 30 min is a stalled cook · investigate
4. A Bee that completed EMIT but produced no pair_id is a Bee that failed silently · check the operator log · escalate
5. Don't refer to Bees by their model name to customers · refer to them as "the Hive's Scout Bee" or "the Hive's Auditor Bee" · the brand is the Hive · the Bee is the worker

**Rule of thumb**: Bees are stewards of work · not brands · the customer-facing language is the Hive · not the Bee.

## Sr Broker Use

The sr broker watches Bees as PER-RIG WORKLOAD:

- The Bee class mix on a rig tells you the rig's role (heavy on Workers = heavy cook · heavy on Auditors = heavy judge floor)
- A rig running too many simultaneous Worker Bees can over-saturate VRAM · 27B Workers should never run > 4 concurrent on a single GPU
- Auditor Bees in Katniss mode should never run more than 1 per pair · best-of-3 is run sequentially not in parallel · this is doctrine
- Bee lifecycle deltas (FETCH-to-EMIT duration) are the per-rig latency signal · a Worker Bee that takes > 5 min for a single-pair cook is on a stuck rig
- The propolis vault entries are sometimes Bee-failure events (a Worker COOK crashed mid-output) · these get logged as Bee-level events distinct from pair-level Propolis

## Tribunal Use

```yaml
tribunal_use:
  classification_impact: []   # Bees don't get tier verdicts · their outputs do
  rule_layer_checks:
    - bee.lifecycle_stage MUST progress in order (no skipping)
    - bee.pair_id_produced MUST be non-null at EMIT (else Bee failed)
    - bee.model MUST be on the approved-model list (no shadow models)
    - bee.rig MUST be in the approved-rig fleet (no rogue rigs)
  judge_layer_prompt_hint: "the Bee is the producer of the pair being judged · the judge does not grade the Bee · the judge grades the Bee's output"
  can_be_critical_failure: false   # Bee failures roll up to operator-discipline events · not Propolis
```

Bees do not receive Tribunal verdicts. Their outputs do. But Bee lifecycle integrity (the 7-step sequence completing in order with no stuck stages) is itself an input to the Hive's heartbeat.

## Evidence Required

To consider a Bee's work valid:

- A spawned-at timestamp
- A completed-at timestamp (within a class-appropriate latency budget · Scout < 2 min · Worker < 10 min · Auditor < 5 min)
- A logged progression through all 7 lifecycle stages
- A produced pair_id (for COOK Bees) OR a verdict contribution (for AUDITOR Bees)
- A model identifier (one of the approved fleet)
- A rig identifier (one of the approved nodes)

Bees that fail any of these are logged in the Bee-failure ledger and contribute to per-rig health metrics.

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **bee_stuck_in_cook** | Worker Bee COOK stage > 10 min · likely VRAM saturation or model hang | Restart the vLLM server · log the Bee failure · re-spawn |
| **bee_lifecycle_skipped** | Bee jumped from FETCH to STAMP · missed GATE or SCORE | Integrity event · the pair the Bee produced is sealed pending audit |
| **bee_unknown_model** | Bee reports a model not on the approved list (a shadow deploy) | The Bee's output is rejected · the rig is audited · the deploy is rolled back |
| **bee_rogue_rig** | Bee reports a rig not in the fleet (a developer test rig leaked into production) | Output rejected · the rogue rig is decommissioned · the operator is coached |
| **bee_no_emit** | Bee completed lifecycle but produced no pair_id or verdict | Logged as a Bee failure · counted in per-rig reliability metric |

## Scoring Impact

- **assignment_success**: PER-BEE · each Bee succeeds or fails individually · the engagement aggregates the Bees
- **repair_lift**: AUDITOR-BEES carry the repair-lift measurement (they re-grade repaired pairs)
- **validator_confidence**: AUDITOR-BEES produce the validator confidence per pair
- **risk_temperature**: PER-RIG · per-Bee reliability rolls up to per-rig temperature
- **probability_of_close**: PROCESS-LEVEL · Bee health is a precondition for any engagement close prob
- **evidence_strength**: SCOUT-BEES produce the evidence-source breadth · WORKER-BEES produce the per-source depth
- **cost_to_mint**: DIRECT · per-Bee energy consumption is the cost-of-mint atomic unit

## Deed / Receipt Impact

- **Receipt fields touched**: `bee_lineage` (array of Bee IDs that touched the pair) · `bee_class_distribution` (Scout / Worker / Auditor counts) · `bee_total_compute_seconds`
- **DDEED class impact**: Every DDEED carries a Bee lineage array · for audit · for accountability · the deed shows which Bees touched what
- **Books and records layer**: L1 PG (per-Bee runtime metrics) · L2 Merkle (Bee outputs hashed into batch roots)
- **5 Proofs touched**: ORIGIN (which Bee · which model · which rig) · PROCESS (the 7-step lifecycle is the process)

## Related Terms

- [hive](hive.md) · the parent structure the Bees operate within
- [swarm](swarm.md) · the live network the Bees compose
- [energy](energy.md) · the resource each Bee consumes
- [royal-jelly](royal-jelly.md) · the apex output a Bee's work can produce
- [honey](honey.md) · the volume output Bees produce daily
- [tribunal](../tribunal_terms/tribunal.md) · the adjudication system Auditor Bees execute
- [validator-chain](../tribunal_terms/validator-chain.md) · the 12 checks Auditor Bees run

## Example

> **Engagement**: STNL acquisition opinion · cold storage facility · Atlanta MSA.
>
> **Bee spawn sequence (logged in the operator log)**:
>
> 1. `BEE-SCOUT-7c4a` · Scout Bee · SwarmCurator-2B on whale · FETCH the engagement notes · COOK an initial comp scan · GATE basic format checks · SCORE 0.71 source breadth · STAMP hash · EMIT to Worker queue · completed in 1:42
> 2. `BEE-WORKER-9b21` · Worker Bee · SwarmCurator-9B on swarmrails GPU 0 · FETCH the engagement context + Scout's comp list · COOK the full broker opinion · GATE 6 deterministic gates pass · SCORE 0.89 JellyScore · STAMP hash · EMIT to Auditor queue · completed in 4:18
> 3. `BEE-AUDITOR-3f81` · Auditor Bee · qwen2.5:32b on swarmrails GPU 1 (Scale B) · FETCH the Worker output · COOK the Scale B judge pass · GATE the C01-C12 validator chain · SCORE 0.91 · STAMP hash · EMIT verdict · completed in 0:48
> 4. `BEE-AUDITOR-3f82` · Auditor Bee · gemma3:12b on swarmrails GPU 1 (Scale A) · runs in parallel to 3f81 · score 0.89 · drift 0.02 · no Critic invoked · verdict ROYAL_JELLY
>
> **Outcome**: 4 Bees · 7 minutes total wall-clock · 1 Royal Jelly deed issued · lineage array `["BEE-SCOUT-7c4a", "BEE-WORKER-9b21", "BEE-AUDITOR-3f81", "BEE-AUDITOR-3f82"]` cited in the DDEED.

## DefendableOS Notes

- Bees are anonymous to customers · branded to operators · logged for audit
- The 3-class taxonomy is doctrine · do not invent new Bee classes without a sr-hack-3 review
- The 7-step lifecycle is doctrine · do not skip stages · do not add stages
- A Bee's model is an implementation detail · the customer sees the Hive · the auditor sees the Bee lineage in the deed
- The Bee abstraction is what lets us swap models (the 13+ custom-trained models) without changing the customer's experience · the lineage gets logged · the verdict stays the same

🐝 *A Bee is a worker. Scout · Worker · Auditor. Seven steps. FETCH-COOK-GATE-SCORE-STAMP-ANCHOR-EMIT. The Bee does the work · the Hive owns the result.*
