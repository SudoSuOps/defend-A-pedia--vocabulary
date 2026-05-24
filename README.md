# Defend-A-Pedia

**The language constitution of DefendableOS.**

This is not a glossary.

This is:

- the language constitution of DefendableOS
- the CRE-to-software translation layer
- the backend schema map
- the Tribunal operating doctrine
- the client trust vocabulary
- the books-and-records dictionary
- the future AI fine-tuning corpus
- the repair intelligence taxonomy
- the Honey / Royal Jelly / Jelly / Propolis classification doctrine
- the foundation for receipts, deeds, validator chains, and assignment scoring

The founder's language is the source material.
The CRE street knowledge is preserved.
The schema follows the language · not the reverse.

---

## Core thesis

```
CRE Street Language
        ↓
Defendable Vocabulary
        ↓
Backend Fields
        ↓
Tribunal Scoring
        ↓
Honey / Royal Jelly / Jelly / Propolis Classification
        ↓
Receipts + DDEED
        ↓
Books and Records
        ↓
Client Trust Layer
        ↓
SwarmFixer Training Data
        ↓
Future DefendableOS Intelligence
```

> *"The language lives in the blocks."*

---

## What this repo is for

**Operators**: This is your playbook. Read the doctrine. Read the vocabulary. Run the deals.

**Engineers**: Every term in here maps to a backend field, a scoring hook, a schema, or a receipt format. The schema follows the language.

**Jr brokers / microscalers**: This is your onboarding library. Read [`docs/playbooks/jr_broker_playbook.md`](docs/playbooks/jr_broker_playbook.md). Master the vocabulary. Then make the dials.

**Sr brokers / validators**: This is your adjudication reference. Read the Tribunal doctrine. The 4-tier classification (Honey · Royal Jelly · Jelly · Propolis) is locked.

**Clients**: The terms here are how we'll speak with you. Plain English supplements ("Client Explanation" section in every term) translate the operator language into your boardroom language.

**AI models in training**: Every term is a training pair. The `data/*.jsonl` corpora are ready for fine-tuning. Future SwarmCurator · SwarmJelly · SwarmJudge cohorts feed from here.

---

## Repository layout

```
defend-A-pedia--vocabulary/
├── docs/
│   ├── doctrine/         16 foundational doctrine docs (manifesto · master map · Tribunal · etc.)
│   ├── vocabulary/       14 category subdirs · 50+ vocabulary terms (production · growing)
│   ├── playbooks/        13 operator playbooks (jr/sr broker · Tribunal · SwarmFixer · etc.)
│   ├── schemas/          14 JSON schemas (term · verdict · taxonomy · validator chain · etc.)
│   ├── examples/         11 reference examples (term · Honey record · LOU · etc.)
│   ├── prompts/          8 Claude/Kimi prompts (extraction · translation · validation)
│   ├── architecture/     6 architecture diagrams (Tribunal flow · SwarmFixer flywheel · etc.)
│   └── ui_dials/         7 dial specs (Probability of Close · Repair Lift · etc.)
├── data/                 15 JSONL corpora (training-ready · validator-ready)
├── scripts/              8 validation + export scripts (Python · zero magic)
├── tests/                5 test files (term integrity · schema alignment · cross-refs)
└── assets/               diagrams · screenshots · branding
```

---

## The 13 mandatory term sections

Every vocabulary term MUST have all of these:

1. **Street Definition** · how the term is used in real CRE/operator conversation
2. **CRE Operator Meaning** · what an experienced broker actually means by it
3. **DefendableOS Definition** · how the term lives inside DefendableOS
4. **Backend Representation** · the fields · enums · schema hooks · scoring impacts
5. **Client Explanation** · plain-English for the boardroom
6. **Jr Broker Use** · how a junior identifies/extracts this
7. **Sr Broker Use** · how a senior interprets/challenges/validates this
8. **Tribunal Use** · how the Tribunal scores/grades/classifies this concept
9. **Evidence Required** · documents · receipts · records that support this term
10. **Failure Modes** · how this is misunderstood · hallucinated · manipulated · overclaimed
11. **Scoring Impact** · effect on assignment success · repair lift · confidence · risk · close prob
12. **Deed / Receipt Impact** · effect on DDEED issuance · books and records · audit chains
13. **Related Terms · Example · DefendableOS Notes** · cross-links + real-world example + ops notes

