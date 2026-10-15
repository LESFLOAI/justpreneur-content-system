# Visual Design Brief — "The Forecast Discount" (Bogotá/BTS Carousel)

**Working title:** bogota-forecast-discount
**Target posting slot:** 2026-10-15, 9:00 PM
**Format:** Instagram carousel, 8 slides, 1080 x 1350 px (portrait) each
**Source copy:** projects/bogota-forecast-discount/content-copy.md
**Source strategy:** projects/bogota-forecast-discount/strategist-angle-brief.md

**STATUS: DRAFT MODE — NO IMAGES GENERATED.** No image-generation API key is available in this environment. This document and the accompanying `image-jobs.json` are the complete design brief and prompt set for a human (or the `/justpreneur-finish` flow) to execute locally once an image-generation key is configured.

---

## 1. Overall creative concept

"The Forecast Discount" visualizes the gap between a hyped pre-event number and a sober post-event estimate using a financial/data-journalism visual language rather than concert-poster energy. Think Bloomberg/Economist-style data storytelling crossed with premium startup-media polish: deep navy backgrounds, gold data accents, clean sans-serif numerals, abstract skyline/crowd/flight-path motifs standing in for the concert and the city — never the artists themselves. The carousel should feel like reading a sharp, quotable analyst note, not a fan-page recap. Each numeric slide functions like a slide from an investor deck: one dominant data point, clearly dated and labeled, with no ambiguity about what it measures.

## 2. Composition and focal hierarchy

Every slide follows the same hierarchy, top to bottom:
1. **Eyebrow/label** (small, uppercase, steel gray or gold — e.g., "PRE-EVENT PROJECTION — FEB 2026") where a slide carries a data point. Cover and closing slides omit this.
2. **Headline/number** — the single largest, boldest element, always warm white or energy gold, always within the safe zone.
3. **Supporting copy** — 1-3 short lines, warm white at reduced weight, directly beneath the headline.
4. **Visual/data motif** — abstract chart, skyline, or flight-path graphic occupying the lower-middle third or used as a full-bleed textured background behind the text (never competing with it — apply a navy gradient/scrim behind all text zones).
5. **JustPreneur wordmark** — small, consistent, bottom-center, on every slide.

No slide should ever have two competing focal points. Numbers get their own visual air; supporting data visuals stay subordinate and are pushed toward the bottom third or used as a low-contrast background texture.

## 3. Exact placement — headline, supporting copy, imagery, branding (per slide)

**Global safe-margin frame for all 8 slides:** keep all text and the wordmark inside a 72px margin from every edge (1080x1350 canvas → safe text zone roughly x:72–1008, y:72–1278). Nothing but full-bleed background art may touch the outer edge.

- **Slide 1 — Cover**
  - Headline (centered, upper-middle, y ≈ 420–760): "Before you build for the big projection, look at what actually happened in Bogotá."
  - Supporting line (below headline, y ≈ 800–880, smaller weight): "A builder's lesson from BTS's two sold-out nights at El Campín."
  - Visual: full-bleed abstract night skyline of Bogotá with a glowing stadium bowl of light and a faint diffuse crowd-silhouette glow at the base, navy-to-charcoal gradient, gold light spill upward behind the headline zone (kept low-contrast so text stays legible).
  - JustPreneur wordmark: bottom-center, y ≈ 1270, warm white, small (~28-32px cap height).

- **Slide 2 — The Pre-Event Number**
  - Eyebrow (top, y ≈ 150): "PRE-EVENT PROJECTION — FEBRUARY 2026"
  - Headline number (center, y ≈ 420–620, largest type on the whole carousel): "$126,054M COP"
  - Supporting copy (below, y ≈ 680–820): "A projection of the economic impact of BTS's two sold-out Bogotá shows — published before a single flight landed."
  - Visual: a single tall abstract upward-sloping bar/line-graph silhouette rising from the bottom edge, gold-lit, set against a dark navy background with a faint grid texture (data-report feel). Positioned lower third so it never crosses the number.
  - Wordmark: bottom-center, same position as Slide 1.

