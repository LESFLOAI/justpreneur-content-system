# QC Report — "The Forecast Discount" (bogota-forecast-discount)

**Reviewer:** JustPreneur Quality Control (independent, final gate)
**Date checked:** 2026-10-15
**Mode:** DRAFT MODE (no real image files exist — expected; checks 6, 7, 9, 10 below are pixel-dependent and deferred, not waived)
**Target posting slot:** 2026-10-15, 9:00 PM

**Files reviewed:**
- research/2026-10-15_fact-verification-bts-bogota.md (source of truth)
- projects/bogota-forecast-discount/strategist-angle-brief.md
- projects/bogota-forecast-discount/content-copy.md
- projects/bogota-forecast-discount/design-brief.md
- projects/bogota-forecast-discount/image-jobs.json

---

## VERDICT: Pass with corrections

Three corrections (one minor-currency-ambiguity fix, two hedge/consistency fixes) were applied directly to the files as part of this review. No blocking factual, legal, or safety issues were found. The core risk this story carries — readers misreading the $99,000M vs. $126,054M gap as the concerts "underperforming" — is explicitly and effectively defused by the copy's own built-in safeguards (see item 5 below).

---

## Checklist results

**1. All factual claims trace to the Approved Facts Block** — PASS. Checked every number against the research file's Approved Facts Block: $126,054M COP (Feb 2026 projection), ~$99,000M COP (Oct 2026 post-event estimate), ~US$25.4M wire-service conversion, the four-category breakdown ($39,108M / $29,384M / $17,557M / $12,976M — sums to ~$99,025M, matching the post-event total as the research file itself notes), 46.6% YoY flight bookings, and Falabella's 110%/90% figures. No invented statistics found anywhere in content-copy.md, design-brief.md, or image-jobs.json. The 21% gap math checks out: (126,054 − 99,000) / 126,054 ≈ 21.5%, correctly rounded to "about 21%" and correctly computed against the original (larger) figure rather than averaged.

**2. $99,000M COP always "estimate," never "actual"; Feb/Oct figures never conflated/averaged** — PASS. Every instance is hedged ("modeled estimate," "not an audited actual," "no full methodology was published"). Slide 5 and the caption explicitly state the two figures are from different times/methodologies and "shouldn't be compared as if they were the same number." Design brief and image-jobs.json both include explicit instructions/negative-prompts that the two bars/figures must never touch, merge, or be rendered as averaged.

**3. 46.6% correctly scoped to flight bookings only** — PASS. Every occurrence (strategy, copy Slide 6, design brief, image job) labels this a flight-booking metric and explicitly states "not a hotel number." No mislabeling found.

**4. Falabella's 110%/90% stay attributed and hedged** — PASS. Content-copy Slide 7, caption-adjacent framing, design brief, and image-jobs.json all attribute these figures to Viajes Falabella specifically, label them "single-sourced," and state they are "reported, not confirmed as a citywide statistic." The design brief even encodes this visually (dashed/hatched bar treatment, no gold color reserved for unconfirmed figures) — a nice reinforcement of the hedge at the visual-design layer.

**5. "21% gap" framing does not read as underperformance — safeguards actually work** — PASS. This was the single highest-risk element of the story and I scrutinized it closely. Slide 5 states directly: "This isn't a story about underperformance. It's a story about what a projection is actually for," immediately after stating both concerts sold out. The caption reinforces: "Both numbers are legitimate. Neither is 'wrong.'" The strategist brief's own "Risk of misunderstanding" entry for Angle 1 correctly anticipated this exact failure mode, and the downstream copy visibly built the countermeasure the brief called for. This safeguard is substantive, not just a disclaimer — it appears at the exact point in the carousel (right after the two big numbers) where the misreading would otherwise occur.

**6. Mobile readability** — DEFERRED (draft mode, no rendered pixels). Design brief specifies concrete minimums (headline ≥64px effective cap height, body ≥36px, eyebrow ≥28px at 1080px width, 2-3 line wrap max) that are reasonable and should be re-verified at actual render time.

