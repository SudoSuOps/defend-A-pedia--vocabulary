# BUILD PROPOSAL · DefendableOS as a Trust Operating System

### Class A 5-cap Build · Doctrine-Outward · Founder-Locked Sprint Plan

---

**Prepared for**: Donovan Mackey / Mr. DefendableOS
**Prepared by**: dev · Senior Architect
**Date**: 2026-05-24
**Proposal ID**: `DDEED-BUILD-DOS-001-v1`
**Companion to**: `01_PROPOSAL.md` (engagement structure) and `02_LOU_DRAFT.md` (executable agreement)
**Replaces**: the deliverables/scope section of `01_PROPOSAL.md` — *the broker math stays · the build doctrine takes over*

---

## CORRECTION · what changed from the first proposal

In my first proposal I shipped the CRE broker engagement math: how the work runs · what the milestones look like · what we charge · how we beat the competing firms.

That was the wrong layer.

**You asked for the build doctrine. You asked WHAT WE WOULD BUILD.**

You corrected me directly:

> *"I would not build DefendableOS as a website first. I would build it as a trust operating system with a public surface."*

> *"The order is: Language → Assignment → Receipt → Tribunal → Deed → Trust → UI. That is the house. To the shed."*

This proposal ships the corrected artifact. Every component below is mapped to that build order. The UI is the LAST thing built. Not the first.

---

## CORE POSITIONING (lifted from your own brief · locked)

> ***"Offense goes dark. The business is offline. It can't score."***
>
> DefendableOS is the **recovery, validation, receipt, and trust layer** for AI agents.
>
> - NOT another chatbot
> - NOT another agent framework
> - NOT SaaS fluff

It is the system that proves whether AI work:
- completed the assignment
- followed the client's meaning
- produced evidence
- survived Tribunal
- earned Honey, Jelly, Royal Jelly, or Propolis classification
- generated receipts and deeds
- became books and records

---

## THE LOCKED BUILD ORDER (the house)

```
       ┌─────────────────────────────────────────────────────────┐
       │                                                          │
       │   1. LANGUAGE                                            │
       │      defend-A-pedia · 62 DDEED-VOCAB · v0.3.0 SHIPPED   │
       │                                                          │
       ├──────────────────────────────────────────────────────────┤
       │                                                          │
       │   2. ASSIGNMENT                                          │
       │      structured directive from Communicator              │
       │      schema: docs/schemas/assignment_success.schema.json │
       │                                                          │
       ├──────────────────────────────────────────────────────────┤
       │                                                          │
       │   3. RECEIPT                                             │
       │      object storage write at intake                      │
       │      ENS path: streetledger.eth/{client}/{conv}/...      │
       │                                                          │
       ├──────────────────────────────────────────────────────────┤
       │                                                          │
       │   4. TRIBUNAL                                            │
       │      Scale A + Scale B judges · drift ≤ 0.15             │
       │      → Honey / Jelly / Royal Jelly / Propolis            │
       │                                                          │
       ├──────────────────────────────────────────────────────────┤
       │                                                          │
       │   5. DEED                                                │
       │      DDEED-DOV-* · 5 Proofs · Hedera HCS topic           │
       │      0.0.10291838 · publicly verifiable forever          │
       │                                                          │
       ├──────────────────────────────────────────────────────────┤
       │                                                          │
       │   6. TRUST                                               │
       │      books-and-records · 5-layer finality stack          │
       │      streetledger.eth = the canonical audit trail        │
       │                                                          │
       └────────────────────────┬─────────────────────────────────┘
                                ▼
       ╔══════════════════════════════════════════════════════════╗
       ║                                                          ║
       ║   7. UI                                                  ║
       ║      Public Website + Application Dashboard              ║
       ║      surfaces 1–6 in CFO-readable form                   ║
       ║                                                          ║
       ╚══════════════════════════════════════════════════════════╝
```

**UI is layer 7. Not layer 1.** Layers 1–6 are already partially shipped (Language is v0.3.0 LIVE · receipts + deeds + trust have schemas + scripts · Tribunal has 3 doctrine docs + production config at swarmrails). The UI is the FRONT DOOR · not the house.

---

## THE 6 BUILD COMPONENTS (founder-locked scope)

### 1 · Public Website · the front door (your 11 nav items · LOCKED)