- **Slide 3 — The Post-Event Number**
  - Eyebrow (top): "POST-EVENT ESTIMATE — ~OCT 6–8, 2026 (modeled, not audited)"
  - Headline number (center, same type size/position as Slide 2 for direct visual comparison): "~$99,000M COP"
  - Supporting copy: "Built from Ticketmaster Colombia and Mabrian data. A modeled estimate of city-wide economic activity — not a confirmed actual."
  - Visual: two abstract bars side by side at the bottom — a taller gold bar labeled implicitly by position as "Feb 2026" echo from Slide 2, and a visibly shorter steel-gray bar for this slide's figure — both bars kept as plain geometric shapes with no numbers baked into the image (exact numerals are added as text layer, not image text). Do NOT render the two bars as touching/merged or imply averaging; keep a clear gap between them.
  - Wordmark: same position.

- **Slide 4 — Where the Estimate Came From**
  - Eyebrow: "INSIDE THE ~$99,000M COP ESTIMATE"
  - Body list (left-aligned, y ≈ 380–760, generous line spacing): four lines, each category name left, figure right —
    - Food & beverage — ~$39,108M COP
    - Lodging — ~$29,384M COP
    - Internal transport — ~$17,557M COP
    - Shopping & souvenirs — ~$12,976M COP
  - Visual: a simple four-segment horizontal stacked bar beneath the list (proportional to the real figures above), gold/steel-gray/warm-white/charcoal segments, no icons, no extra decoration.
  - Wordmark: same position.

- **Slide 5 — The Gap, Framed Correctly**
  - Headline (upper-middle): "Two numbers. Two moments in time. Two different methodologies."
  - Supporting copy (middle): "The post-event estimate landed about 21% below the pre-event projection — and both concerts sold out."
  - Closing line (lower, slightly emphasized in gold): "This isn't a story about underperformance. It's a story about what a projection is actually for."
  - Visual: the same two-bar motif from Slide 3, now with a dashed bracket between them and a "-21%" callout badge positioned in the gap (callout rendered as a text layer, not baked into the image). Bars stay clearly separated and unlabeled with raw numerals in the image itself.
  - Wordmark: same position.

- **Slide 6 — A Real Demand Signal**
  - Eyebrow: "FLIGHT BOOKINGS — SEPT 30–OCT 4, 2026"
  - Headline number (large, center): "+46.6% YoY"
  - Supporting copy: "Mabrian data cited in the city's balance — a flight-booking signal, not a hotel number, and not the whole demand picture."
  - Visual: an abstract ascending flight-path arc/trajectory line over a minimal city-skyline silhouette, gold trail, navy sky, suggestion of motion rather than a literal airplane icon.
  - Wordmark: same position.

- **Slide 7 — The Figure to Hold Loosely**
  - Eyebrow: "VIAJES FALABELLA — OCTOBER 2026 CONCERT CALENDAR (single-sourced)"
  - Headline numbers (two stacked, slightly smaller than Slide 6 to signal lower certainty): "Hotel bookings ~110% ↑" / "Tour packages ~90% ↑"
  - Supporting copy: "Single-sourced to one travel agency. Reported, not confirmed as a citywide statistic."
  - Visual: the same abstract bar/skyline language as prior slides but rendered with a visibly looser, dashed/hatched outline treatment (vs. the solid fills used in Slides 2–4) to visually signal "less certain, attribute carefully." No literal hotel logos or building-brand signage.
  - Wordmark: same position.

- **Slide 8 — Final Takeaway**
  - Eyebrow (small, gold, centered): "THE BUILDER LESSON"
  - Headline (large, centered, upper-middle): "Build the capacity that flexes to the real outcome —"
  - Second line (same weight, directly below): "not the capacity sized to the biggest number circulating before the event."
  - Visual: calm, minimal — a single abstract adjustable/accordion-bracket or flexible-scaffold motif in gold line-art on a deep navy field, symbolizing flexible capacity (no literal construction equipment, no people). Generous negative space; this is the "quote card" slide most likely to be screenshotted on its own.
  - Wordmark: same position, slightly larger here (this is the save/share slide) — still under 40px cap height.

## 4. Typography direction

- **Headline/number typeface:** a bold, geometric-grotesque sans (e.g., a Neue Haas Grotesk / Söhne / General Sans-style face) — tight letter-spacing, high legibility at small phone sizes. Numerals should use tabular/lining figures so columns of digits align cleanly (critical for Slides 2, 3, 4).
- **Eyebrow/label typeface:** same family, all-caps, letter-spaced +6–8%, smaller size (~28–32px), used only for labels/dates/sources — never for primary claims.
- **Body/supporting copy:** a clean, slightly warmer sans at regular weight for contrast against the bold headline weight — keeps the hierarchy unambiguous.
- **Minimum sizes for mobile legibility:** headline numerals/claims no smaller than ~64px effective cap height at 1080px width; body copy no smaller than ~36px; eyebrow/labels no smaller than ~28px.
- **Line length:** wrap headline copy to 2–3 lines max per slide; avoid single unbroken long lines that shrink type to fit.

