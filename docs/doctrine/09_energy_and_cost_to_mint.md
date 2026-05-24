# 09 · Energy and Cost to Mint

> *"Build the math. Eat the fees. The number is the number. We publish the formula because hiding the meter is what fantasy mandates look like."*
>
> — Founder · in the pit · 2026-05-24

---

## Why this doctrine exists

Every CRE broker knows the meter is running on every deal. Loan origination fee · title insurance · escrow · survey · environmental · estoppels · the lender's appraisal. The closing statement (HUD-1) prints all of it. Line by line. Buyer side · seller side · who paid what. The CFO can audit it on a 14-minute coffee break.

The AI industry has spent two years quoting "$X/month per seat" while hiding the per-call cost · the per-token cost · the per-deed cost. We refuse that. DefendableOS publishes the cost-to-mint formula. The principal can re-derive every receipt · every deed · every line item on the monthly invoice with a calculator and an hour.

This doctrine answers three questions:

1. **What does it cost us to issue one Defendable Agent Deed?**
2. **How do we tier the fee structure so the principal can underwrite us?**
3. **Why publish the math instead of hiding it?**

---

## The $0.0052/deed baseline

The all-in cost to mint one **Royal Jelly** Defendable Agent Deed on our owned compute stack is **$0.0052 USD** at 2026-05 production rates. That number ties to a 7-component breakdown · every component re-derivable from public spec sheets and our published bench data:

| Component | Cost per deed | Source / re-derivation path |
|---|---|---|
| **GPU inference** (Qwen 32B · 1.2K avg tokens · 95% util) | $0.0021 | Power draw × wall time × Florida industrial-rate kWh · public bench |
| **Tribunal pass** (2-pass · Scale A + Scale B judges) | $0.0014 | gemma3:12b + qwen2.5:32b · 2 passes · same compute math |
| **Validator chain** (12 checks · 7 critical · 5 advisory) | $0.0005 | Rule-layer + lightweight model · published throughput 777 pairs/hr |
| **Hedera HCS anchor** (1 message · topic 0.0.10291838) | $0.0001 | Hedera mainnet fee schedule · public |
| **NAS L3 archive** (sustained 50 MB/s · 1.1 KB/deed) | $0.0001 | Owned NAS · amortized hardware + power · 5yr depreciation |
| **ENS resolution** (amortized over 14 registered domains) | $0.0002 | ENS registration fees · spread over deed volume |
| **Operator margin** (white-glove ops · principal access · SLA) | $0.0008 | Founder + sr broker labor · amortized at $250K fully-loaded |
| **Total · per deed** | **$0.0052** | |

The number is published. The math is re-derivable. The Hedera anchor for a sample deed is browsable by anyone with the HCS topic ID. That's the CRE-grade transparency standard applied to AI infrastructure.

---

## The 4 fee tiers

Cost-to-mint is the floor. The fee is the floor times a multiplier that reflects the service level the principal contracted for. Four tiers · published · stable · explainable to a CFO in 90 seconds.

| Tier | Multiplier | Effective $/deed | What's included |
|---|---|---|---|
| **T1 · Pilot** | 2x | $0.0104 | First 90 days of any new engagement · no SLA · Tribunal-graded · Morning Brief 3×/week |
| **T2 · Production** | 4x | $0.0208 | Standard engagement · 24/7 ops · daily Morning Brief · 99.5% deed-uptime SLA · weekly sr broker review |
| **T3 · White-Glove** | 8x | $0.0416 | Principal-direct relationship · founder reachable · same-day escalation · custom validator chain · 99.9% SLA |
| **T4 · Embedded** | 12x | $0.0624 | Embedded defense ops team · Fix-or-Refund 90-day guarantee · dedicated SwarmFixer queue · custom training pairs · 99.99% SLA |

The multipliers are not arbitrary · they reflect the marginal cost of human attention. T1 is mostly automated. T4 includes a named sr broker on retainer. The CFO can stack-rank by attention dollars and underwrite the value.

Volume discounts and contracted floors are negotiated at LOU signing · documented in the LOU appendix · NOT secret. Published in the engagement folder · accessible to the principal at any time.

---

## Why we don't hide the math

Three reasons · all CRE-rooted · all non-negotiable.

### 1. The CFO line item is the only line item that survives a recession

When budgets tighten · every line item gets re-justified. The vendor that can hand the CFO a 7-component cost breakdown · re-derivable on a calculator · with a Hedera anchor for the math · survives the cut. The vendor that ships "Enterprise · Contact Us" pricing dies.

The founder closed $8B in CRE through three recessions. Every survivor at the closing table could re-derive their fee. Every casualty couldn't.

### 2. Transparency IS the moat

