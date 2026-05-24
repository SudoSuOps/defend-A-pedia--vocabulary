# UI Dial Spec · Cost-to-Mint

> *The economics dial. Surfaces the per-deed cost · the rolling 7-day actual · the variance vs the contracted ceiling. The CFO's window into the meter.*

---

## Purpose

Surface cost-to-mint to both operator and principal · with the CFO-grade transparency the doctrine requires. This is the dial the CFO checks before approving the next invoice. It must re-derive on the spot · against the published formula · with the variance to ceiling clearly visible.

This spec is the contract between the doctrine ([09_energy_and_cost_to_mint.md](../doctrine/09_energy_and_cost_to_mint.md)) · the cost-to-mint vocabulary term · and the UI implementation.

---

## Visual

### Card shape

A two-section card · 480px × 640px (desktop) · with the headline numeric occupying the top third and the per-component breakdown occupying the bottom two-thirds.

### Top section · The two numbers

Two side-by-side numerics · the actual vs the ceiling · with the variance percentage between them:

```
   $0.0049              $0.0416
   ACTUAL                CEILING
                ↓
            -88.2%
            UNDER
```

Color rules:

| Variance | Color | Label |
|---|---|---|
| Variance > -50% (well under ceiling) | `#15803D` (green) | "WELL UNDER" |
| -50% to -10% (under ceiling) | `#15803D` (green) | "UNDER" |
| -10% to +10% (near ceiling) | `#CA8A04` (yellow) | "NEAR" |
| +10% to +25% (over ceiling within buffer) | `#EA580C` (orange) | "OVER · WITHIN BUFFER" |
| > +25% (over buffer) | `#B91C1C` (red) | "OVER · BUFFER BREACH" |

The +10% LOU buffer is the soft band. Beyond it · renegotiation per LOU §4.4.

### Bottom section · 7-component breakdown

Horizontal stacked bar showing the per-component composition of the actual cost:

```
$0.0049 per deed (7-day rolling)
┌────────────────────────────────────────────┐
│GPU│Trib│Val│Hed│NAS│ENS│Op │                │
└────────────────────────────────────────────┘
 40% 27%  10% 2% 2% 4% 15%

Component              Per-deed   % of total
─────────────────────────────────────────────
GPU inference          $0.00198   40.4%
Tribunal pass          $0.00131   26.7%
Validator chain        $0.00047    9.6%
Hedera HCS anchor      $0.00010    2.0%
NAS L3 archive         $0.00009    1.8%
ENS amortized          $0.00019    3.9%
Operator margin        $0.00076   15.5%
─────────────────────────────────────────────
Total                  $0.00490  100.0%
```

The component widths are proportional · the colors are distinct per component (palette below).

---

## Card layout (full)

```
┌─────────────────────────────────────────────────┐
│  COST TO MINT                                   │
│  ENG-DOV-LOGISTICS-ACME-0001 · 7-day rolling    │
│                                                 │
│  ┌───────────────────────────────────────────┐  │
│  │                                           │  │
│  │   $0.0049            $0.0416              │  │
│  │   ACTUAL             CEILING              │  │
│  │                                           │  │
│  │              ↓                            │  │
│  │          -88.2% UNDER                     │  │
│  │                                           │  │
│  └───────────────────────────────────────────┘  │
│                                                 │
│  Component Breakdown                            │
│  ─────────────────────────────────────────────  │
│  ████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│                                                 │
│  GPU inference       $0.00198   40.4%           │
│  Tribunal pass       $0.00131   26.7%           │
│  Validator chain     $0.00047    9.6%           │
│  Hedera HCS anchor   $0.00010    2.0%           │
│  NAS L3 archive      $0.00009    1.8%           │
│  ENS amortized       $0.00019    3.9%           │
│  Operator margin     $0.00076   15.5%           │
│                                                 │
│  ▼ 30-day trajectory chart                      │
│  ▼ Monthly totals (actual vs invoiced)          │
│                                                 │
│  Formula version: DDEED-DOV-ECON-Q2-2026-v1     │
│  Last computed: 2026-06-15 02:14 ET             │
│                                                 │
│  [View formula doc] [Verify on Hedera] [Export] │
└─────────────────────────────────────────────────┘
```

---

## Component color palette

