# 14 · Assignment Success Doctrine

> *"When a job IS the job · we say so · in writing · with receipts. Anything less is a fantasy mandate."*
>
> — Founder · in the pit · 2026-05-24

---

## Why this doctrine exists

In CRE · "did the assignment close" is a binary. Either the building changed hands or it didn't. Either we collected the fee or we didn't. There's no soft-edge on a HUD-1 closing statement. The number is real or it isn't.

In AI · the industry has spent two years pretending success is a gradient · a "vibe" · a launch tweet. We reject that. DefendableOS treats every engagement like a CRE assignment · with a defined success boundary · a documented success grade · and a closing statement that names exactly where we landed.

This doctrine answers four questions every client deserves a straight answer on:

1. **When is the assignment complete?**
2. **How do we grade the work?**
3. **What does failure look like · in writing?**
4. **What's the lifecycle from intake to closing?**

If a sr broker can't answer these on a Tuesday morning call · we haven't earned the listing.

---

## Definition

An **Assignment** is a specific job within a signed **Engagement**. The engagement is the relationship (signed via LOU). The assignment is the work order (signed via assignment brief). One engagement holds many assignments over its life · just like one client relationship at a CRE shop holds many trades over the years.

**Assignment Success** is the formal Tribunal-graded verdict that the assignment delivered against its written success criteria. It is a boolean (`success: true | false`) accompanied by a 5-grade breakdown that explains WHY.

The boolean is what gets reported to the principal. The 5-grade breakdown is what gets filed in books-and-records. Both are mandatory. Neither can be skipped.

---

## When a job IS the job

The success criteria for every assignment are written into the **assignment brief** at intake. The brief is signed by the principal · countersigned by the sr broker · stored alongside the LOU in the client folder. The criteria are SPECIFIC · MEASURABLE · TIME-BOUND · and AUDITABLE.

A success criterion looks like this:

> *"By 2026-06-15 · the refund agent at company.refund001.acme.defendable.eth must process ≥ 1,200 refund decisions with a Tribunal Honey rate ≥ 92% and zero Propolis events on the 17-item adversarial pack. Cost-to-mint ceiling: $0.011/decision."*

That's a job. The boundary is named. The number ties out or it doesn't. When the assignment closes · the closing statement reports the actual numbers against the contracted numbers. The variance is the truth.

A criterion that looks like this is **NOT** a job:

> *"Improve the refund agent."*

That's a fantasy mandate. We PASS on those. Every time. The PASS doctrine is non-negotiable.

---

## The 5-grade breakdown

Every assignment carries a 5-grade verdict. The composite is a shorthand. The 5 grades are the truth. Never publish a composite without all 5 grades visible alongside it.

| Grade | Weight | What it measures |
|---|---|---|
| **G1 · Outcome** | 30% | Did the assignment hit its written success criteria? Numeric variance vs contract. |
| **G2 · Truth** | 25% | Were the outputs accurate · sourced · non-hallucinated? Tribunal Truth-class verdicts on a sampled cohort. |
| **G3 · Safety** | 20% | Did the agent fleet stay in alignment? Zero Propolis events on critical paths · adversarial pack pass rate. |
| **G4 · Economics** | 15% | Did the cost-to-mint stay under the contracted ceiling? Energy · model spend · validator chain throughput. |
| **G5 · Defensibility** | 10% | Are the receipts complete · the deeds anchored · the books-and-records audit-clean? End-to-end lineage check. |

The composite score is `0.30·G1 + 0.25·G2 + 0.20·G3 + 0.15·G4 + 0.10·G5`.

A grade of **G3 < 70** OR **any Propolis event on a critical path** caps the assignment at FAILED regardless of the composite. Safety is the floor · not a weighting.

---

## The four boolean outcomes

The boolean is reported on the closing statement. It's one of four values:

- **CLOSED · HONEY** · composite ≥ 0.85 · all 5 grades ≥ 0.70 · zero critical failures · the asset performed
- **CLOSED · CONDITIONED** · composite ≥ 0.70 · 4 of 5 grades passing · we delivered with named caveats
- **FAILED · RECOVERABLE** · composite 0.50-0.69 · the work is repair-candidate · SwarmFixer can salvage it
- **FAILED · DARK** · composite < 0.50 OR critical Propolis · the engagement is paused · the principal is briefed within 24 hours · the recovery plan is on the table within 72

Every closing statement names the outcome in the first line. Plain English. No hedge. If we shipped CONDITIONED · we say CONDITIONED. If we went dark · we say dark. We don't dress it up.