Anyone can copy a feature. Nobody can copy a published-formula trust posture without actually owning their compute · running their math · and standing behind it. The published cost-to-mint is a competitive moat the same way EDGAR-disclosed financials are a moat for public companies · the disclosure burden is what filters out the imposters.

A competitor who can't publish their formula is a competitor running someone else's API at margin · with no infrastructure underneath. The principal can tell the difference in 5 minutes once they know to look.

### 3. The principal underwrites US the same way we underwrite the engagement

The CRE PASS doctrine cuts both ways. We PASS on fantasy mandates · the principal PASSES on fantasy vendors. By publishing the math · we invite the principal to underwrite us · the same diligence we apply to the engagement. The relationship is a two-sided contract · NOT a vendor pitch.

This is the M&M operator cadence applied to AI: *"In the pit · make the dials · build the math · eat the fees."* The math is what the principal eats with. Hide it and they leave hungry · or worse · they leave skeptical.

---

## The energy reality

Energy is the largest variable cost · and the most ignored one in the industry. We track it explicitly per the **Compute Bench** doctrine ([compute-bench-shipped-2026-05-22]).

A Royal Jelly deed on a Qwen 32B inference at our Florida rate burns approximately:

- **0.0024 kWh** of GPU energy (Blackwell RTX PRO 6000 · 95% util · 18 sec avg wall time)
- **0.0006 kWh** of CPU + RAM + cooling overhead (sustained at 20% PUE on owned DC)
- **0.0030 kWh** total per deed

At Florida industrial rate of $0.082/kWh · that's **$0.000246/deed** of pure energy · or roughly **5% of the all-in $0.0052**. The rest is compute amortization · validator overhead · anchor fees · operator labor.

We publish this because energy will be the line item the next-generation CFO obsesses over. We'd rather be the vendor who put it in the OM in 2026 than the one scrambling to disclose it in 2028.

---

## How the math gets updated

Cost-to-mint is recomputed quarterly · published on the **/economics** page · and recorded in books-and-records as a deed of its own (`DDEED-DOV-ECON-Q{n}-{year}-v{v}`). Every quarterly update is anchored on Hedera · the principal can verify the meter against the historical baseline.

Three things trigger an out-of-cycle update:

1. **GPU power efficiency change** (new hardware · new firmware · new model)
2. **Hedera fee schedule change** (mainnet protocol fee updates)
3. **Validator chain composition change** (new check added or removed)

Every change ships with a deed · a delta explanation · and a principal notification. No silent meter changes.

---

## The M&M operator cadence applied to deeds

> *"No ideas · in the pit · make the dials · build the math · now your conversion rates · eat fees."*

Translated to defense operations:

- **No ideas** · we don't propose new fee tiers without 90 days of cost-to-mint data backing them
- **In the pit** · the cost meter runs 24/7 · captured per-deed · aggregated nightly
- **Make the dials** · cost-to-mint feeds the Probability of Close dial (operator hygiene driver)
- **Build the math** · the 7-component breakdown is rebuilt every quarter
- **Conversion rates** · how many pilot-tier (T1) engagements convert to production-tier (T2) · how many production convert to white-glove (T3)
- **Eat fees** · the Stripe MRR · the engagement invoices · the actual revenue lands on the same dashboard as the cost-to-mint

The cadence is what makes the math real instead of theatrical. Anyone can publish a formula. The discipline is publishing it every quarter · standing behind the variance · and naming what changed.

---

## How this plugs into the rest of the doctrine

- **Assignment Success** ([14_assignment_success_doctrine.md](14_assignment_success_doctrine.md)) · G4 (Economics) is graded directly against the contracted cost-to-mint ceiling vs actual.
- **Probability of Close** ([15_probability_of_close_doctrine.md](15_probability_of_close_doctrine.md)) · operator hygiene driver (10% of dial) includes cost-to-mint discipline.
- **Receipts · Deeds · Books and Records** ([10_receipts_deeds_and_books_records.md](10_receipts_deeds_and_books_records.md)) · every deed carries a `cost_to_mint_usd` field per the receipt schema.
- **Closing Statement** is where the cost math lands in writing for the principal · same as a HUD-1 in CRE.

---

## Related terms

- [cost-to-mint](../vocabulary/minting_terms/cost-to-mint.md)
- [energy](../vocabulary/minting_terms/energy.md)
- [closing-statement](../vocabulary/client_terms/closing-statement.md)
- [morning-brief](../vocabulary/client_terms/morning-brief.md)
- [letter-of-understanding](../vocabulary/client_terms/letter-of-understanding.md)

🐝 *We publish the meter. The CFO can audit it. That's the CRE standard · applied.*
