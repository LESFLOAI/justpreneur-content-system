# QC Report — "Built to Be Bought Twice"

**Reviewer:** Quality Control / Publishing Agent (final independent audit)
**Date checked:** 2026-10-19 (9:00 PM draft cycle)
**Mode:** Draft mode — no image-generation API key available in this environment; no rendered pixels exist. Checks 6 (mobile readability on actual art), 7 (safe margins/cropping on actual art), 9 (tiny text/watermarks on actual art), and 10 (visual consistency across rendered slides) are **pending** and must be re-run in Finish mode once real images exist. All fact, attribution, strategy, caption/hashtag/tag, and legal/reputational checks below were run in full.

**Inputs reviewed:**
- `approved-facts-block.md`
- `strategist-angle-brief.md`
- `content-copy.md`
- `design-brief.md`
- `image-jobs.json`

---

## Verdict: **PASS WITH CORRECTIONS**

The package is factually clean, internally consistent across all five files, and directly addresses the Strategist's flagged risk ("sounds like a quick/easy flip"). No hard-constraint violations found. Corrections below are procedural/pre-publish gating items, not content defects.

---

## 1. Factual accuracy (content-copy.md vs. Approved Facts Block)

- No acquisition price stated anywhere — correctly rendered only as "undisclosed, multimillion-dollar, all-cash deal — with an earnout" (Slide 5, caption). Matches facts verbatim in spirit and register.
- No Creator Authority co-founder named anywhere (not even with a caveat) — correctly omitted entirely, satisfying the hard constraint by omission.
- BDB's revenue/growth claims (24% YoY, >$100M 2027 projection) are **not used at all** in this angle's copy — compliant, since the constraint ("must be attributed, not stated as fact") is trivially satisfied when the figures are simply never invoked.
- Quartermast M&A stat is not used — correct, that stat belongs only to Angle 3 per the Strategist's brief, which was not selected.
- Client list capped to exactly Amazon, Adobe, IBM, HubSpot on Slide 4 and in the caption — no AT&T/Dropbox/Mastercard/Notion anywhere. Compliant.
- Gahan's history (Epic Signal → Mekanism) stated correctly on Slide 2, consistent with the facts block.
- "Gahan becomes SVP of B2B," team growth 15→30-40, and the Ed East/2023 LinkedIn-outreach origin are **not used** in this angle — acceptable, Angle 1 doesn't require every fact, and nothing used is inaccurate.

**Minor observation (not a required correction):** The Approved Facts Block frames the four clients as Creator Authority's "reported clients." The copy states them as flat fact ("Amazon. Adobe. IBM. HubSpot.") without the word "reported." The hard constraint text ("cap to Amazon, Adobe, IBM, HubSpot unless explicitly attributed as 'reported client roster'") most naturally reads as governing use of the *longer* list, not these four — so this is compliant as written. Flagging only as an optional precision improvement, not a failure.

## 2. Design brief / image prompts — no visual overstatement

- `design-brief.md` Section on legal/fact-accuracy guardrails and all seven prompts in `image-jobs.json` explicitly and repeatedly prohibit: real company logos/wordmarks (Epic Signal, Mekanism, Creator Authority, BDB, Amazon, Adobe, IBM, HubSpot, LinkedIn badge), any photoreal human likeness (including Gahan), any second "co-founder" figure, and any legible dollar figure/price tag. Slide 5's prompt specifically calls out "no visible number, price tag, or dollar figure" given the undisclosed price.
- `image-jobs.json` prompts are verbatim matches of the design brief's Section 10 prompts — no drift between the two files.
- Client names (Slide 4) and company names (Slides 2, 5) are explicitly specified as text-layer overlays added in layout, never baked into the generated art or rendered as logos. Correct approach for trademark risk mitigation.
- This is a planning document only (no pixels exist yet); the real test of "no logo drifted through" happens in Finish mode and must be re-verified against actual output.

## 3. Caption, hashtags, tags

- Caption is faithful to approved facts: no price, no co-founder, capped client list, correct company names, explicit "undisclosed" language preserved.
- Hashtags: exactly 5 — #BusinessStrategy #Positioning #CreatorEconomy #FounderStory #Acquisition. All generic/topical, none imply brand partnership or endorsement.
- Tags: Brendan Gahan, Creator Authority, BDB Group, Mekanism — all directly named as subjects of the approved facts, not brands being used for implied endorsement. The copywriter correctly and explicitly **excluded** Amazon/Adobe/IBM/HubSpot from the tag list with a stated rationale (tagging would imply endorsement/partnership beyond "client" status) — this is the right call and should be preserved.
- **Open item:** all four tag handles are marked "exact handle unverified — confirm before publish." This is correctly flagged by the copywriter but is a **required pre-publish action**, not optional — tagging a wrong/lookalike account would be a real impersonation/attribution risk.

