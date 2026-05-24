# UI Dial Spec · Probability of Close

> *The principal-facing dashboard dial for engagement-level Probability of Close. Lives on the engagement dashboard. Mirrored in the Morning Brief.*

---

## Purpose

Surface the Probability of Close dial to both operator and principal in a single canonical visual representation. The dial is the engagement's pulse · the most important number on any active engagement dashboard.

This spec is the contract between the doctrine ([15_probability_of_close_doctrine.md](../doctrine/15_probability_of_close_doctrine.md)) · the scoring term ([probability-of-close.md](../vocabulary/scoring_terms/probability-of-close.md)) · and the UI implementation.

---

## Visual

### Dial shape

A half-circle gauge dial · 180° arc · pointing UP at 0.50 · sweeping from 0.00 (left) to 1.00 (right).

```
                    1.0
                     |
         GREEN ←  AMBER  →
        /                  \
       /                    \
      /  YELLOW  ORANGE  RED \
     /                        \
   0.0                        1.0
```

- Arc thickness: 24px
- Arc length: 60% of card width
- Needle: solid 4px width · top-pivoting · color matches current band

### Color bands (left to right · 0.00 → 1.00)

| Band | Range | Hex | RGB | Tailwind class |
|---|---|---|---|---|
| RED · DARK | 0.00 - 0.24 | `#B91C1C` | rgb(185, 28, 28) | `bg-red-700` |
| ORANGE · ESCALATION | 0.25 - 0.44 | `#EA580C` | rgb(234, 88, 12) | `bg-orange-600` |
| YELLOW · WATCHLIST | 0.45 - 0.64 | `#CA8A04` | rgb(202, 138, 4) | `bg-yellow-600` |
| AMBER · TRACKING | 0.65 - 0.84 | `#D97706` | rgb(217, 119, 6) | `bg-amber-600` |
| GREEN · LOCKED | 0.85 - 1.00 | `#15803D` | rgb(21, 128, 61) | `bg-green-700` |

NOTE: AMBER and ORANGE are distinct colors · NOT shades of the same family. AMBER reads as "tracking · watch but don't panic." ORANGE reads as "this needs principal attention TODAY." Color discipline matters · the principal's eye should distinguish them in 0.5 seconds.

### Numeric overlay

- Center of the dial · two-decimal value (e.g., `0.78`)
- Below the value · band label (`AMBER · TRACKING`)
- Below the band · 7-day delta arrow + value (e.g., `↓ 0.03 · 7d`)

Font: serif numeric (Source Serif Pro or similar broker-grade typography · NOT sans-serif "fintech" feel).

---

## Card layout

```
┌─────────────────────────────────────────────┐
│  PROBABILITY OF CLOSE                       │
│  ENG-DOV-LOGISTICS-ACME-0001                │
│                                             │
│       ╭──────────────╮                      │
│      ╱                ╲                     │
│     ╱       0.78      ╲                     │
│    ╱  AMBER·TRACKING   ╲                    │
│   │      ↓ 0.03 · 7d    │                   │
│    ╲                   ╱                    │
│     ╲                 ╱                     │
│      ╲_______________╱                      │
│                                             │
│  Drivers ▼                                  │
│  ─────────────────────                      │
│  color_strength       0.88 ↑ +0.07 30d      │
│  principal_motivation 0.85 → steady          │
│  asset_condition      0.79 ↓ -0.04 30d      │
│  buyer_pool_fit       0.86 → steady          │
│  comp_quality         0.72 → steady          │
│  operator_hygiene     0.62 ↓ -0.09 30d      │
│                                             │
│  Last refresh: 2026-06-15 02:14 ET          │
│  [View 90-day history] [View driver detail] │
└─────────────────────────────────────────────┘
```

Card dimensions: 480px × 600px (desktop) · responsive scales to 320px × 480px (mobile).

---

## Data binding

### Read paths (backend → UI)

| UI element | Source field | Update cadence |
|---|---|---|
| Dial value | `engagement.probability_of_close` | Nightly cron + on-demand |
| Band | `engagement.probability_of_close_band` (derived) | Nightly cron |
| 7-day delta | computed from `engagement.probability_of_close_history` | On render |
| Driver values | `engagement.probability_of_close_drivers` | Nightly cron |
| Driver deltas | computed from driver history | On render |
| Last refresh | `engagement.probability_of_close_last_refresh_at` | On update |

### API endpoint

```
GET /api/v1/engagements/{engagement_id}/dial/probability-of-close
```

Response shape:

```json
{
  "engagement_id": "ENG-DOV-LOGISTICS-ACME-0001",
  "value": 0.78,
  "band": "AMBER_TRACKING",
  "trajectory_7d": -0.03,
  "trajectory_30d": -0.05,
  "drivers": {
    "color_strength": {"value": 0.88, "weight": 0.25, "delta_30d": 0.07},
    "principal_motivation": {"value": 0.85, "weight": 0.20, "delta_30d": 0.00},
    "asset_condition": {"value": 0.79, "weight": 0.20, "delta_30d": -0.04},
    "buyer_pool_fit": {"value": 0.86, "weight": 0.15, "delta_30d": 0.00},
    "comp_quality": {"value": 0.72, "weight": 0.10, "delta_30d": 0.00},
    "operator_hygiene": {"value": 0.62, "weight": 0.10, "delta_30d": -0.09}
  },
  "last_refresh_at": "2026-06-15T02:14:08Z",
  "escalation_status": "NONE",
  "history_90d_url": "/api/v1/engagements/ENG-DOV-LOGISTICS-ACME-0001/dial/history?dial=poc&days=90"
}
```

Caching: 1-hour TTL on principal-facing endpoint · sub-minute on operator-facing endpoint. Both endpoints invalidate on the nightly cron.

