# Honey

> *"Honey ships. Royal Jelly trains. Jelly gets repaired. Propolis teaches the next generation what failure looks like. That's the whole sort."*
> — Founder · explaining the 4-tier in 22 words

## Street Definition

"That batch came back Honey · ship it." Honey is production-grade AI work product. The 4-tier middle band. JellyScore 0.70 to 0.84 (or 85-94 in the original 5-tier · "Honey" is the constitutional name for the production-safe band in both views). Honey clears the validator chain · clears two judges · ships to the customer · gets receipted · lands in books-and-records. It does NOT enter the writer-training corpus · that is reserved for Royal Jelly · but it absolutely earns its keep. Most of the volume the customer sees is Honey · and that is fine.

If Royal Jelly is the Class A trophy listing · Honey is the Class B with stable tenant and a clean rent roll · the listing that pencils for core-plus money · the listing that closes consistently without drama.

## CRE Operator Meaning

In CRE · Honey is the Class B asset · decent location · adequate cap rate · replaceable but not commodity · the listing a brokerage runs all year long because it pays the bills. The investment-grade tenant might be one notch shy of full institutional (BBB versus BBB+) · the comp set is solid but not trophy · the buyer pool is core-plus rather than core · and the deal pencils for everyone involved. You don't celebrate Honey deals at the year-end recap · you celebrate the YEAR of Honey deals that built the book.

Inside DefendableOS · Honey carries that same operating role. It is the volume tier. It is what keeps the Hive paying for itself. It is the mass of production that the customer-facing operations depend on day-to-day. Royal Jelly is the moat · Honey is the cash flow.

## DefendableOS Definition

Honey is the second-from-top Tribunal tier · `tribunal_label = HONEY` · JellyScore 0.70-0.84 (in the production 4-tier model) or 85-94 (in the 5-tier Genesis model · where "Honey" is the same name applied to the band one step below Genesis).

In the production pipeline · Honey is eligible for:

- receipt issuance (per `deed_receipt.schema.json`) and publication to books-and-records
- inclusion in the Morning Reconciliation Brief as part of the daily volume
- batch-level Merkle root anchoring to Hedera HCS (NOT per-cell · that is reserved for Royal Jelly)
- citation in the Closing Statement when the engagement scope calls for production output

Honey does NOT enter the writer-training corpus and does NOT receive a cell-level Hedera PoSg certificate. Those privileges are reserved for Royal Jelly · contamination protection.

## Backend Representation

```json
{
  "tribunal_verdict.tier": {
    "type": "enum",
    "values": ["ROYAL_JELLY", "HONEY", "JELLY", "PROPOLIS"],
    "scoring_hook": "tier_assignment"
  },
  "tribunal_verdict.jelly_score": {
    "type": "float",
    "range": [0.70, 0.84],
    "scoring_hook": "jelly_score_v1"
  },
  "deed.eligible_for_receipt": {
    "type": "boolean",
    "rule": "tier IN (ROYAL_JELLY, HONEY)"
  },
  "deed.eligible_for_writer_training": {
    "type": "boolean",
    "rule": "tier == ROYAL_JELLY"
  },
  "deed.merkle_batch_anchor_only": {
    "type": "boolean",
    "rule": "tier == HONEY"
  }
}
```

Schema files: `docs/schemas/tribunal_verdict.schema.json` · `docs/schemas/deed_receipt.schema.json`

Scoring hooks: `jelly_score_v1` · `tier_assignment` · `merkle_batch_anchor`.

## Client Explanation

"Honey" is our production grade · the AI work product that has cleared the full Tribunal review and is safe to ship to you with a receipt and a record-hash you can audit. Honey-grade output backs the day-to-day operating reports you receive from us · the Morning Briefs · the routine analyses · the volume work that keeps your operations running. It is anchored at the batch level to the Hedera public ledger so the lineage is verifiable. When you want the apex grade for a regulatory filing or a flagship customer deliverable, we issue Royal Jelly. For everything else, Honey is the working standard.

## Jr Broker Use

