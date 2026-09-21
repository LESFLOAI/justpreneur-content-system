# Scripts

## generate_images.py — actual image generation

```bash
python3 scripts/generate_images.py --jobs projects/<title>/image-jobs.json --out projects/<title>/images
```

Set `IMAGE_PROVIDER` to `openai` (default) or `gemini`, and the matching key:

| Provider | Env var | Model used |
|---|---|---|
| OpenAI | `OPENAI_API_KEY` | `gpt-image-1` |
| Gemini | `GOOGLE_API_KEY` | `imagen-4.0-generate-001` |

Both are called directly over HTTPS, no SDK required. Model names and endpoints are current as of this writing — if either provider has moved on by the time you run this, update the model string in the script; the request/response shape may also need a small adjustment.

**Which one to use:** I'd default to OpenAI (`gpt-image-1`) for this — it tends to be more reliable at partial in-image text and brand-consistent compositions, which matters for a headline-driven format like this. Gemini/Imagen is a fine alternative, particularly if you already have Google Cloud billing set up. You only need one key to start; the script supports both so you can switch later without a rebuild.

## publish_instagram.py — Instagram Graph API publish

Do not run this until the setup checklist at the top of the file is done — it needs a Meta developer app and a Business/Creator IG account, which only you can create (it's tied to your account). Once set up:

```bash
export IG_ACCESS_TOKEN=...
export IG_BUSINESS_ACCOUNT_ID=...
python3 scripts/publish_instagram.py --package projects/<title>/package.json
```

Important: the Graph API needs a **public URL** for each image, not a local file path. The generated PNGs from `generate_images.py` land locally — you'll need to host them somewhere reachable (S3, Cloudinary, even a simple bucket on your own domain) before this script can use them. I can wire that upload step in once you tell me which host you want to use.
