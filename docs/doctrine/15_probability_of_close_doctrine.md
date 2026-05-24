# 15 · Probability of Close Doctrine

> *"Make the dial. Build the math. The number is the number. It moves or it doesn't · and the principal deserves to know which way."*
>
> — Founder · M&M operator cadence · 2026-05-24

---

## Why this doctrine exists

Every CRE shop in the country runs a dial on every listing. Sr brokers know within 10 minutes of touring a building whether it's a 30% deal or a 70% deal. The dial isn't magic · it's pattern · it's color · it's comps · it's the buyer pool · it's whether the seller is motivated or playing tourist.

We bring the same physics to AI engagements. Every assignment we run carries a **Probability of Close** dial. The dial is a number between 0.00 and 1.00 · updated daily · visible to the principal · visible to the operator · backed by receipts.

This doctrine answers three questions:

1. **What drives the dial?**
2. **How do we communicate it to the principal?**
3. **What threshold triggers escalation · and to whom?**

The dial is not a vibe. The dial is math. The math is the broker's job.

---

## Definition

**Probability of Close** (often abbreviated `P(close)` or `PoC`) is the modeled likelihood that an open assignment lands in one of the two CLOSED outcomes (HONEY or CONDITIONED) per the Assignment Success Doctrine. Values are reported on a 0.00 - 1.00 scale and bucketed into 5 bands for UI clarity.

The dial is updated nightly by the Tribunal during the 2am reconciliation cron · and on-demand any time a material driver moves (new color · new failure event · new principal feedback · new market move).

| Band | Range | What it means | Action |
|---|---|---|---|
| **GREEN · LOCKED** | 0.85 - 1.00 | We're going to close. Color is strong · drivers are stable · no red flags. | Hold the line · weekly cadence · no surprise calls |
| **AMBER · TRACKING** | 0.65 - 0.84 | We're tracking but the deal isn't done. One or two drivers need attention. | Bi-weekly cadence · named action items per driver |
| **YELLOW · WATCHLIST** | 0.45 - 0.64 | We're at risk. Multiple drivers off-spec · or one critical driver underwater. | Daily cadence · sr broker on the desk · principal briefed by Friday |
| **ORANGE · ESCALATION** | 0.25 - 0.44 | We're losing the deal. Principal-level intervention required. | Founder call within 48 hours · revised flight sheet on the table |
| **RED · DARK** | 0.00 - 0.24 | The deal is dark. Recovery plan or release. | Same-day principal call · PASS-pivot decision · failure deed pre-staged |

The bands are not arbitrary · they're calibrated against historical close rates from the founder's 30-year CRE book · scaled to AI engagement patterns observed across the first 8,400+ deeds.

---

## The deal physics · what drives the dial

A CRE deal pencils on five drivers. An AI engagement pencils on the same five drivers · renamed for the medium. The dial is a weighted composite. Each driver is independently scored · independently reported · independently auditable.

| # | Driver | Weight | What it measures (AI engagement form) |
|---|---|---|---|
| 1 | **Color strength** | 25% | Independent-source verification of the principal's pain · the agent's actual behavior · the workflow's actual shape. Higher color = higher dial. |
| 2 | **Principal motivation** | 20% | Real urgency · real budget · real authority. Maps to CRE "seller motivation" (1031 clock · refi expiring · partnership dispute). |
| 3 | **Asset condition** | 20% | The state of the agent fleet under defense. Honey rate · Propolis frequency · validator chain pass rate · last 30 days. |
| 4 | **Buyer pool / fit** | 15% | The fit between the principal's actual workflow and DefendableOS's defense capabilities. Sometimes the right answer is "they need a different vendor" · the dial reflects that. |
| 5 | **Comp quality** | 10% | How well the engagement resembles prior closed engagements where we know the outcome. Strong comps = high confidence in the dial. |
| 6 | **Operator hygiene** | 10% | Cadence kept · deeds filed on time · cost-to-mint under ceiling · the small stuff that proves we can run the assignment without dropping balls. |

The composite is bounded · drift-checked against the Tribunal's two-judge consensus · and rounded to two decimals before display. The raw float is preserved in books-and-records for audit.

---

## What drives the dial UP

- **Color count increases** · the jr broker added 3 new independent sources this week
- **Principal answered the diligence questions same-day** · motivation signal
- **Honey rate trend is positive** · the agents are stabilizing
- **A comparable assignment closed at HONEY recently** · the comp justifies the confidence
- **Cost-to-mint came in under ceiling** · operator hygiene proven
- **The principal accepted a CONDITIONED outcome on a prior assignment** · they understand the contract physics · low surprise risk

## What drives the dial DOWN

