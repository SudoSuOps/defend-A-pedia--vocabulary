# Hive Doctrine

> *"Biology = architecture = product."*
> — Swarm-Hive Genesis (2026-03-12)

The Hive is the architectural metaphor. The Hive is also the literal architecture. The Hive is also the product. Three things, one structure. The founder did not pick "bees" because it was cute · he picked it because the biology already solved the problem we are solving: how does a swarm of independent workers produce a single high-quality, defensible output, repeatedly, at scale, in adversarial conditions?

The answer in biology is the same as the answer in DefendableOS: specialization · pipeline · gates · classification · finality.

---

## The Bee Agent lifecycle · seven stages

Every Bee Agent in the Swarm executes the same seven-stage lifecycle. Same on the smallest Jetson edge node. Same on the 27B SwarmHoney model. Same on a customer's per-agent ledger. The pipeline is constitutional.

```
FETCH  →  COOK  →  GATE  →  SCORE  →  STAMP  →  ANCHOR  →  EMIT
```

Each stage has a single responsibility. Each stage produces an output the next stage consumes. Each stage is independently testable, independently receipted, independently auditable. The Bee that completes all seven stages cleanly produces Honey. The Bee that fails any stage produces Jelly (recoverable) or Propolis (critical · adversarial · trust-break).

---

### Stage 1 · FETCH

**The Bee pulls the signal.** Raw input from the customer's workflow · a refund decision request, a CRE underwriting task, a medical-claim review, a logistics dispatch. The signal arrives unverified, untyped, in whatever shape the upstream system emits.

**Receipt fields touched.** `fetch_at`, `fetch_source`, `fetch_payload_hash`, `fetch_size_bytes`.

**Failure modes.** Source unreachable. Payload corrupted. Schema unrecognized. Schema-drift from upstream vendor. These fail the Bee at stage 1 · trigger a Jelly verdict if recoverable, escalate to Propolis if the source itself is compromised.

**Doctrine rule.** No transformation in FETCH. Pure capture. Any transformation logic moves to COOK.

---

### Stage 2 · COOK

**The Bee processes the signal.** The model runs. The reasoning chain executes. The tools get called. The candidate output is produced. This is where the actual AI work happens · everything else is plumbing or governance.

**Receipt fields touched.** `model_id`, `model_version`, `cook_started_at`, `cook_completed_at`, `cook_token_count`, `cook_energy_wh`, `cook_cost_usd`, `cook_output_payload_hash`.

**Failure modes.** Model timeout. OOM. Token-budget exhaustion. Tool failure mid-chain. Cold model · drifted weights · staled prompt template. Each gets a typed failure code that the GATE stage reads.

**Doctrine rule.** The COOK output is provisional · never published, never billed, never user-facing until it clears GATE.

---

### Stage 3 · GATE

**The Bee runs the deterministic gates.** Six gates from Swarm-Hive Genesis · plus the 7th adversarial gate. JSON validity. Output length. Numeric verification. Concept presence. Dedup. Degeneracy check. Then the adversarial probe: does the output survive a hostile re-prompt with the same task?

**Receipt fields touched.** `gates_passed[]`, `gates_failed[]`, `gate_results.json_valid`, `gate_results.numeric_verify`, `gate_results.adversarial_passed`.

**Failure modes.** Any failed gate flags the output. Multiple failed gates trigger automatic Propolis classification before the SCORE stage even reads it. The gates are non-negotiable · they are the rule layer.

**Doctrine rule.** Gates are deterministic. No judge opinion. No model reasoning. Pure rule. If a gate fails, it fails. The judge in SCORE doesn't get to overrule a gate · only the sr broker can, on documented escalation.

---

### Stage 4 · SCORE

**The Bee runs the Tribunal.** Scale A judge (gemma3:12b) and Scale B judge (qwen2.5:32b) both score the output against the named rubric. Drift between the two judges must be ≤ 0.15 or the output escalates for sr broker review. The verdict drops the output into one of four classes: Honey · Royal Jelly · Jelly · Propolis.

**Receipt fields touched.** `tribunal_scale_a_score`, `tribunal_scale_b_score`, `tribunal_drift`, `tribunal_verdict`, `jellyscore`, `tribunal_reasoning_a_hash`, `tribunal_reasoning_b_hash`.

