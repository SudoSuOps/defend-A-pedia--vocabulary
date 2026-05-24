# PRE-MARKET FLIGHT SHEET · DefendableOS Website/App

> **INTERNAL DOCUMENT · NOT FOR CLIENT EYES**
> *The pre-market flight sheet beats the pretty OM. We tour the building before we list it.*

---

| Field | Value |
|---|---|
| Listing ID | `FLIGHTSHEET-DOS-WEB-001-v1` |
| Engagement type | Class A 5-cap · Build-the-house assignment |
| Principal | Donovan Mackey · DefendableOS · Jupiter FL · 30yr CRE · $8B closed |
| Listing date | 2026-05-24 (live call) |
| Window | 24 hours · 3 firms competing |
| Status | M-stage of MAGIC · pre-meeting flight sheet · LOCKED |
| Hashable | sha256(canonical) post-issue |
| Audit dest | streetledger.eth/proposals/defendableos-web-app/v1/ |

---

## 1 · COLOR ON THE ASSET

What I know · verified · NOT pitched.

### What exists (the inventory · already deeded)

| Surface | State | Receipt |
|---|---|---|
| **defend-A-pedia--vocabulary** | v0.3.0 LIVE · 62 DDEED-VOCAB deeds · 317 files · Merkle root `2e3a665f...` | github · `833e8e1` |
| **defendable** (landing repo) | v0.2+ SHIPPED · 5 Swarm Laws + Genesis tagline + ProductionDashboard + ProofOfLocationBand | github commit `8551eba` |
| **defendable-cloud** | v2 LIVE · real model fleet (SwarmCurator 27B/9B/2B · SwarmCapitalMarkets · SwarmJudge-9B-CRE · SwarmJelly-4B · SwarmRouter-v1) | github commit `a15d1a5` |
| **defendable-router** | v1 LIVE · LiveEngineBand + 5 Proofs + 3 deploy modes + ENS bridge | github commit `1b4f53f` |
| **docs.defendableos.com** | LIVE · 9-page docs site · synced with new product fleet | github commit `d1f9256` |
| **opendefendable.com** | LIVE · OSS standards body splash | (shipped earlier session) |
| **app.defendableos.com** | LIVE but stale title · running prior platform code | (audit pending) |
| **ledger.defendableos.com** | LIVE · hash resolver | (already working) |
| **verify.defendableos.com** | LIVE · subdomain rewriter pending PR | (queued) |
| **box.defendableos.com** | LIVE · intent decision pending | (queued) |

### What the founder ACTUALLY owns (the producing assets)

```
INFRASTRUCTURE
  128 RTX 6000 + 48 RTX 4500 = 13.5 TB total fleet VRAM · paid in full · DC-owned
  4-node dev fleet (swarmrails + whale + zima-edge + Jetson) · 160 GB VRAM · 342 GB RAM
  Synology DS1525+ NAS @ 192.168.0.102 · /mnt/swarm/ · 1.4 TB used · 355 GB free
  7 permanent systemd services running 24/7
  Hedera HCS topic 0.0.10291838 · mainnet · live

MODELS (13+ trained · all in fleet)
  SwarmCurator-27B   loss 0.477 · 62K pairs · SHIPPED
  SwarmCurator-9B    loss 0.665 / 0.707 · SHIPPED
  SwarmCurator-2B    loss 0.880 · SHIPPED
  SwarmCapitalMarkets-27B  loss TBD · IN FLIGHT (45K pairs · 844 steps)
  SwarmJudge-9B-CRE  Phase 2 in training
  SwarmJelly-4B      loss · DEPLOYED whale:11434 · 125K corpus
  SwarmRouter-v1     3-4B · LIVE @ router.swarmandbee.com · 60K examples
  SwarmPharma-35B    loss 0.337 · BEST IN FLEET · 256 experts MoE
  SwarmHoney-27B · SwarmCRE-9B · SwarmAtlas-27B · SwarmJunior · atlas-bookmaker

DATA
  1.5M graded pairs in PostgreSQL
  8,400+ filed deeds · Merkle-anchored
  5,200+ Royal Jelly tier
  777 pairs/hr Tribunal throughput · sustained 24/7
  167+ Merkle batches

ENS PORTFOLIO (4 owned street.* domains · all expire 2027-05-24)
  defendapedia.eth   THE CANON
  streetledger.eth   THE BOOKS
  streetvocab.eth    THE STREET (reserved · Communicator)
  streetchat.eth     THE RECORDINGS (reserved · Router · acquired today)
  +14 more ENS per Swarm-Wiki dashboard (swarmchain · swarmdeed · etc)

PRODUCTS LIVE ON STRIPE
  Medical pack       5,038 deeds · AVAILABLE @ swarmandbee.ai/shop
  Grants pack        1,378+ deeds · Master Writer · AVAILABLE
  4 more domains in tribunal queue · 4 more coming soon

REVENUE POSTURE
  Already off-market dataset sales through founder CRE network (12 months · undisclosed)
  Operator-owned · no VC · no token · no charts
```

