# JustPreneur — Design Brief
**Project:** symone-second-brand-same-builder
**Format:** Instagram Carousel, 7 slides, 1080 x 1350 px (portrait)
**Angle:** Second Brand, Same Builder (DeVonn Francis / Yardy / Symone at MoMA PS1)
**Status:** DRAFT — image generation NOT run in this environment (no API key available). Design brief and prompts only.

---

## 1. Overall Creative Concept

This story sits at the intersection of business strategy and food/culture media — closer to a *Bon Appétit x Fast Company* editorial spread than a standard "founder tip" carousel. The visual language should feel like a premium magazine feature on a chef-entrepreneur, not a motivational-quote template.

Core concept: **"One Builder, Two Brands"** rendered as a visual study in duality — warm Caribbean color/texture language for Yardy, cooler French-African café language for Symone, resolving into a single confident JustPreneur editorial frame. Slide 4 is the structural core of the whole carousel and gets the most deliberate split-panel treatment.

Because of fact-verification constraints, no slide may depict:
- A real, identifiable likeness of DeVonn Francis (no fabricated "photo" of a named real person) — abstract/illustrative human silhouettes only, never a specific rendered face purporting to be him.
- Real MoMA PS1 architecture, signage, or logos as if photographed — use generic/stylized schoolhouse-reuse architectural renderings (arched windows, brick, terrace) that evoke the described details without claiming to document the real building.
- Any specific calendar date — only "early October 2026" as text, never a date graphic/calendar icon.
- Any lease/contract/rent-free visual metaphor — no handshake-over-paperwork, no "$0 rent" badge, no contract/signature imagery tied to the Slide 6 secondary note.

---

## 2. Typography Direction

- **Headlines:** Bold, tall editorial serif or serif-adjacent display face (e.g., a Canela/Freight Display/Druk-style weight) — confident, slightly condensed, in warm white or cream. This is what separates the post from generic sans-only motivational templates.
- **Subheads / section headers (e.g., "The Brand He Already Built"):** Sans-serif, all-caps or small-caps, medium tracking, gold or brass accent color, used as a short editorial "kicker" above or below the headline.
- **Body copy:** Clean grotesque sans (e.g., Inter/Neue Haas style), warm white on dark panels or charcoal on warm-white panels, generous line height for mobile legibility. Max ~40-45 characters per line at the sizes used.
- **Brand lockup:** "JUSTPRENEUR" wordmark, small-caps or all-caps sans, letterspaced, gold or warm-white, consistently placed top-left on every slide (see margin spec below). Never tiny — must read clearly at thumbnail size.
- No decorative script fonts, no handwriting fonts, no more than 2 type families total (1 display/serif for headlines + 1 sans for everything else).

---

## 3. Color Palette

Adjusted from brand default (navy/steel/warm white/gold) toward a culinary-editorial direction, per brand guidance to shift for a specific cultural story. Gold stays as the connective accent across both brand "sides."

**Shared JustPreneur frame:**
- Charcoal / deep espresso black — `#1C1712`
- Warm white / cream — `#F5EFE4`
- Energy gold / brass — `#C8A24B`

**Yardy side-accent (Caribbean culinary studio):**
- Terracotta / warm clay — `#B2512D`
- Deep forest green — `#2E4A33`
- Citrus/mango accent (used sparingly, e.g., small rule lines) — `#E0A23B`

**Symone side-accent (French-African café / museum):**
- Steel gray / stone — `#8A8A82`
- Deep navy-charcoal — `#20242B`
- Soft terracotta-cream (shared bridge tone) — `#E8D9C3`

Rule: every slide keeps the shared charcoal + cream + gold frame; the terracotta (Yardy) vs. steel-gray/navy (Symone) accents are only introduced where the copy is explicitly about one brand or the other (Slides 2, 3, and especially the two columns of Slide 4). Slides 1, 5, 7 stay on the neutral charcoal/cream/gold frame since they're carousel-wide, not brand-specific.

---

## 4. Image Treatment

- All imagery is abstract, illustrative, or stylized-editorial — never photo-real claims of real people or the real PS1 building.
- Treat generated art with a consistent "premium editorial" post-process: slightly desaturated, warm-toned grade, soft grain/matte finish (like a print magazine plate), subtle vignette to protect text zones.
- No stock-photo gloss, no overly saturated "AI render" look, no 3D-render plastic sheen.
- Negative space is mandatory in every background image — generation prompts below specify where text will sit so nothing competes with copy.
- Food/ingredient/architecture elements should look tactile and editorial (shot-on-film quality, shallow depth cues, natural materials) rather than literal product photography of named dishes claiming to be the real restaurant.

---

## 5. Instagram Safe-Margin Instructions

