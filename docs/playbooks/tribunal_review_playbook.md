# Tribunal Review Playbook · The Daily Tribunal-Runner Workflow

> *"You're not grading. You're adjudicating. Two judges. One drift threshold. If they fight, you bring in the Critic. If the Critic blinks, Katniss takes the shot. And if the deal smells wrong, you PASS."*
> — Sr broker desk-side, day-one Tribunal training

---

## Who this playbook is for

The Tribunal Runner. The operator who sits desk-side and watches the verdict queue. Could be a sr broker on the dial · could be a sr hack on rotation · could be the founder during an apex cook. Anyone with the badge to approve a verdict override · seal a propolis pair · escalate a drift case to the Critic. This is the desk manual.

If you are a jr broker, read this once for context and then bring questions to the sr. You do not approve overrides yet. You log · you observe · you learn the queue rhythm.

---

## The daily rhythm

### 06:00 · Morning Brief

The Morning Reconciliation Brief lands in your inbox by 06:00. It is a single page. The fields you read first:

- **Volume last 24h** · total pairs adjudicated. Target ~18,000-19,000 (777 pairs/hr × 24h with maintenance slack).
- **Tier distribution** · what % landed Royal Jelly · Honey · Jelly · Propolis. Healthy production looks like: RJ 35-55% · Honey 25-40% · Jelly 10-20% · Propolis 5-15%. If RJ is below 30% something is upstream-broken · if RJ is above 60% the judges are running hot and you should suspect a temp drift.
- **Drift events** · how many pairs hit `|A - B| > 0.15` and triggered the Critic. Target sub-3% of volume.
- **Katniss invocations** · sub-1%. If you see 5+ in a day · something is being attacked or a cook is fundamentally broken.
- **C01-C07 critical-fail counts** · per check. Any check above 2% of volume is degraded mode · investigate immediately.
- **C07 holdout-contamination alerts** · this is the paging-event line. If non-zero · stop everything and walk through the contamination-response checklist.
- **Repair queue depth** · pairs sitting in `pair-candidates/jelly-repaired/` waiting for SwarmFixer. Healthy depth is < 500. Above 1,000 · SwarmFixer is bottlenecked · check whale:11434.

### 06:15 · The five-minute scan

Open the Tribunal dashboard (`swarmandbee.ai/chain` or local equivalent). Five-minute eyeball pass:

1. Are the rigs green? swarmrails GPU 0 + GPU 1 + whale + zima-edge heartbeat.
2. Is the verdict-per-second rate above 0.15? (Target throughput = 777/hr ≈ 0.215/sec.)
3. Are there any pairs older than 4 hours sitting in the queue without a verdict? Those are stuck · investigate.
4. Is the Bakery hash-write queue draining? (Tigris manifests should be 100% caught up overnight.)
5. Is the Hedera anchor queue draining? (Royal Jelly deeds should anchor within 15 minutes of issue.)

If any of these are red · skip the rest of the playbook and walk the SRE checklist first. The Tribunal cannot adjudicate from a half-down rig.

### 06:30 · The override queue

This is the day's first real work. Pull the override queue · the pairs from the prior 24h where a sr broker (or you) flagged an advisory fail for review.

Each override entry shows:

- the pair (full PairCandidate JSON · displayed in the dashboard)
- the verdict the Tribunal produced
- the advisory check(s) that fired
- the operator notes (if any)
- the proposed override action (typically `accept_with_annotation` · `force_downgrade` · `reseal_as_propolis`)

You read every entry. You apply the PASS doctrine ruthlessly · if the override is asking you to look past a real fail · you PASS · you do not approve. The Hive does not deed fantasy.

### 07:00-12:00 · The live floor

Live Tribunal volume is hitting at ~0.215 pairs/sec. You do not adjudicate every pair · the system adjudicates · you adjudicate the EXCEPTIONS:

- **Drift > 0.15 cases** (~3% volume) · the Critic produces a reconciled verdict · your job is to spot-check Critic verdicts when the dashboard shows you a `critic_low_confidence` flag
- **Katniss invocations** (~sub-1%) · every Katniss verdict gets sr-broker eyes BEFORE the deed writer accepts it · this is non-negotiable
- **C07 contamination alerts** · if any fire · you stop the cook · audit the batch
- **Repair queue stalls** · if SwarmFixer hasn't returned a repair within 30 minutes · you escalate to the rig owner

