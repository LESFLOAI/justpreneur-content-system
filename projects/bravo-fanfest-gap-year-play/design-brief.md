# JustPreneur Visual Design Brief
**Project slug:** bravo-fanfest-gap-year-play
**Draft cycle:** 2026-10-24
**Format:** Instagram carousel, 8 slides, 1080 x 1350 (portrait, brand default)
**Status:** DRAFT MODE — no image-generation API key available in this environment. Prompts below are written for later real generation via `/justpreneur-finish`. No image files have been produced.

---

## 1. Overall Creative Concept

**"The Gap Playbook."** The carousel reads like a premium business-media timeline explainer (think Axios/Bloomberg data-story energy) wearing just enough pop-culture stage gloss to feel native to an entertainment-business crossover audience — without ever depicting the real franchise, its logos, or its people.

A single visual device carries the whole set: a **horizontal/vertical gold timeline rail** that threads through slides 2–7, marking each beat (2023 → 2025 → the gap → the fix → the proof → the mechanics). Slide 1 (cover) and Slide 8 (takeaway/CTA) break from the rail to bookend the story — cover sets the thesis, close resolves it. The rail itself becomes the recurring motif that visually teaches the "build touchpoints in the gap" lesson: on Slide 4 it goes dotted/broken (the dead zone), and on Slide 8 the dots resolve into solid gold connective segments (the fix, visualized).

All event-specific "characters" are represented abstractly: generic crowd silhouettes shot from behind, empty stage/arena interiors, ticket-stub and stamp iconography, abstract bar-chart stat graphics, and a 7-unit blank badge grid for sponsors. No real person's likeness, no network/show/sponsor logos or wordmarks anywhere — the story is told through typography, numerals, and environment, not depicted celebrities or brand marks.

## 2. Composition and Focal Hierarchy

Every slide uses the same three-zone vertical stack (1080 x 1350):

1. **Top zone (y 0–~420px):** Headline / stat zone. Largest type on the slide. This is the scroll-stopping focal point.
2. **Mid zone (y ~420–~980px):** Supporting visual — environment photography/illustration with generous negative space, carrying the timeline rail motif and any stat-chip callouts.
3. **Bottom zone (y ~980–1350px):** Supporting copy, hedge-language captions (rendered as visible on-slide text, not footnotes), slide-position marker on the rail, and (slide 1 + slide 8 only) the JustPreneur wordmark lockup.

Reading order is always headline → stat/visual → supporting text, left-to-right, top-to-bottom — no diagonal or scattered layouts, to protect mobile legibility.

## 3. Exact Placement — Headline, Supporting Copy, Imagery, Branding

- **JustPreneur wordmark:** small, warm-white, letter-spaced caps lockup, top-center, 56px tall max, on every slide at y≈72–120px (quiet, consistent anchor — not a loud logo treatment). On Slide 1 it doubles as the top anchor above the headline; on Slide 8 it also repeats larger at the bottom as a sign-off above the CTA button-text, 48px tall, centered, y≈1230–1280px.
- **Headline (per slide):** centered or left-aligned (left-aligned from Slide 2 onward to mimic an editorial timeline column; centered only on Slide 1 cover), starting at y≈430–480px on data slides, y≈520px on the cover, max width 900px (90px margin each side), heavy condensed caps.
- **Stat numerals (27,000 / 30,000 / 23-month / $475 / $755 / 40+ / 7 / 4 episodes):** set as oversized tabular-numeral callouts, gold on navy, always paired immediately below/beside with their hedge qualifier in smaller warm-white or steel-gray type at no less than 32px — e.g. "ESTIMATED, ~27,000 ATTENDEES" never shrinks below legible size, and is never pushed into a corner footnote.
- **Supporting body copy:** steel-gray or warm-white sans, 36–44px, max 2–3 lines per slide, bottom third, left-aligned, 90px side margins.
- **Timeline rail + slide marker:** a 6px gold line with a filled dot per slide, running along the left margin (x≈90px) from Slide 2 to Slide 7, with the current slide's dot larger/filled gold and past/future dots smaller/outlined — gives swipe-through continuity without adding a literal "slide 3 of 8" label.
- **Imagery:** fills the mid zone edge-to-edge (full bleed within the 1080 width, inset 60px top/bottom from the mid-zone boundaries) with a dedicated clear band (minimum 280px tall, low-detail/low-contrast area of the image) reserved for whichever stat chip or caption sits on top of it, so text is never laid over busy detail.

