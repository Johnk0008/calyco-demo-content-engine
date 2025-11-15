import json, os

def generate_meta(title, description):
    return {
        "meta_title": title,
        "meta_description": description
    }

def generate_jsonld(title, description, url):
    jsonld = {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": title,
      "description": description,
      "mainEntityOfPage": url,
      "publisher": {"@type": "Organization", "name": "Calyco Paints"}
    }
    return jsonld

def save_seo():
    meta = generate_meta(
        "Trending Texture Wall Designs 2025",
        "A complete guide to modern texture wall paint styles trending in 2025."
    )

    jsonld = generate_jsonld(
        meta["meta_title"],
        meta["meta_description"],
        "https://calycopaints.com/blog/texture-wall-designs-2025"
    )

    os.makedirs("outputs/seo", exist_ok=True)

    with open("outputs/seo/meta.json", "w") as f:
        json.dump(meta, f, indent=4)

    with open("outputs/seo/jsonld.json", "w") as f:
        json.dump(jsonld, f, indent=4)

    print("SEO data saved in outputs/seo/")

if __name__ == "__main__":
    save_seo()