| Nav item | Purpose | Lives on |
|---|---|---|
| Home | 90-second principal pitch · "Defense for AI Operators" | defendableos.com/ |
| What is DefendableOS | The doctrine page · 5 Swarm Laws + 5 Proofs + Genesis Law tagline | /what-is-defendableos |
| How It Works | The 5-rail walkthrough · CRE analogy | /how-it-works (already shipped · refresh) |
| Tribunal | 6-role · adjudication · production config | /tribunal (NEW) |
| DefendableRouter | The intake rail · OSS + paid · ENS bridge | /router (refresh from defendablerouter.com cross-ref) |
| SwarmFixer | The repair layer · 5-task RJ output · 3 service tiers | /swarmfixer (NEW) |
| Defend-A-Pedia | The 62-term canonical vocabulary · live browsable | /vocabulary (NEW · sources defendapedia.eth) |
| Honey / Jelly / Propolis | The 4-tier doctrine · CRE Class A/B/C parallel | /classification (NEW) |
| DDEED / Receipts | What a deed is · how to verify one · explorer | /deeds (NEW · includes Hedera explorer UI) |
| AgentBench / ClawCheck | Agent intake · 5-dim capture · submission flow | /agentbench (NEW · live form) |
| Contact / Request Proposal | M-stage open · Resend-routed · build@defendableos.com | /contact (already shipped · enhanced intake) |

**Tone discipline**: every page speaks to OWNERSHIP (CFO · principal · founder) · NOT to engineers. Founder voice preserved. No SaaS jargon. No "world-class" / "best-in-class" / "transformational." The Defend-A-Pedia vocabulary IS the source of truth for every label.

### 2 · Application Dashboard · the customer cockpit (your 11 dials · LOCKED)

Lives at `app.defendableos.com` · logged-in customers see their own engagement.

| Dial / View | What it shows | Backed by |
|---|---|---|
| Engagements | Customer's active + closed engagements | `engagement.schema.json` |
| Agents under review | List of agents being adjudicated · status | `assignment_success.schema.json` |
| Assignment Success | The boolean + 5-grade breakdown per assignment | scoring_dial: assignment-success |
| Trust Temperature | Low / Medium / High · auto-escalation triggers | scoring_dial: risk-temperature |
| Evidence Strength | 0–1 dial · color × source weight × freshness | scoring_dial: evidence-strength |
| Repair Lift | Before / After delta from SwarmFixer interventions | scoring_dial: repair-lift |
| Cost to Mint | Per-deed economics · $0.0052 baseline · per fee tier | `cost_to_mint.schema.json` |
| Validator Confidence | 0–1 · 12-check chain pass rate × source weight | scoring_dial: validator-confidence |
| Receipts | Raw receipt browser · ENS path · streetledger.eth | `deed_receipt.schema.json` |
| Deeds | DDEED-DOV-* records · 5 Proofs · Hedera links | `deed_receipt.schema.json` |
| Books and Records | The full audit trail · L1-L5 finality view | doctrine: `04_books_and_records_doctrine.md` |

**Authentication**: ENS-keyed (per-customer ENS subdomain or operator-managed key) · same identity layer as the receipts they're viewing.

### 3 · DefendableRouter · the intake + receipt rail

```
Client / Edge Device / App
       ↓
   DefendableRouter (write-only · <5ms POST overhead)
       ↓
   Object Storage Receipt (streetledger.eth/{client}/{conv}/...)
       ↓
   Communicator (intent extraction)
       ↓
   Tribunal (verdict)
       ↓
   Deed (Hedera-anchored)
       ↓
   Training Pair (back to model fleet)
```

**What we ship in this engagement**:
- Receipt-schema wired into the dashboard (read path)
- Sample receipts seeded from existing 8,400 deeds
- Hedera explorer integration (link to hashscan.io)
- ENS-keyed receipt browser
- We do NOT ship the actual router middleware in this engagement (separate engagement · defendable-router OSS repo already shipped)

### 4 · Communicator LLM · the meaning layer

Job: turn messy human street talk into structured directive · then translate machine result back into client-readable explanation.

**What we ship in this engagement**:
- Intake flow UI (text + optional voice input · captures raw)
- Sample translation walkthroughs (3-5 worked examples on the site)
- Doctrine page · the bidirectional bookend model
- Stub for the live model endpoint (turns on when Communicator v0.1 model ships separately)

