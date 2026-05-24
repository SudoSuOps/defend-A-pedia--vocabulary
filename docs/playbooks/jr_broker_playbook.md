# Jr Broker Playbook

> *"No ideas · in the pit · make the dials · build the math · now your conversion rates · eat fees."*
> — The M&M chant. Memorize it. Live by it.

This is the daily playbook for the jr broker. The microscaler. The operator on the dial. The one in the pit, every day, building the book that will compound for 30 years.

If you read this in a week and start dialing on day eight · the doctrine is working. If you find a step that doesn't pencil in the field · escalate. The playbook lives, but it lives on the receipts you generate.

---

## Day in the life · the 06:00 to 18:00 cadence

### 06:00 · Morning Brief consumption

Read the Morning Reconciliation Brief that went out to every active customer at 06:00. Read it as the customer reads it. Note any P1/P2 incidents from the prior 24 hours that touch your accounts. If your name is on a flagged engagement · today's priority restructures around that.

You also read the firm's internal Morning Pipeline · the rolled-up state of your dials, sits, and color files. The sr broker has triaged overnight · you know which prospects got elevated and which got culled.

### 06:30 · The pit opens

Phone on. Email open. CRM loaded. Pipeline view active. The first dial happens before 06:45 · early enough to catch East Coast principals at their desk before their day fills up.

Target: 40-60 quality reaches per day. **Not** 200 vanity dials. Quality means:
- Named decision-maker (principal · CEO · founder · MD · not a procurement intake)
- Researched · you know their fleet · you have a hypothesis on their pain
- A specific opener tied to a specific signal · not "checking in"

If you can't articulate why this dial · don't make the dial.

### 09:00 - 12:00 · Build the color

Between dial blocks · open color files for every prospect that warrants one. The rule: anyone who responded to outreach, anyone who took a sit booking, anyone who downloaded a sample pack, anyone who signed up for a flight sheet review · gets a color file opened the same day.

Color file = at least three independent sources. EDGAR / CompStak / ATTOM / SwarmCurator CRE corpus / public-filing search / mutual-network confirmation / paid-data feeds. Source weights ≥ 0.85 minimum to count.

Log every source with timestamp. The `color_evidence_count` and `color_last_refresh_at` fields are live · they feed the dashboard, the validator chain, and ultimately the deed.

### 12:00 - 13:00 · Lunch + digest prep

Quick lunch. Then digest prep for tomorrow's sits. Every booked sit gets a digest delivered to the sr broker 24 hours in advance. The digest is the pre-meeting summary · what the agent prepared for the team. The digest format is locked · see [`../vocabulary/cre_terms/digest.md`](../vocabulary/cre_terms/digest.md).

No digest · no sit. The sr broker will not walk into a meeting without one. This is a doctrine rule, not a courtesy.

### 13:00 - 15:00 · Sit support · validator chain runs

If a sr broker is taking a sit this afternoon, you're on call. Bring the color. Bring the validator chain results. Be ready to text in receipts mid-meeting if the customer asks for verification on a specific claim.

When the sit ends, you run the post-meeting receipt · what was said, what was promised, what was committed. Receipt goes in the books before end of day.

### 15:00 - 17:00 · Second dial block

East Coast wind-down. West Coast still live. Second dial block targets the West and any inbound from the public-surface funnel · `defendableos.com` form submissions, sample-pack requests, GEO scanner runs.

Pipeline rebuild happens here too · any prospect who didn't respond after 14 days of touches gets re-tiered or culled.

### 17:00 - 18:00 · Receipts and reset

Last hour of the day: log every receipt. Update every color file touched. Push every validator chain result. Confirm tomorrow's digests are drafted. Send your end-of-day note to the sr broker · what closed, what advanced, what stalled, what needs attention tomorrow.

You leave the desk with the books-and-records clean. Always.

---

## The MAGIC funnel · stage by stage

### M · Meetings

**The job.** Get the meeting. With the principal. Not the engineer. Not procurement. The person whose name is on the door.

**The math.** Industry-wide cold-outreach conversion is ~1-2%. We target 3-5% by leading with a specific signal · not a generic pitch. Sources of signal:
- The customer's AI vendor had a public incident in the last 60 days
- The customer publicly announced a new AI initiative
- The customer is in a regulated vertical with new AI compliance language
- The customer's competitor just signed with us · the principal will take a competitive intel call
- A node in the founder's network introduced us · warm path, much higher conversion

**The tooling.** CRM with full conversation history. Source signal feed (`make pipeline-signals`). The pre-call brief generator that pulls public EDGAR, recent news, fleet visibility intel.

