# Visual Design Brief — "Take-Rate Math" (Spotify Creator Memberships)

**Status: IMAGES NOT YET GENERATED — DRAFT MODE.** This brief and the prompts below are complete and ready to run through `scripts/generate_images.py` once an image-generation API key is available locally (via `/justpreneur-finish`). No image files exist yet for this project.

Format: Instagram carousel, 7 slides, 1080 x 1350 px each.

---

## 1. Overall creative concept

"Take-Rate Math" is a comparison-journalism piece disguised as a carousel: Spotify's new 90% creator split looks generous in isolation, but the real story is what that number is a percentage *of*, and how it stacks up against platforms creators already use. The visual system should read like a page out of a modern business/data publication (think Stripe's or The Information's editorial decks) — clean stat cards, confident typography, restrained color-coding — not a motivational quote template. The carousel has two visual "modes" that must stay clearly distinguished: **confirmed facts** (navy/white editorial cards) and **the open question on fees** (slide 5), which gets a visibly different, flagged treatment so no reader mistakes it for a settled number.

## 2. Composition and focal hierarchy

Consistent frame grammar across all 7 slides:
- A fixed top zone (approx. top 150px) reserved for the small JustPreneur wordmark lockup — same position, same size, every slide.
- A primary headline zone occupying the upper-to-middle 40–55% of the frame — largest, boldest element, always warm white or navy depending on background, always the first thing the eye lands on.
- A secondary zone (supporting copy, stat callouts, or comparison elements) in the middle 25–35%.
- A clear bottom safe zone (bottom 150px) kept free of copy except where the CTA slide's action button lives.
- Focal hierarchy on every slide: (1) headline statement, (2) supporting stat/visual device, (3) JustPreneur brand mark. Imagery is always a *background/structural device*, never competing with text for attention — no busy photography, no literal people, since this is a data/analysis story, not a personal profile story.

## 3. Exact placement of headline, supporting copy, imagery, and branding

