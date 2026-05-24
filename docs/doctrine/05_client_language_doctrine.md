# Client Language Doctrine

> *"We speak to ownership · not to IT."*

The customer is the principal. The CEO. The founder. The MD. The person whose name is on the door, whose signature is on the loan, whose ass is on the line when the agents go dark. The customer is not the engineering manager. The customer is not the DevOps lead. The customer is not procurement. The customer is the one who eats the loss when offense fails.

This doctrine governs how we speak to that customer. Every email, every dashboard, every Closing Statement, every Morning Brief, every LOU clause. One discipline. End to end.

---

## The core principle

The customer reads at the level of a Class A 5-cap broker · not at the level of a senior engineer at FAANG. They want to know:

1. **Is the asset producing?** (Are the agents in alignment? 100% occupied?)
2. **Is risk contained?** (When something fails, do we catch it · or do they read about it in the press?)
3. **Are the books tying out?** (Can they hand the deed to their auditor and have it ground out clean?)
4. **What does it cost?** (Per agent. Per month. Per receipt. Per deed.)
5. **What do they owe us, and what do we owe them?** (The covenant.)

That's the entire mental model. Five questions. Answered in their language · the way a CRE broker would brief a CEO on a portfolio review · NOT the way an engineer would brief their VP.

---

## What "client-facing" actually means

It means every surface the customer touches:
- The pre-market flight sheet (broker-to-prospect, pre-LOU)
- The Letter of Understanding (the signed engagement)
- The Morning Reconciliation Brief (the 06:00 daily email)
- The dashboard the customer logs into
- The Defendable Closing Statement (engagement variance report)
- The renewal proposal
- Every email from any operator on the firm

All of it pulls from the same vocabulary. All of it preserves the founder voice. All of it speaks broker-to-principal · not engineer-to-engineer.

---

## The plain-English layer is mandatory · the operator layer is preserved

Every term file in this repo has a "Client Explanation" section. That section is the canonical plain-English supplement. It is NOT a watered-down version · it is a sharpened version. The operator language is preserved in the "Street Definition" and "CRE Operator Meaning" sections · the customer language is delivered in the "Client Explanation" section · and the two are NEVER allowed to drift.

Example: the term `color` (see [`../vocabulary/cre_terms/`](../vocabulary/cre_terms/)) carries this Client Explanation:

> "Color is what we KNOW about the asset · not what's been claimed. When we open an engagement on your behalf · we build color by pulling independent sources · verifying numbers · talking to the market. The more color we have · the higher our confidence rating · the lower your risk."

A CEO can read that. A board can read that. A CFO can read that. No engineering jargon. No AI-vendor cliches. Pure broker-to-principal. That's the standard for every Client Explanation in the repo.

---

## Eight rules for speaking to ownership

**Rule 1 · CRE analogy over engineering analogy.** When in doubt, reach for the CRE term. "Your agent fleet is 92% occupied" lands. "Your agent fleet has a 92% availability score" doesn't. CRE-borrowed language puts the customer in their own mental model · which is the only model they trust at speed.

**Rule 2 · One number per sentence.** CFOs read numbers. Don't bury one in a paragraph. "Last week's variance: -$1,200 below proforma. Cause: 3 Propolis events in the medical-claims agent. Fix shipped Tuesday. Re-verified Wednesday." Four sentences, four facts, one decision the CEO can make.

**Rule 3 · Always name the failure mode in the customer's vocabulary.** Don't say "the model hallucinated." Say "the agent fabricated a number on three claims · we caught it before it left the building · here's the deed." The first is a vendor confession. The second is a defense report.

**Rule 4 · Never explain the architecture unsolicited.** The customer does not need to know what a Merkle root is. The customer needs to know that the deed they're holding can be verified by their auditor through a public link. When asked, explain. When not asked, deliver the result.

**Rule 5 · Use the founder vocabulary.** "To the shed." "In the pit." "List the building." "Comp it." "Color on the asset." "The deal pencils." "Class A 5-cap." "White-glove." These are not slogans · they are the operator's vocabulary, and using them communicates that you know what you're doing without having to say so. Customers can tell the difference between a service that uses CRE language because it knows CRE · and one that sprinkles it for marketing. Be the first.

**Rule 6 · No MBA jargon.** No "leverage synergies." No "best-in-class." No "transformational." No "AI-native." No "10x." No "platform." The founder reads these as marketing tells · the customer reads them as evasion. Cut every one of them at the first draft.

**Rule 7 · No "powerful · scalable · AI-native" generic copy.** If a sentence could appear on the homepage of any AI startup, it doesn't belong on a customer-facing DefendableOS surface. Replace it with a specific number, a specific receipt ID, or a specific outcome from the customer's own ledger.

**Rule 8 · Always tie back to the receipt.** Every claim is one click from a deed ID. Every dashboard widget has a "verify this" link to the L4 Hedera anchor. The discipline is what makes the trust earned, not asserted.

---

## What to write · and what to never write

### Write this

- "Three agents went dark on Tuesday between 14:02 and 14:18. SwarmJelly caught the drift, repaired in 11 minutes, and reissued the deed. No customer-facing impact. Deed: `DDEED-DOV-...-v2`. Verify: [link]."
- "Your fleet was 98.4% occupied this week. Up from 96.1% the prior week. The lift came from the medical-claims agent · we retrained it Tuesday after Friday's Propolis flag."
- "The pre-market flight sheet shows the engagement penciling at a 7-cap on annualized agent revenue at risk. We're proposing a 9-cap to give you a margin of safety. Sit available Thursday."
- "The PASS doctrine applies here · we recommend not pursuing the certification claim until we have 60 days of clean Tribunal verdicts on the affected agent class. Walking the short-term win is the right move."

