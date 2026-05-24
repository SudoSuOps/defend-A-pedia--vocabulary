# Judge

> *"The judge is the LLM that scores the pair. Scale A fast pass · Scale B deep pass. Both required · neither alone is the verdict. Two judges agreeing within 0.15 drift is the foundation of every Honey deed we ship."*
> — Founder · day the typed-tool contract was locked

## Street Definition

"What did the judges return?" The judge is the LLM layer inside the Tribunal · the part that produces a JellyScore (0-1) and a reason string on each PairCandidate. Two judges run on every pair · Scale A (`gemma3:12b` on swarmrails GPU 1) and Scale B (`qwen2.5:32b` on swarmrails GPU 0). The judges produce STRUCTURED OUTPUT through a typed `record_tribunal_verdict` tool contract · NOT free-text. Free-text judge outputs are rejected at parse time · the discipline is structural.

In CRE language · the judge is the appraiser · the role that produces a numeric valuation with a reasoning narrative. Two appraisers on the same deal is the discipline that protects against single-appraiser bias. Same here · two judges with a drift threshold protect against single-model bias.

## CRE Operator Meaning

In CRE · the judge maps to the licensed appraiser · the role that produces the appraisal opinion · the cap rate · the value range · with the reasoning narrative attached. A high-stakes deal gets two appraisers (one selected by buyer · one by lender) · their values are reconciled within a tolerance · disagreements outside tolerance trigger a third appraisal. Same exact pattern. Two judges · drift threshold (0.15 score units) · Critic for reconciliation · Katniss for adversarial.

## DefendableOS Definition

A judge is an LLM agent invoked by the Tribunal Filter (after the validator chain clears critical) to produce a JellyScore on a PairCandidate. Two judges run per pair:

### Scale A judge
- Model: `gemma3:12b`
- Rig: swarmrails GPU 1 (RTX PRO 4500 32GB Blackwell sm_120)
- Runtime: vLLM 0.17.0 with `--enforce-eager`
- Temperature: 0.05 (per the temp-doctrine · NEVER 0.7)
- Role: fast pass · routing classification · light Auditor lanes
- Throughput contribution: ~165 tok/s concurrent

### Scale B judge
- Model: `qwen2.5:32b`
- Rig: swarmrails GPU 0 (RTX PRO 6000 96GB Blackwell sm_120)
- Runtime: vLLM 0.17.0 with `--enforce-eager`
- Temperature: 0.05
- Role: deep pass · Critic invocations · Katniss invocations
- Throughput contribution: ~88 tok/s concurrent

Both judges output through the typed `record_tribunal_verdict` tool contract:

```json
{
  "tool": "record_tribunal_verdict",
  "args": {
    "pair_id": "string",
    "jelly_score": "float 0.0-1.0",
    "reason": "string (1-2 sentences · operator-readable)",
    "failure_mode": "enum or null (one of 7 SwarmJelly classes if failure detected)",
    "hallucination_event": "boolean",
    "adversarial_source_flag": "boolean",
    "critical_issue_flag": "boolean (triggers penalized scoring)"
  }
}
```

Free-text outputs are rejected at parse time · 180s timeout per judge invocation · `tool_choice=auto` is respected (Kimi quirk: temperature must be exactly 1 for some Kimi variants but our gemma + qwen production models use 0.05).

## Backend Representation

```json
{
  "judge.judge_id": {
    "type": "string",
    "pattern": "^BEE-AUDITOR-JUDGE-(A|B)-[a-z0-9]+$"
  },
  "judge.scale": {
    "type": "enum",
    "values": ["A", "B"]
  },
  "judge.model": { "type": "string" },
  "judge.rig": { "type": "string" },
  "judge.jelly_score": { "type": "float", "range": [0.0, 1.0] },
  "judge.reason": { "type": "string" },
  "judge.failure_mode": {
    "type": "enum",
    "nullable": true,
    "values": ["missing_step", "false_assumption", "hallucination", "overgeneralization", "drift", "schema_break", "tool_misuse"]
  },
  "judge.hallucination_event": { "type": "boolean" },
  "judge.adversarial_source_flag": { "type": "boolean" },
  "judge.critical_issue_flag": { "type": "boolean" },
  "judge.latency_ms": { "type": "integer" }
}
```