| Component | Color | Hex | Tailwind |
|---|---|---|---|
| GPU inference | Blue | `#1D4ED8` | `bg-blue-700` |
| Tribunal pass | Purple | `#7E22CE` | `bg-purple-700` |
| Validator chain | Indigo | `#4338CA` | `bg-indigo-700` |
| Hedera HCS anchor | Cyan | `#0E7490` | `bg-cyan-700` |
| NAS L3 archive | Slate | `#475569` | `bg-slate-600` |
| ENS amortized | Teal | `#0F766E` | `bg-teal-700` |
| Operator margin | Emerald | `#047857` | `bg-emerald-700` |

Palette is distinct per component · NOT shades of a single hue (CFO needs to distinguish at-a-glance).

---

## Data binding

### Read paths (backend → UI)

| UI element | Source field | Update cadence |
|---|---|---|
| Actual ($/deed) | computed: 7-day rolling avg of `receipt.cost_to_mint_usd` | Hourly |
| Ceiling ($/deed) | `engagement.cost_to_mint_ceiling_per_deed_usd` (from LOU §4.2) | Immutable (LOU-bound) |
| Variance % | computed: (actual - ceiling) / ceiling × 100 | Hourly |
| Per-component values | computed: 7-day rolling avg of `receipt.cost_to_mint_breakdown.*` | Hourly |
| Monthly actual | computed: sum of `receipt.cost_to_mint_usd` for current month | Hourly |
| Monthly invoiced | from billing system · invoice runs | Per invoice cycle |
| Formula version | `engagement.cost_to_mint_formula_version` | Quarterly updates |
| Last computed | timestamp of last hourly cron | Hourly |

### API endpoint

```
GET /api/v1/engagements/{engagement_id}/dial/cost-to-mint
```

Response shape:

```json
{
  "engagement_id": "ENG-DOV-LOGISTICS-ACME-0001",
  "actual_per_deed_usd": 0.0049,
  "ceiling_per_deed_usd": 0.0416,
  "variance_to_ceiling_pct": -88.2,
  "variance_status": "WELL_UNDER",
  "rolling_window_days": 7,
  "component_breakdown": {
    "gpu_inference": {"per_deed_usd": 0.00198, "pct_of_total": 40.4, "color": "#1D4ED8"},
    "tribunal_pass": {"per_deed_usd": 0.00131, "pct_of_total": 26.7, "color": "#7E22CE"},
    "validator_chain": {"per_deed_usd": 0.00047, "pct_of_total": 9.6, "color": "#4338CA"},
    "hedera_anchor": {"per_deed_usd": 0.00010, "pct_of_total": 2.0, "color": "#0E7490"},
    "nas_archive": {"per_deed_usd": 0.00009, "pct_of_total": 1.8, "color": "#475569"},
    "ens_amortized": {"per_deed_usd": 0.00019, "pct_of_total": 3.9, "color": "#0F766E"},
    "operator_margin": {"per_deed_usd": 0.00076, "pct_of_total": 15.5, "color": "#047857"}
  },
  "monthly_summary": {
    "month": "2026-06",
    "actual_usd": 42180,
    "invoiced_usd": 52800,
    "deeds_in_month": 8610,
    "ceiling_total_if_at_ceiling_usd": 358176
  },
  "formula_version": "DDEED-DOV-ECON-Q2-2026-v1",
  "formula_doc_url": "https://defendableos.com/economics",
  "last_computed_at": "2026-06-15T02:14:00Z",
  "lou_buffer_pct": 10.0
}
```

Caching: 1-hour TTL.

---

## Interaction

### Click behaviors

| Element | Action |
|---|---|
| Actual numeric | Show 30-day trajectory in modal (line chart · with ceiling reference line) |
| Ceiling numeric | Show LOU §4.2 quote with version history of ceiling (in case it changed via amendment) |
| Variance label | Show what would trigger renegotiation (the +10% buffer rule) |
| Component row | Show that component's underlying drivers (e.g., GPU row → kWh per deed · rate × kWh math) |
| Stacked bar segment | Same as component row click |
| `▼ 30-day trajectory chart` | Expand to show 30-day line chart with ceiling overlay |
| `▼ Monthly totals` | Expand to show monthly actual vs invoiced for last 12 months |
| `View formula doc` | Open the published formula page in new tab |
| `Verify on Hedera` | Open HashScan for the formula-version deed |
| `Export` | Download CSV with the 7-day rolling component breakdown |

### Hover behaviors

- Hover actual numeric: show 4-decimal value + the exact 7-day deed count
- Hover ceiling: show the multiplier (T3 = 8x cost-to-mint baseline)
- Hover variance: show "buffer remaining" or "buffer consumed"
- Hover formula version: show formula effective date + the quarterly schedule

