# run_all.py
from pipeline import (
    scrape_google_trends,
    scrape_news,
    scrape_competitors,
    scrape_instagram_profile,
    generate_web_copy,
    generate_blog,
    generate_social_posts,
    generate_ads,
)
from pipeline.qc import run_quality_checks

def run_pipeline():
    print("\n🚀 Running improved fully automated Calyco demo pipeline...\n")

    print("1️⃣ Scraping Google Trends...")
    scrape_google_trends()

    print("2️⃣ Scraping Industry News...")
    scrape_news()

    print("3️⃣ Scraping Competitors...")
    scrape_competitors()

    print("4️⃣ Scraping Social Feeds...")
    scrape_instagram_profile("asianpaints")

    print("\n✍️ 5. Generating Web Copy...")
    web_copy = generate_web_copy()

    print("\n📝 6. Generating Blogs...")
    blog = generate_blog()

    print("\n📣 7. Generating Social Media Posts...")
    social = generate_social_posts()

    print("\n📢 8. Generating Ads...")
    ads = generate_ads()

    print("\n🔍 9. Running Quality Checks...")

    qc_web = run_quality_checks(web_copy["body"])
    qc_blog = run_quality_checks(blog["body"])

    print("\nQC Results:")
    print("Web Copy:", qc_web)
    print("Blog:", qc_blog)

    print("\n🎉 Pipeline Complete!")

if __name__ == "__main__":
    run_pipeline()
