# DefendableOS

## Street Definition

"What do you build?" "DefendableOS." That's the founder's answer at every CRE-broker happy hour, every angel pitch, every customer intro. **DefendableOS** is the public-facing brand for the defense layer of the AI economy. Inside the building we call it the Swarm & Bee backend · in the marketplace we call it DefendableOS. One product surface. One trust contract. One brand.

## CRE Operator Meaning

In CRE, the brand is the listing. The listing is what the buyer reads. Behind the listing is the operating company · the asset management team · the construction crew · the leasing brokers · the property accountants. The buyer doesn't care about the org chart · they care about the asset. DefendableOS is the asset. Swarm & Bee is the org chart behind it. The customer never sees the org chart · they see the building.

## DefendableOS Definition

DefendableOS is the public-facing brand and consumer-facing product layer for the entire defense stack. It binds DefendableRouter (capture middleware) + SwarmFixer/DefendableJelly (the agent refinery) + DefendableHack (the bounty rail) + DefendableCloud (the hosted-inference rail) + HoneyBox (the edge appliance) + ClawCheck (the intake) + AgentBench (the bench) into one consumable platform. The internal backend (Swarm & Bee) builds and operates it · DefendableOS is what the customer signs for, pays for, and references in their AP system.

## Backend Representation

```json
{
  "defendableos.product_id": {"type": "string", "const": "defendableos"},
  "defendableos.surface_domains": {
    "type": "array",
    "default": [
      "defendableos.com",
      "defendablerouter.com",
      "defendablecloud.com",
      "defendablehack.com",
      "defendableos.eth",
      "swarmbee.defendable.eth"
    ]
  },
  "defendableos.internal_backend": {"type": "string", "const": "swarm_and_bee"},
  "defendableos.legal_entity": {"type": "string", "const": "Swarm and Bee LLC DBA Swarm & Bee AI"},
  "defendableos.duns": {"type": "string", "const": "138652395"},
  "defendableos.product_components": {
    "type": "array",
    "default": ["DefendableRouter", "DefendableJelly", "DefendableHack", "DefendableCloud", "HoneyBox", "ClawCheck", "AgentBench"]
  }
}
```

Schema files: `docs/schemas/brand_registry.schema.json` · `docs/schemas/product_offering.schema.json`

## Client Explanation

DefendableOS is the defense layer for your AI fleet. Your agents do the offense (the actual work). DefendableOS captures every call, grades it, fixes the weak ones, surfaces the failures, and anchors the receipts. We're not an AI agent vendor · we don't sell the brains. We sell the defense around the brains you already bought. Five-minute install at the edge. Sub-5ms latency overhead. Receipts you can verify on a public chain.

## Jr Broker Use

When you talk to a customer, you talk DefendableOS. NEVER Swarm & Bee in customer-facing surfaces · that's the org chart, not the listing. Use DefendableOS in: the LOU, the dashboard, the invoice, the slide deck, the press release. Use Swarm & Bee in: internal Slack, the operator's flightsheet, the engineering wiki, the model registry.

## Sr Broker Use

The Sr Hack ensures the brand discipline holds across every surface · marketing site copy · sales decks · customer onboarding emails · API documentation · runtime dashboards. A single page that says "Swarm & Bee" instead of "DefendableOS" confuses the buyer about who they're paying. Sr Hack audits the brand monthly · catches drift before it ships.

## Tribunal Use

- **Rule layer**: Customer-facing deliverables MUST cite "DefendableOS" not "Swarm & Bee" (brand compliance check)
- **Rule layer**: Component product names (DefendableRouter · DefendableJelly · etc.) MUST match the canonical list · no aliases in customer surfaces
- **Judge layer**: Tribunal doesn't grade brand directly · it grades the deliverable's overall coherence · brand confusion is a coherence failure
- **Classification impact**: Customer-facing artifact with brand drift drops to JELLY pending marketing review

## Evidence Required

- Legal entity registration (Swarm and Bee LLC · Florida)
- D-U-N-S number (138652395)
- Canonical product component list
- Surface-domain registry (the 5-6 domain ENS bridges)
- Brand-discipline audit log (monthly review)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `internal_brand_in_customer_surface` | Customer-facing artifact says "Swarm & Bee" instead of "DefendableOS" | JELLY · marketing audit |
| `component_alias_drift` | Component referred to by an internal codename in customer surface | JELLY · marketing audit |
| `unregistered_component_claim` | Customer offering refers to a component not in the canonical list | PROPOLIS · governance violation |
| `legal_entity_drift` | Contract cites a non-canonical legal entity | PROPOLIS · contract escalation |

## Scoring Impact

- **assignment_success**: HIGH · brand integrity IS the customer's mental model
- **repair_lift**: NEUTRAL · brand is upstream of refinery operations
- **validator_confidence**: HIGH · brand consistency IS a trust signal
- **risk_temperature**: INVERSE · clean brand = clean accountability chain
- **probability_of_close**: HIGH · one brand to remember · easier to sign
- **evidence_strength**: HIGH · canonical brand registry is the source of truth
- **cost_to_mint**: NEUTRAL

## Deed / Receipt Impact

- **Receipt fields touched**: every deed cites `issuing_party: defendableos` · backed by `legal_entity: Swarm and Bee LLC`
- **DDEED class impact**: all DDEED classes are scoped under the DefendableOS brand · the receipt-clause license is held by the legal entity
- **Books and records layer**: L1 PostgreSQL (brand registry) → L4 Hedera HCS (canonical surface list anchor) → L5 ENS (defendableos.eth)
- **5 Proofs touched**: TRUST (the brand and legal entity backing every receipt) · ORIGIN (the issuing party on every deed)

## Related Terms

- [defendablerouter](defendablerouter.md) · the capture middleware component
- [defendablecloud-com](defendablecloud-com.md) · the cloud-inference component
- [defendablehack](defendablehack.md) · the bounty rail component
- [honeybox](honeybox.md) · the edge appliance component
- [clawcheck](clawcheck.md) · the intake component
- [agentbench](agentbench.md) · the bench rail component
- [defendablejelly](../repair_terms/defendablejelly.md) · the repair-layer brand

## Example

> **Customer-facing surface (correct)**: "We deployed DefendableOS at the edge of RegionalInsurer's claims-triage stack · the DefendableRouter captures all 40 agent calls per second · DefendableJelly refines the JELLY-grade outputs · weekly receipts anchored on DefendableOS.eth."
>
> **Customer-facing surface (incorrect · drift)**: "Swarm & Bee's SwarmFixer service refined the claims-triage agent outputs."
>
> **Internal surface (correct)**: "SH4 ran the SwarmFixer refinery on the JELLY batch · SwarmJelly-4B at whale:11434 · TEMP=0.05 · 47 Royal Jelly Records produced."

## DefendableOS Notes

- The brand quintet is LOCKED · 5 audience surfaces (defendableos.com · defendablerouter.com · defendablecloud.com · defendablehack.com · defendthehive related)
- The customer NEVER sees the Swarm & Bee name in production · this is intentional · the brand surface is DefendableOS · the operating company is Swarm & Bee LLC
- DefendableOS is the LISTING · Swarm & Bee is the BROKERAGE · the customer signs with the listing · the brokerage is the org chart behind it

🐝 *DefendableOS is what the customer signs. Swarm & Bee is who runs the building.*
