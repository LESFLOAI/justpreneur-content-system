# JustPreneur — Draft Package: Fever $250M Raise ("The Demand Data Flywheel")

**Target posting date/slot:** 2026-09-28 (10:00 AM)
**Status:** DRAFT READY — needs local finish (images not yet generated, no image-generation API key in cloud environment)
**Fact Verifier verdict:** Cleared with qualifications
**QC Verdict:** PASS WITH CORRECTIONS (open items listed below)

---

## 1. Facts Summary (Approved Facts Block, verified by Fact Verifier)

Fever, the live-experience and ticketing platform that owns DICE, announced on September 17, 2026 that it had raised $250 million in a primary equity financing round led by EQT, with participation from new investor Baillie Gifford, existing investor Point72 Private Investments, and other existing shareholders. Fever describes this as the largest-ever financing round for a live-entertainment technology company — a characterization from the company itself, not an independently audited industry benchmark. Trade press has calculated an implied valuation of roughly $5.2 billion based on a separate transaction (Spanish broadcaster Atresmedia's sale of its Fever stake to existing shareholder Vitruvian Partners); Fever did not officially disclose a new valuation alongside the funding round itself, so this figure should be treated as an estimate, not a confirmed number.

Separately, in June 2026, Formula 1 announced a five-year agreement naming Fever as its Official Ticketing Supplier, covering the 2027 through 2031 seasons, for general admission, hospitality, and Paddock Club tickets sold via F1.com. As of this story's publication, that platform has not yet launched — it is scheduled to go live with the 2027 F1 season.

Fever also owns and operates its own experiences (e.g., Candlelight concerts), using demand/behavioral data generated from its ticketing marketplace side to inform what it builds.

**Deliberately hedged / not stated as confirmed fact:** the ~$5.2B valuation (trade-press estimate tied to a separate share sale, not a Fever disclosure) and the "largest-ever" superlative (Fever's own characterization). Both must render in copy and design with visible hedging language, not as bare stats.

Full verification detail available from the Fact Verifier's report (not saved to a separate file this cycle).

---

## 2. Headline

**The Real Product Fever Is Selling Isn't Tickets — It's Demand Data**

(Alt options considered: "Fever's $250M Round Isn't About the Money — It's About What They Own on Both Sides of the Marketplace" / "Marketplace or Manufacturer? Why Fever Built Its Own Inventory Before Raising $250M")

---

## 3. Slide Copy (7-slide carousel + optional CTA — "The Demand Data Flywheel")

**Slide 1 — Cover**
The Real Product Fever Is Selling Isn't Tickets — It's Demand Data
*A $250M raise. The real story is what happens between the transactions.*

**Slide 2 — The Headline (hedged)**
Fever — the platform behind DICE — just raised $250M, led by EQT, with Baillie Gifford, Point72, and existing shareholders joining. Fever calls it the largest-ever financing round for a live-entertainment tech company — Fever's own characterization, not an independently audited benchmark. Trade press estimates a ~$5.2B valuation based on a separate Atresmedia share sale; Fever hasn't confirmed a new valuation alongside this round.

**Slide 3 — The Overlooked Detail**
Fever isn't only a resale marketplace. It also owns and runs its own experiences — like Candlelight concerts. Most marketplaces just take a cut. Fever also builds product.

**Slide 4 — Step One of the Loop**
Every ticket sold through Fever's marketplace is a data point — what sells out, what stalls, what price holds, what city wants what and when. That's raw demand signal, generated just by running the marketplace.

**Slide 5 — Step Two of the Loop**
That signal doesn't stay on the marketplace side. It feeds decisions about Candlelight — what to build, where, and for whom. The transactional exhaust from one business becomes the R&D input for the other.

**Slide 6 — Why It's Defensible**
A pure rake-taking marketplace earns a fee and moves on. Fever earns the fee — and keeps the signal. The marketplace keeps scaling too: in June 2026, F1 named Fever its Official Ticketing Supplier for the 2027–2031 seasons. The platform hasn't launched yet, but once live, that's years more transaction data feeding the same loop. More volume on one side, better product decisions on the other — that compounds.

**Slide 7 — Final Takeaway**
This isn't "marketplaces should launch a second product." It's this: if your marketplace data isn't feeding an owned decision somewhere, you're only collecting a rake — not building a moat.

**Slide 8 — Optional CTA**
Look at your own model. Are you capturing a signal, or just a fee? Save this to revisit when you're scoping your next product decision.

---

## 4. Final Caption

Fever just raised $250M, led by EQT, with Baillie Gifford, Point72, and existing shareholders joining. Fever calls it the largest live-entertainment tech raise ever — that's their framing, not an outside benchmark, and the widely cited ~$5.2B valuation comes from a separate share sale, not an official disclosure alongside this round.

But the number isn't the interesting part. Fever runs a resale marketplace (DICE) AND owns its own experiences (Candlelight) — and the demand data generated by the marketplace side feeds product decisions on the owned side. That's not a second revenue line. It's a feedback loop: transactions in, better-informed builds out, margin and defensibility that compound.

Worth asking of your own business: is your marketplace data just sitting there, or is it actually feeding a decision?

**CTA:** Save this for your next product/roadmap review — then ask: is our marketplace data feeding an owned decision, or just a report nobody reads?

---

## 5. Hashtags (exactly 5)

#BusinessStrategy #MarketplaceModel #DataMoat #FounderMindset #StartupNews

---

## 6. Accounts to Tag (all unverified — must confirm before publish)

| Account (unverified handle) | Reason |
|---|---|
| **@feverup** | Company at the center of the story; primary subject of the raise. **Unverified — confirm official handle before publish.** |
| **@dice_fm** | Fever-owned ticketing brand explicitly named in the approved facts. **Unverified — confirm official handle before publish.** |
| **@f1** | Counterpart in the separately verified 2027–2031 Official Ticketing Supplier deal referenced in Slide 6. **Unverified — confirm official handle before publish.** |
| **@eqtgroup** | Lead investor in the $250M round. **Unverified — confirm official handle before publish.** |
| **@point72** | Existing investor named in the round; relevant to a finance/strategy-literate audience. **Unverified — confirm official handle before publish.** |

QC flagged that it could not independently verify any of the five handles (no live lookup available) — this is a required pre-publish action, not a pass.

---

## 7. Image-Generation Prompts — IMAGES NOT YET GENERATED (DRAFT MODE)

No image-generation API key exists in this cloud environment. Full design brief and all 8 prompts are in `design-brief.md` and `image-jobs.json` in this project folder, ready to run locally via:

```
python3 scripts/generate_images.py --jobs "projects/fever-demand-data-flywheel/image-jobs.json" --out "projects/fever-demand-data-flywheel/images"
```

**Creative concept:** Premium business-media explainer register (The Information / Bloomberg Businessweek), not startup-hype. Central visual device is a flywheel/loop of two nodes — "Marketplace" (steel-gray, ticket transactions) and "Owned Experiences" (energy-gold glow, standing in for Candlelight without depicting it) — that assembles progressively across the 8 slides: unconnected (S1) → distinguished (S3) → generating particles (S4) → loop closes (S5) → scales (S6) → fully complete as hero backdrop for the pull quote (S7) → faint echo (S8, optional CTA).

**Palette:** Deep navy `#0E1B2A`, steel gray `#3C4A59` (Marketplace node), warm white `#F4F1EA` (text), energy gold `#C8A24A` (Owned Experiences node, loop glow, pull quote).

**Guardrails baked into every prompt:** abstract flat vector node/particle/loop graphics only — no real photography, no real logos or brand marks for Fever, DICE, Candlelight, EQT, Baillie Gifford, Point72, Atresmedia, or F1 (all stay in the copy layer only). Slide 6's image prompt explicitly bans racing/motorsport visual cues (cars, tracks, checkered flags, red livery) so the F1 reference never implies the ticketing platform is currently live. No watermark, no slide numbers/dates/production marks.

**Critical typography constraint (Slide 2):** The hedge sentences ("Fever's own characterization, not an independently audited benchmark" and "Trade press estimates... Fever hasn't confirmed a new valuation") must render at equal size, weight, and color to the $250M/EQT fact line — no footnote styling, no dimming, no corner/citation placement. This is specified redundantly across four sections of `design-brief.md` (Critical Constraint, Typography, Safe Margins, Accessibility) plus the per-slide layout instructions, and confirmed present by QC's direct read of the file — but has not yet been verified against rendered pixels.

Full per-slide prompts and layout-overlay text: see `design-brief.md` §10 (prompts) and §11 (exact copy placement).

---

## 8. Pre-Finish Checklist (from QC, must close before publish)

- [ ] Verify actual official handles for @feverup, @dice_fm, @f1, @eqtgroup, @point72 before tagging
- [ ] Run `/justpreneur-finish` to generate real artwork from `image-jobs.json`
- [ ] Visually inspect rendered Slide 2 for literal equal-weight/size/color/contrast parity between the two hedge sentences and the $250M/$5.2B fact lines — no footnote treatment, no dimming, no corner placement (highest fact-integrity risk in this package)
- [ ] Visually inspect Slide 6 for safe-margin compliance and legibility given its longer, reduced-size copy block
- [ ] Re-run mobile readability, safe-margin/cropping, stray-marks/watermark, and cross-slide visual-consistency checks against actual rendered images (deferred in draft-mode QC pass)
- [ ] Reconfirm no real logos, trademarks, or photography of Fever/DICE/Candlelight/EQT/Baillie Gifford/Point72/Atresmedia/F1 appear in final rendered images (prompts are clean; verify actual output matches)
- [ ] Reconfirm the F1 reference does not visually or textually imply the ticketing platform is currently live
- [ ] Confirm caption, hashtags, and tags are attached to the correct final image set before scheduling
- [ ] Human publish confirmation required before this goes live — nothing is published from this cloud run

**Recommended posting window:** The raise was announced 2026-09-17 (11 days before this draft cycle). Recommend generating final artwork and publishing as soon as possible — ideally within the next few days and no later than early-to-mid October — to stay inside the typical 2–3 week relevancy window for funding-round commentary. A weekday late-morning/lunch slot (Tue–Thu, 11am–1pm audience-local time) is the standard high-engagement window for this account's business-explainer format.
