# Digest

## Street Definition

"What's the digest say?" — a sr broker asks before walking into a sit.

A **digest** is the pre-meeting summary the agent prepared for the broker. One page. Color built. Pricing thought-out. Pain hypothesis named. The thing the sr broker reads in the seven minutes before they walk into the sit so they show up sharp · not winging it.

In CRE, a digest is the difference between a sr broker who looks like they've done their homework and one who looks like they're improvising. In DefendableOS, a digest is the difference between a deed that ships clean and a deed that gets re-traded mid-engagement because the team didn't catch a known gap.

## CRE Operator Meaning

In CRE, the digest is the jr broker's gift to the sr broker. It's the pre-market flight sheet condensed for a single meeting · the highlights · the gotchas · the asks · the close opportunity. A digest contains:

- Who the principal is (name, title, signing authority, prior relationships)
- What they own (asset class, deal size range, recent activity)
- What we know that they don't know we know (the color advantage)
- What we don't know that we wish we did (the open questions)
- What the meeting needs to accomplish (the specific ask · book the appraisal · win the listing · close the LOU)
- What we're ready to offer (the pricing scenarios, the term structures, the walk-away point)

No digest · no sit. The sr broker walks in without one only when they have decades of relationship with the principal and don't need the brief. New relationships always get a digest.

## DefendableOS Definition

In DefendableOS, the **digest** is a typed, validated, receipted artifact that an agent (human or AI) produces ahead of every meaningful workflow checkpoint. Every customer meeting gets a digest. Every Tribunal verdict review gets a digest. Every escalation gets a digest. Every renewal review gets a digest.

The digest is the agent's last-mile output before a human makes a decision. It compresses the underlying receipts, color files, validator results, and Tribunal verdicts into a one-page brief that the decision-maker can read in under five minutes and act on.

## Backend Representation

```json
{
  "engagement.digest_v1": {
    "type": "jsonb",
    "schema": "docs/schemas/digest.schema.json",
    "required_fields": [
      "engagement_id",
      "meeting_id_or_decision_id",
      "principal_summary",
      "color_summary_score",
      "open_questions[]",
      "ask",
      "offer_scenarios[]",
      "walk_away_threshold",
      "evidence_receipts[]"
    ]
  },
  "engagement.digest_delivered_at": {
    "type": "timestamp",
    "scoring_hook": "preparation_lead_time_hours"
  },
  "engagement.digest_reader_id": {
    "type": "uuid",
    "description": "Sr broker or decision-maker who consumed the digest"
  },
  "engagement.digest_read_at": {
    "type": "timestamp"
  }
}
```

Schema files: `docs/schemas/digest.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

The digest is the pre-meeting brief our team prepares before any conversation with you that requires a decision. It contains everything we know, everything we still need to verify, the specific question we're trying to answer with you, and our recommended path forward. You may never see a digest directly · they live on our side of the table · but every Morning Brief, every Closing Statement, and every LOU clause we present to you started life in a digest. The discipline of preparing one is what makes our team show up to your meetings ready, not improvising.

## Jr Broker Use

You write the digest for every sit on your sr broker's calendar. The discipline is non-negotiable:

- **24-hour rule.** Digest delivered to the sr broker 24 hours before the meeting. Not 23. Not the morning of. 24 hours so they can absorb, ask you questions, and prep their own framing.
- **Use the template.** Digest template lives at `docs/examples/sample_digest.md` (SH2 ships). Same structure every time so the sr broker can find what they need at speed.
- **Cite the receipts.** Every claim in the digest links to a receipt ID. The sr broker can drill into any line and see the evidence.
- **Name the walk-away.** Every digest has an explicit walk-away threshold. If the meeting goes off the script in a way that crosses that threshold, the sr broker knows to PASS.
- **Refresh stale digests.** If a sit gets rescheduled by more than 48 hours, the digest gets a refresh pass · color may have moved, vendor changelogs may have dropped, the customer may have made an announcement.

## Sr Broker Use

You read the digest with three filters:

- **Is the color enough?** If `color_summary_score < 0.70`, you send it back · do not walk into the sit on weak color.
- **Are the open questions material?** If the open questions include anything that would change the pricing scenarios, you delay the meeting · prep first, sit second.
- **Does the walk-away threshold match the relationship?** A first-meeting digest with no walk-away threshold is a doctrine violation · every sit has one. If the jr broker missed it, you set it before you walk in.

You also audit digest discipline weekly. Digests that ship without receipt citations · digests that arrive under 24 hours · digests that lack walk-away thresholds · these are jr broker remediation events.

## Tribunal Use

The Tribunal grades digests as a first-class output type · not just as input to a human decision.

- **Rule layer**: digest with `color_summary_score < 0.70` → automatic JELLY classification regardless of judge
- **Rule layer**: digest missing `walk_away_threshold` → critical_failure → JELLY at minimum, PROPOLIS if customer-facing
- **Judge layer**: digest quality scored on completeness (1-5), accuracy of cited receipts (1-5), and decision-readiness (1-5) by Scale A + Scale B
- **Classification impact**: digests can earn Royal Jelly when the cited evidence is unusually strong and the walk-away analysis is incisive · these become training pairs for future digest agents

```yaml
classification_impact: [HONEY, ROYAL_JELLY, JELLY, PROPOLIS]
can_be_critical_failure: true
rule_layer_checks:
  - color_summary_score >= 0.70
  - walk_away_threshold present
  - all citations resolve to valid receipt IDs
  - delivered ≥ 24h before meeting
