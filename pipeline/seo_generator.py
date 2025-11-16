# pipeline/seo_generator.py
"""
SEO Generator Module for Calyco Demo Content Engine
- Generates JSON-LD schema
- Generates sitemap entries
- Provides a wrapper class SEOGenerator for use in the pipeline
"""

import os
import json
from datetime import datetime

# Ensure directories exist
os.makedirs("outputs/blogs/jsonld", exist_ok=True)
os.makedirs("outputs/web_copy/jsonld", exist_ok=True)

SITEMAP_PATH = "outputs/sitemap.xml"


# ============================================================
# JSON-LD GENERATORS
# ============================================================

def generate_jsonld_article(slug, title, desc):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "author": {"@type": "Organization", "name": "Calyco"},
        "publisher": {"@type": "Organization", "name": "Calyco"},
        "mainEntityOfPage": f"https://calycopaints.com/blog/{slug}",
        "datePublished": datetime.utcnow().strftime("%Y-%m-%d")
    }


def generate_jsonld_web_copy(slug, title, desc, product_type="Product"):
    return {
        "@context": "https://schema.org",
        "@type": product_type,
        "name": title,
        "description": desc,
        "brand": {"@type": "Brand", "name": "Calyco"},
        "mainEntityOfPage": f"https://calycopaints.com/{slug}",
        "datePublished": datetime.utcnow().strftime("%Y-%m-%d")
    }


# ============================================================
# WRITE JSON-LD TO FILE
# ============================================================

def write_jsonld_for_article(slug, title, desc):
    data = generate_jsonld_article(slug, title, desc)
    path = f"outputs/blogs/jsonld/{slug}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path


def write_jsonld_for_web_copy(slug, title, desc, product_type="Product"):
    data = generate_jsonld_web_copy(slug, title, desc, product_type)
    path = f"outputs/web_copy/jsonld/{slug}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path


# ============================================================
# SITEMAP HANDLING
# ============================================================

def init_sitemap():
    if not os.path.exists(SITEMAP_PATH):
        with open(SITEMAP_PATH, "w") as f:
            f.write(
                '<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            )


def append_sitemap_entry(slug, is_blog=True):
    init_sitemap()

    url = (
        f"https://calycopaints.com/blog/{slug}"
        if is_blog else f"https://calycopaints.com/{slug}"
    )

    entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{datetime.utcnow().strftime("%Y-%m-%d")}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

    with open(SITEMAP_PATH, "a") as f:
        f.write(entry)


def finalize_sitemap():
    with open(SITEMAP_PATH, "r") as f:
        content = f.read()

    if not content.strip().endswith("</urlset>"):
        with open(SITEMAP_PATH, "a") as f:
            f.write("</urlset>\n")


# ============================================================
# SEO WRAPPER CLASS  (Required by run_all.py)
# ============================================================

class SEOGenerator:
    """
    Wrapper class providing a clean interface:
    - generate_schema(web_copy or blog_output)
    - generate_sitemap()
    """

    def generate_schema(self, content):
        """
        Accepts generated content dictionary with keys:
        - slug
        - title
        - description
        - type: 'blog' or 'web'
        """
        slug = content.get("slug", "untitled")
        title = content.get("title", "")
        desc = content.get("description", "")
        is_blog = content.get("type") == "blog"

        if is_blog:
            print(f"📄 Creating JSON-LD schema for blog: {slug}")
            write_jsonld_for_article(slug, title, desc)
        else:
            print(f"📦 Creating JSON-LD schema for web page: {slug}")
            write_jsonld_for_web_copy(slug, title, desc)

        append_sitemap_entry(slug, is_blog=is_blog)

    def generate_sitemap(self):
        print("🗺️ Finalizing sitemap.xml ...")
        finalize_sitemap()
        print("Sitemap updated ✔")


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":
    seo = SEOGenerator()
    seo.generate_schema({
        "slug": "test-article",
        "title": "Example Title",
        "description": "Sample description",
        "type": "blog"
    })
    seo.generate_sitemap()
    print("SEO test completed.")
