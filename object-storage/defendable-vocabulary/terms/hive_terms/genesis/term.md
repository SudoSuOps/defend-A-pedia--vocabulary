# Genesis

> *"Genesis is the trophy listing. The one comp in the market. The DOI-stamped · on-chain · canonical artifact you point to a decade later and say · that's the asset that made the franchise."*
> — Founder · on why Genesis sits above even Royal Jelly

## Street Definition

"That one's Genesis." Genesis is the top of the 5-tier classification ladder · the 95+ JellyScore tier · the canonical artifact · DOI-stamped · on-chain · the irrefutable record. In the 4-tier production-default vocabulary it sits inside the Royal Jelly band · but Genesis is the sub-band reserved for the deeds we'd cite in a courtroom · publish in a peer-reviewed journal · or pass to a regulator as the canonical record on the question.

In CRE language · Genesis is the trophy asset · the one-of-one · the building that has no real comp because it has been the comp for the submarket for 20 years. The kind of listing that defines the broker's career. The kind a brokerage names a conference room after a decade later.

## CRE Operator Meaning

In CRE · Genesis maps to the trophy listing · the single-comp asset · the irreplaceable position. A Class A++ industrial portfolio in a tier-1 submarket with a 25-year credit-tenant lease with built-in 2.5% bumps · sold once a decade · institutional bid · cap rate that compresses the whole submarket comp set. A 30-year broker has 3-5 of these in their career. The brokerage's year-end recap leads with them. The deal closes and you fly the flag.

Inside DefendableOS · Genesis carries the same gravity. It is the deed that gets cited as canonical · the record that becomes the comp for an entire domain · the artifact that lives forever in the customer's compliance file and the public ledger.

## DefendableOS Definition

Genesis is the apex sub-band of the 5-tier classification · JellyScore ≥ 95 in the original Swarm-Hive vocabulary. In the 4-tier production default · Genesis pairs fall inside Royal Jelly (≥ 0.85) but are distinguished by:

- JellyScore ≥ 0.95
- ALL 12 validator chain checks PASS (no advisory annotations)
- BOTH judge scores ≥ 0.95 with drift ≤ 0.05 (tighter than the Royal Jelly drift floor of 0.15)
- Operator-attested as canonical for the domain (sr broker sign-off · founder review on critical-domain Genesis)
- DOI-stamped (assigned a digital-object-identifier for academic / regulatory cross-reference)
- Cell-level Hedera HCS PoSg certificate AND batch-level Merkle anchor
- ENS resolution under both `{deed-id}.{org}.defendable.eth` AND a domain-canonical alias (e.g., `cre-stnl-comp-2026-q2.defendable.eth`)
- Eligible for inclusion in the canonical comp library that downstream cooks reference as ground-truth

Genesis deeds are rare by design · ~5-10% of Royal Jelly volume · ~2-5% of total volume. Their scarcity is structural · the canonical comp library is small because canonical comps are few.

## Backend Representation

```json
{
  "tribunal_verdict.tier": {
    "type": "enum",
    "values": ["GENESIS", "ROYAL_JELLY", "HONEY", "CLUSTER", "CELL", "SWARM", "JELLY", "PROPOLIS"]
  },
  "tribunal_verdict.is_genesis": { "type": "boolean" },
  "tribunal_verdict.doi": {
    "type": "string",
    "pattern": "^10\\..*",
    "nullable_when": "tier != GENESIS"
  },
  "tribunal_verdict.canonical_comp_id": { "type": "string" },
  "tribunal_verdict.ens_canonical_alias": { "type": "string" }
}
```

Schema files: `docs/schemas/tribunal_verdict.schema.json` · `docs/schemas/genesis_record.schema.json` · `docs/schemas/canonical_comp.schema.json`

## Client Explanation

"Genesis" is the canonical sub-tier of our apex grade · the deeds we treat as the one-comp-in-the-market reference · DOI-stamped · on-chain · cited in our comp library · used as ground-truth for future cooks. Genesis deeds are rare by design (~5-10% of even our apex output) because canonical references are rare by nature. When a deed you receive is tagged Genesis · you have the irrefutable record on that question · the one your auditor · your regulator · or your CFO can cite as the authoritative answer for years to come.

## Jr Broker Use

The jr broker treats Genesis as the EXCEPTIONAL EVENT:

