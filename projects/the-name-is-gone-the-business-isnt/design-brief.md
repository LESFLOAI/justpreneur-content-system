# JustPreneur Visual Design Brief — "The Name Is Gone. The Business Isn't." (Movistar Arena, Bogotá)

**STATUS: DRAFT MODE — IMAGES NOT YET GENERATED.** No image-generation API key is available in this cloud environment. This document contains the full creative direction and every image-generation prompt needed, ready for later execution via `/justpreneur-finish`. Do not treat any visual described here as an existing asset. `scripts/generate_images.py` has intentionally NOT been run.

**Format:** Instagram Carousel, 7 slides, 1080 x 1350 (portrait)
**Working title:** the-name-is-gone-the-business-isnt
**Target slot:** 2026-10-15, 10:00 AM
**Emotional tone:** calm, clear-eyed respect — a trade-press case study, not alarm, not a "scandal" framing, not generic motivational-poster energy
**Structural principle:** split-timeline convergence — a sponsor's corporate exit track and a venue's operating-continuity track run in parallel, shown as genuinely separate threads, then visually converge once the copy makes the point that they were never causally linked

---

## 0. Hard constraints carried into every visual decision

These override the general brand defaults wherever they conflict. All are non-negotiable — flag them clearly to whoever runs generation locally.

1. **No real company logos, wordmarks, or trade dress.** Telefónica, Movistar, Coltel, Millicom, Tigo, BeatHub, Colombiana de Escenarios (CDE), IDRD, BeLive Entertainment Group, and Procafecol/Juan Valdez are all real, named, currently operating entities. No generated image contains a readable wordmark or logo for any of them, real or fabricated-substitute. Any signage, screens, or marquee elements in generated art are blank, turned away from camera, or softly out of focus. All company names and figures live in the copy layer only — never faked as on-screen branding inside any AI-generated image.
2. **No real-person likeness.** Gabriel Sánchez Olea (the new GM) and the unnamed departing 8-year leader are real individuals. No prompt asks for a recognizable face. Any human presence in generated art is hands-only, rear-view, over-the-shoulder, or fully silhouetted — never a posed portrait that could be read as an attempted likeness.
3. **No literal depiction of the real Movistar Arena.** Per the assignment's own subject-matter note, this is a real, identifiable venue in Bogotá. No prompt claims or implies a photographic reproduction of the actual building. All arena imagery is a generic, illustrative concert-arena silhouette/architecture — could be any mid-size arena anywhere, abstracted at the level of architectural mood, not a specific landmark.
4. **No fabricated financial graphics.** The ~US$214M deal figure, the 67.5%/32.5% stake splits, and the ownership-transfer dates are real. Do not generate stock-ticker boards, exchange graphics, price charts, or fake deal-certificate/contract close-ups with readable (even gibberish) text. Any "corporate transaction" mood is conveyed through abstract architecture, light, and the dual-track graphic motif only (see §1, §6) — all exact figures live in the copy layer.
5. **No government seal or flag treatment.** IDRD is a real Bogotá government agency. Represent the concession/government relationship through generic municipal-building or document-silhouette abstraction only — no official seals, no Colombian flag, no civic emblem.
6. **No text baked into any generated image.** All headlines, kickers, dates, and figures are added afterward as a type layer — see §11. This also avoids AI text-rendering artifacts.
7. **Approved figures are exact and non-negotiable.** Every stake percentage, dollar figure, date, headcount ("50+ shows," "80+ artists"), and name quoted in the approved copy (including the direct quote "as long as the sponsorship remained active") must appear in the type layer exactly as written — no rounding, no paraphrasing, no softening the direct quote.
8. **No added tiny labels, dates, icons, or production marks beyond the approved copy itself.** The split-timeline motif described below is a pure graphic device (two converging lines) with no text, numerals, or icon labels baked onto it — it is a structural visual, not a decorative label. All dates and names the audience needs stay inside the main body copy, which already contains them.

---

