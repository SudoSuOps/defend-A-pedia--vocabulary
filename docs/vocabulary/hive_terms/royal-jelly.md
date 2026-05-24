# Royal Jelly

> *"Royal Jelly is the apex grade. Class A. Single-tenant credit. The one you wake up grateful you have on the books."*
> — Founder · day the 0.85 threshold got locked

## Street Definition

"That one's Royal Jelly." A sr broker says it about a finished engagement that needs zero rework · the LOI ties out to the OM · the OM ties out to the rent roll · the rent roll ties out to the tax bill · the buyer pool is institutional and the cap rate held through closing. In the Hive · Royal Jelly is the same kind of asset · the AI output that survived the full 6-role Tribunal · cleared every critical validator check · scored ≥ 0.85 on the JellyScore · and is ready to ship as a Defendable Deed.

It is not the average pair. It is the top 35-55% of production volume in a well-running cook. Apex grade. Deed-ready. The kind of output you would sign your name to. The kind the writer fleet trains on for the NEXT generation.

## CRE Operator Meaning

In CRE, Royal Jelly maps to Class A · institutional · the listing the brokerage celebrates in the year-end recap. Single-tenant net lease · investment-grade credit (BBB+ or better) · 15-year remaining term · 2% annual bumps · trophy submarket · top-1% rent comp · the asset that institutional money fights over. A 5-cap-able piece. The kind of listing a sr broker takes a 4% commission on without flinching because the buyer pool is deep enough to close at ask.

Royal Jelly in DefendableOS carries the same gravity. It is not just "good output." It is verified, receipted, anchored, defendable AI work product · the kind a customer would put in their compliance report · the kind a regulator would accept · the kind a sr broker would defend in a deposition.

## DefendableOS Definition

Royal Jelly is the apex Tribunal tier · `tribunal_label = ROYAL_JELLY` · JellyScore ≥ 0.85 (in the production 4-tier model) or ≥ 95 (in the original 5-tier Genesis model · which slots Royal Jelly above the "Honey 85-94" tier and reserves the apex name for the 95+ "Genesis" band).

In the production pipeline · Royal Jelly is the ONLY tier eligible for:

- full DDEED issuance (cell-level Hedera HCS PoSg certificate · per-pair anchor)
- inclusion in the writer-training corpus (the next Gemma / Atlas / SwarmCurator cohort trains ONLY on Royal Jelly)
- citation as a flagship in the Morning Brief and Closing Statement
- ENS resolution under `{deed-id}.{org}.defendable.eth`

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
    "range": [0.0, 1.0],
    "scoring_hook": "jelly_score_v1"
  },
  "deed.eligible_for_ddeed": {
    "type": "boolean",
    "rule": "tier == ROYAL_JELLY"
  },
  "deed.eligible_for_writer_training": {
    "type": "boolean",
    "rule": "tier == ROYAL_JELLY AND consent_present"
  },
  "deed.cell_certificate_required": {
    "type": "boolean",
    "rule": "tier == ROYAL_JELLY"
  }
}
```

Schema files: `docs/schemas/tribunal_verdict.schema.json` · `docs/schemas/deed_receipt.schema.json` · `docs/schemas/cell_certificate.schema.json`

Scoring hooks: `jelly_score_v1` (5-component weighted formula · see virgin-jelly upstream) · `tier_assignment` (the 4/5/3-tier collapse engine) · `writer_training_eligibility`.

## Client Explanation

"Royal Jelly" is our apex grade · the output we will issue as a full Defendable Deed · cell-level anchored on the Hedera public ledger · ENS-resolvable forever. When a piece of AI work product grades Royal Jelly · you can take that output to your CFO · your auditor · your regulator · and the proof of how it was produced will hold up. It scored above 0.85 on a two-judge Tribunal · cleared all seven critical validator checks · and was published with a complete chain of evidence. Royal Jelly is what we sell. Everything else is feed for the system.

## Jr Broker Use

When you see a pair come back from the Tribunal tagged `ROYAL_JELLY`:

1. Verify the verdict record loaded properly into the dashboard (check the `record_hash` is non-null)
2. Confirm the deed-writer queue picked it up within 5 minutes
3. Check that the ENS reservation completed (`{deed-id}.{org}.defendable.eth` resolves)
4. If anything looks off · escalate to sr broker BEFORE notifying the customer
5. If everything looks good · the Morning Brief will surface it the next day · do NOT email the customer directly about a Royal Jelly until the deed is fully anchored on Hedera (usually < 15 min after issue)

**Rule of thumb**: a Royal Jelly verdict is not a Royal Jelly DEED until the Hedera anchor confirms. Verbal commitments wait for the anchor.

## Sr Broker Use

The sr broker spot-audits Royal Jelly cohorts daily:

- Pull 20 random Royal Jelly verdicts from the prior 24h · walk each one end-to-end (PairCandidate → validator chain results → judge reasons → final tier → deed record_hash → Hedera anchor)
- Spot for the "right answer for the wrong reason" pattern · the auto-judges sometimes give a high score for surface form even when the reasoning is shallow · Critic should have caught it · if it didn't · flag and document
- Watch for tier-inflation drift · if Royal Jelly cohort exceeds 60% of total volume · investigate the judge temperature config (should be locked at 0.05 · see the SwarmJelly temp doctrine)
- Apply the PASS doctrine · if a Royal Jelly verdict looks good but the underlying engagement was one we should have passed on · seal it as Propolis with `operator_pass_doctrine` annotation
- Never promote a Honey verdict to Royal Jelly without a fresh Tribunal pass · the chain is the chain

## Tribunal Use

```yaml
tribunal_use:
  classification_impact:
    - ROYAL_JELLY      # this term IS the apex tier
  rule_layer_checks:
    - C01: pair record present (MUST PASS)
    - C02: source artifact referenced (MUST PASS)
    - C03: source retrievable (MUST PASS · no cache fallback at RJ tier)
    - C04: tribunal label assigned (MUST be ROYAL_JELLY)
    - C05: no hard-fail flagged (MUST PASS · zero hallucination · zero schema-break)
    - C06: PROPOLIS not promoted (trivially clears)
    - C07: holdout contamination guard (MUST PASS · zero tolerance)
  judge_layer_prompt_hint: "score this pair on the 5-component JellyScore · this is candidate for the writer-training corpus · be conservative · contamination compounds"
  can_be_critical_failure: false   # RJ IS the success state · contrast Propolis