- **A critical color claim turned out to be wrong** · the jr broker over-asserted · sr broker downgrades
- **Principal stopped returning calls** · motivation flag
- **A Propolis event hit a critical path** · the asset condition degraded
- **The vertical fit got reconsidered** · we may have taken a deal we should have PASSED on
- **Cost-to-mint blew past ceiling** · margin is gone · principal will hear it on the closing statement
- **A new competitor entered the conversation** · buyer pool dynamics shifted

The dial isn't punitive. The dial is honest. A drop is a signal · not a verdict. The verdict is the closing statement.

---

## How to communicate the dial to the principal

The Morning Brief (06:00 daily email · client-facing) ALWAYS contains the current dial · the band · the top 3 drivers moving it · and one named action item per driver. The principal should never have to ask "where are we?" — the answer is in their inbox at 06:00 with a coffee timestamp.

The format · per the Morning Brief Playbook:

> **Probability of Close**: `0.78` · **AMBER · TRACKING**
>
> **Up**: Color count moved from 7 to 9 sources this week · principal completed 4 of 5 diligence items same-day.
>
> **Down**: One critical claim ("the refund agent never hallucinates on negative balances") was contradicted by Tribunal observation · we're re-verifying.
>
> **Action**: Sr broker scheduling 30-min call Thursday to walk the principal through the contradiction · proposing one of three remediation paths.

Three sentences. One link to the receipt. No marketing voice. No hedge. The principal reads it · knows where the deal stands · and trusts the broker to run the next step.

When the dial moves more than 0.10 in either direction in a 24-hour window · a same-day call is mandatory. Email is not enough for a 10-point swing.

---

## Escalation thresholds

The dial drives the escalation pyramid. Every band has a named owner and a named response cadence. No band is "ignore."

| Band | Owner | Cadence | Escalation trigger |
|---|---|---|---|
| GREEN · LOCKED | Jr broker | Weekly Morning Brief · monthly review | Any drop > 0.05 → sr broker review |
| AMBER · TRACKING | Sr broker | Bi-weekly Morning Brief upgrade · named drivers reviewed | Any drop > 0.10 OR any driver below 0.50 → founder review |
| YELLOW · WATCHLIST | Sr broker + founder cc | Daily Morning Brief · sr broker on the desk | 7 days without upward movement → founder takes the relationship lead |
| ORANGE · ESCALATION | Founder direct | Twice-daily Morning Brief · founder reachable on text | Any single day in ORANGE → revised flight sheet on the principal's desk by noon next day |
| RED · DARK | Founder + sr broker pair | Real-time · open phone line | Same-day · pause assignment if requested · PASS-pivot decision document drafted |

The escalation pyramid is not bureaucracy · it's the brokerage discipline that earned $8B in CRE closes. When the dial moves · the right voice is on the phone within the right window. No exceptions · no delegation by reflex.

---

## What the dial is NOT

- **NOT a probability of perfection.** A 0.78 dial doesn't mean the assignment closes at 78% quality · it means there's a 78% modeled chance the assignment lands HONEY or CONDITIONED. Quality is graded separately at close.
- **NOT a price tag.** The dial doesn't determine the fee. The LOU does that. The dial determines whether the fee is likely to be earned.
- **NOT a marketing number.** We don't publish dials externally. The dial is operator + principal information only. Surfacing it in a sales deck would be malpractice · same as a CRE broker showing the buyer pool's bid range publicly.
- **NOT static.** A locked dial is a dial that's earned its lock. It can lose it. We re-evaluate weekly minimum · daily under YELLOW or worse.

---

## How this plugs into the rest of the doctrine

- **Assignment Success** ([14_assignment_success_doctrine.md](14_assignment_success_doctrine.md)) is the post-close report. P(close) is the pre-close prediction. The variance between them is a permanent calibration signal.
- **Color** drives 25% of the dial. The color file is the dial's largest input.
- **PASS Doctrine** is the dial's intake filter. We don't let a deal onto the dial that we wouldn't ride to close.
- **Morning Brief** is the daily surfacing channel. The dial · the band · the drivers · the actions · always.

---

## Related terms

- [probability-of-close](../vocabulary/scoring_terms/probability-of-close.md)
- [assignment-success](../vocabulary/scoring_terms/assignment-success.md)
- [client-confidence](../vocabulary/scoring_terms/client-confidence.md)
- [morning-brief](../vocabulary/client_terms/morning-brief.md)
- [pre-market-flight-sheet](../vocabulary/client_terms/pre-market-flight-sheet.md)
- [pass-doctrine](../vocabulary/client_terms/pass-doctrine.md)
- [color](../vocabulary/cre_terms/color.md)

🐝 *Make the dial · build the math · run the deal.*
