# QC Report — Pop Mart Hit-Dependency Carousel (Draft Mode)

**Reviewer:** JustPreneur Quality-Control & Publishing Agent (independent)
**Date/time checked:** 2026-10-09
**Mode:** DRAFT MODE (no image-gen API key in this cloud run — no real pixels exist). Checks 6, 7, 9, 10 (mobile readability on real renders, safe-margin/cropping on real renders, tiny-text/watermark scan, cross-slide visual consistency on real renders) are **pending** until a Finish-mode pass runs on actual generated images. Everything else below was audited in full.

**Files reviewed:**
- `projects/pop-mart-hit-dependency/approved-facts-block.md` (Fact Verifier, status: Cleared with qualifications)
- `projects/pop-mart-hit-dependency/content-copy.md` (Copywriter output — corrected during this QC pass)
- `projects/pop-mart-hit-dependency/design-brief.md` (Visual Director output — corrected during this QC pass)
- `projects/pop-mart-hit-dependency/image-jobs.json` (Visual Director output — one entry corrected during this QC pass)

---

## Verdict: PASS WITH CORRECTIONS

All required corrections listed below have already been applied directly to `content-copy.md`, `design-brief.md`, and `image-jobs.json`. No remaining blocking issues. Draft-mode design/prompt checks (zero Pop Mart/Labubu trademark or likeness use) pass cleanly; pixel-level checks remain pending for the Finish-mode pass.

---

## Required Corrections (applied) — ranked by severity