- Canvas: 1080 x 1350 px for all 7 slides (consistent carousel format).
- Keep all text within a **safe zone of 80px margin on all sides** (so live text area is roughly 920 x 1190 px), to avoid UI crop and comment-overlay clipping in feed/grid previews.
- Top 100px and bottom 120px are treated as extra-protected zones (profile picture/caption overlap in feed, "..." overflow, and swipe-dot overlap) — keep headline baseline and CTA text clear of these bands; background art can bleed full-frame.
- JustPreneur wordmark sits inside the top-left safe margin, never closer than 60px to any edge.
- Minimum body text size equivalent to ~34-40px at 1080 width (scales to clearly legible at typical phone viewing size); headline equivalent to ~70-90px.

---

## 6. Slide-to-Slide Consistency Rules

1. Every slide uses the same 1080x1350 canvas, same safe margins, same JustPreneur wordmark position (top-left) and same gold hairline rule under the kicker/header.
2. Slide number is **not** shown anywhere (per brand instruction — no slide counters).
3. Headline typography scale and weight stays identical slide to slide; only color accent (terracotta vs. steel-gray) shifts to signal "whose story" a slide is about.
4. Background art treatment (grain, desaturation, vignette) is identical across all 7 images so the carousel reads as one coherent set, not 7 unrelated renders.
5. Slide 4 is the only slide with a hard vertical split-panel composition — this visual break is intentional and should feel like the "reveal" slide of the set.
6. Gold is the only color that appears on every single slide (hairline rules, kicker text, or accent dot) — it's the visual thread tying the carousel together.

---

## 7. Accessibility and Contrast Check

- Headline text (cream `#F5EFE4` or warm white) must sit only on charcoal/espresso (`#1C1712`) or deep navy (`#20242B`) backgrounds, or on a scrim/gradient overlay with at least 60% opacity darkening before text is placed over any photographic/illustrative art. Target contrast ratio ≥ 4.5:1 for body text, ≥ 3:1 for large display headline text (WCAG AA for large text).
- Gold (`#C8A24B`) is used only for short kicker words / hairlines / accent — never for full paragraphs of body copy, since gold-on-cream or gold-on-light backgrounds fails contrast at body-text sizes.
- Slide 4 two-column panels: left (terracotta-tinted dark panel) and right (steel-gray/navy-tinted dark panel) both get a darkening scrim before white/cream text is placed, so contrast stays consistent even though the two panels use different accent hues.
- No text is ever placed directly over busy, high-detail image areas without a scrim — every text block in the layout notes below specifies its scrim/panel.
- Avoid color pairings relying on red/green distinction alone (none used here; palette is brass/terracotta/navy/cream, which is colorblind-safe for this purpose).

---

## 8. Per-Slide Layout Notes

### Slide 1 — Cover / Hook
- **Headline:** "Why DeVonn Francis Didn't Just Rename Yardy" — large serif, cream, centered-left, occupying the middle third of the frame.
- **Subhead:** "A builder with one brand already working just launched a second one." — sans, smaller, directly beneath headline, cream at 85% opacity.
- **Imagery:** Full-bleed abstract editorial background — warm culinary-studio-meets-museum-café mood (see prompt below), with a vertical gradient scrim (charcoal, ~65% opacity) rising from bottom two-thirds so headline sits on dark ground.
- **Branding:** "JUSTPRENEUR" wordmark top-left, gold hairline rule beneath the subhead.
- **Focal hierarchy:** Headline > subhead > wordmark > background art.

### Slide 2 — Yardy Context
- **Kicker:** "THE BRAND HE ALREADY BUILT" — gold small-caps, top of text block.
- **Header:** "The Brand He Already Built" (can be same as kicker enlarged, or kicker + a shorter visual header — keep copy as approved, no new text invented).
- **Body:** Full approved sentence in cream sans, left-aligned, in lower two-thirds of frame over a charcoal-terracotta scrim panel.
- **Imagery:** Warm, terracotta-toned abstract culinary-studio visual (spices, citrus, warm plating textures) filling top half / bleeding behind text panel — no people, no identifiable chef.
- **Accent:** Terracotta gold-hairline divider between header and body.