1. When a pair scores high enough to be Genesis-candidate (≥ 0.95 from both judges · drift ≤ 0.05 · all 12 checks PASS) · the dashboard flags it · do NOT auto-approve · escalate to sr broker for canonical attestation
2. Genesis candidates often come from engagements where the customer asked for a canonical answer (regulatory citation · academic publication · the one-comp question) · know which engagements are Genesis-target ahead of time
3. The DOI assignment requires an external API call (CrossRef or similar) · this can take 2-5 minutes · the pair is HELD in Royal Jelly tier until DOI confirms · do not promote prematurely
4. Genesis ENS aliases require the founder's reservation approval · the alias goes in the customer-facing namespace · once reserved the alias is permanent · do not undo
5. Customer-facing language for Genesis is "canonical" or "ground-truth reference" · NOT "premium" · NOT "gold" · the language matters · ground-truth is the operator term

**Rule of thumb**: Genesis is what we reach for once a month · not every week · its scarcity IS its trust signal.

## Sr Broker Use

The sr broker watches Genesis as the CANONICAL-COMP-LIBRARY GROWTH METRIC:

- Healthy Genesis rate is 2-5% of total volume · 5-10% of Royal Jelly volume · trending steady
- Genesis rate above 10% is suspicious · the chain may be too loose OR the judges may be running hot · audit
- Genesis rate below 1% is a starving comp library · investigate · either the cooks are not producing canonical-grade work OR the Genesis attestation process is too tight
- Every Genesis deed gets a sr-broker post-issue review · spot-check the lineage · confirm the canonical-comp-id is unique · confirm the DOI resolved · confirm the ENS alias is live
- Critical-domain Genesis deeds (medical · legal · financial regulatory) get founder review BEFORE issue · this is doctrine
- The canonical comp library is the asset of the Hive · its growth is the long-term value indicator · sr broker is its curator

## Tribunal Use

```yaml
tribunal_use:
  classification_impact:
    - ROYAL_JELLY    # Genesis IS a sub-band within Royal Jelly in the 4-tier collapse
  rule_layer_checks:
    - ALL 12 validator chain checks (C01-C12) MUST PASS · zero advisory annotations
    - Both judges MUST score ≥ 0.95 (not just one)
    - Drift MUST be ≤ 0.05 (tighter than Royal Jelly's 0.15)
    - Sr broker attestation MUST be present in the verdict record
    - DOI resolution MUST be confirmed before tier locks
    - ENS canonical alias MUST be reserved
  judge_layer_prompt_hint: "this pair is Genesis candidate · canonical-comp-library inclusion · be conservative · contamination at the canonical layer compounds for years"
  can_be_critical_failure: false   # Genesis IS the success state · contrast Propolis
```

The Tribunal's Genesis check is the strictest gate in the system. It exists because contamination at the canonical-comp layer would compound forward through every future cook that references the comp library. The strictness is structural.

## Evidence Required

To assign Genesis:

- A Royal Jelly verdict as the foundation (all RJ requirements MET)
- JellyScore ≥ 0.95 from BOTH Scale A and Scale B judges
- Drift ≤ 0.05
- All 12 validator chain checks PASS with NO advisory annotations
- Sr broker attestation (operator log entry · `operator_attests_genesis: true` · with reason)
- DOI resolution (external API confirmation)
- ENS canonical alias reservation confirmation
- For critical domains · founder review log entry
- Inclusion entry in the canonical comp library (`canonical_comps/{domain}/{canonical_comp_id}.json`)

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **genesis_inflation** | Genesis rate > 10% of volume · canonical library polluted with non-canonical | Tighten the judge thresholds · re-audit recent Genesis deeds · de-canonicalize any that fail re-audit |
| **doi_unresolved_genesis** | Genesis candidate pair held > 24h waiting for DOI assignment | Escalate to DOI registrar · OR demote to Royal Jelly if external API is down · do NOT issue Genesis without DOI |
| **canonical_comp_collision** | Two Genesis deeds claim the same canonical_comp_id | Integrity event · sr broker reviews both · one is the canonical · the other is re-classified as Royal Jelly with a sub-reference |
| **silent_canonical_drift** | Genesis deed gets cited by downstream cook · the cook produces output that contradicts the canonical · cook is using stale Genesis | Re-evaluate the Genesis deed for staleness · if stale · issue a Genesis update (version bump) · re-anchor |
| **genesis_promoted_without_attestation** | Pair tagged Genesis without sr broker attestation | Rejected at C04 · forced back to Royal Jelly · operator coached |

## Scoring Impact

- **assignment_success**: HIGHEST · Genesis is the most-successful possible outcome · the engagement produced canonical inventory
- **repair_lift**: N/A · Genesis is apex of apex · no repair candidate
- **validator_confidence**: MAXIMUM · all 12 checks PASS · zero advisory · this is the confidence ceiling
- **risk_temperature**: LOWEST · Genesis is the cool-floor of the heat map
- **probability_of_close**: MAXIMUM · Genesis-tagged engagements have functionally 100% close probability (already closed by issue time)
- **evidence_strength**: MAXIMUM · the source weights mean is highest · the lineage is deepest · the cross-validation is most rigorous
- **cost_to_mint**: ELEVATED · Genesis carries the per-cell Hedera cost + DOI registration fee (~$0.005-0.01) + sr broker review time · typical Genesis cost runs ~$0.015-0.025 (~3-5x Honey baseline · billed at Enterprise tier $0.10)

