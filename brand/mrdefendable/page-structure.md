# Mr. Defendable · Page Structure · mrdefendable.com

> *The 8-page site architecture · per founder spec · 2026-05-24*

---

## The 8 Pages (LOCKED · founder-proposed)

```
mrdefendable.com
│
├── /                       Home · the principal landing · 90-sec test
├── /from-the-desk          Trust memos · operator notes · "from the desk of Mr. Defendable"
├── /flight-sheets          Internal-grade flight sheet samples · operator discipline
├── /tribunal               Adjudication notes · verdict explanations
├── /street-ledger          Books and records · publicly browsable receipts/deeds
├── /defend-a-pedia         Language constitution · 62+ DDEED-VOCAB
├── /request-proposal       MAGIC funnel intake · principal contact
├── /board-room             Board presentations · institutional-grade memos
└── /assignments            Active + completed disposition / build / repair assignments
```

---

## Page Specifications

### `/` · Home (the principal landing)

**Purpose**: pass the 90-second principal test. A CFO sees the page · understands what Mr. Defendable does · in 90 seconds or less.

**Hero**:
```
[Photo or stylized avatar]
"Ring ring — Mr. Defendable speaking."
Trusted operator layer for AI defense, dispositions, and proof.
[CTA: Request a proposal · Read From the Desk]
```

**Sections**:
1. Hero (above the fold · 90-sec principal test)
2. What I do (3-card grid: disposition brokerage · trust infrastructure · operator advisory)
3. Recent assignments (3 anonymized teasers · with DDEED-anchored proof links)
4. 5 Proofs strip (Origin · Quality · Process · Economics · Trust · footer)
5. The brand stack (link to defendableos.com · streetledger.eth · etc.)
6. Contact / Make the dial

**Components**: hero · 3-card grid · assignment teaser strip · proofs strip · brand-stack grid · contact CTA

---

### `/from-the-desk` (Trust memos)

**Purpose**: the recurring publication slot · "Mr. Defendable's Board Notes." First-person operator commentary · CRE-broker cadence · specific deals + specific receipts.

**Layout**:
- List of memos (most recent first)
- Each memo: title · date · short excerpt · DDEED-anchor link · "read" button
- Sidebar: subscribe (Resend opt-in) · archive by month

**Content seed (first 3 memos)**:
1. *"On taking offense to the shed"* (the offense-vs-defense doctrine · positioning piece)
2. *"What a 5-cap actually looks like in trust infrastructure"* (translating CRE pricing to AI defense)
3. *"Books and records are not optional"* (the proof-layer thesis · receipts > vibes)

Each memo signs off: *"To the shed. — Mr. Defendable"*

---

### `/flight-sheets` (Operator artifacts)

**Purpose**: sample internal-grade flight sheets. Show the operator-discipline behind the brand. NOT marketing pages · actual artifact samples (redacted/anonymized where confidential).

**Layout**:
- Grid of flight sheets · each with thumbnail + summary
- Click → embedded PDF viewer + DDEED hash + brief operator commentary

**Initial population**:
- `00_PRE-MARKET_FLIGHT_SHEET.pdf` (from defend-A-pedia repo · anonymized version)
- BOV sample
- Buyer profile sample (from 08 · redacted)
- 1031 upleg buy box template

Each flight sheet shows the structure · not the secret sauce. The DDEED anchor proves provenance.

---

### `/tribunal` (Adjudication transparency)

**Purpose**: surface the Tribunal's verdict logic. Show what was judged · how it was judged · what failed · what was repaired.

**Layout**:
- Recent verdicts feed (latest 20)
- Each verdict: input summary · Honey/Jelly/Propolis tier · key reasoning · DDEED hash
- Filter by tier · by date · by domain
- "How the Tribunal works" sidebar (links to /defend-a-pedia entries for validator-weight · trust-temperature · etc.)

**Includes false-honey incident reports** · the most honest content on the internet.

---

### `/street-ledger` (Books and records)

**Purpose**: publicly browsable receipts + deeds. The institutional-confidence layer. Every deed resolves to a Hedera anchor.

**Layout**:
- Searchable + filterable ledger of all DDEED-* records
- Columns: DDEED ID · type · date · hash · Hedera link · ENS path
- Export to CSV / JSON / N-triples
- Live counter: total deeds · total Royal Jelly · last anchor timestamp

**Sources from**: streetledger.eth ENS path · Hedera HCS topic `0.0.10291838`

---

### `/defend-a-pedia` (Language constitution)

**Purpose**: surface the 62+ DDEED-VOCAB terms. Each term: definition + example + cross-references + DDEED proof.

**Layout**:
- Category navigation (CRE · Hive · Tribunal · Repair · DefendableOS · Scoring · Client)
- Per-term page: definition · usage example · related terms (cross-link graph) · DDEED ID · founder voice notes
- Search · alphabetical index · graph view of cross-links

**Sources from**: this repo (`docs/vocabulary/`) · defendapedia.eth

---

### `/request-proposal` (MAGIC funnel intake)

**Purpose**: principal-direct contact. NOT a chat widget. NOT a generic contact form. Specific qualification questions · PASS doctrine applied.

**Form fields** (qualifying · not generic):
- Who is the principal contact (name + role)
- What is the asset / engagement (1-2 sentences)
- What is the timeline pressure (days · weeks · months)
- What is the budget reality (range · band)
- What is the trigger event (incident · regulatory · M&A · etc.)
- How did you find Mr. Defendable (channel)

**Submit** → Resend → `proposal@mrdefendable.com` → Proton inbox routing → 24-hr response SLA.

