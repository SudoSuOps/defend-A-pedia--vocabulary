# 10 · Receipts · Deeds · and Books and Records

> *"Title insurance is the only reason CRE works at scale. You hand over $50M because a third party guarantees the paper. We're building the title insurance layer for AI."*
>
> — Founder · on the deal physics · 2026-05-24

---

## Why this doctrine exists

Commercial real estate runs on paper. The deed is the deed. The closing statement is the closing statement. The title insurance is the title insurance. Every party in the chain · buyer · seller · lender · title company · escrow agent · county recorder · has a copy of the same document. The document survives the parties. The document IS the asset.

AI today runs on screenshots. "Trust me · my agent did this." Receipts that vanish when the browser tab closes. Logs that get rotated out at 30 days. Vendor dashboards that the vendor can rewrite. No deeds. No books. No records. No survivability.

DefendableOS exists to build the books-and-records layer that AI work has never had. This doctrine is the spec for that layer.

It answers three questions:

1. **What is the difference between a receipt · a deed · and a books-and-records entry?**
2. **What are the 5 Proofs every deed carries · and why?**
3. **What is the 5-layer finality stack · and why does it matter?**

---

## The pipeline

```
AI agent does work
        ↓
RECEIPT issued (per task · cheap · always)
        ↓
Tribunal grades the work
        ↓
DEED issued (if it qualifies · per task · gated)
        ↓
BOOKS-AND-RECORDS entry (5-layer finality)
        ↓
Principal trusts the work because the books survive any single party
```

Every layer is defendable on its own. The compounding is what makes the trust durable.

---

## Receipts

A **Receipt** is the lightweight per-task record an agent produces every time it does a thing. Receipts are cheap · automatic · written by default · NEVER optional. The router writes receipts inline · the agent doesn't have to ask.

A receipt carries the minimum metadata to reconstruct the task:

| Field | Type | Purpose |
|---|---|---|
| `receipt_id` | string · `DCLAW-{cell_hash}-{timestamp}` | Unique identifier |
| `agent_id` | string · ENS subdomain | Which agent did the work |
| `task_class` | enum | What kind of task (refund_decision · cre_underwriting · etc) |
| `model` | string + version | Which model produced the output |
| `input_hash` | sha256 | What went in |
| `output_hash` | sha256 | What came out |
| `wall_time_ms` | int | How long it took |
| `cost_to_mint_usd` | float | What it cost (per the cost-to-mint doctrine) |
| `tribunal_status` | enum | `PENDING` · `HONEY` · `JELLY` · `PROPOLIS` (initially PENDING) |
| `created_at` | timestamp | When |

Receipts are written to PostgreSQL L1 in real-time · synced to NAS L3 nightly · NEVER ANCHORED individually (that would be cost-prohibitive). They're the raw operating ledger.

**Receipts are NOT deeds.** A receipt says "this task ran." A deed says "this task ran AND survived the Tribunal AND meets the 5 Proofs AND is filed in books-and-records." The promotion path is gated.

---

## Deeds

A **Defendable Agent Deed** (DDEED) is a receipt that has been graded · classified · receipted across all 5 Proofs · anchored on Hedera HCS · and resolved via ENS. A deed is the unit the principal trusts. A deed is the unit the auditor inspects. A deed is the unit the books-and-records entry inherits from.

Not every receipt becomes a deed. Receipts that grade PROPOLIS are filed (for SwarmFixer training) but NEVER issued as deeds. Receipts that grade JELLY are repair candidates (also filed · also not yet issued). Only HONEY and Royal Jelly receipts qualify for deed issuance.

A deed carries everything a receipt carries · plus:

