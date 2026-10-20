# Design Brief — "The Referee Who Started Charging Admission" (Arena / LMArena)

**Status: IMAGES NOT YET GENERATED** — no image-generation API key is available in this environment (draft mode). Prompts saved to `image-jobs.json` in this folder for `/justpreneur-finish` to execute later.

## Overall creative concept
"The Referee" visual system: a recurring whistle/scoreboard motif that evolves slide to slide — from an open padlock (free, public) into a closed gold padlock + price tag (paid), and from a flat leaderboard bar chart into a rising valuation line chart. Flat, minimal, line-art/icon-based infographic style throughout (no photoreal/stock people) — this is a B2B data story with no strong celebrity/visual hook, read as business/data journalism (The Information / Axios / Bloomberg graphics), not a generic quote-card template.

Slide 8 ("Our Read") is deliberately a visual rupture in the system — different field color (gold instead of navy/warm-white), hazard-stripe border, "EDITORIAL ANALYSIS" badge — so it reads as opinion, not as another fact-slide in the timeline.

## Canvas & safe margins
1080x1350 (4:5) for all 9 slides. 96px margin on all sides kept clear of critical text/wordmark; top/bottom 120px kept free of critical content (feed UI chrome).

## Typography
- Headlines: bold condensed grotesque sans, all caps (Archivo Black / Area Extended Black / Druk Wide equivalent).
- Body: humanist sans, sentence case, ~130% line-height (Inter / Söhne / Graphik).
- Stat numerals & caption tags: monospace/tabular-numeral grotesque (Space Grotesk / IBM Plex Mono) to visually distinguish self-reported/unaudited tags from narrative copy.
- Slide 8 headline: distinct italic/alternate-weight treatment to signal editorial voice at a glance.
- Minimum sizes at 1080px width: body 42px effective, headline 64px.

## Color palette
- Deep navy #0E1F33, steel gray #8A94A6, warm white #FAF8F4, energy gold #E8B74B — shared across slides 1–7, 9.
- Slide 8 intentional exception: dominant field #D9A441 (amber/gold) with navy ink, to flag "editorial, not fact."
- All contrast ratios checked and pass WCAG for intended text sizes (see QC note).

## Layout rules
- Slides 2–7, 9: left-aligned "timeline/reporting" template — navy header band with era/date tag, central icon zone, left-aligned headline + body, JustPreneur wordmark footer.
- Slides 1 and 9: centered-composition bookends.
- Slide 5 & 7: self-reported/unaudited caption-tag pills placed directly adjacent to the dollar figure they qualify — never a standalone footnote.
- Slide 6: institution list + "peer-review status: unconfirmed" caption directly beneath body copy, steel gray, smaller weight.
- Slide 8: "EDITORIAL ANALYSIS" badge renders first in visual hierarchy, before headline/body.
- No investor-list graphic beyond the two named co-leads (Lightspeed Venture Partners, Khosla Ventures) — full list varies by outlet and is unconfirmed against a primary source.
- No fabricated Instagram handles or logos anywhere.
- No slide-count indicator, date stamp, citation mark, or watermark.

## Image treatment / icon language
Open padlock = free/public. Closed gold padlock + price tag = paid. Bar-chart scoreboard = leaderboard. Rising gold line chart = valuation/funding. Magnifying glass (restrained, not alarmist) = scrutiny/allegation. Overlapping circles = dual role (judge + vendor). No real logos, no fabricated likenesses, no gavel/courtroom clichés, no scoreboard with legible real model names.

## Image-generation prompts
Full prompt text for all 9 slides (dimensions, subject, composition, lighting/mood, palette, reserved text zones, negative constraints) is saved in `image-jobs.json` in this folder — 9 entries, 1080x1350 each, matching the shape `scripts/generate_images.py` expects. Not yet run; no PNGs exist.

## Open items for finish stage
- No verified official Arena/LMArena Instagram handle was confirmed — recheck before publish in case a confirmed handle becomes taggable.
- Font licensing/exact typeface substitution left to whoever builds the final Canva/Figma file; suggested fonts above are accessible equivalents.
