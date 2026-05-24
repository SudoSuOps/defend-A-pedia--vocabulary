# Communicator

> *"We speak first · then we have the receipts to back it up. That's DefendableOS."*
> — Founder · 2026-05-24

## Street Definition

The **Communicator** is the model that listens to a human · figures out what they actually meant · turns that into a structured directive an agent can execute against · then takes the agent's output and translates it back into language the human can act on. It's the bridge. It's the bookend. It's the meaning-alignment layer.

NOT a chatbot. A communication arbitrator.

## CRE Operator Meaning

In CRE · this is what a sr broker DOES on every call. A principal says "yo we're bleeding on Q4 · figure it out" and the sr broker hears: *re-underwrite the asset · check tenant credit drift · flag any covenants triggered · price the workout window · come back with three lanes (refi / restructure / sale)*. The broker translates the principal's emotional/incomplete language into a structured workstream the team can execute.

Then the broker takes the team's analysis (cap rates · DSCR · comp grid · scenarios) and translates it back into a 90-second summary the principal can act on: *"You got 73 days to refi the Sun Belt warehouse. Two willing lenders. Best execution at 6.4. Recommend the Bridgehouse term sheet. Authorize next move?"*

The Communicator is that sr broker · in code · always on · 24/7 · trained on the founder's actual book.

## DefendableOS Definition

The **Communicator LLM** is the bidirectional translation model that sits at both ends of the assignment lifecycle:

- **INTAKE**: human speech (messy · emotional · street-level · incomplete) → structured directive (validator-ready JSON · vocabulary-tagged · risk-scored · evidence-required-named)
- **OUTPUT**: machine output (Tribunal verdict · 5-Proof receipt · agent execution result) → human explanation (CRE-grade · CFO-readable · founder-voice preserved)

Both directions use the SAME defend-A-pedia vocabulary as the canonical reference. Both directions are receipted · graded · deeded. The Communicator is the FIRST model the customer talks to and the LAST model that talks back.

## Backend Representation

```json
{
  "communicator.intake_id": {
    "type": "string",
    "pattern": "DCOM-INTAKE-{cell_hash}-{utc}"
  },
  "communicator.output_id": {
    "type": "string",
    "pattern": "DCOM-OUTPUT-{cell_hash}-{utc}"
  },
  "directive.json": {
    "type": "jsonb",
    "schema_file": "docs/schemas/engagement.schema.json"
  },
  "directive.intent_class": {
    "type": "enum",
    "values": ["INVESTIGATE", "EXECUTE", "VALIDATE", "REPORT", "ESCALATE", "PAUSE"]
  },
  "directive.evidence_required": {
    "type": "array",
    "items": "string"
  },
  "round_trip_match_score": {
    "type": "float",
    "range": [0.0, 1.0],
    "scoring_hook": "communicator_alignment_score"
  },
  "vocabulary_candidates_emitted": {
    "type": "array",
    "description": "New terms heard from client · ready for validator promotion"
  }
}
```

Schema files: `docs/schemas/engagement.schema.json` · `docs/schemas/assignment_success.schema.json` · new schema pending: `communicator_directive.schema.json`

## Client Explanation

When you call us · the first thing on the line is the Communicator. It listens for what you ACTUALLY need · not just what you said. Then we run the work. Then the Communicator writes back to you in your language · with the receipts attached. You get a real answer in your voice · with the math behind it. No technical mystery box. No "the model decided." Real translation · documented · defendable.

## Jr Broker Use

When you take a call:
1. Open the Communicator intake (one button · captures audio + your live notes)
2. Let it draft the structured directive · don't second-guess on the call · let the model catch the intent
3. After the call · review the directive · confirm the intent class (INVESTIGATE / EXECUTE / VALIDATE / etc.)
4. Flag any terms you heard the client use that DON'T already exist in defend-A-pedia (those become Vocabulary Deed candidates)
5. Hand off to the agent/team via the directive ID · NOT via Slack paste

**Discipline**: Do NOT ship work against the raw call audio. Work against the Communicator-emitted directive. The directive is what the Tribunal will grade you against.

## Sr Broker Use

