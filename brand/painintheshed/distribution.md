# Pain in the Shed · Distribution Spec

> *RSS feed · platform distribution · cross-promo discipline.*

---

## Canonical RSS Feed

```
URL:                https://painintheshed.com/rss
Format:             RSS 2.0 with iTunes namespace
Update cadence:     Auto-updated on episode publish
Episode count:      All episodes since launch (no rotation cutoff)
```

The canonical RSS feed is the single source of truth. Apple / Spotify / Pocketcasts / Overcast all pull from this endpoint.

### Required RSS fields (per episode)

```xml
<item>
  <title>Episode {N} · {Title}</title>
  <description>{Show notes summary}</description>
  <pubDate>{RFC-2822 date}</pubDate>
  <enclosure url="..." length="..." type="audio/mpeg"/>
  <guid isPermaLink="true">https://painintheshed.com/{N}-{slug}</guid>
  <link>https://painintheshed.com/{N}-{slug}</link>
  <itunes:duration>{HH:MM:SS}</itunes:duration>
  <itunes:episodeType>full</itunes:episodeType>
  <itunes:episode>{N}</itunes:episode>
  <itunes:explicit>false</itunes:explicit>
  <itunes:author>Mr. Defendable + dev</itunes:author>
  <itunes:summary>{Long-form show notes}</itunes:summary>
  <content:encoded><![CDATA[
    {Full HTML show notes · timestamps · Cost-to-Mint readout · DDEED link · cross-ref to offensetotheshed.com written companion}
  ]]></content:encoded>
</item>
```

### Channel-level RSS fields (one-time setup)

```xml
<channel>
  <title>Pain in the Shed</title>
  <link>https://painintheshed.com</link>
  <description>The cost of making AI real. Operator-grade economics from the shed.</description>
  <language>en-US</language>
  <itunes:category text="Technology">
    <itunes:category text="Tech News"/>
  </itunes:category>
  <itunes:category text="Business">
    <itunes:category text="Entrepreneurship"/>
  </itunes:category>
  <itunes:image href="https://painintheshed.com/cover.jpg"/>
  <itunes:author>Mr. Defendable + dev</itunes:author>
  <itunes:owner>
    <itunes:name>Mr. Defendable</itunes:name>
    <itunes:email>show@painintheshed.com</itunes:email>
  </itunes:owner>
  <itunes:type>episodic</itunes:type>
  <itunes:explicit>false</itunes:explicit>
</channel>
```

---

## Distribution Channels

| Channel | Source | Cadence | Audience |
|---|---|---|---|
| **painintheshed.com** | Direct upload | Every episode · canonical | Web visitors · principals |
| **Apple Podcasts** | RSS pull from painintheshed.com/rss | Auto · 4-hr poll | Mainstream podcast listeners |
| **Spotify** | RSS pull | Auto · 4-hr poll | Mainstream podcast listeners |
| **Pocketcasts / Overcast / etc.** | RSS pull | Auto | Power podcast listeners |
| **YouTube** | Manual upload (when video format used) | Per video episode | Visual/video learners |
| **Hugging Face** | Transcript dataset upload | Per episode (within 7 days) | AI researchers · training corpus consumers |
| **X / Twitter** | Manual clip posts (cold-open + Cost-to-Mint moment) | Per episode + 2-3 clips | Operator audience · founder network |
| **LinkedIn** | Long-form excerpt posts | Per episode (1 long excerpt) | CFO / Principal / Compliance audience |
| **Email digest** | Resend (opt-in via mrdefendable.com/from-the-desk) | Per episode + monthly digest | Engaged audience |

---

## Cross-Promotion Discipline

Every episode triggers these cross-promo posts (auto-templated · operator voice):

### offensetotheshed.com (written companion · same day)

```markdown
# Episode {N} · {Title} (Written Companion)

Pain in the Shed Episode {N} dropped today. Full audio at
[painintheshed.com/{N}-{slug}](https://painintheshed.com/{N}-{slug}).

This is the written deep-dive. {1-2 paragraphs of additional context the
audio couldn't go deep on · charts · code snippets · references.}

## Cost to Mint Receipt (from the episode)

{Embedded Cost-to-Mint readout}

[Listen to the full episode →](https://painintheshed.com/{N}-{slug})

DDEED: `DDEED-MEDIA-POD-{N}-{slug}-v1`
Hedera anchor: [verify on hashscan](https://hashscan.io/mainnet/topic/0.0.10291838)
```