## 4. Typography Direction

- **Headline face (style direction, to be matched by designer's closest licensed equivalent):** a heavy geometric/grotesk display face in the family of Archivo Black, Druk, or Neue Machina — all caps, tight tracking (-1 to -2%), used only for headlines and the big stat numerals.
- **Numerals specifically:** tabular/lining figures, slightly extra-bold even relative to the headline face, so "27,000," "$475," "23-MONTH" read like a data report, not a motivational quote card.
- **Body/support face:** a clean humanist sans (style direction: Inter, Söhne, or Graphik), regular/medium weight, sentence case, for all supporting copy and hedge-language lines — this is what keeps hedges ("estimated," "per the Post and Courier," "neither number is an audited count") readable at a normal reading size instead of shrinking them into disclaimers.
- **Caption chips / labels** (e.g., "TEST RUN #1," "SOLD OUT," "RESALE — SEPARATE NUMBER"): small-caps, medium weight, inside a thin gold-outlined rounded rectangle, 28–32px — visible as a design element, not a tiny corner mark.
- No script, no handwriting fonts, no more than two type families total across the whole carousel (one display, one text) to keep the system premium and consistent.

## 5. Color Palette

- **Deep navy** `#0B1420` — primary background, ~70% of each slide.
- **Steel gray** `#4A5566` — secondary text, dividers, muted UI elements (stat chip outlines on image zones).
- **Warm white** `#F6F2E9` — primary text on navy, cover headline, body copy.
- **Energy gold** `#D9A440` — accent only: stat numerals, timeline rail, chip outlines, the CTA line on Slide 8. Never used as a body-text color on light backgrounds (fails contrast); always gold-on-navy or gold-as-outline/graphic element.
- Imagery is treated to sit within this palette (see Section 6) so photography doesn't introduce competing hues (no reds/greens/blues outside the steel-gray/navy range; gold stage lighting is the one permitted warm accent inside photography).

## 6. Image Treatment

- All environment/photographic imagery is desaturated toward navy/steel-gray with a single warm-gold accent light source (practical or implied stage/spot lighting) — consistent "after dark, before the encore" mood across all 8 slides.
- Any human figures are **silhouettes or back-of-head/body crowd shapes only** — anonymous, non-identifiable, generic clothing, no faces in focus, no names, no outfits or styling that evoke a specific real person. This is a hard constraint carried into every prompt below.
- No real venue signage, no show-title treatments, no sponsor marks, no network bugs/logos. Venues are depicted as generic/abstract versions of "a modern performing-arts theater" or "a convention hall," not reproductions of an actual identifiable building facade or interior branding.
- Grain/contrast: slight editorial grain, moderate contrast, no heavy HDR or oversaturation — matches the "serious business-media" register rather than a glossy entertainment-blog look.

## 7. Instagram Safe-Margin Instructions

- Canvas: 1080 x 1350 for all 8 slides (portrait feed/carousel default).
- Keep all text and the JustPreneur wordmark within a **90px margin on left/right** and a **100px margin on top/bottom** (i.e., live text area ≈ 900 x 1150, centered).
- Nothing critical (headline, stat numerals, CTA) should sit within 60px of any edge even inside that margin, to survive thumbnail cropping and the slight corner-crop some feed placements apply.
- Avoid placing essential text in the bottom-right 150x150px corner on every slide (reserved as "dead zone" in case Instagram overlays a "swipe"/pagination affordance in future UI changes).

## 8. Slide-to-Slide Consistency Rules

1. Same navy background tone, same gold/steel-gray/warm-white palette, every slide.
2. Same JustPreneur wordmark size/position on Slide 1 and Slide 8; present but smaller/quieter on Slides 2–7 (top-center anchor only, no repeat sign-off).
3. Same timeline-rail treatment and position (left margin, x≈90px) from Slide 2–7; rail is intentionally broken/dotted only on Slide 4 (the gap) and shown resolving into solid gold on Slide 8.
4. Same three-zone layout grid (headline / visual+stat / supporting copy) on every slide — no slide should suddenly go full-bleed text or full-bleed photo.
5. Stat callouts always use the same chip style (thin gold-outline rounded rectangle, small-caps label) wherever a hedge or sourcing note appears, so "estimated," "per the Post and Courier," "not an audited count," and "resale — separate number" all read as one consistent visual system rather than one-off footnotes.
6. **Date-sensitivity flag:** Slides 5 and 6 currently use present/near-present framing keyed to Oct 24, 2026 ("Oct. 24, 2026: Bravo Fan Fest Charleston," "two nights before," WWHL tapings "Oct. 22–23"). If this carousel publishes on a date materially later than Oct 24, 2026, the Content Copywriter's text needs a tense pass (e.g., "happened on Oct. 24" instead of present/imminent framing) before this visual system is reused — the layout and image prompts themselves don't need to change, only the copy tense.

## 9. Accessibility and Contrast Check

- Primary text pairing (warm white `#F6F2E9` on deep navy `#0B1420`): contrast ratio ≈ 14.8:1 — passes WCAG AAA for all text sizes.
- Gold accent (`#D9A440`) on navy (`#0B1420`): contrast ratio ≈ 7.1:1 — passes AA for normal text and AAA for large text; approved for stat numerals and headlines where used.
- Gold is never set on warm white or on mid-tone photography directly — it is reserved for navy backgrounds or used as an outline/graphic (rail, chip borders) where exact text contrast isn't load-bearing.
- Steel gray (`#4A5566`) on navy is used only for secondary/supporting copy at 36px+ (contrast ≈ 4.6:1, meets AA for large text; not used below 32px).
- Minimum body type size 36px, minimum stat/caption-chip type size 28px, minimum headline size ~72px at this canvas — all comfortably legible on a phone screen without zooming.
- No text is placed over high-detail image areas without a reserved low-contrast band (see Section 3), protecting legibility regardless of the specific photo generated later.

## 10–11. Per-Slide Image-Generation Prompts + Layout/Text Notes

Full structured prompts are written to `projects/bravo-fanfest-gap-year-play/image-jobs.json` (ready for `scripts/generate_images.py` once API keys exist locally). Summary of each slide's imagery intent and the text to be added afterward in a design tool (not generated into the image) is below.

### Slide 1 — Cover
- **Image:** abstract navy stage/arena interior, converging gold spotlight beams, empty of people, large soft negative-space zone center-and-lower for headline+subline.
- **Text to add in layout (not in image):** Headline "BETWEEN THE BIG EVENTS IS WHERE THE REAL BUSINESS GETS BUILT" (warm white, centered, ~y480-680). Sub-line "The Bravo Fan Fest playbook, broken down." (gold small-caps, centered, ~y720). JustPreneur wordmark top-center ~y90.

### Slide 2 — BravoCon 2023
- **Image:** wide abstract convention-hall interior, generic crowd silhouettes from behind/distance (anonymous, backs turned), navy/steel tones, gold rim lighting, clear low-detail band lower-third for stat chip.
- **Text to add:** Headline "BRAVOCON 2023" + "LAS VEGAS." Stat callout "~27,000 ATTENDEES (ESTIMATED)" in gold numerals. Caption chip "TEST RUN #1." Supporting line: "Bravo's flagship mega-convention."

### Slide 3 — BravoCon 2025
- **Image:** parallel composition to Slide 2 (same hall, slightly larger suggested crowd mass via silhouette density, not identifiable individuals), abstract two-bar comparison graphic (steel-gray bar vs taller gold bar) integrated into the clear band.
- **Text to add:** Headline "BRAVOCON 2025" + "LAS VEGAS, NOVEMBER 2025." Stat "~30,000 ATTENDEES (ESTIMATED) — UP FROM ~27,000 IN 2023." Caption chip "NEITHER NUMBER IS AN AUDITED COUNT" (set visibly, same size tier as other chips — not shrunk).

### Slide 4 — The Gap
- **Image:** dark, mostly empty theater/stage interior, single dim worklight, no people, visual emphasis on empty seats/empty stage to convey absence; the gold timeline rail rendered as broken/dotted segments crossing the frame.
- **Text to add:** Headline "23-MONTH GAP." Body: "At NBCUniversal's May 2026 upfront, Andy Cohen announced BravoCon returns in fall 2027 — no dates or venue announced yet." Line: "That's a long stretch for a fanbase to go quiet."

### Slide 5 — The Fix
- **Image:** generic modern performing-arts-center exterior at dusk, marquee-style architecture (no real signage/text on the building), warm gold accent lighting, empty plaza (no crowd needed), clear band for date/headline overlay.
- **Text to add:** Headline "OCT. 24, 2026" + "BRAVO FAN FEST CHARLESTON." Body: "A one-day event at North Charleston Performing Arts Center. One city. One day. More than 40 Bravolebrities." Date-sensitivity note (not on-slide): see Section 8 item 6.

### Slide 6 — Proof It Worked
- **Image:** close/mid shot of an abstract gold "SOLD OUT" stamp-style graphic element and a generic ticket-stub illustration (no real event name, no logo, perforated-edge ticket shape only), navy background, clean negative space around.
- **Text to add:** Headline "PROOF IT WORKED." Body: "Oct. 22–23: Watch What Happens Live taped four episodes at the same venue. Those tapings, plus Fan Fest GA and VIP tickets, are reported sold out — per Bravo's own event coverage and the venue's official listing." Stat chip "4 EPISODES / 2 NIGHTS."

### Slide 7 — The Mechanics
- **Image:** abstract "data dashboard" background — soft navy gradient with a faint grid pattern, and a row of 7 identical blank rounded-square badge placeholders (plain geometric shapes, no logos/text/color branding) to represent sponsor count only.
- **Text to add:** Headline "THE MECHANICS." Stat callouts: "$475 GA / $755 VIP — plus taxes & fees (original on-sale, per the Post and Courier)." Separate smaller chip: "Resale running well above face value — a separate number." Line: "7 sponsors." Line: "Peacock streaming main-stage panels live and on-demand." Line: "No revenue or profit figures disclosed."

### Slide 8 — Takeaway + CTA
- **Image:** the gold timeline rail motif resolving from dotted into a solid unbroken gold line across a clean navy field, abstract and minimal, generous negative space top and bottom for headline/body/CTA.
- **Text to add:** Headline "THIS ISN'T A SCALED-DOWN CONVENTION. IT'S A RETENTION PLAY." Body: "The businesses that win long-term build smaller, consistent touchpoints so the relationship never goes quiet in between." CTA line (gold, button-style outline): "Your move: audit your calendar. Where's the dead zone between your next two big launches?" JustPreneur wordmark repeated at bottom as sign-off.

---

## Guardrail Confirmation

- No prompt below depicts, names, or implies the likeness of any real person (no Andy Cohen, no cast members, no "Bravolebrities" rendered as recognizable individuals) — all human presence is anonymous silhouette/crowd-at-distance only, and Slides 4–8 contain no human figures at all.
- No prompt references or implies Bravo, NBCUniversal, Peacock, BravoCon, Below Deck, Real Housewives, Southern Charm, Southern Hospitality, Summer House, or any sponsor (Ally Bank, Colgate Optic White, Genesis, Planet Fitness, State Farm, Wayfair, Wendy's) by logo, wordmark, or visual trade dress. The 7-sponsor reference on Slide 7 is represented as blank, generic placeholder shapes, with the brand names appearing only as plain layout text (not stylized to mimic any real logo).
- All hedge language specified in the copy ("estimated," "per the Post and Courier," "neither number is an audited count," "resale — a separate number," "no revenue or profit figures disclosed") is placed in the Section 10/11 layout notes as visible on-slide text at normal reading size, not reduced to footnote treatment.
