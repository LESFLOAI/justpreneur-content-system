# JustPreneur Draft Package — "Take-Rate Math" (Spotify Creator Memberships)

**Status:** Draft ready — needs local finish (image generation + re-QC on real artwork via `/justpreneur-finish`).
**Target posting slot:** 2026-10-27, 9:00 PM
**Pipeline verdicts:** Fact Verifier — Cleared with qualifications. Quality Control — Pass with corrections (corrections applied below).

---

## 1. Facts summary (Approved Facts Block, fact-verifier cleared)

On October 20, 2026, Spotify began rolling out "Creator Memberships," a direct-to-fan paid subscription feature for podcasts, in 34 markets (including the US, UK, Canada, Australia, and most of the EU; Latin America is not part of this initial rollout). According to Spotify, creators keep 90% of membership revenue, with Spotify retaining the remaining 10%; Spotify has not publicly clarified whether payment-processing, foreign-exchange, or payout fees are deducted from either side of that split. To be eligible, a show must be hosted on Spotify for Creators or Megaphone and have at least 3 published episodes, 100 listeners/viewers, and 100 consumption hours in the trailing 30 days. Creators can offer up to three membership tiers with perks such as bonus episodes, ad-free listening, or early access; Spotify does not set prices (its own illustrative example used $4.99/month with a 7-day free trial). Creator Memberships replaces Spotify's 2021 podcast-subscriptions feature and was first previewed at Spotify's Investor Day on May 21, 2026, in New York.

*(Deliberately not used in this piece: Spotify's Q3 2026 earnings and the separate Partner Program expansion — kept out to avoid conflating two different Spotify announcements.)*

**Comparison figures (NOT from Spotify's announcement — sourced separately, approximate, convergent across multiple independent secondary sources, not each platform's own primary documentation):**
- YouTube Channel Memberships: creators keep ~70%, platform takes ~30% (consistent across several independent creator-economy sources; not found stated verbatim on YouTube's own help pages).
- Patreon: current standard plan takes a flat 10% platform fee (creator keeps ~90% before payment processing); legacy plans range 5–12% (creator keeps ~88–95%) — "~88–92%" is a reasonable mid-range approximation, not a single confirmed figure. Processing/FX/payout fees are additional on top of the platform fee, same ambiguity-category as Spotify's own undisclosed-fee caveat.
- These two figures carry a visible "Based on each platform's own published terms. Approximate." sourcing line in the design (Slide 4), added per QC correction.

**Tag-handle check (per QC correction):** @spotify and @youtube are each platform's own primary handle. @spotifyforcreators is Spotify's creator-facing account, consistent across multiple third-party app-store listings pointing to instagram.com/spotifyforcreators (could not be independently confirmed directly on Instagram in this environment — recommend a final manual glance before posting). @patreon is Patreon's primary handle.

---

## 2. Headline

**"90% Sounds Generous. Compare It Before You Believe It."**
Subheadline: "Spotify's new creator split, next to the platforms you already use."

---

## 3. Slide-by-slide copy (7 slides, carousel)

1. **Cover** — "90% Sounds Generous. Compare It Before You Believe It." / sub: "Spotify's new creator split, next to the platforms you already use."
2. **Context** — "Spotify just rolled out Creator Memberships in 34 markets. The pitch: creators keep 90%. Spotify keeps 10%."
3. **Reframe** — "A take-rate is a percentage of *something.* Before you celebrate the number, ask what it's actually a cut of."
4. **Comparison** (locked headline) — "Here's the same number next to the platforms you already use." Bars: "Spotify Creator Memberships — ~90%" / "YouTube Memberships — ~70%" / "Patreon — ~88–92%". Sourcing line beneath bars: "Based on each platform's own published terms. Approximate." Platform-name labels in all-caps (typography now consistent with Section 4 of the design brief).
5. **Caveat (open question — not resolved either way)** — Flag label "NOT YET CONFIRMED" above headline: "Here's what Spotify hasn't said: whether processing, FX, or payout fees come out of that 90% — or come off the top before it. Gross vs. net is still unconfirmed."
6. **Takeaway** — "The real competition isn't audience size. It's take-rate — and you won't know yours until you check it."
7. **CTA** — "1. Pull your last 3 payouts. 2. Calculate what you actually kept. 3. Compare it across every platform you publish on."

---

## 4. Final caption

Spotify's new Creator Memberships feature launched October 20, 2026, in 34 markets — creators keep 90%, Spotify keeps the remaining 10%. That's the headline.

Here's the number that actually matters: Spotify hasn't confirmed whether processing, FX, or payout fees come out of that 90%, or get taken before the split is even applied. Gross and net are not the same thing, and right now, that distinction is an open question.

Compare it to what's already public — YouTube Memberships at roughly 70%, Patreon at roughly 88–92% (based on each platform's own published terms, approximate) — and the "biggest" number stops being the obvious winner by default.

The move worth making isn't picking a side. It's auditing your own take-rate, everywhere you already get paid.

What's your actual take-home rate on the platform you use most? Drop it below.

---

## 5. Hashtags (exactly 5)

#CreatorEconomy #PodcastBusiness #SpotifyForCreators #TakeRateMath #CreatorMonetization

---

## 6. Accounts to tag

- **@spotify** — primary source of the Creator Memberships announcement; direct subject of the post.
- **@spotifyforcreators** — Spotify's creator-facing account, referenced for eligibility/program details in the facts block (handle consistent across third-party sources; do a manual glance before posting).
- **@patreon** — named directly in the take-rate comparison (~88–92%); comparison platform, not a competitor callout.
- **@youtube** — named directly in the comparison (~70% for Channel Memberships); same rationale.

---

## 7. Image-generation prompts

**IMAGES NOT YET GENERATED — DRAFT MODE.** No image-generation API key exists in this cloud environment. Full prompts (one per slide, 1080x1350px) and the complete visual design brief (layout, typography, color, accessibility) are saved at:
- `projects/take-rate-math/design-brief.md`
- `projects/take-rate-math/image-jobs.json` (ready to run through `scripts/generate_images.py` locally via `/justpreneur-finish`)

Slide 5's art direction is the most compliance-sensitive: it must read as a neutral open question (a translucent "?" glyph, an empty dashed "pending" box) — no checkmark, no X, nothing implying Spotify confirmed or denied fee deductions either way.

---

## 8. Corrections applied after QC (all four resolved)

1. Added a visible sourcing caveat for the YouTube/Patreon comparison figures (Slide 4 + caption) since they fall outside Spotify's own announcement.
2. Locked Slide 4's headline to a single final string (removed the either/or hedge).
3. Resolved the ALL-CAPS vs. small-caps inconsistency — platform-name labels on Slide 4 are now ALL-CAPS throughout, consistent with the brief's typography section.
4. Checked tag handles via web search; @spotifyforcreators is corroborated by multiple independent sources but not directly confirmed on Instagram in this environment — flagged for a manual glance before publishing.

## 9. Still pending (next step is local, not cloud)

- Generate real images via `/justpreneur-finish` (needs local image-generation API key).
- Re-run Quality Control on the actual rendered artwork (mobile readability, safe margins, cross-slide consistency, and confirming Slide 5's art doesn't visually lean "yes" or "no").
- Final human publish confirmation — nothing in this pipeline publishes anything.
