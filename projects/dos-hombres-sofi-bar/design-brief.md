# JustPreneur Visual Design Brief — "Presence Over Endorsement" (Dos Hombres @ SoFi Stadium)

**STATUS: DRAFT MODE — IMAGES NOT YET GENERATED.** No image-generation API key is available in this cloud environment. This document contains the full creative direction and every image/video generation prompt needed, ready for local execution via `/justpreneur-finish`. Do not treat any visual described here as an existing asset.

**Target posting slot:** 2026-09-24, 10:00 AM
**Primary format:** Instagram Reel, ~30–38 sec, 1080 x 1920 (9:16)
**Fallback format:** Instagram Carousel, 7 slides, 1080 x 1350 (portrait)
**Working title:** dos-hombres-sofi-bar

---

## 0. Hard constraints carried into every visual decision

These come directly from the Fact Verifier / assignment brief and override the general brand defaults wherever they conflict:

1. **No real-person likenesses.** Aaron Paul and Bryan Cranston are named public figures. No prompt in this brief asks an image generator to render their faces or a recognizable likeness of either man. Any human presence in generated art is hands-only, back-of-frame, or fully silhouetted/rim-lit so no face is identifiable. This is a deepfake-avoidance rule, not a stylistic preference — flag it as non-negotiable to whoever runs generation locally.
2. **No "first-ever" implication.** This is the brand's *first permanent standalone bar*, not its first activation of any kind. Visuals avoid any "grand opening ribbon," "first time ever" iconography, or countdown/milestone number graphics.
3. **No Rams "tequila partner" badging.** That sponsorship role belongs to 1800 Tequila, not Dos Hombres — conflating them is a factual error. No prompt uses Rams team colors (royal blue/gold), the Rams horn logo, jersey numbers, or any "Official Partner" plaque styling. Stadium environments are rendered as generic modern NFL-concourse architecture in neutral steel/concrete/warm-string-light tones — recognizable as "a stadium," not as "SoFi Stadium the specific licensed venue" and not as Rams-branded space.
4. **No deal-structure visuals.** No lease documents, signage-installation, ribbon-cutting, contracts, handshake-over-paperwork, or JV/franchise iconography. The story is about presence, not deal mechanics.
5. **No real Dos Hombres bottle/label reproduction.** Treat their bottle design and wordmark as a real trademark. Any bottle shown is a generic, unbranded agave-spirit bottle silhouette — plain glass, no label text, no logo. Because Dos Hombres is a **mezcal**, not a tequila, glassware should read as a traditional rustic clay *copita* (small clay mezcal cup) rather than a tequila shot glass with salt/lime, to avoid category conflation.
6. **Real footage is the better option for the Reel if it exists.** If the team has actual photos/video from the SoFi Stadium bar opening night, that should replace the generated b-roll described below — this brief's Reel visuals are a fallback path for when no licensed footage is available, not a preferred substitute for the real thing. Flag this clearly to whoever runs `/justpreneur-finish`.

---

## 1. Overall creative concept

The story is about **founder presence as the flex** — two famous names chose to physically work a bar on a live NFL Monday-night crowd instead of sending a rep or running an ad. The visual system should feel like a **behind-the-bar, opening-night atmosphere piece**: warm amber bar lighting, steam/condensation, hands in motion, a big stadium hum in the background — cut against the cool, corporate blandness of "a label" or "a rep" to make the contrast physical, not just verbal.

