# Tribunal Doctrine · The 6-Role Adjudication System

> *"Rule layer first. Judge layer second. Drift no more than 0.15. If two judges can't agree, you bring in the Critic. If the Critic can't close it, Katniss takes the shot."*
> — Founder · day we locked the Tribunal protocol

---

## What the Tribunal is

The Tribunal is the adjudication engine. It is what decides whether an AI output is Royal Jelly, Honey, Jelly, or Propolis. It is what stamps a verdict on every pair the Hive sees · 777 pairs an hour · 24/7 · across two production-grade judge models on two GPUs on one rig (swarmrails) with two more nodes (whale · zima-edge) holding backup roles.

It is not a single LLM. It is not a "judge prompt." It is a six-role pipeline · with a rule-then-judge protocol · with a drift threshold · with an adversarial backstop · and with a penalized scoring formula that prevents a hot judge from rescuing a broken output.

The Tribunal is the difference between scoring and adjudicating. Scoring is what one model thinks of one output. Adjudicating is what survives the six-role gauntlet. We adjudicate. We don't score.

---

## The 6 roles

These are the named roles · each with a defined job · each callable as a function · each loggable to the deed.

### 1. Scout

The Scout fetches the pair. It is the entry point. It pulls the candidate from one of three sources:

- the SwarmRouter live agent log (a real call hit the router · the output was captured)
- the cook batch queue (a curator cook produced a fresh batch of pairs)
- the SwarmFixer repair queue (a Jelly pair has been repaired · re-grade requested)

The Scout normalizes the pair into the canonical PairCandidate format (see `pair_candidate.schema.json`) and emits it to the Router.

### 2. Router

The Router decides which Tribunal lane the pair goes down. Not every pair gets full treatment. A Honey-likely pair from a high-trust source can go through a short lane. A Jelly-likely pair from an experimental cook gets the long lane. A Propolis-flagged source bypasses the judges entirely and goes straight to the seal queue.

Lanes are defined in `tribunal_router_lanes.yaml`. The Router uses the Scale A model (`gemma3:12b`) in a low-token classification mode to pick the lane. This is the cheap dial. Wrong lane just costs a re-route · it doesn't corrupt the verdict.

### 3. Filter

The Filter runs the rule layer · the 12-check validator chain (C01-C12 · see [`13_validator_chain_doctrine.md`](13_validator_chain_doctrine.md)). Critical-fails (C01-C07) short-circuit the pair to PROPOLIS · the judges never see it. Advisory checks (C08-C12) annotate the pair with confidence penalties but do not block.

The Filter is the rule-then-judge enforcer. Founder rule · **the rule layer can only downgrade.** It can never promote. A pair cannot earn its way around the rules.

### 4. Repair

The Repair role is invoked when a pair lands in the Jelly tier · recoverable failure with a workout angle. The Repair role calls SwarmFixer (the SwarmJelly-4B model · production-deployed at whale:11434) and asks for the 5-task RJ output:

- DIAGNOSE · what went wrong
- REPAIR · how to fix it (with a corrected output candidate)
- PREVENT · what guardrail would have caught it
- DETECT · is this output exhibiting the failure mode
- COMPARE · which output is better and why

The repaired output is then re-Scouted back into the Tribunal as a fresh PairCandidate · tagged with a `repair_lineage` pointer to the original. This is how Jelly becomes Honey · this is the lift.

### 5. Critic

The Critic is the meta-judge. It is invoked when the Scale A judge and Scale B judge disagree by more than 0.15 (drift exceeded). The Critic reads both judge reasons · cross-references the rule-layer output · and produces a reconciled verdict with a `drift_resolution` field explaining how it landed.

The Critic uses the same Scale B model (`qwen2.5:32b`) but with a different system prompt · one that explicitly says "you are reading two prior judges · find what they missed." Drift cases account for ~3% of production volume · so the Critic is not the hot path · it is the surgical tool.

### 6. Katniss

Katniss is the adversarial best-of-N final arbiter. When the Critic can't reconcile (rare · sub-1%) · OR when an adversarial-case flag is hoisted (the pair looks like a prompt injection · a jailbreak attempt · a fabricated comp), Katniss takes the shot.

