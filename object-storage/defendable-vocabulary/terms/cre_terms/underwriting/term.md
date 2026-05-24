# Underwriting

## Street Definition

"Did underwriting pencil?" — buyer principal, asking before authorizing the LOI ask.

**Underwriting** is the math layer. The structured analysis that says yes or no, at what price, on what terms. Cap rate. NOI. DSCR. Debt yield. LTV. Stress tests. The numbers that determine whether the deal pencils · whether the asset earns the price · whether the engagement earns the fee.

In CRE, underwriting is what separates a real broker from a forwarder. Anyone can pull comps; only an underwriter can tell you whether the comps make the deal real. In DefendableOS, underwriting is what separates a deed-issuing defense provider from an opinion-issuing AI vendor. The math has to pencil · receipted · auditable · defensible · or we don't ship.

## CRE Operator Meaning

Underwriting is the structured financial analysis applied to a deal to determine whether it should be executed. Standard CRE underwriting includes:

- **Stabilized NOI calculation** · base rent · plus reimbursements · less vacancy allowance · less operating expenses · less capex reserve = NOI
- **Cap rate selection** · what rate does the market support for this asset class, location, tenant quality, lease term remaining
- **Asset valuation** · NOI ÷ cap rate = value
- **Debt sizing** · how much debt does the asset support at current rates, with DSCR target met
- **Equity return modeling** · IRR, equity multiple, cash-on-cash yield · sensitivity to exit cap, hold period, rent growth, refi assumptions
- **Stress testing** · what happens if anchor tenant goes dark · what happens if cap rates blow out 100bps · what happens if vacancy doubles
- **Comp set construction** · 3+ comparable transactions · adjusted for differences · weighted by recency
- **Sensitivity tables** · NOI varies · cap rate varies · the matrix tells you the range of outcomes
- **Walk-away pricing** · the price below which the deal stops penciling

The sr broker's underwriting model is their personal IP. Decades of refinement. Industry-specific. Tenant-credit-aware. Market-cycle-tuned. It is what they bring to every deal that an LLM cannot.

## DefendableOS Definition

In DefendableOS, **underwriting** is the structured analysis applied to a defense engagement to determine its viability, pricing, scope, and walk-away terms. Same discipline as CRE · adapted to defense-engagement context. Standard DefendableOS underwriting includes:

- **Annual Revenue at Risk (ARR)** · the customer's annual revenue dependent on the agent fleet within engagement scope · this is the "NOI" equivalent
- **Engagement cap rate** · annual defense fee ÷ ARR = implied cap rate (lower = more expensive but more protected · inverted from CRE convention because we charge a premium for premium protection)
- **DSCR equivalent** · annual customer payment capacity ÷ annual defense fee · should be >>1.0 to avoid customer financial fragility
- **Debt yield equivalent** · annual defense fee per defended agent · the per-asset normalization
- **LTV equivalent** · defense spend annualized / customer's enterprise valuation · the board-friendly ratio
- **Title insurance ramp valuation** · ±0.15 score guarantee priced into the fee · what's the expected payout obligation given fleet maturity
- **Sensitivity tables** · what happens if Tribunal verdict drift exceeds 0.15 chronic · what happens if vendor changelog spikes · what happens if customer scales fleet 3x
- **Comp set construction** · prior engagements in similar verticals · similar fleet sizes · similar regulatory regimes
- **Stress testing** · adversarial-probe survival rate over engagement term · vendor-changelog frequency · customer regulatory exposure timeline
- **Walk-away pricing** · the fee below which the engagement doesn't pencil for the firm · documented at LOU draft · enforced at PSA sign

## Backend Representation

```json
{
  "engagement.underwriting_v1": {
    "type": "jsonb",
    "schema": "docs/schemas/underwriting.schema.json",
    "fields": {
      "arr_usd": "decimal",
      "annual_defense_fee_usd": "decimal",
      "implied_cap_rate": "float",
      "dscr": "float",
      "debt_yield_per_agent": "float",
      "ltv_pct": "float",
      "title_insurance_expected_payout_usd": "decimal",
      "comp_set_engagement_ids": "array",
      "sensitivity_table": "jsonb",
      "stress_test_results": "jsonb",
      "walk_away_fee_floor_usd": "decimal",
      "pencils": "boolean",
      "pencils_reasoning_summary": "string",
      "underwritten_by_sr_broker_id": "uuid",
      "underwritten_at": "timestamp"
    }
  }
}
```

