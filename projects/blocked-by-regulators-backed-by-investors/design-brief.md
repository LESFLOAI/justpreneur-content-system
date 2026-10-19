# Visual Design Brief — "BLOCKED BY REGULATORS, BACKED BY THE SAME INVESTORS WHO NEVER LEFT"

**Status: IMAGES NOT YET GENERATED — DRAFT MODE, PROMPTS ONLY.** This is a design brief and prompt package only. No image-generation API key is available in this environment; `scripts/generate_images.py` has NOT been run. Actual image generation happens later, locally, via `/justpreneur-finish`.

Format: Instagram carousel, 8 slides, 1080 x 1350 px (portrait) each.
Story: Meta's reported $2B+ agreement to acquire Manus (Dec 2025), China's NDRC foreign-investment review and travel restriction on co-founders (early 2026), the NDRC order unwinding the deal (Apr 27, 2026), the original backers (Tencent, ZhenFund, HSG) reportedly buying the company back (~Aug 2026), Manus's return to independent operations as "Butterfly Effect," and its $500M+ raise (Oct 8, 2026).
Angle: jurisdiction risk is an unpriced term in every cross-border deal; the real moat is whether the team and backers keep the company alive and fundable after a deal collapses.

---

## IMPORTANT TONE/CONTENT GUARDRAIL (read before generating)

Per the assignment's tone guidance, visuals must stay neutral toward both Meta and the Chinese regulator — this is a structural deal-risk/founder-resilience lesson, not geopolitical commentary. No national flags, no political imagery, no literal depictions of government buildings or officials, no identifiable company logos (Meta, Tencent, Manus, Butterfly Effect are never rendered as real logos or wordmarks in the generated artwork — brand names appear only as designer-added text in layout, never baked into the AI image). All eight prompts below use abstract corporate metaphors only: a single evolving gold "deal line" motif (timeline/deal-path/signature stroke) that travels unbroken, meets a barrier, snaps, reconnects, stands alone, and multiplies into a stronger line across the set. This is the one visual device that must appear, in some state, on every slide — it is what makes the carousel read as one story instead of eight unrelated images. If any generated output drifts toward a recognizable real logo, a national flag, or a literal government building/official, QC/finish-mode must reject and regenerate. Flagging this to Quality Control as a confirmed risk to watch for.

---

## 1. Overall creative concept

A "deal line" carousel: one continuous abstract gold line — part timeline, part deal-path, part signature stroke — is the single visual thread that runs through all eight slides, changing state to mirror the story beat: unbroken and confident (cover), meeting a barrier (review opens), snapped in two (deal unwound), redrawn by multiple converging threads (backers return), standing alone on a fresh path (independent again), multiplying into one thick rising beam (new raise), reduced to a quiet elegant arc on a pull-quote card (the lesson), and opening into an inviting loop (the CTA). Nothing about the line, lighting, or composition reads as geopolitical — it is a deal/finance visual metaphor, not a map, border, or flag.

Tone: premium business-culture editorial (Bloomberg Businessweek / The Information / Puck register), deal-structure-breakdown energy — serious, confident, slightly cinematic — not a motivational quote template and not a news-alert graphic.

## 2. Composition and focal hierarchy

Every slide uses the same three-band system:
1. **Kicker/headline band** (top ~25–30%) — the date or headline, highest contrast, read first in a phone thumbnail.
2. **Image stage** (middle ~50%) — the generated artwork (the deal-line motif in its current state), always with a deliberate negative-space zone sized for whichever text block sits in or near it, so text is placed by the designer/layout step, not baked into the AI image.
3. **Body copy + brand footer band** (bottom ~20–25%) — the slide's approved copy line(s) plus the JustPreneur wordmark, consistent position, never competing with the headline for attention.

Focal hierarchy on every slide: (1) kicker/date or headline, (2) the one key fact the slide exists to deliver, (3) the deal-line image motif reinforcing that fact, (4) JustPreneur mark last.

## 3. Exact placement — headline, copy, imagery, branding

Shared grid (1080 x 1350, safe margins already applied — see Section 7):
- Kicker/date (Slides 2–6 only): top-left, baseline at y≈90px, small-caps gold, max width 500px.
- Headline (Slide 1 only): centered, starts at y≈110px, max width 920px, max 3 lines.
- Image stage: y≈380px to y≈1080px, full width with ~60px inset from each side so the deal-line artwork never touches the absolute edge.
- Body copy block: directly below the image stage, starting ≈y=1120px, warm white, left-aligned on data slides (2–6, 8), centered on the cover and the lesson pull-quote (1, 7).
- JustPreneur wordmark: bottom-center, baseline at y≈1290px, consistent size (~34–40px cap height), consistent gold or warm-white color across all 8 slides. No tagline, no handle, no slide number, no date stamp beyond the in-copy dates already approved.