When a pair comes back tagged HONEY:

1. Confirm the receipt was issued (`receipt_id` populated · `record_hash` non-null)
2. Confirm the batch this pair belongs to is queued for the next Merkle anchor (typically anchored in 50-pair batches · should land within an hour)
3. Surface the pair in the customer's daily volume report (do NOT flag it as a flagship · that is Royal Jelly only)
4. If a customer asks "is this Royal Jelly?" the answer is HONEST · "no · it is Honey · production-grade · receipted · audit-ready · the Royal Jelly tier is reserved for [reason]"
5. NEVER · ever · misrepresent Honey as Royal Jelly · the chain catches it · the customer catches it · the founder catches it · the brand catches it

**Rule of thumb**: Honey is honest production. Don't dress it up. Don't apologize for it. It is what most of the work is.

## Sr Broker Use

The sr broker watches the Honey distribution for upstream signal:

- Healthy Honey % is 25-40% of total volume in a well-running cook · if Honey is over 50% · the cook is producing inconsistent reasoning depth · investigate
- If Honey is under 20% · the cook is bimodal (lots of Royal Jelly + lots of Jelly · few middles) · this can be healthy in a high-discipline domain · or a sign of judge calibration drift in a noisier domain
- Spot-audit Honey pairs that came WITHIN 0.02 of the Royal Jelly threshold · these are the candidates a sloppy operator might try to promote · the chain prevents it but you want to see WHY they fell short · usually a single advisory check fired (C08 consent missing · C09 redaction questionable) and the operator can sometimes legitimately backfill
- Honey deeds that get cited by the customer in their own compliance file should be flagged for sr broker review · we want to know what production work the customer is leaning on so we can prioritize the right uplifts

## Tribunal Use

```yaml
tribunal_use:
  classification_impact:
    - HONEY      # this term IS the Honey tier
  rule_layer_checks:
    - C01: pair record present (MUST PASS)
    - C02: source artifact referenced (MUST PASS)
    - C03: source retrievable (MUST PASS · cache fallback ALLOWED at Honey tier within 30-day window)
    - C04: tribunal label assigned (MUST be HONEY)
    - C05: no hard-fail flagged (MUST PASS)
    - C06: PROPOLIS not promoted (trivially clears)
    - C07: holdout contamination guard (MUST PASS · zero tolerance same as Royal Jelly)
  judge_layer_prompt_hint: "score this pair on the 5-component JellyScore · this is production-safe candidate · grade honestly · do not inflate to apex"
  can_be_critical_failure: false   # Honey IS a success state · contrast Propolis
```

Honey is the most common success outcome in production. It clears the same critical checks as Royal Jelly · with two operational differences · C03 allows a cached-source fallback (Royal Jelly does not) and the writer-training pipeline rejects Honey (the writer trains only on Royal Jelly).

## Evidence Required

To issue a Honey receipt · the verdict record must include:

- ≥ 2 independent source citations (per C02 · 1 fewer than Royal Jelly)
- Full validator chain results (C01-C12)
- Both judge reasons (Scale A AND Scale B) with raw scores in the 0.70-0.84 band
- Drift value ≤ 0.15 · OR Critic-reconciled verdict if drift was > 0.15
- SHA-256 record_hash of canonical JSON
- Batch Merkle root reference (Honey anchors at batch level · not per-pair)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **honey_misrepresented_as_apex** | Operator labels Honey as Royal Jelly in customer-facing material | Operator-discipline event · pair stays Honey but the misrep is logged · escalated |
| **stale_source_honey** | C03 source-retrievable used the cached fallback but cache is > 30 days old | JELLY · routed to source-refresh repair |
| **single_source_honey** | Only 1 source cited where 2+ required at Honey tier | JELLY (forced downgrade) |
| **honey_inflation** | Honey % > 50% of volume · judges running hot · false positives leaking up | Whole cohort flagged · judge temp config audited (should be 0.05) |
| **honey_starvation** | Honey % < 15% of volume · cook is bimodal · likely a corpus diversity issue upstream | Cook batch reviewed by sr broker · curator settings audited |

