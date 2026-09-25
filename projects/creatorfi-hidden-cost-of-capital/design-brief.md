# Design Brief — "No Equity. No IP. Still Expensive."
**Project:** creatorfi-hidden-cost-of-capital
**Format:** Instagram carousel, 9 slides, portrait 1080 x 1350
**Status: DRAFT MODE — no images have been generated yet.** This brief and the accompanying `image-jobs.json` are ready to run locally via `/justpreneur-finish` once an image-generation API key is available. No `scripts/generate_images.py` run was attempted in this environment.

---

## 1. Overall Creative Concept

Treat this like a financial-explainer graphic from a modern business publication (think: a Morning Brew / Axios-style "chart-led" explainer, not a motivational-quote template). The visual system should feel analytical and credible: clean grid structure, restrained color blocking, data-forward typography for numbers, and a deliberate "sourced commentary" visual break for the two slides that carry Billy Huang's interview claim. No coins, chains, or crypto iconography anywhere — CreatorFi's crypto/stablecoin history is intentionally omitted from the copy, and the visuals must not reintroduce it.

Three visual "modes" recur across the 9 slides so the carousel reads as one coherent system while still marking the shift into sourced-commentary territory:

- **Mode A — Primary Navy** (slides 1, 3, 7, 9): deep navy background, warm white type, gold accents. Used for cover, mechanics, reframe, and takeaway — the brand's authoritative voice.
- **Mode B — Primary Warm White** (slides 2, 4, 8): warm white/steel gray background, navy type, gold accents. Used for the raise stats, the pitch pivot, and the framework — the "let's look at the facts" register.
- **Mode C — Quote/Attribution** (slides 5, 6 ONLY): a visually distinct charcoal/steel-gray gradient background with an oversized translucent quotation-mark motif. This is the one deliberate break in the system — it must read immediately, even at a glance, as "this is someone's stated commentary, not a company fact sheet."

---

## 2. Composition & Focal Hierarchy (applies to every slide unless noted)

1. **JustPreneur wordmark** — fixed lockup position, top-center, 56–64px cap-height text, always present, always legible, always correctly spelled "JustPreneur."
2. **Headline/primary claim** — largest text block, upper-to-mid frame, left-aligned within safe margins (centered only on slide 1 cover and slide 9 CTA for a bookend effect).
3. **Supporting copy** — secondary weight, directly beneath headline, generous line-height for mobile legibility.
4. **Numeric/data callouts** (slides 2, 3, 8) — set apart in their own visual block (card, badge, or rule-divided row) so figures are scannable without reading full sentences.
5. **Attribution kicker** (slides 5, 6 only) — a full-width label bar, NOT a small corner tag, set in gold uppercase, positioned directly above the quoted claim, sized for easy mobile reading (minimum 32px cap-height at 1080px width). This line must never be shortened for design's sake — publish it in full both times:
   - Slide 5: "ACCORDING TO INTERVIEW COMMENTARY FROM CEO BILLY HUANG — NOT CREATORFI'S OFFICIAL PRESS MATERIALS"
   - Slide 6: "PER THE SAME HUANG INTERVIEW COMMENTARY"
6. **Background texture/photo** — lowest visual priority, always subordinate to text contrast; generous flat negative space behind every text block.

---

## 3. Slide-by-Slide Copy Placement, Imagery, and Branding

### Slide 1 — Cover (Mode A, bg asset: `bg-cover`)
- Background: `bg-cover` (navy, abstract ascending line-chart texture), full bleed.
- JustPreneur wordmark: top-center, warm white.
- Headline: "NO EQUITY. NO IP. STILL EXPENSIVE." — centered, huge, warm white, all caps, tight tracking. Gold rule underlines "STILL EXPENSIVE."
- Subheadline: "What CreatorFi's $45M raise teaches about the real cost of capital." — centered below headline, steel-gray/warm-white at 80% opacity, smaller weight.
- No other elements. Maximum negative space around headline.

### Slide 2 — The Raise (Mode B, bg asset: `bg-primary-white`)
- JustPreneur wordmark: top-center, navy.
- Two **visually distinct, side-by-side (or stacked on narrow safe-width) stat blocks** — never combined into one number:
  - Block 1: solid gold-filled card, navy numerals "$45M", label beneath in navy: "RAISED"
  - A small connecting element (thin arrow or "+" glyph, not a plus-sign merging the numbers) between the two blocks, labeled "CAPACITY TO SCALE"
  - Block 2: outline-only card (gold border, warm-white fill), gold or navy numerals "$100M", label beneath: "MORE IN CAPACITY"