---

## States

### Default state

The card as shown · current 7-day rolling data · all components visible.

### Buffer breach state

When variance > +10% (LOU §4.2 buffer breached):

- Variance label color flips to red
- Banner above: "Buffer breach detected · renegotiation discussion required per LOU §4.4 · sr broker notified {timestamp}"
- "Renegotiation status" panel auto-expanded showing the discussion thread

### Formula change state

Within 7 days of a quarterly formula update:

- Banner above: "New formula deployed · {old version} → {new version} · effective {date} · {delta summary}"
- Banner links to the delta-explanation deed
- Both old + new comparisons shown side by side

### No-data state

For engagement with < 14 days of deeds:

- Card visible but with "Insufficient data · stabilizes after 14 days" overlay
- Component breakdown shows skeleton
- No variance percentage (not enough data to compute reliably)

---

## CFO-mode (operator extension)

When viewed by a CFO-tagged principal contact OR an operator:

Additional UI elements visible:

- **Re-derive button** · runs the formula re-derivation in-place · shows the computation tree · audit-logged
- **Compare to baseline** · shows variance against the published baseline ($0.0052) for this customer's deed class
- **YTD totals** · year-to-date actual + invoiced + deeds
- **Forecast** · projected month-end totals based on month-to-date run-rate

CFO-mode is enabled per-principal in LOU §11.1 (`cfo_mode_enabled: boolean`). Default: enabled for principals tagged as Financial Authority.

---

## Trajectory chart specifics

When the user expands the 30-day trajectory:

- X-axis: days · 30 calendar days · daily aggregates
- Y-axis: $/deed (linear scale · 0 to max(ceiling, max_actual+10%))
- Line 1 (solid): actual per-deed cost · 7-day rolling avg
- Line 2 (dashed): ceiling (constant horizontal line)
- Line 3 (light gray): buffer ceiling (ceiling + 10%)
- Shaded green region: between actual line and ceiling (when under)
- Shaded orange region: between ceiling and buffer ceiling (when in buffer)
- Shaded red region: above buffer ceiling (when breached)

Hovering any day shows the exact actual + deed count + the day's biggest component contributor.

---

## Accessibility

- All numerics readable by screen reader with units ("zero point zero zero four nine US dollars per deed")
- Variance status text is primary signal · color is redundant
- Component breakdown uses semantic table markup
- Stacked bar segments include ARIA labels with component + percentage
- High contrast palette (tested against the 4.5:1 minimum)

---

## Tribunal-integration notes

- Cost-to-mint values are computed by accumulating receipt-level `cost_to_mint_usd` (every deed carries this field per Proof of Economics)
- The component breakdown is computed by accumulating `cost_to_mint_breakdown` sub-fields
- Quarterly formula updates are themselves Hedera-anchored deeds (`DDEED-DOV-ECON-Q{n}-{year}-v{v}`)
- The dial's formula_version field always references the most recent applicable deed
- Buffer breach is a rule-layer flag · auto-triggers sr broker notification + founder cc

---

## Reporting integration

The cost-to-mint dial feeds:

- The Defendable Closing Statement G4 (Economics) grade
- The Morning Brief slot 3 (cost summary)
- The monthly invoice (per-deed line items + variance reporting per LOU §4.3)
- The annual engagement calibration deed (cost-to-mint vs ceiling vs forecast)
- The quarterly cost-to-mint update deed (formula deltas)

---

## Cross-references

- [Energy and Cost to Mint Doctrine](../doctrine/09_energy_and_cost_to_mint.md) · the formula · the components · the published math
- [Cost-to-Mint Playbook](../playbooks/cost_to_mint_playbook.md) · how to walk this dial with a CFO
- [Receipts · Deeds · Books and Records Doctrine](../doctrine/10_receipts_deeds_and_books_records.md) · the Proof of Economics field source
- [Letter of Understanding example](../examples/sample_letter_of_understanding.md) · §4.2 the source of the ceiling
- [Sample Deed Receipt example](../examples/sample_deed_receipt.md) · how the per-deed cost is captured
- [Probability of Close UI Dial](probability_of_close.md) · cost feeds the `operator_hygiene` driver
- [Assignment Success UI Dial](assignment_success.md) · cost feeds G4 (Economics)

🐝 *The meter runs · the math is published · the CFO audits · the trust compounds.*
