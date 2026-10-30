# JUSTPRENEUR artwork maker

Turns one approved story into a branded feed post, a carousel and an animated text reel, in the JUSTPRENEUR look (navy, steel, warm white, energy gold; Anton + Archivo).

```bash
python3 artwork/render_artwork.py --spec media/<story_id>/spec.json --out media/<story_id>
```

The spec format is documented at the top of `render_artwork.py`. Text inside `[brackets]` is set in gold. Use only facts from the story the owner approved.

Finished files live in `media/<story_id>/` and are served to Metricool through jsDelivr, pinned to the commit:
`https://cdn.jsdelivr.net/gh/LESFLOAI/justpreneur-content-system@<commit>/media/<story_id>/post.png`

Nothing here publishes anything. The owner picks a format and approves it on the Editorial Desk or the n8n review page; the LESFLO Metricool Scheduler then schedules it.