- Below both blocks, supporting copy in navy, smaller weight: "Debt led by VerisFi Capital, with Intrinsic Capital and Kamui Finance as mezzanine lenders. Equity led by EV3 (Escape Velocity)."
- Critical: $45M and $100M must remain two separate, clearly labeled figures — no "$145M" or merged total anywhere in the design.

### Slide 3 — How It Works (Mode A, bg asset: `bg-primary-navy`)
- JustPreneur wordmark: top-center, warm white.
- Headline copy: "CreatorFi advances $500K–$5M against a creator's recurring platform income — YouTube AdSense, streaming royalties, TikTok Shop, Roblox/Fortnite earnings." — the dollar range "$500K–$5M" set in gold, rest in warm white.
- Four simple generic line-icons (no brand logos — do not render YouTube/TikTok/Roblox marks) representing: ad revenue (play-triangle-in-circle, generic), streaming royalty (simple music note), commerce (simple shopping-bag outline), gaming (simple controller outline) — small, evenly spaced in a single row, steel-gray line weight, purely illustrative, not literal brand marks.
- Supporting copy beneath: "Repaid from that same revenue. No equity stake. No IP handed over." — smaller weight, warm white.

### Slide 4 — The Pitch (Mode B, bg asset: `bg-primary-white`)
- JustPreneur wordmark: top-center, navy.
- Line 1: "That's the headline: access capital without giving up ownership." — navy, medium weight.
- Line 2 (the pivot): "But 'no equity' answers one question. It doesn't answer the one that matters — what's the real cost?" — "what's the real cost?" set larger/bolder in gold to visually signal the pivot into the article's real argument.
- Optional visual device: a thin gold underline/arrow beneath "no equity" that visually redirects toward "the real cost" phrase — subtle, not a literal icon.

### Slide 5 — The Hidden Variable, Part 1 (Mode C — QUOTE TREATMENT, bg asset: `bg-quote-attribution`)
- Background: `bg-quote-attribution` — charcoal/steel-gray gradient, oversized translucent gold quotation-mark glyph bleeding off the top-left edge, deliberately different from Modes A/B so the shift is unmistakable even scrolling quickly.
- JustPreneur wordmark: top-center, warm white (kept consistent in position even though the background mode changes).
- **Attribution kicker bar** (full width, gold, uppercase, readable size — NOT a small corner tag): "ACCORDING TO INTERVIEW COMMENTARY FROM CEO BILLY HUANG — NOT CREATORFI'S OFFICIAL PRESS MATERIALS" — positioned directly above the quote body, own visual band so it cannot be missed or mistaken for body copy.
- Quote body beneath, in warm white, quote-style (can use a slightly heavier or serif-influenced weight to differentiate from Mode A/B body text): "...some deals involve CreatorFi taking roughly 50% of a customer's specified platform revenue."
- No photo of Billy Huang (no approved photo asset provided — do not fabricate a likeness).

### Slide 6 — The Hidden Variable, Part 2 (Mode C — QUOTE TREATMENT, bg asset: `bg-quote-attribution`, same asset reused for visual continuity of the two-part quote)
- Identical structural treatment to Slide 5 for consistency (same background asset, same kicker-bar position, same quote typography) so slides 5–6 read as a matched pair.
- **Attribution kicker bar**: "PER THE SAME HUANG INTERVIEW COMMENTARY" — full size, same treatment as slide 5's kicker, not trimmed or shrunk.
- Quote body: "...in some cases, that revenue share is paired with a deadline to produce new IP (e.g., a new music release) — or a requirement to carry a life insurance policy where key-person risk is high."

### Slide 7 — The Reframe (Mode A, bg asset: `bg-primary-navy`)
- JustPreneur wordmark: top-center, warm white.
- Headline: "No equity ≠ cheap." — very large, warm white, with the "≠" glyph rendered in gold for emphasis.
- Line 2: "A 50% revenue cut, held for years, can cost more than dilution ever would." — medium weight, warm white.
- Line 3: "The absence of a term sheet clause isn't the same as the absence of a price." — slightly smaller, steel-gray/warm-white at 85% opacity, positioned as a closing aphorism at the bottom third.

### Slide 8 — The Framework: Before You Sign (Mode B, bg asset: `bg-primary-white`)
- JustPreneur wordmark: top-center, navy.
- Kicker line: "ASK FOUR QUESTIONS:" — navy, bold, small caps.
- Four-item numbered checklist, each item with a filled gold circle numeral badge (1–4) and navy text, generous vertical spacing for mobile tap-scan readability:
  1. What % of revenue am I giving up?
  2. For how long — until repaid, or indefinitely?
  3. What obligations come attached (deadlines, insurance, exclusivity)?
  4. What happens if I miss a target?
