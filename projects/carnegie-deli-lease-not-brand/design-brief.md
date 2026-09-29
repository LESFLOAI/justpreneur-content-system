# JustPreneur Visual Design Brief — "The Lease Closed. The Brand Never Did." (Carnegie Deli)

**STATUS: DRAFT MODE — IMAGES NOT YET GENERATED.** No image-generation API key is available in this cloud environment. This document contains the full creative direction and every image-generation prompt needed, ready for local execution via `/justpreneur-finish`. Do not treat any visual described here as an existing asset.

**Format:** Instagram Carousel, 8 slides, 1080 x 1350 (portrait)
**Working title:** carnegie-deli-lease-not-brand
**Emotional tone (from Strategist):** respect and quiet confidence — not shock, not sentimentality
**Structural principle (from Strategist):** timeline-driven — 1937 founding → 1976 purchase → 2016 closure → licensing years → 2026 reopening

---

## 0. Hard constraints carried into every visual decision

These override the general brand defaults wherever they conflict. All are non-negotiable — flag them clearly to whoever runs generation locally.

1. **No real-person likenesses.** Milton Parker, Marian Harper Levine, and Sarri Harper are named real individuals. No prompt asks an image generator to render a recognizable face for any of them. Any human presence in generated art is hands-only, back-of-frame, rear-view, or fully silhouetted — period-appropriate era, never a posed portrait that could be read as an attempted likeness.
2. **No reproduction of the real Carnegie Deli trademark or signage design.** The brand's actual red-script neon wordmark, its menu-board typography, and its specific storefront signage are protected trade dress and instantly recognizable — reproducing them (even approximately) risks trademark/likeness problems and also duplicates copy that JustPreneur is adding as a type layer anyway. No generated image contains readable "Carnegie Deli" text, no script-neon signage, no attempt at the real logo. Storefront/counter signage in generated art is always blank, turned away from camera, softly out of focus, or a plain unmarked awning/board.
3. **No claim to depict the real, specific addresses or venues photographically.** 834 Seventh Avenue, Madison Square Garden, The Mirage, and Sands Casino Resort Bethlehem are real, identifiable places. Generated backgrounds are generic, editorial-style representative environments (a generic Midtown storefront, a generic modern arena concourse counter, a generic casino-resort corridor) — evocative of the category, not an attempted photographic reproduction of the specific real building or venue.
4. **No sensational closure imagery.** Avoid padlocks-on-a-gate, crime-scene tape, eviction-notice paper, or "closed forever" doom framing — this reads as tabloid shock, which conflicts with the assigned tone. Avoid the opposite failure mode too: no candlelit-vigil, weepy-nostalgia, soft-focus tribute-reel imagery. The 2016 closure slide should read as quiet and administrative — a dimmed, orderly, transitional space — not a tragedy and not a eulogy.
5. **No fabricated news-outlet chyrons, mastheads, "BREAKING" banners, citation marks, or timestamp/dateline stamps baked into the image.** This is a JustPreneur editorial carousel, not a simulated news screenshot. All dates and labels are added afterward as JustPreneur's own type layer (see §3, §11).
6. **No text baked into any generated image.** All headlines, kickers, dates, and body copy are added after generation as type layers — see the separate layout prompt in §11. This also avoids AI text-rendering artifacts (garbled letters), which are especially visible on a food/hospitality subject with a lot of natural signage-shaped negative space.

---

## 1. Overall creative concept

This is a **business-editorial timeline piece** — the visual language of a Bloomberg Businessweek or Fast Company feature on brand resilience, not a "sad local business closes" human-interest reel and not a generic motivational template. The core visual idea: **a name can keep earning even when the room it came from is gone.**

The carousel is built as a literal chronology. Each interior slide (2–7) is anchored to a specific year or date, and a persistent **timeline rail** — a slim gold horizontal line with small circular era-markers running near the top of every interior slide — accumulates across the sequence: each new slide lights one more node gold while prior nodes stay lit and future nodes stay dim. By Slide 7 (the 2026 reopening), the full rail is lit end to end. This gives a viewer scrolling slide-to-slide a spatial, almost infographic-like sense of "we are here in the story" without adding a single extra word of copy — it visualizes the nine-and-a-half-year gap the copy is about.

Two visual textures alternate with the story's fortunes:
- **Warm, occupied years** (1937 founding, the licensed-counters "still earning" years, the 2026 reopening) — warm sepia-to-amber deli-counter texture: wood, brass, steam off a griddle, rye bread, a meat slicer's soft chrome gleam, warm sconce and neon-adjacent glow (never the real neon wordmark itself).
- **Quiet, vacant years** (the 1976 ownership transition read as formal/administrative, the 2016 closure, the narrowing-footprint years) — cooler, more restrained navy-steel palette, emptier compositions, more negative space, less warmth — signaling absence and administration rather than tragedy.

