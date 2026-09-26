# JustPreneur Visual Design Brief — "The Price Ladder" (Anthropic Opus 5.5 vs OpenAI GPT-6 Sol/Luna)

**STATUS: DRAFT MODE — IMAGES NOT YET GENERATED.** No image-generation API key is available in this cloud environment. This document contains the full creative direction and every image-generation prompt needed, ready for local execution via `/justpreneur-finish`. Do not treat any visual described here as an existing asset.

**Primary format:** Instagram Carousel, 7 slides, 1080 x 1350 (portrait)
**Working title:** the-price-ladder
**Story date referenced in copy:** September 22, 2026

---

## 0. Hard constraints carried into every visual decision

1. **No fake or real company logos.** Do not render Anthropic, Claude, OpenAI, or GPT wordmarks/logos, or any invented lookalike marks. All company/model attribution (Anthropic, Opus 5.5, GPT-6 Sol, GPT-6 Luna) is added as a type layer after generation — the background art itself stays generic and abstract (architectural light/staircase forms), never a lettermark or icon standing in for a real brand.
2. **Slide 4 pricing-hierarchy caution (from copywriter).** Sol is priced *below* Opus 5.5 despite being labeled the "frontier" tier, which would visually contradict a strict low-to-high price staircase if literalized. Slide 4's visual must NOT be a single continuous ascending staircase with three steps in price order. Instead it uses **two separate tier platforms** (frontier vs. commodity) rising from **one shared baseline** representing Anthropic's single price line — tier identity is the primary visual hierarchy; exact prices are secondary labels added afterward. See §3, Slide 4 for the full spec.
3. **No exact numerals/copy baked into generated images.** All prices ($4/$20, $2/$10, $0.10/$0.50), percentages, tier labels (FRONTIER/COMMODITY), and headline/body text are added in the design/layout tool after generation, not rendered by the image model. Image prompts explicitly forbid illegible or fabricated text.
4. **No stock "AI robot" or brain-circuit clichés.** This is a business-editorial story about pricing strategy, not a sci-fi story about AI itself. Visuals stay in architectural/light-structure metaphor territory (staircases, platforms, beams of light) — no humanoid robots, glowing brains, circuit-board overlays, or code/terminal screens.

---

## 1. Overall creative concept

The story is that **a single price cut (Anthropic) was answered by a structural move (OpenAI's two-tier launch)** — and the visual system should make that structural difference legible at a glance, before a reader processes a single number. The recurring motif is a **staircase / price-ladder built from architectural light** — glowing steps and platforms rising out of a dark navy field, shot like premium fintech-editorial cover art (think Bloomberg Businessweek or The Information's illustrated covers), not a motivational-quote template and not a sci-fi AI visual.

Two structural ideas recur visually across the carousel:
- **The single move** — one hero step or one lone tower, cleanly lit, used for Anthropic's cut and for "one front" framing.
- **The tiered structure** — two distinct platforms/towers of different shape and light color, used for OpenAI's two-model launch and for "two fronts" framing.

The piece resolves on an open, unfinished ladder rising into empty sky for the CTA — inviting the reader to build (and picture) their own.

---

## 2. Composition and focal hierarchy

Every slide (1–7) uses the same structural template:
- **Top band (kicker + headline/body copy):** generous flat negative space, roughly the top 45–55% of the frame on interior slides, for kicker label + headline/body text, sitting on a subtle navy scrim if it overlaps any atmospheric haze from the art below.
- **Lower two-thirds to bottom:** the generated staircase/platform artwork, full-bleed, receding into navy fog at the edges so it blends cleanly with the text band above rather than showing a hard seam.
- **JustPreneur wordmark:** small, centered, in the bottom safe margin, identical size/position/opacity on all 7 slides.
- **Cover (Slide 1)** and **CTA (Slide 7)** flex this template slightly (see §3) since they carry either the full headline or the closing call-to-action rather than a kicker + body-copy pairing.

---

## 3. Exact placement — slide by slide

