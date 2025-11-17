import os
import json
import requests
import base64
import random
from datetime import datetime
from slugify import slugify

# ============================================================
# OUTPUT FOLDERS
# ============================================================

os.makedirs("outputs/web_copy", exist_ok=True)
os.makedirs("outputs/blogs", exist_ok=True)
os.makedirs("outputs/social", exist_ok=True)
os.makedirs("outputs/ads", exist_ok=True)
os.makedirs("outputs/images", exist_ok=True)

# ============================================================
# FREE STOCK IMAGES (Guaranteed Free Commercial License)
# ============================================================

STOCK_IMAGES = {
    "interior": [
        "https://images.pexels.com/photos/6588571/pexels-photo-6588571.jpeg",
        "https://images.pexels.com/photos/271743/pexels-photo-271743.jpeg",
        "https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg"
    ],
    "colors": [
        "https://images.pexels.com/photos/1697213/pexels-photo-1697213.jpeg",
        "https://images.pexels.com/photos/364320/pexels-photo-364320.jpeg"
    ]
}

PLACEHOLDER_IMAGE = "assets/placeholder.jpg"  # must exist

# ============================================================
# 1️⃣ HuggingFace SDXL — Free Tier
# ============================================================

def generate_with_huggingface(prompt, slug):
    HF_API_URL = (
        "https://router.huggingface.co/hf-inference/models/"
        "stabilityai/stable-diffusion-xl-base-1.0"
    )

    headers = {
        "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "negative_prompt": "low quality, blurry, distorted"
        }
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=60)

        if response.status_code == 200:
            r = response.json()
            if "generated_image" in r:
                img_bytes = base64.b64decode(r["generated_image"])
                path = f"outputs/images/{slug}.png"
                with open(path, "wb") as f:
                    f.write(img_bytes)
                print("🖼️ HuggingFace SDXL image saved:", path)
                return path
            
        print("⚠️ HF Error →", response.text)

    except Exception as e:
        print("⚠️ HuggingFace Failure:", e)

    return None


# ============================================================
# 2️⃣ Local Stable Diffusion (AUTOMATIC1111 API)
# ============================================================

def generate_with_local_sd(prompt, slug):
    try:
        url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

        payload = {
            "prompt": prompt,
            "steps": 20
        }

        response = requests.post(url, json=payload, timeout=60)

        if response.status_code == 200:
            img_b64 = response.json()["images"][0]
            img_bytes = base64.b64decode(img_b64)

            path = f"outputs/images/{slug}.png"
            with open(path, "wb") as f:
                f.write(img_bytes)

            print("🖼️ Local SD image saved:", path)
            return path

    except Exception as e:
        print("ℹ️ Local SD not running → skipping:", e)

    return None


# ============================================================
# 3️⃣ Free Stock Images (Pexels / Unsplash / Pixabay)
# ============================================================

def fallback_stock_image(slug, category="interior"):
    try:
        images = STOCK_IMAGES.get(category, [])
        if not images:
            return None

        url = random.choice(images)
        img_data = requests.get(url, timeout=30).content

        path = f"outputs/images/{slug}.jpg"
        with open(path, "wb") as f:
            f.write(img_data)

        print("🖼️ Stock fallback image saved:", path)
        return path

    except Exception as e:
        print("⚠️ Stock fallback failed:", e)

    return None


# ============================================================
# 4️⃣ Placeholder (always works)
# ============================================================

def placeholder_image(slug):
    try:
        path = f"outputs/images/{slug}.jpg"
        with open(PLACEHOLDER_IMAGE, "rb") as src:
            with open(path, "wb") as dst:
                dst.write(src.read())

        print("🖼️ Placeholder image used:", path)
        return path

    except Exception as e:
        print("🚨 Placeholder missing:", e)
        return None


# ============================================================
# MASTER IMAGE GENERATOR WITH 4-LAYER FALLBACK
# ============================================================

def generate_image(prompt, slug):
    print(f"\n🖼️ Generating Image for → {slug}")

    # 1) HuggingFace SDXL
    img = generate_with_huggingface(prompt, slug)
    if img:
        return img

    # 2) Local Stable Diffusion
    img = generate_with_local_sd(prompt, slug)
    if img:
        return img

    # 3) Stock Fallback
    img = fallback_stock_image(slug)
    if img:
        return img

    # 4) Guaranteed Fallback
    return placeholder_image(slug)


# ============================================================
# CONTENT GENERATORS (TEXT ONLY MODELS — OSS, Mistral)
# ============================================================

def text_model(prompt):
    """Simple local model stub — update if needed."""
    return (
        "Generated content (placeholder).\n"
        "Replace with Mistral/OSS text model if required."
    )


# ============================================================
# WEB COPY GENERATOR
# ============================================================

def generate_web_copy():
    title = "Interior Emulsion Paints – Calyco"
    slug = slugify(title)

    body = text_model(
        "Write a high-quality, SEO-friendly webpage copy for Calyco interior paints."
    )

    img = generate_image(
        f"Modern Indian home interior painted in calming tones — {title}",
        slug
    )

    output = {
        "title": title,
        "slug": slug,
        "body": body,
        "image": img,
        "timestamp": str(datetime.utcnow())
    }

    path = f"outputs/web_copy/{slug}.json"
    with open(path, "w") as f:
        json.dump(output, f, indent=2)

    print("✔ Web copy generated")
    return output


# ============================================================
# BLOG GENERATOR
# ============================================================

def generate_blog():
    topic = "Trending Home Paint Colors for 2025"
    slug = slugify(topic)

    body = text_model(f"Write a 700-word blog on: {topic}")

    img = generate_image(
        f"Stylish 2025 trending color palette interior concept art",
        slug
    )

    output = {
        "title": topic,
        "slug": slug,
        "body": body,
        "image": img,
        "timestamp": str(datetime.utcnow())
    }

    path = f"outputs/blogs/{slug}.md"
    with open(path, "w") as f:
        f.write(body)

    print("✔ Blog generated")
    return output


# ============================================================
# SOCIAL POSTS
# ============================================================

def generate_social_posts():
    posts = [
        "🎨 Discover 2025’s hottest paint trends with Calyco!",
        "✨ Transform your home with AI-personalised color palettes.",
        "🏡 Your dream interiors start with the right color choice."
    ]

    slug = "social-posts"
    img = generate_image("simple pastel color wall aesthetic", slug)

    output = {"posts": posts, "image": img}

    with open("outputs/social/social_posts.json", "w") as f:
        json.dump(output, f, indent=2)

    print("✔ Social posts generated")
    return output


# ============================================================
# ADS
# ============================================================

def generate_ads():
    ads = [
        "🏡 Upgrade your walls — choose Calyco Premium Paints!",
        "✨ Smooth finish. Rich colors. Zero hassle.",
        "🎨 Transform your home with Calyco’s 2025 palette."
    ]

    with open("outputs/ads/ad_snippets.json", "w") as f:
        json.dump({"ads": ads}, f, indent=2)

    print("✔ Ads generated")
    return ads