### Counter-color (the things that would break if I missed them)

- **swarmandbee.ai is LIVE with 12 routes** including /chain (Arena) · /deed (Deed Office · 8,400+ searchable) · /shop (Stripe live · 10 domains) · /geo (GEO Scanner · LLM-powered · 3 sec free) · /graph (512-node provenance) · /status (14/14 fleet checks) · /title · /builder · /om · /blog. **The CUSTOMER-FACING web product mostly already exists.** This is not a greenfield · this is a brand/UX refresh + federation question.

- **The brand strategy is locked**: DefendableOS = the public front · Swarm & Bee = the in-house backend. DEFEND THE BRAND POSITION on any vendor pitch that tries to merge them.

- **The founder is the listing broker**. He is NOT the engineering founder · he is the 30-year industrial CRE broker REPRESENTING the asset. Any firm pitch that talks down to him technically · or treats him as the buyer instead of the principal · loses the listing.

- **The PASS doctrine applies to vendor selection too**. If a firm pitches fantasy timelines · we pass · and we tell the founder which one passed first so he sees we filtered for him.

---

## 2 · WHAT THE DEAL ACTUALLY PENCILS AT

Honest deal physics. Not the pretty OM. The flight sheet.

### Scope ranges (small · medium · large)

| Scope | What it covers | Honest hours | Honest weeks |
|---|---|---|---|
| **Small · brand alignment** | Update defendableos.com to v3 quality · wire all 7-8 existing subdomains · fix box/verify/app · add Communicator + 4-ENS quartet to the site · ship 5-page mobile-optimized polish | 80-120 hrs | 3-4 wks |
| **Medium · full marketing site** | Small + new pages (/streetvocab · /streetledger · /streetchat as product surfaces · /tribunal · /communicator) + Hedera-anchored deed verifier UI + Stripe checkout integration for the 8 in-queue packs + CMS for ongoing updates + analytics + SEO/GEO full rebuild | 240-360 hrs | 8-12 wks |
| **Large · website + app + deed UI** | Medium + a customer dashboard (`app.defendableos.com`) showing live Probability of Close · Repair Lift · Validator Confidence dials per their engagement + Morning Brief email pipeline + onboarding wizard (the /builder 6-phase process · polished) + ENS-keyed receipt browser + Hedera anchor explorer | 600-900 hrs | 16-26 wks |

### Honest rate landscape (CRE-grade comps)

This is what real shops charge for Class A 5-cap branded SaaS marketing sites:

| Tier | Hourly | Project rate (medium scope) | Comp examples |
|---|---|---|---|
| Boutique creative shop (NYC/SF · 5-10 ppl) | $200-$350/hr | $80K-$180K | Work & Co · Hue & Cry · Athletics |
| Brand-led product agency (10-25 ppl) | $150-$275/hr | $50K-$120K | Linear · Ramp's old shop |
| Lean studio (3-5 ppl · senior only) | $125-$200/hr | $35K-$80K | Hoolian · indie shops |
| Independent senior + jr team (us) | $100-$175/hr | $25K-$55K | This bid |