Visual language: **modern sports-business editorial** (think The Athletic's business desk or Sportico), not a lifestyle-influencer bar reel and not a generic "hustle culture" motivational template. Confident, a little cinematic, grounded in a real room with real texture (wood, copper, steam, stadium light) rather than flat color-block graphics.

Two visual "worlds" recur across the piece and are set in deliberate contrast:
- **The Label World** — cool, flat, sterile: a plain bottle sitting alone under office-fluorescent light, a rep-shaped absence. This carries the "most brands stop at the label" / "they didn't send a rep" beats.
- **The Bar World** — warm, textured, alive: copper bar top, amber backlight, steam off a pour, a crowd's hands raised in string-lit stadium concourse glow. This carries the "they worked the bar" / "founder presence" beats.

The piece resolves on the JustPreneur wordmark over a calm navy-gold field — pulling both worlds back into brand territory for the CTA.

---

## 2. Composition and focal hierarchy

**Reel (1080 x 1920):**
- Full-bleed background visual per beat (video or animated still/Ken-Burns pan on a generated image).
- A single line of kinetic on-screen text per beat, placed in the **lower-third safe zone** (never the very bottom, which Instagram's UI covers with caption/like/share icons) or **vertically centered** for the two "punch" beats (4 and 8), to give the sequence rhythm rather than a static text position every time.
- Text sits on a dark navy scrim/gradient (roughly 60–75% opacity, feathered edge, not a hard box) so it stays legible over moving or textured backgrounds without looking like a static template.
- JustPreneur wordmark appears small and steady in the **upper-safe-zone corner** (top-left or top-right, rotating consistently) from beat 2 onward as a persistent watermark-style presence — subtle, not a distraction — then appears large and centered only in the final beat 10 sting.

**Carousel (1080 x 1350):**
- Same top-45%-clean / bottom-two-thirds-visual convention used in prior JustPreneur carousels: generous negative space band across the top or side for kicker + body copy, generated visual occupies the lower two-thirds, JustPreneur wordmark small and centered at the very bottom margin.
- Cover slide (Slide 1) carries the full headline; Slides 2–6 carry a kicker + one to two lines of body copy each; Slide 7 is the CTA/save slide.

---

## 3. Exact placement — beat-by-beat / slide-by-slide

### REEL (10 beats, ~38 sec total, 1080x1920)

| Beat | Timing | On-screen text | Background visual (see §10 prompts) | Text placement |
|---|---|---|---|---|
| 1 | 0:00–0:02 | "Most celebrity brands stop at the label." | bg-reel-1-label-world | Centered, mid-frame |
| 2 | 0:02–0:05 | "Dos Hombres just opened its first permanent bar." | bg-reel-2-bar-exterior | Lower third |
| 3 | 0:05–0:09 | "Monday Night Football. Rams vs. Giants. Opening night." | bg-reel-3-stadium-night | Lower third |
| 4 | 0:09–0:14 | "They didn't send a rep." | bg-reel-4-empty-rep | Vertically centered (punch beat) |
| 5 | 0:14–0:18 | "They stood behind the bar. Pouring drinks. For fans." | bg-reel-5-pouring-hands | Lower third |
| 6 | 0:18–0:22 | "Even served fans their own creation: 'GO FOR DOS!'" | bg-reel-6-crowd-toast | Lower third |
| 7 | 0:22–0:27 | "That's not an ad. That's not a license deal." | bg-reel-7-label-vs-bar-split | Lower third |
| 8 | 0:27–0:32 | "That's founder presence — the one thing money can't fake." | bg-reel-8-founder-silhouette | Vertically centered (punch beat) |
| 9 | 0:32–0:37 | "Where in YOUR business could you show up — instead of delegating?" | bg-reel-9-reflective-desk | Lower third |
| 10 | 0:37–0:38 | "Save this. Go find that moment." + JustPreneur wordmark sting | bg-reel-10-wordmark-sting | Centered, wordmark large |

Beats 1, 4, 7, and 8 are the "idea" beats (label/rep/ad contrast, no literal event depiction needed) — these are safest to fully generate. Beats 2, 3, 5, 6 are the "event" beats — this is exactly where real photos/video from the actual bar opening should be substituted in if available (see §0.6); the generated versions below are placeholders only.

### CAROUSEL (7 slides, 1080x1350) — fallback if Reel assets are insufficient

| Slide | Role | Copy | Background visual |
|---|---|---|---|
| 1 | Cover | "They Didn't Just License Their Name. They Worked The Bar." | bg-carousel-1-cover |
| 2 | THE MOVE | "Dos Hombres just opened its first permanent branded bar — inside SoFi Stadium." | bg-carousel-2-the-move |
| 3 | THE STAGE | "Monday Night Football. Rams vs. Giants. Opening night." | bg-carousel-3-the-stage |
| 4 | THE CHOICE | "Aaron Paul & Bryan Cranston didn't send a rep. They worked it themselves." | bg-carousel-4-the-choice |
| 5 | THE MOMENT | "Serving fans their own creation: 'GO FOR DOS!'" | bg-carousel-5-the-moment |
| 6 | THE LESSON | "Founder presence at the moment of experience builds trust advertising can't buy." | bg-carousel-6-the-lesson |
| 7 | CTA | "Save this. Where could YOU show up in person instead of delegating?" | bg-carousel-7-cta |

Note on Slide 4 copy: the visual for this slide must **not** attempt to render Aaron Paul or Bryan Cranston (see §0.1) even though their names appear in the on-slide text — the named text is added afterward as a type layer, the background art stays anonymized (hands/silhouette only, or no human figure at all).

---

## 4. Typography direction

- **Headline/cover typeface:** bold, condensed-to-semicondensed grotesk (e.g., Neue Haas Grotesk Condensed / Akzidenz-style weight), all the JustPreneur carousels to date use this family — keep consistent. Sentence case, not all-caps, for the long headline; short kicker words (THE MOVE, THE STAGE, etc.) in all-caps, slightly letter-spaced, small size, gold.
- **Reel kinetic text:** same grotesk family, heavier weight (bold/black) for single-line punch statements, slightly larger optical size than a static carousel headline would need since it's on screen only 3–5 seconds per beat and must be readable at a glance mid-scroll.
- **Body copy (carousel):** warm white, regular weight, generous line-height, max ~2 lines per slide to protect legibility.
- No script fonts, no decorative western/rodeo-style lettering — despite the mezcal/agave subject matter, avoid "cantina" cliché typography. Keep it in JustPreneur's own premium-business-editorial voice, not a tequila-brand pastiche.

---

## 5. Color palette

**Brand base (unchanged):** deep navy, steel gray, warm white, energy gold — used for all text cards, wordmark, kickers, and UI chrome in both formats.

**Story-specific accent layer (background art only, not text):**
- Warm amber/copper — bar lighting, pours, backlight (the "Bar World")
- Muted clay/terracotta — nods to the mezcal copita and agave category without copying brand-specific color
- Cool flat gray-blue — the "Label World" / rep-absence beats, deliberately less inviting than the bar world, to visually reinforce the contrast the copy is making
- Avoid: Rams royal blue + gold combination (team-color conflation risk per §0.3), any tequila-brand salt-white/lime-green cliché palette

---

## 6. Image treatment

- Photographic, cinematic, slightly warm color grade for all "Bar World" and event-adjacent shots — shallow depth of field, practical-light feel (string lights, sconces, backlit bottles), light steam/condensation detail where natural (a fresh pour, an ice-filled cup).
- Flatter, cooler, slightly desaturated treatment for "Label World" shots — intentionally less appealing, evokes a sterile brand-ops or supply-closet feel.
- No text baked into any generated image anywhere — all copy is added as a type layer after generation.
- No fake logos, no fabricated Dos Hombres wordmark, no fabricated NFL/Rams marks, no watermarks, no small corner icons or production slates.
- Human presence, where used at all, is hands-only or fully silhouetted/backlit with no visible facial features — never a posed "two men at a bar" portrait that could read as an attempt at Aaron Paul/Bryan Cranston likenesses.

---

## 7. Instagram safe-margin instructions

**Reel (1080x1920):** Keep all text within x: 80px–1000px and y: 250px–1550px. The top ~230px is covered by the account name/follow button/audio bar in the app UI; the bottom ~370px is covered by caption text, like/comment/share/save icons, and the audio disc. Punch-beat centered text (beats 4, 8) should sit roughly at y: 850–1100 (true vertical center of the safe zone) so it reads clearly even if the viewer has the volume/caption bar showing.

**Carousel (1080x1350):** Standard JustPreneur margin — 72px minimum on all sides for any text or wordmark; keep the top ~45% of each interior slide (2–6) clear and low-detail for the kicker/body-copy overlay as in prior carousels; cover (Slide 1) headline block centered with equal top/bottom breathing room; CTA slide (7) wordmark centered in the bottom safe margin, never touching the edge.

---

## 8. Slide-to-slide / beat-to-beat consistency rules

- Every beat/slide uses the same navy scrim treatment and the same grotesk type family — no font or scrim-style switching mid-piece.
- The Label World ↔ Bar World color contrast (cool flat gray-blue vs. warm amber/copper) must be visually consistent every time each world reappears, so a viewer recognizes "we're back in the cold world" or "we're back in the warm world" without rereading the text.
- JustPreneur wordmark treatment (size, position, opacity) stays identical across all Reel beats 2–9, then scales up only for the beat-10 sting — and stays identical in size/position across all 7 carousel slides.
- Kicker label style (all-caps, gold, small, letter-spaced) is identical across all 6 non-cover, non-CTA carousel slides.

---

## 9. Accessibility and contrast check

- Warm-white text (#F5F3EE-equivalent) on navy scrim (#0B1E32-equivalent) at ≥70% scrim opacity comfortably clears WCAG AA contrast for large text (≥18pt-equivalent at Reel/carousel scale).
- Gold kicker text (energy-gold, e.g., #D4A017-equivalent) is used only for short, large-size labels (kickers, "GO FOR DOS!" emphasis word if isolated) — never for full paragraph body copy, since gold-on-navy body text at small sizes drops below comfortable contrast on compressed mobile screens.
- No text is ever placed directly over high-frequency background detail (steam texture, crowd texture, bottle glass) without the navy scrim between them — scrim is mandatory on every beat/slide, not optional.
- Minimum single-line text size for Reel kinetic beats should render at no less than ~64px cap-height equivalent at 1080px width, so it's legible on a phone at arm's length mid-scroll.

---

## 10. Image-generation prompts

**IMAGES NOT YET GENERATED — DRAFT MODE.** All prompts below are written for later execution via `scripts/generate_images.py` (or manual submission to an image tool) once an API key is available locally. They are saved verbatim in `image-jobs.json` in this same project folder. Do not run the generation script in this environment.

Full prompt text lives in `image-jobs.json`. Summary of what each job covers:

- **Reel backgrounds (10, 1080x1920):** bg-reel-1-label-world, bg-reel-2-bar-exterior, bg-reel-3-stadium-night, bg-reel-4-empty-rep, bg-reel-5-pouring-hands, bg-reel-6-crowd-toast, bg-reel-7-label-vs-bar-split, bg-reel-8-founder-silhouette, bg-reel-9-reflective-desk, bg-reel-10-wordmark-sting.
- **Carousel backgrounds (7, 1080x1350):** bg-carousel-1-cover, bg-carousel-2-the-move, bg-carousel-3-the-stage, bg-carousel-4-the-choice, bg-carousel-5-the-moment, bg-carousel-6-the-lesson, bg-carousel-7-cta.

Every prompt in `image-jobs.json` explicitly states: required dimensions, subject/environment, composition, lighting/mood, brand palette, clear negative space reserved for exact copy, and a negative-constraints clause banning illegible text, fake logos, real-person likenesses, Rams/NFL team branding, duplicate people, malformed hands, and clutter.

---

## 11. Layout prompt — where exact text goes after image generation

Use this as the standing instruction for whoever assembles the final Reel/carousel in an editing or design tool once images exist:

**For the Reel:**
1. Place each `bg-reel-*` image (or real substituted footage) as the full-bleed background for its corresponding beat, per the timing table in §3, using a slow Ken-Burns push-in (105%→112% scale) over each beat's duration if using a static image rather than motion footage.
2. Add a soft navy gradient scrim (bottom-anchored for lower-third beats, full-frame vignette for centered punch beats) at 60–75% opacity before placing type.
3. Set the exact on-screen text for that beat (word-for-word from the approved copy in §3 — do not paraphrase) in the grotesk bold/black weight, warm-white color, centered horizontally, positioned per the "Text placement" column in §3, within the safe margins in §7.
4. Add the small JustPreneur wordmark, gold, top-safe-zone corner, consistent position/opacity, beats 2 through 9.
5. On beat 10, cut to bg-reel-10-wordmark-sting, remove the corner wordmark, and center a large JustPreneur wordmark/logo lockup with the final line "Save this. Go find that moment." positioned just above it.
6. Cut cleanly between beats on the beat boundary timestamps in §3 — no crossfades longer than ~4 frames, this is a punchy kinetic-text edit, not a slow dissolve piece.

**For the Carousel (fallback):**
1. Place each `bg-carousel-*` image as the lower-two-thirds visual on its slide.
2. Reserve the top ~45% of each interior slide, and the full slide for the cover/CTA per §2, as clean negative space.
3. Set kicker (all-caps, gold, small, letter-spaced) at the top of slides 2–6 exactly as labeled in the "Role" column of §3's carousel table.
4. Set body copy directly below the kicker, warm-white, word-for-word from the "Copy" column in §3 — do not paraphrase or shorten the approved lines.
5. Set the full headline centered on Slide 1 with no kicker.
6. Place the small JustPreneur wordmark centered in the bottom safe margin on every slide, identical position/size across all 7.

---

## Open design decisions for local finish

- **Reel vs. real footage:** confirm whether the team can source actual event photos/video before defaulting to the fully-generated b-roll version described here (see §0.6).
- **"GO FOR DOS!" treatment:** on Reel beat 6 and Carousel Slide 5, consider isolating "GO FOR DOS!" in gold within the otherwise warm-white line for emphasis, since it's a direct quoted creation name — confirm this reads as a quote and not as a fabricated tagline being presented as JustPreneur's own.
- **Reel length:** copy timing sums to 38 seconds across 10 beats; confirm final cut isn't padded past 40 seconds, which can hurt Reels retention.
