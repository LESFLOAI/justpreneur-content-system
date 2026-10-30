# Fact Verifier Report — DoorDash / Instacart (Maplebear) Merger
Date/time checked: 2026-10-30 (AM cloud draft cycle)
Verifier: Independent Fact Verifier agent (JustPreneur)

## Process note / limitation
I was asked to read `research/2026-10-30_story-scout.md` first. My toolset in this
session (WebSearch, WebFetch, Write, SubagentHandback) has no file-system Read/Bash
access and WebFetch rejects `file://` URLs ("Invalid URL"), so I could NOT open the
Story Scout's notes file directly. I did not treat this as blocking: I independently
re-derived and checked every numbered claim in the assignment against primary/
secondary sources via WebSearch. Direct WebFetch to www.sec.gov also failed in this
session (DNS/network not permitted — "ENOTFOUND www.sec.gov"), so EDGAR primary-text
confirmation relies on search-engine extraction of the SEC exhibit/8-K text rather
than my own rendering of the raw HTML. I ran the SEC-text queries multiple times with
different phrasings; the numbers (price, ratios, dates, termination fee, closing
window) came back identical and internally consistent every time, which gives
reasonable confidence, but this residual gap should be closed by whoever has EDGAR
access before anything here is treated as beyond-doubt primary verification.
**Recommend**: orchestrator either grant this agent file/EDGAR access next cycle, or
have Story Scout paste raw filing text into its notes for direct quoting.

---

## Claim-by-claim verification

