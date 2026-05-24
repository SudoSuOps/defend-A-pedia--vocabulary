# CRE → DefendableOS Translation Doctrine

> *"Every term we use in a deal has a home in the schema. If it doesn't, the field doesn't exist."*

This doctrine is the bridge. CRE on the left. DefendableOS on the right. No drift between the two columns. The same operator running a $40M cold-storage trade in 2018 can run a $40K/mo AI defense engagement in 2026 using the same words. That's by design.

---

## The mental model

```
The customer is a SELLER.
The AI agent fleet they run is the ASSET.
The defense engagement is the LISTING.
DefendableOS is the LISTING BROKER.
The validator chain is the TITLE WORK.
The Tribunal is the APPRAISAL.
The deed is the CLOSING STATEMENT.
The books-and-records are the FILE THE COUNTY RECORDS.
```

A jr broker who has run a CRE trade can read this map and skip the AI-jargon onboarding. A sr broker can adjudicate AI deals using the same instincts that closed eight figures of industrial NNN. An engineer can wire a backend field knowing the operator's mental model is locked.

---

## The master translation table

Every column below has a one-to-one map. If you find a CRE term that doesn't have a DefendableOS analog in this file, you've found a missing schema field · escalate to SH2 (Vocabulary Infrastructure Architect).

### Asset and ownership terms

| CRE term | DefendableOS analog | Backend field | Notes |
|---|---|---|---|
| Asset / property | Agent fleet / operator workflow | `engagement.asset_descriptor` | The thing being defended |
| Sponsor / principal | Business owner / CEO / founder | `engagement.principal_id` | The buyer of defense |
| Tenant | Live AI agent in production | `agent.id` (ENS subdomain) | The thing that pays rent (produces revenue) |
| Tenant credit | Agent grade · Honey/Royal Jelly tier | `agent.honey_tier`, `agent.credit_grade` | Investment-grade = production-ready |
| Rent roll | Per-agent production ledger | `agent_ledger.entries[]` | Who's producing · who's idle |
| Anchor tenant | Critical-path agent | `agent.criticality = ANCHOR` | The agent the business depends on |
| Vacancy | Failed / dark agents | `agent.status = DARK` | Empty space = lost revenue |
| Occupancy | % of agents in alignment | `fleet.occupancy_pct` | 100% occupied = no agent dark |
| Class A | Royal Jelly / Genesis tier | `asset.class = A` | Prime · irreplaceable |
| Class B | Honey tier | `asset.class = B` | Decent · replaceable |
| Class C | Propolis / risk-flagged | `asset.class = C` | Bad neighborhood |
| Brick and mortar footprint | The real business workflow the agents sit in | `engagement.brick_and_mortar_scope` | Founder's term · always preserve |

### Valuation and underwriting terms

| CRE term | DefendableOS analog | Backend field | Notes |
|---|---|---|---|
| Cap rate | Engagement yield · annual defense fee / annual revenue at risk | `engagement.cap_rate_implied` | Inverts: lower = more expensive (better protected) |
| NOI | Net agent-produced revenue · gross less drift/repair cost | `agent.noi_monthly_usd` | Per-agent NOI rolls up to fleet NOI |
| DSCR | Defense coverage ratio · defense $ vs revenue at risk | `engagement.dscr` | <1.0 = under-defended |
| Debt yield | $/agent of defense vs agent's annual revenue | `engagement.debt_yield_pct` | The CFO sanity check |
| LTV | Defense spend / asset value | `engagement.ltv_pct` | The board's ratio |
| Pro forma | Forecasted fleet performance under defense | `engagement.proforma_v1` (jsonb) | The pitch math |
| T-12 NOI | Trailing 12-mo agent revenue actuals | `agent.t12_noi` | What the rent roll actually produced |
| Yield maintenance | Defense renewal economics | `engagement.renewal_yield` | What it costs the customer to leave us |
| Underwriting | The math · the rubric · the gates | `tribunal.rubric_v1` | 6 gates + 7th adversarial |
| Comp / comparable | Prior deeds against similar agent class | `deed.comp_set[]` | We comp deeds the way brokers comp sales |

### Deal flow and lifecycle terms

