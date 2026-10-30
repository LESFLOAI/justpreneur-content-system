#!/usr/bin/env python3
"""Render JUSTPRENEUR artwork for one approved story.

Usage:
  python3 artwork/render_artwork.py --spec spec.json --out media/<story_id>

spec.json:
{
  "story_id": "JP-71aff300",
  "post":   {"headline": "A fan base is a [business asset.]",
             "fact": "MLB team sponsorship revenue reportedly hit a record [$2.12 billion] for the 2026 season.",
             "kicker": "Brands pay for who you reach and why they care."},
  "slides": [{"headline": "...", "body": "..."}, ...],      # 3-5 slides, last one is the takeaway
  "reel":   [{"big": "..."}, {"num": "$2.12B", "sub": "..."}, ...]   # 3-5 scenes
}
Text inside [square brackets] is set in gold. Use only facts from the approved story.

Writes post.png, slide-1.png ... slide-N.png and reel.mp4 into --out.
Needs: python playwright (chromium) and ffmpeg.
"""
import argparse, json, os, pathlib, shutil, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fps", type=int, default=24)
    a = ap.parse_args()

    spec = json.loads(pathlib.Path(a.spec).read_text())
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("playwright is not installed: pip install playwright && python -m playwright install chromium")
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg is not installed")

    url = (HERE / "template.html").as_uri()
    with sync_playwright() as p:
        b = p.chromium.launch()

        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        pg.goto(url)
        pg.evaluate("document.fonts.ready")
        if spec.get("post"):
            pg.evaluate("p => renderPost(p)", spec["post"])
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            pg.screenshot(path=str(out / "post.png"))
            print("wrote", out / "post.png")
        slides = spec.get("slides") or []
        for i, s in enumerate(slides):
            pg.evaluate("([s,i,n]) => renderSlide(s,i,n)", [s, i, len(slides)])
            pg.wait_for_timeout(100)
            path = out / f"slide-{i + 1}.png"
            pg.screenshot(path=str(path))
            print("wrote", path)

        scenes = spec.get("reel") or []
        if scenes:
            pg = b.new_page(viewport={"width": 1080, "height": 1920})
            pg.goto(url)
            pg.evaluate("document.fonts.ready")
            total = pg.evaluate("s => setupReel(s)", scenes)
            pg.evaluate("document.fonts.ready")
            with tempfile.TemporaryDirectory() as tmp:
                n = int(total * a.fps)
                for i in range(n):
                    pg.evaluate("t => drawReel(t)", i / a.fps)
                    pg.screenshot(path=f"{tmp}/f{i:05d}.png")
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", f"{tmp}/f%05d.png",
                                "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest",
                                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                                "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", str(out / "reel.mp4")], check=True)
            print("wrote", out / "reel.mp4")
        b.close()


if __name__ == "__main__":
    main()