### Slide 3 — Symone Intro
- **Kicker:** "THEN HE BUILT SOMETHING ELSE"
- **Body:** Approved sentence, including the "early October 2026" / niece-naming detail verbatim — cream sans over a navy-steel scrim panel, lower two-thirds.
- **Imagery:** Abstract stylized museum-café/terrace-dining architectural rendering — arched schoolhouse-style windows, brick texture, outdoor terrace furniture silhouettes, soft French-café color accents (cream, sage, brass) — generic/stylized, not a photographed real building.
- **Accent:** Steel-gray/navy hairline divider (signals "Symone side" visually, contrasting Slide 2's terracotta divider).

### Slide 4 — Side-by-Side Brand Comparison (STRUCTURAL CORE)
This slide carries the thesis of the whole carousel and gets the most deliberate layout:
- **Overall composition:** Hard vertical split down the center of the 1080px-wide canvas — left panel = YARDY (540px wide), right panel = SYMONE (540px wide). A thin gold vertical rule (4-6px) runs the full height of the canvas at the center seam, the one unifying element between the two halves.
- **Top band (shared, spans both panels):** Header "One Builder. Two Brands." centered across the full width, cream serif, sitting on a charcoal strip ~180px tall at the very top (within safe margins) — this is the only element that bridges both columns.
- **Left panel (YARDY):**
  - Background: terracotta-toned abstract texture/art, darkened with charcoal scrim for text legibility.
  - Panel label "YARDY" in bold gold small-caps near top of panel.
  - Three stacked bullet lines below, cream sans: "Culinary studio" / "Jamaican/Caribbean roots" / "Est. 2017" — each with a small gold dash/bullet marker, generous line spacing.
- **Right panel (SYMONE):**
  - Background: steel-gray/navy-toned abstract architectural texture, same charcoal scrim treatment for consistency.
  - Panel label "SYMONE" in bold gold small-caps near top of panel, same size/weight/position as "YARDY" label for visual parity.
  - Three stacked bullet lines, cream sans: "Standalone café" / "French-African menu, Jamaican/Caribbean influence" / "Opening window: early October 2026" — same bullet style as left panel.
- **Alignment rule:** Every text line in the left panel has a mirrored vertical position in the right panel (label-to-label, bullet-1-to-bullet-1, etc.) so the eye reads the comparison as a true parallel grid, not two mismatched halves.
- **No imagery of people or real architecture** in either panel — both are abstract textures/patterns only, since this slide is pure comparison, not scene-setting.

### Slide 5 — The Positioning Lesson
- **Kicker:** "THE DECISION POINT"
- **Body:** Approved paragraph, cream sans, centered text block in lower half over charcoal scrim.
- **Imagery:** Abstract visual metaphor — a single path/line diverging into two paths (rendered as abstract light-trails, architectural lines, or plating-knife lines — not literal road/fork-in-road cliché, not a literal fork utensil pun) rendered in neutral charcoal/gold/cream palette (no terracotta or steel-specific accent — this slide is brand-neutral, about the decision itself).
- **Accent:** Gold hairline only (no color-side-taking on this slide).

### Slide 6 — Supporting Proof Points
- **Header:** "What Makes Symone Its Own Thing" — cream serif, upper third.
- **Body:** Primary approved sentence (menu items + design studio + terrace + museum-admission detail), cream sans, mid-frame over scrim.
- **Secondary note:** Rendered smaller and in italic or lighter-weight sans, clearly visually subordinate (smaller size, lower opacity ~75%) directly beneath the primary body copy, separated by a thin gold rule — so it reads as supporting context, not an equal claim, and carries no deal/lease graphic treatment whatsoever (text only, no icon).
- **Imagery:** Abstract editorial flatlay-style composition suggesting pastries/coffee/patties/soft-serve textures and a hint of schoolhouse-brick/terrace architectural texture blended at the edges — generic, stylized, no literal branded cup/packaging, no readable menu board.
- **Accent:** Mixed terracotta + steel-gray hairlines (this slide bridges both brand stories, so both accent hues appear in small doses, e.g., alternating bullet dashes).

### Slide 7 — Takeaway / CTA
- **Header:** "The Takeaway" — cream serif, upper-middle.
- **Body:** Approved takeaway paragraph, cream sans, centered.
- **CTA:** "Which would you do — extend your brand, or start a new one? Drop your answer below." — set apart visually (slightly larger, gold color or boxed in a thin gold-outlined rule) as the clear call-to-action, positioned in the lower safe-margin zone but still above the 120px bottom protected band.
- **Imagery:** Neutral charcoal/cream abstract background — minimal, calm, closing-note mood (e.g., soft gold light gradient, no literal objects) so the CTA text is the clear focal point with zero competing visual noise.
- **Branding:** JustPreneur wordmark top-left as on every slide; this is the natural "close" slide so the wordmark can optionally repeat slightly larger/centered at the very bottom within the safe zone — optional treatment, not required.

---

## 9. Open Flags for Downstream QC

- Confirm no slide's body/caption text has been altered from the approved copy block in `content-copy.md` — this brief only adds layout/typography direction, no new claims.
- Confirm Slide 6's secondary note stays visually and textually hedged ("exact financial terms... haven't been publicly disclosed") and that no icon/graphic implying "free rent" or "lease deal" was added during actual asset production.
- Confirm Slide 3 and Slide 4 never render a specific calendar date graphic (e.g., no calendar icon, no "Oct 5" or similar) — only the text "early October 2026."
- Confirm no generated image on any slide includes a rendered human face intended to represent DeVonn Francis, and no architectural render is presented as a literal photo of MoMA PS1.
- Confirm account handles (Slide/caption tag list) remain unverified per Copywriter's note — this is outside Visual Director scope but should not be dropped before publishing.
