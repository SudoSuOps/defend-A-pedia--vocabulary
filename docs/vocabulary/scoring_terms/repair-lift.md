# Repair Lift (UI Dial)

> **Cross-link**: this term is the SCORING DIAL version of the underlying repair concept. The CONCEPT term lives at [`../repair_terms/repair-lift.md`](../repair_terms/repair-lift.md). Same number · different surface · this file documents the UI dial spec.

## Street Definition

"What did the lift dial show this week?" That's how the customer reads their Monday dashboard. **Repair Lift dial** is the UI surface for the Repair Lift number · the gauge that shows the customer the before/after delta on their refinery work. Green when ≥ 0.10 · yellow 0.0-0.10 · red below 0.0. Glance-readable. Boardroom-ready.

## CRE Operator Meaning

In CRE this is the **NOI lift graph** on the asset's monthly statement. The graph shows trailing-12-month NOI · the rehab investment · the post-rehab NOI · the lift in basis-points. The CFO reads it · the lender reviews it · the equity partners stay informed. Nobody re-derives the number from the rent roll · they trust the graph because the graph is downstream of a closing statement they signed. The Repair Lift dial is the NOI lift graph for the agent economy.

## DefendableOS Definition

The Repair Lift dial is the UI surface representation of the Repair Lift score. It renders the lift number with three visual states: GREEN (≥ 0.10 · cleared promotion threshold), YELLOW (0.0-0.10 · positive but below threshold), RED (< 0.0 · regression). It appears on the customer-facing dashboard (per-week aggregate), the operator's Morning Reconciliation Brief (per-day aggregate), and the per-pair detail view (single-pair lift). The dial is rendered from the canonical `repair_lift.value` field · no UI-side computation.

## Backend Representation

```json
{
  "repair_lift_dial.source_field": {"type": "string", "const": "repair_lift.value"},
  "repair_lift_dial.thresholds": {
    "type": "object",
    "const": {
      "green_min": 0.10,
      "yellow_min": 0.00,
      "red_max": 0.00
    }
  },
  "repair_lift_dial.display_modes": {
    "type": "array",
    "const": ["per_pair", "daily_aggregate", "weekly_aggregate", "trailing_30d_aggregate"]
  },
  "repair_lift_dial.color_state": {
    "type": "enum",
    "values": ["GREEN", "YELLOW", "RED"]
  },
  "repair_lift_dial.tooltip_evidence_link": {"type": "string", "description": "URL to underlying Repair Lift receipt"},
  "repair_lift_dial.refresh_interval_seconds": {"type": "integer", "default": 300}
}
```

Schema files: `docs/schemas/ui_dial.schema.json` · `docs/schemas/repair_lift_dial.schema.json`

## Client Explanation

The Repair Lift dial on your dashboard shows whether our refinery is moving the number on your AI fleet. Green means we hit the promotion threshold (≥ 0.10 lift). Yellow means we're positive but below threshold · we're working on it. Red means a regression · the operator gets paged when red shows up. Click the dial · you see the underlying receipt with both Tribunal verdicts · the math is transparent.

## Jr Broker Use

The Jr Hack reads the dial in the Morning Brief · the dial color is the morning's first decision tree. Green dial = continue normal cycle. Yellow dial = check whether refinery had off-batch · investigate. Red dial = page the Sr Hack · do not proceed with day-routine until the regression is triaged.

## Sr Broker Use

The Sr Hack watches the dial trend · not the spot value. A spot green can hide a 4-week trend toward yellow. The Sr Hack sets dashboard alerts on TREND drift (delta of weekly aggregate vs prior 4-week mean > 0.05) · NOT just on absolute thresholds. A trending dial is information · a static-color dial is noise.

## Tribunal Use

- **Rule layer**: Dial color MUST be derived from `repair_lift.value` · no UI-side rounding, capping, or "smoothing"
- **Rule layer**: Tooltip evidence link MUST resolve to the underlying anchored receipt · broken links = dial UI is misleading
- **Judge layer**: Tribunal doesn't grade the dial · it grades the underlying score · the dial is a pure rendering
- **Classification impact**: A dial showing GREEN backed by a JELLY-classified pair is a UI bug · the dial MUST agree with the underlying classification

