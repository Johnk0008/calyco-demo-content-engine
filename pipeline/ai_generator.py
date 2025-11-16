import os
import json
from slugify import slugify
import google.generativeai as genai

# -----------------------------------------
# Load environment
# -----------------------------------------
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

TEXT_MODEL = genai.GenerativeModel("models/gemini-1.5-flash-latest")
IMAGE_MODEL = genai.GenerativeModel("models/gemini-1.0-pro-vision-latest")

# -----------------------------------------
# Helpers
# -----------------------------------------
def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def generate_text(prompt):
    try:
        response = TEXT_MODEL.generate_content(prompt)
        return response.text
    except Exception as e:
        print("⚠️ Gemini text generation failed:", e)
        return "Placeholder text (AI offline)."

def generate_image(prompt, slug):
    try:
        response = IMAGE_MODEL.generate_content(prompt)
        # Extract the first file
        img = response._result.candidates[0].content.parts[0].inline_data
        img_bytes = img.data

        path = f"outputs/images/{slug}.png"
        os.makedirs("outputs/images", exist_ok=True)
        with open(path, "wb") as f:
            f.write(img_bytes)

        print("🖼 Image saved:", path)
        return path

    except Exception as e:
        print("⚠️ Gemini image generation failed:", e)
        return None

# --------------------------------------------------------
# 1. Generate Web Copy
# --------------------------------------------------------
def generate_web_copy():
    title = "Interior Emulsion Paints – Calyco"
    slug = slugify(title)

    prompt = """
Write a polished, brand-safe product page for Calyco interior emulsion paints.
Tone: premium, clean, helpful.
Avoid AI mentions.
Include: features, benefits, use cases, durability, VOC levels.
"""

    print("🧩 Generating web copy via Gemini...")
    body = generate_text(prompt)

    data = {
        "title": title,
        "slug": slug,
        "description": "Premium interior emulsion paints with low VOC and smooth finish.",
        "body": body
    }

    out_path = f"outputs/web_copy/{slug}.json"
    write_file(out_path, json.dumps(data, indent=2))

    # image generation
    img_prompt = """
High-quality interior home design photo, beautiful pastel wall paint,
soft natural lighting, minimalistic modern Indian decor, DSLR realism, 8k.
"""
    generate_image(img_prompt, slug)

    print("✍️ Web copy saved:", out_path)
    return data

# --------------------------------------------------------
# 2. Blog Generation
# --------------------------------------------------------
def generate_blog(topic="Trending Home Paint Colors 2025"):
    slug = slugify(topic)

    prompt = f"""
Write a detailed blog article titled '{topic}' from the perspective of Calyco Paints.
Tone: expert but friendly.
Avoid AI mentions.
Include: trends, materials, textures, consumer behavior, color palettes.
Length: ~700 words.
"""

    print("🧠 Generating blog via Gemini...")
    content = generate_text(prompt)

    data = {
        "title": topic,
        "slug": slug,
        "body": content
    }

    out_path = f"outputs/blogs/{slug}.md"
    write_file(out_path, content)

    # Blog image
    img_prompt = """
Modern wall paint texture palette, trending 2025 colors, soft gradients,
minimal clean layout, aesthetic render.
"""
    generate_image(img_prompt, slug)

    print("📝 Blog saved:", out_path)
    return data

# --------------------------------------------------------
# 3. Social Media Content
# --------------------------------------------------------
def generate_social_posts():
    prompt = """
Generate 5 short Instagram captions for a paint brand.
Tone: exciting, modern, aesthetic.
Avoid AI mentions.
"""

    print("📣 Generating social posts via Gemini...")
    text = generate_text(prompt)

    posts = text.split("\n")
    posts = [p.strip("-• ") for p in posts if p.strip()]

    data = {"posts": posts}

    out_path = "outputs/social/social_posts.json"
    write_file(out_path, json.dumps(data, indent=2))

    print("📤 Social posts saved:", out_path)
    return data

# --------------------------------------------------------
# 4. Ads
# --------------------------------------------------------
def generate_ads():
    prompt = """
Write 5 Google/Meta ad headlines + descriptions for Calyco Paints.
Tone: clean, premium, high-conversion.
"""

    print("💡 Generating ads via Gemini...")
    text = generate_text(prompt)

    ads = text.split("\n")
    ads = [a.strip("-• ") for a in ads if a.strip()]

    data = {"ads": ads}

    out_path = "outputs/ads/ad_snippets.json"
    write_file(out_path, json.dumps(data, indent=2))

    print("📣 Ads saved:", out_path)
    return data
