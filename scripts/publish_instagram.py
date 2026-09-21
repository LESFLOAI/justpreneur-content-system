#!/usr/bin/env python3
"""Publish a finished JustPreneur package to Instagram via the Graph API.

SCAFFOLD — do not run until:
  1. Your JustPreneur Instagram account is a Business or Creator account linked
     to a Facebook Page.
  2. You've created a Meta developer app and generated a long-lived Page access
     token with instagram_content_publish permission.
  3. IG_ACCESS_TOKEN and IG_BUSINESS_ACCOUNT_ID are set as env vars.
  4. Image files are hosted somewhere Instagram's servers can fetch them by URL
     (the Graph API needs a public image_url, not a local file — e.g. upload to
     S3/Cloudinary/your own site first, or use a service with a public URL).

This script only runs when explicitly invoked after the human "post it"
confirmation in the orchestrator workflow. It never runs on its own.
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import urllib.parse

GRAPH_VERSION = "v21.0"


def graph_post(path, params, access_token):
    url = f"https://graph.facebook.com/{GRAPH_VERSION}/{path}"
    data = urllib.parse.urlencode({**params, "access_token": access_token}).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"ERROR calling {path}: {e.code} {body}", file=sys.stderr)
        sys.exit(1)


def publish_single_image(ig_user_id, image_url, caption, access_token):
    container = graph_post(f"{ig_user_id}/media", {
        "image_url": image_url,
        "caption": caption,
    }, access_token)
    creation_id = container["id"]
    result = graph_post(f"{ig_user_id}/media_publish", {
        "creation_id": creation_id,
    }, access_token)
    return result


def publish_carousel(ig_user_id, image_urls, caption, access_token):
    children = []
    for url in image_urls:
        child = graph_post(f"{ig_user_id}/media", {
            "image_url": url,
            "is_carousel_item": "true",
        }, access_token)
        children.append(child["id"])
    container = graph_post(f"{ig_user_id}/media", {
        "media_type": "CAROUSEL",
        "children": ",".join(children),
        "caption": caption,
    }, access_token)
    creation_id = container["id"]
    result = graph_post(f"{ig_user_id}/media_publish", {
        "creation_id": creation_id,
    }, access_token)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True,
                     help="Path to package.json: {\"caption\": str, \"image_urls\": [str, ...]}")
    args = ap.parse_args()

    access_token = os.environ.get("IG_ACCESS_TOKEN")
    ig_user_id = os.environ.get("IG_BUSINESS_ACCOUNT_ID")
    if not access_token or not ig_user_id:
        print("ERROR: set IG_ACCESS_TOKEN and IG_BUSINESS_ACCOUNT_ID first. "
              "See the setup checklist at the top of this file.", file=sys.stderr)
        sys.exit(1)

    with open(args.package) as f:
        package = json.load(f)

    caption = package["caption"]
    image_urls = package["image_urls"]

    if len(image_urls) == 1:
        result = publish_single_image(ig_user_id, image_urls[0], caption, access_token)
    else:
        result = publish_carousel(ig_user_id, image_urls, caption, access_token)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
