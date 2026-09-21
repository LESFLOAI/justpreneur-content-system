# JustPreneur Multi-Agent Content System

Built from `JustPreneur Multi-Agent Content System.pdf`, then reworked twice per your direction: first to autopilot (one checkpoint instead of five), then split into a cloud half and a local half so it can actually run unattended twice a day.

## Why it's split into two commands

A cloud scheduled routine runs in total isolation — no access to your Mac, no local files, no local environment variables. That means it can't hold your image-generation or Instagram API keys. Rather than either giving up on unattended scheduling or putting your keys in a cloud config (you chose to keep those local), the pipeline splits at the point where secrets become necessary:

```
CLOUD — /justpreneur-draft (runs itself, 10am & 9pm daily, no secrets)
  scheduler → story-scout → fact-verifier → strategist → copywriter → visual-director (prompts only)
  → quality-control (draft mode) → emails + texts you the draft, logs it

                              ↓  (whenever you're ready)

LOCAL — /justpreneur-finish (you run it, or ask me to)
  visual-director generates real images → quality-control (full check) → shows you the finished package
  → you say "post it" → publish_instagram.py
```

The one thing that never moves, in either half: **nothing publishes without your explicit "post it" on that specific package.** That's fixed on my end, not a setting — even "full autopilot" doesn't remove it. In practice it's still just one message from you, twice a day at most.

## What's here

```
.claude/agents/                 7 specialist subagents
  story-scout.md, fact-verifier.md, justpreneur-strategist.md,
  content-copywriter.md, visual-director.md, quality-control.md, scheduler.md
.claude/commands/
  justpreneur-draft.md          cloud entry point — draft only, no secrets, emails/texts you
  justpreneur-finish.md         local entry point — images + publish, after your approval
  justpreneur-post.md           all-in-one local version, for when you want to run it yourself right now
templates/
  intake-brief.md, approved-facts-block.md, content-log.md, content-calendar.md
scripts/
  generate_images.py            OpenAI or Gemini → real PNGs
  publish_instagram.py          Instagram Graph API publish
  README.md
projects/                       one folder per post: package.md, image-jobs.json, images/
```

## Status — what's done vs. what needs one more thing from you

**Done:**
- Folder moved to `~/Documents/JustPreneur` (out of the temporary session folder, so it persists and a cloud routine can actually reach it once pushed to GitHub).
- Draft/finish split built, cadence set to 10:00 AM + 9:00 PM every day.
- Gmail and Inkbox (SMS/iMessage) connector cards are up in chat — click Connect on both so the cloud routine can actually send you things.

**Needs you, in order:**
1. **GitHub repo** — the cloud routine checks out its code from a git repo; it can't see this Mac. I don't have `gh` or any git credentials configured here, so I can't create/push it myself. Tell me if you already have a GitHub account, and I'll walk you through creating a free repo and pushing this project to it.
2. **Connect Gmail and Inkbox** — click Connect on the two cards above. Inkbox also needs your phone number for SMS — send it to me and I'll drop it into `justpreneur-draft.md` (I won't paste it back to you in chat once it's in the file, just confirm it's set).
3. **Create the routine** — once 1 and 2 are done, I'll create the actual cloud schedule (cron `0 10,21 * * *` in your local time, converted to UTC) pointing at your new repo, running `/justpreneur-draft`.

## Delivery format

Each draft email/text is written to be copy-paste-ready: caption in its own block, hashtags on their own line, tagged accounts listed with the reason for each, image prompts labeled separately. The text message is a one-line heads-up ("draft ready, check email") rather than the full package — SMS/iMessage isn't the place for five hashtags and an image prompt.

## Image generation

`generate_images.py` supports OpenAI (`gpt-image-1`, default) or Gemini (`imagen-4.0-generate-001`) via `IMAGE_PROVIDER`. I'd default to OpenAI for better in-image text and cross-slide consistency. Runs locally in `/justpreneur-finish`, using whichever `OPENAI_API_KEY` / `GOOGLE_API_KEY` you have set in your local shell — nothing about this needs to touch the cloud routine.

## Instagram publishing

`publish_instagram.py` uses the Graph API (the only method Meta actually supports for programmatic posting). Needs, one-time: your JustPreneur account as Business/Creator linked to a Facebook Page, a Meta developer app with a long-lived access token, and somewhere public to host the generated images by URL (Graph API needs a fetchable `image_url`, not a local file — tell me what host you want and I'll wire the upload step in).

## Next message from you, ideally:

- Do you already have a GitHub account? (yes/no is enough to start the walkthrough)
- Your phone number, for Inkbox
- Confirm once you've clicked Connect on the Gmail and Inkbox cards
