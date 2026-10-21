# QC Findings — Getty Images "The Vote Was Already Won" (DRAFT MODE)

Reviewed:
- /tmp/claude-0/-home-user-justpreneur-content-system/8bff9b8b-ecb3-5630-b6b6-39905d944362/scratchpad/getty_vote_already_won_carousel.md
- /home/user/justpreneur-content-system/projects/getty-vote-already-won/design-brief.md
- /home/user/justpreneur-content-system/projects/getty-vote-already-won/image-jobs.json

Mode confirmed: DRAFT MODE. No image files exist; design brief and image-jobs.json explicitly and repeatedly state no image-generation key is available and `scripts/generate_images.py` has not run. Checks 6, 7, 9, 10 (mobile readability, safe margins/cropping, unwanted tiny text/watermarks on actual pixels, cross-slide visual consistency on actual pixels) are PENDING by design and were not evaluated against real artwork — only against the brief/prompts' stated intent, which is internally consistent and well-specified.

## VERDICT: PASS WITH CORRECTIONS (not a Fail — no critical guardrail was violated)

No instance of the two NOT VERIFIED figures (~$143M Koch DIP financing; ~$433M net-of-conversion figure) appears anywhere in copy, design brief, or image-jobs.json. Shareholder wipeout is stated clearly and is NOT minimized (Slide 6 copy, design brief, and image prompt all reinforce this deliberately). No implication the bankruptcy is fake/deceptive — caption explicitly states "this is a legitimate, court-supervised process... not a workaround, not a trick." The $100M+ figure is never labeled a "breakup fee" anywhere, and the design brief/image-jobs explicitly instruct against doing so. The UK regulator is correctly framed as conditioning clearance on a divestiture that Getty declined — never described as having "blocked" the deal. No regulator-bashing tone. No real logos, trademarks, courthouse likenesses, or named-executive likenesses in any image prompt — all explicitly negative-constrained. Exactly 5 hashtags, all relevant and tone-appropriate. JustPreneur brand name/handle spelled correctly throughout.

## Required corrections (ranked by severity)

1. **(Medium) Dropped attribution on the $100M+ figure.** The Approved Facts Block specifically attributes this figure to a statement by Getty's CEO: "Getty's CEO stated the company incurred more than $100 million..." This is a deliberate sourcing/uncertainty signal (it is management's own disclosed figure, not an independently audited number). The copy (Slide 5: "Cost of the chase: $100M+ in sunk professional and financing fees over 18+ months"), the caption ("...after already spending $100M+ chasing that deal..."), the design brief's Tier 3 line, and the image-jobs layout note all present this as a flat, unattributed fact. Add attribution (e.g., "per the company" / "Getty's CEO said the company spent...") to Slide 5 copy, the caption, the design-brief Tier 3 text, and the Section 11 layout note before finishing.

2. **(Medium) Cover headline carries out-of-context risk.** "Getty Images Didn't File for Bankruptcy. It Executed One." is a rhetorical device that is immediately corrected by the subtext and by the caption's first line ("On Oct 21, 2026, Getty Images filed for Chapter 11 bankruptcy."). But Slide 1 of a carousel is the single most commonly cropped/screenshotted/reshared frame on Instagram, and taken alone and literally, the sentence is false — Getty did file. Recommend either (a) swapping to Headline Option 2 ("The Vote Was Already Won Before the Public Knew There Was a Vote"), which carries the same thesis without a literal-falsehood risk, or (b) keeping Option 1 but only if the subtext is guaranteed to render in the same crop/aspect as the headline on the actual cover art once generated (verify at finishing time). This is a safety/precision issue, not a Fail-level fabrication, since full context within the same post corrects it.

3. **(Low/procedural) Unverified Instagram tag handles.** The copy file itself flags that @gettyimages, @kochind, @shutterstock, and @reuters handle spelling/active status have not been independently verified. Given this is a sensitive bankruptcy/shareholder-wipeout story, tagging an incorrect, inactive, or parody account would be a real reputational misstep. Required: verify all four handles resolve to the correct, active, official accounts before any tagging occurs at publish time.

