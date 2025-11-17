"""
Free Image Generator using HuggingFace Stable Diffusion
No paid APIs required.
"""

import os
import requests

# Ensure output directory exists
os.makedirs("outputs/images", exist_ok=True)

# Free-tier HF SD model
# HF_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

# Optional auth token (free) — improves rate limit slightly
HF_TOKEN = os.getenv("HF_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}

def generate_image(prompt, slug):

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
            "negative_prompt": "blurry, distorted, low quality",
            "guidance_scale": 7.0
        }
    }

    try:
        response = requests.post(
            HF_API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        if response.status_code == 200:
            import base64
            result = response.json()

            if "generated_image" in result:
                img_b64 = result["generated_image"]
                img_bytes = base64.b64decode(img_b64)

                path = f"outputs/images/{slug}.png"
                os.makedirs("outputs/images", exist_ok=True)

                with open(path, "wb") as f:
                    f.write(img_bytes)

                print("🖼️ HuggingFace image saved:", path)
                return path
            else:
                print("⚠️ HF response missing image:", result)

        else:
            print("⚠️ HF Image Generation Failed:", response.text)

    except Exception as e:
        print("⚠️ HF Image Generation Error:", str(e))

    # fallback to stock
    return fallback_stock_image(slug)



def use_stock_image(slug):
    """
    Uses free-license fallback stock image if SD fails.
    """

    src = "assets/placeholder.jpg"
    dst = f"outputs/images/{slug}.jpg"

    if os.path.exists(src):
        with open(src, "rb") as f_src:
            with open(dst, "wb") as f_dst:
                f_dst.write(f_src.read())

        print("📸 Using stock placeholder:", dst)
        return dst

    print("⚠️ No stock fallback image found.")
    return None


if __name__ == "__main__":
    generate_image(
        "Colorful modern Indian interior wall paint, realistic, soft lighting",
        "test-image"
    )
