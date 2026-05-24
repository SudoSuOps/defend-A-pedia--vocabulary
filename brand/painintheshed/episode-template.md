# Pain in the Shed · Episode Template

> *Per-episode artifact structure · Cost-to-Mint segment · DDEED-anchor discipline.*

---

## Episode Anatomy

Every episode produces these artifacts:

| Artifact | Where | Purpose |
|---|---|---|
| **Audio file** | painintheshed.com/{ep_num}-{slug} + R2/IPFS | Primary distribution |
| **Video file** (optional · for live-debug or whiteboard formats) | painintheshed.com + YouTube | Visual format |
| **Show notes** | painintheshed.com/{ep_num}-{slug}/notes | Timestamps · references · links |
| **Transcript** | offensetotheshed.com/{slug} (written companion) | Searchable · accessible · trainable |
| **Cost-to-Mint readout** | painintheshed.com/cost-to-mint (cumulative) | Public operator-economics ledger |
| **Vocabulary candidates** | defendapedia.eth pending queue | Vocab expansion |
| **Tribunal verdict** | StreetLedger record | Quality grade |
| **DDEED hash** | Hedera HCS topic 0.0.10291838 | Immutable provenance |
| **Training corpus chunk** | SwarmCurator pipeline | Model training input |

---

## Episode Structure (locked · 4 sections)

### Section 1 · Cold Open (~1 min)

```
[ring ring]
Mr. D:   "Hello dev · Mr. Defendable here · got a minute"
dev:     "Yes Mr. D · what's on the desk"
Mr. D:   "[The lane · 1-sentence framing · why this episode now]"
```

### Section 2 · The Pit (~20-45 min · the substance)

Real conversation on the chosen lane. No script · no edit-cuts · no music bed.

Format depends on episode type:
- **Lane 1-2** (Cost to Mint · Hyperscaler Pain) → economics deep-dive · spreadsheet-style numbers
- **Lane 3-4** (GPU Prices · Vast.ai Field Notes) → market report · screenshots referenced
- **Lane 5-6** (Edge · Energy) → hardware-floor conversation · power meters
- **Lane 7-8** (False Honey · Repair Lift) → case study · pull a real Tribunal verdict

### Section 3 · Cost-to-Mint Segment (~3-5 min · signature · NON-NEGOTIABLE)

Closes every episode. Standardized readout:

```
Mr. D:  "Cost to mint segment · dev pull the numbers"
dev:    "[reads the readout below · live]"
```

**Standardized Cost-to-Mint readout** (read aloud · also published on painintheshed.com/cost-to-mint):

```
COST TO MINT · Episode {N}
═══════════════════════════════════════════════════════
Topic:            {episode lane / specific artifact}
Run scope:        {what was minted in this episode's example}

Compute           $X.XX     ({GPU model} · {hours} · ${/hr rate})
Human review      $X.XX     ({minutes} · ${/hr rate})
Validator pass    $X.XX     ({# passes} · {model} · ${/pass})
Storage           $X.XX     ({GB} · ${/GB/mo})
Energy            $X.XX     ({kWh} · ${/kWh})
Retries           $X.XX     ({# retries} · {avg cost})
Repair            $X.XX     (SwarmFixer interventions · {count})
Deed issuance     $X.XX     (Hedera HCS · ${/msg})
═══════════════════════════════════════════════════════
Total:            $X.XX  per minted artifact

Comparison
  Hyperscaler equivalent      ~$X.XX  ({X}× our cost)
  Human-only equivalent       ~$X.XX  ({X}× our cost)
═══════════════════════════════════════════════════════
```

### Section 4 · Sign-Off (~30 sec)

```
Mr. D:   "[Lesson · doctrine takeaway · 1-2 sentences]"
Mr. D:   "To the shed. Mr. Defendable speaking out."
[end]
```

---

## Pre-Production Checklist (before recording)

- [ ] Choose lane (one of the 8)
- [ ] Choose the SPECIFIC artifact / run / case study to discuss
- [ ] Pull the Cost-to-Mint numbers in advance (do NOT calculate live · pre-compute)
- [ ] Identify 2-3 receipts to cite live (commit hash · Hedera anchor · DDEED ID · etc.)
- [ ] Confirm no NDA-protected client material will surface
- [ ] If video: set up screen-share / whiteboard / power meter readouts

---

## Recording Discipline (LOCKED)

| YES | NO |
|---|---|
| Real conversation · operator cadence | Scripted dialogue |
| Audible typing · audible reading · audible thinking | Music beds |
| Mistakes left in (lightly cleaned audio only) | Heavy editing |
| Cold open with [ring ring] | "Welcome back to the show" intros |
| Sign off with "To the shed" | "Subscribe and like" outros |
| Real numbers · real receipts · real failures | Aspirational hypotheticals |
| Founder voice · 30-yr operator cadence | AI-startup / VC / influencer energy |

---