4. **(Low) Inconsistent precision treatment of qualifiers.** The Approved Facts Block says "approximately 83.5%" and "approximately $2.1 billion"; the copy drops "approximately" for both of these while correctly retaining the "~" for the ~89% secured-lender figure. Not a factual error (the headline numbers are unchanged), but inconsistent — recommend normalizing (either keep "approximately"/"~" everywhere or drop it everywhere) for internal consistency.

## Optional improvements (not required)

- Caption line "Getty reported $2.1B in total debt as of June 30, 2026" shifts sourcing from the Approved Facts Block's "(Reuters, citing company financials)" to a direct "Getty reported." This is a common and generally acceptable journalistic simplification, but tightening to "according to Reuters" or "Getty's reported financials show" would track the source attribution more precisely.
- Approved Facts Block says "early July 2026"; copy/design brief shorten to "July 2026" throughout. Immaterial, but noted for completeness.
- Design brief's internal (non-public-facing) visual description for Slide 5 uses the word "blocked" to describe the abstract gate motif representing the declined divestiture condition. No literal text renders in the artwork, so public-facing risk is effectively nil, but worth a note to whoever finishes the art: don't let any added caption/alt-text for this slide drift toward "UK blocked the deal" phrasing — keep the "conditioned/declined" framing that the rest of the package correctly uses.
- Consider whether tagging the subject company and counterparties (@gettyimages, @kochind, @shutterstock) in a bankruptcy/wipeout story is strategically wise beyond the handle-verification issue above — standard financial-journalism practice, but flag for a human publish-time judgment call, not a blocker.

## Cross-file consistency check

Design brief Section 11 (layout/text-overlay instructions) quotes the copy file's Copy Approval Block verbatim for all 8 slides — confirmed line-for-line match for headline, subtext, Slides 2–7 primary/secondary lines, and Slide 8 pull-quote/lesson/CTA. No drift between the copy source of truth and the design brief. Image-jobs.json prompts match the design brief's per-slide composition descriptions (motifs, palette, tag-pill treatment, Slide 6's gold-free departure, Slide 5's compact/dense layout, Slide 7's generic-column caveat) with no contradictions found.

## Recommended posting window

The filing occurred today (Oct 21, 2026) and the story is maximally fresh right now. The brief's current schedule of 2026-10-21, 9:00 PM is a reasonable same-day window for a financial/business-news audience. Recommend posting within the next 24–48 hours while search/news interest is at its peak; if real artwork and finishing corrections above cannot be completed before tonight's 9:00 PM slot, the next-best window is tomorrow morning (first business-news cycle) rather than letting the story go stale past 48 hours. Before publishing, reconfirm no case developments (e.g., contested first-day hearing, amended plan terms) have emerged that would require a copy update, since this is an active, moving legal proceeding.

## Final pre-publish checklist

- [ ] Add attribution ("per the CEO" / "the company said") to the $100M+ figure in Slide 5 copy, caption, design-brief Tier 3 text, and image-jobs layout note.
- [ ] Resolve cover-headline out-of-context risk (swap headline or confirm subtext always travels with it in final art).
- [ ] Verify @gettyimages, @kochind, @shutterstock, @reuters handles are correct, active, and intended before tagging.
- [ ] Normalize "approximately"/"~" qualifier usage across the 83.5%, ~89%, and $2.1B figures.
- [ ] Confirm no NOT VERIFIED figures (~$143M Koch DIP; ~$433M net-of-conversion) are introduced during the finishing pass.
- [ ] Once real artwork exists via `/justpreneur-finish`, re-run full checks 6, 7, 9, 10 (mobile readability, safe margins/cropping risk, no stray tiny text/icons/watermarks/slide numbers, cross-slide visual consistency) against actual pixels — currently only verified against written intent.
- [ ] Reconfirm Slide 6 (shareholder wipeout) renders with zero gold accent and no caveat-style downgrade, per the brief's own stated departure.
- [ ] Reconfirm no real logos, courthouse likeness, or executive likeness appear in rendered art.
- [ ] Reconfirm JustPreneur wordmark/handle spelling and placement in rendered art.
- [ ] Reconfirm no case developments have occurred since this review that would require a copy update.
- [ ] Human publish confirmation obtained before posting (no step in this package authorizes auto-publishing).