**Failure modes.** Drift > 0.15. Both judges fail to render verdict. Rubric mismatch (the score asked for a rubric the model doesn't carry). All flagged · all escalated.

**Doctrine rule.** Rule-then-judge. The rule layer (gates) can downgrade or critical-fail · the judge layer cannot upgrade a rule-fail. Composite score is shorthand · the 5 grades are the truth · never published without all 5.

---

### Stage 5 · STAMP

**The Bee stamps the receipt.** Canonical JSON form. SHA-256 hash. The receipt becomes immutable at this stage · any modification creates a new receipt with a new hash, never alters the existing one.

**Receipt fields touched.** `receipt_id` (DCLAW-{cell_hash}-{timestamp}), `record_hash`, `canonical_json_size_bytes`, `stamp_at`.

**Failure modes.** Canonicalization drift (JSON key ordering off, whitespace off, number precision off). This is a P1 doctrine violation · all 7 senior hacks notified.

**Doctrine rule.** Canonical JSON is the dictionary's hash form. The dictionary's hash form is what the books-and-records anchor. Drift here breaks the entire 5-layer finality stack. Zero tolerance.

---

### Stage 6 · ANCHOR

**The Bee anchors to the public ledger.** Merkle batch (50 receipts) gets a root computed. Root gets published to Hedera HCS topic 0.0.10291838. ENS subdomain provisioned for the deed. The receipt is now publicly verifiable by any third party with the deed ID.

**Receipt fields touched.** `merkle_root`, `merkle_index_in_batch`, `hedera_topic_id`, `hedera_sequence_number`, `hedera_consensus_at`, `ens_subdomain`, `ens_resolved_at`.

**Failure modes.** Hedera anchor latency > 15 min. ENS resolution failure. These are P1 incidents in the books-and-records SLA · see [`04_books_and_records_doctrine.md`](04_books_and_records_doctrine.md).

**Doctrine rule.** The receipt is not "complete" until L4 + L5 land. Until then, it is in-flight · counted in pipeline metrics, not in retained deeds.

---

### Stage 7 · EMIT

**The Bee delivers the output.** To the customer system. To the dashboard. To the Morning Brief queue. To the SwarmJelly training pipeline (if JELLY-tier). To the customer's auditor system (if scheduled). The emission is the only customer-facing artifact · everything else is back-of-house.

**Receipt fields touched.** `emit_destinations[]`, `emit_at`, `emit_payload_hash`, `emit_acknowledgment_at`.

**Failure modes.** Customer endpoint unreachable. Acknowledgment timeout. These get retried on backoff and logged · but the receipt is already final at STAMP. EMIT failure does not invalidate the verdict · it just delays delivery.

**Doctrine rule.** Emission is observable to the customer. The Morning Brief includes emission status. Anything chronically delayed becomes a sit-down conversation, not a silent failure.

---

## The three Bee classes

The pipeline above is universal · but Bees specialize. Three classes, each with a job. Same lifecycle, different focus, different deployment density.

### Scout Bees

**The first responders.** Scout Bees do FETCH and COOK on novel signals. They are the agents we point at new domains, new customer fleets, new vertical workflows where we don't yet have a curated rubric. Scouts produce mostly Jelly-tier output initially · which is intentional · because Scout output becomes the seed corpus for the next Curator cook.

**Where they run.** Edge nodes. Cheap inference. High throughput, low precision. The Scout is the first ten dials of any new market.

**What they're judged on.** Coverage. Did they pull the signal cleanly? Did they cook a draft? Did they surface the right ambiguity to escalate to a Worker?

**CRE analog.** The jr broker on day one in a new market · making dials, building first-pass color, surfacing what's interesting to the sr broker. Scouts are the M of MAGIC · Meetings, broadly defined.

---

### Worker Bees

**The production line.** Worker Bees run the established pipeline for the established customers. They are the agents in production · scoring the live customer workflow · producing the Honey · feeding the dashboard. Workers carry the bulk of the daily throughput.

**Where they run.** Mixed deployment · Jetson edge for low-latency tasks, 9B-27B mid-tier for reasoning tasks, 27B+ for adversarial-resistant tasks. Workers are deployed by task profile, not by model size.

**What they're judged on.** Honey production rate. Drift between Scale A and Scale B judges. Repair-lift contribution (do their JELLY pairs improve the next training cycle?). Energy economics.

**CRE analog.** The seasoned jr broker carrying their own listings under sr broker oversight. The Worker is the A of MAGIC · Appraisals, fully done.

---

### Auditor Bees

**The Tribunal arm.** Auditor Bees do not produce customer output. They consume Worker output and Scout output, run the Tribunal rubrics, run the validator chain, score the receipts, surface critical failures. The Auditor is the firm's adversarial layer · the one that catches what the Worker missed.

**Where they run.** Always on the highest-precision available model in the rubric class. Tribunal Scale A is gemma3:12b · Scale B is qwen2.5:32b · Auditors include both, plus the adversarial probe layer that runs 7th-gate stress tests on randomly sampled outputs.

**What they're judged on.** False-positive rate (flagging Honey as Propolis incorrectly) AND false-negative rate (passing Propolis as Honey). Both are equally bad. Auditor performance is itself audited by the sr broker on a weekly cadence.

**CRE analog.** The sr broker doing the appraisal review · the title officer doing the chain-of-title check · the closing agent verifying every line of the closing statement before the deed goes to the county. Auditors are the I and C of MAGIC · Ink and Close.

---

## Why biology · why bees

Three reasons the metaphor earns its place. Not aesthetic. Operational.

**1. Specialization is the only way to scale a pipeline.** A hive doesn't have one bee doing everything. It has Scouts for novelty, Workers for production, Auditors (yes, real-life "guard bees" exist) for defense. Trying to build a single super-agent that does all three is the failure mode every monolithic AI startup is currently learning the hard way.

**2. The output is a graded substance.** Honey isn't a binary. Honey has grades, viscosities, vintages. Real apiarists grade their honey. We grade our Honey. Royal Jelly is the apex grade · only the queen-tier output earns it. Propolis is the protective resin · in our world, it is the adversarial / flagged class because in nature it's what the bees use to seal the hive against intrusion. The metaphor is doing real cognitive work · not decoration.

**3. The receipts model is biological.** A bee returns from a foraging run, performs the waggle dance to communicate the source's value and location to the hive, and the hive collectively evaluates. Our Tribunal is the waggle dance, formalized into deterministic gates and dual-judge scoring. The model is older than software · it has been load-tested for millions of years.

---

## The four-tier classification · the Honey grade

| Tier | Score | Description | CRE asset analog |
|---|---|---|---|
| **Royal Jelly** | ≥ 0.85 (or 95+) | Apex · production-grade · deed-ready · queen feed | Class A · 5-cap · prime · irreplaceable |
| **Honey** | 0.70 - 0.84 | Production-safe · validator-approved · ship | Class B · adequate · replaceable |
| **Jelly** | repair-candidate | Recoverable failure · feeds SwarmFixer training | Workout · distressed · re-leasable |
| **Propolis** | critical | Adversarial · hallucinated · trust-break · sealed | Class C · bad neighborhood · do not list |

Royal Jelly is rare on purpose. If too much output qualifies as Royal Jelly, the rubric is too generous · we tighten. The discipline is what makes Royal Jelly valuable. Same way a CRE broker doesn't list every property as Class A · doing so destroys the grading system's information value.

---

## How the doctrine becomes product

The Bee lifecycle becomes the per-task receipt. The Bee classes become the per-agent deployment profile. The Honey grade becomes the per-output classification. The pipeline becomes the customer's defense workflow. The biology is the architecture is the product.

When a customer signs an LOU, they are buying:
- A fleet of Scouts, Workers, and Auditors right-sized to their workflow
- A 7-stage lifecycle running on every defensive action
- A 4-tier classification grading every output
- A 5-layer finality stack receipting every grade

That's the product. Wrapped in the biology because the biology is what makes it scale.

---

## What this doctrine prevents

- **Monolithic agent architecture.** You can't ship one super-Bee that does everything. The biology forbids it · the doctrine enforces it.
- **Hidden pipeline stages.** Every stage is explicit, named, receipted, auditable. No black-box "and then magic happens" steps.
- **Ungraded output.** Every output gets a class · Honey, Royal Jelly, Jelly, or Propolis. No "unclassified" bucket. No "we're still figuring out how to grade this." The grading is the gate.
- **Auditor-as-afterthought.** The Auditor Bees are first-class · same lifecycle, same deployment, same investment. Defense is the brand · the Auditor is how it scales.

---

## Read next

- [`07_honey_royal_jelly_propolis.md`](07_honey_royal_jelly_propolis.md) · the 4-tier classification in full
- [`08_tribunal_doctrine.md`](08_tribunal_doctrine.md) · the 6-role adjudication system
- [`11_swarmfixer_doctrine.md`](11_swarmfixer_doctrine.md) · what happens to JELLY pairs

🐝 *The Hive verifies before it issues. What the Hive verifies becomes truth.*
