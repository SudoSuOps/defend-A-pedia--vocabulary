# Cap Rate

## Street Definition

"What's the cap on it?" — buyer, in the first 30 seconds of any CRE conversation.

The **capitalization rate** · cap rate · is the yield metric that prices every CRE asset. Income produced ÷ asset price = cap rate. A 5-cap means the asset returns 5% of its price in annual income. Lower cap = more expensive asset. Higher cap = cheaper asset (or more risk). It is the single number that lets every broker, owner, and investor pencil a deal in seconds.

In CRE, cap rate is the language of asset pricing · the way wines have vintages and stocks have P/E ratios. In DefendableOS, cap rate is the language of engagement pricing · the way we communicate the economic structure of defense engagements to CFOs, boards, and auditors who already speak cap rate fluently.

## CRE Operator Meaning

Cap rate is the most-used metric in CRE. Definition:

```
Cap Rate = NOI / Asset Value
```

Or equivalently:

```
Asset Value = NOI / Cap Rate
```

A $1M NOI building at a 6-cap is worth $1M / 0.06 = $16.67M. At a 5-cap, the same NOI is worth $20M. At a 7-cap, the same NOI is worth $14.29M. Cap rate compression (lower cap rates) means asset values rise · cap rate expansion means asset values fall · holding NOI constant.

Cap rates encode multiple things in a single number:

- **Asset class** · industrial trades tighter than retail, retail tighter than office, etc.
- **Location quality** · Class A urban core trades 100-300bps tighter than Class B suburban
- **Tenant credit** · investment-grade tenant trades 50-150bps tighter than non-credit
- **Lease term remaining** · long WALT (weighted average lease term) trades tighter than short
- **Building age and physical condition** · trophy assets trade tighter than vintage
- **Market state** · cap rates compress in low-rate environments, expand in high-rate
- **Capital availability** · abundant debt compresses caps; tight debt expands

Sr brokers carry mental cap rate matrices · they can quote a fair cap for any asset type in any market within 25bps without looking it up. That instinct is the personal IP.

## DefendableOS Definition

