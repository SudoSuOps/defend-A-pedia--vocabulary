# Sample Deal Digest

> *A worked example of a pre-meeting digest · CRE-style · 8-section format. This is the internal operating doc the broker writes before the meeting. The principal never sees this raw · they see the walk of it.*

---

**DIGEST · Q3 Quarterly Business Review · Acme Logistics Inc.**

Prepared by: Jenny Reyes · Sr Broker
For: 2026-06-15 · 14:00 ET · 60-minute video call

---

## 1 · Meeting metadata

- **Meeting type**: Q3 QBR (the first QBR under this engagement)
- **MAGIC stage**: In-flight (post-Ink · pre-Close on Q3 milestones)
- **Attendees**:
  - Principal side · Jane Smith (COO · decision authority) · Mike Chen (CFO · financial authority) · Dana Park (VP Eng · operational contact)
  - Defender side · Jenny Reyes (sr broker · running the meeting) · Donovan Mackey (founder · attending in support · not running)
- **Format**: Zoom · screen-share enabled · recording requested by Mike for board archive (Principal owns recording per §10)

---

## 2 · Engagement context

- **Engagement ID**: ENG-DOV-LOGISTICS-ACME-0001
- **LOU date**: 2026-03-12 · 12-month initial term
- **Tier**: T3 · White-Glove ($0.0416/deed effective ceiling · $8,500 monthly floor)
- **Active assignments**:
  - ASN-0001 · refund-decision agent · target 92% Honey rate · in flight
  - ASN-0002 · invoice-reconciliation agent · target 95% Honey rate · in flight
- **Last 3 dials**: 0.81 → 0.79 → 0.78 (drifting down · still amber)
- **Last close**: CLOSED · HONEY · pilot assignment ASN-0000 · 2026-05-30 · all 5 grades passing
- **Last failure**: None recorded (zero FAILED outcomes since engagement open)
- **Principal stated top-3 priorities** (in their language · captured 2026-04-22):
  1. "Reduce DSO" (days sales outstanding · CFO priority · invoice agent should help)
  2. "Catch fraud earlier" (COO priority · refund agent + invoice agent both relevant)
  3. "Prep for SOC2" (operational · 2026-Q4 audit window · our books-and-records is directly relevant)

---

## 3 · Color summary

- **Sources count**: 11 (up from 7 at engagement open)
- **Most recent refresh**: 2026-06-12 (3 days ago · fresh)
- **Active contradictions**:
  - Vendor's claimed Honey rate (94%) vs our observed (89%) on refund-decision · investigating · likely a different rubric · resolving by 2026-06-20
- **Color gaps to close before meeting**: none material · color file is meeting-ready
- **Notable add since last QBR**: 2 EDGAR confirmations on Acme's tenant-credit position (their warehouse landlord is investment-grade · de-risks the engagement)

---

## 4 · The dial

- **Current Probability of Close**: **0.78** · AMBER · TRACKING
- **7-day trajectory**: -0.03 (mild drift · attributable to one driver · documented below)
- **Top 2 drivers moving the dial**:
  - **DOWN**: `operator_hygiene` driver at 0.62 (was 0.71 30 days ago) · cost-to-mint at 108% of ceiling 3 of last 4 weeks · driven by a routing inefficiency on the refund-decision path identified 2026-06-08
  - **UP**: `color_strength` driver at 0.88 (was 0.81 30 days ago) · the +2 EDGAR sources
- **Escalation status**: NONE (within AMBER · sr broker handled · founder cc on Friday Brief but no call needed)

---

## 5 · Open items

| Item | Owner | ETA | Status |
|---|---|---|---|
| Routing strategy tune (refund-decision path) | Sr broker + eng | 2026-06-22 | In flight · 60% complete |
| Honey-rate rubric reconciliation with vendor | Sr broker | 2026-06-20 | In flight · awaiting vendor doc |
| SOC2 readiness scoping | Engineering | 2026-06-30 | In flight · 30% complete |
| Custom validator chain proposal for Q4 | Sr broker | 2026-07-01 | Not started · QBR will scope |

---

## 6 · The walk

The literal sentence-by-sentence walk Jenny plans to give. 30-min target.

### Opening (3 min)

> "Q3 is closing strong on both assignments. ASN-0000 (the pilot) closed HONEY clean. Both in-flight assignments are tracking against criteria. The dial is in amber at 0.78 · driven by one operational driver we have a fix in flight for. I'll walk the dial · walk the cost variance · and we'll get into the Q4 scoping in the back half."