Auto-reply mirrors operator voice: *"Ring ring — Mr. Defendable speaking. I'll review your intake within 24 hours and either make the dial or pass cleanly with referrals. To the shed."*

---

### `/board-room` (Institutional artifacts)

**Purpose**: board presentation library. CONFIDENTIALITY DISCIPLINE per `09_GO_TO_MARKET_STRATEGY.md`.

**Layout**:
- Library of public-tier board memos
- Each artifact: title · date · DDEED hash · download link (PDF)
- Sidebar: confidential artifacts (auth-gated · ENS-keyed access)

**Public tier examples**:
- "DefendableOS Listing Package · 11-document overview"
- "Class A 5-cap board pitch · the comp-set framework"
- "1031 upleg parallel-track strategy"

**Confidential tier** (auth required):
- Per-engagement materials
- Active deal flight sheets
- Buyer-pool deep dives

---

### `/assignments` (Active + completed work)

**Purpose**: track record · public proof of execution. Each assignment with DDEED-anchored receipts.

**Layout**:
- Filter: active · completed · all
- Filter: by asset class (CRE · IP · platform · etc.)
- Filter: by Honey/Jelly/Propolis classification (post-completion)
- Per-assignment card: principal (anonymized if required) · asset class · scope · current status · DDEED links · close timeline

**Card example**:
```
Assignment: DefendableOS Disposition
Principal: [confidential during process]
Asset class: AI defense protocol
Scope: Exclusive listing + 1031 upleg advisory
Status: Pitching arc complete · execution arc begun · LOU pending
DDEED: AWARD-DOS-001-v1 (anchor pending)
Started: 2026-05-24
Target close: 2027-05-24 (12-mo exclusive)
```

---

## Build Stack (consistent with existing defendable surfaces)

| Layer | Choice |
|---|---|
| Framework | Vite + React 18 + TypeScript + Tailwind 3 |
| Routing | react-router-dom 6 |
| Hosting | Cloudflare Pages |
| Email | Resend → Proton inbox routing (`proposal@mrdefendable.com`) |
| Auth (for confidential artifacts) | ENS-keyed (per founder doctrine) + magic-link fallback |
| Object storage | streetledger.eth path + Tigris S3 fallback |
| PDF viewer | Embedded (for flight sheets · board memos) |
| Search | Local fuzzy (Fuse.js) for vocabulary · server-side for ledger |
| Analytics | Plausible (privacy-first · operator-grade) |

---

## SEO / GEO / llms.txt

- Sitemap.xml: all 8 routes + sub-routes (memos · verdicts · deeds · terms · assignments)
- llms.txt: brand positioning + voice-rule extract + cross-references to defendableos.com / defendapedia.eth / streetledger.eth
- OG / Twitter cards: each page has Mr. Defendable avatar + signature opening line
- Schema.org: Person markup for Mr. Defendable · Organization markup for DefendableOS / Swarm and Bee LLC

---

## Confidentiality Discipline (carried from listing-package doctrine)

| Surface | Public | Confidential (ENS-auth) |
|---|---|---|
| `/` · home | ✅ | |
| `/from-the-desk` | ✅ | |
| `/flight-sheets` | ✅ (redacted samples) | ✅ (full client-grade) |
| `/tribunal` | ✅ (anonymized verdicts) | ✅ (per-engagement detail) |
| `/street-ledger` | ✅ (all DDEED records) | |
| `/defend-a-pedia` | ✅ | |
| `/request-proposal` | ✅ (form) | (responses confidential) |
| `/board-room` | ✅ (public memos) | ✅ (per-engagement materials) |
| `/assignments` | ✅ (track record) | ✅ (active-deal detail) |

---

## Implementation Roadmap (4 weeks)

### Week 1 · Foundation
- Provision CF Pages + DNS for mrdefendable.com
- Scaffold Vite + React + TS app
- Build `/` home (90-sec principal landing)
- Build `/from-the-desk` (first 3 memos drafted)
- Wire Resend → Proton inbox routing

### Week 2 · Trust layer
- Build `/flight-sheets` (5 sample artifacts)
- Build `/tribunal` (sample verdicts)
- Build `/street-ledger` (live DDEED browser)

### Week 3 · Vocabulary + Intake
- Build `/defend-a-pedia` (62 DDEED-VOCAB browsable)
- Build `/request-proposal` (MAGIC funnel intake)
- Wire to existing contact infra

### Week 4 · Boardroom + Assignments + Ship
- Build `/board-room` (memo library + auth-gated tier)
- Build `/assignments` (track record + active-deal view)
- SEO / GEO / llms.txt
- Founder voice review (V03 chain pass on every page)
- Deploy

### Phase 5 (downstream) · Communicator Integration
- Wire Mr. Defendable as human-readable interface to DefendableRouter intake
- Communicator translates Mr. Defendable conversations → structured directives
- StreetChat captures · StreetLedger preserves · Tribunal grades
- Mr. Defendable becomes the principal LLM persona for the 5-rail stack

---

## Cross-references

- `README.md` (brand architecture overview)
- `voice-guide.md` (voice / tone / cadence discipline)
- Memory: `mrdefendable-brand-architecture-voice-doctrine-2026-05-24`
- Existing brand surfaces to align with: `defendableos.com` · `defendablecloud.com` · `defendablerouter.com` · `defendapedia.eth`
- The 11-artifact listing package this surface will reference: `proposals/defendableos-website-app/`

---

🐝 *Ring ring — Mr. Defendable speaking. To the shed.*
