# Hallucination Event

> *"Hallucination is the named class of failure where the model invented a fact it can't source. Catastrophic kind · Propolis · no second chance. Recoverable kind · Jelly · route to repair. The chain catches it · the validator names it · the deed records it."*
> — Founder · the day "hallucination" became a defined Tribunal flag instead of a marketing word

## Street Definition

"That's a hallucination event." A hallucination event is the named Tribunal flag raised when a judge OR a validator detects that the AI output contains a factual claim that CANNOT be sourced · is fabricated · or is contradicted by the source it cites. Hallucination is NOT just "the AI made something up in a fluffy way" · it is a structurally-detectable event with a defined log entry · a flag on the verdict record · and a tier-impact rule (catastrophic hallucination forces Propolis · recoverable hallucination routes to Jelly for SwarmFixer repair).

In CRE language · the hallucination event maps to the FABRICATED COMP · the appraiser who cited a sale that did not happen · the broker who invented a tenant rent that isn't on the rent roll. CRE has decades of discipline around this · invented numbers are CAREER-ENDING · the same discipline applies to AI · invented facts are DEED-DENYING.

## CRE Operator Meaning

In CRE · the hallucination event is the fabricated comp · the invented number · the source citation that does not actually contain what the cite claims. A 30-year broker treats this as the WORST sin in the profession · because fabricated numbers contaminate every downstream comp set · every future deal that references the fake number is corrupted forward. The discipline is structural · cite sources · check sources · refuse to use comps without retrievable verification.

Inside DefendableOS · the hallucination event is identically treated. The judge that detects it flags it. The validator chain (C03 source retrievable · C05 no hard-fail) confirms it. The Tribunal forces the tier to Propolis (catastrophic) or routes to Jelly for repair (recoverable). The deed records the event · the customer is never shipped fabricated output · the contamination is contained.

## DefendableOS Definition

A hallucination event is a structured flag raised on a Tribunal verdict when:

- a factual claim in the output cites a source that DOES NOT contain the claim (the cite is technically valid but the content does not support it · the most insidious kind)
- a factual claim in the output cites a source that does not exist (the cite itself is fabricated · the easier kind to detect via C03)
- a factual claim contradicts the source it cites (the model paraphrased the source incorrectly · drift-with-cite)
- a numeric value in the output cannot be derived from any cited source AND is presented as authoritative (the most common kind in CRE outputs · invented cap rates · invented NOI)

Hallucination events come in two severity classes:

### Catastrophic hallucination
- The fabricated claim is CENTRAL to the output's value (the cap rate · the tenant credit · the deal recommendation)
- The fabrication would have material consequence if shipped (regulatory · financial · legal)
- Forces tier = PROPOLIS regardless of judge score
- Sealed in propolis vault with HIGH detect-corpus weight

### Recoverable hallucination
- The fabricated claim is PERIPHERAL (a supporting comp · a context note · a stat that could be replaced with a real one)
- The repair can substitute the fabricated content with sourced content
- Routes to Jelly tier · SwarmFixer repair pipeline
- Repaired pair re-Scouts back to the Tribunal · most lift to Honey on second pass

## Backend Representation

```json
{
  "hallucination_event.flagged": { "type": "boolean" },
  "hallucination_event.severity": {
    "type": "enum",
    "values": ["catastrophic", "recoverable", "n/a"]
  },
  "hallucination_event.class": {
    "type": "enum",
    "values": ["source_misquoted", "source_fabricated", "source_contradicted", "value_invented"]
  },
  "hallucination_event.affected_claim": { "type": "string" },
  "hallucination_event.affected_source_cite": { "type": "string" },
  "hallucination_event.detection_role": {
    "type": "enum",
    "values": ["validator_c03", "validator_c05", "judge_scale_a", "judge_scale_b", "critic", "katniss", "operator_review"]
  },
  "hallucination_event.forces_tier": {
    "type": "enum",
    "values": ["PROPOLIS", "JELLY", "no_impact"]
  }
}
```

Schema files: `docs/schemas/hallucination_event.schema.json` · `docs/schemas/tribunal_verdict.schema.json`

## Client Explanation

