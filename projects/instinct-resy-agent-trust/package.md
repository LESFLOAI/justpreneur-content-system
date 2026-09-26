# JustPreneur — Draft Package: Instinct/Resy AI-Agent Trust Story

**Target posting date/slot:** 2026-09-26, 10:00 AM
**Status:** DRAFT READY — needs local finish (images not yet generated, no API key in cloud environment)
**QC Verdict:** PASS WITH CORRECTIONS (corrections applied below)

---

## 1. Facts Summary (Approved Facts Block, verified by Fact Verifier)

Venture capital investor J.C. Bahr-de Stefano — a Principal at Better Tomorrow Ventures (BTV), a fintech-focused venture fund, and a former Affirm employee — asked his personal AI assistant, Instinct, to secure a reservation at 4 Charles Prime Rib, a West Village (NYC) steakhouse where reservations are known to disappear within seconds of release. According to CNN Business (published September 23, 2026), Instinct pinged Resy's platform "hundreds of times every hour of the day" while searching for the table, which triggered Resy's anti-bot defenses and locked Bahr-de Stefano out of his own Resy account. Resy told CNN it "does not currently permit unapproved third-party bots or agents to independently access or interact with the Resy platform." Per CNN, Bahr-de Stefano's account has since been reinstated, and he said it was his first and last time using an AI agent to book a reservation.

Instinct, a personal AI-assistant app, announced on August 26, 2026 that it had raised a $250 million Series B round — co-led by Index Ventures and Benchmark — at a $2.5 billion valuation, bringing its total funding to date to $350 million (these two figures are kept distinct, never conflated). Instinct is made by Spear Street Technology, founded in 2025 by Noah Shinn (23, ex-Sierra).

**Deliberately omitted (unverified or off-limits):** exact day-count between the funding announcement and the lockout; any OpenTable comment; granular ping-rate figures beyond "hundreds of times every hour"; a specific CNN byline; named/detailed other alleged victims; the investor's name, photo, or direct tag (private individual — referenced by role only).

---

## 2. Headline

**Your AI Agent Doesn't Know the Rules You Agreed To**

(Alt options considered: "A VC's AI Assistant Got Him Locked Out of His Own Account" / "Nobody Has Approved AI Agents Yet — Act Like It")

---

## 3. Slide Copy (7-slide carousel)

**Slide 1 — Cover / The Ask**
Your AI Agent Doesn't Know the Rules You Agreed To
A venture capital investor asked his AI assistant to book him a table at a nearly impossible-to-get NYC steakhouse.

**Slide 2 — The Agent's Behavior**
The assistant — an app called Instinct — went to work. It pinged the reservation platform, Resy, hundreds of times every hour, hunting for an opening at a restaurant where tables vanish within seconds of release.

**Slide 3 — The Platform's Defense Response**
Resy's systems read that pattern as an attack. The platform says it "does not currently permit unapproved third-party bots or agents" on its platform — and at machine speed, the agent looked exactly like one.

**Slide 4 — The Lockout**
Resy locked the account. Not the AI's account. His.

**Slide 5 — The Reinstatement**
Access was eventually restored. But for a stretch, a routine dinner reservation cost him control of his own account.

**Slide 6 — His Own Reaction**
His response, afterward: it was the first — and last — time he'd let an AI agent handle a booking for him.

**Slide 7 — Builder Takeaway + Pull Quote**
The gap here isn't what the AI could do. It's that no platform has written the rulebook yet for agents acting with your full authority. Before you connect an AI agent to anything business-critical — booking, CRM, ad accounts, scheduling — know what it's doing at machine speed, and what that platform's tolerance for it actually is.

> "The account, the access, and the consequences are still yours."

---

## 4. Final Caption (QC-corrected)

A venture capitalist wanted a dinner reservation. His AI assistant wanted it at machine speed.

Instinct — an AI personal-assistant app that recently raised a high-profile $250M Series B (co-led by Index Ventures and Benchmark, at a $2.5B valuation) — was asked by a Principal at Better Tomorrow Ventures to book a table at 4 Charles Prime Rib, a West Village steakhouse where reservations are gone within seconds of release.

Per CNN Business, the assistant pinged Resy's platform hundreds of times every hour while searching for an opening. Resy's anti-bot defenses read that as an attack and locked him out of his own account — access was later reinstated.

Resy has been clear about where it stands: it "does not currently permit unapproved third-party bots or agents" on its platform. Most platforms haven't said anything yet. That's not the same as permission.

This isn't a story about a reckless AI or an overly sensitive platform. It's a preview of a question every builder needs to answer before an agent touches something business-critical: what is it actually doing at machine speed — and does the platform on the other end agree to let it?

