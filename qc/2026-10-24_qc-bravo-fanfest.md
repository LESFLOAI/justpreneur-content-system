# JustPreneur QC Report — bravo-fanfest-gap-year-play
**Draft cycle:** 2026-10-24
**Mode:** DRAFT MODE (no image-generation API key in this environment — audited design brief + image prompts as specifications, not rendered pixels)
**Reviewer:** Quality Control / Publishing Agent (independent final gate)
**Files reviewed:**
- projects/bravo-fanfest-gap-year-play/content-copy.md
- projects/bravo-fanfest-gap-year-play/design-brief.md
- projects/bravo-fanfest-gap-year-play/image-jobs.json

---

## Verdict: **PASS WITH CORRECTIONS**

The package is fundamentally sound: no fabricated facts, no real-person likeness, no logo/trade-dress exposure, slide counts match across all three files (8/8/8), hashtag count is exactly 5, and the majority of required hedges (attendance estimates, "announced for fall 2027," ticket-price-vs-resale separation, sold-out attribution, no-revenue disclaimer) survive intact in the actual slide text and caption — not just in a footnote. However, three issues must be corrected before this goes to the publish-confirmation step, plus one standing process flag that must be re-checked at the moment of actual publish.

---

## Required Corrections (ranked by severity)

### 1. (High) Sponsor list stated as unattributed fact — missing required hedge
**Where:** content-copy.md Slide 7, content-copy.md Final Caption, design-brief.md Slide 7 "Text to add."

- Slide 7 currently reads: *"Seven sponsors: Ally Bank, Colgate Optic White, Genesis, Planet Fitness, State Farm, Wayfair, Wendy's."*
- Caption currently reads: *"Seven sponsors are on board..."*
- Design brief Slide 7 layout note: *"Line: '7 sponsors.'"*

None of these carry the Approved Facts Block's required attribution: *"7 sponsors ... per Bravo/Peacock's own coverage, not an independently confirmed press release."* This is the one approved hedge that got dropped from the live slide/caption text (every other hedge made it through).

