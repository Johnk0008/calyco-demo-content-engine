import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name)

def generate_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text


# ------------ Example Templates --------------

def generate_web_copy():
    prompt = """
    Create JSON web copy for a Calyco paint product page.
    Include:
    - title
    - subtitle
    - features
    - usage
    - why_calcyo
    - SEO meta
    Format ONLY in JSON.
    """
    output = generate_with_gemini(prompt)

    os.makedirs("outputs/web_copy", exist_ok=True)
    with open("outputs/web_copy/web_copy.json", "w") as f:
        f.write(output)

    print("Web copy generated!")


def generate_blog():
    prompt = """
    Write a 1200-word SEO blog about 'Trending Home Paint Colors 2025'
    Tone: Calyco brand-safe, no mention of AI.
    Include:
    - H1
    - H2 sections
    - SEO meta title & meta description
    - JSON-LD schema in final output
    """
    output = generate_with_gemini(prompt)

    os.makedirs("outputs/blogs", exist_ok=True)
    with open("outputs/blogs/color_trends_2025.md", "w") as f:
        f.write(output)

    print("Blog generated!")


def generate_social_posts():
    prompt = """
    Generate 10 social media posts with:
    - Instagram captions
    - LinkedIn captions
    - Hashtags
    Output in CSV format.
    """
    output = generate_with_gemini(prompt)

    os.makedirs("outputs/social", exist_ok=True)
    with open("outputs/social/posts.csv", "w") as f:
        f.write(output)

    print("Social posts generated!")


def generate_ads():
    prompt = """
    Write:
    - 10 Google Ads headlines
    - 10 Google Ads descriptions
    - 10 Facebook Ads primary text
    - 10 WhatsApp short texts
    Format in CSV.
    """
    output = generate_with_gemini(prompt)

    os.makedirs("outputs/ads", exist_ok=True)
    with open("outputs/ads/ad_copies.csv", "w") as f:
        f.write(output)

    print("Ads generated!")


if __name__ == "__main__":
    generate_web_copy()
    generate_blog()
    generate_social_posts()
    generate_ads()