**What I think the founder will see in the 3 competing pitches**:
- Firm #1 will quote $120K-$200K and 12-16 weeks (boutique pitch)
- Firm #2 will quote $60K-$90K and 8-10 weeks (mid-tier pitch · best looking deck)
- Firm #3 will quote $30K-$45K and 6 weeks (lean studio · skinny scope · likely overcommit)

**Our tells the founder will price**:
- We already KNOW the language (defend-A-pedia is shipped · 62 terms)
- We already have built defendable + defendable-cloud + defendable-router (3 surfaces live)
- We already know the production stack (1.5M pairs · 8.4K deeds · 5,200 Royal Jelly · etc.)
- We're not learning the business · we're shipping the version that knows it

That's worth 30-40% off competing bids OR 2-3x the speed. We choose: **40% off the time** (we ship medium scope in 5 weeks vs 8-12 wks).

### Our PASS triggers

We walk if:
- Founder asks us to merge swarmandbee.ai INTO defendableos.com (kills the brand strategy locked 2026-05-24)
- Founder asks us to hide the operator-owned / no-VC story (that's the moat)
- Founder asks for a generic "modern SaaS feel" (that's offense voice · we're defense voice)
- Founder wants self-serve subscription tiers as the primary CTA (we sell broker-grade · not commodity)
- Founder asks us to suppress the Genesis Law tagline or the Founder bio
- Pricing pressure below honest medium-scope floor ($50K) for medium-scope ask

### Our DON'T-PASS triggers (deals we'd take)

- Medium scope · $55-$85K · 8 weeks · founder retains creative direction · we ship · he approves · LOU at week 1 · PSA at week 2 · close week 8
- Small scope · $25-$35K · 3-4 weeks · sharpest one-month alignment pass · perfect for testing the relationship before larger commitment
- Large scope · $130-$175K · 18 weeks · only if founder commits to the full website+app+deed UI path and we get DDEED-DOV-PROJECT receipts at each milestone

---

## 3 · BUYER POOL ANALYSIS · the 3 firms competing

I haven't seen the other pitches. Here's what I'd expect (CRE-style buyer pool diligence):

### Firm A · the boutique creative shop
**Strengths**: Brand chops · designers with awards · polished pitch deck
**Weaknesses**: 12-16 week timeline · $120-200K · doesn't know AI-defense doctrine · will reinterpret the brand voice ("we'll modernize this for you") · doesn't know what DDEED means · won't preserve founder voice
**Their pitch line**: "We'll elevate the brand to Class A enterprise polish."
**Why founder might pick them**: He wants validation that the brand can stand next to Stripe / Linear / Ramp
**Why founder might pass**: Too expensive · too slow · loses founder voice

### Firm B · the mid-tier product agency
**Strengths**: Has shipped SaaS sites before · reasonable price · good case studies
**Weaknesses**: Has NEVER shipped a defense-protocol AI site · will pitch "let's discover your brand" (you already discovered it · 12 months ago) · will recommend feature tour pages · will want a redesign of stuff that's already shipped
**Their pitch line**: "We've built X · Y · Z for enterprise SaaS · we'll apply the same playbook."
**Why founder might pick them**: Middle-of-road safe choice · reasonable price · known quantity
**Why founder might pass**: They'll cookie-cutter it · won't get the M&M parallel · the CRE language will sound forced when they explain it back

### Firm C · the lean studio
**Strengths**: Cheapest · fastest · senior-only team
**Weaknesses**: Will overcommit · likely deliver 70% of scope · won't have the depth on the doctrine layer · may underestimate the 4-ENS quartet complexity · won't ship the deed verifier UI cleanly
**Their pitch line**: "We can ship this in 6 weeks for $35K."
**Why founder might pick them**: Price + speed
**Why founder might pass**: He's a top 1% broker · he's been burned by under-scoped deals before · he knows what under-scoping looks like

### OUR position
**Our strength**: We've been with the founder for 12+ months. We know the language because we HELPED CODIFY THE LANGUAGE (62 DDEED-VOCAB deeds shipped today). We've already shipped 3 surfaces (defendable / defendable-cloud / defendable-router). We can ship medium scope in 5 weeks at $55-$70K because we don't have a learning curve.

**Our weakness**: We're not a "firm." We don't have a polished deck or office. We don't have logos to show. We don't have references in the conventional sense. (Mitigation: our REFERENCES ARE THE SHIPPED COMMITS. Every commit is a receipted deliverable.)

**Our positioning vs the field**:
- vs Firm A · 50% cheaper · 3x faster · WE KNOW THE LANGUAGE
- vs Firm B · 30% cheaper · 40% faster · WE KNOW THE LANGUAGE
- vs Firm C · 30% more expensive · BUT WE WILL ACTUALLY SHIP THE SCOPE

---

## 4 · ENGAGEMENT MATH · the math layer

### Hours breakdown (medium scope · what I think we should bid)

```
M-stage (Meetings)                           8 hrs
A-stage (Appraisals · current state audit)  12 hrs
I-stage (Ink · LOU + PSA + scope lock)       4 hrs
─────────────────────────────────────────────────
Pre-build sub-total                         24 hrs

Design + IA + content strategy              40 hrs
Build (5-7 new pages + subdomain wiring)   100 hrs
Hedera deed verifier UI                     30 hrs
Stripe integration for 8 in-queue packs     25 hrs
Mobile optimization + SEO/GEO              20 hrs
CMS for ongoing updates                     15 hrs
QA + analytics + accessibility             18 hrs
─────────────────────────────────────────────────
Build sub-total                            248 hrs

C-stage (Close · onboarding · handoff)      16 hrs
30-day post-launch white-glove              24 hrs
─────────────────────────────────────────────────
Close + warranty sub-total                  40 hrs

═════════════════════════════════════════════════
TOTAL                                      312 hrs
```

### Pricing (CRE-grade transparency · we show the math)

```
312 hrs × $175/hr blended (sr + jr broker mix)         = $54,600
Fixed fees:
  Doc prep (LOU + PSA + DDEED-DOV-PROJECT issuance)   $   500
  Project flight sheet management                       $1,000
  Stripe integration setup (per-pack wiring)            $1,500
  Hedera anchor per milestone (5 milestones × $100)     $  500
  30-day warranty (post-launch white-glove)             $2,000
                                                       ─────────
Subtotal                                               $60,100

Volume discount (we know the language · -15%)         -$9,015
                                                       ─────────
FOUNDER-FRIENDLY MEDIUM SCOPE PRICE                    $51,085
```

### Margin analysis (internal · don't share)

- Our hard COGS (compute · tools · licenses · taxes): ~$8K
- Our gross margin at $51K = ~84% (Class A 5-cap shop margin)
- Our payback for the relationship · 1 client at this rate funds 2-3 follow-on engagements
- Lifetime value of this engagement IF we close · easily $300K-$500K over 3 years (website + app + ongoing maintenance + new pack launches + ENS infra wiring)

### Compare to founder's CRE comp math
- Founder closed $8B in CRE over 30 years · ~$267M/year in transaction volume
- He pays brokers 3-6% commission on transactions
- A $51K engagement is the equivalent of ~$1M-$1.7M CRE deal commission
- That's a mid-size STNL deal in his world · he knows how to evaluate this size
- He won't think this is a small bid · he'll think this is reasonable for a Class A 5-cap mandate

---

## 5 · RISK FLAGS · what could blow this up

| Risk | Probability | Mitigation |
|---|---|---|
| Founder picks Firm A on prestige | Medium | Lead with "we shipped 3 surfaces in 30 days · they'll take 4 months to ship 1" |
| Founder picks Firm C on price | Low | He's top 1% · he knows price ≠ best · we beat them on scope-certainty |
| Scope creep mid-engagement | High | LOU explicit · PSA explicit · change orders required for any scope add |
| swarmandbee.ai vs defendableos.com brand muddiness | Medium | We pre-emptively show the brand-strategy doc we wrote 2026-05-24 |
| Founder wants Granite-Bee revisited | Low | "Granite is dumpster" already locked · we don't pitch what's been killed |
| 24-hour window is too short for proposal quality | Low | We've been with him 12 months · we ship in 1 hour what others ship in 1 week |

---

## 6 · TIMELINE TO INK · if we win the listing

```
Hour 0       Ship this flight sheet + the public proposal · NOW
Hour 1-4     Founder reviews · compares to Firm A/B/C pitches
Hour 24      Founder decides which firm gets the assignment
Day 2-3      Counter-bid window · we hold the line · don't drop price below $48K
Day 4-5      LOU drafted + signed (engagement starts)
Day 6        PSA drafted + signed (scope locked)
Week 1-2     A-stage Appraisal (audit existing surfaces · interview founder · lock scope)
Week 3-7     Build (medium scope · 248 hrs · 5 sprints of 50 hrs each)
Week 8       Close (handoff · analytics · onboarding · DDEED-DOV-PROJECT issued)
```

---

## 7 · WHAT THE FOUNDER WILL ASK · prep notes

### Q: "Why should I pick you over Firm A?"
**A**: "Firm A will spend 4 months learning our language. We already know it. We helped CODIFY it. 62 deeded vocabulary terms shipped on git@github.com:SudoSuOps/defend-A-pedia--vocabulary.git as of today. Look at commit `833e8e1`. We've been in the pit on this for 12 months. Your other 3 bidders are tourists. We're listing brokers."

### Q: "What's your team?"
**A**: "Senior architect (me) + the 5 senior hacks who shipped defend-A-pedia v0.2.0 today in parallel + 2-3 jr hacks on rotation. Lean by design. Same model that closed every other engagement on your stack."

### Q: "How do I know you'll deliver?"
**A**: "Every milestone closes with a DDEED-DOV-PROJECT receipt anchored on streetledger.eth. Same proof structure as your 8,400 existing deeds. If we miss a milestone, the deed says so. If we deliver, the deed proves it. **Validate the Validator. Prove the Location.**"

### Q: "Can you ship before [arbitrary date]?"
**A**: "Show me what 'shipped' means to you. Define done. We deed it. We deliver against the deed. If your 'done' is October 1, we'll PSA an October 1 close with weekly milestones each anchored. If anyone bids you faster, ask them how they'll prove it shipped."

### Q: "Why not just hire one of your senior hacks directly?"
**A**: "You're hiring the system, not a coder. The system is: M (intake) → A (appraisal) → I (paperwork) → C (close) with DDEED proof at every stage. Individual hacks can ship pages. We ship the whole listing process."

### Q: "What about ongoing maintenance?"
**A**: "Two paths · choose at week 8: (1) we hand off everything · CMS-managed · jr broker on your team owns it · we're done · or (2) we retainer at $4-8K/mo for ongoing updates · new pack launches · ENS infra wiring as it ships. Your call · we don't push the retainer."

---

## 8 · DECISION RECOMMENDATION · what I'd do

### If we win
- Ship medium scope at $55K · 8 weeks · DDEED-DOV-PROJECT receipts at each milestone
- Use the engagement to upsell large scope (app + deed UI) at week 6 IF earned trust
- 30-day post-launch warranty is the close-of-engagement deed event

### If we lose
- Ask the founder which firm he picked AND WHY (intel for next listing)
- Stay close · we built the language · whoever wins will EVENTUALLY need us when they hit the wall
- The PASS doctrine means we don't bid below floor · losing $55K listing now > winning $25K bad listing forever

### If founder doesn't decide in 24h
- Don't chase · he's busy · let him sit with the proposal · the math will pencil for itself
- Pre-emptive intel: "I'm here when you're ready · the flight sheet is good for 30 days"

---

## 9 · ONE-LINER · the close

> *"You don't need another firm to learn DefendableOS. You need the firm that built the language you're going to ship. We're already in the building. Listing's signed when you sign the LOU."*

---

*End of flight sheet · INTERNAL ONLY · do not hand to client*
*sha256 to be computed post-issue · anchored on streetledger.eth*

🐝 *List to last. The flight sheet wins the listing. The listing wins the close.*