The final slide (8) breaks from the photographic timeline entirely and resolves as a clean navy-and-gold quote card — the piece's single moment of direct address, holding the pull-quote and the closing question with maximum legibility and zero competing texture.

---

## 2. Composition and focal hierarchy

- **Cover (Slide 1):** Full headline + subhead centered in the top ~55% of the frame on a clean navy field with a restrained, softly blurred deli-counter texture as background atmosphere (not a literal scene) — headline is the dominant element, nothing competes with it. No timeline rail yet (the story hasn't started).
- **Interior slides (2–7):** Timeline rail sits in the top safe zone (~y:120–180). Below it, a short kicker (the year/date, bold gold, large) sits at ~y:220–320. Below the kicker, 1–2 lines of body copy in warm white. The generated photographic/editorial visual occupies the lower ~55–60% of the frame, full-bleed to the side margins with the top safe zone reserved for type. JustPreneur wordmark sits small, centered, in the bottom safe margin on every slide.
- **Final takeaway (Slide 8):** No photographic background — a clean navy-and-gold quote-card layout. The completed timeline rail (all nodes lit) sits at the top as a quiet "we made it through the whole story" callback. Pull-quote line ("The Lease Was Disposable. The Brand Wasn't.") large and centered. Supporting lines below in a smaller warm-white weight, with the closing question ("What's your lease, and what's your brand?") set apart as the final line before the wordmark.

---

## 3. Exact placement — slide by slide

| Slide | Kicker (gold, top) | Copy (word-for-word from approved copy) | Timeline rail state | Background visual |
|---|---|---|---|---|
| 1 — Cover | — | "The Lease Closed In 2016. The Brand Never Did." (headline) / "How Carnegie Deli spent nine years staying alive without a home." (subhead) | Not shown | slide-1-cover |
| 2 | 1937 | "Carnegie Deli opens in Midtown Manhattan. A pastrami institution is born." | Node 1 of 6 lit | slide-2-1937-founding |
| 3 | 1976 | "Milton Parker buys Carnegie Deli with partners — nearly 40 years after it opened. He's the owner, not the founder." | Nodes 1–2 lit | slide-3-1976-purchase |
| 4 | DEC 31, 2016 | "Marian Harper Levine closes the Manhattan flagship, citing personal and legal difficulties, including an ongoing divorce and lawsuits. The deli goes dark." | Nodes 1–3 lit | slide-4-2016-closure |
| 5 | THE BRAND KEEPS WORKING | "No flagship. No dining room. The name still earns — through a counter at Madison Square Garden, licensed counters at The Mirage (Las Vegas, opened 2005) and Sands Casino Resort Bethlehem (opened 2009), plus wholesale and packaged products." | Nodes 1–4 lit | slide-5-brand-keeps-working |
| 6 | THE FOOTPRINT NARROWS | "Sands Bethlehem closes at the end of 2017. The Mirage counter closes around February 2020. Only the Madison Square Garden counter remains open today." | Nodes 1–5 lit | slide-6-footprint-narrows |
| 7 | SEPT 15, 2026 | "Carnegie Deli reopens its Manhattan flagship at 834 Seventh Avenue — the former home of rival Stage Deli. 110 seats. Led by Sarri Harper, third-generation owner and CEO — granddaughter of Milton Parker, daughter of Marian Harper Levine." | Nodes 1–6 lit (complete) | slide-7-2026-reopening |
| 8 — Final takeaway | — | "The Lease Was Disposable. The Brand Wasn't." (pull-quote) / "Nine and a half years without a dining room. The name never stopped earning." / "In a crisis: protect what people believe in — not what you're renting." / "What's your lease, and what's your brand?" | Complete rail shown as closing callback | slide-8-final-takeaway (quote-card, no photographic scene) |

Note on Slide 7: this slide carries the most facts of the set. Keep the generated visual simple and let the copy do the work — a busier background here will hurt legibility of the longest body-copy block in the carousel.

---

## 4. Typography direction

- **Headline/cover typeface:** bold, semicondensed grotesk (same family used across prior JustPreneur carousels — keep consistent). Sentence case for the full headline and subhead on Slide 1.
- **Kicker (years/dates, interior slides):** all-caps for the named-era kickers ("THE BRAND KEEPS WORKING," "THE FOOTPRINT NARROWS"), numeral-as-set for the date kickers ("1937," "1976," "DEC 31, 2016," "SEPT 15, 2026") — bold, gold, noticeably larger than a typical kicker label elsewhere in the brand system, since the year *is* the story's spine here and should read at a glance even in a fast scroll.
- **Body copy:** warm white, regular-to-medium weight, generous line-height, word-for-word from the approved copy — no paraphrasing, no shortening. Slide 5 and Slide 7 carry the longest blocks (3–4 lines); keep body copy at a slightly smaller but still comfortably legible size on those two slides only, rather than shrinking it globally.
- **Slide 8 pull-quote:** largest single-line treatment in the whole carousel, warm white or a warm-white/gold split (quote line in warm white, closing question in gold) — this is the "save this" slide and should be the most typographically confident frame.
- No script fonts, no deli-menu-board lettering, no red-neon-diner cliché typography anywhere — despite the subject matter, this stays in JustPreneur's own premium-business-editorial voice, not a "retro diner" pastiche.

---

## 5. Color palette

**Brand base (unchanged):** deep navy, steel gray, warm white, energy gold — used for all text, kicker, wordmark, timeline rail, and UI chrome across every slide.

**Story-specific accent layer (background photographic art only, not text):**
- Warm sepia-amber — 1937 founding, the "brand keeps working" licensed-counter years, and the 2026 reopening (occupied, earning years)
- Cooler steel-navy, more clinical/formal — 1976 ownership-transition slide (a business transaction, not a warm scene)
- Muted, dimmed cool gray-blue — Dec 2016 closure and the footprint-narrowing slide (quiet and administrative, not black-and-mourning, not tabloid-dark)
- Slide 8 is pure brand navy field with gold accents only — no photographic color grade at all

---

## 6. Image treatment

- Photographic, editorial-documentary texture throughout — natural/practical light sources (sconce, griddle glow, window light), shallow depth of field, believable material texture (wood counter, brass rail, steam, rye bread, deli-case glass) rather than flat vector/illustration style.
- Warm-era slides (2, 5, 7) get a warmer, slightly richer color grade; quiet-era slides (3, 4, 6) get a cooler, slightly desaturated grade — the contrast itself carries the "occupied vs. vacant years" story beat without any extra text.
- No text baked into any generated image anywhere — all copy, kickers, dates, and the timeline rail are added as layers after generation (see §11).
- No reproduction of the real Carnegie Deli wordmark, script neon, or specific storefront signage (see §0.2). No fabricated substitute logos either — signage in frame is always blank, turned away, or softly out of focus.
- Human presence, where used at all, is hands-only, rear-view, or silhouetted — no posed portraits, no recognizable faces (see §0.1).

---

## 7. Instagram safe-margin instructions

**Carousel (1080x1350):** Minimum 72px margin on all sides for any text or wordmark. Interior slides (2–7): keep the top ~35% of the frame (through y ≈ 380) clean and low-detail for the timeline rail + kicker + body copy stack; the generated visual occupies the lower ~55–60%, full-bleed to the side margins. Cover (Slide 1): headline block centered with equal top/bottom breathing room, no rail. Slide 8: entirely typographic — reserve generous margin around the pull-quote (at least 100px top/bottom beyond the 72px minimum) so it reads as a deliberate quote card, not a cramped text dump. JustPreneur wordmark centered in the bottom safe margin, identical size/position, on all 8 slides.

---

## 8. Slide-to-slide consistency rules

- Timeline rail position, node size, and gold/dim styling stay pixel-identical across Slides 2–7 (and its completed form on Slide 8) — only the number of lit nodes changes.
- Kicker style (position, size, gold color) stays identical across all six interior slides; only the label content changes (year numeral vs. all-caps era label).
- The warm/cool grade alternation (§6) must be visually consistent every time a given "temperature" reappears, so a viewer feels the rhythm of occupied-years vs. quiet-years without rereading the copy.
- JustPreneur wordmark treatment (size, position, opacity) is identical across all 8 slides.
- Grotesk type family is identical throughout — no font switching between slides.

---

## 9. Accessibility and contrast check

- Warm-white text (#F5F3EE-equivalent) on a navy scrim (#0B1E32-equivalent) at ≥70% scrim opacity clears WCAG AA for large text at carousel scale.
- Gold kicker/date text (energy-gold, e.g., #D4A017-equivalent) is reserved for short, large-size labels (kickers, dates, the Slide 8 closing question) — never for full paragraph body copy, since gold-on-navy body text at small sizes drops below comfortable contrast on compressed mobile screens.
- Body copy is never placed directly over high-frequency photographic texture (wood grain, steam, brass reflection) without a navy scrim between text and image — scrim is mandatory on every interior slide, not optional, especially on Slides 5 and 7 where the copy block is longest.
- Minimum body-copy size renders no smaller than is comfortably legible at arm's length on a phone; Slides 5 and 7 (longest copy) should be checked first during local assembly since they have the least margin for error.

---

## 10. Image-generation prompts

**IMAGES NOT YET GENERATED — DRAFT MODE.** All prompts below are written for later execution via `scripts/generate_images.py` (or manual submission to an image tool) once an API key is available locally. They are saved verbatim in `image-jobs.json` in this same project folder. Do not run the generation script in this environment.

Full prompt text lives in `image-jobs.json`. Summary of what each job covers:

- **slide-1-cover** (1080x1350) — soft, blurred, warm-navy atmospheric deli-counter texture behind a clean type field; no literal scene, no readable signage.
- **slide-2-1937-founding** (1080x1350) — warm sepia-amber period deli counter, 1930s Midtown Manhattan storefront mood, no real logo, no faces.
- **slide-3-1976-purchase** (1080x1350) — cooler, formal composition suggesting an ownership handshake/transaction moment, hands-only, no faces, no real signage.
- **slide-4-2016-closure** (1080x1350) — quiet, dimmed, orderly closed-for-the-day deli interior, empty counter, lights dimmed, blank signage, no padlocks/tape, no candles.
- **slide-5-brand-keeps-working** (1080x1350) — warm generic arena-concourse food counter plus a suggestion of a casino-resort corridor counter, both blank-signed, conveying "still earning, no home base."
- **slide-6-footprint-narrows** (1080x1350) — cooler, sparser composition, fewer warm light points across a receding row of counters, one still lit, others dim/closed — visual metaphor for narrowing footprint.
- **slide-7-2026-reopening** (1080x1350) — warm, optimistic but restrained new storefront counter, fresh materials, blank awning/signage, quiet-confidence opening-day mood, no crowd, no real address signage.
- **slide-8-final-takeaway** (1080x1350) — pure navy-and-gold minimal quote-card texture, no literal scene, generous clean space for large pull-quote type.

Every prompt in `image-jobs.json` explicitly states: required dimensions, subject/environment, composition, lighting/mood, brand palette, clear negative space reserved for exact copy, and a negative-constraints clause banning illegible text, real trademarks/logos, real-person likenesses, sensational closure imagery, duplicate people, malformed hands, and clutter.

---

## 11. Layout prompt — where exact text goes after image generation

Use this as the standing instruction for whoever assembles the final carousel in a design tool once images exist.

1. Place each `slide-*` image as the lower ~55–60% full-bleed visual on its corresponding slide (Slides 2–7), per §2 and §3. Slide 1 and Slide 8 use their images as full-bleed atmospheric backgrounds behind a clean type field, not as a lower-block visual.
2. Draw the timeline rail as a vector element (not baked into the AI image) — a slim horizontal gold line in the top safe zone of Slides 2–8, with 6 small circular nodes evenly spaced. Fill nodes gold cumulatively per the "Timeline rail state" column in §3; leave remaining nodes a dim steel-gray outline. Slide 1 has no rail; Slide 8 shows the completed rail (all 6 nodes gold) as a closing callback.
3. Set the kicker (year or all-caps era label, gold, bold, large) directly below the rail on Slides 2–7, exactly as labeled in the "Kicker" column of §3.
4. Set the body copy directly below the kicker on Slides 2–7, warm white, word-for-word from the "Copy" column in §3 — do not paraphrase, shorten, or add extra facts.
5. Set the full headline and subhead centered on Slide 1, no kicker, no rail, generous top/bottom breathing room.
6. On Slide 8, set the pull-quote large and centered, then the two supporting lines in a smaller warm-white weight, then the closing question set apart (gold) as the final line before the wordmark — all four lines word-for-word from the approved copy, no paraphrasing.
7. Add a soft navy gradient scrim behind every text block that sits over a photographic visual (Slides 2–7), at 60–75% opacity, before placing type, per §9.
8. Place the small JustPreneur wordmark centered in the bottom safe margin, identical position/size, on all 8 slides.

---

## Open design decisions for local finish

- **Timeline rail execution:** confirm the rail reads clearly at Instagram's compressed carousel-thumbnail size, not just in the full-size slide — if the nodes are too small to register in the grid preview, consider thickening the line or enlarging the current-node marker slightly.
- **Slide 7 copy density:** this slide carries four distinct facts (address, former tenant, seat count, and three generations of ownership). If local review finds the body copy too dense for one slide at comfortable mobile type size, consider a minor type-size reduction on this slide only (per §4) rather than trimming any approved fact.
- **Trademark caution:** confirm with legal/brand ops before final publish that no generated background, even unintentionally, drifts toward the real Carnegie Deli red-script wordmark style — this is the single highest-risk visual element in the set given §0.2.
