# OM · Offering Memorandum

## Street Definition

"Did you read the OM yet?" — buyer-side broker, dialing in on a new listing.

The **Offering Memorandum** (OM) is the marketing book the listing broker puts together to sell a property. Pretty renders. Stabilized financials. Tenant rent roll. Market overview. Comps. CapEx forecast. The pretty book that lands in every potential buyer's inbox the week the property goes to market.

In CRE, the OM is necessary · but not sufficient. The OM wins the meeting · the pre-market flight sheet wins the deal. Every sr broker knows this. Every jr broker eventually learns it the hard way.

## CRE Operator Meaning

The OM is the public-facing offering document for an asset on market. It is designed to attract a buyer pool · stratify the buyer pool · qualify the buyer pool · and elevate the perceived value of the asset enough to drive a competitive bidding environment.

Sections in a real CRE OM:
- Executive summary (the one-page hook)
- Property overview (location, size, asset class, photos)
- Tenant overview (rent roll, lease expirations, tenant credit)
- Financial summary (T-12 NOI, pro forma NOI, stabilization assumptions)
- Market overview (cap rate trends, supply pipeline, demographic drivers)
- Investment highlights (the bullet points the listing broker wants you to walk away with)
- CapEx schedule (what needs to be spent and when)
- Comparable sales (the comps the broker wants to anchor against)
- Disclaimer (the legal language at the back)

The sr broker reads the OM for what's NOT there. The pre-market flight sheet is for what IS there · and what the seller knows but didn't put in the book.

## DefendableOS Definition

In DefendableOS, the **OM** is the public-facing engagement-tier document. It is the pretty book the customer sees. It is NOT the internal pre-market flight sheet · which is the operator-internal doc that contains the math, the color, and the disclosure schedule.

The OM wins the meeting (gets the customer to schedule a sit). The flight sheet (delivered after LOU draft) wins the deal (gets the customer to sign).

The OM in DefendableOS is what gets attached to a contact-form response. It is what gets shared in a sample-pack download. It is what the customer's procurement team requests by name. It is marketing collateral · receipted, but marketing collateral · and it must NEVER be confused with the underwriting artifacts.

## Backend Representation

```json
{
  "engagement.om_v1": {
    "type": "document_reference",
    "schema": "docs/schemas/offering_memorandum.schema.json",
    "storage": "object_storage://defendable-public/om/{engagement_id}/v1.pdf",
    "watermarked": true,
    "watermark_field": "watermark.recipient_email"
  },
  "engagement.om_delivered_at": {
    "type": "timestamp"
  },
  "engagement.om_recipient_id": {
    "type": "uuid"
  },
  "engagement.om_view_count": {
    "type": "integer",
    "scoring_hook": "interest_signal_strength"
  },
  "engagement.flight_sheet_v1": {
    "type": "document_reference",
    "private": true,
    "comment": "INTERNAL · never sent to customer · the math the OM hides"
  }
}
```

Schema files: `docs/schemas/offering_memorandum.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

The Offering Memorandum is the document we share with you to introduce DefendableOS and the engagement we're proposing. It contains the headline service description, the pricing tiers, the typical customer profile, and the receipts framework that backs every claim. It is intentionally short and intentionally legible · designed for a 15-minute read before our first conversation.

Behind the OM, our team is building the deeper underwriting artifact · the pre-market flight sheet · which we'll walk you through after we've signed a Letter of Understanding to begin the formal engagement. The OM tells you what we do. The flight sheet shows you exactly what we'd do for your specific fleet.

## Jr Broker Use

You manage the OM distribution. The OM is templated · you customize light layers (recipient name, suspected vertical fit, prior interaction context) but you do NOT rewrite the body. The body is canonical · same words to every customer in a tier · same receipts framework.

Distribution discipline:

- **Watermark every send.** The OM PDF carries a recipient-specific watermark embedded in metadata. If it leaks, we know who leaked it.
- **Receipt every send.** `om_delivered_at`, `om_recipient_id` populated in real time. This is the leading indicator of pipeline health.
- **Track view signals.** The OM is served from instrumented storage · we see opens, page-depth, dwell time. View signals feed `interest_signal_strength` which informs follow-up timing.
- **Don't substitute for the flight sheet.** If a prospect asks for "more detail than the OM has" · that's the signal to schedule the appraisal sit, not to send the flight sheet ahead of time. The flight sheet is for engaged customers, not browsers.
- **Refresh quarterly.** OM versioned every quarter at minimum · receipts framework, customer roster, and pricing tiers reviewed by SH5.

## Sr Broker Use

You sign off on OM versions. Every new OM revision goes through sr broker review · because every word in the OM is a claim the firm will defend on a deed five years from now.

You also audit OM-to-flight-sheet handoffs. The failure mode is jr brokers leaking flight-sheet content into OM responses · either because the customer pressed for detail or because the jr broker confused the two artifacts. This degrades both: the OM becomes too dense to land, and the flight sheet loses its value as an LOU trigger.

When customers complain that "your OM doesn't give us enough detail" · that's the correct outcome. The OM is designed to make them want a meeting · not to substitute for one.

## Tribunal Use

The OM is graded as a customer-facing artifact · separately from the flight sheet.

- **Rule layer**: any claim in the OM that doesn't tie to a receipt anchor or a public-domain doctrine document → critical_failure → PROPOLIS
- **Rule layer**: any marketing claim that conflicts with the Client Language Doctrine (MBA jargon · "AI-native" · "transformational" · "10x") → JELLY
- **Judge layer**: OM quality scored on customer-readability (1-5), claim-to-receipt traceability (1-5), brand voice alignment (1-5)
- **Classification impact**: OMs that ship without ANY watermark · ANY receipt · ANY brand voice anchor → automatic PROPOLIS, withdrawn from distribution immediately

```yaml
classification_impact: [HONEY, ROYAL_JELLY, JELLY, PROPOLIS]
can_be_critical_failure: true
rule_layer_checks:
  - all numeric claims trace to receipt anchors
  - no MBA jargon (banned-words list enforced)
  - watermark present and recipient-bound
  - version stamped and date stamped