The sr broker REVIEWS the Communicator's intake directive before it ships:
- Does the intent class match what you'd diagnose hearing the call directly?
- Are the evidence requirements complete · or did the Communicator miss something the client implied?
- Is there a risk tag the Communicator didn't catch (regulatory · political · financial)?
- Are any new vocabulary candidates worth promoting to the dictionary?

The sr broker has OVERRIDE AUTHORITY on the directive. If you change it · the change is itself receipted (transition_log) and becomes training signal for Communicator vNext. **Your override is the gold standard.**

## Tribunal Use

The Tribunal grades the Communicator at BOTH ends:

| Stage | Tribunal check | Class on fail |
|---|---|---|
| INTAKE · intent extraction | Does the structured directive match what the human actually said + meant? | JELLY (recoverable · re-prompt human) or PROPOLIS (intent fabricated) |
| INTAKE · vocabulary mapping | Did the Communicator use canonical defend-A-pedia terms? Did it flag new ones? | JELLY (lexicon drift) or HONEY (clean) |
| OUTPUT · explanation accuracy | Does the human-language output accurately reflect the agent's actual result + the Tribunal verdict? | PROPOLIS (mistranslation = trust break) |
| OUTPUT · client voice match | Does it use the client's vocabulary · not generic SaaS speak? | JELLY (sanitized · re-translate) |
| ROUND-TRIP | Did the final answer match the ORIGINAL intent? | The killer check · PROPOLIS if the agent answered a different question than asked |

`round_trip_match_score < 0.7` triggers the Communicator's own SwarmFixer-style repair loop (re-prompt human · re-extract intent · re-execute).

## Evidence Required

- Audio or text capture of the original human input (raw)
- Communicator-emitted structured directive (JSON)
- Agent execution log (Tribunal-graded)
- Communicator-emitted human-language output
- Round-trip match score
- Any vocabulary candidates emitted (with frequency · context · client_id)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **fabricated_intent** | Communicator emitted a directive the human didn't actually authorize | PROPOLIS |
| **lost_in_translation** | Output explanation contradicts the agent's actual result | PROPOLIS |
| **lexicon_drift** | Communicator used generic terms instead of canonical defend-A-pedia vocab | JELLY |
| **scope_creep_at_intake** | Directive contained tasks the human never asked for | JELLY |
| **scope_loss_at_intake** | Directive missed tasks the human implied but didn't explicitly state | JELLY (sr broker catches via review) |
| **client_voice_loss** | Output explanation reads SaaS-y · not in client's own vocabulary | JELLY |
| **missed_vocabulary_candidate** | Heard a new term from client · didn't flag it for promotion | JELLY (advisory · not a deed-blocker) |
| **round_trip_mismatch** | Final output answered a different question than was asked | PROPOLIS |

## Scoring Impact

- **assignment_success**: HIGH · if the directive is wrong · the assignment can succeed against the wrong target and still count as a failure
- **repair_lift**: HIGH at intake (better directives compound over time as Communicator learns) · MEDIUM at output (cosmetic vs functional)
- **validator_confidence**: HIGH · the sr broker's override behavior is the strongest validator signal in the system
- **risk_temperature**: INVERSE · better Communicator = lower risk because misunderstanding is caught at entry
- **probability_of_close**: HIGH · meaningful translation IS the close
- **evidence_strength**: INDIRECT · Communicator names the evidence required · so completeness is downstream-correlated
- **cost_to_mint**: MEDIUM · adds 1 model in the path · but saves cost on every Tribunal re-grade due to scope errors

## Deed / Receipt Impact

- **Receipt fields touched**: `intake_id` · `output_id` · `directive_json_hash` · `round_trip_match_score` · `vocabulary_candidates_emitted`
- **DDEED class impact**: TWO new deed classes
  - `DDEED-DOV-COMMUNICATOR` · receipts the bidirectional translation event (intake + output bundled)
  - `DDEED-DOV-VOCAB` · receipts any vocabulary candidates promoted to canonical defend-A-pedia terms
- **Books and records layer**: ALL 5 layers · the Communicator events live alongside the deeds in PostgreSQL → Merkle → NAS → Hedera → ENS
- **5 Proofs touched**: ALL FIVE
  - ORIGIN (which Communicator version · which model · which prompt)
  - QUALITY (round-trip match score · client voice match)
  - PROCESS (full intake → directive → execution → output → explanation trace)
  - ECONOMICS (cost-to-translate · extra model in the path)
  - TRUST (Hedera anchor · ENS-bound · client can verify they were heard correctly)

