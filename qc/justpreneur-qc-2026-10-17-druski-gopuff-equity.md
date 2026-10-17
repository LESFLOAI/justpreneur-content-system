# QC Report — Druski x Gopuff Equity Partnership (Draft Mode)
**Reviewer:** Quality Control / Publishing Agent
**Date checked:** 2026-10-17
**Mode:** Draft (no image-generation API key in this environment; checks 6, 7, 9, 10 pending real artwork)

## Verdict: Pass with corrections (applied)

## Inputs reviewed
- projects/druski-gopuff-equity-partnership/content-copy.md
- projects/druski-gopuff-equity-partnership/design-brief.md
- projects/druski-gopuff-equity-partnership/image-jobs.json
- research/fact-verifier-2026-10-17-druski-gopuff-equity.md (Approved Facts Block + mandatory hedges)

## Checks performed
1-5, 8, 11-14 (facts, names/spellings, attribution/uncertainty, takeaway clarity, headline, brand spelling, caption/hashtag/tag quality, legal/reputational/impersonation risk) — full review.
6, 7, 9, 10 (mobile readability, safe margins/cropping, stray marks, cross-slide visual consistency of actual pixels) — **pending**, no real artwork exists yet; design-brief specs for these were reviewed on paper and are sound (60px safe margin, equal-weight hedge typography, consistent navy/gray/white/gold palette, wordmark placement).

## Findings
- All 8 mandatory hedges verified present and correctly worded in copy, caption, design brief, and image prompts: no equity %/valuation stated; all deal specifics attributed to "Gopuff's announcement"/"according to the company"; Gola quote explicitly framed as a company statement, not an interview; caption uses the exact required phrase "widely reported based on one company announcement — not independently verified deal terms"; no Druski birth year/place anywhere; all 5 tag handles flagged unverified; no real photography/logos/likeness anywhere in design brief or the 8 image prompts (Gopuff, Tom Brady, Yakir Gola, Druski all abstract/typographic only); hedge language specified at equal visual weight throughout (explicitly called out in Sections 2, 4, 9, 11 of the design brief).
- Names/spellings verified against facts block: Druski (Drew Desbordes), Coulda Been Records, 4Lifers Entertainment, Yakir Gola, "A true creative and commercial partnership" quote — all exact matches. Headline, slides, and caption are internally consistent. Hashtags: exactly 5, relevant, non-spammy. Tag list: 5 suggestions, all correctly caveated.
- **Correction applied:** The fact-verifier's Required Attribution Language explicitly calls for "reportedly" or "according to the company" when restating the HARD PASS/Tom Brady connection. Slide 6 and the caption stated this connection with unhedged certainty ("Druski previously appeared..." / "the campaign... got Druski in the door"). Added "reportedly" to content-copy.md (Slide 6, caption) and design-brief.md (Slide 6 description, Section 11 layout instructions) to bring this in line with the Approved Facts Block's own phrasing ("The deal reportedly builds on a prior relationship...").
- No legal/reputational/impersonation concerns found; no real likenesses or logos anywhere in draft copy or prompts.

## Optional improvements (not required)
- Consider adding "(unverified)" directly beside @druski and @couldabeenrecords handles in the on-platform tag UI as a final human reminder before posting, beyond the written caveats already present.

## Recommended posting window
Same-day/next-day relevance window — story broke Oct 9, 2026, already recirculated through Oct 12; post within 24-48 hours of this QC pass (i.e., by 2026-10-19) to stay inside the news cycle before it's stale.

## Final pre-publish checklist
- [ ] Generate real artwork via `/justpreneur-finish`, then re-run checks 6/7/9/10 (mobile readability, safe margins, stray marks/watermarks, cross-slide visual consistency).
- [ ] Human verifies all 5 tagged handles (@gopuff, @druski, @couldabeenrecords, @tombrady, @adweek) before tagging.
- [ ] Confirm no equity percentage/valuation language was introduced during image/text-overlay production.
- [ ] Final human publish confirmation per JustPreneur process.