## 5. Color palette

- **Deep navy** (#0B1726 approx.) — primary background.
- **Steel gray** (#5B6B7A approx.) — secondary bars, de-emphasized data, Slide 7's "looser" visual elements.
- **Warm white** (#F5F1E8 approx.) — primary body text, wordmark.
- **Energy gold** (#D4A13D approx.) — headline numerals, key callouts, primary data bars, eyebrow accents.
- Charcoal (#1C2630 approx.) used as a tertiary tone for scrims/gradients behind text to guarantee contrast over background art.
- Reserve gold strictly for the *most* important number or claim per slide so it keeps its "this is the headline" signal value — don't let it bleed into decorative use.

## 6. Image treatment

- All background art is abstract/atmospheric: skyline silhouettes, light trails, data-chart geometry, crowd-glow bokeh. No photographic or illustrated likenesses of BTS members or any identifiable real person.
- No logos, wordmarks, or trademarks of any kind rendered inside the generated art (no Ticketmaster, HYBE, Falabella, Bogotá city seal, stadium signage, team crests, etc.) — describe generic/unbranded equivalents only.
- Treat every background image with a navy gradient/scrim (roughly 40–60% opacity at the top and bottom thirds) wherever text sits, to guarantee contrast regardless of the generated art's exact tonal values.
- Keep generated art slightly desaturated/moody (film-like grain is fine) so gold and warm-white text pop without additional glow/drop-shadow effects doing the contrast work.
- Data-visual elements (bars, graphs, flight paths) should be generated as clean, smooth geometric shapes — no attempt to render exact numerals or labels inside the generated image; all numerals and words are added afterward as a text layer per Section 10.

## 7. Instagram safe-margin instructions

- Canvas: 1080 x 1350 px for all 8 slides (standard portrait carousel ratio, consistent across the set).
- Keep all text, numerals, and the JustPreneur wordmark within a 72px margin on every edge (safe zone: x 72–1008, y 72–1278).
- Avoid placing any critical content within the top ~150px or bottom ~150px beyond the margin where Instagram's UI (profile header, caption/like bar) can crop or obscure content on some devices/feeds — the wordmark at y≈1270 is close to this limit; if feed-preview testing shows clipping, nudge it up to y≈1230.
- Center-align all headline/number text horizontally for consistent optical balance slide to slide.

## 8. Slide-to-slide consistency rules

- Same canvas size (1080x1350), same safe margins, same wordmark position/size (with the Slide 8 size bump noted above) across all 8 slides.
- Same navy/charcoal base background and same gold/steel-gray accent logic on every slide — no slide should introduce a new color.
- Same eyebrow-label placement and styling on every slide that uses one (Slides 2, 3, 4, 6, 7) so the "data slide" slides visually read as a matched set distinct from the cover (1), transition (5), and closing-quote (8) slides.
- The two-bar comparison motif introduced in Slide 3 must stay visually consistent (same bar width, same gold-vs-steel-gray color coding, same baseline) through Slides 4, 5, and 7 so the eye reads it as one continuing data story, not four unrelated charts.
- Numerals must never be baked into the generated background art — all exact figures, dates, and labels are added as a precise text layer in a design tool after image generation, per the layout prompt in Section 10. This avoids AI-generated text artifacts corrupting sensitive, fact-checked figures.

## 9. Accessibility and contrast check

- Warm white (#F5F1E8) text on deep navy (#0B1726) background yields a contrast ratio well above WCAG AA (>12:1) — safe for body text at all approved sizes.
- Energy gold (#D4A13D) on deep navy yields roughly 7–8:1 — safe for headline-size text; avoid using gold for small body-copy sizes where contrast margin matters more.
- Never place body or headline text directly over an ungraded photographic/art area — always apply the navy scrim described in Section 6 first, then verify contrast visually before export.
- Avoid steel-gray text on navy for anything except large decorative numerals (Slide 7's secondary stat) — steel-gray-on-navy contrast is borderline and unsuitable for primary reading text.
- Keep a minimum 1.4x line-height on all multi-line text blocks for readability at arm's-length mobile viewing.

## 10. Image-generation prompts

See `projects/bogota-forecast-discount/image-jobs.json` for the full structured prompt set (one job per slide, labeled **"images not yet generated — draft mode"**). Each prompt specifies dimensions, subject/environment, composition, lighting/mood, brand palette, required negative space for text, and explicit negative constraints (no BTS likenesses, no logos/trademarks, no illegible/fake text, no duplicated people, no malformed hands, no clutter).

## 11. Layout prompt — adding exact text after image generation

Once the 8 background images are generated locally (via `/justpreneur-finish` running `scripts/generate_images.py`), apply this layout pass in a design tool (Figma/Canva/Photoshop) to every image before export:

1. Import each generated PNG at 1080x1350 (or 1080x1080 if the format is later changed to a square grid post) as the base layer.
2. Add a navy/charcoal gradient scrim layer (per Section 6) wherever text will sit — typically top third and/or bottom two-thirds depending on the slide's text zone described in Section 3.
3. Place text in this exact order and content, using the typography/color specs from Sections 4–5, positioned per the per-slide placement in Section 3:
   - **Slide 1:** Headline — "Before you build for the big projection, look at what actually happened in Bogotá." / Supporting line — "A builder's lesson from BTS's two sold-out nights at El Campín."
   - **Slide 2:** Eyebrow — "PRE-EVENT PROJECTION — FEBRUARY 2026" / Number — "$126,054M COP" / Body — "A projection of the economic impact of BTS's two sold-out Bogotá shows — published before a single flight landed."
   - **Slide 3:** Eyebrow — "POST-EVENT ESTIMATE — ~OCT 6–8, 2026 (modeled, not audited)" / Number — "~$99,000M COP" / Body — "Built from Ticketmaster Colombia and Mabrian data. A modeled estimate of city-wide economic activity — not a confirmed actual."
   - **Slide 4:** Eyebrow — "INSIDE THE ~$99,000M COP ESTIMATE" / Four-line list — "Food & beverage — ~$39,108M COP"; "Lodging — ~$29,384M COP"; "Internal transport — ~$17,557M COP"; "Shopping & souvenirs — ~$12,976M COP" / proportional stacked-bar graphic drawn in the design tool (not AI-generated) using these exact figures.
   - **Slide 5:** Headline — "Two numbers. Two moments in time. Two different methodologies." / Body — "The post-event estimate landed about 21% below the pre-event projection — and both concerts sold out." / Closing line (gold) — "This isn't a story about underperformance. It's a story about what a projection is actually for." / "-21%" callout badge drawn in the gap between the two bars.
   - **Slide 6:** Eyebrow — "FLIGHT BOOKINGS — SEPT 30–OCT 4, 2026" / Number — "+46.6% YoY" / Body — "Mabrian data cited in the city's balance — a flight-booking signal, not a hotel number, and not the whole demand picture."
   - **Slide 7:** Eyebrow — "VIAJES FALABELLA — OCTOBER 2026 CONCERT CALENDAR (single-sourced)" / Numbers — "Hotel bookings ~110% ↑" and "Tour packages ~90% ↑" / Body — "Single-sourced to one travel agency. Reported, not confirmed as a citywide statistic."
   - **Slide 8:** Eyebrow (gold) — "THE BUILDER LESSON" / Headline — "Build the capacity that flexes to the real outcome — not the capacity sized to the biggest number circulating before the event."
4. Add the JustPreneur wordmark (exact brand wordmark asset, correctly spelled "JustPreneur") at bottom-center of every slide, per Section 3/8 placement.
5. Export each slide as a flattened PNG at 1080x1350, verify every numeral/date/label against `content-copy.md` character-for-character before finalizing, and confirm no two dollar figures are ever rendered touching/merged/averaged on the same bar or chart element.
6. Run a final mobile-preview check (view each slide at actual Instagram feed thumbnail size) to confirm headline legibility before scheduling.

---

**Draft-mode note:** No images have been generated for this project. All content above is a complete, ready-to-execute brief. When image-generation credentials are available, run `/justpreneur-finish` to execute `scripts/generate_images.py` against `image-jobs.json` and then perform the Section 11 text-layout pass.

---

## QC Amendment Log (applied by Quality Control, 2026-10-15)

- Slide 3 eyebrow (Section 3 and Section 11): "OCT 6–8, 2026" → "~OCT 6–8, 2026" to preserve the Approved Facts Block's "around October 6–8, 2026" hedge, matching the same correction made in content-copy.md.