- Clean checklist/card layout — this slide is the "save-worthy" utility slide, so prioritize scanability over decoration.

### Slide 9 — Takeaway + CTA (Mode A, bg asset: `bg-primary-navy`, bookend with slide 1)
- JustPreneur wordmark: top-center, warm white.
- Headline: "'No equity' is a marketing line, not a cost calculation." — centered, large, warm white, quotation marks around "No equity" only (thin, not the oversized Mode C motif — keep this visually distinct from the slide 5/6 quote treatment so it doesn't get confused with sourced commentary; this line is JustPreneur's own editorial voice, not attributed to Huang).
- CTA line beneath: "Save this post. Run the math before you sign anything." — gold, bold, centered.
- Simple bookmark/save line-icon above or beside the CTA line (single, small, functional — not decorative clutter).

---

## 4. Typography Direction

- **Headlines:** Bold geometric/grotesque sans, heavy weight — direction: Neue Haas Grotesk Display Bold / Inter Black / Founders Grotesk Bold. All-caps for slide 1 and kicker labels; sentence case for conversational headlines (slides 4, 7, 9).
- **Body/supporting copy:** Same family, Regular/Medium weight, generous line-height (1.3–1.4x) for mobile legibility.
- **Numerals/financial figures ($45M, $100M, $500K–$5M, 50%):** A tabular/monospace-influenced numeral treatment (direction: IBM Plex Mono or Inter Tight tabular figures) to visually flag "this is a hard number" and reinforce the financial-explainer tone.
- **Attribution kicker (slides 5, 6):** Same grotesque family, uppercase, medium-bold weight, wide letter-spacing (~4–6%) so it reads as a labeled citation band, not body prose — but never below 32px cap-height at 1080px canvas width.
- Minimum body text size: 44px at 1080px canvas width for any sentence-length copy; minimum 32px for the attribution kicker; headline sizes scale up from there. No copy smaller than these floors anywhere in the carousel.

---

## 5. Color Palette

| Role | Color | Hex |
|---|---|---|
| Deep Navy (primary dark bg / dark text on light bg) | Deep Navy | `#0B1B33` |
| Steel Gray (secondary text, Mode C backgrounds, icon strokes) | Steel Gray | `#3D4652` |
| Warm White (primary light bg / light text on dark bg) | Warm White | `#F6F2E9` |
| Energy Gold (accent, numerals, CTAs, kicker labels) | Energy Gold | `#D9A441` |
| Quote-mode gradient base (slides 5–6 only) | Charcoal-Steel gradient | `#23282F` → `#3D4652` |

No additional colors. No crypto-associated colors/motifs (no neon greens, no coin-gold gradients meant to evoke crypto iconography — the Energy Gold here reads as "premium financial accent," styled matte/flat, not metallic-coin-like).

---

## 6. Image Treatment

- All background imagery is abstract/textural — line-chart motifs, subtle grid patterns, soft gradient fields, paper-grain or noise texture at very low opacity for premium print-like feel. No literal photography of people (no approved photo of Billy Huang or any subject was supplied — do not generate a likeness).
- No brand logos of YouTube, TikTok, Roblox, Fortnite, or any named lender/investor (VerisFi, Intrinsic Capital, Kamui Finance, EV3) — these are named only in text, never depicted as fabricated logos.
- No blockchain, coin, token, or ledger-chain imagery anywhere, per instruction — the crypto/stablecoin chapter of CreatorFi's history is deliberately excluded from the copy and must not leak into visuals.
- Icons (slide 3 revenue streams, slide 8 numeral badges, slide 9 save icon) are simple, flat, single-color line icons — generic representations only, kept minimal so they never compete with text.
- Every background must be generated (or art-directed) with a clear, flat negative-space zone sized to the safe-margin text blocks described above — text will be added in the design tool, not baked into the AI-generated image.

---

## 7. Instagram Safe-Margin Instructions

- Canvas: 1080 x 1350px (portrait, 4:5).
- Safe margins: minimum 96px left/right, 150px top (below profile/username UI overlap zone), 180px bottom (above caption/like-bar UI overlap zone and swipe-indicator dots).
- All text, the JustPreneur wordmark, and the attribution kicker bars must sit fully inside these margins on every slide — nothing meaningful within 96px of the left/right edges or 150px/180px of the top/bottom edges.
- Background art may bleed fully to the canvas edge; only text and logo lockups must respect the safe zone.