### mrdefendable.com/from-the-desk (founder note · within 3 days)

```markdown
# From the Desk · Notes on Episode {N}

Dropped Pain in the Shed Episode {N} this week. {1-paragraph principal
commentary on why this episode mattered · what we learned · what surprised
even us about the cost-to-mint numbers.}

The receipt: {standalone Cost-to-Mint readout}.

— Mr. Defendable
To the shed.
```

### X / Twitter clips (per episode · 2-3 clips)

- Clip 1: cold-open (`[ring ring] · Hello dev · Mr. Defendable here · {hook}`)
- Clip 2: signature Cost-to-Mint moment (`What did it cost to mint this truth?`)
- Clip 3: one operator quote or surprising revelation from The Pit section

---

## Hugging Face Distribution (training corpus)

Each episode's transcript becomes a publicly downloadable dataset:

```
sudosuops/pain-in-the-shed-transcripts
  ├── ep-001-false-honey.jsonl
  ├── ep-002-117gb-reclaimed.jsonl
  ├── ...
  └── metadata.json   (Cost-to-Mint per episode · DDEED links · Tribunal verdicts)
```

Each `.jsonl` line:
```json
{
  "episode": 1,
  "speaker": "Mr. Defendable|dev",
  "timestamp_sec": 0,
  "text": "...",
  "tribunal_tier": "Royal Jelly|Honey|Jelly|Propolis",
  "ddeed_id": "DDEED-MEDIA-POD-001-false-honey-v1",
  "vocab_candidates": ["..."]
}
```

This makes Pain in the Shed transcripts the most provenance-attested AI training data on the internet · publicly verifiable · operator-grade · cost-receipted.

---

## SEO / GEO / llms.txt

| File | Content |
|---|---|
| `painintheshed.com/sitemap.xml` | All episode URLs + RSS + about + lanes + cost-to-mint |
| `painintheshed.com/llms.txt` | Show thesis + 8 lanes + cross-references to defendableos.com / offensetotheshed.com / mrdefendable.com / defendapedia.eth |
| `painintheshed.com/robots.txt` | Allow all crawlers (we WANT discovery) |
| Per-episode OG tags | Mr. Defendable + dev avatar · episode title · cold-open hook |
| Per-episode Schema.org | PodcastEpisode markup with full Cost-to-Mint structured data |

---

## What We Don't Do (PASS doctrine applied to distribution)

- **No sponsored episodes** · ever · doctrine-grade
- **No paywalled content** · the doctrine is meant to be public
- **No platform exclusives** (no Spotify-exclusive deals · RSS-everywhere)
- **No DRM** on audio (open formats · MP3 · M4A)
- **No giveaways / sweepstakes / engagement-bait** · operator voice never grovels
- **No SEO keyword-stuffing** in episode titles (titles are operator-direct · not search-optimized)
- **No "Subscribe and like" outros** · the sign-off is "To the shed"

---

## Launch Sequence (Episode 001 readiness checklist)

- [ ] painintheshed.com live · CF Pages deployed
- [ ] RSS feed validated (use Apple Podcasts Connect validator)
- [ ] Cover art produced (operator-grade · NOT influencer cover)
- [ ] Apple Podcasts Connect submitted (1-7 day approval)
- [ ] Spotify for Podcasters submitted (1-2 day approval)
- [ ] Episode 001 audio recorded · transcribed · DDEED-anchored
- [ ] Cost-to-Mint readout pre-computed (do NOT compute live)
- [ ] Written companion on offensetotheshed.com ready (same-day publish)
- [ ] X clips queued (cold-open + Cost-to-Mint + 1 quote)
- [ ] LinkedIn long-form excerpt queued
- [ ] Hugging Face dataset repo created · first episode uploaded

Launch when ALL above checked. PASS doctrine: do NOT launch with any item incomplete.

---

## Cross-References

- `README.md` (podcast domain overview · show thesis · 8 lanes)
- `episode-template.md` (per-episode artifact structure)
- Pipeline: `brand/offensetotheshed/media-to-dataset-pipeline.md`
- Memory: `painintheshed-podcast-domain-defense-lock-2026-05-24`
- Memory: `pain-in-the-shed-cost-of-intelligence-scope-2026-05-24`

---

🐝 *Single RSS endpoint. Single source of truth. Books-and-records-grade distribution. To the shed.*
