# Design Brief — Supabase / Turso "Build vs. Buy, Decided by Data"

**IMAGES NOT YET GENERATED — prompts only, draft mode.** No image-generation API key is available in this cloud environment. `scripts/generate_images.py` was NOT executed. Prompts are saved in `image-jobs.json` in this folder, ready for later local execution via `/justpreneur-finish`:
`python3 scripts/generate_images.py --jobs "projects/supabase-turso-build-vs-buy/image-jobs.json" --out "projects/supabase-turso-build-vs-buy/images"`

## Creative concept
Premium business/tech editorial carousel built around two hero visual motifs: a literal "fork in the road" (Build fading out in steel-gray vs. Buy lit up in energy-gold, slide 3) and a rising adoption-stat motif (human-developer icon fading → AI-agent node icon brightening, 60%→70%, slide 2). Restrained gradients, architectural line graphics, one dominant light source per slide. No stock photos of people, no icon soup, no fake logos.

## Canvas & palette
- Canvas: 1080x1350, identical across all 8 slides.
- Deep navy #0B1220 (background), steel gray #4A5568/#9AA3AE (secondary/fading), warm white #F5F1E8 (primary text), energy gold #D4A33E (accent/stat/"lit" path).
- Safe margins: 60px left/right, 80px top, 100px bottom (for JustPreneur wordmark).

## Typography
- Headline: bold geometric/grotesk sans (Inter Bold/Black, Söhne Bold, or Neue Montreal Bold), warm-white, tight tracking.
- Stats/numerals (slides 2, 6): same family, Black weight, energy-gold, larger than body headline.
- Supporting copy: Regular/Medium weight, steel-gray or warm-white at ~85% opacity.
- JustPreneur wordmark: small, consistent, bottom-center every slide.

## Per-slide placement notes
1. Cover — 2-line headline, centered 35-55% height, wordmark bottom-center.
2. Stat — large "70%" / "60%→70%" numeral dominant upper half in gold; supporting sentence below.
3. Fork — "Build" over dim left path, "Buy" over lit right path at 55-65% height band.
4. Buy decision — date-led headline top-center, supporting sentence in lower two-thirds.
5. Who/what acquired — headline top third, three stacked supporting lines below.
6. Capital raise — stacked stat lines ($150M top, $500M Series F/~$10.5B below), investor names smallest.
7. Takeaway — three-line reflective headline centered in negative space, no supporting line.
8. CTA — CTA headline, question line, "Save this..." line, wordmark slightly larger as closer.

## Image treatment
Abstract/architectural backgrounds only — no literal stock photography, no illustrated humans/faces/hands, no fake UI screenshots or logos. Consistent warm-gold single light source per slide, directed away from the text-safe zone. Subtle grain/vignette, identical intensity across slides.

## Consistency & accessibility
Identical canvas, palette, type system, wordmark placement, and safe margins across all 8 slides. Contrast checked: warm-white/navy ~13:1, gold/navy ~7:1 (large text only), steel-gray/navy ~4.5:1+ (secondary/tertiary copy only).

## Text-overlay instructions (post-generation, design tool)
Apply approved copy exactly as punctuated via text layer (not baked into AI image generation) — headline ~64-80px warm-white, supporting ~36-44px steel-gray, stat numerals ~96-120px gold on slides 2/6, "Build"/"Buy" single-word labels on slide 3. JustPreneur wordmark uses the approved brand logo asset (not a generated/fake logo) — asset path needs sourcing before local finishing.

## Open questions for local finishing
- Need sourced JustPreneur logo asset path for the wordmark layer.
- No real photo/logo of Glauber Costa, Supabase, or Turso was used — slide 5 intentionally stays abstract; confirm acceptable or substitute an approved real asset once available.
