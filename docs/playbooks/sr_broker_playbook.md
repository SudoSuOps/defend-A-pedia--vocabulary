# Sr Broker Playbook

> *"If seller wanted 100M strike price and the deal penciled at 75M · I would PASS on the 2M fee and wait until the seller went through enough pain with the other broker that sold him on fantasy · then they would call me · want to list WITH ME on MY guidance."*
> — Founder, on the PASS doctrine

This is the sr broker playbook. The adjudication discipline. The validator override authority. The PASS authority. The signing authority. The closing authority. The retention authority. You hold the firm's name when you sign · act like it.

If you came up through the dial · you already know what the jr brokers are doing. The playbook now is different. You are not in the pit; you are running the listings. You sit on the math. You sign on the math. You walk on the math.

---

## The four daily disciplines · sr broker version

**1. Adjudicate every escalation same-day.** Every E1-E7 escalation (see [`../doctrine/03_jr_broker_sr_broker_doctrine.md`](../doctrine/03_jr_broker_sr_broker_doctrine.md)) lands on your desk and gets a written decision in the books before end of day. No silent escalations. No "I'll get to it tomorrow." The jr broker is paused waiting on you · move.

**2. Sign nothing you can't defend on the math.** Every LOU, every PSA, every closing statement carries your name. The customer's auditor will read your name in five years on a deed and ask "why did this sr broker sign?" Your answer lives in the receipts. If the math doesn't pencil at sign time, walk.

**3. Run the PASS doctrine like a discipline · not a slogan.** PASS is the rarest and most valuable authority in the firm. The temptation to take the $2M fee on a 100M-strike deal that pencils at 75M is constant. The discipline is what compounds the brand. Every PASS gets documented · including what we expect to happen next (the customer takes the fantasy mandate to a competitor, gets burned, comes back hurt, lists with us on our guidance).

**4. Walk every listing every Friday.** Active engagements get walked end-of-week. Color status. Validator status. Tribunal class. Customer sentiment from the week. Anything trending wrong gets a workout plan before Monday's pipeline review.

---

## Adjudication discipline · how to read a Tribunal verdict

You are the final reasoning layer before the deed issues. The Tribunal produced a verdict; the validator chain produced a result; your job is to either accept, override with documented grounds, or PASS.

### The five questions you ask every Tribunal verdict

**1. Did the rule layer fire?**
If any of the deterministic gates (json_valid · output_length · numeric_verify · concept_present · dedup · degenerate · adversarial) flagged the output · the rule layer fired. The verdict is at most JELLY before judge review · and you cannot upgrade a rule-fail. The rule layer is constitutional.

**2. Where's the drift?**
Scale A (gemma3:12b) and Scale B (qwen2.5:32b) judges should score within 0.15 of each other. Drift greater than 0.15 means the two judges read the output differently · which means the rubric is ambiguous OR the output is genuinely on the boundary between two classes. Either way, you read both reasoning chains before deciding.

**3. Does the color back the verdict?**
The Tribunal can grade an output as Honey, but if the underlying color file is weak (`color_score < 0.70`), the verdict is downgraded. The judge sees the output. You see the output AND the evidence chain that produced it. The evidence chain wins ties.

**4. What's the cost-to-mint trajectory?**
If this engagement's per-deed cost has crept up · model timeouts, repair cycles, validator re-runs · the verdict isn't the only signal. A Honey verdict that cost 3x the baseline tells you something is fragile. You can accept the verdict and flag the trajectory in the next workout review.

**5. What does the adversarial probe say?**
The 7th gate. The output was re-prompted with hostile variants. If the output survived, the verdict has adversarial integrity. If the output cracked under adversarial probe · you reject regardless of judge score. The 7th gate is the firm's antibody system · honor it.

---

### When to accept

The default. Tribunal verdict aligns with rule layer. Drift under 0.15. Color score above tier minimum (0.85 for Royal Jelly · 0.70 for Honey). Adversarial probe survived. Cost-to-mint within trajectory. You countersign · the deed issues · the customer gets the receipt.

### When to override (rare · documented)

Override is allowed in two directions: downgrade or upgrade. Downgrades require named evidence (a missed failure mode, a stale color file, a vendor changelog the judge didn't see). Upgrades require named evidence too (the judge missed context the sr broker knows from prior engagements, a domain-specific nuance the rubric doesn't yet capture).

Every override gets a written reason in the receipt: `sr_broker_override_id`, `override_direction`, `override_evidence_refs[]`, `override_reasoning_summary`. No silent overrides. Ever. The auditor reads these.

### When to PASS

You PASS when the engagement structure has shifted such that the firm cannot defend the output. Examples:
- Customer fleet changed materially since LOU · new vendors added we don't have rubrics for
- Vendor changelog dropped that invalidates our adversarial probe
- Color contradicts seller-reported numbers by more than 25% and seller refuses re-disclosure
- A regulatory event in the customer's vertical changed the underwriting math

