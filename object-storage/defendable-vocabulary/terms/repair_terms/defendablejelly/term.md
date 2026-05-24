# DefendableJelly

## Street Definition

"DefendableJelly is what the customer gets." That's the founder line. **DefendableJelly** is the brand name on the customer's invoice · the dashboard tile · the LOU clause. Inside the building we call it SwarmFixer (the refinery) and SwarmJelly (the model). The customer sees DefendableJelly · one name · one product · one trust surface.

## CRE Operator Meaning

In CRE the customer doesn't buy "the leasing software" or "the property management system." The customer buys **the building**. The systems are how we run it · the building is the asset. DefendableJelly is the asset name. It's what the CFO writes on the AP voucher. SwarmFixer is how the rehab crew talks about it · SwarmJelly is the model that powers it · DefendableJelly is what the contract says.

## DefendableOS Definition

DefendableJelly is the public-facing brand name for the entire repair layer of DefendableOS. It binds the SwarmFixer refinery + the SwarmJelly model + the Royal Jelly Record output + the DDEED-DOV-REPAIR deed lineage into one consumable product. The customer buys DefendableJelly · the operator runs SwarmFixer · the model is SwarmJelly · the deed is DDEED-DOV-REPAIR. Three internal names · one external name.

## Backend Representation

```json
{
  "defendablejelly.product_id": {"type": "string", "const": "defendablejelly"},
  "defendablejelly.internal_stack": {
    "type": "object",
    "fields": {
      "refinery": "swarmfixer",
      "model": "swarmjelly-4b:v1.2",
      "deed_class": "DDEED-DOV-REPAIR",
      "record_type": "royal_jelly_record"
    }
  },
  "defendablejelly.tier": {"type": "enum", "values": ["SELF_SERVE","MANAGED","EMBEDDED"]},
  "defendablejelly.sla_lift_target": {"type": "float", "min": 0.10},
  "defendablejelly.fix_or_refund_eligible": {"type": "boolean", "default": false},
  "defendablejelly.fix_or_refund_window_days": {"type": "integer", "default": 90}
}
```

Schema files: `docs/schemas/product_offering.schema.json` · `docs/schemas/sla.schema.json`

## Client Explanation

DefendableJelly is the part of DefendableOS that fixes the AI you already have. You ship us the failed answers · we ship back a Royal Jelly Record · five outputs that diagnose · repair · prevent · detect · and prove the fix worked. If you're on the embedded tier and we don't move the number in 90 days, we refund. That's the deal. Most customers don't take the refund · they re-up. But the option is what made the contract sign.

## Jr Broker Use

When you're on a discovery call · use the word **DefendableJelly**. Never SwarmFixer (internal). Never SwarmJelly (internal). The customer doesn't need to know the refinery from the model from the deed class · they need to know what they're buying. The dashboard tile, the invoice line, the case study, the press release · all say DefendableJelly.

When the customer asks "how does it work?" · pivot to the 5-task output · DIAGNOSE/REPAIR/PREVENT/DETECT/COMPARE. That's the customer-facing architecture. The internal stack is a footnote at the bottom of the appendix.

## Sr Broker Use

The Sr Hack on a Tier-3 engagement co-owns the **DefendableJelly SLA receipt** · the weekly attestation that the lift target is being hit. The Sr Hack signs the receipt · the customer countersigns · the receipt anchors. If the 90-day Fix-or-Refund clock is running and the receipt trend shows we're going to miss · the Sr Hack triggers a refinery tuning cycle BEFORE the SLA window closes · not after.

## Tribunal Use

- **Rule layer**: All DefendableJelly product outputs MUST be Royal Jelly Records (5-task contract) · MUST cite the SwarmJelly model tag · MUST have a validator chain pass
- **Judge layer**: Tribunal grades the underlying refinery output · the DefendableJelly brand carries the verdict but does not change it
- **Classification impact**: DefendableJelly tier-3 customers have a contractual right to weekly aggregate lift verdicts · a JELLY or PROPOLIS aggregate triggers a refund-window review

## Evidence Required

