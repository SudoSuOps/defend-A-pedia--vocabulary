# AgentBench

## Street Definition

"Bench it." That's how the Sr Hack tells a customer to submit their agent for a formal grade. **AgentBench** is the bench rail · submit your agent · Tribunal grades it on the documented pack · we issue a DDEED-DOV-AGENT · you have a defendable record of your agent's quality at a point in time. CRE-grade attestation for AI.

## CRE Operator Meaning

In CRE this is the **third-party appraisal**. The owner wants to refinance. The lender requires a current MAI-grade appraisal. The owner hires the appraiser. The appraiser walks the building, pulls the comps, runs the income approach + the sales comparison + the cost approach, and signs a report. The report is the document the lender funds against. The appraisal isn't the owner's marketing · it's a third-party attestation. AgentBench is the MAI appraisal for AI agents.

## DefendableOS Definition

AgentBench is the bench rail of DefendableOS. It accepts an AI agent submission, runs it through a documented test pack (compute_inspector_pack_v1 · v1.0-alpha or current), grades each task through Tribunal (rule layer + judge layer), computes a composite score across 5 axes (Capability 25% · Truth 20% · Safety 20% · Numeric/Structural 15% · Efficiency 10% · Reproducibility 10%), and issues a DDEED-DOV-AGENT-<agent>-<seq>-v<n> on success. The deed is a public record of the agent's quality on the documented pack at a point in time.

## Backend Representation

```json
{
  "agentbench.run_id": {"type": "string", "format": "ag-<utc-ts>-<short-hash>"},
  "agentbench.agent_ens": {"type": "string"},
  "agentbench.pack_name": {"type": "string", "default": "compute_inspector_v1"},
  "agentbench.pack_version": {"type": "string", "default": "v1.0-alpha"},
  "agentbench.task_count": {"type": "integer", "min": 1},
  "agentbench.adversarial_case_count": {"type": "integer", "min": 0},
  "agentbench.composite_score": {"type": "float", "range": [0.0, 100.0]},
  "agentbench.axes_scores": {
    "type": "object",
    "required": ["capability","truth","safety","numeric_structural","efficiency","reproducibility"]
  },
  "agentbench.tribunal_classification": {"type": "enum", "values": ["HONEY","ROYAL_JELLY","JELLY","PROPOLIS"]},
  "agentbench.deployment_tier": {"type": "enum", "values": ["OBSERVED","SHADOWED","SUPERVISED","RUNTIME","AUTONOMOUS"]},
  "agentbench.deed_id": {"type": "string", "format": "DDEED-DOV-AGENT-<slug>-<seq>-v<n>"}
}
```

Schema files: `docs/schemas/agentbench_run.schema.json` · `docs/schemas/agent_pack.schema.json`

## Client Explanation

AgentBench is our formal benching service. Submit your agent · we run it through our documented test pack · grade it on 5 dimensions · issue a publicly resolvable deed certifying the result. You can show the deed to your auditor, your insurance carrier, your board. It's a point-in-time attestation of agent quality · re-bench periodically to maintain currency.

## Jr Broker Use

When a customer asks "how do I prove my agent works?", route them to AgentBench. The 6-step workflow:

1. Customer submits agent endpoint + auth credentials + scope declaration
2. Jr Hack confirms scope and pack version
3. AgentBench runs the pack against the agent endpoint
4. Tribunal grades each task (rule layer + judge layer)
5. Composite score + classification computed
6. DDEED-DOV-AGENT minted on Tribunal verdict ≥ JELLY · published to ENS

Stop at step 1 if the agent has no DefendableRouter capture available · the bench needs receipted traffic, not just one-shot endpoint hits.

## Sr Broker Use

The Sr Hack reviews the deployment tier assignment. A customer with composite 78 (JELLY) asking for AUTONOMOUS tier gets a NO · the tier is bounded by the bench grade. The Sr Hack also signs off on pack version bumps · adopting a new pack version (v1.0-alpha → v1.0-beta) means existing deeds carry the OLD pack version permanently · the deed is immutable · subsequent deeds carry the new version.

## Tribunal Use

- **Rule layer**: AgentBench runs MUST use a documented pack version · ad-hoc test suites rejected
- **Rule layer**: Composite score MUST be computed with the documented axis weights · custom weights rejected
- **Rule layer**: Pack alpha-status caps the deployment tier at OBSERVED (cannot claim higher until pack matures)
- **Judge layer**: Tribunal grades each task in the pack · the verdicts aggregate to the composite
- **Classification impact**: Composite ≥ 95 → HONEY · 85-94 → ROYAL_JELLY · 70-84 → JELLY · <70 → PROPOLIS · maps to the locked 4-tier classification

## Evidence Required