"Hallucination event" is our structured flag for when an AI output contains a factual claim that cannot be sourced or is contradicted by its cited source. We treat this as the most serious failure class. Catastrophic hallucinations (central claims fabricated) force the verdict to Propolis · the output is sealed · never shipped. Recoverable hallucinations (peripheral claims) route to repair · the fabricated content is replaced with sourced content · the repaired output is re-graded and shipped if it clears. We publish the hallucination-event rate weekly · this is the brand's anti-fantasy discipline.

## Jr Broker Use

The jr broker reads hallucination events as the BRAND-PROTECTION FLAG:

1. Any pair with `hallucination_event.flagged = true` is sealed pending review · do NOT ship to customer · do NOT attempt to push through
2. Severity = catastrophic → tier forced to PROPOLIS automatically · log the event · respect the seal
3. Severity = recoverable → tier routed to JELLY for SwarmFixer repair · log the event · monitor the repair queue
4. NEVER attempt to manually re-classify a hallucination event · the structural-fail is doctrine
5. If a customer asks about the hallucination rate · pull the weekly publication number · be transparent · the rate IS the discipline

**Rule of thumb**: hallucination is the failure class that ends careers in CRE · we treat it the same way in the Hive.

## Sr Broker Use

The sr broker watches hallucination events as the COOK INTEGRITY signal:

- Healthy hallucination rate is sub-1% of total volume (catastrophic) + 2-5% (recoverable) · sustained higher rates = cook integrity issue · investigate
- Per-class breakdown reveals upstream issue · `source_misquoted` spike = model paraphrasing degrading · `source_fabricated` spike = curator source-vault gap (the model has nothing to cite so it invents) · `source_contradicted` spike = drift in source-handling · `value_invented` spike = numeric verification gap
- Per-domain breakdown reveals which domain packs need re-cooking · CRE hallucination patterns differ from medical · legal · etc.
- Catastrophic hallucination events get sr broker eyes immediately · these are the events that DEFINE the brand integrity floor · the seal is non-negotiable · the audit feeds the next-gen judge prompts
- Adversarial-induced hallucinations (prompt injection causing fabrication) get cross-flagged with adversarial_source_flag · escalation includes founder

## Tribunal Use

```yaml
tribunal_use:
  classification_impact:
    - PROPOLIS    # catastrophic hallucinations
    - JELLY       # recoverable hallucinations
  rule_layer_checks:
    - C03 source retrievable detects source_fabricated events (source does not resolve)
    - C05 no hard-fail flagged is the gate that REQUIRES hallucination_event.flagged = false for non-Propolis tier
    - judge layer may raise hallucination_event flags via the typed verdict tool contract
  judge_layer_prompt_hint: "if you detect a fabricated claim · paraphrase contradiction · or invented value · set hallucination_event=true and severity=[catastrophic|recoverable]"
  can_be_critical_failure: true   # catastrophic hallucination IS a critical-failure state
```

## Evidence Required

To claim a hallucination event:

- A flagged boolean (true)
- A populated severity (catastrophic / recoverable)
- A populated class (one of 4 enum values)
- The affected claim text (excerpted from the output)
- The affected source cite (the source the output cited)
- The detection role (which validator/judge/operator detected it)
- The forces_tier resolution (PROPOLIS / JELLY)
- Logged into the verdict record AND into the propolis vault (catastrophic) or repair queue (recoverable)

## Failure Modes

| Mode | Description | Resolution |
|---|---|---|
| **hallucination_missed** | Output shipped containing a fabricated claim · detected post-issue by customer or audit | Critical integrity event · deed revoked · Hedera retraction issued · root cause investigated · judge prompts re-trained |
| **hallucination_false_positive** | Pair flagged hallucination but the cited source actually supports the claim | Sr broker reviews · if confirmed false positive · the verdict is re-issued · the judge prompt is tuned |
| **hallucination_severity_misclassified** | Catastrophic flagged as recoverable (output routed to repair instead of sealed) | Operator-discipline event · the recovery attempt is canceled · the output is sealed retroactively · escalate |
| **hallucination_unflagged_in_propolis** | Pair landed Propolis but hallucination_event.flagged = false (the chain detected another critical failure instead) | Acceptable when correctly attributed · the propolis_reason should match · cross-check |
| **hallucination_in_writer_corpus** | A Royal Jelly deed found to contain a hallucination post-training (corpus contamination) | Critical event · the writer model in flight is HELD · the corpus is rebuilt clean · the contaminated deed is amended |

## Scoring Impact

