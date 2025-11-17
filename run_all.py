from pipeline.scrapers.news_scraper import scrape_news
from pipeline.ai_generator import (
    generate_web_copy,
    generate_blog,
    generate_social_posts,
    generate_ads
)
from pipeline.qc import run_quality_checks
from pipeline.dashboard import build_dashboard

print("🚀 Running Calyco Free-Tier Demo Pipeline...\n")

# 1. Scrape basic industry news (local demo)
scrape_news()

# 2. Web copy
print("✍️ Generating web copy...")
web_copy = generate_web_copy()

# 3. Blog
print("\n📝 Generating blog...")
blog = generate_blog()

# 4. Social posts
print("\n📣 Generating social content...")
social = generate_social_posts()

# 5. Ads
print("\n💡 Generating ad snippets...")
ads = generate_ads()

# 6. QC
print("\n🔎 Running Quality Checks...")
qc_web = run_quality_checks(web_copy["body"])
qc_blog = run_quality_checks(blog["body"])

# 7. Dashboard
print("\n📊 Building dashboard...")
build_dashboard()

print("\n🎉 Pipeline Complete — Free Image + Full Automation Ready!")
