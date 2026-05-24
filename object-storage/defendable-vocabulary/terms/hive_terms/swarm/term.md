# Swarm

> *"The Swarm is the floor in motion. The phones ringing. The dials in flight. The bees coming back to the Hive with intel · stamping it · anchoring it · moving on to the next. The Swarm is what the Hive looks like when it's working."*
> — Founder · the Swarm-vs-Hive distinction

## Street Definition

"The Swarm is hot today." The Swarm is the active network · the live agents · the compute that's metabolizing energy and producing pairs RIGHT NOW. If the Hive is the brick-and-mortar footprint · the Swarm is the activity inside it · the phones ringing · the dials in flight · the cooks running · the Tribunal grading · the deeds being issued · the customers being briefed. The Swarm is what makes the Hive's heartbeat readable.

In CRE language · the Swarm is the deal flow · the pipeline · the live floor · the brokers on the dials · the appraisers in the field · the underwriters in the back · the closers at the title company · the relationships in motion. A brokerage's Hive doesn't change much week-to-week · its Swarm changes by the hour. The Swarm is the verb. The Hive is the noun.

## CRE Operator Meaning

In CRE · the Swarm is what fills the pipeline. The 14 listings being scanned this morning. The 3 LOIs being negotiated this afternoon. The 1 deal closing today. The 2 sponsors on the phone this hour. The 6 jr brokers on the dials. The sr broker reading inbound digests. The validator running comps. The back-office reconciling commissions. All of it · all happening at once · all coordinated by the Hive's standards · all logged in the Hive's books. THAT is the Swarm.

A healthy Swarm is the proof the Hive is alive. A quiet Swarm is the warning the Hive is starving. A chaotic Swarm is the warning the Hive's discipline is slipping. The sr broker reads the Swarm's tempo every hour.

## DefendableOS Definition

The Swarm is the runtime layer of the Hive · the live active network of:

- agents (the SwarmCurator cooks running · the SwarmJudge passes · the SwarmJelly repairs · the SwarmRouter routing)
- validators (the 12-check chain running on every pair in flight)
- compute (the 4 rigs metabolizing energy · swarmrails 165 tok/s 9B concurrent + 88 tok/s 27B concurrent · whale's RTX 3090 running SwarmJelly inference · zima-edge holding the signal heartbeat · signal-edge holding the inference edge case)
- inflight verdicts (the Tribunal queue · the Bakery write queue · the Hedera anchor queue · the ENS reservation queue)
- live customer engagements (the LOUs in flight · the Morning Briefs being generated · the Closing Statements being assembled)

The Swarm is what produces the 777 pairs/hr throughput. The Swarm is what makes Royal Jelly. The Swarm is what makes Honey. The Swarm is what flags Jelly. The Swarm is what seals Propolis. The Swarm IS the work. The Hive is the structure that holds it.

## Backend Representation

```json
{
  "swarm.live_agents_count": { "type": "integer" },
  "swarm.active_cooks": {
    "type": "array",
    "items": { "type": "string" }
  },
  "swarm.tribunal_queue_depth": { "type": "integer" },
  "swarm.bakery_write_queue_depth": { "type": "integer" },
  "swarm.hedera_anchor_queue_depth": { "type": "integer" },
  "swarm.energy_draw_watts": { "type": "float" },
  "swarm.pairs_in_flight": { "type": "integer" },
  "swarm.last_pair_completed_at": { "type": "timestamp" }
}
```

Schema files: `docs/schemas/swarm_status.schema.json` · `docs/schemas/swarm_queue.schema.json`

## Client Explanation

"The Swarm" is what you see running on our live status page · the work happening right now · the agents working · the validators checking · the deeds being issued · the throughput in pairs-per-hour. The Swarm is the live counterpart to the Hive · the Hive is the stable infrastructure · the Swarm is what is operating inside it. When you receive a Morning Brief, the Swarm produced it. When you receive a Closing Statement, the Swarm assembled it. When a deed lands on the public ledger with your record_hash, the Swarm was the verb that put it there.

## Jr Broker Use

The jr broker treats the Swarm as the LIVE FLOOR they operate on:

1. The Swarm's tempo (live pair throughput) is the heartbeat you watch · when it stalls · investigate
2. Your own engagements ADD to the Swarm · log them within 5 minutes of opening · the Swarm depth is a real-time number
3. When the Swarm's queue depth balloons (Tribunal queue > 1000 · Bakery queue > 500) · stop opening new engagements · close out what's in flight · let the Swarm catch up
4. When the Swarm is HOT (throughput > target) · don't slow it · ride it · the cook is performing
5. When the Swarm is QUIET (throughput < 50% target for > 1h) · check the Hive's heartbeat · usually an upstream component went amber

**Rule of thumb**: the Swarm is the live workflow · the Hive is the stable wall · operate AT the Swarm's pace WITHIN the Hive's bounds.

## Sr Broker Use

The sr broker watches the Swarm as the OPERATING-PRESSURE GAUGE:

- The Swarm's queue depths are the first early-warning signal for upstream breakage · faster than the heartbeat (heartbeat lags by 5 min · queue depth changes second-by-second)
- The Swarm's energy draw tells you what your cost-to-mint is in real time · spikes mean a heavy cook is in flight · sustained high draw without throughput gain means an inefficiency · investigate
- The Swarm's per-rig contribution should be balanced according to its allocated role · if swarmrails GPU 1 is at 100% for hours while GPU 0 is idle · the scheduler is broken
- The Swarm's adversarial-source flag rate (Propolis verdicts per hour) is the SECURITY heat map · spikes mean a campaign is incoming
- The sr broker can throttle the Swarm (slow inbound cook rate · drain the queue) but cannot speed it (the throughput ceiling is the rigs' compute · don't push past it · burnt cooks corrupt the corpus)

## Tribunal Use

```yaml
tribunal_use:
  classification_impact: []   # the Swarm itself does not get a tier · it IS the verdict-producing layer
  rule_layer_checks:
    - swarm.tribunal_queue_depth MUST be within operational bounds (< 5000) for normal-mode verdicts
    - swarm.bakery_write_queue_depth MUST be < 1000 for any verdict to be considered finalized
    - swarm.hedera_anchor_queue_depth MUST be < 200 for any Royal Jelly verdict to be considered anchored
  judge_layer_prompt_hint: "the Swarm is the verdict producer · the judge does not grade the Swarm · the judge runs INSIDE the Swarm"
  can_be_critical_failure: false   # Swarm-level failures cascade to Hive-level alerts · not single-pair Propolis events
```

The Swarm is the runtime container of the Tribunal · not a thing the Tribunal grades. But Swarm-level metrics (queue depths · throughput · energy draw) are inputs to the rule layer's degraded-mode decisions.

## Evidence Required

To describe the Swarm as healthy:

- A live throughput reading (pairs/hr) within 30% of the 777 target
- A current per-rig contribution map (which rig is doing what · in what proportion)
- Queue depth readings across Tribunal · Bakery · Hedera · ENS layers
- An energy draw reading (watts) consistent with the active cook profile
- A `last_pair_completed_at` within 5 minutes
- Zero stuck verdicts (verdicts older than 4 hours without resolution)

When any of these are missing or out-of-band · the Hive's heartbeat downgrades to AMBER and the Swarm is described as degraded in the Morning Brief.

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **swarm_stall** | Throughput drops to zero for > 5 min · queue keeps growing | Hive heartbeat goes AMBER · sr broker pages rig owner |
| **swarm_runaway** | Energy draw spikes above safe limits · cooks running hot without lift | Throttle the upstream cook rate · investigate · usually a misconfigured temp |
| **swarm_imbalance** | One rig at 100% · others idle · scheduler stuck | Restart the router proxy · re-balance · log the event |
| **swarm_queue_overflow** | Tribunal queue > 5000 · Bakery > 1000 · system back-pressure failing | Halt new engagements · drain the queues · escalate to founder if not resolved in 30 min |
| **swarm_adversarial_spike** | Propolis-rate-per-hour exceeds threshold · security event | Page sr broker AND founder · investigate likely attack campaign |

## Scoring Impact

- **assignment_success**: PROCESS-LEVEL · the Swarm's health is the necessary condition for any assignment to close
- **repair_lift**: PROCESS-LEVEL · SwarmFixer runs INSIDE the Swarm · the Swarm's health gates repair throughput
- **validator_confidence**: PROCESS-LEVEL · the validator chain runs INSIDE the Swarm · queue back-pressure can defer validator confidence reporting
- **risk_temperature**: SYSTEM-LEVEL · the Swarm's adversarial-flag rate IS the risk-temperature gauge
- **probability_of_close**: PROCESS-LEVEL · close probability is calculated within engagements running inside the Swarm
- **evidence_strength**: PROCESS-LEVEL · the evidence vault writes happen inside the Swarm
- **cost_to_mint**: DIRECT · the Swarm's energy draw IS the cost-to-mint numerator · throughput IS the denominator

## Deed / Receipt Impact

- **Receipt fields touched**: `swarm.throughput_at_issue` · `swarm.queue_depths_at_issue` · `swarm.energy_draw_at_issue` · `swarm.rig_contribution_map`
- **DDEED class impact**: Every DDEED carries Swarm-level telemetry from the moment of issue
- **Books and records layer**: L1 PG (the Swarm's queue depth metrics are stored hot) · L3 NAS (the Swarm's per-rig contribution maps are archived)
- **5 Proofs touched**: PROCESS (the Swarm is the process) · ECONOMICS (the Swarm's energy draw is the cost)

## Related Terms

- [hive](hive.md) · the structural parent · the Swarm operates inside the Hive
- [bee](bee.md) · the individual worker · many Bees coordinated make the Swarm
- [energy](energy.md) · the resource the Swarm metabolizes
- [royal-jelly](royal-jelly.md) · what the Swarm produces at apex
- [honey](honey.md) · what the Swarm produces at volume
- [tribunal](../tribunal_terms/tribunal.md) · the adjudication layer that runs within the Swarm

## Example

> **Customer dashboard view at 14:00 local**:
>
> - Swarm throughput: 783 pairs/hr (target 777) · GREEN
> - Active cooks: SwarmCurator-9B (CRE batch) · SwarmCurator-27B (medical batch) · SwarmJelly repairs queue
> - Tribunal queue depth: 142 pairs (healthy)
> - Bakery write queue depth: 27 pairs (healthy)
> - Hedera anchor queue depth: 8 Royal Jelly cells (healthy)
> - Energy draw: 1,247 W (within profile)
> - Per-rig contribution: swarmrails GPU 1 (Scale A judging) 38% · swarmrails GPU 0 (Scale B judging + 27B cook) 47% · whale (SwarmJelly repair + 2B curator) 12% · zima-edge (heartbeat + signal) 3%
> - Last pair completed at: 13:59:58
> - Status: GREEN · Hive heartbeat consistent · no adversarial spike
>
> **Customer takeaway**: the Swarm is working · my engagements are being processed within service-level expectations · the deeds I'm expecting later today will land on time. The transparency of the dashboard is itself the trust dial.

## DefendableOS Notes

- The Swarm is the verb · the Hive is the noun · keep this distinction tight in customer-facing copy
- The Swarm's throughput is the most user-visible health metric · customers track it · we publish it · we do not hide degradations
- The Swarm-LEVEL adversarial flag rate is the security weather report · we publish it weekly · transparency about attacks is part of the brand discipline
- A quiet Swarm is a problem · a hot Swarm is a feature · a chaotic Swarm is a discipline failure · operators learn to read the difference within their first 30 days
- The Swarm is not "the team" · it is the active runtime · the team operates the Swarm · the team is part of the Hive

🐝 *The Swarm is what the Hive looks like when it's working. The phones ringing. The dials in flight. The Tribunal grading. The deeds anchoring. Watch the Swarm to know if the Hive is alive.*