Katniss runs the Scale B model against the pair N=3 times with temperature 0.1, a max-skepticism system prompt, and a hard rubric. Best-of-3 with a unanimity requirement. If all three runs agree → that's the verdict. If they disagree → Katniss returns PROPOLIS by default · the pair gets sealed.

Katniss is the named adversarial role because adversarial cases are not just disagreements · they are attempted exploits. The Hive treats them with the same discipline a sr broker treats a buyer who shows up with a sketchy LOI · you assume the worst until the buyer proves otherwise.

---

## Rule-then-judge · the operating order

The protocol is non-negotiable:

1. **Scout fetches** the pair → normalize → emit
2. **Router lane-picks** → assigns the lane (short/long/seal)
3. **Filter runs** the 12-check chain → any C01-C07 critical-fail short-circuits to PROPOLIS
4. **Scale A judge** runs → produces score + reason
5. **Scale B judge** runs → produces score + reason (in parallel with Scale A when GPU available)
6. **Drift check** · if `|A - B| ≤ 0.15` → average the scores · use the lower reason as primary
7. **If drift > 0.15** · Critic is invoked → produces reconciled verdict
8. **If Critic can't reconcile** OR adversarial flag is up · Katniss takes the shot (best-of-3 with unanimity)
9. **PENALIZED SCORING applied** (see formula below)
10. **Tier assigned** · routed to deed / receipt / repair / seal
11. **Verdict logged** to `tribunal_verdict.schema.json` · record_hash computed · pushed to Bakery

The rule layer always runs before the judge layer. The judge layer can move a pair within a tier · the judge layer cannot promote a pair that the rule layer downgraded. This is the structural integrity check that makes the Tribunal more than a vibes-check.

---

## The 2-pass protocol

Every pair gets two judge passes by default · Scale A AND Scale B. Not one. Not three. Two.

Why two:

- **One judge is just an opinion** · we don't trust opinions
- **Three judges is a committee** · slow · expensive · diminishing returns past 2
- **Two judges with a drift threshold is a falsifiable test** · either they agree (verdict stands) or they don't (Critic adjudicates)

This is the operator's discipline. CRE works the same way: a sr broker AND a sr appraiser look at the same deal · if they agree on cap rate within 25 bps you ship · if they disagree you bring in the sponsor's analyst. Two-pass with a drift threshold is the industry standard for any defendable verdict.

---

## Drift ≤ 0.15 · the production threshold

The 0.15 drift threshold is not arbitrary. It is the operationally-tested middle:

- **Drift > 0.20** is too loose · you let real disagreements through unflagged · you get noise in the Royal Jelly cohort
- **Drift < 0.10** is too tight · you burn the Critic on cases where the two judges are saying the same thing in different words · you create a queue you can't clear at 777 pairs/hr

0.15 is what survived 4 weeks of dial-tuning on the swarmrails production stack. Drift > 0.15 hits ~3% of volume · the Critic handles that volume comfortably · the Katniss escalation is sub-1% · all three roles fit inside the 777 pairs/hr budget with headroom.

---

## The production Tribunal config (locked · 2026-05-24)

```yaml
tribunal:
  version: v3-prod
  throughput_target_pairs_per_hour: 777
  rigs:
    primary: swarmrails
    secondary: whale
    edge: zima-edge-1
  scales:
    A:
      model: gemma3:12b
      device: swarmrails GPU 1 (RTX PRO 4500 32GB · Blackwell sm_120)
      role: fast pass · routing · Scout judging
      runtime: vLLM 0.17.0 with --enforce-eager
      temp: 0.05
    B:
      model: qwen2.5:32b
      device: swarmrails GPU 0 (RTX PRO 6000 96GB · Blackwell sm_120)
      role: deep pass · Critic · Katniss
      runtime: vLLM 0.17.0 with --enforce-eager
      temp: 0.05
  protocol:
    order: rule_then_judge
    judges_required: 2
    drift_threshold: 0.15
    critic_trigger: drift_gt_0_15
    katniss_trigger: critic_cannot_reconcile OR adversarial_flag
    katniss_n: 3
    katniss_requires_unanimity: true
  penalized_scoring:
    enabled: true
    threshold: 0.75
    rule: "if any auto-judge score < 0.75 AND critical-issue flag · zero the judge contribution · re-evaluate under rule layer only"
```