### 12:00 · Midday check

- Tier distribution still healthy?
- Override queue caught up?
- Any new C07 alerts since 06:00?
- Repair queue depth stable?
- Royal Jelly deeds anchoring to Hedera on time?

### Afternoon · the deep work

Use the afternoon for the work the queue doesn't surface:

- review the prior week's PASS-rate (how often we PASSed on a Tribunal verdict · should be 2-5%)
- spot-check 20 random Royal Jelly deeds end-to-end (you sample-audit your own pipeline · CRE discipline)
- read the prior day's Propolis vault for patterns (recurring hallucination triggers · adversarial source clusters · schema-break frequency)
- update the holdout manifest if a new eval is being prepped
- coach the jr brokers on what you saw in the queue

### 18:00 · Evening close-out

- Drain the override queue · no overrides carry into the next day
- Confirm the Bakery manifest is fully written
- Confirm Hedera anchoring is current
- Send the close-out note to the team Discord · what shipped · what didn't · what's open

---

## When verdicts conflict · drift > 0.15

The protocol is locked. You don't improvise.

### Step 1 · The Critic has already run

If you are looking at a drift case in the dashboard, the Critic has ALREADY produced a reconciled verdict. Your job is NOT to redo the Critic's work. Your job is to read the `drift_resolution` field and decide if the Critic's reasoning holds.

### Step 2 · Read both judge reasons

The dashboard shows you Scale A reason · Scale B reason · Critic reason side-by-side. Read all three. Look for:

- Is one judge anchored on a real-world fact the other missed?
- Did one judge fall for a surface form (formatting · length · tone) while the other read the substance?
- Is the disagreement actually about the same thing · or are they grading different aspects?

### Step 3 · Accept · escalate · or PASS

Three actions available:

- **Accept the Critic's verdict** · the most common path · the Critic is usually right · click through and the deed writer picks it up
- **Escalate to Katniss** · if the Critic's verdict still feels off · if the reasoning is thin · if you smell adversarial intent · invoke Katniss (best-of-3 with unanimity)
- **PASS** · if the pair stinks · if you wouldn't sign your name to either verdict · seal the pair as Propolis with `operator_pass_doctrine` annotation. You are protecting the apex cohort.

Never · ever · override a Critic verdict UPWARD without invoking Katniss. The whole point of the chain is that no human reaches around the rules. You can downgrade with a PASS · you cannot promote.

---

## When to call Critic + Katniss manually

The Tribunal calls Critic and Katniss automatically. There are also manual-invoke buttons in the dashboard. Use them when:

### Manual Critic invoke

