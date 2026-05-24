# Honey · Royal Jelly · Jelly · Propolis · The 4-Tier Classification

> *"Class A · Class B · Class C · and the trash that the city won't even haul. Same logic. Different building."*
> — Founder · on the day we locked the four tiers

---

## What this doctrine is

This is the classification spec. The four tiers a Tribunal verdict can land in. Every output the Hive produces · every pair the validators see · every receipt the Bakery hashes · drops into one of these four buckets. Nothing escapes the grade. Nothing goes ungraded. The grade is the asset.

The four tiers are not opinion. They are not vibes. They are a numeric score plus a rule-layer floor, and the score is produced by a 6-role Tribunal running 24/7 on `gemma3:12b` and `qwen2.5:32b` at 777 pairs/hr. The rule layer can only downgrade · it can never promote. The judge layer can move a pair within a tier or hand it up · it can never override a critical-fail.

This is how we keep the books clean.

---

## The four tiers (4-tier · the production default)

| Tier | Score window | Class equivalent | What it is | What it does in the system |
|---|---|---|---|---|
| **Royal Jelly** | ≥ 0.85 | Class A | Apex · production-grade · deed-ready · the kind of output a sr broker would sign their name to | Eligible for full DDEED issuance · trains the next writer cohort · referenced in the Morning Brief as a flagship |
| **Honey** | 0.70 – 0.84 | Class B | Production-safe · validator-approved · ships to the customer without rework | Receipted · published · used in operating reports · NOT used as training data for the writer (only Royal Jelly is) |
| **Jelly** | repair candidate (typically 0.50 – 0.69 with recoverable failure mode) | Class C · workout candidate | Recoverable failure · the most valuable training data in the Hive · routed to SwarmFixer for repair lift | Held in `pair-candidates/jelly-repaired/` · re-graded after repair · promoted to Honey when fix lands |
| **Propolis** | < 0.70 with critical-fail · OR any score with hallucination_event flag · OR any score with adversarial-source flag | Class C minus · trash heap · "bad neighborhood" | Critical failure · adversarial · hallucinated · trust-break · the deed CANNOT issue | Logged · sealed · NEVER published · feeds the PropolisCollector for SwarmFixer DETECT-task training · "no waste in a Hive" |

The 0.85 floor for Royal Jelly is the **Google Gemma 4 FTW threshold** · more inclusive than the original virgin-jelly apex-only 0.95. We adopted 0.85 because production proved that 55% of medical pairs and 55% of CRE pairs at that threshold survived validator review with zero rework. Lower the bar to 0.95 and you starve the writer fleet · raise it above 0.85 and you ship Honey-grade output as if it were apex. 0.85 is the operator-tested middle.

---

## The 5-tier extension (Genesis vocabulary · used in public surfaces)

The original Swarm-Hive (March 2026 · the genesis repo) defined a 5-tier grade. This is what shows up in the `swarmandbee.ai/chain` glass wall and in any customer-facing comp sheet that needs the full CRE-equivalent ladder.

| Score (0-100) | Tier | What it maps to |
|---|---|---|
| 95+ | **Genesis** | Canonical · DOI-stamped · on-chain · the irreplaceable record · CRE equivalent: trophy asset, single comp in the market |
| 85-94 | **Honey** | Production grade · model-validated · CRE: Class A institutional |
| 70-84 | **Cluster** | Domain-dataset quality · CRE: Class B with stable tenant |
| 50-69 | **Cell** | Atomic verified unit · CRE: Class C with workout angle |
| < 50 | **Swarm** | Raw / unverified · CRE: dirt that needs entitlements |

The 5-tier is the **constitutional vocabulary**. The 4-tier is the **production-default abstraction**. They map cleanly:

- Genesis (95+) + top of Honey (85-94) → Royal Jelly (≥ 0.85)
- Mid Honey (70-84) → Honey (0.70-0.84)
- Cluster + Cell → Jelly (repair candidate)
- Swarm + any critical-fail → Propolis

Use the 5-tier when you are speaking publicly · documenting a flagship deed · or talking to a CRE-mindset client who needs the full Class A / B / C ladder. Use the 4-tier when you are running the Tribunal and routing pairs in production.

---

## The 3-tier collapse (operator shorthand)

Sometimes the operator just wants to know: did it ship · does it need work · or did it blow up. That's the 3-tier collapse:

| 3-tier | 4-tier source | What the operator does |
|---|---|---|
| **HONEY** | Royal Jelly + Honey | Ship it · receipt it · move on |
| **JELLY** | Jelly | Route to SwarmFixer · re-grade · come back tomorrow |
| **PROPOLIS** | Propolis | Seal it · feed it to the failure corpus · do not publish |

The 3-tier is what gets surfaced on the dashboard `Tribunal Verdict` chip. The 4-tier is what gets written into the deed JSON. The 5-tier is what gets used in the public comp sheet. All three views are valid · all three are the same underlying score · just at different zoom levels.