**7. Safe margins and cropping risk** — DEFERRED (draft mode). Design brief specifies a 72px safe margin and flags its own potential risk point (wordmark at y≈1270 is close to the bottom-crop zone) with a stated contingency (nudge to y≈1230 if feed-preview testing shows clipping). This is good practice; must be re-checked against real renders.

**8. JustPreneur spelling and brand visibility** — PASS (as specified). "JustPreneur" is spelled correctly and consistently everywhere it appears, including an explicit reminder in design-brief Section 11 ("exact brand wordmark asset, correctly spelled 'JustPreneur'"). Wordmark placement is specified on every slide. Actual rendered visibility cannot be confirmed until real images exist.

**9. Unwanted tiny text, icons, watermarks, slide numbers, production marks** — DEFERRED (draft mode, pixel-dependent). Image-jobs.json prompts do include strong negative constraints against watermarks, borders, fake/illegible text, and baked-in numerals — good preventative design — but this must be re-verified visually once images are generated.

**10. Visual consistency across slides** — DEFERRED (draft mode, pixel-dependent) for actual rendered output. The brief/plan itself (Section 8) is internally consistent: same canvas, same palette, same wordmark position (with one documented, intentional exception at Slide 8), same bar-chart visual language continued across Slides 3-4-5-7.

**11. Caption alignment with artwork** — PASS (at the brief level). Caption's two headline figures and 21% framing match Slides 2, 3, and 5 exactly. One inconsistency found and corrected: the caption originally said "before a single ticket holder landed" while Slide 2 says "before a single flight landed" — not a factual error, just an avoidable inconsistency. Fixed (see Corrections Applied).

**12. Exactly five useful hashtags** — PASS. #ForecastDiscipline #StartupStrategy #CapacityPlanning #EntrepreneurMindset #BuilderLessons — exactly five, relevant, non-spammy, no banned/trademarked terms.

**13. Accuracy of suggested Instagram tags** — PASS. All five candidate handles are correctly reasoned against the Approved Facts Block (city government, tourism observatory, Ticketmaster Colombia, Viajes Falabella, BTS/HYBE), and the table explicitly and prominently flags every handle as unverified-by-browsing, with an extra editorial-judgment flag on tagging BTS's account on unrelated financial-analysis content. This satisfies the "flagged as unverified" requirement clearly.

**14. Legal/reputational/copyright/impersonation risk** — PASS. Design brief and every image-job prompt explicitly forbid BTS/artist likenesses, real-person likenesses, and any logos/trademarks/wordmarks (Ticketmaster, HYBE, Falabella, city seal, stadium signage). No fabricated quotes from BTS, city officials, or any company representative appear anywhere in the package. Falabella's data is named and hedged as a commercial claim, not asserted as fact — standard, defensible attribution journalism practice, not impersonation.

**9 (cross-file). Internal consistency across all four files** — PASS, with corrections applied. Headline, slide count (8), and all figures matched exactly across strategist-angle-brief.md, content-copy.md, design-brief.md, and image-jobs.json. Two small inconsistencies were found and corrected (see below).

---

## Corrections Applied (all three now fixed in the files)

