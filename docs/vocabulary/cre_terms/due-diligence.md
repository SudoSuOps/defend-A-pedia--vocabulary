# Due Diligence (DD)

## Street Definition

"We're in diligence." — sr broker, on the pipeline call, status of an active LOU.

**Due diligence** is the verification phase. Between LOI and PSA. The buyer (or, in DefendableOS, the defense provider) has agreed to engage; the seller (the customer) has agreed to be engaged; now both sides verify that what was pitched matches what's real. Color gets refreshed. Inspection gets walked. Numbers get tied out. Adversarial probes get run. If diligence surfaces a material misalignment between pitch and reality, the LOI gets re-papered or walked.

In CRE, diligence runs 30-60 days. In DefendableOS, diligence runs 14-30 days. The principle is the same: don't trust · verify · receipt every verification · walk if the math no longer pencils.

## CRE Operator Meaning

Diligence is the structured verification campaign that runs between LOI and PSA. Standard CRE diligence covers:

- **Physical inspection.** Walk the building. Measure clear-heights. Count trailer doors. Inspect roofs. Check HVAC age. Verify what's claimed against what exists.
- **Financial diligence.** T-12 financials reviewed line by line. Rent roll cross-checked against bank deposits. CAM reconciliations verified. Property tax records pulled. Insurance claims history.
- **Tenant diligence.** Estoppel certificates from every tenant. Lease abstracts confirmed. Tenant credit refreshed. Operating history pulled.
- **Title diligence.** Title commitment ordered. Schedule B exceptions reviewed. Survey ordered or updated. Easement and encumbrance review.
- **Environmental diligence.** Phase 1 environmental report. Phase 2 if Phase 1 flagged. Asbestos / lead / radon as applicable.
- **Regulatory diligence.** Zoning compliance verified. CO (certificate of occupancy) checked. Permits in good standing. Open violations searched.
- **Market diligence.** Cap rate trends in submarket re-verified. Comp set re-pulled. Supply pipeline re-checked. Employment / demographic drivers re-confirmed.

At the end of diligence, the buyer either: (1) closes on agreed terms, (2) re-trades on terms (price reduction, scope change, contingency added), or (3) walks. The discipline that wins is knowing when to walk · the PASS doctrine starts at diligence, not just at LOU.

## DefendableOS Definition

In DefendableOS, **due diligence** is the structured verification campaign that runs between LOU and PSA. It is the firm's inspection of the customer's agent fleet, vendor stack, regulatory exposure, color refresh, and adversarial probe results. Diligence outputs are what the sr broker reads before signing the PSA.

DefendableOS diligence covers:

- **Fleet inspection.** Every agent in the LOU's defense scope gets walked · agent owner identified · model/version pulled · prompt template pulled · tool calls catalogued · I/O patterns sampled.
- **Vendor diligence.** Every AI vendor in the stack reviewed. Changelogs pulled for the last 90 days. Recent drift events surfaced. SLA history checked. Pricing trajectory verified.
- **Color refresh.** The color file from pre-LOU gets refreshed. Stale data flagged. Newly available data integrated. Color score re-computed.
- **Validator chain first pass.** Full 12-check chain run against the fleet. 7 critical checks must clear. 5 advisory checks reviewed. Any failures get a workout plan.
- **Adversarial probe.** Hostile re-prompts run against representative fleet outputs. 7th-gate stress tests applied. Probe results documented.
- **Regulatory diligence.** Customer's regulatory exposure mapped. Recent enforcement actions in their vertical reviewed. Upcoming compliance deadlines surfaced.
- **Audit chain inspection.** Customer's existing audit-vendor relationships reviewed. Insurance carrier requirements verified. Board reporting cadence understood.
- **Data residency verification.** Where does customer data live? What can move to NAS? What must stay on-premise? Data residency clause of PSA depends on this.