| Slide | Role (kicker) | Copy (verbatim, set after generation) | Background visual (image-jobs.json id) |
|---|---|---|---|
| 1 | Cover, no kicker | "OpenAI Didn't Launch One Model. It Launched a Price Ladder." / subhead: "Sept 22, 2026 — the AI price war got more interesting than the price." | slide-1-cover |
| 2 | THE CUT EVERYONE NOTICED | "Anthropic dropped Claude Opus 5.5 to $4/$20 per million tokens, a 20% cut from Opus 5's $5/$25 list price. Anthropic says it's also 30%+ faster." | slide-2-the-cut |
| 3 | 90 MINUTES LATER... | "90 minutes later, OpenAI followed with two new models, not one: GPT-6 Sol and GPT-6 Luna." | slide-3-the-answer |
| 4 | TWO TIERS, ONE LAUNCH | "Sol (frontier): $2/$10, down 50%, permanent per OpenAI, undercuts Opus 5.5 on both ends. Luna (commodity): $0.10/$0.50, down 50–58%. Meanwhile, Anthropic: one model, one price line at $4/$20." | slide-4-two-tiers |
| 5 | WHY TWO BEATS ONE | "A single price cut defends one front. A tiered launch defends two, same day." | slide-5-two-fronts |
| 6 | READ THE MOVE, NOT JUST THE PRICE | "Builders who compete on one price point are exposed on one front. Builders who architect tiers are harder to out-position." | slide-6-blueprint |
| 7 | Map Your Own Ladder (CTA) | "Where's your premium tier? Where's your accessible one? Save this. Audit your offer stack this week." | slide-7-cta |

### Slide 4 detail spec (critical — read before generating or laying out)

Per the copywriter's note, do **not** depict Sol, Luna, and Opus 5.5 as three sequential steps ordered by price (which would visually rank Sol beneath Opus 5.5 and could read as "Sol is the cheap one"). Instead:

- **Two platforms, not three steps.** A tall, narrow, sharply gold-lit platform (visual stand-in for "frontier" tier / Sol) and a wide, broad, cool-steel-lit platform (visual stand-in for "commodity" tier / Luna) — different *shapes*, not different *heights on the same staircase*. Shape encodes tier identity; height is deliberately not used as a price-ranking signal.
- **One shared baseline.** Both platforms rise from a single glowing horizontal foundation line, which after generation carries the label "Anthropic — one model, one price: $4/$20" directly on or just above the baseline, visually representing "the one price line the two-tier launch is answering."
- **Label hierarchy when text is added:** tier name (FRONTIER / COMMODITY) is the largest, most prominent label on each platform; the exact price ($2/$10, $0.10/$0.50) sits beneath it in a visibly smaller, secondary weight. This ordering (tier first, price second) is mandatory — it's the fix for the ranking-confusion risk the copywriter flagged.

---

## 4. Typography direction