| CRE term | DefendableOS analog | Backend field | Notes |
|---|---|---|---|
| Pre-market | Pre-engagement diligence | `engagement.stage = PRE_ENGAGE` | Before the LOU |
| OM (Offering Memorandum) | The public pitch deck · the deal-flow brochure | doc artifact `om_v1.pdf` | Pretty book · NOT the flight sheet |
| Pre-market flight sheet | The operator-internal deal doc · color built | doc artifact `flight_sheet_v1.json` | What WINS the deal · not what wins the meeting |
| LOI / LOU | Letter of Intent · Letter of Understanding · soft commitment | `engagement.lou_signed_at` | First ink |
| PSA | Purchase and Sale Agreement · binding contract | `engagement.psa_signed_at` | Hard ink |
| Due diligence | The verification phase · evidence + color + validator chain run | `engagement.dd_status` | The Tribunal calls this evidence_required |
| Earnest money | Engagement deposit | `engagement.deposit_usd` | Skin in the game |
| Inspection | Pre-engagement audit of the agent fleet | `engagement.inspection_record_id` | What we found before we agreed |
| Title work | Validator chain run | `validator_chain.run_id` | 12 checks · 7 critical · 5 advisory |
| Appraisal | Tribunal scoring run | `tribunal.run_id` | Honey/Jelly/Propolis verdict |
| Closing | Deed issuance + Hedera anchor | `deed.issued_at`, `deed.hedera_topic_id` | "To the shed" |
| Closing statement | Defendable Closing Statement · per-engagement variance report | `engagement.closing_statement_v1.pdf` | The doc the customer signs at the end |
| Hold period | Engagement term length | `engagement.term_months` | 12/24/36-month listings |
| Disposition | Engagement wind-down / non-renewal | `engagement.disposition_reason` | Why we (or they) walked |

### Pricing and commission terms

| CRE term | DefendableOS analog | Backend field | Notes |
|---|---|---|---|
| Strike price | Pitched fee | `engagement.pitched_fee_usd` | What the customer asked for |
| Trade price | Closed fee | `engagement.closed_fee_usd` | What we actually closed at |
| Re-trade | Mid-deal renegotiation | `engagement.retrade_count` | Each one weakens trust |
| Commission | Defense fee | `engagement.fee_monthly_usd` | The white-glove price |
| Co-broker split | Partner/integrator split | `engagement.partner_split_pct` | When we don't list direct |
| Listing fee | Engagement-onboarding fee | `engagement.onboarding_fee_usd` | One-time at LOU |
| Fee tail | Post-engagement repair/retraining lift | `engagement.tail_revenue_usd` | The compounding part |
| Lead-broker | Engagement owner of record | `engagement.lead_broker_id` | The name on the deal |

### Diligence and disclosure terms

| CRE term | DefendableOS analog | Backend field | Notes |
|---|---|---|---|
| Color on the asset | Verified-evidence layer | `engagement.color_score`, `color_status` | See `cre_terms/color.md` (sample) |
| Books and records | The 5-layer finality stack | `deed.books_layer = L1...L5` | PG → Merkle → NAS → Hedera → ENS |
| Encumbrance | Known agent failure mode disclosed | `agent.encumbrances[]` | What's NOT defendable on this fleet |
| Easement | Third-party dependency · vendor lock | `agent.dependencies[]` | The stuff we can't fix because someone else owns it |
| Phase 1 environmental | Adversarial probe report | `inspection.adversarial_report_v1` | What ugly things we found before signing |
| Survey | Topology audit of the agent fleet | `inspection.topology_map` | The map of what's actually there |
| Estoppel | Tenant/agent self-attestation | `agent.estoppel_signed_at` | Confirms what we think we're defending |
| Title insurance | Tribunal title-insurance receipt · ±0.15 score guarantee | `deed.title_insurance_id` | We back our verdict with $ |
| Disclosure schedule | Failure-mode catalog per engagement | `engagement.disclosures[]` | What we promise we'll surface, not hide |

### Counterparty terms

| CRE term | DefendableOS analog | Backend field | Notes |
|---|---|---|---|
| Buyer pool | Live customer pipeline by tier | `pipeline.buyers_by_tier` | Who's currently engageable |
| Buyer strength | Customer financial health / contract size | `engagement.buyer_strength_score` | Investment-grade vs distressed |
| Seller motivation | Customer urgency · pain level · deadline | `engagement.seller_motivation_score` | 1031 deadline equivalents |
| Whisper price | Pre-LOU informal fee discussion | `engagement.whisper_fee_usd` | Tested in conversation · not committed |
| Stalking horse | Anchor reference customer | `engagement.reference_anchor` | The deal that calibrates the rest |
| Off-market | Direct relationship · not in public funnel | `engagement.source = OFF_MARKET` | The high-trust channel |
| On-market | Inbound from public surfaces | `engagement.source = ON_MARKET` | The funnel from `defendableos.com` |
| Repping the seller | Acting for the customer | `engagement.broker_side = SELLER` | The default |
| Repping the buyer | Acting for the AI vendor / integrator | `engagement.broker_side = BUYER` | Rare · usually conflict |
| Dual rep | Bilateral engagement | `engagement.broker_side = DUAL` | Requires explicit disclosure |

