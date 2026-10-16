# Visual Design Brief — "THE SHOW ENDED. THE BUSINESS DIDN'T."

**Status: IMAGES NOT YET GENERATED — DRAFT MODE.** This is a design brief and prompt package only. No image-generation API key is available in this environment; `scripts/generate_images.py` has NOT been run. Actual image generation happens later, locally, via `/justpreneur-finish`.

Format: Instagram carousel, 7 slides, 1080 x 1350 px (portrait) each.
Story: Stranger Things series finale (Dec 31, 2025) vs. Bucket Listers' "Netflix's Stranger Things: The Diner" pop-up announcement (Oct 7, 2026), waitlist-only, no venue/date/price confirmed.
Angle: the fandom an ended show built is a monetizable asset long after the content stops.

---

## IMPORTANT LEGAL/BRAND GUARDRAIL (read before generating)

This post discusses Stranger Things and Netflix's branded pop-up, but JustPreneur has no license to reproduce Netflix's or Stranger Things' actual logos, title typography, character likenesses, actors' faces, or the real "Upside Down" set design. All seven prompts below are written to evoke the *aesthetic mood* (dark, red-lit, fog, retro-80s neon, decayed Americana) generically — NOT to recreate any copyrighted frame, logo, poster, or identifiable character. No prompt should be altered to add "Stranger Things logo," "Netflix N," "Eleven," "Hawkins," or any named character/actor. If a generation output drifts toward a recognizable likeness of the real show or real Netflix branding, QC/finish-mode must reject and regenerate. This is a confirmed risk to flag to Quality Control.

---

## 1. Overall creative concept

A "portal" carousel: each slide is a lit doorway between two states — the finished story (cold, closing, fading neon) and the still-open business (warm gold signal cutting through red fog). Visually this plays out as a recurring **red-fog-to-gold-light gradient motif**: the Upside Down palette (blood red, near-black, static/fog) dominates the "ending" beats (Slides 1–2), gives way to warm neon diner energy for the "new chapter" beats (Slides 3–5), and resolves into the brand's energy-gold for the strategic payoff (Slides 6–7). This mirrors the copy's own arc — ending, surprise, specifics, uncertainty, lesson, challenge — without ever trying to pass as official Stranger Things or Netflix artwork.