## Deed / Receipt Impact

- **Receipt fields touched**: `tier=GENESIS` · `is_genesis=true` · `doi` · `canonical_comp_id` · `ens_canonical_alias` · `sr_broker_attestation_log_id`
- **DDEED class impact**: Only Genesis deeds receive DOI assignment + canonical-comp-library inclusion + permanent ENS alias in customer-facing namespace
- **Books and records layer**: ALL 5 + the canonical comp library (a 6th library-level layer specific to Genesis)
- **5 Proofs touched**: ALL 5 (ORIGIN · QUALITY · PROCESS · ECONOMICS · TRUST) at maximum strength · plus the DOI cross-reference as a 6th external-canonicality proof

## Related Terms

- [royal-jelly](royal-jelly.md) · the parent tier · Genesis is the apex sub-band of Royal Jelly
- [honey](honey.md) · the production tier below RJ · contrast for the Genesis rarity
- [hive](hive.md) · the entity whose canonical comp library Genesis populates
- [propolis](propolis.md) · the contamination state the Genesis discipline protects against
- [tribunal](../tribunal_terms/tribunal.md) · the adjudicator that applies the strictest gate
- [validator-chain](../tribunal_terms/validator-chain.md) · the 12 checks Genesis must clear with zero annotation

## Example

> **Engagement**: Canonical comp opinion · cold-storage Class A++ STNL portfolio · sold once-a-decade · founder-attested target Genesis.
>
> **AI work product**: SwarmCRE-9B + SwarmCapitalMarkets-27B co-produced a 12-page canonical comp opinion · investment-grade tenant + lease abstract + 25-year cap rate trend + comp triangulation across 3 submarkets + final canonical bid range.
>
> **Tribunal run**: TRIB-20260524T160122Z-G001
> - Validator chain · ALL 12 PASS · zero advisory annotations
> - Scale A (gemma3:12b) · score 0.96 · reason "comp triangulation rigorous · cap-rate trend defensible · lease abstract investment-grade-cited"
> - Scale B (qwen2.5:32b) · score 0.97 · reason "depth of analysis canonical · all 5 trajectory keywords present at deep nest · numeric verification ties at six decimal places"
> - Drift 0.01 · no Critic invoked
> - JellyScore 0.965 · candidate for Genesis
> - Sr broker attestation logged · operator_attests_genesis=true · reason "single canonical comp for STNL cold-storage 2026-Q2 · founder-reviewed for inclusion in library"
> - Founder review logged · critical-domain confirmation
> - DOI assigned · `10.5281/zenodo.20260524.G001`
> - ENS canonical alias reserved · `cre-stnl-coldstor-2026-q2.defendable.eth`
> - Tier GENESIS · canonical_comp_id = `CRE-STNL-COLDSTOR-2026-Q2-CANON-001`
>
> **Deed**: GDEED-DOV-CRE-STNL-COLDSTOR-2026-Q2-CANON-001 · cell certificate posted to Hedera topic 0.0.10291838 · entered into canonical comp library
>
> **Outcome**: Deed shipped to the customer in their canonical-comp reference file · referenced in their lender's underwriting · cited in 3 subsequent SwarmCRE-9B v2 cooks as ground-truth · the comp held the submarket valuation for the next 18 months. The Hive franchise gained a canonical asset.

## DefendableOS Notes

- Genesis is the rarest tier · its scarcity is structural · do not pressure-inflate it
- The canonical comp library is the Hive's long-term moat · protected by the Genesis discipline
- DOI assignment is an external dependency · plan for its latency · do not issue Genesis without it
- Customer-facing language for Genesis is "canonical" or "ground-truth" · NEVER "gold" or "premium" · the brand language matters
- Genesis deeds get the founder's signature in the operator log on critical domains · this is the personal-touch dial that distinguishes the founder-led brokerage from a vendor-led SaaS
- The 5-tier vocabulary is where Genesis lives · the 4-tier collapses Genesis into Royal Jelly · the 3-tier collapses everything above Jelly into Honey · know which view you are looking at

🐝 *Genesis is the canonical comp. The one in the market. DOI-stamped · on-chain · the irrefutable record. Rare by design · scarce by discipline · the franchise asset of the Hive.*