## Post-Production Pipeline (per episode)

```
1. Upload raw audio to CF R2
2. Run Whisper transcription
3. Light audio clean (volume normalization · gain match · NO music)
4. Generate show notes (timestamps + cited receipts + cross-links)
5. Extract vocabulary candidates (NER vs defendapedia.eth)
6. Tribunal grade per chunk (Honey · Jelly · Propolis)
7. Mint DDEED-MEDIA-POD-{num}-{slug}-v1
8. Anchor to Hedera HCS topic 0.0.10291838
9. Publish to painintheshed.com/{num}-{slug}
10. Update RSS feed
11. Cross-publish written companion to offensetotheshed.com/{slug}
12. Update cumulative cost-to-mint ledger at painintheshed.com/cost-to-mint
13. Submit clips to X / LinkedIn (cold-open + signature Cost-to-Mint moment)
14. Add to training corpus (Honey + Royal Jelly tiers only)
```

---

## DDEED-MEDIA-POD Schema (per episode)

```json
{
  "deed_class": "DDEED-MEDIA-POD",
  "deed_id": "DDEED-MEDIA-POD-{N:03d}-{slug}-v1",
  "show": "Pain in the Shed",
  "episode_num": N,
  "lane": "{one of 8 lanes}",
  "title": "{episode title}",
  "url": "https://painintheshed.com/{N}-{slug}",
  "audio_url": "https://painintheshed.com/{N}-{slug}/audio.mp3",
  "transcript_url": "https://offensetotheshed.com/{slug}",
  "published_at": "2026-MM-DD",
  "duration_sec": NNNN,
  "audio_hash": "sha256:...",
  "transcript_hash": "sha256:...",
  "cost_to_mint": {
    "compute_usd": 0.00,
    "human_review_usd": 0.00,
    "validator_usd": 0.00,
    "storage_usd": 0.00,
    "energy_usd": 0.00,
    "retries_usd": 0.00,
    "repair_usd": 0.00,
    "deed_issuance_usd": 0.00,
    "total_usd": 0.00,
    "hyperscaler_equivalent_usd": 0.00,
    "human_only_equivalent_usd": 0.00,
    "savings_multiple": 0.0
  },
  "tribunal_verdict": {
    "overall_tier": "Royal Jelly|Honey|Jelly|Propolis",
    "per_chunk_count": N,
    "drift_ok": true
  },
  "vocabulary_candidates": [
    {"term": "...", "context": "...", "frequency": N}
  ],
  "training_corpus_chunks_added": N,
  "ens_anchor": "streetledger.eth/media/pod/{N:03d}-{slug}/",
  "hedera_tx": "0.0.10291838@TIMESTAMP",
  "five_proofs": {
    "origin": {"hosts": ["Mr. Defendable", "dev"], "recorded_at": "..."},
    "quality": {"tribunal_pass": true, "drift_ok": true, "v03_voice_pass": true},
    "process": {"pipeline": "pain-in-the-shed-v1", "steps_logged": true},
    "economics": {"cost_to_mint_usd": "...", "compounding_value_pairs": N},
    "trust": {"hedera_anchor": "...", "publicly_verifiable": true}
  }
}
```

---

## Cumulative Cost-to-Mint Ledger (painintheshed.com/cost-to-mint)

Public running totals across all episodes. Live page · auto-updated per episode publish.

```
PAIN IN THE SHED · CUMULATIVE COST TO MINT
═══════════════════════════════════════════════════════════════════════════════
Episodes published:           N
Total artifacts minted:       N
Total spend (real):           $X.XX
Hyperscaler equivalent:       $X.XX  (~{X}× ours)
Human-only equivalent:        $X.XX  (~{X}× ours)

Average per artifact:         $X.XX
Lowest single artifact:       $X.XX  (Episode {N})
Highest single artifact:      $X.XX  (Episode {N})

Cost-to-mint trend (last 6 episodes):
  Ep N-5   $X.XX
  Ep N-4   $X.XX
  Ep N-3   $X.XX
  Ep N-2   $X.XX
  Ep N-1   $X.XX
  Ep N     $X.XX
═══════════════════════════════════════════════════════════════════════════════
```

This page IS the live receipt. Anyone can verify: open the page · pick an episode · pull the audio · listen to the Cost-to-Mint segment · cross-check the published number. Books-and-records-grade transparency on the show's own economics.

---

## Cross-References

- `README.md` (podcast domain overview · show thesis · 8 lanes)
- `distribution.md` (RSS feed spec · platform distribution)
- Pipeline: `brand/offensetotheshed/media-to-dataset-pipeline.md`
- Voice: `brand/mrdefendable/voice-guide.md`
- Cost-to-mint baseline: memory `swarm-os-operator-platform-2026-05-24`
- Memory: `pain-in-the-shed-cost-of-intelligence-scope-2026-05-24`

---

🐝 *What did it cost to mint this truth? To the shed.*
