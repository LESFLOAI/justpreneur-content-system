# QC Report — "The Wolseley's Real Product Isn't The Hotel" (Wolseley Members Club reveal)
**Reviewed by:** Quality Control (final gate)
**Date/time checked:** 2026-10-18
**Mode:** DRAFT MODE (no real artwork exists — no image-generation API key in this cloud environment; checks 6, 7, 9, 10 assessed only at the spec/brief level and flagged as pending real-pixel re-verification)

**Inputs reviewed:**
- `research/2026-10-18-approved-facts-wolseley.md` (status: Cleared with qualifications)
- `content/justpreneur-copywriter-2026-10-18-wolseley-members-club.md`
- `projects/wolseley-members-club-real-asset/package.md`
- `projects/wolseley-members-club-real-asset/image-jobs.json`

## Verdict: PASS WITH CORRECTIONS

The package is well-constructed and shows careful, specific compliance with all eight Fact Verifier qualifications. I found two minor issues, both corrected directly during this review (no re-submission needed). No factual, legal, or guardrail violations were found.

---

## Required corrections (applied directly — no human action needed)

1. **Brand-name inconsistency — "Members' Club" vs. "Members Club" (Severity: Low, but a real naming-accuracy issue).**
   Slide 5 and the "Qualifications" list in the copy file used "Members' Club" (with an apostrophe), while Slides 2 and 4, the caption, and the Approved Facts Block all use the official unapostrophized name "Members Club." This was an internal inconsistency that also deviated from the approved facts' naming.
   - Fixed in `content/.../wolseley-members-club.md`: Slide 5 line and the qualifications list, both now read "Members Club."
   - Fixed in `package.md` Section 11 (Slide 5 layout instruction): now reads "Members Club: targeting Q2 2027."
   - `image-jobs.json` did not need changes (no baked-in text in image prompts).

2. **Internal spec contradiction — slide 8 wordmark placement vs. stated safe-margin exclusion zone (Severity: Low-medium, design-brief logic issue, not yet a pixel problem).**
   `package.md` Section 3 placed the closing JustPreneur wordmark at "100px from bottom edge," while Section 7's safe-margin rules state that all critical text must stay out of the bottom ~250px to avoid Instagram's caption/UI chrome and carousel dot-indicator. The wordmark placement sat inside the zone the brief itself says to avoid — an unresolved contradiction in the brief, independent of actual pixels.
   - Fixed by adding an explicit, documented exception in both Section 3 and Section 7 (the wordmark is a small discrete mark, not a line of readable copy, so it is deliberately exempted) and adding a new line item to the Pre-Finishing Checklist (Section 12) requiring this placement be re-verified against the real IG dot-indicator overlay once artwork exists in `/justpreneur-finish`, with instruction to nudge it upward if any clipping risk appears.

---

## Fact-by-fact verification against the Approved Facts Block

- News peg: every slide and the caption correctly frame Oct 7, 2026 as "the Members Club reveal" / "revealed its next move," never as "the launch" — correctly distinguished from the March 17, 2026 brand-launch announcement. **Confirmed compliant.**
- Room count: "76 rooms" stated as an exact figure, consistently, no range, no "76-77" outlier. **Confirmed compliant.**
- CEO name: "Dillip Rajakarier" spelled correctly (double "l") everywhere it appears (copy Slide 7, caption, package.md Section 11, Pre-Finishing Checklist). **Confirmed compliant.**
- No Jeremy King reaction, no Simpson's-in-the-Strand reference anywhere in copy, caption, tag list, or design brief — explicitly and correctly called out by the copywriter as deliberately omitted. **Confirmed compliant.**
- Hotel "early 2027" vs. club "Q2 2027" kept as two distinct, separately hedged targets, never merged into one date, both in copy (Slide 5, caption) and in the visual design (two separate timeline rails, explicit instruction never to merge them). **Confirmed compliant.**
- Membership fees: stated plainly as undisclosed ("Minor Hotels has not released pricing for the club"), no figure invented, and the artwork brief explicitly forbids any numeral/currency symbol anywhere on Slide 6, including inside the generated art. **Confirmed compliant.**
- No "18+ months/no CEO" stalled-expansion narrative used anywhere — correctly excluded rather than loosely attributed. **Confirmed compliant.**
- 2022 Corbin & King history/dispute: not referenced at all in this piece. Since it isn't present, the "must be framed as disputed, not asserted" requirement is satisfied vacuously — no violation.

