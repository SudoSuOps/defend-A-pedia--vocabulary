# Contributing to Defend-A-Pedia

This is not a glossary. This is the **language constitution** of DefendableOS.

Every term you add becomes:
- backend schema
- Tribunal scoring hook
- receipt field
- DDEED line item
- books-and-records entry
- SwarmFixer training pair
- client trust language
- jr broker playbook step

Write accordingly.

## Voice & tone

- Preserve **founder/operator language**. CRE street terms stay CRE street terms.
- No academic MBA fluff. No corporate fluff. No "leverage synergies."
- Write like an operator who's closed deals · not like a consultant who's written decks.
- "To the shed" · "on the dial" · "list the building" · "comp it" · "color on the asset" — keep them.
- If a term has a CRE meaning AND a DefendableOS meaning · preserve BOTH.

## Adding a new vocabulary term

1. Pick the right category subdir under `docs/vocabulary/` (e.g., `cre_terms/`, `hive_terms/`, `tribunal_terms/`)
2. Create `<term-slug>.md` using the exact structure in `docs/examples/sample_term_color.md` · **all 13 sections are mandatory**
3. Add the term to `data/vocabulary_terms.jsonl` with the canonical schema fields
4. Cross-link to ≥ 2 related terms in the **Related Terms** section
5. Run `make validate` · all checks must pass

## The 13 mandatory sections (per term)

1. Street Definition
2. CRE Operator Meaning
3. DefendableOS Definition
4. Backend Representation
5. Client Explanation
6. Jr Broker Use
7. Sr Broker Use
8. Tribunal Use
9. Evidence Required
10. Failure Modes
11. Scoring Impact
12. Deed / Receipt Impact
13. Related Terms + Example + Notes

## Schema-first

If your term affects a backend field · scoring dial · or receipt structure · also update the relevant JSON schema in `docs/schemas/`.

## The Genesis Law applies to vocabulary too

> *"What the Hive verifies becomes truth."*

Don't ship a term that hasn't been used in an actual operator conversation · a real CRE deal · a Tribunal verdict · or a customer engagement. The vocabulary is receipted just like the deeds.

## Pull request checklist

- [ ] Term file exists with all 13 sections
- [ ] JSONL entry added to `data/vocabulary_terms.jsonl`
- [ ] At least 2 cross-links to related terms
- [ ] `make validate` passes
- [ ] `make test` passes
- [ ] No generic textbook definitions
- [ ] Founder voice preserved
- [ ] Backend mapping shown (fields · enums · schemas)
- [ ] Failure modes named
- [ ] Cross-reference in `docs/doctrine/00_defendable_language_map.md` if introducing a new domain

## Senior hacks · architects

Senior hack assignments live in the founding charter (see `README.md`). Six senior hacks own the foundational doctrine:

- **Senior Hack 1** · CRE Doctrine Architect
- **Senior Hack 2** · Vocabulary Infrastructure Architect
- **Senior Hack 3** · Tribunal Architect
- **Senior Hack 4** · SwarmFixer Architect
- **Senior Hack 5** · Client Language Specialist
- **Senior Hack 6** · QA Validator

Cross-architect changes require a check-in.

## License

MIT. The vocabulary is open. The receipts are public. The doctrine compounds.

🐝 *Validate the Validator. Prove the Location.*
