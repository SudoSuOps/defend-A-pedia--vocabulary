# SwarmFixer Doctrine · The Agent Refinery

> *"The deed is only as good as the fix it delivers."*
>
> — Founder charter

---

## What SwarmFixer is

SwarmFixer is the **agent refinery**. It is not a chatbot. It is not a model wrapper. It is the production layer that takes a failed or low-grade agent output · diagnoses it · repairs it · prevents the next occurrence · detects the failure class · and compares the repair against the original. Five tasks. One refinery. Receipted end-to-end.

In CRE terms: SwarmFixer is the **rehab crew on a value-add deal**. Tenant moved out · roof is leaking · HVAC is shot · rent roll is half-empty. You don't tear the building down. You diagnose what's broken · scope the repair · do the work · re-lease the space · and the comps show a cap rate compression and a NOI lift. That lift is what makes the deal pencil. **Repair Lift is the NOI of the agent economy.**

SwarmFixer runs on a trained model · **SwarmJelly-4B** · deployed at `whale:11434`. Cooked in-house on a 125,000-pair corpus organized as a 7-failure-mode × 5-RJ-task taxonomy. **TEMP locked at 0.05.** The model is licensed open-weights · open the books · the customer can host it on their own HoneyBox if they want · we still get paid on the deeds.

---

## The 5-task Royal Jelly output

When a pair candidate flows into SwarmFixer, it MUST exit with a structured 5-task output. Not 4. Not 6. Five. If any task is missing or below confidence threshold, the pair stays in `pending/` and re-routes.

1. **DIAGNOSE** · root cause analysis. Names the failure mode (one of 7 · see below) · assigns severity 1-5 · recommends an action. This is the broker's pre-listing inspection · what's actually broken · how bad is it · what does it cost to fix.
2. **REPAIR** · the corrected output. Step-by-step recovery from the failure state to a Honey-grade answer. This is the GC's punch list · what gets done · in what order · to what spec.
3. **PREVENT** · the trigger condition + check logic + remediation. A rule that, if it had existed yesterday, would have stopped today's failure. This is the title insurance · the policy that prevents the same defect from showing up at the next closing.
4. **DETECT** · positive/negative classification with evidence. Given a new input, does it look like THIS failure class? Yes/no + the evidence that says so. This is the smoke alarm · cheap to run · loud when it fires.
5. **COMPARE** · ranked outputs scored on 4 dimensions (correctness · completeness · format compliance · reasoning depth). Was the repair actually a lift? By how much? On what axes? This is the appraisal · the comp · the before/after pic that proves the rehab worked.

All five tasks together are a **Royal Jelly Record**. One record. One hash. One deed. The customer doesn't buy a "fix." They buy a Royal Jelly Record.

---

## The 7-failure-mode taxonomy

Every failure that enters the refinery gets bucketed into one of 7 modes. The taxonomy is locked. No mode = no pair = no training data = no fix. If a Hack can't bucket the failure, it escalates to a Sr Hack before SwarmFixer runs.

| # | Mode | What it looks like |
|---|---|---|
| 1 | `HALLUCINATION` | Agent fabricated a fact · cited a non-existent source · invented a tool output |
| 2 | `SCHEMA_DRIFT` | Agent output doesn't match the contract · wrong fields · wrong types · missing required keys |
| 3 | `TOOL_MISUSE` | Agent called the wrong tool · called the right tool with wrong args · ignored a tool result |
| 4 | `INSTRUCTION_FAILURE` | Agent ignored or partially obeyed the user/system prompt · drifted from scope |
| 5 | `REASONING_GAP` | Logic chain breaks · math is wrong · step skipped · conclusion doesn't follow from premises |
| 6 | `SAFETY_VIOLATION` | Agent emitted unsafe content · leaked secret · bypassed guard · executed forbidden action |
| 7 | `LATENCY_REGRESSION` | Agent took > 2× expected wall-time · burned > 2× expected tokens · timed out |

**The 25% distribution cap** · No single mode may exceed 25% of the training corpus. The 125K-pair refinery enforces this at intake. Why? Because the model overfits to whatever dominates · and the customer's real-world traffic doesn't look like an unbalanced training set. The cap forces breadth. The cap is non-negotiable.

---

## The TEMP 0.05 RULE · the production doctrine

This is the LOCKED operational rule. Engrave it in the cook scripts. Engrave it in the runtime configs. Engrave it in the on-call runbook.

> **TEMP = 0.05 for any SwarmFixer inference call. Period. No exceptions.**

The production evidence:

| Temperature | Honey rate | Propolis rate | Notes |
|---|---|---|---|
| 0.7 (default) | **0.7%** | 88% | Catastrophic · model drifts · format breaks · taxonomy ignored |
| 0.3 | 11% | 64% | Better but still unreliable · 1-in-9 Honey is not a refinery |
| 0.1 | 71% | 14% | Good but not production · still misses the contract sometimes |
| **0.05** | **93.9%** | 3% | Production rate · the locked setting |
| 0.0 | 92% | 3% | Marginally worse · loses tie-breaking diversity on the COMPARE task |

This is not a tuning preference. This is **a constitutional setting**. A 0.05 SwarmFixer inference is what the deed represents. A 0.7 SwarmFixer inference is **not a SwarmFixer inference** · it's a different model · it doesn't get to issue a Royal Jelly Record · the validator chain rejects it on Check C03 (model-config compliance).

If you run hot, you're not running SwarmFixer. You're running a research notebook.

---

## AgentHash · the 5 failure buckets observed in the wild

