#!/usr/bin/env python3
"""
Generate a single static HTML dashboard at outputs/dashboard.html
Run from project root: python scripts/generate_dashboard.py
"""

import os, json, glob, html, pathlib
from datetime import datetime

OUT_DIR = "outputs"
DASH_PATH = os.path.join(OUT_DIR, "dashboard.html")

def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def read_text(path, n=800):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()[:n]
    except Exception:
        return None

def make_card(title, subtitle="", body_html="", link=None, thumb=None, meta=""):
    link_attr = f'<a class="card-link" href="{link}" target="_blank">Open</a>' if link else ""
    thumb_html = f'<img class="thumb" src="{thumb}" alt="image">' if thumb else ""
    return f'''
    <div class="card">
      <div class="card-left">{thumb_html}</div>
      <div class="card-body">
        <h3>{html.escape(title)}</h3>
        <div class="subtitle">{html.escape(subtitle)}</div>
        <div class="content">{body_html}</div>
        <div class="meta">{meta} {link_attr}</div>
      </div>
    </div>
    '''

def gather_webcopy():
    items = []
    for p in glob.glob("outputs/web_copy/*.json"):
        j = read_json(p) or {}
        title = j.get("title", pathlib.Path(p).stem)
        desc = j.get("description", "")
        body = j.get("body", "")
        thumb = None
        # try images folder by slug
        slug = j.get("slug", pathlib.Path(p).stem)
        img_candidate = f"outputs/images/{slug}.png"
        if os.path.exists(img_candidate):
            thumb = img_candidate
        items.append((title, desc, body, p, thumb))
    return items

def gather_blogs():
    items = []
    for p in glob.glob("outputs/blogs/*.md"):
        text = read_text(p, n=2000) or ""
        # extract first header
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        title = lines[0] if lines and lines[0].startswith("#") else pathlib.Path(p).stem
        excerpt = ""
        if len(lines) > 1:
            excerpt = lines[1][:300]
        # image guess from slug
        slug = pathlib.Path(p).stem
        img_candidate = f"outputs/images/{slug}.png"
        thumb = img_candidate if os.path.exists(img_candidate) else None
        items.append((title, excerpt, text, p, thumb))
    return items

def gather_social():
    items = []
    p = "outputs/social/social_posts.json"
    j = read_json(p)
    if j:
        for post in j:
            platform = post.get("platform", "n/a")
            caption = post.get("caption", str(post))
            hashtags = post.get("hashtags", [])
            items.append((platform, caption, hashtags, p, None))
    return items

def gather_ads():
    items = []
    p = "outputs/ads/ad_snippets.json"
    j = read_json(p)
    if j:
        for ad in j:
            channel = ad.get("channel", "n/a")
            text = ad.get("description") or ad.get("text") or ad.get("headline") or str(ad)
            items.append((channel, text, "", p, None))
    return items

def gather_raw():
    items = []
    for p in glob.glob("outputs/raw/*"):
        if os.path.isfile(p):
            snippet = read_text(p, n=800) or ""
            items.append((pathlib.Path(p).name, snippet, p))
    return items

def gather_images():
    items = []
    for p in glob.glob("outputs/images/*"):
        if p.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            items.append(p)
    return items

def gather_seo():
    items = []
    for p in glob.glob("outputs/blogs/jsonld/*.json") + glob.glob("outputs/web_copy/jsonld/*.json"):
        j = read_json(p) or {}
        items.append((pathlib.Path(p).name, json.dumps(j, indent=2)[:1000], p))
    sitemap = None
    s_path = "outputs/sitemap.xml"
    if os.path.exists(s_path):
        sitemap = s_path
    return items, sitemap

# --- build HTML ---
html_parts = []
html_parts.append(f"<h1>Calyco Demo — Dashboard</h1>")
html_parts.append(f"<p>Generated: {datetime.utcnow().isoformat()} (UTC)</p>")

# Web copy
html_parts.append("<h2>Web Copy</h2>")
for title, desc, body, path, thumb in gather_webcopy():
    body_html = f"<p>{html.escape(desc)}</p>"
    html_parts.append(make_card(title, subtitle=desc, body_html=body_html, link=path, thumb=thumb))

# Blogs
html_parts.append("<h2>Blogs</h2>")
for title, excerpt, full, path, thumb in gather_blogs():
    body_html = f"<p>{html.escape(excerpt)}</p>"
    html_parts.append(make_card(title, subtitle=excerpt, body_html=body_html, link=path, thumb=thumb))

# Social
html_parts.append("<h2>Social Posts</h2>")
for platform, caption, hashtags, path, _ in gather_social():
    body_html = f"<p>{html.escape(caption)}</p><div class='tags'>{', '.join(html.escape(h) for h in hashtags)}</div>"
    html_parts.append(make_card(platform, subtitle="", body_html=body_html, link=path))

# Ads
html_parts.append("<h2>Ads</h2>")
for channel, text, _, path, _ in gather_ads():
    html_parts.append(make_card(channel, subtitle="", body_html=f"<p>{html.escape(text)}</p>", link=path))

# Raw
html_parts.append("<h2>Raw Scraper Outputs</h2>")
for name, snippet, path in gather_raw():
    html_parts.append(make_card(name, subtitle="", body_html=f"<pre>{html.escape(snippet)}</pre>", link=path))

# Images
html_parts.append("<h2>Images</h2>")
imgs = gather_images()
if imgs:
    imgs_html = "".join(f'<a href="{p}" target="_blank"><img class="thumb" src="{p}" /></a>' for p in imgs)
    html_parts.append(f"<div class='images'>{imgs_html}</div>")
else:
    html_parts.append("<p>No images found in outputs/images/</p>")

# SEO
html_parts.append("<h2>SEO Artifacts</h2>")
seo_items, sitemap = gather_seo()
for name, snip, path in seo_items:
    html_parts.append(make_card(name, subtitle="", body_html=f"<pre>{html.escape(snip)}</pre>", link=path))
if sitemap:
    html_parts.append(f'<p>Sitemap: <a href="{sitemap}" target="_blank">{sitemap}</a></p>')

# Footer
html_parts.append("<hr><p>Dashboard generated by scripts/generate_dashboard.py</p>")

# Wrap with style
HTML = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>Calyco Demo — Dashboard</title>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <style>
    body{{font-family:Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:20px;background:#f7f8fb;color:#111}}
    h1{{margin-bottom:0}}
    .card{{display:flex;gap:12px;background:#fff;padding:12px;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.06);margin:10px 0}}
    .card-left{{width:120px;flex:0 0 120px}}
    .thumb{{max-width:120px;border-radius:6px;display:block}}
    .card-body h3{{margin:0 0 6px 0}}
    .subtitle{{
      color:#555;font-size:0.95rem;margin-bottom:6px
    }}
    .content{{color:#222}}
    pre{{white-space:pre-wrap;background:#fafafa;padding:8px;border-radius:6px;overflow:auto;max-height:220px}}
    .meta{{margin-top:8px;font-size:0.9rem;color:#666}}
    .card-link{{float:right;background:#0b74de;color:#fff;padding:6px 8px;border-radius:6px;text-decoration:none}}
    .images img.thumb{{max-width:160px;margin-right:8px;margin-bottom:8px}}
    @media (max-width:700px){{
      .card{{flex-direction:column}}
      .card-left{{width:100%}}
    }}
  </style>
</head>
<body>
{''.join(html_parts)}
</body>
</html>
"""

# write file
with open(DASH_PATH, "w", encoding="utf-8") as f:
    f.write(HTML)

print("✅ Dashboard generated:", DASH_PATH)
print("Open it in your browser (file:// path).")
