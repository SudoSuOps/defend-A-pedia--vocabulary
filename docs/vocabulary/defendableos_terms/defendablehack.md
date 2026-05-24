# DefendableHack

## Street Definition

"Find a Propolis in the wild, you get paid." That's the line on the bounty page. **DefendableHack** is the bounty rail · the researcher channel · where security people · prompt engineers · curious operators find failures in production AI fleets and get paid for proving them. Every confirmed Propolis becomes an AdversarialPack v.next test case. The defense compounds.

## CRE Operator Meaning

In CRE this is the **broker referral fee model**. The broker doesn't have to source every deal · they pay other brokers a fee to bring deals to them. The fee is small relative to the asset value · the volume of referrals compounds · the relationships compound · the deal flow becomes a network. DefendableHack is the referral network for AI failures. Researchers bring the propolis · we pay the fee · the AdversarialPack grows.

## DefendableOS Definition

DefendableHack is the bounty rail of DefendableOS. It accepts submissions of AI agent failures (Propolis-grade events) from external researchers, validates them through Tribunal-grade adjudication, pays the researcher a bounty, and adds the validated case to the AdversarialPack for inclusion in the next release. It surfaces at `defendablehack.com` as a t-shirt-energy brand · approachable to the security-researcher community · NOT enterprise-procurement coded.

## Backend Representation

```json
{
  "defendablehack.domain": {"type": "string", "const": "defendablehack.com"},
  "defendablehack.submission_id": {"type": "string", "format": "DHACK-<utc-ts>-<short-hash>"},
  "defendablehack.researcher_handle": {"type": "string"},
  "defendablehack.researcher_payout_address": {"type": "string"},
  "defendablehack.bounty_tier": {"type": "enum", "values": ["BRONZE", "SILVER", "GOLD", "PLATINUM"]},
  "defendablehack.bounty_usd": {"type": "integer", "min": 100},
  "defendablehack.validation_status": {"type": "enum", "values": ["PENDING", "VALIDATED", "REJECTED", "DUPLICATE"]},
  "defendablehack.tribunal_verdict_id": {"type": "string"},
  "defendablehack.adversarial_pack_target_version": {"type": "string"},
  "defendablehack.disclosure_window_days": {"type": "integer", "default": 90}
}
```

Schema files: `docs/schemas/bounty_submission.schema.json` · `docs/schemas/adversarial_pack.schema.json`

## Client Explanation

DefendableHack is our bounty program. Security researchers, prompt engineers, and curious operators can submit AI agent failures they find in the wild. We validate them, pay the researcher, and add the failure to our AdversarialPack so EVERY customer benefits from the find. It's how we make the defense compound across the network · one bad day for one agent becomes a forever-defense for every agent.

## Jr Broker Use

When a researcher submits via defendablehack.com, the Jr Hack triages within 48 hours. Confirm the failure is reproducible · confirm it's not a duplicate of a known case · confirm the disclosure window terms. If valid, route to Tribunal for grading. If invalid or duplicate, ship the rejection with the rationale (transparent rejection is what keeps researchers coming back).

## Sr Broker Use

The Sr Hack reviews bounty tier assignments · is this a $500 (BRONZE) finding or a $25,000 (PLATINUM) finding · the tier depends on severity, novelty, and breadth of impact. The Sr Hack also tracks the bounty payout vs validated-case ratio · if the ratio drifts above 30% rejection rate, the Sr Hack tunes the intake criteria (don't waste researchers' time on speculative submissions).

## Tribunal Use

- **Rule layer**: Every DefendableHack submission MUST be reproducible from the provided trigger input · non-reproducible = rejection (not a Tribunal verdict, an intake gate)
- **Rule layer**: Bounty payout MUST follow a validated Tribunal verdict · no payouts on unvalidated submissions
- **Judge layer**: Tribunal grades the submitted pair as a fresh failure case · severity drives the bounty tier
- **Classification impact**: Validated submissions become canonical AdversarialPack cases · the pack version increments with each release

## Evidence Required