---

## What failure looks like

The industry runs from failure naming. We name it · because that's what brokers do at closing tables · and that's what makes the relationship survive past the trade.

A FAILED · DARK outcome triggers:

1. **Same-day principal call.** Founder on the phone if the principal asks. No deflection.
2. **Failure deed issued.** `DDEED-{org}-FAIL-{slug}-{seq}` · same 5 Proofs · the failure is receipted just like a success.
3. **Repair plan within 72 hours.** Diagnosed root cause · proposed lift · cost-to-repair estimate · revised timeline.
4. **Optional fee abatement.** Per the Fix-or-Refund 90-day clause in the LOU. The principal decides.
5. **Permanent training pair.** The failure feeds SwarmFixer's Jelly corpus. We get smarter at the customer's expense · so the next customer doesn't see the same dark.

The PASS doctrine and the failure-naming discipline are the same mechanism on opposite ends. PASS rejects fantasy mandates at intake. Failure-naming reports actual outcomes at exit. Both refuse the seductive lie.

---

## The assignment lifecycle

Every assignment moves through 8 stages. Each stage has a named gate. Each gate has a named owner. Each owner files a named artifact.

| # | Stage | Gate | Owner | Artifact |
|---|---|---|---|---|
| 1 | **Intake** | Principal identified · pain named | Jr broker | Pre-market flight sheet |
| 2 | **Color build** | ≥ 5 independent sources · contradictions reconciled | Jr broker | Color file |
| 3 | **PASS check** | Fantasy mandate test passed | Sr broker | PASS verdict log |
| 4 | **Proposal** | Success criteria written · numeric · time-bound | Sr broker | Assignment brief |
| 5 | **Ink** | Brief countersigned · LOU updated if needed | Sr broker + principal | Signed assignment brief |
| 6 | **In-flight** | 24/7 ops · daily Morning Brief · weekly Tribunal rollup | Defense ops team | Daily reconciliation deeds |
| 7 | **Closing** | All 5 grades scored · composite computed · boolean assigned | Tribunal + sr broker | Defendable closing statement |
| 8 | **Books** | Receipts anchored · deed published · folder filed | QA validator | Books-and-records entry |

Skipping a gate is a structural failure. The QA validator (SH6) checks the gate-trail on every closed assignment. Missing artifacts trigger a `Propolis` event on the assignment itself · not just the work.

---

## How this plugs into the rest of the doctrine

- **Probability of Close** ([15_probability_of_close_doctrine.md](15_probability_of_close_doctrine.md)) is the dial that PREDICTS the assignment boolean. Assignment Success is the dial that REPORTS it. Same physics · different timestamps.
- **Honey · Royal Jelly · Jelly · Propolis** ([07_honey_royal_jelly_propolis.md](07_honey_royal_jelly_propolis.md)) is the per-output classification system. Assignment Success is the per-assignment rollup.
- **Receipts · Deeds · Books and Records** ([10_receipts_deeds_and_books_records.md](10_receipts_deeds_and_books_records.md)) is the trust layer that makes the assignment boolean defendable. Without receipts · the boolean is a claim. With receipts · it's an attestation.
- **Energy and Cost to Mint** ([09_energy_and_cost_to_mint.md](09_energy_and_cost_to_mint.md)) is the G4 input. The CFO line item lives here.

---

## What this enables

When the doctrine is enforced end-to-end · the principal can ask three questions on any Tuesday morning and get three crisp answers:

1. **"Is the assignment on track?"** → Probability of Close dial · current driver list · current weekly Honey rate.
2. **"Did the last close succeed?"** → Boolean · composite · 5-grade breakdown · variance vs contract.
3. **"What's it costing?"** → Cost-to-mint actual · vs ceiling · vs prior period · projected through close.

Three questions. Three numbers. Three receipts. That's a broker-grade relationship · not a SaaS dashboard.

---

## Related terms

- [assignment](../vocabulary/client_terms/assignment.md)
- [engagement](../vocabulary/client_terms/engagement.md)
- [assignment-success](../vocabulary/scoring_terms/assignment-success.md)
- [closing-statement](../vocabulary/client_terms/closing-statement.md)
- [pass-doctrine](../vocabulary/client_terms/pass-doctrine.md)
- [probability-of-close](../vocabulary/scoring_terms/probability-of-close.md)

🐝 *When a job IS the job · we say so · in writing · with receipts.*
