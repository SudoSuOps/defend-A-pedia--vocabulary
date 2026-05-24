# Validator Chain Doctrine · The 12-Check Rule Layer

> *"The validator chain is title insurance for AI output. Twelve checks. Seven are stop-the-deal critical. Five are advisory. If you can't clear the chain, you don't get to close."*
> — Founder · CRE-broker framing of the validator stack

---

## What the validator chain is

The validator chain is the rule layer the Tribunal Filter runs BEFORE any LLM judge sees the pair. It is 12 deterministic checks · 7 critical · 5 advisory. Each check is a named function (C01 through C12) · each function is auditable · each function logs a pass/fail with a reason string.

This is the structural integrity layer. A pair that does not clear the critical checks (C01-C07) cannot become Honey. Cannot become Royal Jelly. Cannot become a deed. The judges never get to weigh in · the rule layer has already adjudicated.

This is what makes the Tribunal more than a vibes-check. The judges adjudicate the soft questions (was the reasoning sound · did it answer the prompt · is the depth appropriate). The validator chain adjudicates the hard questions (does the record exist · is the source retrievable · was operator consent captured · did anyone redact a secret). The hard questions are not opinion · they are facts. Facts get rule-layer treatment.

---

## The 12 checks (locked production sequence)

| # | Check | Type | What it verifies | Fail mode |
|---|---|---|---|---|
| **C01** | pair record present | CRITICAL | A PairCandidate JSON exists · is well-formed · parses against `pair_candidate.schema.json` | PROPOLIS · cannot proceed |
| **C02** | source artifact referenced | CRITICAL | Every claim in the output has at least one source pointer (URL · doc_id · EDGAR accession · etc.) | PROPOLIS · cannot proceed |
| **C03** | source retrievable | CRITICAL | At least one source pointer resolves successfully (HTTP 200 · doc fetched · accession valid) within a 30-day cache window | PROPOLIS unless cached evidence in vault · then Jelly |
| **C04** | tribunal label assigned | CRITICAL | The pair carries a `tribunal_label` field (HONEY / JELLY / PROPOLIS) post-judge · OR a `judges_pending` flag if pre-judge | PROPOLIS · cannot deed without a verdict |
| **C05** | no hard-fail flagged | CRITICAL | No hallucination_event · no schema_break · no tool_misuse flagged on the record | PROPOLIS · the hard-fail is the verdict |
| **C06** | PROPOLIS not promoted | CRITICAL | If `tribunal_label == PROPOLIS` · the deed-writer queue is rejected · sealed instead | Hard reject from deed pipeline |
| **C07** | holdout contamination guard | CRITICAL | The pair is NOT in any known eval-holdout set (cross-referenced against `holdout_manifest.jsonl` · 5 known holdouts as of 2026-05-24) | PROPOLIS · pair sealed · do not train · do not deed |
| **C08** | operator consent | ADVISORY | An operator (jr broker · sr broker · validator) has marked the engagement consent flag for this pair | Advisory penalty · -0.05 score · annotate `consent_missing` |
| **C09** | redaction status | ADVISORY | The pair has been scanned for PII · secrets · API keys · customer-identifying data · result logged | Advisory penalty · -0.05 score · annotate `redaction_status` |
| **C10** | transition audit log | ADVISORY | Every state change (Scout → Router → Filter → judge → tier) was logged to `tribunal_transitions.jsonl` | Advisory penalty · -0.03 score · annotate `audit_gap` |
| **C11** | SHA-256 recorded | ADVISORY | The canonical-JSON record_hash is computed and persisted to Bakery manifest | Advisory penalty · -0.02 score · annotate `hash_missing` · auto-retry hash compute |
| **C12** | no secrets in pair | ADVISORY · also a SAFETY GATE | Regex + entropy scan for AWS keys · API tokens · private keys · password strings · cardholder PANs | If detected · pair is BLOCKED from any persistence layer until secrets are scrubbed · then re-Scouted as a fresh pair |

The 7 critical checks (C01-C07) can stop a deed cold. The 5 advisory checks (C08-C12) can downgrade confidence but cannot block. C12 has a special status · it is technically advisory in scoring impact but is a hard safety gate · a pair with detected secrets does not get written anywhere until those secrets are stripped.

---

## Why these twelve · and not more · and not less

The validator chain was bootstrapped from three sources:

1. **CRE due diligence checklists** · the 7 critical checks mirror the CRE title-insurance underwriting workflow (does the deed exist · is the chain of title clear · is the survey current · is the encumbrance disclosed · is there a pending lien · is the entitlement transferred · is the holdout-buyer protected). One-for-one CRE-to-software mapping.
2. **SOC2 / NIST audit controls** · the 5 advisory checks pull from operator-consent · data-retention · audit-log discipline that any SOC2 Type II auditor expects to see.
3. **Royal Jelly Protocol upstream** (virgin-jelly · cell-level provenance) · the SHA-256 manifest discipline and the holdout contamination guard come from the JellyScore production pipeline.

12 was the operator-tested number. Below 10, you start missing real failure modes (the agenthash 5-bucket study showed `RECOVER` and `LOOP` failures slip past 9-check chains). Above 14, you create operator fatigue and the checks themselves start drifting. 12 is what fits on one page of the broker's flight sheet · 12 is what a jr broker can memorize by week 2 · 12 is what the rule layer can execute in under 80ms per pair (which is what gets us to 777 pairs/hr throughput).

---

## Critical vs advisory · the operating difference

