import os
import json

OUTPUT_DIR = "outputs/dashboard"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def _load_json(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}


def _load_text(path):
    if not os.path.exists(path):
        return ""
    try:
        with open(path, "r") as f:
            return f.read()
    except:
        return ""


def build_dashboard():

    print("📊 Building dashboard → outputs/dashboard/dashboard.html")

    # Load all generated output files
    web_copy = _load_json("outputs/web_copy/interior-emulsion-paints-calyco.json")
    blog_md = _load_text("outputs/blogs/trending-home-paint-colors-2025.md")
    social_posts = _load_json("outputs/social/social_posts.json")
    ads = _load_json("outputs/ads/ad_snippets.json")
    news = _load_json("outputs/raw/news.json")

    # QC results might exist or not
    qc_web = _load_json("outputs/qc/web_copy_qc.json")
    qc_blog = _load_json("outputs/qc/blog_qc.json")

    # Images folder
    images_folder = "outputs/images"
    os.makedirs(images_folder, exist_ok=True)
    images = os.listdir(images_folder)

    # SEO JSON-LD
    jsonld_folder = "outputs/blogs/jsonld"
    jsonld_files = []
    if os.path.exists(jsonld_folder):
        jsonld_files = os.listdir(jsonld_folder)

    # Build HTML
    html = f"""
    <html>
    <head>
        <title>Calyco AI Pipeline Dashboard</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
            }}
            h2 {{
                background: #EEE;
                padding: 10px;
            }}
            pre {{
                background: #F7F7F7;
                padding: 12px;
                border-radius: 5px;
                white-space: pre-wrap;
            }}
            .image-box {{
                margin: 10px 0;
            }}
            img {{
                max-width: 400px;
                border-radius: 8px;
                margin-bottom: 15px;
            }}
        </style>
    </head>
    <body>

        <h1>📊 Calyco AI Content Engine — Demo Dashboard</h1>

        <h2>📰 Industry News (Scraped)</h2>
        <pre>{json.dumps(news, indent=2)}</pre>

        <h2>📝 Web Copy</h2>
        <pre>{json.dumps(web_copy, indent=2)}</pre>

        <h2>📄 Blog Article (Markdown)</h2>
        <pre>{blog_md}</pre>

        <h2>📣 Social Media Posts</h2>
        <pre>{json.dumps(social_posts, indent=2)}</pre>

        <h2>💡 Ad Snippets</h2>
        <pre>{json.dumps(ads, indent=2)}</pre>

        <h2>🔍 QC — Web Copy</h2>
        <pre>{json.dumps(qc_web, indent=2)}</pre>

        <h2>🔍 QC — Blog</h2>
        <pre>{json.dumps(qc_blog, indent=2)}</pre>

        <h2>🖼️ Generated Images</h2>
    """

    for img_file in images:
        html += f"""
        <div class="image-box">
            <img src="../images/{img_file}" alt="{img_file}">
        </div>
        """

    html += """
        <h2>📦 JSON-LD Files</h2>
        <ul>
    """

    for f in jsonld_files:
        html += f"<li>{f}</li>"

    html += """
        </ul>
    </body>
    </html>
    """

    # Write output HTML
    with open(os.path.join(OUTPUT_DIR, "dashboard.html"), "w") as f:
        f.write(html)

    print("✅ Dashboard ready → outputs/dashboard/dashboard.html")