**1. [HIGH — factual fabrication] Slide 4 and the caption described an unverified second ~20–23% stock-price crash in "May 2026."**
The Approved Facts Block verifies only ONE ~20–23% stock-price decline event (March 25, 2026, tied to FY2025 results) and a separate, distinct August 21, 2026 reaction (8.8% intraday / -3.1% close). The May 2026 item in the facts block is an **analyst estimate downgrade** (Morgan Stanley cut its 2026 growth estimate to 13% vs. the company's own "no less than 20%" guidance; Deutsche Bank modeled a 2% revenue decline) — not a reported stock-price move of 20–23%. The original copy's "May 2026: It Happens Again — Another drop in the same 20–23% range" and the caption's "the market panicked twice... each time the stock falling 20–23%" invented a second price-crash statistic not present anywhere in the verified facts.
*Correction applied:* Rewrote Slide 4 headline/copy to "May 2026: Wall Street Piles On — Morgan Stanley cuts its 2026 growth estimate to 13%... Deutsche Bank models an outright revenue decline" (fully supported by the facts block). Rewrote the caption's "twice this year" paragraph to distinguish the verified March price decline from the verified May analyst-downgrade event. Updated `design-brief.md` (Section 3, Section 8 rule 3, Section 10/11, image-jobs.json slide-4 entry) to re-describe the Slide 4 graphic's narrative framing accordingly — the underlying abstract visual (a textless downward-trend line chart) did not need to change, since it never specified a literal price figure.

**2. [MEDIUM — fabricated-looking quotation, resolved by fix #1] Slide 4 originally presented `"Pop Mart is too dependent on one toy."` in quotation marks as if it were a verbatim published headline.** No such exact quote is sourced in the Approved Facts Block. This risk is removed as a side effect of the Slide 4 rewrite in correction #1 (the line no longer appears).

**3. [MEDIUM — echoes a banned framing] Slide 3's original supporting copy read "on fears the Labubu craze is cooling."** The Fact Verifier explicitly required that "cooling demand for Labubu" (as a Labubu-product-specific claim) never be used anywhere in the piece — only a broader "overseas sales slowdown" framing is supported, and no source ties the March 2026 decline causally to "the Labubu craze cooling" specifically.
*Correction applied:* Changed to "on fears its growth is slowing" in `content-copy.md` Slide 3 and the matching line in `design-brief.md` Sections 3 and 11.

**4. [MEDIUM — attribution/uncertainty not preserved] The "may fall short of its 20% growth target" claim is Yicai Global's characterization of CEO Wang Ning's remarks, and the Fact Verifier flagged that at least one other outlet characterized management's position more optimistically.** The original caption stated this flatly as "a caution that growth may fall short" without attributing the characterization to its source.
*Correction applied:* Caption now reads "...according to Yicai Global's report on CEO Wang Ning's remarks, growth may fall short of its 20% target..." The slide-level copy (Slide 5) was left concise ("Pop Mart says it may fall short...") for mobile-readability reasons — it still attributes to the company and uses the Fact-Verifier-approved hedge ("may fall short," never "will miss"/"missed").

**5. [MEDIUM — inference presented as confirmed fact] Several lines asserted, as flat fact, that Pop Mart deliberately and on a specific timeline "cut" its Labubu dependency as a planned corporate decision** ("It was a company already mid-plan," "It had already cut its own dependency on schedule"). The Approved Facts Block (Section 3) explicitly states that framing the revenue-mix shift as a *direct, management-stated, scheduled response* to dependency concerns is a reasonable inference / analyst interpretation, not a verbatim company statement, and must be labeled as such, not asserted as settled fact.
*Correction applied:* Softened Slide 7 ("This wasn't a reaction to bad news — the numbers show the change was already underway") and the caption's parallel line ("the shift in its revenue mix was already showing up in the numbers") to describe the *observed, verified timing* of the data (which is factually true — the H1 2026 concentration drop did precede the Aug 21 public caution) without asserting unverified claims about Pop Mart's internal intent or scheduling. Softened the cover headline from "Pop Mart Cut Its Biggest Risk Before Anyone Called It a Risk" (active, deliberate-agency framing) to "Pop Mart's Biggest Risk Was Shrinking Before Anyone Called It a Risk" (describes the verified trend without asserting deliberate corporate intent). Left Slide 8's general entrepreneurial-advice language ("It's a decision made on a schedule — before you need it to save you") unchanged, as it reads as generalized advice to the reader's own business rather than a specific factual claim about Pop Mart's internal process.

**6. [LOW/PROCESS — unverified tag accounts] None of the five suggested tag accounts (@popmart, @cnbc, @bloomberg, @forbes, @businessinsider) have been independently verified by this pipeline** (no handle-resolution check was run). Tagging an incorrect or unverified account risks impersonation/affiliation-implication problems, particularly for @popmart.
*Correction applied:* Added an explicit "Verification status" note under "Accounts to Tag" in `content-copy.md` requiring human confirmation of every handle (especially @popmart) before publishing, and flagged the same in the Copy Approval Block.

---

## Checklist walkthrough

**1. Facts vs. Approved Facts Block.** All required Fact-Verifier corrections are now satisfied: "may fall short of" used throughout, never "will miss"/"missed"; "overseas sales slowdown" used for the Aug 21 commentary (not Labubu-specific cooling language — and the Labubu-specific cooling phrase that had leaked into Slide 3 has been removed); Skullpanda is not mentioned anywhere (no mislabeling risk); home appliances are not presented as a comparable pillar (not mentioned in the copy at all); no Q3 2026 date is stated anywhere; every citation of 38.1% is explicitly labeled "FY2025" and the piece's central comparison (Slide 6, caption) pairs it with ~26% H1 2026, with 38.1% never presented as current; all stock-decline figures are now expressed only as the verified ranges/events actually in the facts block (March ~20–23%; May = analyst estimate cuts, not a price-crash percentage).

**2. Image-jobs.json / trademark check — zero tolerance.** Confirmed clean. All eight prompts are explicitly abstract (pie wedges, line charts, a faceless rounded-box silhouette, a timeline rail, a compass/arrow) and each prompt explicitly instructs "no logos, no brand marks, no toy imagery, no real toy character likeness, no packaging, no photorealism." No Pop Mart or Labubu name, logo, trademark, or character likeness appears in any prompt. Passes cleanly.

**3. Standard guardrails.** Hashtags are exactly 5 and topically consistent with the copy (#PopMart #Labubu #BusinessStrategy #RiskManagement #Entrepreneurship). Caption now aligns with the corrected slide narrative (no more orphaned/fabricated May price-crash claim). Mobile-readability is addressed thoroughly at the brief level (Section 4 typography minimums, Section 7 safe margins, Section 9 contrast ratios) — this is as far as "mobile readability" can be verified in draft mode; a Finish-mode pass must re-check actual rendered type at thumbnail size. Tag-account verification gap flagged and documented (correction #6 above).

**4. Financial/editorial-risk check.** The piece reads as fair editorial business-strategy commentary, not financial advice, insider-information claims, or market-manipulation framing — there is no buy/sell recommendation and no claim of non-public information. All forward-looking language (the 20% growth target risk, the analyst estimates) is explicitly attributed to the company's own cautionary statement or to named third-party analysts (Morgan Stanley, Deutsche Bank), never presented as JustPreneur's own prediction. The one remaining editorializing risk — implying deliberate corporate intent/scheduling behind the Labubu-concentration decline — has been softened per correction #5 so the piece asserts only the verified, sourced trend rather than an unverified claim about the company's internal motives.

**5. Headline strength/accuracy.** Strong and attention-grabbing; accuracy improved per correction #5 (removed the implied-deliberate-agency verb "Cut" in favor of the verified, observed trend "Was Shrinking").

**6–7, 9–10 (pixel-dependent checks).** Not applicable yet — no real artwork exists. Design brief pre-emptively addresses most of these at the specification level (safe margins, no slide numbers/extra logos/production marks, consistency rules), but must be re-verified against actual rendered images in a Finish-mode QC pass before publish.

**8. JustPreneur spelling/brand visibility.** "JustPreneur" and "@justpreneur_hq" spelled correctly and consistently throughout both files; wordmark placement/consistency specified for every slide in the design brief.

**11–14.** Caption-to-artwork alignment is consistent at the brief-description level (cannot be pixel-verified yet). Hashtag count correct (exactly 5). Tag-account accuracy flagged as unverified pending human confirmation (correction #6). No copyright/impersonation risk identified in the design brief (abstract-only visuals); no defamation/market-manipulation risk identified in the copy after corrections.

---

## Optional improvements (not required, not applied)

- Consider adding a brief caption footnote or a 9th "sources" slide/story-sticker noting "H1 2026 results, HKEX filing; Yicai Global; SCMP; Morgan Stanley/Deutsche Bank research notes" for extra credibility and defensibility, though not required for an Instagram carousel format.
- Consider softening "Diversification isn't a headline reaction. It's a decision made on a schedule" (Slide 8/caption) slightly further if the team wants to fully decouple the general lesson from any residual implication about Pop Mart's specific internal process — current wording is acceptable as generalized advice to the reader, not a factual claim about Pop Mart.
- Consider shortening the new Slide 4 supporting copy slightly further for mobile glanceability once real type rendering is tested (two analyst figures in one line is information-dense; test at thumbnail size in Finish mode).

---

## Final publication package (post-correction)

- `projects/pop-mart-hit-dependency/content-copy.md` — corrected cover headline, Slide 3, Slide 4, Slide 7, caption, and tag-verification note.
- `projects/pop-mart-hit-dependency/design-brief.md` — corrected Slide 1 headline, Slide 3 copy, Slide 4 headline/copy/graphic narrative, Section 8 rule 3, Section 10/11 text to match.
- `projects/pop-mart-hit-dependency/image-jobs.json` — slide-4 prompt re-described (abstract visual unchanged; narrative framing corrected; still zero trademark/likeness risk).
- `projects/pop-mart-hit-dependency/approved-facts-block.md` — unchanged (source of truth).

All four files are internally consistent with each other as of this QC pass.

---

## Recommended posting window

The story's news hook (H1 2026 results, Aug 20–21, 2026) is now ~7 weeks old as of today (2026-10-09); there is no confirmed Q3 2026 trading-update date to time against (per the facts block, this must not be stated as confirmed). Recommend posting within the next 3–5 days to stay reasonably close to the ongoing news cycle (the story is evergreen-adjacent — "diversification as a scheduled decision" — so it is not highly time-sensitive, but freshness still helps engagement). Avoid scheduling it to coincide with or immediately precede any unconfirmed Q3 2026 trading-update date; if Pop Mart issues new results before this is published, re-verify the facts block is still current before publishing.

---

## Final pre-publish checklist

- [ ] Finish-mode QC pass completed on real generated artwork (checks 6, 7, 9, 10): mobile readability at thumbnail size, safe margins/cropping, no stray tiny text/icons/watermarks/slide numbers, visual consistency across all 8 slides (especially Slides 2/6 numeral parity and Slides 3/4 template matching).
- [ ] Human has independently confirmed all 5 tag-account handles resolve to the correct, active official accounts (@popmart in particular) before tagging.
- [ ] Final side-by-side zoom check of Slides 2 and 6 (numeral parity) and Slides 3 and 4 (template matching) per design-brief Section 11.
- [ ] Confirm no Pop Mart/Labubu logo, trademark, or character likeness appears in any final rendered image (re-confirm after generation, not just in the prompt).
- [ ] Reconfirm hashtags still exactly 5 and unchanged at final export.
- [ ] Reconfirm caption text matches the corrected version in `content-copy.md` exactly (no stale/original draft text accidentally reused).
- [ ] One human publish-confirmation step completed per JustPreneur process (this QC pass does not constitute publish approval).