In DefendableOS, **cap rate** is the engagement-level yield metric · the structural way we communicate the economic shape of a defense engagement. Definition (inverted from CRE convention because we're pricing protection · not asset):

```
Engagement Cap Rate = Annual Defense Fee / Annual Revenue at Risk (ARR)
```

A $500K annual defense fee on $10M of ARR is a 5-cap engagement (5%). A $500K fee on $7M of ARR is a 7.1-cap engagement. Lower engagement cap rates mean the defense is a smaller share of protected revenue (cheaper protection · or smaller exposure). Higher cap rates mean defense is a larger share (more expensive protection · or larger exposure relative to ability to pay).

Cap rate in DefendableOS encodes:

- **Fleet class** · Royal Jelly tier engagements trade tighter (lower cap) than Honey tier
- **Vertical** · medical and finance trade tighter than generic SMB defense
- **Vendor concentration** · single-vendor fleets trade tighter (less complexity) than multi-vendor
- **Customer credit** · investment-grade customers trade tighter than emerging-stage
- **Regulatory exposure** · regulated verticals trade tighter (defense is more valuable per dollar)
- **Engagement term remaining** · long-term engagements price tighter than short
- **Market state** · AI-incident-driven demand compresses caps · low-demand periods expand them
- **Title insurance ramp commitment** · ±0.15 guarantee tightens cap (we're charging for the guarantee)

A sr broker quotes engagement cap rates the way a CRE broker quotes asset cap rates · same instinct, adapted vocabulary, same compounding personal IP.

## Backend Representation

```json
{
  "engagement.cap_rate_implied": {
    "type": "float",
    "range": [0.01, 0.50],
    "description": "Annual defense fee / Annual revenue at risk",
    "scoring_hook": "engagement_pricing_v1"
  },
  "engagement.cap_rate_comp_set_median": {
    "type": "float",
    "description": "Median cap rate of 3+ comparable engagements"
  },
  "engagement.cap_rate_variance_vs_comp": {
    "type": "float",
    "description": "Spread between this engagement's cap and comp median"
  },
  "engagement.cap_rate_drivers": {
    "type": "jsonb",
    "description": "Named factors compressing or expanding the cap"
  }
}
```

Schema files: `docs/schemas/cap_rate.schema.json` · `docs/schemas/engagement.schema.json` · `docs/schemas/underwriting.schema.json`

## Client Explanation

Cap rate is a CRE term we use to communicate the economic shape of a defense engagement to your CFO and your board. The engagement cap rate is the annual defense fee divided by your annual revenue at risk through the agent fleet we're defending. A 5-cap engagement means our annual fee is 5% of the revenue we're protecting; a 7-cap engagement means our fee is 7% of revenue protected.

We use cap rate because your finance team already thinks in cap rate terms · it lets your CFO understand DefendableOS pricing the same way they understand commercial real estate, infrastructure assets, or insurance products. The lower the cap rate, the lower-priced the defense relative to what it protects · which typically means we're more confident in the fleet's grade or you have less revenue at risk. Higher cap rates reflect more complex fleets, larger exposure, or premium engagements with elevated title-insurance commitments.

## Jr Broker Use

You compute cap rate at every underwriting cycle. The discipline:

- **Always present cap rate in the flight sheet.** Cap rate is the single most-readable number for a CFO · it should be on every flight sheet · ahead of the dollar fee even.
- **Cite the inputs.** ARR cites customer financial receipt. Fee cites the pricing-scenario the engagement is being offered at.
- **Compare to comp set.** Every cap rate quoted is compared to the comp set median for similar vertical / fleet size / term. Variance > 100bps from comp median requires explanation in flight sheet · either you have a strong reason (premium-tier engagement, hurt-customer-return premium, regulatory-density compression) or you should re-pencil.
- **Use cap rate in negotiation.** When customer pushes back on dollar fee, reframe as cap rate vs comp set median. "Our proposed 6.1% engagement cap rate is at the comp median for cold-storage 14-agent fleets · the $42K/mo number is exactly what your peer set is paying for comparable defense."
- **Track cap rate trajectory by vertical.** Where are caps compressing? Where expanding? You bring these observations to the weekly pipeline review · sr broker uses them to inform quarterly walk-away floor adjustments.

## Sr Broker Use

You hold the firm's cap rate matrix. Same way a CRE sr broker holds the cap matrix for industrial NNN in their market · published or unpublished personal IP.

- **Quarterly cap rate matrix update.** Every quarter, you refresh the cap rate matrix by vertical, fleet size, engagement term, customer credit class. The matrix becomes the underwriting baseline jr brokers apply.
- **Walk-away floor by cap.** Walk-away fee floor for a given engagement is the lowest fee that still hits the floor cap rate for the engagement's vertical and tier. Below this, you PASS · regardless of customer pressure.
- **Cap rate as the negotiation anchor.** When customer counsel pushes back at PSA stage, you reframe in cap rate. "Your engagement at 6.1% engagement cap rate is consistent with your peer set in cold-storage at 5.8-6.5%. We are not over-pricing · we are at market."
- **Cap rate trajectory as strategic indicator.** Cap compression in a vertical means demand is strong · capacity to expand listings · capacity to invest in the vertical. Cap expansion means demand is softening · time to re-segment or reduce vertical investment.

## Tribunal Use

Cap rate is Tribunal-checked as part of underwriting · the calculation must be defensible.

- **Rule layer**: cap rate value outside [0.01, 0.50] bound → critical_failure → math anomaly
- **Rule layer**: cap rate calculated without comp set comparison → critical_failure → return for comp comparison
- **Rule layer**: variance from comp median > 150bps without named explanation → critical_failure → return for justification
- **Rule layer**: cap rate below sr broker's quarterly walk-away floor for vertical → critical_failure → cannot proceed
- **Judge layer**: cap rate selection quality scored on comp construction (1-5), driver identification (1-5), market-state awareness (1-5)
- **Classification impact**: defensible cap rates → Honey · cap rates with weak comp justification → Jelly · cap rates set below walk-away floor or with fabricated comps → Propolis

```yaml
classification_impact: [HONEY, ROYAL_JELLY, JELLY, PROPOLIS]
can_be_critical_failure: true
rule_layer_checks:
  - cap rate in [0.01, 0.50] bound
  - comp set size >= 3
  - cap rate variance from comp median documented if > 100bps
  - cap rate at or above sr broker's quarterly walk-away floor
```

## Evidence Required

- ARR source (customer revenue receipt · EDGAR filing · attestation)
- Comp set with 3+ prior engagement deeds cited
- Comp set vertical-similarity scoring
- Sr broker's quarterly walk-away floor receipt referenced
- Drivers compressing or expanding the cap rate documented

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **cap_below_floor** | Cap rate set below sr broker quarterly walk-away floor | PROPOLIS |
| **fabricated_comps** | Comp set includes deeds that don't match vertical/size criteria | PROPOLIS |
| **unjustified_variance** | Cap > 100bps from comp median with no named driver | JELLY |
| **stale_comp_set** | Comp set deeds > 18 months old without market adjustment | JELLY |
| **wishful_arr** | ARR inflated to justify higher fee at apparent same cap rate | PROPOLIS |
| **single_scenario_cap** | Cap quoted without sensitivity to ARR / fee variation | JELLY |
| **missing_driver_documentation** | Cap quoted without naming what compresses or expands it | JELLY |

## Scoring Impact

- **assignment_success**: MEDIUM · cap rate discipline is necessary but not sufficient for engagement success
- **repair_lift**: MEDIUM · mis-priced engagements can be re-priced at renewal · but the customer relationship takes a hit
- **validator_confidence**: HIGH · cap rate is part of the validator chain's PSA-readiness check
- **risk_temperature**: VARIABLE · cap rate too tight = under-priced risk · cap rate too loose = over-priced (loses deal)
- **probability_of_close**: MEDIUM · in-range cap rates raise close probability · out-of-range cap rates trigger re-trades
- **evidence_strength**: HIGH · cap rate is the most-cited engagement-pricing metric
- **cost_to_mint**: LOW · cap rate calculation is templated · poor cap rate discipline costs in retention drag

## Deed / Receipt Impact

- **Receipt fields touched**: `cap_rate_implied`, `cap_rate_comp_set_median`, `cap_rate_variance_vs_comp`, `cap_rate_drivers`
- **DDEED class impact**: every engagement deed cites the cap rate at PSA sign · deeds at cap rates significantly off-comp carry a `pricing_quality_flag` for retrospective review
- **Books and records layer**: ALL FIVE · cap rate computation is part of the PSA-anchor batch
- **5 Proofs touched**: ECONOMICS (the deal logic) · PROCESS (underwriting discipline) · QUALITY (comp set integrity) · TRUST (open math to customer's CFO)

## Related Terms

- [underwriting](underwriting.md) · cap rate is underwriting's headline metric
- [loi](loi.md) · LOU pricing usually quoted in cap rate
- [psa](psa.md) · PSA pricing clause cites cap rate
- [digest](digest.md) · digests include cap rate for any active negotiation
- [probability-of-close](probability-of-close.md) · cap rate vs comp median feeds capacity_multiplier and pattern_match_multiplier
- [due-diligence](due-diligence.md) · diligence updates may shift ARR · which moves cap rate
- [books-and-records](books-and-records.md) · cap rate history anchored alongside engagement deeds

## Example

> **Engagement**: cold-storage operator · 14-agent fleet · Atlanta MSA · LOU pricing $42K/mo (annual $504K) · customer ARR $8.2M.
>
> **Engagement cap rate computed**:
> - $504K / $8.2M = 6.15%
> - Rounded for communication: 6.1-cap
>
> **Comp set** (cold-storage · 11-17 agent fleets · last 18 months):
> - DDEED-DOV-CRE-FRESH-DAL-000071 · $38K/mo · $7.1M ARR · 6.4% cap
> - DDEED-DOV-CRE-COLD-PHX-000063 · $52K/mo · $9.8M ARR · 6.4% cap
> - DDEED-DOV-CRE-COLD-CHI-000049 · $31K/mo · $6.3M ARR · 5.9% cap
>
> **Comp median cap**: 6.4%
> **This engagement cap**: 6.1%
> **Variance**: -30bps (this engagement is slightly tighter than comp median · 30bps less expensive in cap terms)
>
> **Drivers compressing the cap**:
> - Hurt-customer-return engagement · customer motivation high · firm willing to price competitive to lock relationship
> - Color score 0.91 (top decile) · firm confident in fleet integrity · less risk premium needed
> - Validator first pass clean on 13/14 agents · low workout-plan overhead expected
>
> **Drivers expanding the cap** (none material): 1 agent advisory finding (agent-09 logging-tooling) included in workout-plan scope · already priced in.
>
> **Sr broker walk-away floor for cold-storage 12-16 agent fleet 2026-Q2**: 5.2% cap (corresponds to $36K/mo at $8.2M ARR). This engagement at 6.1% is comfortably above floor.
>
> **Communication on flight sheet**: "Engagement priced at a 6.1% cap rate on $8.2M annual revenue at risk · which is 30bps tighter than the comp median of 6.4% for cold-storage operators of similar size · reflecting strong color, clean validator status, and our confidence in the fleet's grade."
>
> **Outcome**: customer's CFO immediately understood the framing. No fee pushback. PSA signed at proposed terms. Cap rate cited in PSA receipt: `PSA-COLD-ATL-000088-2026-06-12-16_00-7a2f.cap_rate_implied = 0.0615`.

## DefendableOS Notes

- Cap rate is the founder's most direct vocabulary inheritance from CRE into DefendableOS. The same number that priced $8B in industrial NNN now prices defense engagements · same intuition, same discipline, same comp-set rigor.
- The cap rate matrix is the firm's compounding pricing IP. Every closed deed adds data points · every quarter the matrix gets sharper · every year the matrix becomes more valuable. Competitors without 30 years of CRE pricing discipline cannot reproduce it.
- The inversion from CRE convention (lower-cap = more expensive in CRE → lower-cap = cheaper engagement in DefendableOS) trips up new operators initially. Worth a single training session to lock the mental model. Once locked, the language flows.
- Cap rate language is what separates DefendableOS conversations with CFOs from typical AI-vendor conversations. CFOs hear "AI defense" and discount it · they hear "6.1-cap engagement priced 30bps tighter than your peer set" and they engage substantively. Vocabulary is access.

🐝 *Cap rate prices the deal. The comp set is the moat. The discipline is the brand.*