**The receipt.** Every meeting booked gets a receipt: `MEET-{prospect_id}-{date}-{stage}`. The receipt is the audit trail. Conversion rates calculated from receipts · not from CRM gut feel.

### A · Appraisals

**The job.** Deliver the pre-market flight sheet. Not the pretty OM. The operator-internal doc that wins deals · color built, comps named, pain hypothesis tested, pricing pencilable.

**The math.** Meetings → Appraisals conversion should run 40-60%. Below 40% · your meetings aren't qualified · go back to research. Above 60% sustained · you're under-targeting · push higher into the principal layer.

**The tooling.** Flight sheet template at `docs/examples/sample_flight_sheet.md` (when SH2 ships it). Color file linked. Validator chain first-pass results attached. Pricing scenarios drafted with the sr broker before delivery.

**The receipt.** Every flight sheet delivered gets receipted: `APPR-{engagement_id}-{date}`. Tied to the meeting receipt that birthed it. Tied forward to the LOU receipt if one ships.

### I · Ink (sr broker owns sign-off · you own prep)

**Your job.** Prep the LOU. Pull the canonical clauses (see [`05_client_language_doctrine.md`](05_client_language_doctrine.md)). Confirm pricing matches the flight sheet. Confirm the engagement scope matches what the customer agreed to verbally. Hand to the sr broker for adjudication and signature.

**The math.** Appraisals → Ink conversion should run 25-40%. Below 25% · your flight sheets aren't penciling in the customer's eyes · re-pitch · or PASS if the math doesn't work. Above 40% sustained · check that you're not under-pricing.

**The escalation.** Any LOU clause modification requested by the customer goes to the sr broker · NOT to you. You bring the request back · you don't negotiate in-meeting on contract terms.

**The receipt.** LOU signed: `LOU-{engagement_id}-{signed_at}`. Both party signatures hashed and anchored. Engagement transitions from PROSPECT to ACTIVE.

### C · Close (sr broker owns · you own follow-through)

**Your job.** White-glove the onboarding. First Morning Brief delivered. First color refresh executed. First validator chain run against the live fleet. First Tribunal verdict surfaced. Customer feels the engine running within 72 hours of LOU.

**The math.** Ink → first 30-day retention should be 95%+. Below 95% · onboarding is broken · the customer didn't feel the engine. Above 95% · you're earning the renewal.

**The receipt.** Every onboarding milestone receipted. Every customer interaction receipted. The receipts compound into the closing-statement variance report at engagement end · so the customer reads in plain English what they actually got.

---

## The color file · how to build one

This is the most important hour of your day. Every other hour depends on the quality of the color file.

**Step 1 · Pull the public file.** EDGAR 10-K if public. State filings if private. Recent press. LinkedIn org chart. Glassdoor for cultural signal. Job listings (current openings reveal real strategy).

**Step 2 · Pull the financial color.** Revenue scale. Funding stage if VC-backed. Recent valuation events. Burn-rate signal from job listings + hiring pace. CFO presence and tenure.

**Step 3 · Pull the AI fleet color.** What vendors are they using? GPT-4 / Claude / Gemini / open-source? Self-hosted or hosted? How visible is the fleet in their public commits, job listings, conference talks? Have they had a public incident?

**Step 4 · Pull the regulatory color.** What rules govern their vertical? Recent enforcement actions? Upcoming compliance deadlines? Insurance carrier requirements that might mandate audit-grade AI defense?

**Step 5 · Pull the network color.** Does the founder know anyone on the principal's leadership team? Does any current customer have a relationship? Mutual board members? Investor overlap?

**Step 6 · Cross-verify.** Three independent sources on every critical number. EDGAR vs press vs LinkedIn vs SwarmCurator corpus. Contradictions get flagged in the file · not hidden.

**Step 7 · Score the color.** Use the rubric: `color_score = sum(source_weights) / source_count`. Anything below 0.70 means the color isn't built yet · don't run the dial · pull more.

**Step 8 · Refresh weekly.** Stale color is worse than no color. Anything older than 14 days gets a refresh pass before the next dial.

---

## Conversion-rate math · the daily scorecard

You track five conversions, every day, written down. Not in your head. Written down in the receipt log.