Slide-by-slide text placement:
- **Slide 1 (Cover):** Headline "Blocked By Regulators, Backed By the Same Investors Who Never Left" centered in upper third, max 3 lines, bold caps or title case per final type test. Supporting line (the Dec 2025 Meta/Manus $2B+ deal copy) directly below, smaller, warm white, centered, max 3 lines. JustPreneur wordmark bottom-center.
- **Slide 2:** Kicker "EARLY 2026" top-left in gold, body copy (NDRC review opens; co-founders barred from leaving China, per Reuters/FT) left-aligned below the image, over the reserved negative-space band.
- **Slide 3:** Kicker "APRIL 27, 2026" top-left in gold, body copy (NDRC orders the deal unwound; foreign investment in Manus prohibited; acquisition over) left-aligned below the image.
- **Slide 4:** Kicker "~AUGUST 2026" top-left in gold, body copy (Tencent, ZhenFund, HSG reportedly buy the company back from Meta at ~$2B per 36Kr/Caixin; Benchmark didn't participate; Tencent becomes largest shareholder) left-aligned below the image.
- **Slide 5:** Kicker "WEEKS LATER" top-left in gold, body copy ("Manus announced a return to independent operations.") centered or left-aligned, kept short and spacious — this is the calmest, least-cluttered slide of the set.
- **Slide 6:** Kicker "OCTOBER 8, 2026" top-left in gold, body copy (Butterfly Effect raises $500M+ led by Boyu Capital and IDG Capital, with Tencent/HSG/ZhenFund returning; no valuation disclosed; Bloomberg/WSJ reported sources near $4B, unconfirmed by the company) left-aligned below the image — this is the densest slide, so keep the stacked lines short rather than one dense paragraph.
- **Slide 7 (Lesson):** No kicker (bookend with Slide 1). The two-sentence lesson ("A blocked deal isn't a dead company. Jurisdiction is an unpriced term in every cross-border deal — the real moat is whether your team and backers keep the business alive and fundable after the deal falls apart.") set as a large centered pull-quote over the quiet arc artwork.
- **Slide 8 (CTA):** The three CTA lines (Save this post. / Comment your own "deal almost fell apart" story. / Follow for more deal-structure breakdowns.) centered or stacked left, generous spacing, JustPreneur wordmark bottom-center as usual. No extra "swipe" prompt added beyond what's approved.

## 4. Typography direction

- **Headline (Slide 1) and kickers (Slides 2–6):** a bold, confident grotesque/sans in the Neue Haas Grotesk / Söhne Kräftig / Archivo Black family — no condensed or display-novelty fonts; this is a deal-breakdown post, not a lifestyle post. Kickers set in small-caps or all-caps, gold, letter-spaced slightly wide for an editorial-dateline feel.
- **Body/supporting copy:** clean humanist sans (Inter, Söhne, or similar), warm white, generous line height (1.3–1.4x), never smaller than ~34px effective size at this resolution so it reads on a phone thumbnail. Dense slides (4, 6) should break copy into short stacked lines rather than one dense justified paragraph.
- **Lesson pull-quote (Slide 7):** same body sans at a larger size and bolder weight, centered, with the single most important clause ("the real moat is whether your team and backers keep the business alive and fundable") optionally set slightly bolder or in gold for emphasis — but only one emphasis device per slide.
- **Numerals and money figures ($2B+, $500M+, $4B):** always set in the brand's bold sans, never in a decorative font — figures must be instantly legible and should not be visually downplayed, since they carry real narrative weight.
- **Hierarchy discipline:** maximum two typefaces across the whole carousel, maximum three weight/size steps per slide. No italics on headlines or kickers (reduces legibility at small sizes).

## 5. Color palette

Brand-default system, used consistently with a single restrained accent for the two "disruption" beats:

- Deep navy base: `#0B1220`
- Steel gray (secondary text, dividers, faint document/grid texture): `#8A94A6`
- Warm white (primary body text): `#F5F2EC`
- Energy gold (deal-line motif, kickers, numerals, JustPreneur wordmark): `#D4A24C`
- Restrained burnt-amber accent (used only at the break point on Slide 3, and faintly on Slide 2's barrier): `#C77B3F` — a muted, non-alarmist warning tone, never a bright red, to avoid any accidental political/alarm coding per the tone guardrail.

Palette progression across the carousel: Slides 1–2 are confident navy+gold with the amber accent just beginning to appear at the barrier; Slide 3 is the one moment amber is most present (the break); Slides 4–6 return fully to navy+gold as the line reconnects and strengthens; Slide 7 is the calmest, most minimal navy+gold+warm-white pull-quote card; Slide 8 closes on the same confident navy+gold as the cover, bookending the set.

## 6. Image treatment

Cinematic, premium, slightly desaturated except for the glowing gold deal-line itself (and the restrained amber accent on Slides 2–3). Soft studio-style directional light, fine grain, subtle lens bloom at points where the line glows brightest. No flat stock-photo lighting, no literal buildings, flags, officials, or company logos in any generated image — all such specificity is abstracted into the line/document/light metaphor, or added afterward as designer text. No readable fake signage or document text baked into any image — any wording needed is added in layout.

## 7. Instagram safe-margin instructions

For all 8 slides (1080 x 1350):
- Side margins: keep all text and critical graphic elements at least 80px from the left/right edges.
- Top margin: keep kicker/headline baseline no higher than 90–110px from the top edge; nothing critical in the top ~40px (feed-preview crop risk).
- Bottom margin: keep the JustPreneur wordmark and any text at least 100px from the bottom edge; nothing critical in the bottom ~60px.
- Center-safe zone: the primary message of each slide should read correctly even if a viewer only sees the middle 80% of the frame (per-slide feed thumbnails crop edges on some devices).

## 8. Slide-to-slide consistency rules

- Same 3-band grid (kicker/headline band, image stage, body+footer band) on all 8 slides — never swap to a different layout mid-carousel.
- Same JustPreneur wordmark size, color, and bottom-center position on all 8 slides.
- Same kicker treatment (gold, small-caps or caps, top-left) on Slides 2–6; Slides 1, 7, and 8 are the no-kicker slides (cover, lesson, CTA), an intentional bookend/pause rhythm.
- The deal-line motif must visibly carry over its state from the previous slide (unbroken → meets barrier → snapped → reconverging → standing alone → multiplying/rising → quiet arc → open loop) so the set reads as one continuous visual story, not eight random images.
- Color progression (confident navy/gold → amber accent rising → amber peak at the break → full return to navy/gold → calm pull-quote → confident navy/gold close) must read as one deliberate arc per Section 5.
- Fine grain and lens-bloom intensity held consistent across all 8 slides so the set feels like one shoot.
- No slide may introduce a new decorative motif (a new icon style, a new border treatment, a new accent color) that doesn't appear elsewhere in the set.

## 9. Accessibility and contrast check

- Primary body text (`#F5F2EC` warm white) on navy (`#0B1220`) background: contrast ratio ≈ 15:1 — passes WCAG AAA for all text sizes.
- Gold (`#D4A24C`) kickers/numerals on navy background: contrast ratio ≈ 7:1 — passes AA for normal text and AAA for large text; gold is restricted to short kickers, numerals, and the wordmark only (never full sentences) to stay safely in the large-text contrast band.
- Burnt-amber (`#C77B3F`) is used only as atmospheric glow/background accent on Slides 2–3, never as a text color — amber-on-dark text would sit near the edge of acceptable contrast at small sizes, so it's excluded from the typography palette entirely.
- Minimum effective text size kept large enough to read in a 3-inch-wide phone feed thumbnail (no text block should require pinch-zoom to read).
- No flashing/strobing effects implied in any prompt (static glow and bloom only) — avoids motion-sensitivity concerns if this is ever adapted to Reels.

## 10. Image-generation prompts (one per slide)

**IMAGES NOT YET GENERATED — DRAFT MODE, PROMPTS ONLY.** All 8 prompts below are saved to `projects/blocked-by-regulators-backed-by-investors/image-jobs.json` for later use by `scripts/generate_images.py` once an image-generation API key is available. `scripts/generate_images.py` was NOT run in this session.

**Slide 1 — Cover**
> 1080x1350 vertical premium business-editorial background. Deep navy (#0B1220) to charcoal gradient backdrop with a subtle soft studio light from upper left. A single thick, glowing energy-gold line (like a deal-flow path on a map or a signature stroke) sweeps diagonally from lower-left to upper-right across the frame, confident and unbroken, with a soft bloom/glow. Faint, barely visible abstract grid or ledger lines in steel gray in the background suggest financial/legal documents without any readable text. In the lower third, leave a large clean negative-space block (navy, minimal texture) for a bold headline and a smaller subhead beneath it. Top-left corner has quiet open space for a small wordmark. Mood: cinematic, high-stakes, premium Bloomberg/FT-style business editorial, serious but not corporate-stock-photo generic. No text, no logos, no numbers, no human figures, no flags, no national symbols, no government buildings. Avoid: illegible text, fake logos, duplicate people, malformed hands, clutter, small decorative icons, watermarks.

**Slide 2 — Early 2026 (review opens)**
> 1080x1350 vertical premium business-editorial background, same navy/steel/gold palette and lighting style as a cinematic deal-timeline series. The same thick gold line from the cover now travels forward but meets a translucent frosted-glass barrier or semi-transparent gate partway across the frame, its glow dimming and scattering into fine particles where it touches the barrier — a visual metaphor for a regulatory review, not a literal wall or building. Abstract overlapping document/paper silhouettes in steel gray sit behind the barrier, suggesting paperwork under review, with no readable text on them. Soft dramatic side lighting, slightly cooler and more tense than the cover. Large clean negative-space area in the lower half (navy, low texture) reserved for headline-style copy. No text, no logos, no flags, no national emblems, no government buildings, no human figures, no numbers. Avoid: illegible text, fake logos, duplicate people, malformed hands, clutter, small icons, watermarks.

**Slide 3 — April 27, 2026 (deal unwound)**
> 1080x1350 vertical premium business-editorial background, continuing the same navy/steel/gold cinematic palette. The thick gold line that was traveling forward is now snapped cleanly in two, the two severed ends drifting apart with fine glowing particles dispersing from the break point, like a torn financial contract rendered as light. A single muted amber-red accent glow (not a red alarm, a restrained burnt-amber tone) marks the break point to signal disruption without reading as alarmist or political. Abstract paper/document fragments in steel gray float faintly near the break, with no readable text. Generous negative-space block in the lower third for bold headline copy. Mood: a decisive, serious turning point, not chaotic. No text, no logos, no flags, no government imagery, no human figures, no numbers. Avoid: illegible text, fake logos, duplicate people, malformed hands, clutter, small icons, watermarks.

**Slide 4 — ~August 2026 (backers buy it back)**
> 1080x1350 vertical premium business-editorial background, same cinematic navy/steel/gold series style. The two severed ends of the gold line from the previous slide are now being drawn back together by several thinner converging gold threads arriving from different directions (suggesting multiple investors/backers reconnecting the deal), meeting at a single bright point of light where the lines rejoin. Faint abstract ledger-line or wireframe network texture in steel gray in the background. Warm, hopeful but still serious lighting, slightly brighter than Slide 3. Clear negative-space block in the lower third reserved for bold headline copy. No text, no logos, no flags, no national symbols, no human figures, no numbers. Avoid: illegible text, fake logos, duplicate people, malformed hands, clutter, small icons, watermarks.

**Slide 5 — Weeks later (independent again)**
> 1080x1350 vertical premium business-editorial background, same cinematic series style. The reunited gold line now stands alone as a single strong, steady beam of light cutting across a dark navy backdrop, no longer following the exact path of the earlier broken line — it now travels in a fresh, slightly upward direction, evoking a new independent start. A subtle warm dawn-like glow on the horizon line of the frame (soft gold-to-navy gradient at the bottom) reinforces a "new chapter" mood. Minimal, calm composition with lots of breathing room. Large clean negative-space block in the lower half for supporting copy. No text, no logos, no flags, no human figures, no numbers. Avoid: illegible text, fake logos, duplicate people, malformed hands, clutter, small icons, watermarks.

**Slide 6 — October 8, 2026 (the new raise)**
> 1080x1350 vertical premium business-editorial background, same cinematic navy/steel/gold series style. Several bright gold lines of varying thickness converge from the edges of the frame and merge into one bold, thick upward-sloping beam of light rising toward the upper right corner, conveying strong fresh capital and renewed momentum. Soft lens bloom at the point of convergence. Faint abstract growth-chart grid lines in steel gray in the far background, extremely subtle, no numbers or labels. Confident, energetic but still premium and restrained lighting. Large negative-space block in the lower third for bold headline copy. No text, no logos, no flags, no human figures, no numbers. Avoid: illegible text, fake logos, duplicate people, malformed hands, clutter, small icons, watermarks.

**Slide 7 — Lesson (pull-quote card)**
> 1080x1350 vertical premium quote-card background in deep navy with a warm white soft vignette toward the center, evoking a modern business-editorial pull-quote slide (similar to a premium newsletter or Bloomberg Businessweek opinion page). A single thin, elegant energy-gold line arcs gently across the upper third of the frame like a horizon or minimal graph line, then fades into soft light — restrained and sophisticated, not literal. Extremely generous negative space across the full middle and lower two-thirds of the frame for a large pull-quote headline and short supporting line. No background clutter, no texture overload. No text, no logos, no flags, no human figures, no numbers, no icons. Avoid: illegible text, fake logos, duplicate people, malformed hands, clutter, small icons, watermarks.

**Slide 8 — CTA**
> 1080x1350 vertical premium business-editorial closing background, same navy/steel/gold series style as the rest of the carousel. Deep navy background with a single bold energy-gold line forming a soft, abstract open-ended loop or upward arc in the upper portion of the frame, suggesting continuation and invitation to engage rather than a closed ending. Clean, warm, inviting lighting. Large, clear negative-space block across the center and lower half of the frame reserved for bold call-to-action text and the JustPreneur wordmark. No text, no logos, no flags, no human figures, no numbers, no icons. Avoid: illegible text, fake logos, duplicate people, malformed hands, clutter, small icons, watermarks.

## 11. Layout/text-overlay instructions (applied after image generation)

Applies uniformly: all headline/kicker/body text is added as a true text layer in the design tool (not baked into the AI image), using the typography and placement rules in Sections 3–4, positioned inside the pre-reserved negative-space zones described in each image prompt above, and respecting the safe margins in Section 7.

- **Slide 1:** Add centered headline "Blocked By Regulators, Backed By the Same Investors Who Never Left" in the upper-third negative space, then the Dec 2025 Meta/Manus deal copy (full Slide 1 approved copy) directly below in smaller warm-white type, centered. JustPreneur wordmark bottom-center.
- **Slide 2:** Add gold kicker "EARLY 2026" top-left, then the full Slide 2 approved copy (NDRC review; co-founders barred from leaving China, per Reuters/FT) left-aligned into the reserved lower-half space. JustPreneur wordmark bottom-center.
- **Slide 3:** Add gold kicker "APRIL 27, 2026" top-left, then the full Slide 3 approved copy (NDRC orders the deal unwound; foreign investment prohibited; acquisition over) left-aligned into the reserved lower-third space. JustPreneur wordmark bottom-center.
- **Slide 4:** Add gold kicker "~AUGUST 2026" top-left, then the full Slide 4 approved copy (Tencent/ZhenFund/HSG buy back at ~$2B per 36Kr/Caixin; Benchmark didn't participate; Tencent becomes largest shareholder), broken into short stacked lines rather than one dense paragraph, inside the reserved lower-third band. JustPreneur wordmark bottom-center.
- **Slide 5:** Add kicker "WEEKS LATER" top-left (or omit and center the single line for maximum breathing room — designer's call at layout time), then the full Slide 5 approved copy ("In the weeks that followed, Manus announced a return to independent operations.") inside the reserved lower-half space. JustPreneur wordmark bottom-center.
- **Slide 6:** Add gold kicker "OCTOBER 8, 2026" top-left, then the full Slide 6 approved copy ($500M+ raise led by Boyu Capital and IDG Capital; Tencent/HSG/ZhenFund returning; no valuation disclosed; Bloomberg/WSJ reported ~$4B target, unconfirmed), broken into short stacked lines, inside the reserved lower-third band. JustPreneur wordmark bottom-center.
- **Slide 7:** No kicker. Center the full two-sentence lesson copy ("A blocked deal isn't a dead company. Jurisdiction is an unpriced term in every cross-border deal — the real moat is whether your team and backers keep the business alive and fundable after the deal falls apart.") as a large pull-quote in the reserved middle/lower negative space. JustPreneur wordmark bottom-center.
- **Slide 8:** No kicker. Stack the three CTA lines ("Save this post." / "Comment your own 'deal almost fell apart' story." / "Follow for more deal-structure breakdowns.") centered or left-stacked in the reserved center/lower negative space. JustPreneur wordmark bottom-center. Do not add any extra "swipe" prompt text beyond what's approved.

Caption, hashtags, and tags are finalized separately by the copywriter and are out of scope for this visual pass.