See [`docs/examples/sample_term_color.md`](docs/examples/sample_term_color.md) for the canonical structure.

---

## Foundational doctrine (read in order)

| # | Doc | What you learn |
|---|---|---|
| 00 | [Manifesto](docs/doctrine/00_manifesto.md) | The founder voice · why we built this · the brick-and-mortar footprint |
| 00 | [Defendable Language Map](docs/doctrine/00_defendable_language_map.md) | The full 10-step pipeline CRE → trust · the master map |
| 01 | [Language is Infrastructure](docs/doctrine/01_language_is_infrastructure.md) | Why vocabulary IS schema · not separate from it |
| 02 | [CRE to DefendableOS](docs/doctrine/02_cre_to_defendableos.md) | The translation table · every CRE term → every DefendableOS field |
| 03 | [Jr Broker · Sr Broker Doctrine](docs/doctrine/03_jr_broker_sr_broker_doctrine.md) | The career ladder · what each role owns |
| 04 | [Books and Records Doctrine](docs/doctrine/04_books_and_records_doctrine.md) | The auditable trail · receipts → deeds → trust |
| 05 | [Client Language Doctrine](docs/doctrine/05_client_language_doctrine.md) | How to speak to the principal · NOT to engineers |
| 06 | [Hive Doctrine](docs/doctrine/06_hive_doctrine.md) | The 5-tier biology · Bee Agent lifecycle |
| 07 | [Honey · Royal Jelly · Propolis](docs/doctrine/07_honey_royal_jelly_propolis.md) | The 4-tier classification (95+ / 85-94 / 70-84 / <70 · 50-69 Cell · <50 Swarm) |
| 08 | [Tribunal Doctrine](docs/doctrine/08_tribunal_doctrine.md) | The adjudication system · 6-role Tribunal (Scout · Router · Filter · Repair · Critic · Katniss) |
| 09 | [Energy and Cost to Mint](docs/doctrine/09_energy_and_cost_to_mint.md) | The economics · $0.0052/deed baseline · fee tiers |
| 10 | [Receipts · Deeds · Books and Records](docs/doctrine/10_receipts_deeds_and_books_records.md) | The 5-proof framework · Hedera anchoring · ENS |
| 11 | [SwarmFixer Doctrine](docs/doctrine/11_swarmfixer_doctrine.md) | The agent refinery · 5-task RJ output (DIAGNOSE · REPAIR · PREVENT · DETECT · COMPARE) |
| 12 | [DefendableRouter Doctrine](docs/doctrine/12_defendablerouter_doctrine.md) | The middleware · write-only · <5ms · ENS-anchored |
| 13 | [Validator Chain Doctrine](docs/doctrine/13_validator_chain_doctrine.md) | The 12-check chain · 7 critical + 5 advisory |
| 14 | [Assignment Success Doctrine](docs/doctrine/14_assignment_success_doctrine.md) | When a job IS the job · the scoring rubric |
| 15 | [Probability of Close Doctrine](docs/doctrine/15_probability_of_close_doctrine.md) | The deal-physics dial · CRE comp logic applied to AI engagements |

---

## Mandatory core terms (locked vocabulary · expanding)

### CRE terms
`color` · `digest` · `OM` · `LOI` · `PSA` · `due diligence` · `deal flow` · `probability of close` · `underwriting` · `cap rate` · `NOI` · `rent roll` · `sponsor` · `principal` · `buyer strength` · `seller motivation` · `books and records` · `engagement` · `assignment` · `broker opinion` · `IC memo` · `on-market` · `off-market`

### Hive terms
`Honey` · `Royal Jelly` · `Jelly` · `Propolis` · `Hive` · `Swarm` · `Bee` · `Energy` · `Cost to Mint` · `Receipt` · `Deed` · `DDEED` · `Proof of Value` · `Proof of Compute` · `Proof of Repair`

