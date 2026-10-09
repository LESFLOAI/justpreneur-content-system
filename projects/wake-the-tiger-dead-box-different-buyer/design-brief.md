# Design Brief — "Dead Box, Different Buyer"
Project: wake-the-tiger-dead-box-different-buyer
Agent: Visual Director
Status: DRAFT MODE — no images generated yet (no image-generation API key available in this environment)
Format: Instagram Carousel, 9 slides, 1080 x 1350 px (portrait) each
Target slot: 2026-10-09, 9:00 PM

---

## DRAFT MODE NOTICE

No image-generation API key is available in this cloud environment. This brief contains the complete creative direction and all nine image-generation prompts, saved to `projects/wake-the-tiger-dead-box-different-buyer/image-jobs.json`. **Images have NOT been generated.** Run the generation step locally via `/justpreneur-finish`:

```bash
python3 scripts/generate_images.py --jobs "projects/wake-the-tiger-dead-box-different-buyer/image-jobs.json" --out "projects/wake-the-tiger-dead-box-different-buyer/images"
```

Everything below is designed to be used as-is at that point — no further creative decisions should be needed, only execution.

---

## 1. Overall Creative Concept

An editorial "case-file" carousel built around a single recurring motif: a stylized architectural floor-plan outline of Unit 5001 at Westfield London, rendered first in a desaturated, dormant "closed" state and then in a saturated, immersive "reopened" state — the same footprint, two different businesses. The carousel reads like a business-media investigative explainer (think Fast Company / The Hustle), not a motivational quote template. Photography/illustration leans toward abstract architectural and spatial imagery (empty retail shells, glowing immersive-art corridors, crowd silhouettes) rather than literal brand photography of either company, since we do not have licensed photos of KidZania or Absurd City. No invented signage, no fake logos.

Tone discipline: KidZania is shown neutrally (empty, quiet, dormant — not mocked, not decayed/trashed). Absurd City is shown as a **rendering/concept-art mood**, not a documentary photo of a finished, operating space — the opening is scheduled (Oct 15, 2026), not completed as of post date. Treat Absurd City visuals as "concept visualization" in feel: vivid, glowing, art-directed, slightly stylized/painterly rather than photoreal crowd documentation, so nothing implies the event has already happened.

## 2. Composition and Focal Hierarchy

Each slide follows a strict hierarchy so the carousel feels like one authored piece:
1. Headline / slide label (top third, largest type)
2. Supporting copy (middle, readable block)
3. Image motif (background or contained panel, never fighting with text)
4. JustPreneur wordmark (fixed position, bottom, every slide)

For slides with heavier copy (4, 5, 6, 9), the image motif shrinks to a background texture/frame rather than a full-bleed photo, so word count can stay legible. For visual-forward slides (1, 2, 3, 7, 8), the floor-plan motif gets more real estate.

## 3. Branding, Headline, and Copy Placement (Master Grid)

Canvas: 1080 x 1350 px. Instagram-safe margins: keep all text and the JustPreneur wordmark inside a 96 px margin on all four sides (effective safe area 888 x 1158 px). Keep critical headline text additionally clear of the very bottom 120 px (UI overlap on some devices) and top 80 px (notification bar on reposts/stories crops).

- **JustPreneur wordmark**: bottom-center, 64 px from bottom safe-margin line, warm white or energy gold wordmark depending on background value, every slide, identical position/size for consistency. Small enough to not compete with headline, large enough to be legibly read as "JustPreneur" (not a tiny illegible mark).
- **Slide label / eyebrow** (e.g., "KIDZANIA — CLOSED"): top safe margin, all-caps, letter-spaced, 36-40px, gold or steel gray depending on slide.
- **Headline**: upper-middle third, left-aligned, generous line-height, warm white or deep navy depending on background contrast.
- **Supporting copy**: directly below headline, lighter weight, max ~60-65 characters per line, warm white/steel gray.
- **Floor-plan motif**: positioned as a right-aligned or full-bleed background element, always kept behind or beside text — never under headline type without a scrim/gradient for contrast.

