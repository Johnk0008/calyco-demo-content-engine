# pipeline/scrapers/social_scraper.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, time, os

os.makedirs("outputs/raw", exist_ok=True)

def scrape_instagram_profile(profile):
    """
    Scrapes minimal Instagram HTML preview for a given profile.
    (Demo-only extraction)
    """
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(f"https://www.instagram.com/{profile}/")
    time.sleep(5)

    posts_html = driver.page_source[:2000]

    output_path = f"outputs/raw/{profile}_social.json"
    with open(output_path, "w") as f:
        json.dump({"profile": profile, "html_sample": posts_html}, f, indent=4)

    driver.quit()
    print(f"📸 Scraped Instagram: {profile} → {output_path}")


def fetch_social_posts(profiles=None):
    """
    Pipeline wrapper — scrapes multiple social profiles.
    Default profiles are Calyco-relevant competitors.
    """
    if profiles is None:
        profiles = [
            "asianpaints",
            "bergerpaints",
            "indigopaints"
        ]

    for p in profiles:
        scrape_instagram_profile(p)
