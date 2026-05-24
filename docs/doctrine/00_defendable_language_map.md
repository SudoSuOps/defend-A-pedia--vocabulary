# The Defendable Language Map

> *"CRE language becomes DefendableOS language. DefendableOS language becomes schema. Schema becomes scoring. Scoring becomes receipts. Receipts become deeds. Deeds become books and records. Books and records become trust."*

> *"We speak first · then we have the receipts to back it up. That's DefendableOS."*
> — Founder · 2026-05-24

This is the master pipeline. Every term in this repo participates in it. Every schema. Every doctrine. Every playbook.

**The Communicator LLM** (see [`16_communicator_doctrine.md`](16_communicator_doctrine.md)) sits as a bookend at BOTH ENDS of the pipeline · translating between human conversation and structured action at INTAKE · and between structured result and human explanation at OUTPUT. Every step below is bracketed by Communicator translation.

---

## The 10-step pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│  1. CRE STREET LANGUAGE                                              │
│  ──────────────────────────────────────────────────────────────────  │
│  "What's the color on the asset?"                                    │
│  "Did the digest pencil?"                                            │
│  "Who's repping the seller?"                                         │
│  "What's our probability of close?"                                  │
│  "Are we in the buyer pool or out?"                                  │
│  "Did they sign the LOI?"                                            │
│  "What's the books-and-records story?"                               │
│                                                                       │
│  Source · the founder · 30 years of CRE deal flow                    │
│  Preserved · in every term file under docs/vocabulary/cre_terms/     │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  2. DEFENDABLE VOCABULARY                                            │
│  ──────────────────────────────────────────────────────────────────  │
│  Every CRE term is mapped to its DefendableOS analog · WITHOUT       │
│  losing the street meaning. Both definitions live side-by-side       │
│  in the same term file.                                              │
│                                                                       │
│  Example mappings:                                                   │
│    color           → "what we know about the asset · verified"       │
│    digest          → "the pre-meeting summary the agent prepares"    │
│    LOI             → "Letter of Understanding · client sign-off"     │
│    probability     → "the close-probability dial on the UI"          │
│    of close                                                          │
│    deal flow       → "the pipeline · jobs by stage"                  │
│                                                                       │
│  Lives in · docs/vocabulary/{14 category subdirs}                    │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  3. BACKEND FIELDS                                                   │
│  ──────────────────────────────────────────────────────────────────  │
│  Every term has a Backend Representation section that names:         │
│    · the field name(s)                                               │
│    · the data type(s)                                                │
│    · the enum values (if applicable)                                 │
│    · the schema location                                             │
│    · the scoring hook (if applicable)                                │
│                                                                       │
│  Example:                                                            │
│    color         → asset.color_status (enum: VERIFIED, PARTIAL,      │
│                    UNVERIFIED, MISSING)                              │
│    digest        → engagement.digest_v1 (jsonb)                      │
│    LOI           → engagement.lou_signed_at (timestamp)              │
│    probability   → engagement.probability_of_close (float 0-1)       │
│                                                                       │
│  Schemas live · docs/schemas/{14 .schema.json files}                 │
│  Field map · data/backend_field_map.jsonl                            │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  4. TRIBUNAL SCORING                                                 │
│  ──────────────────────────────────────────────────────────────────  │
│  Every term that affects an output is scored by the Tribunal:        │
│                                                                       │
│  Scoring dials (per docs/ui_dials/):                                 │
│    · Probability of Close (0-1)                                      │
│    · Assignment Success (Honey/Jelly/Propolis)                       │
│    · Repair Lift (Δ score before vs after)                           │
│    · Validator Confidence (0-1)                                      │
│    · Evidence Strength (0-1)                                         │
│    · Risk Temperature (low/medium/high)                              │
│    · Cost to Mint ($/deed)                                           │
│                                                                       │
│  Tribunal config: Scale A gemma3:12b + Scale B qwen2.5:32b           │
│  Protocol: 2-pass · drift ≤ 0.15 · rule-then-judge                   │
│  Throughput: 777 pairs/hr · 24/7 (per swarm-wiki dashboard)          │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  5. HONEY · ROYAL JELLY · JELLY · PROPOLIS CLASSIFICATION            │
│  ──────────────────────────────────────────────────────────────────  │
│  Every Tribunal verdict drops into a class:                          │
│                                                                       │
│    Royal Jelly   ≥ 0.85   Apex · production-grade · deed-ready       │
│                            (or 95+ in apex-only variant)             │
│    Honey         0.70+    Production-safe · validator-approved       │
│    Jelly         repair   Recoverable failure · repair-candidate     │
│                  candidate   (the gold for SwarmFixer training)      │
│    Propolis      critical Adversarial · hallucinated · trust-break   │
│                                                                       │
│  Class system maps to CRE asset grading:                             │
│    Class A · Royal Jelly · prime location · irreplaceable            │
│    Class B · Honey · decent · adequate · replaceable                 │
│    Class C · Propolis · bad neighborhood · hallucinations            │
│                                                                       │
│  Doctrine · 07_honey_royal_jelly_propolis.md                         │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  6. RECEIPTS + DDEED                                                 │
│  ──────────────────────────────────────────────────────────────────  │
│  Every output that survives the Tribunal is receipted and (when      │
│  it qualifies) issued as a DDEED.                                    │
│                                                                       │
│  Receipt fields (per docs/schemas/deed_receipt.schema.json):         │
│    · receipt_id           DCLAW-{cell_hash}-{timestamp}              │
│    · agent_id             ENS subdomain (agent.op.defendable.eth)    │
│    · task_class           e.g., refund_decision · cre_underwriting   │
│    · model + version                                                 │
│    · tribunal_verdict     HONEY · JELLY · PROPOLIS                   │
│    · jellyscore           0-100                                      │
│    · record_hash          sha256 of canonical JSON                   │
│    · cost_to_mint_usd     per cost_to_mint.schema.json               │
│                                                                       │
│  DDEED issuance (per glass-wall · 5 proofs):                         │
│    1. Proof of Origin (which model · node · hardware)                │
│    2. Proof of Quality (JellyScore · 6 gates + 7th adversarial)      │
│    3. Proof of Process (HoneyCard factory_path)                      │
│    4. Proof of Economics (cost-to-mint · energy)                     │
│    5. Proof of Trust (Hedera HCS anchor · Merkle root)               │
│                                                                       │
│  Anchored · Hedera HCS topic 0.0.10291838                            │
│  Resolved · {ddeed-id}.{org}.defendable.eth                          │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  7. BOOKS AND RECORDS                                                │
│  ──────────────────────────────────────────────────────────────────  │
│  Every receipt and deed lands in books-and-records · 5-layer         │
│  finality stack:                                                     │
│                                                                       │
│    L1 PostgreSQL · hot queries · mutable · 1.5M+ pairs               │
│    L2 Merkle trees · SHA256 · batches of 50                          │
│    L3 NAS archive · /mnt/swarm/swarmdeed-finality/                   │
│    L4 Hedera HCS mainnet · immutable · topic 0.0.10291838            │
│    L5 ENS domains · 14 registered · permanent resolution             │
│                                                                       │
│  Doctrine · 04_books_and_records_doctrine.md                         │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  8. CLIENT TRUST LAYER                                               │
│  ──────────────────────────────────────────────────────────────────  │
│  Every term has a Client Explanation section · the language          │
│  ownership speaks. This is what gets surfaced in:                    │
│                                                                       │
│    · the pre-market flight sheet (broker → client)                   │
│    · the Letter of Understanding (signed engagement)                 │
│    · the Morning Reconciliation Brief (06:00 daily email)            │
│    · the Defendable Closing Statement (variance report)              │
│    · the Title Insurance receipt (score guarantee ±0.15)             │
│                                                                       │
│  Tone · CRE 5-cap mindset · CFO-readable · NOT engineer-shaped       │
│  Doctrine · 05_client_language_doctrine.md                           │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  9. SWARMFIXER TRAINING DATA                                         │
│  ──────────────────────────────────────────────────────────────────  │
│  Every JELLY-verdict pair feeds SwarmFixer's training corpus.        │
│  Every term in this repo becomes a training signal.                  │
│                                                                       │
│  5 RJ tasks per failure (per pipeline_swarmjelly.py):                │
│    DIAGNOSE  · what went wrong · root cause · severity (1-5)         │
│    REPAIR    · step-by-step recovery + corrected output              │
│    PREVENT   · trigger_condition · check_logic · remediation         │
│    DETECT    · POSITIVE/NEGATIVE · confidence · evidence             │
│    COMPARE   · ranked + scored (correctness · completeness)          │
│                                                                       │
│  7 failure modes (with 25% distribution cap each):                   │
│    missing_step · false_assumption · hallucination ·                 │
│    overgeneralization · drift · schema_break · tool_misuse           │
│                                                                       │
│  Doctrine · 11_swarmfixer_doctrine.md                                │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  10. FUTURE DEFENDABLEOS INTELLIGENCE                                │
│  ──────────────────────────────────────────────────────────────────  │
│  Future models train on the corpus we build today.                   │
│                                                                       │
│  Active cooks: Gemma 4 31B (75% complete · eval_loss 0.5194)         │
│  Fleet: SwarmCurator (27B/9B/2B) · SwarmCapitalMarkets-27B ·         │
│         SwarmJudge-9B-CRE · SwarmJelly-4B · SwarmRouter-v1 ·         │
│         SwarmHoney-27B · SwarmCRE-9B · SwarmAtlas-27B · etc.         │
│                                                                       │
│  Every model that trains on this vocabulary ships the founder's      │
│  voice in its output. That's the moat.                               │
│                                                                       │
│  "The language lives in the blocks."                                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## The bidirectional rule