| Field | Type | Purpose |
|---|---|---|
| `ddeed_id` | string · `DDEED-{org}-{class}-{slug}-{seq}-v{n}` | Permanent identifier |
| `parent_receipt_id` | string | Backlink to originating receipt |
| `tribunal_verdict` | enum · HONEY / ROYAL_JELLY | Promoted classification |
| `tribunal_score_composite` | float 0-1 | The weighted score |
| `validator_chain_pass_count` | int (0-12) | How many of the 12 checks passed |
| `merkle_batch_id` | string | Which batch of 50 it joined for L2 |
| `hedera_topic_id` | string · `0.0.10291838` | The HCS topic where it's anchored |
| `hedera_consensus_timestamp` | timestamp | When the anchor finalized |
| `ens_resolution_path` | string · `{ddeed-id}.{org}.defendable.eth` | Public resolution |
| `proof_origin` | object | Model · node · hardware · strategy |
| `proof_quality` | object | Deterministic checks · gate results |
| `proof_process` | object | Lineage · attempts · what survived |
| `proof_economics` | object | Energy · token cost · CFO line item |
| `proof_trust` | object | HCS anchor · Merkle root · verifier instructions |

The deed is the canonical record. The deed is what gets cited in a closing statement. The deed is what survives a vendor change · a team rotation · a litigation discovery request.

---

## The 5 Proofs

Every deed must carry all 5 Proofs. Missing any one Proof cancels the deed issuance · the receipt stays a receipt · the work is filed but not certified.

### Proof of Origin

**Question answered**: *Where did this work come from?*

Fields: model name · model version · model fingerprint hash · serving node hostname · hardware identifier (anonymized device class · NEVER serial numbers in public payload) · routing strategy.

CRE analog: *the seller's deed conveying title · provenance of the asset back through the chain of ownership.*

### Proof of Quality

**Question answered**: *Was the work good?*

Fields: validator chain results (12 checks · pass/fail per check) · Tribunal composite score · drift between Scale A and Scale B judges · adversarial pack pass rate · per-gate evidence weights.

CRE analog: *the appraisal · the engineering report · the environmental assessment · the deterministic verification that the asset is what the seller says it is.*

### Proof of Process

**Question answered**: *How did the work get done?*

Fields: HoneyCard `factory_path` · attempt count · failed attempts (counted · not hidden) · repair attempts (if any) · routing decisions · escalation triggers fired · the full lineage from input to final output.

CRE analog: *the chain of title · every transfer · every easement · every encumbrance ever recorded against the property.*

### Proof of Economics

**Question answered**: *What did the work cost?*

Fields: `cost_to_mint_usd` · `energy_kwh` · `token_count_input` · `token_count_output` · `wall_time_ms` · per-component cost breakdown referencing the published formula.

CRE analog: *the closing statement line items · the HUD-1 · the per-dollar accounting that lets the buyer and seller agree the trade pencils.*

### Proof of Trust

**Question answered**: *Who else can verify this without trusting us?*

Fields: Hedera HCS topic ID · consensus timestamp · message hash · Merkle root for the L2 batch · ENS resolution path · verifier instructions (copy-paste-runnable curl or web query).

CRE analog: *the title insurance policy · the county recorder entry · the independent third party who guarantees the paper without needing to trust either side of the trade.*

The 5 Proofs together are what make a deed defendable. Pull any one and the deed is a claim. Stack all 5 and the deed is an attestation.

---

## The 5-layer finality stack

Books-and-records is not a database. It's a 5-layer finality stack where each layer's role is calibrated against the failure modes of the layer below it.

### L1 · PostgreSQL · hot queries

The operating database. Receipts and deeds written in real-time. Mutable by design (the system needs to grade · classify · annotate). 1.5M+ pairs at present count. Sub-second query latency.

**Failure mode it covers**: live operations · the principal's dashboard · the operator's pit · the validator's adjudication.

**Failure mode it has**: mutable · anyone with DB access can rewrite history.

### L2 · Merkle trees · SHA-256 batches

Every 50 deeds get hashed into a Merkle tree · root computed · root written to a separate immutable log. Now the database can lie · but the lie won't match the root. Tampering detectable.

**Failure mode it covers**: silent corruption · disgruntled-insider rewrite · accidental migration error.

**Failure mode it has**: the root is just a number · still needs an independent storage location.

### L3 · NAS archive

Every Merkle root + every batch of 50 underlying deeds gets written to the owned NAS at `/mnt/swarm/swarmdeed-finality/` · sustained 50 MB/s · 3x redundancy · offsite snapshot weekly. Owned hardware · operator-controlled · no cloud dependency.

**Failure mode it covers**: vendor lock-in · cloud account suspension · ransom or extortion attempts on the operating system.