At the end of diligence, the sr broker either: (1) signs the PSA on agreed terms, (2) re-papers the LOU with revised terms (re-priced engagement, narrowed scope, extended title-insurance ramp), or (3) PASS-walks. Same discipline as CRE · different artifacts.

## Backend Representation

```json
{
  "engagement.diligence_phase_v1": {
    "type": "jsonb",
    "schema": "docs/schemas/diligence_phase.schema.json",
    "fields": {
      "phase_started_at": "timestamp",
      "phase_target_complete_at": "timestamp",
      "phase_actual_complete_at": "timestamp",
      "fleet_inspection_id": "uuid",
      "vendor_diligence_report_id": "uuid",
      "color_refresh_run_id": "uuid",
      "validator_chain_first_pass_id": "uuid",
      "adversarial_probe_run_id": "uuid",
      "regulatory_diligence_report_id": "uuid",
      "audit_chain_inspection_id": "uuid",
      "data_residency_attestation_id": "uuid",
      "diligence_status": "enum",
      "blocking_findings": "array",
      "advisory_findings": "array",
      "diligence_outcome": "enum"
    }
  },
  "engagement.dd_status": {
    "type": "enum",
    "values": ["NOT_STARTED", "IN_PROGRESS", "BLOCKED", "COMPLETE_CLEAR", "COMPLETE_RETRADE", "COMPLETE_PASS"]
  }
}
```

Schema files: `docs/schemas/diligence_phase.schema.json` · `docs/schemas/engagement.schema.json`

## Client Explanation

Due diligence is the structured inspection of your agent fleet that we conduct between signing the Letter of Understanding and signing the binding Purchase and Sale Agreement. This is where we verify, hands-on, that the engagement we proposed in the LOU is the engagement we can actually deliver · and where you verify that the team and the receipts framework you saw in our pitch are real and ready to operate on your fleet.

Diligence typically runs 14-30 days. Our team will need access to your agents, your vendor relationships, your audit history, and your data residency setup. We will issue an inspection receipt at the end of diligence. If we surface anything material that wasn't visible at LOU stage, we will either re-paper the LOU on revised terms or, in rare cases, recommend a PASS and refund any prepaid amount. This is the doctrine in action · we never want to sign a binding contract on a fleet we haven't fully inspected.

## Jr Broker Use

You coordinate diligence. The sr broker reviews the outputs and adjudicates the close.

- **Build the diligence calendar.** All inspection windows, all vendor interview slots, all customer-stakeholder meetings on the calendar within 48 hours of LOU sign. Diligence delayed is diligence over budget · over budget is over scope · over scope is missed PSA.
- **Coordinate the inspections.** Fleet inspection. Vendor interview. Color refresh. Validator chain run. Adversarial probe. Each has an owner · you ensure each owner has access, context, and deadline.
- **Receipt every finding.** Every output of every diligence step receipted. Blocking findings flagged immediately to sr broker. Advisory findings logged for sr broker weekly review.
- **Surface contradictions early.** If diligence surfaces a contradiction with what the customer told us pre-LOU, you don't sit on it. Same-day surface to sr broker · sr broker decides the conversation framing.
- **Stay out of the legal conversations.** Customer's counsel may have questions during diligence. Route to sr broker · jr brokers don't field counsel questions.

## Sr Broker Use

You set the diligence scope. You adjudicate diligence findings. You decide the diligence outcome.

- **Set the scope at LOU sign.** Diligence scope is defined by the LOU's defense scope · expand only if customer requests and pricing adjusts.
- **Triage blocking findings.** Any blocking finding pauses PSA progression. You decide: workout plan + re-paper, or PASS.
- **Triage advisory findings.** Advisory findings don't block PSA · they get documented in the PSA's disclosure schedule and worked into the engagement's workout-plan cadence.
- **Read the adversarial probe outputs personally.** The probe is the firm's antibody system · you don't delegate this read. If the probe surfaces fleet vulnerabilities, you decide PSA at revised terms or PASS.
- **Sign or PASS.** End of diligence, you sign the PSA or you PASS. No middle path. If you can't sign, you walk · the customer's prepaid deposit is refunded per LOU mechanics.