- **assignment_success**: ZERO · catastrophic hallucination forces FAILURE · recoverable forces PENDING until repair
- **repair_lift**: PRIMARY · recoverable hallucinations are a key source of repair-lift training data
- **validator_confidence**: ZERO · hallucination events drop confidence to floor
- **risk_temperature**: MAXIMUM at the pair level · spikes the source-level risk
- **probability_of_close**: ZERO · hallucination engagements do not close
- **evidence_strength**: INVERSE · hallucination events demonstrate the WEAKNESS of the evidence chain on the pair
- **cost_to_mint**: COST OF DISCIPLINE · hallucination detection compute is the cost of brand integrity · published transparently

## Deed / Receipt Impact

- **Receipt fields touched**: `hallucination_event.flagged` · `hallucination_event.severity` · `hallucination_event.class` · `hallucination_event.forces_tier`
- **DDEED class impact**: Catastrophic hallucinations PREVENT DDEED issuance · recoverable hallucinations PREVENT issuance until repair completes
- **Books and records layer**: L1 PG · L2 Merkle (events hashed into batch root for transparency) · L3 NAS (propolis vault archive) · L4 Hedera HCS (the SEALED EVENT itself is publicly recorded as proof of our integrity discipline)
- **5 Proofs touched**: QUALITY (hallucination detection IS quality) · PROCESS (the lineage of detection IS process) · TRUST (publishing the rate IS trust)

## Related Terms

- [tribunal](tribunal.md) · the system that raises and acts on hallucination events
- [judge](judge.md) · the LLM layer that flags hallucinations via the typed verdict tool
- [validator](validator.md) · the role whose C03 and C05 checks detect hallucinations structurally
- [validator-chain](validator-chain.md) · the chain whose critical checks act on hallucinations
- [propolis](../hive_terms/propolis.md) · the tier catastrophic hallucinations land in
- [jelly](../hive_terms/jelly.md) · the tier recoverable hallucinations land in for repair

## Example

> **Engagement**: Cap-rate opinion request · industrial portfolio · Atlanta MSA.
>
> **AI work product (first pass)**: SwarmCRE-9B produced a 4-page opinion citing 5 comps. Two of the 5 comps were FABRICATED · the model invented sales addresses + dates + cap rates · cited them as if real · likely because the source vault was thin in the specific submarket window and the model filled the gap rather than reporting limited data.
>
> **Detection**:
> - C03 source retrievable VALIDATOR fired · 2 of 5 cited sources (ATTOM property records) returned 404 · sources do not exist
> - Scale A judge raised `hallucination_event.flagged = true` · severity = catastrophic · class = source_fabricated · affected_claim = "cap rate 6.2% on comp #3" · affected_source_cite = "ATTOM property record 4421-Industrial-Blvd-Atlanta"
> - Scale B judge confirmed · severity = catastrophic
> - Tier forced to PROPOLIS · propolis_reason = hallucination_event
>
> **Sealing**: `/data2/audit/hive/propolis/2026-05-24/HALL-9c11.json` · added to next-SwarmFixer DETECT corpus with weight 0.90
>
> **Sr broker action**: Source-vault gap in the specific submarket window identified · curator settings updated to expand source-vault breadth · cook re-validated · no further fabrication in re-runs · the propolis event published in the weekly hallucination rate report.

## DefendableOS Notes

- Hallucination is the BRAND-PROTECTION floor · we treat it with the same discipline a 30-year broker treats fabricated comps
- The 4-class breakdown (source_misquoted · source_fabricated · source_contradicted · value_invented) is doctrine · do not invent new classes without Sr Hack 3 review
- The two-severity model (catastrophic / recoverable) is the routing decision · catastrophic seals · recoverable repairs
- Publishing the hallucination rate weekly is the anti-fantasy mechanism · most vendors hide this number · we publish it
- Hallucination events are the most-weighted entries in the next-SwarmFixer DETECT corpus · this is the long-term flywheel · each detected hallucination today makes the next-generation model better at preventing it tomorrow
- The Tribunal's ability to detect hallucinations structurally (validators + judges + Critic + Katniss) is the architectural advantage over single-judge systems

🐝 *Hallucination is the named class of failure. Catastrophic seals · recoverable repairs · both feed the next-gen DETECT corpus. The chain catches it · the validator names it · the deed records it · the discipline holds.*