| Dimension | Critical (C01-C07) | Advisory (C08-C12) |
|---|---|---|
| Effect on tier | Forces PROPOLIS (or in C03 cached case · Jelly) | Score penalty · max -0.05 each |
| Operator action | STOP THE DEAL · investigate · fix or seal | Annotate · flag · do not block ship |
| Override allowed | No · founder-locked | Yes · with sr broker sign-off + reason logged |
| Logged where | tribunal_verdict.record_hash · ALWAYS | tribunal_verdict.advisory_annotations · ALWAYS |
| 5 Proofs touched | QUALITY (always) · PROCESS (always) · TRUST (when override happens) | QUALITY · PROCESS |

The critical checks are non-negotiable. A sr broker cannot override C01-C07. The founder cannot override C01-C07. The only way to clear a C01-C07 fail is to fix the underlying defect and re-Scout the pair as a fresh PairCandidate. This is the structural discipline.

The advisory checks are operator-tunable. A sr broker can sign off on a C09 redaction-status advisory fail with a logged reason (e.g., "PII scan was offline · manual review completed · no PII present"). Every override is logged · every override is auditable · every override gets reviewed in the weekly check.

---

## Escalation paths

When a check fails · what happens next is defined by the failure type:

### Critical fail (C01, C02, C04, C05, C06)
- Pair is short-circuited to PROPOLIS
- PropolisCollector ingests the pair into the failure corpus
- Operator gets a notification on the Morning Brief (next day 06:00)
- No further action required unless the failure rate exceeds the threshold (see below)

### Critical fail (C03 · source retrievable)
- If a cached copy of the source exists in `evidence_vault/cached_sources/` (within 30-day window) · pair is downgraded to Jelly · routed to SwarmFixer for source-refresh
- If no cache exists · pair is PROPOLIS · sealed

### Critical fail (C07 · holdout contamination)
- Pair is PROPOLIS · sealed · WITH a `contamination_alert` flag
- Sr broker gets paged immediately (this is the highest-severity event in the Tribunal)
- The cook batch that produced the pair is held · audited · the corpus is re-validated against the full holdout manifest before any further deeds issue from that batch
- If contamination is systemic · the cook is rolled back · the writer model is NOT trained on that batch

### Advisory fail (C08-C12)
- Pair proceeds with score penalty applied
- Annotation written to verdict record
- Aggregated in the weekly check · if any advisory check fail rate exceeds 5% · sr broker investigates root cause
- C12 (secrets) is special · pair is BLOCKED from persistence · operator must scrub secrets and re-Scout

### Systemic failure rate triggers
- If any single critical check fails on > 2% of pairs in a 24-hour window · Tribunal goes into degraded mode · all deeds held for sr broker review until the upstream cause is identified
- If C07 fires AT ALL · the entire cook batch is held pending audit · no degradation tolerance for holdout contamination

---

## How the chain integrates with the Tribunal pipeline

```
Scout fetches pair
       │
       ▼
Router picks lane
       │
       ▼
Filter runs C01 → C02 → C03 → C04 → C05 → C06 → C07
       │
       ├── any CRITICAL fail → PROPOLIS or Jelly · pipeline halts
       │
       ▼
Filter runs C08 → C09 → C10 → C11 → C12 (advisory · annotates only)
       │
       ▼
Scale A judge runs → score + reason
       │
       ▼
Scale B judge runs → score + reason
       │
       ▼
Drift check / Critic / Katniss as needed
       │
       ▼
PENALIZED SCORING applied → final tier
       │
       ▼
Verdict record assembled · advisory annotations attached · record_hash computed
       │
       ▼
Routed: Royal Jelly → DDEED · Honey → receipt · Jelly → SwarmFixer · Propolis → seal
```

The chain is deterministic · the order is locked · the checks do not skip. This is the audit trail. This is what defends the deed.

---

## What the chain enables

When the validator chain runs clean end-to-end:

- A deed can be issued with full confidence that the source is real · the operator consented · no secrets leaked · no holdout was poisoned
- A customer can be told "the chain cleared" and that statement is verifiable from the record_hash
- An auditor (KPMG · SOC2 · regulatory) can replay the chain from the verdict record and reach the same answer
- A future model trained on the resulting corpus is not contaminated · not consent-violating · not source-fabricated
- The books-and-records reconcile

When the chain fails and the failure is sealed properly · the Hive still benefits · the propolis vault grows · the DETECT-task training data for the next SwarmFixer cohort gets richer. No waste in a Hive.

---

## What the chain is not

- **It is not a substitute for the judges.** Rule layer answers fact questions. Judges answer judgment questions. You need both.
- **It is not a CI check.** It runs at inference time on every live pair · not just at batch time.
- **It is not optional for production deeds.** Every DDEED that ships carries a verdict record that includes the C01-C12 results. No exceptions.
- **It is not opaque.** Every check has a named function · a reason string on fail · a regression test in `tests/validator_chain_test.py`. An operator can replay any check on any pair.

---

## Read next

- [`08_tribunal_doctrine.md`](08_tribunal_doctrine.md) · how the chain integrates with the 6-role Tribunal
- [`07_honey_royal_jelly_propolis.md`](07_honey_royal_jelly_propolis.md) · what tier each fail mode lands a pair in
- [`../playbooks/tribunal_review_playbook.md`](../playbooks/tribunal_review_playbook.md) · the operator workflow for reading verdicts
- [`../vocabulary/tribunal_terms/validator-chain.md`](../vocabulary/tribunal_terms/validator-chain.md) · the term file
- [`../vocabulary/tribunal_terms/validator.md`](../vocabulary/tribunal_terms/validator.md) · the auditor-bee role

🐝 *Twelve checks. Seven critical. Five advisory. Run them in order. Log every result. The chain is title insurance for AI output.*