- Customer contract specifying tier (Self-serve / Managed / Embedded)
- SLA lift target (typically ≥ 0.10 for Embedded · advisory for Managed)
- Weekly aggregate lift receipt
- Underlying refinery run IDs and Royal Jelly Record IDs
- For Embedded tier · 90-day Fix-or-Refund clock and current cumulative lift

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `brand_confusion` | Customer-facing surface mentions SwarmJelly or SwarmFixer instead of DefendableJelly | n/a · brand violation |
| `unbacked_claim` | Sales surface claims a lift number not backed by anchored receipts | PROPOLIS · marketing claim audit |
| `sla_miss_no_refund` | Embedded customer hits 90-day clock with miss · refund not processed | PROPOLIS · contract violation |
| `tier_mismatch` | Customer billed at Embedded but only receiving Self-serve service level | JELLY · operations escalation |
| `weekly_receipt_skipped` | Aggregate weekly lift receipt not generated for an Embedded customer | JELLY · auto-alert to operator |

## Scoring Impact

- **assignment_success**: HIGH · DefendableJelly is THE flagship paid product
- **repair_lift**: DIRECT · the brand IS the lift promise
- **validator_confidence**: MEDIUM · brand trust correlates with weekly receipt trend
- **risk_temperature**: MEDIUM · Fix-or-Refund exposure is real but bounded
- **probability_of_close**: HIGH · the Fix-or-Refund clause is the killer sales line
- **evidence_strength**: HIGH · every DefendableJelly invoice cites the underlying anchored receipts
- **cost_to_mint**: MEDIUM · cost is the refinery run + the deed mint + the weekly receipt overhead

## Deed / Receipt Impact

- **Receipt fields touched**: `customer_id` · `tier` · `weekly_lift_aggregate` · `royal_jelly_record_ids` · `sla_status`
- **DDEED class impact**: parent class · binds many DDEED-DOV-REPAIR children · issued weekly as DDEED-DOV-DEFENDABLE-JELLY-WEEKLY-<customer>-<week>
- **Books and records layer**: L1 PostgreSQL → L4 Hedera HCS → L5 ENS (customer-resolvable at `<customer>.customers.defendable.eth`)
- **5 Proofs touched**: PROCESS (the week's refinery lineage) · QUALITY (the aggregate lift) · ECONOMICS (the invoice line) · TRUST (customer-countersigned weekly receipt)

## Related Terms

- [swarmfixer](swarmfixer.md) · the refinery underneath the brand
- [swarmjelly](swarmjelly.md) · the model underneath the refinery
- [repair-lift](repair-lift.md) · the dial the brand promises
- [pair-candidate](pair-candidate.md) · the unit flowing through the product
- [defendableos](../defendableos_terms/defendableos.md) · the parent platform

## Example

> **Customer**: RegionalInsurer · mid-market P&C carrier · 40-agent fleet in production
>
> **Contract**: Embedded tier · $180K ARR · 90-day Fix-or-Refund · lift target 0.15 on the claims-triage agent fleet
>
> **Product surface**: dashboard tile says "DefendableJelly" · invoice line says "DefendableJelly · Embedded · 12 weeks" · weekly receipts say "DefendableJelly Weekly Lift Receipt · Week of 2026-05-17"
>
> **Internal stack**: SwarmFixer refinery runs nightly · SwarmJelly-4B v1.2 inference at whale:11434 · 47 Royal Jelly Records produced this week · 41 cleared validator · 6 routed to quarantine
>
> **Week-7 receipt**: aggregate lift = +0.21 (over target) · customer countersigned · refund clock disarmed for this period
>
> **Day-90 outcome**: cumulative lift 0.23 · contract auto-renews at $240K ARR · refund not invoked

## DefendableOS Notes

- DefendableJelly is the FIRST DefendableOS product with a falsifiable, refundable SLA · this is the moat
- The 3-name discipline (DefendableJelly external · SwarmFixer internal · SwarmJelly model) keeps the brand surface clean and the engineering surface honest
- DefendableJelly is sold to ownership · not procurement · not engineering · the customer who signs is the CFO or the COO with PnL exposure on AI failures

🐝 *The brand is the receipt. DefendableJelly · refundable lift on the AI you already have.*