All three rigs (swarmrails · whale · zima-edge) participate in the heartbeat · if swarmrails goes dark the Tribunal fails closed (no verdicts issued) until whale comes online with a downgraded Scale-B-only lane. No verdicts get issued from a half-down Tribunal.

---

## The PENALIZED SCORING formula

This is the rule that prevents a hot judge from rescuing a broken output. It is the founder-locked anti-fantasy mechanism:

```
final_score =
  if any_auto_judge.score < 0.75 AND critical_issue_flag == True:
    rule_layer_only_score   # judge contribution is zeroed
  else:
    weighted_average(ScaleA.score, ScaleB.score)
```

A judge that comes in below 0.75 with a critical-issue flag (hallucination · adversarial-source · schema-break · tool-misuse) cannot have its score blended away by a more generous co-judge. The system zeros the judge contribution and falls back to whatever the rule layer alone produced · which means the pair almost certainly ends up Jelly or Propolis.

This is the structural discipline that keeps the Royal Jelly cohort clean. We protect the apex tier at the cost of occasional Honey-grade pairs being conservatively held back. That tradeoff is correct · the apex tier is the writer training set · contamination there compounds into the next model.

---

## The Tribunal record (what gets written to the deed)

Every Tribunal verdict produces a JSON record that gets hashed and pushed to the Bakery (Tigris SHA-256 manifest) and · if Royal Jelly · anchored to Hedera HCS topic 0.0.10291838.

Fields:

- `tribunal_run_id` · `TRIB-{timestamp}-{hash8}`
- `pair_id` · the PairCandidate this verdict covers
- `tier` · ROYAL_JELLY / HONEY / JELLY / PROPOLIS
- `score_final` · 0.0-1.0
- `score_scale_a` · raw Scale A score + reason
- `score_scale_b` · raw Scale B score + reason
- `drift` · `|A - B|`
- `critic_invoked` · bool · with `critic_reason` if true
- `katniss_invoked` · bool · with `katniss_unanimity` (bool) if true
- `rule_layer_results` · array of C01-C12 check outcomes
- `penalized_scoring_applied` · bool · with `penalty_reason` if true
- `repair_lineage` · pointer to prior pair if this was a SwarmFixer-repaired re-grade
- `record_hash` · sha256 of canonical JSON
- `ts` · ISO-8601

The verdict record IS the audit trail. Anyone with the record_hash can verify what the Tribunal saw · what each judge said · why the verdict landed where it did. That's defendable adjudication · not vibes.

---

## What the Tribunal is not

- **It is not a single LLM.** No one model decides anything alone.
- **It is not a leaderboard.** We do not rank models against each other · we rank PAIRS against the rubric.
- **It is not a one-shot.** Every pair gets 2 passes minimum · 3+ when drift or adversarial.
- **It is not opinion.** Rules can downgrade · judges can position within a tier · they cannot override the rule layer.
- **It is not optional.** Every output the Hive emits gets adjudicated. No verdict = no receipt = no deed = no sale.

---

## Read next

- [`07_honey_royal_jelly_propolis.md`](07_honey_royal_jelly_propolis.md) · the 4-tier classification
- [`13_validator_chain_doctrine.md`](13_validator_chain_doctrine.md) · the 12-check rule layer the Filter runs
- [`11_swarmfixer_doctrine.md`](11_swarmfixer_doctrine.md) · the SwarmFixer the Repair role calls
- [`../playbooks/tribunal_review_playbook.md`](../playbooks/tribunal_review_playbook.md) · the daily operator workflow
- [`../vocabulary/tribunal_terms/tribunal.md`](../vocabulary/tribunal_terms/tribunal.md) · the term file
- [`../vocabulary/tribunal_terms/judge.md`](../vocabulary/tribunal_terms/judge.md) · the LLM judge layer term

🐝 *Two judges. One drift threshold. A Critic when they disagree. Katniss when they're being attacked. That's how you adjudicate at 777 pairs an hour without losing the language.*