1. **content-copy.md, Slide 3 & design-brief.md, Slide 3 (two places)** — The Approved Facts Block says the post-event balance was "released **around** October 6–8, 2026" (a hedge). Content-copy and design-brief had both dropped that hedge, stating the date as a bare "(Oct 6–8, 2026)." Low severity (it's already a date range, which is somewhat self-hedging), but per the mandatory "no dropped hedges" standard, I changed both instances to "(~Oct 6–8, 2026)" to restore the upstream hedge and keep notation consistent with the "~" used elsewhere in the same documents (~$99,000M, ~US$25.4M).

2. **content-copy.md, Final Caption** — Changed "before a single ticket holder landed" to "before a single flight landed" to match Slide 2's identical claim and remove an avoidable internal inconsistency in how the same fact is phrased across the package. Not a factual error, just inconsistent imagery.

3. **strategist-angle-brief.md, "Three headline options," item 1** — Changed "Bogotá Projected $126 Billion From BTS..." to "Bogotá Projected $126,054M COP From BTS..." The bare "$126 Billion" with no currency specified is a real misreading risk (could be read as US$126 billion vs. the actual ~126 billion Colombian pesos — roughly a 3,000x error). This specific headline option was never the one selected for publication (content-copy.md correctly used the safe, number-free Option 3, and had already independently applied this same currency fix to its own copy of Option 1), so it was not a live risk to the current package — but the strategist brief remains part of the reviewed package of record, so I corrected it for consistency and to prevent this ambiguous phrasing from being reused in a future cycle.

No other factual, attribution, hedging, or consistency issues were found. All four of the previously-flagged fact-verification corrections (estimate-labeling, USD tightening to $25.4M, flight/hotel mislabel fix, Falabella hedging) were already correctly and consistently carried through every downstream document before this review began.

---

## Optional improvements (not required, not applied)

- Angle 2 and Angle 3 in strategist-angle-brief.md (non-selected angles) are fine as historical record but could be marked "not pursued" more explicitly if this document is ever reused as a template.
- Consider adding one line to the caption explicitly naming the breakdown categories (F&B/lodging/transport/retail) for readers who don't swipe to Slide 4 — purely an engagement optimization, not a correctness issue.
- Design brief's Slide 4 color-order description ("gold/steel-gray/warm-white/charcoal") vs. image-jobs.json's size-based assignment ("largest=gold, 2nd=warm-white, 3rd=steel-gray, smallest=charcoal") are not contradictory but could be made more explicitly consistent in a future revision; this is resolved anyway by Section 11's instruction that the real proportional chart is hand-drawn in post, not AI-generated.

---

## Final publication package (post-corrections)

- **Strategy:** projects/bogota-forecast-discount/strategist-angle-brief.md — Angle 1 ("The Forecast Discount"), as corrected.
- **Copy:** projects/bogota-forecast-discount/content-copy.md — 8-slide carousel copy, cover headline Option 3, final caption, 5 hashtags, tag table (all unverified-flagged), as corrected.
- **Design brief:** projects/bogota-forecast-discount/design-brief.md — full visual spec and layout instructions, as corrected.
- **Image jobs:** projects/bogota-forecast-discount/image-jobs.json — 8 prompt jobs, status "images not yet generated — draft mode," unchanged (no issues found).

This is a complete, internally consistent, fact-safe draft-mode package ready for image generation via `/justpreneur-finish`. It is NOT ready for direct publication as-is, because no artwork exists yet — publication requires running the finish flow and then a second finish-mode QC pass (checks 6, 7, 9, 10) against the real rendered images before the final publish decision.

---

## Recommended posting window

Target slot 2026-10-15, 9:00 PM (today, per system date) remains reasonable. The concerts were Oct 2–3, and the city's post-event balance was released ~Oct 6–8, so by Oct 15 this is a ~1-2 week old story — past the "breaking news" window but well within range for an analysis/builder-lesson carousel, which trades on timeless applicability rather than news freshness. Evening (9:00 PM) is a standard high-engagement slot for carousel content. No urgency to move the slot earlier or later; if real images are not ready in time via `/justpreneur-finish`, prefer delaying the post over publishing without the finish-mode QC pass, rather than moving the slot earlier.

---

## Final pre-publish checklist (for the orchestrator / human publish decision)

1. [ ] Run `/justpreneur-finish` to generate real artwork from image-jobs.json and perform the Section 11 text-layout pass in design-brief.md.
2. [ ] Run a finish-mode QC pass (checks 6, 7, 9, 10: mobile readability, safe margins/cropping, no stray marks/watermarks, visual consistency) against the actual rendered PNGs.
3. [ ] Manually verify every numeral/date/label on the final rendered slides character-for-character against content-copy.md (per design-brief Section 11, step 5) — especially confirm the two COP bars never render as touching/merged/averaged.
4. [ ] Manually confirm (do not assume) every @handle in the tag table before tagging — all are currently unverified guesses; drop any that cannot be confirmed, and apply editorial judgment on whether to tag BTS's account at all.
5. [ ] Confirm JustPreneur wordmark renders correctly, legibly, and in the correct position on all 8 final slides.
6. [ ] Reconfirm hashtags are still exactly five and none have been co-opted/repurposed by unrelated communities since this review.
7. [ ] Obtain the one human publish confirmation before the post goes live (per orchestrator policy — QC does not publish).