- **Headline/cover typeface:** bold condensed-to-semicondensed grotesk (e.g., Neue Haas Grotesk Condensed Black / Suisse Int'l Bold), consistent with prior JustPreneur carousels. Sentence case for the full headline (Slide 1); kicker labels in all-caps, gold, letter-spaced, small (matches prior carousel convention).
- **Body copy:** warm white, regular-to-medium weight, generous line height, max 3 lines per slide to protect mobile legibility — Slide 4 has the densest copy, so its body text should drop one size step smaller than Slides 2/3/5/6 while staying above the minimum legible size for mobile (no smaller than roughly 34–36px cap-height equivalent at 1080px width).
- **Price/number treatment:** set all exact prices and percentages in tabular (fixed-width) numerals, extra-bold weight, so figures don't visually wobble against surrounding prose — this is a numbers-forward story and the numerals should read as confidently as the headline.
- **Tier-color coding for Slide 4 only:** FRONTIER label + its price in energy gold; COMMODITY label + its price in a brighter "platinum steel" tone (a lightened steel gray, distinct enough from body-copy warm white to read as its own category at a glance); Anthropic's baseline label in plain warm white, no tier color, since it is not part of either tier.

---

## 5. Color palette

**Brand base:** deep navy (#0B1220), steel gray (#5B6470), warm white (#F5F3EE), energy gold (#E7B740).

**Story-specific accent layer (background art and Slide 4 label coding only, not general body text):**
- **Energy gold** — the "frontier" tier, the single dramatic beam/cut on Slides 1–2, and all CTA light in Slide 7.
- **Platinum steel** (a brightened, cooler variant of the base steel gray, roughly #A9B4BE) — the "commodity" tier on Slide 4, and the "second tower" in Slide 5's two-fronts visual, so a reader learns to associate this cooler tone with "scale/accessible" versus gold's "premium/frontier" the moment they hit Slide 4, and can carry that association forward.
- Avoid: red/green stock-market up/down color coding (this isn't a stock-ticker story), racing/countdown clock iconography, coin or cash imagery.

---

## 6. Image treatment

- Cinematic architectural-render / premium-editorial illustration style throughout — glowing light-built staircases and platforms suspended in navy fog/atmosphere, consistent single light-source direction (upper-left) across all 7 slides for visual cohesion.
- No literal screens, keyboards, terminal windows, code, or chat-bubble UI anywhere — this is a strategy story, not a product-demo story.
- No humanoid robots, glowing brains, or circuit-board textures.
- No text baked into any generated image anywhere — all copy, kickers, labels, and prices are added as type layers after generation.
- No fake or real company logos/wordmarks (see §0.1).
- No watermarks, no small corner icons, no production slates, no slide-count indicators.

---

## 7. Instagram safe-margin instructions

**Carousel (1080x1350):** 72px minimum margin on all sides for any text or wordmark. Keep the top ~45–55% of interior Slides 2–6 clear and low-detail (light fog only, no hard architectural edges) for the kicker + body-copy overlay. Slide 1's headline block is centered with equal top/bottom breathing room within the top ~60% of the frame. Slide 4 additionally needs two clear flat zones directly over or beside each platform (roughly the upper third of each platform shape) for the tier-name + price labels, and a clear band directly along the shared baseline for the Anthropic label — flag these three zones explicitly to whoever lays out this slide. Slide 7's CTA text and JustPreneur wordmark sit in the open sky/negative-space area above the unfinished ladder, never overlapping the structure itself.

---

## 8. Slide-to-slide consistency rules

- Every slide uses the same navy fog atmosphere, the same upper-left key light direction, and the same grotesk type family — no font or lighting-direction switching mid-carousel.
- Gold = frontier/premium/single-dramatic-move throughout; platinum steel = commodity/scale/second-front throughout. Once this mapping is established on Slide 4, it must not be contradicted on Slides 5–7.
- Kicker label style (all-caps, gold, small, letter-spaced) is identical across Slides 2–6.
- JustPreneur wordmark size, position (bottom-center safe margin), and opacity are identical across all 7 slides.
- The "single tower/step" visual language (Slides 2, 5-left-side) and the "multi-platform/tower" visual language (Slides 3, 4, 5-right-side, 6) should each be immediately recognizable as the same recurring idea reappearing, not redesigned each time.

---

## 9. Accessibility and contrast check

- Warm-white text (#F5F3EE) on the deep-navy scrim (#0B1220) at ≥70% scrim opacity clears WCAG AA comfortably for body text at carousel scale (contrast ratio well above 7:1).
- Energy gold (#E7B740) on navy is reserved for large kicker labels and Slide-4 tier/price numerals — never for full paragraph body copy, since gold-on-navy body text at small sizes drops below comfortable mobile contrast.
- Platinum steel (#A9B4BE) on navy is legible for the Slide-4 COMMODITY label at the specified large/secondary sizes, but should not be used for small body copy either — treat it the same way as gold, as a large-label-only accent.
- No text is placed directly over high-frequency fog/light-bloom texture without a navy scrim beneath it — scrim is mandatory on every slide, not optional.
- Minimum body-copy size renders no smaller than ~34–36px cap-height equivalent at 1080px width so it stays legible on a phone at arm's length; Slide 4's denser copy is the one slide that gets closest to this floor and should be checked first during layout QA.

---

## 10. Image-generation prompts

**IMAGES NOT YET GENERATED — DRAFT MODE.** All prompts below are written for later execution via `scripts/generate_images.py` (or manual submission to an image tool) once an API key is available locally. They are saved verbatim in `image-jobs.json` in this same project folder. Do not run the generation script in this environment.

Full prompt text lives in `image-jobs.json`. Summary of what each job covers:

- **slide-1-cover** (1080x1350) — wide establishing shot of a grand illuminated staircase of light ascending through navy fog, single dramatic gold beam; top ~60% left clean for the full headline + date subhead.
- **slide-2-the-cut** (1080x1350) — one isolated glowing platform/step catching a single gold beam, minimal and hero-lit, for "the cut everyone noticed."
- **slide-3-the-answer** (1080x1350) — kinetic, energy-trail image of a second set of light structures rapidly igniting beside the first, conveying a fast counter-response ("90 minutes later").
- **slide-4-two-tiers** (1080x1350) — the two-platform-plus-shared-baseline composition specified in §3's Slide 4 detail spec; the most constrained prompt in this set.
- **slide-5-two-fronts** (1080x1350) — split composition, one lone defended tower (gold) on one side vs. two interconnected defended towers (gold + platinum steel) on the other, strategic-defense metaphor.
- **slide-6-blueprint** (1080x1350) — wide blueprint-style illustration of a tiered light structure with a single small back-of-frame silhouette studying it from a distance, evoking analysis over reaction.
- **slide-7-cta** (1080x1350) — an open, unfinished ladder of light extending into empty navy sky, soft gold glow at the top, generous open negative space for CTA text and the JustPreneur wordmark.

Every prompt in `image-jobs.json` explicitly states: required dimensions, subject/environment, composition, lighting/mood, brand palette, clear negative space reserved for exact copy, and a negative-constraints clause banning illegible text, fake/real logos, duplicate structures, malformed hands (where any human silhouette appears), and clutter.

---

## 11. Layout prompt — where exact text goes after image generation

Use this as the standing instruction for whoever assembles the final carousel in a design tool once images exist:

1. Place each `slide-*` image as the full-bleed background for its slide, per the table in §3.
2. Add a soft navy gradient scrim across the top ~45–55% of interior Slides 2–6 (and the top ~60% of Slide 1) at 60–75% opacity before placing type, so text sits clearly above the atmospheric art beneath.
3. Set the kicker (all-caps, gold, small, letter-spaced) at the top of Slides 2–6 exactly as labeled in the "Role" column of §3 — do not paraphrase.
4. Set body copy directly below the kicker, warm white, word-for-word from the "Copy" column of §3 — do not paraphrase or shorten the approved lines.
5. Set the full headline + date subhead centered on Slide 1, no kicker, per §3.
6. **Slide 4 only:** after placing the background, add "FRONTIER" in large gold type over the tall narrow platform with "$2/$10 · down 50% · permanent per OpenAI" beneath it in smaller gold type; add "COMMODITY" in large platinum-steel type over the wide platform with "$0.10/$0.50 · down 50–58%" beneath it in smaller platinum-steel type; add "Anthropic: one model, one price — $4/$20" in warm white directly on or just above the shared baseline. Tier label must always render larger and higher-contrast than its price line, per §3's mandatory hierarchy fix.
7. Set the CTA copy and JustPreneur wordmark in the open sky area of Slide 7, per §3 and §7 — wordmark never overlaps the ladder structure itself.
8. Place the small JustPreneur wordmark centered in the bottom safe margin on every slide, identical position/size across all 7.

---

## Open design decisions for local finish

- **Slide 4 QA priority:** because this is the slide the copywriter flagged, whoever runs local generation/layout should render and review Slide 4 first, independent of the other six, and confirm a reader cannot mistake platform height for a price ranking before finalizing the carousel.
- **Tier color-coding carryover:** confirm during layout that gold/platinum-steel tier coding introduced on Slide 4 doesn't clash with the plain gold-kicker convention used on Slides 2/3/5/6 (kickers stay gold regardless of tier; the platinum-steel accent appears only where "commodity tier" is being depicted).
- **Caption/alt-text:** since Slide 4 carries the most safety-sensitive claim (tier vs. price ranking), consider echoing the "frontier tier priced below a competitor, tier ≠ rank" clarification in the post caption or alt text as a belt-and-suspenders measure — flagging for Quality Control / Fact Verifier rather than deciding unilaterally here.