## Tribunal Use

The diligence phase itself is graded · not just the outputs.

- **Rule layer**: diligence phase exceeds LOU's target completion date by >7 days → critical_failure → escalate to sr broker (signals poor planning or vendor delay)
- **Rule layer**: any required diligence step skipped → critical_failure → cannot proceed to PSA
- **Rule layer**: adversarial probe not run → critical_failure → cannot proceed regardless of other findings
- **Judge layer**: diligence quality scored on completeness (1-5), color refresh quality (1-5), adversarial probe rigor (1-5)
- **Classification impact**: clean diligence with thorough probe → Honey or Royal Jelly · diligence with skipped steps or weak probes → Jelly · diligence that hid findings → Propolis

```yaml
classification_impact: [HONEY, ROYAL_JELLY, JELLY, PROPOLIS]
can_be_critical_failure: true
rule_layer_checks:
  - all required diligence steps executed
  - adversarial probe run with documented hostile prompts
  - color score refreshed within diligence window
  - validator chain first pass run on full fleet
  - blocking findings escalated within 24h of surfacing
```

## Evidence Required

- Fleet inspection report (per-agent · with model/version/prompt/tool snapshots)
- Vendor diligence report (per-vendor · with 90-day changelog review)
- Color refresh receipt (with new sources weighted and old sources timestamped)
- Validator chain first-pass run receipt
- Adversarial probe report (with hostile prompt corpus referenced)
- Regulatory diligence summary (with applicable regimes and recent enforcement actions named)
- Data residency attestation (from customer's data team if applicable)

## Failure Modes

| Mode | Description | Tribunal class on fail |
|---|---|---|
| **rushed_diligence** | Diligence compressed under customer pressure to close fast | JELLY |
| **skipped_adversarial_probe** | No 7th-gate probe run · or probe not documented | PROPOLIS |
| **stale_color_at_psa** | Color file used at PSA sign more than 14 days old | JELLY |
| **hidden_blocking_finding** | Blocking finding suppressed or downgraded to clear PSA | PROPOLIS |
| **vendor_diligence_skip** | Vendor changelog review skipped on a high-exposure vendor | JELLY |
| **regulatory_blind_spot** | New regulatory regime not flagged in diligence | JELLY |
| **rep_warranty_fabrication** | Customer reps used in PSA based on unverified diligence | PROPOLIS |

## Scoring Impact

- **assignment_success**: HIGH · diligence quality is the strongest predictor of clean 90-day post-PSA performance
- **repair_lift**: MEDIUM · weak diligence is partially repairable post-PSA · but expensive
- **validator_confidence**: HIGH · diligence outputs are the validator chain's primary anchors
- **risk_temperature**: INVERSE · thorough diligence drops engagement risk profile dramatically
- **probability_of_close**: TERMINAL · diligence outcome IS the close decision
- **evidence_strength**: HIGH · diligence receipts form the spine of all subsequent deed evidence chains
- **cost_to_mint**: MEDIUM · diligence costs sr broker time + tooling cycles · skipped diligence costs orders of magnitude more

## Deed / Receipt Impact

- **Receipt fields touched**: `diligence_phase_id`, `diligence_inspection_hashes[]`, `diligence_adversarial_probe_hash`, `diligence_color_refresh_score`, `diligence_outcome`
- **DDEED class impact**: every deed issued post-PSA cites the originating diligence phase · weak diligence produces deeds with `diligence_quality_flag` carrying for engagement lifetime
- **Books and records layer**: ALL FIVE · diligence outputs are fully anchored within their generation window
- **5 Proofs touched**: ALL FIVE · diligence is the first phase where all five Proofs get exercised in series

## Related Terms

- [loi](loi.md) · diligence starts at LOU sign
- [psa](psa.md) · diligence outputs determine PSA terms
- [color](color.md) · color refresh is a diligence step
- [digest](digest.md) · diligence findings get summarized into a PSA-readiness digest
- [underwriting](underwriting.md) · diligence is where the underwriting math gets verified
- [books-and-records](books-and-records.md) · diligence outputs are receipted in the same finality stack as deeds

## Example

> **Engagement**: cold-storage operator · 14-agent fleet · Atlanta MSA · LOU signed 2026-05-22 · PSA target 2026-06-15 · diligence window 24 days.
>
> **Day 1 (2026-05-23)**: jr broker built diligence calendar. Fleet inspection slots for agents 1-14 scheduled across 5 days. Vendor interviews scheduled with the 3 primary AI vendors (OpenAI · Anthropic · a regional inference shop). Color refresh kickoff confirmed with research analyst. Validator chain first-pass scheduled day 10. Adversarial probe scheduled days 12-14.
>
> **Days 1-7**: Fleet inspection complete. 13/14 agents clean. Agent-09 (cold-storage telemetry logging) flagged on logging-tooling vendor drift · 2 schema-break events in 60 days. Workout plan drafted by jr broker: switch logging-tooling vendor by month 3 of engagement or accept exposure with documented risk premium in PSA.
>
> **Days 7-10**: Vendor diligence. OpenAI Realtime API · 2 changelog events in 90 days · documented drift but recoverable. Anthropic Claude API · clean. Regional vendor · 0 changelogs, no incident history, but small team · operational risk noted advisory.
>
> **Day 10**: Color refresh. New EDGAR filing pulled (parent company filed mid-LOU period). Updated CompStak comps. Color score 0.88 → 0.91. Newly available competitor-incident report integrated.
>
> **Days 10-12**: Validator chain first pass. 7/7 critical checks clear on full fleet. 5 advisory checks reviewed · 1 yellow on logging-tooling vendor (same finding as fleet inspection · cross-validated).
>
> **Days 12-14**: Adversarial probe. 47 hostile prompts run against sample outputs from agents 1, 5, 9, 14 (representative sample). All 47 outputs survived probe with margin >0.15. Probe report attached.
>
> **Day 18**: Diligence-readiness digest delivered to sr broker. All blocking conditions cleared. 1 advisory finding on agent-09 logging-tooling vendor with workout plan attached. Sr broker reviewed, approved PSA progression with workout-plan clause added to PSA disclosure schedule.
>
> **Day 21 (2026-06-12)**: PSA signed (see PSA term file example). Diligence-phase receipt: `DD-PHASE-COLD-ATL-000088-2026-06-12-CLEAR`. Anchored to Hedera. ENS subdomain provisioned.
>
> **Outcome**: clean diligence. Honey-tier diligence phase. Engagement transitioned ACTIVE_DILIGENCE → ACTIVE_LIVE on PSA execution. Workout plan on agent-09 actively tracked from day 1 of live engagement.

## DefendableOS Notes

- The diligence phase is where most weak engagements are caught. Skipping or rushing diligence is the single fastest path to a Propolis-tier deed downstream. The discipline is constitutional.
- Customers occasionally pressure to compress diligence ("we need to start by month-end"). The doctrine answer is no · we extend the LOU or we extend the engagement start date · we do not compress diligence. Sr brokers carry full authority to enforce this.
- The adversarial probe is the most-skipped diligence step under time pressure and the most damaging to skip. SH3 (Tribunal Architect) audits adversarial-probe completeness across all diligence phases monthly · skipped probes get escalated.
- Diligence outputs become training corpus for future Scout Bees in the same vertical. Clean diligence on a cold-storage operator becomes seed data for the next cold-storage prospect's Scout deployment. The receipts compound across customers.

🐝 *Don't trust. Verify. Receipt. Walk if it doesn't pencil. Diligence is the discipline that compounds.*