### Outcome and audit terms

| CRE term | DefendableOS analog | Backend field | Notes |
|---|---|---|---|
| To the shed | Deal closed · deed issued · books filed | `engagement.status = CLOSED` | Founder's close-out phrase |
| Walked the building | Live agent-fleet inspection | `inspection.physical_walked_at` | Equivalent of a site visit |
| Pencils | The numbers work | `engagement.pencils = true/false` | The math sanity check |
| Doesn't pencil | The numbers don't work · PASS | `engagement.pencils = false` | Trigger the PASS doctrine |
| Re-trade | Price changed mid-deal | `engagement.retrade_count` | One is forgivable · two is concerning · three you walk |
| Hold for the next cycle | Engagement deferred · re-pitch later | `engagement.deferred_to` | Patience over fee |
| Closing the file | Deed permanently archived | `deed.archived_at` (L5 ENS) | The forever record |

### Risk and stress-test terms

| CRE term | DefendableOS analog | Backend field | Notes |
|---|---|---|---|
| Stress test | Adversarial Tribunal run | `tribunal.adversarial_run_id` | The 7th gate |
| Workout | Mid-engagement remediation | `engagement.workout_plan_v1` | When agents drift, we work out the loan |
| Recourse | Defense provider liability | `engagement.recourse_terms` | What we owe if we fail |
| Non-recourse | Insurance-only defense · no liability | `engagement.non_recourse = true` | The cheaper tier |
| Mezz | Mid-priority defense layer | `defense_layer = MEZZ` | Senior is critical · mezz is important · junior is advisory |
| Going dark | Agent stops producing | `agent.status = DARK` | The failure mode the killer sentence names |
| Conditioning the asset | Recovery doctrine · agent re-alignment | `engagement.conditioning_plan_v1` | SwarmJelly application |

---

## Cross-domain rules

**1. The bidirectional rule applies here too.** Any term in the left column must have a row in the right column. Any field in the right column must trace back to a real CRE concept in the left column. Orphan rows are a doctrine violation.

**2. Where the analog isn't clean, name the gap.** Some CRE concepts don't have a clean AI defense equivalent (yet). When that happens, the row says `[gap · candidate term · escalate]` and SH1 is on the hook to either close it or remove the row.

**3. Never let the analog DRIFT the original.** If an engineer wants to rename `engagement.cap_rate_implied` to something more "intuitive," they have to first rename the CRE term. They won't. That's the protection.

**4. Founder voice trumps "industry standard."** Where CRE and AI/SaaS conflict on a word, CRE wins. Example: in AI, "agent" can mean a software process. In our world, "agent" can mean the operator on the dial (CRE usage). When ambiguous, we qualify · `human agent` vs `AI agent` · and we honor the CRE-first reading in the doctrine.

---

## How to use this table

**Jr broker · day 1:** read this table cover-to-cover. Memorize the left column · you already know it. Memorize the right column · you'll need it tomorrow.

**Sr broker · day 1:** read this table to spot the gaps. Where the analog is weak, you'll see it before anyone else. Escalate to SH1 with a proposed strengthening.

**Engineer · day 1:** read this table to understand naming discipline. If you're adding a new field, find its CRE analog. If there isn't one, you might be adding the wrong field.

**Client-facing operator · day 1:** read this table to translate. When the customer says "my agent fleet has 80% occupancy and 30% of my anchor tenants went dark," you understand they're describing a defense crisis · not just a tech issue. Speak back in their CRE-borrowed terms.

**Future model in training:** every row in this table is a training pair. The vocabulary is the corpus. The corpus is the constitution. The constitution is what makes the model speak the founder's voice.

---

## What this doctrine prevents

It prevents three failure modes that kill most AI-defense plays:

1. **Vocabulary drift** · engineers and sales teams diverge on terminology · within 6 months nobody knows what a "deed" means
2. **Schema sprawl** · backend grows fields nobody can defend in plain English · audits get expensive · clients lose trust
3. **Client confusion** · customer reads one term in the LOU, a different term in the dashboard, a third in the Closing Statement · churn follows

The CRE table is the antidote. One language. One schema. One client experience. Top to bottom. End to end.

---

## Read next

- [`03_jr_broker_sr_broker_doctrine.md`](03_jr_broker_sr_broker_doctrine.md) · the career ladder that runs the language
- [`04_books_and_records_doctrine.md`](04_books_and_records_doctrine.md) · the 5-layer audit trail this vocabulary anchors
- [`../vocabulary/cre_terms/`](../vocabulary/cre_terms/) · the canonical term files

🐝 *The schema follows the language. Top to bottom. End to end.*