## 4. "Quick flip" risk (Strategist's flagged concern)

Directly and explicitly countered:
- Slide 6: "Two exits don't happen by accident. This was years of staying in one lane — until that lane became impossible to ignore."
- Caption: "This isn't a story about a fast flip — it's years of positioning that eventually became impossible to ignore."

This satisfies the Strategist's risk note in `strategist-angle-brief.md` ("must be framed as a disciplined, years-long positioning choice, not a quick flip").

## 5. Cross-file internal consistency

- Headline used (content-copy.md Slide 1 / design-brief.md Slide 1) matches Strategist's Headline Option 1 verbatim: "He Sold His Company Twice. Here's the One Thing He Never Changed."
- Format/slide count consistent everywhere: Carousel, 7 slides (strategist brief → design brief → image-jobs.json, all 7 ids present at 1080x1350).
- Visual concept (two-panel Exit 1 / Exit 2 diptych, no logos) matches the Strategist's stated visual concept for Angle 1 exactly.
- Slide-by-slide text in content-copy.md matches the text the design brief's Section 11 instructs to be overlaid — no drift between what the Copywriter wrote and what the Visual Director briefed to add.
- Palette, typography, and safe-margin rules are stated once and applied uniformly across all 7 slide prompts — no contradictions found.

---

## Required Corrections (ranked by severity)

1. **(Pre-publish gate, high priority)** Verify the real Instagram handles for Brendan Gahan, Creator Authority, BDB Group, and Mekanism before tagging. Do not publish with placeholder/guessed handles — risk of tagging an unrelated or impersonation account.
2. **(Procedural, high priority — carries over from draft-mode limits)** Once real artwork exists (Finish mode), re-run checks 6, 7, 9, and 10 against the actual rendered files: confirm no real/garbled logos appeared, no photoreal face rendered, no legible numbers leaked onto any panel, and that JustPreneur wordmark/margins/consistency hold across all 7 slides as specified. This package cannot be considered publish-ready until that pass is done.

## Optional Improvements (not required)

1. Consider labeling the Slide 4 / caption client list as "reported clients" rather than flat fact, for maximum fidelity to the Approved Facts Block's own phrasing (currently compliant as written, but this would remove any ambiguity).
2. Consider a short note in the caption or a pinned comment plan addressing that BDB's revenue claims are self-reported — not required for Angle 1 since those figures aren't used, but worth having ready if commenters raise it.

---

## Final Publication Package (pending the two required corrections above)

- Headline: "HE SOLD HIS COMPANY TWICE. HERE'S THE ONE THING HE NEVER CHANGED."
- Format: Carousel, 7 slides, 1080x1350
- Slide copy: as finalized in `content-copy.md`
- Caption: as finalized in `content-copy.md`
- Hashtags: #BusinessStrategy #Positioning #CreatorEconomy #FounderStory #Acquisition
- Tags: Brendan Gahan, Creator Authority, BDB Group, Mekanism (handles pending verification)
- Artwork: pending generation via `/justpreneur-finish`; design brief and prompts are approved as planning input

## Recommended Posting Window

Underlying news broke 2026-10-14; this is now day 5. Because Angle 1 is framed as a durable strategic lesson rather than breaking news, some shelf life remains, but relevancy tailwind from the news cycle is fading. Recommend publishing within the next 1–3 days (by 2026-10-22) during JustPreneur's normal weekday high-engagement window (late morning or lunch, audience-local time). Do not hold past roughly one week from the announcement date, or the "here's what just happened" framing in the caption will read as stale.

## Final Pre-Publish Checklist

- [ ] Confirm real Instagram handles for all 4 tagged accounts; drop any that cannot be verified
- [ ] Generate final artwork via `/justpreneur-finish`
- [ ] Re-run QC checks 6, 7, 9, 10 against actual rendered slides (readability, margins/crop risk, no stray marks/logos/numbers, 7-slide visual consistency)
- [ ] Spot-check Slide 4 and Slide 5 renders specifically for any logo-like artifacts or legible numerals (highest-risk prompts)
- [ ] Confirm JustPreneur wordmark present, correctly spelled, consistently placed on all 7 slides
- [ ] Final human sign-off before publish