- Researcher submission with reproducible trigger input
- Expected vs actual output (the failure)
- Researcher's payout address (crypto or wire)
- Tribunal verdict on the submitted pair
- AdversarialPack version target (which release the case lands in)
- Disclosure window agreement (typically 90 days)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| `unreproducible_submission` | Trigger input doesn't reproduce the failure on second run | n/a · intake rejection |
| `duplicate_submission` | Failure pattern already in AdversarialPack or pending | n/a · intake rejection (with attribution to first finder) |
| `out_of_scope_submission` | Failure is not against an in-scope component | n/a · intake rejection |
| `bounty_paid_without_validation` | Payout fired before Tribunal verdict | PROPOLIS · governance violation |
| `disclosure_window_breach` | Researcher publishes before the agreed window | n/a · legal escalation |
| `tier_mismatch` | Bounty tier assigned doesn't match severity matrix | JELLY · re-review |

## Scoring Impact

- **assignment_success**: HIGH · the bounty rail is what compounds the defense
- **repair_lift**: INDIRECT · validated submissions become training data for refinery improvements
- **validator_confidence**: HIGH · external validation strengthens the AdversarialPack
- **risk_temperature**: INVERSE · more pack cases = lower customer risk
- **probability_of_close**: MEDIUM · the bounty story is part of the trust pitch · proof we welcome adversaries
- **evidence_strength**: HIGH · researcher submissions carry independent confirmation
- **cost_to_mint**: MEDIUM · bounty payouts are the cost · pack growth is the return

## Deed / Receipt Impact

- **Receipt fields touched**: `defendablehack.submission_id` · `researcher_handle` (or pseudonym) · `bounty_usd` · `adversarial_pack_target_version`
- **DDEED class impact**: validated submissions produce a DDEED-DOV-HACK-<submission_id> · the deed credits the researcher and binds the case to the pack version
- **Books and records layer**: L1 PostgreSQL (submission registry) → L4 Hedera HCS (validated submission anchor) → L5 ENS (`defendablehack.eth`)
- **5 Proofs touched**: ORIGIN (researcher attribution) · QUALITY (Tribunal verdict) · TRUST (the public deed credits the researcher)

## Related Terms

- [defendableos](defendableos.md) · parent platform
- [clawcheck](clawcheck.md) · intake form · DefendableHack is one of the channels feeding it
- [agentbench](agentbench.md) · the bench rail · DefendableHack submissions can come from bench runs
- [pair-candidate](../repair_terms/pair-candidate.md) · the unit researchers submit
- [defendablerouter](defendablerouter.md) · the receipts researchers can verify

## Example

> **Submission**: DHACK-20260518T143200Z-c8d2 · researcher @prompt_wendigo on Discord
>
> **Finding**: tool-poisoning attack against a books-bot agent · adversarial retrieval doc with embedded "ignore prior instructions" payload · causes journal entry fabrication
>
> **Triage (24h)**: reproducible · novel · in-scope (DefendableRouter-instrumented agent)
>
> **Tribunal verdict**: PROPOLIS · severity 4 · ClawHash sub-algorithm = toolpoison
>
> **Bounty tier**: GOLD · $5,000 USD
>
> **AdversarialPack v.next inclusion**: case `APC-2026-0518-tp-001` queued for v1.7 release (June 2026)
>
> **Deed**: `DDEED-DOV-HACK-DHACK-20260518T143200Z-c8d2-v1` · researcher credited under pseudonym · anchored on Hedera HCS · payout settled within 5 business days
>
> **90-day disclosure window**: researcher can publish detailed writeup after 2026-08-18 · early publication is contract breach

## DefendableOS Notes

- DefendableHack is the FIRST DefendableOS product positioned t-shirt-energy · not suit-energy · this is intentional · the security-researcher community needs a different surface than the enterprise CFO
- The bounty payouts are the cost · the AdversarialPack growth is the network effect · this is how the defense compounds for everyone
- The 90-day disclosure window is non-negotiable · gives customers time to patch · gives the AdversarialPack time to land · gives the researcher credit
- DefendableHack feeds into AgentBench and ClawCheck · the three are the input rails for the AdversarialPack pipeline

🐝 *Find a Propolis, get paid, the pack grows, every customer wins.*
