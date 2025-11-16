# pipeline/image_generator.py
import os, json, hashlib
from dotenv import load_dotenv
load_dotenv()

# If using google generative image (Gemini)
try:
    import google.generativeai as genai
    GEMINI = True
except Exception:
    GEMINI = False

CACHE_DIR = "outputs/images"
os.makedirs(CACHE_DIR, exist_ok=True)

def prompt_hash(prompt):
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:12]

def save_image_bytes(image_bytes, out_path):
    with open(out_path, "wb") as f:
        f.write(image_bytes)

def generate_image(prompt, style="photorealistic", model=os.getenv("GEMINI_IMAGE_MODEL","gemini-image-1.0")):
    """
    Generates an image for a prompt and caches it.
    Returns path to saved image.
    """
    key = prompt_hash(prompt)
    out_file = os.path.join(CACHE_DIR, f"{key}.png")
    if os.path.exists(out_file):
        return out_file

    if GEMINI:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        img = genai.images.generate(
            model=model,
            prompt=prompt,
            size="1024x1024"
        )
        # gemini returns base64 or url depending on sdk — handle accordingly
        b64 = img[0].b64_json if hasattr(img[0], "b64_json") else img[0].b64
        import base64
        save_image_bytes(base64.b64decode(b64), out_file)
        return out_file

    # fallback: if no Gemini installed, write prompt to file for manual generation
    with open(out_file.replace(".png", ".prompt.txt"), "w") as f:
        f.write(prompt)
    return out_file
