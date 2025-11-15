from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, time

def scrape_instagram_profile(profile):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(f"https://www.instagram.com/{profile}/")
    time.sleep(5)

    posts = driver.page_source[:2000]  # simple demo extraction

    with open("outputs/raw/social.json", "w") as f:
        json.dump({"profile": profile, "html_sample": posts}, f, indent=4)

    driver.quit()
    print("Instagram scraping done.")

if __name__ == "__main__":
    scrape_instagram_profile("asianpaints")