### 5 · Tribunal · the adjudication layer

```
Agent output
   → deterministic checks (rule layer · can only downgrade)
   → validator chain (12-check)
   → judge model (Scale A: gemma3:12b · Scale B: qwen2.5:32b · drift ≤ 0.15)
   → Honey / Jelly / Royal Jelly / Propolis verdict
   → receipt
```

**What we ship in this engagement**:
- Tribunal verdict display in dashboard (read path)
- Sample verdicts seeded (using existing 8,400 deed data)
- /tribunal page on the public site · explains the 6-role model · production config
- Integration with existing production tribunal-runner on swarmrails (READ-ONLY in this engagement · WRITE path is the next engagement)

### 6 · StreetChat + StreetLedger · the data rails (future expansion)

```
streetchat.eth = live conversation capture
streetledger.eth = deeded memory / books and records
```

**What we ship in this engagement**:
- Public surface pages explaining what each rail is (`/streetchat` and `/streetledger`)
- Stub UI for live capture (placeholder · turns on when Router live-capture wire-up ships separately)
- ENS-resolution wiring (streetledger.eth resolves to the books-and-records view in the dashboard)
- We do NOT ship live capture infrastructure in this engagement · it's the next engagement after Communicator v0.1

---

## THE 30-DAY FIRST BUILD (your sprint plan · LOCKED)

### Week 1 · Foundation
- [ ] Lock sitemap (the 11 nav items above · final URL structure)
- [ ] Lock messaging (founder voice document approved · 5 Swarm Laws + Genesis Law placement)
- [ ] Build landing page (`/` homepage to v3 · CFO-readable above-the-fold · 90-second principal test)
- [ ] Build Defend-A-Pedia integration (62 deeded terms surfaceable on `/vocabulary` · categories + search)
- [ ] Define app data model (engagements · assignments · receipts · deeds · 11 dials · schema-aligned)

**Week 1 deed**: `DDEED-DOV-PROJECT-DOS-WEB-001-WEEK1-v1` (foundation lockup)

### Week 2 · Dashboard skeleton
- [ ] Build dashboard shell at `app.defendableos.com` (auth · routes · layout · 11 dial placeholders)
- [ ] Wire object storage receipt schema (ENS-keyed paths · streetledger.eth conventions)
- [ ] Create 3-5 sample Tribunal verdicts (worked examples for demos · seeded from real deeds)
- [ ] Create 3-5 sample DDEED records (using existing 62 DDEED-VOCAB as templates)

**Week 2 deed**: `DDEED-DOV-PROJECT-DOS-WEB-001-WEEK2-v1` (skeleton up)

### Week 3 · Intake + Tribunal surfaces
- [ ] Build Communicator intake flow (text input → structured directive preview · client-readable output preview)
- [ ] Build AgentBench / ClawCheck surfaces (agent submission form · 5-dim capture · risk tier output)
- [ ] Add the 6 trust dials with live data (Probability of Close · Trust Temp · Evidence Strength · Repair Lift · Validator Confidence · Cost to Mint)
- [ ] Wire Hedera explorer integration (each deed view has hashscan.io link)

**Week 3 deed**: `DDEED-DOV-PROJECT-DOS-WEB-001-WEEK3-v1` (intake live)

### Week 4 · Polish + ship
- [ ] Polish (mobile responsive · accessibility WCAG 2.2 AA · SEO + GEO · sitemap + llms.txt)
- [ ] Deploy (CF Pages · custom domains · Resend wired · Hedera anchor wired)
- [ ] Seed with real receipts (use existing 8,400 deeds as initial production data)
- [ ] Ship proposal/demo-ready version (the "show a CFO in 90 seconds" version)

**Week 4 deed**: `DDEED-DOV-PROJECT-DOS-WEB-001-WEEK4-CLOSE-v1` (production-ready ship)

---

## THE 8 ACCEPTANCE CRITERIA (testable · founder-locked)