---

## Mapping to CRE asset grading (the dial that already exists in the founder's head)

CRE has had this same grading model for 50 years. We didn't invent it · we ported it.

| CRE class | DefendableOS tier | What it means |
|---|---|---|
| **Class A** | Royal Jelly (Genesis when 95+) | Prime location · irreplaceable · institutional buyer pool · 5-cap-able · the listing you wake up grateful for |
| **Class B** | Honey | Decent · adequate · replaceable · core-plus buyer pool · the listing that pencils on the right re-trade |
| **Class C** | Jelly (workout) | Bad neighborhood · deferred maintenance · value-add buyer pool · the listing that needs a repair plan before it sells |
| **Below Class C** | Propolis | Trash · environmental issues · functional obsolescence · the listing you PASS on (PASS doctrine applies directly) |

A sr broker reads this table and nods. That's the point. We didn't invent a new ladder · we just gave the AI output the same ladder that already governs $30 trillion of institutional real estate.

---

## How a score becomes a tier (the production pipeline)

1. **Pair arrives at Tribunal** · either from a live agent call (SwarmRouter logs it) or a cook batch (validator queue).
2. **Rule layer runs first** · 12-check validator chain (C01-C12 · see [`13_validator_chain_doctrine.md`](13_validator_chain_doctrine.md)). Any critical-fail → automatic PROPOLIS · the judge never sees it.
3. **Scale A judge** (gemma3:12b on GPU 1 swarmrails) produces a JellyScore 0-1 + reason. Fast pass.
4. **Scale B judge** (qwen2.5:32b on GPU 0 swarmrails) produces a JellyScore 0-1 + reason. Deep pass.
5. **Drift check** · if `|ScaleA - ScaleB| > 0.15` · Critic is invoked. If Critic can't reconcile · Katniss arbitrates. (See [`08_tribunal_doctrine.md`](08_tribunal_doctrine.md).)
6. **PENALIZED SCORING applied** · if either auto-judge returns < 0.75 with a critical-issue flag, the judge contribution is zeroed and the pair is forced to be re-evaluated under the rule layer only. This prevents a hot judge from rescuing a fundamentally broken output.
7. **Tier assigned** · final score → 4-tier bucket → 5-tier expanded view → 3-tier dashboard chip.
8. **Routed**:
   - Royal Jelly → DDEED writer · published · ENS-resolved · Hedera-anchored.
   - Honey → receipt issued · published · books-and-records updated.
   - Jelly → `pair-candidates/jelly-repaired/` · SwarmFixer queue.
   - Propolis → sealed · `propolis-vault/` · feeds DETECT-task training.

---

## Why no tier escapes the system

The founder rule: **no waste in a Hive.** Even Propolis pairs have a job · they teach the next model what failure looks like. Even Jelly pairs have a job · they are the repair flywheel that produces lift. Even Honey pairs that don't make Royal Jelly have a job · they ship to the customer and build the books.

This is the difference between DefendableOS and a vendor that throws away its bad outputs. We grade everything · we keep everything · we put everything to work. The propolis vault is the second-most-valuable corpus in the Hive · only behind the Royal Jelly training set.

The waste in most AI shops is the cost of pretending failure didn't happen. We pretend nothing. We grade everything. We receipt the grade. We anchor the receipt. That's how the language lives in the blocks.

---

## What every tier touches in the 5 Proofs

- **Royal Jelly** · touches all 5 (ORIGIN · QUALITY · PROCESS · ECONOMICS · TRUST · deed-issued · Hedera-anchored).
- **Honey** · touches 4 of 5 (skips TRUST anchoring on a per-pair basis · batched into Merkle root only).
- **Jelly** · touches PROCESS + QUALITY (the failure lineage is the asset).
- **Propolis** · touches PROCESS + ECONOMICS (the cost of the failure · the lineage of what tried).

Every tier participates in the books-and-records. Every tier is auditable. That's the rule.

---

## Read next

- [`08_tribunal_doctrine.md`](08_tribunal_doctrine.md) · the 6-role Tribunal that produces the scores
- [`13_validator_chain_doctrine.md`](13_validator_chain_doctrine.md) · the 12-check rule layer
- [`11_swarmfixer_doctrine.md`](11_swarmfixer_doctrine.md) · the repair pipeline for Jelly
- [`../vocabulary/hive_terms/royal-jelly.md`](../vocabulary/hive_terms/royal-jelly.md) · the apex term
- [`../vocabulary/hive_terms/jelly.md`](../vocabulary/hive_terms/jelly.md) · the workout term
- [`../vocabulary/hive_terms/propolis.md`](../vocabulary/hive_terms/propolis.md) · the trash-heap-that-trains term

🐝 *Grade everything. Keep everything. Put everything to work. The Hive verifies before it issues.*