Tone: premium business-culture editorial (think Puck, The Information, Morning Brew's bolder cousin), not a fan-art meme page and not a generic "hustle quote" template.

## 2. Composition and focal hierarchy

Every slide uses the same three-band system:
1. **Headline/kicker band** (top ~30%) — largest, highest-contrast text. This is read first on a phone thumbnail.
2. **Image stage** (middle ~55%) — the generated artwork, always with a deliberate negative-space zone sized for whichever text block sits in or near it (so text is placed by the designer/layout step, not baked into the AI image).
3. **Brand footer band** (bottom ~15%) — JustPreneur wordmark lockup, consistent position, never competing with the headline for attention.

Focal hierarchy on every slide: (1) headline, (2) the one key data point or phrase that slide exists to deliver, (3) supporting image mood, (4) JustPreneur mark last. No slide should ask the eye to do more than look at two things.

## 3. Exact placement — headline, copy, imagery, branding

Shared grid (1080 x 1350, safe margins already applied — see Section 7):
- Headline/kicker: starts at y≈90px, max width 920px, centered or left-aligned per slide (cover is centered, data slides are left-aligned for an editorial feel).
- Supporting line (date stamp, subhead, or body copy): directly below headline block, 24–32px gap, warm white or muted steel-gray.
- Image stage: y≈420px to y≈1140px, full width with ~60px inset from each side so artwork never touches the absolute edge.
- JustPreneur wordmark: bottom-center, baseline at y≈1290px, consistent size (~34–40px cap height) and consistent warm-white or gold color across all 7 slides. No tagline, no handle, no slide number.

Slide-by-slide text placement:
- **Slide 1 (Cover):** Headline "THE SHOW ENDED. THE BUSINESS DIDN'T." centered in upper third, max 2 lines. Subhead "Stranger Things wrapped four months ago. A new chapter just opened." directly below, smaller, one line if possible (wrap to 2 max). JustPreneur wordmark bottom-center.
- **Slide 2:** Small kicker "DEC 31, 2025" top-left in gold, headline/body "Stranger Things airs its series finale after five seasons. The story is officially over." below it, left-aligned over the image's left-side negative space.
- **Slide 3:** Kicker "OCT 7, 2026" top-left in gold, body text (the Bucket Listers/Diner announcement) left-aligned, image occupies right two-thirds with negative space pocket on the left for the text block.
- **Slide 4:** Kicker "WHAT'S CONFIRMED" top-left, then the five confirmed facts rendered as a short checklist/tag-style stack (not paragraph) over a clear negative-space band in the lower-middle of the image.
- **Slide 5:** Kicker "WHAT'S NOT CONFIRMED (YET)" top-left, three short "No ___" lines plus the waitlist line and closing insight line, stacked, over a fogged-out/obscured negative-space zone.
- **Slide 6:** Kicker "THE REAL LESSON" top-left (now switches to gold-forward, no more red), the two-sentence lesson centered over a calmer, more premium image.
- **Slide 7 (CTA):** The question, large, centered, with generous breathing room; this is the slide most likely to be screenshotted, so keep it the cleanest of all seven. JustPreneur wordmark bottom-center as usual — no extra "swipe/share/comment" prompts added (none were requested in copy).

## 4. Typography direction

- **Headlines/kickers:** a bold, slightly condensed grotesque/sans (e.g., something in the Neue Haas/Druk/Archivo Black family) for the editorial-premium beats (Slides 1, 4–7), switched to a retro-digital/VHS-tracking-flavored display face ONLY for the two "finale/ending" kickers (Slides 2–3 date stamps) to nod at the 80s aesthetic without becoming a costume-party font. Never use a horror/dripping/distressed font for body copy — legibility first.
- **Body/supporting copy:** clean humanist sans (e.g., Inter, Söhne, or similar), warm white, generous line height (1.3–1.4x), never smaller than ~34px effective size at this resolution so it reads on a phone thumbnail.
- **Numerals (dates, $10, counts):** always set in the brand's bold sans, never in a decorative font — numbers must be instantly legible.
- **Hierarchy discipline:** maximum two typefaces per slide, maximum three weight/size steps. No italics on headlines (reduces legibility at small sizes).

## 5. Color palette

Blended "Upside Down meets JustPreneur" system — red/neon dominant early, resolving to brand gold/navy by the end:

- Near-black navy base: `#0A0E14`
- Blood/Upside Down red (accent, fog, glow): `#8A1220` with a brighter neon highlight `#C8102E`
- Steel gray (secondary text, dividers): `#6B7280`
- Warm white (primary body text): `#F5F1E8`
- Energy gold (brand accent, CTA emphasis, kickers, JustPreneur wordmark): `#D4AF37`
- Retro neon teal (used sparingly, only in Slide 3's diner-sign glow, to sell "80s neon" without leaning only on red): `#2DD4BF` at low opacity, background accent only — never on text.

Palette progression across the carousel: Slides 1–2 lean navy+red (ending), Slide 3 introduces neon teal+red (the diner reveal, most "retro-80s" slide), Slides 4–5 stay red/navy with fog (uncertainty), Slides 6–7 shift to navy+gold with red fully receded (the lesson/payoff — calmer, more premium, less "horror").

## 6. Image treatment

Cinematic, moody, slightly desaturated except for practical neon/glow light sources (red, and teal only on Slide 3). Heavy use of atmospheric fog/haze and film grain for texture — this sells "premium editorial" rather than "stock photo." No flat studio lighting. Every image must be generic/conceptual: invented retro diners, invented marquees, invented corkboards — never a real, identifiable storefront, real address signage, or real city skyline, since no venue exists yet. No readable fake signage text (blank or abstractly-lit signs only — any wording needed is added in layout, not baked into the image).

## 7. Instagram safe-margin instructions

For all 7 slides (1080 x 1350):
- Side margins: keep all text and critical graphic elements at least 80px from the left/right edges.
- Top margin: keep headline/kicker baseline no higher than 90px from the top edge; nothing critical in the top ~40px (feed-preview crop risk).
- Bottom margin: keep the JustPreneur wordmark and any text at least 100px from the bottom edge; nothing critical in the bottom ~60px.
- Center-safe zone: the primary message of each slide should read correctly even if a viewer only sees the middle 80% of the frame (per-slide feed thumbnails crop edges on some devices).

## 8. Slide-to-slide consistency rules

- Same 3-band grid (headline/kicker band, image stage, footer band) on all 7 slides — never swap to a different layout mid-carousel.
- Same JustPreneur wordmark size, color, and bottom-center position on all 7 slides.
- Same kicker treatment (gold, small-caps or caps, top-left) on Slides 2–6; Slides 1 and 7 are the only centered/no-kicker slides (cover and CTA), which is intentional bookending.
- Color progression (red/navy → teal accent → red/navy fog → navy/gold) must read as one deliberate arc, not random variation — see Section 5.
- Fog/haze and grain texture present on every slide at consistent intensity so the set feels like one shoot, not seven unrelated images.
- No slide may introduce a new decorative motif (e.g., a new icon style, a new border treatment) that doesn't appear elsewhere in the set.

## 9. Accessibility and contrast check

- Primary body text (`#F5F1E8` warm white) on near-black navy (`#0A0E14`) background: contrast ratio ≈ 16:1 — passes WCAG AAA for all text sizes.
- Gold (`#D4AF37`) kickers/numerals on navy background: contrast ratio ≈ 7.5:1 — passes AA for normal text and AAA for large text; gold is restricted to short kicker labels and numerals only (never full sentences) to stay safely in the large-text contrast band.
- Red (`#C8102E`) is used only as atmospheric glow/background accent, never as a text color — red-on-dark text would fail contrast and legibility at small sizes, so it's excluded from the typography palette entirely.
- Minimum effective text size kept large enough to read in a 3-inch-wide phone feed thumbnail (no text block should require pinch-zoom to read).
- No flashing/strobing effects implied in any prompt (static glow and fog only) — avoids motion-sensitivity concerns if this is ever adapted to Reels.

## 10. Image-generation prompts (one per slide)

**IMAGES NOT YET GENERATED — DRAFT MODE.** All 7 prompts below are saved to `projects/the-show-ended-the-business-didnt/image-jobs.json` for later use by `scripts/generate_images.py` once an image-generation API key is available.

**Slide 1 — Cover**
> 1080x1350 vertical. A moody, cinematic wide shot of a generic abandoned small-town movie theater exterior at night, lit by pulsing red neon glow and thick atmospheric fog drifting across cracked pavement. The marquee is dark and blank (no readable text, no logos). Retro-80s neon accent lighting along the theater's edges, faint electrical flicker. Deep navy sky, red practical light sources only, no people, no characters, no readable signage, no text. Negative space in the upper third of the frame (clear dark navy/red gradient sky, no busy detail) reserved for a bold headline to be added later in layout. Brand palette: near-black navy #0A0E14, blood red #8A1220/#C8102E glow, warm white highlights. Cinematic, slightly desaturated, fine film grain. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter, no small decorative elements, no real brand names or show title treatments.

**Slide 2 — Dec 31, 2025 (the finale)**
> 1080x1350 vertical. A dark, generic old television or cinema screen glowing with red static/scan-line light, sitting alone in a dim navy-toned room, fog drifting at floor level. The screen shows only abstract red glow and soft static texture — no readable text, no logos, no characters, no faces. A single warm ember-like light source suggests a "closing curtain" mood. Composition leaves a clear, uncluttered negative-space band in the left third of the frame for a kicker label and a short paragraph of text to be added in layout. Brand palette: navy #0A0E14, red glow #C8102E, warm white rim light. Cinematic, moody, fine grain, no flashing/strobe. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter, no small decorative elements.

**Slide 3 — Oct 7, 2026 (the diner announcement)**
> 1080x1350 vertical. A generic retro-1980s American diner interior at night, red and teal neon light spilling across empty vinyl booths and a checkerboard floor, soft fog/haze near the ceiling, a jukebox silhouette in the background (unbranded, no readable text or logos on it). Warm practical neon glow mixes red and teal for a "portal between two worlds" feel. No people, no characters, no readable signage, no real restaurant branding. Composition keeps the left third of the frame open and uncluttered (soft dark negative space) for a kicker and short paragraph to be added in layout. Brand palette: navy #0A0E14 shadows, red #C8102E and teal #2DD4BF neon accents, warm white highlights. Cinematic, slightly desaturated except neon, fine grain. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter, no small decorative elements.

**Slide 4 — What's confirmed**
> 1080x1350 vertical. A top-down or three-quarter view of a stylized retro diner tray or tabletop with a ticket stub, a small food tray, and a drink glass arranged simply on a dark surface, lit by warm red-tinted practical light with a soft neon rim glow. All objects are generic/unbranded — the ticket stub and any surfaces are blank, no readable text, no logos, no price printed on anything. Fog/haze kept minimal here for clarity since this slide needs to feel organized and "confirmed," not murky. Composition leaves a clear, uncluttered horizontal negative-space band in the lower half of the frame for a short checklist of facts to be added in layout. Brand palette: navy #0A0E14, red accent #8A1220, warm white tabletop highlights. Cinematic but clean, minimal fog, fine grain. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter, no small decorative elements.

**Slide 5 — What's not confirmed (yet)**
> 1080x1350 vertical. A dim, generic blank storefront or marquee silhouette almost entirely obscured by thick drifting red-tinted fog, so that its details are deliberately indistinct and unreadable — no address, no signage, no logos, no legible text of any kind, intentionally mysterious and unresolved. A single faint warm light suggests presence without revealing form. Composition keeps the upper two-thirds relatively open and foggy (soft negative space) for a kicker and several short stacked lines of text to be added in layout. Brand palette: navy #0A0E14, deep red fog #8A1220, muted steel-gray #6B7280 haze. Cinematic, heavy atmospheric fog, fine grain. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter, no small decorative elements.

**Slide 6 — The real lesson**
> 1080x1350 vertical. A close, warm-toned shot of a corkboard with fine red string connecting several small blank photo-card silhouettes (anonymous, faceless, abstract card shapes — no real faces, no celebrities, no identifiable people), lit softly with the red fog receded and a warm gold practical light now dominant, suggesting a network or community made visible. No readable text on any card. Composition leaves a clear open negative-space zone in the upper third and lower third for a kicker and a two-line statement to be added in layout. Brand palette shifts here: navy #0A0E14 base, warm gold #D4AF37 key light, muted red #8A1220 only as a faint residual accent. Cinematic, calmer and more premium than earlier slides, fine grain, no fog murk. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter, no small decorative elements.

**Slide 7 — CTA**
> 1080x1350 vertical. A single generic open doorway glowing with warm gold light spilling through it into a dark navy room, the last trace of red fog curling near the floor at the threshold but not dominating the frame — an inviting, forward-looking "step through" mood rather than an ominous one. No people, no characters, no readable text or signage anywhere in the frame. Composition is clean and uncluttered, with generous open negative space centered in the frame (above, through, and below the doorway) for a single bold centered question to be added in layout. Brand palette: navy #0A0E14, warm gold #D4AF37 glow, faint red #8A1220 residual accent only at the floor. Cinematic, calm, premium, fine grain, no flashing light. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter, no small decorative elements.

## 11. Layout/text-overlay instructions (applied after image generation)

Applies uniformly: all headline/kicker/body text is added as a true text layer in the design tool (not baked into the AI image), using the typography and placement rules in Sections 3–4, positioned inside the pre-reserved negative-space zones described in each image prompt above, and respecting the safe margins in Section 7.

- **Slide 1:** Add centered headline "THE SHOW ENDED. THE BUSINESS DIDN'T." in the upper-third negative space, subhead "Stranger Things wrapped four months ago. A new chapter just opened." directly below in smaller warm-white type. Add JustPreneur wordmark bottom-center.
- **Slide 2:** Add gold kicker "DEC 31, 2025" top-left, then the body line "Stranger Things airs its series finale after five seasons. The story is officially over." in warm white directly beneath, left-aligned into the reserved left-third space. JustPreneur wordmark bottom-center.
- **Slide 3:** Add gold kicker "OCT 7, 2026" top-left, then the announcement body copy (Bucket Listers / "Netflix's Stranger Things: The Diner" / Manhattan this fall / bookings into early 2027) left-aligned into the reserved left-third space. JustPreneur wordmark bottom-center.
- **Slide 4:** Add kicker "WHAT'S CONFIRMED" top-left in gold, then render the five confirmed facts as short stacked checklist-style lines (not a dense paragraph) inside the reserved lower-half band. JustPreneur wordmark bottom-center.
- **Slide 5:** Add kicker "WHAT'S NOT CONFIRMED (YET)" top-left in gold, then stack the "No venue address / No opening date / No ticket price / Just a waitlist, open now at bucketlisters.com" lines, followed by the closing insight sentence, inside the reserved foggy negative-space zone. JustPreneur wordmark bottom-center.
- **Slide 6:** Add kicker "THE REAL LESSON" top-left in gold, then center the two-sentence lesson copy in the reserved upper/lower negative space around the corkboard image. JustPreneur wordmark bottom-center.
- **Slide 7:** Add the CTA question, large and centered, in the reserved open negative space around the doorway. No kicker on this slide (intentional bookend with Slide 1). JustPreneur wordmark bottom-center. Do not add any extra "swipe/comment/share" prompt text — none was in the approved copy.

Caption, hashtags, and tags are finalized separately by the copywriter and are out of scope for this visual pass.