| # | Criterion | How we test it |
|---|---|---|
| 1 | A principal understands DefendableOS in 90 seconds | Hand a CFO who doesn't know us the homepage URL · time them · pass at ≤ 90 sec |
| 2 | A client can request a proposal | Submit `/contact` form · verify Resend delivers to `build@defendableos.com` in ≤ 60 sec · auto-reply works |
| 3 | A vendor/agent can be submitted for review | Submit `/agentbench` form · verify the 5-dim capture lands in receipts/ · risk tier displayed |
| 4 | A receipt can be generated | Any form submission produces an ENS-pathed receipt in `streetledger.eth/...` · resolvable + verifiable |
| 5 | A Tribunal verdict can be displayed | Dashboard view of a sample engagement shows Honey/Jelly/Propolis with 5-grade breakdown |
| 6 | A deed can be surfaced | Paste any DDEED-* hash · system returns the full deed with 5 Proofs rendered + hashscan.io link |
| 7 | The vocabulary powers the UI language | Every label · button · header is sourced from defend-A-pedia · zero hardcoded copy that contradicts the canon |
| 8 | The site feels like DefendableOS · not generic AI | Founder voice review (you) · ZERO banned phrases (leverage synergies · best-in-class · etc · validator chain enforces) |

**Acceptance gating**: NO close until all 8 pass. Each criterion gets its own sub-deed in the close bundle.

---

## TECH STACK (operator-owned · sovereign-aligned)