## 1. Overall creative concept

This is a **business-editorial case file**, visually closer to a Bloomberg Businessweek or Fast Company explainer than a motivational carousel. The visual spine is the **split-timeline motif** requested in the brief: two parallel horizontal tracks running through the top safe zone of every interior slide —

- **Sponsor track** (energy gold) — the corporate exit: Telefónica → Millicom, the government stake sale, the naming-rights non-renewal.
- **Venue track** (warm white / steel) — the operating reality: the concession, the ownership structure, the new GM, the booking pipeline.

The two tracks run visibly separate and roughly parallel across Slides 2–5, reinforcing the strategic point that one did not cause the other — they are shown as coincidental-but-connected threads, not a cause-and-effect arrow. On Slide 6 ("The Real Lesson"), the two tracks visually converge into a single gold line beneath a plain infrastructure glyph-free graphic (see §3), making the point visible without adding a single extra word: the name was one track; the business was always the other, and only the second one mattered. Slide 1 (cover) and Slide 7 (CTA) carry no track graphic — Slide 1 is a clean hook, Slide 7 is a clean direct-address card.

No dates, numerals, or labels are printed on the tracks themselves (per §0.8) — they are a pure line-weight-and-color graphic device. The dates and names live entirely in the body copy beneath them.

---

## 2. Composition and focal hierarchy

- **Cover (Slide 1):** Headline ("The Name Is Gone. The Business Isn't.") dominant, centered in the upper-to-middle frame on a clean navy field with a softly blurred, atmospheric arena-at-dusk silhouette behind it (generic, not literal). Subhead ("An eight-year sponsor just left the country. The venue didn't blink.") sits smaller, directly beneath the headline. No track graphic.
- **Interior slides (2–6):** Dual-track graphic sits in the top safe zone (~y:110–170). Below it, a short bold kicker in caps (gold) at ~y:210–300. Below the kicker, the exact approved copy in warm white, left-aligned or centered per slide (see table). The generated photographic/graphic visual occupies the lower ~50–55% of the frame, full-bleed to the side margins, with a navy scrim behind any text that overlaps it. JustPreneur wordmark sits small, centered, in the bottom safe margin on every slide.
- **Slide 6 (convergence):** The dual-track graphic visibly merges into one line partway down, directly above the kicker — the single clearest visual payoff moment in the carousel.
- **CTA (Slide 7):** No track graphic, no photographic scene — a clean navy-and-gold direct-address card. "YOUR TURN" kicker, then the two CTA lines, set large and centered, with generous breathing room. This is the save/comment-prompt slide and should be the calmest, most legible frame in the set.

---

## 3. Exact placement — slide by slide

