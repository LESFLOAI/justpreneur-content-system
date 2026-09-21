#!/usr/bin/env python3
"""Generate JustPreneur post images from Visual Director prompts.

Reads a jobs JSON file: [{"id": str, "prompt": str, "width": int, "height": int}, ...]
Writes one PNG per job into --out, named <id>.png.

Provider is chosen by the IMAGE_PROVIDER env var: "openai" (default) or "gemini".
Requires OPENAI_API_KEY or GOOGLE_API_KEY to be set accordingly.
"""
import argparse
import base64
import json
import os
import sys
import urllib.request
import urllib.error

OPENAI_SIZES = {
    (1080, 1350): "1024x1536",  # closest supported portrait
    (1080, 1080): "1024x1024",
}


def generate_openai(prompt, width, height, api_key):
    size = OPENAI_SIZES.get((width, height), "1024x1024")
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=json.dumps({
            "model": "gpt-image-1",
            "prompt": prompt,
            "size": size,
            "n": 1,
        }).encode(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    b64 = data["data"][0]["b64_json"]
    return base64.b64decode(b64)


def generate_gemini(prompt, width, height, api_key):
    model = "imagen-4.0-generate-001"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:predict?key={api_key}"
    aspect = "3:4" if height > width else ("1:1" if height == width else "4:3")
    req = urllib.request.Request(
        url,
        data=json.dumps({
            "instances": [{"prompt": prompt}],
            "parameters": {"sampleCount": 1, "aspectRatio": aspect},
        }).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    b64 = data["predictions"][0]["bytesBase64Encoded"]
    return base64.b64decode(b64)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", required=True, help="Path to jobs JSON file")
    ap.add_argument("--out", required=True, help="Output directory for PNGs")
    args = ap.parse_args()

    provider = os.environ.get("IMAGE_PROVIDER", "openai").lower()
    with open(args.jobs) as f:
        jobs = json.load(f)

    os.makedirs(args.out, exist_ok=True)

    for job in jobs:
        width = job.get("width", 1080)
        height = job.get("height", 1350)
        out_path = os.path.join(args.out, f"{job['id']}.png")
        try:
            if provider == "gemini":
                api_key = os.environ["GOOGLE_API_KEY"]
                img_bytes = generate_gemini(job["prompt"], width, height, api_key)
            else:
                api_key = os.environ["OPENAI_API_KEY"]
                img_bytes = generate_openai(job["prompt"], width, height, api_key)
        except KeyError as e:
            print(f"ERROR: missing required env var {e} for provider '{provider}'", file=sys.stderr)
            sys.exit(1)
        except urllib.error.HTTPError as e:
            print(f"ERROR: {job['id']} failed — {e.code} {e.read().decode()[:500]}", file=sys.stderr)
            sys.exit(1)

        with open(out_path, "wb") as f:
            f.write(img_bytes)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