```

## Evidence Required

- ≥ 3 cited evidence receipts (each resolving to an L2-sealed Merkle batch)
- `color_score` source weight average ≥ 0.85
- `open_questions[]` populated · empty array is a doctrine red flag (means the jr broker stopped looking)
- Walk-away threshold explicitly named with dollar value or term-of-engagement equivalent
- Pricing scenarios at least 3 (low / target / stretch)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **late_digest** | Delivered < 24h before meeting | JELLY |
| **uncited_claims** | Claims without receipt links | JELLY |
| **missing_walk_away** | No walk-away threshold named | JELLY (PROPOLIS if customer-facing) |
| **stale_color_in_digest** | Color file > 14 days old, not refreshed | JELLY |
| **fabricated_principal_intel** | Principal background asserted without source | PROPOLIS |
| **wishful_pricing** | Pricing scenarios don't tie to actual color or comp set | JELLY |
| **single_scenario_only** | Only one pricing scenario · no negotiation room | JELLY |

## Scoring Impact

- **assignment_success**: HIGH · digest quality is the strongest predictor of in-meeting close rate
- **repair_lift**: HIGH · digests that flag adversarial cases early prevent downstream PROPOLIS events
- **validator_confidence**: HIGH · digest-cited receipts feed directly into validator chain inputs
- **risk_temperature**: INVERSE · strong digests reduce engagement risk profile
- **probability_of_close**: HIGH · sits prepped with strong digests close at 1.5-2x the rate of unprepped sits
- **evidence_strength**: DIRECT · digest evidence count = engagement evidence count
- **cost_to_mint**: LOW · digest creation is cheap · poor digests are expensive in re-trade cycles

## Deed / Receipt Impact

- **Receipt fields touched**: `digest_v1_hash`, `digest_delivered_at`, `digest_lead_time_hours`, `digest_evidence_receipt_refs[]`, `digest_walk_away_threshold_usd`
- **DDEED class impact**: deeds for engagements with poor digest discipline carry a `preparation_quality_flag` that downgrades retention probability scoring
- **Books and records layer**: L1_PG (digest stored hot) → L2_MERKLE (digest hash sealed in batch) → L3_NAS (canonical archive)
- **5 Proofs touched**: PROCESS (the lineage of decision-making) · QUALITY (evidence integrity) · ECONOMICS (preparation cost vs re-trade savings)

## Related Terms

- [color](color.md) · digest summarizes the color file
- [om](om.md) · digest is the operator-facing companion to the customer-facing OM
- [loi](loi.md) · digest precedes the LOI ask
- [due-diligence](due-diligence.md) · digest is the diligence-summary artifact
- [probability-of-close](probability-of-close.md) · digest quality is a leading indicator of close prob
- [books-and-records](books-and-records.md) · every digest receipt anchors to the 5-layer stack

## Example

> **Engagement**: STNL defense engagement · cold-storage operator · Atlanta MSA · 14-agent fleet · sit booked for Thursday 10:00 ET.
>
> **Digest delivered**: Wednesday 09:00 ET (25 hours lead time)
>
> **Principal summary**: Janet K., CEO and 60% owner. Prior CRE relationship via founder's network (1031 exchange 2019). Signs personally on engagements under $250K/yr. Procurement involved above that.
>
> **Color summary score**: 0.88. 5 independent sources. EDGAR 10-K of parent (0.90). CompStak comp set on similar-size cold-storage portfolios (0.85). Vendor changelog for OpenAI Realtime API (the customer's primary inference layer · two drift events in 60 days · 0.85). Mutual board member confirmation that Janet is fee-conscious but premium-quality-driven (0.90 human-verified). SwarmCurator corpus matched 8 prior engagements of similar shape (0.85).
>
> **Open questions**: (1) does Janet know about the OpenAI Realtime drift events · or will we be surfacing? (2) is the medical-claims agent in scope for this engagement or a future phase? (3) is the existing audit vendor renewal in Q3 a tailwind or a procurement complication?
>
> **Ask**: book the appraisal · 60-min flight sheet review next week · commit to a sample receipt against the cold-storage logistics agent.
>
> **Offer scenarios**: Low: $18K/mo · 5 agents · advisory only. Target: $42K/mo · 12 agents · full Tribunal + Morning Brief. Stretch: $89K/mo · 14 agents + medical-claims · co-signed insurance carrier rider.
>
> **Walk-away threshold**: if Janet requests certification of the medical-claims agent without 60 days of clean Tribunal verdicts first · PASS · cite the doctrine · offer the cold-storage scope only.
>
> **Outcome**: sr broker walked in prepped. Janet did know about the OpenAI drift. We surfaced the receipt-anchored alternative. Booked the appraisal for following Tuesday. Engagement closed at target tier 11 days later. DDEED-DOV-CRE-COLD-ATL-000088-v1.

## DefendableOS Notes

- The digest is the canonical example of how vocabulary becomes infrastructure. Same word in CRE. Same artifact in DefendableOS. Same discipline.
- Digest agents are a near-term productization target · the SwarmCurator family is suited for digest generation, and the discipline is uniform enough to template.
- Customers should never see the operator-facing digest · they see the Morning Brief, which is the customer-facing analog (same source data, different audience, different language).
- Bad digests are the leading indicator of bad sits. Bad sits are the leading indicator of bad LOUs. Bad LOUs are the leading indicator of bad retentions. Fix the digest discipline · the rest compounds.

🐝 *Digest before sit. Color before digest. Receipts before color.*
