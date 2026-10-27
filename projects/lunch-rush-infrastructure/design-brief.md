# JustPreneur Visual Design Brief — "The Infrastructure Hiding in the Lunch Rush"

**STATUS: DRAFT MODE — IMAGES NOT YET GENERATED.** No image-generation API key is available in this cloud environment. This document contains the full creative direction and every image-generation prompt needed, ready for local execution via `/justpreneur-finish` or a manual run of `scripts/generate_images.py`. Do not treat any visual described here as an existing asset.

**Primary format:** Instagram Reel, ~45–60 sec, 1080 x 1920 (9:16)
**Secondary/optional format:** Instagram Carousel repurpose, 6 slides, 1080 x 1350 (portrait)
**Working title:** lunch-rush-infrastructure
**Source story:** Rappi-reported corrientazo/executive-lunch order surge in Colombia (data as reported Oct 20, 2026)

---

## 0. Mandatory design constraints (carried from Fact Verifier / Strategist / Copywriter — non-negotiable)

These override general brand defaults wherever they would conflict. Flag them clearly to whoever runs generation locally; every prompt below is already written to comply.

1. **Never show "$5" anywhere.** If a price appears on screen at all, it must read exactly "COP $19,900 (~US$6, per Rappi, Oct. 2026)." No generated image bakes in ANY price text — all numerals are added afterward as a JustPreneur type layer (see §10). No price tag, menu, or receipt prop in any generated image may contain legible numerals of any kind.
2. **No naive city bar/height chart.** Any visual referencing Villavicencio, Ibagué, Santa Marta, or Bogotá must avoid comparative bar-height graphics that could imply absolute order-volume comparison between cities. Use an abstract map with directional growth arrows and/or percentage callouts only — never bars, columns, or stacked blocks sized by city. Where a map/chart appears, an explicit "growth rate, not volume" visual cue (e.g., an arrow-based legend, not a bar) must be part of the design, and the exact disclaimer text is added as a type layer.
3. **No clean "3:00 PM" clock numeral.** Any clock-face or time-sweep graphic referencing the lunch window must visibly stop just short of 3 (e.g., the sweep hand/arc ends at the "2:59" mark, or the clock face's "3" numeral is never highlighted/landed-on as the resting point). This applies to both Reel beat 1 (clock ticking toward noon) and Reel beat 5 / Carousel slide 5 (clock sweep 11:00–2:59).
4. **No Rappi logo or branding implying partnership.** No generated image or overlay reproduces Rappi's actual logo, brand colors-as-identity, app UI, or wordmark. This is third-party commentary on publicly reported data, not a Rappi-sponsored post. Delivery bikes/bags in generated images must be generic and unbranded — no readable or invented delivery-app logos of any kind.
5. **No profitability messaging about Rappi, implied or explicit.** No cash stacks, rising profit-line graphs, dollar-sign iconography, or "cha-ching" visual cues tied to Rappi. All financial-adjacent imagery stays strictly on the *operational* side (order volume, time windows, kitchen logistics) — never frames Rappi's business performance or margins.
6. **No text baked into any generated image.** All headlines, stat callouts, prices, percentages, city names, clock labels, and the JustPreneur wordmark are added after generation as type layers (see §10). This also avoids AI text-rendering artifacts, which are a known failure mode for numeral-heavy data content like this story.
7. **Approved facts stay attributed.** Every data point used in copy overlays keeps its "per Rappi" / "Rappi-reported" sourcing exactly as written in the approved copy — no visual should let a stat read as a JustPreneur-verified or independently-audited number.

---

## 1. Overall creative concept

This is a **data-journalism explainer**, not a food-delivery ad and not a generic hustle-culture motivational Reel. The visual world is "operations and systems," matching the headline's real subject: a narrow, predictable 4-hour demand window is infrastructure, not a coupon story. Think Bloomberg Businessweek's or The Information's data-desk motion graphics — clean kinetic typography over restrained abstract/photographic backgrounds, not stock photos of someone biting a sandwich.

Visual thesis carried through every beat: a recurring **blueprint/time-block motif** — thin gold grid lines, a subtle clock-arc device, and simple directional arrows — that visually says "this is a system being mapped," echoing JustPreneur's established "infrastructure thinking" visual language (the same family used on prior carousels like the Corner Store brief). Food/lunch imagery is used sparingly and only as texture (plates, a counter, a delivery bag silhouette) — it never becomes the hero subject, because the story's point is the *pattern*, not the meal.

Because several beats carry sensitive constraints (no city bar chart, no "$5", no clean 3pm, no Rappi logo, no profitability framing), every background image is deliberately abstract or generic-environmental rather than literal/documentary — this also sidesteps any implied Rappi endorsement.

---

## 2. Composition and focal hierarchy

**Reel (every beat unless noted):**
1. **Kinetic on-screen text** — centered or lower-third, largest/highest-contrast element, always the first thing the eye hits; exact wording per the approved beat-by-beat script, never paraphrased.
2. **JustPreneur wordmark** — small, fixed bottom-safe-zone position on beats 2–7 (steady signature, not a stop on the reading path); scales up and becomes the hero element only on beat 8 (closing sting).
3. **Background visual/motif** — generic, abstract-leaning supporting texture (clock arcs, map-and-arrow graphics, kitchen-ops line diagrams, blurred delivery-bike silhouettes) that never competes with or undercuts the text above it.
4. **Attribution micro-text ("per Rappi," "Rappi-reported")** — set small, directly adjacent to the stat it supports, same weight/position logic every time it appears — part of the type layer, never baked into the image.

**Carousel (if produced):**
Same hierarchy as the Reel, adapted to the 1080x1350 static frame: headline/stat top, supporting line middle, background visual lower 45–55% or restrained full-bleed with a dark gradient text-safe zone, JustPreneur wordmark bottom-left, consistent across all 6 slides.

---

## 3. Exact placement — beat by beat (Reel) and slide by slide (Carousel)

### REEL (8 beats, ~60 sec total, 1080x1920)

| Beat | Time | On-screen text (verbatim) | Background job | Text position |
|---|---|---|---|---|
| 1 | 0:00–0:02 | "Rappi just reported something bigger than cheap lunch." | bg-reel-1-clock-and-bikes | Centered, mid-frame |
| 2 | 0:02–0:08 | "+160% YTD (Rappi-reported) · 250K → 660K+ orders" | bg-reel-2-growth-counter | Lower third, counter-style numerals animate in |
| 3 | 0:08–0:16 | "Growth RATE, not order volume — Rappi didn't disclose city totals" | bg-reel-3-colombia-map-arrows | Lower third; city labels + arrows added as type/vector layer, not baked into image |
| 4 | 0:16–0:26 | "800+ restaurants: full lunch under COP $19,900 (~US$6, per Rappi, Oct. 2026)" | bg-reel-4-restaurant-counter | Lower third; price text added as type layer only, exact string as written |
| 5 | 0:26–0:36 | "84% of orders: 11:00 a.m.–2:59 p.m. · peak ~noon — Rappi" | bg-reel-5-clock-sweep-spike | Lower third; clock-arc graphic stops visibly short of "3" |
| 6 | 0:36–0:48 | "Predictability is the asset. Not the price." | bg-reel-6-kitchen-ops-blueprint | Vertically centered (thesis/punch beat) |
| 7 | 0:48–0:56 | "Find your window. Build around it." | bg-reel-7-minimal-frame | Centered, text-forward, minimal background |
| 8 | 0:56–1:00 | "JustPreneur — Infrastructure thinking for entrepreneurs." | bg-reel-8-wordmark-sting | Centered, wordmark large, clean background |

### CAROUSEL (6 slides, 1080x1350) — optional secondary repurpose

| Slide | Text (verbatim) | Background job |
|---|---|---|
| 1 — Cover | "Rappi reported 84% of Colombia's lunch orders hit the same 4-hour window. That's the real story." | slide-1-cover-clock-skyline |
| 2 | "+160% YTD in corrientazo/executive-lunch orders on Rappi, 2026 vs. 2025 — from roughly 250,000 to over 660,000 orders, per Rappi." | slide-2-growth-counter |
| 3 | "Growth was strongest in mid-sized cities — Villavicencio, Ibagué, Santa Marta — compared with Bogotá, per Rappi. These are growth-RATE percentages off undisclosed bases, not order-volume comparisons." | slide-3-colombia-map-arrows |
| 4 | "2,000+ restaurants offer corrientazo on Rappi. 800+ price a full lunch under COP $19,900 — about US$6, per Rappi, October 2026." | slide-4-restaurant-counter |
| 5 | "84% of these orders land between 11:00 a.m. and 2:59 p.m., peaking around noon, per Rappi. A recurring, narrow demand window isn't a quirk — it's infrastructure waiting to be designed around. Predictability is the asset, not the price." | slide-5-clock-sweep-spike |
| 6 — CTA | "Map your business's own 4-hour window. Is anything actually built around it yet?" | slide-6-minimal-frame-cta |

Note: the Carousel reuses the same visual concepts as the Reel (same background job *content*, re-rendered at 1080x1350) so the two assets feel like one coherent system if both are published, not two unrelated campaigns.

---

## 4. Typography direction

- **Kinetic/headline typeface:** bold, modern geometric or grotesque sans serif (same family used across prior JustPreneur Reels/carousels — e.g., Neue Haas Grotesk Bold / Inter Black family) — confident, business-editorial, never a script or decorative display font.
- **Stat/counter numerals (beat 2, beat 4, beat 5):** tabular/monospaced-leaning numeral style within the same type family, so counters feel like a data readout, not a casual label — set noticeably large since numerals carry most of the information density in those beats.
- **Attribution micro-text ("per Rappi," "Rappi-reported," "Oct. 2026"):** smallest text size used anywhere in the piece, steel gray, always directly adjacent to its stat — never isolated as a tiny corner credit, and never omitted when a stat is on screen.
- **Body/kicker lines (beats 6, 7; carousel body copy):** lighter-weight humanist sans serif companion to the headline face, generous line-height, left-aligned or centered per beat as specified in §3.
- Minimum kinetic-text size for Reel beats renders no smaller than ~64px cap-height equivalent at 1080px width — legible at arm's length mid-scroll. Minimum carousel headline size stays above ~60–70pt equivalent at 1080px width.
- No more than two typefaces total across the entire Reel + Carousel system (one for headline/stat/kinetic text, one for body/attribution).

---

## 5. Color palette

- **Primary:** deep navy (#0E1A2B approx.) — dominant background across every beat/slide.
- **Accent/energy:** energy gold (#C9A24A approx.) — stat numerals, clock-arc highlight, arrow/map accents, JustPreneur wordmark.
- **Neutral text:** warm white (#F5F1E8 approx.) — primary on-screen text and most headline/body copy.
- **Secondary neutral:** steel gray (#8A93A1 approx.) — attribution micro-text, de-emphasized supporting lines, dimmed/not-yet-highlighted map regions.
- No red, green, or "cha-ching" cash-green introduced anywhere — keeps the piece in JustPreneur's own editorial register rather than Rappi's brand colors or a generic "growth chart" cliché palette, and avoids any accidental profitability-coded color cues (see §0.5).

---

## 6. Image treatment

- All backgrounds are **abstract or generic-environmental motion-graphic textures** — blueprint-style thin gold line work, soft-focus generic city/street atmosphere, clock-arc and map-and-arrow vector-style graphics, restrained kitchen-operations diagram lines — not literal food photography, not documentary photos of real Bogotá streets or real restaurants, and not stock images of someone eating.
- Desaturate/grade every generated image toward the navy/gold/steel palette in post so returned images sit naturally inside the fixed system regardless of generator output.
- Every background reserves an explicit dark, low-detail zone sized to the text block that will sit on top of it (see each prompt in §10) — never a busy image directly behind kinetic text.
- Delivery bikes/bags, where used (beat 1 only), are generic, unbranded silhouettes — no readable or invented delivery-app logos, no Rappi orange, no Rappi wordmark shape.
- No price numerals, city names, percentages, or clock numerals are ever baked into a generated image — all of that is exact type/vector layer work added afterward (§10), both for brand-system consistency and because image models render precise numerals/text unreliably.
- No human faces as hero subjects anywhere in this piece — if any human presence appears (e.g., a hand placing a plate, a silhouette at a counter), it is anonymous, out-of-focus, or silhouetted only, avoiding malformed-hands/duplicate-face risk entirely.

---

## 7. Instagram safe-margin instructions

**Reel (1080x1920):** Keep all kinetic text within x: 80px–1000px and y: 250px–1550px. The top ~230px is covered by the account name/follow button/audio bar in the Instagram Reels UI; the bottom ~370px is covered by caption text, like/comment/share/save icons, and the audio disc. Centered/punch beats (1, 6, 8) should sit roughly at y: 850–1100 (true vertical center of the safe zone) so they read clearly regardless of UI chrome state.

**Carousel (1080x1350):** Minimum 80px margin on all sides for any text or wordmark; keep essential text additionally clear of the top 120px and bottom 150px where Instagram's UI chrome is most likely to overlap. No essential word within 60px of the left/right edges.

---

## 8. Slide-to-slide / beat-to-beat consistency rules

1. Same canvas size and palette (navy/gold/warm-white/steel) across all 8 Reel beats and, separately, across all 6 Carousel slides — no exceptions.
2. Same JustPreneur wordmark size/color/position on beats 2–7 and carousel slides 1–6; it only scales up intentionally on Reel beat 8 (the sting).
3. Same kinetic/headline typeface and weight throughout; only emphasis (gold vs. warm white) shifts intentionally for stat numerals and the thesis beat (6).
4. The blueprint/gold-line-grid motif established in beat/slide 1 recurs at consistent weight/style across subsequent beats/slides tying the city-map (3), kitchen-ops (6), and minimal-frame (7) visuals into one visible system.
5. The clock-arc device (beats 1 and 5; slides 1 and 5) must always visibly stop short of "3" per §0.3 — this is checked on every occurrence, not just the primary one.
6. No beat/slide introduces a new accent color, a new font, or a new Rappi-adjacent brand color — the only intentional "surprise" from beat to beat is content, never system.

---

## 9. Accessibility and contrast check

- Warm white (#F5F1E8) text on deep navy (#0E1A2B) background clears WCAG AA comfortably for large kinetic/headline text.
- Energy gold (#C9A24A) reads with strong contrast on navy for headline/stat-numeral-size text; gold is never used for the small attribution micro-text, where contrast at small size would drop.
- Steel gray attribution text is reserved for short, secondary lines only, always paired with (never replacing) the warm-white or gold primary stat it supports.
- Every beat/slide passes a "squint test" — the primary text reads as a legible shape/contrast block even blurred, before fine background detail resolves, because text always sits on a flat navy field or a dedicated dark gradient scrim, never directly on high-detail imagery.
- No information is conveyed by color alone: the "growth rate, not volume" distinction (beat/slide 3), the "2:59 not 3:00" distinction (beat/slide 5), and the exact price string (beat/slide 4) are all carried by the literal words in the type layer, not by color coding — safe for color-vision-deficient viewers and immune to any single frame being viewed out of context (e.g., as a shared screenshot).

---

## 10. Image-generation prompts (ready to run later — NOT yet executed)

**IMAGES NOT YET GENERATED — DRAFT MODE.** All prompts below are written for later execution via `scripts/generate_images.py` (or manual submission to an image tool) once an API key is available locally. They are saved verbatim in `image-jobs.json` in this same project folder (`projects/lunch-rush-infrastructure/image-jobs.json`). Do not run the generation script in this environment.

Every prompt explicitly states: required dimensions, subject/environment, composition, lighting/mood, brand palette, clear negative space reserved for exact copy, and a negative-constraints clause banning illegible/fake text, real logos (especially Rappi's), city-size bar charts, a landed-on "3:00" clock numeral, cash/profit iconography, duplicate people, malformed hands, and clutter.

Summary of what each job covers (full prompt text lives in `image-jobs.json`):

**Reel backgrounds (1080x1920):**
- **bg-reel-1-clock-and-bikes** — abstract pre-dawn-to-noon city atmosphere, soft gold clock-arc sweeping toward (not landing on/past) noon, blurred generic unbranded delivery-bike silhouettes in the lower frame, large clean navy negative space above for centered text.
- **bg-reel-2-growth-counter** — abstract upward data-counter motif, thin gold ascending line/arc graphic (no numerals baked in), navy field, lower-third negative space reserved for animated stat text.
- **bg-reel-3-colombia-map-arrows** — stylized, generic (non-political, non-labeled) Colombia-shaped map outline with simple gold directional arrows radiating from a few unlabeled points — explicitly NOT a bar/column chart — clean negative space reserved for city-name labels and arrows to be added as a vector/type layer.
- **bg-reel-4-restaurant-counter** — generic restaurant counter/kitchen-pass mood, stacked plates, a single blank unmarked price-tag/placard shape (no numerals), warm counter lighting within the navy/gold palette, lower-third negative space for stat text.
- **bg-reel-5-clock-sweep-spike** — large gold clock-arc graphic sweeping from roughly 11 o'clock position and stopping visibly just shy of the 3 o'clock position (never landing on or passing "3"), paired with a simple rising-then-falling spike-line graphic peaking near the top-center (symbolizing a noon peak), navy field, lower-third negative space for stat text.
- **bg-reel-6-kitchen-ops-blueprint** — abstract blueprint-style kitchen-operations diagram: thin gold line work suggesting a prep schedule grid, delivery-routing lines, and simple inventory-box outlines snapping into a highlighted time-block zone, navy field, centered negative space for the thesis line.
- **bg-reel-7-minimal-frame** — nearly empty, clean deep-navy field with one restrained thin gold corner-bracket or line-grid accent, maximum negative space, centered for text-forward minimal treatment.
- **bg-reel-8-wordmark-sting** — clean, quiet deep-navy field (optionally the faintest blueprint grid texture at very low opacity) with large clear centered negative space reserved for the JustPreneur wordmark lockup to be placed on top.

**Carousel backgrounds (1080x1350) — optional secondary asset, same visual concepts re-rendered for the portrait frame:**
- **slide-1-cover-clock-skyline** — same clock-arc-toward-noon concept as bg-reel-1, generic skyline/city-atmosphere silhouette in the lower frame, large clean upper two-thirds negative space for the headline block.
- **slide-2-growth-counter** — same ascending gold data-line concept as bg-reel-2, portrait framing, top/middle negative space reserved for headline + stat.
- **slide-3-colombia-map-arrows** — same generic map-and-arrows concept as bg-reel-3 (no bar chart), portrait framing, negative space reserved for headline, city labels, and the "growth rate, not volume" disclaimer line.
- **slide-4-restaurant-counter** — same blank-price-tag restaurant-counter concept as bg-reel-4, portrait framing, negative space reserved for the exact price string and restaurant-count stat.
- **slide-5-clock-sweep-spike** — same stop-short-of-3 clock-arc-plus-spike concept as bg-reel-5, portrait framing, negative space reserved for the longer body-copy block on this slide.
- **slide-6-minimal-frame-cta** — same minimal navy/gold-corner-bracket concept as bg-reel-7, portrait framing, negative space reserved for the closing CTA question and JustPreneur wordmark.

---

## 11. Layout prompt — where exact text goes after image/background generation

Use this as the standing instruction for whoever assembles the final Reel/Carousel in an editing or design tool once backgrounds exist. Do not let any design tool or model improvise, paraphrase, or auto-generate substitute copy — use the exact strings from §3.

**For the Reel:**
1. Place each `bg-reel-*` image as the full-bleed background for its corresponding beat, per the timing table in §3, using a slow Ken-Burns push-in (approx. 105%→112% scale) over each beat's duration if using a static image rather than true motion graphics.
2. Set kinetic text per beat exactly as written in §3's "On-screen text (verbatim)" column — no paraphrasing, no trimming. Position per the "Text position" column: centered mid-frame for beats 1, 6, 8; lower-third for beats 2, 3, 4, 5, 7.
3. Beat 2: animate the "250K → 660K+" numerals as a counting-up effect; keep "+160% YTD (Rappi-reported)" as a static line above or beside the counter, same frame, same beat.
4. Beat 3: draw city labels (Villavicencio, Ibagué, Santa Marta, Bogotá) and growth-rate arrows as a vector/type overlay directly on `bg-reel-3-colombia-map-arrows` — arrows and percentage callouts only, never bar heights. Keep the "didn't disclose city totals" clause visible in the same beat, smaller weight, directly under the headline line.
5. Beat 4: set "COP $19,900 (~US$6, per Rappi, Oct. 2026)" as one exact, unbroken string wherever the price appears — never shortened to "$19,900" alone and never abbreviated to "$5" or "$6" alone.
6. Beat 5: set "11:00 a.m.–2:59 p.m." and "peak ~noon — Rappi" exactly as written; confirm the clock-arc graphic underneath visibly stops short of 3 before finalizing the cut.
7. Add a soft navy gradient scrim behind every text block sitting over imagery (all beats except 7 and 8, which are already near-empty) at 60–75% opacity before placing type.
8. Place the small JustPreneur wordmark in a fixed bottom-safe-zone position on beats 2–7; on beat 8, remove the small corner wordmark and center a large JustPreneur wordmark/lockup with the line "Infrastructure thinking for entrepreneurs." set just below it.

**For the Carousel (if produced):**
1. Place each `slide-*` image as the background per §3, portrait full-bleed with a dark gradient text-safe zone sized to each slide's copy length (slide 5 carries the longest block and needs the most reserved space).
2. Set headline/body copy exactly as written in §3's Carousel table — word-for-word, including every "per Rappi" / "Rappi-reported" attribution clause.
3. Slide 3: same arrows-not-bars rule as Reel beat 4 above — draw city labels and arrows as a type/vector overlay, never bar heights.
4. Slide 4: same exact price string as Reel beat 4 above.
5. Slide 5: same stop-short-of-3 clock-arc rule as Reel beat 5 above.
6. Place the JustPreneur wordmark bottom-left, identical size/position, on all 6 slides.

---

## 12. Open notes for local finish / downstream agents

- **Image count:** this brief specifies 8 Reel backgrounds + 6 optional Carousel backgrounds (14 total image jobs) — all logged in `image-jobs.json`. If the team decides to publish the Reel only, the 6 carousel jobs can be skipped at generation time without any change to this brief.
- **Compliance checkpoints before publish:** confirm (a) no price string anywhere reads "$5," (b) the city-growth visual uses arrows/labels only, never bars, (c) the clock graphic never lands on or passes "3:00," (d) no Rappi logo/wordmark/brand-orange appears anywhere, (e) no cash/profit iconography appears anywhere. These five checks map directly to §0 and should be the first thing Quality Control re-verifies against the rendered assets, not just against this text brief.
- **Attribution density:** because this story leans entirely on Rappi-reported figures, every on-screen stat (beats 2, 3, 4, 5) carries its own "per Rappi" / "Rappi-reported" clause by design — do not let a design pass "clean up" or drop these for visual tidiness; the sourcing is load-bearing, not decorative.
- **Status: images generated in this session: NONE.** This is draft mode — no image-generation API key is available in this environment. All prompts in §10 and the layout instructions in §11 are complete and ready to run later via `scripts/generate_images.py` or `/justpreneur-finish`. No placeholder or fabricated image files were created.