---

## 8. Slide-to-Slide Consistency Rules

1. JustPreneur wordmark: identical size, identical top-center position, on every slide (color flips navy↔warm-white depending on background mode, position never moves).
2. Exactly three background modes (A/Navy, B/Warm White, C/Quote) — no slide introduces a fourth background treatment.
3. Mode C (charcoal quote background + quotation-mark motif) is reserved exclusively for slides 5 and 6 — it must not appear on any other slide, and no other slide may borrow its quotation-mark motif, so the "this is sourced commentary" signal stays unambiguous.
4. Gold is the only accent color used for numerals, CTAs, and kicker labels across all 9 slides — consistent accent logic reinforces it as "the financial-detail color" throughout.
5. Attribution kicker bars on slides 5 and 6 use identical typography, size, and band treatment (only the copy differs) so they read as a matched two-part citation.
6. Numeral treatment (tabular/mono-influenced figures) is used consistently for every hard number across the carousel: $45M, $100M, $500K–$5M, 50%, and the "1–4" framework badges.

---

## 9. Accessibility & Contrast Check

- Warm white (`#F6F2E9`) text on Deep Navy (`#0B1B33`) background: contrast ratio ≈ 13.9:1 — passes WCAG AAA for body text.
- Deep Navy (`#0B1B33`) text on Warm White (`#F6F2E9`) background: same ratio, passes AAA.
- Energy Gold (`#D9A441`) on Deep Navy: contrast ratio ≈ 6.3:1 — passes AA for large text/headlines; gold is used only for large/bold text (numerals, headlines, kickers), never for small body copy, to stay safely above threshold.
- Energy Gold on Charcoal-Steel gradient (Mode C, slides 5–6): verify at design time that gold text sits on the darker end of the gradient (`#23282F`) for the attribution kicker, giving contrast ≈ 7:1+; avoid placing gold text over the lighter gradient stop.
- Minimum type sizes specified in Section 4 (44px body / 32px kicker floor at 1080px width) protect legibility on a phone screen at typical thumb-scroll viewing distance.
- No text is placed over high-frequency background texture areas — all text sits on flat or near-flat negative-space zones per Section 6.

---

## 10. Image-Generation Prompts

Four reusable background assets cover all 9 slides (see mapping above). Saved as structured jobs in `image-jobs.json` in this folder. **Images have not been generated in this draft-mode session** — no API key is available in this environment, and `scripts/generate_images.py` was intentionally not run. Run it locally via `/justpreneur-finish` when ready.