## Evidence Required

- Underlying `repair_lift.value` from anchored receipt
- Threshold definitions matching the locked doctrine (0.10 / 0.00)
- Tooltip URL resolving to receipt detail
- Refresh timestamp (proves the dial is current)
- Aggregation window declaration (per-pair / daily / weekly / 30d)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `ui_side_smoothing` | Dial color rendered from a smoothed/rolling average that masks regressions | JELLY · UI bug |
| `broken_evidence_link` | Tooltip link broken · customer can't drill in | JELLY · UI quality |
| `threshold_drift` | UI uses different thresholds than the doctrine (e.g., 0.05 instead of 0.10) | PROPOLIS · governance violation |
| `stale_dial` | Refresh interval breached · dial showing yesterday's data | JELLY · operational alert |
| `color_mismatch` | Dial GREEN but pair classified JELLY · UI not in sync | PROPOLIS · UI bug · auto-rollback |

## Scoring Impact

- **assignment_success**: HIGH · dial color is the customer's primary visual cue
- **repair_lift**: SELF · the dial IS the rendering of repair lift
- **validator_confidence**: HIGH · dial transparency (drill-in to receipt) IS a trust signal
- **risk_temperature**: DIRECT · red dial = high risk · green dial = low risk
- **probability_of_close**: HIGH · customers re-up against the dial trend
- **evidence_strength**: HIGH · the dial's drill-in IS the evidence
- **cost_to_mint**: NEUTRAL · dial is UI render · no per-render mint cost

## Deed / Receipt Impact

- **Receipt fields touched**: dial reads `repair_lift.value` and renders · doesn't write
- **DDEED class impact**: dial doesn't issue deeds · it surfaces them
- **Books and records layer**: dial reads L1 PostgreSQL · references L4 Hedera HCS via tooltip link
- **5 Proofs touched**: QUALITY (the lift IS the quality measurement being surfaced) · TRUST (drill-in to anchored receipt)

## Related Terms

- [repair-lift (concept)](../repair_terms/repair-lift.md) · the underlying concept this dial renders
- [validator-confidence](validator-confidence.md) · partner dial · together gate promotion
- [evidence-strength](evidence-strength.md) · partner dial
- [risk-temperature](risk-temperature.md) · partner dial
- [defendablejelly](../repair_terms/defendablejelly.md) · the product surface where the dial lives

## Example

> **Customer dashboard · week of 2026-05-17 to 2026-05-23**:
> - Repair Lift dial: GREEN · weekly aggregate +0.18
> - Tooltip: "47 Royal Jelly Records this week · mean lift +0.18 · median +0.16 · p10 +0.04 · p90 +0.31"
> - Drill-in link → `dashboard.acmecorp.defendable.eth/lift/2026-W21`
> - Refresh: 6 minutes ago
>
> **Operator Morning Brief 2026-05-24 06:00**:
> - Yesterday's daily aggregate: GREEN · +0.21 (above 7-day mean of +0.18)
> - 4 pairs lift > 0.30 · 1 pair lift < 0.05 (re-routed to pending for retry)
> - 0 regressions
>
> **Per-pair detail (pair-20260524T061208Z-7e2a)**:
> - Repair Lift dial: GREEN · spot value +0.15
> - Tooltip evidence link → anchored receipt with both Tribunal verdicts
> - Color state: GREEN (0.15 ≥ 0.10 threshold)

## DefendableOS Notes

- The dial is a DERIVED surface · the source of truth is the receipt · the dial just renders
- "No UI-side smoothing" is non-negotiable · customer trust requires the dial color matches the receipt classification
- The dial is the FIRST thing customers see when they open the dashboard · it's the load-bearing UI element
- See also the CONCEPT term at [`../repair_terms/repair-lift.md`](../repair_terms/repair-lift.md) · same number · different surface

🐝 *Green is the lift. Yellow is the work. Red is the page. The dial is the closing statement glance.*
