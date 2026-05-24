# LOI · Letter of Intent (a.k.a. LOU · Letter of Understanding)

## Street Definition

"Did they sign the LOI yet?" — sr broker, every Monday morning, on the pipeline call.

The **LOI** (Letter of Intent · sometimes called the **LOU**, Letter of Understanding, in defense-engagement context) is the soft commitment that moves a customer from "interested" to "engaged." It's the first ink. Not the binding contract (that's the PSA), but the documented agreement on terms-in-principle that triggers diligence, color refresh, and the real underwriting work.

In CRE, "got the LOI" is the moment the deal becomes real. The sr broker celebrates here only in private · the celebration goes public at the deed. But the LOI is the inflection point · pre-LOI you're selling, post-LOI you're underwriting.

## CRE Operator Meaning

The LOI is a 1-3 page document that captures:

- The asset (or in defense-engagement context, the agent fleet scope)
- The proposed price (or fee structure)
- The proposed timeline (engagement term, key dates, milestones)
- The proposed structure (exclusive vs co-broker, recourse vs non-recourse, etc.)
- The diligence period (typically 30-60 days for CRE, 14-30 days for defense engagements)
- The walk-aways (what voids the LOI · failed inspection, financing falling through, regulatory event)
- The earnest money or deposit (skin in the game, refundable conditions named)
- The exclusivity period (during diligence, both sides agree not to shop)
- The signatures of both parties

In CRE, the LOI is typically non-binding on price (subject to diligence) but binding on process (exclusivity, deposit, timeline). The PSA is the binding contract on price and terms · the LOI is the binding contract on the right to do diligence.

In DefendableOS, we use LOU (Letter of Understanding) when "intent" feels too cold for the relationship-driven motion. Same document, slightly warmer name. Some sr brokers use LOI for procurement-led customers and LOU for principal-led customers · either works.

## DefendableOS Definition

In DefendableOS, the **LOI / LOU** is the document that transitions an engagement from `PROSPECT` to `ACTIVE_PRE_DILIGENCE` status. It is the first receipted commitment from the customer · and the first receipted commitment FROM us as well.

The LOU contains the same canonical clauses as a CRE LOI plus DefendableOS-specific clauses:

- Engagement term and pricing
- Defense scope (agents covered, verticals covered, regulatory regimes covered)
- Receipt SLA (every defensive action receipted within 15 min · anchored to Hedera within 30 min)
- Title insurance ramp (Tribunal verdicts ship with ±0.15 score guarantee starting day 60)
- The PASS clause (DefendableOS reserves the right to recommend non-action and credit the prepaid fee if structure changes such that defense becomes infeasible)
- The audit clause (customer's auditors and regulators get same-day deed access on request)
- The white-glove discipline clause (named sr broker · response SLA · escalation path)

## Backend Representation

```json
{
  "engagement.lou_document_v1": {
    "type": "document_reference",
    "schema": "docs/schemas/letter_of_understanding.schema.json",
    "storage": "object_storage://defendable-engagements/lou/{engagement_id}/v1.pdf"
  },
  "engagement.lou_signed_at": {
    "type": "timestamp",
    "scoring_hook": "engagement_inflection_point"
  },
  "engagement.lou_customer_signatory_id": {
    "type": "uuid",
    "description": "Principal · CEO · MD · the name on the door"
  },
  "engagement.lou_defendable_signatory_id": {
    "type": "uuid",
    "description": "Sr broker · personal signature · personal liability"
  },
  "engagement.lou_walk_away_conditions": {
    "type": "jsonb",
    "description": "Documented PASS triggers"
  },
  "engagement.lou_exclusivity_period_days": {
    "type": "integer",
    "default": 30
  },
  "engagement.lou_deposit_usd": {
    "type": "decimal"
  },
  "engagement.status_post_lou": {
    "type": "enum",
    "values": ["ACTIVE_PRE_DILIGENCE", "ACTIVE_DILIGENCE", "DEAD", "PASSED"]
  }
}
```

Schema files: `docs/schemas/letter_of_understanding.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

The Letter of Understanding is the document that formalizes our agreement to engage. It is not the final binding contract (that comes after the diligence period, in the Purchase and Sale Agreement). The LOU captures the proposed scope, the proposed fee, the timeline, and our mutual commitments during the diligence window: we agree to perform a full inspection of your agent fleet at no charge; you agree to give us the access and information we need to do that inspection thoroughly; we both agree not to engage other parties during the diligence window so we can both focus.

The LOU is signed by you as the principal and by your named sr broker as DefendableOS's representative. Both signatures carry personal accountability · this is not a software signup. It is a CRE-grade engagement document, structured to make both sides' commitments legible to your auditor, your board, and your insurance carrier.

## Jr Broker Use

You prep the LOU. The sr broker signs it. The discipline:

- **Pull the canonical clauses.** Do NOT draft new clauses. The clause library lives at `docs/examples/sample_lou_clauses.md` (SH2 ships). You select clauses; you do not author them.
- **Match the engagement scope to the flight sheet.** Every agent named in the flight sheet must appear in the LOU's `defense_scope` clause. Every vertical referenced must appear in the regulatory-coverage clause.
- **Match the pricing to the flight sheet.** If the customer negotiated mid-meeting, the new pricing must trace back to a flight sheet revision · NOT to a verbal agreement undocumented in receipts.
- **Surface every modification request to sr broker.** ANY customer-requested clause change · you take the request back · you don't negotiate clauses in meeting.
- **Confirm signing authority.** The principal must have the legal authority to bind their entity. Verify via EDGAR (if public), state filing (if private), or board resolution (if requested). The verification gets receipted.

## Sr Broker Use

You sign. The signature is personal liability. Treat it that way.

Before you sign, you verify:

- **Diligence outputs.** Inspection report. Color file. Validator chain first-pass result. Adversarial probe results. If any of these are weak, you don't sign · you re-pitch.
- **PASS triggers documented.** Every walk-away in the LOU is named explicitly. If something would void our engagement, the customer must see it in writing at sign time.
- **Pricing pencils.** You re-pencil the deal at LOU sign. The deal that penciled at appraisal may not pencil now if anything changed in diligence. If it doesn't pencil, you PASS or re-pitch.
- **Title insurance ramp realistic.** The ±0.15 score guarantee starts at day 60. You verify the Tribunal can hit that on this customer's fleet by day 60. If not, you either delay the guarantee start or PASS.
- **Customer signatory legitimate.** Founder · CEO · principal · MD. Not a procurement intake. Not a manager. The name on the door · or you don't sign.

You also adjudicate disputes about LOU content post-sign. If the customer comes back asking to revise a clause two weeks after signing, that's a T4 (re-trade) escalation · evaluated against the PASS doctrine.

## Tribunal Use

The LOU is graded as a structured engagement-origination document.

- **Rule layer**: missing PASS clause → critical_failure → cannot proceed to diligence
- **Rule layer**: pricing doesn't trace to flight sheet → critical_failure → escalate to sr broker for review before sign
- **Rule layer**: customer signatory not verified as binding-authority → critical_failure → cannot sign until verified
- **Judge layer**: LOU completeness scored on clause coverage (1-5), scope-to-flight-sheet match (1-5), receipt anchor integrity (1-5)
- **Classification impact**: LOUs that ship clean become Honey-tier engagement records · LOUs requiring multiple re-drafts get Jelly · LOUs that ship with critical failures and require post-hoc remediation get Propolis

```yaml
classification_impact: [HONEY, ROYAL_JELLY, JELLY, PROPOLIS]
can_be_critical_failure: true
rule_layer_checks:
  - PASS clause present
  - pricing traces to flight sheet receipt
  - signatory binding authority verified
  - both signatures hashed and anchored within 24h
  - exclusivity period named
```

## Evidence Required

- Flight sheet receipt referenced in LOU pricing clause
- Color file with `color_score >= 0.85` at LOU sign date
- Inspection report stored and hash-cited
- Signatory authority verification (EDGAR / state filing / board resolution)
- Adversarial probe results from diligence inspection
- Both signatures hashed (PDF signature + receipt entry) and Hedera-anchored within 24 hours

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **scope_drift** | LOU scope doesn't match flight sheet · agents missing or extra | JELLY |
| **verbal_pricing** | Pricing in LOU based on undocumented verbal agreement | JELLY |
| **missing_pass_clause** | LOU lacks the PASS-doctrine clause | PROPOLIS |
| **unverified_signatory** | LOU signed by someone without binding authority | PROPOLIS |
| **wishful_title_insurance** | ±0.15 guarantee start date unrealistic for fleet maturity | JELLY |
| **clause_drift** | Jr broker authored new clause not in canonical library | JELLY (PROPOLIS on repeat) |
| **anchor_lag** | LOU signed but not Hedera-anchored within 24h | JELLY |
| **post_sign_retrade** | Customer requests material clause change within 14 days of sign | JELLY (signals weak pre-sign discipline) |

## Scoring Impact

- **assignment_success**: HIGH · clean LOU is the strongest predictor of clean engagement
- **repair_lift**: LOW · LOUs that fail are usually walked, not repaired
- **validator_confidence**: HIGH · the LOU is the validator chain's anchor document
- **risk_temperature**: INVERSE · strong LOUs lower engagement risk profile dramatically
- **probability_of_close**: TERMINAL · LOU sign IS one of the close events · after this, retention math takes over
- **evidence_strength**: HIGH · LOU citations form the spine of the deed evidence chain
- **cost_to_mint**: LOW · LOU production is templated · weak LOUs are expensive in retention loss

## Deed / Receipt Impact

- **Receipt fields touched**: `lou_hash`, `lou_signed_at`, `lou_signatory_ids[]`, `lou_walk_away_conditions_hash`, `lou_flight_sheet_ref`
- **DDEED class impact**: every deed cites the originating LOU · LOUs with poor Tribunal scores produce deeds with `origination_quality_flag`
- **Books and records layer**: ALL FIVE · LOUs are full-stack anchored · L1 → L2 → L3 → L4 → L5 within 24 hours of sign
- **5 Proofs touched**: ALL FIVE · LOU is the first receipt that touches every Proof simultaneously

## Related Terms

- [om](om.md) · the OM wins the meeting · the LOU formalizes the commitment
- [psa](psa.md) · LOU is the soft commitment · PSA is the binding contract
- [due-diligence](due-diligence.md) · diligence happens between LOU and PSA
- [digest](digest.md) · the digest preceded the sit that produced the LOU
- [underwriting](underwriting.md) · the underwriting math pencils into the LOU
- [books-and-records](books-and-records.md) · LOU is the most fully anchored origination document

## Example

> **Engagement**: cold-storage operator · 14-agent fleet · Atlanta MSA · prior PASS in 2025-11 (customer pursued fantasy mandate with competitor · competitor over-promised certification · agent went dark in March 2026 · customer came back hurt).
>
> **LOU drafted**: 2026-05-19 by jr broker. Pulled from canonical clause library. Pricing $42K/mo, term 12 months renewable 30-day windows, defense scope: all 14 agents in cold-storage logistics workflow. Excluded scope: medical-claims agent (per prior PASS doctrine · 60 days clean Tribunal verdicts required before scope expansion).
>
> **LOU reviewed**: sr broker review same day. Flagged: title-insurance ramp originally set to day 30 · revised to day 60 to match fleet maturity. PASS clause confirmed present. Disclosure clause added: "DefendableOS previously declined this engagement on 2025-11-04 for reason 'fantasy mandate fleet certification.' The undersigned customer acknowledges the prior recommendation and engages defense services on revised terms."
>
> **LOU signed**: 2026-05-22, 14:33 ET. Customer: Janet K., CEO. DefendableOS: Marcus T., sr broker. Both signatures hashed. Anchored to Hedera HCS topic 0.0.10291838 at 14:48 ET (15-minute SLA met). ENS subdomain `lou-cold-atl-000088-v1.swarmdeed.eth` resolves.
>
> **Receipt ID**: `LOU-COLD-ATL-000088-2026-05-22-14_33-9b3c`
>
> **Outcome**: engagement transitioned to `ACTIVE_DILIGENCE`. Diligence period 21 days. PSA target 2026-06-15. First Morning Brief delivered to Janet at 06:00 on 2026-05-23.

## DefendableOS Notes

- The LOU is the highest-receipt-density document in the engagement lifecycle · every clause cites a receipt or a doctrine doc. This is intentional · the LOU is what the customer's auditor reads first in any future review.
- The LOU is where the PASS doctrine becomes contractual. The clause is not optional · it is constitutional. A LOU without it is a doctrine violation.
- Customers who request the PASS clause be removed are themselves a PASS signal · we don't engage with customers who want to disable our walk-away authority.
- The hurt-customer return path (PASS at month X → hurt at month X+6 → LOU at month X+9) is the highest-LTV path in the firm's history. The disclosure clause in those LOUs is the artifact future regulators will read with the most interest · don't shortcut it.

🐝 *First ink. Personal liability. Binding on process. The math has to pencil at sign.*