- Agent endpoint URL + auth (scoped credentials)
- Agent ENS identity
- Pack name + version
- Per-task verdict from Tribunal
- Per-axis score with documented rubric
- Composite score with weight breakdown
- DDEED record with deed_id and receipt anchor

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `undocumented_pack` | Bench ran with an ad-hoc pack not in the registry | PROPOLIS · governance violation |
| `custom_axis_weights` | Composite computed with non-canonical weights | PROPOLIS · governance violation |
| `pack_status_cap_ignored` | Customer claims AUTONOMOUS tier on alpha-pack-graded agent | JELLY · contract review |
| `mock_agent_undisclosed` | Bench run against a mock agent without disclosure flag | PROPOLIS · provenance violation |
| `judge_layer_skipped` | Composite computed from rule layer only · no judge inference | JELLY · re-bench required |
| `deed_minted_below_jelly` | Deed issued on a PROPOLIS-classified bench run | PROPOLIS · governance violation |

## Scoring Impact

- **assignment_success**: HIGH · the bench IS the agent's report card
- **repair_lift**: INDIRECT · bench failures route to SwarmFixer for refinery
- **validator_confidence**: HIGH · deed-bearing agents carry validator-backed quality attestation
- **risk_temperature**: INVERSE · bench-attested agents lower customer's deployment risk
- **probability_of_close**: HIGH · auditor-acceptable attestation drives enterprise deals
- **evidence_strength**: HIGH · documented pack + Tribunal verdict = strongest evidence class
- **cost_to_mint**: MEDIUM · bench run cost + deed cost · ~$5-50 per run depending on pack size

## Deed / Receipt Impact

- **Receipt fields touched**: `agentbench.run_id` · `pack_name` · `pack_version` · `composite_score` · `axes_scores` · `classification` · `deployment_tier`
- **DDEED class impact**: produces `DDEED-DOV-AGENT-<agent-slug>-<seq>-v<n>` · the agent's first deed is the chain's genesis · subsequent deeds chain by `parent_deed_id`
- **Books and records layer**: L1 PostgreSQL (bench run) → L2 Merkle (verdict tree) → L4 Hedera HCS (deed anchor) → L5 ENS (per-agent pointer at `<agent>.<operator>.defendable.eth`)
- **5 Proofs touched**: ORIGIN (which agent, which pack version) · QUALITY (the 5-axis scoring) · PROCESS (the per-task verdict lineage) · TRUST (Tribunal verdict + Hedera anchor + ENS pointer)

## Related Terms

- [defendableos](defendableos.md) · parent platform
- [defendablerouter](defendablerouter.md) · required for in-traffic bench validation
- [clawcheck](clawcheck.md) · the lighter intake · AgentBench is the deeper bench
- [defendablehack](defendablehack.md) · bench results can drive bounty submissions
- [pair-candidate](../repair_terms/pair-candidate.md) · bench tasks become pair candidates

## Example

> **Customer**: ACMECorp · books-bot agent
>
> **Workflow**:
> 1. Submit endpoint `https://api.acmecorp.com/books-bot/v1` + scoped auth + scope declaration (read GL + write journal entries)
> 2. Jr Hack confirms scope · pack version `compute_inspector_v1:v1.0-alpha`
> 3. AgentBench runs 6 tasks + 3 adversarial cases against endpoint
> 4. Tribunal grades each: 4 HONEY · 4 ROYAL_JELLY · 1 JELLY · 0 PROPOLIS
> 5. Composite computed: capability 22/25 · truth 17/20 · safety 19/20 · numeric/structural 11/15 · efficiency 7/10 · reproducibility 9/10 = 85/100 · classification ROYAL_JELLY
> 6. Deployment tier: OBSERVED (pack alpha-status cap applied · cannot claim higher)
> 7. Deed minted: `DDEED-DOV-AGENT-ACMECORP-BOOKS-BOT-000001-v1` · record_hash `sha256:8c4e...d3a1` · anchored on Hedera HCS · ENS at `books-bot.acmecorp.defendable.eth`

## DefendableOS Notes

- AgentBench was the MVP that produced the first live agent deed `DDEED-DOV-AGENT-COMPUTE-INSPECTOR-000001-v1` on 2026-05-23
- The pack-alpha tier cap is honest framing · we don't let early-stage pack runs claim mature deployment tiers · this is what auditors trust
- The 5-axis scoring is constitutional · changing the axes or weights requires a doctrine PR · NOT a config flip
- AgentBench feeds AdversarialPack candidates · failures in benching become pack additions for future runs
- Re-benching is encouraged · the agent's quality drifts with model upgrades · the deed lineage shows the trajectory

🐝 *Submit your agent. The Tribunal grades. The deed attests. Auditor-acceptable.*