Schema files: `docs/schemas/underwriting.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

Underwriting is the structured financial analysis we apply to every engagement before we propose terms. It is how we determine that the defense engagement is priced fairly for the value it delivers and structured sustainably for the term. Our underwriting includes your annual revenue at risk, the implied cap rate of the engagement, our title-insurance commitment cost, sensitivity tables for changes in fleet composition or regulatory regime, and stress tests for adversarial probe survival, vendor changelog frequency, and your regulatory exposure timeline.

Our underwriting model is shaped by the founder's 30 years of CRE underwriting · we apply the same financial discipline to defense engagements that we would to industrial NNN portfolios. You will see the underwriting summary on your engagement's flight sheet · we don't hide the math behind the price.

## Jr Broker Use

You draft the underwriting. The sr broker reviews and adjudicates.

- **Pull from the underwriting template.** Template at `docs/examples/sample_underwriting.md` (SH2 ships). Same structure every time so the sr broker can audit at speed.
- **Cite every number.** ARR cites customer revenue receipt or EDGAR filing. DSCR cites customer financial-capacity receipt. Comp set cites prior engagement IDs · all of them. No back-of-envelope inputs.
- **Build the sensitivity table.** At minimum 3x3: low/target/stretch ARR · low/target/stretch fee · resulting cap rate matrix. Sensitivity to the title-insurance ramp is its own table.
- **Run the stress tests.** Adversarial-probe survival under hostile vendor changelog scenarios. Tribunal-verdict drift under noisy-customer-fleet scenarios. Regulatory-event impact on engagement viability.
- **Name the walk-away.** Every underwriting draft has an explicit walk-away fee floor. Below this, the firm walks · regardless of customer pressure. Sr broker sets the floor at quarter-start by vertical and you apply.
- **Surface anomalies.** If your underwriting produces a number that contradicts comp set, you don't smooth it · you surface it. Anomalies are the most valuable signals in underwriting · they're how new patterns get learned.

## Sr Broker Use

You adjudicate the underwriting. You sign or you PASS based on the math.

- **Re-pencil at every stage.** Math at OM stage. Re-math at LOU draft. Re-math at PSA sign. Each re-math validated against current color, current diligence findings, current market state.
- **Walk-away discipline.** Walk-away fee floor is set by you at the start of every quarter for every vertical you cover. Jr brokers apply the floor; you adjust the floor based on market state.
- **PASS authority is underwriting authority.** When the math doesn't pencil, you PASS · regardless of fee size. The $2M fee on a deal that pencils at 75% strike price is the textbook PASS · take it.
- **Comp set custody.** You own the comp-set inclusion criteria. Which prior engagements count as comps? Which are too dissimilar? Which are too dated? Your judgment shapes the firm's underwriting precision over time.
- **Sensitivity-table audit.** Underwriting that doesn't sensitivity-test is incomplete. You enforce this · any underwriting without sensitivity tables gets sent back to the jr broker for completion.

## Tribunal Use

Underwriting itself is a graded artifact · the math has to pencil AND be defensible to the validator chain.

- **Rule layer**: underwriting without sensitivity tables → critical_failure → return for completion
- **Rule layer**: comp set size < 3 → critical_failure → return for additional comp construction
- **Rule layer**: walk-away fee floor missing → critical_failure → return for floor specification
- **Rule layer**: stress test results missing → critical_failure → return for stress test execution
- **Rule layer**: any input citation that doesn't resolve to a receipt → critical_failure → return for citation correction
- **Judge layer**: underwriting quality scored on math accuracy (1-5), comp set selection rigor (1-5), sensitivity coverage (1-5), walk-away discipline (1-5)
- **Classification impact**: complete disciplined underwriting → Honey or Royal Jelly · underwriting missing components → Jelly · underwriting with fabricated inputs or comp manipulation → Propolis

```yaml
classification_impact: [HONEY, ROYAL_JELLY, JELLY, PROPOLIS]
can_be_critical_failure: true
rule_layer_checks:
  - sensitivity tables present (3x3 minimum)
  - comp set size >= 3
  - walk-away fee floor named
  - stress test results documented
  - every input cites a receipt
