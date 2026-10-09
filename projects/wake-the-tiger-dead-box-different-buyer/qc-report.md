# QC Report — "Dead Box, Different Buyer" (Wake The Tiger / Absurd City)

Project: wake-the-tiger-dead-box-different-buyer
Reviewer: Quality Control (final gate)
Mode: **Draft mode** — no final artwork exists (cloud routine ran without image-generation keys). Checks 6, 7, 9, and 10 (pixel-level mobile legibility, cropping/safe-margin rendering, stray tiny text/watermarks, cross-slide visual consistency of actual rendered images) are **not possible yet** and are marked PENDING below. All other checks (facts, attribution, tone, takeaway, headline, caption/hashtag/tag quality, legal/reputational/impersonation risk, and whether the design brief *plans* correctly for the pending items) were run in full.
Inputs reviewed: `content-copy.md`, `design-brief.md`, `image-jobs.json`.

## Overall Verdict: **Pass with corrections**

The package is strategically sound, consistently hedged, and — critically — the single highest-risk item (Bristol-specific financing: Creative UK/Triodos "Creative Growth Finance," Bristol & Bath Regional Capital "City Funds") is **absent from every document reviewed**. It is not mentioned, implied, or alluded to anywhere in the copy, the design brief, or the image prompts. This is the correct outcome and is explicitly confirmed in the Copywriter's own handoff notes (the figures were deliberately excluded as off-thesis and Bristol-only). No correction needed there.

Two smaller internal-consistency corrections are required before this is publish-ready, plus one cosmetic tag-table nit. Details below.

---

## Required Corrections (ranked by severity)

**1. (Moderate) Square-footage figure is stated two different ways with no reconciliation.**
Slide 1 headline/cover copy states the figure as a bare, unhedged number: *"SAME 80,000 SQUARE FEET."* Slide 3 copy, describing the same physical space, hedges it: *"Same ~80,000 sq ft shell."* Two different certainty levels for the identical fact, inside the same 9-slide piece, is the kind of inconsistency that erodes credibility and invites a "which is it" challenge in comments.
- Fix: confirm against the Approved Facts Block whether 80,000 sq ft is an exact, sourced figure (e.g., from a property listing or official release) or an approximation reported in press coverage. Then make the treatment consistent everywhere the number appears (headline, Slide 1 support line, Slide 3) — either drop the "~" in Slide 3 (if exact) or add an "approx./~" qualifier to the headline and Slide 1 (if approximate). Headlines can reasonably round a number, but they should not present as certain a figure the body copy itself calls approximate.

