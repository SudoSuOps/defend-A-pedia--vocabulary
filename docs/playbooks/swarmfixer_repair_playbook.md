# SwarmFixer Repair Playbook

> *"You don't get paid on the diagnosis. You get paid on the lift."*
>
> — Sr Hack rule

This playbook is the operator workflow for running pair candidates through SwarmFixer. Read it once before you touch the refinery. Reference it every day after.

---

## Audience

- Jr Hacks on intake duty (route the pair · don't touch the model)
- Sr Hacks on adjudication (read the 5-task output · decide bucket · mint or reject)
- On-call operators handling Propolis spikes (re-feed the loop · escalate to AdversarialPack)
- Embedded operators on Tier-3 customer engagements (defend the 90-day Fix-or-Refund SLA)

---

## Pre-flight · what must be true before you push a pair into SwarmFixer

1. The pair has a Tribunal verdict and the verdict is `JELLY` (not `HONEY` · not `PROPOLIS` · not `pending`). Honey pairs don't need repair. Propolis pairs route to the AdversarialPack pipeline first.
2. The pair carries an AgentHash bucket tag (`STOP` · `CALL` · `READ` · `RECOVER` · `LOOP`). If untagged, run the DETECT-only pass first and tag manually before the full refinery run.
3. The pair carries an EvidenceStrength score ≥ 0.4. Below 0.4, the input is too thin to repair · the diagnosis would be a hallucination of a hallucination. Re-route to evidence-gathering.
4. The pair carries the agent's ENS identity (`<agent>.<operator>.defendable.eth`). Without ENS, the eventual deed has no parent · the chain breaks.
5. SwarmJelly-4B is up at whale:11434 · `curl whale:11434/api/tags` returns 200 · the model tag is `swarmjelly-4b:v1.2` or current production tag.
6. The runtime TEMP is **0.05**. Read the env. Read the config. Read the request payload. If any of the three reads ≠ 0.05, ABORT. Run the TEMP check skill before retrying.

---

## The 7-step refinery loop

### Step 1 · Intake

```
INPUT  : pair_candidate.json (Tribunal-graded JELLY · tagged · ENS'd · evidence ≥ 0.4)
OUTPUT : queue entry in pending/ with run_id ag-fix-<utc-ts>-<short-hash>
ACTOR  : Jr Hack
SLA    : within 30 minutes of Tribunal JELLY verdict
```

Drop the pair into `pending/` with a `run_id`. Log the AgentHash bucket and the 7-mode pre-classification (if known). If unknown, leave the field null · the DIAGNOSE task will fill it.

### Step 2 · Trigger SwarmFixer

```
INPUT  : pending/<run_id>.json
OUTPUT : 5-task Royal Jelly Record draft (in jelly_drafts/<run_id>.json)
ACTOR  : SwarmJelly-4B at whale:11434 · TEMP=0.05
SLA    : ≤ 90 seconds wall-time for a single pair · ≤ 30 min for a batch of 100
```

The trigger is a single POST. The 5-task prompt template lives in `docs/prompts/swarmfixer_5task.md`. Use the canonical template. Don't paraphrase.

### Step 3 · Validator review of the 5-task output

```
INPUT  : jelly_drafts/<run_id>.json
OUTPUT : validator_chain_result.json + draft Royal Jelly Record (annotated)
ACTOR  : Validator chain (12 checks · 7 critical + 5 advisory)
SLA    : within 5 minutes of draft generation
```

The validator chain runs the 12-check sweep. Critical checks include:

- C01 · schema compliance · the 5 tasks present · correct types · required fields
- C02 · TEMP compliance · model config = 0.05 · no override on the request
- C03 · taxonomy compliance · DIAGNOSE.mode ∈ the 7-mode taxonomy · DIAGNOSE.agenthash ∈ the 5 buckets
- C04 · evidence binding · REPAIR cites the input evidence · doesn't fabricate sources
- C05 · format compliance · COMPARE returns 4-dim scoring · ranked outputs
- C06 · confidence floor · every task has a confidence ∈ [0,1] · no task < 0.50
- C07 · no critical safety violation surfaced in the repair itself

Pass all 7 critical = proceed. Fail any 1 critical = re-route (see Step 7).

### Step 4 · Re-bench · run the REPAIRED output through Tribunal

```
INPUT  : draft Royal Jelly Record · REPAIR task output
OUTPUT : new Tribunal verdict + new composite score for the repaired output
ACTOR  : Tribunal (rule layer + judge layer · same as original grading)
SLA    : within 10 minutes
```

This is the **lift measurement**. Tribunal scores the REPAIR task's output as if it were a fresh agent submission. We compare against the original failed pair's score.

### Step 5 · Compute Repair Lift

```
repair_lift = repaired_composite_score - original_composite_score
```

This is the dial that decides the bucket. The threshold is locked:

- `repair_lift ≥ 0.10 AND validator_confidence ≥ 0.6` → **transition to `jelly-repaired/`**
- `0.0 ≤ repair_lift < 0.10` → **back to `pending/`** for a second pass (max 2 retries)
- `repair_lift < 0.0` (regression) → **route to `propolis-failures/`** · this is a refinery failure · flag for AdversarialPack v.next

The lift is the NOI of the agent economy. CRE analogy: you bought a building at a 6-cap, did the rehab, re-leased it at a 5-cap · the lift IS the deal. No lift, no deal. Negative lift, you blew it.

### Step 6 · Mint the deed (on `jelly-repaired/` transitions)

```
INPUT  : Royal Jelly Record + Tribunal lift + validator chain pass
OUTPUT : DDEED-DOV-REPAIR-<agent>-<seq>-v<n> · anchored on Hedera HCS · ENS pointer updated
ACTOR  : Deed minter (services/edge-agent · cost ~$0.0052/deed)
SLA    : within 15 minutes of jelly-repaired transition
```

The deed is the customer asset. It carries all 5 Proofs. It's resolvable at `<deed-slug>.swarmbee.defendable.eth`. It's verifiable by the customer · their auditor · their insurance carrier · without asking us.

### Step 7 · Re-route on failure

If Step 3 fails any critical check, OR Step 5 shows `repair_lift < 0.10` after 2 retries, route as follows:

| Failure mode | Route to |
|---|---|
| Schema/format broken (C01/C05) | `pending/` after fixer-prompt patch |
| TEMP wrong (C02) | ABORT · escalate · this is a runtime bug · don't run more pairs |
| Taxonomy violation (C03) | `pending/` with mode override + Sr Hack note |
| Evidence fabrication (C04) | `quarantined/` · this is a model regression signal |
| Confidence floor (C06) | `pending/` for 1 retry · if 2nd fails · `quarantined/` |
| Safety violation (C07) | `propolis-failures/` · escalate to AdversarialPack within 24h |
| Negative lift after 2 retries | `propolis-failures/` · this is a defense gap · the pair becomes a training case |

---

## The 6 buckets (pair candidate lifecycle)

Every pair flows through these 6 buckets. The bucket IS the state. There is no separate state machine. The folder is the truth.

| Bucket | Meaning | Exit criteria |
|---|---|---|
| `pending/` | Awaiting refinery run OR retry | Successful Steps 2-5 with lift ≥ 0.10 |
| `honey/` | Already Honey-grade · no refinery needed | Direct to archive · feeds positive training data |
| `jelly/` | Tribunal-classified JELLY · needs refinery | Picked up by Step 1 within 30 minutes |
| `jelly-repaired/` | Refinery succeeded · lift ≥ 0.10 · validator pass · deed minted | Archived as Royal Jelly Record |
| `propolis-failures/` | Refinery failed OR original was Propolis · feeds AdversarialPack | Becomes adversarial test case in next pack version |
| `quarantined/` | Suspected model regression · fabrication detected · safety event | Sr Hack review within 4 hours · no auto-route |

---

## Weekly check · the operator rhythm

Sr Hacks run the weekly check every Monday morning · pre-9am. Read against the prior 7 days of refinery runs.

- **Throughput** · how many pairs entered `jelly/` · how many transitioned to `jelly-repaired/`
- **Lift distribution** · mean lift · median · p10 · p90 · any negative-lift drift
- **Bucket flow** · what % of pairs cleared on first pass · what % needed retry · what % quarantined
- **Taxonomy distribution** · check the 25% cap on the 7-mode taxonomy · re-balance the training set if any mode exceeds
- **AgentHash distribution** · which bucket dominated the week · what does it tell us about the customer's agent fleet
- **ClawHash hits** · how many adversarial events · which sub-algorithms fired · adversarial pack candidates
- **Customer-facing lift report** · the Morning Reconciliation Brief that ships at 6am Monday includes the prior week's aggregate lift number · this is the customer's KPI

---

## Tier-3 embedded checklist (Fix-or-Refund · 90-day SLA)

When you're embedded on a Tier-3 engagement, the Fix-or-Refund clause changes the rhythm. Every weekly check feeds the SLA receipt.

- Day 0-7 · baseline measurement · capture the customer's pre-refinery agent fleet quality
- Day 7-30 · first refinery cycle · build the AgentHash distribution · ship first Royal Jelly Record cohort
- Day 30-60 · iterate · tune the 7-mode prompt templates to the customer's failure shape · measure lift trend
- Day 60-90 · prove the lift · the agreed-on KPI must show ≥ X% improvement (X is in the SLA · typically 15-30%)
- Day 90 · the receipt · the deed lineage proves the lift OR triggers the refund

The refund is unconditional. We don't argue. We ship the receipt that says we missed · we wire the money back · we keep the relationship. Most customers don't take the refund · they re-up. But the OPTION is what made the contract sign.

---

## Read next

- [`honey_jelly_propolis_playbook.md`](honey_jelly_propolis_playbook.md) · the daily classifier playbook
- [`../doctrine/11_swarmfixer_doctrine.md`](../doctrine/11_swarmfixer_doctrine.md) · the refinery doctrine
- [`../vocabulary/repair_terms/pair-candidate.md`](../vocabulary/repair_terms/pair-candidate.md) · the unit that flows through
- [`../vocabulary/repair_terms/repair-lift.md`](../vocabulary/repair_terms/repair-lift.md) · the dial that decides the bucket

---

🐝 *No lift, no deed. The refinery proves itself on receipts, not on slides.*