### Tribunal terms
`Tribunal` · `Validator` · `Validator Chain` · `Judge` · `Assignment Success` · `Assignment Failure` · `Repair Lift` · `Failure Flag` · `Evidence Strength` · `Confidence Weight` · `Hallucination Event` · `Adversarial Case`

### System terms
`DefendableRouter` · `SwarmFixer` · `DefendableJelly` · `DefendableHack` · `ClawCheck` · `AgentBench` · `Pair Candidate` · `Honey Record` · `Royal Jelly Record` · `Propolis Event`

---

## The senior hacks (founding architects)

This repository was bootstrapped under a 6-architect charter. Each senior hack owns a doctrine layer:

| Hack | Role | Owns |
|---|---|---|
| SH1 | **CRE Doctrine Architect** | Doctrine files · CRE-to-DefendableOS translation · jr/sr broker doctrine · books-and-records doctrine |
| SH2 | **Vocabulary Infrastructure Architect** | Repo tree · schemas · JSONL structures · validation scripts · backend mappings |
| SH3 | **Tribunal Architect** | Tribunal doctrine · Honey/Jelly/Propolis taxonomy · validator chain doctrine · scoring definitions |
| SH4 | **SwarmFixer Architect** | Repair terminology · repair lift language · pair-candidate taxonomy · failure→repair→validation vocabulary |
| SH5 | **Client Language Specialist** | Client-facing explanations · engagement language · dashboard language · trust language · probability-of-close explanations |
| SH6 | **QA Validator** | Schema consistency · vocabulary consistency · cross-links · founder-language preservation · no generic fluff |

---

## Quick start

```bash
# Clone
git clone git@github.com:SudoSuOps/defend-A-pedia--vocabulary.git
cd defend-A-pedia--vocabulary

# Install dependencies
make install

# Read the manifesto first
cat docs/doctrine/00_manifesto.md

# Read the master map second
cat docs/doctrine/00_defendable_language_map.md

# Browse the vocabulary index
cat docs/vocabulary/index.md

# Validate the repo (run after any change)
make validate

# Run tests
make test

# Build the index
make build-index

# Export the backend field map (for engineers wiring schemas)
make export-backend

# Export the client dictionary (for sales/marketing)
make export-client
```

---

## Operating principles

These are non-negotiable:

1. **Preserve founder/operator language** · CRE street vocabulary stays · no academic sanitization
2. **Every term maps to software** · backend field · scoring hook · receipt impact
3. **Every software field maps back to real-world meaning** · no orphan fields
4. **Every term supports future AI training** · all 50+ terms are training-pair ready
5. **Every term supports receipts/deeds/books-and-records** · auditable end-to-end
6. **Every term supports Tribunal scoring** · grade-able · classify-able
7. **Every term supports client-facing communication** · plain-English layer mandatory
8. **Every term supports validator review** · evidence-required field mandatory
9. **Every term supports DefendableOS UI dials** · scoring impact section feeds dashboard
10. **Avoid generic MBA or textbook definitions** · this is operator infrastructure
11. **Think in systems, not marketing**
12. **The repo must feel production-grade · not academic**

---

## The 5 Swarm Laws apply to vocabulary too

1. **Honey Law** · *You get more Bees with Honey* · clear vocabulary attracts more operators
2. **Cell Law** · *Great intelligence begins with a single Cell* · every term is a Cell
3. **Swarm Law** · *The Swarm is stronger than the Bee* · cross-linked vocabulary is stronger than isolated terms
4. **Purity Law** · *Virgin signal is the seed of great Honey* · founder voice is the virgin signal
5. **Genesis Law** · *What the Hive verifies becomes truth* · vocabulary is receipted

---

## License

MIT · Swarm and Bee LLC · DBA Swarm & Bee AI · Florida · D-U-N-S 138652395

---

🐝 *Validate the Validator. Prove the Location.*
*The language lives in the blocks.*

Built by Donovan Mackey · 30-year CRE broker · $8B in closed transactions · Jupiter, FL.
Powered by the Swarm & Bee in-house refinery · operator-owned · no VC · no token · no charts. Just receipts.
