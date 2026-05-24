# Principal

## Street Definition

"Who's the principal?" — the founder asks before agreeing to any sit.

The **Principal** is the actual decision-maker on the customer side. The person whose name is on the door · whose ass is on the line · who has the authority to sign · the budget to fund · and the operational stake to live with the outcome.

NOT IT. NOT procurement. NOT a finance manager. NOT "let me check with my team." The principal is the principal. If we don't have access to the principal · we don't have a deal · we have a forwarding chain · and forwarding chains don't close engagements at broker-grade.

## CRE Operator Meaning

In CRE · the principal is the building owner · the LP-stake holder · the family-office director · the credit-tenant CFO · whoever can say yes and have the yes stick. The broker spends years building access to principals · because principals are who write the checks that close trades.

The number-one CRE rule: **never spend more than 20 minutes with a non-principal · unless it's a path to the principal.** Procurement gates · IT diligence · legal review · all of those are necessary stops on the road · but the road ends at the principal. If the principal isn't reachable · the road doesn't end at a close.

A sr broker can tell within 2 conversations whether they're talking to the principal or to a deflector. The signals: budget authority · operational pain ownership · willingness to engage on tradeoffs without checking back · ability to schedule the next meeting on the spot.

## DefendableOS Definition

The **Principal** in DefendableOS is the named decision-authority contact on the customer side · documented in the Letter of Understanding §11 · and required to sign every assignment brief under the engagement.

