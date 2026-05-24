# Deal Digest Playbook

> *"The pre-market flight sheet beats the pretty OM. Every time. The OM gets the meeting. The flight sheet wins the deal."*
>
> — Founder · 2026-05-24

---

## Purpose

A **deal digest** is the pre-meeting brief a broker writes before any material principal touch. It's the internal operating document that captures everything the broker knows about the engagement · the assignment · the principal · the open issues · the dial · the recommended path. The principal never sees the raw digest · they see the WALK of it.

This playbook is how to write one. The format. The cross-references. The MAGIC funnel stage adaptations. The output is 1-2 pages · NEVER more · always shorter when possible.

The discipline: **if the broker can't write the digest in 30 minutes · they don't know the deal well enough to take the meeting.**

---

## When to write a digest

Every material principal touch gets a digest. "Material" means:

- First discovery call (Meetings stage)
- Color-build sync (Appraisals stage)
- LOU walkthrough (Ink stage)
- Quarterly business review (in-flight)
- Closing statement walk (Close stage)
- Any sr broker → principal call triggered by the dial moving 2+ bands
- Any founder-level escalation call

If it's just a weekly Morning Brief update · the brief IS the digest. No separate doc needed.

---

## The 8-section format

Every digest has 8 sections · in order · always. Skipping a section is acceptable IF the section has nothing material to report · but the section header stays (with "n/a · no material change since [date]") so the missing section is visible · NOT silently dropped.

### 1. Meeting metadata

- Meeting type · meeting date · meeting time · attendees (with role)
- MAGIC stage (M · A · G · I · C)
- Who's running the meeting · who's the principal contact

### 2. Engagement context

- Engagement ID · LOU date · tier (T1/T2/T3/T4) · current assignment(s) in flight
- Last 3 Morning Brief dial values · last close (if any) · last failure (if any)
- Principal's stated top-3 priorities (in their language · NOT translated to our doctrine)

### 3. Color summary

- Sources count · most recent refresh · any active contradictions
- Any color change since last digest
- Color gaps that need closing before the meeting

### 4. The dial

- Current Probability of Close · band · 7-day trajectory
- Top 2 drivers moving the dial in either direction
- The escalation status (if any)

### 5. Open items

- Action items from the last meeting · status · owner · ETA
- New action items the broker plans to propose
- Anything the principal asked us for that isn't yet delivered

### 6. The walk

The literal sentence-by-sentence walk the broker plans to give. Bullet form. Includes:

- The opening sentence (the truth the broker leads with)
- The 2-3 talking points (drivers · numbers · variance)
- The proposed next step (call to action)
- The fallback if the principal pushes back on the next step

### 7. PASS check

A sentence answering: *"Is there anything in the current state of this engagement that should trigger a PASS-pivot conversation?"*

If yes · the digest names what · and proposes how to surface it with the principal (now · at next milestone · or after the close).

### 8. Cross-references

- Links to receipts · deeds · LOU sections · prior digests · Morning Briefs
- Schema fields the broker should be ready to reference if asked
- The names of any internal stakeholders the broker might pull into the meeting

---

## Adaptations by MAGIC stage

The 8-section format is constant. The emphasis shifts by stage.

### Meetings stage digest