### Never write this

- "Our AI-native platform leverages advanced ML to deliver transformational outcomes."
- "We use a proprietary algorithm to score your agents."
- "Synergies between our defense layer and your existing stack will unlock 10x productivity."
- "Best-in-class governance and observability."
- "Robust, scalable, enterprise-grade."

The contrast is not stylistic. It is operational. The first set of sentences are receipts in language form · the second are marketing claims a customer correctly discounts.

---

## The Morning Reconciliation Brief · the daily test

Every morning at 06:00 local, every active customer gets the Morning Reconciliation Brief. One page. Markdown. Plain text fallback. Mobile-readable. Three sections:

1. **Yesterday in numbers.** Occupancy. NOI. Variance vs proforma. Any P1/P2 incidents and their resolution status.
2. **Today's risks named.** What we're watching. Why. What action would trigger an escalation.
3. **Receipts you can verify.** A short list of deed IDs from yesterday, each with a Hedera anchor link.

If the customer reads the Brief for 90 seconds and walks away knowing the state of their fleet · the doctrine is working. If they have to forward it to their engineering team to interpret · the doctrine has failed and the brief needs a rewrite.

The Brief is the daily test of this entire doctrine. SH5 (Client Language Specialist) owns the template. Every operator drafts to it. Every sr broker signs off before send.

---

## The Letter of Understanding · the contractual test

The LOU is where the language becomes legally binding. Every clause must be readable by the principal in one pass. No legalese smuggled in. No "subject to terms and conditions available upon request." Every term used in the LOU is a term defined in this repo · the customer can look any one of them up and find the canonical definition.

LOU clauses to use:
- "Engagement term: 12 months. Renewable in 30-day windows. White-glove service throughout."
- "Defense coverage: all agents in the fleet declared at engagement open. New agents covered at incremental rates per addendum."
- "Receipt SLA: every defensive action receipted within 15 minutes of execution. Anchored to Hedera within 30 minutes."
- "Title insurance: Tribunal verdicts ship with ±0.15 score guarantee. Variance beyond guarantee triggers automatic credit."
- "PASS clause: DefendableOS reserves the right to recommend non-action and credit the prepaid fee if the engagement scope changes such that defense becomes infeasible. Customer reserves the right to refuse and engage a third party · no penalty."

CRE-grade clarity. Boardroom-readable. Auditor-defensible.

---

## The Closing Statement · the variance test

At the end of every engagement (or every annual renewal review), the customer receives a Defendable Closing Statement. Same shape as a CRE closing statement: line-by-line variance between what was promised (the proforma in the LOU) and what was delivered (the actuals from L1-L5).

Variances explained in plain English:
- "Proforma: 99.0% occupancy. Actual: 97.8%. Variance: -1.2 points. Cause: 14-hour outage during the agent vendor's mid-cycle patch. Defense response: detected within 47 seconds, escalated within 5 minutes, customer notified within 8. No customer-facing transactions affected."

The customer reads this and knows · without consulting an engineer · whether to renew, expand, or walk. That's the test.

---

## The five sentences a customer should be able to repeat after one meeting

If we've done the language right, the customer can summarize what they bought in five sentences:

1. "Defendable defends my AI agents · 24/7 · like a SOC for offense."
2. "They issue a receipt for every defensive action and anchor it to a public ledger I can verify."
3. "They walk deals they can't defend, even when it costs them fees."
4. "I get a one-page Morning Brief every day. I read it in 90 seconds."
5. "I can hand any deed to my auditor and it grounds out clean."

If the customer can say these five sentences back to a peer over coffee, they will refer the peer. That's the M&M model · 80% of deals come from referrals from satisfied principals. The language is what makes the referral repeatable.

---

## What this doctrine prevents

- **Customer ghosting after onboarding.** Customers ghost when they don't understand what they're paying for. Plain-English receipts prevent the ghost.
- **Engineering team interception.** When the dashboard speaks engineer, the engineering team intercepts the relationship. The principal becomes a stakeholder, not the buyer. We lose the room.
- **Renewal friction.** When the Closing Statement is in customer language, renewal is a 15-minute call. When it's in vendor language, renewal becomes a procurement cycle.
- **Auditor confusion.** When the deed speaks broker, the auditor reads broker. When the deed speaks engineer, the auditor reads "vendor wants to bury something." Trust dies.
- **Brand drift.** Every marketing surface that drifts into AI-vendor cliche damages the brand. The Client Language Doctrine is the brand's vocabulary firewall.

---

## Who owns it

SH5 (Client Language Specialist) owns the templates. SH1 (this doctrine) owns the words. SH3 (Tribunal Architect) ensures every Tribunal output renders into client-language correctly. Every sr broker signs off on every customer-facing artifact before send. No exceptions.

---

## Read next

- [`06_hive_doctrine.md`](06_hive_doctrine.md) · the Bee Agent biology that the language describes
- [`../playbooks/sr_broker_playbook.md`](../playbooks/sr_broker_playbook.md) · how the sr broker enforces this doctrine in adjudication
- [`../vocabulary/cre_terms/`](../vocabulary/cre_terms/) · every term carries a Client Explanation section · this is where the doctrine lives

🐝 *We speak to ownership. Not to IT. The receipts do the rest.*
