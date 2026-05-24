# Letter of Understanding (LOU)

## Street Definition

"Did the LOU get signed?" — the founder asks at the Friday huddle before opening any new engagement file.

A **Letter of Understanding** (LOU) is the signed engagement contract between Defender and Principal. It's the document that converts a discovery conversation into a formal relationship. Closes the M (Meetings) stage of MAGIC · opens the in-flight phase.

In CRE terms · the LOU is the listing agreement · the exclusive-rep agreement · the engagement letter. Every senior broker who has ever closed a deal at scale lives by the same rule: **if it's not on paper · it didn't happen.** The LOU is the paper.

If a customer wants us to do the work without signing the LOU · they don't want a defender · they want a vendor · and we don't sell that.

## CRE Operator Meaning

A sr broker in CRE knows the LOU does five things at once:

1. **Names the parties** · principal · broker · authorized signatories
2. **Defines scope** · what's covered · what's not · what triggers an amendment
3. **Names the economics** · the fee · the structure · the floor · the ceiling · the variance buffer
4. **Defines the operating cadence** · how often we report · who calls whom · what the escalation pyramid looks like
5. **Names the exits** · termination for cause · termination for convenience · what happens to the books after

The LOU is the prenuptial agreement of a CRE relationship. The principal who refuses to sign a clear LOU is signaling something · usually that they want optionality at the broker's expense · usually a relationship best PASSED on.

## DefendableOS Definition

A **Letter of Understanding** in DefendableOS is the engagement-opening contract · drafted on the canonical template (`docs/examples/sample_letter_of_understanding.md`) · signed by both Defender (founder + sr broker) and Principal (decision-authority + financial-authority).

The LOU is filed as deed `DDEED-{org}-{vertical}-{customer}-LOU-v1` immediately upon execution · anchored on Hedera HCS topic 0.0.10291838 · resolvable at `ddeed-{org}-{vertical}-{customer}-lou-v1.{customer}.defendable.eth`. Amendments increment the version (`-v2`, `-v3`).

The LOU includes 13 mandatory sections (per the template):
- §1 Purpose · §2 Scope · §3 Success Criteria Framework · §4 Economics · §5 Operating Cadence · §6 Receipts/Deeds/Books · §7 Failure Handling · §8 PASS Doctrine · §9 Term and Termination · §10 Confidentiality · §11 Designated Recipients · §12 Acknowledgment · §13 Signatures

Every LOU must reference the canonical doctrine docs (§12 acknowledgment is mandatory). Principals sign acknowledging they've been walked through the operating model · NOT just sold a service.

## Backend Representation

```json
{
  "lou.lou_id": {"type": "string", "primary_key": true},
  "lou.engagement_id": {"type": "string", "fk": "engagement.engagement_id"},
  "lou.version": {"type": "integer"},
  "lou.deed_id": {
    "type": "string",
    "pattern": "DDEED-.+-LOU-v[0-9]+"
  },
  "lou.template_version": {"type": "string", "default": "v1.0"},
  "lou.effective_date": {"type": "date"},
  "lou.term_months": {"type": "integer"},
  "lou.auto_renew": {"type": "boolean"},
  "lou.tier": {
    "type": "enum",
    "values": ["T1_PILOT", "T2_PRODUCTION", "T3_WHITE_GLOVE", "T4_EMBEDDED"]
  },
  "lou.cost_to_mint_ceiling_per_deed_usd": {"type": "float"},
  "lou.monthly_floor_usd": {"type": "float"},
  "lou.formula_change_buffer_pct": {"type": "float", "default": 10.0},
  "lou.fix_or_refund_window_days": {"type": "integer", "default": 90},
  "lou.signature_defender_founder": {"type": "boolean"},
  "lou.signature_defender_sr_broker": {"type": "boolean"},
  "lou.signature_principal_decision": {"type": "boolean"},
  "lou.signature_principal_financial": {"type": "boolean"},
  "lou.acknowledgment_doctrine_docs_read": {"type": "boolean"},
  "lou.acknowledgment_cost_walk_completed": {"type": "boolean"},
  "lou.acknowledgment_hedera_verify_completed": {"type": "boolean"},
  "lou.amendments": {"type": "string_array", "nullable": true}
}
```