## Scoring Impact

- **assignment_success**: HIGH · Honey is a closed assignment · the deal pencils
- **repair_lift**: LOW · Honey already cleared · repair lift applies upstream from Jelly
- **validator_confidence**: HIGH · 0.70-0.84 is the production-safe band
- **risk_temperature**: LOW-MEDIUM · safer than Jelly · slightly higher than Royal Jelly because no cell-level anchor
- **probability_of_close**: HIGH · Honey-tagged engagements close at ~1.5x the rate of Jelly-tagged
- **evidence_strength**: HIGH · 2+ source citations mandatory · weights mean ≥ 0.65
- **cost_to_mint**: BASELINE · ~$0.0052/deed at batch-anchor level · cheaper than Royal Jelly per-pair

## Deed / Receipt Impact

- **Receipt fields touched**: `tier=HONEY` · `jelly_score` · `batch_merkle_root` · `receipt_id` · `writer_training_eligible=false`
- **DDEED class impact**: Eligible for receipt + batch Merkle anchor · NOT eligible for cell-level Hedera PoSg certificate
- **Books and records layer**: L1 PG · L2 Merkle · L3 NAS · L4 Hedera HCS (batch root only) · NOT L5 ENS by default
- **5 Proofs touched**: 4 of 5 · ORIGIN · QUALITY · PROCESS · ECONOMICS · (TRUST is batch-level not per-pair)

## Related Terms

- [royal-jelly](royal-jelly.md) · the tier directly above · the writer-training feedstock
- [jelly](jelly.md) · the tier directly below · the repair-candidate band Honey can fall to
- [propolis](propolis.md) · the failure tier Honey can be downgraded to if a critical check fires retroactively
- [hive](hive.md) · the system that grades
- [tribunal](../tribunal_terms/tribunal.md) · the adjudicator that assigns Honey
- [validator-chain](../tribunal_terms/validator-chain.md) · the 12 checks every Honey pair clears

## Example

> **Engagement**: Daily CRE deal-flow digest · industrial submarket scan · 14 listings reviewed.
>
> **AI work product**: SwarmCurator-9B produced a 2-page deal-flow digest summarizing the 14 listings with cap-rate ranges · tenant credit notes · re-trade flags on 3.
>
> **Tribunal run**: TRIB-20260524T091533Z-2f81
> - Validator chain · all 7 critical PASS · C09 advisory raised "PII scan partial · no PII present" (operator backfilled)
> - Scale A (gemma3:12b) · score 0.78 · reason "comp ranges sourced · 3 re-trade flags well-supported · reasoning depth moderate"
> - Scale B (qwen2.5:32b) · score 0.81 · reason "structure clean · numeric verification ties · would prefer 1 more source on the tenant credit notes"
> - Drift 0.03 · no Critic invoked
> - JellyScore 0.795 · tier HONEY
>
> **Receipt**: DCLAW-20260524T091533Z-2f81 · batch Merkle root anchored on Hedera within the hour
>
> **Outcome**: Digest shipped to the customer's morning deal-flow inbox · used to triage the 14 listings into a 3-listing call list · no further action required. Volume Honey · honest production · paid for itself.

## DefendableOS Notes

- Honey is honest production · don't dress it up · don't apologize for it · most of the work is Honey and that is correct
- The cache fallback on C03 is the operating-mercy that distinguishes Honey from Royal Jelly · production work often legitimately depends on cached sources where Royal Jelly demands a live fetch
- Customers who try to negotiate "everything Royal Jelly" should be educated · the cost to mint Royal Jelly on every output would burn the energy budget · Honey is what makes the unit economics work
- Honey contamination is a real risk in the inverse direction · if Honey starts getting promoted as Royal Jelly by operator pressure · the writer-training corpus contaminates · the next model degrades · we hold this line ruthlessly

🐝 *Honey ships. Most of the work is Honey. The cash flow runs on it. Don't apologize for it · earn it · publish it · receipt it · anchor the batch · move on.*