The 7-mode taxonomy is the training axis. **AgentHash** is the runtime-observation axis · how agent failures actually surface in production. Five buckets. Mapped from the Gemma corpus · validated against 90 days of Tribunal verdicts.

| Bucket | What goes wrong | Example |
|---|---|---|
| `STOP` | Agent halts when it should continue | refuses a benign task · hits a fake guardrail · exits on partial result |
| `CALL` | Agent calls the wrong thing | wrong tool · wrong endpoint · wrong sub-agent · wrong model |
| `READ` | Agent reads wrong / misreads | wrong file · stale context · skips the system prompt · misinterprets a flag |
| `RECOVER` | Agent fails to recover from a fixable error | one tool error → full task abandonment · no retry logic · no fallback |
| `LOOP` | Agent loops without progress | same call repeated · same reasoning step repeated · burns tokens for no lift |

Every SwarmFixer DIAGNOSE task MUST tag the AgentHash bucket as well as the 7-mode taxonomy class. Two axes. One verdict. Cross-tagged data trains a better refinery.

---

## ClawHash · the 6 sub-algorithms for adversarial input

When the failure is adversarial · not accidental · the diagnosis routes through **ClawHash**. Six sub-algorithms. Each one a defense pattern against a specific attack class.

| # | Sub-algorithm | Defends against |
|---|---|---|
| 1 | `injection` | Prompt-injection · jailbreak · system-prompt override |
| 2 | `toolpoison` | Tool-result poisoning · adversarial doc returned by retrieval |
| 3 | `rce` | Remote code execution attempts · shell escapes · sandbox break |
| 4 | `supply` | Supply-chain attacks · poisoned model · poisoned dependency |
| 5 | `sandbox` | Container/jail escape · privilege escalation · lateral movement |
| 6 | `audit` | Audit-log tampering · receipt forgery · timestamp manipulation |

Each ClawHash sub-algorithm applies the **4-step defense pattern**:

1. **detect** · pattern-match the adversarial signal
2. **refuse** · short-circuit the unsafe path
3. **complete** · give the user the safe partial result + the reason for the refusal
4. **log** · write the event to the audit ledger · feed the AdversarialPack v.next

This 4-step pattern is what makes the refusal **defendable** vs **rude**. We don't just say no. We say no · here's why · here's what you CAN have · and it's all on the receipt.

---

## The 3 service tiers

SwarmFixer ships in three tiers. Same model. Same TEMP 0.05. Different surface · different SLA · different price.

### Tier 1 · Self-serve · $99-$499/mo

Customer wires their pipeline to the SwarmFixer API. They send failed pairs. They get 5-task Royal Jelly Records back. They wire the records into their own re-training loop. No managed service · no Sr Hack · no Fix-or-Refund. Brokerage-grade DIY. For mature ML teams who just want the refinery.

### Tier 2 · Managed · $2K-$10K/mo

We run the loop. We watch the dashboards. We do the weekly check. We surface pattern flags · escalate Propolis spikes · ship the AdversarialPack updates · tune the routing. Brokerage-grade managed service. For ops teams who want defense without staffing it.

### Tier 3 · Embedded · $50K-$250K ARR · 90-day Fix-or-Refund

We embed. The Sr Hack sits in the customer's Slack. We co-own the agent's quality bar. We commit to a measurable Repair Lift target in 90 days · with refund if we miss. This is the broker-grade flagship · the deal that compounds · the relationship that becomes a 5-year deed lineage. Sold to ownership · not procurement.

> The Fix-or-Refund is the killer clause. Nobody else in AI ships a refundable guarantee on a falsifiable lift number. We do. Because we have the receipts.

---

## How it ties to the rest of DefendableOS

- **Pair candidates** flow in from DefendableRouter (the write-only middleware) · graded by Tribunal · routed by classification.
- **Honey-tier pairs** get archived directly · they're already good.
- **Jelly-tier pairs** route to SwarmFixer · this is the refinery's primary input.
- **Propolis-tier pairs** route to the AdversarialPack pipeline · SwarmFixer may participate (PREVENT + DETECT tasks generate adversarial test cases).
- **Repaired pairs** re-enter Tribunal · if Repair Lift ≥ 0.10 and validator confidence ≥ 0.6 · they transition to `jelly-repaired/` · if not · they re-route or quarantine.
- **DDEED-DOV-REPAIR** is the deed class issued on every successful Royal Jelly Record · anchored on Hedera HCS · ENS-resolvable at `swarmdeed.eth`.

The refinery never sits in the customer's production call path. We grade in the shadows. We deliver overnight. The customer's agents run free during the day · the refinery runs hot at night · the Morning Reconciliation Brief shows up at 6am with the night's lift number.

---

## Read next

- [`12_defendablerouter_doctrine.md`](12_defendablerouter_doctrine.md) · the write-only middleware that feeds SwarmFixer
- [`../playbooks/swarmfixer_repair_playbook.md`](../playbooks/swarmfixer_repair_playbook.md) · the operator workflow
- [`../vocabulary/repair_terms/swarmfixer.md`](../vocabulary/repair_terms/swarmfixer.md) · the term file
- [`../vocabulary/repair_terms/swarmjelly.md`](../vocabulary/repair_terms/swarmjelly.md) · the model behind the refinery
- [`../vocabulary/defendableos_terms/temp-five-cent-rule.md`](../vocabulary/defendableos_terms/temp-five-cent-rule.md) · the LOCKED setting

---

🐝 *The refinery is the moat. The lift is the receipt. The deed is only as good as the fix it delivers.*