Schema files: `docs/schemas/lou.schema.json`

## Client Explanation

The **Letter of Understanding** is our engagement contract. It's the document we sign together that opens the formal relationship. It names what we do · what you pay · how we report · what triggers escalation · how termination works · what happens to your records after.

We walk you through every section before signing. We don't email a PDF and ask for a signature · we book a 60-minute working session to walk the document · answer questions · and capture any tailoring you need. The walk is part of the discipline · not a courtesy.

The LOU is itself filed as a Defendable Deed · anchored on Hedera mainnet · independently verifiable. The contract that governs the relationship lives on the same trust layer as the work we do under it. That's intentional.

## Jr Broker Use

You don't draft the LOU. The sr broker does. But you support:

- **Capture the principal's intent** during the Appraisals stage so the sr broker has clean inputs
- **Confirm the LOU acknowledgments** before the walk meeting (principal has the doctrine docs · principal has read at least the summary)
- **Coordinate the walk meeting** logistics (calendar invites · screen-share setup · scribe role)
- **Verify the e-signature workflow** is working (don't surprise the principal with broken DocuSign during the close)
- **File the signed LOU** in the engagement folder · trigger the deed-issuance pipeline · confirm the deed lands on Hedera within 24 hours

Don't ever modify the LOU template without sr broker review. The template is a doctrine artifact · NOT a freely-editable doc.

## Sr Broker Use

The sr broker:

- **Drafts the LOU from the canonical template** · tailoring §2 (scope) · §3 (success criteria framework) · §4 (economics) · §5 (cadence) · §11 (recipients) for the specific engagement
- **Walks the LOU with the principal personally** · 60-90 minute session · NEVER asynchronously
- **Co-signs as Defender's sr broker** (the founder also signs)
- **Authorizes amendments** as the engagement evolves · with re-walk if material
- **Owns the renewal conversation** 60+ days before auto-renewal · re-walks the LOU at renewal · captures changes in v2 / v3 amendments

The sr broker is also the **dispute-first-responder** if any LOU clause is interpreted differently between sides. The sr broker walks the math · cites the section · escalates to founder only if not resolvable at sr-broker level.

## Tribunal Use

The Tribunal doesn't adjudicate the LOU itself (it's a contract artifact · not an output) · but:

- LOU-referenced success criteria become Tribunal inputs (they shape what HONEY · CONDITIONED · FAILED means for this engagement)
- LOU-defined cost-to-mint ceiling becomes a Tribunal rule-layer gate (any deed over ceiling triggers an operator_hygiene flag)
- LOU-defined escalation triggers become Tribunal escalation outputs (the Tribunal fires escalation events per the LOU pyramid)
- LOU acknowledgment status feeds engagement_health checks (un-acknowledged amendments flag the engagement)

## Evidence Required

For an LOU to be defensible:

- All 4 signatures captured (Defender founder + sr broker · Principal decision + financial)
- §12 acknowledgments confirmed in writing (3 acknowledgments · doctrine read · cost walked · Hedera verified)
- Deed issued and Hedera-anchored within 24 hours of last signature
- ENS resolution path confirmed live
- Engagement folder created with LOU referenced as primary contract artifact
- First Morning Brief delivered within 7 days of effective date

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **unsigned_lou** | Engagement spun up to ACTIVE without all required signatures | PROPOLIS · engagement reverted to INK_PENDING |
| **template_drift** | LOU drafted without canonical template · missing mandatory sections | PROPOLIS · re-draft required |
| **silent_amendment** | LOU modified mid-engagement without re-walk · principal not re-acknowledged | PROPOLIS · re-walk + re-sign |
| **acknowledgment_skipped** | §12 acknowledgments not confirmed before signature | JELLY · acknowledgment captured retroactively · flagged in books |
| **deed_anchor_failed** | LOU signed but Hedera anchor failed · not re-attempted within 24 hours | JELLY · operator hygiene · re-anchor required |
| **principal_mismatch** | LOU signed by non-decision-authority · later discovered | PROPOLIS · LOU re-paper + re-sign with correct authority |