- **Heavy on color section** (we're building it)
- **Light on dial** (no dial yet · note "pre-engagement · no dial")
- **Heavy on walk** (the first conversation sets the tone for everything)
- **Mandatory PASS check** (early PASS saves 60 days of effort)

### Appraisals stage digest

- **Heavy on color section** (color file should be reaching maturity)
- **Light on dial** (dial spins up only after LOU)
- **Heavy on open items** (diligence questions outstanding)
- **Mandatory PASS check** (this is the canonical PASS window)

### Ink stage digest

- **Heavy on LOU sections** (the broker should walk specific clauses)
- **Heavy on the cost-to-mint walk** (CFO is in the room)
- **Heavy on success criteria** (these become the assignment contract)
- **Light on dial** (still pre-engagement)

### In-flight digest (Quarterly Business Review)

- **Heavy on the dial** (it's the lead artifact)
- **Heavy on cost-to-mint actual vs ceiling**
- **Heavy on assignment success trajectory**
- **Heavy on next-quarter proposal**

### Close stage digest (closing statement walk)

- **Heavy on the boolean** (CLOSED · HONEY / CONDITIONED / FAILED · RECOVERABLE / FAILED · DARK)
- **Heavy on the 5-grade breakdown**
- **Heavy on variance vs contract** (per success criterion)
- **Heavy on next-assignment proposal OR graceful exit**

---

## Cross-references the broker MUST be ready to pull

The principal will ask questions in the meeting. The broker should know the answer · OR know where to pull it in 60 seconds. The digest names the source for each likely question.

| Likely question | Source |
|---|---|
| "Show me the dial trajectory" | Last 4 Morning Briefs · dashboard URL |
| "What does our last close say?" | Closing statement deed ID · DDEED resolution path |
| "What's our cost running at?" | 30-day rolling cost-to-mint in dashboard · last 3 invoice line items |
| "How does this compare to similar engagements?" | Comp set in the dial driver #5 · sanitized · 3-5 examples |
| "Why did you make this recommendation?" | The PASS check section · the color file · the dial drivers |
| "What does our LOU say about [X]?" | Specific LOU section · with clause number |
| "Where's the Hedera anchor for [deed]?" | Deed ID → resolution path → topic ID + consensus timestamp |
| "Can you walk us through the math?" | Cost-to-mint 7-component breakdown · per-deed |

The broker who fumbles a likely question loses confidence faster than the dial ever could. The digest is the cheat-sheet that prevents the fumble.

---

## What goes in the digest · and what stays OUT

### In

- Operator's interpretation of the principal's signals
- Color-file source citations
- The dial · the bands · the drivers
- The cost math
- The proposed walk
- The PASS check
- Cross-references and schema fields
- Internal coordination notes (who else to loop in)

### Out

- Internal team gossip (keep it professional · digests get reviewed)
- Marketing language ("synergies" · "best-in-class" · etc · the founder's vocab lock applies)
- Speculation presented as fact (always tag uncertainty explicitly: "we believe" · "color suggests" · "unconfirmed")
- PII the principal didn't share with us in writing
- Any field that's not auditable back to a source

---

## The 30-minute timer

Discipline rule: the broker should be able to write a digest in 30 minutes. If it takes longer:

- **The engagement isn't well-instrumented** (Morning Briefs aren't doing their job · dashboard isn't pulling) → fix the instrumentation
- **The broker doesn't know the deal well enough** (last touch was too long ago · color is stale) → re-touch first · digest second
- **The deal has accumulated debt** (open items have been piling up) → run a debt-cleanup session before the meeting

The 30-minute timer is the canary. When it goes off · stop and fix the underlying issue · don't push through.

---

## A worked example structure

```
DIGEST · Q3 QBR with Acme Logistics (principal: J. Smith · COO)
Meeting: 2026-06-15 · 14:00 ET · 60 min · Zoom

1. METADATA
   MAGIC stage: In-flight · QBR
   Engagement: ENG-DOV-LOGISTICS-ACME-0001 · T3 White-Glove · LOU 2026-03-12
   Running: Sr broker (J. Reyes) · Founder (D. Mackey) cc'd

2. CONTEXT
   Active assignments: 2 (refund-decision · invoice-reconciliation)
   Last 3 dials: 0.81 · 0.79 · 0.78 (drifting down · still amber)
   Last close: CLOSED · HONEY · ASN-0003 · 2026-05-30
   Principal priorities: (1) reduce DSO · (2) catch fraud earlier · (3) prep for SOC2

3. COLOR
   Sources: 11 · Last refresh: 2026-06-12
   Active contradictions: 1 (vendor's claimed Honey rate vs our observed · resolving)

4. DIAL
   Current: 0.78 · AMBER · TRACKING
   Up: Color +2 sources in past 14 days
   Down: Cost-to-mint at 108% of ceiling for 3 of last 4 weeks

5. OPEN ITEMS
   - Routing strategy tune (sr broker · ETA 2026-06-22)
   - SOC2 readiness scoping (engineering · ETA 2026-06-30)

6. WALK
   - Open: "Q3 closed HONEY on both assignments. Dial drifted to amber on cost · let's walk why."
   - Show: cost variance · routing tune · projection back to ceiling by 2026-07-08
   - Propose: T3 → T3+ (custom validator chain · adds ~12% cost · adds 99.95% SLA)
   - Fallback: hold T3 · accept ceiling at 105% · revisit in 60 days

7. PASS CHECK
   No PASS-pivot needed. Engagement is healthy · dial drift is operational not structural.

8. CROSS-REFS
   Deeds: DDEED-DOV-LOGISTICS-ACME-CLOSE-0003-v1 · DDEED-DOV-LOGISTICS-ACME-CLOSE-0004-v1
   LOU: §4.2 (cost ceiling) · §6.1 (tier upgrade procedure)
   Schema: cost_to_mint_usd · probability_of_close · validator_chain.custom_path
```

Two pages max in actual rendering. Built to walk · NOT to read.

---

## Cross-references

- [Client Engagement Playbook](client_engagement_playbook.md) · where the digest fits in MAGIC
- [Probability of Close Playbook](probability_of_close_playbook.md) · how to talk to the dial in the meeting
- [Cost-to-Mint Playbook](cost_to_mint_playbook.md) · how to walk the math
- [Pre-Market Flight Sheet term](../vocabulary/client_terms/pre-market-flight-sheet.md) · the digest is the in-flight version of the flight sheet
- [Sample Deal Digest example](../examples/sample_deal_digest.md) · a full worked digest
- [Letter of Understanding example](../examples/sample_letter_of_understanding.md) · what the digest cross-references

🐝 *The digest is the discipline · the walk is the close.*