Before you connect an AI agent to your booking system, CRM, ad accounts, or scheduling tools — audit it. The account, the access, and the consequences are still yours.

---

## 5. Hashtags (exactly 5)

#AIAgents #DigitalTrust #PlatformRisk #BuilderLessons #StartupTech

---

## 6. Accounts to Tag (QC-corrected)

| Account | Reason |
|---|---|
| **@resy** | Platform directly involved and quoted in the source reporting. **Unverified handle — confirm official account before publish.** |
| **@instinct** (or Spear Street Technology's real handle, if distinct) | Maker of the AI assistant at the center of the story. **Unverified handle — confirm official account before publish.** |
| **@indexventures** and **@benchmark** | Co-leads of Instinct's Series B, referenced in the caption. **Unverified handles — confirm official accounts before publish.** |

**Not tagged, by design:**
- **@bettertomorrowventures** — removed per QC correction. Tagging the firm alongside the role description ("a Principal at Better Tomorrow Ventures") would make the private individual materially easier to re-identify via the firm's small team page, and would drag an uninvolved third party into a personal story without consent. The firm name stays in caption text only.
- **Bahr-de Stefano** — private individual, not tagged; referenced by role only ("a Principal at Better Tomorrow Ventures," "the investor," "he").

---

## 7. Image-Generation Prompts — IMAGES NOT YET GENERATED (DRAFT MODE)

No image-generation API key exists in this cloud environment. Full design brief and all 7 prompts are in `design-brief.md` and `image-jobs.json` in this project folder, ready to run locally via:

```
python3 scripts/generate_images.py --jobs "projects/instinct-resy-agent-trust/image-jobs.json" --out "projects/instinct-resy-agent-trust/images"
```

**Creative concept:** Editorial "systems failure" visual language (Bloomberg Businessweek / The Information style, not startup-gossip or restaurant photography). A single evolving phone/app UI motif runs across Slides 1–5 (calm chat bubble → rapid-ping pattern → flagged/scanning state → locked padlock → reopened padlock). Slide 6 drops the UI for a quiet typographic breather. Slide 7 closes on a large pull quote with the UI reduced to a faint background echo.

**Palette:** Deep navy `#0E1B2A` (dominant), steel gray `#3C4A59` (secondary), warm white `#F4F1EA` (text), muted gold `#C79A4B` (restrained accent only). Deliberately no green/red — keeps the lockout from reading as alarm and the reinstatement from reading as a celebratory ending.

**Guardrails baked into every prompt:** no human figures/faces (investor is a private individual, never depicted), no restaurant/food/table imagery, no fake legible app text or logos for Instinct/Resy, no watermark.

Full per-slide prompts (see `design-brief.md` §10 for complete text):

1. **Slide 1:** Calm phone-UI chat bubble with minimal calendar/checkmark glyph, generous upper space for headline.
2. **Slide 2:** Same UI frame now showing dense pulse/ping pattern radiating from the phone — machine-speed repetition, abstract, no numbers.
3. **Slide 3:** Pulse pattern intersected by a thin gold scanning line/radar-sweep, one pulse flagged in gold.
4. **Slide 4:** Minimal padlock glyph inside the UI frame, single muted-gold accent line, no red/alarm treatment.
5. **Slide 5:** Padlock shown reopened, same muted tones — no green, no celebratory color.
6. **Slide 6:** Full-bleed navy/steel-gray field, no UI frame, extremely subtle texture only — a quiet "breather" page.
7. **Slide 7:** Faint ghosted UI frame as background echo, oversized decorative quotation mark in muted gold anchoring the pull-quote placement.

---

## 8. Pre-Finish Checklist (from QC, must close before publish)

- [x] Caption corrected — removed unsupported "in the weeks following" temporal framing
- [x] @bettertomorrowventures removed from tag list — firm name kept in caption text only
- [ ] Verify actual official handles for @resy, @instinct/Spear Street Technology, @indexventures, @benchmark before tagging
- [ ] Run `/justpreneur-finish` to generate real artwork from `image-jobs.json`
- [ ] Re-submit to QC for full checks (mobile readability, safe margins/cropping, stray marks/watermarks, cross-slide visual consistency) once real images exist — draft-mode QC pass did not cover rendered pixels
- [ ] Confirm no investor name/photo/direct tag appears anywhere in final rendered slides or caption
- [ ] Reconfirm hashtag count is exactly 5 in the final posted copy
- [ ] Human publish confirmation required before this goes live — nothing is published from this cloud run

**Recommended posting window:** Story broke via CNN Business on 2026-09-23; as of 2026-09-26 this is still within the peak relevance window for an AI/startup audience. Recommend posting within 24–48 hours of finishing (no later than 2026-09-29) to stay inside the ~1-week news-cycle relevance window.