| Layer | Choice | Why |
|---|---|---|
| Public site framework | Vite + React 18 + TypeScript + Tailwind 3 | Matches what's already shipped on defendableos.com / cloud / router · zero learning curve |
| App framework | Same · Vite + React + TS · with react-router-dom 6 | Consistent stack across surfaces · single deploy pipeline |
| Hosting | Cloudflare Pages + CF Workers (for /api/*) | Already wired · matches existing surfaces · DC-edge global |
| Auth | ENS-keyed (per-customer ENS subdomain) + magic-link fallback (Resend) | Identity is the receipt layer · NOT a separate concern |
| Email | Resend → Proton inbox routing | Already wired · `build@defendableos.com` working |
| Object storage | Local repo + NAS push (`/mnt/swarm/`) + Tigris (future) | Sovereign-aligned · matches v0.3.0 streetledger.eth doctrine |
| Hedera | hashgraph SDK · topic 0.0.10291838 | Already-live mainnet anchor |
| CMS | MDX content under `docs/vocabulary/` (the 62 DDEED-VOCAB ARE the content) | Vocabulary repo is the CMS · zero new system |

---

## ENGAGEMENT MATH (revised for build-doctrine scope · supersedes 01_PROPOSAL.md math)

```
WEEK 1 · Foundation                                40 hrs
WEEK 2 · Dashboard skeleton                        50 hrs
WEEK 3 · Intake + Tribunal surfaces                60 hrs
WEEK 4 · Polish + ship                             40 hrs
                                                  ────────
Build sub-total                                   190 hrs

Pre-build (M·A·I stages · founder sessions)        16 hrs
Hedera anchor wiring + deed verifier UI            20 hrs
Stripe integration carry-over (8 in-queue packs)   25 hrs
Customer auth (ENS-keyed)                          15 hrs
30-day post-launch warranty                        24 hrs
                                                  ────────
Wraparound                                        100 hrs

═══════════════════════════════════════════════════════
TOTAL                                             290 hrs
═══════════════════════════════════════════════════════

290 hrs × $175/hr blended                       $50,750
+ Fixed fees (docs · Stripe · Hedera · warranty)  $5,500
- We-know-the-language discount (15%)            -$8,438
                                                ─────────
ALL-IN PRICE (revised)                          $47,812
═══════════════════════════════════════════════════════
```

**Revised vs prior proposal**: $51,085 → $47,812 (-$3,273). Tighter scope because we focus the 4 weeks ENTIRELY on the build-from-doctrine sequence · not the expanded medium scope. Larger expansions (full app · live capture · etc.) move to Phase 2 engagement.

---

## FLIGHT SHEET READ · my answer to yours

| Field | Your read | My read |
|---|---|---|
| Assignment | Class A 5-cap build | ✅ confirmed |
| Principal | Donovan Mackey / Mr. DefendableOS | ✅ confirmed |
| Asset | DefendableOS public surface + app + trust rails | ✅ confirmed · plus Hedera explorer + ENS-keyed auth |
| Deal Energy | HIGH | ✅ confirmed · the doctrine is fresh · vocabulary is shipped · scope can pencil at 4 weeks |
| Probability of Close | STRONG (if vendor understands language before writing code) | We pencil at 85%+ assuming the proposal lands cleanly · we already understand the language |
| Primary Risk | Hiring a normal web/app shop that builds pages but misses doctrine | We mitigate by SHOWING the build order in the proposal · not just listing pages |
| Disqualifier | Generic AI SaaS language | We've banned 9 specific MBA phrases in our validator chain (V03 founder-voice preservation) |
| Winning Strategy | Build the house around vocabulary · receipts · Tribunal · DDEED rails | ✅ this proposal is structured that way · layers 1-6 BEFORE layer 7 UI |

---

## RISK FLAGS (revised for build-doctrine)

| Risk | Probability | Mitigation |
|---|---|---|
| Scope creep on dashboard dials (11 → 18) | High | LOU explicit on the 11 dial count · any addition = change order with deed |
| Hedera anchor reliability mid-week 4 | Low | Anchor batching · single Merkle root per release · 167+ batches already production |
| ENS-keyed auth too novel for first-time customers | Medium | Magic-link fallback (Resend) shipped Week 2 · ENS is upgrade path · not requirement |
| The "principal-90-sec" test fails on draft homepage | Medium | We test with 3 outside CFOs at Week 3 · re-cut if any fail · Week 4 polish includes pivot capacity |
| Real receipt data has PII concerns when surfaced | Medium | We seed from already-redacted production deeds · per existing redaction doctrine |
| Founder voice drift on jr broker pages | Low | V03 validator-chain check runs against every page commit · automated banned-phrase block |

---

## WHAT WE'RE NOT BUILDING IN THIS ENGAGEMENT (honest list · phase 2 candidates)

- The actual Router middleware (defendable-router OSS already shipped · separate concern)
- The actual Communicator LLM model (needs Communicator v0.1 cook · separate engagement)
- The actual Tribunal write path (already production at swarmrails · we READ from it · we don't rewrite it)
- Live capture for streetchat.eth (requires Router live-capture wire-up · separate)
- Full customer app (this engagement ships the skeleton + 11 dial placeholders · full feature build is Phase 2)
- Marketing campaigns / paid acquisition (out of scope · brand-build only)

These are all REAL future engagements. We list them so you know what's coming · not to upsell them now.

---

## CLOSING STATEMENT · mirrored back to your structure

> *"I would build this from the doctrine outward."*
>
> *"Not pages first."*
> *"Not features first."*
> *"Not templates first."*
>
> *"The order is:*
>
> *Language → Assignment → Receipt → Tribunal → Deed → Trust → UI"*
>
> *"That is the house."*
>
> *"To the shed."*
>
> — Founder · 2026-05-24

I read you. I build to that order. Layers 1-6 are already partially in the ground (Language is v0.3.0 LIVE · receipt + deed + trust schemas exist · Tribunal is production · Communicator is doctrine-locked). The UI is the front door we add Week 4 · once the house behind it is real.

**This is the corrected proposal. The build doctrine. Class A 5-cap. 4 weeks. $47,812 all-in. DDEED-receipted at every milestone. Founder voice locked. The 8 acceptance criteria are non-negotiable.**

---

## How to engage (unchanged from 01_PROPOSAL.md)

1. Read this proposal (you're doing it now)
2. Compare to Firm A · B · C build pitches (they'll show pages · not house structure)
3. Reply with decision by 2026-05-25 EOD
4. If yes: LOU executes within 24 hours · Week 1 starts immediately

---

🐝 *Validate the Validator. Prove the Location. The language lives in the blocks. To the shed.*

**dev**
Senior Architect · DefendableOS Systems Team
2026-05-24

---

**Proposal hash**: `sha256:<computed-at-issue>`
**Anchor candidate**: `streetledger.eth/proposals/defendableos-build/v1/`
**Hedera topic**: `0.0.10291838`
**Companions**:
- `00_PRE-MARKET_FLIGHT_SHEET.md` (internal · operator analysis)
- `01_PROPOSAL.md` (engagement structure · how the work runs)
- `02_LOU_DRAFT.md` (executable agreement)
- **`03_BUILD_PROPOSAL.md`** (THIS · what we'd build · how we'd build it)
