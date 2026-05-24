# UI Dial Spec · Assignment Success

> *The post-close report dial. Surfaces the boolean outcome · the 5-grade breakdown · the variance vs contract. Lives on the assignment dashboard and on the Defendable Closing Statement.*

---

## Purpose

Surface the Assignment Success boolean + 5-grade breakdown to both operator and principal in a single canonical visual representation. This is the post-close report dial · NOT the in-flight prediction dial (that's Probability of Close).

This spec is the contract between the doctrine ([14_assignment_success_doctrine.md](../doctrine/14_assignment_success_doctrine.md)) · the scoring term ([assignment-success.md](../vocabulary/scoring_terms/assignment-success.md)) · and the UI implementation.

---

## Visual

### Card shape

A two-row card · 480px × 720px (desktop) · with the boolean outcome occupying the top third and the 5-grade breakdown occupying the bottom two-thirds.

### Top section · Boolean outcome

A single bold typographic statement · centered · with band-color background tint:

| Boolean | Background | Text color | Display |
|---|---|---|---|
| `CLOSED_HONEY` | `#15803D` 10% tint | `#15803D` | "CLOSED · HONEY" |
| `CLOSED_CONDITIONED` | `#CA8A04` 10% tint | `#CA8A04` | "CLOSED · CONDITIONED" |
| `FAILED_RECOVERABLE` | `#EA580C` 10% tint | `#EA580C` | "FAILED · RECOVERABLE" |
| `FAILED_DARK` | `#B91C1C` 10% tint | `#B91C1C` | "FAILED · DARK" |

Below the boolean · the composite score · serif-numeric · 36px:

```
        CLOSED · HONEY
            0.925
```

Composite shown to 3 decimals (more precision than the PoC dial · because this is the final score · not an in-flight measurement).

### Bottom section · 5-Grade breakdown

Stacked horizontal bar chart · 5 rows · each grade on its own row:

```
G1 · Outcome       (30%)  ████████████████████░░  0.93
G2 · Truth         (25%)  ███████████████████░░░  0.91
G3 · Safety        (20%)  ██████████████████████  1.00
G4 · Economics     (15%)  █████████████████░░░░░  0.88
G5 · Defensibility (10%)  ███████████████████░░░  0.95
                                         ─────────
                                Composite 0.925
```

Bar fill colors match the boolean outcome band (HONEY = green family · CONDITIONED = yellow · FAILED·R = orange · FAILED·D = red).

### Variance vs contract (collapsible)

Below the 5-grade breakdown · a collapsible section showing per-criterion variance:

```
▼ Variance vs Contract
─────────────────────────────────────────────────
Honey rate ≥ 92% on ≥ 1,200 decisions/mo
  Target: 92.0%  Actual: 94.1%  +2.3%  ✓ PASSED

Zero Propolis on adversarial pack
  Target: 0      Actual: 0      0      ✓ PASSED

Cost-to-mint ≤ $0.011/decision
  Target: $0.011 Actual: $0.005 -54%   ✓ PASSED

Validator chain critical pass ≥ 95%
  Target: 95.0%  Actual: 100%   +5%    ✓ PASSED
```

---

## Card layout (full)

```
┌─────────────────────────────────────────────────┐
│  ASSIGNMENT SUCCESS                             │
│  ASN-0001 · refund-decision · 6-mo assignment   │
│                                                 │
│  ┌───────────────────────────────────────────┐  │
│  │                                           │  │
│  │           CLOSED · HONEY                  │  │
│  │             0.925                         │  │
│  │                                           │  │
│  └───────────────────────────────────────────┘  │
│                                                 │
│  G1 · Outcome       (30%)  ████████████░  0.93  │
│  G2 · Truth         (25%)  ████████████░  0.91  │
│  G3 · Safety        (20%)  ██████████████ 1.00  │
│  G4 · Economics     (15%)  ███████████░░  0.88  │
│  G5 · Defensibility (10%)  ████████████░  0.95  │
│                              ───────────────    │
│                              Composite  0.925   │
│                                                 │
│  ▼ Variance vs Contract                         │
│  ▼ Cost-to-mint summary                         │
│  ▼ Deed inventory                               │
│  ▼ Failure deeds (0)                            │
│                                                 │
│  Closing statement: DDEED-DOV-LOGISTICS-...     │
│  Walked: 2026-09-20 · Acknowledged: 2026-09-22  │
│                                                 │
│  [View on Hedera]  [Download PDF]  [Next sub]   │
└─────────────────────────────────────────────────┘
```

---

## Data binding

### Read paths (backend → UI)

| UI element | Source field | Update cadence |
|---|---|---|
| Boolean | `closing_statement.boolean_outcome` | On close · immutable thereafter |
| Composite | `closing_statement.composite_score` | On close · immutable |
| G1-G5 | `closing_statement.g{1-5}_*` | On close · immutable |
| Variance rows | `closing_statement.criteria_variance` | On close · immutable |
| Cost summary | `closing_statement.cost_actual_per_deed_usd` · `_ceiling_*` · `_variance_pct` | On close · immutable |
| Deed inventory | `closing_statement.deed_count_*` | On close · immutable |
| Failure deeds | `closing_statement.failure_deed_ids` | On close · immutable |
| Walk + ack timestamps | `closing_statement.principal_walk_completed_at` · `_acknowledged` | After walk · ack |

### API endpoint

```
GET /api/v1/assignments/{assignment_id}/success
```

Response shape:

```json
{
  "assignment_id": "ASN-0001",
  "engagement_id": "ENG-DOV-LOGISTICS-ACME-0001",
  "closing_statement_deed_id": "DDEED-DOV-LOGISTICS-ACME-CLOSE-0001-v1",
  "boolean_outcome": "CLOSED_HONEY",
  "composite": 0.925,
  "grades": {
    "g1_outcome": {"value": 0.93, "weight": 0.30},
    "g2_truth": {"value": 0.91, "weight": 0.25},
    "g3_safety": {"value": 1.00, "weight": 0.20},
    "g4_economics": {"value": 0.88, "weight": 0.15},
    "g5_defensibility": {"value": 0.95, "weight": 0.10}
  },
  "g3_floor_violated": false,
  "critical_propolis_flag": false,
  "variance_vs_contract": [
    {"criterion": "Honey rate ≥ 92%", "target": "92.0%", "actual": "94.1%", "variance": "+2.3%", "passed": true},
    {"criterion": "Zero Propolis on adversarial", "target": "0", "actual": "0", "variance": "0", "passed": true},
    {"criterion": "Cost-to-mint ≤ $0.011/decision", "target": "$0.011", "actual": "$0.0051", "variance": "-54%", "passed": true},
    {"criterion": "Validator chain critical ≥ 95%", "target": "95%", "actual": "100%", "variance": "+5%", "passed": true}
  ],
  "deed_inventory": {
    "honey": 7832, "jelly": 489, "propolis": 0, "total": 8321
  },
  "cost_summary": {
    "actual_per_deed_usd": 0.0051,
    "ceiling_per_deed_usd": 0.0416,
    "variance_to_ceiling_pct": -87.7,
    "monthly_actual_usd": 42180,
    "monthly_invoiced_usd": 52800
  },
  "failure_deeds": [],
  "walk_completed_at": "2026-09-20T16:30:00Z",
  "acknowledged_at": "2026-09-22T11:14:00Z",
  "hedera_anchor": {
    "topic": "0.0.10291838",
    "sequence": 8401890,
    "consensus_timestamp": "2026-09-18T02:48:11.482101Z"
  },
  "next_step_recommendation": "UPGRADE_TIER"
}
```

Caching: Forever (immutable after close · safe for permanent CDN caching).

---

## Interaction

### Click behaviors

| Element | Action |
|---|---|
| Boolean | Show plain-English explanation modal ("CLOSED · HONEY means...") |
| Composite | Show the weight math (the formula computation) |
| G1-G5 rows | Show the grade-specific evidence (variance sources for G1 · Tribunal verdicts for G2 · etc) |
| Variance row | Show the underlying data + the verification path |
| Cost summary | Open the cost-to-mint detail card (mirrors the cost dial) |
| Deed inventory | Open deed list (sample 5 · with Hedera anchor links) |
| Failure deeds | If empty · show "0 failures · clean assignment." If non-empty · list with root-cause links |
| `View on Hedera` | Direct link to HashScan for the closing statement deed |
| `Download PDF` | Render and download PDF version (signed · timestamped) |
| `Next sub` (or "Renewal" / "Graceful Exit") | Open the next-step recommendation flow |

### Hover behaviors

- Hover G3 row: emphasize the floor-rule (G3 < 0.70 caps boolean at FAILED)
- Hover variance row · `PASSED`: green checkmark + confirmation source
- Hover variance row · `FAILED`: red X + remediation status
- Hover cost summary: rolling 30-day chart

---

## States

### Closed state (default)

The card as shown above · all data populated · immutable.

### Provisional state

Between assignment completion and closing-statement publication (typically 5 business days):

- Boolean shows "PENDING · CLOSING"
- Composite shows `--`
- Grades show provisional values with `[provisional]` tag
- Banner: "Closing statement in preparation · expected by {date}"
- No download / Hedera / next-step buttons yet

### Failed-walk state

If the closing statement was issued but no principal walk was completed within 14 days:

- Standard card · BUT
- Banner above: "Walk pending · scheduled {date}" OR "Walk overdue · sr broker notified"
- Acknowledged-at field shows `--` · the lack of ack is visible

### Disputed state

If the principal flags a dispute on the closing statement (rare · process documented in LOU §9.2):

- Standard card · BUT
- Banner: "Dispute in review · sr broker walking with principal · founder cc"
- Banner color: orange (escalation tone)
- All Hedera anchors still visible (the dispute doesn't unanchor the deed)

---

## Boolean determination rules

```
def boolean_outcome(grades, critical_propolis):
    if critical_propolis:
        return "FAILED_DARK"
    if grades.g3 < 0.70:
        return "FAILED_DARK"   # safety floor
    composite = (
        0.30 * grades.g1 +
        0.25 * grades.g2 +
        0.20 * grades.g3 +
        0.15 * grades.g4 +
        0.10 * grades.g5
    )
    if composite < 0.50:
        return "FAILED_DARK"
    if composite < 0.70:
        return "FAILED_RECOVERABLE"
    if composite < 0.85 or any(g < 0.70 for g in grades):
        return "CLOSED_CONDITIONED"
    return "CLOSED_HONEY"
```

The rule layer is the rule layer. The UI does NOT independently compute the boolean · it reads the value from the closing statement deed · which was set by the rule layer at close.

---

## Accessibility

- Boolean readable by screen reader as full text + status
- Grade bars include numeric + percentage readouts
- Variance section uses semantic table markup
- Color (band-tint backgrounds) is REDUNDANT signal · text + value are primary
- All Hedera anchor URLs are full-text · screen-reader-readable

---

## Operator-only extensions

For operator views (sr broker · founder · QA validator):

- Additional `[QA validator audit notes]` panel (visible to ops · NOT to principal)
- Additional `[Override boolean]` button (founder-only · audit-logged · requires written rationale)
- Additional `[Re-derive composite]` button (sr broker · audit-logged · forces re-computation if data was added late)
- Additional cross-engagement comparison (this assignment's grades vs avg across similar assignments)

---

## Tribunal-integration notes

- All grade values are computed by the Tribunal at close
- The closing-statement deed carries the Tribunal version + judge versions in its Proof of Origin
- The G3 floor rule is enforced at the rule layer · NOT at the UI · UI just reads the boolean
- Sampled cohort for G2 (Truth) is documented in the deed's Proof of Process field · auditable

---

## Cross-references

- [Assignment Success Doctrine](../doctrine/14_assignment_success_doctrine.md) · the rules behind the boolean
- [Assignment Success (scoring term)](../vocabulary/scoring_terms/assignment-success.md) · schema and scoring impact
- [Closing Statement term](../vocabulary/client_terms/closing-statement.md) · the artifact this dial surfaces
- [Sample Closing Statement example](../examples/sample_letter_of_understanding.md) · related closing artifact
- [Sample Deal Digest example](../examples/sample_deal_digest.md) · how the dial gets walked
- [Probability of Close UI Dial](probability_of_close.md) · the pre-close prediction this calibrates against
- [Cost-to-Mint UI Dial](cost_to_mint.md) · the G4 input dial

🐝 *The dial reports the truth · the truth lives in the deed · the deed survives the relationship.*