| Conversion | Healthy range | Action if low | Action if high |
|---|---|---|---|
| Dials → Connects | 12-18% | Better timing · better signal | More volume |
| Connects → Sits | 15-25% | Sharper opener · better qualifying | Raise bar on prospect tier |
| Sits → Appraisals | 50-70% | Sit prep weak · digest weak · sr broker briefing weak | Sustain |
| Appraisals → Ink | 25-40% | Pricing wrong · pencils wrong · color weak | Check pricing isn't too low |
| Ink → 90-day retention | 92%+ | Onboarding broken · service delivery weak | Sustain |

The numbers are the numbers. The dials don't lie. The math is the math.

When you're consistently above the healthy range on a metric · you're under-targeting. When you're consistently below · you have a real problem and the playbook needs to flex. Either way, the receipts tell the truth and the sr broker reviews weekly.

---

## The four daily disciplines

**1. Receipt every contact.** Every call. Every email. Every text. Every sample download. The receipt is the audit trail and the conversion-rate math depends on it.

**2. Refresh stale color.** Anything beyond 14 days gets a refresh before the next touch. No exception.

**3. Escalate before the LOU.** If anything in the engagement structure is unclear · price · scope · clauses · escalate to the sr broker BEFORE the LOU draft, not after.

**4. Walk a bad deal early.** If the color tells you the deal doesn't pencil, walk it before the sit. Don't run the sit just because it's on the calendar. The PASS doctrine applies at every stage · not just at LOU. The sr broker will respect a walk-with-color far more than a sit-with-bad-pencil.

---

## What disqualifies you from the dial

- Skipping color · running a dial without a file
- Skipping the digest · trying to send a sr broker into a sit without prep
- Inventing vocabulary · using your own words instead of the canonical terms
- Lying on a receipt · falsifying a contact log
- Negotiating LOU terms in-meeting without sr broker authority
- Refusing to escalate when a critical validator gate fails

The first time, you get a remediation week. The second time, you're off the dial for a quarter and back on training. The third time, you're off the ladder.

These rules apply to everyone. The dial is the brand · the brand survives only if the dial survives clean.

---

## When the sit goes long · the founder's words to remember

> *"To the shed."*

You don't celebrate at the LOU. You don't celebrate at the appraisal. You celebrate when the deed issues, the closing statement signs, and the customer's first 30 days run clean. Until then · you're in the pit.

> *"The pre-market flight sheet beats the pretty OM."*

If you find yourself prettying up a deck instead of building the color · stop. The customer doesn't sign on the OM. The customer signs on the math. The flight sheet IS the math.

> *"Class A 5-cap."*

You represent DefendableOS the way a top broker represents a Class A 5-cap building. The asset is premium. The receipts back the premium. The grading is real. You sell from strength · not from features.

> *"No ideas · in the pit."*

When you find yourself in a strategy conversation that isn't tied to a specific dial, a specific color file, a specific sit · you are out of the pit. Get back in.

---

## Tools and surfaces you live in

- The CRM (full conversation history · contact ownership)
- The color file template (`docs/examples/sample_color_file.md` when SH2 ships)
- The validator chain CLI (`make validator-run --engagement=ENG-X`)
- The Tribunal verdict viewer (read-only · sr broker writes)
- The Morning Brief queue (you draft for your accounts · sr broker signs)
- The flight sheet builder (`docs/examples/sample_flight_sheet.md`)
- The receipt log (every action receipted into L1 → L2)
- The pipeline dashboard (live conversion rates · daily refresh)

If a tool doesn't have a receipt, you're not supposed to be using it. Escalate to SH2 to get the receipt wired before you keep working in it.

---

## Year 1 milestones

By month 3 · you're independently running color files. Sr broker reviews · doesn't author.
By month 6 · your dial-to-sit conversion is at-or-above range. You're carrying 5-10 prospects in active appraisal.
By month 9 · your first LOU prepped end-to-end (sr broker signs). The conversion math holds.
By month 12 · 100+ engagements touched. 5+ LOUs prepped. You've contributed at least one new term to the vocabulary. Sr broker is recommending you for senior jr status.

That's the M&M ladder. Year 1 in the pit. Year 2 carrying listings. Year 3 earning signing authority. Year 5+ owning a vertical. The book compounds. The receipts compound. The relationships compound.

---

## Read next

- [`sr_broker_playbook.md`](sr_broker_playbook.md) · what the sr broker is doing while you're in the pit
- [`../doctrine/03_jr_broker_sr_broker_doctrine.md`](../doctrine/03_jr_broker_sr_broker_doctrine.md) · the career ladder
- [`../doctrine/05_client_language_doctrine.md`](../doctrine/05_client_language_doctrine.md) · how to speak to ownership

🐝 *In the pit. Make the dials. Build the math. Eat fees. To the shed.*