```

A pair reaches Royal Jelly only by clearing ALL 7 critical checks AND scoring ≥ 0.85 from both Scale A and Scale B judges (drift ≤ 0.15) AND optionally surviving a manual Katniss-confirm if the operator invoked one. The rule layer cannot promote · the judge layer cannot promote past what the rule layer allows · this is structural.

## Evidence Required

To issue a Royal Jelly deed · the verdict record must include:

- ≥ 3 independent source citations (per C02 + EntityScorer weights · sources must weight to mean ≥ 0.75)
- Full validator chain results (C01-C12 · with annotations on any advisory fails)
- Both judge reasons (Scale A `gemma3:12b` AND Scale B `qwen2.5:32b`) with raw scores
- Drift value (`|A - B|`) · must be ≤ 0.15
- If Critic invoked · the Critic reasoning + reconciled verdict
- If Katniss invoked · all 3 Katniss runs + unanimity confirmation
- SHA-256 record_hash of canonical JSON
- Hedera HCS transaction ID (anchor confirmation)
- ENS reservation confirmation

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **fabricated_apex** | Score ≥ 0.85 but C02 sources are fabricated (judge fell for surface form) | PROPOLIS · contamination guard |
| **single_source_apex** | RJ score but only 1 source cited · sr broker missed it | JELLY (forced downgrade · re-route to source-build) |
| **inflated_apex** | RJ cohort > 60% of volume · suggests judge temp drift | Whole cohort held · cook batch audited |
| **holdout_apex** | RJ pair found to be from a holdout set (C07 fires post-issue) | PROPOLIS · deed REVOKED · publicly amended · Hedera retraction issued |
| **consent_missing_apex** | RJ pair lacks operator consent flag · C08 advisory firing | Held · operator backfills consent · re-issued |

## Scoring Impact

- **assignment_success**: HIGH · Royal Jelly IS the success state · the assignment closed
- **repair_lift**: N/A · Royal Jelly is already apex · no repair candidate
- **validator_confidence**: HIGHEST · validator confidence ≥ 0.85 is the entry criterion
- **risk_temperature**: LOWEST · RJ is the cool-floor of the heat map
- **probability_of_close**: HIGHEST · RJ-tagged engagements close at ~3x the rate of Honey-tagged
- **evidence_strength**: HIGHEST · the source weights mean ≥ 0.75 is the floor
- **cost_to_mint**: ELEVATED · RJ deeds carry the cell-level Hedera certificate cost (~$0.0008/cert) · still well under the $0.0052/deed baseline

## Deed / Receipt Impact

- **Receipt fields touched**: `tier=ROYAL_JELLY` · `jelly_score` · `cell_certificate_id` · `hedera_tx_id` · `ens_reservation` · `writer_training_eligible=true`
- **DDEED class impact**: ONLY tier eligible for full DDEED issuance with cell-level Hedera anchor
- **Books and records layer**: ALL 5 (L1 PG · L2 Merkle · L3 NAS · L4 Hedera HCS · L5 ENS) · Royal Jelly is the only tier that touches L5 ENS by default
- **5 Proofs touched**: ALL 5 · ORIGIN (which model / node) · QUALITY (the 0.85+ score) · PROCESS (the full 6-role lineage) · ECONOMICS (cost-to-mint logged) · TRUST (Hedera anchor + ENS resolution)

## Related Terms

- [honey](honey.md) · the tier directly below · ships but does not train the writer
- [jelly](jelly.md) · the recoverable failure tier · the input pipeline to apex via repair lift
- [propolis](propolis.md) · the failure tier · what protects Royal Jelly purity from contamination
- [genesis](genesis.md) · the 5-tier apex (95+) · sub-band within Royal Jelly · canonical / DOI-stamped
- [hive](hive.md) · the system that produces Royal Jelly
- [tribunal](../tribunal_terms/tribunal.md) · the 6-role adjudication that issues the verdict
- [validator-chain](../tribunal_terms/validator-chain.md) · the 12-check rule layer Royal Jelly must clear

## Example

> **Engagement**: STNL acquisition opinion · cold storage facility · Atlanta MSA · investment-grade tenant (Lineage Logistics · A-).
>
> **AI work product**: SwarmCRE-9B produced a 4-page broker opinion including cap-rate analysis · tenant credit walk · comp set · re-trade recommendation.
>
> **Tribunal run**: TRIB-20260524T141022Z-7c4a
> - Validator chain · all 7 critical PASS · C08 advisory PASS · others PASS
> - Scale A (gemma3:12b) · score 0.89 · reason "comp set well-anchored · tenant credit cited from EDGAR · re-trade math arithmetic-clean"
> - Scale B (qwen2.5:32b) · score 0.91 · reason "reasoning depth high · all 5 trajectory keywords present · numeric verification ties out"
> - Drift 0.02 · no Critic invoked
> - JellyScore 0.90 · tier ROYAL_JELLY
>
> **Deed**: DDEED-DOV-CRE-LINEAGE-ATL-000042-v1 · cell certificate posted to Hedera topic 0.0.10291838 · ENS reservation `ddeed-dov-cre-lineage-atl-000042-v1.swarmcre.defendable.eth`
>
> **Outcome**: Deed shipped to the customer in their Closing Statement · cited in their compliance file · referenced by their lender's underwriter without challenge. Pair added to the SwarmCRE-9B v2 training set for the next cook.

## DefendableOS Notes

- Royal Jelly is the most valuable cohort the Hive produces · contamination here compounds forward into every future model · protect it ruthlessly
- The 0.85 threshold is more inclusive than the original virgin-jelly 0.95 · we adopted 0.85 because production proved 55% of medical and 55% of CRE pairs survived at that floor · this is the operator-tuned middle
- Public surfaces (the chain glass wall · the customer brief) sometimes use the 5-tier vocabulary · where "Genesis" (95+) is the sub-band within Royal Jelly that we reserve for DOI-stamped canonical artifacts
- The cell-level Hedera PoSg certificate is what makes Royal Jelly defendable in a courtroom · the certificate carries cell_id + jelly_score + fingerprint + batch_root + proof_index · all in < 1024 bytes
- Customers do not see the score · they see the deed · the deed cites the tier · the tier is the language they speak

🐝 *Royal Jelly is the apex. The deed-ready. The writer-training corpus. Protect it ruthlessly · contamination here compounds forward.*