Schema files: `docs/schemas/tribunal_verdict.schema.json` · `docs/schemas/judge_invocation.schema.json`

## Client Explanation

"The judges" are the AI models inside our Tribunal that produce a numeric score (JellyScore 0-1) and a reasoning narrative on every AI output we ship. Two judges run on every pair · Scale A is our fast pass · Scale B is our deep pass. If they agree within a tight threshold (0.15 score units) the verdict stands. If they disagree, we invoke a Critic to reconcile. If the case looks adversarial, we invoke Katniss for a best-of-three. Every deed you receive carries both judge scores and both judge reasons in its record.

## Jr Broker Use

The jr broker reads judge output but does not adjudicate independently:

1. Every pair gets two judge passes within ~5 seconds · both scores visible in dashboard
2. If Scale A and Scale B agree within 0.15 · the verdict stands · proceed
3. If they disagree by > 0.15 · the Critic auto-invokes · wait for the Critic verdict
4. If `critical_issue_flag` is true on either judge · the penalized scoring formula applies · the pair drops to rule-layer-only score (often Jelly or Propolis)
5. NEVER manually edit a judge score · NEVER paraphrase a judge reason · they are structural · their record_hash is verifiable

**Rule of thumb**: the judges produce structured output · the structure is the discipline · respect the chain.

## Sr Broker Use

The sr broker watches judge behavior as a SYSTEM-CALIBRATION GAUGE:

- Judge score distribution per cook · Scale A and Scale B should look similar in shape · divergence in distributions = calibration drift · investigate
- Judge reason quality · spot-audit 10 random Honey verdicts · the reasons should cite specific aspects of the pair · generic reasons ("looks good" · "scores well") indicate the judge is degraded
- Judge temperature drift is the #1 cook-degradation cause · production temp is 0.05 · if a cook's outputs become bimodal (high RJ + high Propolis · little Honey) suspect temp drift FIRST
- Critic invocation rate · healthy is ~3% · sustained above 8% means the two judges are systematically disagreeing · investigate which is drifting
- Katniss invocation rate · healthy is sub-1% · sustained above 3% = either an attack campaign or a fundamental cook problem · escalate

## Tribunal Use

```yaml
tribunal_use:
  classification_impact: []   # the judges don't get a tier · they ASSIGN tiers
  rule_layer_checks:
    - Both Scale A AND Scale B judges MUST produce a structured verdict (C04)
    - Either judge raising hallucination_event triggers C05 critical fail
    - Either judge raising adversarial_source_flag triggers Katniss invocation
    - Either judge with critical_issue_flag AND score < 0.75 triggers penalized scoring
  judge_layer_prompt_hint: "you are one of two judges · be conservative on apex tier · use the typed tool contract · do not free-text"
  can_be_critical_failure: false   # judges don't fail · they DETECT failures · validator chain detects judge-pipeline failures
```

## Evidence Required

To consider a judge verdict valid:

- A judge_id (links to auditor-bee lineage)
- A scale (A or B)
- A model identifier (one of the approved fleet · `gemma3:12b` or `qwen2.5:32b` in production)
- A jelly_score in [0.0, 1.0]
- A reason string (1-2 sentences · operator-readable · MANDATORY)
- The four flag booleans (failure_mode · hallucination_event · adversarial_source_flag · critical_issue_flag)
- A latency_ms reading
- Output via the typed `record_tribunal_verdict` tool contract (NOT free-text)

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **judge_freetext_output** | Judge returned free-text instead of structured tool call | Rejected at parse · pair re-routed to judge · if recurring · judge prompt audited |
| **judge_timeout** | Judge did not respond within 180s | Pair re-routed to alternate rig · if both judges timeout · pair held · escalate |
| **judge_temp_drift** | Judge producing degraded outputs · suspect temperature config slipped above 0.05 | Restart vLLM with correct temp · audit recent verdicts |
| **judge_silent_pass** | Judge returned high score but reason is generic / does not justify the score | Operator spot-audit catches it · pair re-routed for re-judge · if recurring · judge model audited |
| **judge_unanimous_pass_adversarial** | Both judges scored adversarial pair as HONEY · the chain missed the adversarial-source flag | Critical integrity event · update adversarial-source watchlist · re-train judge prompts |