## Related Terms

- [directive](../workflow_terms/directive.md) · the structured output Communicator produces at intake
- [intent](../workflow_terms/intent.md) · what Communicator extracts from raw speech
- [meaning-alignment](../tribunal_terms/meaning-alignment.md) · the doctrine layer Communicator implements
- [communication-arbitration](../tribunal_terms/communication-arbitration.md) · what the Communicator does (vs chat)
- [book-of-business](../client_terms/book-of-business.md) · the CRE concept · the Communicator's training corpus
- [language-asset](../client_terms/language-asset.md) · the proprietary moat Communicator builds over time
- [vocabulary-deed](../minting_terms/vocabulary-deed.md) · the new deed class that codifies language additions
- [round-trip-verification](../tribunal_terms/round-trip-verification.md) · did the final output match the original intent?
- [tribunal](../tribunal_terms/tribunal.md) · the judge that grades Communicator at both ends
- [pre-market-flight-sheet](../client_terms/pre-market-flight-sheet.md) · the document Communicator helps the broker prepare

## Example

> **Engagement**: Imaging center principal calls 16:42 on Tuesday. Says: *"yo my MRI agent quoted three patients last week prices that came back wrong · insurance freaked · what the hell is going on get me answers by Thursday."*
>
> **Communicator INTAKE directive**:
> ```json
> {
>   "intake_id": "DCOM-INTAKE-A7F3-2026-05-24T20:42:18Z",
>   "intent_class": "INVESTIGATE",
>   "subject_agent": "mri-quote-bot-prod-002",
>   "incident_window": "2026-05-19/2026-05-24",
>   "incident_count": 3,
>   "evidence_required": [
>     "agent execution logs for the 3 quote events",
>     "insurance pre-auth comparison",
>     "agent prompt version diff (last 30d)",
>     "training corpus check for billing-code drift"
>   ],
>   "risk_tags": ["financial", "compliance", "patient_facing"],
>   "deadline_utc": "2026-05-29T17:00Z",
>   "vocabulary_candidates": ["insurance freaked"]
> }
> ```
>
> **Communicator OUTPUT explanation (Thursday morning brief)**:
> ```
> Boss · here's the read.
>
> All 3 mis-quotes traced to a Stripe API change on May 18 that
> shifted how the agent reads HSA-eligible vs HSA-ineligible
> imaging codes. The agent kept quoting HSA prices on procedures
> Stripe re-classified out of HSA eligibility on May 18.
>
> Patients · insurance · all three confirmed.
> Fix · prompt patch shipped Wednesday 14:00.
> Re-bench · 6/6 quotes Honey since.
> Liability · we covered the 3 mis-quotes ($840 total) ·
> deed DDEED-DOV-FIXER-MRI-000007-v1 anchored.
>
> No more drift expected. Tribunal monitoring continuous.
> Insurance comms · I have a draft ready when you say go.
>
> Lift on this fix: avoided estimated $34K/quarter in similar
> mis-quotes had drift continued.
>
> ROI on the day: 41x.
> ```
>
> **Vocabulary deed**: `"insurance freaked"` candidate promoted via validator review to canonical term `insurance-escalation-event` · added to defend-A-pedia · client's exact wording preserved in the term's `Street Definition` section. The book of business just got 1 entry richer.

## DefendableOS Notes

- The Communicator is what makes DefendableOS feel like a HUMAN brokerage · not a SaaS bot
- Every Communicator interaction is BOTH service AND training data · the dual-use is the moat
- The vocabulary candidates emitted by Communicator become the proprietary corpus competitors can't replicate
- Pairs with [[swarmjelly]] · when Tribunal flags PROPOLIS due to round-trip mismatch · SwarmFixer's REPAIR task fires on the Communicator (not the underlying agent)
- The bidirectional model is ONE model · trained both directions · shares the same defend-A-pedia vocabulary base
- Ship sequence: defend-A-pedia v0.2.x (this) → Tribunal v1.0 → Communicator v0.1 (depends on both)

🐝 *We speak first · then we have the receipts to back it up. That's the brokerage in code.*