Shared grid (1080 x 1350, safe margins 60px left/right, 80px top, 100px bottom — comfortably inside Instagram's ~250px top/bottom UI-overlap zone):

- **JustPreneur lockup:** top-left, baseline at y≈100px, wordmark only (no tagline), in warm white on dark slides / deep navy on light slides. Height ≈ 36px. Never resized, never repositioned, every slide.
- **Headline:** starts at y≈260px, left-aligned, max width 920px (60px margins), max 3 lines, generous line-height (~1.15).
- **Supporting copy / subheadline:** directly below headline with 32px gap, smaller weight, max width 880px.
- **Visual device (bars, question mark, chart):** lives in the middle-to-lower-middle band, roughly y≈750–1150px, never overlapping text, never touching the 60px side margins.
- **CTA slide only:** a gold accent bar (8px, full content-width) sits above the final action line at y≈1180px to mark it as the terminal action slide.

## 4. Typography direction

- **Headline font:** heavy geometric/grotesque sans-serif, tight tracking, true black/heavy weight (direction reference: Inter Black, Söhne Kräftig, or Neue Haas Grotesk Display Black). Set in sentence case, never all-caps for full sentences (all-caps reserved only for the three platform-name labels on slide 4 and the "NOT YET CONFIRMED" flag on slide 5).
- **Supporting copy font:** same type family, Regular/Medium weight, slightly warmer tracking, 60–65% the headline's point size.
- **Numerals (90%, 70%, 88–92%, 10%):** set in the headline weight but can step up in size as standalone stat callouts on slides 2 and 4 — these are typeset by the design tool, never generated inside the image.
- **Minimum effective headline size:** must remain legible at Instagram in-feed thumbnail scale — no line should require zooming to read on a standard phone screen.

## 5. Color palette

Brand defaults, used with intention rather than decoration:
- Deep navy `#0B1B33` — primary dark background, authority/analysis tone.
- Steel gray `#3D4652` — structural lines, chart tracks, secondary text.
- Warm white `#F6F2E9` — primary light background and primary text-on-navy color.
- Energy gold `#D9A441` — accent only: the Spotify bar on slide 4, the CTA accent bar on slide 7, and the question-mark motif on slide 5 (gold here reads as "flagged," not "celebratory" — context changes its meaning).

No new colors are introduced. Slide 5's distinctness comes from **motif and texture** (dashed border, diagonal hatch, oversized translucent "?"), not a new hue, to keep the palette disciplined while still visually flagging "this is unresolved."

**Slide color rhythm (alternation for editorial pacing):**
1. Cover — Navy
2. Context/setup — Warm white
3. Concept ("what is a take-rate") — Navy
4. Comparison — Warm white (best legibility for a data chart)
5. Caveat/open question — Navy base + dashed/hatched "unconfirmed" overlay + gold "?" (visibly the outlier slide)
6. Insight — Warm white
7. CTA — Navy + gold accent bar

## 6. Image treatment

No photography, no human figures, no stock-photo clichés, no literal platform logos (Spotify/YouTube/Patreon names appear only as typeset text added in the design tool, never as generated logo marks — this avoids fake/distorted logos entirely). All 7 background images are abstract, editorial, data-adjacent textures: fine grid lines, abstract bar-chart silhouettes, a single quotation/question glyph, subtle gradients. Every background must be generated with large, genuinely flat negative space in the zones specified in Section 3 — not just "space that happens to be empty," but deliberately composed emptiness the design tool can lay exact type into without fighting texture or gradient noise.

## 7. Instagram safe-margin instructions

- Canvas: 1080 x 1350 px (4:5), matches Instagram's current carousel-safe portrait ratio.
- Keep all text and essential graphic elements within a 960 x 1190 px safe area (60px side margins, 80px top margin, 100px bottom margin) to avoid UI cropping in-feed and in the carousel-dot overlay area.
- No text within 80px of the top edge or 100px of the bottom edge.
- JustPreneur lockup never touches the absolute top-left corner — minimum 60px/80px inset.

## 8. Slide-to-slide consistency rules

- Same lockup position/size/color-per-background-type on every slide.
- Same headline start position (y≈260px) and same left margin (60px) on every slide — reader's eye should land in the same spot slide after slide.
- Same type family and weight system throughout; only size and color shift.
- The navy/white alternation (Section 5) must hold except where a slide is deliberately flagged as the outlier (slide 5) — and even then, navy remains the base, only the overlay motif changes, so the sequence doesn't feel broken, only flagged.
- Numerals/stats always rendered in the same stat-callout style (tabular-aligned, headline weight) wherever they appear (slides 2, 4, 5).
- The "~" / "approximately" qualifier on YouTube's and Patreon's figures (slide 4) must appear in the actual typeset numerals every time they're referenced — this is a copy/layout instruction for the design tool, not something the image-generation step needs to render.

## 9. Accessibility and contrast check

- Headline text: warm white (`#F6F2E9`) on navy (`#0B1B33`) = contrast ratio ~13.9:1 (AAA). Deep navy on warm white = same ratio, AAA.
- Supporting copy at reduced opacity must not drop below ~70% opacity on its background to retain AA-level contrast at smaller point sizes; verify in layout tool before export.
- Gold (`#D9A441`) is used only for accents/numerals at headline weight and size — never for body-copy-sized text, since gold-on-navy at small sizes drops below comfortable contrast.
- Slide 5's dashed/hatch overlay must stay low-opacity (≤20%) behind the headline zone so it doesn't reduce text legibility — texture sits in the visual-device band only, never behind type.
- No information is conveyed by color alone: slide 5's "open question" status is carried by the literal words "NOT YET CONFIRMED" / the question-mark glyph, not by gold color alone, so it still reads correctly for colorblind viewers.

## 10. Image-generation prompts (one per slide)

**IMAGES NOT YET GENERATED — DRAFT MODE.** All prompts below are also saved to `projects/take-rate-math/image-jobs.json` for later execution via `scripts/generate_images.py` once a local image-generation API key is available.

**Slide 1 — Cover background (`slide-1-cover`)**
> 1080 x 1350px. Abstract premium business-editorial background, deep navy (#0B1B33) base. Three very subtle, soft-edged vertical bar-chart silhouettes of different heights rise from the lower third of the frame in low-opacity steel gray (#3D4652), hinting at a comparison concept without any numbers, labels, or logos on them. A faint fine-line grid texture sits behind the bars at very low opacity for a data/analytics feel. Soft single-source lighting from the upper right, subtle depth, no glare or harsh highlights. Mood: confident, analytical, premium — resembles a modern business-magazine cover, not a motivational template. No text, no numbers, no logos, no icons, no people, no coins or currency symbols. Large flat, genuinely uncluttered negative space across the full upper-to-middle band (roughly the top 60% of the frame) for a bold headline and subheadline to be added afterward in a design tool. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter.

**Slide 2 — Context/setup background (`slide-2-context`)**
> 1080 x 1350px. Clean warm white (#F6F2E9) editorial background with an extremely subtle paper-grain texture and a faint steel-gray (#3D4652) fine-line grid in the upper portion only, evoking a modern business-report page. Soft, even lighting, no harsh shadows, no gradients. Mood: clean, premium, analytical, like a page from a contemporary business publication. No text, no numbers, no icons, no logos, no people, no coins or currency symbols. Generous flat negative space through the full frame, especially the middle band, for a headline, a supporting line, and a simple two-figure split callout (90%/10%) to be added afterward in a design tool. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter.

**Slide 3 — Concept background (`slide-3-concept`)**
> 1080 x 1350px. Deep navy (#0B1B33) background with a single abstract motif: a thin steel-gray (#3D4652) circle or ring outline positioned in the lower-middle of the frame, suggesting "a percentage of something" without rendering any numbers, percentage signs, or pie-chart segments. Soft ambient lighting, minimal and restrained. Mood: thoughtful, analytical, slightly inquisitive — a "pause and think" visual beat between the setup and the data. No text, no numbers, no icons, no logos, no people. Large flat negative space across the upper two-thirds of the frame for a multi-line headline to be added afterward in a design tool. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter.

**Slide 4 — Comparison chart background (`slide-4-comparison`)**
> 1080 x 1350px. Clean warm white (#F6F2E9) editorial background featuring three empty, unlabeled vertical bar-chart tracks of different heights arranged side by side in the lower-middle band of the frame, rendered as simple flat color-blocked shapes with no numbers, no percentage signs, and no platform names or logos anywhere on them. The tallest bar (left-most) is filled in energy gold (#D9A441); the other two bars are filled in steel gray (#3D4652) at two visibly different heights. Thin baseline rule beneath all three bars. Soft, even, shadow-free lighting for maximum legibility. Mood: precise, data-forward, editorial infographic — like a chart in a business magazine before captions are added. No text, no numbers, no logos, no icons, no people. Clear flat negative space above the bars for a headline and above/below each bar for stat labels (to be typeset afterward, including "~" and "approximately" qualifiers) in a design tool. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter.

**Slide 5 — Open-question / caveat background (`slide-5-caveat`)**
> 1080 x 1350px. Deep navy (#0B1B33) background, visually distinct from the other navy slides in this set: a very large, soft-edged, translucent energy-gold (#D9A441) question-mark glyph is centered in the lower-middle band of the frame at low opacity (roughly 15-20%), rendered as a single clean typographic question mark shape, not clipart. A thin dashed steel-gray (#3D4652) rectangle outline sits just below the question mark, like an empty "pending" callout box with nothing written inside it. A faint diagonal hatch-line texture at very low opacity fills a narrow band near the bottom edge, reinforcing an "unresolved/pending" feeling. The composition must not lean toward either a "yes" or "no" answer — it should read as neutrally unresolved, not as confirming or denying anything. Soft, moody, slightly more shadowed lighting than the other slides to signal "this one is different." Mood: alert but credible, "there's a question mark here," not alarmist, not conspiratorial. No text, no numbers, no checkmarks, no X marks, no icons, no logos, no people. Clear flat negative space in the upper half of the frame for a headline and a "NOT YET CONFIRMED" flag label to be added afterward in a design tool. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter.

**Slide 6 — Insight background (`slide-6-insight`)**
> 1080 x 1350px. Clean warm white (#F6F2E9) editorial background with a single thin steel-gray (#3D4652) line graph sweeping gently across the lower-middle band of the frame, left to right, with one single point on the line highlighted as a small solid energy-gold (#D9A441) dot — representing "your own number," not a market trend. No axis labels, no numbers, no gridlines beyond the single line itself. Soft, even lighting. Mood: clarifying, confident, "here's the one number that matters." No text, no numbers, no icons, no logos, no people. Generous flat negative space across the upper two-thirds of the frame for a bold headline to be added afterward in a design tool. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter.

**Slide 7 — CTA background (`slide-7-cta`)**
> 1080 x 1350px. Deep navy (#0B1B33) background with a single bold horizontal energy-gold (#D9A441) accent bar positioned in the lower third of the frame, full content-width, flat and clean, no gradient, no glow effects beyond a soft subtle edge. Rest of the background is minimal navy with a very faint fine-line grid texture at low opacity, matching the cover slide's texture for series bookending. Soft, even lighting, confident and action-oriented mood — the "close" of the carousel. No text, no numbers, no icons, no logos, no people, no buttons or UI chrome rendered in the image. Clear flat negative space above the gold bar for a three-line action statement and below it for the JustPreneur lockup, to be added afterward in a design tool. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter.

## 11. Layout / text-placement prompt (applies after image generation, for all 7 slides)

Once the 7 background images above are generated, use a design tool (Canva/Figma/Photoshop) to add all exact copy — do not rely on image generation for any of this text:

- **Slide 1:** Headline "90% Sounds Generous. Compare It Before You Believe It." set across 2–3 lines starting at y≈260px, 60px left margin, warm white, headline weight, max width 920px. Subheadline "Spotify's new creator split, next to the platforms you already use." directly below, 32px gap, warm white at 80% opacity, Regular weight. JustPreneur wordmark top-left at y≈100px, warm white.
- **Slide 2:** Headline statement "Spotify just rolled out Creator Memberships in 34 markets." at top. Below it, a two-figure stat callout: "90%" (large, navy, headline weight, labeled "Creators keep" beneath in small caption) paired with "10%" (smaller, steel gray, labeled "Spotify keeps" beneath). JustPreneur lockup top-left in navy.
- **Slide 3:** Headline "A take-rate is a percentage of *something.*" with "something" in italic or gold emphasis. Below it: "Before you celebrate the number, ask what it's actually a cut of." as supporting copy. JustPreneur lockup top-left in warm white.
- **Slide 4:** Headline "Here's the same number next to the platforms you already use." (restated framing, not new copy — summarizes the comparison; if a more literal lead-in is preferred, use the approved comparison copy directly as the headline). Over each bar, typeset: "Spotify Creator Memberships — ~90%" (gold bar), "YouTube Memberships — ~70%" (steel-gray bar), "Patreon — ~88–92%" (steel-gray bar). The "~" must be present on every figure except none — all three carry the qualifier, consistent with the approved copy. Platform names in small caps above each bar, stat numerals in headline weight below or beside each bar.
- **Slide 5:** A small "NOT YET CONFIRMED" flag label (all caps, condensed, gold) placed just above the headline. Headline: "Here's what Spotify hasn't said: whether processing, FX, or payout fees come out of that 90% — or come off the top before it." Supporting line: "Gross vs. net is still unconfirmed." set inside or just below the dashed callout box from the background image. This slide must visually read as an open question, not a resolved fact in either direction — do not add a checkmark, an X, or any element implying Spotify confirmed or denied fee deductions.
- **Slide 6:** Headline "The real competition isn't audience size. It's take-rate — and you won't know yours until you check it." set across 2–3 lines, navy text, positioned above the highlighted data point in the background art.
- **Slide 7:** Three-line CTA set as a short numbered sequence for mobile scanability: "1. Pull your last 3 payouts." / "2. Calculate what you actually kept." / "3. Compare it across every platform you publish on." stacked above the gold accent bar, warm white text, headline weight for the numerals, Regular weight for the rest. JustPreneur lockup below the gold bar, centered, warm white — this is the one slide where the lockup may move to the bottom to mark it as the carousel's final frame.

All copy above is the approved copy verbatim or a direct restatement for headline framing (slide 4's lead-in) — no new claims, statistics, or qualifiers have been added. The "~" qualifiers on slide 4 and the "unconfirmed" framing on slide 5 are preserved exactly as specified by the copywriter.
