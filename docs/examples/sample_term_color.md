# Color

> *Canonical example of the 13-section structure. Every term in `docs/vocabulary/` must follow this exact shape.*

## Street Definition

"What's the color on this one?" — a broker asks before stepping into a call.

**Color** is the qualified intel an operator has on an asset · the verified-by-touch knowledge a broker accumulates by walking the building · pulling the rent roll · checking comps · knowing who the seller is · knowing the buyer pool · knowing the financing market. It's the antidote to "what does the listing say" — it's what the broker KNOWS · not what's been pitched.

## CRE Operator Meaning

In CRE · "color on the asset" is the difference between a real broker and someone who just forwards listings. A sr broker on a $50M industrial portfolio has color on:

- The asset itself (deferred maintenance · clear-height · trailer count · power capacity)
- The seller's actual motivation (1031 deadline · partnership dispute · refi expiring)
- The buyer pool (who's looking · who's funded · who's been outbid recently)
- The financing market (debt yields · who's lending on this asset class)
- The market state (cap rate movements · supply pipeline · employment trends)

If you don't have color · you're not a broker. You're a forwarder.

## DefendableOS Definition

In DefendableOS · **Color** is the verified-evidence layer that a Tribunal-grade engagement carries. It maps to the `Proof of Process` and `Proof of Quality` pillars of the 5-Proof framework.

Color is what makes a deed defendable · not just issued. A deed without color is a claim. A deed with color is an attestation.

## Backend Representation

```json
{
  "asset.color_status": {
    "type": "enum",
    "values": ["VERIFIED", "PARTIAL", "UNVERIFIED", "MISSING"],
    "default": "MISSING"
  },
  "asset.color_evidence_count": {
    "type": "integer",
    "min": 0
  },
  "asset.color_last_refresh_at": {
    "type": "timestamp",
    "nullable": true
  },
  "engagement.color_score": {
    "type": "float",
    "range": [0.0, 1.0],
    "scoring_hook": "validator_confidence_weight"
  }
}
```

Schema files: `docs/schemas/evidence_record.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

"Color" is what we KNOW about the asset · not what's been claimed. When we open an engagement on your behalf · we build color by pulling independent sources · verifying numbers · talking to the market. The more color we have · the higher our confidence rating · the lower your risk · the better our recommendation pencils. No color · no deed.

## Jr Broker Use

When you open a new engagement · build a color file IMMEDIATELY:
- Pull at least 2 independent comps
- Verify any seller-reported numbers against EDGAR · CompStak · ATTOM · or the SwarmCurator CRE corpus
- Log every source you pulled (independent confirmation feeds `engagement.color_evidence_count`)
- Flag any contradiction in the `failure_modes` field
- If color is missing on a critical field · escalate to sr broker BEFORE drafting the LOU

**Rule of thumb**: if your color file has fewer than 5 independent sources · you don't have color yet.

## Sr Broker Use

The sr broker validates color by:
- Cross-referencing the jr broker's sources against the canonical Hive datasets (1.5M+ graded pairs in PostgreSQL)
- Challenging any claim that has < 3 independent confirmations
- Checking the timestamps · stale color (> 30 days) gets discounted
- Verifying source quality via the EntityScorer weights (EDGAR 0.90 · OpenAlex 0.85 · CRE News 0.65 · Reddit 0.50)
- Applying the PASS doctrine · if color contradicts the seller's pitch by > 25% · we pass on the listing OR re-pitch with corrected numbers

## Tribunal Use

The Tribunal uses color as a CRITICAL gate · NOT an advisory one:

- **Rule layer**: `color_evidence_count < 3` triggers automatic Tribunal verdict downgrade
- **Rule layer**: `color_status == MISSING` on a Class A engagement = PROPOLIS verdict (the deed cannot issue)
- **Judge layer**: Color quality is weighted into Tribunal's reasoning · drift ≤ 0.15 between Scale A and Scale B judges
- **Classification impact**: missing color caps a deed at Honey tier (cannot reach Royal Jelly)

## Evidence Required

To establish color · the engagement record must include:

- ≥ 3 independent source citations (with timestamps + source weights)
- Documentation of any contradictions surfaced (in `failure_modes`)
- Validator review checkmarks on the 7 critical checks (C01-C07 in `validator_chain.schema.json`)
- For Class A engagements: physical or live-equivalent site verification (broker site visit · drone footage · live tenant interview)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **fabricated_color** | Sources cited but don't actually confirm the claim (the broker invented the confirmation) | PROPOLIS |
| **stale_color** | All sources older than 30 days · market has moved | JELLY |
| **single_source_color** | Only 1 source cited where 3+ required | JELLY |
| **low_quality_source** | Sources are only Reddit/HN/RSS · no EDGAR/FRED/EDGAR-grade | JELLY |
| **contradicted_color** | Sources cited but they CONTRADICT each other · no reconciliation noted | PROPOLIS |
| **missing_critical_field** | Color on tenant credit OR financing OR seller motivation is MISSING | PROPOLIS for Class A |

## Scoring Impact

- **assignment_success**: HIGH · color is the foundation of every assignment · without it the deal is built on sand
- **repair_lift**: MEDIUM · SwarmFixer can sometimes add color post-hoc but it costs · prefer to gather upfront
- **validator_confidence**: HIGH · validators weight color heavily · low color → low confidence regardless of judge verdict
- **risk_temperature**: INVERSE · more color = lower risk
- **probability_of_close**: HIGH · deals with strong color close at 2-3× the rate of deals without
- **evidence_strength**: DIRECT · color evidence count IS evidence strength
- **cost_to_mint**: MEDIUM · gathering color costs energy but DEFICIT color costs more (rework + Tribunal downgrades)

## Deed / Receipt Impact

- **Receipt fields touched**: `evidence_count` · `source_weights_mean` · `color_age_days` · `validator_color_score`
- **DDEED class impact**: Royal Jelly deeds REQUIRE color_score ≥ 0.85 · Honey deeds require ≥ 0.70 · below 0.70 cannot become a deed
- **Books and records layer**: All 5 layers · color persists across L1 PostgreSQL → L2 Merkle → L3 NAS → L4 Hedera HCS → L5 ENS
- **5 Proofs touched**: PROCESS (the lineage of color-building) · QUALITY (the source weights) · TRUST (the validator confidence backing it)

## Related Terms

- [digest](../vocabulary/cre_terms/digest.md) · color is the input · digest is the output
- [color_score](../vocabulary/scoring_terms/color-score.md) · the numeric dial color drives
- [probability-of-close](../vocabulary/cre_terms/probability-of-close.md) · color is the strongest predictor
- [evidence-strength](../vocabulary/scoring_terms/evidence-strength.md) · the dial color directly feeds
- [validator-chain](../vocabulary/tribunal_terms/validator-chain.md) · the 12-check chain that audits color claims
- [honey](../vocabulary/hive_terms/honey.md) · deeds at the Honey tier require ≥ 0.70 color score

## Example

> **Engagement**: STNL acquisition · cold storage facility · Atlanta MSA · seller pitched 6.0% cap on T-12 NOI of $4.2M.
>
> **Color built**:
> - EDGAR 10-K of tenant (Lineage Logistics) · investment-grade credit confirmed (Source weight: 0.90)
> - CompStak: 3 closed sales in same submarket · range 6.3%-6.8% cap (Source weight: 0.85)
> - ATTOM: property records · clear title · no recent permits (Source weight: 0.85)
> - Local broker contact: 2 phone conversations · confirmed seller has 1031 deadline in 73 days (Source weight: human-verified · 0.90)
> - SwarmCurator CRE corpus: 12 historical comps matching shape (Source weight: 0.85)
>
> **Color score**: 0.91 · Royal Jelly tier
>
> **Tribunal verdict**: HONEY · PROMOTED to Royal Jelly after validator review confirmed 5 independent sources
>
> **Deed issued**: DDEED-DOV-CRE-LINEAGE-ATL-000042-v1 · published on swarmdeed.eth · anchored on Hedera HCS topic 0.0.10291838
>
> **Outcome**: Re-priced from 6.0% to 6.4% cap on color-verified comps · seller accepted re-trade · saved buyer $2.6M on $42M asset.

## DefendableOS Notes

- Color is the ANTI-FANTASY mechanism in the PASS doctrine. If color doesn't pencil, we pass. We don't run engagements on seller's pitch alone.
- Color compounds over time within a relationship · returning customers get pre-loaded color on their domain.
- Color is what separates DefendableOS engagement quality from any AI tool that ships outputs without lineage.
- The "color file" concept maps directly to the HoneyCard `factory_path` field · same lineage discipline.

🐝 *No color · no deed. The Hive verifies before it issues.*