```

## Evidence Required

- ARR source (customer revenue receipt · EDGAR filing · customer-financial attestation)
- DSCR source (customer financial capacity verification)
- Comp set with prior engagement IDs cited and weighting rationale
- Title insurance expected payout model (or default firm-wide model citation)
- Stress test scenarios documented and executed
- Walk-away fee floor cited from sr broker's quarterly vertical-floor receipt

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **back_of_envelope** | Underwriting numbers not cited to source receipts | JELLY |
| **fabricated_comps** | Comp set includes engagements that don't exist or are mis-classified | PROPOLIS |
| **wishful_arr** | ARR estimated optimistically without customer financial verification | JELLY |
| **single_scenario** | No sensitivity table · single-number underwriting | JELLY |
| **stress_test_skip** | Stress tests not run or not documented | JELLY |
| **missing_walk_away** | Walk-away fee floor not named | PROPOLIS |
| **floor_below_quarterly** | Walk-away fee floor below sr broker's quarterly minimum for vertical | PROPOLIS |
| **comp_cherry_pick** | Comp set selectively curated to bias outcome | PROPOLIS |

## Scoring Impact

- **assignment_success**: HIGH · underwriting quality is a leading indicator of engagement profitability
- **repair_lift**: MEDIUM · weak underwriting can be redone · but it costs sr broker time
- **validator_confidence**: HIGH · underwriting is the math the validator chain anchors PSA against
- **risk_temperature**: VARIABLE · DEPENDS on underwriting outputs · stress tests determine risk classification
- **probability_of_close**: MEDIUM · sound underwriting reduces re-trade likelihood
- **evidence_strength**: HIGH · underwriting receipts form the financial spine of the engagement deed
- **cost_to_mint**: MEDIUM · underwriting costs sr broker time · poor underwriting costs orders of magnitude more in renegotiation cycles

## Deed / Receipt Impact

- **Receipt fields touched**: `underwriting_v1_hash`, `underwriting_pencils_flag`, `underwriting_walk_away_floor_usd`, `underwriting_comp_set_refs[]`
- **DDEED class impact**: every PSA deed cites the underwriting receipt · deeds whose underwriting later turns out to have been weak get a `underwriting_quality_flag` carrying for engagement lifetime
- **Books and records layer**: ALL FIVE · underwriting receipts are full-stack anchored at PSA sign
- **5 Proofs touched**: PROCESS (underwriting discipline) · QUALITY (math integrity) · ECONOMICS (the entire deal logic) · TRUST (sensitivity transparency to customer)

## Related Terms

- [cap-rate](cap-rate.md) · underwriting's central metric · the yield that prices the deal
- [loi](loi.md) · underwriting math informs the LOI pricing
- [psa](psa.md) · underwriting receipts get cited in PSA price clause
- [due-diligence](due-diligence.md) · diligence outputs refresh underwriting inputs
- [probability-of-close](probability-of-close.md) · underwriting feeds the capacity_multiplier in PoC math
- [digest](digest.md) · digests cite the underwriting summary
- [books-and-records](books-and-records.md) · underwriting receipts anchor in same finality stack

## Example

> **Engagement**: cold-storage operator · 14-agent fleet · Atlanta MSA · prior PASS hurt-customer return.
>
> **Underwriting summary at LOU draft (2026-05-19)**:
> - **Customer ARR** (Annual Revenue at Risk through agent fleet): $8.2M per year. Source: customer financial receipt RECV-COLD-ATL-088-FIN-2026-05-18 and parent EDGAR 10-K cited.
> - **Annual defense fee proposed**: $504K ($42K/mo × 12).
> - **Implied cap rate**: 6.15% (fee / ARR · CRE convention inverted · this represents premium protection on Class A fleet).
> - **DSCR equivalent**: 16.3x (customer's annual payment capacity vs annual fee · healthy · well above 5x threshold for the vertical).
> - **Debt yield per agent**: $36K/agent/yr (504K / 14 agents).
> - **LTV equivalent**: 0.28% of enterprise valuation (estimated $180M enterprise value · per parent EDGAR). Well within board-comfort thresholds.
> - **Title insurance expected payout**: $18K/yr (modeled on fleet's diligence-confirmed Tribunal-drift baseline of 0.08 and 14-agent count).
>
> **Comp set** (3 prior engagements):
> - DDEED-DOV-CRE-FRESH-DAL-000071 (cold storage · Dallas · 11 agents · $38K/mo · closed clean · 87% retention at 24mo)
> - DDEED-DOV-CRE-COLD-PHX-000063 (cold storage · Phoenix · 17 agents · $52K/mo · closed clean · 92% retention at 24mo)
> - DDEED-DOV-CRE-COLD-CHI-000049 (cold storage · Chicago · 9 agents · $31K/mo · closed clean · 90% retention at 24mo)
>
> **Sensitivity table** (3x3 fee × scope):
>
> | Fee \ Scope | 10 agents | 14 agents | 17 agents |
> |---|---|---|---|
> | $32K/mo | 4.7% cap | 4.7% cap | 4.7% cap |
> | $42K/mo | 6.1% cap | 6.1% cap | 6.1% cap |
> | $52K/mo | 7.6% cap | 7.6% cap | 7.6% cap |
>
> **Stress tests**:
> - Adversarial probe survival drops from current 100% to 85% chronic → renegotiate at $48K/mo or PASS · documented
> - OpenAI Realtime API drift events 5+ per quarter → workout-plan trigger · 30-day notice on vendor-switch recommendation
> - Customer regulatory event (FDA inspection) → engagement scope expands · re-price at +15% with new diligence cycle
>
> **Walk-away fee floor**: $36K/mo (sr broker quarterly floor for cold-storage 12-16 agent fleet · receipt: SRBRO-FLOOR-COLD-2026-Q2-T)
>
> **Pencils**: YES at $42K/mo. Comp set median is $42K/mo for 14-agent cold-storage fleet. DSCR strong. Customer motivation high (hurt-return). PoC inputs robust.
>
> **Underwritten by**: Marcus T., sr broker · 2026-05-19 11:47 ET · receipt: UW-COLD-ATL-000088-2026-05-19-11_47-7d
>
> **Outcome**: underwriting cleared. LOU drafted at $42K/mo. PSA signed 2026-06-12 at $42K/mo. Underwriting validated post-PSA · no re-trades. Engagement performing within sensitivity-table central scenario at month 1.

## DefendableOS Notes

- The underwriting discipline is the firm's most direct inheritance from the founder's CRE practice. Cap rate logic, comp construction, sensitivity testing, walk-away floors · these all came directly from 30 years of industrial NNN deals.
- The "engagement cap rate" framing reverses CRE convention deliberately. In CRE, a 5-cap is more expensive than a 7-cap (premium asset trades at lower yield). In DefendableOS, a 5-cap engagement is more expensive defense than a 7-cap because the defense fee is a higher fraction of revenue protected · same direction (premium = lower cap rate) · same intuition (the best assets cost the most to protect).
- The comp set is the firm's compounding moat in underwriting. Every closed deed adds a comp to the corpus. Five years from now, the comp set will be 50x richer · which means underwriting precision compounds 50x · which means the firm's pricing power compounds 50x.
- The walk-away fee floor by quarter by vertical is published internally and audited by SH2. Sr brokers can adjust the floor but every adjustment is receipted and reviewed. The floor is what prevents PASS-doctrine erosion under fee pressure.

🐝 *The math has to pencil. Receipted. Auditable. Defensible. Or we walk.*