**Failure mode it has**: physical location · operator failure (fire · flood · seizure).

### L4 · Hedera HCS mainnet

Every Merkle root · every deed manifest · gets anchored to Hedera HCS topic `0.0.10291838` on mainnet. Consensus timestamp signed by 39 globally-distributed council nodes. Not theoretically immutable · mathematically immutable (no party can rewrite without compromising the council).

**Failure mode it covers**: operator failure · operator dishonesty · operator disappearance.

**Failure mode it has**: depends on Hedera mainnet continuing to operate (long-tail risk · same class as US treasury bond risk).

### L5 · ENS domains

14 ENS domains registered (defendable.eth · swarmbee.defendable.eth · swarmdeed.eth · etc). Every deed resolves to a permanent path: `{ddeed-id}.{org}.defendable.eth`. The path survives our hosting · our company · our DNS.

**Failure mode it covers**: company shutdown · brand pivot · 30-year-from-now research access.

**Failure mode it has**: depends on Ethereum mainnet · ENS protocol survival · same long-tail class.

The 5 layers together are what make books-and-records survive every failure mode short of civilizational collapse. The principal can verify a 2026 deed in 2046 by walking the ENS path · pulling the Hedera anchor · re-deriving the Merkle root from the NAS snapshot. Every layer is the backstop for the layer above it.

---

## Why books-and-records IS the trust layer

A vendor without books-and-records is a vendor whose claims expire with the contract. The day the relationship ends · the receipts are gone · the dashboard goes dark · the principal has no defense if a regulator · an auditor · a litigant comes asking.

A vendor WITH books-and-records is a vendor whose work survives the relationship. The deeds resolve · the anchors verify · the principal can produce a 2026 deed in a 2030 deposition without needing the vendor to still exist.

That's the trust layer. Not features. Not uptime. Not even price. The books-and-records layer is the only thing that converts AI work from "vendor magic" into a defendable producing asset.

It's also the only thing that makes the **Defendable Work Unit Deed** possible · the trinity of (compute deed + agent deed + economic opinion) that becomes a single issuable record. That deed is what regulated industries (healthcare · finance · legal) will eventually require. We built the books-and-records layer first so the Work Unit deed has somewhere to live.

---

## The relationship to vocabulary

This is why **every vocabulary term in this repo has a "Deed / Receipt Impact" section.** No exceptions. A term that doesn't touch a receipt · a deed · or a books-and-records entry doesn't belong in the operating constitution.

The schema follows the language. The deed inherits the schema. The books-and-records entry inherits the deed. The principal trusts the books. The trust loop closes because the vocabulary is constitutional · not decorative.

---

## How this plugs into the rest of the doctrine

- **Honey · Royal Jelly · Jelly · Propolis** ([07_honey_royal_jelly_propolis.md](07_honey_royal_jelly_propolis.md)) · the classification system that gates receipt-to-deed promotion.
- **Tribunal Doctrine** ([08_tribunal_doctrine.md](08_tribunal_doctrine.md)) · the adjudication system that produces the verdicts.
- **Energy and Cost to Mint** ([09_energy_and_cost_to_mint.md](09_energy_and_cost_to_mint.md)) · Proof of Economics field source.
- **Validator Chain Doctrine** ([13_validator_chain_doctrine.md](13_validator_chain_doctrine.md)) · Proof of Quality field source.
- **Assignment Success Doctrine** ([14_assignment_success_doctrine.md](14_assignment_success_doctrine.md)) · the deed-level rollup into assignment-level reporting.

---

## Related terms

- [receipt](../vocabulary/minting_terms/receipt.md)
- [deed](../vocabulary/minting_terms/deed.md)
- [ddeed](../vocabulary/minting_terms/ddeed.md)
- [closing-statement](../vocabulary/client_terms/closing-statement.md)
- [letter-of-understanding](../vocabulary/client_terms/letter-of-understanding.md)
- [morning-brief](../vocabulary/client_terms/morning-brief.md)
- [cost-to-mint](../vocabulary/minting_terms/cost-to-mint.md)

🐝 *Books-and-records is what survives the relationship. The receipts are the evidence. The deeds are the title. The principal trusts what the books say.*