| # | Claim | Status | Notes / strongest source |
|---|---|---|---|
| 1 | Per-share mechanics: $65.00 cash per share, OR 0.3372 DoorDash shares ("Stock Exchange Ratio"), OR a mixed election of $48.75 cash + 0.0843 DoorDash shares; aggregate consideration at least 75% cash, stock capped at 25% with proration if oversubscribed; stock ratio subject to adjustment if DoorDash Class C trades at a discount to Class A before closing | **Attributed claim (high confidence, source = primary filing text via search extraction)** | DoorDash Form 8-K exhibit 99.1, [SEC EDGAR filing index](https://www.sec.gov/Archives/edgar/data/0001792789/000114036126041111/ef20084547_ex99-1.htm) and 8-K cover ([ef20084547_8k.htm](https://www.sec.gov/Archives/edgar/data/0001792789/000114036126041111/ef20084547_8k.htm)). Could not personally render raw HTML (network block); numbers repeated identically across 3 independent queries. |
| 2 | "~$100M/year combined DashPass/Instacart+ membership savings" | **Attributed claim — must be framed as the companies' own estimate, not a verified fact** | Confirmed this figure originates in the official 8-K press-release exhibit itself ("two memberships for the price of one," estimated ~$100 million/year in membership-fee savings), not an aggregator invention. It is explicitly an estimate/projection tied to a not-yet-closed deal — use "the companies estimate" or "DoorDash and Instacart project," never state as settled fact. |
| 3 | Named Instacart executive | **Correction required — do NOT use Fidji Simo as current CEO** | Current Instacart CEO is **Chris Rogers**, who succeeded Fidji Simo as CEO effective August 15, 2025 ([NOSH](https://www.nosh.com/news/2025/instacart-names-chris-rogers-as-next-ceo), [PerishableNews](https://perishablenews.com/retailfoodservice/instacart-appoints-chris-rogers-as-chief-executive-officer/)). Simo departed to lead OpenAI's applications/consumer business ([Adweek](https://www.adweek.com/commerce/chris-rogers-will-take-over-as-instacart-ceo-as-fidji-simo-heads-to-openai/)) and is reported (per TechCrunch coverage referenced in search results) to remain Instacart board chair — that board-chair detail is secondhand in my search results and should be independently re-confirmed before publication if used. **No direct quote from Chris Rogers about this specific merger was found in my research** — do not fabricate one. |
| 4 | Expected closing timeline | **Attributed claim — confirmed, not a misread** | The "end of 2027 or the first half of 2028" closing window is genuine filing/announcement language, not a secondary-source error — it recurred identically across three independently phrased searches pulling from the 8-K exhibit. Closing is explicitly conditioned on: Instacart stockholder approval (~19% of shares already committed to vote yes), HSR antitrust waiting period, and competition-authority approvals in Canada and Israel. Use "expected to close by the end of 2027 or in the first half of 2028, subject to regulatory and shareholder approval" — do not compress this into a firm date. |
| 5 | Prior Uber interest/withdrawal | **Attributed claim, sourced to unnamed people familiar with the matter — not an on-record Uber statement** | Reuters (citing WSJ) and Bloomberg reporting (via [BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2026/10/26/doordash-in-talks-to-buy-instacart-in-roughly-us17b-deal-source-says/)) say Instacart had approached Uber, held preliminary talks, and that by ~Oct 26, 2026 "Instacart's deal talks with Uber are no longer active." Neither Uber nor Instacart confirmed this on record in anything I found; Instacart declined to comment to Reuters/Bloomberg. Must attribute as "according to people familiar with the matter, per Reuters/WSJ reporting," not as confirmed fact. |
| 6 | Stock-move percentages (Instacart +7.9%, DoorDash -6.1%) | **Verified fact, but wrong date association must be fixed** | Figures confirmed via Fast Company's reported numbers (DoorDash closed -6.10%, Instacart +7.87%) cited within US reporting (Reuters/BNN Bloomberg lineage), not the Taiwanese outlet. **Critical correction: these moves happened on October 26, 2026**, the day WSJ/Reuters reported DoorDash was in "advanced talks" — they are NOT the market reaction to the October 28 signing or October 29 8-K announcement. Any copy must say the stocks moved on the talks-reports day, not on the deal-confirmation day. |
| 7 | Merger agreement dated Oct 28, 2026; 8-K filed Oct 29, 2026 | **Verified fact (high confidence)** | 8-K cover page "Date of Report (Date of earliest event reported): October 28, 2026" per search-extracted filing metadata; the press release/8-K exhibit and accompanying Q3 2026 earnings release are dated October 29, 2026, consistent with a Wednesday signing and Thursday filing. I could not independently load the raw EDGAR filing-index "Accepted" timestamp due to the network block — this is the one piece I'd still like to confirm via direct EDGAR access, though it is corroborated by multiple consistent secondary mentions. |
| Sanity check | Deal still pending as of Oct 30, 2026 (not closed/terminated/renegotiated) | **Verified / reasonable inference** | No reporting found of termination, lawsuit, regulatory block, or renegotiation as of the search date. The 8-K exhibit text includes a **$650,000,000 termination fee** payable by Instacart under specified circumstances — a detail that itself confirms this is a genuinely signed definitive agreement (not just advanced talks), and is useful missing context for the story (illustrates deal seriousness/breakup risk). Long regulatory runway (through 2027–28) means status could still change before any publication date; flag as time-sensitive. |

## Additional corrections / names
- Instacart's legal/SEC name: **Maplebear Inc.**, d/b/a Instacart, ticker **CART**. DoorDash, Inc., ticker **DASH**. Both confirmed.
- "26% premium to Instacart's Oct 22, 2026 close" — confirmed in multiple independent extractions, consistent with Oct 22 being the last trading day before the Oct 23 WSJ/Information reports of a possible sale process.
- DoorDash's financing: cash portion backed by cash on hand plus debt, including a 364-day senior unsecured bridge loan commitment letter from JPMorgan Chase; no financing condition on the deal; DoorDash intends to preserve investment-grade ratings. This is useful context not in the original claim list but strengthens credibility of the "definitive agreement" framing.
- 2021 history: DoorDash reportedly explored acquiring Instacart previously at a $40B–$50B valuation; those talks reportedly collapsed partly over price/antitrust concerns under the prior administration. This is attributed-reporting context (Reuters/Benzinga lineage), useful for a "second time's the charm" angle but must stay labeled as reported, not confirmed by either company.

## Required attribution language (for downstream copy)
- Deal terms, price, ratios, financing, termination fee, closing-timeline window → attribute to "DoorDash's SEC filing" / "the companies' joint announcement," since I could not personally render the raw primary HTML in this session.
- $100M savings figure → "DoorDash and Instacart estimate" / "the companies project" — never bare fact.
- Uber withdrawal → "according to people familiar with the matter (Reuters/WSJ)" — never stated as confirmed by Uber.
- Stock moves → tie explicitly to October 26, 2026 (talks-report reaction), separate from the October 28–29 signing.
- Any Instacart executive reference → Chris Rogers, CEO (not Fidji Simo). No quote from him should be used unless a primary source for that exact quote is located.

## Missing context that could change interpretation
- Regulatory runway is long (through 2027–2028) and explicitly contingent on HSR, Canadian, and Israeli antitrust clearance plus Instacart shareholder vote — this is not a done deal, and framing it as "DoorDash buys Instacart" without the pending/regulatory caveat would be misleading.
- The headline stock moves reporters are citing happened on rumor/report day (Oct 26), not confirmation day — conflating the two dates overstates the market's reaction to the actual signed deal.
- 2021 prior failed DoorDash–Instacart talks (antitrust-related collapse) is relevant background for any "will regulators allow this" angle.
- $650M Instacart-payable termination fee is a strong signal of deal seriousness and also a genuine downside/breakup-risk data point worth including for balance.

## Approved Facts Block (verbatim for downstream agents)

> On October 28, 2026, DoorDash, Inc. (NASDAQ: DASH) and Maplebear Inc. d/b/a Instacart (NASDAQ: CART) signed a definitive merger agreement under which DoorDash will acquire Instacart for $65.00 per share — an equity value of approximately $17 billion — representing a reported 26% premium to Instacart's October 22, 2026 closing price. DoorDash filed an 8-K disclosing the agreement on October 29, 2026. Instacart shareholders may elect to receive $65.00 in cash, 0.3372 shares of DoorDash Class A common stock, or a mixed election of $48.75 cash plus 0.0843 DoorDash shares, subject to proration so that stock consideration does not exceed 25% of total deal consideration (at least 75% cash). Instacart's board has unanimously approved the deal, and holders of roughly 19% of Instacart shares have agreed to vote in favor. The companies state the deal is expected to close by the end of 2027 or in the first half of 2028, subject to Instacart stockholder approval, expiration of the U.S. Hart-Scott-Rodino antitrust waiting period, and competition approvals in Canada and Israel; the agreement includes a $650 million termination fee payable by Instacart under specified circumstances. DoorDash and Instacart state they estimate combining DashPass and Instacart+ into a single membership would save combined members approximately $100 million per year in membership fees — an estimate from the companies, not an independently verified figure. Instacart's current CEO is Chris Rogers (since August 2025); prior CEO Fidji Simo departed to lead an applications/consumer business role at OpenAI and should not be referenced as Instacart's current CEO. According to Reuters and Wall Street Journal reporting citing people familiar with the matter, Uber had earlier held preliminary acquisition talks with Instacart that were reported as no longer active by around October 26, 2026 — this has not been confirmed on record by Uber or Instacart. On October 26, 2026 — the day WSJ/Reuters first reported DoorDash was in "advanced talks" to acquire Instacart — Instacart shares closed up approximately 7.9% and DoorDash shares closed down approximately 6.1%; these moves reflect the market's reaction to the talks reports, not to the October 28–29 signed-deal announcement. As of October 30, 2026, no termination, regulatory block, lawsuit, or renegotiation of the agreement has been reported; the deal remains pending and subject to a lengthy regulatory and shareholder-approval process.

## Final status: **Cleared with qualifications**

Qualifications that must travel with this story:
1. Every numeric deal term (price, ratios, financing, termination fee, closing window) is sourced to the SEC filing via search-engine text extraction, not my own direct rendering of the raw EDGAR HTML (sec.gov was unreachable in this session). Numbers were cross-checked across multiple independent queries and were consistent, but direct EDGAR confirmation is recommended before legal/compliance-sensitive use.
2. The $100M savings figure and the 2027–2028 closing window must be clearly attributed as company estimates/targets, not settled facts.
3. Stock-move percentages must be tied to October 26 (talks reports), not the later signing/filing dates.
4. Any Instacart executive mention must use Chris Rogers, not Fidji Simo, and no quote should be invented.
5. Uber-withdrawal claim must stay attributed to anonymous-sourced reporting.
6. This remains a pending/unconsummated transaction with a multi-year regulatory runway — do not frame as a completed acquisition.
