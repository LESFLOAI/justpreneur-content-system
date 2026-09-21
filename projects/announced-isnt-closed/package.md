# JustPreneur Draft Package — "Announced Isn't Closed"

**Posting cycle:** 9:00 PM, 2026-09-21
**Status:** Draft ready — needs local finish (image generation + Finish-mode QC + human publish approval)

---

## Facts Summary (Approved Facts Block)

On March 24, 2026, OpenAI announced it would discontinue its Sora AI video product. The consumer Sora web and app experience was shut down on April 26, 2026, and the Sora API is scheduled to be discontinued on September 24, 2026, per OpenAI's official Help Center — the final step in winding the product down.

In December 2025, OpenAI and The Walt Disney Company announced an agreement covering (1) a three-year licensing arrangement that would let Sora and ChatGPT Images generate short, user-prompted videos using more than 200 characters from Disney, Marvel, Pixar, and Star Wars, and (2) a planned $1 billion equity investment by Disney in OpenAI, with warrants for additional equity. This was reported by OpenAI's and Disney's own press releases, and independently covered by CNBC, Bloomberg, Axios, and NPR.

After OpenAI announced Sora's shutdown in March 2026 — roughly three months after the deal was announced — Disney withdrew from the partnership. Multiple reports indicate the equity investment had not closed and no funds or warrants had actually transferred between the companies before the deal collapsed.

The $150 million figure that appears in some secondary sources for the deal size is incorrect; every primary source and major outlet (OpenAI, Disney, CNBC, Bloomberg, Axios) confirms the figure was $1 billion.

**Excluded (unverifiable, do not use):** Sora's daily operating cost, lifetime IAP revenue, active-user decline numbers, and exact minute-by-minute Disney notification timing.

**Fact Verifier status:** Cleared with qualifications.

---

## Headline

**Zero Dollars Moved. The Headline Still Said $1 Billion.**
Subhead: Announced isn't closed. Here's what actually happened.

---

## Slide Copy (4-slide carousel)

**Slide 1 — Hook**
> ZERO DOLLARS MOVED.
> THE HEADLINE STILL SAID $1 BILLION.
>
> Announced isn't closed.

**Slide 2 — The Facts**
> DECEMBER 2025:
> OpenAI + Disney announce a deal.
>
> • 3-year license: Sora + ChatGPT Images generate short videos using 200+ characters from Disney, Marvel, Pixar, Star Wars
> • Disney to invest $1B in equity into OpenAI, plus warrants for more
>
> Covered by CNBC, Bloomberg, Axios, NPR.

**Slide 3 — The Collapse**
> MARCH 2026:
> OpenAI announces it's shutting down Sora.
>
> Disney then withdraws from the partnership.
>
> The $1B investment never closed.
> No funds. No warrants. Nothing transferred.

**Slide 4 — Takeaway + CTA**
> ANNOUNCED ISN'T CLOSED.
>
> Until the ink is dry and the money moves, a deal is worth zero.
>
> Build on what's actually in hand — not what's in the headlines.
>
> Save this. Then go audit your own LOIs, MOUs, and "partnership announced" posts.

---

## Final Caption

(See `caption.md` in this folder for the verbatim, verification-checked version.)

A $1 billion deal made headlines everywhere. Zero dollars ever moved.

In December 2025, OpenAI and Disney announced a partnership: a 3-year license for Sora and ChatGPT Images to use 200+ characters from Disney, Marvel, Pixar, and Star Wars — plus a planned $1B equity investment by Disney into OpenAI, with warrants for more.

Three months later, OpenAI announced it was shutting down Sora. Disney then walked away from the partnership. The equity investment never closed. No funds, no warrants, nothing transferred.

The lesson isn't about OpenAI or Disney. It's about every founder who's ever built a roadmap, a hiring plan, or a pitch deck around a deal that was "basically done."

Announced isn't closed. Treat unclosed capital and partnerships as zero until the ink is dry and the money moves.

(One more clock ticking: OpenAI's Sora API itself is scheduled to shut down September 24 — three days from today.)

Call to action: Save this post. Then go pull up your own pending deals, LOIs, or "partnership announced" posts and ask yourself honestly: closed, or just announced?

---

## Hashtags (5)

#DueDiligence #FounderLessons #StartupReality #DealFlow #BuildOnWhatsReal

---

## Accounts to Tag (pending handle verification — see QC note below)

- **@cnbc** — independently reported and confirmed both the deal terms and the $1B figure.
- **@bloomberg** — independent confirmation of deal size and collapse; financial-press credibility.
- **@axios** — independent coverage cited in the facts block.
- **@openai** — primary party to the deal and the Sora shutdown. *(Confirm handle before publish.)*
- **@disney** — primary party to the deal and the withdrawal. *(QC flagged: Disney's consumer/parks Instagram may not represent the same corporate entity that signed the equity deal — confirm the correct handle or drop this tag before publish, keeping the three outlet tags as sufficient on their own.)*

---

## Image-Generation Prompts

**Images not yet generated — draft mode. No image-generation API key exists in this environment.**

Full design brief and per-slide prompts (palette, typography, layout system, and the 4 individual image-generation job specs) are in:
- `design-brief.md`
- `image-jobs.json`

Design concept: financial-press "voided ledger" motif — a stamped/crossed-out "$1B" bookends the carousel (Slide 1 and Slide 4). Slides 2–3 use paired abstract motifs (film-reel/light-beam for the entertainment side, neural-network nodes for the AI side) shown converging then fracturing. No Disney or OpenAI trademarks, logos, or characters anywhere — abstract motifs only. Palette: navy / steel gray / warm white / gold, with sparing ink-red confined to the "VOID" stamp accents.

To generate real images and finish this package, run `/justpreneur-finish` locally with a configured image-generation API key, then re-run Quality Control in Finish mode (mobile readability, safe margins, stray-text check, cross-slide visual consistency) before any publish approval.

---

## QC Verdict

**Pass with corrections** (not a Fail — pipeline proceeded to assembly).

Corrections applied in this package:
1. Caption saved as a standalone, verbatim-checked artifact (`caption.md`).
2. Tag-handle verification flagged explicitly above — confirm @openai/@disney handles or drop them before publish.

Outstanding before actual publish (per QC's pre-publish checklist):
- [ ] Confirm @disney and @openai are correct, current, entity-accurate handles (or drop in favor of outlet tags only)
- [ ] Generate final images via `/justpreneur-finish`, then re-run full QC (mobile readability, safe margins/crop risk, stray text/watermarks, cross-slide visual consistency)
- [ ] Confirm layout burns in copy verbatim, no paraphrasing
- [ ] Reconfirm hashtag/tag counts after any last-minute edits
- [ ] One human eyes-on pass for typos on rendered slides