| Slide | Kicker (gold, top) | Copy (word-for-word from approved copy) | Track state | Background visual |
|---|---|---|---|---|
| 1 — Cover | — | "The Name Is Gone. The Business Isn't." (headline) / "An eight-year sponsor just left the country. The venue didn't blink." (subhead) | No track shown | slide-1-cover |
| 2 | THE EXIT | "Telefónica sold 67.5% of Coltel (Movistar's Colombian operator) to Millicom, Tigo's parent — Feb 6, 2026 (~US$214M). Colombia's government sold the remaining 32.5% stake to Millicom — Apr 24, 2026. Two decades in Colombia. Gone in two deals." | Sponsor track active/moving; venue track flat, dim, present but quiet | slide-2-the-exit |
| 3 | A DIFFERENT CONTRACT | "Bogotá's Movistar Arena naming deal: 8 years, expiring Oct 31, 2026. Separate from the corporate exit — but non-renewal became all but certain once Movistar left the country. As recently as July 2026, BeatHub said the name would stay \"as long as the sponsorship remained active.\"" | Sponsor track continuing toward its end-point; venue track running parallel beneath, unaffected | slide-3-different-contract |
| 4 | MOVISTAR NEVER OWNED THE BUILDING | "The arena is run by Colombiana de Escenarios (CDE), under a concession with Bogotá's IDRD since 2016. Movistar was only ever the naming sponsor — never an owner or operator. Sept 17, 2026: BeatHub became CDE's sole shareholder, buying out BeLive Entertainment Group's 50% stake." | Venue track becomes visually dominant (thicker/brighter); sponsor track thinning, receding | slide-4-never-owned-building |
| 5 | NOTHING STOPPED | "New GM Gabriel Sánchez Olea started Oct 5, 2026, replacing an 8-year leader who departed to run Juan Valdez (Procafecol). No new naming sponsor yet — BeatHub opened a call for proposals, expects one in early 2027. 50+ shows still booked through the rest of 2026. 80+ artists already booked for 2027." | Venue track strong and continuous; sponsor track has gone flat/absent, no longer rendered as active | slide-5-nothing-stopped |
| 6 | THE REAL LESSON | "The sponsor's name was never the business. It was a revenue line sitting on top of infrastructure the venue actually controlled: the concession, the building, the booking pipeline. That's why losing the name didn't cost them the business." | Both tracks visibly converge into a single gold line mid-slide | slide-6-the-real-lesson |
| 7 — CTA | YOUR TURN | "Name your top 1-3 revenue dependencies. Ask: what happens if this partner disappears from my market entirely — not just stops paying? Comment or save your answer." | No track (clean card) | slide-7-your-turn (quote/CTA card, no photographic scene) |

---

## 4. Typography direction

- **Headline/cover typeface:** bold, semicondensed grotesk (consistent with the brand system used across prior JustPreneur carousels). Slide 1 headline set exactly as given, in title case per the approved copy (not all-caps — it is a quietly declarative statement, not a shout); subhead in sentence case directly beneath, smaller, warm white.
- **Kicker (interior slides):** all-caps, bold, gold, consistent size across Slides 2–7 — short stage labels that let a fast-scrolling viewer track the argument's structure at a glance.
- **Body copy:** warm white, regular-to-medium weight, generous line-height, word-for-word from the approved copy — no paraphrasing, no shortening, no altered figures (§0.7). Slide 2, 3, and 4 carry the densest factual blocks (multiple dates/percentages/names in one paragraph); keep these at a slightly smaller but still comfortably legible size on those slides only, rather than shrinking type globally.
- **Direct quote treatment (Slide 3):** the quoted phrase "as long as the sponsorship remained active" is set in italic within the body copy to visually mark it as a direct quotation, exactly as punctuated in the approved copy.
- **Slide 6 pull-line:** "The sponsor's name was never the business." may be set as a slightly larger lead line, with the remainder of the paragraph in standard body size directly beneath — a scale choice only, no words altered.
- **Slide 7 CTA:** largest, most confident typographic treatment after the cover — "YOUR TURN" kicker, then the two CTA sentences set large and centered with generous spacing, inviting a comment/save action without crowding.
- No script fonts, no faux-ticket or faux-legal-document novelty lettering, no stock-ticker/LED font cliché anywhere.

---

## 5. Color palette

**Brand base (unchanged):** deep navy, steel gray, warm white, energy gold — used for all text, kickers, wordmark, dual-track graphic, and UI chrome across every slide.

**Story-specific accent layer (background visuals only, not text):**
- Slides 2–3 (the exit, the contract): cooler steel-navy, abstract corporate/architectural light — consequential but calm, not alarming.
- Slides 4–5 (ownership, continuity): warmer gold-amber glow layered into the navy base — signals stability, continuity, "business as usual."
- Slide 6 (the lesson): the two accent temperatures visually resolve into one consistent warm-gold-on-navy treatment, reinforcing convergence.
- Slide 1 and Slide 7: pure brand navy fields with restrained gold accent glow only — no heavy photographic grade.

---

## 6. Image treatment