**2. (Moderate) The Boomtown Fair founding claim is hedged inconsistently across the package.**
Slide 3 and the caption both state as flat fact: *"New operator: Wake The Tiger — founded by members of the Boomtown Fair festival team."* But the Accounts-to-Tag table, justifying `@boomtownfair`, describes the same claim with a hedge: *"Wake The Tiger's founders are **reported** as members of the Boomtown Fair festival team."* This is the same underlying fact given two different confidence levels in the same document. Per the brief's own standard (preserve attribution/uncertainty), this needs to be resolved one way, not left split.
- Fix: check the Approved Facts Block for how confidently this is sourced. If it's a company self-statement or lightly-sourced report, add a light hedge to Slide 3/caption as well (e.g., "founded by members of the Boomtown Fair festival team, per the company" or similar, without over-qualifying a short slide line). If it's solidly confirmed (e.g., stated on Wake The Tiger's own official "About" materials), soften the tag-table language to match instead. Either direction is fine; the inconsistency itself is the problem.

**3. (Low) Draft-mode items remain genuinely pending, not yet cleared.**
Checks 6, 7, 9, and 10 cannot be signed off until real images exist. The design brief's *plans* for these are sound (matching camera angle/outline for Slides 2–3, consistent wordmark position/size, explicit "no baked-in text/logos/signage" instruction on every single image prompt, defined safe-margin and contrast rules, explicit instruction never to depict Absurd City as already operating/crowded). This is a planning pass, not a final pass — flag clearly in the handoff that a second QC pass against actual rendered images is still required after `/justpreneur-finish` runs, before the one human publish confirmation.

---

## Optional Improvements (not blocking)

- The confidence language across the four tag candidates is uneven: `@wakethetiger` and `@westfieldlondon` are described as "reasonably confident exists — verify," while `@boomtownfair` and `@bcorporation` are "flag for verification — not confirmed." None are asserted as confirmed, which satisfies the hard requirement, but standardizing all four to the same "unverified — confirm exact handle before publish" phrasing would remove any implied gradient of certainty that hasn't actually been checked.
- Consider whether Slide 3's eyebrow label "ABSURD CITY — OPENING OCT 15, 2026" reads unambiguously as a future/scheduled state on first glance (it does, aided by the explicit disclaimers on Slides 5 and 9 and in the caption) — no change required, just worth a final human eyeball once laid out with real type.

---

## Checklist Walkthrough

1. **Factual claims vs. Approved Facts Block** — Consistent with what's documented in both agents' handoff blocks; no invented facts found. Two numeric/attribution phrasing inconsistencies noted above (corrections 1–2).
2. **Names, spellings, job titles, dates, numbers, quotations** — Edutainment Operations Limited, Graham MacVoy (CEO), Luke Mitchell (Chief Creative Officer), Jan 2/11 2024 dates, July 21 2026 ticket date, Oct 15 2026 opening date all appear identically in both the copy and the design-brief layout section (verbatim pass-through confirmed line by line). No quotations are used in this piece, so no quote-accuracy risk.
3. **Attribution and uncertainty preserved** — Largely yes: Bristol visitor figures are "reportedly... per Wake The Tiger"; B Corp "UK's first" is explicitly flagged "a self-description, not an independently verified superlative"; district count is "reports vary on the exact number"; no ticket price asserted. The one gap is the Boomtown Fair hedge inconsistency (correction 2).
4. **Entrepreneurial takeaway immediately clear** — Yes. Slides 6–8 state the diagnostic framework (execution failure vs. audience-fit failure) and the closing line ("didn't need a new unit... needed a new customer") lands the thesis cleanly even skimmed on mobile.
5. **Headline strength and accuracy** — Strong, concrete, neutral-toned, and works cold (no sound needed). Accuracy caveat is the 80,000 vs. ~80,000 sq ft issue above.
6. **Mobile readability** — PENDING (draft mode, no rendered pixels). Planning is solid: type-size floors specified (56–64px headlines, no sub-32px body), max ~60–65 characters per line, high-contrast palette pairings called out with WCAG AA target.
7. **Safe margins and cropping risk** — PENDING (draft mode). Plan specifies 96px safe margin all sides, extra 120px bottom / 80px top avoidance zones, and wordmark placement math that clears both — looks correctly specified on paper.
8. **JustPreneur spelling and brand visibility** — Spelled correctly and consistently throughout the design brief ("JustPreneur," bottom-center, identical treatment every slide). Not referenced in the slide copy itself, which is expected (wordmark is a design-layer element, not body copy).
9. **Unwanted tiny text/icons/watermarks/slide numbers/production marks** — PENDING (draft mode, no pixels to inspect). Every one of the nine image prompts explicitly instructs "no text, no numbers, no logos, no signage, no fake logos" — strong protective instruction baked in; final check still required once rendered.
10. **Visual consistency across slides** — PENDING for rendered pixels, but the *plan* is strong: Slides 2/3 locked to identical camera angle/outline shape (the explicit "core visual thesis" rule), recurring floor-plan watermark threaded through 1, 4, 6, 7, 8, consistent palette-by-state logic, identical wordmark treatment every slide.
11. **Caption alignment with artwork** — Caption's "Same shell. Different buyer." and the before/after framing match the planned bisected floor-plan / closed-vs-glowing motif concept. Full confirmation pending real images.
12. **Exactly five hashtags** — Confirmed: `#AbsurdCityLondon #WakeTheTiger #WestfieldLondon #RepositioningStrategy #BusinessStrategy`. Five, relevant, no duplicates, no banned/spam tags.
13. **Accuracy of suggested Instagram tags** — All four candidates are correctly flagged as unverified/needing manual confirmation before publish; none asserted as confirmed. Minor phrasing-consistency nit noted in Optional Improvements.
14. **Legal/reputational/copyright/impersonation risk** — No licensed or literal depictions of either brand's actual décor/signage/logos are planned; all imagery is original abstract/illustrative. No real individual's likeness is to be rendered. Tone toward the liquidated KidZania operator (Edutainment Operations Limited) is factual and neutral throughout — closure and liquidation dates stated plainly, "the unit sat empty," no blame or mockery language, and the design brief explicitly protects this ("not decayed/trashed... neutral in tone"). The Bristol funding risk flagged by Fact Verification is fully absent from the package — confirmed clean.

---

## Final Publication Package (pending the two required text corrections above)

- **Headline:** "Same 80,000 Square Feet. Completely Different Business." *(confirm/reconcile sq-ft hedge per Correction 1 before lock)*
- **Slides 1–9:** As written in `content-copy.md` Section 3 *(confirm/reconcile Boomtown Fair hedge per Correction 2 before lock)*
- **Caption:** As written in `content-copy.md` Section 4
- **Hashtags:** #AbsurdCityLondon #WakeTheTiger #WestfieldLondon #RepositioningStrategy #BusinessStrategy
- **Tags (all unverified, confirm handles before publish):** @wakethetiger, @westfieldlondon, @boomtownfair, @bcorporation
- **Visual spec:** `design-brief.md` + `image-jobs.json`, unchanged — no creative-direction issues found; only the pending rendered-artwork checks remain before final sign-off.

## Recommended Posting Window

Target slot (2026-10-09, 9:00 PM) is appropriate and should be kept or moved earlier, not later. The entire piece depends on the "not yet opened / scheduled bet" framing being true at publish time — that framing is accurate any day through Oct 14, 2026. If the actual publish date slips to Oct 15, 2026 or later, the copy, caption, and all nine image prompts must be re-reviewed and updated to reflect that the opening has occurred (the disclaimers in Slide 9/caption would otherwise be stale or misleading). Recommend locking publish no later than Oct 14, 2026, evening slot, to stay inside the "countdown to a real-world event" news hook while the story is maximally topical.

## Final Pre-Publish Checklist

- [ ] Correction 1 resolved: 80,000 sq ft figure treated consistently (exact vs. approximate) across headline, Slide 1, and Slide 3
- [ ] Correction 2 resolved: Boomtown Fair founding claim hedged consistently across Slide 3, caption, and tag-justification table
- [ ] All four @-handles manually verified as the correct, currently-active accounts immediately before publish
- [ ] Images generated via `/justpreneur-finish` against the unchanged `image-jobs.json`
- [ ] Second QC pass run against rendered images specifically for: mobile legibility at actual size, safe-margin/cropping on a real device preview, absence of any stray baked-in text/logos/watermarks, and Slide 2/3 angle-and-scale match
- [ ] Confirm publish date is on or before Oct 14, 2026 (or re-verify tense/disclaimers if later)
- [ ] One human publish confirmation obtained before the post goes live