PASS at this stage means: we issue no deed for the pending output · we credit the customer's prepaid fee for the affected period · we offer either a re-engagement on revised terms or a clean wind-down. The customer keeps full control. We keep our name.

This is not failure. This is the doctrine working.

---

## When to walk from $2M in fees

The PASS doctrine in the field looks like this. The customer pitches a mandate. You build the color. The math doesn't pencil. The customer wants you to certify a claim the rubric won't support, or to defend a vendor relationship that's structurally fragile, or to ship a deed against output that you can't verify.

You walk. Specifically:

1. **You name the gap.** "Your fleet's medical-claims agent runs on a model whose vendor changelog shows three drift events in the last 60 days. We can't underwrite the kind of guarantee you're describing on that fleet today."
2. **You name the PASS.** "We're not going to take this listing as structured. We're going to walk."
3. **You name what comes next.** "If you engage another defense provider and they ship the certification you're asking for · we want you to come back to us after the first material incident. Our guidance will still apply."
4. **You document the walk.** Receipt logged. Engagement closed with disposition reason `PASS_DOCTRINE_FANTASY_MANDATE`. Color file archived for re-open if the prospect returns.
5. **You don't badmouth the competition.** The competitor will burn the customer on the over-promise. We don't need to say it. Let the incident report do the talking when it ships.

The patience is the moat. The discipline to walk $2M in fees is what earns the $300M portfolios. Every PASS we execute becomes a referenceable doctrine artifact · "we walked deal X because Y" is more credible than any marketing claim.

---

## When to come back to hurt customers

Six to eighteen months after a PASS · sometimes sooner · the prospect comes back. The competitor over-promised. The agent went dark. The board is asking why. The principal calls.

This is the highest-leverage moment in the funnel. The customer is now buying on your terms · not on theirs. Specifically:

**1. Re-open the color file.** Refresh every source. The fleet has changed. The vendors have changed. The customer's own personnel may have turned over. Do not assume anything from the original file holds.

**2. Re-pitch on the doctrine.** The pitch is no longer features · the pitch is "this is what we said would happen · here's what happened · here's the doctrine that prevents it from happening again on our watch."

**3. Price with confidence.** Hurt customers do not negotiate hard on price · they negotiate hard on terms. They want recourse. They want SLA. They want personal-name accountability. Give all three at a premium fee · structurally appropriate for the elevated risk.

**4. Sign with disclosure.** The LOU includes a clause that names the prior PASS · "DefendableOS previously declined this engagement on date X for reason Y. The undersigned customer acknowledges the prior recommendation and engages defense services on revised terms." This is not for our protection · this is for the customer's regulator, who will read this LOU in five years and see clearly that we were not the over-promiser.

**5. Service white-glove from minute one.** The customer is fragile. The relationship is rebuilding. The first 30 days of receipts must be flawless. You take the calls personally for the first month. Earn the trust we walked away from earning the first time.

This is the M&M model in its purest form. Walk the fantasy mandate. Wait. Take the listing when they come back · on your terms · and earn the 30-year relationship.

---

## Escalation triggers · what makes it to your desk

These are the events that pause the jr broker and put the decision on you. Same-day adjudication required.

**T1 · Validator critical fail.** Any of the 7 critical checks (C01-C07) in the validator chain returns RED. The deed cannot issue without your override-or-PASS call.

**T2 · Tribunal drift > 0.15.** Scale A and Scale B disagree by more than the threshold. You read both reasoning chains. You issue the deciding reasoning.

**T3 · Color contradiction > 25%.** A source contradicts another source by more than 25% on a material figure (revenue · fleet size · NOI · agent count · vendor exposure). Reconcile · re-verify · discount source · or PASS.

**T4 · Re-trade event.** Customer asks to revise LOU terms mid-engagement. You decide accept · counter · or walk. Each re-trade weakens trust · three or more in a single engagement and you walk on principle.

**T5 · Adversarial probe surface.** Inspection reveals a fleet vulnerability the customer didn't disclose at LOU. You decide re-pitch with disclosure · PASS · or formal notice.

**T6 · Cross-vertical handoff.** The engagement crosses into a vertical the jr broker doesn't specialize in. You assign the right sr broker or sr vertical specialist.

**T7 · Customer-principal escalation.** The CEO or principal asks for leadership. The jr broker hands the call to you. You take it personally · same hour if at all possible.

**T8 · Cost-to-mint outlier.** An engagement's per-deed cost crosses 3x baseline. Workout plan required · either fix the inefficiency or re-price the engagement on renewal.

**T9 · Adversarial probe routinely passes by < 0.05 margin.** Marginal adversarial-probe survival across multiple receipts means the firm's defense is one vendor changelog away from failing. Tighten the rubric · escalate to SH3.