### Dial walk (8 min)

- Show the 6-driver breakdown on screen
- Highlight `color_strength` UP (+0.07 over 30 days)
- Highlight `operator_hygiene` DOWN (-0.09 over 30 days)
- Walk the cost variance: 108% of ceiling 3 of 4 weeks · root cause is routing strategy on refund-decision path
- Show the remediation: routing tune deploying 2026-06-22 · projection back to 99% of ceiling within 7 days post-deploy

### Cost walk (8 min)

- Show the 7-component breakdown for the current month
- Walk the variance to ceiling per component
- Show the projected return-to-baseline post-tune
- Show the published formula doc (Mike will appreciate the audit-trail availability)
- Show a sample Hedera anchor for one deed from the past week

### Q4 scoping (10 min)

- Propose: maintain T3 · NOT upgrade to T3+ (custom validator chain) yet · we have headroom in the current tier
- Alternative if Mike wants the upgrade discussion: custom validator chain adds ~12% cost · adds 99.95% SLA · adds 3 custom Tribunal rules (one for fraud-detection specifically · maps to Acme priority #2)
- Recommend: scope the custom validator chain for Q4 kickoff · 30-day spec window · go-live targeted 2026-09-15

### Close (5 min)

- Action items captured
- Next QBR scheduled (Q4 · 2026-09-15 tentative)
- Mike's audit-trail walk-through to be scheduled separately (30 min · Jenny + Mike + sr engineer)
- Open Q&A

### Time buffer (6 min)

For Mike's likely cost-deep-dive · for Dana's likely technical questions.

---

## 7 · PASS check

**No PASS-pivot needed.**

Engagement is healthy. Dial drift is operational (a routing inefficiency · already root-caused · already fixing) · NOT structural (the engagement is sound · the principal is engaged · the fleet is responsive).

The vendor-rubric disagreement on Honey rate could become a structural issue IF it turns out the vendor's rubric is materially different from ours and the principal prefers theirs. Low probability · but watch. If it materializes · raise at Q4 QBR · NOT today (don't surface a non-issue · it makes the engagement feel unstable).

---

## 8 · Cross-references

### Deeds the broker should be ready to pull on screen
- `DDEED-DOV-LOGISTICS-ACME-CLOSE-0000-v1` (pilot close · CLOSED · HONEY)
- `DDEED-DOV-LOGISTICS-ACME-LOU-v1` (the LOU itself)
- `DDEED-DOV-ECON-Q2-2026-v1` (current cost-to-mint formula version)
- 3 sample weekly DDEED batches from the past 30 days (any will do · Mike likely picks one randomly)

### LOU clauses likely to be referenced
- §3.2 (5-grade breakdown · for the closing statement walk)
- §4.2 (ceiling and buffer · for the cost variance walk)
- §5.3 (escalation pyramid · for the dial discussion)
- §7.2 (Fix-or-Refund 90-day · NOT in play but Mike may probe)

### Schema fields likely to be questioned
- `engagement.probability_of_close_drivers`
- `engagement.cost_to_mint_30d_rolling`
- `assignment.tribunal_honey_rate`
- `deed.hedera_consensus_timestamp`

### Internal stakeholders looped in
- Founder (Donovan) · attending in support
- Engineering (M. Patel · lead on routing tune) · on-call for technical questions but NOT in the meeting
- QA validator (SH6) · already reviewed the digest · sign-off filed in shared folder

---

## Pre-meeting checklist

- [ ] Dashboard URL bookmarked · loaded · tested screen-share
- [ ] Sample Hedera anchor URL tested (verified consensus timestamp loads)
- [ ] Color file open in second window · ready to pull
- [ ] LOU PDF open in third window · §§ tabbed
- [ ] Cost formula doc open in fourth window
- [ ] Backup contact info for all attendees (in case Zoom fails · text fallback ready)
- [ ] Recording consent confirmed with Mike (per §10)
- [ ] 30-min Q&A buffer reserved on calendar after the meeting

---

## Post-meeting deliverables (within 24 hours)

- [ ] Updated digest filed (with notes section · what we learned · what changed)
- [ ] Action items added to engagement folder · owners notified
- [ ] Morning Brief tomorrow includes meeting summary in the 4-line slot
- [ ] If custom validator chain scoping was approved · spec kick-off scheduled within 7 days
- [ ] Recording (if approved) shared via secure link · 30-day expiry

---

🐝 *The digest is the discipline. The walk is the close. The Morning Brief tomorrow reflects what we learned today.*