### `bg-cover` (Slide 1)
1080 x 1350px. Abstract premium financial-editorial background: deep navy (#0B1B33) base with a subtle, elegant ascending line-chart motif sweeping from lower-left to upper-right, rendered in faint steel-gray (#3D4652) linework at low opacity, plus a very fine grid texture in the background for a data/analytics feel. Soft directional lighting suggesting a single light source from the upper right, giving gentle depth without glare. Mood: confident, analytical, premium business publication — not corporate-stock-photo, not sensational. No text, no numbers, no logos, no coins, no blockchain or crypto imagery, no people. Large flat, uncluttered negative space across the vertical center and lower third of the frame for a bold headline and subheadline to be added afterward in a design tool. No illegible text, no fake logos, no duplicate elements, no clutter.

### `bg-primary-navy` (Slides 3, 7, 9)
1080 x 1350px. Minimal deep navy (#0B1B33) background with a very subtle fine-line grid or graph-paper texture at low opacity in steel gray (#3D4652), evoking a financial ledger/analytics feel without being literal. Even, soft lighting, no strong gradients or hotspots. Mood: calm, authoritative, analytical business tone. No text, no numbers, no icons, no logos, no coins or blockchain motifs, no people. Generous flat negative space across the full frame so multiple text blocks and small icon rows can be added afterward in a design tool. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter.

### `bg-primary-white` (Slides 2, 4, 8)
1080 x 1350px. Minimal warm white (#F6F2E9) background with an extremely subtle paper-grain texture and a faint steel-gray (#3D4652) fine-line grid pattern at very low opacity in the upper portion of the frame, evoking a clean financial report or ledger page. Soft, even lighting, no harsh shadows. Mood: clean, premium, analytical — like a page from a modern business magazine. No text, no numbers, no icons, no logos, no coins or blockchain motifs, no people. Generous flat negative space through the full frame for stat cards, checklist items, and body copy to be added afterward in a design tool. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter.

### `bg-quote-attribution` (Slides 5, 6 — reused for both to form a matched pair)
1080 x 1350px. Distinct charcoal-to-steel-gray gradient background (from #23282F at the top to #3D4652 lower down), featuring one oversized, softly translucent gold (#D9A441) quotation-mark glyph bleeding off the upper-left edge of the frame at low opacity — a single elegant typographic quotation mark shape, not a decorative flourish, not literal punctuation clipart. Subtle soft-focus vignette toward the edges to keep the center-to-lower frame clean. Mood: still premium and analytical, but visually distinct from the navy/white slides — signals "this is a quoted statement," not a company fact sheet. No text, no numbers, no icons, no logos, no coins or blockchain motifs, no people, no photo of any individual. Generous flat negative space in the lower two-thirds of the frame for an attribution kicker bar and quote body text to be added afterward in a design tool. No illegible text, no fake logos, no duplicate people, no malformed hands, no clutter.

---

## 11. Layout Prompt — Exact Text to Add After Image Generation

Apply this text, positioning, and hierarchy exactly once backgrounds are generated. Do not alter wording from the approved copy file. Wordmark reads "JustPreneur" (verify spelling/casing against brand assets before finalizing) on every slide, top-center, per Section 3.

1. **Slide 1** (on `bg-cover`): Headline "NO EQUITY. NO IP. STILL EXPENSIVE." centered, warm white, all caps, gold underline beneath "STILL EXPENSIVE." Subheadline beneath, centered: "What CreatorFi's $45M raise teaches about the real cost of capital."
2. **Slide 2** (on `bg-primary-white`): Two stat blocks — gold-filled card "$45M / RAISED" and gold-outline card "$100M / MORE IN CAPACITY" — connected by a small "+" or arrow glyph labeled "CAPACITY TO SCALE." Beneath both: "Debt led by VerisFi Capital, with Intrinsic Capital and Kamui Finance as mezzanine lenders. Equity led by EV3 (Escape Velocity)." Keep $45M and $100M visually and numerically separate — never sum or merge them.
3. **Slide 3** (on `bg-primary-navy`): Headline with "$500K–$5M" in gold: "CreatorFi advances $500K–$5M against a creator's recurring platform income — YouTube AdSense, streaming royalties, TikTok Shop, Roblox/Fortnite earnings." Four small generic line icons in a row beneath (ad, music, commerce, gaming — no brand logos). Supporting line beneath: "Repaid from that same revenue. No equity stake. No IP handed over."
4. **Slide 4** (on `bg-primary-white`): "That's the headline: access capital without giving up ownership." then "But 'no equity' answers one question. It doesn't answer the one that matters — what's the real cost?" with "what's the real cost?" enlarged/gold.
5. **Slide 5** (on `bg-quote-attribution`): Full attribution kicker bar (gold, uppercase, full size, not trimmed): "ACCORDING TO INTERVIEW COMMENTARY FROM CEO BILLY HUANG — NOT CREATORFI'S OFFICIAL PRESS MATERIALS." Beneath it, quote body in warm white: "...some deals involve CreatorFi taking roughly 50% of a customer's specified platform revenue."
6. **Slide 6** (on `bg-quote-attribution`): Full attribution kicker bar, same treatment as slide 5, full size, not trimmed: "PER THE SAME HUANG INTERVIEW COMMENTARY." Beneath it, quote body: "...in some cases, that revenue share is paired with a deadline to produce new IP (e.g., a new music release) — or a requirement to carry a life insurance policy where key-person risk is high."
7. **Slide 7** (on `bg-primary-navy`): "No equity ≠ cheap." (large, "≠" in gold). "A 50% revenue cut, held for years, can cost more than dilution ever would." "The absence of a term sheet clause isn't the same as the absence of a price." (smaller, bottom third).
8. **Slide 8** (on `bg-primary-white`): Kicker "ASK FOUR QUESTIONS:" then numbered list with gold circle badges 1–4: "What % of revenue am I giving up?" / "For how long — until repaid, or indefinitely?" / "What obligations come attached (deadlines, insurance, exclusivity)?" / "What happens if I miss a target?"
9. **Slide 9** (on `bg-primary-navy`): "'No equity' is a marketing line, not a cost calculation." (centered, warm white, thin quote marks only around "No equity," visually distinct from the slide 5/6 quote motif). Beneath, gold CTA: "Save this post. Run the math before you sign anything." Small bookmark icon near CTA.

No slide should receive any additional copy beyond what's listed above (no counters, dates, citations beyond the two Huang attribution lines, or production marks).