All exact wording comes from `content-copy.md` verbatim — no new copy is invented here.

## 4. Typography Direction

- **Headline typeface**: a bold, modern geometric/grotesk sans (e.g., a style akin to Söhne/Inter Tight/Neue Haas Grotesk Bold) — confident, editorial, not a script or novelty font.
- **Body/support typeface**: a clean grotesk at regular/medium weight, same family as headline for consistency, smaller size, slightly increased line-height for mobile legibility.
- **Eyebrow/labels**: same family, semi-bold, all-caps, letter-spacing +4-6%.
- Minimum effective headline size on a phone screen: no smaller than roughly 56-64px at this canvas size for primary headline slides (1, 2, 3, 8); slightly smaller (44-52px) acceptable for copy-dense slides (4, 5, 6, 9) since those carry more words.
- No condensed/decorative fonts, no drop shadows on text, no outlined/stroked text — use solid color + scrim contrast instead.

## 5. Color Palette

Primary brand palette (deep navy, steel gray, warm white, energy gold), split by motif state:

- **"Before" / KidZania-closed state**: deep navy (#0E1626) and steel gray (#6B7280) dominant, desaturated, cool, quiet. Minimal gold — if used, a thin dim gold accent line only, signaling "dormant," not energetic.
- **"After" / Absurd City state**: energy gold (#E8B23D-ish) and a richer saturated accent (can introduce one secondary vivid hue, e.g., a magenta or teal, *only* within the floor-plan motif's interior glow, not as a new brand color) against deep navy base, warmer, higher contrast, more "alive."
- **Neutral/explainer slides (4, 5, 6, 7, 9)**: deep navy base + warm white text + gold accent dividers, steel gray for secondary/hedge text (e.g., disclaimers), keeping the editorial, analytical register throughout.
- Avoid pure black and pure white — use warm white (#F5F1E8-ish) and deep navy instead for softer, premium contrast.

## 6. Image Treatment

- Floor-plan motif: clean architectural line-art/outline style (like a blueprint or wayfinding map), not a literal photograph of a mall directory — this lets us depict "Unit 5001" without claiming real floor-plan accuracy we don't have.
- "Before" imagery: empty, still, softly lit retail-shell interiors — dust-free, neutral, not derelict/trashed (protects neutral tone toward the liquidated operator).
- "After" imagery: concept-art/rendering mood — glowing geometric light installations, abstract immersive-art environments, painterly or stylized rendering quality — deliberately avoiding "photo of a packed grand opening," since the opening has not happened yet.
- No real photographs of actual KidZania or Absurd City locations (we don't have licensed assets) — everything is original illustrative/photographic-style generation, abstract enough to not misrepresent either brand's actual décor.
- No people's faces rendered with specific likeness; crowd/visitor references (slide 8) use silhouettes or soft-focus anonymized figures only.
- No readable fake signage, fake logos, or fabricated UI/maps with invented labels — any lettering baked into the image itself must be avoided entirely; all real wording is added as a text layer afterward (see Section 11 below).

## 7. Instagram Safe-Margin Instructions

- Canvas 1080 x 1350.
- Keep all text 96 px minimum from every edge.
- Keep JustPreneur wordmark and headline additionally clear of bottom 120 px (profile-grid crop / UI overlap zone) and top 80 px.
- When swiping between carousel slides, keep the floor-plan motif's "closed" (slide 2) and "opening" (slide 3) renders at matching scale/crop/angle so the before/after flip reads instantly without text.

## 8. Slide-to-Slide Consistency Rules

- Every slide uses the identical JustPreneur wordmark treatment, position, and size.
- Slides 2 and 3 must use the *same camera angle, framing, and floor-plan outline shape* — only palette/light/mood differ ("closed" muted vs. "opening" saturated) — this is the core visual thesis and must be unmistakable when swiped side by side.
- The floor-plan outline motif recurs as a subtle background watermark/line-art element on slides 1, 4, 6, 7, and 8 to keep the "same footprint" idea threaded through the whole carousel, even on copy-heavy slides.
- Color temperature arcs from cool/muted (slide 2) to warm/saturated (slide 3) and that warmer register continues for slides 4 onward, reinforcing "the shift has been decided," while slide 9's CTA returns to a slightly more restrained navy/gold balance to host the disclaimer calmly.
- No slide may visually depict Absurd City as already open/operating with a crowd — concept-render mood only, every time it appears (slides 1, 3, 4, 5, 7, 8, 9 backgrounds).

## 9. Accessibility and Contrast Check

- Headline text: warm white (#F5F1E8) on deep navy (#0E1626) or deep navy on warm white — both pairings exceed WCAG AA contrast (>7:1) for large text.
- Avoid placing body copy directly over high-detail image areas; use a navy gradient scrim (60-80% opacity) behind any text sitting on photographic/illustrative backgrounds.
- Gold (#E8B23D) is used only for short labels/accents/dividers at larger sizes — never for small long-form body text — to avoid insufficient contrast on navy.
- Disclaimer/hedge text (slide 9: "not yet live as of this post... scheduled bet, not a proven result") must be set in warm white or light steel gray at normal body weight/size — legible, not buried in fine print, since it's a core approved-facts requirement, not a legal footnote.
- Minimum body text size kept at a mobile-legible floor even on the copy-dense slides (no sub-32px body text).

## 10. Image-Generation Prompts (per slide)

See `image-jobs.json` in this same folder for the structured version. Full prompt text:

**Slide 1 — Cover**
"Editorial business-media cover illustration, 1080x1350 portrait. Subject: a clean architectural blueprint-style floor-plan outline of a large single retail unit, bisected vertically down the center — left half rendered in cool, desaturated deep-navy and steel-gray line art (quiet, dormant, empty), right half rendered in warm, saturated gold-and-navy line art with a soft glowing immersive-art ambience (alive, vivid) — same outline shape on both halves, perfectly mirrored, symbolizing one footprint with two different lives. Composition: floor-plan centered and large, occupying the lower two-thirds of the frame, with generous empty dark-navy sky/negative space in the top third and a soft dark gradient across the very top and bottom for text legibility. Lighting: cool flat light on the left, warm glowing light on the right, dramatic but premium, editorial — not sci-fi, not neon-club. Brand palette: deep navy, steel gray, warm white, energy gold, with one additional warm accent glow strictly inside the right-hand floor plan only. Negative space: large clear area in the top third of the frame and a clear strip across the very bottom for text and logo — no text, no numbers, no letters, no logos, no signage anywhere in the image. No illegible text, no fake logos, no duplicated people, no malformed hands, no clutter, no small decorative icons."

**Slide 2 — The Before (KidZania, closed)**
"Editorial business-media photograph-style illustration, 1080x1350 portrait. Subject: the interior of a large, empty retail/entertainment unit — soaring ceiling, bare polished floor, faint ghost outlines where play structures and signage once stood (rendered abstractly, not as readable signage), a few shafts of cool daylight entering from clerestory windows. Mood: quiet, still, dormant — not decayed, not trashed, not creepy — simply vacant and waiting, neutral in tone. Composition: wide symmetrical interior view, vanishing point centered, lots of open floor space in the lower two-thirds, clear plain upper-wall area in the top third for text overlay. Lighting: soft, cool, overcast daylight, long soft shadows, slightly desaturated. Brand palette: deep navy and steel gray dominant, a single thin dim gold accent line on the floor as the only warm note. Negative space: clear plain upper third and a clear lower strip for text and logo. No visible text, numbers, logos, or brand signage of any kind. No illegible text, no fake logos, no people, no malformed hands, no clutter, no small decorative icons."

**Slide 3 — The After (Absurd City, opening Oct 15 2026 — concept-render mood, not yet open)**
"Editorial business-media concept-rendering illustration, 1080x1350 portrait. Subject: the same large interior shell as a 'before' companion image, same architectural proportions and camera angle, now reimagined as a glowing immersive-art environment — abstract oversized sculptural light installations, painterly saturated color washes, geometric glowing forms suspended in the space — styled clearly as a concept visualization / architectural rendering, not a documentary photo of a finished, crowded, operating venue. No people present, no grand-opening crowd, to avoid implying the event has already occurred. Composition: same wide symmetrical interior view and vanishing point as the 'before' image, open floor space in the lower two-thirds, clear plain upper-wall area in the top third for text overlay. Lighting: warm, vivid, glowing ambient light, saturated golds and one secondary accent hue (e.g. magenta or teal) used only within the light installations. Brand palette: deep navy base with energy gold and warm accent glow dominant. Negative space: clear plain upper third and clear lower strip for text and logo. No visible text, numbers, logos, or brand signage of any kind, no people, no crowd, no readable UI or wayfinding maps. No illegible text, no fake logos, no duplicated people, no malformed hands, no clutter, no small decorative icons."

**Slide 4 — What Actually Changed**
"Editorial business-media illustration, 1080x1350 portrait. Subject: an abstract split composition — left side a small, soft-edged motif suggesting family/children's play (simple abstract shapes like a toy block or balloon silhouette, no readable text or brand marks), right side a small soft-edged motif suggesting adult immersive art (an abstract glowing sculptural form), both motifs modest in scale and positioned low in the frame, with the same ghost floor-plan outline from slides 2-3 running faintly across the full width behind both as a connecting watermark line. Composition: large clear negative space across the top two-thirds of the frame for a substantial headline and body copy block; visual motifs confined to the bottom third only. Lighting: moody deep-navy background with soft directional light on each motif, cool on the left, warm on the right. Brand palette: deep navy base, steel gray, warm white, energy gold accent on the right-hand motif only. Negative space: top two-thirds fully clear for text, bottom strip for logo. No visible text, numbers, logos, or signage. No illegible text, no fake logos, no duplicated people, no malformed hands, no clutter, no small decorative icons."

**Slide 5 — The Track Record Behind the Bet**
"Editorial business-media concept illustration, 1080x1350 portrait. Subject: a moody, abstract immersive-art corridor or chamber — glowing sculptural light forms receding into the distance, evoking an established, successful immersive attraction (suggesting Wake The Tiger's original Bristol site) without depicting any specific real building or signage. Composition: motif confined to the lower half of the frame as a glowing horizon-like band, with a large clear dark-navy area across the top half for a headline and multiple lines of supporting copy. Lighting: warm, confident, glowing gold and amber light with deep navy shadow, premium and atmospheric, not garish or neon-club. Brand palette: deep navy base, energy gold dominant accent, warm white highlights. Negative space: top half fully clear for text, bottom strip clear for logo. No visible text, numbers, logos, badges, or signage of any kind (no B Corp badge rendering). No illegible text, no fake logos, no duplicated people, no malformed hands, no clutter, no small decorative icons."

**Slide 6 — The Lesson**
"Editorial business-media illustration, 1080x1350 portrait. Subject: a single abstract architectural outline (echoing the recurring floor-plan motif) rendered faintly in thin gold line-art against a deep navy background, with a soft diagnostic visual cue — a simple abstract magnifying-lens-shaped glow or a soft circular highlight — resting over one corner of the outline, symbolizing diagnosis/evaluation rather than literally depicting a magnifying glass object. Composition: motif small and placed in the lower third or lower corner, large open negative space above and across the frame for a multi-line headline and body copy. Lighting: calm, even, moody deep-navy ambient light with one soft gold glow point. Brand palette: deep navy, steel gray, energy gold accent, warm white. Negative space: top two-thirds and most of the frame clear for text; motif kept small and quiet so it never competes with the copy. No visible text, numbers, logos, or signage. No illegible text, no fake logos, no duplicated people, no malformed hands, no clutter, no small decorative icons."

**Slide 7 — The Play**
"Editorial business-media illustration, 1080x1350 portrait. Subject: the recurring floor-plan outline motif shown once more, now rendered as a single clean gold line-art shape centered low in the frame, with a subtle visual suggestion of 'change of ownership' — two soft overlapping glow tones (one cool navy, one warm gold) meeting at the outline's edge, symbolizing the same footprint being reinterpreted, without any literal key, handshake, or figurative icon. Composition: motif occupies roughly the bottom third, large clear dark-navy negative space fills the top two-thirds for a short, punchy headline and two supporting lines. Lighting: balanced, moody, premium, soft gradient from cool to warm across the outline. Brand palette: deep navy base, energy gold and steel gray accents, warm white. Negative space: top two-thirds fully clear for text, bottom strip clear for logo. No visible text, numbers, logos, or signage. No illegible text, no fake logos, no duplicated people, no malformed hands, no clutter, no small decorative icons."

**Slide 8 — Final Takeaway**
"Editorial business-media illustration, 1080x1350 portrait. Subject: a wide, modern shopping-centre exterior or atrium at dusk, rendered in an abstract/painterly architectural style (not a specific identifiable real building, no readable signage), with soft anonymized crowd silhouettes of varied, diverse people walking through an open plaza in the foreground, suggesting 'a new customer base' arriving. The recurring floor-plan outline appears faintly as a thin gold watermark line integrated into the architecture's glass facade reflection. Composition: architecture and crowd silhouettes occupy the lower half of the frame, large clear dusk-navy sky area across the top half for a two-line headline. Lighting: warm dusk light, glowing windows, gold and navy twilight palette, premium and cinematic, not garish. Brand palette: deep navy, energy gold, warm white, steel gray. Negative space: top half fully clear for text, bottom strip clear for logo. No visible text, numbers, logos, storefront signage, or brand marks of any kind. No illegible text, no fake logos, no duplicated people, no malformed hands, no clutter, no small decorative icons."

**Slide 9 — CTA / Closing**
"Editorial business-media illustration, 1080x1350 portrait. Subject: a calm, minimal deep-navy background with the recurring floor-plan outline rendered very faintly and small as a subtle centered watermark, surrounded by generous open space — a restrained, quiet closing composition rather than a busy visual, appropriate for hosting a longer block of closing copy plus a disclaimer line. Composition: motif small and centered, vast open negative space on all sides for multiple paragraphs of text plus a prompt/question line. Lighting: soft, even, moody ambient navy glow with a single soft gold highlight on the outline. Brand palette: deep navy dominant, energy gold accent only on the thin outline, warm white implied for text. Negative space: nearly the entire frame clear for text; motif minimal and unobtrusive. No visible text, numbers, logos, or signage. No illegible text, no fake logos, no duplicated people, no malformed hands, no clutter, no small decorative icons."

## 11. Layout Prompt — Exact Text Placement After Image Generation

Apply identically across all 9 slides unless noted: JustPreneur wordmark bottom-center, 64px above the bottom safe-margin line, in warm white (on navy backgrounds) — consistent size/weight every slide. All text blocks respect the 96px safe margin on every edge.

- **Slide 1**: Headline (two lines, bold, warm white, left-aligned, upper-middle of frame, over the dark gradient at top of the bisected floor-plan art): "SAME ~80,000 SQUARE FEET. / COMPLETELY DIFFERENT BUSINESS." Directly beneath, smaller italic/regular support line in steel gray or muted gold: "Westfield London, Unit 5001 — before and after." JustPreneur wordmark bottom-center.

- **Slide 2**: Eyebrow label top-left, all-caps gold, letter-spaced: "KIDZANIA — CLOSED". Beneath it, smaller warm white line: "Westfield London, Unit 5001, Ariel Way". Mid-lower block in warm white, regular weight: "UK operator Edutainment Operations Limited announced closure Jan 2, 2024. Entered creditors' voluntary liquidation Jan 11, 2024." Final short line, slightly larger/bold: "The unit sat empty." JustPreneur wordmark bottom-center.

- **Slide 3**: Eyebrow label top-left, all-caps gold: "ABSURD CITY — OPENING OCT 15, 2026". Beneath it: "Same ~80,000 sq ft shell." Mid-lower block, warm white: "New operator: Wake The Tiger — founded by members of the Boomtown Fair festival team. Tickets on sale since July 21, 2026." JustPreneur wordmark bottom-center.

- **Slide 4**: Headline top area, bold, warm white, two short lines: "Not the real estate. / The buyer." Beneath, body copy: "KidZania sold family edutainment. Absurd City is built for adult-leaning immersive art — several themed districts (reports vary on the exact number)." Smaller line below: "Co-founders: Graham MacVoy (CEO), Luke Mitchell (Chief Creative Officer)." JustPreneur wordmark bottom-center.

- **Slide 5**: Headline/eyebrow: "The Track Record Behind the Bet" (can be set as a mid-size bold header rather than tiny eyebrow, since this slide has no separate large headline in the approved copy). Body copy below: "Wake The Tiger's original site — Bristol's Amazement Park, opened July 2022 — has reportedly drawn 500,000+ visitors from 70+ countries, per Wake The Tiger." Second paragraph: "The company is a certified B Corp (per the official B Corp directory) and describes itself as the UK's first visitor attraction to hit that mark — a self-description, not an independently verified superlative." Keep both hedges ("reportedly," "per Wake The Tiger," "self-description, not an independently verified superlative") fully intact and equally legible to the rest of the body text — do not shrink or visually bury them. JustPreneur wordmark bottom-center.

- **Slide 6**: Headline, bold, warm white: "Before you write off distressed infrastructure —" Second line, slightly smaller: "a venue. a platform. an audience. a lease —" Third block, bold, gold or warm white, slightly larger for emphasis: "diagnose first:" Final two short lines as a stacked pair: "Did it fail on execution?" / "Or on audience fit?" JustPreneur wordmark bottom-center.

- **Slide 7**: Headline, bold, warm white, large: "Same asset. Different buyer." Beneath, two supporting lines: "Don't operate the old idea harder." / "Reposition it for who actually wants it." JustPreneur wordmark bottom-center.

- **Slide 8**: Headline, bold, warm white, two lines, large (this is the final-takeaway slide, should feel like a strong closing statement): "Westfield London didn't need a new unit." / "It needed a new customer." JustPreneur wordmark bottom-center.

- **Slide 9**: Body copy block, warm white, legible body size (not fine print): "Absurd City opens Oct 15, 2026 — not yet live as of this post. This is a scheduled bet, not a proven result. Check Wake The Tiger's official channels for tickets, pricing, and details." Space below, then a distinct question line, bold or larger size: "What dead asset in your business needs a different buyer — not a harder push?" Final short line: "Save this for your next audit." JustPreneur wordmark bottom-center.

All copy above is verbatim from the approved `content-copy.md` Section 3 — no wording has been added, trimmed, or rephrased.

---

## Summary for Next Agent

Images are NOT generated — this is a prompts-only draft brief. `image-jobs.json` in this folder is ready to feed directly into `scripts/generate_images.py` once run locally with a valid image-generation API key (via `/justpreneur-finish`). No further creative decisions should be required at that point; only execution and QC of the generated output against this brief (especially the Section 9 accessibility checks and the Section 8 slide 2/3 angle-matching rule).