One observation (not a required correction): Slide 7/caption refer to Rajakarier as "Minor Hotels CEO," while the Facts Block's own parenthetical describes him as "Minor International[/Minor Hotels] Group CEO." Both titles are used in real-world trade coverage for Rajakarier and are not contradictory (he holds both roles), so I did not treat this as a factual error — but flagging it so the human reviewer can confirm the title phrasing against the latest press material before publish, since title precision is one of the explicit QC checks.

A second observation on editorial framing (not a required correction): Slide 4 ("The Members Club is built to keep them — and generate revenue whether or not they ever book a room") and Slide 7's "the strategy sits under..." are stated in a flat, fact-like register, but they are JustPreneur's own strategic interpretation/thesis (the entire "Membership Model as the Real Asset" angle), not a reported fact from Minor Hotels. This is a legitimate, deliberate editorial framing for a business-strategy commentary account and isn't inconsistent with any approved fact, so I'm not requiring a change — but note it for awareness in case the human publisher wants an even softer hedge word (e.g., "seems built to") before posting.

---

## Design-brief / guardrail verification

- No real logos/trademarks (Minor Hotels, Wolseley, Chatwal, Hyatt) — explicitly and repeatedly forbidden in both `package.md` and every prompt in `image-jobs.json`. **Confirmed compliant at the spec level** (pending real-pixel confirmation once images are generated — deferred per draft-mode rules).
- No human likeness of Rajakarier or King — Slide 7's prompt explicitly and repeatedly forbids any human figure/silhouette/face/body/hands, using only abstract schematic shapes. **Confirmed compliant at the spec level.**
- No literal/identifiable depiction of 130 West 44th Street or the Chatwal building — every facade-related prompt (Slides 1, 3, 8) explicitly specifies "generic," "not a specific recognizable building," "not any specific real address." **Confirmed compliant at the spec level.**
- No stray numerals/currency symbols on the "undisclosed" pricing slide — Slide 6's prompt explicitly forbids "no digits, no currency symbols, no dollar signs, no placeholder digits or 'X' marks," and the layout instructions reinforce this. **Confirmed compliant.**
- On-image text matches approved copy exactly — verified line-by-line between `package.md` Section 11 and the copy file's Section 2; all lines matched verbatim except the "Members' Club" vs. "Members Club" discrepancy, now corrected (see above).

All of the above are necessarily "compliant at the spec/brief level" rather than pixel-verified, since no artwork exists yet in this draft-mode run. They are carried into `package.md`'s own Pre-Finishing Checklist (Section 12) for mandatory re-verification once `/justpreneur-finish` runs locally and real images exist.

---

## Copy, caption, hashtags, tags