**Fix (apply verbatim or equivalent):**
- content-copy.md Slide 7 → *"Seven sponsors, per Bravo/Peacock's own coverage (not an independently confirmed press release): Ally Bank, Colgate Optic White, Genesis, Planet Fitness, State Farm, Wayfair, Wendy's."*
- Final Caption → *"Seven sponsors are on board, per Bravo/Peacock's own coverage, and Peacock is streaming the panels."* (pending correction #2 below on the Peacock streaming clause)
- design-brief.md Slide 7 layout note → *"Line: '7 sponsors (per Bravo/Peacock's own coverage).'"*

### 2. (High) "Peacock streaming main-stage panels live and on-demand" is not in the Approved Facts Block
**Where:** content-copy.md Slide 7, content-copy.md Final Caption, design-brief.md Slide 7 "Text to add."

This claim appears three times but is absent from the Approved Facts Block supplied for this audit, and carries no attribution. Every other factual claim in the package traces back to a named, hedged source in the facts block; this one does not. As written it reads as independently verified fact when it is unsourced in the materials I was given to check against.

**Fix:** Either
- (a) **Remove** the Peacock-streaming line from Slide 7, the caption, and the design-brief Slide 7 text-to-add (safest default, since no source is specified in the facts block I audited against), or
- (b) If the Strategist/Copywriter has a specific source for it, add it to the Approved Facts Block and attribute it on-slide (e.g., "Peacock is streaming main-stage panels, per Bravo/Peacock's own coverage") before this goes further.

Do not publish with the current unattributed phrasing either way.

### 3. (Medium) "23-month gap" states false precision against an unfixed future date
**Where:** content-copy.md Slide 4 ("Then: a 23-month gap."), design-brief.md Slide 4 (rendered as a bold gold stat-numeral headline: "23-MONTH GAP," using the same hard-data visual treatment as the audited-style stats).

The Approved Facts Block only supports "announced for fall 2027" — no month, date, or venue. "Fall" spans roughly late September through December, so the actual gap from BravoCon 2025 (Nov 2025) could run anywhere from ~22 to ~25 months. Stating "23-month gap" as an exact figure, and visually treating it as a hard numeral stat chip (same gold-numeral tier as "$475," "27,000," etc.), overstates precision on a figure built from an unconfirmed future date.

**Fix:**
- content-copy.md Slide 4 → soften to *"Then: roughly a two-year gap"* or *"Then: an estimated ~23-month gap (exact BravoCon 2027 dates not yet announced)."*
- design-brief.md Slide 4 → downgrade "23-MONTH GAP" from a bare hard-numeral headline treatment to a hedged version (e.g., "~23-MONTH GAP (EST.)" or pair it with the same hedge-chip style already used for the attendance/price stats) so it doesn't visually read as audited data.

---

## Standing Process Flag (not a content error today, but required re-check before actual publish)

### 4. Date-sensitivity — Slides 5–6 and the caption use present/imminent tense tied to Oct 24, 2026
Today's date is **2026-10-24**, the same day as the event, so the current present/imminent tense ("Oct. 24, 2026: Bravo Fan Fest Charleston," "happening today," "two nights before") is accurate **right now**. Per design-brief.md Section 8, item 6: if this package is not actually published today, Slide 5, Slide 6, and the caption need a tense pass (e.g., "happened on Oct. 24" instead of present/imminent framing) before reuse. **Flag this explicitly to whoever executes the publish step — confirm the publish timestamp is still 2026-10-24 before posting as-is; if it slips to a later date, re-run the tense pass first.**

---

## Optional Improvements (not blocking)

- content-copy.md's headline-options footnote (not the chosen headline) includes the alt line *"Bravo Just Sold Out an Arena Anyway"* — North Charleston Performing Arts Center is not an arena. This alt line is not used in the published copy, but since it remains verbatim in the file, consider deleting or correcting it so it can't be mistakenly reused later.
- Once correction #3 is applied, consider giving the softened "~23-month" figure the same gold-outlined hedge-chip visual treatment already used for "estimated ~27,000," "neither number is an audited count," etc., for internal visual-system consistency.
- The venue-handle row in Suggested Instagram Tags could include a best-guess handle string (e.g., "@ncpac_official") explicitly marked unverified, purely for operator convenience — current phrasing is already safely hedged, so this is cosmetic only.

---

## Checklist Results (against the 14-point QC checklist)

1. **Factual claims vs. Approved Facts Block:** Mostly clean. Two drift issues found and corrected above (sponsor attribution dropped; Peacock-streaming claim unsourced against the supplied facts block).
2. **Names/spellings/titles/dates/numbers/quotations:** Clean, except the false-precision "23-month gap" (#3 above). "Andy Cohen," "Bravolebrities," "Post and Courier," "North Charleston Performing Arts Center," "Colgate Optic White" all spelled correctly and consistently across all three files.
3. **Attribution/uncertainty preserved:** Attendance estimates, "announced for fall 2027" (not confirmed/scheduled), ticket-price-vs-resale separation, sold-out attribution, and the no-revenue disclaimer all survive intact in the live slide copy and caption — not just a footnote. Sponsor attribution is the one hedge that did not survive (#1).
4. **Entrepreneurial takeaway immediately clear:** Yes — Slide 8's "retention play" framing and the calendar-audit CTA are explicit and unambiguous; headline leads with the transferable lesson.
5. **Headline strength/accuracy:** Strong, accurate, factually neutral (no unhedged claims in the chosen headline itself).
6. **Mobile readability:** *Pending — draft mode, no rendered pixels.* Design-brief spec (min 36px body, 28px chip, ~72px headline, 1080x1350 canvas) is well-specified on paper; must be re-verified against actual renders.
7. **Safe margins/cropping risk:** *Pending — draft mode.* Spec calls for 90px side / 100px top-bottom margins and a 60px no-critical-text buffer plus a reserved bottom-right dead zone; sound on paper, unverified until real images exist.
8. **JustPreneur spelling/brand visibility:** Correct and consistent in both files; wordmark placement spec (top-center every slide, larger sign-off Slide 1/8) is clear and consistent.
9. **Unwanted tiny text/icons/watermarks/slide numbers/production marks:** *Pending — draft mode.* Image-jobs.json prompts explicitly exclude watermarks, logos, readable lettering, and slide-number labels (rail-dot system replaces an explicit "3 of 8" label) — well-specified, unverified until rendered.
10. **Visual consistency across slides:** *Pending — draft mode.* Design-brief Section 8 ("Slide-to-Slide Consistency Rules") specifies one consistent system; unverified until rendered.
11. **Caption alignment with artwork:** Caption's factual content matches the slide sequence and thesis; cannot fully confirm caption-to-artwork visual alignment until real images exist, but no mismatch in subject matter or claims.
12. **Exactly five hashtags:** Confirmed — #BravoFanFest #CustomerRetentionStrategy #BrandBuildingTips #EntrepreneurMindset #SmallBusinessStrategy (count = 5, all topically relevant).
13. **Suggested Instagram tags accuracy:** Confirmed — 5 tags listed, 3 of 5 (@andycohen, @bravocon, venue handle) correctly flagged "unverified — confirm before publish"; @bravotv and @peacock flagged "likely correct, confirm before publish." Matches expected pattern.
14. **Legal/reputational/copyright/impersonation risk:** No real-person likeness depicted in any image prompt; no network/show/sponsor logos or trade dress; Andy Cohen is referenced only via a factual, attributed public statement (not depicted). Sponsor company names appear as plain nominative text (not styled as logos), which is standard editorial use but is the reason attribution hedge #1 matters — naming real companies' sponsorship as settled fact without the "per Bravo/Peacock's own coverage" qualifier is the main residual risk, now flagged for correction.

---

## Final Publication Package (after corrections #1–#3 are applied)

- **Headline:** Between the Big Events Is Where the Real Business Gets Built
- **Slides 1–8:** As drafted in content-copy.md, with Slide 4 and Slide 7 text corrected per #1 and #3 above.
- **Caption:** As drafted, with the sponsor-attribution and Peacock-streaming clauses corrected per #1 and #2 above.
- **Hashtags:** #BravoFanFest #CustomerRetentionStrategy #BrandBuildingTips #EntrepreneurMindset #SmallBusinessStrategy (unchanged)
- **Tags:** @bravotv, @peacock, @andycohen (unverified), @bravocon (unverified), North Charleston Performing Arts Center venue handle (unverified) (unchanged)
- **Design brief / image-jobs.json:** No image-prompt changes required for legal/brand-safety guardrails (already clean); only the Slide 4 and Slide 7 "text to add" layout notes need the wording updates matching #1 and #3.

## Recommended Posting Window
Given the story's relevance is keyed to the event happening **today, Oct 24, 2026**, the highest-relevance window is **today, same-day, ideally within the next few hours** (afternoon/evening ET, while Fan Fest is live or just wrapping, to ride real-time search/social interest). If same-day publish is not possible, apply the Section 8.6 tense pass (flag #4) before posting on any later date — the story remains usable as a retrospective ("what Bravo did and why it worked") for roughly 1–2 weeks after, but loses urgency beyond that.

## Final Pre-Publish Checklist
- [ ] Apply correction #1: add sponsor-attribution hedge to Slide 7 copy, caption, and design-brief Slide 7 layout note.
- [ ] Apply correction #2: remove or source-and-attribute the Peacock-streaming claim in Slide 7 copy, caption, and design-brief Slide 7 layout note.
- [ ] Apply correction #3: soften "23-month gap" to a hedged figure in Slide 4 copy and downgrade its stat-numeral visual treatment in design-brief Slide 4.
- [ ] Confirm actual publish date/time is still 2026-10-24 before posting Slides 5–6/caption as-is; if not, run the Section 8.6 tense pass first.
- [ ] Once real artwork is generated (image-gen keys available / `/justpreneur-finish` run), re-run full QC checks 6, 7, 9, and 10 against rendered pixels before the publish-confirmation step.
- [ ] Confirm @bravotv, @peacock, @andycohen, @bravocon, and the venue handle before tagging at actual publish time (per existing "confirm before publish" flags already in the tag table).