- You see a verdict that landed inside the drift threshold (so the Critic didn't auto-trigger) but the two judges are clearly disagreeing in their REASONS even though their SCORES are close (this is the "right answer for the wrong reason" problem)
- A jr broker has flagged a pair for review and your gut says the Tribunal got it wrong but you can't articulate why · Critic produces an explicit reconciliation that you can read

### Manual Katniss invoke

- A pair is from a NEW source · a source the Hive has not seen before · adversarial-source-flag is on by default but the score came in high · Katniss confirms or denies
- A customer-facing deed (the highest-stakes lane · the ones that go in the Closing Statement) · you may choose to Katniss-confirm every Royal Jelly verdict before it ships in the Closing Statement · this is operator discretion · costs energy · buys insurance
- The pair touches a regulated domain (medical · legal · financial) and the deed will be cited in a customer compliance report · Katniss-confirm is cheap insurance

Manual invokes are logged · audited · counted in the weekly check. Operator discretion is not unbounded · if you are Katniss-invoking on 10% of volume something is upstream-broken.

---

## When to escalate to a human (and which human)

The Tribunal IS a human-in-the-loop system at the override level · but some events require additional humans:

| Trigger | Escalate to | How fast |
|---|---|---|
| C07 holdout contamination alert | Founder + Sr Hack 1 (CRE Doctrine) + cook owner | Immediately · stop the cook |
| Same advisory check failing > 5% of volume for 24h | Sr Hack 3 (Tribunal Architect · me · in this playbook context · in real ops: whoever owns the Tribunal) | Same day |
| Katniss returns PROPOLIS on > 3 pairs in 1 hour | Sr broker + Sr Hack 4 (SwarmFixer) | Within the hour · suspect adversarial campaign |
| Bakery hash-write queue is backed up > 1000 pairs | Sr Hack 2 (Vocab Infra) + whoever owns Tigris | Same day |
| Hedera anchor queue stalled > 30 minutes | Sr Hack 6 (QA Validator) + Hedera ops | Within the hour |
| Customer reports a deed they don't recognize | Sr broker + founder | Immediately · pull the record · verify hash · walk the audit |
| Repair queue depth > 1000 for > 2 hours | Sr Hack 4 (SwarmFixer) + rig owner | Within 2 hours · whale:11434 likely needs restart |
| Any judge returning identical scores across batches | Sr Hack 3 · check temperature drift first | Same day · likely a temp config slipped above 0.05 |

Escalation is logged · timestamped · linked to the triggering record_hash. The escalation log is itself a Bakery manifest entry. Every page is auditable.

---

## PASS doctrine application · the Tribunal-side rules

The PASS doctrine comes from the founder's CRE practice · refuse fantasy mandates · let competitors burn the seller · come in clean afterward. Inside the Tribunal it means:

### When you PASS on a verdict

You are saying: this pair MIGHT be Honey or Royal Jelly according to the auto-judges · but the underlying engagement / source / customer-fit is so wrong that promoting it would corrupt the books. Seal it as Propolis with `operator_pass_doctrine` annotation and a reason string.

Examples of operator-PASS:
- The pair grades well but the source is a vendor we've blacklisted (e.g., a known-bad ScamFeed)
- The output is technically correct but answers a question we should not be answering for this customer (out-of-scope)
- The pair grades Royal Jelly but the engagement that produced it is one we never should have opened (the customer was a tire-kicker · the cook ate $400 in compute to produce nothing we want to deed)

### When you do NOT PASS

You do not PASS to manage politics. You do not PASS because a customer would prefer a different answer. You do not PASS because the verdict makes a partner look bad. PASS is for protecting the books · not for managing relationships.

If you find yourself wanting to PASS for a non-doctrine reason · escalate to the founder · do not adjudicate alone.

### PASS rate as a health metric

A healthy PASS rate is 2-5% of verdicts touched in override review. Below 1% · you are not exercising discretion (the chain is doing all the work and that's actually OK · but spot-check yourself). Above 8% · something is wrong upstream · either the cooks are producing junk that the auto-judges aren't catching, or the customer pipeline is bringing in deals we shouldn't be opening.

---

## What you log · always

Every action you take in the Tribunal dashboard writes a row to `tribunal_operator_log.jsonl`. Fields:

- `operator_id` · your handle
- `action` · `accept_critic` / `escalate_katniss` / `pass_doctrine` / `force_downgrade` / `manual_invoke_critic` / etc.
- `pair_id` · the pair touched
- `verdict_before` · what the Tribunal returned
- `verdict_after` · what shipped
- `reason` · free-text · MANDATORY · explain why
- `ts` · timestamp

The log feeds the weekly check. Sr brokers and the founder read the log. Patterns get coached. This is the curator-as-manager loop.

---

## What you do NOT do

- You do NOT edit the verdict JSON by hand · ever
- You do NOT bypass the validator chain · ever
- You do NOT promote a verdict upward without invoking Katniss · ever
- You do NOT silence a C07 contamination alert · ever
- You do NOT operate without the Morning Brief · if it didn't land · find out why before touching the queue
- You do NOT skip the close-out · the queue starts the next morning at zero

---

## Read next

- [`08_tribunal_doctrine.md`](../doctrine/08_tribunal_doctrine.md) · the 6-role Tribunal spec
- [`13_validator_chain_doctrine.md`](../doctrine/13_validator_chain_doctrine.md) · the 12-check chain
- [`07_honey_royal_jelly_propolis.md`](../doctrine/07_honey_royal_jelly_propolis.md) · what each verdict tier means
- [`11_swarmfixer_doctrine.md`](../doctrine/11_swarmfixer_doctrine.md) · the repair pipeline you feed
- [`../vocabulary/tribunal_terms/tribunal.md`](../vocabulary/tribunal_terms/tribunal.md) · the term file
- [`../vocabulary/tribunal_terms/judge.md`](../vocabulary/tribunal_terms/judge.md) · the LLM judge layer

🐝 *Run the queue. Trust the chain. Apply the PASS. Log every action. The Tribunal protects the books · the operator protects the Tribunal.*