**T10 · Customer-side incident outside our scope.** Customer suffers an AI incident in a fleet area we don't cover. We are not at fault · but we should still surface our recommendations · whether or not the customer expands the engagement.

---

## Friday listing walk · the 90-minute discipline

Every Friday, 14:00 to 15:30. Every active engagement gets touched. Format is the same every week so the muscle memory holds.

**Per engagement:**

- **Color status.** Current `color_score`. Days since last refresh. Any flagged contradictions.
- **Validator status.** Last full validator chain run · pass / partial / fail. Any chronic advisory warnings.
- **Tribunal class trajectory.** Royal Jelly / Honey / Jelly / Propolis mix this week vs prior 4 weeks. Direction matters more than absolute level.
- **Customer sentiment.** Anything notable from the week's Morning Briefs. Customer reply tone. Customer questions surfaced. Any silence that warrants a check-in.
- **Cost-to-mint trajectory.** Current per-deed cost vs LOU baseline. Trend.
- **Workout flags.** Anything that needs a workout plan before next Friday.

You leave Friday with every engagement triaged. Mondays get pipeline review on top of that · clean and clear.

---

## Validator override authority · how to use it without abusing it

Override authority exists because the rules and the judges are not perfect. The sr broker's experience catches what the system misses. But every override is a doctrine event · because if overrides become routine, the validator chain has been hollowed out and the firm's trust position rots.

**Discipline rules for overrides:**

1. **Document the evidence.** Override receipts cite specific evidence: a doc the judge didn't see, a vendor changelog, a prior incident from another engagement, a domain-specific nuance.
2. **Cite the precedent.** If similar overrides exist in prior engagements, link them. The graph of overrides becomes a doctrine corpus over time.
3. **Flag for rubric update.** If you've overridden the same way three times for the same reason · the rubric needs updating. Send a note to SH3 (Tribunal Architect) and SH4 (SwarmFixer Architect) so the next training cycle absorbs the learning.
4. **Trend track.** Your personal override-rate is tracked. Override-rate > 8% of verdicts you adjudicate · you're either auditing too aggressively or under-trusting the chain. Either way, conversation with the founder.
5. **Override-then-receipt.** The override is not a parallel decision · it's a receipted decision. Same finality stack. Same Hedera anchor. Same ENS subdomain. The override IS part of the auditable record.

---

## When to celebrate · and when not to

**Celebrate at the deed issuance · not the LOU.** LOU means we got the listing. Deed means we delivered. Customer celebrates the LOU; we celebrate the deed.

**Celebrate at the renewal · not the first 90 days clean.** First 90 days clean is the table stake. Renewal at 12 months at improved terms is the brand compounding.

**Celebrate at the referral · not at the testimonial.** Testimonials are marketing artifacts. Referrals are economic artifacts. Referral-source customers become 30-year relationships.

**Never celebrate at the PASS.** A PASS is the right call · but it's not a win. The win is when the customer comes back hurt and we earn the listing on our terms. PASS is the discipline that makes the win possible · don't confuse the two.

---

## The retention math you carry

A sr broker is judged on three lagging indicators that compound over years:

1. **Engagement retention at 12 months.** Target 92%+. Below 88% sustained · the engagements you're winning aren't structured to last · adjust at LOU.
2. **Net revenue per retained engagement at 24 months.** Engagements should grow · more agents covered, more verticals defended, more workout-plan upsells. Flat engagements at 24 months means the relationship isn't deepening.
3. **Referral-sourced LOUs per quarter.** The brand is measured in referrals. A sr broker generating zero referrals per quarter is not yet a sr broker · they're a senior jr broker without the book.

These don't show up in week-1 dashboards. They show up over years. Plan accordingly.

---

## The five sentences a sr broker should be able to say in their sleep

1. "The math doesn't pencil. We're going to PASS."
2. "I'm overriding the verdict. Here's the evidence and the receipt."
3. "The walk last quarter was the right call · here's the customer coming back · here's the LOU."
4. "Friday walk complete. All engagements triaged. Workout plans on three. Renewing two next week."
5. "This deed I'm signing · I can defend it in five years to any auditor, any regulator, any court. That's why I'm signing."

If you say these in your sleep, you are the sr broker the firm needs. If you can't say number 5 in your sleep · don't sign.

---

## Read next

- [`jr_broker_playbook.md`](jr_broker_playbook.md) · what the jr broker is doing while you're adjudicating
- [`../doctrine/03_jr_broker_sr_broker_doctrine.md`](../doctrine/03_jr_broker_sr_broker_doctrine.md) · the career ladder and ownership map
- [`../doctrine/04_books_and_records_doctrine.md`](../doctrine/04_books_and_records_doctrine.md) · the audit trail every override anchors to

🐝 *Sign on the math. Walk on the math. Come back to the hurt customers. Earn the 30-year relationship.*