## Scoring Impact

- **assignment_success**: HIGH (LOU clarity directly affects assignment success rates)
- **repair_lift**: MEDIUM (LOU amendments can repair scope drift mid-engagement)
- **validator_confidence**: HIGH (LOU is the foundational evidence artifact for any engagement-level audit)
- **risk_temperature**: INVERSE (clear LOU = low risk · vague LOU = high risk)
- **probability_of_close**: HIGH (well-walked LOU is a strong predictor of healthy engagement closes)
- **evidence_strength**: HIGH (signed-and-anchored LOU is the strongest engagement-level evidence)
- **cost_to_mint**: NEUTRAL (drafting the LOU is operator-margin time · amortized across the engagement)

## Deed / Receipt Impact

- **Receipt fields touched**: every receipt under any assignment under the engagement references the LOU deed_id for contract-trace
- **DDEED class impact**: the LOU itself IS a DDEED (`DDEED-{org}-LOU-{slug}-v1`)
- **Books and records layer**: all 5 layers · LOU deed_id is a join key for any engagement-level audit query
- **5 Proofs touched**: ALL FIVE (the LOU deed carries Origin · Quality · Process · Economics · Trust like any other DDEED)

## Related Terms

- [engagement](engagement.md) · the relationship the LOU opens
- [principal](principal.md) · the signer on the customer side
- [assignment](assignment.md) · the work orders authorized by the LOU
- [closing-statement](closing-statement.md) · the per-assignment artifact that reports vs LOU criteria
- [morning-brief](morning-brief.md) · the daily cadence the LOU defines
- [pass-doctrine](pass-doctrine.md) · the protocol that screens LOU intake

## Example

> **LOU**: `DDEED-DOV-LOGISTICS-ACME-LOU-v1`
>
> **Engagement**: `ENG-DOV-LOGISTICS-ACME-0001`
>
> **Effective**: 2026-03-12 · 12-month initial term · auto-renew enabled · 60-day notice required
>
> **Tier**: T3 · White-Glove · effective rate $0.0416/deed · monthly floor $8,500 · +10% formula buffer · 90-day Fix-or-Refund
>
> **Signatures captured 2026-03-12**:
> - Donovan Mackey · Founder · Defender
> - Jenny Reyes · Sr Broker · Defender
> - Jane Smith · COO · Principal (decision authority)
> - Mike Chen · CFO · Principal (financial authority)
>
> **Acknowledgments**:
> - §12 doctrine docs read (all 5 referenced): confirmed via separate signed acknowledgment 2026-03-10
> - Cost-to-mint 7-component walk completed: 2026-03-11 (45-min Zoom with Mike + Jane + Jenny)
> - Hedera verify completed: 2026-03-11 (sample deed verified live during the cost walk)
>
> **Hedera anchor**: topic 0.0.10291838 · seq 8398122 · consensus 2026-03-12T17:42:08.103291Z
>
> **ENS**: `ddeed-dov-logistics-acme-lou-v1.acme.defendable.eth` (resolvable since 2026-03-12T17:46:11Z)

## DefendableOS Notes

- The LOU is a Class A 5-cap asset. It's worth more than the fee revenue · because it's the contract that survives team rotations · regulatory inquiries · and 10-year audits.
- Re-walking the LOU at renewal is the discipline that prevents silent drift. We never silent-renew on T3 / T4 tiers.
- The LOU template lives in this repo (`docs/examples/sample_letter_of_understanding.md`) on purpose · the template IS doctrine · changes to it require SH1 + SH5 + founder review.
- Every LOU is also a marketing artifact (sanitized). Signed LOUs aggregated over time become a Class A 5-cap brand asset of their own · "8,400 deeds and 47 signed LOUs" is more credibility than any landing page.

🐝 *The LOU is the paper. The paper is the trust. The trust is the engagement.*