- Editorial-abstract texture throughout — generic architecture, light, and the dual-track graphic device rather than literal photojournalism of real people, real logos, or the real venue.
- No text baked into any generated image anywhere — all copy, kickers, and the dual-track graphic are added as layers after generation (see §11), except the base line-and-color structure of the track itself, which may be generated as part of the background art or added as a vector overlay — whichever renders more cleanly; vector overlay is preferred for precision and consistency.
- No reproduction of any real company wordmark/logo (§0.1), no real government seal (§0.5), no literal real-venue photography (§0.3), no recognizable real-person likeness (§0.2).
- Human presence, where used at all, is hands-only, rear-view, or silhouetted — no posed portraits, no visible faces.

---

## 7. Instagram safe-margin instructions

**Carousel (1080x1350):** Minimum 72px margin on all sides for any text or wordmark. Interior slides (2–6): keep the top ~30% of the frame (through y ≈ 400) clean and low-detail for the dual-track graphic + kicker + body copy stack; the generated visual occupies the lower ~50–55%, full-bleed to the side margins, with a navy scrim behind any overlapping text. Cover (Slide 1): headline + subhead block centered with equal top/bottom breathing room. Slide 7: entirely typographic — reserve generous margin (at least 100px top/bottom beyond the 72px minimum) so it reads as a deliberate, calm direct-address card. JustPreneur wordmark centered in the bottom safe margin, identical size/position, on all 7 slides.

---

## 8. Slide-to-slide consistency rules

- Dual-track graphic position, line weight, and gold/warm-white color coding stay pixel-identical across Slides 2–6 — only the relative state (which track is active/dominant/converging) changes, per §3.
- Kicker style (position, size, gold color, caps) stays identical across all slides that carry one (2–7).
- The cool-to-warm accent temperature shift (§5) must read consistently each time a given "phase" of the story reappears.
- JustPreneur wordmark treatment (size, position, opacity) is identical across all 7 slides.
- Grotesk type family is identical throughout — no font switching between slides.

---

## 9. Accessibility and contrast check

- Warm-white text on a navy scrim at ≥70% scrim opacity clears WCAG AA for large text at carousel scale.
- Gold kicker text is reserved for short, large-size labels — never for full paragraph body copy, since gold-on-navy body text at small sizes drops below comfortable contrast on compressed mobile screens.
- Body copy is never placed directly over high-frequency photographic/architectural texture without a navy scrim between text and image — mandatory on every interior slide, especially Slides 2–4, which carry the densest factual paragraphs.
- Minimum body-copy size renders no smaller than is comfortably legible at arm's length on a phone; Slides 2, 3, and 4 (most fact-dense) should be checked first during local assembly since they have the least margin for error.
- The direct quote on Slide 3 must remain fully legible in italic at mobile size — do not let the quotation marks or italicization reduce apparent size below the rest of the body copy.

---

## 10. Image-generation prompts

**IMAGES NOT YET GENERATED — DRAFT MODE.** All prompts below are written for later execution via `scripts/generate_images.py` (or manual submission to an image tool) once an API key is available locally. They are saved verbatim in `image-jobs.json` in this same project folder. Do not run the generation script in this environment.

Summary of what each job covers (full prompt text lives in `image-jobs.json`):

- **slide-1-cover** (1080x1350) — soft, blurred, warm-navy atmospheric generic-arena-at-dusk silhouette behind a clean type field; no literal venue, no readable signage.
- **slide-2-the-exit** (1080x1350) — abstract cool-toned corporate handoff: two generic blurred office-tower silhouettes with a soft light/signal transferring between them, evoking an ownership sale without any readable branding or financial chart.
- **slide-3-different-contract** (1080x1350) — a generic arena facade at dusk with a blank, unlit rectangular marquee/nameplate silhouette (no text), paired with a subtle abstract countdown/calendar-light motif, conveying an expiring agreement.
- **slide-4-never-owned-building** (1080x1350) — a generic arena building rendered in a quiet architectural/blueprint-adjacent style, emphasizing structure and foundation over signage, with a soft warm-gold glow signaling stability and ownership continuity.
- **slide-5-nothing-stopped** (1080x1350) — a generic arena interior suggesting an active, booked venue — warm stage-light glow, rows of empty seats implying upcoming shows, anonymized hands-only gesture suggesting a calm handoff/continuity, no faces, no readable signage or screens.
- **slide-6-the-real-lesson** (1080x1350) — a clean, minimal abstract graphic: two soft light-lines converging into one steady gold line against a navy field, with generous negative space for a pull-line and body copy.
- **slide-7-your-turn** (1080x1350) — pure navy-and-gold minimal texture, no literal scene, generous clean space for large centered CTA type.

