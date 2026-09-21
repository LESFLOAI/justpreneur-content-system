Finish a JustPreneur draft — generate real images, re-run QC, and publish after approval.

Run locally, where the image-generation and Instagram API keys live. Argument: the project folder under `projects/` to finish (e.g. `projects/2026-09-24-some-story`). If not given, list the folders in `projects/` with status "draft ready — needs local finish" in `content-log.md` and ask which one.

$ARGUMENTS

## Steps

1. Read `package.md` from the project folder — this has the approved facts, copy, and the Visual Director's image-generation prompts from the draft run.
2. Dispatch to `visual-director` with those exact prompts and an explicit instruction to generate real images this time (keys are available locally) — it writes `image-jobs.json` and runs `scripts/generate_images.py`.
3. Dispatch the complete package (facts, copy, actual image files) to `quality-control` in **finish mode** (full checklist, including artwork checks).
4. If verdict is **Fail**: stop, report why, do not auto-correct and resubmit.
5. If **Pass** or **Pass with corrections** (with corrections applied): assemble the final package — final images, final caption, five hashtags, tagged accounts, QC's pre-publish checklist — and show it to me in full.
6. Update `content-log.md` status to "ready to post."

## The one checkpoint

7. Wait for me to say something equivalent to "post it" / "approved, publish" for THIS specific package. This is not optional and nothing overrides it — not autopilot, not a prior approval on a different post. If I ask for a change instead, apply it, show the updated package, and wait again.
8. Only after that explicit confirmation, run `scripts/publish_instagram.py` for this package and report the result (post URL or error). Update `content-log.md` status to "posted" with the date.
