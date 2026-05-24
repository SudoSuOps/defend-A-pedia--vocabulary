# PSA · Purchase and Sale Agreement

## Street Definition

"Did we get the PSA executed?" — sr broker, asking the closing officer, every Friday afternoon of a closing week.

The **Purchase and Sale Agreement** (PSA) is the binding contract. The LOI / LOU was the soft commitment that triggered diligence. The PSA is the hard contract that emerges from diligence · price locked, terms locked, contingencies named, walk-away conditions tightened, signatures binding both parties to the transaction.

In CRE, the PSA is where the deal becomes legally enforceable. In DefendableOS, the PSA is where the defense engagement becomes contractually committed for the full term · pricing, scope, SLAs, recourse, and PASS authority all written into binding language that survives leadership changes on either side.

## CRE Operator Meaning

A PSA in CRE is typically 40-120 pages, depending on asset complexity. It is the document the closing attorney runs · not the broker. The broker negotiates the business terms; the attorney drafts the language.

PSA sections that always appear:

- **Recitals** (the parties, the asset, the prior negotiations including the LOI)
- **Purchase price and earnest money** (down to the dollar, with all adjustments named)
- **Closing conditions** (what must be true at closing or the deal voids)
- **Representations and warranties** (each party's binding statements about the asset · what's true · what's not)
- **Covenants** (what each party commits to do between PSA sign and closing)
- **Indemnification** (who covers what if a rep or warranty turns out false)
- **Risk of loss** (what happens if the asset is damaged before closing)
- **Closing mechanics** (escrow agent, closing date, document delivery schedule)
- **Survival clauses** (which reps and warranties live beyond closing · which die at closing)
- **Default and remedies** (what each side gets if the other breaches)
- **Assignment rights** (can the contract be transferred)
- **Confidentiality** (what stays under NDA)
- **Disputes and governing law** (which jurisdiction, which forum, which dispute mechanism)

The PSA is the document that gets filed if litigation happens. Every word matters. The sr broker's involvement is to ensure the business terms in the PSA match the LOI exactly · the attorney's involvement is to ensure the language is enforceable.

## DefendableOS Definition

In DefendableOS, the **PSA** is the binding service agreement that follows the LOU and the diligence period. It is the document that legally commits both parties for the engagement term · typically 12, 24, or 36 months · with renewal mechanics and disposition mechanics named in advance.

The PSA in DefendableOS includes all the standard CRE clauses adapted to a defense-service context, plus:

- **Receipt SLA** with named consequences for missed SLAs (typically pro-rated fee credit)
- **Title insurance commitment** (Tribunal verdict ±0.15 guarantee, ramp schedule, payout mechanics)
- **PASS doctrine clause** (extended from LOU · now binding · including the credit-back mechanics if we PASS mid-engagement)
- **Audit access clause** (customer's auditors and regulators get same-day deed access · named contact · response SLA)
- **Data residency clause** (customer data stays on operator-owned NAS · cloud-mirror requires explicit customer authorization · 5-layer finality stack named explicitly)
- **Vendor change clause** (what happens if the customer changes AI vendors mid-engagement · re-pricing trigger, re-inspection trigger)
- **Renewal mechanics** (auto-renew vs opt-in, notice periods, price-change windows)
- **Disposition mechanics** (orderly wind-down language, deed-archive transfer to customer custody, post-engagement support tier)

## Backend Representation

```json
{
  "engagement.psa_document_v1": {
    "type": "document_reference",
    "schema": "docs/schemas/purchase_and_sale_agreement.schema.json",
    "storage": "object_storage://defendable-engagements/psa/{engagement_id}/v1.pdf"
  },
  "engagement.psa_signed_at": {
    "type": "timestamp"
  },
  "engagement.psa_executed_by_customer_signatory_id": {
    "type": "uuid"
  },
  "engagement.psa_executed_by_defendable_signatory_id": {
    "type": "uuid",
    "description": "Sr broker · personal liability"
  },
  "engagement.psa_attorney_review_by": {
    "type": "string",
    "description": "External counsel signoff · firm name + attorney"
  },
  "engagement.psa_term_months": {
    "type": "integer"
  },
  "engagement.psa_fee_monthly_usd": {
    "type": "decimal"
  },
  "engagement.psa_recourse_terms": {
    "type": "jsonb"
  },
  "engagement.psa_data_residency": {
    "type": "enum",
    "values": ["NAS_ONLY", "NAS_PLUS_CLOUD_MIRROR", "CUSTOMER_PREMISE"]
  },
  "engagement.status_post_psa": {
    "type": "enum",
    "values": ["ACTIVE_LIVE", "TERMINATED", "DISPUTED"]
  }
}
```

Schema files: `docs/schemas/purchase_and_sale_agreement.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

The Purchase and Sale Agreement is the binding contract that follows your Letter of Understanding and our completion of diligence. The LOU was our handshake; the PSA is the contract. It is reviewed by external counsel on both sides · we recommend you have your own counsel review before signing · and it commits both parties for the full engagement term with explicit terms covering price, scope, service-level commitments, our title-insurance guarantee, our PASS authority and the credit-back mechanics if we exercise it, your audit access rights, data residency, and what happens at the end of the engagement.

The PSA is structured to be readable by you, your CFO, your general counsel, your insurance carrier, and your regulator · simultaneously. We use CRE-grade language, not vendor-license boilerplate. If anything in the PSA is unclear to your team, we want to address it before signature · not after.

## Jr Broker Use

You stage the PSA. The sr broker signs it. External counsel reviews it. The discipline:

- **Pull from canonical PSA template.** Same discipline as LOU · NO clause authoring · NO improvisation. PSA template at `docs/examples/sample_psa_template.md` (SH2 ships).
- **Ensure LOU-to-PSA continuity.** Every term in the LOU must appear in the PSA either preserved or expanded. NO terms drop silently. If a term changes between LOU and PSA, that change must be highlighted for sr broker review and (typically) for customer attention.
- **Coordinate external counsel review.** Both sides' counsel review in parallel. You manage the calendar · you don't manage the legal substance.
- **Surface ALL counsel-requested changes to sr broker.** Even minor language tweaks come back to the sr broker for review against the canonical template. Counsel may improve the language; counsel does not get to drift the doctrine.
- **Confirm signing logistics.** Wet signatures or e-signatures? Both parties on same call or sequential? Hashed and anchored within 24h regardless.

## Sr Broker Use

You sign. Personal liability. Same as LOU but with more weight · the PSA is the document that lives in litigation if litigation happens.

Before you sign:

- **Re-pencil one more time.** The deal that penciled at LOU may not pencil at PSA if anything material changed in diligence. If it doesn't pencil, you PASS · even at this late stage. Walking from a PSA pre-sign costs nothing material. Walking from a PSA post-sign costs the entire engagement.
- **Verify the PASS-credit mechanics.** If we exercise the PASS clause mid-engagement, the customer must be made whole on prepaid fees for the affected period. Verify this language is correct and the dollar mechanics are clean.
- **Verify the title-insurance commitment.** ±0.15 score guarantee is a real financial commitment. Confirm the Tribunal pipeline can hit this on this customer's fleet by the named ramp date. If not, you negotiate the ramp date · you do not sign a guarantee you can't honor.
- **Verify the data-residency clause.** This is what regulated customers will read most carefully. Make sure it accurately reflects where data will live for the engagement term.
- **Verify the disposition clause.** Customers should be able to walk at the end of term without losing their audit trail. The deed-archive transfer must be operational, not theoretical.

You also adjudicate any PSA-amendment requests post-sign. Amendments are rare · we structure PSAs to flex through renewal mechanics rather than amendment · but they happen. Amendment requests get the same scrutiny as a new PSA · sometimes more.

## Tribunal Use

The PSA is graded as the highest-stakes engagement-origination artifact. The bar is higher than any other document.

- **Rule layer**: every term in LOU must trace into PSA → critical_failure if any drop
- **Rule layer**: external counsel signoff required → critical_failure if missing
- **Rule layer**: PASS-credit mechanics must include dollar arithmetic, not just narrative → critical_failure if vague
- **Rule layer**: title-insurance commitment must include named ramp date and named consequences → critical_failure if missing
- **Judge layer**: PSA scored on enforceability (1-5), LOU-to-PSA continuity (1-5), clarity for non-legal reader (1-5), brand voice alignment (1-5)
- **Classification impact**: PSAs are typically Honey or Royal Jelly · PSAs hitting Jelly trigger immediate post-sign legal review · PSAs hitting Propolis are voided and re-papered before any service delivery

```yaml
classification_impact: [HONEY, ROYAL_JELLY, JELLY, PROPOLIS]
can_be_critical_failure: true
rule_layer_checks:
  - all LOU terms present in PSA
  - external counsel signoff documented
  - PASS-credit mechanics include arithmetic
  - title-insurance commitment ramp and consequences named
  - data-residency clause matches operational reality
  - dispute and governing law named
  - signatures hashed and anchored within 24h
```

## Evidence Required

- LOU receipt referenced and term-by-term continuity verified
- Diligence completion receipt (inspection report · color refresh · validator chain final pass · adversarial probe)
- External counsel signoff documented (firm name, attorney name, date, signoff hash)
- Customer counsel review documented (or customer's written waiver of counsel review)
- Both signatures hashed and anchored to Hedera within 24 hours
- ENS subdomain provisioned for the PSA receipt

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **lou_to_psa_drift** | A LOU term silently disappeared in PSA | PROPOLIS |
| **vague_pass_mechanics** | PASS credit-back named but arithmetic missing | JELLY |
| **wishful_title_insurance** | ±0.15 commitment with no ramp realism | PROPOLIS |
| **unverified_counsel** | External counsel signoff missing or fabricated | PROPOLIS |
| **datafied_residency_wrong** | Data-residency clause doesn't match operational reality | PROPOLIS |
| **boilerplate_creep** | Vendor-license boilerplate snuck in via counsel edits | JELLY |
| **anchor_lag_psa** | PSA signed but not Hedera-anchored within 24h | JELLY |
| **post_sign_amendment_request** | Customer requests material change within 30d of sign | JELLY (signals weak LOU-to-PSA review) |

## Scoring Impact

- **assignment_success**: TERMINAL · clean PSA execution IS engagement success initialization
- **repair_lift**: ZERO · PSAs are not repaired · they are voided and re-papered
- **validator_confidence**: HIGHEST · PSA is the document the validator chain anchors every subsequent deed to
- **risk_temperature**: INVERSE · strong PSAs lower engagement risk for both parties dramatically
- **probability_of_close**: TERMINAL · PSA sign IS the close · post-PSA the math is retention math
- **evidence_strength**: HIGHEST · PSA citations form the legal spine of the engagement
- **cost_to_mint**: MEDIUM · PSA production costs more than LOU (counsel time) · weak PSAs cost orders of magnitude more in litigation

## Deed / Receipt Impact

- **Receipt fields touched**: `psa_hash`, `psa_signed_at`, `psa_signatory_ids[]`, `psa_term_months`, `psa_external_counsel_ref`, `psa_data_residency_class`
- **DDEED class impact**: every deed issued during engagement cites the originating PSA · PSAs with poor Tribunal scores produce deeds with `origination_quality_flag` carrying over for the engagement lifetime
- **Books and records layer**: ALL FIVE · PSAs are immediately full-stack anchored
- **5 Proofs touched**: ALL FIVE · PSA is the most fully-proof-bound artifact in the engagement record

## Related Terms

- [loi](loi.md) · LOI is the soft commitment · PSA is the hard contract
- [om](om.md) · OM is the marketing artifact · PSA is the binding one
- [digest](digest.md) · digests preceded the sits that produced the LOU that becomes the PSA
- [due-diligence](due-diligence.md) · diligence happens between LOI and PSA · PSA cites the diligence outputs
- [books-and-records](books-and-records.md) · PSAs are the most heavily anchored documents in the firm
- [underwriting](underwriting.md) · underwriting math is what makes the PSA pencil

## Example

> **Engagement**: cold-storage operator · Janet K. · prior LOU signed 2026-05-22 (the hurt-customer-return engagement from the LOI example).
>
> **Diligence period**: 2026-05-23 to 2026-06-12. Full fleet inspection. Color refresh to 0.91 score. Validator chain final pass clean on 13 of 14 agents · 1 advisory on agent-09 (logging-tooling vendor drift) · workout plan attached.
>
> **PSA drafted**: 2026-06-10 by jr broker. Pulled from canonical template `PSA-Defense-Engagement-v4.1`. All LOU terms preserved · pricing $42K/mo confirmed · term 12 months auto-renew on opt-in · PASS-credit mechanics: 30-day pro-rated refund of prepaid fees plus 60-day post-PASS observation period free of charge for orderly wind-down.
>
> **External counsel review**: Defendable's counsel (Lewis & Co., Jupiter FL) signed off 2026-06-11. Customer's counsel (in-house GC) signed off 2026-06-12 with two minor language tweaks · both pulled into canonical clause library for future PSAs.
>
> **Title-insurance commitment**: ±0.15 score guarantee on Tribunal verdicts starting day 60 of engagement (2026-08-11). Ramp realistic per fleet diligence findings. Credit mechanism: variance beyond ±0.15 triggers automatic 5% monthly fee credit per affected verdict, capped at 25% of monthly fee.
>
> **Signatures**: 2026-06-12, 16:00 ET. Customer: Janet K., CEO. DefendableOS: Marcus T., sr broker. Both signatures hashed. Anchored to Hedera HCS topic 0.0.10291838 at 16:18 ET (18-minute SLA met). ENS subdomain `psa-cold-atl-000088-v1.swarmdeed.eth`.
>
> **Receipt ID**: `PSA-COLD-ATL-000088-2026-06-12-16_00-7a2f`
>
> **Outcome**: engagement transitioned `ACTIVE_DILIGENCE` → `ACTIVE_LIVE`. First production Tribunal verdicts issued 2026-06-13. Title-insurance commitment armed for 2026-08-11. Customer's procurement team and external auditor both received PSA copies in same business day.

## DefendableOS Notes

- The PSA is where the founder's CRE rigor most clearly differentiates DefendableOS from typical AI vendors. Most AI vendors ship 50-page click-through ToS that no principal ever reads. We ship a CRE-grade PSA that the principal, the CFO, and the auditor all read · and they sign because the language meets their expectations.
- External counsel review is non-negotiable. We pay our counsel. Customer pays theirs. Both sides have skin. No "use our template, save legal fees" shortcuts · those produce litigation risk.
- The PASS-credit clause is the firm's most studied clause by customer counsel · because it's the most unusual one. "You'd refund our money if you decided you couldn't defend us anymore?" Yes. That's the doctrine. The clause is what makes the doctrine contractual rather than aspirational.
- Customers who push hard to remove or weaken the PASS-credit clause are themselves a PASS signal · we'd rather walk pre-PSA than have a PSA in force with a customer who doesn't trust our walk-away authority.

🐝 *The PSA is the contract. The contract is the receipt. The receipt is the brand.*