Every step in this pipeline MUST be traceable in both directions:

- **Forward**: CRE term → vocab entry → schema field → Tribunal score → deed line item
- **Backward**: deed line item → schema field → vocab entry → CRE term → operator meaning

If you can't trace a backend field BACK to the CRE language that birthed it · the field doesn't belong in DefendableOS.
If you can't trace a CRE term FORWARD to a backend field · the term hasn't earned its place in the repo.

This is the structural integrity check. The doctrine rule. The Genesis Law applied to vocabulary.

---

## What this pipeline enables

When the pipeline works end-to-end:

1. A jr broker hears a customer say something in their language · maps it to a CRE term · knows the DefendableOS vocab · knows what data to capture
2. The system records the event with the right schema field · the right scoring hook · the right tribunal class
3. The Tribunal grades the output · drops it in the right class (Honey/Jelly/Propolis)
4. A receipt is issued · a deed is filed · books-and-records are updated
5. The customer gets a Morning Brief that uses their language · explains what happened
6. SwarmFixer trains on any JELLY pairs · the model gets better
7. Future agents speak the founder's voice because the vocabulary trained them

**That's a closed loop.** That's the brick-and-mortar footprint. That's what no other AI defense play has.

---

## Read next

- [`01_language_is_infrastructure.md`](01_language_is_infrastructure.md) · why vocabulary IS schema
- [`02_cre_to_defendableos.md`](02_cre_to_defendableos.md) · the explicit translation table
- [`07_honey_royal_jelly_propolis.md`](07_honey_royal_jelly_propolis.md) · the 4-tier classification spec
- [`08_tribunal_doctrine.md`](08_tribunal_doctrine.md) · the adjudication system

🐝 *The language lives in the blocks.*