## Scoring Impact

- **assignment_success**: PRIMARY DRIVER · the judge score IS the assignment success metric (once chain has cleared)
- **repair_lift**: MEASUREMENT · the lift is computed by comparing the judge score before and after repair
- **validator_confidence**: PARTIAL · validator confidence aggregates chain + judge confidence
- **risk_temperature**: PER-PAIR · judge-flagged adversarial pairs spike risk
- **probability_of_close**: HEAVY · judge scores predict customer-acceptable close rates
- **evidence_strength**: WEIGHTED · judges weight evidence per the 5-component JellyScore formula
- **cost_to_mint**: DIRECT · judge GPU compute is a major line item in cost-to-mint (~$0.002-0.005 per pair)

## Deed / Receipt Impact

- **Receipt fields touched**: `judge.scale_a.score` · `judge.scale_a.reason` · `judge.scale_b.score` · `judge.scale_b.reason` · `judge.drift` · `judge.penalized_scoring_applied`
- **DDEED class impact**: NO DDEED issues without TWO judge verdicts (Scale A + Scale B)
- **Books and records layer**: L1 PG (judge results hot) · L2 Merkle (judge results in batch root) · L3 NAS (judge invocation log archived)
- **5 Proofs touched**: QUALITY (judges PRODUCE the quality score) · PROCESS (judge invocation lineage IS process) · ORIGIN (judge model + rig is part of origin)

## Related Terms

- [tribunal](tribunal.md) · the parent system the judges run within
- [validator](validator.md) · the rule-layer role that runs BEFORE the judges
- [validator-chain](validator-chain.md) · the 12-check chain the judges run after
- [hallucination-event](hallucination-event.md) · the named class of failure judges flag
- [assignment-success](assignment-success.md) · the dial the judge scores feed
- [confidence-weight](confidence-weight.md) · the dial judge consistency feeds

## Example

> **Engagement**: STNL opinion · cold storage · Atlanta MSA.
>
> **Judge invocations**:
>
> **Scale A** · BEE-AUDITOR-JUDGE-A-4f02 · gemma3:12b on swarmrails GPU 1 · temp 0.05 · latency 1,847ms
> - record_tribunal_verdict tool call returned:
>   - jelly_score: 0.89
>   - reason: "comp set well-anchored from EDGAR-cited tenant credit walk · all 3 industrial comps within 25 bps of submarket median · re-trade math arithmetically clean"
>   - failure_mode: null
>   - hallucination_event: false
>   - adversarial_source_flag: false
>   - critical_issue_flag: false
>
> **Scale B** · BEE-AUDITOR-JUDGE-B-9c11 · qwen2.5:32b on swarmrails GPU 0 · temp 0.05 · latency 4,221ms
> - record_tribunal_verdict tool call returned:
>   - jelly_score: 0.91
>   - reason: "depth high · 5 trajectory keywords present at appropriate nest levels · numeric verification ties at 4 decimal places · would prefer one additional source on the tenant credit notes but not blocking"
>   - failure_mode: null
>   - hallucination_event: false
>   - adversarial_source_flag: false
>   - critical_issue_flag: false
>
> **Drift**: 0.02 (within 0.15 threshold) · no Critic invoked · JellyScore averaged to 0.90 · tier ROYAL_JELLY.

## DefendableOS Notes

- The two-judge requirement is doctrine · one judge is opinion · two judges with a drift threshold is adjudication
- Scale A is gemma3:12b · Scale B is qwen2.5:32b · these are the production-locked models · model swaps require Tribunal-config version bump and sr broker sign-off
- The typed tool contract is non-negotiable · free-text judges are rejected · this is the structural-discipline that makes verdicts parseable and verifiable
- Temperature 0.05 is the production setting · 0.7 is the cook-degradation killer · documented in the SwarmJelly temp doctrine · violation produces Pollen-heavy corpora
- The judges run INSIDE the Tribunal · the Tribunal owns the verdict · individual judge scores are visible but the verdict is the Tribunal's product

🐝 *Two judges. Typed tool contract. Temperature 0.05. Drift threshold 0.15. The judges score · the Tribunal adjudicates · the chain protects both.*