```

## Evidence Required

- Watermark metadata embedded and recipient-bound
- Every numeric claim traceable to a public receipt or doctrine doc
- Brand voice attestation by SH5 (Client Language Specialist)
- Sr broker signoff on version
- Distribution log (every send receipted, every recipient logged)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **flight_sheet_leak** | OM contains flight-sheet-level detail · undermines the funnel | JELLY |
| **claim_without_receipt** | Numeric claim with no receipt anchor | PROPOLIS |
| **mba_jargon** | "Transformational," "best-in-class," "synergies," etc. | JELLY |
| **unwatermarked** | OM PDF shipped without recipient watermark | JELLY |
| **stale_version** | OM more than 90 days old in active distribution | JELLY |
| **unauthorized_edit** | Jr broker rewrote canonical body language | JELLY (PROPOLIS on repeat) |
| **misaligned_pricing** | Pricing tiers in OM don't match current engagement pricing | PROPOLIS |

## Scoring Impact

- **assignment_success**: MEDIUM · OM quality affects the M (Meetings) of MAGIC · not directly the I (Ink)
- **repair_lift**: LOW · OMs that fail get withdrawn · not repaired
- **validator_confidence**: MEDIUM · poor OMs degrade brand trust which compounds across all engagements
- **risk_temperature**: MEDIUM · over-claimed OMs create regulatory exposure
- **probability_of_close**: MEDIUM · OM gets the meeting · the flight sheet wins the deal
- **evidence_strength**: LOW · OM is marketing · not evidence
- **cost_to_mint**: LOW · OM production is templated, low marginal cost

## Deed / Receipt Impact

- **Receipt fields touched**: `om_version_hash`, `om_delivered_at`, `om_recipient_id`, `om_view_signals`
- **DDEED class impact**: deeds whose origination engagement carried an OM that later failed Tribunal review get a `provenance_quality_flag` · the customer is notified and the engagement audit is updated
- **Books and records layer**: L1_PG (distribution log) · L2_MERKLE (canonical version hash) · L3_NAS (PDF archive)
- **5 Proofs touched**: PROCESS (the marketing-to-engagement funnel discipline) · QUALITY (the brand voice integrity)

## Related Terms

- [digest](digest.md) · digest is to the meeting what the OM is to the funnel
- [loi](loi.md) · LOI follows the meeting the OM secured
- [due-diligence](due-diligence.md) · diligence happens after LOU · OM precedes it
- [deal-flow](deal-flow.md) · OM is the funnel input artifact
- [probability-of-close](probability-of-close.md) · OM view depth is a leading indicator
- [books-and-records](books-and-records.md) · OM distribution is receipted just like any deed-bound action

## Example

> **Engagement**: prospect inbound from `defendableos.com` contact form. Medical-billing AI defense engagement target. Mid-market hospital network in the Midwest. CFO submitted the form herself · not procurement.
>
> **OM delivered**: same day, watermarked to the CFO's email, version `OM-v3.2-2026-Q2`. Distribution receipt: `OM-DELIV-2026-05-24-9b3c`.
>
> **OM contents**: 12 pages. Section 1: what defense means and what it doesn't. Section 2: the 5-Proof framework. Section 3: the three engagement tiers and pricing ranges. Section 4: typical customer profile (mid-market, regulated, audit-needy). Section 5: the receipts framework with link to Hedera topic for live verification. Section 6: founder bio. Section 7: how to schedule a sit.
>
> **View signals**: opened within 90 minutes. Pages 1-7 read fully. Page 8 (the founder bio) opened twice. Page 11 (the sit-scheduling page) opened, scrolled, but no booking made within first 48 hours.
>
> **Follow-up trigger**: jr broker dialed at hour 50 referencing the founder-bio interest. Booked the sit on the call. Sit delivered the appraisal on flight sheet `FS-2026-Q2-0044`. LOU signed 14 days post-OM.
>
> **Deed lineage**: the OM is cited in the engagement origination record · `DDEED-DOV-MED-MID-000017-v1` notes `origination_artifact_id = OM-DELIV-2026-05-24-9b3c`. Five-year audit trail intact.

## DefendableOS Notes

- The OM is the most-leaked DefendableOS artifact. Watermark discipline catches the leak. We never sue · we surface the leak to the customer who leaked it · and they almost always close on principle.
- The OM is the canonical example of "what wins the meeting · not the deal." Every jr broker who tries to make the OM do too much weakens both the OM and the flight sheet.
- Customers occasionally ask "can we see your underwriting model?" before LOU. The doctrine answer: the underwriting model lives in the flight sheet, which we share after LOU. The OM contains the framework · the flight sheet contains the math · and we keep that separation because mixing them collapses the funnel.
- Quarterly OM refresh discipline is what keeps the brand voice locked. Without it, drift creeps in via well-meaning jr broker edits.

🐝 *The OM wins the meeting. The flight sheet wins the deal.*