A principal carries:
- `role` (CEO · COO · Founder · MD · Owner · etc · NOT "IT Director" · NOT "Procurement Lead")
- `decision_authority_scope` (engagement-level · assignment-level · escalation-level)
- `escalation_tier` (which escalation events trigger which contact path)
- `morning_brief_recipient` (does the principal receive the daily 06:00 brief)
- `founder_text_authorized` (T3 / T4 tiers only · principal has founder's text)

Every engagement must have ONE primary principal. Multi-principal engagements (e.g., COO + CFO co-decision) are documented as such · with explicit decision-allocation rules in the LOU.

## Backend Representation

```json
{
  "principal.principal_id": {"type": "string", "primary_key": true},
  "principal.engagement_id": {"type": "string", "fk": "engagement.engagement_id"},
  "principal.name": {"type": "string"},
  "principal.role": {"type": "string"},
  "principal.role_is_decision_authority": {
    "type": "boolean",
    "validation_rule": "must be true · enforced at engagement creation"
  },
  "principal.email": {"type": "string", "format": "email"},
  "principal.phone": {"type": "string", "nullable": true},
  "principal.escalation_tier": {
    "type": "enum",
    "values": ["DAILY_BRIEF_ONLY", "WEEKLY_SR_BROKER", "FOUNDER_ON_TEXT", "FOUNDER_ON_TEXT_24X7"]
  },
  "principal.is_primary_decision_authority": {"type": "boolean"},
  "principal.co_decision_with": {"type": "string_array", "nullable": true},
  "principal.last_touch_at": {"type": "timestamp"},
  "principal.responsiveness_score": {
    "type": "float",
    "range": [0,1],
    "derived_from": "avg response time to sr broker outreach last 30 days"
  }
}
```

Schema files: `docs/schemas/principal.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

The **principal** is YOU · if you're the decision-maker on your side · the person who signs · funds · and stakes their name on the engagement.

We work with principals directly. Not procurement. Not your IT team (though we coordinate with them). Not a designated middle-manager (though we'll loop them in for operational details). We need to talk to the person who can say yes · live with the outcome · and call us when something doesn't pencil.

If you're NOT the principal · we'll ask warmly to be introduced. We don't grandstand · we don't pressure · we just don't pretend a non-principal conversation is the same as a principal conversation. Both sides waste less time when we're honest about that up front.

## Jr Broker Use

When you make first contact:

- **Confirm principal status within the first 2 conversations**. If you're not talking to the principal · politely ask who is · and request the warm intro. Most professional principals respect this directness.
- **Don't pitch hard to non-principals**. Use the conversation to gather color · build credibility · earn the intro. Pitching at non-principals burns the warm-handoff opportunity.
- **Log principal role explicitly** in the lead folder. "Director of Operations" is not "COO." The difference matters at LOU stage.
- **Track responsiveness**. If a self-identified principal takes 14+ days to respond to a discovery question · they may not actually be the decision-authority · re-assess.

The PASS doctrine has a principal-specific corollary: if we can't get principal access in 60 days after first contact · we PASS · graceful exit · re-queue in 6 months. We don't run engagements through deflection chains.

## Sr Broker Use

The sr broker:

- **Validates principal authority** at the Appraisals stage (BEFORE drafting an LOU)
- **Negotiates the LOU directly with the principal** · never through intermediaries on material terms
- **Maintains principal relationship continuity** · across multiple sr-broker handoffs (the relationship survives the broker rotation)
- **Calls the principal directly** on any escalation trigger (per the escalation pyramid in the LOU)
- **Walks the closing statement personally** with the principal on T2 / T3 / T4 tiers

The sr broker is also responsible for the **principal-handoff doc** when sr broker reassignments happen. The new sr broker must be introduced to the principal in writing · with a 30-min hand-off call scheduled · BEFORE the previous sr broker disengages.

## Tribunal Use

The Tribunal doesn't grade principals (they're not adjudicated) · but it tracks:

- `principal.responsiveness_score` feeds the `principal_motivation` driver of the Probability of Close dial (20% weight)
- `principal.last_touch_at` feeds engagement-health flags (no-touch > 14 days triggers sr broker outreach)
- Principal-acknowledgment of closing statements is a required gate before issuing the closing-deed
- Multi-principal disagreement (e.g., COO and CFO send conflicting signals) flags the engagement for sr-broker reconciliation

## Evidence Required

For a principal record to be defensible:

- Confirmed decision-authority role (documented in LOU §11 · principal acknowledges in writing)
- At least one direct touch documented (not via intermediary)
- Contact methods confirmed (email · phone if T3/T4)
- Escalation tier explicitly chosen
- Annual re-confirmation that the principal still holds the role (org changes happen · we re-verify yearly)

A principal record without confirmed authority is treated as `STAKEHOLDER_NOT_PRINCIPAL` · and operations against it follow a different cadence (no direct LOU signature · no founder-text path · no closing-walk).

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **mislabeled_principal** | Person tagged as principal · turns out to be a stakeholder · LOU signature was non-binding | PROPOLIS · LOU re-paper required · sr broker review |
| **proxy_signing** | LOU signed by someone other than the named principal · forwarded · no direct acknowledgment | PROPOLIS · LOU re-paper · trust breach |
| **principal_silence** | Principal goes 30+ days without acknowledging any Morning Brief | JELLY · pulse-check required · sr broker call |
| **role_change_undetected** | Principal leaves the org · we don't catch it for 60+ days · engagement runs on phantom authority | PROPOLIS · founder-led re-engagement |
| **escalation_skip** | Material event happened · principal not notified per LOU escalation pyramid | PROPOLIS · trust breach · founder review |

## Scoring Impact

- **assignment_success**: HIGH (principal engagement correlates strongly with assignment success rates)
- **repair_lift**: MEDIUM (principals who acknowledge failure deeds quickly enable faster repair)
- **validator_confidence**: HIGH (principal acknowledgment of closing statements is a required gate)
- **risk_temperature**: INVERSE (engaged principal = lower risk · disengaged principal = elevated risk)
- **probability_of_close**: HIGH (principal_motivation is 20% of the dial)
- **evidence_strength**: HIGH (principal-signed artifacts are the strongest evidence class)
- **cost_to_mint**: NEUTRAL (principal doesn't directly affect cost · but disengagement raises rework costs)

## Deed / Receipt Impact

- **Receipt fields touched**: every assignment-level deed (brief · closing · amendment) requires principal signature · captured in deed metadata
- **DDEED class impact**: deeds requiring principal signature cannot issue without `principal_signature_confirmed: true`
- **Books and records layer**: principal contact info preserved across all 5 layers · with explicit "this principal held this role at this time" historical record (org changes don't rewrite history)
- **5 Proofs touched**: PROCESS (principal involvement is part of the deed lineage) · TRUST (principal-acknowledged deeds carry higher trust weight)

## Related Terms

- [engagement](engagement.md) · the canopy the principal authorizes
- [assignment](assignment.md) · the work order the principal signs
- [letter-of-understanding](letter-of-understanding.md) · the document the principal countersigns
- [closing-statement](closing-statement.md) · the artifact walked with the principal
- [morning-brief](morning-brief.md) · the daily principal-facing communication
- [pass-doctrine](pass-doctrine.md) · the protocol when principal access can't be earned

## Example

> **Principal**: Jane Smith · COO · Acme Logistics Inc.
>
> **Authority scope**: Engagement-level + assignment-level signature · escalation tier `FOUNDER_ON_TEXT` (T3 White-Glove inclusion)
>
> **Role validation**: confirmed at LOU signing 2026-03-12 · LinkedIn cross-verified · Acme corporate website cross-verified · annual re-confirmation scheduled 2027-03-12.
>
> **Co-decision**: CFO Mike Chen has financial-authority co-sign on items > $20K/month variance (LOU §11.1)
>
> **Responsiveness score**: 0.91 (avg response time to sr broker outreach: 4.3 hours · last 30 days)
>
> **Last touch**: 2026-06-12 (Q3 QBR scheduling email · responded same-day)
>
> **Morning brief recipient**: yes (06:00 ET daily)
>
> **Founder text**: yes (used twice in the engagement to date · both times appropriately · founder kept it brief and professional)

## DefendableOS Notes

- The principal is the relationship · NOT the user. We optimize the principal relationship · not user-count metrics. A high-engagement single-principal account is more valuable than a 50-user low-engagement one.
- Principal-acknowledged deeds are the strongest deeds in the books-and-records. We track principal-ack rates as an engagement-health KPI.
- We don't sell to procurement. Procurement is a process gate · not a buyer. Treating procurement as the buyer is how engagements turn into commodity SaaS subscriptions · and we don't run those.
- The founder is the principal on Swarm & Bee's side · the same way the customer principal is on theirs. Both sides have a person whose name is on the door. That's how the relationship balances.

🐝 *The principal is the relationship. The relationship is the deal. The deal is the receipt.*