Every prompt in `image-jobs.json` explicitly states: required dimensions, subject/environment, composition, lighting/mood, brand palette, clear negative space reserved for exact copy, and a negative-constraints clause banning illegible text, real trademarks/logos/seals, real-person likenesses, literal real-venue depiction, duplicate people, malformed hands, and clutter.

---

## 11. Layout prompt — where exact text goes after image generation

Use this as the standing instruction for whoever assembles the final carousel in a design tool once images exist.

1. Place each `slide-*` image as the lower ~50–55% full-bleed visual on its corresponding slide (Slides 2–6), per §2 and §3. Slide 1 and Slide 7 use their images as full-bleed atmospheric backgrounds behind a clean type field, not as a lower-block visual.
2. Draw the dual-track graphic as a vector element (not baked into the AI image, to keep it crisp and consistent) — two thin horizontal lines in the top safe zone of Slides 2–6: a gold line (sponsor track) and a warm-white/steel line (venue track). No text, dates, or icons on the lines themselves (§0.8). Adjust each line's weight/brightness/position per the "Track state" column in §3 — on Slide 6, merge the two lines into one gold line partway across the frame. Slide 1 and Slide 7 carry no track graphic.
3. Set the kicker (gold, bold, caps) directly below the track graphic on Slides 2–7, exactly as labeled in the "Kicker" column of §3.
4. Set the body copy directly below the kicker on Slides 2–7, warm white, word-for-word from the "Copy" column in §3 — do not paraphrase, shorten, or alter any figure, name, date, or the direct quote on Slide 3.
5. Set the full headline and subhead centered on Slide 1, no kicker, no track graphic, generous top/bottom breathing room, exactly as written in the approved copy.
6. On Slide 7, set "YOUR TURN" as the kicker, then the two CTA sentences large and centered below it, word-for-word from the approved copy.
7. Add a soft navy gradient scrim behind every text block that sits over a photographic/graphic visual (Slides 2–6), at 60–75% opacity, before placing type, per §9.
8. Place the small JustPreneur wordmark centered in the bottom safe margin, identical position/size, on all 7 slides.

---

## Open design decisions for local finish

- **Dual-track graphic execution:** confirm the two-line motif reads clearly as "two separate things happening" at Instagram's compressed carousel-thumbnail size, not just at full size. If the convergence on Slide 6 is too subtle at thumbnail scale, consider increasing the line-weight contrast between the two tracks on Slides 2–5 so the merge on Slide 6 reads as a clear payoff.
- **Fact density on Slides 2–4:** these carry the most names, dates, and percentages in the set. If local review finds body copy too dense for comfortable mobile type size, reduce type size on those slides only (per §4) rather than trimming any approved fact.
- **Real-entity caution:** confirm with legal/brand ops before final publish that no generated background, even unintentionally, drifts toward a recognizable rendering of the real Movistar Arena, any real company's color-coded brand identity (e.g., Movistar's blue, Tigo's blue-and-white), or any real person's likeness — this is the highest-risk visual element in the set given §0.1–§0.3 and the number of real, named entities in this story.
- **Tone check:** this story's desired emotional register is "calm, clear-eyed respect," not drama. If any generated background reads as more ominous/alarming than intended (e.g., too stark a "collapse" mood on Slides 2–3), prefer a cooler, more neutral-editorial treatment over a tense one.