---

## Interaction

### Click behaviors

| Element | Action |
|---|---|
| Dial center | Expand to full driver detail panel (modal) |
| Band label | Show band-specific guidance (the same text as the Probability of Close Playbook · per-band scripts) |
| 7-day delta arrow | Show 30-day · 60-day · 90-day deltas in tooltip |
| Driver row | Show driver-specific evidence (color sources for color_strength · responsiveness data for principal_motivation · etc) |
| Last refresh | Show next-refresh ETA (typically 02:00 next day for nightly cron) |
| `View 90-day history` | Open trajectory chart in panel |
| `View driver detail` | Open driver evidence drill-down |

### Hover behaviors

- Hovering over the dial shows the exact float value (4 decimals · for operator precision)
- Hovering over a driver shows the underlying evidence sources count + last refresh
- Hovering over the band shows the band's escalation pyramid (which roles are notified at this band)

### Keyboard navigation

- `Tab` cycles through driver rows
- `Enter` on dial center opens detail modal
- `Escape` closes modal
- `R` triggers manual refresh (operator-only · requires permission · audit-logged)

---

## States

### Loading state

- Dial outline visible · arc empty · pulsing skeleton
- "Refreshing..." text below
- All driver rows skeleton

### Provisional state

When dial is < 3 daily snapshots since engagement open:

- Dial visible at value · band visible · BUT
- Banner above: "Provisional · {N} of 3 daily snapshots captured · stabilizes 2026-06-18"
- Drivers shown but flagged with `[provisional]` tag

### Stale state

When `last_refresh_at` > 72 hours ago:

- Dial visible · BUT rendered grayscale
- Banner: "Stale · last refresh {N} hours ago · investigating"
- Auto-escalation triggered to sr broker (per `stale_dial` failure mode)

### Error state

When the dial cannot be computed (missing inputs · driver compute failure · etc):

- Dial shows `--` instead of a value
- No band color · neutral gray
- Banner: "Dial unavailable · sr broker notified · ETA {N}"
- Morning Brief slot also shows `--` (per the morning_brief doctrine: never fake a value)

---

## Ranges and band rules

### Hard band edges

```
band(value):
  if value >= 0.85: return GREEN_LOCKED
  if value >= 0.65: return AMBER_TRACKING
  if value >= 0.45: return YELLOW_WATCHLIST
  if value >= 0.25: return ORANGE_ESCALATION
  return RED_DARK
```

NO interpolation between bands · NO "you're at 0.85 but still amber for transition." The thresholds are sharp · the discipline is the sharpness. If you're 0.851 · you're GREEN.

### Composite derivation rule

```
composite = (
  0.25 * driver.color_strength +
  0.20 * driver.principal_motivation +
  0.20 * driver.asset_condition +
  0.15 * driver.buyer_pool_fit +
  0.10 * driver.comp_quality +
  0.10 * driver.operator_hygiene
)
```

Weights are FIXED at the schema level · not adjustable per-engagement. Calibration changes to weights happen annually only · in conjunction with a calibration deed.

### Anomaly flag rules

| Condition | Flag | Auto-action |
|---|---|---|
| Single-day drop > 0.20 | `dial_anomaly_flag` | QA validator notified |
| Below 0.50 for > 7 consecutive days | `engagement_health_check` | Deed auto-issued |
| Cross from AMBER → YELLOW | `escalation_band_change` | Sr broker notified |
| Cross from YELLOW → ORANGE | `escalation_band_change` | Founder cc · sr broker drives |
| Cross from ORANGE → RED | `relationship_emergency` | Founder leads · same-day call |

---

## Accessibility

- Dial value AND band readable by screen readers (ARIA labels)
- Color is REDUNDANT signal · band label text is the primary signal
- Color-blind safe palette (tested against deuteranopia · protanopia · tritanopia)
- Keyboard-navigable for every interaction
- Minimum 4.5:1 contrast on all text overlays

---

## Operator-only extensions

When viewed by an operator (sr broker · jr broker · QA validator · founder):

- Additional `[Override]` button (sr broker + founder only · audit-logged)
- Additional driver-evidence drill-down (full source lists · weights · timestamps)
- Additional `Cross-engagement comp` button (shows similar dials across the book for pattern analysis)
- Additional `Last calibration delta` (shows the delta between predicted close-rate and actual close-rate from the most recent annual calibration report)

These extensions are NOT visible in the principal-facing view. Schema-level visibility enforcement.

---

## Tribunal-integration notes

- The dial value is computed by the nightly 2am Tribunal reconciliation cron
- The Tribunal does NOT directly grade the dial (the dial is a derived output · not an attestation)
- Rule-layer flags (anomaly · stale · provisional) are surfaced in the UI banner
- Drift-checks between Scale A + Scale B judges on the `asset_condition` driver inputs flag the UI for manual review

---

## Cross-references

- [Probability of Close Doctrine](../doctrine/15_probability_of_close_doctrine.md) · the deal physics
- [Probability of Close Playbook](../playbooks/probability_of_close_playbook.md) · per-band scripts the band-label click action uses
- [Probability of Close (scoring term)](../vocabulary/scoring_terms/probability-of-close.md) · schema and scoring impact
- [Probability of Close (sample term)](../examples/sample_term_probability_of_close.md) · the canonical 13-section worked example
- [Morning Brief term](../vocabulary/client_terms/morning-brief.md) · where the dial also surfaces (text-only · slot 1)
- [Assignment Success UI Dial](assignment_success.md) · the post-close companion dial
- [Cost-to-Mint UI Dial](cost_to_mint.md) · the economics companion dial

🐝 *The dial is the pulse · the UI is the window · the discipline is the daily refresh.*