- Entrepreneurial takeaway: immediately clear by Slide 4 and crystallized at Slide 8 ("build recurring revenue first; the room/product comes second"). **Pass.**
- Headline: "The Wolseley's Real Product Isn't The Hotel" — strong, accurate as an editorial framing device, not a misstatement of fact. **Pass.**
- Caption alignment with the planned artwork/copy: consistent — covers the same facts and hedges (76 rooms, two separate targets, undisclosed pricing, CEO name) as the slides. **Pass.**
- Hashtags: exactly 5, all relevant and non-redundant (#WolseleyMembersClub #MinorHotels #MembershipModel #HospitalityBusiness #FounderStrategy). **Pass.**
- Suggested Instagram tags: @minorhotels, @skift, @hotelsmag — all plausible and relevant, and the copywriter already flagged two of the three handles as unverified ("verify exact handle before posting"), which is the correct cautious posture. **Pass, pending the human's pre-publish handle verification (already flagged, not a new item).**
- JustPreneur spelling/brand visibility: spelled correctly everywhere it appears in both files; wordmark placement specified on every slide. **Pass.**
- Legal/reputational/copyright/impersonation risk: low. The piece is framed as business-strategy commentary/analysis (fair comment), omits all of the riskiest material (King reaction, CEO-vacancy narrative, Corbin & King dispute), uses no real names in imagery, and avoids inventing any unverified figures (pricing, dates). No concerns identified.

---

## Optional improvements (not required, separated from required corrections)

1. Consider whether "Minor Hotels CEO Dillip Rajakarier" should instead read "Minor International/Minor Hotels Group CEO" to mirror the Facts Block's own phrasing more precisely — likely unnecessary given real-world dual-title usage, but worth a quick human glance.
2. Consider a slightly softer hedge word on Slide 4's "is built to keep them... whether or not they ever book a room" (e.g., "seems built to" / "looks built to") to visually distinguish JustPreneur's strategic read from a literal company statement — purely a tone preference, not a factual problem.
3. Once real handles are verified for @minorhotels and @hotelsmag, remove the "(Verify exact handle before posting.)" caveats from the final posted caption (keep them in the working file until then).

---

## Final publication package (post-corrections)

- **Copy/caption/hashtags/tags:** `content/justpreneur-copywriter-2026-10-18-wolseley-members-club.md` (corrected; "Members Club" apostrophe fix applied, QC note appended).
- **Visual design brief + prompts:** `projects/wolseley-members-club-real-asset/package.md` (corrected; apostrophe fix, wordmark-placement contradiction resolved with documented exception, new checklist item added) and `projects/wolseley-members-club-real-asset/image-jobs.json` (unchanged — no corrections needed).
- **Artwork:** not yet generated (draft mode). Must be produced via `/justpreneur-finish` before this package can move to actual publish.

## Recommended posting window

The underlying news (Oct 7, 2026 Members Club reveal) is now 11 days old as of this review (2026-10-18). This is a strategy/business-model commentary angle rather than a breaking-news post, so some residual relevance remains, but freshness is decaying. Recommend generating final artwork and publishing within the next 2–4 days (by roughly 2026-10-22) to stay inside a reasonable "recent industry development" window; after that, consider re-anchoring the caption's opening line to a more evergreen framing ("Earlier this month, Wolseley revealed...") rather than the specific date-forward hook, since "On October 7, 2026" will read as stale further out.

## Final pre-publish checklist

- [ ] Run `/justpreneur-finish` locally to generate real artwork from `image-jobs.json` (requires image-generation API key).
- [ ] Re-run checks 6, 7, 9, 10 (mobile readability, safe margins/cropping, unwanted tiny text/watermarks, cross-slide visual consistency) against the real rendered images.
- [ ] Specifically re-verify the Slide 8 JustPreneur wordmark (bottom-center, 100px from bottom edge) against Instagram's real carousel dot-indicator/UI overlay; nudge upward if any clipping risk is visible.
- [ ] Confirm no generated artwork accidentally resembles the real Chatwal building/130 West 44th Street, contains real logos, or depicts a human likeness for Rajakarier/King.
- [ ] Verify the @minorhotels and @hotelsmag Instagram handles are correct before tagging (already flagged by the copywriter as unverified).
- [ ] Re-confirm "76," "Dillip Rajakarier," "early 2027"/"Q2 2027," and "undisclosed" render exactly as specified once real text is composited onto the artwork.
- [ ] Obtain the one human publish confirmation before this (or any) package goes live — nothing in this draft authorizes publishing on its own.
