#!/usr/bin/env python3
"""
Extract figures/images from CLRS textbook PDFs using Upstage Document Parse API.

Usage:
    python scripts/extract_images.py <pdf_path> <output_dir> [--pages START-END]

Examples:
    python scripts/extract_images.py materials/books/Ch04_Divide_and_Conquer.pdf lectures/week04/1_theory/images/
    python scripts/extract_images.py materials/books/Ch15_Dynamic_Programming.pdf lectures/week06/1_theory/images/ --pages 1-10
"""

import argparse
import base64
import json
import os
import sys
from pathlib import Path

import requests

API_URL = "https://api.upstage.ai/v1/document-digitization"


def get_api_key():
    """Load API key from .env file."""
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("UPSTAGE_API_KEY="):
                return line.split("=", 1)[1].strip()
    key = os.environ.get("UPSTAGE_API_KEY")
    if not key:
        print("Error: UPSTAGE_API_KEY not found in .env or environment", file=sys.stderr)
        sys.exit(1)
    return key


def parse_pdf(pdf_path: str, api_key: str) -> dict:
    """Send PDF to Upstage Document Parse and return the response."""
    headers = {"Authorization": f"Bearer {api_key}"}
    with open(pdf_path, "rb") as f:
        files = {"document": (os.path.basename(pdf_path), f, "application/pdf")}
        data = {
            "output_formats": '["html", "text"]',
            "base64_encoding": '["figure", "chart"]',
            "ocr": "auto",
            "coordinates": "true",
            "model": "document-parse",
        }
        print(f"Uploading {pdf_path} to Upstage Document Parse...")
        resp = requests.post(API_URL, headers=headers, files=files, data=data, timeout=300)

    if resp.status_code != 200:
        print(f"API error {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    return resp.json()


def extract_figures(response: dict, output_dir: str, prefix: str = "fig") -> list:
    """Extract base64-encoded figures from the API response and save as images."""
    os.makedirs(output_dir, exist_ok=True)
    saved = []

    elements = response.get("elements", [])
    fig_num = 0

    for elem in elements:
        category = elem.get("category", "")
        if category not in ("figure", "chart", "diagram", "image"):
            continue

        b64_data = elem.get("base64_encoding")
        if not b64_data:
            # Try content.html for embedded base64 images
            html = elem.get("content", {}).get("html", "")
            if "base64," in html:
                b64_data = html.split("base64,", 1)[1].split('"')[0]

        if not b64_data:
            continue

        fig_num += 1
        page = elem.get("page", 0)
        filename = f"{prefix}_p{page:03d}_{fig_num:03d}.png"
        filepath = os.path.join(output_dir, filename)

        img_data = base64.b64decode(b64_data)
        with open(filepath, "wb") as f:
            f.write(img_data)

        saved.append(filepath)
        print(f"  Saved: {filename} (page {page}, {len(img_data)} bytes)")

    return saved


def main():
    parser = argparse.ArgumentParser(description="Extract images from CLRS PDFs via Upstage Document Parse")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("output_dir", help="Directory to save extracted images")
    parser.add_argument("--prefix", default="fig", help="Filename prefix (default: fig)")
    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print(f"Error: {args.pdf_path} not found", file=sys.stderr)
        sys.exit(1)

    api_key = get_api_key()
    response = parse_pdf(args.pdf_path, api_key)

    # Save raw response for debugging
    debug_path = os.path.join(args.output_dir, "_response.json")
    os.makedirs(args.output_dir, exist_ok=True)
    with open(debug_path, "w") as f:
        json.dump(response, f, indent=2)
    print(f"Raw response saved to {debug_path}")

    saved = extract_figures(response, args.output_dir, prefix=args.prefix)
    print(f"\nExtracted {len(saved)} figures to {args.output_dir}")

    if not saved:
        print("No figures found. Check _response.json for the raw API output.")
        print("Categories found:", set(e.get("category", "unknown") for e in response.get("elements", [])))


if __name__ == "__main__":
    main()
